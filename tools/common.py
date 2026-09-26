"""Shared paths, schemas and CSV helpers for the registry tools.

Standard library only; run the tools from anywhere — paths resolve from
this file's location.
"""
import csv
import hashlib
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN_COLS = ['id', 'tier', 'short_title', 'journal_or_series', 'year', 'doi_or_url',
               'authors_short', 'access_status', 'pipeline_mapping']
REGISTRY_COLS = ['domain_dir'] + DOMAIN_COLS
MANIFEST_COLS = ['domain_dir', 'id', 'file', 'bytes', 'sha256']
CANDIDATE_COLS = ['id', 'status', 'kind', 'domain_dir', 'source_ids', 'found_round', 'target_repo',
                  'target_file', 'target_row', 'field', 'current_value', 'proposed', 'evidence',
                  'checked_against', 'checked_date']

TIERS = {'T1', 'T2', 'T3'}
# First token of access_status. `full_text_hosted` requires a manifest entry.
ACCESS_CLASSES = {
    'full_text_hosted',              # full text committed under <domain>/full_texts/
    'public_domain_excerpt_hosted',  # public-domain passage quoted in FINDINGS.md, PDF linked
    'verified_live_not_pulled',      # fetched and read from this machine, not committed
    'open_not_pulled',               # open access, but blocked here or licence forbids hosting
    'open_service',                  # live database / API, verified from this machine
    'skipped',                       # deliberately not hosted (user decision recorded)
}
CANDIDATE_STATUSES = {'open', 'applied', 'declined', 'superseded', 'blocked'}
CANDIDATE_KINDS = {'value', 'citation', 'wording', 'range', 'method'}

REGISTRY = ROOT / 'sources.csv'
MANIFEST = ROOT / 'full_texts_manifest.csv'
CANDIDATES = ROOT / 'revision_candidates.csv'
INDEX = ROOT / 'INDEX.md'
README = ROOT / 'README.md'


def domain_dirs():
    """Domain directories in order: 01_..., 02_..., ..."""
    return sorted(p.name for p in ROOT.iterdir() if p.is_dir() and re.fullmatch(r'\d\d_[a-z0-9_]+', p.name))


def read_csv(path):
    """(header, rows-as-lists) with the UTF-8 BOM stripped if present."""
    with open(path, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    return (rows[0] if rows else []), rows[1:]


def read_dicts(path):
    with open(path, encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def line_terminator(path):
    """Keep whatever the file already uses so a rewrite does not churn line endings."""
    return '\r\n' if path.exists() and b'\r\n' in path.read_bytes()[:4096] else '\n'


def to_csv_text(header, rows, lineterminator='\n'):
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator=lineterminator)
    writer.writerow(header)
    writer.writerows(rows)
    return buf.getvalue()


def aggregate_rows():
    """sources.csv rows rebuilt from every <domain>/sources_domain.csv, in domain then file order."""
    rows = []
    for d in domain_dirs():
        for r in read_dicts(ROOT / d / 'sources_domain.csv'):
            rows.append([d] + [r.get(k, '') for k in DOMAIN_COLS])
    return rows


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
