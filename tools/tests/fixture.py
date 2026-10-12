"""A minimal, valid General_Research checkout for the tool tests, plus sibling upstream clones.

build_template(parent) writes, under `parent`:
    General_Research/   two domains, one hosted file, extracted CSV + JSON, INDEX.md with a rejected source and a
                        research log, README layout, revision candidates and an upstream commit map; the tools are
                        copied in from this checkout, and sources.csv and the manifest hashes come from its own
                        build_registry.py. It is a git repository (validate.py lists files with git).
    spacecost/, AsteroidCatalog/, economicspace/
                        upstream clones with an origin/main ref, for `validate.py --upstream`.
It returns the upstream commit ids the tests need. Each test copies the template and plants one defect.
"""
import csv
import io
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = 'General_Research'
GIT_ID = ['-c', 'user.name=fixture', '-c', 'user.email=fixture@example.invalid', '-c', 'commit.gpgsign=false',
          '-c', 'core.autocrlf=false']

DOMAIN_HEADER = ['id', 'tier', 'short_title', 'journal_or_series', 'year', 'doi_or_url', 'authors_short',
                 'access_status', 'pipeline_mapping']
ALPHA = [
    ['src_hosted', 'T1', 'Hosted paper', 'J. Fixture 1:1', '2020', 'https://doi.org/10.1/fixture', 'Doe',
     'full_text_hosted - read from the fixture PDF', 'the alpha cell'],
    ['src_pending', 'T2', 'Pending report', 'NASA TM', 'n.d.', 'https://ntrs.example/1', 'Roe',
     'registered_not_pulled - an upstream citation, not yet read', 'the beta cell'],
]
BETA = [
    ['src_live', 'T3', 'Live dataset', 'Fixture service', '2021', 'https://data.example/live', 'Poe',
     'verified_live_not_pulled - read live', 'the gamma cell'],
]
EXTRACTED_HEADER = ['source_id', 'item', 'value', 'unit', 'location_in_source', 'notes']
CANDIDATE_HEADER = ['id', 'status', 'kind', 'domain_dir', 'source_ids', 'found_round', 'target_repo', 'target_file',
                    'target_row', 'field', 'current_value', 'proposed', 'evidence', 'checked_against', 'checked_date']
MAP_HEADER = ['repo', 'old_sha', 'main_sha', 'tree', 'subject', 'checked_against_in']

INDEX_MD = """# Fixture index

## Domain 1 — Alpha

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| src_hosted | T1 | Hosted paper | full text hosted | the alpha cell |
| src_pending | T2 | Pending report | registered, not pulled | the beta cell |

## Domain 2 — Beta

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| src_live | T3 | Live dataset | verified live, not hosted | the gamma cell |

## Rejected sources

| id | source | link | reason |
|---|---|---|---|
| rej_one | A rejected page | https://rejected.example | off-topic |

## Research log
- **Round 1** (2026-01-02): second round; rej_one rejected.
- **Round 0** (2026-01-01): first round.
"""

README_MD = """# Fixture

## Why this repo exists

| # | domain | pipeline cell(s) it could back or replace |
|---|---|---|
| 1 | Alpha | the alpha and beta cells |
| 2 | Beta | the gamma cell |

## Layout

```
README.md                 this file
INDEX.md                  index
sources.csv               generated
full_texts_manifest.csv   hosted files
revision_candidates.csv   candidates
upstream_commit_map.csv   commit map
AGENTS.md                 rules
tools/                    the tools
01_alpha/                 domain 1
02_beta/                  domain 2
```
"""

PDF = b'%PDF-1.4 fixture\n'


def csv_text(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()


def write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode('utf-8') if isinstance(text, str) else text)


def git(cwd, *args):
    proc = subprocess.run(['git', *GIT_ID, *args], cwd=str(cwd), capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f'git {" ".join(args)} failed in {cwd}: {proc.stderr}')
    return proc.stdout.strip()


