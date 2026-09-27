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
