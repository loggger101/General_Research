# Domain 11 — Spacecraft power & electric propulsion

Backings: the power and electric-propulsion rows of spacecost `reference/operational_costs.csv` (EP efficiency, thruster and PPU specific mass, RTG specific power and cost, power-system specific mass, EP recurring cost).

## R66 - Domain opened with four hosted NTRS papers

Targets: 'Electric propulsion efficiency' 0.6 [0.45-0.72]; 'Electric thruster + PPU specific mass' 8 kg/kW [5-15]; 'Power processing unit specific mass' 4.7 kg/kW; 'RTG specific power' 5.0 W/kg [2.4-5.5] (note: GPHS 5.2, MMRTG 110 We / 45 kg = 2.4); 'Power system specific mass' 60 W/kg [30-150] (note: ROSA ~150 at the wing).

- **thomas_2025_advanced_next_iepc** (IEPC-2025): "8.2 kW; ~3,400 sec Isp; ~330 mN, F/P = 40 mN/kW" (p4); "a 40% increase in thrust (330 mN)" and "comparable mass and volume relative to the NEXT-C system" (p15); PPU efficiency 92%-95% (PPU only). Extends every NEXT-C point (nextc_protoflight_2021 caps at 6.85 kW / 235 mN); supports the PPU row.
- **shastry_2024_aeps_hall_qualification_production** (IEPC-2024): "210mm in height by 530mm in diameter, with a total mass of 53kg"; ~600 mN and ~2800 s at 12 kW (p4); QM1 acceptance at 600 V: 9 kW 444 mN / 2605 s, 10 kW 491 / 2651, 11 kW 540 / 2704, 12 kW 586 / 2736 (+/- 5 mN, +/- 25 s; p7). Head alone 4.42 kg/kW at 12 kW, below the 8 kg/kW string row.
- **frieman_2021_aeps_etu2_extended_characterization** (AIAA 2021): measured Hall total efficiency 51.4% (300 V / 2.60 kW) to 69.4% (600 V / 12.50 kW, PPE characterisation mean; 67.1% at RFC) (p6, p9). The note's "Hall thrusters run 0.50-0.60" is low at the top; the 0.6 value and band hold (rc-040 proposes ~0.51-0.70).
- **schmitz_2023_rps_vs_solar_array_comparison** (IEEE Aerospace 2023): BOL specific power MMRTG 2.7 / NextGen Mod-1 4.4 / DRPS 3.7 W/kg (p4); Lucy array 415 W/m2 and 184 W/kg at 1 AU, 32% efficiency (p8). The 5.0 RTG row matches GPHS-class hardware (historical 5.3 W/kg in the NETS companion), 13.6% above Mod-1; the note's MMRTG 2.44 is 9.5% under 2.7; Lucy's 184 W/kg is 22.7% above the cited ROSA figure. No per-W costs.

## R67 - RTG cost and Pu-238 production (two OIG audits, hosted)

