"""Tests for tools/build_registry.py: what it regenerates, and that every bad input stops it with nothing written.

    python -m unittest discover -s tools/tests -v
"""
import contextlib
import hashlib
import importlib
import io
import os
import re
import subprocess
import sys
import unittest
from concurrent.futures import ThreadPoolExecutor

from fixture import TOOLS
from test_validate import BETA_CSV, BOM, MAN, FixtureCase, delete, duplicate_first_row, edit, put


def build(root, *args, env=None, cwd=None):
    proc = subprocess.run([sys.executable, str(root / 'tools' / 'build_registry.py'), *args], capture_output=True,
                          text=True, encoding='utf-8', env=dict(os.environ, **(env or {})), cwd=cwd)
    return proc.returncode, proc.stdout + proc.stderr


# (code, mutate(root)[, also]) — each must stop the build with `ERROR code:`, report no other code but those in `also`,
# and leave both derived files untouched.
BUILD_CASES = [
    ('file-missing', lambda r: delete(r, BETA_CSV)),
    ('text-bom', lambda r: put(r, BETA_CSV, BOM + (r / BETA_CSV).read_bytes())),
    ('text-not-utf8', lambda r: put(r, BETA_CSV, (r / BETA_CSV).read_bytes() + b'caf\xe9\n')),
    ('csv-blank-line', lambda r: put(r, BETA_CSV, (r / BETA_CSV).read_bytes() + b'\nsrc_x,T1,a,b,2020,u,v,skipped,m\n')),
    ('csv-quoting', lambda r: edit(r, BETA_CSV, 'src_live,T3', 'src_live,"T3"x')),
    ('csv-empty', lambda r: put(r, BETA_CSV, b'')),
    ('csv-width', lambda r: edit(r, BETA_CSV, ',Poe,', ',Poe,extra,')),
    ('domain-header', lambda r: edit(r, BETA_CSV, 'short_title', 'title')),
    ('registry-empty', lambda r: [put(r, f, 'id,tier,short_title,journal_or_series,year,doi_or_url,authors_short,'
                                         'access_status,pipeline_mapping\n')
                                  for f in ('01_alpha/sources_domain.csv', BETA_CSV)]),
    ('manifest-header', lambda r: edit(r, MAN, 'license', 'licence')),
    ('manifest-domain-unknown', lambda r: edit(r, MAN, '01_alpha,src_hosted', '09_nope,src_hosted')),
    ('manifest-field-empty', lambda r: edit(r, MAN, ',hosted.pdf,', ',,')),
    ('manifest-file-name', lambda r: edit(r, MAN, ',hosted.pdf,', ',../full_texts/hosted.pdf,')),
    ('manifest-license-empty', lambda r: edit(r, MAN, 'cc-by 4.0 (statement on PDF p1)', '')),
    ('manifest-duplicate', lambda r: duplicate_first_row(r, MAN)),
    ('manifest-file-missing', lambda r: edit(r, MAN, 'hosted.pdf', 'gone.pdf')),
    # the manifest itself unreadable, and a derived file that is not UTF-8 (it cannot be compared, so nothing is written)
    ('text-bom', lambda r: put(r, MAN, BOM + (r / MAN).read_bytes())),
    ('text-not-utf8', lambda r: put(r, 'sources.csv', (r / 'sources.csv').read_bytes() + b'caf\xe9\n')),
]


def build_case_parts(case):
    """(code, mutate, also) of a BUILD_CASES entry; `also` is empty when the case declares none."""
    if len(case) not in (2, 3):
        raise AssertionError(f'test setup: a build case has {len(case)} fields, expected 2 or 3: {case[0]}')
    return case[0], case[1], set(case[2]) if len(case) == 3 else set()


