"""Check that the registry, INDEX.md, the manifest and the data files agree.

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
  other checks still run;
- each check counts what it examined, and one that examined nothing reports
  `nothing-checked`, because a check with no input passes vacuously;
- the summary line says whether the --upstream checks ran.
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
                    DOMAIN_RE, INDEX, LICENSE_CLASSES, LIVE_CANDIDATE_STATUSES, MANIFEST, MANIFEST_COLS,
                    NOT_REDISTRIBUTABLE, PENDING_ACCESS, README, REGISTRY, REGISTRY_COLS, ROOT, TIERS, UPSTREAM_MAP,
                    UPSTREAM_MAP_COLS, UPSTREAM_REPOS, DataError, access_class, domain_dirs, file_digest, read_csv,
                    read_domain_csv, read_text, rel, repo_files)

INDEX_HEADER = ['id', 'tier', 'source (short)', 'access', 'backs / could replace']
REJECTED_HEADER = ['id', 'source', 'link', 'reason']
ACCESS_WORDS = re.compile(r'(full[_ ]text[_ ]hosted|open[_ ]not[_ ]pulled|verified[_ ]live|open[_ ]service|'
                          r'public[_ ]domain[_ ]excerpt|registered[_ ]not[_ ]pulled|skipped)\b', re.I)
GITHUB_HARD_LIMIT = 100 * 1024 * 1024
GITHUB_WARN_LIMIT = 50 * 1024 * 1024
# Root-level files and directories, each with a line in README "Layout" unless marked False.
ROOT_FILES = {'README.md': True, 'INDEX.md': True, 'sources.csv': True, 'full_texts_manifest.csv': True,
              'revision_candidates.csv': True, 'upstream_commit_map.csv': True, 'DOWNLOADS.md': True,
              'AGENTS.md': True, 'CLAUDE.md': False, 'LICENSE': False, '.gitignore': False}
REQUIRED_ROOT_FILES = ['README.md', 'INDEX.md', 'sources.csv', 'full_texts_manifest.csv', 'revision_candidates.csv',
                       'upstream_commit_map.csv', 'AGENTS.md']
ROOT_DIRS = {'tools'}
DOMAIN_FILES = {'sources_domain.csv', 'FINDINGS.md', '.gitkeep'}
EXTRACTED_SUFFIXES = {'.csv', '.json'}
TEXT_SUFFIXES = {'.csv', '.md', '.py', '.json'}
# A year cell starts with a year, an approximate year or "n.d.", and may explain itself after that.
YEAR_RE = re.compile(r'(~?\d{4}|n\.d\.)')
LOG_ENTRY_RE = re.compile(r'- \*\*(?:Round (\d+)|Maintenance)\*\* \((\d{4}-\d{2}-\d{2})(?:/\d{2})?\)')
# Entry labels in a form other than "- **Round N**": AGENTS.md bans "**RN**" and "### RN".
LOG_MISLABEL_RE = re.compile(r'\s*(#{1,6}\s|\*\*R(?:ound)?\s*\d|- \*\*R\d)')
SHA_RE = re.compile(r'[0-9a-f]{7,40}')


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


def table_cells(line):
    inner = line.strip()[1:-1]
    return [c.strip() for c in re.split(r'(?<!\\)\|', inner)]


# ---------------------------------------------------------------------------------------------- files and layout

def check_files(rep, ctx):
    """Every text file: UTF-8, no BOM, no stray carriage returns, ends with a newline."""
    rep.start('text files')
    for name in ctx['files']:
        parts = name.split('/')
        if 'full_texts' in parts or not any(name.endswith(s) for s in TEXT_SUFFIXES):
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
    for f in REQUIRED_ROOT_FILES:
        if f not in files:
            rep.error('root-file-missing', f'{f} is missing')

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
                continue
            sid = cells[0]
            ids.append(sid)
            if any(not c for c in cells):
                rep.error('index-empty-cell', f'Domain {num}: {sid or line[:50]} has an empty cell')
            if sid not in reg:
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
    text = read_text(INDEX)
    ctx['latest_round'] = None
    if '\n## Research log\n' not in text:
        rep.error('log-missing', 'INDEX.md has no "## Research log" section')
        return
    log = text.split('\n## Research log\n', 1)[1]
    if re.search(r'^## ', log, flags=re.M):
        rep.error('log-not-last', '"## Research log" must be the last section of INDEX.md')
    rounds, dates, started = [], [], False
    today = datetime.date.today()
    for n, line in enumerate(log.rstrip('\n').split('\n'), 1):
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
                                         f'not headings or bare bold labels')
        elif not line.strip():
            if started:
                rep.error('log-blank-line', f'log line {n}: blank line inside the log — keep entries contiguous')
        elif not started:
            rep.error('log-preamble', f'log line {n}: text before the first entry')
    rep.expect('log entries')
    if not rounds:
        rep.error('log-no-rounds', 'no "- **Round N**" entries found')
        return
    ctx['latest_round'] = max(rounds)
    if rounds != sorted(rounds, reverse=True):
        rep.error('log-order', 'rounds are not newest-first')
    missing = sorted(set(range(max(rounds) + 1)) - set(rounds))
    if missing:
        rep.error('log-gap', f'rounds missing from the log: {missing} — an INDEX.md rewrite may have dropped them '
                             f'(recover with git show <sha>:INDEX.md)')
    dups = sorted(r for r, c in Counter(rounds).items() if c > 1)
    if dups:
        rep.error('log-duplicate', f'rounds logged twice: {dups}')
    if dates != sorted(dates, reverse=True):
        rep.error('log-date-order', 'entry dates are not newest-first')


def check_rejected(rep, ctx):
    """README "Rejecting a source": the INDEX.md table is a rejected source's only record outside the research log."""
    rep.start('rejected sources')
    reg = ctx['reg']
    ctx['rejected'] = {}
    text = read_text(INDEX)
    m = re.search(r'^## Rejected sources\n(.*?)(?=^## |\Z)', text, flags=re.M | re.S)
    if not m:
        rep.error('rejected-missing', 'INDEX.md has no "## Rejected sources" section (it goes directly above "## Research log")')
        return
    if not text[m.end():].startswith('## Research log\n'):
        rep.error('rejected-position', '"## Rejected sources" must be directly above "## Research log"')
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
    before_log = text[:m.start()] + re.split(r'^## Research log\n', text[m.end():], maxsplit=1, flags=re.M)[0]
    for name in ctx['files']:
        rep.count('files scanned for rejected ids')
        hits = set(token.findall(name))
        path = ROOT / name
        if path == INDEX:
            hits |= set(token.findall(before_log))
        elif any(name.endswith(s) for s in ('.csv', '.md', '.json')):
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
        if sid not in reg:
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
    no_source_col = []
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
        for n, row in enumerate(rows, 2):
            if row == header:
                rep.error('extracted-header-repeat', f'{name} line {n}: repeats the header line')
        if 'source_id' not in header:
            no_source_col.append(name)
            continue
        col = header.index('source_id')
        # A row derived from two sources lists both, joined by ';'.
        unknown = sorted({sid for row in rows if row != header for sid in row[col].split(';') if sid and sid not in reg})
        if unknown:
            rep.error('extracted-unknown-source', f'{name}: source_id not in sources.csv: {", ".join(unknown)}')
    rep.expect('extracted files')
    if no_source_col:
        rep.warn('extracted-no-source-col', f'{len(no_source_col)} CSVs have no source_id column, so their rows are not '
                                            f'traceable to a registry id: {", ".join(no_source_col)}')
    # README "How an item earns a place" #3: numbers extracted into a CSV, or the row says context-only.
    # A registered_not_pulled row has not been read yet, so it cannot be either; it is counted in the summary instead.
    uncovered = Counter(r['domain_dir'] for sid, r in reg.items()
                        if sid not in cited[r['domain_dir']]
                        and access_class(r['access_status']) not in PENDING_ACCESS
                        and not re.search(r'context[- ]only', r['access_status'] + r['pipeline_mapping'], re.I))
    if uncovered:
        rep.warn('source-uncited', f'{sum(uncovered.values())} sources are not cited by id in any extracted-data file of '
                                   f'their domain and are not marked context-only: '
                                   + ', '.join(f'{d[:2]}x{n}' for d, n in sorted(uncovered.items())))


