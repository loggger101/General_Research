# Domain 5 Findings — in-space storage / cryogenic boil-off, ISRU, operational costs

Backings: spacecost `storage_systems.csv`; the volatile-ISRU, power and electric-propulsion rows of `operational_costs.csv` (power and EP overlap domain 11; finance, licensing, operations, mining and hardware-rate rows moved to domains 16-21 in R77); environment penalties.

## Round 1 - Boil-off, transfer loss, ISRU yields

- **lac_bac_2024** [T1] (Cryogenics 148:104065; arXiv copy un-hosted 2026-09-26): finite-element LH₂ tank study. Boil-off: perlite 5905 W ≈ 0.04 %/day (the better stack), HePUR 35 350 W ≈ 0.24 %/day (round 1 had the labels swapped; corrected 2026-09-26). The hydrolox passive boil-off of 0.05 %/day sits beside the best case, with a ~6x spread by insulation that the MLI row (1.2 kg/m²) carries implicitly. Reliquefaction 5 kWh/kg (Kim et al.); local-area cooling shrinks the cooler when heat ingress is concentrated, the architecture the ZBO rows assume.
- **zero_bo_off_2025** [T2, hosted; arXiv preprint, no journal version]: LH₂ transfer between large ground tanks: VSD pump 0.00–0.24 wt%, fixed-speed 0.76–1.06 wt% per ~11,248 t transfer, against the in-space transfer-loss row's 3 % (1–8 %). Keep 3 % for current TRL and use this as range_low once space-rated pumps exist (rc-028).
- **ssap_2021** [T1] (Acta Astronautica 188:57-63; un-hosted; moved to d19): Table 3 products per 1000 kg of silicates at 100 % efficiency: CM/Murchison Fe 375 kg, O₂ 125, SiO₂ 260, H₂O 87; CI/Orgueil 65 / 3 / 430 / 118; H-chondrite 132 / 27 / 509 / none; peak ~950 °C. The CM-CI spread within one type argues for subtyping. Full table: `19_asteroid_excavation_beneficiation/extracted_data/ssap_2021_table3_theoretical_yields.csv`.

`extracted_data/storage_isru_key_numbers.csv`.

## Round 3 - Volatiles handling and plant decomposition

All NTRS, hosted:

- **kleinhenz_2016** (NTRS 20160010281): ~5 wt% water beds (per LCROSS); the single push-tube sample (65 g, long exposure) lost 88.9% of its water, the coring-auger samples (~115 g) 23-59% (R70 correction of "88% for coring"). `r70_kleinhenz_2016_deltion_capture_results.csv`.
- **kleinhenz_2018** (NTRS 20180005235): water escape across temperature and pressure; five-year average loss ~30% (5 wt% beds) and ~80% (0.8 wt% beds).
- **carlson_2024** (NASA JSC SIMA, NTRS 20240007647): plant decomposition excavation → transfer → dryer and cold trap → electrolysis mirrors the cost lines; chart-read power shares electrolysis ~37%, H2 liquefaction ~35%; liquefaction ~58% of volume.

Handling loses a large share of the water, so `Volatile cargo containment` (0.05 kg/kg) prices a measured need; the `Water liberation energy` row (2500 Wh/kg) gets its mechanism (heated extraction and cold trapping; no Wh/kg here). `extracted_data/volatile_recovery_isru_key_numbers.csv`.

## Round 4 - nextc_ppu_2020 [T2]

NEXT-C PPU for DART (NTRS 20205004248; un-hosted: NTRS says may include copyright): prototype 34.5 kg at 0.5–7 kW output (80–160 V input); 94.8% efficiency (7 kW, 120 V, March 2019), 93.8% hot; flight PPU 3.7 kW / 93.9% (Jan 2020); beam supply up to 90% of output. Confirms `Power processing unit specific mass` 4.7 kg/kW (34.5 / 7.4 kW input); the PPU's ~0.94 bounds the 0.60 total EP efficiency (anode × utilisation ≈ 0.64). `extracted_data/nextc_ppu_performance_key_numbers.csv`.

## Round 6 - ambrosi_2019 [T1, hosted, CC BY]

