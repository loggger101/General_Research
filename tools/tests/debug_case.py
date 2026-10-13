"""Plant test cases' defects in a fresh fixture and show exactly what the tools report for them.

    python tools/tests/debug_case.py log-rewritten            # every validate.py case for that code
    python tools/tests/debug_case.py log-rewritten --keep     # keep the planted repos and print where they are
    python tools/tests/debug_case.py --build manifest-header  # every build_registry.py case for that code
    python tools/tests/debug_case.py --accepted               # every valid variant, which must pass --strict --upstream
    python tools/tests/debug_case.py --list                   # every code with its number of cases

For a failing test: it shows the planted repo's full report and exit codes, which the unittest message truncates, and
the same problem list the test asserts is empty (test_validate.problems, test_build_registry.run_build_case), so it
cannot disagree with the suite. Exits 1 if any case it ran has a problem; prints `ERROR <code>:` and exits 1 for a code
no case plants.
"""
import argparse
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fixture  # noqa: E402
import test_build_registry  # noqa: E402
import test_validate  # noqa: E402


class Runner(test_validate.FixtureCase):
    """The test class's runners, used outside unittest."""

    def runTest(self):  # unittest requires a test method to construct a TestCase
        raise AssertionError('not a test')


def show_validate_cases(runner, cases, keep):
    failed = 0
    for n, case in enumerate(cases, 1):
        code, level, args, _, also = test_validate.case_parts(case)
        started = runner.start_case(case)
        rc, out, strict_rc, stderr = runner.finish_case(case, started)
        found = test_validate.problems(case, rc, out, strict_rc, stderr)
        failed += bool(found)
        how = 'in-process, patched' if started[2] is None else 'subprocess'
        print(f'=== case {n}/{len(cases)}: {code} ({level}), args {args or "none"}, also {sorted(also) or "none"}, {how}')
        print(f'    exit {rc}, --strict exit {strict_rc}, {"FAIL" if found else "PASS"}')
        for p in found:
            print(f'    problem: {p}')
        if keep:
            print(f'    planted repo: {started[0]}')
        print(out.rstrip())
        if stderr:
            print('--- stderr\n' + stderr.rstrip())
    return failed


def show_build_cases(runner, cases, keep):
    failed = 0
    for n, case in enumerate(cases, 1):
        code, _, also = test_build_registry.build_case_parts(case)
        root, runs, found = test_build_registry.run_build_case(runner, case)
        failed += bool(found)
        print(f'=== build case {n}/{len(cases)}: {code}, also {sorted(also) or "none"}, {"FAIL" if found else "PASS"}')
        for p in found:
            print(f'    problem: {p}')
        if keep:
            print(f'    planted repo: {root}')
        for args, rc, out in runs:
            print(f'--- build_registry.py {" ".join(args) or "(no args)"}: exit {rc}\n{out.rstrip()}')
    return failed


def show_accepted(runner, keep):
    failed = 0
    for n, (label, mutate) in enumerate(test_validate.ACCEPTED, 1):
        root = runner.copy()
        mutate(root)
        rc, out, err = test_validate.run_validate_proc(root, ['--strict', '--upstream'])
        ok = rc == 0 and not err
        failed += not ok
        print(f'=== accepted {n}/{len(test_validate.ACCEPTED)}: {label}\n    exit {rc}, {"PASS" if ok else "FAIL"}')
        if keep:
            print(f'    planted repo: {root}')
        print(out.rstrip() + ('\n--- stderr\n' + err.rstrip() if err else ''))
    return failed


def main(argv=None):
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('code', nargs='?', help='a report code, e.g. log-rewritten')
    ap.add_argument('--build', action='store_true', help="run build_registry.py's cases for the code, not validate.py's")
    ap.add_argument('--accepted', action='store_true', help='run every valid variant instead of a code\'s cases')
    ap.add_argument('--keep', action='store_true', help='keep the planted repositories and print their paths')
    ap.add_argument('--list', action='store_true', help='list every code and how many cases plant it')
    args = ap.parse_args(argv)

    if args.list:
        for tool, counts in (('validate', Counter(c[0] for c in test_validate.CASES)),
                             ('build', Counter(c[0] for c in test_build_registry.BUILD_CASES))):
            for code, n in sorted(counts.items()):
                print(f'{tool:9} {code:32} {n} case(s)')
        return 0
    if args.accepted == bool(args.code):
        ap.error('give a code, or --accepted, or --list')
    if args.code:
        pool = test_build_registry.BUILD_CASES if args.build else test_validate.CASES
        cases = [c for c in pool if c[0] == args.code]
        if not cases:
            print(f'ERROR unknown-code: no {"build" if args.build else "validate"} case plants {args.code!r}; '
                  f'--list shows the codes')
            return 1

    tmp = Path(tempfile.mkdtemp(prefix='gr-debug-'))
    runner = Runner()
    runner._tmp, runner.template = tmp, tmp / 'template'
    runner.template.mkdir()
    runner.shas = fixture.build_template(runner.template)
    try:
        if args.accepted:
            failed = show_accepted(runner, args.keep)
        elif args.build:
            failed = show_build_cases(runner, cases, args.keep)
        else:
            failed = show_validate_cases(runner, cases, args.keep)
    finally:
        if args.keep:
            print(f'kept {tmp}; delete it when done')
        else:
            runner.doCleanups()
            fixture.remove_tree(tmp)
    print(f'{failed} case(s) with problems')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
