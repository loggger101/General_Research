# Domain 3 Findings — Δv budgets and propulsion performance tables

Backings: spacecost `reference/delta_v_segments.csv`, `reference/propellants.csv` (Isp, density, cost, EP sizing columns), `delivery.py` stage-mass fractions; economicspace `calc.py` `ep_target_thrust_yr`.

## Round 1 - NEA Δv anchors (both un-hosted 2026-09-26, arXiv default licence)

**elvis2011** [T1] (Planetary and Space Science 59(13):1408-1412; arXiv:1105.4152), the paper the easy-NEA row cites:

| segment | our value | elvis2011 | verdict |
|---|---|---|---|
| LEO → easy NEA | 4500 m/s | ultra-low threshold <4.5 km/s (65/6699 NEOs, ~1%) | agrees; citation correct |
| LEO → average NEA | 6500 m/s | distribution peaks at 6.65 km/s (Benner compilation, Shoemaker-Helin formalism; Sec 4 p4, the plot captioned Figure 3) | value agrees, citation wrong |
| LEO → hard NEA | 8500 m/s | upper tail, below main belt | defensible |

Payload-gain formula e^((Δv−<Δv>)/v_ex) with v_ex = 4.4 km/s (Isp ≈ 449 s), the rocket-equation logic of Module 4.

**ieva2014** [T1] (A&A 569:A59; arXiv:1406.5027): NEOSURFACE survey of 13 objects (all Δv < 10.5 km/s; 11 S-complex, 2 C-complex), with no median or mean Δv. The average-NEA note ("Median NEA Δv per low-Δv NEA survey (arXiv:1406.5027)") should cite elvis2011 and say peak, not median. R71 files: `r71_elvis2011_key_numbers.csv`, `r71_elvis2011_table1_lowest_dv_neos.csv`, `r71_ieva2014_key_numbers.csv`, `r71_ieva2014_table3_mineralogy.csv`, `r71_ieva2014_tables1_2_low_dv_nea_targets.csv`.

## Round 3 - shoemaker_helin_1978 [T2, hosted]

NASA CP-2053 (NTRS 19780021079), the root of Asterank's `dv`: rendezvous impulse ~1 km/s for low-Δv Amors/Apollos; sample-return round trip 2–3 km/s to easy targets vs 5–6+ km/s for typical main-belt objects; dV = 30F + 0.5 km/s (Eq. 11 p4, Fig. 1 p5; corrected in R70 from "3.0F"). The outbound leg dominates the 6500 m/s row; the belt is 2-3x harder than NEAs. `extracted_data/shoemaker_helin_delta_v_key_numbers.csv`.

taylor2018 (Acta Astronautica 146, DOI 10.1016/j.actaastro.2018.02.014), behind the 10500 m/s main-belt row, is paywalled: context-only.

## Round 5 - nextc_protoflight_2021 [T2, hosted]

NEXT-C flight thruster SN001 (NTRS 20210018563): Isp 1400–4160 s, thrust 25–235 mN at up to 6.85 kW; delivered for DART. The Xenon row's 3000 s is a mid-envelope throttle point of flown hardware. With nextc_ppu_2020 (d05), both thruster and PPU rest on flight-article tests. `extracted_data/nextc_flight_thruster_key_numbers.csv`; R72 Tables 2-8 (320 rows: `r72_nextc_protoflight_2021_tables2_8_component_performance.csv`; the 0.69 sccm margin and 1267 V limit print under TL09 in Tables 3-4 but TL05 in Tables 7-8, kept as printed).

## Round 12 - sanna_2024 [T1, hosted, CC BY]

Gateway (NRHO) → LLO bi-impulsive transfers, ≤48 h: lowest total 666 m/s (polar LLO, free RAAN; Table 1 p10), fixed-RAAN polar 671-851 m/s (Table 4), up to ~1253 m/s at i = 20°. (R12's 648 m/s was a single burn of the 738 m/s RAAN = 0 case; corrected R70, with rc-018's text.) The 730 row cites Whitley & Martinez instead (R49). `r72_sanna_2024_tables2_3_method1_transfers.csv`.

## Rounds 13-31 - Isp anchors for propellants.csv

