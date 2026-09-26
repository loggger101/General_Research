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

**Verdict vs our row.** The note's historical-test half — *'NRX/XE ran on a test stand at 825 s in 1968'* — is now institutionally backed by TWO independent AEC/NASA documents agreeing to the same performance point (75,000 lb / ~825 s). The row's `isp_vac_s = 900` cell is NOT an institutional figure: per the note itself it is the **DRACO target** ('DRACO targeted 900 s before being descoped in 2025') — a design goal, not a measurement -> no revision forced. Designation caveat (R51 citation-integrity discipline): neither document names 'NRX-XE' in extractable text (the subject line is OCR-garbled; the program's XE-series reactors are referenced as 'XE-I and XE-2'), so the anchor is recorded as NERVA-program test-stand performance of 1968, not a reactor-specific pin.

**Negative probes / honest gaps (R65):** ETS-1 performance characteristics doc (NTRS 19670020629) = 53-page image-only scan with NO text layer -> unusable, not registered; NTP Ground Test History paper (NTRS 20140008771) resolves to a 15 KB single-page abstract only -> not hostable as full text. No per-test Isp table extractable from either status doc beyond the figures above.

**R64 defect repair (same round).** R64's programmatic token slice cut the RL10 uncertainty at '±2' instead of '±2.5' (PDF p9 raw token = `444.4` + U+F0B1 + `2.5`, three font spans). All 5 committed occurrences repaired to `444.4±2.5 sec`: FINDINGS x3, extracted CSV x1, INDEX x1 (the R64 log line already carried the correct '±2.5' — now consistent everywhere). The delta is unaffected: it uses 444.4 only (+1.71%).


## R66 — Domain 10 deepening attempt: BE-4 / Raptor institutional sweep (NEGATIVE)

Per criterion #2 the methalox row in `spacecost/reference/propellants.csv` cites 'SpaceX Raptor public data' for both engine variants. Full NTRS discovery sweep this round: single-word queries BE-4 (13 hits), Raptor, Blue Origin (48), Commercial Propulsion Development (68), methalox (2) — every candidate record pulled and title-screened:

- All 13 'BE-4' NTRS hits are false positives: legacy rocket designations (e.g. Boeing X-20 / early booster studies) whose text incidentally contains the token; none is Blue Origin's BE-4.
- The single 'Raptor' hit matching an engine context was a coding-theory paper ('Protograph-Based Raptor-Like Codes') — false positive.
- 'methalox' (2 hits): in-situ propellant production at KSC, not an engine test record.
- Blue Origin's only NTRS presence is the de-orbit descent/landing program final report (20210026314) — no propulsion data relevant to our rows.

**Verdict**: neither BE-4 nor Raptor has ever flown a NASA-funded test campaign, so NTRS carries no institutional performance records for either engine. The methalox row's 'per SpaceX Raptor public data' citation remains secondary-sourced by construction — recorded as a standing gap (R67+ candidates: AIAA/peer-reviewed hot-fire reports outside NTRS, Blue Origin published test summaries). Registry unchanged this round for domain 10.
