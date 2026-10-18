"""Check that the registry, INDEX.md, the research log, the manifest and the data files agree.

    python tools/validate.py              # exit 1 on any ERROR
    python tools/validate.py --strict     # exit 1 on any ERROR or WARN
    python tools/validate.py --verbose    # also print how many items each check examined
    python tools/validate.py --upstream   # also check candidate commits in the sibling upstream clones

Run it before every commit; each check exists because that failure has
happened in a past round. Every finding is printed as
`ERROR [section] code: message` or `WARN  [section] code: message`.
tools/tests/test_validate.py plants a defect for every code and fails if a
code here has no test.

Nothing is allowed to pass silently:
- the file readers in common.py are strict (no BOM, UTF-8 only, rectangular
  CSVs) and report a bad file instead of reading around it;
- a check that raises is reported as `check-crashed` and fails the run, and the
  other checks still run; git that cannot be run is `git-unavailable`, and if git cannot list the repository's
  files no check runs (on an empty list each would report every file missing);
- an id missing from the registry while a sources_domain.csv is unreadable is not reported as unknown, since it may
  be in that file: it is counted as not checked, and the unreadable file fails the run;
- each check counts what it examined, and one that examined nothing reports
  `nothing-checked`, because a check with no input passes vacuously;
- a file .gitignore hides is reported (`ignored-file`): no check would see it;
- a data file that a write-up, registry row or candidate cites must exist, in the working tree or in the commit the
  reference names (`path-ref-missing`): a reference nobody follows goes stale unnoticed;
- a check that depends on an unreadable file skips only its cross-checks
  against that file, whose failure is already reported, rather than crash or
  report false errors;
- the summary line says whether the --upstream checks ran, and --verbose names
  the upstream commits compared with.
tools/tests/measure_coverage.py fails unless the tests reach every line and
branch here; tools/tests/debug_case.py shows one case's full report.
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
import traceback
from collections import Counter, defaultdict

from common import (ACCESS_CLASSES, CANDIDATE_COLS, CANDIDATE_KINDS, CANDIDATE_STATUSES, CANDIDATES, DOMAIN_COLS,
                    DOMAIN_RE, INDEX, LICENSE_CLASSES, LIVE_CANDIDATE_STATUSES, LOG, MANIFEST, MANIFEST_COLS,
                    NOT_REDISTRIBUTABLE, PENDING_ACCESS, README, REGISTRY, REGISTRY_COLS, ROOT, TIERS, UPSTREAM_MAP,
                    UPSTREAM_MAP_COLS, UPSTREAM_REPOS, DataError, access_class, domain_dirs, file_digest, read_csv,
                    ignored_files, plain_file_name, read_domain_csv, read_text, rel, repo_files)

INDEX_HEADER = ['id', 'tier', 'source (short)', 'access', 'backs / could replace']
REJECTED_HEADER = ['id', 'source', 'link', 'reason']
ACCESS_WORDS = re.compile(r'(full[_ ]text[_ ]hosted|open[_ ]not[_ ]pulled|verified[_ ]live|open[_ ]service|'
                          r'public[_ ]domain[_ ]excerpt|registered[_ ]not[_ ]pulled|skipped)\b', re.I)
GITHUB_HARD_LIMIT = 100 * 1024 * 1024
GITHUB_WARN_LIMIT = 50 * 1024 * 1024
# Root-level files and directories, each with a line in README "Layout" unless marked False.
ROOT_FILES = {'README.md': True, 'INDEX.md': True, 'RESEARCH_LOG.md': True, 'sources.csv': True,
              'full_texts_manifest.csv': True, 'revision_candidates.csv': True, 'upstream_commit_map.csv': True,
              'DOWNLOADS.md': True, 'AGENTS.md': True, 'CLAUDE.md': False, 'LICENSE': False, '.gitignore': False,
              '.gitattributes': False}
# .gitattributes keeps hosted files byte for byte. git check-attr reads the staged copy when the working one is
# deleted, so full-text-eol-converted cannot see a deletion that is about to be committed; root-file-missing does.
REQUIRED_ROOT_FILES = ['README.md', 'INDEX.md', 'RESEARCH_LOG.md', 'sources.csv', 'full_texts_manifest.csv',
                       'revision_candidates.csv', 'upstream_commit_map.csv', 'AGENTS.md', '.gitattributes']
ROOT_DIRS = {'tools'}
# tools/ holds the tools and tools/tests/ their tests, Python only; any other file there is read by no check.
TOOLS_FILE_RE = re.compile(r'tools/(?:tests/)?[a-z0-9_]+\.py')
DOMAIN_FILES = {'sources_domain.csv', 'FINDINGS.md', '.gitkeep'}
EXTRACTED_SUFFIXES = {'.csv', '.json'}
TEXT_SUFFIXES = {'.csv', '.md', '.py', '.json'}
TEXT_NAMES = {'.gitignore', '.gitattributes'}
# A year cell starts with a year, an approximate year or "n.d.", and may explain itself after that.
YEAR_RE = re.compile(r'(~?\d{4}|n\.d\.)')
# RESEARCH_LOG.md is this heading, then the entries; it moved out of INDEX.md's last section on 2026-10-18.
LOG_HEADING = '# Research log\n'
LOG_ENTRY_RE = re.compile(r'- \*\*(?:Round (\d+)|Maintenance)\*\* \((\d{4}-\d{2}-\d{2})(?:/\d{2})?\)')
# Entry labels in a form other than "- **Round N**": AGENTS.md bans "**RN**" and "### RN". An unbolded "Round N" or
# "RN:" at a line start is an entry missing its label, which would otherwise read as part of the entry above.
LOG_MISLABEL_RE = re.compile(r'\s*(#{1,6}\s|\*\*R(?:ound)?\s*\d|- \*\*R\d|(?:- )?(?:Round\s*\d|R\d+\b))')
SHA_RE = re.compile(r'[0-9a-f]{7,40}')
# A candidate's target_file starts with the upstream path; notes may follow it ("reference/x.csv (+ CITATIONS.md)").
TARGET_PATH_RE = re.compile(r'[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.[A-Za-z0-9]+(?=$|[\s(+;,])')


class Report:
    def __init__(self):
        self.lines = []
        self.errors = 0
        self.warnings = 0
        self.section = ''
        self.counts = defaultdict(Counter)

    def start(self, name):
        self.section = name

    def error(self, code, msg):
        self.errors += 1
        self.lines.append(f'ERROR [{self.section}] {code}: {msg}')

    def warn(self, code, msg):
        self.warnings += 1
        self.lines.append(f'WARN  [{self.section}] {code}: {msg}')

    def count(self, what, n=1):
        self.counts[self.section][what] += n

    def expect(self, what):
        """A check whose input is empty passes vacuously; report it instead."""
        if not self.counts[self.section][what]:
            self.error('nothing-checked', f'no {what} examined — the check passed only because it saw no input')


def parse_date(text):
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        return None


def registry_partial(rep, ctx):
    """True if a sources_domain.csv is unreadable (check_registry reports it). An id missing from the registry may then
    be in that file, so the caller does not report it as unknown; it is counted here as not checked instead."""
    if ctx['unread_domains']:
        rep.count('ids not checked: a sources_domain.csv is unreadable')
        return True
    return False


def table_cells(line):
    inner = line.strip()[1:-1]
    return [c.strip() for c in re.split(r'(?<!\\)\|', inner)]


# ---------------------------------------------------------------------------------------------- files and layout

def check_files(rep, ctx):
    """Every text file: UTF-8, no BOM, no stray carriage returns, ends with a newline."""
    rep.start('text files')
    for name in ctx['files']:
        parts = name.split('/')
        if 'full_texts' in parts or not (parts[-1] in TEXT_NAMES or any(name.endswith(s) for s in TEXT_SUFFIXES)):
            continue
        rep.count('text files')
        path = ROOT / name
        try:
            read_text(path)
        except DataError as e:
            rep.error(e.code, str(e))
            continue
        data = path.read_bytes()
        if not data:
            rep.error('text-empty', f'{name}: empty file')
            continue
        if b'\r\r' in data:
            rep.error('text-doubled-cr', f'{name}: doubled carriage returns — git treats the file as binary and shows '
                                         f'no diffs; write CSVs with csv.writer on a file opened with newline=""')
        elif re.search(rb'\r(?!\n)', data):
            rep.error('text-lone-cr', f'{name}: a carriage return not followed by a line feed')
        if not data.endswith(b'\n'):
            rep.error('text-no-final-newline', f'{name}: no newline at the end, so the next appended line joins the last one')
    rep.expect('text files')


def check_layout(rep, ctx):
    """Root and domain directories hold only what the layout allows."""
    rep.start('layout')
    files = ctx['files']
    # Any file, tracked, untracked or ignored: an empty folder holds no data, but a file here is unreachable.
    stray = sorted(p for p in (ROOT / 'extracted_data').rglob('*') if p.is_file())
    if stray:
        rep.error('root-extracted-data', f'extracted_data/ at the repo root holds {len(stray)} file(s) ({rel(stray[0])} ...): '
                                         f'FINDINGS paths are relative to a domain, so nothing reaches them; move each '
                                         f'into <domain>/extracted_data/')
    domains = set(ctx['domains'])
    for name in files:
        top = name.split('/')[0]
        if '/' not in name:
            if name not in ROOT_FILES:
                rep.error('root-unexpected-entry', f'{name}: unexpected file at the repo root')
        elif top not in domains and top not in ROOT_DIRS:
            rep.error('root-unexpected-entry', f'{top}/: unexpected directory at the repo root '
                                               f'(a domain directory is named NN_lowercase_words)')
        elif top == 'tools' and not TOOLS_FILE_RE.fullmatch(name):
            rep.error('tools-unexpected-entry', f'{name}: tools/ holds Python modules and tools/tests/ their tests; '
                                                f'no check reads any other file there')
    for f in REQUIRED_ROOT_FILES:
        if f not in files:
            rep.error('root-file-missing', f'{f} is missing')
    # Every check reads the git file list, so a file .gitignore hides is invisible to all of them.
    for name in ctx['ignored']:
        if '__pycache__' not in name.split('/')[:-1]:
            rep.error('ignored-file', f'{name}: .gitignore hides it, so no check reads it and it would never be '
                                      f'committed; only __pycache__/ may be ignored — remove the rule that hides it')

    nums = Counter(int(DOMAIN_RE.fullmatch(d).group(1)) for d in ctx['domains'])
    for n, c in sorted(nums.items()):
        if c > 1:
            rep.error('domain-number-duplicate', f'{c} domain directories are numbered {n:02d}')
    if nums and sorted(nums) != list(range(1, max(nums) + 1)):
        missing = sorted(set(range(1, max(nums) + 1)) - set(nums))
        rep.error('domain-number-gap', f'domain numbers skip {missing}')

    for name in files:
        parts = name.split('/')
        if parts[0] not in domains or len(parts) == 1:
            continue
        rep.count('domain files')
        if len(parts) == 2:
            if parts[1] not in DOMAIN_FILES:
                rep.error('domain-unexpected-entry', f'{name}: a domain directory holds sources_domain.csv, FINDINGS.md, '
                                                     f'full_texts/ and extracted_data/ only')
        elif len(parts) > 3 or parts[1] not in ('full_texts', 'extracted_data'):
            rep.error('domain-unexpected-entry', f'{name}: not directly inside the domain\'s full_texts/ or extracted_data/')
        elif parts[1] == 'extracted_data' and not any(parts[2].endswith(s) for s in EXTRACTED_SUFFIXES):
            rep.error('extracted-bad-extension', f'{name}: extracted data is CSV (or JSON for a raw service response)')
    for d in ctx['domains']:
        for part in ('sources_domain.csv', 'FINDINGS.md'):
            if f'{d}/{part}' not in files:
                rep.error('domain-file-missing', f'{d}/{part} is missing')
    rep.expect('domain files')
    # The manifest's sha256 is of the bytes git stores. A checkout with core.autocrlf rewrites the line ends of a file
    # git treats as text (five hosted .html/.txt files, until 2026-10-12), so a fresh clone failed manifest-stale.
    hosted = [n for n in files if len(n.split('/')) == 3 and n.split('/')[1] == 'full_texts']
    attrs = text_attributes(hosted)
    converted = [n for n in hosted if attrs[n] != 'unset']
    if converted:
        rep.error('full-text-eol-converted', f'{len(converted)} hosted file(s), first {converted[0]}, are not marked '
                                             f'-text: a checkout with core.autocrlf would rewrite a text file\'s line '
                                             f'ends, so its bytes would stop matching full_texts_manifest.csv; '
                                             f'.gitattributes must hold "**/full_texts/** -text"')


# ---------------------------------------------------------------------------------------------- registry

def check_registry(rep, ctx):
    rep.start('registry')
    rep.count('domain directories', len(ctx['domains']))
    rep.expect('domain directories')
    rows, unreadable = [], 0
    for d in ctx['domains']:
        try:
            domain_rows = read_domain_csv(d)
        except DataError as e:
            unreadable += 1
            ctx['unread_domains'].add(d)
            rep.error(e.code, f'{e} — its sources are not in this check')
            continue
        for r in domain_rows:
            rec = dict(zip(DOMAIN_COLS, r))
            sid = rec['id']
            for k, v in rec.items():
                if not v.strip():
                    rep.error('domain-field-empty', f'{d}/sources_domain.csv {sid or "(no id)"}: {k} is empty')
                elif v != v.strip() or '\n' in v or '\r' in v:
                    rep.error('domain-field-whitespace', f'{d}/sources_domain.csv {sid}: {k} has leading/trailing '
                                                         f'whitespace or a line break')
            if rec['year'].strip() and not YEAR_RE.match(rec['year']):
                rep.error('year-format', f'{sid}: year {rec["year"]!r} must start with a year, ~year or "n.d."')
            rows.append([d] + r)
    rep.count('sources', len(rows))
    rep.expect('sources')

    try:
        header, built = read_csv(REGISTRY)
    except DataError as e:
        rep.error(e.code, str(e))
    else:
        if header != REGISTRY_COLS:
            rep.error('registry-header', f'sources.csv header is {header}, expected {REGISTRY_COLS}')
        elif unreadable:
            rep.error('registry-stale', f'sources.csv cannot be compared: {unreadable} sources_domain.csv file(s) unreadable')
        elif built != rows:
            rep.error('registry-stale', 'sources.csv does not match the per-domain CSVs — run: python tools/build_registry.py')

    reg = {}
    for row in rows:
        r = dict(zip(REGISTRY_COLS, row))
        sid = r['id']
        if sid in reg:
            rep.error('registry-duplicate-id', f'duplicate id {sid} ({reg[sid]["domain_dir"]} and {r["domain_dir"]})')
            continue
        reg[sid] = r
        if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', sid):
            rep.error('id-format', f'{sid!r}: id must be lowercase letters, digits, underscores and hyphens')
        if r['tier'] not in TIERS:
            rep.error('tier', f'{sid}: tier {r["tier"]!r} is not one of {sorted(TIERS)}')
        cls = access_class(r['access_status'])
        if cls not in ACCESS_CLASSES:
            rep.error('access-class', f'{sid}: access_status starts with {cls!r}; allowed: {sorted(ACCESS_CLASSES)}')
    ctx['reg'] = reg


# ---------------------------------------------------------------------------------------------- INDEX.md

def check_index(rep, ctx):
    rep.start('INDEX.md')
    reg = ctx['reg']
    text = read_text(INDEX)
    sections = re.split(r'^## ', text, flags=re.M)
    seen, order = set(), []
    for sec in sections[1:]:
        m = re.match(r'Domain (\d+)\b', sec)
        if not m:
            continue
        num = int(m.group(1))
        order.append(num)
        matches = [d for d in ctx['domains'] if d.startswith(f'{num:02d}_')]
        if len(matches) != 1:
            rep.error('index-domain-no-dir', f'"## Domain {num}" matches {len(matches)} domain directories, expected 1')
            continue
        d = matches[0]
        if d in seen:
            rep.error('index-domain-duplicate', f'"## Domain {num}" appears twice')
            continue
        seen.add(d)
        if d in ctx['unread_domains']:
            rep.count('domain tables not compared: their sources_domain.csv is unreadable')
            continue
        rep.count('domain tables')
        lines = sec.split('\n')
        table = [i for i, l in enumerate(lines) if l.startswith('|')]
        if not table:
            rep.error('index-no-table', f'Domain {num}: no source table')
            continue
        if table != list(range(table[0], table[0] + len(table))):
            rep.error('index-table-split', f'Domain {num}: table is split by a blank line or text — rows after the break '
                                           f'do not render as table rows')
        # A header narrower than the rows makes GitHub drop the extra cells, so check the full header.
        if table_cells(lines[table[0]]) != INDEX_HEADER:
            rep.error('index-header', f'Domain {num}: table header must be "| {" | ".join(INDEX_HEADER)} |"')
        if len(table) < 2 or table_cells(lines[table[1]]) != ['---'] * len(INDEX_HEADER):
            rep.error('index-separator', f'Domain {num}: second table line must be the 5-column "|---|...|" separator')
        ids = []
        for i in table[2:]:
            line = lines[i]
            cells = table_cells(line)
            if not line.rstrip().endswith('|') or len(cells) != 5:
                rep.error('index-row-cells', f'Domain {num}: row "{line[:50]}..." has {len(cells)} cells, expected 5 '
                                             f'(and a closing "|")')
                if cells[0]:
                    ids.append(cells[0])  # the row lists its id, so it is not also reported as missing
                continue
            sid = cells[0]
            ids.append(sid)
            if any(not c for c in cells):
                rep.error('index-empty-cell', f'Domain {num}: {sid or line[:50]} has an empty cell')
            if sid not in reg:
                if not registry_partial(rep, ctx):
                    rep.error('index-id-unknown', f'Domain {num}: id {sid!r} is not in sources.csv')
                continue
            if reg[sid]['domain_dir'] != d:
                rep.error('index-wrong-domain', f'Domain {num}: {sid} is registered under {reg[sid]["domain_dir"]}')
                continue
            if cells[1] != reg[sid]['tier']:
                rep.error('index-tier', f'Domain {num}: {sid} tier {cells[1]} here vs {reg[sid]["tier"]} in sources.csv')
            # R26-R27 wrote three rows as id | tier | source | venue | access; the cell count still matched.
            if ACCESS_WORDS.match(cells[4]):
                rep.error('index-access-in-last-cell', f'Domain {num}: {sid} has its access in the last cell — order is '
                                                       f'{" | ".join(INDEX_HEADER)}')
            hosted = access_class(reg[sid]['access_status']) == 'full_text_hosted'
            says_hosted = 'hosted' in cells[3].lower() and 'not hosted' not in cells[3].lower()
            if hosted != says_hosted:
                rep.error('index-access-mismatch', f'Domain {num}: {sid} access cell "{cells[3][:40]}" disagrees with '
                                                   f'access_status {access_class(reg[sid]["access_status"])!r}')
        expected = [sid for sid, r in reg.items() if r['domain_dir'] == d]
        missing = [s for s in expected if s not in ids]
        if missing:
            rep.error('index-missing-rows', f'Domain {num}: registered but not listed: {", ".join(missing)}')
        dups = [s for s, n in Counter(ids).items() if n > 1]
        if dups:
            rep.error('index-duplicate-rows', f'Domain {num}: listed twice: {", ".join(dups)}')
        if not missing and not dups and set(ids) <= set(expected) and ids != expected:
            rep.error('index-order', f'Domain {num}: rows are not in sources_domain.csv order')
    if order != sorted(order):
        rep.error('index-domain-order', f'"## Domain N" sections are out of order: {order}')
    for d in ctx['domains']:
        if d not in seen:
            rep.error('index-domain-missing', f'no "## Domain {int(d[:2])}" section for {d}')
    rep.expect('domain tables')


def check_log(rep, ctx):
    rep.start('research log')
    ctx['latest_round'] = None  # set before the read that can fail, so check_candidates sees "unknown", not a crash
    lines = log_lines(read_text(LOG))
    if lines is None:
        rep.error('log-missing', f'RESEARCH_LOG.md does not start with "{LOG_HEADING.strip()}"')
        return
    rounds, dates, started = [], [], False
    today = datetime.date.today()
    for n, line in enumerate(lines, 1):
        m = LOG_ENTRY_RE.match(line)
        if m:
            started = True
            rep.count('log entries')
            if m.group(1) is not None:
                rounds.append(int(m.group(1)))
            date = parse_date(m.group(2))
            if date is None:
                rep.error('log-date-invalid', f'log line {n}: {m.group(2)} is not a calendar date')
            elif date > today:
                rep.error('log-date-future', f'log line {n}: {m.group(2)} is after today ({today})')
            dates.append(m.group(2))
        elif line.startswith('- **'):
            rep.error('log-entry-format', f'log line {n}: entry must start "- **Round N** (YYYY-MM-DD)" or '
                                          f'"- **Maintenance** (YYYY-MM-DD)"')
        elif LOG_MISLABEL_RE.match(line):
            rep.error('log-mislabelled', f'log line {n}: "{line[:40]}" — log entries are "- **Round N** (YYYY-MM-DD): ...", '
                                         f'not headings or bare bold labels; the file holds no other section')
        elif not line.strip():
            # A blank line between the heading and the first entry is ordinary Markdown; one between entries is not.
            if started:
                rep.error('log-blank-line', f'log line {n}: blank line inside the log — keep entries contiguous')
        elif not started:
            rep.error('log-preamble', f'log line {n}: text before the first entry')
        # Any other line continues the entry above: Markdown folds a line that follows a list item with no blank line
        # into that item (Round 40's second paragraph, line 127). An unlabelled new entry is caught as log-mislabelled.
    rep.expect('log entries')
    if not rounds:
        rep.error('log-no-rounds', 'no "- **Round N**" entries found')
        return
    ctx['latest_round'] = max(rounds)
    if rounds != sorted(rounds, reverse=True):
        rep.error('log-order', 'rounds are not newest-first')
    missing = sorted(set(range(max(rounds) + 1)) - set(rounds))
    if missing:
        rep.error('log-gap', f'rounds missing from the log: {missing} — a RESEARCH_LOG.md rewrite may have dropped '
                             f'them (recover with git show <sha>:RESEARCH_LOG.md)')
    dups = sorted(r for r, c in Counter(rounds).items() if c > 1)
    if dups:
        rep.error('log-duplicate', f'rounds logged twice: {dups}')
    if dates != sorted(dates, reverse=True):
        rep.error('log-date-order', 'entry dates are not newest-first')


def log_lines(log_text):
    """The research log's lines below its heading, or None if the text does not start with the heading."""
    if not log_text.startswith(LOG_HEADING):
        return None
    return log_text[len(LOG_HEADING):].rstrip('\n').split('\n')


