# Domain 8 — NEA accessibility oracles (R53)

Backings: distribution and rank reference for the NEA rows of spacecost `delta_v_segments.csv`, through economicspace `probe_nhats.py` (FINDINGS F4/F6), which validates the shipped one-way estimator against these external oracles. Key statistics: `extracted_data/r53_nea_oracle_key_numbers.csv`.

**1. NASA/JPL NHATS** (`jpl_nhats_nea_dv_oracle`; `ssd-api.jpl.nasa.gov/nhats.api`, T3 live service): JPL's numerically optimised **round-trip** delta-v for every NEA with a viable crewed trajectory (real ephemerides, multi-revolution transfers, entry-speed capped). N=7092 on 2026-09-24. Round-trip median **9.367 km/s** (p10 5.99, p90 11.55; range 3.39-12.00), reproducing economicspace SECOND-PASS.md F6 to 3 dp. Shares: <5 km/s 281 (4.0%); 5-8 1879 (26.5%); 8-10 2114 (29.8%); >=10 2818 (39.7%). The population is bounded by the filter, so it is an accessibility ladder, not a census.

**2. Asterank NEO service** (`asterank_neo_service_shoemaker_helin`; `www.asterank.com/api/asterank`, MIT, T3): the Shoemaker-Helin closed form (registered in d03 as `shoemaker_helin_1978`) as the `dv` column. 1,000-row NEA sample: median **8.140 km/s** (p10 6.15, p90 14.44), again matching F6. Its profit/price columns are degenerate through the public endpoint (99/200 nonzero): use dv only.

**Scope:** both oracles are round-trip quantities while the `delta_v_segments.csv` NEA rows (easy 4500 / average 6500 / hard 8500 m/s) are one-way legs, so they anchor rank and distribution, not cells. The easy tier maps to NHATS bodies under 5 km/s round trip (4.0%), the ultra-low class `elvis2011` counts as ~65/6699 NEOs.

## R73 - Full NHATS per-body table (2026-09-27)

Re-pulled with the default constraints (dv <= 12 km/s, duration <= 450 d, stay >= 8 d, launch 2020-2045): `r73_jpl_nhats_per_body_table.csv` (7,094 bodies) and `r73_jpl_nhats_key_numbers.csv` (32).

- Median minimum Δv still 9.367 km/s and the same shares; minimum-duration median 178 d.
- Bodies with a trajectory at Δv caps 4, 5, ..., 12 km/s: 38, 281, 717, 1,367, 2,163, 3,131, 4,277, 5,562, 7,094; each count equals the table rows at or below the cap.
- 968 bodies have orbit condition code 0-2, 69 a measured size, 696 a maximum size of 140 m or more. Lowest minimum Δv: 2021 GM1 at 3.389 km/s; (2000 SG344) fifth at 3.549.

## R113 - The NHATS filter, and a mining-specific accessibility database (2026-10-04)

**`barbee_mink_adamo_2011_nhats_methodology`** (hosted) defines the oracle's filter: departure 2015-2040, round trip <=450 d, stay >=8 d, C3 <=60 km2/s2, total delta-v <=12 km/s from a 400 km parking orbit, entry speed <=12 km/s, size >=30 m (H <=26.5 at albedo 0.05). Phase II: of 7,665 NEAs in SBDB on 2011-02-03, 765 passed the trajectory filter (79,157,604 trajectory solutions) and 590 also the size cut. These limits must be stated whenever the oracle's median is compared with one-way legs. `extracted_data/r113_nhats_methodology_key_numbers.csv`.

**`xie_bennett_dempster_2021_nea_mining_target_evaluation`** (abstract only; Acta Astronautica vol 181): a database of 6,373 accessible NEA mining missions of up to 6 years in 2030-2065; ~55% of accessible NEAs allow a stay over 4 years; retrievable water, PGM and silicate mass per asteroid. The closest published counterpart to economicspace's ranking and the next oracle to pull.

## R138 - NASA's definition of "NHATS-compliant": the SBAG-12 deck (2026-10-09)

**barbee_2015_accessible_near_earth_objects_nhats_sbag_deck** (NTRS 20150000798, hosted). Slide 3 criteria: departure 2015-01-01 to 2040-12-31; C3 ≤60 km²/s²; total Δv ≤12 km/s including "(1) the Earth departure maneuver from a 400 km altitude circular parking orbit, (2) the maneuver to match the NEA's velocity at arrival, (3) the maneuver to depart the NEA and, (4) if necessary, a maneuver to control the atmospheric re-entry speed"; round trip ≤450 days; stay ≥8 days; entry ≤12 km/s at 125 km.

Slides 5-6: "As of 2014-12-06, 1317 NHATS-compliant NEAs have been discovered"; 49 cost less Δv than lunar orbit and 556 less than the lunar surface. Calibration pairs: Mars surface 12.53 km/s / 923 d; elliptical Mars orbit 6.29 / 923 and 12.14 / 422; Venus-flyby variants 12.81 / 485 and 8.12 / 588; Mars flyby 9.01 / 501 and 6.07 / 582; "No round-trip mission to Mars (orbit, surface, or flyby) or Phobos/Deimos is possible with both Δv ≤12 km/s AND mission duration ≤450 days." The PDF text layer is garbled, so quotes come from NTRS's extracted fulltext, checked against slide renders. Pins the definition of the oracle output; no cell changes.

`extracted_data/r138_nhats_criteria_key_numbers.csv`.

## R143 - Dated points for the NHATS population (2026-10-09)

Three hosted NASA papers:

- **barbee_abell_adamo_mazanek_johnson_yeomans_chodas_2015_nea_mission_accessibility_pdc** (IAA-PDC-15-04-22): "When NHATS assessments began in September of 2010, just over 7,000 NEAs were known and 666 of those were identified as NHATS-compliant"; 1,034 compliant (83%) have MOID <=0.05 AU but only 9% are PHAs; lunar DRO reference ~4.5 km/s / 25 d.
- **adamo_barbee_2011_atens_enhanced_accessibility_aas11_449** (AAS 11-449): of 7,210 NEOs at Sep-2010, compliant bodies are 58.6% Apollos / 25.5% Atens / 15.9% Amors while Atens are 8.2% of known NEOs; defines the accessibility metric n; top target 2000 SG344 at n=4,153,445 (d 29-66 m).
- **barbee_abell_adamo_johnson_landis_mazanek_2023_prospects_human_nea_missions_pdc**: "There are currently 4,658 NHATS NEAs" (CNEOS, 2022-12-22); NEO Surveyor is the growth driver.

Ladder: 666 (Sep-2010) -> 765/590 (Feb-2011) -> 1,317 (Dec-2014) -> 4,658 (~Dec-2022) -> 7,094 live. `extracted_data/r143_nhats_population_ladder_key_numbers.csv`. Context only.
