"""Shared paths, schemas and strict file readers for the registry tools.

Standard library only (Python 3.8+); run the tools from anywhere — paths
resolve from this file's location.

The readers here are strict. A file that is not UTF-8 or starts with a
byte-order mark, a CSV with a blank line, bad quoting or a row whose width
differs from its header, raises DataError naming the file, the line and a
code. Nothing is skipped, padded or decoded with replacement characters: a bad
file is reported, never read around.
"""
import csv
import hashlib
import io
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN_RE = re.compile(r'(\d\d)_[a-z0-9_]+')
DOMAIN_COLS = ['id', 'tier', 'short_title', 'journal_or_series', 'year', 'doi_or_url',
               'authors_short', 'access_status', 'pipeline_mapping']
REGISTRY_COLS = ['domain_dir'] + DOMAIN_COLS
MANIFEST_COLS = ['domain_dir', 'id', 'file', 'bytes', 'sha256', 'license']
CANDIDATE_COLS = ['id', 'status', 'kind', 'domain_dir', 'source_ids', 'found_round', 'target_repo',
                  'target_file', 'target_row', 'field', 'current_value', 'proposed', 'evidence',
                  'checked_against', 'checked_date']
# R152: upstream histories were rewritten, so commits that checked_against cites are mapped to their main equivalents.
UPSTREAM_MAP_COLS = ['repo', 'old_sha', 'main_sha', 'tree', 'subject', 'checked_against_in']
# The repos this registry anchors. They are read-only from here (AGENTS.md); `validate.py --upstream` reads the
# sibling clones next to this repo.
UPSTREAM_REPOS = {'AsteroidCatalog', 'spacecost', 'economicspace'}

# T4 (R74): secondary / grey sources the upstream rows cite: company documents and price pages, news, encyclopedias,
# vendor or market-research posts, textbooks, software, market-data APIs.
TIERS = {'T1', 'T2', 'T3', 'T4'}
# First token of access_status. `full_text_hosted` requires a manifest entry.
ACCESS_CLASSES = {
    'full_text_hosted',              # full text committed under <domain>/full_texts/
    'public_domain_excerpt_hosted',  # public-domain passage quoted in FINDINGS.md, PDF linked
    'verified_live_not_pulled',      # fetched and read from this machine, not committed
    'open_not_pulled',               # open access, but blocked here or licence forbids hosting
    'open_service',                  # live database / API, verified from this machine
    'skipped',                       # deliberately not hosted (user decision recorded)
    'registered_not_pulled',         # upstream citation registered; metadata or landing page checked, full text not sought
}
# Rows still waiting for a first pull; exempt from the "no extracted-data CSV cites it" warning until re-classed.
PENDING_ACCESS = {'registered_not_pulled'}
# First token of a manifest `license`; the rest says where it was read (PDF page, NTRS record, arXiv abs page).
LICENSE_CLASSES = {
    'public-domain',               # US government work, NASA PDS archive data
    'ntrs-public-use',             # NTRS determinationType PUBLIC_USE_PERMITTED / GOV_PUBLIC_USE_PERMITTED / GOV_PERMITTED
    'cc-by', 'cc-by-sa', 'cc-by-nc', 'cc-by-nc-sa',
    # None of these grants redistribution, so README access rule 1 is not met while the file stays hosted:
    'arxiv-nonexclusive',          # arXiv's default licence grants arXiv, not third parties, the right to distribute
    'ntrs-may-include-copyright',  # NTRS determinationType MAY_INCLUDE_COPYRIGHT_MATERIAL
    'copyright',                   # publisher / institution copyright, no licence granted
    'unknown',                     # no licence statement found
}
NOT_REDISTRIBUTABLE = {'arxiv-nonexclusive', 'ntrs-may-include-copyright', 'copyright', 'unknown'}
# withdrawn = this repo's own evidence turned out wrong (distinct from declined, which is the upstream owner's call).
CANDIDATE_STATUSES = {'open', 'applied', 'declined', 'superseded', 'blocked', 'withdrawn'}
# Statuses whose checked_against must be re-read against upstream main, not left on an old commit.
LIVE_CANDIDATE_STATUSES = {'open', 'blocked'}
CANDIDATE_KINDS = {'value', 'citation', 'wording', 'range', 'method'}

REGISTRY = ROOT / 'sources.csv'
MANIFEST = ROOT / 'full_texts_manifest.csv'
CANDIDATES = ROOT / 'revision_candidates.csv'
UPSTREAM_MAP = ROOT / 'upstream_commit_map.csv'
INDEX = ROOT / 'INDEX.md'
README = ROOT / 'README.md'

BOM = b'\xef\xbb\xbf'


