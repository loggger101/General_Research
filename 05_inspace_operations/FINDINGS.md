# Domain 5 Findings — in-space storage / cryogenic boil-off, ISRU, operational costs

Backings: spacecost `storage_systems.csv`; the volatile-ISRU, power and electric-propulsion rows of `operational_costs.csv` (power and EP overlap domain 11; finance, licensing, operations, mining and hardware-rate rows moved to domains 16-21 in R77); environment penalties.

## R1 - Boil-off, transfer loss, ISRU yields (2026-09-17)

- **lac_bac_2024** [T1] (Cryogenics 148:104065; arXiv copy un-hosted 2026-09-26): finite-element LH₂ tank study. Boil-off: perlite 5905 W ≈ 0.04 %/day (the better stack), HePUR 35 350 W ≈ 0.24 %/day (round 1 had the labels swapped; corrected 2026-09-26). The hydrolox passive boil-off of 0.05 %/day sits beside the best case, with a ~6x spread by insulation that the MLI row (1.2 kg/m²) carries implicitly. Reliquefaction 5 kWh/kg (Kim et al.); local-area cooling shrinks the cooler when heat ingress is concentrated, the architecture the ZBO rows assume.
- **zero_bo_off_2025** [T2, hosted; arXiv preprint, no journal version]: LH₂ transfer between large ground tanks: VSD pump 0.00–0.24 wt%, fixed-speed 0.76–1.06 wt% per ~11,248 t transfer, against the in-space transfer-loss row's 3 % (1–8 %). Keep 3 % for current TRL and use this as range_low once space-rated pumps exist (rc-028).
- **ssap_2021** [T1] (Acta Astronautica 188:57-63; un-hosted; moved to d19): Table 3 products per 1000 kg of silicates at 100 % efficiency: CM/Murchison Fe 375 kg, O₂ 125, SiO₂ 260, H₂O 87; CI/Orgueil 65 / 3 / 430 / 118; H-chondrite 132 / 27 / 509 / none; peak ~950 °C. The CM-CI spread within one type argues for subtyping. Full table: `19_asteroid_excavation_beneficiation/extracted_data/ssap_2021_table3_theoretical_yields.csv`.

`extracted_data/storage_isru_key_numbers.csv`.

## R3 - Volatiles handling and plant decomposition (2026-09-18)

All NTRS, hosted:

- **kleinhenz_2016** (NTRS 20160010281): ~5 wt% water beds (per LCROSS); the single push-tube sample (65 g, long exposure) lost 88.9% of its water, the coring-auger samples (~115 g) 23-59% (R70 correction of "88% for coring"). `r70_kleinhenz_2016_deltion_capture_results.csv`.
- **kleinhenz_2018** (NTRS 20180005235): water escape across temperature and pressure; five-year average loss ~30% (5 wt% beds) and ~80% (0.8 wt% beds).
- **carlson_2024** (NASA JSC SIMA, NTRS 20240007647): plant decomposition excavation → transfer → dryer and cold trap → electrolysis mirrors the cost lines; chart-read power shares electrolysis ~37%, H2 liquefaction ~35%; liquefaction ~58% of volume.

Handling loses a large share of the water, so `Volatile cargo containment` (0.05 kg/kg) prices a measured need; the `Water liberation energy` row (2500 Wh/kg) gets its mechanism (heated extraction and cold trapping; no Wh/kg here). `extracted_data/volatile_recovery_isru_key_numbers.csv`.

## R4 - nextc_ppu_2020 [T2] (2026-09-18)

NEXT-C PPU for DART (NTRS 20205004248; un-hosted: NTRS says may include copyright): prototype 34.5 kg at 0.5–7 kW output (80–160 V input); 94.8% efficiency (7 kW, 120 V, March 2019), 93.8% hot; flight PPU 3.7 kW / 93.9% (Jan 2020); beam supply up to 90% of output. Confirms `Power processing unit specific mass` 4.7 kg/kW (34.5 / 7.4 kW input); the PPU's ~0.94 bounds the 0.60 total EP efficiency (anode × utilisation ≈ 0.64). `extracted_data/nextc_ppu_performance_key_numbers.csv`.

## R6 - ambrosi_2019 [T1, hosted, CC BY] (2026-09-18)

European RTGs and RHUs (Space Sci Rev 215:55): GPHS/MMRTG heritage; Pu-238 production restart toward ~1.5 kg/yr by 2025 (the ceiling hard-coded in calc.py); small or stacked RTGs 1.3-2.1 W/kg; skutterudite and zintl thermoelectrics as the efficiency path. R72: the americium unit as built gives 9.1-9.3 We from 200 Wth in a 9.4 kg 10 We system, ~1 W/kg. `extracted_data/european_rtg_review_2019_key_numbers.csv`.

## R7 - hoffman_2000 [T2, hosted] (2026-09-18)

Thin-film PV parametric assessment (NASA/TM-2000-210342): the Main Belt Asteroid Tour at 1.5 AU with SEP: 7.5 kW EOL, array 121 kg (4-junction GaAs), $14.1M (2000$). ~62 W/kg at 1.5 AU = ~140 W/kg array-only at 1 AU, about twice the 60 W/kg system row, matching its "batteries, regulation and structure roughly halve that". ~$1880/W at array level vs cells at $400/W (4-j GaAs), $220/W (thin Si), ~$60/W (CIS). Below ~12% film efficiency a lighter substrate does not win on mass. `extracted_data/hoffman_2000_pv_array_key_numbers.csv`.

## R9 - ali_2023 [T1, hosted, CC BY] (2026-09-18)

Li-ion calendar ageing for long missions (Front. Energy Res. 11:1108269): space cells ~265 Wh/kg, 670 Wh/L, ~1000 W/kg; flown on Perseverance, OSIRIS-REx, Parker, THEMIS; controlled envelope -40..+40 °C (an asteroid surface needs active heating); fade grows with temperature and state of charge. Anchors the "cells reach 250–300 Wh/kg" input of the 104 Wh/kg usable row. `extracted_data/ali_2023_space_batteries_key_numbers.csv`.