def run_build_case(runner, case):
    """Plant a BUILD_CASES entry in a fresh copy from `runner` (a FixtureCase) and run the build, then the build with
    --check. Returns (root, [(args, rc, out)], problems): problems is empty when both runs fail with exactly the
    planted code (and its `also`), say nothing was written, and leave both derived files as they were. Thread-safe."""
    code, mutate, also = build_case_parts(case)
    root = runner.copy()
    # Make sources.csv stale too, so a build that wrote anything would change it.
    if code != 'registry-empty':
        edit(root, '01_alpha/sources_domain.csv', 'Hosted paper', 'Hosted article')
    mutate(root)
    before = {n: (root / n).read_bytes() for n in ('sources.csv', MAN)}
    runs, found = [], []
    for args in ([], ['--check']):
        rc, out = build(root, *args)
        runs.append((args, rc, out))
        codes = set(re.findall(r'(?m)^ERROR ([a-z0-9-]+): ', out))
        if rc != 1:
            found.append(f'{args}: exit {rc}, expected 1')
        if code not in codes:
            found.append(f'{args}: {code} is not reported')
        if codes - {code} - also:
            found.append(f'{args}: codes the case does not declare: {sorted(codes - {code} - also)}')
        if also - codes:
            found.append(f'{args}: codes the case declares but the report lacks: {sorted(also - codes)}')
        if 'nothing written' not in out:
            found.append(f'{args}: the report does not say nothing was written')
        found += [f'{args}: {name} was written' for name, data in before.items() if (root / name).read_bytes() != data]
    return root, runs, found


def build_codes_in_source():
    src = (TOOLS / 'build_registry.py').read_text(encoding='utf-8')
    common = (TOOLS / 'common.py').read_text(encoding='utf-8')
    appended = set(re.findall(r"errors\.append\(\(\s*'([a-z0-9-]+)'", src))
    printed = set(re.findall(r"print\(f?'ERROR ([a-z0-9-]+):", src))
    # common.py's codes that the build's readers can raise (not the git file listing, which only validate.py uses)
    raised = set(re.findall(r"DataError\(\s*'([a-z0-9-]+)'", common + src)) - {'git-ls-files'}
    return appended | printed | raised