# ---------------------------------------------------------------------------------------------- candidates

def check_candidates(rep, ctx):
    rep.start('revision_candidates')
    reg = ctx['reg']
    ctx['candidates'] = []
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
        for sid in filter(None, r['source_ids'].split(';')):
            if sid not in reg:
                rep.error('cand-source-unknown', f'{cid}: source id {sid!r} is not in sources.csv')
        fr = re.fullmatch(r'R(\d+)', r['found_round'])
        if not fr:
            rep.error('cand-found-round', f'{cid}: found_round {r["found_round"]!r} should look like R12')
        elif ctx.get('latest_round') is not None and int(fr.group(1)) > ctx['latest_round']:
            rep.error('cand-found-round-future', f'{cid}: found_round {r["found_round"]} is after the latest logged '
                                                 f'round, R{ctx["latest_round"]}')
        date = parse_date(r['checked_date']) if re.fullmatch(r'\d{4}-\d{2}-\d{2}', r['checked_date']) else None
        if date is None:
            rep.error('cand-date', f'{cid}: checked_date {r["checked_date"]!r} should be a YYYY-MM-DD date')
        elif date > today:
            rep.error('cand-date-future', f'{cid}: checked_date {r["checked_date"]} is after today ({today})')
        if r['target_repo'] not in UPSTREAM_REPOS:
            rep.error('cand-target-repo', f'{cid}: target_repo {r["target_repo"]!r} not in {sorted(UPSTREAM_REPOS)}')
        ca = r['checked_against'].split('@')
        if len(ca) != 2 or ca[0] not in UPSTREAM_REPOS or not SHA_RE.fullmatch(ca[1]):
            rep.error('cand-checked-against', f'{cid}: checked_against {r["checked_against"]!r} must be <repo>@<sha> with '
                                              f'repo in {sorted(UPSTREAM_REPOS)}')
    rep.expect('candidates')


