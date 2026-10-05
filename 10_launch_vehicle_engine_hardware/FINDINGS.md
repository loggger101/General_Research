# Domain 10 — Launch vehicle & engine hardware / propellant performance (R64)

**Scope.** New domain per user criterion #2: all gatherable information on the rockets themselves + fuel/propellant performance data, anchored against `spacecost/reference/launch_vehicles.csv` and `spacecost/reference/propellants.csv`. Round 64 registers three NTRS-hosted NASA documents carrying engine-level MEASURED / TESTED numbers that no previously registered source carried. All three pulled fresh from NTRS this round, sha-verified byte-identical to the hosted copies below.

**Anchor 1 — Baumeister (NASA Glenn), *RL10 Engine Ability to Transition from Atlas to Shuttle/Centaur Program*, NASA/TM—2015-218736** [T2, NTRS 20150008246, hosted sha 2c9bc9077ae14778...]. Verbatim p9:

> "Each Centaur RL10A-3-3A engine at space vacuum conditions produced a rated thrust of 16,500 lb and a 444.4±2.5 sec nominal specific impulse at a nominal propellant oxidizer to fuel mixture ratio of 5.0:1."

(the ± symbol is encoded as U+F0B1 in this PDF's text layer; display-normalized above — the verbatim probe runs against the raw token, count==1 on a fresh pull.)

- **vs our `propellants.csv` hydrolox row** (note: 'Vac Isp 452 s per RS-25 / RL-10 datasheets'): the measured Centaur-engine figure is 444.4±2.5 sec -> our single family-level value sits **+1.71% above** the institutional measurement (computed in code: (452.0 - 444.4)/444.4 x 100). The row's one Isp spans two engines; its RL-10 half now has an institutional MEASURED anchor. Verdict: **consistency anchor, no revision forced.**
- Same sentence also fixes the rated thrust (16,500 lb vacuum = 73.4 kN computed) — engine-level thrust is not a spacecost column; extracted to `extracted_data/` for future use.
- p18 verbatim: "Reduce thrust level, 15,000 lb instead of 16,500 lb" and "Operate at a higher nominal mixture ratio (O/F) of 6.0:1 instead of 5.0:1" — the RL10A-3-3B qualification deltas (context only).

**Anchor 2 — Vetcha et al. (Jacobs Technology / NASA MSFC), *Overview of RS-25 Adaptation Hot-Fire Test Series for SLS, Status and Lessons Learned*** [T2, NTRS 20180006338, hosted sha 273c1daa8e4a62ed...]. Verbatim p2:

> "...successfully on all 135 Space Shuttle flights."
>
> "the RS-25 engine will be started at sea level and will shut down at altitude conditions after approximately 500 seconds of operation at a primary thrust level of 512,000 pounds (109 percent of rated thrust)"
>
> "Plans called for a minimum of seven starts and 3500 seconds of hot-fire operation on one development engine..."
>
> "...almost 9,000 seconds of hot-fire test time were accumulated on developmental and flight engines."

- Institutional confirmation of the RS-25/SLS mission profile (~500 s burn at 109% RPL) and the adaptation test campaign's scale — supporting evidence for `launch_vehicles.csv`'s SLS Block 1 row (operational status, hydrolox core).
- **Honest gap:** this document carries NO RS-25 vacuum-Isp figure (negative probe: no '46x sec'-class token in any of the three docs) — so the *RS-25 half* of our hydrolox row's 'per RS-25 / RL-10 datasheets' citation remains secondary-sourced; only the RL-10 half is now institutionally anchored.

**Anchor 3 — Ballard (NASA MSFC), *Next-Generation RS-25 Engines for the NASA Space Launch System*** [T2, NTRS 20170008958, hosted sha 2d0776c3aae786c6...]. Verbatim p2:

> "...the system was designed to be reusable, providing a certified service life of 55 starts and 27,000 seconds."

- RS-25 = SSME lineage (flew all 135 Shuttle flights per Anchor 2) with a certified **55 starts / 27,000 s** service life — the institutional basis for engine-level reusability. `launch_vehicles.csv` lists SLS as an expendable VEHICLE; this records that its engines are reusable hardware (the distinction matters for any future reuse-economics row).

**Per-row comparison table (computed in code):**

| our row | our value | institutional anchor | delta | verdict |
|---|---|---|---|---|
| propellants.csv hydrolox `isp_vac_s` | 452.0 s | RL10A-3-3A measured 444.4±2.5 sec (NASA/TM—2015-218736 p9) | **+1.71%** high vs the Centaur engine's measurement | consistency anchor — family-level figure; no revision forced |
| launch_vehicles.csv SLS Block 1 (status/profile context) | operational, hydrolox core | RS-25 hot-fire campaign + ~500 s @ 109% RPL profile (NTRS 20180006338 p2); 55-start engine service life (NTRS 20170008958 p2) | n/a (context, not a numeric cell) | supporting evidence recorded |

**Negative probes / honest gaps:** no RS-25 vacuum-Isp figure in any of the three documents; NTRS single-word 'Raptor'/'BE-4' hits were false positives (helicopter rotor codes, protograph code-naming) — our methalox row's 'per SpaceX Raptor public data' citation therefore remains secondary-sourced. Domain 10 deepening candidates for later rounds: Raptor/BE-4 institutional test reports, NTP/NERVA performance records (our nuclear thermal rows cite 'NERVA's NRX/XE ran at 825 s in 1968'), and per-engine thrust/mass specs from the OIG SLS audits already registered in d4/d7.