def make_upstream(parent):
    """spacecost: main = M0 -> M1; O has M1's tree but is off main (a rewritten copy); O2 has M0's tree, off main."""
    shas = {}
    for name in ('spacecost', 'AsteroidCatalog', 'economicspace'):
        repo = parent / name
        repo.mkdir()
        git(repo, 'init', '-q')
        write(repo / 'reference.csv', 'x\n0\n')
        git(repo, 'add', '.')
        git(repo, 'commit', '-q', '-m', 'M0')
        m0 = git(repo, 'rev-parse', 'HEAD')
        if name == 'spacecost':
            write(repo / 'reference.csv', 'x\n1\n')
            git(repo, 'commit', '-q', '-am', 'M1')
            m1 = git(repo, 'rev-parse', 'HEAD')
            tree1 = git(repo, 'rev-parse', 'HEAD^{tree}')
            tree0 = git(repo, 'rev-parse', 'HEAD~1^{tree}')
            shas.update(M0=m0, M1=m1, tree1=tree1,
                        O=git(repo, 'commit-tree', tree1, '-m', 'M1 before the history rewrite'),
                        O2=git(repo, 'commit-tree', tree0, '-m', 'an unmapped commit'))
            git(repo, 'update-ref', 'refs/remotes/origin/main', m1)
        else:
            git(repo, 'update-ref', 'refs/remotes/origin/main', m0)
    return shas


def build_template(parent):
    parent = Path(parent)
    shas = make_upstream(parent)
    root = parent / REPO
    root.mkdir()
    (root / 'tools').mkdir()
    for f in ('common.py', 'validate.py', 'build_registry.py'):
        shutil.copyfile(TOOLS / f, root / 'tools' / f)
    write(root / '.gitignore', '__pycache__/\n')
    write(root / 'AGENTS.md', '# Rules\n')
    write(root / 'README.md', README_MD)
    write(root / 'INDEX.md', INDEX_MD)
    for d, rows in (('01_alpha', ALPHA), ('02_beta', BETA)):
        write(root / d / 'sources_domain.csv', csv_text(DOMAIN_HEADER, rows))
        write(root / d / 'FINDINGS.md', f'# {d} findings\n')
    write(root / '01_alpha' / 'full_texts' / 'hosted.pdf', PDF)
    write(root / 'full_texts_manifest.csv', csv_text(['domain_dir', 'id', 'file', 'bytes', 'sha256', 'license'],
                                                     [['01_alpha', 'src_hosted', 'hosted.pdf', '', '',
                                                       'cc-by 4.0 (statement on PDF p1)']]))
    write(root / '01_alpha' / 'extracted_data' / 'r1_alpha.csv',
          csv_text(EXTRACTED_HEADER, [['src_hosted', 'mass', '1', 'kg', 'p1', 'a note, with a comma']]))
    write(root / '02_beta' / 'extracted_data' / 'r1_beta.csv',
          csv_text(EXTRACTED_HEADER, [['src_live', 'rate', '2', 'kg/h', 'API', '']]))
    write(root / '02_beta' / 'extracted_data' / 'r1_beta_response.json', '{"source": "src_live", "rate": 2}\n')
    write(root / 'revision_candidates.csv', csv_text(CANDIDATE_HEADER, [
        ['rc-001', 'open', 'value', '01_alpha', 'src_hosted', 'R1', 'spacecost', 'reference.csv', 'x', 'x', '1', '2',
         'the hosted paper gives 2', f'spacecost@{shas["M1"]}', '2026-01-02'],
        ['rc-002', 'applied', 'citation', '02_beta', 'src_live', 'R0', 'spacecost', 'reference.csv', 'x', 'notes',
         'none', 'cite src_live', 'upstream applied it', f'spacecost@{shas["O"]}', '2026-01-01'],
    ]))
    write(root / 'upstream_commit_map.csv', csv_text(MAP_HEADER, [
        ['spacecost', shas['O'], shas['M1'], shas['tree1'], 'M1 before the history rewrite', 'rc-002']]))
    write(root / 'sources.csv', '')
    proc = subprocess.run([sys.executable, str(root / 'tools' / 'build_registry.py')], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f'fixture build failed:\n{proc.stdout}{proc.stderr}')
    git(root, 'init', '-q')
    return shas


def _make_writable(func, path, *_):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def remove_tree(path):
    """git marks object files read-only, which shutil.rmtree cannot delete on Windows; clear the flag and retry."""
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=_make_writable)
    else:
        shutil.rmtree(path, onerror=_make_writable)
