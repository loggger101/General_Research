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

## R206 - Vallado edition stated upstream (2026-10-19)

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

## R295 - MODEL.md programme-scale search-cost claim vs the committed runtime record (rc-233) (2026-10-28)

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

Extracted data: `extracted_data/r295_campaign_search_runtime_key_numbers.csv`.

## R296 - Self-correction: the R295 banked containment note was a misread - no seam exists (2026-10-28)

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

## R297 - present-tense runtime-claim sweep of economicspace docs - one seam, rc-234 (2026-10-28)

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

Extracted data: `extracted_data/r297_beneficiation_label_key_numbers.csv`.

## R298 - runtime-ratio restatement sweep completed across economicspace - seam family closed, no RC (2026-10-28)

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

## R299 - MODEL.md launch-window table seam - rc-235 opened (2026-10-28)

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

## R300 - MODEL.md delivery-table currency proof and the hardware-share band seam - rc-236 opened (2026-10-28)

Reproduction at exactly what economicspace consumes: requirements.txt pins spacecost @ v0.14.0 (= aa1118c; MIT LICENSE present).
Extracted that tag with git archive and called the module directly (read-only, no edits anywhere): every cell of the MODEL.md
delivery table reproduces - costs within display rounding ($2,555 / 5,168 / 8,462 / 7,236 / 48,226 / 9,154 / 186,306), kg-in-LEO
ratios to two decimals (1.86 / 2.95 / 2.54 / 5.28 / 3.17 / 10.61), stage-hardware amounts exact ($414 / $937 / $742 / $34,737 /
$1,046 / $159,209); downlegs compute to $25,410 (LEO) and $27,317 (cislunar), matching the printed ~$25,400/~$27,300; MARS_EDL
fraction 0.3 as quoted. Tip 860bef9 gives identical numbers (delivery.py unchanged between tag and tip).

The one defect: prose band "against 11-12% at the orbital destinations" vs live shares gto 8.02%, cislunar 10.26%, geo 11.07%,
mars_orbit 11.43%. The GTO and cislunar rows of the same table print cells that any reader can divide to get 8% and 10.3%; only
GEO and Mars-orbit sit inside the stated band. Surface figures are accurate (72.03%, 85.46%). Opened as rc-236 [wording].

Two readings banked so future rounds do not false-flag:
- Single-stage claim "12.81 kg in LEO per kg landed" for the whole 6,100 m/s reproduces exactly via stage_mass_ratio(6100, isp=465,
  dry=0.2) - lander dry class; tug-class delta=0.1 gives 5.54 instead. The prose does not state which class it assumed; the claim is
  valid under a defensible reading (the stage that lands must be built like a lander), so never flag without checking both classes.
- Mars-orbit period claim: the 250 x 33,793 km ellipse gives P = 88,582 s against the sidereal sol of 88,642.7 s - within one minute
  as claimed (against the solar day it would be ~193 s off; sidereal is the right comparison).

Skip-note: do not re-sweep the delivery table unless MODEL.md tables or the pinned spacecost move; rc-236 covers the band sentence.
Claim map checked before drafting: rc-185 (open) matched only on substring noise - it targets LOX component price in spacecost
propellants, different repo/file/claim.

Extracted data: `extracted_data/r300_delivery_chain_shares_key_numbers.csv`.

## R301 - economicspace pin enumeration and catalog shape claims verified at 3ba6f3a (skip-note) (2026-10-29)

The README quantitative contract was last swept in full at be86297 (R231); pins moved since, so the enumeration was re-verified against published blobs only. spacecost v0.14.0 confirmed in all five places the README names: requirements.txt URL pin, modules/_runtime.py PIP_SPEC entry, README itself (L154), CLAUDE.md (L503) and CITATIONS.md (L297); tag v0.14.0 dereferences to commit edfd5bec (annotated tag object aa1118c). Catalog pin data-2026-10-21b confirmed at modules/catalog.py L121 and price release prices-2026-10-07 at modules/mineral_value.py L104. README L536 shape claims reproduce exactly on the R286-audited -21b parquet: rows 1,575,889; columns 102; comp_phases and comp_phases_detailed both present (comp_phases new at contract 1.7.0 per AC enrich.py comment at the release tag). README L1221 measured-diameter sentence matches the -21b manifest counts R286 reproduced from the shipped parquet; its single data-2026-09-29c mention (L1092) is a dated past-tense run record, accurate by design. Skip unless these pins move or MODEL.md prose changes.

## R303 - economicspace CITATIONS.md verified complete at tip 3ba6f3a (skip-note) (2026-10-29)

Work-level pass over the whole file plus an accession-token pass: every named work resolves to a registry row and every NTRS, DOI or OIG token appears in one. The only unregistered identifier is arXiv:2108.03215, which sits on an explicit disclaimer sentence stating that the Izzo 2015 Lambert solver and its Kepler starter live in starred-repos orbital.py rather than economicspace - out of scope per the R227 carve-out convention (starred-repos carries its own CITATIONS.md, blob-verified faithful at R227). The previous work-level sweep was anchored pre-#154; this round closes drift #154 through #187. Do not re-sweep this file unless it changes at a new tip.

## R306 - spacevalue CHANGELOG claim battery fully verified at pinned tag v0.2.0; skip-note for this seam (2026-10-29)