def committed_log(rep, rev, label):
    """The research log's lines in `rev`'s RESEARCH_LOG.md; reports log-no-baseline and returns None if it has none."""
    rc, blob = git_raw(ROOT, 'show', f'{rev}:RESEARCH_LOG.md')
    if rc != 0:
        rep.error('log-no-baseline', f'{label} has no RESEARCH_LOG.md to compare the research log with')
        return None
    try:
        text = blob.decode('utf-8').replace('\r\n', '\n')
    except UnicodeDecodeError as e:
        rep.error('log-no-baseline', f'{label}\'s RESEARCH_LOG.md is not UTF-8 ({e}), so the log cannot be compared')
        return None
    lines = log_lines(text)
    if lines is None:
        rep.error('log-no-baseline', f'{label}\'s RESEARCH_LOG.md does not start with "{LOG_HEADING.strip()}"')
    return lines


def check_log_history(rep, ctx):
    """AGENTS.md: the log is append-at-top only. The committed log must survive, unchanged, as the working log's tail.

    R43's rewrite deleted Rounds 0-41 and R46's deleted R45; a rewrite that keeps every round number would pass
    check_log, so this compares the text with the last commit. It catches a rewrite before it is committed.

    During a merge both sides have added entries at the top since they split, so neither side's log can be the
    merged log's tail (R153 and a maintenance entry, 2026-10-12). Then the log at their merge base must be the tail,
    and every line either side committed must still be in the merged log, in whichever order the entries are put.
    """
    rep.start('research log history')
    rc, _ = git(ROOT, 'rev-parse', '--verify', '--quiet', 'HEAD^{commit}')
    if rc != 0:
        rep.error('log-no-baseline', 'the repository has no commit to compare the research log with')
        return
    current = log_lines(read_text(LOG))
    if current is None:
        rep.error('log-missing', f'RESEARCH_LOG.md does not start with "{LOG_HEADING.strip()}", so it cannot be '
                                 f'compared with the committed log')
        return
    rc, merging = git(ROOT, 'rev-parse', '--verify', '--quiet', 'MERGE_HEAD^{commit}')
    if rc == 0:
        rc, base = git(ROOT, 'merge-base', 'HEAD', merging)
        if rc != 0:
            rep.error('log-no-baseline', f'HEAD and MERGE_HEAD {merging[:7]} share no history, so the merged research '
                                         f'log has no common log to keep')
            return
        tail_rev, tail_label, sides = base, f'the merge base {base[:7]}', [('HEAD', 'HEAD'), (merging, 'MERGE_HEAD')]
    else:
        tail_rev, tail_label, sides = 'HEAD', 'HEAD', []
    committed = committed_log(rep, tail_rev, tail_label)
    if committed is None:
        return
    rep.count('committed log lines', len(committed))
    if not (len(current) >= len(committed) and current[len(current) - len(committed):] == committed):
        # Name the first committed line, from the oldest end, that is changed or gone (one must be: the tail differs).
        line = next(committed[-k] for k in range(1, len(committed) + 1)
                    if k > len(current) or current[-k] != committed[-k])
        rep.error('log-rewritten', f'{tail_label}\'s log line "{line[:60]}" is changed, moved or gone — the log is '
                                   f'append-at-top only; restore the older entries from git show {tail_rev[:7]}:RESEARCH_LOG.md')
    kept = set(current)
    for rev, label in sides:
        lines = committed_log(rep, rev, label)
        if lines is None:
            continue
        rep.count('merged-side log lines', len(lines))
        lost = [line for line in lines if line not in kept]
        if lost:
            rep.error('log-merge-lost', f'{len(lost)} line(s) of {label}\'s log are not in the merged log, first '
                                        f'"{lost[0][:60]}" — a merge keeps both sides\' entries')