## R10 - The excavation row's "Zacny et al." resolved (2026-09-18)

- **metzger_zacny_2020** [T1] (J. Aerosp. Eng. 33(6):04020075; arXiv preprint, no licence, read only): regolith conductivity (Eq 21, basalt A0=6.12e-3 W/m-K); volatile release below ~300 °C for epsomite-class material (UCF-CI-1, Orgueil TGA); drilling heat takes hours to days to dissipate, a timeline cost not modelled. Stays in this domain (thermal extraction). `extracted_data/metzger_zacny_2020_key_findings.csv`.
- **just_2019** [T1] (PSS, CC BY; moved to d19): parametric review of 13 excavation techniques.

## R43 - Excavation force model and test facility (moved to d19 in R77) (2026-09-23)

NTRS reachable again through `ntrs.nasa.gov/api/citations/<id>`.

- **zeng_2007** (hosted): drawbar-force model; JSC-1a ρ = 1680 kg/m3, c = 170 N/m2, ca = 1930 N/m2, φ = 35° (β 10°, δ 20°, K0 0.573), SG 2.85; force "lowest values for cohesionless soil but the highest values for very cohesive soil", the mechanism behind the loose/consolidated split.
- **proctor_apex_2019**: Glenn's APEX digger (325 VDC / 100 A; bucket 21.6 cm, 15,600 cm3; load cell Fx,Fy ≤1300 N, Fz ≤3900 N, torque ±203 N-m; 1,587 kg GRC-3B bin): tare-subtracted excavation power.
- **zeitlin_asteroid_excavation_project** (KSC, TRL 3→5): C-type icy regolith under vacuum and cryogenic conditions.

just_2019's indexed table (RASSOR bucket drum 0.761 Wh/kg excluding transport; pneumatic ~2 Wh/kg; impeller ~115–130 W at 6–30 kg/h; bucket ladder <200 W at up to 2400 kg/h) puts loose-regolith cutting far below the 200 Wh/kg median (later rc-027). `19_asteroid_excavation_beneficiation/extracted_data/r43_excavation_energy_key_numbers.csv`.

## R44 - ZBO cryocoolers: tested hardware (all hosted) (2026-09-23)

**nugent_2022_rtb_cryocooler_test** (NTRS 20220009350), Table 1:

| Parameter @20K | State of art | Threshold | Project goal | Tested¹ | Projected² |
|---|---|---|---|---|---|
| Lift capacity (W) | 1 | 17 | 20 | 19.2 (max 22.46) | 20.4 |
| Specific mass (kg/W, flight-like) | 18.7 | 5.5 | 4.4 | 5.5 | 5.2 |
| Specific power (W/W) | 370 | 80 | 60 | 91.6 | 86.3 |

¹ at 285 K rejection; ² at 270 K. Test-point sweep 78.7-281.2 W/W (Carnot efficiency 7.1-8.2%).

- **hastings_2010_lht_zbo_demonstration** (NASA/TP-2010-216453) p16: "The cryocooler rated capacity is 30 W at 20 K and requires 350 W of power input per watt of cooling for a 4% Carnot cycle efficiency. The first stage provides 50 W of cooling at 80 K."
- **plachta_2017_cryo_zbo_goals**: "the largest has less than 1W of cooling at 20K and just 20W at 90K"; an 8.4 m LH2 tank leaks "hundreds of watts" without a 90 K shield.

The 80 W/W median equals NASA's threshold and the tested 91.6 sits in the 50-150 band; the worked example (20 W leak → ~100 kg, ~1.6 kW) matches 5.5 kg/W × 91.6 W/W (≈108 kg, ≈1.83 kW). The 60 W/W goal is unmet.

## R47 - damodaran_cost_of_capital_by_industry (moved to d17) (2026-09-23)

January 2026 table (96 industries; CoC = wE×CoE + wD×AT-CoD within ±0.05 pp on every row):

| sector | n | beta | CoE | E/(D+E) | AT-CoD | D/(D+E) | CoC |
|---|---|---|---|---|---|---|---|
| Aerospace/Defense | 79 | 0.95 | 8.17% | 86.53% | 3.97% | 13.47% | 7.60% |
| Metals & Mining | 73 | 1.04 | 8.60% | 90.10% | 2.52% | 9.90% | 8.20% |
| Precious Metals | 56 | 0.84 | 7.68% | 93.21% | 5.97% | 6.79% | 7.47% |
| Total Market | 5994 | 0.91 | 8.02% | 73.98% | 3.97% | 26.02% | 6.96% |

The 10% WACC sits 240 bps above aerospace; range_low 7.5% matches the floor; 15% bounds venture cases. `17_cost_of_capital_contingency_insurance/extracted_data/r47_damodaran_cost_of_capital_key_numbers.csv`.

## R50 - DSN rate and launch insurance (both moved in R77) (2026-09-23)

**jpl_dsn_services_catalog_820_100** (Rev H, 2022-06-06; un-hosted, Caltech copyright): AF = RB × AW × MW (p65; AW 1.0 one 34 m, 2.0 two-station, 3.0 three-array or any combination with a 70 m, 4.0 four; MW 1.0 or 0.5 downlink-only); "the DSN contact dependent hourly rate (RB) was $1,792" (p66); passes over 8 h segmented. CPI-U H1-2022 288.347 -> Aug-2026 334.980 (x1.1617): 34 m ≈ $2,082/hr, so $1,530 is 26.5% low (rc-030); 70 m (AW 3.0) ≈ $6,245 vs the note's ~$4k. The note's own method (FY09 $1,057 x 1.4570 = $1,540) is consistent but rests on the superseded MOCS rate. BLS and World Bank chains agree within 0.02% over 2016-2024.

