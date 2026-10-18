# Domain 9 — In-space delivery mass fractions & EDL survival (R54)

Backings: spacecost `delivery.py` typed constants with no table row: `MARS_LANDED_MASS_FRACTION = 0.30` (sets the published mars_surface price; the comment calls it "Measured, not assumed" from MSL and Perseverance), `LANDER_DRY_MASS_FRAC = 0.20` and `TUG_DRY_MASS_FRAC = 0.10`.

**Sources (R54):**

- `edquist_2022_mars2020_aerothermal_entry_masses` (NTRS 20210024709, hosted): Table 3 (p14) entry masses: MSL BET 3153 kg; Mars 2020 TPS design cases 3436/3436 kg; Mars 2020 BET 3369 kg.
- `nasa_mars2020_flight_mech_edl_simulation` (NTRS 20210024480, hosted), p1: "At 1026 kg, Perseverance is the largest, most sophisticated rover ever delivered to another planet."
- `jpl_msl_factsheet_curiosity_mass` (live): Curiosity "899 kg in Earth gravity" (1,982 lbs).

**Audit:** MSL 899/3153 = 28.51%; Perseverance 1026/3369 = 30.45% (29.86% on the design case). Band [28.51%, 30.45%]; 0.30 sits inside at the optimistic edge (+5.22% vs MSL, -1.49% vs Perseverance), as the code's "takes the better of the two" says.

**Note-level discrepancy (constant unaffected):** the comment cites MSL entry 3257 kg where the BET is 3153 kg (+3.30%), and rover 1025 kg vs 1026. It shifts the quoted per-mission percentages (27.6%/29.8%), not the constant.

The other two constants were later anchored from SP-4029 (d03): TUG in R56 (S-IVB dry weights, p294), LANDER in R147 (below).

## R56 - As-flown TPS thicknesses and parachute numbers (no new sources)

- Edquist p3: "MSL material thicknesses for PICA on the heatshield (1.25 inches), SLA-561V on the backshell (0.5 inches), and Acusil-II on the parachute cone (variable thicknesses) were unchanged for the Mars 2020 vehicle": the TPS priced at $50k/kg in the `edl` leg is a thin ablative layer, supporting a material-plus-manufacturing cost basis.
- Flight-mech p2, Mars 2020 parachute deploy at E+4:01: peak inflation load 34.2 kips, 5.3 Earth g, 12.2 km altitude, Mach 1.76, 504 Pa, 433 m/s. No per-unit parachute price exists, so nothing is pinned.

## R70 - Full extraction (2026-09-27)

`r70_edquist_2022_mars2020_aerothermal_entry_masses.csv` (6), `r70_edquist_2022_table3_entry_trajectories.csv` (4), `r70_edquist_2022_table4_mars2020_bet_conditions.csv` (14; 0.5 rho V^2 matches printed dynamic pressure on every row), `r70_mars2020_flight_mech_table7_gnc_reconstructed_events.csv` (20), `r70_nasa_mars2020_flight_mech_edl_simulation.csv` (13). PICA 1.25 in (31.75 mm); heatshield peak ~68 W/cm2 (chart-read). Mars 2020 used 298 kg of descent propellant to touchdown with 77 kg left at flyaway for a 1,026 kg rover; peak deceleration 10.7 g.

## R72 - Remaining tables (2026-09-27)

`r72_mars2020_edl_sim_vs_flight_summaries.csv` (16), `r72_mars2020_edl_table10_newstep_trajectory.csv` (36), `r72_mars2020_edl_table13_atmosphere.csv` (31). Velocity / sound speed reproduces every printed Mach; 0.5 rho v^2 reproduces dynamic pressure except at range control, where Table 13 prints density to one significant figure (0.00004; 511.09 Pa implies 3.53e-5 kg/m3).

## R113 - A lander dry-mass fraction with a table behind it (2026-10-04)

`LANDER_DRY_MASS_FRAC` = 0.20 rests on the Apollo LM descent stage (2,134 kg dry on 8,200 kg propellant, 0.21; spacecost@85da36c L254-258).

**`kennedy_2019_nasa_lunar_lander_reference_design`** (NTRS 20190033128, hosted), NASA's ~300 kg-payload pallet lander. Figure 2 (p25): dry basic mass 1,053.77 kg, growth 234.26 kg, 8% margin 84.30 kg, 3% customer reserve 127.5 kg, propellant 2,753.62 kg, ~4,250 kg at launch. Dry/(dry+propellant) = **0.333** without the reserve, **0.353** with it: an upper bound for small landers (solid braking motor, fixed avionics floor), not a contradiction of Apollo's large-lander 0.21. A cargo-class lander mass table is still missing. `extracted_data/r113_lunar_lander_mass_breakdown.csv`.

## R139 - MSL design-time mass budget; low-beta entry context (2026-10-09)

**way_et_al_2006_msl_entry_descent_landing_system_performance** (NTRS 20070016022, hosted): designed "to land an 850 kg rover to altitudes as high as 1 km above the Mars Orbiter Laser Altimeter" (Curiosity flew at 899 kg); MER "delivered a 173 kg rover to an altitude of -1.44 km MOLA"; usable hydrazine "up to 390 kg"; Table 9 mean use 298.2 kg (bounds 284.2/312.8, std 4.7): Powered Approach 193.4 / Constant Velocity 9.7 / Constant Deceleration 35.0 / Sky Crane 42.1 / Fly Away 17.8, so ~26% margin at design time. Ballistic coefficient ~140 kg/m^2.

**dutta_et_al_2012_low_ballistic_coefficient_entry_sizing_trade_studies** (NTRS 20120006657; "©2012 IEEE", so read, not hosted): "The lowest ballistic coefficient of the past successful missions has been 188 kg/m2"; deployables "may attain aeroshell areal densities of 10 kg/m2 as opposed to 50 kg/m2 for rigid aeroshells". Context only.

## R147 - LANDER_DRY_MASS_FRAC backed by as-flown Apollo data (no new sources)

From the hosted SP-4029 (`sp4029_apollo_by_the_numbers`, d03):

- p287 'LM Descent Stage' dry weights: A9 4,265 lb / A11 4,483 / A12 4,875 / A13 4,650 (A10, A14-A17 OCR-damaged). Footnote 14: weights "as published in mission press kits".
- p305 'LM Descent Stage Propellant Status': A9 18,040 lb (fuel 6,977 + oxidizer 11,063) up to 19,564.2 lb for A17 = 8,183-8,874 kg.

The comment's 2,134/(2,134+8,200) = 0.2065; 8,200 kg sits in the A9-A13 loaded band (8,183-8,362 kg). As-flown dry/(dry+propellant): A9 0.1912, A11 0.1978, A12 0.2092, A13 0.2014, so 0.2065 and the dial 0.20 both sit inside. No candidate. `extracted_data/r147_lm_descent_stage_mass_key_numbers.csv`.
