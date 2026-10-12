"""Tests for tools/build_registry.py: what it regenerates, and that every bad input stops it with nothing written.

    python -m unittest discover -s tools/tests -v
"""
import contextlib
import hashlib
import importlib
import io
import re
import subprocess
import sys
import unittest

from fixture import TOOLS
from test_validate import BETA_CSV, BOM, MAN, FixtureCase, delete, duplicate_first_row, edit, put


def build(root, *args):
    proc = subprocess.run([sys.executable, str(root / 'tools' / 'build_registry.py'), *args], capture_output=True,
                          text=True, encoding='utf-8')
    return proc.returncode, proc.stdout + proc.stderr


# (code, mutate(root)) — each must stop the build with `ERROR code:` and leave both derived files untouched.
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
    ('manifest-license-empty', lambda r: edit(r, MAN, 'cc-by 4.0 (statement on PDF p1)', '')),
    ('manifest-duplicate', lambda r: duplicate_first_row(r, MAN)),
    ('manifest-file-missing', lambda r: edit(r, MAN, 'hosted.pdf', 'gone.pdf')),
]


def build_codes_in_source():
    src = (TOOLS / 'build_registry.py').read_text(encoding='utf-8')
    common = (TOOLS / 'common.py').read_text(encoding='utf-8')
    appended = set(re.findall(r"errors\.append\(\(\s*'([a-z0-9-]+)'", src))
    printed = set(re.findall(r"print\(f?'ERROR ([a-z0-9-]+):", src))
    # common.py's codes that the build's readers can raise (not the git file listing, which only validate.py uses)
    raised = set(re.findall(r"DataError\(\s*'([a-z0-9-]+)'", common)) - {'git-ls-files'}
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

    def test_every_code_has_a_case(self):
        planted = {c for c, _ in BUILD_CASES} | {'write-mismatch'}  # write-mismatch: test_write_mismatch
        self.assertEqual(build_codes_in_source() - planted, set(), 'codes build_registry can report but no case plants')
        self.assertEqual(planted - build_codes_in_source(), set(), 'cases for codes build_registry no longer reports')

    def test_bad_inputs_stop_the_build_with_nothing_written(self):
        for code, mutate in BUILD_CASES:
            with self.subTest(code=code):
                root = self.copy()
                # Make sources.csv stale too, so a build that wrote anything would change it.
                if code != 'registry-empty':
                    edit(root, '01_alpha/sources_domain.csv', 'Hosted paper', 'Hosted article')
                mutate(root)
                before = {n: (root / n).read_bytes() for n in ('sources.csv', MAN)}
                for args in ([], ['--check']):
                    rc, out = build(root, *args)
                    self.assertEqual(rc, 1, f'{code} {args}: build did not fail:\n{out}')
                    self.assertRegex(out, rf'(?m)^ERROR {re.escape(code)}: ', f'{code}: not reported:\n{out}')
                    self.assertIn('nothing written', out)
                    for name, data in before.items():
                        self.assertEqual((root / name).read_bytes(), data, f'{code} {args}: {name} was written')

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
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = b.main([])
        finally:
            sys.path.remove(tools)
            for m in ('common', 'validate', 'build_registry'):
                sys.modules.pop(m, None)
            sys.modules.update(saved)
        self.assertEqual(rc, 1, buf.getvalue())
        self.assertIn('ERROR write-mismatch: sources.csv', buf.getvalue())


if __name__ == '__main__':
    unittest.main()