European RTGs and RHUs (Space Sci Rev 215:55): GPHS/MMRTG heritage; Pu-238 production restart toward ~1.5 kg/yr by 2025 (the ceiling hard-coded in calc.py); small or stacked RTGs 1.3-2.1 W/kg; skutterudite and zintl thermoelectrics as the efficiency path. R72: the americium unit as built gives 9.1-9.3 We from 200 Wth in a 9.4 kg 10 We system, ~1 W/kg. `extracted_data/european_rtg_review_2019_key_numbers.csv`.

## Round 7 - hoffman_2000 [T2, hosted]

Thin-film PV parametric assessment (NASA/TM-2000-210342): the Main Belt Asteroid Tour at 1.5 AU with SEP: 7.5 kW EOL, array 121 kg (4-junction GaAs), $14.1M (2000$). ~62 W/kg at 1.5 AU = ~140 W/kg array-only at 1 AU, about twice the 60 W/kg system row, matching its "batteries, regulation and structure roughly halve that". ~$1880/W at array level vs cells at $400/W (4-j GaAs), $220/W (thin Si), ~$60/W (CIS). Below ~12% film efficiency a lighter substrate does not win on mass. `extracted_data/hoffman_2000_pv_array_key_numbers.csv`.

## Round 9 - ali_2023 [T1, hosted, CC BY]

Li-ion calendar ageing for long missions (Front. Energy Res. 11:1108269): space cells ~265 Wh/kg, 670 Wh/L, ~1000 W/kg; flown on Perseverance, OSIRIS-REx, Parker, THEMIS; controlled envelope -40..+40 °C (an asteroid surface needs active heating); fade grows with temperature and state of charge. Anchors the "cells reach 250–300 Wh/kg" input of the 104 Wh/kg usable row. `extracted_data/ali_2023_space_batteries_key_numbers.csv`.

## Round 10 - The excavation row's "Zacny et al." resolved

- **metzger_zacny_2020** [T1] (J. Aerosp. Eng. 33(6):04020075; arXiv preprint, no licence, read only): regolith conductivity (Eq 21, basalt A0=6.12e-3 W/m-K); volatile release below ~300 °C for epsomite-class material (UCF-CI-1, Orgueil TGA); drilling heat takes hours to days to dissipate, a timeline cost not modelled. Stays in this domain (thermal extraction). `extracted_data/metzger_zacny_2020_key_findings.csv`.
- **just_2019** [T1] (PSS, CC BY; moved to d19): parametric review of 13 excavation techniques.

## Round 43 - Excavation force model and test facility (moved to d19 in R77)

NTRS reachable again through `ntrs.nasa.gov/api/citations/<id>`.

- **zeng_2007** (hosted): drawbar-force model; JSC-1a ρ = 1680 kg/m3, c = 170 N/m2, ca = 1930 N/m2, φ = 35° (β 10°, δ 20°, K0 0.573), SG 2.85; force "lowest values for cohesionless soil but the highest values for very cohesive soil", the mechanism behind the loose/consolidated split.
- **proctor_apex_2019**: Glenn's APEX digger (325 VDC / 100 A; bucket 21.6 cm, 15,600 cm3; load cell Fx,Fy ≤1300 N, Fz ≤3900 N, torque ±203 N-m; 1,587 kg GRC-3B bin): tare-subtracted excavation power.
- **zeitlin_asteroid_excavation_project** (KSC, TRL 3→5): C-type icy regolith under vacuum and cryogenic conditions.

just_2019's indexed table (RASSOR bucket drum 0.761 Wh/kg excluding transport; pneumatic ~2 Wh/kg; impeller ~115–130 W at 6–30 kg/h; bucket ladder <200 W at up to 2400 kg/h) puts loose-regolith cutting far below the 200 Wh/kg median (later rc-027). `19_asteroid_excavation_beneficiation/extracted_data/r43_excavation_energy_key_numbers.csv`.

## Round 44 - ZBO cryocoolers: tested hardware (all hosted)

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

## Round 47 - damodaran_cost_of_capital_by_industry (moved to d17)

January 2026 table (96 industries; CoC = wE×CoE + wD×AT-CoD within ±0.05 pp on every row):

