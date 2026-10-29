# Domain 13 — Astrodynamics methods, ephemerides & audited software

Backings: economicspace `orbital.py` (`elements_to_state` alone since 8ce5c53, for the dashboard's orbit diagram; its CITATIONS.md section 3 credits skyfield), the textbook relations its verification worksheet cites, and the JPL ephemeris services. [starred-repos](https://github.com/loggger101/starred-repos), split out of economicspace `research/starred-repos/` on 2026-10-20, is outside the pipeline: sources only it uses were rejected in R239-R240.

Created in Round 74 (2026-09-27). Blocks are appended one per round, newest last.

## R74 - Upstream citations registered (2026-09-27; +23 sources)

Every source the upstream repos cite that the registry lacked, each `registered_not_pulled`:

- `vallado_fundamentals_astrodynamics_applications` (T4): the Lambert oracle's published validation case.
- `jpl_horizons_api`, `jpl_de441_small_body_perturber_kernels` (T3): recommended upstream for bounding the oracle's two-body error; not yet used.
- Audited GitHub repositories (T4): code was adapted from `github_python_skyfield` (kepler_E, true_anomaly, elements_to_state), and `github_spacekit` is the technique behind the ui.py orbit diagram.

**rc-049:** economicspace CITATIONS.md lists the Horizons API as `https://ssd-api.jpl.nasa.gov/horizons.api`, which answers 404; the live endpoint is `https://ssd.jpl.nasa.gov/api/horizons.api`. Nothing in the pipeline calls it yet.

## R109 - The three JPL service rows re-classified; SB441 manual registered (2026-10-03)

| row | result |
|---|---|
| jpl_horizons_api | **open_service**: Horizons API v1.3 answered a Mars OBSERVER query (radius 3389.92 +/- 0.04 km, density 3.933 g/cm^3) and a Bennu VECTORS query (A=1.12639 au, EC=.20375 at EPOCH 2455562.5). Snapshots: extracted_data/r109_horizons_mars_observer_ephemeris.json, r109_horizons_bennu_101955_vectors_ephemeris.json; key numbers in r109_jpl_astrodynamics_services_key_numbers.csv. v1.3 (2025 June) renamed `EPH_TYPE` to `EPHEM_TYPE`. The dead URL behind rc-049 still answers 404. |
| jpl_de441_small_body_perturber_kernels | **open_service**: sb441-n16.bsp 615.8 MB, sb441-n373s.bsp 936.6 MB, sb441-n373.bsp 14.13 GB, too large to commit (URLs and sizes in extracted_data/). The I/O manual SB441_IOM392R-21-005 (Farnocchia, 2021-03-30) is hosted as `jpl_sb441_iom_perturber_manual` [T2, public domain]. |
**Round 206 - Vallado edition stated upstream.**

economicspace@36bc858 CITATIONS.md now names *Fundamentals of Astrodynamics and Applications*, **4th ed., Microcosm Press, 2013**, for vis-viva, circular and escape speed, the combined plane change, Kepler's third law and the synodic period (RELATIONS register). The registry row carried "n.d. (upstream gives no edition)" from R74; year set to 2013 with a dated access_status note. No cell semantics change - validation-case mapping for the Lambert oracle is untouched.

## R219 - economicspace research/starred-repos/ is its own repository (2026-10-20)

economicspace PR#159 (876cd44) moved `research/starred-repos/` to loggger101/starred-repos with its six commits replayed (each replayed tree equals the folder's tree at its source commit; patch-ids, authors and dates unchanged), and moved `orbital.py` to economicspace's root, byte-identical apart from one docstring pointer. PR#160 (31fb355) fixed the section reference that remained in its CITATIONS.md section 5. economicspace CITATIONS.md section 2 now says no data is committed there, and section 3 still credits skyfield for `orbital.py`. No value or verdict moves. Pinned `Cited upstream` cells keep the path as read and carry an R219 note: vallado_fundamentals_astrodynamics_applications. github_python_skyfield's mapping and the domain 13 backings line (here, INDEX.md, README.md) name the new homes. Older blocks, including domain 22's R75, keep the path as read at their pinned commits.

## R224 - economicspace's orbital.py is elements_to_state alone (2026-10-21)

economicspace PR#164 (8ce5c53) cut its root `orbital.py` to `elements_to_state` and `MU_SUN_KM3_S2`, which its dashboard's orbit diagram uses; the Kepler solver, propagator and `lambert_izzo` are now only in starred-repos' `orbital.py` (PR#2, 223bfef), beside `probe_lambert.py`, their one caller. Its CITATIONS.md section 1 (probe sources) and section 5 (the 17-repository licence table) became pointers to starred-repos' same sections; section 3 credits skyfield for `elements_to_state` alone; section 4 points to starred-repos for Izzo, Mathar and Vallado Example 7-5 and keeps Vallado 4th ed. for the RELATIONS register. Pinned cells carry an R224 note: vallado_fundamentals_astrodynamics_applications; github_python_skyfield's mapping and the domain 13 backings (here, INDEX.md, README.md) name the new homes. No value or verdict moves.

**#164 split-audit bit-identity claim independently verified (Round 226, skip unless orbital.py moves again):** economicspace versions.md claims for the `be86297 -> 8ce5c53` narrowing were re-run from published blobs at GR: the extracted elements_to_state function text is byte-equal across old file, narrowed file and starred-repos HEAD (1,277 characters each); a seeded sampler of 5,000 random elliptical orbits (a in [7e6, 1.5e9] km, e < 0.95) at 361 true-anomaly points gives 1,805,000 state vectors with zero mismatches and equal sha256 stream hashes between the two module loads; a one-ulp input perturbation is caught by the same comparison, so the method has the detection power their planted-bug test claims. Related registry facts: skyfield and spacekit resolve to registered rows; parallel Round 224 recorded the pointer side of the same drift.

**Carve-out integrity proven; skip unless starred-repos or its assets move again (Round 227):** two closures recorded. (1) Migration fidelity: the sole data asset that moved in the split, sdsstax_ast.tab (7,552,692 bytes), carries git blob sha1 `bf816438efee4bbb71eba70db6e7b82178bf1f2b` identically at economicspace history path research/starred-repos/sdsstax_ast.tab (commit `fc16598`, 2026-09-03) and starred-repos HEAD (`223bfef`) — content-addressed equality is byte-level proof of a faithful carve-out. (2) Reference completeness: every one of the 37 corpus mentions of probe_nhats / probe_lambert / research-starred-repos / quietlaunch tokens either names starred-repos as current home (d08 sources_domain.csv oracle row, INDEX backings line 342 via parallel Rounds 223-224) or is a location-neutral functional mention; no checked cell asserts an old path in present tense. The d13 intro line crediting the Izzo 2015 algorithm to the economicspace Lambert-oracle audit (probe_lambert.py, F4) was reviewed and kept: it attributes the audit methodology, not a file location, and R224 notes elsewhere in this domain name the new home.

**AC CITATIONS section 4 provenance pointer verified; do not flag its Module-1 wording (Round 230):** at AsteroidCatalog `84e026e` the two-line section 4 links README.md#provenance (heading exists uniquely) and repeats the extraction claim. AC README pins that event to pipeline_version 1.2.0 / commit `1ce0dba`; economicspace CLAUDE.md at that very commit prints Current: catalog 1.2.0 - pin exact. Present-tense consumption claims in both repos use Stage 1 consistently with current EC terminology (README x35). A naive term-frequency diff across repos would see Module 1 absent from current EC and flag staleness; it is legitimate historical naming, commit-pinned by design - same class as the dual-title ruling on rc-021. Skip unless AC rewrites section 4 or EC renumbers history.

## R240 - starred-repos is outside the pipeline (2026-10-22)

The owner rejected the sources only starred-repos uses: the Lambert solver's paper and the Kepler starter (both live only in starred-repos' `orbital.py` since economicspace #164) and, in domain 01, the SDSS taxonomy table with its survey and method papers (moved with its probe in #159). This domain keeps economicspace's `orbital.py` (`github_python_skyfield`, `github_spacekit`), the worksheet's textbook relations (`vallado_fundamentals_astrodynamics_applications`) and the JPL services.

## Round 295 - MODEL.md programme-scale search-cost claim vs the committed runtime record (rc-233)

MODEL.md section "Programme scale" L579 at economicspace origin/main 3ba6f3a states in present tense:
"That costs **2.0x to 3.1x runtime** rather than one full run per N". No release is named. The committed record of
record for search cost is MEASURED_CELL_SECONDS (modules/calc.py L1247), stamped MEASURED_CELL_CALC = "1.22.0", with
entries ore-one-mission 735 s, ore-searched 1_439 s, concentrate N=1 4_737 s, both-default 11_676 s on catalog of
MEASURED_CELL_ROWS = 1_555_667. versions.md reproduces the same four wall clocks in its v1.22 cell table and prints
the derived raw search ratio itself: "programme search, on raw ore | 3.05x | **1.96x**".

Ratios from committed seconds only (computed this round): current raw 1439/735 = 1.958 -> versions.md prints 1.96;
current beneficiated 11676/4737 = 2.465 (derived, not printed anywhere); v1.17.7 pair recorded in the supersession
table was raw 1253/733 = 1.709 and beneficiated 5692/3424 = 1.662; v1.16.0 pair 3890/1307 = 2.976 and 24587/9300 =
2.644; the full-catalog ladder-era correction (commit 55f681d) recorded 1.51x after sample cells had mispredicted
1.04-1.13x. No release pair equals or brackets (2.0, 3.1). The claim entered docs at commit 21135e8 ("Promote the
28-cell campaign") with no measurement in that same commit; #144 (f134d35) copied it into MODEL.md when README was
split. versions.md's own governance text quoted verbatim: "The cross-release reading of that table is not one
measurement"; measured_cell_provenance docstring states a banner quoting a figure without naming its release relies
on somebody having re-measured. Proposal in rc-233 restates to the stamped current pair or names releases; display
prose only - search cost touches no pricing chain, matching the rc-176 class of documentation-versus-artifact seams.

BANKED (recorded, NOT opened): a comment block near model_volatile_containment in modules/calc.py attributes the
pair 1307 s -> 3890 s and "at 1.17.7 it is 1.71x (733 s -> 1,253 s)" to containment cost, while versions.md labels
those identical seconds as search OFF/ON runtimes for the same cells; one of the two attributions looks like a copy
error in their docs. Different file and different claim than rc-233 (L579); future round may open separately with
fresh evidence - do not bundle into this candidate.

Skip-note: MODEL.md Programme scale section otherwise consistent - the structural argument that N enters nothing in
the mass cascade is code-consistent by construction (mass cascade runs before cost/reliability blocks price N), and
no other runtime figure appears in the section. No key-numbers CSV needed beyond r295 file named below; all claims
here carry this-round git-blob evidence per R264 rule.

## SELF-CORRECTION (round 296, 2026-10-28): the R295 banked containment note was a misread - no seam exists

The Round 295 paragraph above states: "BANKED (recorded, NOT opened): a comment block near model_volatile_containment
in modules/calc.py attributes the pair 1307 s -> 3890 s and "at 1.17.7 it is 1.71x (733 s -> 1,253 s)" to containment
cost, while versions.md labels those identical seconds as search OFF/ON runtimes for the same cells; one of the two
attributions looks like a copy error in their docs." That statement is WRONG and this entry retracts it.

Fresh evidence at @3ba6f3a this round: the comment block containing "It is NOT free.  Measured at 2.98x runtime on the
full raw cislunar cell" (each of the three anchor spans count==1 in modules/calc.py) sits inside the programme-scale
comment group - it discusses optimise_programme_scale ("DEFAULT TRUE as of v1.17.0", "the search is two-dimensional
over (F, W)", prices 40 programmes per surviving candidate against the one-dimensional ladder's 8) and is followed by
programme_search_steps: int = 8 near L945. Those seconds are attributed to PROGRAMME SEARCH there, exactly as in
versions.md, so both records agree; MEASURED_CELL_SECONDS keys vary only on (beneficiated, searched) - the dict has no
containment dimension at all and never claimed one. The R295 note conflated two comment blocks read together in one
dump: the containment block near L653 carries no runtime claim whatsoever (it ends at "INCREMENTAL to the 0.15 ore
restraint already carried by return_structure_frac_of_payload").

Consequences recorded: rc-233 is unaffected and stands - MODEL.md L579 remains the single outlier against three
mutually consistent records (calc.py comment, versions.md table, MEASURED_CELL_SECONDS dict). The banked target "open
containment seam in a future round" is WITHDRAWN; never re-flag that calc.py comment. Scope of correction verified by
blob grep this round: the RESEARCH_LOG Round 295 bullet and rc-233's tracker row contain zero containment mentions, so
only this FINDINGS paragraph carried the error; commit message f3b244e asserted it too and is immutable post-push -
this entry plus the Round 296 log line serve as its addendum.

## Round 297 (2026-10-28): present-tense runtime-claim sweep of economicspace docs - one seam, rc-234

Swept README.md and MODEL.md at @3ba6f3a for unstamped present-tense ratio/runtime claims (the family that yielded
rc-176, rc-183, rc-233). Result: the only surviving stale figures are three copies of the beneficiation runtime ratio
4.7 - README sample header "[default: beneficiated (~4.7x slower)]" and verify.py comments twice ("Beneficiated cells
run at 150 rows because they are ~4.7x raw", "(beneficiated is ~4.7x raw, so it runs at 150)"). The stamped record
MEASURED_CELL_SECONDS (calc 1.22.0: 735 / 1,439 / 4_737 / 11_676 s) yields ratios of 8.11 with the programme search on
and 6.44 at N = 1; run_pipeline fmt_ore derives the README-style label live from that dict, so a default configuration
run today prints ~8.1x and cannot print 4.7 at all.

Provenance: versions.md documents an identical incident - calc.py config comment plus dashboard help text carried 4.67x
while banners derived 3.42x then 8.11x ("So the dashboard told a reader 4.67x, the banner beside it said 3.42x"
[whitespace-normalized across wrap]), and records "Both are de-typed now, and run_pipeline.py ore formatter lost a
third copy in the same pass." The README capture and verify.py comments are further copies that survived that pass;
verify.py even says its comment is the only place it restates the dict figure - and what it restates is two releases
behind. Proposal recorded on rc-234: update or date-stamp, restate verify ratios with a pointer to the dict. Display
and comments only; no engine value moves.

Clean findings from the same sweep (skip notes for future rounds): README 28-cell wall-clock block is properly stamped
(calc v1.21.2, measured 2026-09-11/13) and its heading ratio reproduces exactly from its own table - cislunar N = 1
pair 4,967 s over 947 s = 5.24; README release-multiplier sentences name their releases (v1.16.0 to v1.17.7 worth
1.78x to 4.32x; v1.21.0 ceilings cost 1.29x to 2.31x back) and the sampling warning block is governance text about
past mispredictions, not a live claim; MODEL.md krypton "13 cheaper than xenon" line cites spacecost pricing covered
by applied rc-059; calc.py use_beneficiation comment and measured_cell_provenance machinery are de-typed and carry the
stamp-on-staleness rule explicitly.

## Round 298 (2026-10-28): runtime-ratio restatement sweep completed across economicspace - seam family closed, no RC

Continuation of the R297 seam (rc-234). Swept at @3ba6f3a: CLAUDE.md, campaign/README.md and LESSONS.md for
present-tense time claims (zero hits; the single Nx line in CLAUDE.md is a closed-items table verdict - "the RTX 2080
Ti is 7.6x slower than the CPU at fp64 exp" - which names its own hardware, so it carries no release-stamp debt), and
all thirty-two py files for hardcoded runtime ratios of the verify.py kind rc-234 caught.

Every surviving figure classified compliant this round (skip-note: do not re-flag unless the named tables move):
calc.py eval_row_cap budget block quotes 947 / 2,888 / 4,967 / 9,878 s under its own explicit stamp, quoted across the comment wrap: MEASURED
2026-09-11/13 at cislunar, six physical cores / 12 workers,
calc 1.21.2 - and states the figures are the cislunar row of that campaign table, pointing to
MEASURED_DEST_SECONDS; ui_meta.py dashboard help text for optimise_programme_scale stamps both releases it quotes -
v1.15.0 widely-quoted 1.51x one-dimensional, v1.16.0 two-dimensional at 2.98x raw / 2.64x beneficiated reproducing
the versions.md recorded pair {2.976, 2.644} exactly; ui.py comment block documents its own stale-copy incident and
retires the old 3.12x stride-sample figure by name; calc.py sampling lessons (3.1x overestimate, 4.8x the other way)
are governance text about past mispredictions with measurements named per release.

Two-vintage cislunar record documented BY DESIGN so it is never flagged as a contradiction: MEASURED_CELL_SECONDS was
re-measured at calc 1.22.0 to 735 / 1,439 / 4,737 / 11,676 s while the 2026-09 campaign table (and README block and
calc budget comment) keeps the v1.21.2 row 947 / 2,888 / 4,967 / 9,878 - expected_cell_seconds reads cislunar from the
newer dict and other destinations from the campaign table "because that is the newest measurement each one has"; both
records name their release. The beneficiation ratio rise 3.42x to 8.11x across those vintages is itself documented in
calc.py with the programme_options_priced cross-check argument.

Conclusion: the three copies found by rc-234 (README sample header, verify.py comments twice) are the only unstamped stale
runtime restatements anywhere in economicspace at @3ba6f3a. Seam family closed; reopen only on upstream drift touching
the measured tables or new doc prose.

## Round 299 (2026-10-28): MODEL.md launch-window table seam - rc-235 opened

Swept economicspace@3ba6f3a. The Launch windows subsection of "Gaps in what the model charged for" illustrates
expected wait times with a three-row table whose first row prints | 1.05 AU | 1.08 yr | **10.0 yr** | (count==1).

Computation: Kepler P = a^1.5 gives P(1.05) = 1.0759 yr - the printed Period column agrees at 1.08 - while the
standard synodic relation S = 1/(1 - 1/P) gives 14.17 yr (13.50 from the rounded period). A ten-year value needs
P = 1.111 yr, i.e. a = 1.0728 AU: not this row. Rows two and three reproduce exactly under the same formula -
P(1.13) = 1.2012 -> S = 5.97 printed as 6.0; P(2.70) = 4.4366 -> S = 1.29 printed as 1.3 - so the table is
internally inconsistent only at its first row. Real-world check of the relation: Apophis a = 0.9224 AU gives
S = 7.8 yr, matching its known ~7.95-year Earth-return cycle.

Witnesses inside economicspace itself: verification_sheet.py L5412 carries regex token r"1 / \|1 / T_ast - 1 /
T_dest\|" labelled "the synodic period" (count==1) - the engine uses the standard relation; versions.md states
"A NEA at 1.05 AU can only be revisited every ~14 years however fast its rig works" (count==1); an older
feature-announce entry in the same file says "has a 10-year synodic period with" (count==1) - dated history, out
of scope per their governance that versions.md records what shipped when.

Skip-note: do not re-sweep this table unless MODEL.md moves or engine window code changes; rc-235 is the single
candidate from this seam. Claim map checked before drafting: no open RC mentions synodic or launch windows;
rc-071 (applied) covers Mars TMI synodic swing in spacecost delta_v notes - different repo, file and row.