def check_rejected(rep, ctx):
    """README "Rejecting a source": the INDEX.md table is a rejected source's only record outside the research log."""
    rep.start('rejected sources')
    reg = ctx['reg']
    ctx['rejected'] = {}
    text = read_text(INDEX)
    m = re.search(r'^## Rejected sources\n(.*?)(?=^## |\Z)', text, flags=re.M | re.S)
    if not m:
        rep.error('rejected-missing', 'INDEX.md has no "## Rejected sources" section (it is the last section)')
        return
    if m.end() != len(text):
        rep.error('rejected-position', '"## Rejected sources" must be the last section of INDEX.md')
    lines = m.group(1).split('\n')
    table = [i for i, l in enumerate(lines) if l.startswith('|')]
    if not table:
        rep.error('rejected-no-table', 'no table — keep the header and separator even while it has no rows')
        return
    if table != list(range(table[0], table[0] + len(table))):
        rep.error('rejected-table-split', 'table is split by a blank line or text — rows after the break do not render')
    if table_cells(lines[table[0]]) != REJECTED_HEADER:
        rep.error('rejected-header', f'table header must be "| {" | ".join(REJECTED_HEADER)} |"')
    if len(table) < 2 or table_cells(lines[table[1]]) != ['---'] * len(REJECTED_HEADER):
        rep.error('rejected-separator', 'second table line must be the 4-column "|---|...|" separator')
    rejected = {}
    for i in table[2:]:
        line = lines[i]
        cells = table_cells(line)
        if not line.rstrip().endswith('|') or len(cells) != len(REJECTED_HEADER):
            rep.error('rejected-row-cells', f'row "{line[:50]}..." has {len(cells)} cells, expected '
                                            f'{len(REJECTED_HEADER)} (and a closing "|")')
            continue
        sid = cells[0]
        if sid in rejected:
            rep.error('rejected-duplicate', f'{sid} is listed twice')
        rejected[sid] = cells
        if any(not c for c in cells):
            rep.error('rejected-empty-cell', f'{sid or line[:50]}: every row needs an id, source, link and reason')
        if sid in reg:
            rep.error('rejected-still-registered', f'{sid} is rejected but still registered in '
                                                   f'{reg[sid]["domain_dir"]}/sources_domain.csv (ids stay reserved)')
    ctx['rejected'] = rejected
    if not rejected:
        return
    # Nothing but the research log may name a rejected id: not a file path, not a CSV cell, not a FINDINGS block.
    token = re.compile(r'(?<![A-Za-z0-9_-])(' + '|'.join(map(re.escape, rejected)) + r')(?![A-Za-z0-9_-])')
    outside_table = text[:m.start()] + text[m.end():]
    for name in ctx['files']:
        rep.count('files scanned for rejected ids')
        hits = set(token.findall(name))
        path = ROOT / name
        if path == INDEX:
            hits |= set(token.findall(outside_table))
        elif path != LOG and any(name.endswith(s) for s in ('.csv', '.md', '.json')):
            try:
                hits |= set(token.findall(read_text(path)))
            except DataError as e:
                rep.error(e.code, f'{e} — it was not searched for rejected ids')
        for sid in sorted(hits):
            rep.error('rejected-still-named', f'{name} still names rejected source {sid} — its only record is the '
                                              f'"Rejected sources" row')
    rep.expect('files scanned for rejected ids')