def check_upstream_map(rep, ctx):
    rep.start('upstream_commit_map')
    ctx['upstream_map'] = []
    try:
        header, rows = read_csv(UPSTREAM_MAP)
    except DataError as e:
        rep.error(e.code, f'{e} — no commit map checks ran')
        return
    if header != UPSTREAM_MAP_COLS:
        rep.error('map-header', f'header is {header}, expected {UPSTREAM_MAP_COLS}')
        return
    by_ref = defaultdict(list)
    for c in ctx.get('candidates', []):
        by_ref[c['checked_against']].append(c['id'])
    seen = set()
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
        listed = sorted(filter(None, r['checked_against_in'].split(';')))
        if listed != sorted(by_ref.get(ref, [])):
            rep.error('map-cited-mismatch', f'{ref}: checked_against_in lists {listed}, but the candidates citing it are '
                                            f'{sorted(by_ref.get(ref, []))}')


def git(repo, *args):
    proc = subprocess.run(['git', '-C', str(repo)] + list(args), capture_output=True)
    return proc.returncode, proc.stdout.decode('utf-8', 'backslashreplace').strip()


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
    mapped = {f'{r["repo"]}@{r["old_sha"]}': r for r in ctx.get('upstream_map', [])}
    for r in ctx.get('upstream_map', []):
        path = repos.get(r['repo'])
        if path is None:
            continue
        rep.count('commits checked')
        rc1, old_tree = git(path, 'rev-parse', '--verify', f'{r["old_sha"]}^{{tree}}')
        rc2, new_tree = git(path, 'rev-parse', '--verify', f'{r["main_sha"]}^{{tree}}')
        rc3, _ = git(path, 'merge-base', '--is-ancestor', r['main_sha'], 'origin/main')
        if rc1 or rc2 or rc3 or old_tree != new_tree:
            rep.error('map-not-equivalent', f'{r["repo"]}@{r["old_sha"]} -> {r["main_sha"]}: both must exist, the second '
                                            f'must be on origin/main, and their trees must be identical')
    for c in ctx.get('candidates', []):
        ref = c['checked_against']
        name, _, sha = ref.partition('@')
        path = repos.get(name)
        if path is None:
            continue
        rep.count('commits checked')
        if git(path, 'cat-file', '-e', f'{sha}^{{commit}}')[0] != 0:
            rep.error('upstream-sha-unknown', f'{c["id"]}: {ref} is not a commit in {path}')
            continue
        if git(path, 'merge-base', '--is-ancestor', sha, 'origin/main')[0] == 0:
            continue
        if c['status'] in LIVE_CANDIDATE_STATUSES:
            rep.error('upstream-open-off-main', f'{c["id"]} is {c["status"]} but {ref} is not on {name} origin/main; '
                                                f're-check the cell against main and update checked_against')
        elif ref not in mapped:
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

CHECKS = [check_files, check_layout, check_registry, check_index, check_log, check_rejected, check_manifest,
          check_extracted, check_candidates, check_upstream_map, check_readme]


def run(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--strict', action='store_true', help='exit 1 on warnings too')
    ap.add_argument('--verbose', action='store_true', help='print how many items each check examined')
    ap.add_argument('--upstream', action='store_true', help='check cited commits in the sibling upstream clones')
    args = ap.parse_args(argv)

    rep = Report()
    ctx = {'domains': domain_dirs(), 'reg': {}, 'rejected': {}}
    rep.start('setup')
    try:
        ctx['files'] = repo_files()
    except DataError as e:
        rep.error(e.code, str(e))
        ctx['files'] = []
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
    reg = ctx['reg']
    tiers = Counter(r['tier'] for r in reg.values())
    pending = sum(access_class(r['access_status']) in PENDING_ACCESS for r in reg.values())
    print(f'{len(reg)} sources ({", ".join(f"{t}x{tiers[t]}" for t in sorted(tiers))}) in {len(ctx["domains"])} domains, '
          f'{pending} registered but not yet pulled, {len(ctx["rejected"])} rejected — {rep.errors} error(s), '
          f'{rep.warnings} warning(s); upstream checks {"run" if args.upstream else "not run (pass --upstream)"}')
    return 1 if rep.errors or (args.strict and rep.warnings) else 0


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
    sys.exit(run())


if __name__ == '__main__':
    main()
