## R954 — Spacevalue Mars entry-survival comparator cited upstream (2026-11-19)

At Spacevalue main 69549f772a43d155dc27d5ae5f01f90a7e4ce996, the Mars-surface note retains 0.30 and describes it as an approximate MSL / Perseverance entry-to-rover ratio: 899/3,153 kg = 28.5% and 1,026/3,369 kg = 30.5%. Entry masses are attributed to Edquist et al. 2022 Table 3, PDF p. 14; rover masses to the JPL MSL fact sheet and NASA Mars 2020 flight-mechanics paper (`edquist_2022_mars2020_aerothermal_entry_masses`; `jpl_msl_factsheet_curiosity_mass`; `nasa_mars2020_flight_mech_edl_simulation`; rc-770).

Verdict: the two measured analogues and their limits are named; the 0.30 value is unchanged. Extracted data: none new.
# Domain 9 — In-space delivery mass fractions & EDL survival (R54)

## R891 — Spacevalue Mars-surface entry-survival citation trail (2026-11-18)

`spacevalue_mars_surface_entry_survival_note_current_2026` — At `spacevalue/catalog.py` lines 412–417, the Mars-surface note interpolates the EDL leg as 30% and says “MSL / Perseverance measured”; it names no study or source figure. `spacevalue/CITATIONS.md` lines 3–6 says the `catalog.py` note beside a value identifies its source and figure.

`spacecost_mars_landed_fraction_basis_current_2026` — At `spacecost/delivery.py` lines 298–307, the 0.30 fraction is paired with MSL entry 3,153 kg → rover 899 kg (28.5%) and Perseverance entry 3,369 kg → rover 1,026 kg (30.5%); the comment attributes the entry masses to Edquist et al. 2022. `spacecost/CITATIONS.md` §8 points readers to that comment.

`edquist_2022_mars2020_aerothermal_entry_masses` — Table 3 (PDF p. 14) lists MSL BET entry mass 3,153 kg and Mars 2020 BET entry mass 3,369 kg. `jpl_msl_factsheet_curiosity_mass` gives Curiosity as 899 kg; `nasa_mars2020_flight_mech_edl_simulation` states “At 1026 kg, Perseverance is the largest” (PDF p. 1). The paired ratios are 28.51% and 30.45%; 0.30 lies between them.

**Verdict:** The 30% destination-note figure has supporting measurements in the registry and a source trail in Spacecost, but the Spacevalue note does not identify those sources or figures under its own citation convention. Open `rc-770` for the downstream attribution gap; applied `rc-039` corrected the Spacecost comment figures and does not cover the Spacevalue note. No replacement value inferred. Extracted data: `extracted_data/r891_spacevalue_mars_surface_citation_gap.csv`.

## R731 — Downleg capsule dry-mass factor (2026-11-14)

`parcero_etal_2022_planetary_entry_vehicles_quick_reference_guide_v4` — NASA’s Hayabusa entry-vehicle table lists “Vehicle mass 18 kg,” “Payload mass 1.04 kg,” and “TPS mass fraction, inc. insul. 43%” (PDF p. 23). This is a small sample-return entry vehicle, not a bulk-cargo container, and supplies no generic cargo-container scaling.

`spacecost_downleg_capsule_dry_fraction_record_2026` — at spacecost `a401930efe30aaad01aafd2b3cb332ad0438c841`, `delivery.py` sets `DOWNLEG_CAPSULE_DRY_FRAC = 0.10` as “capsule dry mass per kg of cargo” (line 420); `downleg_cost_usd_per_kg` uses it directly for `capsule_kg` in the hardware cost term (lines 703–705). The declaration gives no geometry, component scope, source, or sensitivity for the 0.10 value.

**Verdict:** Hayabusa provides a non-like-for-like context comparator, not a replacement. No bulk-cargo capsule sizing source or uncertainty is stated for the 0.10 factor. Open `rc-598`; distinct from rc-497’s capsule recurring cost, rc-135’s TPS fraction, and rc-134’s TPS mass scaling. Extracted data: `extracted_data/r731_hayabusa_and_downleg_capsule_mass_basis.csv`.

Backings: spacecost `delivery.py` typed constants with no table row: `MARS_LANDED_MASS_FRACTION = 0.30` (sets the published mars_surface price; the comment calls it "Measured, not assumed" from MSL and Perseverance), `LANDER_DRY_MASS_FRAC = 0.20` and `TUG_DRY_MASS_FRAC = 0.10`.

**Sources (R54):**

- `edquist_2022_mars2020_aerothermal_entry_masses` (NTRS 20210024709, hosted): Table 3 (p14) entry masses: MSL BET 3153 kg; Mars 2020 TPS design cases 3436/3436 kg; Mars 2020 BET 3369 kg.
- `nasa_mars2020_flight_mech_edl_simulation` (NTRS 20210024480, hosted), p1: "At 1026 kg, Perseverance is the largest, most sophisticated rover ever delivered to another planet."
- `jpl_msl_factsheet_curiosity_mass` (live): Curiosity "899 kg in Earth gravity" (1,982 lbs).