| row (our Isp) | source | what it gives |
|---|---|---|
| hydrolox (452 s) | **bowles_dawson_2004** [T2, hosted] (SP-4176, Centaur/RL-10 history) | narrative only |
| hydrolox (452 s) | **jue_2003** [T2, hosted] (RS-25, AIAA JPC) | vac thrust 2190 kN, SL 1770 kN, vac Isp 452 s, SL 366 s, 69:1, O/F 6.0, 3530 kg: exact (it is the hydrolox row, not kerolox) |
| hydrolox | **ssme_rs25_adaptation_2015** [T2, hosted] | ~3000 ground tests, >1M s hot fire; no Isp table |
| methalox (380 s) | **kim_2013** [T1] (KSPE 17(6):120; un-hosted) | Raptor 2nd stage 380 s vac at 2940 kN: exact; RD-192 356 s vs RD-191 kerolox 337 s |
| several | **thapa_2023** [T1, hosted, CC BY] | Shuttle LOX/LH2 453 s, Saturn V LOX/RP-1 304 s, OMS NTO/MMH 313 s, Shuttle SRB APCP 268 s |
| Solid (285-286 s, kick motors) | **thiokol_sts33r_1990** [T2, hosted] (TWR-17546-1) | RSRM 268.2 s (LH) / 267.6 s (RH) vs predicted 268.5; burn rate 0.368/0.369 ips. R72: propellant mass fraction 0.881, inerts 13.5% (a booster, context only; `r72_thiokol_sts33r_rsrm_mass_properties.csv`) |
| MMH/NTO (336 s) | **yim_2014** [T2, hosted] (Orion ESM) | OMS-E 26.7 kN at 55:1, eight R-4D 490 N, twenty-four 220 N RCS; no Isp. A companion paper quotes 27.7 kN; NASA says 26.7 |
| Hydrazine monoprop (220 s) | **jpl_1968** [T2, hosted] (TR 32-7227) | measured 235 lbf-s/lbm (~97% of theoretical) at 50-55% NH3 dissociation, 44:1; Fig. 3 curve |
| HTP monoprop (165 s) | **hitt_2001** [T1, hosted] | theoretical ~185 s for 98% H2O2; ~140 s at 80% efficiency (1955) |
| Hydrazine arcjet (600 s) | **morren_curran_1991** [T2, hosted] (TM-105149) | SOA ~530 s at 1.6 kW; 300 h at 550 s / 2.0 kW; 600 s at 2-5 kW the goal. `r70_morren_curran_1991_table2_arcjet_performance.csv` |
| NTP (900 s) | **borowski_2012** [T2, hosted] | "~900 seconds or more"; DRA 5.0 ~875-950 s; MCNP ~894-940 s |
| NTP | **robbins_1991** [T2, hosted] (CR-187154) | flight-baseline engine rated 75,000 lbf / 825 s; twenty reactor tests and two engine tests (p11) |
| UDMH/NTO (318 s) | **schoenman_1992** [T2, abstract only] | NTO/MMH 490 N: 309 s at 44:1, 321 lbf-s/lbm at 286:1 |
| Solar thermal (~800 s) | **woodcock_byers_2003** [T2, hosted] | H2 at 2500-3000 K "in excess of 800 seconds"; design case 811 s |
| Solar thermal | **boddy_1980** [T2, hosted] (AFRPL TR-79-7g) | "a specific impulse of 680 seconds was achieved" (the only measured value); 500-1100 s range |
| Aerozine-50/NTO (320 s) | **cuffe_jacobs_1970** [T2, hosted] | SM injector #115 312.8 / 311.4 s; AEDC uncertainty 0.2 s |
| Aerozine-50/NTO | **boyce_aj10_oral_history** [T2, hosted] | AJ10-137 SPS: 20,000 lbf, 100 psi, Isp 314.5, 62.5:1, NTO/A-50 |
| Green monoprop (235 s) | **spores_2013** [T2, hosted] (GPIM, 50th JPC 2014) | GR-1 vac Isp 235 s: exact; GR-1 0.4–1.1 N, GR-22 8–25 N |
| Water resistojet | **asakawa_aquarius_onorbit_2024** [T1, hosted] (EQUULEUS) | Table 3: 91.7 ± 1.0 s (DV1), 90.3 ± 3.0 s (TCM1), ground 68.5 ± 5.5 s; ~6.0 mN, <14 W; CF 1.53 / 1.51 (p5). Low end of the row's 150-220 s |
| Water resistojet | **komurasaki_aquarius_ground_2018** [T1] (JSASS, all rights reserved; un-hosted) | 4.0 mN (Δv thruster) / 2.0 mN (RCS) at 70 s; measured 1.6 mN |
| HTP/RP-1 (320 s, O/F 7) | **krishnan_2010_h2o2_rp1_upper_stage** [T2; un-hosted] | RD-161P 3128 N-s/kg (~319 s) at Phi 5.9; Gamma-2 2599 (~265 s); BA-44/BA-810 2941/2765; Table 2: maximum frozen 3268 at O/F 6.26, O/F 7.38 gives 3407 equilibrium / 3236 frozen; efficiencies 0.90-0.94 |
| HTP/RP-1 | **pietrobon_1999_h2o2_kero_shuttle_boosters** [T1; un-hosted] (JBIS 52) | 98% H2O2/kero at MR 7.30: ve 3017 m/s (~308 s), Id 3940 Ns/l vs LOX/kero 3305 m/s, 3388 Ns/l |
| ALICE (210 s) | **risha_2014_alice_jpp** [T1; un-hosted] (JPP 30(1):133-142) | ideal 207 s SL / 230 s vac; Table 7 motors deliver 56 / 83 / 133 s (1.91 / 3.81 / 7.62 cm). 210 s is an ideal figure, not hardware-realistic: **rc-044** (wording) |
| ALICE | **pourpoint_2012_alice_feasibility** [T1, abstract only, CC BY] | the flight paper; CEA >300 s at O/F ~1.2, ε 100 |
| CO/LOX (260 s) | **hepp_landis_kubiak_1991_mars_co2** [T2, hosted] (TM-103728) | "Mars-derived carbon monoxide can be used directly as a fuel, at a specific impulse of about 300 seconds."; contains no Earth-derived hydrogen |
| CO/LOX | **linne_1996_co_ox_ignition** [T2, hosted] (TM-107267) | chilled CO/O2 combustion at O/F 0.55 (stoichiometric ≈ 1.14). R72: the printed lower-boundary model's cross term (0.0000683) gives O/F 64 at the test point; a refit gives 6.6e-6 (kept as printed). `r72_linne_1996_table1_ignition_boundaries.csv` |

