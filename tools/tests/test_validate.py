"""Planted-defect tests for tools/validate.py.

    python -m unittest discover -s tools/tests -v

Each case copies a valid fixture repository (fixture.py), plants one defect and asserts that validate.py reports
that defect's code: an ERROR fails the run; a WARN does not, except under --strict. test_every_code_has_a_case
fails if validate.py or common.py can report a code that no case here plants, so a new check cannot land untested.
"""
import contextlib
import importlib
import io
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fixture  # noqa: E402

TOOLS = fixture.TOOLS
BOM = b'\xef\xbb\xbf'


# ------------------------------------------------------------------------------------------- editing helpers

def edit(root, rel, old, new, count=1):
    path = root / rel
    text = path.read_text(encoding='utf-8')
    if text.count(old) != count:
        raise AssertionError(f'test setup: {old!r} occurs {text.count(old)} times in {rel}, expected {count}')
    path.write_text(text.replace(old, new), encoding='utf-8', newline='')


def put(root, rel, data):
    fixture.write(root / rel, data)


def delete(root, rel):
    path = root / rel
    if path.is_dir():
        fixture.remove_tree(path)
    else:
        path.unlink()


def rebuild(root):
    proc = subprocess.run([sys.executable, str(root / 'tools' / 'build_registry.py')], capture_output=True, text=True)
    if proc.returncode != 0:
        raise AssertionError(f'test setup: build_registry failed:\n{proc.stdout}{proc.stderr}')


def domain_edit(root, rel, old, new):
    """Edit a sources_domain.csv and regenerate sources.csv, so only the planted defect is reported."""
    edit(root, rel, old, new)
    rebuild(root)


def duplicate_first_row(root, rel):
    lines = (root / rel).read_text(encoding='utf-8').split('\n')
    lines.insert(2, lines[1])
    (root / rel).write_text('\n'.join(lines), encoding='utf-8', newline='')


def drop_line(root, rel, prefix):
    lines = (root / rel).read_text(encoding='utf-8').split('\n')
    keep = [l for l in lines if not l.startswith(prefix)]
    if len(keep) != len(lines) - 1:
        raise AssertionError(f'test setup: {len(lines) - len(keep)} lines of {rel} start with {prefix!r}, expected 1')
    (root / rel).write_text('\n'.join(keep), encoding='utf-8', newline='')


def swap_lines(root, rel, a, b):
    text = (root / rel).read_text(encoding='utf-8')
    if text.count(a) != 1 or text.count(b) != 1:
        raise AssertionError(f'test setup: cannot swap {a!r} and {b!r} in {rel}')
    text = text.replace(a, '\0').replace(b, a).replace('\0', b)
    (root / rel).write_text(text, encoding='utf-8', newline='')


# ------------------------------------------------------------------------------------------- the cases
# (code, level, args, mutate) — mutate(root, shas) plants the defect. level is 'error' or 'warn'.
# A mutate that returns a callable runs validate in-process and passes that callable the loaded module to patch.

ROW_ALPHA_HOSTED = '| src_hosted | T1 | Hosted paper | full text hosted | the alpha cell |\n'
ROW_ALPHA_PENDING = '| src_pending | T2 | Pending report | registered, not pulled | the beta cell |\n'
ROW_BETA = '| src_live | T3 | Live dataset | verified live, not hosted | the gamma cell |\n'
DOMAIN2_SECTION = ('## Domain 2 — Beta\n\n| id | tier | source (short) | access | backs / could replace |\n'
                   '|---|---|---|---|---|\n' + ROW_BETA + '\n')
REJ_ROW = '| rej_one | A rejected page | https://rejected.example | off-topic |\n'
LOG1 = '- **Round 1** (2026-01-02): second round; rej_one rejected.\n'
LOG0 = '- **Round 0** (2026-01-01): first round.\n'
ALPHA_CSV = '01_alpha/sources_domain.csv'
BETA_CSV = '02_beta/sources_domain.csv'
CANDS = 'revision_candidates.csv'
MAP = 'upstream_commit_map.csv'
MAN = 'full_texts_manifest.csv'
X_ALPHA = '01_alpha/extracted_data/r1_alpha.csv'
X_BETA = '02_beta/extracted_data/r1_beta.csv'
X_JSON = '02_beta/extracted_data/r1_beta_response.json'