# ---------------------------------------------------------------------------------------------- manifest

def check_manifest(rep, ctx):
    rep.start('manifest')
    reg = ctx['reg']
    try:
        header, rows = read_csv(MANIFEST)
    except DataError as e:
        rep.error(e.code, str(e))
        return
    if header != MANIFEST_COLS:
        rep.error('manifest-header', f'header is {header}, expected {MANIFEST_COLS}')
        return
    by_id = defaultdict(list)
    listed = set()
    restricted = []
    for row in rows:
        rep.count('manifest rows')
        d, sid, fname, size, digest, license = row
        lic = license.split(' ', 1)[0]
        if lic not in LICENSE_CLASSES:
            rep.error('manifest-license', f'{fname}: license {lic!r} must start with one of {sorted(LICENSE_CLASSES)}')
        elif lic in NOT_REDISTRIBUTABLE:
            restricted.append(f'{sid} ({lic})')
        if (d, fname) in listed:
            rep.error('manifest-duplicate', f'{d}/full_texts/{fname} listed twice')
        listed.add((d, fname))
        if d not in ctx['domains']:
            rep.error('manifest-domain-unknown', f'{fname}: domain_dir {d!r} is not a domain directory')
            continue
        if not plain_file_name(fname):
            rep.error('manifest-file-name', f'{d} {sid}: file {fname!r} must be a bare file name inside '
                                            f'{d}/full_texts/, with no directory part')
            continue
        if sid not in reg:
            if not registry_partial(rep, ctx):
                rep.error('manifest-id-unknown', f'{fname}: id {sid!r} is not in sources.csv')
        elif reg[sid]['domain_dir'] != d:
            rep.error('manifest-wrong-domain', f'{fname}: {sid} is registered under {reg[sid]["domain_dir"]}, not {d}')
        path = ROOT / d / 'full_texts' / fname
        if not path.is_file():
            rep.error('manifest-file-missing', f'{d}/full_texts/{fname} does not exist')
            continue
        actual_size, actual_digest = file_digest(path)
        if str(actual_size) != size or actual_digest != digest:
            rep.error('manifest-stale', f'{fname}: bytes/sha256 differ from disk — run: python tools/build_registry.py')
        if actual_size > GITHUB_HARD_LIMIT:
            rep.error('manifest-file-too-large', f'{fname} is {actual_size / 2**20:.0f} MB — GitHub rejects files over 100 MB')
        elif actual_size > GITHUB_WARN_LIMIT:
            rep.warn('manifest-file-large', f'{fname} is {actual_size / 2**20:.0f} MB — GitHub warns above 50 MB')
        by_id[sid].append(actual_digest)
    # A warning, not an error: taking a file down is the owner's decision (README access rule 1).
    if restricted:
        rep.warn('manifest-not-redistributable', f'{len(restricted)} hosted files have no licence that permits '
                                                 f'redistribution: {", ".join(restricted)}')

    for name in ctx['files']:
        parts = name.split('/')
        if len(parts) == 3 and parts[1] == 'full_texts' and (parts[0], parts[2]) not in listed:
            rep.error('manifest-unlisted-file', f'{name} is not in full_texts_manifest.csv')

    for sid, r in reg.items():
        hosted = access_class(r['access_status']) == 'full_text_hosted'
        if hosted and sid not in by_id:
            rep.error('hosted-without-file', f'{sid} is full_text_hosted but has no file in full_texts_manifest.csv')
        if not hosted and sid in by_id:
            rep.error('file-without-hosted', f'{sid} has a hosted file but access_status is {access_class(r["access_status"])!r}')
        for prefix in re.findall(r'sha256=([0-9a-f]{6,})', r['access_status']):
            if sid in by_id and not any(h.startswith(prefix) for h in by_id[sid]):
                rep.warn('access-sha-mismatch', f'{sid}: access_status records sha256={prefix}… which matches none of '
                                                f'its hosted files')