| sector | n | beta | CoE | E/(D+E) | AT-CoD | D/(D+E) | CoC |
|---|---|---|---|---|---|---|---|
| Aerospace/Defense | 79 | 0.95 | 8.17% | 86.53% | 3.97% | 13.47% | 7.60% |
| Metals & Mining | 73 | 1.04 | 8.60% | 90.10% | 2.52% | 9.90% | 8.20% |
| Precious Metals | 56 | 0.84 | 7.68% | 93.21% | 5.97% | 6.79% | 7.47% |
| Total Market | 5994 | 0.91 | 8.02% | 73.98% | 3.97% | 26.02% | 6.96% |

The 10% WACC sits 240 bps above aerospace; range_low 7.5% matches the floor; 15% bounds venture cases. `17_cost_of_capital_contingency_insurance/extracted_data/r47_damodaran_cost_of_capital_key_numbers.csv`.

## Round 50 - DSN rate and launch insurance (both moved in R77)

**jpl_dsn_services_catalog_820_100** (Rev H, 2022-06-06; un-hosted, Caltech copyright): AF = RB × AW × MW (p65; AW 1.0 one 34 m, 2.0 two-station, 3.0 three-array or any combination with a 70 m, 4.0 four; MW 1.0 or 0.5 downlink-only); "the DSN contact dependent hourly rate (RB) was $1,792" (p66); passes over 8 h segmented. CPI-U H1-2022 288.347 -> Aug-2026 334.980 (x1.1617): 34 m ≈ $2,082/hr, so $1,530 is 26.5% low (rc-030); 70 m (AW 3.0) ≈ $6,245 vs the note's ~$4k. The note's own method (FY09 $1,057 x 1.4570 = $1,540) is consistent but rests on the superseded MOCS rate. BLS and World Bank chains agree within 0.02% over 2016-2024.

**gallagher_plane_talking_space_market_updates** (Q1-2024, the cited issue): 2023 loss ~USD900mn on ~USD550mn premium; "insurers are suggesting that premium rating needs to increase significantly." No issue gives a launch-premium percentage, so 10% is directionally supported, not pinned. The note's "post-Intelsat 33e loss" is wrong: Q4-2023 attributes the reset to Viasat-3 and Inmarsat 6-F2 (">85% of the 2023 loses ... post-separation spacecraft issues"), and IS-33e broke up in GEO on Oct 19, 2024 (rc-031).

`extracted_data/r50_dsn_rates_and_launch_insurance_key_numbers.csv`.

## Round 56 - stackpoole_2013_pica_pica_x_postflight_eval (TPS heritage; moved to d21)

The TPS row's cited NTRS 20140005558 (IPPW 2013 summary slide): "Both materials performed well with no unusual ablation performance"; PICA chosen for MSL and OSIRIS-REx; SpaceX's PICA-X flew Dragon COTS Demo 1 (2010); "PICA‐X virgin and char have higher density than Stardust era PICA"; Stardust PICA peak 1000 W/cm2 / 28 kJ/cm2 vs ~50 W/cm2 for Dragon-1 (R70). The $50k/kg stays an estimate.

## Round 57 - Plane Talking through Q2-2026

Seven issues read: Q4-2024 "circa. USD2bn of claims being notified within 18 months."; Q1-2025 capacity USD 550m (2024) / 502m (2025); Q2-2025 "finally shown signs of having turned the corner ... pressure on premium rates", premium fell "by over 50%" 2012-2018; Q1-2026 capacity +~USD100m, SpainSat NG-2 (over USD400m) moves the 2025 loss ratio "from circa 15% to circa 75%", "launch pricing continues to improve"; Q2-2026 +USD 70 million capacity, BlueBird 7 (Blue Origin failure, April 2026) ~USD30m, rate reductions possible in H2-2026. The 10% may sit high for 2026; still no explicit launch rate. R50's claim of Q2-2026 coverage was premature and corrected. `17_cost_of_capital_contingency_insurance/extracted_data/r57_plane_talking_series_key_numbers.csv`.