def crash_manifest(v):
    def check_manifest(rep, ctx):
        raise RuntimeError('planted crash')
    v.CHECKS[v.CHECKS.index(v.check_manifest)] = check_manifest


CASES = [
    # common.py readers
    ('file-missing', 'error', [], lambda r, s: delete(r, CANDS)),
    ('text-bom', 'error', [], lambda r, s: put(r, '01_alpha/FINDINGS.md', BOM + b'# findings\n')),
    ('text-not-utf8', 'error', [], lambda r, s: put(r, '01_alpha/FINDINGS.md', b'# caf\xe9\n')),
    ('csv-blank-line', 'error', [], lambda r, s: edit(r, CANDS, '\nrc-002', '\n\nrc-002')),
    ('csv-quoting', 'error', [], lambda r, s: edit(r, X_BETA, 'src_live,rate', 'src_live,"rate"x')),
    ('csv-empty', 'error', [], lambda r, s: put(r, '02_beta/extracted_data/r2_empty.csv', b'')),
    ('csv-width', 'error', [], lambda r, s: edit(r, X_BETA, 'API,', 'API,extra,')),
    ('domain-header', 'error', [], lambda r, s: edit(r, BETA_CSV, 'short_title', 'title')),
    ('git-ls-files', 'error', [], lambda r, s: delete(r, '.git')),
    # check_files
    ('text-empty', 'error', [], lambda r, s: put(r, '01_alpha/FINDINGS.md', b'')),
    ('text-doubled-cr', 'error', [], lambda r, s: put(r, '01_alpha/FINDINGS.md', b'# a\r\r\nb\r\r\n')),
    ('text-lone-cr', 'error', [], lambda r, s: put(r, '01_alpha/FINDINGS.md', b'# a\rb\n')),
    ('text-no-final-newline', 'error', [], lambda r, s: put(r, '01_alpha/FINDINGS.md', b'# findings')),
    # check_layout
    ('root-extracted-data', 'error', [], lambda r, s: put(r, 'extracted_data/r1.csv', 'source_id\nsrc_live\n')),
    ('root-unexpected-entry', 'error', [], lambda r, s: put(r, 'notes.txt', 'stray\n')),
    ('root-file-missing', 'error', [], lambda r, s: delete(r, 'AGENTS.md')),
    ('domain-number-duplicate', 'error', [], lambda r, s: put(r, '02_gamma/FINDINGS.md', '# gamma\n')),
    ('domain-number-gap', 'error', [], lambda r, s: put(r, '04_delta/FINDINGS.md', '# delta\n')),
    ('domain-unexpected-entry', 'error', [], lambda r, s: put(r, '01_alpha/notes.txt', 'stray\n')),
    ('extracted-bad-extension', 'error', [], lambda r, s: put(r, '01_alpha/extracted_data/table.xlsx', b'PK')),
    ('domain-file-missing', 'error', [], lambda r, s: delete(r, '02_beta/FINDINGS.md')),
    ('nothing-checked', 'error', [], lambda r, s: [delete(r, p) for p in (X_ALPHA, X_BETA, X_JSON)]),
    # check_registry
    ('domain-field-empty', 'error', [], lambda r, s: domain_edit(r, ALPHA_CSV, ',Doe,', ',,')),
    ('domain-field-whitespace', 'error', [], lambda r, s: domain_edit(r, ALPHA_CSV, ',Doe,', ', Doe,')),
    ('year-format', 'error', [], lambda r, s: domain_edit(r, ALPHA_CSV, ',2020,', ',circa 2020,')),
    ('registry-header', 'error', [], lambda r, s: edit(r, 'sources.csv', 'domain_dir,', 'domain,')),
    ('registry-stale', 'error', [], lambda r, s: edit(r, ALPHA_CSV, 'Hosted paper', 'Hosted article')),
    ('registry-duplicate-id', 'error', [], lambda r, s: domain_edit(r, BETA_CSV, 'src_live,', 'src_hosted,')),
    ('id-format', 'error', [], lambda r, s: domain_edit(r, BETA_CSV, 'src_live,', 'Src Live,')),
    ('tier', 'error', [], lambda r, s: domain_edit(r, BETA_CSV, ',T3,', ',T9,')),
    ('access-class', 'error', [], lambda r, s: domain_edit(r, BETA_CSV, 'verified_live_not_pulled', 'downloaded')),
    # check_index
    ('index-domain-no-dir', 'error', [], lambda r, s: edit(r, 'INDEX.md', '## Rejected sources',
                                                         '## Domain 9 — Nine\n\n## Rejected sources')),
    ('index-domain-duplicate', 'error', [], lambda r, s: edit(r, 'INDEX.md', DOMAIN2_SECTION, DOMAIN2_SECTION * 2)),
    ('index-no-table', 'error', [], lambda r, s: edit(r, 'INDEX.md', DOMAIN2_SECTION, '## Domain 2 — Beta\n\nno table\n\n')),
    ('index-table-split', 'error', [], lambda r, s: edit(r, 'INDEX.md', ROW_ALPHA_HOSTED, ROW_ALPHA_HOSTED + '\n')),
    ('index-header', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| backs / could replace |', '| backs |', 2)),
    ('index-separator', 'error', [], lambda r, s: edit(r, 'INDEX.md', '|---|---|---|---|---|\n' + ROW_BETA,
                                                       '|---|---|\n' + ROW_BETA)),
    ('index-row-cells', 'error', [], lambda r, s: edit(r, 'INDEX.md', ROW_BETA, '| src_live | T3 | verified live, not hosted |\n')),
    ('index-empty-cell', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| the gamma cell |', '|  |')),
    ('index-id-unknown', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| src_live |', '| src_nope |')),
    ('index-wrong-domain', 'error', [], lambda r, s: edit(r, 'INDEX.md', ROW_ALPHA_PENDING, ROW_ALPHA_PENDING + ROW_BETA)),
    ('index-tier', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| src_live | T3 |', '| src_live | T2 |')),
    ('index-access-in-last-cell', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| the gamma cell |', '| verified live |')),
    ('index-access-mismatch', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| full text hosted |', '| not pulled |')),
    ('index-missing-rows', 'error', [], lambda r, s: edit(r, 'INDEX.md', ROW_ALPHA_PENDING, '')),
    ('index-duplicate-rows', 'error', [], lambda r, s: edit(r, 'INDEX.md', ROW_ALPHA_PENDING, ROW_ALPHA_PENDING * 2)),
    ('index-order', 'error', [], lambda r, s: swap_lines(r, 'INDEX.md', ROW_ALPHA_HOSTED, ROW_ALPHA_PENDING)),
    ('index-domain-order', 'error', [], lambda r, s: (edit(r, 'INDEX.md', DOMAIN2_SECTION, ''),
                                                      edit(r, 'INDEX.md', '## Domain 1', DOMAIN2_SECTION + '## Domain 1'))),
    ('index-domain-missing', 'error', [], lambda r, s: edit(r, 'INDEX.md', DOMAIN2_SECTION, '')),
    # check_log
    ('log-missing', 'error', [], lambda r, s: edit(r, 'INDEX.md', '## Research log', '## Log')),
    ('log-not-last', 'error', [], lambda r, s: edit(r, 'INDEX.md', LOG0, LOG0 + '## Appendix\n')),
    ('log-date-invalid', 'error', [], lambda r, s: edit(r, 'INDEX.md', '(2026-01-02)', '(2026-02-30)')),
    ('log-date-future', 'error', [], lambda r, s: edit(r, 'INDEX.md', '(2026-01-02)', '(2999-01-02)')),
    ('log-entry-format', 'error', [], lambda r, s: edit(r, 'INDEX.md', LOG1, '- **R2** (2026-01-03): x\n' + LOG1)),
    ('log-mislabelled', 'error', [], lambda r, s: edit(r, 'INDEX.md', LOG1, '### R2 (2026-01-03)\n' + LOG1)),
    ('log-blank-line', 'error', [], lambda r, s: edit(r, 'INDEX.md', LOG1, LOG1 + '\n')),
    ('log-preamble', 'error', [], lambda r, s: edit(r, 'INDEX.md', LOG1, 'Rounds below.\n' + LOG1)),
    ('log-no-rounds', 'error', [], lambda r, s: edit(r, 'INDEX.md', LOG1 + LOG0, '- **Maintenance** (2026-01-01): x\n')),
    ('log-order', 'error', [], lambda r, s: swap_lines(r, 'INDEX.md', LOG1, LOG0)),
    ('log-gap', 'error', [], lambda r, s: edit(r, 'INDEX.md', '**Round 1**', '**Round 2**')),
    ('log-duplicate', 'error', [], lambda r, s: edit(r, 'INDEX.md', LOG1, LOG1 * 2)),
    ('log-date-order', 'error', [], lambda r, s: edit(r, 'INDEX.md', '(2026-01-02)', '(2025-12-31)')),
    # check_rejected
    ('rejected-missing', 'error', [], lambda r, s: edit(r, 'INDEX.md', '## Rejected sources\n', '')),
    ('rejected-position', 'error', [], lambda r, s: edit(r, 'INDEX.md', '## Research log', '## Notes\n\ntext\n\n## Research log')),
    ('rejected-no-table', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| id | source | link | reason |\n|---|---|---|---|\n' + REJ_ROW, 'none\n')),
    ('rejected-table-split', 'error', [], lambda r, s: edit(r, 'INDEX.md', REJ_ROW, REJ_ROW + '\n| rej_two | b | c | d |\n')),
    ('rejected-header', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| id | source | link | reason |', '| id | source | why |')),
    ('rejected-separator', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| reason |\n|---|---|---|---|\n',
                                                                  '| reason |\n|---|---|\n')),
    ('rejected-row-cells', 'error', [], lambda r, s: edit(r, 'INDEX.md', REJ_ROW, '| rej_one | off-topic |\n')),
    ('rejected-duplicate', 'error', [], lambda r, s: edit(r, 'INDEX.md', REJ_ROW, REJ_ROW * 2)),
    ('rejected-empty-cell', 'error', [], lambda r, s: edit(r, 'INDEX.md', '| off-topic |', '|  |')),
    ('rejected-still-registered', 'error', [], lambda r, s: edit(r, 'INDEX.md', REJ_ROW, REJ_ROW + '| src_live | b | c | d |\n')),
    ('rejected-still-named', 'error', [], lambda r, s: put(r, '01_alpha/FINDINGS.md', '# findings\nrej_one was useful\n')),
    # check_manifest
    ('manifest-header', 'error', [], lambda r, s: edit(r, MAN, 'license', 'licence')),
    ('manifest-license', 'error', [], lambda r, s: edit(r, MAN, 'cc-by 4.0', 'gpl 3')),
    ('manifest-duplicate', 'error', [], lambda r, s: duplicate_first_row(r, MAN)),
    ('manifest-domain-unknown', 'error', [], lambda r, s: edit(r, MAN, '01_alpha,src_hosted', '09_nope,src_hosted')),
    ('manifest-id-unknown', 'error', [], lambda r, s: edit(r, MAN, 'src_hosted', 'src_nope')),
    ('manifest-wrong-domain', 'error', [], lambda r, s: edit(r, MAN, '01_alpha,src_hosted', '02_beta,src_hosted')),
    ('manifest-file-missing', 'error', [], lambda r, s: edit(r, MAN, 'hosted.pdf', 'gone.pdf')),
    ('manifest-stale', 'error', [], lambda r, s: put(r, '01_alpha/full_texts/hosted.pdf', b'%PDF-1.4 changed\n')),
    ('manifest-file-too-large', 'error', [], lambda r, s: (lambda v: setattr(v, 'GITHUB_HARD_LIMIT', 1))),
    ('manifest-file-large', 'warn', [], lambda r, s: (lambda v: setattr(v, 'GITHUB_WARN_LIMIT', 1))),
    ('manifest-not-redistributable', 'warn', [], lambda r, s: edit(r, MAN, 'cc-by 4.0', 'unknown')),
    ('manifest-unlisted-file', 'error', [], lambda r, s: put(r, '02_beta/full_texts/extra.pdf', b'%PDF extra\n')),
    ('hosted-without-file', 'error', [], lambda r, s: domain_edit(r, BETA_CSV, 'verified_live_not_pulled - read live',
                                                                  'full_text_hosted - claimed')),
    ('file-without-hosted', 'error', [], lambda r, s: domain_edit(r, ALPHA_CSV, 'full_text_hosted', 'verified_live_not_pulled')),
    ('access-sha-mismatch', 'warn', [], lambda r, s: domain_edit(r, ALPHA_CSV, 'read from the fixture PDF',
                                                                 'read from the fixture PDF sha256=deadbeef')),
    # check_extracted
    ('extracted-json-invalid', 'error', [], lambda r, s: put(r, X_JSON, '{"source": "src_live",\n')),
    ('extracted-header-duplicate', 'error', [], lambda r, s: edit(r, X_BETA, 'item,value', 'item,item')),
    ('extracted-header-empty', 'error', [], lambda r, s: edit(r, X_BETA, 'item,value', 'item,')),
    ('extracted-header-repeat', 'error', [], lambda r, s: edit(r, X_BETA, '\nsrc_live', '\nsource_id,item,value,unit,location_in_source,notes\nsrc_live')),
    ('extracted-unknown-source', 'error', [], lambda r, s: edit(r, X_BETA, '\nsrc_live', '\nsrc_nope')),
    ('extracted-no-source-col', 'warn', [], lambda r, s: put(r, '02_beta/extracted_data/r2_plain.csv', 'item,value\nsrc_live rate,2\n')),
    ('source-uncited', 'warn', [], lambda r, s: edit(r, X_ALPHA, '\nsrc_hosted,', '\n,')),
    # check_candidates
    ('cand-header', 'error', [], lambda r, s: edit(r, CANDS, 'checked_date', 'date')),
    ('cand-id', 'error', [], lambda r, s: edit(r, CANDS, 'rc-002', 'rc-2')),
    ('cand-field-empty', 'error', [], lambda r, s: edit(r, CANDS, 'upstream applied it', '')),
    ('cand-status', 'error', [], lambda r, s: edit(r, CANDS, 'rc-002,applied', 'rc-002,pending')),
    ('cand-kind', 'error', [], lambda r, s: edit(r, CANDS, ',citation,', ',guess,')),
    ('cand-domain', 'error', [], lambda r, s: edit(r, CANDS, 'citation,02_beta', 'citation,09_nope')),
    ('cand-source-unknown', 'error', [], lambda r, s: edit(r, CANDS, '02_beta,src_live', '02_beta,src_nope')),
    ('cand-found-round', 'error', [], lambda r, s: edit(r, CANDS, ',R0,', ',0,')),
    ('cand-found-round-future', 'error', [], lambda r, s: edit(r, CANDS, ',R0,', ',R9,')),
    ('cand-date', 'error', [], lambda r, s: edit(r, CANDS, '2026-01-01', '2026-13-01')),
    ('cand-date-future', 'error', [], lambda r, s: edit(r, CANDS, '2026-01-01', '2999-01-01')),
    ('cand-target-repo', 'error', [], lambda r, s: edit(r, CANDS, 'R0,spacecost', 'R0,otherrepo')),
    ('cand-checked-against', 'error', [], lambda r, s: edit(r, CANDS, f'spacecost@{s["O"]}', 'spacecost-abc')),
    # check_upstream_map
    ('map-header', 'error', [], lambda r, s: edit(r, MAP, 'main_sha', 'new_sha')),
    ('map-repo', 'error', [], lambda r, s: edit(r, MAP, '\nspacecost,', '\notherrepo,')),
    ('map-sha-format', 'error', [], lambda r, s: edit(r, MAP, s['tree1'], 'not-a-sha')),
    ('map-duplicate', 'error', [], lambda r, s: duplicate_first_row(r, MAP)),
    ('map-cited-mismatch', 'error', [], lambda r, s: edit(r, MAP, ',rc-002', ',rc-001')),
    # check_upstream (--upstream)
    ('upstream-repo-missing', 'error', ['--upstream'], lambda r, s: delete(r.parent, 'AsteroidCatalog')),
    ('map-not-equivalent', 'error', ['--upstream'], lambda r, s: edit(r, MAP, s['M1'], s['M0'])),
    ('upstream-sha-unknown', 'error', ['--upstream'], lambda r, s: edit(r, CANDS, f'spacecost@{s["M1"]}', 'spacecost@' + 'f' * 40)),
    ('upstream-open-off-main', 'error', ['--upstream'], lambda r, s: edit(r, CANDS, f'spacecost@{s["M1"]}', f'spacecost@{s["O2"]}')),
    ('upstream-sha-unmapped', 'error', ['--upstream'], lambda r, s: (edit(r, CANDS, f'spacecost@{s["O"]}', f'spacecost@{s["O2"]}'),
                                                                     edit(r, MAP, ',rc-002', ','))),
    # check_readme
    ('readme-layout-missing', 'error', [], lambda r, s: edit(r, 'README.md', '## Layout', '## Files')),
    ('readme-domain-missing', 'error', [], lambda r, s: drop_line(r, 'README.md', '02_beta/')),
    ('readme-root-file-missing', 'error', [], lambda r, s: drop_line(r, 'README.md', 'AGENTS.md')),
    ('readme-domain-table', 'error', [], lambda r, s: drop_line(r, 'README.md', '| 2 |')),
    # driver
    ('check-crashed', 'error', [], lambda r, s: crash_manifest),
]


def codes_in_source():
    """Every code validate.py and common.py can report, read from their source."""
    validate_src = (TOOLS / 'validate.py').read_text(encoding='utf-8')
    common_src = (TOOLS / 'common.py').read_text(encoding='utf-8')
    literal = set(re.findall(r"(?:rep|self)\.(?:error|warn)\(\s*'([a-z0-9-]+)'", validate_src))
    raised = set(re.findall(r"DataError\(\s*'([a-z0-9-]+)'", common_src + validate_src))
    return literal | raised


# ------------------------------------------------------------------------------------------- running

class FixtureCase(unittest.TestCase):
    template = None

    @classmethod
    def setUpClass(cls):
        cls._tmp = Path(tempfile.mkdtemp(prefix='gr-tools-'))
        cls.template = cls._tmp / 'template'
        cls.template.mkdir()
        cls.shas = fixture.build_template(cls.template)

    @classmethod
    def tearDownClass(cls):
        fixture.remove_tree(cls._tmp)

    def copy(self):
        """A fresh copy of the template (repo and upstream siblings); returns the repo root."""
        parent = Path(tempfile.mkdtemp(prefix='case-', dir=self._tmp))
        fixture.remove_tree(parent)
        shutil.copytree(self.template, parent)
        self.addCleanup(fixture.remove_tree, parent)
        return parent / fixture.REPO

    def run_validate(self, root, *args):
        proc = subprocess.run([sys.executable, str(root / 'tools' / 'validate.py'), *args], capture_output=True,
                              text=True, encoding='utf-8')
        self.assertEqual(proc.stderr, '', f'validate.py wrote to stderr:\n{proc.stderr}')
        return proc.returncode, proc.stdout

    def run_inprocess(self, root, args, patch):
        """Load the copy's validate.py, let `patch` alter it, run it and capture its output."""
        tools = str(root / 'tools')
        saved = {m: sys.modules.pop(m) for m in ('common', 'validate', 'build_registry') if m in sys.modules}
        sys.path.insert(0, tools)
        try:
            module = importlib.import_module('validate')
            self.assertEqual(Path(module.ROOT), root.resolve(), 'loaded validate.py from the wrong checkout')
            patch(module)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = module.run(list(args))
            return rc, buf.getvalue()
        finally:
            sys.path.remove(tools)
            for m in ('common', 'validate', 'build_registry'):
                sys.modules.pop(m, None)
            sys.modules.update(saved)


class TestValidate(FixtureCase):
    def test_clean_fixture_passes(self):
        root = self.copy()
        for args in ([], ['--strict'], ['--upstream', '--strict']):
            rc, out = self.run_validate(root, *args)
            self.assertEqual(rc, 0, f'args {args}:\n{out}')
            self.assertIn('0 error(s), 0 warning(s)', out)
            self.assertNotIn('ERROR', out)

    def test_summary_says_whether_upstream_ran(self):
        root = self.copy()
        self.assertIn('upstream checks not run (pass --upstream)', self.run_validate(root)[1])
        self.assertIn('upstream checks run', self.run_validate(root, '--upstream')[1])

    def test_verbose_reports_what_each_check_examined(self):
        rc, out = self.run_validate(self.copy(), '--verbose', '--upstream')
        self.assertEqual(rc, 0, out)
        for expected in ('3 sources', '2 domain tables', '2 log entries', '1 manifest rows', '3 extracted files',
                         '2 candidates', '1 map rows', 'commits checked'):
            self.assertIn(expected, out)

    def test_every_code_has_a_case(self):
        planted = {c[0] for c in CASES}
        self.assertEqual(len(planted), len(CASES), 'a code has two cases')
        self.assertEqual(codes_in_source() - planted, set(), 'codes the tools can report but no case plants')
        self.assertEqual(planted - codes_in_source(), set(), 'cases for codes the tools no longer report')

    def test_every_report_call_names_a_code(self):
        src = (TOOLS / 'validate.py').read_text(encoding='utf-8')
        calls = re.findall(r"(?:rep|self)\.(?:error|warn)\(\s*([^'\s][^,]*),", src)
        # Report.error/warn themselves take `code`; every caller passes a literal or a DataError's code.
        self.assertEqual(sorted(set(calls)), ['e.code'], f'report calls with a non-literal code: {calls}')

    def test_no_silent_exception_handlers(self):
        """No `except ...: pass` or bare `except:` in the tools: a swallowed error is a silent pass."""
        for name in ('common.py', 'validate.py', 'build_registry.py'):
            src = (TOOLS / name).read_text(encoding='utf-8')
            self.assertIsNone(re.search(r'except[^\n]*:\s*\n\s*pass\b', src), f'{name} swallows an exception')
            self.assertIsNone(re.search(r'except\s*:', src), f'{name} has a bare except')

    def test_planted_defects(self):
        for code, level, args, mutate in CASES:
            with self.subTest(code=code):
                root = self.copy()
                patch = mutate(root, self.shas)
                if callable(patch):
                    rc, out = self.run_inprocess(root, args, patch)
                    strict_rc = self.run_inprocess(root, args + ['--strict'], patch)[0]
                else:
                    rc, out = self.run_validate(root, *args)
                    strict_rc = self.run_validate(root, *args, '--strict')[0]
                tag = 'ERROR' if level == 'error' else 'WARN '
                self.assertRegex(out, rf'(?m)^{tag} \[[^\]]+\] {re.escape(code)}: ',
                                 f'{code}: not reported as {level}:\n{out}')
                self.assertEqual(strict_rc, 1, f'{code}: --strict run did not fail:\n{out}')
                if level == 'error':
                    self.assertEqual(rc, 1, f'{code}: run did not fail:\n{out}')
                else:
                    self.assertEqual(rc, 0, f'{code}: a warning alone failed the run:\n{out}')
                    self.assertNotIn('ERROR', out, f'{code}: the warning case also produced an error:\n{out}')


if __name__ == '__main__':
    unittest.main()
