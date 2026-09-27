"""Check that the registry, INDEX.md, the manifest and the data files agree.

    python tools/validate.py

Exits 1 if any ERROR is reported; WARN lines do not fail the run. Run it
before every commit — each check below exists because that failure has
happened in a past round.
"""
import re
import sys
from collections import Counter, defaultdict

from common import (ACCESS_CLASSES, CANDIDATE_COLS, CANDIDATE_KINDS, CANDIDATE_STATUSES, CANDIDATES,
                    DOMAIN_COLS, INDEX, LICENSE_CLASSES, MANIFEST, MANIFEST_COLS, NOT_REDISTRIBUTABLE, PENDING_ACCESS, README,
                    REGISTRY, REGISTRY_COLS, ROOT, TIERS, access_class, aggregate_rows, domain_dirs, file_digest,
                    read_csv, read_dicts)

INDEX_HEADER = ['id', 'tier', 'source (short)', 'access', 'backs / could replace']
ACCESS_WORDS = re.compile(r'(full[_ ]text[_ ]hosted|open[_ ]not[_ ]pulled|verified[_ ]live|open[_ ]service|'
                          r'public[_ ]domain[_ ]excerpt|registered[_ ]not[_ ]pulled|skipped)\b', re.I)
GITHUB_HARD_LIMIT = 100 * 1024 * 1024
GITHUB_WARN_LIMIT = 50 * 1024 * 1024


class Report:
    def __init__(self):
        self.lines = []
        self.errors = 0
        self.warnings = 0
        self.section = ''

    def start(self, name):
        self.section = name

    def error(self, msg):
        self.errors += 1
        self.lines.append(f'ERROR [{self.section}] {msg}')

    def warn(self, msg):
        self.warnings += 1
        self.lines.append(f'WARN  [{self.section}] {msg}')


def check_registry(rep):
    rep.start('registry')
    domains = domain_dirs()
    for d in domains:
        # full_texts/ and extracted_data/ are optional: git does not keep empty folders.
        for part in ('sources_domain.csv', 'FINDINGS.md'):
            if not (ROOT / d / part).exists():
                rep.error(f'{d}/{part} is missing')
        header, rows = read_csv(ROOT / d / 'sources_domain.csv')
        if header != DOMAIN_COLS:
            rep.error(f'{d}/sources_domain.csv header is {header}, expected {DOMAIN_COLS}')
        if any(not r for r in rows):
            rep.error(f'{d}/sources_domain.csv has blank lines')

    header, rows = read_csv(REGISTRY)
    if header != REGISTRY_COLS:
        rep.error(f'sources.csv header is {header}, expected {REGISTRY_COLS}')
    if rows != aggregate_rows():
        rep.error('sources.csv does not match the per-domain CSVs — run: python tools/build_registry.py')

    reg = {}
    for r in read_dicts(REGISTRY):
        sid = r['id']
        if sid in reg:
            rep.error(f'duplicate id {sid} ({reg[sid]["domain_dir"]} and {r["domain_dir"]})')
        reg[sid] = r
        if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', sid):
            rep.error(f'{sid}: id must be lowercase letters, digits, underscores and hyphens')
        if r['tier'] not in TIERS:
            rep.error(f'{sid}: tier {r["tier"]!r} is not one of {sorted(TIERS)}')
        cls = access_class(r['access_status'])
        if cls not in ACCESS_CLASSES:
            rep.error(f'{sid}: access_status starts with {cls!r}; allowed: {sorted(ACCESS_CLASSES)}')
        if r['domain_dir'] not in domains:
            rep.error(f'{sid}: domain_dir {r["domain_dir"]!r} does not exist')
    return reg


def table_cells(line):
    inner = line.strip()[1:-1]
    return [c.strip() for c in re.split(r'(?<!\\)\|', inner)]