# ---------------------------------------------------------------------------------------------- extracted data

def check_extracted(rep, ctx):
    rep.start('extracted_data')
    reg = ctx['reg']
    cited = defaultdict(set)  # domain -> every registry id its extracted files name
    # The same token boundaries as the rejected-id scan: an id glued to more id characters is a different token.
    id_token = re.compile(r'[A-Za-z0-9_-]+')
    for name in ctx['files']:
        parts = name.split('/')
        if len(parts) != 3 or parts[1] != 'extracted_data' or parts[0] not in ctx['domains']:
            continue
        d, path = parts[0], ROOT / name
        if name.endswith('.json'):
            rep.count('extracted files')
            try:
                text = read_text(path)
                json.loads(text)
            except DataError as e:
                rep.error(e.code, f'{e} — its citations are not counted')
                continue
            except ValueError as e:
                rep.error('extracted-json-invalid', f'{name}: not valid JSON ({e})')
                continue
            cited[d] |= set(id_token.findall(text)) & set(reg)
            continue
        if not name.endswith('.csv'):
            continue  # check_layout reports any other extension as extracted-bad-extension
        rep.count('extracted files')
        try:
            header, rows = read_csv(path)
        except DataError as e:
            rep.error(e.code, f'{e} — its rows and citations are not checked')
            continue
        cited[d] |= set(id_token.findall(read_text(path))) & set(reg)
        dup_cols = sorted(c for c, n in Counter(header).items() if n > 1)
        if dup_cols:
            rep.error('extracted-header-duplicate', f'{name}: column names repeat: {dup_cols}')
        if any(not c.strip() for c in header):
            rep.error('extracted-header-empty', f'{name}: a header cell is empty')
        if not rows:
            rep.error('extracted-no-rows', f'{name}: a header and no rows, so the file holds no data')
        for n, row in enumerate(rows, 2):
            if row == header:
                rep.error('extracted-header-repeat', f'{name} line {n}: repeats the header line')
            elif not any(c.strip() for c in row):
                rep.error('extracted-row-empty', f'{name} line {n}: every cell is blank')
        if 'source_id' not in header:
            # AGENTS.md: every extracted-data CSV needs a source_id column, or its rows trace to no registry id.
            rep.error('extracted-no-source-col', f'{name}: no source_id column, so its rows are not traceable to a '
                                                 f'registry id (leave the cell blank for the pipeline\'s own value)')
            continue
        col = header.index('source_id')
        unknown = set()
        for n, row in enumerate(rows, 2):
            cell = row[col]
            if row == header or not cell:
                continue  # a blank source_id is the pipeline's own value or a comparison computed here (AGENTS.md)
            # A row derived from two sources lists both, joined by ';'.
            ids = cell.split(';')
            if any(not i or i != i.strip() for i in ids):
                rep.error('extracted-source-id-format', f'{name} line {n}: source_id {cell!r} must be ids joined by ";" '
                                                        f'with no empty or padded entry')
            # A padded entry is reported above as a format error, not again as an unknown id.
            unknown |= {i for i in ids if i and i == i.strip() and i not in reg}
        if unknown and not registry_partial(rep, ctx):
            rep.error('extracted-unknown-source', f'{name}: source_id not in sources.csv: {", ".join(sorted(unknown))}')
    rep.expect('extracted files')
    # AGENTS.md / README "How an item earns a place" #3: numbers extracted into a CSV, or the row says context-only.
    # A registered_not_pulled row has not been read yet, so it cannot be either; it is counted in the summary instead.
    for sid, r in reg.items():
        if (sid not in cited[r['domain_dir']] and access_class(r['access_status']) not in PENDING_ACCESS
                and not re.search(r'context[- ]only', r['access_status'] + r['pipeline_mapping'], re.I)):
            rep.error('source-uncited', f'{sid} ({r["domain_dir"]}): no extracted-data file of its domain cites it by id, '
                                        f'and its registry row is not marked "Context-only: <reason>"')


