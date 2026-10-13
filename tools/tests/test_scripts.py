"""Tests for the debugging scripts: tools/tests/debug_case.py and tools/tests/measure_coverage.py.

    python -m unittest discover -s tools/tests -v

A debugging aid that reports PASS for a broken case, or a coverage gate that exits 0 when nothing was measured, would
mislead whoever trusts it, so each script's pass and fail paths are run here. measure_coverage.py's runs of coverage.py
are replaced by scripted exit codes: running it for real runs this suite under coverage, which is what it is for.
"""
import contextlib
import io
import re
import shutil
import subprocess
import sys
import types
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import debug_case  # noqa: E402
import measure_coverage  # noqa: E402
import test_build_registry  # noqa: E402
import test_validate  # noqa: E402
from fixture import TOOLS  # noqa: E402
from test_validate import delete  # noqa: E402

SCRIPTS = TOOLS / 'tests'


def run_script(name, *args):
    proc = subprocess.run([sys.executable, str(SCRIPTS / name), *args], capture_output=True, text=True,
                          encoding='utf-8')
    return proc.returncode, proc.stdout + proc.stderr


@contextlib.contextmanager
def patched(obj, name, value):
    saved = getattr(obj, name)
    setattr(obj, name, value)
    try:
        yield
    finally:
        setattr(obj, name, saved)


def debug_inprocess(*args):
    """debug_case.main in this process (so its case lists can be patched), with stdout as a console has it."""
    raw = io.BytesIO()
    stream = io.TextIOWrapper(raw, encoding='cp1252')
    with contextlib.redirect_stdout(stream):
        rc = debug_case.main(list(args))
    stream.flush()
    return rc, raw.getvalue().decode('utf-8')


def printed_codes(name):
    """The codes a script prints as `ERROR <code>:`."""
    return set(re.findall(r"print\(f?'ERROR ([a-z0-9-]+):", (SCRIPTS / name).read_text(encoding='utf-8')))


class TestDebugCase(unittest.TestCase):
    def test_runs_a_codes_validate_cases(self):
        n = Counter(c[0] for c in test_validate.CASES)['log-rewritten']
        rc, out = run_script('debug_case.py', 'log-rewritten')
        self.assertEqual(rc, 0, out)
        self.assertEqual(len(re.findall(r'(?m)^    exit 1, --strict exit 1, PASS$', out)), n, out)
        self.assertRegex(out, r'(?m)^ERROR \[research log history\] log-rewritten: ')
        self.assertIn('0 case(s) with problems', out)

    def test_runs_a_codes_build_cases(self):
        rc, out = run_script('debug_case.py', '--build', 'manifest-header')
        self.assertEqual(rc, 0, out)
        self.assertRegex(out, r'(?m)^=== build case 1/1: manifest-header, also none, PASS$')
        self.assertEqual(out.count('ERROR manifest-header:'), 2, out)  # the build and the --check run

    def test_runs_the_accepted_variants(self):
        rc, out = run_script('debug_case.py', '--accepted')
        self.assertEqual(rc, 0, out)
        self.assertEqual(out.count(', PASS'), len(test_validate.ACCEPTED), out)

    def test_keep_leaves_the_planted_repo(self):
        rc, out = run_script('debug_case.py', 'tier', '--keep')
        self.assertEqual(rc, 0, out)
        kept = Path(re.search(r'(?m)^kept (.+); delete it when done$', out).group(1))
        self.addCleanup(test_validate.fixture.remove_tree, kept)
        planted = Path(re.search(r'(?m)^    planted repo: (.+)$', out).group(1))
        self.assertTrue((planted / 'INDEX.md').is_file(), out)

    def test_list_names_every_code_of_both_tools(self):
        rc, out = run_script('debug_case.py', '--list')
        self.assertEqual(rc, 0, out)
        for tool, cases in (('validate', test_validate.CASES), ('build', test_build_registry.BUILD_CASES)):
            for code, n in Counter(c[0] for c in cases).items():
                self.assertRegex(out, rf'(?m)^{tool} +{re.escape(code)} +{n} case\(s\)$')

    def test_unknown_code_and_bad_arguments_fail(self):
        for args in (['no-such-code'], ['--build', 'log-rewritten']):
            rc, out = run_script('debug_case.py', *args)
            self.assertEqual(rc, 1, out)
            self.assertIn('ERROR unknown-code:', out)
        for args in ([], ['tier', '--accepted']):
            rc, out = run_script('debug_case.py', *args)
            self.assertEqual(rc, 2, f'{args}: {out}')  # argparse's usage error

    def test_a_broken_case_is_reported_as_fail(self):
        """A case whose mutation plants nothing, a build case likewise, and a valid variant that is not valid."""
        with patched(test_validate, 'CASES', [('tier', 'error', [], lambda r, s: None)]):
            rc, out = debug_inprocess('tier')
        self.assertEqual(rc, 1, out)
        self.assertIn('problem: tier is not reported as error', out)
        with patched(test_build_registry, 'BUILD_CASES', [('manifest-header', lambda r: None)]):
            rc, out = debug_inprocess('--build', 'manifest-header')
        self.assertEqual(rc, 1, out)
        self.assertIn("problem: []: manifest-header is not reported", out)
        with patched(test_validate, 'ACCEPTED', [('AGENTS.md deleted', lambda r: delete(r, 'AGENTS.md'))]):
            rc, out = debug_inprocess('--accepted')
        self.assertEqual(rc, 1, out)
        self.assertIn('exit 1, FAIL', out)

    def test_every_printed_code_has_a_test(self):
        self.assertEqual(printed_codes('debug_case.py'), {'unknown-code'})