def check_index(rep, reg):
    rep.start('INDEX.md')
    text = INDEX.read_text(encoding='utf-8')
    sections = re.split(r'^## ', text, flags=re.M)
    seen = set()
    for sec in sections[1:]:
        m = re.match(r'Domain (\d+)\b', sec)
        if not m:
            continue
        num = int(m.group(1))
        matches = [d for d in domain_dirs() if d.startswith(f'{num:02d}_')]
        if not matches:
            rep.error(f'"## Domain {num}" has no matching directory')
            continue
        d = matches[0]
        seen.add(d)
        lines = sec.split('\n')
        table = [i for i, l in enumerate(lines) if l.startswith('|')]
        if not table:
            rep.error(f'Domain {num}: no source table')
            continue
        if table != list(range(table[0], table[0] + len(table))):
            rep.error(f'Domain {num}: table is split by a blank line or text — rows after the break do not render as table rows')
        # A header narrower than the rows makes GitHub drop the extra cells, so check the full header.
        if table_cells(lines[table[0]]) != INDEX_HEADER:
            rep.error(f'Domain {num}: table header must be "| {" | ".join(INDEX_HEADER)} |"')
        if len(table) < 2 or table_cells(lines[table[1]]) != ['---'] * len(INDEX_HEADER):
            rep.error(f'Domain {num}: second table line must be the 5-column "|---|...|" separator')
        ids = []
        for i in table[2:]:
            line = lines[i]
            cells = table_cells(line)
            if not line.rstrip().endswith('|') or len(cells) != 5:
                rep.error(f'Domain {num}: row "{line[:50]}..." has {len(cells)} cells, expected 5 (and a closing "|")')
            sid = cells[0]
            ids.append(sid)
            if sid not in reg:
                rep.error(f'Domain {num}: id {sid!r} is not in sources.csv')
            elif reg[sid]['domain_dir'] != d:
                rep.error(f'Domain {num}: {sid} is registered under {reg[sid]["domain_dir"]}')
            elif len(cells) > 1 and cells[1] != reg[sid]['tier']:
                rep.error(f'Domain {num}: {sid} tier {cells[1]} here vs {reg[sid]["tier"]} in sources.csv')
            if len(cells) == 5 and sid in reg:
                # R26-R27 wrote three rows as id | tier | source | venue | access; the cell count still matched.
                if ACCESS_WORDS.match(cells[4]):
                    rep.error(f'Domain {num}: {sid} has its access in the last cell — order is {" | ".join(INDEX_HEADER)}')
                hosted = access_class(reg[sid]['access_status']) == 'full_text_hosted'
                says_hosted = 'hosted' in cells[3].lower() and 'not hosted' not in cells[3].lower()
                if hosted != says_hosted:
                    rep.error(f'Domain {num}: {sid} access cell "{cells[3][:40]}" disagrees with access_status '
                              f'{access_class(reg[sid]["access_status"])!r}')
        expected = [sid for sid, r in reg.items() if r['domain_dir'] == d]
        missing = [s for s in expected if s not in ids]
        if missing:
            rep.error(f'Domain {num}: registered but not listed: {", ".join(missing)}')
        dups = [s for s, n in Counter(ids).items() if n > 1]
        if dups:
            rep.error(f'Domain {num}: listed twice: {", ".join(dups)}')
        if not missing and not dups and set(ids) <= set(expected) and ids != expected:
            rep.error(f'Domain {num}: rows are not in sources_domain.csv order')
    for d in domain_dirs():
        if d not in seen:
            rep.error(f'no "## Domain {int(d[:2])}" section for {d}')
    check_log(rep, text)


def check_log(rep, text):
    rep.start('research log')
    if '\n## Research log\n' not in text:
        rep.error('INDEX.md has no "## Research log" section')
        return
    log = text.split('\n## Research log\n', 1)[1]
    if re.search(r'^## ', log, flags=re.M):
        rep.error('"## Research log" must be the last section of INDEX.md')
    # A multi-day round may write its date as 2026-09-17/18; ordering uses the start date.
    entry_re = re.compile(r'- \*\*(?:Round (\d+)|Maintenance)\*\* \((\d{4}-\d{2}-\d{2})(?:/\d{2})?\)')
    rounds, dates, started = [], [], False
    lines = log.rstrip('\n').split('\n')
    for n, line in enumerate(lines, 1):
        m = entry_re.match(line)
        if m:
            started = True
            if m.group(1) is not None:
                rounds.append(int(m.group(1)))
            dates.append(m.group(2))
        elif line.startswith('- **'):
            rep.error(f'log line {n}: entry must start "- **Round N** (YYYY-MM-DD)" or "- **Maintenance** (YYYY-MM-DD)"')
        elif started and not line.strip():
            rep.error(f'log line {n}: blank line inside the log — keep entries contiguous')
    if not rounds:
        rep.error('no "- **Round N**" entries found')
        return
    if rounds != sorted(rounds, reverse=True):
        rep.error('rounds are not newest-first')
    missing = sorted(set(range(max(rounds) + 1)) - set(rounds))
    if missing:
        rep.error(f'rounds missing from the log: {missing} — an INDEX.md rewrite may have dropped them (recover with git show <sha>:INDEX.md)')
    dups = [r for r, c in Counter(rounds).items() if c > 1]
    if dups:
        rep.error(f'rounds logged twice: {dups}')
    if dates != sorted(dates, reverse=True):
        rep.error('entry dates are not newest-first')