# ---------------------------------------------------------------------------------------------- file references

# A data file a write-up cites: `extracted_data/<file>` or `full_texts/<file>`, relative to the domain whose FINDINGS.md
# or INDEX.md section cites it; `<domain>/...` from anywhere; `<sha>:<domain>/...` for a file only git history holds
# (DOWNLOADS.md's restore commands).
DATA_REF_RE = re.compile(r'(extracted_data|full_texts)/([A-Za-z0-9_.-]+\.[A-Za-z0-9]+)')
REF_PREFIX_RE = re.compile(r'(?<![\w.:/-])(?:([0-9a-f]{7,40}):)?(\d\d_[a-z0-9_]+)/$')
# Root files whose references are checked. RESEARCH_LOG.md is not: it is history, and files have moved since the
# rounds that named them.
REF_ROOT_FILES = ('README.md', 'INDEX.md', 'DOWNLOADS.md')


def reference_scopes(name, text, domain, domains):
    """(start, end, domain or None) for each stretch of `text` whose bare references resolve in that domain."""
    if name != 'INDEX.md':
        return [(0, len(text), domain)]
    # Each "## Domain N" section resolves bare references in its own domain; the other sections in none.
    starts = [m.start() for m in re.finditer(r'^## ', text, flags=re.M)]
    scopes = [(0, starts[0] if starts else len(text), None)]
    for a, b in zip(starts, starts[1:] + [len(text)]):
        m = re.match(r'## Domain (\d+)\b', text[a:b])
        matches = [d for d in domains if m and d.startswith(f'{int(m.group(1)):02d}_')]
        scopes.append((a, b, matches[0] if len(matches) == 1 else None))
    return scopes


def check_text_references(rep, files, text, start, end, domain, where):
    """Report every data file cited in text[start:end] that does not exist; `where(pos)` locates a match for the report."""
    for m in DATA_REF_RE.finditer(text, start, end):
        rep.count('file references')
        before = text[max(start, m.start() - 120):m.start()]
        prefix = REF_PREFIX_RE.search(before)
        if prefix:
            sha, d = prefix.groups()
        elif before.endswith('/'):
            rep.error('path-ref-unresolved', f'{where(m.start())}: the directory before {m.group(0)} is not a domain '
                                             f'directory, so the reference cannot be checked')
            continue
        elif domain is None:
            rep.error('path-ref-no-domain', f'{where(m.start())}: {m.group(0)} names no domain here; write '
                                            f'<domain>/{m.group(0)}')
            continue
        else:
            sha, d = None, domain
        path = f'{d}/{m.group(0)}'
        if sha is not None:
            rep.count('references into git history')
            if git(ROOT, 'cat-file', '-e', f'{sha}:{path}')[0] != 0:
                rep.error('path-ref-missing-at-commit', f'{where(m.start())}: {sha}:{path} is not in the '
                                                        f'repository\'s history')
        elif path not in files:
            rep.error('path-ref-missing', f'{where(m.start())}: {path} does not exist; correct the path, or name a file '
                                          f'that is no longer here without its directory')


def check_references(rep, ctx):
    """Every data file cited exists, in the working tree or in the commit the reference names. Cited where: FINDINGS.md,
    README.md, DOWNLOADS.md, INDEX.md, every registry cell and every candidate cell.

    Ten FINDINGS.md entries said "Full text hosted" for PDFs un-hosted on 2026-09-26; four FINDINGS.md paths, one
    candidate's evidence and two access_status cells named files that had moved or been un-hosted.
    """
    rep.start('file references')
    files = set(ctx['files'])
    sources = [(f'{d}/FINDINGS.md', d) for d in ctx['domains']] + [(n, None) for n in REF_ROOT_FILES]
    for name, domain in sources:
        if name not in files:
            continue  # check_layout reports a missing FINDINGS.md or required root file; DOWNLOADS.md is optional
        try:
            text = read_text(ROOT / name)
        except DataError as e:
            rep.error(e.code, f'{e} — its file references were not checked')
            continue
        for start, end, scope_domain in reference_scopes(name, text, domain, ctx['domains']):
            check_text_references(rep, files, text, start, end, scope_domain,
                                  lambda pos: f'{name} line {text.count(chr(10), 0, pos) + 1}')
    # Bare references in a row resolve in the row's domain. The registry rows are the readable ones (check_registry
    # reports an unreadable sources_domain.csv); the candidates are None when unreadable (check_candidates reports it).
    for sid, r in ctx['reg'].items():
        for col in DOMAIN_COLS:
            check_text_references(rep, files, r[col], 0, len(r[col]), r['domain_dir'],
                                  lambda pos: f'{r["domain_dir"]}/sources_domain.csv {sid} {col}')
    for c in ctx['candidates'] if ctx['candidates'] is not None else ():
        domain = c['domain_dir'] if c['domain_dir'] in ctx['domains'] else None  # cand-domain reports a bad one
        for col in CANDIDATE_COLS:
            check_text_references(rep, files, c[col], 0, len(c[col]), domain,
                                  lambda pos: f'revision_candidates.csv {c["id"]} {col}')
    rep.expect('file references')


# ---------------------------------------------------------------------------------------------- candidates

