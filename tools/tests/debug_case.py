"""Plant one test case's defect in a fresh fixture and show exactly what validate.py reports for it.

    python tools/tests/debug_case.py log-rewritten          # every case for that code
    python tools/tests/debug_case.py log-rewritten --keep   # keep the planted repo and print where it is
    python tools/tests/debug_case.py --list                 # every code with its number of cases

For a failing planted-defect test: it shows the planted repo's full report, exit code and --strict exit code, which
the unittest message truncates. Exits 1 if a case did not report its code at its level, or a check crashed, so it
agrees with test_planted_defects.
"""
import argparse
import re
import shutil
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fixture  # noqa: E402
import test_validate  # noqa: E402


class Runner(test_validate.FixtureCase):
    """The test class's runners, used outside unittest."""

    def runTest(self):  # unittest requires a test method to construct a TestCase
        raise AssertionError('not a test')


def main(argv=None):
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('code', nargs='?', help='a report code, e.g. log-rewritten')
    ap.add_argument('--keep', action='store_true', help='keep the planted repositories and print their paths')
    ap.add_argument('--list', action='store_true', help='list every code and how many cases plant it')
    args = ap.parse_args(argv)

    if args.list:
        for code, n in sorted(Counter(c[0] for c in test_validate.CASES).items()):
            print(f'{code:32} {n} case(s)')
        return 0
    if not args.code:
        ap.error('give a code, or --list')
    cases = [c for c in test_validate.CASES if c[0] == args.code]
    if not cases:
        print(f'ERROR unknown-code: no case plants {args.code!r}; --list shows the codes')
        return 1

    tmp = Path(tempfile.mkdtemp(prefix='gr-debug-'))
    template = tmp / 'template'
    template.mkdir()
    shas = fixture.build_template(template)
    runner = Runner()
    runner._tmp, runner.template, runner.shas = tmp, template, shas
    failed = 0
    try:
        for n, (code, level, cargs, mutate) in enumerate(cases, 1):
            parent = Path(tempfile.mkdtemp(prefix=f'case{n}-', dir=tmp))
            fixture.remove_tree(parent)
            shutil.copytree(template, parent)
            root = parent / fixture.REPO
            plan = mutate(root, shas)
            if callable(plan):
                rc, out = runner.run_inprocess(root, cargs, plan)
                strict_rc = runner.run_inprocess(root, cargs + ['--strict'], plan)[0]
                how = 'in-process, patched'
            else:
                env = plan['env'] if isinstance(plan, dict) else None
                rc, out = runner.run_validate(root, *cargs, env=env)
                strict_rc = runner.run_validate(root, *cargs, '--strict', env=env)[0]
                how = f'subprocess{", env " + str(env) if env else ""}'
            tag = 'ERROR' if level == 'error' else 'WARN '
            reported = re.search(rf'(?m)^{tag} \[[^\]]+\] {re.escape(code)}: ', out) is not None
            ok = (reported and strict_rc == 1 and rc == (1 if level == 'error' else 0)
                  and (code == 'check-crashed' or 'check-crashed' not in out))
            failed += not ok
            print(f'=== case {n}/{len(cases)}: {code} ({level}), args {cargs or "none"}, {how}')
            print(f'    exit {rc}, --strict exit {strict_rc}, {"PASS" if ok else "FAIL"}')
            if args.keep:
                print(f'    planted repo: {root}')
            print(out.rstrip())
    finally:
        if args.keep:
            print(f'kept {tmp}; delete it when done')
        else:
            fixture.remove_tree(tmp)
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
