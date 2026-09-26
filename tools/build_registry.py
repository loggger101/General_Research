"""Regenerate the derived files from their hand-edited sources.

    python tools/build_registry.py           # write sources.csv + manifest sizes/hashes
    python tools/build_registry.py --check   # exit 1 if either file is out of date

- sources.csv is rebuilt from every <domain>/sources_domain.csv (domain order,
  then file order), with `domain_dir` prepended. Never edit it by hand.
- full_texts_manifest.csv keeps its hand-written (domain_dir, id, file) mapping;
  this fills in `bytes` and `sha256` from disk. To register a new hosted file,
  add a row with those three columns and leave the last two empty.
"""
import argparse
import sys

from common import (MANIFEST, MANIFEST_COLS, REGISTRY, REGISTRY_COLS, ROOT, aggregate_rows,
                    file_digest, line_terminator, read_csv, to_csv_text)


def build_registry():
    return to_csv_text(REGISTRY_COLS, aggregate_rows(), line_terminator(REGISTRY))


def build_manifest():
    header, rows = read_csv(MANIFEST)
    if header != MANIFEST_COLS:
        sys.exit(f'{MANIFEST.name}: header must be {",".join(MANIFEST_COLS)}')
    out = []
    for domain, sid, fname, *_ in rows:
        path = ROOT / domain / 'full_texts' / fname
        if not path.is_file():
            sys.exit(f'{MANIFEST.name}: {domain}/full_texts/{fname} (id {sid}) does not exist')
        size, digest = file_digest(path)
        out.append([domain, sid, fname, size, digest])
    return to_csv_text(MANIFEST_COLS, out, line_terminator(MANIFEST))


def normalized(path):
    return path.read_text(encoding='utf-8').replace('\r\n', '\n') if path.exists() else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true', help='report staleness instead of writing')
    args = ap.parse_args()

    stale = []
    for path, text in ((REGISTRY, build_registry()), (MANIFEST, build_manifest())):
        if normalized(path) == text.replace('\r\n', '\n'):
            print(f'up to date  {path.name}')
            continue
        if args.check:
            stale.append(path.name)
            print(f'STALE       {path.name}')
        else:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(text)
            print(f'wrote       {path.name}')
    if stale:
        print('run: python tools/build_registry.py')
        sys.exit(1)


if __name__ == '__main__':
    main()
