"""Run the tool tests under coverage.py and report which lines and branches of the tools no test reaches.

    python tools/tests/measure_coverage.py            # report; exit 1 if anything is unreached
    python tools/tests/measure_coverage.py --html     # also write an HTML report and print where it is

A debugging aid, not part of the unittest suite: the tools are standard library only, and this needs coverage.py
(pip install coverage, 7.10 or later for subprocess measurement). It fails, rather than skipping, when coverage.py
is missing, when the tests fail, or when no data was collected.

The tests run validate.py and build_registry.py from throwaway fixture copies, in subprocesses and in-process. Both
are measured (coverage's subprocess patch), and the copies' paths are mapped back onto tools/ here.

A line that cannot be reached by design is marked `# pragma: no cover` with the reason on the same line; the run
fails on any other unreached line or branch.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
MEASURED = ('common.py', 'validate.py', 'build_registry.py')

RC = """\
[run]
branch = True
parallel = True
patch = subprocess
data_file = {data}
include =
    */tools/common.py
    */tools/validate.py
    */tools/build_registry.py

[paths]
tools =
    {tools}/
    */General_Research/tools/

[report]
show_missing = True
skip_covered = False
"""


def run(cmd, **kw):
    print('$ ' + ' '.join(str(c) for c in cmd), flush=True)
    return subprocess.run([str(c) for c in cmd], **kw).returncode


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--html', action='store_true', help='also write an HTML report')
    args = ap.parse_args(argv)
    try:
        import coverage
    except ImportError:
        print('ERROR coverage-missing: coverage.py is not installed (pip install coverage); nothing was measured')
        return 1
    version = tuple(int(p) for p in coverage.__version__.split('.')[:2])
    if version < (7, 10):
        print(f'ERROR coverage-too-old: coverage.py {coverage.__version__} cannot measure subprocesses; need 7.10+')
        return 1

    with tempfile.TemporaryDirectory(prefix='gr-coverage-') as tmp:
        rc_file = Path(tmp) / 'coveragerc'
        rc_file.write_text(RC.format(data=Path(tmp) / '.coverage', tools=TOOLS.as_posix()), encoding='utf-8')
        cov = [sys.executable, '-m', 'coverage']
        if run(cov + ['run', f'--rcfile={rc_file}', '-m', 'unittest', 'discover', '-s', TOOLS / 'tests']) != 0:
            print('ERROR tests-failed: the test suite failed, so the coverage figures would mislead; fix the tests first')
            return 1
        if run(cov + ['combine', f'--rcfile={rc_file}']) != 0:
            print('ERROR coverage-combine: no coverage data to combine; the measurement did not reach the tools')
            return 1
        report_rc = run(cov + ['report', f'--rcfile={rc_file}', '--fail-under=100'])
        if args.html:
            # Outside the repo: validate.py would report an HTML report inside it as an unexpected file.
            out = Path(tempfile.mkdtemp(prefix='gr-htmlcov-'))
            if run(cov + ['html', f'--rcfile={rc_file}', '-d', out]) != 0:
                print('ERROR coverage-html: the HTML report was not written')
                return 1
            print(f'HTML report: {out / "index.html"}')
    if report_rc != 0:
        print('ERROR coverage-incomplete: lines or branches above are reached by no test; add a case that reaches '
              'each, or mark a by-design unreachable line `# pragma: no cover` with its reason')
        return 1
    print('every line and branch of ' + ', '.join(MEASURED) + ' is reached by a test')
    return 0


if __name__ == '__main__':
    sys.exit(main())