Every falsifiable numeric or cross-repo claim in the package CHANGELOG was tested against surviving committed bytes, all five repo tips static (spacecost 860bef9 / economicspace 3ba6f3a / AsteroidCatalog 92f7739 / spacevalue main 873b91c ahead of pin by tests-only commits; no tag newer than v0.2.0). Results: package version string equals 0.2.0 at the tag and all eight committed fixture tables carry pipeline_version stamp 1.17.0, matching the declared data contract; exactly eight destination CSVs are committed under tests/data/prices-2026-10-07/ as claimed; economicspace versions.md contains the named Stage 2 changelog section that the CHANGELOG points to for contracts before 1.17.0; the consumer-contract claim of twenty-five imported cargo names reproduces exactly - the from-import block in economicspace modules/calc.py at tip lists precisely those twenty-five distinct names; the golden recording holds thirteen distinct cells across sixteen recorded functions and 4,858 calls as stated (default raw, default benef+search, detailed_off benef, elasticity raw and benef+search, phases_off both, refinery_off both, single_mission both, surplus_wall, unbounded). The headline byte-for-byte claim was verified directly: economicspace tracks frozen Stage-2 tables under campaign/stage2/mineral_value-1.15.0/ for exactly seven destinations (no gto - that destination joined later per the #141 history at R203), and comparing each against the spacevalue fixture leaves precisely one differing column, pipeline_version, with 59 rows giving exactly 59 differing cells per table; every value cell including catalog_date is identical. The claim of equality for all eight destinations against a mineral_value 1.16.0 build has no surviving committed bytes on the economicspace side (zero files under mineral_value-1.16.0/, publication having moved to spacevalue), so that half stands as their CI-era assertion; the CHANGELOG wording is accurate about which seven are byte-frozen. The requires-python 3.12 rationale was reproduced mechanically on this machine: a mixed-magnitude float list summed naively gives bits 402f20345f3459f1 under CPython 3.11.16 (uv-managed) versus 402f20345f1ac05a under system 3.13, the latter equal to math.fsum - pre-3.12 builtin sum is genuinely uncompensated, so one-bit yield differences at lower interpreters are real; demonstrated at mechanism level on a synthetic list, not from their exact yield inputs. Registered spacevalue_release_record_v0_2_0 T4 in d13. Skip-note: this seam is fully mined while tips hold - do not re-sweep unless spacevalue tags beyond v0.2.0, economicspace unfreezes Stage-2 tables, or the CHANGELOG changes.

Extracted data: `extracted_data/r306_spacevalue_release_record_key_numbers.csv`.

## R313 - A phase lookup overwrites the refinery composition-cache key (2026-11-01)

`spacevalue_refinery_composition_cache_record_2026`: at spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011,
`spacevalue/cargo.py` L476 obtains a composition tuple and L478-481 looks up its
refinery result. The phase loop reassigns `key` to a phase name at L492; L507
therefore stores the result under that string instead of the composition tuple.
`_composition_key` L654-657 explicitly sends unsupported scalar types down
"the uncached path". Its None result is also overwritten by the phase loop,
so the final write can refer to `entries` without having initialized it.
The cargo blob is identical at the consumer pin v0.2.0. Economicspace
`modules/calc.py` L8150 calls `asteroid_refinery` for each evaluated body.

The original complete cargo module was executed against the committed cislunar
price fixture, switched to gross prices exactly as economicspace L1603-1608
does, with mappings assembled from AsteroidCatalog@66fb47a's taxonomy and
detailed-phase CSVs. All 32 populated reference compositions miss the refinery
cache on each of three identical-value calls. For C, `_phase_terms` calls are
12,12,12; the tuple's refinery slot remains empty and a `silicates` string-key
entry holds the result. Across the 33 reference rows, including Unknown,
99 calls invoke `_phase_terms` 1,188 times.

Renaming only the loop's two `key` references to `phase_key` in an in-memory
copy changes C's counts to 12,0,0 and the aggregate to 396. Every returned
phase energy and raw weighted sum is bit-identical for all 33 rows. Unknown
returns zero and caches normally on both versions because its phase loop is
empty. Removing detailed phases from C gives counts 5,5,5 versus 5,0,0;
switching the refinery off returns None on both versions.

A hand-built C mapping with its finite metal fraction written as
`Decimal("0.01")` has an uncacheable key. The original raises
`UnboundLocalError` at L507; the same variable rename returns the ordinary
float-input energy result bit for bit without caching it. This control is an
API-input witness, not an observed catalog-loader failure.

Verdict: a key-shadowing defect defeats composition memoization on populated
rows and breaks the documented uncached path. `rc-243`: preserve the
composition key and use a separate phase lookup variable. Full-catalog wall
time and ranking effects were not measured; no price or energy value change
is proposed. `extracted_data/r313_refinery_composition_cache_witness.csv`.

## R325 - The prefilter report counts only the first stage (2026-11-02)

Source `economicspace_prefilter_probe_stage_coverage_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`;
original spacecost@860bef9902aa67fec705875cd52fdb8e6def159f reference rows
and spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011 cargo functions and
recorded mineral-price fixture. The `_prefilter_probe` docstring says it
"Mirrors the loop nest in `evaluate_asteroid` exactly" (L8047), with the same
test so the printed rate describes the upcoming search. Its predicate at
L8080-8086 calls only `_combo_can_close`, the first-stage mass-budget test.
The real search also calls `_closes_carrying_its_own_stage` at L8326-8331
before entering `evaluate_combo`. The printed whole-filter kept/pruned
report at L8735-8741 uses the probe's incomplete count.

Fourteen original probe/search pairs use the original candidate builder,
actual vehicle/propellant rows and all 46 operational-cost rows, plus the
committed 2026-10-07 Earth-surface mineral fixture. The principal synthetic
body is 1e9 kg of silicates, density 2 g/cm3, a=1.2 AU, e=0.1 and rotation
5 hours. Explicit fallback delta-v is 6,500 m/s per leg before each
propellant's own low-thrust penalty. Aerocapture, ISRU, beneficiation,
programme search, launch windows and refinery are off to isolate the gate;
damping and low-thrust sizing retain their defaults except in named controls.
Observational wrappers call and return the unchanged numerical functions.

| original case | candidates seen | probe kept | pass both stages | evaluator entries |
|---|---|---|---|---|
| Falcon 9, electrospray | 1 | 1 | 0 | 0 |
| Falcon 9, PPT | 1 | 1 | 0 | 0 |
| Falcon 9, FEEP | 1 | 1 | 1 | 1 |
| Falcon 9, xenon | 1 | 1 | 1 | 1 |
| three vehicles, five propellants | 15 | 9 | 5 | 5 |
| Falcon 9, cold gas | 1 | 0 | 0 | 0 |

The mixed grid uses Falcon 9 reusable, Falcon Heavy expendable and Electron,
crossed with kerolox, xenon, electrospray, FEEP and PPT. All nine reported
survivors reach the real second-stage check, which rejects four, leaving
five evaluator calls. The printed counts therefore imply 60.0% kept and
six pruned, whereas the same original search keeps 33.3% and prunes ten.
The single electrospray and PPT cases imply 100% kept although neither
enters the evaluator. These are architecture counts before power-source
branching, not final viable-mission counts.

The electrospray discrepancy remains with operational-only propellants,
at a=2.5 AU, and the PPT discrepancy remains without damping. Low-delta-v
xenon/PPT and a 1,000 m/s kerolox control agree between probe and search.
Disabling electric-stage sizing also removes the electrospray count gap.
A xenon case at a=4 AU, e=0.8 passes both stages once but enters the evaluator
twice, for solar and RTG; it confirms that solver-call counts must not be
substituted for architecture counts. In total six of the fourteen cases
disagree. This is a synthetic test set, not a catalogue pruning-rate estimate.

Verdict: the report describes first-stage pruning as the entire prefilter,
contrary to its exact-mirroring contract. `rc-255`: include both stages or
label and report them separately. The diagnostic does not feed the optimiser;
these results establish no false rejection of feasible missions or changed
winner. `extracted_data/r325_prefilter_probe_stage_coverage.csv`.

## R327 - Duplicate rows can combine one measurement with another's sigma (2026-11-02)

Source `asteroidcatalog_duplicate_measurement_pairing_record_2026`:
AsteroidCatalog@66fb47aaeb17aa7e11c023773a39765c1aa793fb, `README.md` and
`asteroid_catalog/{merge,derive,validate,enrich,physics,release}.py`.
`deduplicate_catalog` says "each column takes the first non-null value"
(merge.py L49). It stably sorts duplicate rows by completeness, then calls
`groupby(...).first()` (L83-89). `_dedup_source` uses this before measured
fields are resolved (L635-646, L514 and L539). Consequently a missing sigma
on the preferred value's row can be filled from a different measurement.
The later resolver itself says "A sigma with no value to belong to says
nothing" (L323), but independent duplicate coalescing can already have
associated that sigma with another row's value.

Thirteen original fixtures execute deduplication, merge, H-based diameter
derivation, validation and enrichment. They use a synthetic join key,
a=2.3 AU, H=15 and S type. The preferred duplicate row has more populated
fields than its competitor, so it supplies the value under the documented
priority. For the principal mass case:

| stage | mass kg | sigma kg |
|---|---|---|
| preferred raw row | 1e13 | missing |
| less-complete raw row | 1e18 | 1e16 |
| combined source row | 1e13 | 1e16 |
| measured-source resolution | rejected | cleared |
| final enrichment | 2.931659606e13, derived | missing |

The synthetic pair appears in neither raw row. The mass screen's
`sigma >= mass` condition (L361-371) rejects it. Running the preferred row
alone retains its 1e13 kg measured mass. Reversing arrival order preserves
the same erroneous combination; the effect also occurs inside a supplement's
duplicates. Thus the active mass changes, rather than only its displayed
uncertainty. Missing uncertainty on the preferred row is already a supported
case in the original single-row path.

Other fixtures retain the value but borrow an unjustified small sigma:
1e13 kg mass takes 1e8 kg uncertainty from a different mass; 2.7 km diameter
takes 0.001 km from a 4 km measurement; H=15 takes 0.001 mag from H=20;
albedo 0.2 takes 0.001 from albedo 0.5. A diameter-less row's orphan sigma
can likewise become attached to another duplicate's diameter. A common
provider name does not make uncertainties of different measurements
interchangeable.

Thirteen in-memory diagnostics keep the original deduplication's value
choices and complementary fields, but take each measured field's sigma only
from the raw row that supplied that field. Every later numerical function
is unchanged. The three erroneous-rejection variants then retain 1e13 kg
with unknown sigma instead of substituting a 2.932-times larger class-derived
mass. Five other affected fixtures keep their values and clear the unpaired
sigma. Five controls preserve every final column: one row, a preferred
mass's own sigma, no sigmas, a preferred diameter's own sigma, and a genuinely
complementary diameter/sigma pair from the same row.

Verdict: independent column coalescing synthesizes unsupported measurement
pairs and can change physical screening decisions. `rc-258`: keep measured
values and their uncertainties together during duplicate combination.
These are synthetic fixtures, not a measured published-catalog duplicate
frequency or ranking effect. The NEOWISE-specific averaging of repeat fits
was not changed by the diagnostic.
`extracted_data/r327_duplicate_measurement_sigma_pairing.csv`.

## R329 - Non-finite fields survive validation and the physical-row check (2026-11-02)

Source `asteroidcatalog_nonfinite_catalogue_fields_record_2026`:
AsteroidCatalog@66fb47aaeb17aa7e11c023773a39765c1aa793fb,
`asteroid_catalog/{merge,derive,validate,enrich,physics,taxonomy,release,build}.py`,
with the configuration and numeric-column helper. Diameter validation uses
`diam.isna() | (diam <= 0)` (validate.py L79-88); the semi-major-axis check
uses the same form (L98-103). Positive infinity passes both. Merge's positive
ratio filter also retains it (merge.py L329-330). Diameter derivation marks
any positive input measured (derive.py L356-360); its comment, "Guard against
a non-finite result reaching the catalog", applies to the newly derived H
result at L406-408, not every source diameter. The physical-row helper promises
"Every physically impossible value in a catalog" (release.py L152), but its
density bounds and identity comparisons (L169-180) do not flag NaN results.

Eighteen synthetic single-body fixtures execute the original merge, derive,
validate and enrich sequence (build.py L90-108), then `physical_problems` on
retained frames. They use the unchanged default CONFIG and a source S type;
normal values are D=2.7 km, H=15 and a=2.3 AU. Principal outcomes:

| changed input | final composition | final mass kg | physical-row problems |
|---|---|---|---|
| none, normal control | S | 2.782618569e13 | none |
| a=positive infinity, numeric or string Infinity | D | 1.236719364e13 | none |
| D=positive infinity, numeric or string inf; H missing | S | positive infinity | none |
| D=1e120 km, finite; H missing | S | positive infinity | none |
| D and mass=positive infinity; H missing | S | positive infinity; density NaN | none |

For infinite a, the source label remains S but the rule a>5.5 AU selects the
D composition row (enrich.py L211-218; physics.py L219). Its 1.2 g/cm3
estimate replaces S's 2.7 (taxonomy.py L189-193,L366-370), giving exactly
4/9 of the normal mass at the same diameter. Infinite diameter without H
evades the H/albedo screen because the implied albedo is missing (merge.py
L350-354). The finite 1e120 km case overflows the volume power (physics.py
L264-266), so screening input infinities alone is insufficient. Enrichment
writes the resulting infinite mass (enrich.py L347-355). In these cases
infinite mass over infinite volume yields NaN, and all physical-check
inequalities are false. Simultaneous infinite measured mass and diameter
also leave the reported density NaN. Runtime warnings are recorded separately
from the helper's empty problem lists.

Six cases retain non-finite critical fields. Twelve controls delimit the
finding: four missing/non-positive/unparseable a inputs and three missing or
non-positive diameters without H are rejected; five finite or repaired paths
are retained. In particular known H makes the earlier screen remove infinite
D and derive 2.747369371 km, while infinite mass with finite D is screened
and replaced by a finite class estimate. Finite D with missing H is valid.
An entirely absent a column retains the existing warning/legacy behavior
(validate.py L105-108), distinct from an invalid value in a present column.

Verdict: positivity tests and density comparisons do not ensure finite
critical fields. `rc-260`: finite input and post-computation validation.
These are synthetic robustness witnesses, not measured bad rows in the
published catalogue or ranking effects. The physical helper is the one
called by `check_release` (release.py L245-246); the complete release gate,
population floors and source-count requirements were not exercised or changed.
The extraction retains every intermediate frame and distinguishes numeric
infinity markers from input strings.
`extracted_data/r329_nonfinite_catalogue_fields.csv`.

## R333 - Reused propellant rows retain the first configuration's tank setting (2026-11-02)

Source `economicspace_propellant_cache_configuration_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`,
`README.md` and `MODEL.md`; spacecost@860bef9902aa67fec705875cd52fdb8e6def159f,
original launch/propellant/ops CSVs;
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011, `spacevalue/cargo.py`.
Sizing constants are described as functions of "(propellant row × config)
alone" (calc.py L3609-3610). `_tank_frac_per_kg` returns 0 when
`model_tank_mass` is False, otherwise the row's tank-per-litre divided by
density (L3629-3645; README.md L645 describes the switch). The solver
attaches that configuration-dependent tuple to its caller's row and later
reads it without checking the current flag (L6011-6016). `candidate_combos`
also attaches sizing and prefilter tuples for its own config (L7955-7964).

Eighteen complete original `evaluate_combo` sequences compare a reused
propellant dictionary with a fresh copy of the same physical source row
under the same final config. They retain actual Falcon 9 reusable,
kerolox/hydrolox and all 46 ops rows. The body is synthetic, 1e9 kg at
2 g/cm3; caller delta-v is 1,000 m/s each way, raw cargo is 100 USD/kg and
the programme is one mission. ISRU, aerocapture, refinery and boil-off are
off, isolating tankage. Representative final calls are:

| propellant | first flag -> current flag | reused tank ratio kg/kg | correct current ratio | reused payload kg | fresh payload kg |
|---|---|---|---|---|---|
| kerolox | True -> False | 0.026914468803 | 0 | 17,794.394348 | 18,501.069719 |
| hydrolox | False -> True | 0 | 0.097263455658 | 25,529.154868 | 22,835.390472 |

The kerolox call with tankage now disabled still carries 199.209996 kg of
return tank and 121.348916 kg outbound tank; its fresh disabled counterpart
carries zero. Hydrolox with tankage now enabled instead carries zero in the
reused call, versus 675.337997/341.799807 kg return/outbound in the fresh
call. The cached ratio, not the current flag, exactly explains each tank
mass through tank_mass=ratio*propellant_mass.

Both toggle directions fail for both propellants. A new configuration object,
editing the existing config in place, and shallow-copying the cached row
all preserve the stale coefficient. An initial infeasible call, made with
a deliberately oversized dry return vehicle, also leaves a tuple that can
affect the next otherwise valid call. Four same-setting row controls match
fresh results. Repeated stale calls are internally repeatable, so repeated
output alone does not establish that the current inputs were honoured.

Four complete `evaluate_asteroid` comparisons cover reused candidate lists.
The two cross-setting cases retain the same 706.675371 kg kerolox payload
difference; the two same-setting cases agree. Fresh `candidate_combos`
under the current config and omitting the optional combos argument produce
identical results in all four cases. These lists contain the same physical
candidate, so changed filtering is not needed for the discrepancy.

Twenty-two diagnostics recompute only the existing original sizing tuple
for the current config, and the original prefilter tuple for a reused
candidate list. Every result then matches the corresponding fresh call,
including field types, finite float.hex values and NaN positions. No
numerical helper or physical source field changes. Source tank coefficients
and all nominal rates remain fixed; different payloads can also change dig
time and cost, so those cost differences are not fixed-payload comparisons.

Verdict: row-attached constants outlive the configuration they depend on.
`rc-264`: validate or refresh cache dependencies, or apply the current tank
switch to configuration-independent cached physics. This finding concerns
reused input rows/candidate lists across settings. The standard build creates
fresh candidates per configuration and gives the correct setting in these
controls; no incorrect fresh-build result, population incidence, false-pruning
rate or catalogue ranking effect is claimed.
`extracted_data/r333_propellant_cache_configuration.csv`.

## R335 - Delta-v sum discards a better or uniquely feasible apsis (2026-11-02)

Source `economicspace_apsis_dv_sum_preselection_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`,
`README.md` and `MODEL.md`; spacecost@860bef9902aa67fec705875cd52fdb8e6def159f,
original launch/propellant/ops CSVs; spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011,
original cargo dependency and its 2026-10-07 Mars-orbit price fixture.
README.md L1030-1034 describes "the best mission found for it" across axes
including rendezvous apsis. `asteroid_transfer_options_km_s` supplies both
apsides (calc.py L2928-2942), but `asteroid_dv_options` keeps one per return
mode by smallest `dv_out + dv_ret` (L3321-3343), before any launcher,
propellant or mass/cost solve. It calls this the "best apsis already resolved
for each return mode" (L3302-3305). `evaluate_asteroid` only prices the offered
legs through its original objective (L8285-8350).

Sixteen complete consumer pairs retain the original numerical functions and
append the missing apsis to the original options. There are 31 corresponding
direct original `evaluate_combo` solves. The main synthetic body is 1e9 kg,
2 g/cm3, all silicates, a=1.1 AU, e=0.2, i=0 degrees and 8 h rotation.
Actual Falcon 9 reusable, kerolox and all 46 ops rows are unchanged. Cargo
is raw at a caller price of 100 USD/kg, N=1, Mars-orbit delivery and
propulsive return. ISRU, boil-off, refinery, WACC, reliability and learning
are off. The original analytic geometry gives:

| apsis | outbound m/s | return m/s | sum m/s | returned cargo kg | cost/revenue |
|---|---|---|---|---|---|
| perihelion, offered normally | 5,299.415825 | 2,311.393458 | 7,610.809283 | 109.987665 | 156,253.546915 |
| aphelion, discarded normally | 4,285.049316 | 3,949.887248 | 8,234.936565 | 243.995310 | 70,716.469558 |

Both options satisfy the 17,400 kg launch capacity. An independent rocket/
material balance at the same 100 kg returned cargo needs 17,325.415613 kg
at perihelion versus 15,717.482836 kg at aphelion, despite the latter's
larger delta-v sum. Cargo is mined at the target; the outbound manifest
carries rig, return vehicle, tanks and return propellant. The two burns
therefore act on different masses, and their unweighted sum is not the
mission objective. Independent solved-payload and outbound/return propellant
calculations match the original numerical outputs.

At the nearby i=2 degrees, the normally chosen perihelion still has a smaller
sum, 8,255.527636 versus 8,388.784903 m/s. Its zero-cargo stack already needs
18,048.165689 kg, so the original full search returns None. The discarded
aphelion option returns 190.311790 kg within the same 17,400 kg capacity.
A second synthetic orbit, a=1.15 AU, e=0.25, i=1 degree, likewise changes
from no mission to an accepted 133.482947 kg aphelion delivery.

Nine pairs improve, including those two restored feasible results. Nearby
orbital cases and a tank-disabled case retain the effect. A fixture keeping
the committed Mars-orbit silicates price, 2,082.429580 USD/kg, improves
cost/revenue from 7,503.425249 to 3,395.863669 at the same physical loads.
Turning the existing combo prefilter off reproduces the main normal and
augmented results exactly, locating this miss in the earlier apsis choice.
Every changed-case delta-v lies strictly inside the original floors and cap;
no clipping, geometry correction or price/rate change produces the difference.

Seven controls retain the complete original result: aerocapture available,
cislunar delivery, circular orbit, fixed reference delta-v, missing-element
fallback, Falcon Heavy expendable and hydrolox. The last two retain
perihelion as the best mission under their original source mass/cost rules;
there is no globally preferred apsis. Every original and augmented consumer
repeats with identical full-result type/float.hex signatures, and every
augmented winner has the same objective as the best direct original solve.

Verdict: unweighted delta-v-sum preselection can discard a better or the only
feasible mission before the physical/economic search. `rc-266`: carry both
apsides into the original mission search and select on its objective, retaining
existing options and fallback behaviour. This comparison holds the analytic
trajectory approximation unchanged; MODEL.md L1286-1294's separate accuracy
limitations are not corrected here. Actual-population incidence, catalogue
rankings and true trajectory-optimal missions were not measured.
`extracted_data/r335_apsis_dv_sum_preselection.csv`.

## R337 - Designation case can change the body or lose its measurement (2026-11-02)

Sources `asteroidcatalog_designation_case_identity_record_2026` and
`jpl_sbdb_small_body_database`: AsteroidCatalog@66fb47aaeb17aa7e11c023773a39765c1aa793fb,
original designation/identity helpers and complete build; live SBDB API
identity objects queried by `sstr=3568`, `sstr=1999` and `sstr=1999 KW4`.
JPL identifies these as 3568 ASCII (1936 UB), 1999 Hirayama (1973 DR),
and 66391 Moshup (1999 KW4), respectively. Its returned shortname for the
first is exactly `3568 ASCII`.

`_extract_canonical_designation` classifies a numeric prefix followed by a
capital/lowercase pair as number-plus-name (designations.py L75-87).
`_designation_key` calls it before folding case, while claiming that
"upper-casing stops case variation fragmenting a group" (L107-113).
The two classifications fail in opposite directions:

| incoming string | original canonical/key behaviour | independently identified target |
|---|---|---|
| `1999 Kw4` | truncates to `1999` | `66391`, via `1999 KW4` |
| `3568 ASCII` | retains the whole string, no numeric/name alias match | `3568` |
| `(3568) ASCII` | becomes the same unmatched `3568 ASCII` | `3568` |
| `1936 Ub` | truncates to `1936` | `3568`, via `1936 UB` |

Eighteen resolver fixtures give seven failures and eleven controls. The
capitalisation/spacing variants are constructed inputs, except the exact
JPL shortname `3568 ASCII`. Correct uppercase/lowercase provisional inputs,
title-case numbered names, bare ASCII, numeric/zero-padded/float-form keys
and missing values retain their expected identities. Thus the comparison
key's case folding does not make the preceding classification case-safe.

Ten complete original `build_catalog` pairs continue through merge, diameter
derivation, validation, enrichment, final dedup and CSV export/readback.
The three-body backbone uses the verified identities above. Its physical
values are synthetic: diameters 10, 1 and 6 km for fixture rows 1999, 66391
and 3568, H=12/18/14, positive finite orbits and S-type composition. These
are not measurements of the named asteroids. One supplement carries only
rotation_period_h=4.25 and its source flag.

With `1999 Kw4`, the original pipeline publishes that rotation value on
1999 Hirayama; 66391 Moshup receives none. Changing only the incoming
designation to `1999 KW4` places the same value on 66391. Correct MPC-style
alias links do not rescue the original: the string is reduced to the
already-known number before the alias lookup. The same wrong-body result
occurs with those links disabled.

Four other build cases lose the measurement: `3568 ASCII`, `(3568) ASCII`,
`3568 ascii` and `1936 Ub` enter as unmatched supplement-only rows and are
rejected for missing diameter. Replacing only their designation with the
verified numeric/provisional spelling retains the value on 3568. Every
build still ends with three bodies, so the final row count hides both the
misjoin and these losses. Original and diagnostic outputs pass the unchanged
`physical_problems` check; physical consistency cannot establish identity.

Six full-build pairs expose a failure, and four uppercase-provisional,
title-case-name, numeric and missing-key controls preserve the entire
result. Every original build repeats exactly, including field types and
numeric values, and the recipient read back from CSV matches memory. Only
source frames, links and metadata clock are controlled; all original
normalization, merge and scientific functions remain unchanged.

Verdict: case-dependent number/name discrimination can create a wrong body
key or defeat an available alias before matching. `rc-268`: distinguish
provisional/survey designations from numbered-name forms using their complete
grammar and preserve identity through supported case variants; leave an
unrecognised form unresolved rather than projecting it onto another body's
number. No actual-provider incidence, published-catalog corruption, real
rotation value or downstream ranking effect was measured.
`extracted_data/r337_designation_case_identity.csv`.


## R338 - Orbital epochs and source-record coherence (2026-11-02)

`imcce_ssodnet_orbital_metadata_api` lists
`orbital_elements.ref_epoch` as float64 in days, described as
"Reference epoch of osculation" (ssoBFT documentation, Metadata description,
Dynamical properties). Its ssoCard documentation selects orbital elements
from a resource such as ASTORB or MPCORB rather than averaging them.
The live Ceres ssoCard supplies ref_epoch=2461300.5,
ref_epoch_timescale=TT, ref_plane=Ecliptic and ref_center=Heliocenter.
`jpl_sbdb_small_body_database` documents its epoch as "epoch of osculation
(TDB) in Julian day form" (SBDB API, Orbit Data Section, epoch row); its
live Ceres response has epoch=2461200.5. These displayed day numbers differ
by 100; the records also declare different time scales. That difference is
not a propagated-orbit residual or a TT/TDB conversion.

`asteroidcatalog_orbital_epoch_pairing_record_2026` pins AsteroidCatalog
at `66fb47aaeb17aa7e11c023773a39765c1aa793fb`. In `asteroid_catalog/ssodnet.py`
L82-105, `_SSODNET_WANTED` requests the orbital elements including mean
anomaly but omits `orbital_elements.ref_epoch`; L308-329 reads only those
projected columns. The rename/numeric lists likewise have no epoch entry
(L127-160). The JPL adapter already describes its anomaly as "mean anomaly
AT EPOCH" and fetches a per-row epoch (`jpl.py` L61-74).

Seven original adapter pairs use a controlled schema/column-projection
reader and replace only parquet/cache I/O. Four lose known epochs: a replay
of Ceres orbital metadata, two rows with distinct epochs, an unnumbered
body and a numerically capped/sorted table. Three absent-epoch, null-epoch
and absent-required-key controls have no known epoch to recover. A mapping
diagnostic retains the raw source epoch number and changes no pre-existing
adapter output cell; it does not establish a TT-to-TDB conversion. Actual
parquet decoding and current bulk-table incidence were not measured.

The second seam is independent: `merge_sources` fills every non-measured
column separately (`merge.py` L565-575). Seven direct original merge pairs
produce three complete orbital records that match neither provider bundle:
a mean-anomaly gap, an epoch gap and a node gap. Four complete-backbone,
compatible-same-epoch and unavailable-data controls retain coherent or
explicitly incomplete records.

In the synthetic mean-anomaly fixture, both providers describe one circular
1-AU orbit with period 365.25 days, expressly using the same assumed time
scale and frame. The supplement gives M=10 degrees at JD2451545.0. The
backbone has JD2451645.0 and no M; the original merge publishes M=10 beside
that later epoch. The independent periodic relation requires
M=108.562628336756 degrees there: a 98.562628336756-degree phase difference,
equivalent to a 1.515843254995-AU chord in this idealized orbit. These are
synthetic errors, not measured errors for Ceres or any released row.

Eleven complete original build cases run fetch, merge, diameter derivation,
validation, enrichment, final dedup and CSV export. Three retain a source-only
or supplement-only body while losing its known source epoch; two fill a
backbone anomaly gap across different epochs, in opposite time directions.
The other six are controls. All original outputs repeat exactly; all
physical-row checks pass and exported orbit cells match memory. Forty-four
final build invocations include the repeat and two diagnostics per case.
Adding only the epoch projection leaves both original hybrid outputs
exactly unchanged. A separate diagnostic selecting a complete provider
bundle removes the mismatch; every non-orbital output cell remains equal,
and all six controls preserve the entire projection/coherent result.
Eleven raw local files match their pinned GitHub blobs; all four upstream
main comparisons are identical to the commits read.

Verdict: `rc-269`, retain the source orbital epoch and its time convention;
`rc-270`, preserve a coherent orbital-element/epoch record across source
gaps. Neither diagnostic is a production patch. The live complete Ceres
responses establish distinct source metadata, not a currently missing
provider field, released-catalog corruption, launch-window error or ranking
effect. `extracted_data/r338_orbital_epoch_and_bundle_pairing.csv`.


## R339 - Final-size eligibility and missing spectral classes (2026-11-02)

`asteroidcatalog_quality_gate_consistency_record_2026` pins AsteroidCatalog at
`66fb47aaeb17aa7e11c023773a39765c1aa793fb`. Its configuration says the global
`min_diameter_km` gate "drops anything below this size" (`config.py`
L151-155), default 0.001 km. The build derives diameters, validates rows,
then enriches (`build.py` L96-108). Enrichment can replace an H-derived size
with the diameter implied by measured mass and class density, labelled
`derived_mass` (`enrich.py` L322-335); no subsequent size gate runs.

Thirteen original build cases give two false positives, two false negatives
and nine exact final-catalog controls. For a synthetic S-type body, keep
the adopted density 2.7 g/cm3 and measured albedo 0.04; choose H for an
initial 10-km diameter and mass for a 4-km diameter at that density.
A 5-km global floor accepts the H estimate and the unchanged enrichment
then exports 4.000000000000001 km. The original validator rejects that
final row when reapplied. With the default one-metre floor, the same
sequence accepts an initial 2.5 m and exports 0.8 m.

The reverse cases use albedo 0.2: initial sizes 4 km and 0.8 m are rejected
before mass reconciliation. The original enrichment would instead yield
10 km and 2.5 m, above their 5-km and one-metre floors. A membership
diagnostic predicts final size with the unchanged enrichment and applies
the original validator at the actual floor, returning the unchanged
eligible source rows for the build's normal enrichment. Only those four
accepted sets change. Independent H/albedo and mass-volume arithmetic
reproduces both sizes. Controls cover final sizes on the same side of the
cut, a final boundary, measured diameters, absent mass/H, rejected
impossible-albedo mass and a zero global floor. No interpretation of the
separate `min_derived_diameter_km` setting is changed.

The spectral contract says that strict mode rejects a body with no Bus or
Tholen classification (`config.py` L157-159). `_BLANK_CLASSES` expressly
defines `""`, `"-"`, `"nan"`, `"NaN"`, `"None"`, `"none"`, `"NA"` and
`"<NA>"` as missing (`taxonomy.py` L922-926). The Bus normalization and
diameter-derivation fallback use that vocabulary. In contrast, the strict
gate's `_blank` tests null/empty/whitespace only (`validate.py` L19-25,
L109-136), and Tholen fallback sends every nonempty string through stripping
and case folding without masking those markers (`enrich.py` L82-92,
L125-129).