class TestMeasureCoverage(unittest.TestCase):
    def measure(self, exit_codes, *args, version='7.16.0'):
        """measure_coverage.main with coverage.py replaced: its runs exit with `exit_codes` in turn."""
        calls = []

        def run(cmd, **kw):
            calls.append(cmd)
            return exit_codes[len(calls) - 1]
        had = 'coverage' in sys.modules  # it is, when this suite runs under measure_coverage.py
        saved = sys.modules['coverage'] if had else None
        # None in sys.modules makes `import coverage` raise ImportError.
        sys.modules['coverage'] = None if version is None else types.SimpleNamespace(__version__=version)
        buf = io.StringIO()
        try:
            with patched(measure_coverage, 'run', run), contextlib.redirect_stdout(buf):
                rc = measure_coverage.main(list(args))
        finally:
            if had:
                sys.modules['coverage'] = saved
            else:
                del sys.modules['coverage']
        self.assertEqual(len(calls), len(exit_codes), f'ran {len(calls)} commands, scripted {len(exit_codes)}')
        return rc, buf.getvalue()

    def test_full_coverage_passes(self):
        rc, out = self.measure([0, 0, 0])
        self.assertEqual(rc, 0, out)
        self.assertIn('every line and branch of common.py, validate.py, build_registry.py is reached', out)

    def test_html_report_is_written_outside_the_repo(self):
        rc, out = self.measure([0, 0, 0, 0], '--html')
        self.assertEqual(rc, 0, out)
        where = Path(re.search(r'(?m)^HTML report: (.+)$', out).group(1))
        self.addCleanup(shutil.rmtree, where.parent)
        self.assertNotIn(TOOLS.parent.resolve(), where.resolve().parents)

    def test_each_failure_exits_1_with_its_code(self):
        cases = {
            'coverage-missing': ([], None),
            'coverage-too-old': ([], '7.9.2'),
            'tests-failed': ([1], '7.16.0'),
            'coverage-combine': ([0, 1], '7.16.0'),
            'coverage-incomplete': ([0, 0, 2], '7.16.0'),
            'coverage-html': ([0, 0, 0, 1], '7.16.0'),
        }
        for code, (exit_codes, version) in cases.items():
            with self.subTest(code=code):
                rc, out = self.measure(exit_codes, *(['--html'] if code == 'coverage-html' else []), version=version)
                self.assertEqual(rc, 1, out)
                self.assertRegex(out, rf'(?m)^ERROR {code}: ')
                self.assertNotIn('every line and branch', out)
        self.assertEqual(printed_codes('measure_coverage.py'), set(cases), 'a printed code without a case here')

    def test_measures_every_tool_module(self):
        """A tool module left out of MEASURED and the coverage include list would never be held to the gate."""
        tools = {p.name for p in TOOLS.glob('*.py')}
        self.assertEqual(set(measure_coverage.MEASURED), tools)
        included = set(re.findall(r'\*/tools/([a-z_]+\.py)', measure_coverage.RC))
        self.assertEqual(included, tools)


if __name__ == '__main__':
    unittest.main()
