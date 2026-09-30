# Domain 16 — Reliability, learning curves & hardware service life

Backings: spacecost `reference/operational_costs.csv` rows `Launch vehicle reliability`, `Spacecraft mean time between failures`, the three `Mining system` / `Mining reliability` rows, `Mining rig service life`, `Mining rig maximum trips` and `Rig salvage fraction`, and economicspace `modules/calc.py` `learning_curve_rate`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

These rows set the probability that a mission earns anything and how many missions one rig can serve. The two sources behind the growth exponent sit in domain 5, and no registry source backs the rest. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Launch vehicle reliability` | 0.97 [0.90, 0.99] probability of a successful launch | Falcon 9 ">99% success over 300+ flights", a first-flight vehicle "near 0.90"; no source |
| `Spacecraft mean time between failures` | 30 yr [15, 60], exponential survival P = exp(-T/MTBF) | examples (Voyager 1/2, New Horizons, Dawn, Akatsuki, Hayabusa); no failure dataset |
| `Mining system first-of-kind success probability` | 0.85 [0.70, 0.95] | a tally of flown regolith-contact mechanisms (Apollo, Luna, Phoenix, Curiosity, Hayabusa2, OSIRIS-REx, Perseverance, Chang'e and others); the tally has no source |
| `Mining reliability growth exponent` | alpha = 0.30 [0.10, 0.60] (Duane / AMSAA) | MIL-HDBK-189: 0.3-0.6 for an active growth programme, 0.1-0.2 for passive fielding |
| `Mining system mature success probability` | 0.95 [0.85, 0.99] ceiling | "solar-array and antenna deployments run ~97-99% across the fleet record"; no source |
| `Mining rig service life` | 15 yr [5, 30] | "ISS-class hardware is rated 15-30 years"; no source |
| `Mining rig maximum trips` | 5 [2, 12] campaigns | "JUDGEMENT, and there is no flight heritage for it" |
| `Rig salvage fraction` | 0.5 [0.0, 0.8] of remaining book value | "a deliberately unheroic haircut"; no source |
| `calc.py` `learning_curve_rate` | 0.85 per doubling (Wright's law); `model_learning_curve` has defaulted to False since v1.22.0 | "Wright's law at 85% is standard for aerospace serial production"; no source |

**What a source has to supply.**

- Launch success-rate statistics that treat small samples explicitly, so a new vehicle and a mature one can be told apart.
- On-orbit failure or survival analyses of spacecraft that fit a lifetime distribution, to test both the exponential form and the 30-year scale for deep-space craft.
- Success rates of spacecraft mechanisms by type (deployments, sampling, drilling).
- Fitted reliability-growth parameters from real programmes, and measured learning-curve slopes for spacecraft and launch-vehicle production runs.
- Wear-life data for mechanisms working in abrasive regolith (seals, bearings, cutting surfaces), and, as a terrestrial analogue for salvage, the residual value of used heavy mining equipment.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `mil_hdbk_189c_reliability_growth_management` (domain 5): the growth-exponent band.
- `duane_1964_learning_curve_reliability_monitoring` (domain 5): the Duane growth model.

**Boundary.** Domain 10 holds engine-level certified life (`ballard_2017_rs25_nextgen_sls`), which bears on reusability rather than on these probabilities. Insurance, which replaces hardware but not revenue, is domain 17.

## R77 - Sources moved in (2026-09-27; registry unchanged at 267)

These rows were registered in other domains before this one existed; they moved here because the cells they back are this domain's. Their earlier write-ups stay in the old domain's FINDINGS.md under the blocks named.

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `mil_hdbk_189c_reliability_growth_management` | domain 5 | `05_inspace_operations/FINDINGS.md`: R74 | none |
| `duane_1964_learning_curve_reliability_monitoring` | domain 5 | `05_inspace_operations/FINDINGS.md`: R74 | none |

The cross-references to `mil_hdbk_189c_reliability_growth_management`, `duane_1964_learning_curve_reliability_monitoring` in the opening block are now rows of this domain.
## R86 - First empirical launch-reliability anchors (2026-09-30; registry 311 -> 313)

Two NTRS-hosted conference presentations, both pulled live from ntrs.nasa.gov this round and hosted under `full_texts/` (NTRS copyright determination PUBLIC_USE_PERMITTED for each - same precedent as the R82 d3 rows):

- **cross_vesely_2018_lv_first_flight_failure_probability** [T2] - PSAM 2018 (JSC): builds a database of ALL US+foreign launches 1980-2017 by model type, then computes an assumed new-vehicle design from every failure on the first two flights of each model -> **first-flight failure probability = 0.134 (success ~0.866)**; with assurance-program credit for heritage elements (equivalent of 5 flights: solid propulsion, upper-stage engines, TVC) the total drops to **0.0898 (~success 0.910**). Element rates per element-launch: upper-stage liquid engines 2.03E-02 (highest), avionics 1.32E-02, stage separation 1.36E-02, TVC 1.95E-03 (lowest). Conclusion p11 verbatim: new vehicles have 'significantly higher average failure probability than mature launch vehicles' and PRA 'do[es] not adequately assess their failure probability'.
- **al_hassan_novack_2015_bayesian_reliability_data_applicability** [T2] - Huntsville SRE RAM VIII 2015 (MSFC): the METHOD for exactly this domain's small-sample problem. A new vehicle is heritage + new hardware; its failure rate is estimated with lognormal priors per reliability block, each weighted by a subjective data-APPLICABILITY heuristic over generic sources (NPRD/EPRD/NUCLARR, MIL-HDBK-217F part-count), then correlated and Monte-Carlo'd. 'Higher data applicability improves certainty of estimates' (p16).

What they supply this domain's cells:

| cell | anchor |
|---|---|
| `Launch vehicle reliability` (0.97; band 0.9-0.99) | Cross & Vesely: upstream's own note ('a first-flight or low-cadence vehicle sits near 0.90') now has an empirical figure - raw first flight ~0.866, with assurance credit ~0.910; the fleet-representative 0.97 is consistent with (not computed from) this paper's per-model series, which separates new vs mature vehicles explicitly (p4 chart). No re-pin proposed: value and band unchanged |
| `Mining reliability growth exponent` + rig rows | Al Hassan & Novack supplies the method for combining heritage data with little flight experience - the machinery any small-sample reliability estimate in this domain should use; no numeric pin |

Extracted data: `extracted_data/r86_launch_reliability_key_numbers.csv` (11 rows). No revision candidate opened or closed by this round. Still unbacked cells: spacecraft MTBF / lifetime distribution, mechanism success rates by type, measured learning-curve slopes for production runs, regolith-abrasion wear life and used-equipment residual value - the rest of the opening brief.