Also: no source gives a Centaur III or EUS unit price (IG-24-001's $482M EUS is a launch scope; SP-4176 has programme costs: R&D FY59-FY61 $4m -> $36.6m -> $62.6m), so the upper-stage high end stays unanchored.

## Round 63 - FY2027 budget: the ISS envelope

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

`faa_14_cfr_part_450_launch_reentry_licensing`, `crs_r48582_commercial_launch_reentry_regulations` (d18); `mil_hdbk_189c_reliability_growth_management`, `duane_1964_learning_curve_reliability_monitoring` (d16); `valueinvesting_io_2026_boeing_howmet_wacc` (d17); `space_com_pu238_rtg_cost_reporting` (RTG Pu-238 cost context, stays here).

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

## R127 - The Space.com Pu-238 article

`space_com_pu238_rtg_cost_reporting` (2012-04-06, read live): "The goal is to eventually produce between 3.3 pounds and 4.4 pounds (1.5 to 2 kg) of plutonium-238 per year": backs the note's supply clause; the $2.5M/kg is not from it.

## R154 - RTG programme cost and status

- **hamley_2016_rps_program_overview_focus_users** (hosted): Pu-238 supply "originally intended to reach the full production rate of 1.5 kg/yr in 2021", now phasing in "possibly as early as 2019"; MMRTG F2/F3 in storage; "The RPS Program has averaged approximately $75M/year".
- **zakrajsek_et_al_2017_rps_status_expectations_aiaa** (hosted): "the short-term goal being to average 400 g/year by 2019, and a long-term goal to obtain an average rate of 1,500 g/year by 2025".
- **gao_2017_pu238_rps_production_planning** (GAO-17-673; registered from GAO's text): one MMRTG "would cost $77 million, two MMRTGs would cost $94 million, and three MMRTGs would cost $117 million" against an "$850 million development cost cap"; "about 120 watts ... 6 percent power conversion efficiency"; "32 general purpose heat source (GPHS) fuel clads".

$77M per ~110 We ≈ $700k/W, inside the $200k-$1M band. `extracted_data/r154_rtg_program_cost_key_numbers.csv`.

## R163 - The ZBO note's Carnot band (rc-089; 2026-10-14)

The note's "real machines run 15-25% of Carnot" is unsourced: Nugent's measured fractions are 5.0-15.6% (14.5% at the 91.6 W/W point), the MHTB GM cooler 4%; and 14 W/W at 15-25% of Carnot is 56-93 W/W, not 50-150. rc-089 (wording); value and range stand.

## R164 - Candidates (2026-10-14)

rc-101 (cite Hoffman and Schmitz for power-system mass), rc-103 (cite the NEXT-C PPU paper; 4.7 kg/kW is per kW input), rc-108 (cite the RTB test: 5.5 kg/W). Texts in `revision_candidates.csv`.

## R184 - Kleinhenz & Paz ISRU plants (rc-167; 2026-10-17)

Both hosted:

- **kleinhenz_paz_2017_isru_propellant_production_aiaa** (AIAA 2017-0423): "Production rate based on a mission timeline of 480 days (16 months)"; "Requirement: CH4 6978 kg 0.61 kg/hr" with "(22728 kg propellant, 5184 kg leftover)": 29,706 kg ≈ the note's 29.7 t; "A system to produce all 30 mT of Mars ascent propellant is estimated to weigh 1.7 mT using the lowest yield regolith." → 13.2 kg/yr per kg ≈ range_high 13.3.
- **kleinhenz_paz_2021_lunar_water_isru_ptmss_srr** (2021-06-10): H2/O2 at mixture ratio 6; "The baseline system to produce 10 mT of O2 and 1.67 mT of H2 in 225 days was 4.9 mT and 68 kW"; ridge system 2.6 tons, 46 kW ridge + 22 kW mine → 7.28, the row's value and range_low exactly. The 46 kW is also rc-166's cross-check.

Crossref titles the 2017 paper "An ISRU propellant production system for a fully fueled Mars Ascent Vehicle", as spacecost cites; NTRS's copy says "to Fully Fuel". **rc-167:** add DOI 10.2514/6.2017-0423 and note the variant title. No unregistered upstream reference remains for spacecost v0.12.0.

`extracted_data/r184_kp_isru_plant_key_numbers.csv`.