Eighteen strict-mode build cases expose ten missing-class acceptances:
the seven nonempty Bus markers, two Tholen markers and a two-row catalog
with one valid anchor and one placeholder-only row. The predicate diagnostic
rejects only the missing-class rows and restores original source cells for
all retained rows. Eight controls preserve the entire final catalog,
including valid Bus, valid Tholen, a valid Tholen after a missing Bus marker,
whitespace/actual nulls, a real complex label and strict mode disabled.

Eight additional builds use default permissive spectral mode. Five Tholen
markers block normal inference; three valid/missing/Bus-precedence controls
are unchanged. For a synthetic one-km body with H=18, albedo=0.2 and no
measured mass, a Tholen hyphen is published as spectral_type_source=tholen
and comp_class=Unknown, with no density or mass. Masking only the recognized
missing-type predicate lets the original albedo fallback choose S,
density=2.7 g/cm3 and derived mass=1.413716694115407e12 kg. The raw Tholen
cell remains a hyphen. This is the existing inferred composition/mass path,
not a new measured mass or a change to the taxonomy table.

Thirty-nine cases run the original build, an exact original repeat and the
stated in-memory diagnostic: 117 invocations. Eighty-four newly produced
catalogs pass selected diameter/class/mass/density/provenance readback;
33 all-rejected builds create no new CSV, as `build.py` L103-105 specifies.
All original outputs repeat exactly and physical checks pass. Ten raw
local files match pinned GitHub blobs; all four upstream main comparisons
are identical to the commits read.

