"""Regenerate the derived files from their hand-edited sources.

    python tools/build_registry.py           # write sources.csv + manifest sizes/hashes
    python tools/build_registry.py --check   # exit 1 if either file is out of date

- sources.csv is rebuilt from every <domain>/sources_domain.csv (domain order,
  then file order), with `domain_dir` prepended. Never edit it by hand.
- full_texts_manifest.csv keeps its hand-written (domain_dir, id, file, license)
  columns; this fills in `bytes` and `sha256` from disk. To register a new
  hosted file, write `domain_dir,id,file,,,license` (see LICENSE_CLASSES in
  common.py for the license's first word).

Every problem in the inputs is reported as `ERROR code: message` and the run
exits 1 without writing anything: a partial rebuild would leave sources.csv
and the manifest disagreeing with each other. Codes are listed in
tools/tests/test_build_registry.py, which plants each defect.
"""
import argparse
import sys

from common import (MANIFEST, MANIFEST_COLS, REGISTRY, REGISTRY_COLS, ROOT, DataError, domain_dirs,
                    file_digest, line_terminator, plain_file_name, read_csv, read_domain_csv, rel, to_csv_text)


def build_registry(errors):
    rows = []
    for d in domain_dirs():
        try:
            rows.extend([d] + r for r in read_domain_csv(d))
        except DataError as e:
            errors.append((e.code, str(e)))
    if not rows and not errors:
        errors.append(('registry-empty', f'no sources found: {len(domain_dirs())} domain directories under {ROOT}'))
    return to_csv_text(REGISTRY_COLS, rows, line_terminator(REGISTRY))


def build_manifest(errors):
    try:
        header, rows = read_csv(MANIFEST)
    except DataError as e:
        errors.append((e.code, str(e)))
        return None
    if header != MANIFEST_COLS:
        errors.append(('manifest-header', f'{MANIFEST.name}: header is {header}, expected {",".join(MANIFEST_COLS)}'))
        return None
    domains = set(domain_dirs())
    out, seen = [], set()
    for n, row in enumerate(rows, 2):
        domain, sid, fname, _, _, license = row
        where = f'{MANIFEST.name} line {n}'
        if domain not in domains:
            errors.append(('manifest-domain-unknown', f'{where}: domain_dir {domain!r} is not a domain directory'))
            continue
        if not sid or not fname:
            errors.append(('manifest-field-empty', f'{where}: id and file are required'))
            continue
        if not plain_file_name(fname):
            errors.append(('manifest-file-name', f'{where}: file {fname!r} must be a bare file name inside '
                                                 f'{domain}/full_texts/, with no directory part'))
            continue
        if not license.strip():
            errors.append(('manifest-license-empty', f'{where}: {fname} has no license; read it off the file or its record'))
        if (domain, fname) in seen:
            errors.append(('manifest-duplicate', f'{where}: {domain}/full_texts/{fname} is listed twice'))
        seen.add((domain, fname))
        path = ROOT / domain / 'full_texts' / fname
        if not path.is_file():
            errors.append(('manifest-file-missing', f'{where}: {rel(path)} (id {sid}) does not exist'))
            continue
        size, digest = file_digest(path)
        out.append([domain, sid, fname, size, digest, license])
    return to_csv_text(MANIFEST_COLS, out, line_terminator(MANIFEST))


def normalized(path):
    """The file's current text with LF line ends, or None if it does not exist yet. A BOM is kept, so a file that
    has one compares stale and is rewritten without it; bytes that are not UTF-8 raise DataError."""
    if not path.exists():
        return None
    try:
        return path.read_bytes().decode('utf-8').replace('\r\n', '\n')
    except UnicodeDecodeError as e:
        raise DataError('text-not-utf8', f'{rel(path)}: not UTF-8 ({e}); delete it and rebuild')


def main(argv=None):
    # The messages hold non-ASCII; a cp1252 console would raise partway through the report.
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true', help='report staleness instead of writing')
    args = ap.parse_args(argv)

    errors = []
    outputs = [(REGISTRY, build_registry(errors)), (MANIFEST, build_manifest(errors))]
    current = {}
    for path, _ in outputs:
        try:
            current[path] = normalized(path)
        except DataError as e:
            errors.append((e.code, str(e)))
    if errors:
        for code, msg in errors:
            print(f'ERROR {code}: {msg}')
        print(f'{len(errors)} error(s); nothing written')
        return 1

    stale = []
    for path, text in outputs:
        if current[path] == text.replace('\r\n', '\n'):
            print(f'up to date  {path.name}')
            continue
        if args.check:
            stale.append(path.name)
            print(f'STALE       {path.name}')
            continue
        with open(path, 'w', encoding='utf-8', newline='') as fh:
            fh.write(text)
        if normalized(path) != text.replace('\r\n', '\n'):
            print(f'ERROR write-mismatch: {path.name} reads back different from what was written')
            return 1
        print(f'wrote       {path.name}')
    if stale:
        print('run: python tools/build_registry.py')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