def check_candidates(rep, ctx):
    rep.start('revision_candidates')
    reg = ctx['reg']
    # None means unreadable (reported here): the commit-map and upstream checks then skip their cross-checks
    # against the candidates instead of reporting every map row as unused.
    ctx['candidates'] = None
    try:
        header, rows = read_csv(CANDIDATES)
    except DataError as e:
        rep.error(e.code, str(e))
        return
    if header != CANDIDATE_COLS:
        rep.error('cand-header', f'header is {header}, expected {CANDIDATE_COLS}')
        return
    today = datetime.date.today()
    seen = set()
    ctx['candidates'] = []
    for row in rows:
        rep.count('candidates')
        r = dict(zip(header, row))
        ctx['candidates'].append(r)
        cid = r['id']
        if not re.fullmatch(r'rc-\d{3}', cid) or cid in seen:
            rep.error('cand-id', f'id {cid!r} must be unique and look like rc-001')
        seen.add(cid)
        for k in ('status', 'kind', 'domain_dir', 'source_ids', 'found_round', 'target_repo', 'target_file', 'target_row', 'field',
                  'current_value', 'proposed', 'evidence', 'checked_against', 'checked_date'):
            if not r[k].strip():
                rep.error('cand-field-empty', f'{cid}: {k} is empty')
        if r['status'] not in CANDIDATE_STATUSES:
            rep.error('cand-status', f'{cid}: status {r["status"]!r} not in {sorted(CANDIDATE_STATUSES)}')
        if r['kind'] not in CANDIDATE_KINDS:
            rep.error('cand-kind', f'{cid}: kind {r["kind"]!r} not in {sorted(CANDIDATE_KINDS)}')
        if r['domain_dir'] not in ctx['domains']:
            rep.error('cand-domain', f'{cid}: domain_dir {r["domain_dir"]!r} does not exist')
        ids = r['source_ids'].split(';')
        if r['source_ids'] and any(not i or i != i.strip() for i in ids):
            rep.error('cand-source-ids-format', f'{cid}: source_ids {r["source_ids"]!r} must be ids joined by ";" with no '
                                                f'empty or padded entry')
        for sid in ids:
            # An empty or padded entry is reported above as a format error, not again as an unknown id.
            if sid and sid == sid.strip() and sid not in reg and not registry_partial(rep, ctx):
                rep.error('cand-source-unknown', f'{cid}: source id {sid!r} is not in sources.csv')
        fr = re.fullmatch(r'R(\d+)', r['found_round'])
        if not fr:
            rep.error('cand-found-round', f'{cid}: found_round {r["found_round"]!r} should look like R12')
        elif ctx['latest_round'] is not None and int(fr.group(1)) > ctx['latest_round']:
            rep.error('cand-found-round-future', f'{cid}: found_round {r["found_round"]} is after the latest logged '
                                                 f'round, R{ctx["latest_round"]}')
        date = parse_date(r['checked_date']) if re.fullmatch(r'\d{4}-\d{2}-\d{2}', r['checked_date']) else None
        if date is None:
            rep.error('cand-date', f'{cid}: checked_date {r["checked_date"]!r} should be a YYYY-MM-DD date')
        elif date > today:
            rep.error('cand-date-future', f'{cid}: checked_date {r["checked_date"]} is after today ({today})')
        if r['target_repo'] not in UPSTREAM_REPOS:
            rep.error('cand-target-repo', f'{cid}: target_repo {r["target_repo"]!r} not in {sorted(UPSTREAM_REPOS)}')
        # --upstream checks that this file exists. Only a method candidate may name a model stage instead
        # (rc-025 "Stage 4 cost cascade"), because a method has no single cell.
        if r['kind'] != 'method' and not TARGET_PATH_RE.match(r['target_file']):
            rep.error('cand-target-file', f'{cid}: target_file {r["target_file"][:50]!r} must start with the upstream '
                                          f'file path (only a method candidate may name a model stage instead)')
        ca = r['checked_against'].split('@')
        if len(ca) != 2 or ca[0] not in UPSTREAM_REPOS or not SHA_RE.fullmatch(ca[1]):
            rep.error('cand-checked-against', f'{cid}: checked_against {r["checked_against"]!r} must be <repo>@<sha> with '
                                              f'repo in {sorted(UPSTREAM_REPOS)}')
        elif r['status'] in LIVE_CANDIDATE_STATUSES and ca[0] != r['target_repo']:
            # A closed row may cite the repo where it was resolved (rc-014: an AsteroidCatalog cell closed by an
            # economicspace change); an open one is re-checked against its own cell.
            rep.error('cand-checked-wrong-repo', f'{cid} is {r["status"]} but was checked against {ca[0]}, not its '
                                                 f'target_repo {r["target_repo"]}')
    rep.expect('candidates')


def check_upstream_map(rep, ctx):
    rep.start('upstream_commit_map')
    ctx['upstream_map'] = None  # None means unreadable (reported here); check_upstream then skips map lookups
    try:
        header, rows = read_csv(UPSTREAM_MAP)
    except DataError as e:
        rep.error(e.code, f'{e} — no commit map checks ran')
        return
    if header != UPSTREAM_MAP_COLS:
        rep.error('map-header', f'header is {header}, expected {UPSTREAM_MAP_COLS}')
        return
    cands = ctx['candidates']
    by_ref = defaultdict(list)
    for c in cands if cands is not None else ():
        by_ref[c['checked_against']].append(c['id'])
    seen = set()
    ctx['upstream_map'] = []
    for row in rows:
        rep.count('map rows')
        r = dict(zip(header, row))
        ctx['upstream_map'].append(r)
        ref = f'{r["repo"]}@{r["old_sha"]}'
        if r['repo'] not in UPSTREAM_REPOS:
            rep.error('map-repo', f'{ref}: repo not in {sorted(UPSTREAM_REPOS)}')
        if not all(SHA_RE.fullmatch(r[k]) for k in ('old_sha', 'main_sha', 'tree')):
            rep.error('map-sha-format', f'{ref}: old_sha, main_sha and tree must be hex commit ids')
        if ref in seen:
            rep.error('map-duplicate', f'{ref} is mapped twice')
        seen.add(ref)
        cited_in = r['checked_against_in'].split(';')
        if r['checked_against_in'] and any(not c or c != c.strip() for c in cited_in):
            rep.error('map-cited-format', f'{ref}: checked_against_in {r["checked_against_in"]!r} must be candidate ids '
                                          f'joined by ";" with no empty or padded entry')
        if cands is None:
            continue  # revision_candidates.csv is unreadable (reported there), so who cites the row is unknown
        listed = sorted(filter(None, cited_in))
        citing = sorted(by_ref[ref]) if ref in by_ref else []
        if not citing:
            rep.error('map-unused', f'{ref}: no candidate cites this commit (checked_against_in lists {listed}); '
                                    f'delete the row')
        elif listed != citing:
            rep.error('map-cited-mismatch', f'{ref}: checked_against_in lists {listed}, but the candidates citing it are '
                                            f'{citing}')


def git_raw(repo, *args, stdin=None):
    """(returncode, stdout bytes). A git that cannot be run at all raises DataError, which stops the check."""
    try:
        proc = subprocess.run(['git', '-C', str(repo)] + list(args), input=stdin, capture_output=True)
    except OSError as e:
        raise DataError('git-unavailable', f'cannot run git: {e}')
    return proc.returncode, proc.stdout


def text_attributes(paths):
    """{path: git's `text` attribute}. "unset" (from `-text`) means a checkout writes the committed bytes unchanged."""
    rc, out = git_raw(ROOT, 'check-attr', '-z', '--stdin', 'text', stdin='\0'.join(paths).encode('utf-8'))
    if rc != 0:
        raise DataError('git-check-attr', f'git check-attr failed in {ROOT}, so no hosted file\'s line-end handling '
                                          f'was checked')
    fields = out.decode('utf-8').split('\0')
    # -z output is path NUL attribute NUL value NUL, for each path.
    return {fields[i]: fields[i + 2] for i in range(0, len(fields) - 1, 3)}


def git(repo, *args):
    """(returncode, stdout text). Output that is not UTF-8 keeps its bytes as escapes, so it compares unequal."""
    rc, out = git_raw(repo, *args)
    return rc, out.decode('utf-8', 'backslashreplace').strip()


def check_target_file(rep, c, checked_repo, sha, repos):
    """The file a candidate names exists upstream: at the commit it was checked against, or, for a closed row checked
    in another repo (cand-checked-wrong-repo allows that only for closed rows), on its target repo's origin/main."""
    m = TARGET_PATH_RE.match(c['target_file'])
    if not m:
        # cand-target-file allows a stage name instead of a path only for a method candidate.
        rep.count('targets named by model stage, no file to check')
        return
    target = c['target_repo']
    if target not in repos:
        return  # reported as upstream-repo-missing, or by check_candidates as cand-target-repo
    where = sha if target == checked_repo else 'origin/main'
    rep.count('target files checked')
    if git(repos[target], 'cat-file', '-e', f'{where}:{m.group(0)}')[0] != 0:
        rep.error('upstream-target-file-missing', f'{c["id"]}: {target} has no {m.group(0)} at {where}')