Verdict: `rc-271`, apply global size eligibility to reconciled final size in
both directions; `rc-272`, interpret missing class markers consistently in
strict filtering and Tholen fallback. The source frames are synthetic and
do not establish provider frequency, released-catalog errors or ranking
effects. `extracted_data/r339_catalog_quality_gate_order_and_class_markers.csv`.


## R340 - Composite-summary consumer dependency (2026-11-03)

`spacecost_summary_consumer_contract_record_2026` reads spacecost
`860bef9902aa67fec705875cd52fdb8e6def159f` against economicspace
`54e30b0ae82be71c987f08feb95630502b7f54f0`. The summary docstring says:
"This is what Module 4 reads to pick the cheapest viable combination for
any asteroid" (`spacecost/tables.py` L116-119). The same dependency is
asserted in spacecost README L394-399, `spacecost/query.py` L176-180 and
the comment in `tests/test_query.py` L260-267, as the rationale for leaving
the composite summary unpenalized while query helpers apply low-thrust
delta-v factors.

The actual `load_all_catalogs` constructs six catalogs (`calc.py`
L1519-1562): asteroid, mineral, launch vehicle, propellant, delta-v and
operations. Its `_CATALOG_PROVENANCE` assertion has those exact keys and
no summary. No code string constant in the module names
`transportation_summary.csv` or its total-cost field. Sizing/prefilter
constants read `dv_penalty_factor` from the raw propellant row
(`calc.py` L3648-3672), rather than a composite-summary cost.

