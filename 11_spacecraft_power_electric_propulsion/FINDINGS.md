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

rc-100 (battery: Schmitz 175 Wh/kg at 80% DoD, usable 140 vs 104), rc-102 (AEPS ~9 kg/kW string; NEXT-C mass mismatch 12.7 vs 13.5 kg), rc-104 (no source for $10-15M per string; PPE $12.2M/kW element), rc-105 (RTG $/W from institutional unit costs), rc-120 (economicspace: Pu-238 1.5 kg/yr is a goal). Texts in `revision_candidates.csv`.