**gallagher_plane_talking_space_market_updates** (Q1-2024, the cited issue): 2023 loss ~USD900mn on ~USD550mn premium; "insurers are suggesting that premium rating needs to increase significantly." No issue gives a launch-premium percentage, so 10% is directionally supported, not pinned. The note's "post-Intelsat 33e loss" is wrong: Q4-2023 attributes the reset to Viasat-3 and Inmarsat 6-F2 (">85% of the 2023 loses ... post-separation spacecraft issues"), and IS-33e broke up in GEO on Oct 19, 2024 (rc-031).

`extracted_data/r50_dsn_rates_and_launch_insurance_key_numbers.csv`.

## R56 - stackpoole_2013_pica_pica_x_postflight_eval (TPS heritage; moved to d21) (2026-09-24)

The TPS row's cited NTRS 20140005558 (IPPW 2013 summary slide): "Both materials performed well with no unusual ablation performance"; PICA chosen for MSL and OSIRIS-REx; SpaceX's PICA-X flew Dragon COTS Demo 1 (2010); "PICA‐X virgin and char have higher density than Stardust era PICA"; Stardust PICA peak 1000 W/cm2 / 28 kJ/cm2 vs ~50 W/cm2 for Dragon-1 (R70). The $50k/kg stays an estimate.

## R57 - Plane Talking through Q2-2026 (2026-09-24)

Seven issues read: Q4-2024 "circa. USD2bn of claims being notified within 18 months."; Q1-2025 capacity USD 550m (2024) / 502m (2025); Q2-2025 "finally shown signs of having turned the corner ... pressure on premium rates", premium fell "by over 50%" 2012-2018; Q1-2026 capacity +~USD100m, SpainSat NG-2 (over USD400m) moves the 2025 loss ratio "from circa 15% to circa 75%", "launch pricing continues to improve"; Q2-2026 +USD 70 million capacity, BlueBird 7 (Blue Origin failure, April 2026) ~USD30m, rate reductions possible in H2-2026. The 10% may sit high for 2026; still no explicit launch rate. R50's claim of Q2-2026 coverage was premature and corrected. `17_cost_of_capital_contingency_insurance/extracted_data/r57_plane_talking_series_key_numbers.csv`.

Also: no source gives a Centaur III or EUS unit price (IG-24-001's $482M EUS is a launch scope; SP-4176 has programme costs: R&D FY59-FY61 $4m -> $36.6m -> $62.6m), so the upper-stage high end stays unanchored.

## R63 - FY2027 budget: the ISS envelope (2026-09-25)

From the hosted FY2027 Budget Estimates (d07), p60 Space Operations ($M):

| line | FY2027 req | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Commercial LEO Development | 299.7 | 299.8 | 599.8 | 599.8 | 1,577.2 |
| International Space Station | 921.2 | 921.2 | 921.3 | 921.3 | 921.3 |
| Space Transportation | 1,152.5 | 1,152.4 | 1,152.3 | 1,152.3 | 174.7 |
| Space and Flight Support (SFS) | 673.8 | 673.8 | 673.8 | 673.8 | 674.0 |

Plus $250.0M/yr FY2027-31 of mandatory WFTC funding (PL 119-21) for ISS operations and cargo. The $2M per-delivery berthing estimate is 0.217% of the ISS line; "depot" occurs 0 times; $1.0 billion for future commercial station services (p63). Envelope only.

`extracted_data/r63_fy2027_space_operations_iss_lines.csv`.

## Maintenance (2026-09-26)

Un-hosted: lac_bac_2024, ssap_2021 (arXiv), nextc_ppu_2020 (NTRS copyright flag), jpl_dsn_services_catalog_820_100 (Caltech). lac_bac labels corrected (above). ssap Table 3: all 9 bodies now extracted. zero_bo_off_2025 re-tiered T2; lac_bac and ssap stay T1. stackpoole context-only then.

## R70 / R71 / R72 - Extraction (2026-09-27)

- R70: `r70_ali_2023.csv`, `r70_ali_2023_table3_calendar_aging_fit.csv`, `r70_ambrosi_2019.csv`, `r70_carlson_2024.csv`, `r70_hastings_2010_lht_zbo_demonstration.csv`, `r70_hoffman_2000.csv`, `r70_kleinhenz_2016.csv`, `r70_kleinhenz_2016_deltion_capture_results.csv`, `r70_kleinhenz_2018.csv`, `r70_plachta_2017_cryo_zbo_goals.csv`, `r70_stackpoole_2013_pica_pica_x_postflight_eval.csv`, `r70_zeng_2007.csv`, `r70_zero_bo_off_2025.csv`.
- R71: `r71_lac_bac_2024_key_numbers.csv`, `r71_metzger_zacny_2020_key_numbers.csv`, `r71_metzger_zacny_2020_table1_lcross_volatiles.csv`, `r71_nextc_ppu_2020_key_numbers.csv`, `r71_nextc_ppu_2020_table1_ppu_supplies.csv`, `r71_nextc_ppu_2020_table2_flight_ppu_survey.csv`, `r71_ssap_2021_key_numbers.csv`, `r71_ssap_2021_reactions_energetics.csv` (the DSN, Proctor and Zeitlin files moved with their sources).
- R72: `r72_ambrosi_2019_tables1_10_rtg_rhu.csv` (108), `r72_hastings_2010_tables1_10_pump_and_heat_leak.csv` (23), `r72_nugent_2022_rtb_cryocooler_test_results.csv` (109).
  - nugent Tables 2-3: Eq. 2 reproduces specific power except DP4 (122.2 printed, 105.0 computed); DP3/DP4 specific masses 6.4 and 5.3 look swapped (kept). DP1 lifts 19.56 W at 22.5 K for 1.68 kW and 106.3 kg (85.9 W/W), matching the note; 3 W part-load points reach 247-281 W/W; 0.3 kg/h of H2 liquefaction needs 150-300 W at 20 K (p8).
  - hastings Table 10: 0.0971 kg/h boil-off = 13.10 W (12.23 from mdot x hfg x rho_l/(rho_l - rho_v) plus 0.87 superheat), 0.377 W/m2, 2.385 W through penetrations; not reproduced: the "4 legs" 1.449 W (4 x mean = 1.249) and 0.377 W/m2 (implies 34.74 vs 35.74 m2).
  - metzger_zacny's lunar c_p averages 763 J/kg K over 200-400 K (4.7% below the row's flat 800) but diverges above ~400 K (6,724 at 700 K).

