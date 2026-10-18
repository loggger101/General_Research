# Domain 27 — Orbital debris & collision risk

Backings: the debris environment behind spacecost `operational_costs.csv` launch-insurance and third-party liability premium drivers (domain 17), economicspace's satellite-lifetime and end-of-life disposal assumptions, and the survivable environment behind domain 26's depot mission durations.

Created in Round 130 (2026-10-06). Blocks are appended one per round, newest last.

## R130 - Domain opened with three sources, none hostable (2026-10-06)

- **esa_2026_space_environment_report_issue_10** [T3]: ESA Space Debris Office annual report, Issue 10 Rev 1 (2026-09-08). Copyright notice forbids reproduction, so read only.
- **nasa_otps_2023_cost_benefit_analysis_orbital_debris_remediation** [T2]: NASA OTPS report (Colvin/Karcz/Wusk, NTRS 20230002817), MAY_INCLUDE_COPYRIGHT_MATERIAL, so read only.
- **colvin_2024_sustainability_cba_iac** [T2]: IAC-24-A6.8-E9.1.2, IAF copyright in-file, so read only.

Key numbers (quotes in `extracted_data/r130_debris_environment_key_numbers.csv`):

- MASTER epoch 2026-02-01: "68,450 space objects greater than 10 cm (including approximately 11,300 active payloads)", "1.5 million ... from 1 cm to 10 cm", "230 million ... from 1 mm to 1 cm".
- GEO end-of-life compliance over the last decade: 85-100% attempt to comply, 70-90% succeed.
- OTPS: removing the 50 most concerning objects is worth "around $3.5 million in the first year after removal"; a small-debris cluster "approximately $23 million".
- IAC: a 15-year deorbit rule yields benefits "20–750 times the costs", up to $6 billion net; a 0-year rule "nearly $9B"; shielding against 3 mm debris up to ~1,000x.

No upstream cell carries an absolute debris figure yet, so no candidate.

## R131 - Conjunction-assessment methodology: four NTRS papers hosted (2026-10-07)

- **bollenbacher_guptill_1999_launch_collision_probability** (NASA/TP-1999-208852): launch-vehicle collision probability against the ~10,000 tracked objects, used to avoid launching when it is unacceptably high.
- **hejduk_johnson_2016_pc_uncertainty** (AAS 16-241): carries input uncertainties through to a probability density of Pc instead of a point estimate.
- **elkantassi_davison_2025_miss_distance_inference_sdc9** (9th European Conference on Space Debris): significance probabilities and confidence intervals on miss distance as an alternative to Pc.
- **toumey_murphy_2026_federated_conjunction_assessment** (AMOS 2026): a framework for reconciling conflicting risk assessments of one conjunction.

`extracted_data/r131_conjunction_assessment_key_numbers.csv`. Together they show why a single Pc number is not enough (dilution, hard-body-radius uncertainty) if a cell ever pins a probability. No candidate.

## R135 - How much active debris removal is needed (2026-10-07)

Six NASA (JSC Orbital Debris Program Office) papers, hosted:

- Liou 2010 (ISTC deck): ~5,500 fragments, a >60% LEO population increase, "five objects per year" and the [M x Pc] selection criterion.
- Liou & Johnson 2007 (IAC): ERF=36 at 5 removals/yr from 2020 (935 removals, -33,337 LEO objects by 2206); cumulative collision-probability reduction 98.7%; ERF=12 at 20/yr (diminishing returns).
- Burns 2012 (abstract): one vehicle "disposing of several large objects per mission".
- Liou 2011 (engineering-challenges abstract): targets are spent upper stages of 1 to >8 t in ~10 inclination bands.
- Liou 2012: several ADR systems per launch preferred; tug propellant and operations cost "may be too high for a routine operation".
- Liou 2011 AAS 11-254: the canonical five-large-objects-per-year statement.

The Burns and engineering-challenges records carry no internal date; their years come from NTRS.

**yang_2026_adr_thresholds_frontiers_space_technologies** (CC BY, hosted): under the FCC 5-year rule and 90% compliance, removing ~60 objects >10 cm per year turns growth negative in the 500-600 km band, which the author calls "an illustrative threshold under controlled assumptions". Not a contradiction of NASA's ~5/yr, which counts massive intacts across LEO for 200-year stabilisation.

**liou_2013_adr_mission_design_eucass** registered_not_pulled (bot-walled; author copyright, so read-only even if pulled). `extracted_data/r135_adr_requirements_key_numbers.csv`. No candidate.

## R149 - The collision-frequency model lineage (2026-10-10)

Hosted:

- **kessler_su_1985_orbital_debris_nasa_cp-2360**: NASA CP-2360 *Orbital Debris*, the 1982 JSC workshop proceedings (454 pp, ~30 MB scan; year from NTRS). Its reference list cites Kessler & Cour-Palais 1978.
- **kessler_zhang_matney_et_al_1996_ordem_tm-104825**: NASA TM-104825, the ORDEM LEO environment model for spacecraft design.
- **krisko_2007_predicted_growth_leo_debris_evolve**: the EVOLVE growth model's history and collision characterisation (preprint; year from NTRS).

Queued: **kessler_cour_palais_1978_collision_frequency_debris_belt** [T1], JGR 83(A6):2637-2646; NTRS has no file and AGU/Wiley refuse this machine (DOWNLOADS.md).

`extracted_data/r149_debris_foundations_key_numbers.csv`. Context only; the 1978 paper could later anchor a population-growth figure.