Four executions of the original loader and its three unchanged reader/list
parser helpers test the scratch summary in valid-original, absent,
invalid-UTF8 and misleading-negative-total states. Each execution makes
exactly the same six CSV reads; none reads the summary. All six returned
frames are identical in values, dtypes and column order. Stage-1/2 inputs
are small synthetic fixtures, including a mineral-list string; the actual
generated Stage-3 inputs have 76 vehicles, 41 propellants, 34 delta-v rows
and 46 operations rows. The original AST function bodies and line numbers
are retained, with a config namespace supplying their normal path/model
attributes; startup/install/output actions are not executed.

Verdict: `rc-274`, correct the repeated consumer dependency and test
rationale while retaining the stated raw-summary API and standalone query
helper behavior. This is a documentation/interface finding, not evidence
that the current Stage-4 ranking uses an unpenalized summary or is changed
by its total-cost correction. The associated cost-field audit is
`spacecost_summary_propellant_uplift_record_2026`. All four live main comparisons remain identical to
the commits read. `extracted_data/r340_summary_consumer_dependency.csv`.


## R342 - Release quote attestation (2026-11-03)

`spacevalue_release_quote_attestation_record_2026` reads spacevalue
873b91c1ce51fd2f5fe9ead63ce171d755e73011. `release.py` L163 says:
"The quotes the manifest records must be the snapshot's, exactly."
The builder writes ticker, source, close, unit and close_date (L114-116).
The checker compares only a set of (ticker, close) pairs (L174-176),
discarding the other declared fields and record multiplicity. README L190
repeats the quote-equality contract.