def check_manifest(rep, reg):
    rep.start('manifest')
    if not MANIFEST.exists():
        rep.error(f'{MANIFEST.name} is missing')
        return
    header, rows = read_csv(MANIFEST)
    if header != MANIFEST_COLS:
        rep.error(f'header is {header}, expected {MANIFEST_COLS}')
        return
    by_id = defaultdict(list)
    listed = set()
    restricted = []
    for row in rows:
        if len(row) != len(MANIFEST_COLS):
            rep.error(f'row {row[:3]} has {len(row)} cells')
            continue
        d, sid, fname, size, digest, license = row
        lic = license.split(' ', 1)[0]
        if lic not in LICENSE_CLASSES:
            rep.error(f'{fname}: license {lic!r} must start with one of {sorted(LICENSE_CLASSES)}')
        elif lic in NOT_REDISTRIBUTABLE:
            restricted.append(f'{sid} ({lic})')
        if (d, fname) in listed:
            rep.error(f'{d}/full_texts/{fname} listed twice')
        listed.add((d, fname))
        if sid not in reg:
            rep.error(f'{fname}: id {sid!r} is not in sources.csv')
        elif reg[sid]['domain_dir'] != d:
            rep.error(f'{fname}: {sid} is registered under {reg[sid]["domain_dir"]}, not {d}')
        path = ROOT / d / 'full_texts' / fname
        if not path.is_file():
            rep.error(f'{d}/full_texts/{fname} does not exist')
            continue
        actual_size, actual_digest = file_digest(path)
        if str(actual_size) != size or actual_digest != digest:
            rep.error(f'{fname}: bytes/sha256 differ from disk — run: python tools/build_registry.py')
        if actual_size > GITHUB_HARD_LIMIT:
            rep.error(f'{fname} is {actual_size / 2**20:.0f} MB — GitHub rejects files over 100 MB')
        elif actual_size > GITHUB_WARN_LIMIT:
            rep.warn(f'{fname} is {actual_size / 2**20:.0f} MB — GitHub warns above 50 MB')
        by_id[sid].append(actual_digest)
    # A warning, not an error: taking a file down is the owner's decision (README access rule 1).
    if restricted:
        rep.warn(f'{len(restricted)} hosted files have no licence that permits redistribution: {", ".join(restricted)}')

    for d in domain_dirs():
        folder = ROOT / d / 'full_texts'
        for f in sorted(p.name for p in folder.iterdir() if p.is_file()) if folder.exists() else []:
            if (d, f) not in listed:
                rep.error(f'{d}/full_texts/{f} is not in full_texts_manifest.csv')

    for sid, r in reg.items():
        hosted = access_class(r['access_status']) == 'full_text_hosted'
        if hosted and sid not in by_id:
            rep.error(f'{sid} is full_text_hosted but has no file in full_texts_manifest.csv')
        if not hosted and sid in by_id:
            rep.error(f'{sid} has a hosted file but access_status is {access_class(r["access_status"])!r}')
        for prefix in re.findall(r'sha256=([0-9a-f]{6,})', r['access_status']):
            if sid in by_id and not any(h.startswith(prefix) for h in by_id[sid]):
                rep.warn(f'{sid}: access_status records sha256={prefix}… which matches none of its hosted files')