## R74 - Upstream citations registered (+7; most moved in R77)

`faa_14_cfr_part_450_launch_reentry_licensing`, `crs_r48582_commercial_launch_reentry_regulations` (d18); `mil_hdbk_189c_reliability_growth_management`, `duane_1964_learning_curve_reliability_monitoring` (d16); `valueinvesting_io_2026_boeing_howmet_wacc` (d17).

## R76 - Gap: Starship tanker flights

| cell | current value | upstream's stated basis |
|---|---|---|
| `storage_systems.csv` `Depot refuelling flights to escape` (Starship `tanker_flights_for_escape`) | 12 [8, 16] | "SpaceX's own range for filling a Starship in LEO before a high-energy departure"; no source |

Needed: propellant a departing Starship needs in LEO and what each tanker delivers.

## R77 - Sources moved to domains 16-21

| id | moved to | files now at |
|---|---|---|
| `mil_hdbk_189c_reliability_growth_management`, `duane_1964_learning_curve_reliability_monitoring` | 16 | none |
| `damodaran_cost_of_capital_by_industry` | 17 | `17_cost_of_capital_contingency_insurance/extracted_data/r47_damodaran_cost_of_capital_key_numbers.csv`, `17_cost_of_capital_contingency_insurance/extracted_data/r47_damodaran_cost_of_capital_full_table_96_industries.csv` |
| `valueinvesting_io_2026_boeing_howmet_wacc` | 17 | none |
| `gallagher_plane_talking_space_market_updates` | 17 | `17_cost_of_capital_contingency_insurance/extracted_data/r57_plane_talking_series_key_numbers.csv` |
| `faa_14_cfr_part_450_launch_reentry_licensing`, `crs_r48582_commercial_launch_reentry_regulations` | 18 | none |
| `just_2019` | 19 | `19_asteroid_excavation_beneficiation/extracted_data/r43_excavation_energy_key_numbers.csv` |
| `zeng_2007` | 19 | `19_asteroid_excavation_beneficiation/extracted_data/r70_zeng_2007.csv`, `19_asteroid_excavation_beneficiation/full_texts/zeng_2007_excavation_force.pdf` |
| `proctor_apex_2019` | 19 | `19_asteroid_excavation_beneficiation/extracted_data/r71_proctor_apex_2019_key_numbers.csv` |
| `zeitlin_asteroid_excavation_project` | 19 | `19_asteroid_excavation_beneficiation/extracted_data/r71_zeitlin_asteroid_excavation_project_key_numbers.csv` |
| `ssap_2021` | 19 | `19_asteroid_excavation_beneficiation/extracted_data/ssap_2021_table3_theoretical_yields.csv`, `19_asteroid_excavation_beneficiation/extracted_data/r71_ssap_2021_key_numbers.csv`, `19_asteroid_excavation_beneficiation/extracted_data/r71_ssap_2021_reactions_energetics.csv` |
| `jpl_dsn_services_catalog_820_100` | 20 | `20_mission_operations_communications/extracted_data/r71_jpl_dsn_820_100_key_numbers.csv`, `20_mission_operations_communications/extracted_data/r71_jpl_dsn_820_100_table5_1_station_rf_capabilities.csv` |
| `stackpoole_2013_pica_pica_x_postflight_eval` | 21 | `21_mass_cost_estimating_relationships/extracted_data/r70_stackpoole_2013_pica_pica_x_postflight_eval.csv`, `21_mass_cost_estimating_relationships/full_texts/pica_pica_x_stardust_dragon_postflight_eval_ntrs_20140005558_publicdomain.pdf` |

Shared CSVs staying here: `extracted_data/r50_dsn_rates_and_launch_insurance_key_numbers.csv`, `extracted_data/storage_isru_key_numbers.csv`, `extracted_data/unhosted_sources_key_numbers.csv`. rc-026, rc-027, rc-030 and rc-031 keep `domain_dir` 05.

## R97 - Pu-238 unit price

**howe_et_al_niac_economical_production_pu238_phase_i_final_report** (NIAC Phase I, USRA CSNR / Univ. of Utah, NNX11AR30G; NTRS 20160010587, hosted), p32:

| scenario | price/kg | production rate |
|---|---|---|
| 5 MW reactor, 20% ROI | $7.8 M | 2.25 kg/yr |
| 5 MW reactor, 0% ROI | $3.5 M | 2.25 kg/yr |
| 10 MW reactor, 20% ROI | $4.3 M | 6.25 kg/yr |
| 10 MW reactor, 0% ROI | $1.6 M | 6.25 kg/yr |

p37: capital $35.7M ($35.2M reactor + CAT.-1 fence), process cost $3.2M +/- 50% per kg, "the sale price of $6,000,000", ROI 4%/yr, 5.3-year payback; $0.56M/kg using an existing facility's flux. Kept as printed: "$3.2 million (±50%) which is substantially above the sale price of $6,000,000". Upstream's ~$2.5M/kg Russian figure sits inside; no candidate (rc-043 covers the production-rate wording). `extracted_data/r97_pu238_unit_price_key_numbers.csv`.

## R154 - RTG programme cost and status