Four complete offline builds cover the two stored metal snapshots, with
one exact repeat each. All eight 59-row destination CSVs and the full
manifest reproduce byte for byte, and the original gate accepts them.
The five quoted prices are independently converted from the stored closes;
the unchanged public destination-price helper supplies their effective
destination values. The source snapshots and checksums are unchanged.

Eight manifest-only fixtures per snapshot change or omit unit/source/
close_date, or add an identical or conflicting-metadata duplicate quote.
All 16 return no gate findings and CLI exit 0. Comparing the multiset of
all five declared fields rejects every one. Reordering the quote list stays
valid; changing the close, removing a quote and changing the manifest
catalog date are detected controls. recorded_date and note are not fields
of the per-quote manifest schema and are not part of this finding.

The second contract is "every quoted metal is priced from its quote"
(README L194). `check_release` instead counts nonblank live_price_source
cells and compares that count with five (L219-223). Eight table fixtures per
snapshot preserve all five source-bearing rows and rehash only the changed
table. They double gold's live/effective value on Earth and in cislunar
space, alter the final Earth/GEO value alone, change live date/source,
replace palladium with a second gold row, or reassign gold's source ticker.
All 16 return no findings and CLI exit 0.

For metals-2026-10-26, Earth gold 128856.97403016586 USD/kg becomes
257713.94806033172 USD/kg while the raw close stays unchanged. Cislunar
gold 101540.01543822547 becomes 230396.98946839134 USD/kg under the same
destination rule. A GEO final-price-only edit from 94542.29355535637 to
95542.29355535637 also passes. The duplicate fixture keeps 59 rows and
five source-bearing cells, with two gold rows and no palladium. Added
canonical-name, converted-price, date/source and effective-price checks
reject all 16, using a relative tolerance of 1e-12 and absolute tolerance
of 1e-9 for serialization rather than rejecting last-bit rounding.