- **nasa_oig_2017_ig-17-009_mars2020_project** p14 Table 3: "Multi-Mission Radioisotope Thermoelectric Generator 66 66 70" ($M, MCR / KDP-A / KDP-C): $600-$636k per W at 110 We if one unit; the $500k/W centre sits 16.7-21.4% below, inside [$200k, $1M].
- **nasa_oig_2023_ig-23-010_rps_program_management** p13 Table 1: MMRTG 4.8 kg Pu-238, 32 clads, 110 W BODL, 63 W EODL, 44 kg; Next-Gen Mod-1 9.6 kg, 64 clads, 245 W, 177 W, 56 kg (4.38 W/kg, matching Schmitz's 4.4). p27: "an annual CRP goal of 1.5 kg per year by 2026"; "although DOE planned to produce a total of 1.5 kg from 2018 through 2021, they produced only 0.77 kg—about half the projected amount". p3: no viable new RPS technology since 2010 despite ~$40 million a year. The note's 45 kg MMRTG is 2.3% high. DRPS 150-200 kg.

## R68 - Gateway PPE contract values (two OIG audits, hosted)

Target: 'Electric propulsion system recurring cost' $1.5M/kW [0.5-3.0] (note: ~$10-15M per NEXT-C string, secondary).

- **nasa_oig_2020_ig-21-004_gateway_program_management**: May 2019 award to Maxar "for a potential value of $375 million" (p18); Table 3 (p17) $453,573,559, obligated $223,495,810 (49%), performance period 5/23/2019 to 2/28/2026; of $78.5 million growth, $51 million NASA-driven changes, $24 million task order, $3.5 million co-manifest; two ROSA arrays of ~8 x 20 m at 32.5 kW each for 60 kW (p25); Aerojet would not fix-price its PPU, so Maxar supplies power components "except for the government furnished electrical thrusters" (p26).
- **nasa_oig_2023_ig-24-003_artemis_supply_chain**: PPE "Fixed-price $730.9 million" as of 2023-04-18 (p12); Russia and Ukraine supply 25 to 30 percent of xenon and krypton, and Maxar has procured PPE's xenon (p20).

Element-level: $6.25M/kW (award), $7.56M (2020), $12.18M (final; +61.14% from 2020, +94.91% from award), far above the EP-train-only centre as expected. Thrusters are bought separately from the bus, as the row models.

## R69 - NASA FY2025 budget request (hosted)

`nasa_fy2025_budget_request_congressional_justification` (April 2024). SEP: BA $18.5M (FY23) -> $1.7M (FY29) (p4); January 2024 MPAR LCC $402.5M, total budget $360.2M (p221); p225 table rows as printed: "Nuclear Thermal Propulsion 90.0 -- 92.5 53.0 37.0 28.0 25.0 Nuclear Electric Propulsion 1.3 -- 17.5 17.5 17.5 17.5 17.5 Total Budget 91.3 -- 110.0 70.5 54.5 45.5 42.5"; "the first operational demonstration of the SEP 12-kilowatt (kW) thruster will be on the Power and Propulsion Element (PPE)" and harness modifications "for the three flight models" (p221); development cost $203.2M (2022, JCL 70%) -> $223.2M (+9.8%), Science/Technology 159.7 -> 172.8, other 43.5 -> 50.4; QSAR-1 Jun 2024 -> Dec 2024, QSAR-2 Jun 2025 -> Aug 2026, life-qual report Oct 2028 -> Jan 2029; GRC manages the Aerojet Rocketdyne contract, JPL thruster testing (p222-223). $402.5M / 60 kW = $6.710M per kW development-phase. NTP $90.0M (FY23) / $92.5M (FY25) -> $25.0M (FY29) plus NEP $17.5M/yr (p225).

## Maintenance (2026-09-26) - Corrections

- **R69:** the 12-kW SEP thruster is AEPS (p222 "Advanced Electric Propulsion System Life Qualification Test Report"; p224 AEPS contract), not NEXT-C: three AEPS flight models for PPE; NEXT-C per-string pricing stays a gap. R69's "$6.25k-$12.18k/kW" should read $6.25M-$12.18M per kW.
- **R67:** the 'RTG specific power' note says "DOE Pu-238 production runs ~1.5 kg/yr"; IG-23-010 p27 calls 1.5 kg/yr the 2026 goal (0.77 kg made 2018-2021) and p30 says production above 1.5 kg/yr cannot be funded. **rc-043** (wording).

## R70 - Full extraction (2026-09-27)

26 files in `extracted_data/`: `r70_frieman_2021_aeps_etu2_extended_characterization.csv` (2), `r70_frieman_2021_aeps_etu2_performance.csv` (16), `r70_nasa_fy2025_budget_all_budget_authority_lines.csv` (701), `r70_nasa_fy2025_budget_development_cost_commitments.csv` (17), `r70_nasa_fy2025_budget_development_cost_details_by_element.csv` (112), `r70_nasa_fy2025_budget_funds_distribution_by_center.csv` (99), `r70_nasa_fy2025_budget_project_lifecycle_tables.csv` (78), `r70_nasa_oig_2017_ig-17-009_mars2020_project.csv` (7), `r70_nasa_oig_2017_ig-17-009_table3_mars2020_estimate_history.csv` (9), `r70_nasa_oig_2017_ig-17-009_table5_mars_program_lifecycle_costs.csv` (16), `r70_nasa_oig_2020_ig-21-004_gateway_program_management.csv` (1), `r70_nasa_oig_2020_ig-21-004_table2_gateway_budget.csv` (11), `r70_nasa_oig_2020_ig-21-004_table3_gateway_contracts.csv` (3), `r70_nasa_oig_2023_ig-23-010_rps_program_management.csv` (7), `r70_nasa_oig_2023_ig-23-010_table1_rps_technologies.csv` (5), `r70_nasa_oig_2023_ig-23-010_table2_power_system_cost_mass.csv` (15), `r70_nasa_oig_2023_ig-23-010_tables3-5_decadal_missions_power_cost.csv` (18), `r70_nasa_oig_2023_ig-24-003_artemis_supply_chain.csv` (3), `r70_nasa_oig_2023_ig-24-003_table1_artemis_prime_contracts.csv` (22), `r70_schmitz_2023_rps_performance_table.csv` (3), `r70_schmitz_2023_rps_vs_solar_array_comparison.csv` (5), `r70_schmitz_2023_solar_battery_mass_for_100W_by_location.csv` (19), `r70_shastry_2024_aeps_hall_qualification_production.csv` (11), `r70_thomas_2025_advanced_next_iepc.csv` (6), `r70_thomas_2025_advnext_ppu_supplies.csv` (6), `r70_thomas_2025_advnext_throttle_table.csv` (10).

- **Licence flag for the owner:** every page of the hosted `shastry_2024_aeps_hall_qualification_production` PDF says "Copyright 2024 by the Electric Rocket Propulsion Society. All rights reserved." while its basis is NTRS GOV_PERMITTED; all its numbers are now extracted.
- AdvNEXT throttle table: 10 levels, 71-330 mN, 2,530-3,424 s (2 eta / (g0 Isp) reproduces mN/kW). AEPS ETU-2: recomputed efficiency agrees within ~0.5 point except the 69.4%, 1.6 points high (edge of +/-1.7%).
- Schmitz: solar + battery mass for 100 W continuous (Moon ~284 kg, Callisto ~208, Iapetus ~920, Triton ~1,225 vs MMRTG ~40); the legend's "194 W-h/kg" is Table 3's 194 Wh/L; Table 3 gives 175 Wh/kg.
- IG-23-010 Table 2 power-system costs: MMRTG 5 / 6 / 9 units $114M / $129M / $174M; Mod-1 2 / 3 / 4 units $95M / $120M / $145M; DRPS 2 / 3 units $89M / $114M; solar $24M (Lucy), $72M (Europa Clipper). MMRTG rows reproduce units x 86.5 W; the "Mod-1" 248 W per unit matches Mod-0, not Mod-1. Plus 18 Decadal missions.
- IG-17-009 Table 5: every Mars mission 1964-2020, sums exactly to $24,370M (FY2016); Mars 2020 MCR $1,811M -> ABC $2,442M.
- Gateway budget FY2015-2025 (rows sum); Artemis prime contracts $63.5B (Orion $15.0B, Boeing stages $9.7B, HLS SpaceX $3.5B / Blue Origin $3.4B, PPE $730.9M).
- FY2025 request: 701 BA lines, 16 life-cycle tables, centre funds sum 25,383.8, 16 commitments (Gateway $3,561.8M, Europa Clipper $2,412.8M -> $2,509.0M, SLS Block 1B $3,675.0M). Kept as printed: Block 1B elements sum to $3,657.0M vs $3,675.0M.

## R72 - Remaining tables (2026-09-27)

`r72_ig17009_tables2_6_mass_margin_technology.csv` (4), `r72_nasa_fy2025_mpar_summary_table.csv` (16), `r72_shastry_2024_table1_qm1_atp_performance.csv` (4). FY2025 MPAR (p774): Orion $9,622.4M (+3%), later $10,174.4M (+9.4%); SEP $203.2M -> $223.2M. AEPS QM1 thrust efficiency 0.630-0.655 on discharge power, inside rc-040's band. Mars 2020 mass 3,393 kg against 3,540 kg (4% margin, 3% required); five of seven critical technologies below TRL 6 in November 2016.

## R84 - FY2026 budget documents (2026-09-30)

FY2026 Budget Technical Supplement (May 2025) and FY2026 Spending Plan for PL 119-74 (July 2026), hosted:

- SEP is now a Space Transportation project: BA $8.5M (FY24), request $7.7 -> 6.6 -> 5.7 -> 1.7 -> $0 by FY30; development $223.2M, JCL 70%, +9.8% on $203.2M; enacted $7.2M.
- "This budget funds the orderly shutdown of the Gateway program": $447.5M (FY24), $267.3M and $212.9M requested, zero after; enacted close-out $150.0M within Moon To Mars Systems Development ($3,465.9M). PPE combines 12 kW and 6 kW SEP thrusters from STMD investments (the AEPS hosted here).
- "The nuclear propulsion projects are terminated to achieve cost savings"; DRACO cancelled by its partner.
- RPS $175.5M -> $139.0M; Pu-238 production continues (MMRTG for Dragonfly); NextGen RTG sustainment terminated.
- QSAR-1 -> Feb 2026, QSAR-2 -> Jun 2027, life-qual report Oct 2028 -> Jan 2029.

`extracted_data/r84_fy2026_sep_gateway_budget_lines.csv`.

## R113 - NEP power-system specific mass (2026-10-04)

The `Nuclear electric (NEP, xenon)` row (TRL 4, Isp 5000 s, spacecost@85da36c) is gated off.

- **`polzin_et_al_2026_nep_technology_maturation_plan`** (NASA/TP SNP-PLAN-0043 Rev 1.1, 2026-02-16, hosted): Table 2.1 power-system specific mass 24 kg/kWe threshold, 13 kg/kWe target (41.7 and 76.9 We/kg) for 2-4 MWe; an opposition-class crewed Mars mission closes at 13-24 kg/kWe and 2 MWe; most key NEP technologies at or below TRL 4.
- **`nasa_sr1_freedom_mission_page`** (read): Space Reactor-1 Freedom, ~12,000 kg, 20 kWe HALEU Brayton reactor, 48 kW PPE bus, 12-kW Hall thrusters, launch late 2028 to Mars: 1.67 We/kg whole vehicle.

`extracted_data/r113_nep_key_numbers.csv`. The row is gated, not wrong.

## R114 - Nuclear-thermal KPPs (2026-10-04)

`burns_2022_inl_subscale_maturation_ntp_reactor_testing` (INL/RPT-22-65557) p13: exit temperature above 2,700 K, 10,000-15,000 lbf, 900 s Isp, reactor below 3,500 kg, more than 2 h cumulative burn and 2 restarts: the 900 s cell is a requirement; NERVA (d10) is the demonstrated record. `extracted_data/r114_gr_links_key_numbers.csv`.

## R163 - Solar arrays priced per delivered watt (rc-091; 2026-10-14)

economicspace@f7fe1c6 `_mission_cost_prologue` prices the plant array as `processing_power_w x $800/W` and the EP array as `ep_power_w x $800/W` while their masses scale with 1/a² (and the plant's 2.11x eclipse oversize): at 2.7 AU an array is ~15x heavier per delivered watt (7.29 x 2.11) at the same cost. IG-23-010 Table 2: Lucy $24M for 500 W (168 kg), Europa Clipper $72M for 798 W (525 kg): $48,000 and $90,226 per watt, ~$140,000 per kg. Hoffman 2000 MBAT: $14.1M for 7.5 kW EOL at 1.5 AU = $1,880/W there, $836 per 1-AU watt. $800 fits a 1-AU-rated watt; at the Trojans it values array mass at $1,772/kg, 80.6x below Lucy's. rc-091 proposes pricing per installed 1-AU watt. `extracted_data/r163_solar_power_cost_per_watt_vs_upstream.csv`.

## R164 - Candidates (2026-10-14)

rc-100 (battery: Schmitz 175 Wh/kg at 80% DoD, usable 140 vs 104), rc-102 (AEPS ~9 kg/kW string; NEXT-C mass mismatch 12.7 vs 13.5 kg), rc-104 (no source for $10-15M per string; PPE $12.2M/kW element), rc-105 (RTG $/W from institutional unit costs), rc-120 (economicspace: Pu-238 1.5 kg/yr is a goal). Texts in `revision_candidates_closed.csv`.

## R210 - rc-181 opened on the EP recurring-cost anchor; two seams closed clean (2026-10-19)

spacecost operational_costs.csv 'Electric propulsion system recurring cost' ($1.5M per kW input power, band $500k-$3M) rests entirely on an uncited procurement-class assertion - procured in the $10-15M-per-string class for a NEXT-C flight string. No document is named anywhere upstream: CITATIONS.md at @29a7ced carries no NEXT-C entry in any section (only the SETS Space xenon/argon/krypton pricing line matches an EP grep). Anchor hunt this round found no public per-string or per-kW figure: OIG IG-23-005 STMD portfolio review pulled live and read all 35 pages mentions the Solar Electric Propulsion project qualitatively only (near-miss, not registered per convention); usaspending spending_by_award keyword probes for NEXT-C thruster return zero rows from this machine; frieman_2021_aeps_etu2 and shastry_2024 are registered for AEPS performance not procurement price. rc-102 and rc-103 claim the two specific-mass rows beside it - the recurring-cost anchor was unclaimed before this round.
Seams closed clean: (1) spacecost CHANGELOG.md dollar-line sweep, 101 figure-bearing lines read against live v0.12.0 cells - all historical or consistent; notably Propellant tank $6,000/kg matches its cell exactly with the notes transparently deriving ~$5,300/kg from Centaur and rounding up as a stated lower bound. (2) The unnamed '(AIAA 2024)' of rc-180 stays unresolvable: Crossref title and bibliographic sweeps over 2023-2025 find no AIAA pricing paper; closest is Masse et al. SCITECH 2024 Hydrazine-Based Green Monopropellant Blends (10.2514/6.2024-1619) behind a paywall with zero OA license, no NTRS record and no arXiv entry - not registered since its price table cannot be verified.
EP cost cluster now fully claimed: rc-181 (this row), rc-102/rc-103 (mass rows); skip unless upstream names a procurement document or USAspending award records become reachable from institutional access.

## R294 - spacecost storage_systems.csv audit, skip-note (2026-10-28)

Audited reference/storage_systems.csv at @860bef9 from raw committed bytes (20 rows x 12 columns, uniform parsed width). Band containment holds on all 20 rows inclusive of endpoints; no headline-vs-band convention applies to this table (the two values within 2 percent of their geometric band-centre - COPV burst factor and sintered cargo - are coincidences: exact band_centre reproduction per spacecost vehicles.py gives 387,000 not 392,000, and 346 not 350). The table is a value/band estimate registry with no derived-column physics layer; R282 already swept it under the self-citation contract (rc-225) and rc-224 covers the tanker row.

RTG specific power row: probed for mixed denominators between its GPHS-RTG and MMRTG comparison figures - FALSE ALARM, cleared against institutional records fetched this round. NASA MMRTG fact sheet (science.nasa.gov/wp-content/uploads/2024/02/mmrtg-factsheet-updated-5-18-20-1.pdf, 992,530 B sha256 5599c14ef6b66a989dfc7323b05d945bca170fc74b64ed5f1bd9358f95fc1e70, US government work) prints weighs about 94 pounds (45 kilograms), approximately 2,000 watts of thermal power, and 10.6 pounds (4.8 kilograms) of plutonium dioxide - each count==1 on the text layer. The NASA-funded Next-Generation RTG Final Report (rtg-study-d-99657-final-report-june-2017, science.nasa.gov copy, export-marked therefore extraction-only if ever registered) comparison table p.83: GPHS-RTG 282 W / 57 kg and MMRTG 95 W / 45 kg; New Horizons Final EIS on nasa.gov prints the GPHS-RTG has a mass of about 56 kg (123.5 lb).

The upstream note prints 44 kg for MMRTG because applied rc-041 (R67) corrected it from 45 to 44 citing IG-23-010 Table 1 - an adjudicated institutional-figure choice already implemented in spacecost v0.5.2; never re-open against the fact-sheet figure of 45. The derived comparison figures (GPHS-class ~5.2, MMRTG ~2.5 W/kg) match the record within rounding of BOM-versus-EOL power quotes across sources. Stored value 5.0 with band [2.4..5.5] brackets both flight classes; economicspace worked_calculation.py L2590 feeds val() of this row to RTG-shaped campaign cells (plant mass = draw / w) - documented-by-design.

Do not re-sweep storage_systems.csv physics unless value/band columns move at a future spacecost tip.


## R314 - Electric ISRU stages are sized from a placeholder propellant book (2026-11-01)

`economicspace_electric_stage_placeholder_propellant_record_2026`: at
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`
L4315-4324 returns an ISRU "Placeholder cascade" with `m_return_prop=0` and
outbound propellant for the empty-return-vehicle floor. The sizing loop sends
this cascade to `_ep_stage_kg` at L6336-6343. That helper sums its outbound and
return propellant, sizes power and thrust to `ep_target_thrust_yr=3`, and
reports that same three-year duration (L3887-3909). The actual capped return
propellant and outbound book are rebuilt later (L6648-6680), with no EP resize.
The mission-duration check then reads the provisional three years, not the
burn time of the settled load (L6849-6853). The configured limit is 25 years.

The complete original evaluator and its original numerical helpers return
the following synthetic missions using the committed `Falcon 9 (reusable)`
and `Water  (gridded ion / ECR)` rows of spacecost@860bef9, and its 46 original
operational rows. The body is 1e9 kg, density 2 g/cm3, water fraction 0.2 and
semi-major axis 1.2 AU. Caller delta-v is 1,000 m/s per leg, multiplied by the
row's 1.5 penalty. These are function-level witnesses, not observed catalog
bodies or an orbital-trajectory claim. Refinery, launch windows, water heating,
volatile containment and propellant boil-off are initially off. Market pricing
is unbounded and programme-scale search is off; other defaults, including the
three-year EP target and 25-year mission limit, remain. The CSV records all
effective settings and inputs.

| raw cargo cap | returned cargo (kg) | reported EP power (W) | settled propellant (kg) | reported thrust (yr) | thrust at reported power (yr) |
|---|---|---|---|---|---|
| 100 kg | 100 | 564.838636 | 588.958312 | 3 | 3.676923 |
| 1,000 kg | 1,000 | 567.674729 | 812.566903 | 3 | 5.047588 |
| 10,000 kg | 10,000 | 589.800641 | 3,037.703941 | 3 | 18.162037 |
| no caller cap | 77,391.923434 | 589.800641 | 19,173.783007 | 3 | 114.637559 |

For the 10,000 kg case, the final stage-sizing input contains only
501.767042 kg outbound propellant and zero return propellant. The settled
mission carries 805.414055 kg outbound and makes 2,232.289886 kg for return.
The original power relation, `P=m_prop*(Isp*g0)^2/(2*efficiency*t)`, inverted
at its reported 589.800641 W, 900 s Isp and efficiency 0.35 gives 18.162037 yr.
Independently inverting its reported 0.046777833 N thrust gives the same time.
Using the original stage helper on that fixed settled book instead requires
3,570.660447 W for three years; this diagnostic does not include the feedback
of flying a larger stage and is not a completed replacement design.

All ISRU witness cases fit both the body and rig-throughput material budgets.
The uncapped case uses 169,888.004024 kg of the 219,150 kg throughput budget,
and reports a 5.298325 yr mission despite needing 114.637559 yr of thrusting
alone at the reported power. Switching tank mass off still gives 18.531251 yr
for the 10,000 kg case: this defect is independent of rc-241's fuel-feed
resource check. With water liberation and volatile containment on, that case
still needs 16.785576 yr; with those features on and no caller cap, 71,012.935069
kg cargo is accepted with a 5.144580 yr reported mission but 98.216220 yr of
thrusting at its reported power. The latter also fits both material budgets.

Controls: a non-ISRU xenon mission that fills its launch budget implies
2.999375 yr, consistent with the loop's 1% convergence tolerance. Capping that
non-ISRU body to 100 kg instead leaves the opposite mismatch: a full-vehicle
stage, whose actual propellant only needs 0.139848 yr. Switching the low-thrust
model off explicitly reports zero EP mass, power and time; no inversion is
made for that control.

Verdict: the electric stage and its duration refer to a different propellant
book from the returned mission. `rc-244`: couple EP sizing to the actual
capped outbound and ISRU-return loads, and propagate settled thrust duration
through feasibility and cost. Current-catalog incidence and ranking effects
were not measured. `extracted_data/r314_electric_stage_vs_settled_propellant.csv`.

## R316 - Electric propulsion hardware is missing from the return mass book (2026-11-01)

Source `economicspace_electric_stage_return_mass_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0 `modules/calc.py`, with
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f original reference rows and
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011 cargo helpers. The EP helper
returns array, PPU and thruster mass (L3899-3911). That mass enters
`hardware_total_kg` (L6742-6746), which is carried outbound and added at the
asteroid (L6670-6675). The return dry mass is only the configured floor plus
payload-dependent structure/containment (L6640); post-burn return mass adds
the payload, TPS and return tank (L6650-6653), with no EP term. The stage is
sized from both legs' propellant, although its mass is carried on one leg.

Nine complete original-evaluator cases use original numerical helpers and
reference rows. The main witness is a synthetic 1e9 kg, 2 g/cm3 body at
1.2 AU, actual Falcon 9 reusable and electrospray rows, caller delta-v
2,500 m/s each way (row penalty 1.5), raw cargo, no ISRU or aerocapture,
single-mission market, synthetic 100 USD/kg silicate cargo. Windows,
refinery, water liberation, containment and boil-off are disabled for the
isolation case. It accepts 6,047.515549 kg cargo and reports 10,214.098028 kg
of EP hardware, 1,236.188075 kg return propellant and 3.25 years total mission.
All non-cargo mass after the return burn, including the tank, is only
1,432.050479 kg.

The model's own momentum-flux relation and adopted 10,000 kg/N electrospray
rate give an independent lower bound. Even granting the entire mission,
including outbound travel and mining, to thrusting on return:
`T_min = m_return_prop * Isp * g0 / mission_seconds = 0.295500286 N`, so
thrusters alone need at least 2,955.002864 kg. This already exceeds all return
dry mass by 2.063477 times, before adding any array, PPU, tanks or structure.
Thus an unspecified allocation inside the capsule floor cannot close the
book under the adopted device model. The bound uses actual returned fuel
and full reported mission time, independently of provisional EP timing.

| case | all reported return dry mass (kg) | minimum return thrusters using the entire mission (kg) |
|---|---|---|
| electrospray isolation | 1,432.050479 | 2,955.002864 |
| electrospray, tank mass off | 1,423.557098 | 2,994.920785 |
| electrospray, default physical flags at 1.8 AU | 1,342.218266 | 2,129.632951 |
| PPT, same 2,500 m/s caller legs | 1,222.904936 | 1,324.495917 |

A separate diagnostic relocates the unchanged reported EP unit from one-way
hardware to return dry mass, counting it once. Keeping the original cargo
then requires 19,420.248042 kg launch mass against the 17,400 kg capacity;
the original closed-form helper refits to 1,032.431902 kg cargo at that fixed
stage size. This is not a completed joint mass/power redesign. A xenon case
confirms the missing placement without exceeding the generous thruster-only
bound. Chemical and low-thrust-off controls have no explicit EP mass; with
zero return delta-v the return impulse bound is zero and moving the stage
does not increase launch mass. A zero-outbound-delta-v limiting case has
exactly three years of actual-book thrusting and still fails the return
hardware bound. Every case is a resource-safe single mission, isolating
the ISRU and programme-resource candidates.

Verdict: the declared electric propulsion hardware has no return-leg mass
allocation, and accepted cases cannot hide it within the existing return dry
allowance. `rc-246`: carry a shared EP unit through the return burn, or size
and account for separate stages and jettison events, then re-solve the coupled
mass/power problem. No observed-catalog incidence or ranking effect was
measured. `extracted_data/r316_electric_stage_return_mass.csv`.

## R345 - The RTG ceiling rejects a trial before smaller cargo is searched (2026-11-03)

`economicspace_rtg_payload_search_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0. The trial payload is bounded by
launch capacity, body mass and throughput (calc.py L6350-6354). The RTG check
calls its ceiling a "hard constraint, not a preference" (L6467-6474), then
returns None if that trial exceeds it. The normal consumer prices solar
alongside RTG (L8180-8200), but does not search smaller RTG cargo before
discarding that architecture. The final power check remains valid; the
intermediate oversized trial does not establish that every payload fails.

Twenty-three controlled fixtures run original, exact repeat, bounded-RTG
alternative, its exact repeat, and the original/alternative with excavation
charged: 138 complete `evaluate_asteroid` calls. The unchanged original
kernel prices the bounded cargo through its existing `payload_cap_kg`
argument. Every original candidate remains available and the original
selection objective chooses the winner. Fourteen cases improve, including
four restored native refusals; nine controls retain identical winners.

At 20 AU, homogeneous magnetite and configured 1000 m/s reference burns on
each leg, the first RTG trial is 18,592.349374 kg at 88,500 W and returns None
at L6474 under the 5,000 W ceiling. The actual Falcon 9 reusable/kerolox
consumer instead selects solar: 142.256523 kg cargo, cost/revenue 8897.013496.
The unchanged 59-row LEO input gives refined-route energy
`(7 + 0.724*5)*1000 = 10620 Wh/kg`. With the 0.25-year stay floor, independent
power-limited cargo is `5000*(0.25*365.25*24)/10620 = 1031.779661 kg`.
An interior point 1e-12 below that bound converges in two passes at
4999.999999995 W, 5,869.325797 kg launch mass against 17,400 kg capacity, and
cost/revenue 3440.676043. Both prices and the selected refining route remain
unchanged. This is a better configured ratio, not a profit improvement.

The same fourteen gains persist when the separate raw-excavation gates are
enabled in memory. The added 200 Wh/kg changes the example's energy to
10820 Wh/kg and cargo to 1,012.707948 kg at the same power ceiling;
cost/revenue is 3505.042630 versus 8925.496630 for that corrected native
consumer. Two corrected native refusals are restored. Ilmenite, chromite,
mixed ore, different ceilings and a longer stay supply further gains.
Default beneficiation search and damping-disabled fixtures also reproduce.
Closer-in solar choices, small-body and large-ceiling RTG choices, RTG-off,
zero-refinery draw and a profit-objective fixture retain exact winners.

Verdict: `rc-281`, couple payload/stay/plant sizing to the RTG ceiling before
rejecting an architecture. Both repeats pass recursive native type/value
checks, including float.hex, and result digests. Every feasible result fits
launch, body-feed, time, volume and RTG limits. All examples are unprofitable
synthetic compositions with reference burns, not observed trajectories or a
population/ranking measurement. Thirty-one source/input blobs, including
all 22 imported local modules, match fresh pinned GitHub metadata; all four
live main comparisons are identical.
`extracted_data/r345_rtg_power_constrained_payload.csv`.