tirila_2023 [T1] (Hall thruster database) is context-only. kim_2013 R40 Table 2 vs our rows: N2H4 240 vs 220; MMH/NTO 323 vs 336 (+4%); LH2/LOX 455 vs 452; LCH4/LOX 364 generic / 380 Raptor; costs ~$10^3 (hypergols), ~$10^1 (LH2/LOX), <$10^1 (LCH4/LOX) per kg; Table 1 at 6.89 MPa, 40:1: kerolox max 358.2 s, methalox 368.9 s. `extracted_data/r40_kim2013_propellant_isp_cost_key_numbers.csv`; R71 `r71_kim_2013_table3_methalox_engines.csv`.

## Round 35 - Cislunar and Mars Δv (four hosted)

**sp4029_apollo_by_the_numbers** (SP-2000-4029), burn tables by word coordinates:

| segment | our value | SP-4029 | verdict |
|---|---|---|---|
| LEO → TLI | 3150 (note 3.05–3.20 km/s) | S-IVB 2nd-burn cutoff A8 9,974 / A11 10,008 / A12 10,515 / A13 10,039 / A14 10,367 / A15 10,415 / A16 10,390 / A17 10,376 ft/s = 3.04–3.20 km/s | agrees |
| TLI → LLO | 900 | LOI cutoff A8 2,997 / A10 2,982 / A11 2,918 / A14 3,022 / A15 3,000 / A17 2,988 ft/s = 889–922 m/s (A16 column-shifted, excluded) | agrees |
| LLO → surface | 1870 (now 2050) | descent A15 6,813 / A16 6,703 / A17 6,698 ft/s = 2.04–2.08 km/s | was 9–11% low; fixed upstream (R134) |
| surface → LEO | 5900 | LM ascent A14 6,066.1 / A15 6,059 / A17 6,075.7 ft/s ≈ 1.85 km/s component | consistent |

Lunar TEI A8 3,519 / A11 3,279 / A17 3,046 ft/s.

**dra5_2009_human_exploration_of_mars** (SP-2009-566) p62: conjunction class "the average total delta-V was approximately 7 km/s ± 1 km/s" (our TMI 3,600 + MOI 900 + TEI 2,100 ≈ 6.6 km/s); opposition class "10 km/s ± 3.7 km/s". EDL mass chain 110.2 → 56.8 → 40.4 t (R70).

**qu_merrill_chai_aas19_225_hybrid_mars_e2e_optimization** (AAS 19-225): "A direct burn from LDHEO during its Earth close approach is needed for Earth departure/arrival V∞ greater than 2 km/s". **chai_merrill_pfrang_qu_aas19_226_landing_site_accessibility** (AAS 19-226): SEP effective ΔV "from 7.5 – 8.5 km/s in 2033 to 6.5 – 7.5 km/s in 2041"; ±20° latitude access 2033–2052.

`extracted_data/r35_cislunar_mars_delta_v_key_numbers.csv`.

## Round 37 - DRA Fig 4-2 per burn; the MOI v∞