There are 54 original/repeated-API/CLI case triples: 32 false passes,
six valid controls and 16 correctly detected controls. The latter include
unrehashed bytes, a missing table, LF line endings, a blank quoted source
and a negative price as well as the manifest controls. Gate calls leave
every case file unchanged. All 16 local source/input blobs match pinned
GitHub metadata, and four fresh main comparisons are identical.

Verdict: `rc-276`, complete manifest quote records; `rc-277`, verify quoted
table content. These are planted-defect gate results, not evidence of
corrupt published releases or changed rankings. The workflow separately
compares committed fixtures where the tag has them (publish-prices.yml
L75-85); its later summary indexes unit and close_date directly (L94), so
missing-key cases need not finish that workflow despite passing this gate.
`extracted_data/r342_release_quote_attestation.csv`.


## R343 - Cached-release data contracts (2026-11-03)

`economicspace_cached_release_contract_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0. Both installer module headers
promise refusal "before anything on disk is touched" when the release's
data contract differs from the configured reader (catalog.py L45;
mineral_value.py L44). The configuration comments repeat this contract
(catalog.py L146-155; mineral_value.py L139-146). Fresh manifests are
checked at catalog.py L211-220 and mineral_value.py L224-237, with
"STAGE 1 CONTRACT MISMATCH" and "STAGE 2 CONTRACT MISMATCH" errors.

Stage 1 `release_on_disk` checks the installed tag and catalog byte count/
SHA-256, without comparing the contract (L243-257). `build_catalog`
skips the manifest check on that cache hit (L309). Stage 2 `cached_release`
checks the tag and every listed table hash, also without comparing the
contract (L240-256). `install_destination` selects that cached manifest
instead of `_download_release` (L315), copies the active CSV, and the
builder writes its installation record (L340-375).

Twenty-four cases execute the original Config classes and complete
installer function bodies, exact repeats and an in-memory cache guard:
72 calls. Startup installation/UI actions are excluded; manifest/asset
HTTP calls are replaced by recorded local fixture responses. Original
hash checks, staging, copy/replace operations and CSV reads remain in use.
The Stage 1 input is a two-row synthetic release-shaped fixture, not a
downloaded public catalog. Stage 2 inputs are two complete original
spacevalue releases from the stored metal snapshots, each with eight
59-row destination tables and a clean original release-gate report.

With intact caches, Stage 1 returns a 1.10.0-stamped frame to readers
configured for 1.9.0 or 1.11.0, making no manifest/asset request. Stage 2
installs the 1.17.0 table for expectations 1.16.0 or 1.18.0 on each price
profile, replacing the pre-existing active CSV and writing its record
with no request. The configured incompatible versions are deliberate
test inputs, not a claim that current defaults mismatch their releases.

The same incompatible expectations on absent or hash-damaged caches
fetch one manifest, raise the original contract error, transfer no asset
and preserve the previous target and installation record. Adding only
the missing contract comparison after admitted-cache hash checks rejects
all six warm mismatch cases before returning/installing the table.
Eighteen controls remain identical in outcome, request sequence, file
effects and complete returned frames, including valid offline cache hits,
valid fresh/hash-damaged refreshes and existing fresh-path refusals.
All original repeats are exact; all returned frames and target bytes
match the selected input CSVs.

The original `stamp_check` warns and returns False for all twelve
original/repeated incompatible returns when their owning module/config
is visible (calc.py L1896-1985). Its `integrity_check` caller ignores that
return (L1799). This later diagnostic is not the installer's promised
refusal. No full profitability catalog or ranking is executed. Fifteen
local source/input blobs match pinned GitHub metadata and all four
fresh main comparisons are identical to the commits read.

Verdict: `rc-278`, enforce reader-contract compatibility on cached as well
as fresh release admission while retaining valid offline cache reuse.
`extracted_data/r343_cached_release_contract.csv`.

## R346 - An unconverged sizing sequence can be accepted after twelve passes (2026-11-03)

`economicspace_unconverged_sizing_iteration_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0. The loop says "Solve the fixed point
instead of assuming it away" (calc.py L6086-6093), but stops after twelve
passes unless a nonviable cascade activates backoff (L6285-6288). Its final
guard is `if damped_here and not converged: return None` (L6517-6518).
An always-viable sequence can therefore be accepted with converged=False
and damped_here=0 under default damp_sizing_loop=True.