class TestBuildRegistry(FixtureCase):
    def test_template_is_up_to_date(self):
        rc, out = build(self.copy(), '--check')
        self.assertEqual(rc, 0, out)
        self.assertEqual(out.count('up to date'), 2, out)

    def test_check_reports_stale_and_writes_nothing(self):
        root = self.copy()
        edit(root, BETA_CSV, 'Live dataset', 'Live service')
        before = (root / 'sources.csv').read_bytes()
        rc, out = build(root, '--check')
        self.assertEqual(rc, 1, out)
        self.assertIn('STALE       sources.csv', out)
        self.assertEqual((root / 'sources.csv').read_bytes(), before, '--check wrote sources.csv')

    def test_build_regenerates_registry_in_domain_order(self):
        root = self.copy()
        edit(root, BETA_CSV, 'Live dataset', 'Live service')
        rc, out = build(root)
        self.assertEqual(rc, 0, out)
        self.assertIn('wrote       sources.csv', out)
        lines = (root / 'sources.csv').read_text(encoding='utf-8').splitlines()
        self.assertEqual(lines[0].split(',')[:2], ['domain_dir', 'id'])
        self.assertEqual([l.split(',')[1] for l in lines[1:]], ['src_hosted', 'src_pending', 'src_live'])
        self.assertIn('Live service', lines[3])
        self.assertEqual(build(root, '--check')[0], 0, 'a second build is not idempotent')

    def test_build_fills_manifest_size_and_hash_and_keeps_license(self):
        root = self.copy()
        edit(root, MAN, (root / MAN).read_text(encoding='utf-8').split('\n')[1],
             '01_alpha,src_hosted,hosted.pdf,,,cc-by 4.0 (statement on PDF p1)')
        rc, out = build(root)
        self.assertEqual(rc, 0, out)
        row = (root / MAN).read_text(encoding='utf-8').split('\n')[1].split(',')
        data = (root / '01_alpha/full_texts/hosted.pdf').read_bytes()
        self.assertEqual(row[3:5], [str(len(data)), hashlib.sha256(data).hexdigest()])
        self.assertEqual(row[5], 'cc-by 4.0 (statement on PDF p1)')

    def test_keeps_crlf_line_endings(self):
        root = self.copy()
        for name in ('sources.csv', MAN):
            (root / name).write_bytes((root / name).read_bytes().replace(b'\n', b'\r\n'))
        edit(root, BETA_CSV, 'Live dataset', 'Live service')
        self.assertEqual(build(root)[0], 0)
        data = (root / 'sources.csv').read_bytes()
        self.assertEqual(data.count(b'\r\n'), data.count(b'\n'), 'line endings changed')

    def test_runs_from_any_directory_on_an_ascii_console(self):
        root = self.copy()
        edit(root, BETA_CSV, 'Live dataset', 'Live service')
        rc, out = build(root, env={'PYTHONIOENCODING': 'ascii'}, cwd=str(root.parent))
        self.assertEqual(rc, 0, out)
        self.assertIn('wrote       sources.csv', out)

    def test_missing_derived_files_are_created(self):
        root = self.copy()
        before = (root / 'sources.csv').read_bytes()
        delete(root, 'sources.csv')
        rc, out = build(root, '--check')
        self.assertEqual(rc, 1, out)
        self.assertIn('STALE       sources.csv', out)
        rc, out = build(root)
        self.assertEqual(rc, 0, out)
        self.assertEqual((root / 'sources.csv').read_bytes(), before)

    def test_a_bom_in_a_derived_file_is_rebuilt_away(self):
        """sources.csv is generated, so a BOM there is fixed by regenerating it, not reported as an input error."""
        root = self.copy()
        put(root, 'sources.csv', BOM + (root / 'sources.csv').read_bytes())
        self.assertEqual(build(root, '--check')[0], 1, 'a BOM in sources.csv was not reported stale')
        rc, out = build(root)
        self.assertEqual(rc, 0, out)
        self.assertFalse((root / 'sources.csv').read_bytes().startswith(BOM))

    def test_every_code_has_a_case(self):
        planted = {c[0] for c in BUILD_CASES} | {'write-mismatch'}  # write-mismatch: test_write_mismatch
        self.assertEqual(build_codes_in_source() - planted, set(), 'codes build_registry can report but no case plants')
        self.assertEqual(planted - build_codes_in_source(), set(), 'cases for codes build_registry no longer reports')

    def test_bad_inputs_stop_the_build_with_nothing_written(self):
        with ThreadPoolExecutor() as pool:
            futures = [pool.submit(run_build_case, self, case) for case in BUILD_CASES]
            for n, (case, future) in enumerate(zip(BUILD_CASES, futures)):
                with self.subTest(case=n, code=case[0]):
                    _, runs, found = future.result()
                    self.assertEqual(found, [], '\n'.join(out for _, _, out in runs))

    def test_write_mismatch(self):
        """A file that reads back different from what was written fails the build."""
        root = self.copy()
        edit(root, BETA_CSV, 'Live dataset', 'Live service')
        tools = str(root / 'tools')
        saved = {m: sys.modules.pop(m) for m in ('common', 'validate', 'build_registry') if m in sys.modules}
        sys.path.insert(0, tools)
        try:
            b = importlib.import_module('build_registry')
            real = b.normalized
            calls = []

            def flaky(path):
                calls.append(path)
                text = real(path)
                return text + 'corrupted' if len(calls) > 1 and text is not None else text
            b.normalized = flaky
            # A real text stream, as a console is: main() reconfigures stdout to UTF-8.
            raw = io.BytesIO()
            stream = io.TextIOWrapper(raw, encoding='cp1252')
            with contextlib.redirect_stdout(stream):
                rc = b.main([])
            stream.flush()
            out = raw.getvalue().decode('utf-8')
        finally:
            sys.path.remove(tools)
            for m in ('common', 'validate', 'build_registry'):
                sys.modules.pop(m, None)
            sys.modules.update(saved)
        self.assertEqual(rc, 1, out)
        self.assertIn('ERROR write-mismatch: sources.csv', out)


if __name__ == '__main__':
    unittest.main()