def check_extracted(rep, reg):
    rep.start('extracted_data')
    # FINDINGS.md cites `extracted_data/<file>` relative to its own domain, so a root-level copy is unreachable.
    stray = ROOT / 'extracted_data'
    if stray.is_dir() and any(stray.iterdir()):
        rep.error('extracted_data/ at the repo root: move each file into <domain>/extracted_data/')
    no_source_col = []
    cited = defaultdict(str)  # domain -> text of its extracted CSVs, to find which ids they cite
    for d in domain_dirs():
        folder = ROOT / d / 'extracted_data'
        for path in sorted(folder.glob('*.csv')) if folder.exists() else []:
            name = f'{d}/extracted_data/{path.name}'
            try:
                header, rows = read_csv(path)
            except UnicodeDecodeError as e:
                rep.error(f'{name}: not UTF-8 ({e})')
                continue
            cited[d] += path.read_text(encoding='utf-8-sig')
            if header and 'source_id' not in header:
                no_source_col.append(name)
            if not header:
                rep.error(f'{name}: empty file')
                continue
            for n, row in enumerate(rows, 2):
                if row == header:
                    rep.error(f'{name} line {n}: repeats the header line')
                elif row and len(row) != len(header):
                    rep.error(f'{name} line {n}: {len(row)} cells under a {len(header)}-column header (unquoted comma?)')
            rows = [r for r in rows if r != header]
            if 'source_id' in header:
                col = header.index('source_id')
                # A row derived from two sources lists both, joined by ';'.
                unknown = sorted({sid for row in rows if len(row) > col for sid in row[col].split(';')
                                  if sid and sid not in reg})
                if unknown:
                    rep.error(f'{name}: source_id not in sources.csv: {", ".join(unknown)}')
    # README "How an item earns a place" #3: numbers extracted into a CSV, or the row says context-only.
    # A registered_not_pulled row has not been read yet, so it cannot be either; it is counted in the summary instead.
    if no_source_col:
        rep.warn(f'{len(no_source_col)} CSVs have no source_id column, so their rows are not traceable to a '
                 f'registry id: {", ".join(no_source_col)}')
    uncovered = Counter(r['domain_dir'] for sid, r in reg.items()
                        if sid not in cited[r['domain_dir']]
                        and access_class(r['access_status']) not in PENDING_ACCESS
                        and not re.search(r'context[- ]only', r['access_status'] + r['pipeline_mapping'], re.I))
    if uncovered:
        rep.warn(f'{sum(uncovered.values())} sources are not cited by id in any extracted-data CSV of their domain '
                 f'and are not marked context-only: '
                 + ', '.join(f'{d[:2]}x{n}' for d, n in sorted(uncovered.items())))


def check_candidates(rep, reg):
    rep.start('revision_candidates')
    if not CANDIDATES.exists():
        rep.error(f'{CANDIDATES.name} is missing')
        return
    header, _ = read_csv(CANDIDATES)
    if header != CANDIDATE_COLS:
        rep.error(f'header is {header}, expected {CANDIDATE_COLS}')
        return
    seen = set()
    for r in read_dicts(CANDIDATES):
        cid = r['id']
        if not re.fullmatch(r'rc-\d{3}', cid) or cid in seen:
            rep.error(f'id {cid!r} must be unique and look like rc-001')
        seen.add(cid)
        if r['status'] not in CANDIDATE_STATUSES:
            rep.error(f'{cid}: status {r["status"]!r} not in {sorted(CANDIDATE_STATUSES)}')
        if r['kind'] not in CANDIDATE_KINDS:
            rep.error(f'{cid}: kind {r["kind"]!r} not in {sorted(CANDIDATE_KINDS)}')
        if r['domain_dir'] not in domain_dirs():
            rep.error(f'{cid}: domain_dir {r["domain_dir"]!r} does not exist')
        for sid in filter(None, r['source_ids'].split(';')):
            if sid not in reg:
                rep.error(f'{cid}: source id {sid!r} is not in sources.csv')
        if not re.fullmatch(r'R\d+', r['found_round']):
            rep.error(f'{cid}: found_round {r["found_round"]!r} should look like R12')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r['checked_date']):
            rep.error(f'{cid}: checked_date {r["checked_date"]!r} should be YYYY-MM-DD')
        if not r['target_repo'] or not r['target_file']:
            rep.error(f'{cid}: target_repo and target_file are required')


def check_line_endings(rep):
    rep.start('line endings')
    for path in sorted(ROOT.rglob('*')):
        if path.suffix not in ('.csv', '.md', '.py') or {'.git', 'full_texts'} & set(path.parts):
            continue
        if b'\r\r' in path.read_bytes():
            rep.error(f'{path.relative_to(ROOT).as_posix()}: doubled carriage returns — git treats the file as binary '
                      f'and shows no diffs; write CSVs with csv.writer on a file opened with newline=""')


def check_readme(rep):
    rep.start('README.md')
    text = README.read_text(encoding='utf-8')
    for d in domain_dirs():
        if d not in text:
            rep.error(f'{d} is not mentioned in README.md (layout section is stale)')


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    rep = Report()
    reg = check_registry(rep)
    check_index(rep, reg)
    check_manifest(rep, reg)
    check_extracted(rep, reg)
    check_candidates(rep, reg)
    check_line_endings(rep)
    check_readme(rep)
    for line in rep.lines:
        print(line)
    tiers = Counter(r['tier'] for r in reg.values())
    pending = sum(access_class(r['access_status']) in PENDING_ACCESS for r in reg.values())
    print(f'{len(reg)} sources ({", ".join(f"{t}x{tiers[t]}" for t in sorted(tiers))}) in {len(domain_dirs())} domains, '
          f'{pending} registered but not yet pulled — {rep.errors} error(s), {rep.warnings} warning(s)')
    sys.exit(1 if rep.errors else 0)


if __name__ == '__main__':
    main()