Twenty-three fixtures run original, exact repeat, an additional analytic
closure, its exact repeat, and the same pair with excavation charged:
138 complete `evaluate_asteroid` calls. The oracle is added only after an
accepted, unconverged, never-backed-off raw solar branch. It uses the
unchanged kernel's payload_cap_kg argument; all native candidates and the
original objective remain available. Fifteen cases improve; eight controls
retain identical winners. With excavation charged, thirteen still improve
and ten controls retain exact winners; the changed energy makes two cases
start backing off and converge without the extra candidate.

At 1.4 AU, homogeneous magnetite, actual Falcon 9 reusable/kerolox and
configured 1000 m/s reference burns each way, the selected raw solar branch
exhausts twelve passes with converged=False and no backoff. It returns
4,743.852061 kg cargo and 10,766.976256 kg launch against 17,400 kg allowance,
at cost/revenue 283.017319. Body, throughput and volume are not binding.
The selected refining route, 59-row LEO price input and 0.25-year stay
remain unchanged. In this fixed-stay chemical/no-ISRU regime the settled
mass book is independently affine in cargo m:

`M_launch = 1.362572353161971 * (2681.2861765809853 + 1.1005111525434224*m)`.

Its capacity root is 9,167.265480 kg; a point 1e-12 inside it makes the
original kernel converge in two passes at 17,399.999999986 kg launch and
cost/revenue 160.486179. The direct mass formula matches that returned
launch mass. The native fixed-point derivative is -0.941079855, explaining
the slowly decaying oscillation captured in all twelve original passes.
The independent recurrence `m_n = m_star * [1 - (-c)^n]` also reproduces
the native twelfth payload to floating-point precision.
With the independent excavation omission corrected, native cargo is
3,694.003409 kg at 9,239.484697 kg launch; a converged 9,090.488329 kg load
still fits the same allowance and improves the configured ratio.

Verdict: `rc-282`, use justified convergence or constrained closure before
accepting the last sizing iterate. Damping-off, default-beneficiation-search,
other ores, tank-off and longer-stay cases reproduce; naturally converged,
body-limited, volume-limited, refinery-off and profit-objective controls
retain their native winners. Every feasible result fits launch, resource,
throughput, time and volume bounds. Both repeated pairs pass native
type/value checks including float.hex and result digests. All examples
remain unprofitable controlled compositions/reference burns; no observed
trajectory, population effect or global optimum is claimed. Thirty-one
source/input blobs match fresh pinned metadata and all four live main
comparisons are identical. `extracted_data/r346_unconverged_sizing_iteration.csv`.