def check_upstream(rep, ctx):
    """--upstream: every cited commit exists in the sibling clone; open rows sit on main; off-main closed rows are mapped."""
    rep.start('upstream')
    repos = {}
    for name in sorted(UPSTREAM_REPOS):
        path = ROOT.parent / name
        rc, _ = git(path, 'rev-parse', '--verify', 'origin/main^{commit}')
        if rc != 0:
            rep.error('upstream-repo-missing', f'{path} is not a clone with an origin/main branch; clone it next to this '
                                               f'repo and fetch, or run without --upstream')
            continue
        repos[name] = path
        # Which origin/main was compared: a clone that was not fetched compares against an old main.
        ctx['upstream_heads'][name] = git(path, 'rev-parse', '--short', 'origin/main')[1]
    map_rows = ctx['upstream_map']  # None: the map is unreadable, reported by check_upstream_map
    mapped = {f'{r["repo"]}@{r["old_sha"]}': r for r in map_rows} if map_rows is not None else None
    for r in map_rows if map_rows is not None else ():
        if r['repo'] not in repos:
            continue  # reported above as upstream-repo-missing (or by check_upstream_map as map-repo)
        path = repos[r['repo']]
        rep.count('commits checked')
        ref = f'{r["repo"]}@{r["old_sha"]}'
        rc1, old_tree = git(path, 'rev-parse', '--verify', f'{r["old_sha"]}^{{tree}}')
        rc2, new_tree = git(path, 'rev-parse', '--verify', f'{r["main_sha"]}^{{tree}}')
        rc3, _ = git(path, 'merge-base', '--is-ancestor', r['main_sha'], 'origin/main')
        if rc1 or rc2 or rc3 or old_tree != new_tree:
            rep.error('map-not-equivalent', f'{ref} -> {r["main_sha"]}: both must exist, the second must be on '
                                            f'origin/main, and their trees must be identical')
            continue
        if not old_tree.startswith(r['tree']):
            rep.error('map-tree-mismatch', f'{ref}: tree column {r["tree"]} is not the commits\' tree {old_tree[:12]}')
        if git(path, 'merge-base', '--is-ancestor', r['old_sha'], 'origin/main')[0] == 0:
            rep.error('map-old-on-main', f'{ref} is on origin/main, so it needs no mapping; delete the row')
        subject = git(path, 'log', '-1', '--format=%s', r['main_sha'])[1]
        if subject != r['subject']:
            rep.error('map-subject-mismatch', f'{ref}: subject column {r["subject"][:50]!r} is not {r["main_sha"]}\'s '
                                              f'subject {subject[:50]!r}')
    # None: the candidates are unreadable, reported by check_candidates.
    for c in ctx['candidates'] if ctx['candidates'] is not None else ():
        ref = c['checked_against']
        name, _, sha = ref.partition('@')
        if name not in repos:
            continue  # reported above as upstream-repo-missing (or by check_candidates as cand-checked-against)
        path = repos[name]
        rep.count('commits checked')
        if git(path, 'cat-file', '-e', f'{sha}^{{commit}}')[0] != 0:
            rep.error('upstream-sha-unknown', f'{c["id"]}: {ref} is not a commit in {path}')
            continue
        check_target_file(rep, c, name, sha, repos)
        if git(path, 'merge-base', '--is-ancestor', sha, 'origin/main')[0] == 0:
            continue
        if c['status'] in LIVE_CANDIDATE_STATUSES:
            rep.error('upstream-open-off-main', f'{c["id"]} is {c["status"]} but {ref} is not on {name} origin/main; '
                                                f're-check the cell against main and update checked_against')
        elif mapped is not None and ref not in mapped:
            rep.error('upstream-sha-unmapped', f'{c["id"]}: {ref} is not on {name} origin/main and has no row in '
                                               f'upstream_commit_map.csv')
    rep.expect('commits checked')


# ---------------------------------------------------------------------------------------------- README

def check_readme(rep, ctx):
    rep.start('README.md')
    text = read_text(README)
    m = re.search(r'^## Layout\n+```\n(.*?)\n```', text, flags=re.M | re.S)
    if not m:
        rep.error('readme-layout-missing', 'README.md has no "## Layout" section with a code block')
        return
    layout = m.group(1)
    for d in ctx['domains']:
        rep.count('layout entries')
        if not re.search(r'^' + re.escape(d) + r'/', layout, flags=re.M):
            rep.error('readme-domain-missing', f'{d}/ has no line in README "Layout"')
    entries = [n for n, listed in ROOT_FILES.items() if listed and (ROOT / n).exists()]
    entries += [d + '/' for d in sorted(ROOT_DIRS) if (ROOT / d).is_dir()]
    for name in entries:
        if not re.search(r'^' + re.escape(name) + r'(\s|$)', layout, flags=re.M):
            rep.error('readme-root-file-missing', f'{name} has no line in README "Layout"')
    rep.expect('layout entries')
    # "Why this repo exists" maps each domain to the pipeline cells it backs (R152: domain 27 had no row).
    rows = Counter(int(n) for n in re.findall(r'^\| (\d+) \|', text, flags=re.M))
    for d in ctx['domains']:
        n = int(d[:2])
        if rows[n] != 1:
            rep.error('readme-domain-table', f'domain {n} has {rows[n]} rows in the README domain table, expected 1')


# ---------------------------------------------------------------------------------------------- driver

# Order matters: a check reads the ctx keys earlier checks write (reg, latest_round, rejected, candidates,
# upstream_map) by subscript, so a reordering crashes as check-crashed instead of checking against nothing.
CHECKS = [check_files, check_layout, check_registry, check_index, check_log, check_log_history, check_rejected,
          check_manifest, check_extracted, check_candidates, check_upstream_map, check_references, check_readme]


def run(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--strict', action='store_true', help='exit 1 on warnings too')
    ap.add_argument('--verbose', action='store_true', help='print how many items each check examined')
    ap.add_argument('--upstream', action='store_true', help='check cited commits in the sibling upstream clones')
    args = ap.parse_args(argv)

    rep = Report()
    # reg and rejected feed the summary line, so they exist even if the checks that fill them crash.
    ctx = {'domains': domain_dirs(), 'reg': {}, 'rejected': {}, 'upstream_heads': {}, 'unread_domains': set()}
    rep.start('setup')
    try:
        ctx['files'] = repo_files()
        ctx['ignored'] = ignored_files()
    except DataError as e:
        # Every check reads the file list. Run on an empty one, they would report every file missing; none runs.
        rep.error(e.code, f'{e} — no check can run without the list of repository files, so none ran')
        checks = []
    else:
        checks = CHECKS + ([check_upstream] if args.upstream else [])
    for check in checks:
        try:
            check(rep, ctx)
        except DataError as e:
            rep.error(e.code, f'{e} — {check.__name__} stopped here, so its remaining checks did not run')
        except Exception:
            rep.error('check-crashed', f'{check.__name__} raised, so its remaining checks did not run:\n'
                                       + traceback.format_exc().rstrip())
    for line in rep.lines:
        print(line)
    if args.verbose:
        for section, counts in rep.counts.items():
            print(f'checked [{section}] ' + ', '.join(f'{n} {what}' for what, n in counts.items()))
        if ctx['upstream_heads']:
            print('compared with origin/main ' + ', '.join(f'{n}@{s}' for n, s in sorted(ctx['upstream_heads'].items()))
                  + ' (fetch the clones first if these are old)')
    reg = ctx['reg']
    tiers = Counter(r['tier'] for r in reg.values())
    pending = sum(access_class(r['access_status']) in PENDING_ACCESS for r in reg.values())
    print(f'{len(reg)} sources ({", ".join(f"{t}x{tiers[t]}" for t in sorted(tiers))}) in {len(ctx["domains"])} domains, '
          f'{pending} registered but not yet pulled, {len(ctx["rejected"])} rejected — {rep.errors} error(s), '
          f'{rep.warnings} warning(s); upstream checks {"run" if args.upstream else "not run (pass --upstream)"}')
    return 1 if rep.errors or (args.strict and rep.warnings) else 0


def main():
    # The messages hold non-ASCII ("—"); a cp1252 console would raise partway through the report.
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
    sys.exit(run())


if __name__ == '__main__':
    main()