class DataError(Exception):
    """A file that cannot be read as the tools require. `code` names the defect for reports and tests."""

    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def rel(path):
    """The path relative to ROOT. Every path the tools report is inside the repo; one outside it is a bug and raises."""
    return Path(path).relative_to(ROOT).as_posix()


def domain_dirs():
    """Domain directories in order: 01_..., 02_..., ..."""
    return sorted(p.name for p in ROOT.iterdir() if p.is_dir() and DOMAIN_RE.fullmatch(p.name))


def _ls_files(*flags):
    try:
        proc = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-z', *flags], capture_output=True)
    except OSError as e:
        raise DataError('git-ls-files', f'cannot run git to list the repository files: {e}')
    if proc.returncode != 0:
        raise DataError('git-ls-files', f'git ls-files failed in {ROOT}: {proc.stderr.decode("utf-8", "backslashreplace").strip()}')
    names = proc.stdout.decode('utf-8').split('\0')
    # --cached also lists tracked files deleted from the working tree; those are git status's business, not content.
    return sorted(n for n in names if n and (ROOT / n).is_file())


def repo_files():
    """Every file git tracks or would track (untracked but not ignored), as POSIX paths relative to ROOT.

    Raises DataError if git cannot list them: a scan with no file list would check nothing and pass.
    """
    return _ls_files('--cached', '--others', '--exclude-standard')


def ignored_files():
    """Untracked files that .gitignore hides. No check reads them, so validate.py reports any outside __pycache__/."""
    return _ls_files('--others', '--ignored', '--exclude-standard')


def read_text(path):
    """The file's text, which must be UTF-8 with no byte-order mark, with CRLF line ends read as LF.

    The working tree is CRLF on Windows (core.autocrlf) and LF elsewhere; the checks parse either the same way.
    Byte-level defects (doubled or lone carriage returns) are checked on the raw bytes by validate.check_files.
    """
    path = Path(path)
    if not path.is_file():
        raise DataError('file-missing', f'{rel(path)} does not exist')
    data = path.read_bytes()
    if data.startswith(BOM):
        raise DataError('text-bom', f'{rel(path)}: starts with a UTF-8 byte-order mark; remove the first three bytes')
    try:
        return data.decode('utf-8').replace('\r\n', '\n')
    except UnicodeDecodeError as e:
        raise DataError('text-not-utf8', f'{rel(path)}: not UTF-8 ({e})')


def read_csv(path):
    """(header, rows-as-lists). Raises DataError on an empty file, a blank line, bad quoting or a ragged row."""
    text = read_text(path)
    reader = csv.reader(io.StringIO(text, newline=''), strict=True)
    rows = []
    try:
        for row in reader:
            if not row:
                raise DataError('csv-blank-line', f'{rel(path)} line {reader.line_num}: blank line')
            rows.append((reader.line_num, row))
    except csv.Error as e:
        raise DataError('csv-quoting', f'{rel(path)} line {reader.line_num}: {e}')
    if not rows:
        raise DataError('csv-empty', f'{rel(path)}: empty file, no header line')
    header = rows[0][1]
    for line, row in rows[1:]:
        if len(row) != len(header):
            raise DataError('csv-width', f'{rel(path)} line {line}: {len(row)} cells under a {len(header)}-column header '
                                         f'(an unquoted comma, or a cell lost)')
    return header, [row for _, row in rows[1:]]


def read_domain_csv(domain):
    """Rows of <domain>/sources_domain.csv as lists in DOMAIN_COLS order; the header must be exactly DOMAIN_COLS."""
    path = ROOT / domain / 'sources_domain.csv'
    header, rows = read_csv(path)
    if header != DOMAIN_COLS:
        raise DataError('domain-header', f'{rel(path)}: header is {header}, expected {DOMAIN_COLS}')
    return rows


def line_terminator(path):
    """Keep whatever the file already uses so a rewrite does not churn line endings; a new file gets LF,
    which git stores either way."""
    return '\r\n' if path.exists() and b'\r\n' in path.read_bytes() else '\n'


def to_csv_text(header, rows, lineterminator='\n'):
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator=lineterminator)
    writer.writerow(header)
    writer.writerows(rows)
    return buf.getvalue()


def plain_file_name(name):
    """A bare file name: no directory part, not "." or "..", no leading or trailing whitespace. A manifest `file` that
    is not one points outside its domain's full_texts/ or at a subdirectory no check lists."""
    return bool(name) and name == name.strip() and not re.search(r'[/\\]', name) and name not in ('.', '..')


def access_class(access_status):
    return re.split(r'[\s(]', access_status.strip(), maxsplit=1)[0]


def file_digest(path):
    h = hashlib.sha256()
    size = 0
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
            size += len(chunk)
    return size, h.hexdigest()