**Audit:** MSL 899/3153 = 28.51%; Perseverance 1026/3369 = 30.45% (29.86% on the design case). Band [28.51%, 30.45%]; 0.30 sits inside at the optimistic edge (+5.22% vs MSL, -1.49% vs Perseverance), as the code's "takes the better of the two" says. `extracted_data/r54_mars_edl_landed_mass_fractions.csv`.

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

`extracted_data/r139_edl_mass_budget_key_numbers.csv`.

## R147 - LANDER_DRY_MASS_FRAC backed by as-flown Apollo data (no new sources)

From the hosted SP-4029 (`sp4029_apollo_by_the_numbers`, d03):

- p287 'LM Descent Stage' dry weights: A9 4,265 lb / A11 4,483 / A12 4,875 / A13 4,650 (A10, A14-A17 OCR-damaged). Footnote 14: weights "as published in mission press kits".
- p305 'LM Descent Stage Propellant Status': A9 18,040 lb (fuel 6,977 + oxidizer 11,063) up to 19,564.2 lb for A17 = 8,183-8,874 kg.

The comment's 2,134/(2,134+8,200) = 0.2065; 8,200 kg sits in the A9-A13 loaded band (8,183-8,362 kg). As-flown dry/(dry+propellant): A9 0.1912, A11 0.1978, A12 0.2092, A13 0.2014, so 0.2065 and the dial 0.20 both sit inside. No candidate. `extracted_data/r147_lm_descent_stage_mass_key_numbers.csv`.

## R974 — Spacecost return-capsule bibliography omits the Hayabusa guide (2026-11-19)

- `spacecost_citations_report_reference_gaps_current_2026`: At Spacecost main `868f42890ac97ee40a50d79f7b33863046edb0ff`, `spacecost/delivery.py` lines 420–426 call the generic 0.10 downleg capsule factor a scenario and cite the Hayabusa table as a non-substitute; `CITATIONS.md` §4 lists a Stardust press kit but omits NASA/SP-20220010761.
- `parcero_etal_2022_planetary_entry_vehicles_quick_reference_guide_v4`: Printed p. 23 lists “Vehicle mass 18 kg,” “Payload mass 1.04 kg,” and a 43% TPS mass fraction including insulation.
- **Verdict:** open **rc-834**; add Parcero et al.’s full NASA/SP-20220010761 entry, official NTRS link, and Hayabusa table locator to §4. The sample-return evidence does not replace the generic cargo factor; this bibliography gap is separate from rc-598.
- **Extracted data**: `extracted_data/r731_hayabusa_and_downleg_capsule_mass_basis.csv`.

## R985 — Spacecost Hayabusa capsule guide referenced upstream (2026-11-19)

At Spacecost main 5ae7f70855d24c71dc54fc3a916624f325c034e8 (PR #53, 0.18.6), CITATIONS.md section 4 gains `parcero_etal_2022_planetary_entry_vehicles_quick_reference_guide_v4` with its Hayabusa table locator, scoped as a sample-return comparator beside the generic 0.10 capsule factor (rc-834). Values unchanged.

Verdict: rc-834 closed as applied. Extracted data: none new.


## R1075 — Mars powered-descent mass boundary and TPS pricing (2026-11-24)

- spacecost_mars_delivery_stage_loss_pricing_2026 records Spacecost's Mars surface chain with 0.30 “survives to be useful payload” followed by an 800 m/s terminal burn. edquist_2022_mars2020_aerothermal_entry_masses, p. 14 Table 3, gives 3,153 and 3,369 kg at atmospheric entry. jpl_msl_factsheet_curiosity_mass and nasa_mars2020_flight_mech_edl_simulation, the latter p. 1, give delivered rover masses of 899 and 1,026 kg. sell_etal_2013_msl_as_flown_powered_descent, abstract, states powered flight “extends from backshell separation through landing.” The pinned chain implies 23.97% delivery from atmospheric entry. With only the terminal burn set to zero for sensitivity, LEO mass per delivered kg moves from 10.606 to 8.472 and delivered cost from $186,307 to $140,788/kg. dwyer_cianciolo_etal_2020_edlas_phase3_mass_tps, p. 10 Table 5, gives 58,786 and 54,910 kg entry masses for two 20 t useful payload concepts. **rc-981** records the stages and the flight-ratio boundary.
- spacecost_mars_delivery_stage_loss_pricing_2026 records “USD per kg of TPS mass” for the $50,000/kg Earth-return TPS rate. The Mars chain applies it to 2.9208 kg of modeled EDL discard per kg landed, yielding $146,041/kg landed or 78.4% of total delivery cost. dwyer_cianciolo_etal_2020_edlas_phase3_mass_tps, p. 10 Table 5, separately lists “Total TPS Mass” of 3,454 and 3,634 kg and vehicle structure masses of 12,168 and 8,796 kg for its two cases. **rc-982** records the mass denominator and hardware-cost citation.

Extracted data in extracted_data/r1075_mars_edl_stage_and_tps_cost_boundaries.csv.