## Domain 10 — NERVA nuclear-thermal performance records (R65 deepening)

**Scope.** The `propellants.csv` nuclear-thermal row's note claims *'NERVA's NRX/XE ran on a test stand at 825 s in 1968'*; R64 flagged NTP/NERVA performance records as the top deepening candidate. Two AEC/NASA program documents from 1968 (both public domain, hostable) now carry that figure verbatim — independently of each other.

**Anchor 1 — NERVA Development Status (NTRS 19700004945), p4** (engine description; the sentence's subject is OCR-garbled in the scan):
> "Astronuclear Laboratory delivers approximately 75,000 lb of thrust at a specific impulse of 825 sec/lbm" — verbatim as printed: '...at a specific impulse of 825 1bf-sec/lbm' (OCR for 'lbf-sec/lbm')
> "The reactor produces 1575 Mw of power and the core consists of clusters of graphite fuel elements surrounded by a beryllium reflector"
> "provides approximately 91 lb/sec through the pump discharge line to the nozzle inlet plenum" (LH2 feed)

**Anchor 2 — NERVA program status (NTRS 19680011933), p12** (upgraded-model plan):
> "With a flight-type nozzle this will permit a vacuum thrust of 75,000 lbs. and a vacuum specific impulse of approximately 825 seconds." — at the PFRT-path rating of 1560 MW thermal / 4500 R chamber temperature (technology-type baseline: 1100 MW / 4090 R).

**Supporting figures** (Development Status, verbatim): p6 restart record — "experience has been gained on 25 starts - I an KIWI B4D, 2 on KIWI B4E, 2 on NRX-A2, 3 on NRX-A3, 1 on Phoebus 1A, 10 on NRX/EST, 2 on NRX-A5, 2 on Phoebus 18 and 2 on NRX-A6" (the verbatim per-test breakdown reconciles EXACTLY with the stated total: OCR 'I' = one start + 2+2+3+1+10+2+2+2 = **25**; 'Phoebus 18' is OCR for Phoebus 1B — a parse-integrity check that passed); p12 vacuum correction: "All of the performance demonstrations which I have described to you in this paper were at specific impulses when corrected for vacuun conditions of about 800 sec" (OCR 'vacuun' = vacuum).

**Verdict vs our row.** The note's historical-test half — *'NRX/XE ran on a test stand at 825 s in 1968'* — is now institutionally backed by TWO independent AEC/NASA documents agreeing to the same performance point (75,000 lb / ~825 s). The row's `isp_vac_s = 900` cell is NOT an institutional figure: per the note itself it is the **DRACO target** ('DRACO targeted 900 s before being descoped in 2025') — a design goal, not a measurement -> no revision forced. **[Corrected 2026-09-26 — the verdict on the note's historical-test half is wrong; see "Maintenance correction" at the end of this file and rc-042.]** Designation caveat (R51 citation-integrity discipline): neither document names 'NRX-XE' in extractable text (the subject line is OCR-garbled; the program's XE-series reactors are referenced as 'XE-I and XE-2'), so the anchor is recorded as NERVA-program test-stand performance of 1968, not a reactor-specific pin.

**Negative probes / honest gaps (R65):** ETS-1 performance characteristics doc (NTRS 19670020629) = 53-page image-only scan with NO text layer -> unusable, not registered; NTP Ground Test History paper (NTRS 20140008771) resolves to a 15 KB single-page abstract only -> not hostable as full text. No per-test Isp table extractable from either status doc beyond the figures above.

**R64 defect repair (same round).** R64's programmatic token slice cut the RL10 uncertainty at '±2' instead of '±2.5' (PDF p9 raw token = `444.4` + U+F0B1 + `2.5`, three font spans). All 5 committed occurrences repaired to `444.4±2.5 sec`: FINDINGS x3, extracted CSV x1, INDEX x1 (the R64 log line already carried the correct '±2.5' — now consistent everywhere). The delta is unaffected: it uses 444.4 only (+1.71%).


## R66 — Domain 10 deepening attempt: BE-4 / Raptor institutional sweep (NEGATIVE)

Per criterion #2 the methalox row in `spacecost/reference/propellants.csv` cites 'SpaceX Raptor public data' for both engine variants. Full NTRS discovery sweep this round: single-word queries BE-4 (13 hits), Raptor, Blue Origin (48), Commercial Propulsion Development (68), methalox (2) — every candidate record pulled and title-screened:

- All 13 'BE-4' NTRS hits are false positives: legacy rocket designations (e.g. Boeing X-20 / early booster studies) whose text incidentally contains the token; none is Blue Origin's BE-4.
- The single 'Raptor' hit matching an engine context was a coding-theory paper ('Protograph-Based Raptor-Like Codes') — false positive.
- 'methalox' (2 hits): in-situ propellant production at KSC, not an engine test record.
- Blue Origin's only NTRS presence is the de-orbit descent/landing program final report (20210026314) — no propulsion data relevant to our rows.

**Verdict**: neither BE-4 nor Raptor has ever flown a NASA-funded test campaign, so NTRS carries no institutional performance records for either engine. The methalox row's 'per SpaceX Raptor public data' citation remains secondary-sourced by construction — recorded as a standing gap (R67+ candidates: AIAA/peer-reviewed hot-fire reports outside NTRS, Blue Origin published test summaries). Registry unchanged this round for domain 10.

## Maintenance correction (2026-09-26) — R65 NERVA verdict reversed (no registry change)

R65 recorded the two 1968 NERVA documents as institutional backing for the `propellants.csv` nuclear-thermal note *'NERVA's NRX/XE ran on a test stand at 825 s in 1968'*. Re-reading both hosted PDFs, neither supports a 1968 test-stand run at 825 s:

- **nerva_development_status_1968** p4 gives 825 lbf-sec/lbm as the rating of the NERVA engine being described. The same paper, p12: "All of the performance demonstrations which I have described to you in this paper were at specific impulses when corrected for vacuun conditions of about 800 sec" ('vacuun' is sic). p11 lists XE-I and XE-2 engine-system testing as part of the *future* ROVER program.
- **nerva_program_status_1968** p12: the upgraded PFRT-path model "will permit a vacuum thrust of 75,000 lbs. and a vacuum specific impulse of approximately 825 seconds" — a planned rating. The same page calls the XE-1 and XE-2 test series "forthcoming". p2 says only that specific impulses of about 825 s "are obtainable".

So both documents give ~825 s as the engine's rated or planned figure and ~800 s (vacuum-corrected) as what had been demonstrated by early 1968; the XE engine had not yet run. They come from the same program, so they agree on the rating, not on a measurement. The `isp_vac_s = 900` cell is unaffected (it is the DRACO target). Recorded as wording candidate **rc-042**; the two registry rows, their INDEX rows and the NTP rows of `extracted_data/r64_engine_performance_key_numbers.csv` now say this. The R65 text above is left as written, with a pointer here.

## R70 - Full-extraction pass of the hosted sources (2026-09-27; registry unchanged)

Every hosted full text in this domain was re-read end to end for pipeline-useful numbers; tables were read by word coordinates (or from rendered page images where the text layer fails) and checked against their printed totals. New files (all in `extracted_data/`, every row carries `source_id` and a page location): `r70_ballard_2017_rs25_nextgen_sls.csv` (17); `r70_baumeister_2015_rl10_atlas_to_shuttle_centaur.csv` (14); `r70_baumeister_2015_table1_rl10_performance_upgrades.csv` (5); `r70_baumeister_2015_table3_centaur_vehicle_engine_characteristics.csv` (3); `r70_nerva_development_status_1968.csv` (20); `r70_nerva_program_status_1968.csv` (8); `r70_nerva_program_status_1968_fig6_nrx_reactor_test_comparisons.csv` (5); `r70_vetcha_2018_rs25_adaptation_hotfire_sls.csv` (15).

- **Baumeister 2015 (RL10)**: Table 1 upgrade history (RL10A-1 to A-3-3A: 424 -> 446.4 s, 300 -> 465 psia, 40:1 -> 61:1) and Table 3 Centaur vehicle/engine data. Thrust / (LOX + LH2 flow) = 443.5 s and 438.6 s agree with the printed Isp; LOX/LH2 flows give O/F 5.0 and 6.0. **Inconsistency kept as printed**: Table 1 gives RL10A-3-3A Isp 446.4 s, while the p9 text and Table 3 give 444.4 +/- 2.5 s for the same engine.
- **Vetcha 2018 (RS-25)**: the p3 requirements figure gives rated vacuum thrust 470,000 +/- 6,000 lbf, **minimum vacuum Isp 451.3 s at 109%**, engine mass 8,280 lbm (3,756 kg), 94 x 167 in, 65-109% throttle and life of 6 starts / 2,500 s. The Fig.9 bars (chart-read) sum to ~7,900 s against "almost 9,000 s" in the text.
- **Ballard 2017**: component cost-reduction targets for the restart RS-25 (MCC -60%; injector, preburners, hot gas manifold and nozzle -30%; HPOTP/HPFTP -25%; low-pressure pumps and valves -20%) against an overall goal of one-third.
- **NERVA 1968**: the NRX reactor comparison table (Figure 6, rotated page image). Endurance time x average power reproduces the printed integrated power for all five reactors, e.g. NRX-A6 62.9 min at 1,150 MW = 4.3e6 MW-s. The design point is 75 klbf at 825 s from 1,575 MW (75,000 / 91 lb/s = 824 s). **Inconsistencies kept as printed**: the power-starts table totals 24 while the text says 25 (NRX-A6: 1 vs 2), and NRX-A2 is 0.8 min at full power in the table against "about two minutes" in the text.
## R96 - Methalox engine test anchors + the negative finding that closes the AIAA sub-item of the standing gap (2026-10-01; +3 rows -> registry 338)

The d10 brief's open item since R64/R66: *'Raptor/BE-4 institutional test reports, NTP/NERVA performance records ... AIAA peer-reviewed hot-fire reports outside NTRS'* (the methalox row in `spacecost/reference/propellants.csv` cites 'SpaceX Raptor public data' for both engine variants). This round does two things: registers the three nearest PEER-REVIEWED LOX/methane test sources, and records a documented negative finding on why no better ones exist.

**Negative finding (the actual answer to the standing gap).** A full bibliographic sweep this round - Crossref title-level 'Raptor' (20 hits: all unrelated raptors in biology/CS/astronomy), title-level 'BE-4 engine' (0 hits), author/bibliographic sweeps for New Glenn / Blue Origin upper-stage engines (0 relevant), the Journal of Propulsion and Power ISSN filter with methane queries (0 hits) - confirms what R66's NTRS sweep already showed: **as of 2026-10-01 there is no indexed peer-reviewed report on the Raptor or BE-4 engine in Crossref at all.** Neither company publishes its test data in the open literature; their public figures (Raptor vacuum Isp ~380 s class, chamber pressure, thrust) are grey-source by construction. The standing gap therefore narrows from 'AIAA peer-reviewed hot-fire reports' to 'Blue Origin/SpaceX published test summaries only', which is T4 territory and already reflected in the upstream row's own citation style.

**The three registered anchors (all context for the methalox family-level figure, none a Raptor/BE-4 report):**

| source | tier/access | what it carries |
|---|---|---|
| Ueda et al. 2013 [T2; AIAA JPC 49th proceedings] | registered_not_pulled (DOI Crossref-verified) | Hot-fire test of a LOX/methane engine under high-altitude-simulated conditions - the nearest peer-reviewed methalox hot-fire performance record to our row's population |
| Judd et al. 2006 [T2; AIAA SciTech 44th proceedings] | registered_not_pulled (DOI Crossref-verified) | Combustion-process study on an LOX/methane engine: how the combustion process drives performance/stability/durability - the physical basis for oxidizer-rich staged combustion (the Raptor cycle) and why a family-level 380 s is the right kind of figure, not an engine pin |
| Engelen/Souverein/Twigt 2009 [T1; JBIS 62:211-218 - peer-reviewed journal per BIS's own site] | registered_not_pulled (BIS product page + IAF archive record verified) | The DEIMOS liquid CH4/LOX engine test campaign: measured thrust/chamber-pressure/mass-flow data, ignition reliability, combustion stability and an explicit REUSABILITY assessment; design point 1800 N / 287 s at 40 bar with the provisional tests averaging a mere 3.8% of design thrust (per the abstract) - honest small-scale methalox test data including failure |

**Verdict vs our row.** The methalox `isp_vac_s = 380` cell stays exactly as is: its citation ('SpaceX Raptor public data') remains secondary-sourced BY CONSTRUCTION - there is no peer-reviewed alternative to cite, and that absence is now documented with the sweep evidence above rather than left as an open question. The three anchors give future rounds (a) a per-type physical basis for staged-combustion methalox performance/stability/durability trade-offs, (b) altitude-condition test methodology precedent, and (c) measured small-scale CH4/LOX data including reusability behaviour - the same property class d16's mechanism-reliability cells are built on. No revision candidate: nothing here contradicts a cell value; it documents that the cited figure has no T1-T3 substitute available in the open literature.

**Domain 10 status after R96:** all five originally registered sources (RL10, RS-25 x2, NERVA x2) plus these three methalox anchors are now in place; the only remaining d10 gap is T4 grey-source replacement for 'SpaceX Raptor public data' / Blue Origin test summaries - a deliberate weak-evidence marker per the repo's tier system, not an oversight.

## R114 - Methalox and rotating-detonation hot-fire sources (2026-10-04; +9 sources, T1x2, T2x7)

Nine sources from the owner's methane and RDRE block. Measured or stated engine-level figures: the NASA MSFC ECI report's best RDRE hot fire (about 5,300 lbf at about 740 psia, Isp 246 s, p32); ASI's MIRA 100 kN LOX/LCH4 expander engine (more than 11 tests to full operating condition, more than 600 s, p7 of the ISECG review) and an IHI/JAXA 30 kN engine at about 350 s (p11); JAXA/IHI's injector tests reaching a characteristic-velocity efficiency equivalent to 370 s at the 30 kN reference point (EUCASS 2019); and Tan (2024), which compares LOX/kerosene (theoretical Isp about 3% below LOX/methane) and LOX/LH2 (density Isp about 10% below). Abstract-only registrations: Smith & Stanley 2021 (RDRE at 68-85% of ideal deflagration Isp), Hemming et al. 2024 (RDE meta-analysis) and Meyer et al. 2012 (a LOX/LCH4 test campaign at Glenn, up to 24 hot fires a day). Two NASA RDRE/vehicle papers (Teasley 2025; Morehead et al. 2017) give hardware scale but no Isp.

None sets the methalox row of `propellants.csv`, whose 'Raptor public data' basis stays secondary (R65): the numbers are for other engines or for an experimental RDRE. Rejected: facility and project pages with no figures, a design-optimisation paper without hot-fire data, a test-requirements report and slide decks (Round 114 log entry). A UTEP thesis on a 500 lbf engine could not be identified (Cloudflare block) and stays undecided. No revision candidate.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.