- **hamley_2016_rps_program_overview_focus_users** (hosted): Pu-238 supply "originally intended to reach the full production rate of 1.5 kg/yr in 2021", now phasing in "possibly as early as 2019"; MMRTG F2/F3 in storage; "The RPS Program has averaged approximately $75M/year".
- **zakrajsek_et_al_2017_rps_status_expectations_aiaa** (hosted): "the short-term goal being to average 400 g/year by 2019, and a long-term goal to obtain an average rate of 1,500 g/year by 2025".
- **gao_2017_pu238_rps_production_planning** (GAO-17-673; registered from GAO's text): one MMRTG "would cost $77 million, two MMRTGs would cost $94 million, and three MMRTGs would cost $117 million" against an "$850 million development cost cap"; "about 120 watts ... 6 percent power conversion efficiency"; "32 general purpose heat source (GPHS) fuel clads".

$77M per ~110 We ≈ $700k/W, inside the $200k-$1M band. `extracted_data/r154_rtg_program_cost_key_numbers.csv`.

## R163 - The ZBO note's Carnot band (rc-089; 2026-10-14)

The note's "real machines run 15-25% of Carnot" is unsourced: Nugent's measured fractions are 5.0-15.6% (14.5% at the 91.6 W/W point), the MHTB GM cooler 4%; and 14 W/W at 15-25% of Carnot is 56-93 W/W, not 50-150. rc-089 (wording); value and range stand.

## R164 - Candidates (2026-10-14)

rc-101 (cite Hoffman and Schmitz for power-system mass), rc-103 (cite the NEXT-C PPU paper; 4.7 kg/kW is per kW input), rc-108 (cite the RTB test: 5.5 kg/W). Texts in `revision_candidates_closed.csv`.

## R184 - Kleinhenz & Paz ISRU plants (rc-167; 2026-10-17)

Both hosted:

- **kleinhenz_paz_2017_isru_propellant_production_aiaa** (AIAA 2017-0423): "Production rate based on a mission timeline of 480 days (16 months)"; "Requirement: CH4 6978 kg 0.61 kg/hr" with "(22728 kg propellant, 5184 kg leftover)": 29,706 kg ≈ the note's 29.7 t; "A system to produce all 30 mT of Mars ascent propellant is estimated to weigh 1.7 mT using the lowest yield regolith." → 13.2 kg/yr per kg ≈ range_high 13.3.
- **kleinhenz_paz_2021_lunar_water_isru_ptmss_srr** (2021-06-10): H2/O2 at mixture ratio 6; "The baseline system to produce 10 mT of O2 and 1.67 mT of H2 in 225 days was 4.9 mT and 68 kW"; ridge system 2.6 tons, 46 kW ridge + 22 kW mine → 7.28, the row's value and range_low exactly. The 46 kW is also rc-166's cross-check.

Crossref titles the 2017 paper "An ISRU propellant production system for a fully fueled Mars Ascent Vehicle", as spacecost cites; NTRS's copy says "to Fully Fuel". **rc-167:** add DOI 10.2514/6.2017-0423 and note the variant title. No unregistered upstream reference remains for spacecost v0.12.0.

`extracted_data/r184_kp_isru_plant_key_numbers.csv`.

## R198 - Johnson AIAA ASCEND 2023 H2-liquefaction deck registered; every upstream attribution verified verbatim; no RC (2026-10-19)

The hydrolox ISRU energy band in spacecost v0.12.0 (`isru_processing_wh_per_kg` = 15,200 Wh/kg low end of a 15.2-26.3 kWh/kg band; economicspace MODEL.md and versions.md carry the same construction) rests on three named components: DOE HFTO PEM electrolysis (verified live at R183), Kleinhenz & Paz whole-plant cross-check (registered + verified R184), and **W. Johnson, AIAA ASCEND 2023 - which was cited by name in all three places but absent from the GR registry**: it carries no DOI and only a bare NTRS accession number, so the URL/DOI-token completeness sweep of R186 could not see it. Pulled live (NTRS 20230014839; 785,453 B; sha256 27161cbe... prefix), scanned all 16 pages for copyright marks - zero hits under GOV_PUBLIC_USE_PERMITTED determination → hosted as `johnson_2023_h2_liquefaction_ascend` [T2, ntrs-public-use] with key-numbers file r198_h2_liquefaction_key_numbers.csv.

Every figure upstream charges to this deck reproduces verbatim (all count==1 against the PDF text layer): "Single 20 K cryocooler requires 35 kW input power and 85 m2 radiator"; baseline rate "Liquefaction rate of 0.3 kg/hr of hydrogen (~10 ton/yr total prop, ~1.6 ton/yr LH2) with production margin"; combined pre-cooling "Even with 15% Carnot intermediate cryocooler, cut input power by 70%" (= upstream's divide-by-three); "System oxygen liquefaction system would require < 2 kW"; and the rejected-alternative anchor "Double-sided vertical radiator – 3.9 kg/kW heat rejection" - whose very next deck line is "Ignore cryocooler mass", exactly matching spacecost's caveat that the floor leaves out electrolyser and cryocoolers. The arithmetic chain also reproduces: 35 kW / 0.3 kg/hr = 116.7 kWh/kg H2 baseline (upstream prints '39 to 117'), third-of-baseline precooled case, x(1/7) per-kg-propellant shares giving 5.56-16.7 exactly; the O2 rate of ~0.96 kg/hr that bounds the <=1.79 kWh term is derived from the deck's own p4 parenthetical (MR-consistent with ~10 t/yr total and ~1.6 t/yr LH2) - not an unsourced import, so no candidate on it either. One printed inconsistency noted inside the source itself: the radiator-only slide says input power reduced "from 34 kW" while the comparison bullet says 35 kW baseline; upstream quotes 35 (present verbatim), and both numbers are in the deck - recorded here so a future round does not flag it against us.

No RC opened this round: the band's low end remains contested by rc-166 (open, kornuta_2019 plant-level figures vs the DOE-system construction) - a different question from attribution fidelity, and that candidate row is untouched per convention. Completeness-scan lesson recorded: registry sweeps against upstream must grep bare NTRS accession tokens (NTRS \d{8,}) in addition to URL/DOI patterns, or citation-by-accession references like this one stay invisible.

## R205 - DOE HFTO PEM electrolysis technical targets registered (2026-10-19)

spacecost CITATIONS.md section 2 credits the DOE Hydrogen and Fuel Cell Technologies Office technical-targets table for hydrolox ISRU electrolysis at system level 55 kWh/kg H2 (2022 status); no registry row carried that source. Registered this round as doe_hfto_pem_electrolysis_technical_targets [T3; verified_live_not_pulled]: read live from energy.gov on 2026-10-19 (https://www.energy.gov/cmei/fuels/technical-targets-proton-exchange-membrane-electrolysis), where the System block prints Energy Efficiency kWh/kg H2 (% LHV) = 55 (61%) / 51 (65%) / 46 (72%). The string '55 (61%)' is count==1; '51 (65%)' appears twice on the page (Stack-block 2022 Status cell and System-block 2026 Targets cell) - disambiguated by table position per the [appears twice] convention. Extracted to r205_doe_hfto_pem_targets_key_numbers.csv (4 rows). The stack-vs-system distinction is recorded for the rc-166 evidence trail: kornuta_2019's ~4.41 kWh/kg electrolysis-alone figure is a plant-level measurement, not comparable to DOE target cells; rc-166 stays open and untouched.

## R311 - Settled ISRU feed can exceed the asteroid resource budget (2026-11-01)

`economicspace_isru_feed_resource_budget_record_2026`: economicspace `modules/calc.py`
at 54e30b0ae82be71c987f08feb95630502b7f54f0 says ISRU feed "comes off both budgets
before any ore is loaded" (L6566-6567). The sizing loop estimates return propellant
without `k_ret` (L6361-6365); the settled return book includes that tank-closure factor
(L6648-6653). Settled fuel feed is then checked against rig throughput (L6678-6682),
with no corresponding check against `mineable_kg`.

A complete call through the original `_evaluate_combo_at_ratio`, its original physical
and cost helpers, and the 46 original spacecost operational rows returns this synthetic
mission: body budget 1,000 kg, raw cargo 100 kg, return dry floor 10 kg, structure fraction
0.1, return mass ratio 2, tank fraction 0.1, water fraction 0.2, recovery 0.9, and
water/propellant ratio 9/7. The LEO capacity is deliberately nonbinding (1e8 kg); the
caller caps cargo at 100 kg. This is a function-level conservation witness, not an
observed catalog body or quoted launch architecture.

The loop computes 120 kg of propellant and 857.142857 kg of fuel feed. The settled book
instead has `k_ret=1/(1-0.1*(2-1))=1.1111111111`, 133.333333 kg of propellant and
952.380952 kg of fuel feed. With 100 kg cargo feed, this consumes **1,052.380952 kg**
from a 1,000 kg body, yet returns a complete mission result at L7303.

| case | body budget (kg) | cargo feed (kg) | fuel feed (kg) | total feed (kg) | original result |
|---|---|---|---|---|---|
| baseline | 1,000 | 100 | 952.380952 | 1,052.380952 | returned |
| zero tank control | 1,000 | 100 | 857.142857 | 957.142857 | returned, within budget |
| larger body control | 1,200 | 100 | 952.380952 | 1,052.380952 | returned, within budget |
| throughput limited to 1,000 kg | 1,000 | 100 | 952.380952 | 1,052.380952 | rejected at L6682 |
| processing, liberation and containment on | 1,000 | 100 | 960.317460 | 1,060.317460 | returned |
| smaller 94 kg cargo | 1,000 | 94 | 900 | 994 | returned, within budget |

The baseline disables those three processing/containment features and the refinery to
isolate the resource book; the enabled case restores processing, liberation and containment.
The extracted CSV records fixture dictionaries, config overrides, call arguments and
results. Independently solving `P+q*k_ret*(1.1*P+10)<=1000` gives a maximum payload below
100 kg; the 94 kg control fits. Adding only a settled material-budget comparison to an
in-memory copy rejects the baseline, with no upstream source-file change.

Verdict: the returned resource book violates its own finite-material bound. `rc-241`:
use consistent tank-inclusive fuel estimates and enforce both resource budgets after
settlement, refitting payload/feed when necessary. Current-catalog incidence and ranking
impact were not measured. `extracted_data/r311_isru_feed_vs_asteroid_resource_budget.csv`.

## R317 - Disabled water liberation still charges ISRU heating (2026-11-01)

Source `economicspace_isru_water_liberation_flag_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0 `modules/calc.py`, with
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f original reference rows and
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011 cargo helpers.
`model_water_liberation` defaults to True (L417-421). The sizing branch gates
both water sources, described as "the water turned into ISRU propellant, and
the water sold as CARGO" (L6427-6429). Final settlement instead initializes
`water_kg = isru_water_kg` before testing the flag; only cargo water is gated,
and the water-heating draw is added outside the flag (L6707-6717).

Eleven complete original-evaluator cases use actual Falcon 9 reusable,
hydrolox and all 46 ops rows. Synthetic inputs: 1e9 kg body, density 2 g/cm3,
water fraction 0.2, 1.2 AU, cargo value 100 USD/kg and a nonbinding commodity
ceiling. Main case: 100 kg raw cargo cap, caller 1,000 m/s per leg, ISRU on,
single-mission market, no aerocapture; windows, refinery, containment,
boil-off and the separate ISRU chemical-processing model are disabled.
No EP hardware is involved.

| original case | final power (W) | cargo water heated (kg) | ISRU water heated (kg) |
|---|---|---|---|
| ISRU, liberation flag False | 347.185555 | 0 | 205.160440 |
| ISRU, flag True | 370.000978 | 20 | 205.160440 |
| ISRU, flag False, water-energy row set to zero | 113.144442 | 0 | 0 |
| non-ISRU, flag False | 0 | 0 | 0 |
| non-ISRU, flag True | 22.815423 | 20 | 0 |

The False ISRU case includes 234.041113 W of water heating, exactly
`2500 * 205.16043958720536 / (0.25 * 365.25 * 24)`. Against the zero-rate
control it adds 16.178842 kg of solar power hardware and 333,705.210064 USD
of total cost. The zero-rate control still makes and reports the physical
ISRU water; the table's zero denotes its uncharged heating load. An iron-only
concentrated hold contains no cargo water, and both flag settings then return
the same 370.000978 W, despite different sizing-loop draws.

For a 10,000 kg raw cargo cap, caller outbound/return delta-v 1,000/4,000 m/s
and the original 5,000 W RTG limit, False gives 1,666.666667 W in the sizing
loop but 5,177.047517 W at settlement. It is rejected at L6737. The excess is
3,510.380850 W of ISRU-water heating. Setting only the water-energy row to
zero returns the same cargo and fuel book at 1,666.666667 W and 8,129.807868 kg
launch mass. The solar candidate survives with the unwanted heating term.
Both body and throughput budgets fit; this is a flag-consistency witness,
not a claim that a real mission can omit the physical heat requirement.

Five separate in-memory diagnostics gate just L6707 by the same flag. Disabled
raw, concentrated and RTG cases reproduce the zero-rate controls' power,
mass and costs. Enabled and non-ISRU controls preserve the complete serialized
outputs and every finite output float bit-for-bit.

Verdict: the loop and settled mission implement different meanings of the
same flag. `rc-247`: apply one policy consistently to both water sources,
including feasibility and reporting, or explicitly narrow the flag and make
ISRU heating mandatory in both stages. The default True path is not shown
to fail; current-catalog incidence and ranking effects were not measured.
`extracted_data/r317_isru_water_liberation_flag.csv`.

## R323 - Cryogenic fuel retains the pre-volume mining duration (2026-11-02)

Source `economicspace_settled_boiloff_hold_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`
and `MODEL.md`; original spacecost@860bef9902aa67fec705875cd52fdb8e6def159f
reference rows and spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011
cargo functions. MODEL.md L932-933 says return propellant sits in the tank
"from launch until the departure burn". The model's factor is
`exp(boiloff_pct_per_day / 100 * hold_yr * 365.25)`, with hold equal to
outbound time plus the estimated asteroid stay (calc.py L6293-6298).

The sizing loop precedes the cargo volume cap at L6542-6580. That cap can
reduce final feed and mining duration (L6597-6604, L6700), but settlement
retains the loop's return ratio and tank factor (L6611-6612, L6648-6653).
It rebuilds power, hardware and launch masses without recalculating the
cryogenic storage factor or effective return delta-v. Thus final fuel can
still be sized for a dig the returned mission no longer performs.

Fourteen baseline full-evaluator cases and ten early-volume diagnostics use
unchanged numerical functions and actual Falcon 9 reusable, propellant and
all 46 operational-cost rows. The principal synthetic body is 1e9 kg,
density 0.2 g/cm3, 10% iron and 90% silicates, priced at 100 and 1 USD/kg.
Recovery is 0.9, concentration ratio 10, and delta-v is 1,000 m/s per leg.
N=1 and an unbounded market remove programme/resource and capped-mix issues.
Propulsion is chemical without ISRU or aerocapture. The isolation cases turn
off refinery, launch windows, cargo-water liberation and containment; the
cryogenic model remains enabled at its default. The actual 157 m3 fairing,
25% usable-volume rule and body density bound cargo to 7,850 kg. Its
78,500 kg feed takes 1.074606 years to mine; including the 0.5-year outbound
leg gives a final storage duration of 1.574606 years.

| original propellant | booked storage yr | booked factor | final-clock factor | extra launch kg in paired comparison |
|---|---|---|---|---|
| hydrolox | 2.632628 | 1.617341 | 1.333174 | 1,040.039 |
| methalox | 2.953816 | 1.138220 | 1.071452 | 274.157 |
| kerolox | 2.647310 | 1.156085 | 1.090099 | 314.274 |

The diagnostics give the existing evaluator its already-required volume
ceiling through `payload_cap_kg`, so the loop can see it before sizing fuel.
All three pairs retain exactly the same cargo, feed, mining/mission clocks,
processing power, power-system mass, composition and revenue. Hydrolox then
loads 3,323.585 kg return fuel instead of 4,061.384 kg, with launch mass
9,594.597 kg instead of 10,634.636 kg. Total cost falls by 5.974M USD while
gross value stays 707,285 USD. Methalox and kerolox cost differences are
1.465M and 1.664M USD. These are comparisons at the same returned cargo,
not a new global vehicle or concentration optimisation.

The effect also occurs on raw ore: a 100 m/s-per-leg case drops to the
0.25-year mining floor after volume clipping but retains a 1.549683-year
fuel-storage exposure instead of 0.75 years. A denser 0.5 g/cm3 concentrated
case shows a 0.361M USD difference. With launch windows enabled, the principal
hydrolox result retains 4.225339 storage years instead of its final 3.664259;
the same-cargo early-limit comparison reduces launch mass by 794.597 kg.
Enabling both cargo-water models preserves the complete principal output
because this composition contains no water.

Boil-off-disabled and zero-rate MMH/NTO controls retain every physical and
cost output; only `volume_fits` changes, as it describes demand before the
cap. An already tighter 1,000 kg cap preserves the complete output, including
that flag. Nonbinding dense cases retain small ordinary finite-loop residuals
from the existing 1% state-convergence test; this candidate concerns the
larger subsequent volume change, not a claim of exact loop convergence.
All 24 cases converge before the 12-pass limit and fit separate body,
throughput and launch limits. Independent clock inversion and tank-closed
fuel calculations reproduce the reported books and seven affected pairs.

Verdict: the reported final mission clock and the cryogenic sizing exposure
describe different digs. `rc-253`: settle cryogenic fuel against final cargo
and mining duration. The adopted evaporation rates are unchanged; these are
synthetic-body witnesses with no measured population incidence or ranking
effect. `extracted_data/r323_settled_boiloff_hold.csv`.

## R348 - Capture propellant remains stored during the return coast (2026-11-03)

`economicspace_return_capture_boiloff_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0. The return budget adds the asteroid
departure burn and later LEO capture (calc.py L2834-2861), but non-ISRU
storage exposure ends at outbound flight plus stay (L6293-6298). ISRU is
exempt because it is made on departure (L6203-6206). Capture fuel still has
to remain available after the return cruise; the ISRU plant and processing
power stay at the asteroid (L6650-6673). MODEL.md's acknowledged uncharged
production-window loss (L943-949) is a separate issue.

Twenty controlled chemical/single-mission fixtures run original, repeat,
an additional return-storage mass ratio and its repeat: 80 complete original
kernel evaluations. Source vehicle, propellant and operations rates remain
unchanged except declared rate/capacity sensitivities. Physical burns and
the original travel-time proxy stay fixed. The diagnostic passes a storage-
equivalent ratio through the existing numerical kernel and preserves the
physical clock with a scoped duration wrapper; it is not a new trajectory.

At synthetic a=1.2 AU, e=i=0, 100 kg cargo and one-year stay, asteroid
departure is 1265.303230 m/s and LEO capture is 3303.723236 m/s. The model's
1.050876087-year return cruise and adopted 0.05%/day loss give B=1.211569038.
The native ISRU book provides 1347.056809 kg fuel and 747.019400 kg terminal
dry/cargo/tank mass. After departure, 827.041622 kg capture fuel remains;
after coast, only 682.620301 kg remains versus 827.041622 kg required.

Let Rd and Rc be the departure and capture rocket ratios. For terminal mass
M, departure requires `[Rd*(1+B*(Rc-1))-1]*M`, rather than `(Rd*Rc-1)*M`.
Even retaining the original tank mass gives a lower bound of 1579.839346 kg
departure fuel. Independent tank closure and the original kernel agree on
1640.122457 kg, with the return tank increasing from 131.019400 to
159.523978 kg. At the same cargo, launch rises from 10495.836457 to
10918.009602 kg, both below 17400 kg; cost rises from 1741004657.100574 to
1758684304.770426 USD. The physical 3.101752174-year clock is unchanged.
Cargo value is a controlled 100 USD/kg; all examples remain unprofitable.

Fourteen native books lack terminal-capture fuel under the adopted rate.
Thirteen changed same-cargo books close the independent forward inventory;
one 10550 kg capacity variant is refused by this kernel, without establishing
global infeasibility for other payloads/architectures. Six controls retain
exact original results: zero/disabled loss, zero return fuel, both-refused,
and direct-entry Earth-return cases with Earth-supplied or ISRU fuel.

`kleinhenz_paz_2021_lunar_water_isru_ptmss_srr` identifies liquefaction
cryocoolers with an included radiator estimate and capacity-sized storage
tanks (p15, subsystem rows checked by word coordinates and rendered page).
Its system-level thermal exclusion is qualified by subsystem allowances
(p3). This calculation grants perfect on-site production/storage and credits
that equipment; it does not assert a physical production-capacity ceiling or
charge another on-site cooler. Flown return-coast storage is the issue.

Verdict: `rc-284`, account for later-burn fuel through the return cruise or
explicitly size/credit a flown zero-boiloff system, then reclose tanks,
feed, power, launch mass and costs. Native and diagnostic repeats match in
types/values/float.hex and digests. Every returned book passes current
launch, body, throughput, time and volume checks. No observed-trajectory,
population/ranking or global-optimum claim is made. Twenty-seven blobs,
including all 21 imported local modules, match fresh pinned metadata and
four live main comparisons are identical.
`extracted_data/r348_return_capture_boiloff.csv`.

## R349 - NEXT-C PPU input-power inference and a conflicting output label (2026-11-03)

`nextc_ppu_2020` p4 Table 2 labels the NEXT-C 7.4 kW cell
"PPU Max Output Power (kW)" above 34.5 kg. The text's paired prototype
point is "7 kW output at 94.8% efficiency" (p2; p10 Sec.III.D, 120 V and
25 C). Table 3 p11 instead gives design output 7.0 kW and DART flight
output 3.7 kW; p11 gives identical 34.5 kg prototype/flight mass.
The two table columns and row labels were checked by word coordinates
and rendered pages. The complete 14-page copy matches the previously
removed file's 7393690 bytes and sha256
450c737c6c340735234c4d8c5c72edf12d0892954aad6f905e5f08931ea691e1.

At spacecost 860bef9902aa67fec705875cd52fdb8e6def159f,
operations.py L384-408 retains 4.7 kg/kW input and presents 7.4 kW as
input at full power. The R164 reasoning for `rc-103` did not acknowledge
the survey's conflicting output label. At the paired prototype point,
input inferred as 7/0.948 = 7.383966245 kW gives 4.672285714 kg/kW input,
supporting the adopted 4.7 to rounding (+0.593%). The numerical centre
is not contradicted; the unqualified source interpretation needs correction.

Verdict: `rc-103` re-opened for citation/derivation qualification. The source
does not resolve its 7.0/7.4 output discrepancy; an inferred nominal input
point must be distinguished from a printed rating and the DART test range.
Three local upstream blobs match fresh pinned metadata; four live main
comparisons are identical. `extracted_data/r349_nextc_ppu_power_basis.csv`.
