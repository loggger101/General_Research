# Domain 10 — Launch vehicle & engine hardware / propellant performance (R64)

**Scope.** New domain per user criterion #2: all gatherable information on the rockets themselves + fuel/propellant performance data, anchored against `spacecost/reference/launch_vehicles.csv` and `spacecost/reference/propellants.csv`. Round 64 registers three NTRS-hosted NASA documents carrying engine-level MEASURED / TESTED numbers that no previously registered source carried. All three pulled fresh from NTRS this round, sha-verified byte-identical to the hosted copies below.

**Anchor 1 — Baumeister (NASA Glenn), *RL10 Engine Ability to Transition from Atlas to Shuttle/Centaur Program*, NASA/TM—2015-218736** [T2, NTRS 20150008246, hosted sha 2c9bc9077ae14778...]. Verbatim p9:

> "Each Centaur RL10A-3-3A engine at space vacuum conditions produced a rated thrust of 16,500 lb and a 444.4±2 sec nominal specific impulse at a nominal propellant oxidizer to fuel mixture ratio of 5.0:1."

(the ± symbol is encoded as U+F0B1 in this PDF's text layer; display-normalized above — the verbatim probe runs against the raw token, count==1 on a fresh pull.)

- **vs our `propellants.csv` hydrolox row** (note: 'Vac Isp 452 s per RS-25 / RL-10 datasheets'): the measured Centaur-engine figure is 444.4±2 sec -> our single family-level value sits **+1.71% above** the institutional measurement (computed in code: (452.0 - 444.4)/444.4 x 100). The row's one Isp spans two engines; its RL-10 half now has an institutional MEASURED anchor. Verdict: **consistency anchor, no revision forced.**
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
| propellants.csv hydrolox `isp_vac_s` | 452.0 s | RL10A-3-3A measured 444.4±2 sec (NASA/TM—2015-218736 p9) | **+1.71%** high vs the Centaur engine's measurement | consistency anchor — family-level figure; no revision forced |
| launch_vehicles.csv SLS Block 1 (status/profile context) | operational, hydrolox core | RS-25 hot-fire campaign + ~500 s @ 109% RPL profile (NTRS 20180006338 p2); 55-start engine service life (NTRS 20170008958 p2) | n/a (context, not a numeric cell) | supporting evidence recorded |

**Negative probes / honest gaps:** no RS-25 vacuum-Isp figure in any of the three documents; NTRS single-word 'Raptor'/'BE-4' hits were false positives (helicopter rotor codes, protograph code-naming) — our methalox row's 'per SpaceX Raptor public data' citation therefore remains secondary-sourced. Domain 10 deepening candidates for later rounds: Raptor/BE-4 institutional test reports, NTP/NERVA performance records (our nuclear thermal rows cite 'NERVA's NRX/XE ran at 825 s in 1968'), and per-engine thrust/mass specs from the OIG SLS audits already registered in d4/d7.