Fig 4-2 is vector: 51 bars on a 0.5 km/s grid. Crew (2031–2046): TMI 3.95–4.10, MOI 0.97 (2035) – 1.79 (2031), TEI 1.563 constant; totals 6.27–7.38 km/s, mean 7.17 (inside DRA's 7 ± 1). Cargo (2028–2045): TMI 3.55–4.01, propulsive MOI 0.82–1.35. Our 0.9 MOI is at the low end.

"arrival v∞ of 2.65 km/s (NASA DRA 5.0)" is not in DRA 5.0; Hohmann gives V∞ = 2.6489 km/s and MOI into 250 × 33,793 km = 0.918 km/s, so the value is computed, not sourced.

AAS 19-225 Table 3 (2035): MOI 121.31/122.04 m/s, TEI 121.37/127.21, outbound SEP 3624.05/3615.80; Table 4 (2039, 50° latitude): MOI 367.72/368.16, reorientation 135.27/127.11, TEI 279.35/281.16 (hybrid architecture: context, not our pure-chemical rows). AAS 19-226 Figs 8/10 at |lat| ≈ 50°: MOI ≈ 0.33–0.39 + reorient 0.07–0.11 + TEI 0.08–0.24 km/s; tank capacity 58 t; power at TMI 675/624/574 kW. `extracted_data/r37_mars_per_burn_key_numbers.csv`.

## Round 42 - ssoBFT per-body Δv (berthier_2023_ssodnet, d1)

`delta_v.delta_v` = "Best total velocity range (Delta-V) that a spacecraft must undergo from Earth orbit to match orbit and rendezvous with a target" [km/s].

| population | n | p05 | median | mean | p95 |
|---|---|---|---|---|---|
| whole table | 1,563,628 | — | 10.156 | 10.293 | — (min 3.459, max 37.582) |
| NEA (q<1.3 au) | 42,379 | 5.539 | 8.877 | 10.071 | 18.334 |
| MBA | 1,467,308 | 8.492 | 10.129 | 10.249 | 12.506 |
| other | 53,941 | 8.213 | 11.797 | 11.656 | 14.915 |

The 10,500 m/s main-belt row sits just above the MBA median (p75 = 10.89). Only 0.219% of NEAs (93) are below 4 km/s, 2.2% below 5, 9.1% below 6: the easy/average rows price the accessible tail. Bennu 7.368, Ryugu 6.985, Eros 7.643, Didymos 6.139 km/s (transfer times 233–382 days, 2–3 burns). Join on `number`: (69230) is Hermes, Bennu is 101955. `extracted_data/r42_sso_bft_delta_v_key_numbers.csv`.

## Round 49 - whitley_martinez_2015_nro_staging_orbits [T2, hosted]

IEEE Aerospace 2015 (NTRS 20150019648), behind both cislunar depot rows. Table 3 one-way staging orbit → LLO (m/s): NRO polar 730, NRO equatorial 898, ELO 515, PCO 700, Frozen polar 556 + 252, Frozen equatorial 556 + 408, EM-L2 halo 800, DRO 830. Table 2: NRO round trips 840 m/s (21 d) and 751 m/s (60 d).

- `NRHO → low lunar orbit` = 730: exact (Table 3 and Table 6).
- `TLI → NRHO insertion` = 450: Figure 2 splits the 840 m/s round trip into flyby 178 + NRO insertion 250.5 = 428.5 m/s from TLI (R72); 450 is 5% above. Agrees.

R72: Table 6 gives ELO → polar LLO 953 m/s vs Table 3's 515 + 478 = 993 (kept as printed). `extracted_data/r49_whitley_martinez_nro_staging_orbits_key_numbers.csv`, `r72_whitley_martinez_2015_tables1_6_staging_orbits.csv`.

## Round 55 - LANDER_DRY_MASS_FRAC = 0.20 (SP-4029)

delivery.py's comment "Apollo LM descent stage flew 2,134 kg dry on 8,200 kg of propellant = 0.21" is Apollo 10: dry 4703 lb = 2133.2 kg (+0.04%), loaded 18218.7 lb = 8263.9 kg (−0.77%); 2134/(2134+8200) = 0.2065, so "0.21" rounds up. Fleet δ (p287 press-kit dry, p305 as-flown propellant): A9 0.1912, A10 0.2052, A11 0.1978, A12 0.2092, A13 0.2014, A16 0.2372; median 0.2033. 0.20 is inside the band. `extracted_data/r55_sp4029_lm_stage_mass_key_numbers.csv`.

## Round 56 - TUG_DRY_MASS_FRAC = 0.10 (SP-4029 p294)

S-IVB 'Ground Ignition Weights' (A7–A17; components sum to the printed total within 0.5 lb in 9 of 11): δ structure-only [0.0857, 0.0989], median 0.0963 (A7, the first S-IVB, lowest: 21852 lb dry vs fleet median ~25089); 'other' hardware ~1432–1873 lb; including 'other' hardware [0.0908, 0.1044], median 0.1021. 0.10 is inside (−2.01% vs median), between Centaur V ~0.08 and DCSS ~0.11. `extracted_data/r56_sp4029_sivb_stage_mass_key_numbers.csv`.

## Maintenance (2026-09-26)

Un-hosted: elvis2011, ieva2014, kim_2013, komurasaki_aquarius_ground_2018, krishnan_2010_h2o2_rp1_upper_stage, pietrobon_1999_h2o2_kero_shuttle_boosters, risha_2014_alice_jpp. Tiers: krishnan_2010_h2o2_rp1_upper_stage, spores_2013, borowski_2012 and whitley_martinez_2015_nro_staging_orbits are conference papers (T2). Venue, value and attribution fixes are folded into the text above. 44 rows for 20 hosted sources in `extracted_data/backfill_2026-09-26_key_numbers.csv`.

## R70 / R71 / R72 - Extraction (2026-09-27)

- R70: `r70_asakawa_aquarius_onorbit_2024.csv`, `r70_boddy_1980.csv`, `r70_borowski_2012.csv`, `r70_bowles_dawson_2004.csv`, `r70_boyce_aj10_oral_history.csv`, `r70_chai_merrill_pfrang_qu_aas19_226_landing_site_accessibility.csv`, `r70_cuffe_jacobs_1970.csv`, `r70_dra5_2009_human_exploration_of_mars.csv`, `r70_hepp_landis_kubiak_1991_mars_co2.csv`, `r70_hitt_2001.csv`, `r70_jpl_1968.csv`, `r70_jue_2003.csv`, `r70_linne_1996_co_ox_ignition.csv`, `r70_morren_curran_1991.csv`, `r70_morren_curran_1991_table2_arcjet_performance.csv`, `r70_nextc_protoflight_2021.csv`, `r70_nextc_protoflight_2021_table1_throttle_performance.csv`, `r70_qu_merrill_chai_aas19_225_hybrid_mars_e2e_optimization.csv`, `r70_robbins_1991.csv`, `r70_sanna_2024.csv`, `r70_shoemaker_helin_1978.csv`, `r70_sp4029_apollo_budget_appropriations.csv`, `r70_sp4029_apollo_by_the_numbers_vehicle_summary.csv`, `r70_sp4029_entry_and_key_facts.csv`, `r70_sp4029_ground_ignition_weights.csv`, `r70_sp4029_launch_vehicle_propellant_usage.csv`, `r70_sp4029_lm_ascent_propellant_status.csv`, `r70_sp4029_selected_mission_weights.csv`, `r70_spores_2013.csv`, `r70_ssme_rs25_adaptation_2015.csv`, `r70_thapa_2023.csv`, `r70_thiokol_sts33r_1990.csv`, `r70_woodcock_byers_2003.csv`, `r70_yim_2014.csv`. SP-4029 appropriations: the NASA-total row's years sum to 41,625,782 vs the printed 56,661,332 (kept as printed).
- R71 (un-hosted PDFs restored from git `5dd58d5`): `r71_kim_2013_key_numbers.csv`, `r71_kim_2013_table5_energomash_kerolox_vs_methalox.csv`, `r71_komurasaki_aquarius_ground_2018_key_numbers.csv`, `r71_krishnan_2010_key_numbers.csv`, `r71_krishnan_2010_table1_propellant_properties.csv`, `r71_krishnan_2010_table2_theoretical_performance.csv`, `r71_krishnan_2010_table3_sample_upper_stage_engines.csv`, `r71_krishnan_2010_table4_stage_performance.csv`, `r71_pietrobon_1999_key_numbers.csv`, `r71_pietrobon_1999_table2_engine_performance.csv`, `r71_pietrobon_1999_table3_shuttle_liftoff_masses.csv`, `r71_pietrobon_1999_table4_h2o2_properties.csv`, `r71_risha_2014_key_numbers.csv`, `r71_risha_2014_table4_composite_baselines.csv`, `r71_risha_2014_table7_alice_motor_performance.csv`, `r71_risha_2014_tables5_6_motor_tests.csv` (plus the elvis, ieva and kim files above).
- R72: `r72_kim_2013_table4_aerojet_methane_experience.csv`, `r72_risha_2014_tables1_3_nano_al_characterization.csv`, `r72_woodcock_byers_2003_table2_mission_payloads.csv`, `r72_yim_2014_table2_plume_heat_flux.csv` (plus the files named above).

## R74 - Upstream citations registered (+6)

`nasa_sp125_huzel_huang_design_liquid_rocket_engines` (ascent Δv), `curtis_orbital_mechanics_engineering_students`, `rafalskyi_2021_iodine_ep_in_orbit` (iodine row), `astronautix_encyclopedia_propellant_engine_pages`, `rocketcea_nasa_cea_python_wrapper`, `nasa_std_5019_fracture_control_spaceflight_hardware` (COPV factor).

## R76 / R82 - Low-thrust penalty and thrusting duration

| cell | value | upstream basis |
|---|---|---|
| spacecost `_LOW_THRUST_DV_PENALTY` (`propellants.csv` `dv_penalty_factor`, every electric row) | 1.5 x impulsive Δv | "1.5 is a mid-range figure"; no source |
| economicspace `calc.py` `ep_target_thrust_yr` | 3.0 yr | none |

R82 (three NTRS-hosted):

- **woodcock_dankanich_2006_sep_applications_near_earth**: lunar spiral "40% more than the chemical lunar orbit insertion" (~1.4x); "a unit of launch vehicle delta V was "worth" 70% more than a unit of SEP delta V" (1.7x); GEO "a 35 kWe SEP starting from a 400 x 10,000 orbit could deliver 3600 kg to GEO in about 130 days". 1.5 is bracketed.
- **sjauw_mcguire_freeh_2016_hat_emc_cargo_mars_sep**: Mars cargo from C3 = +2.0 km2/s2 to Vinf 5.2 km/s, "E-M trip= 975 days" (~89% of 3 yr).
- **johnson_castillo_rogez_dervan_mcnutt_2017_nea_scout**: "two year-long cruise".

No candidate. Dawn flight records remain unreachable (R148 below). `extracted_data/r82_low_thrust_dv_penalty_and_duration.csv`.

## Round 103 - STD-5019A and SP-125

- `nasa_std_5019_fracture_control_spaceflight_hardware` hosted at NASA-STD-5019A w/Change 4 (2024-07-29): §7.2.2 covers fracture-critical COPVs and defers to ANSI/AIAA S-081-2000. The 392 kJ/kg figure is a material property; context only.
- `nasa_sp125_huzel_huang_design_liquid_rocket_engines` read (47.8 MB, too large to host): engine design only, no ascent or Δv content (for rc-060).

`extracted_data/r103_sp125_content_check.csv`.

## R115 - DRA 5.0 vs five more Mars rows (rc-070 to rc-074)

- 1-sol orbit → Earth 900 m/s vs DRA's constant TEI 1.563 km/s (p36): rc-070.
- TMI note 3.6-4.3 km/s vs the bars' 3.545-4.103: rc-071.
- Mars entry → surface 800 m/s vs DRA Table 4-3 descent 595 + 15 deorbit: rc-072.
- Low Mars orbit → Earth 2,100 (rc-073) and surface → low Mars orbit 4,100 (rc-074) cite DRA 5.0, which gives neither.

`extracted_data/r115_dra5_vs_spacecost_mars_rows.csv`.

## R120 - rafalskyi_2021_iodine_ep_in_orbit hosted (CC BY in file)

Nature 599:411-415, the NPT30-I2 flight behind the iodine row. Also verified live: `astronautix_encyclopedia_propellant_engine_pages` (use the letter-index paths, e.g. /m/mmh.html) and `rocketcea_nasa_cea_python_wrapper` (v1.2.3, GPL-3.0).

## R129 - Orion nuclear pulse (two hosted)

The `Nuclear pulse (Orion)` row (10,000 s, "Designed in full engineering detail by General Atomics 1958-1965") had no source.

- **general_dynamics_1964_nuclear_pulse_vehicle_study_ga4891** (GA-4891, NTRS 19760065935): "Technical studies on nuclear pulse propulsion were initiated in 1957 ... Early governmental support was awarded in 1958"; direct-launch vehicles of 4,000 tons at 4,000 to 6,000 sec; "a specific impulse between 10,000 and 20,000 sec is predicted for vehicles somewhat larger than the 20-m vehicle"; the Test Ban Treaty "precludes the final development and or operation".
- **schmidt_bonometti_morton_2000_nuclear_pulse_orion_and_beyond** (AIAA 2000-3856): external pusher-plate Isp limits "approximately 3.000 to 10,000 seconds"; NASA ended funding in December 1964; "approximately $11 million had been spent on Orion over nearly seven years".

10,000 s is a range endpoint, not a pin; the "meganewton thrust" clause is unread (GA-4891 Fig 2). `extracted_data/r129_orion_nuclear_pulse_key_numbers.csv`. Meanwhile economicspace@09814da applied rc-030, rc-050, rc-051, rc-052 and rc-057; rc-016 and rc-022 stayed open. Every other swept claim was already registered (`johnson_castillo_rogez_dervan_mcnutt_2017_nea_scout`, `pielke_byerly_2011_shuttle_programme_lifetime_cost`).

## R134 - Lunar descent re-pin verified

spacecost 0.9.0 re-pins `LLO → lunar surface (descent)` 1,870 → 2,050 m/s (mean of 6,813, 6,703, 6,698 ft/s) and adds `Lunar surface → LLO (ascent)` 1,850 m/s (6,066, 6,059, 6,076). All six match SP-4029 (A17 ascent prints 6,075.7). R35's discrepancy closes with no candidate. `extracted_data/r134_spacecost_v090_lunar_repin_verification.csv`.

## Round 148 - Dawn flight records (queue)

NTRS's Dawn IPS records are metadata-only and the EPAG handbook domains are NXDOMAIN. Registered `registered_not_pulled`: `brophy_2011_dawn_ips` (Space Sci Rev 163), `rayman_mase_2014_dawn_cruise_acta` (Acta 103), `garner_rayman_2013_jpc_cruise_yr1`, `garner_rayman_2015_jpc_orbit_ops`, `garner_rayman_2016_jpc_lamo`, `garner_rayman_2018_jpc_final_orb`. They need a library route (DOWNLOADS.md).

## R164 / R165 - Candidates (2026-10-14)

rc-111 (hydrazine: cite JPL 1968), rc-112 (HTP: cite Hitt 2001), rc-113 (arcjet: cite Morren & Curran), rc-114 (NTP: cite Borowski 2012), rc-116 (Orion: 1957-1965, 10,000 s as the upper bound), rc-117 (CO/LOX: cite Hepp and Linne), rc-118 (water resistojet: cite AQUARIUS), rc-138 (cite the 975-day SEP cargo study for `ep_target_thrust_yr`), rc-155 (MMH/NTO 336 s above the measured 309-321), rc-156 (Aerozine-50 to 314.5 s), rc-157 (UDMH/NTO family anchor), rc-158 (kerolox: RD-191 337 s), rc-159 (hydrolox: Jue 2003 and `baumeister_2015_rl10_atlas_to_shuttle_centaur`: RL10A-3-3A 444.4 s), rc-160 (methalox: Kim 2013, `ukai_2019_eucass_jaxa_ihi_lox_methane_full_expander_component_tests`), rc-161 (green monoprop: Spores 2013), rc-162 (solar thermal: 680 s measured, 800-811 s design), rc-163 (xenon: NEXT-C envelope; Hall lower), rc-164 (lunar surface → LEO by flown parts, ~5,930-6,120 m/s). Texts in `revision_candidates.csv`.

## R189 - Thruster mass per newton

The EP sizing columns (`thruster_kg_per_n`, `thrust_scaling`, 16 devices) had no coverage beyond the NEXT-C files cited by rc-102 and rc-104.

- Xenon 54 kg/N: at NEXT-C's 235 mN, a ~12.7 kg head; consistent.
- PPT 5000 kg/N: **zalawski_benson_smernan_hoskins_2002_eo1_ppt_on_orbit_testing** [T2, hosted]: EO-1 PPT 4.95 kg at ~860 µN mean thrust ≈ 5756 kg/N (+13%). The paper prints impulse bits in pico units but its total impulse shows micro (kept with a flag). `extracted_data/r189_eo1_ppt_kg_per_newton_key_numbers.csv`.
- FEEP, MPD, electrospray and exotic rows: no measurements found; their notes name no source.

No candidate.

## R190 - Non-thruster propellant columns (no candidate)

All 41 rows of `isp_vac_s`, `density_kg_per_L`, `ref_cost_usd_per_kg`, `boiloff_pct_per_day`: Xenon 3000 s mid NEXT-C envelope; argon 0.3 kg/L supercritical at 18 MPa (PM/RT ~0.29), krypton 0.55 at 16-17 MPa, xenon 2.0 needs cold near-critical storage (Tc 165 K), iodine 4.93; krypton $794 is the centre of the rc-059 band ($300-$2,100); hydrazine 75 and green monoprop 500 have no price series. The ssoBFT item is closed by R42.

## R192 - The two dead un-hosted file references re-pointed (hygiene)

- After the 2026-10-18 re-clone, `validate.py` failed both `<sha>:<path>` refs in `access_status`
  (`krishnan_2010_h2o2_rp1_upper_stage`, `pietrobon_1999_h2o2_kero_shuttle_boosters`) at commit
  5dd58d5: the object survives only in the pre-re-clone copy and is not in origin's history.
- Re-pointed to 89b6f5f, whose tree (e46be5a3da568b365e262e470dea7cc2535f47b6) is IDENTICAL to
  the orphan's: same maintenance commit survived a history rewrite under a new id. `git show`
  at that state returns exactly what each cell records - krishnan 268,620 B sha256 0641a5e9...,
  pietrobon 89,348 B sha256 31e72bb5... - so the refs now resolve in every fresh clone.
- The bare prose mentions "restored from git 5dd58d5" (the R71 re-extraction anchor) are left as
  history: they record what was fetched at the time and are not checked references.

No source changed; this round's candidate is rc-172, recorded in `02_composition_value/FINDINGS.md`.
## Round 197 - MODEL.md tank-fraction list audited against live pinned rows; rc-175 opened (2026-10-19)

The economicspace model reference documents eight propellant-tank fractions as a fraction of contained propellant mass. That is exactly the ratio the runtime computes (`tank_kg_per_L / density_kg_per_L`, worked_calculation.py line 2409; master.py line 8523 reads the row fields verbatim), so each entry must equal the pinned spacecost v0.12.0 row division. Recomputed all eight live: iodine 0.23, xenon 1.91, APCP solid motor 6.94, hydrolox 9.73, krypton 12.52, cold gas GN2 45.92, bare LH2 (nuclear-thermal row) 52.97 - all seven round to the documented figures; **kerolox is the exception: live rows give 0.027326 / 1.0153 = 2.69 percent while MODEL.md says "xenon 1.9%, kerolox 2.5%"** (quote unique in the file at time of writing; not repeated in README or CITATIONS). Provenance: spacecost propellants.py _STORAGE_CLASS_TANK_MULT comment for mild_cryogen reads 'LOX at 1.141 kg/L -> 2.5%' - the pure-LOX class fraction (0.02875 / 1.141 = 2.52) - and base plus all multipliers are identical between economicspace@260d536, which wrote the sentence on 2026-08-08, and v0.12.0; a class anchor was mislabelled as the blend figure from day one rather than drifting later. Opened **rc-175** (value): change to 2.7 percent or state both figures with their semantics. Documentation-only impact - model output already correct - but it breaks the invariant that MODEL.md can be read as an oracle for what verification_sheet.py prints, understating kerolox tankage by about 0.19 percentage points per kilogram of propellant (+7.6 percent relative) for a reader working from prose.

Same sweep, two consistency results recorded without RCs: (a) the GCAT claim "613 active geostationary satellites (McDowell's GCAT, Jan 2026; 550 until mineral_value 1.13.0)" agrees with registered source mc_dowell_2025_space_activities_gcat - rc-057 was applied upstream and the model re-pinned exactly as the registry predicted; (b) MODEL.md quotes Mars entry survival derivations "MSL landed 899 kg of a 3,153 kg entry mass" and "Perseverance 1,026 of 3,369" - internally consistent with the documented fractions (28.5 percent / 30.5 percent) but spacecost stores only the flat MARS_LANDED_MASS_FRACTION = 0.3; no registered GR source carries institutional entry masses for either mission, so no candidate can be opened on them yet - if a future pull lands JPL mission factsheets with entry masses, re-check this line first (899 kg landed matches r139_edl_mass_budget_key_numbers.csv).
## Round 203 - rc-177: the GEO coplanar-burn context figure contradicts exact two-body arithmetic and upstream's own docs (2026-10-19)

While sweeping economicspace MODEL.md delivery-table claims against the pinned spacecost v0.12.0 delta-v table, one prose-vs-code seam opened onto a three-way contradiction on the same manoeuvre:

- **Exact two-body** at the geometry upstream itself prints (mu = 398600.4418 km^3/s^2; r_p = 6578 km — fixed by the table's own perigee-burn note, which prints v_LEO 7.784 and v_p(GTO) 10.239, values that only hold for R_E = 6378 + 200; r_a = 42,164 km): GTO apogee speed **1597.4 m/s**, GEO circular **3074.67 m/s**, coplanar circularisation **1477.29 -> "1,477"**, combined burn at 28.5 deg **1836.50** (row value 1,836 is within rounding either way), inclination cost **359.21 -> "359"**.
- **economicspace MODEL.md L191**: "Those are two different numbers for the same manoeuvre, 1,730 and 1,836 m/s against 1,477 coplanar, and the model keeps them apart on purpose." (sentence joined across its line wrap) — matches exact math. The Module 4 docstring (master.py at d77f1ce) agrees: "Coplanar the same burn would be 1.477, so the inclination is worth 253 m/s on arrival and 359 on launch."
- **The consumed constant** `_GEO_COPLANAR_GTO_BURN_M_S = 1_478.0` (master.py L988; duplicated verbatim at modules/mineral_value.py L502) prints "Coplanar that burn would be 1,478, so 358 m/s of this price is the latitude of the launch site" — off by one against both docs and the exact value.
- **spacecost delta_v_segments.csv** GTO->GEO note carries the same pair: "Coplanar it would be 1,478; the 358 m/s difference is what an equatorial launch site is worth" (count==1).

The constant's own comment marks these figures as comparisons and context rather than terms in the price, and `plane_change` feeds only note strings — no pricing chain moves. But three sites print a coplanar figure that does not reproduce under upstream's stated geometry, contradicting MODEL.md and Module 4 within economicspace itself. rc-177 proposes setting it to 1_477 (or deriving from constants) and restating the spacecost note so its coplanar figure reads 1,477 and its equatorial-site difference figure reads 359.

Boundary case recorded for completeness: Module 4's arrival-plane-change figure of 253 m/s recomputes to ~252 from unrounded inputs (arrival combined burn at 23.44 deg = 1729.2; minus coplanar 1477.3) — the same rounded-intermediate family; deliberately not part of the proposal.

Source: curtis_orbital_mechanics_engineering_students (T4, d03), the textbook spacecost's own delta_v_segments header cites for ascent-line values and covering Hohmann transfers with inclined plane change by law of cosines.

**Round 205 - Sutton & Biblarz registered as RELATIONS-register context.**

economicspace CITATIONS.md section 4 names Sutton and Biblarz (Rocket Propulsion Elements, 9th ed., Wiley 2017) for the rocket equation, exhaust velocity, thrust and jet power relations that campaign/verification_sheet.py prints in its RELATIONS register. No registry row carried it; registered this round as sutton_biblarz_2017_rocket_propulsion_elements_ninth_edition [T4; registered_not_pulled], textbook class alongside curtis_orbital_mechanics_engineering_students (d03) and vallado_fundamentals_astrodynamics_applications (d13). Context-only: no cell pins a figure to it.

**Round 206 - drift audit of economicspace #150-#153 and provenance correction.**

economicspace moved d77f1ce -> **36bc858** (four commits: verification-worksheet backing part "Backing, row by row", layout fixes, retired-$50-ISRU-rate naming, text pass; no engine or reference-table changes). Audit results:
- The new CITATIONS.md section "Textbook relations the verification worksheet cites" names exactly three works - Sutton & Biblarz 2017 (registered R205), Vallado 4th ed. 2013 (row updated this round, see d13 FINDINGS) and Fowler & Chillemi 1992 in Tedesco et al., PL-TR-92-2049 (hosted since R70). No new registration needed; the inline "(SpaceNews 2024)" and "per Reuters analyst consensus" attributions surfaced by their source-splitter audit are already registered (`spacenews_launch_reporting_2024_2026`, `reuters_2026_gold_analyst_consensus`).
- **Provenance correction (this round):** the R205 Sutton row pinned CITATIONS.md section 4 to @d77f1ce, but both that section and the RELATIONS register of verification_sheet.py arrived with #153 at 36bc858 - `git show d77f1ce:CITATIONS.md` has no Sutton line and its verification_sheet.py contains zero RELATIONS tokens. The sweep had read the parallel session's dirty working tree while HEAD was still d77f1ce. access_status now carries the dated correct pin; registration itself stands unchanged (the source is genuinely cited upstream at HEAD).
- Money-Mass-ematics: their versions.md records that the frozen spacecost 0.5.0 table cited "NASA Money-Mass-ematics 2023" for beneficiation energy and the installed release withdrew it - verified genuine (`spacecost a4cb4fc` "Cut 0.5.1: withdraw two dead citations"). GR never registered or cited it (zero hits in sources.csv); the current beneficiation cell self-declares as an unsourced engineering estimate and its anchor space is already claimed by open rc-097 (doe_2007 mining-energy bandwidth) - no candidate from this seam.
- Open candidates unaffected: MODEL.md tank-fraction text (rc-175), README "~1.2 GB" line (rc-176, root README untouched by the drift; campaign/README.md gained only feature prose) and the GEO coplanar strings (rc-177) all still read as recorded.
