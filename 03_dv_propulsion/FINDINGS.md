## R542 — Mars ascent Δv additional configuration comparator (2026-11-10)

- **palaszewski_2022_mars_landing_ascent_delta_v** (NASA NTRS 20210026187; Bryan Palaszewski, *Mars Research*, IntechOpen): §2.5 Table 3 gives 4,200 m/s for ascent from the Martian surface to a 100 km circular low Mars orbit and states a 20% gravity-loss allowance; §3.0 repeats the 4,200 m/s ascent value. Table 3 separately gives 244.8 m/s for transfer to 500 km circular orbit, 4,444.8 m/s combined.
- The current spacecost row remains 4,100 m/s and is described as an unsourced estimate including gravity and drag losses. The new LMO-only case is 100 m/s (2.4%) higher; it supports the scale of the estimate but is a human Mars landing vehicle case, not a generic mission requirement. Combined with the already registered 3,950 m/s Lewis et al. two-stage 100 × 100 km / 30° case, the comparisons bracket 4,100 m/s but do not establish a universal replacement. **rc-377** remains open.
- Extracted: extracted_data/r542_palaszewski_mars_ascent_dv.csv.

# Domain 3 Findings — Δv budgets and propulsion performance tables

## R512 — Water resistojet specific-impulse range (2026-11-10)

- **morren_1992_nasa_tm_105877_water_resistojet** (NASA TM-105877; AIAA 92-3533): the abstract (p. 1) reports a maximum measured 234 s for a water-vaporizer / engineering-model resistojet assembly at 6.8 MJ/kg combined specific power. Table II (p. 10) identifies 234 s in its final specific-impulse test point, with 1,043 W total power and 6.86 MJ/kg total specific power.
- Current spacecost reference/propellants.csv gives the water electrothermal/resistojet row a 150–220 s estimated range and 190 s center for higher-power designs. The lab measurement is 14 s above the range ceiling; it was a narrow test of an engineering model, not a flight result. **rc-378** records the range-bound question without proposing a new center value.
- Extracted: extracted_data/r512_morren_water_resistojet_isp.csv.

## R511 — Mars surface-to-orbit ascent Δv comparator (2026-11-09)

- **lewis_etal_2020_mars_ascent_vehicle_synergy** (NTRS 20205007701; NASA Langley, ASCEND 2020): Table 2 p. 3 reports 3,950 m/s from Mars surface to LMO. Table 1 p. 3 defines LMO as 100 × 100 km at 30° inclination. The paper says the value is for a two-stage vehicle, rounded to 50 m/s, and includes main-propulsion burns without reserves or residuals.
- Current spacecost reference/delta_v_segments.csv still has 4,100 m/s for “Mars surface → low Mars orbit”; its note calls the value an unsourced estimate including gravity and drag losses. The source is a bounded configuration comparator, 150 m/s below the stored value; it does not establish a universal replacement. **rc-377** remains open.
- Extracted: extracted_data/r511_mars_ascent_delta_v.csv.

Backings: spacecost `reference/delta_v_segments.csv`, `reference/propellants.csv` (Isp, density, cost, EP sizing columns), `delivery.py` stage-mass fractions; economicspace `calc.py` `ep_target_thrust_yr`.

## R1 - NEA Δv anchors (both un-hosted 2026-09-26, arXiv default licence) (2026-09-17)

**elvis2011** [T1] (Planetary and Space Science 59(13):1408-1412; arXiv:1105.4152), the paper the easy-NEA row cites:

| segment | our value | elvis2011 | verdict |
|---|---|---|---|
| LEO → easy NEA | 4500 m/s | ultra-low threshold <4.5 km/s (65/6699 NEOs, ~1%) | agrees; citation correct |
| LEO → average NEA | 6500 m/s | distribution peaks at 6.65 km/s (Benner compilation, Shoemaker-Helin formalism; Sec 4 p4, the plot captioned Figure 3) | value agrees, citation wrong |
| LEO → hard NEA | 8500 m/s | upper tail, below main belt | defensible |

Payload-gain formula e^((Δv−<Δv>)/v_ex) with v_ex = 4.4 km/s (Isp ≈ 449 s), the rocket-equation logic of Module 4.

**ieva2014** [T1] (A&A 569:A59; arXiv:1406.5027): NEOSURFACE survey of 13 objects (all Δv < 10.5 km/s; 11 S-complex, 2 C-complex), with no median or mean Δv. The average-NEA note ("Median NEA Δv per low-Δv NEA survey (arXiv:1406.5027)") should cite elvis2011 and say peak, not median. R71 files: `r71_elvis2011_key_numbers.csv`, `r71_elvis2011_table1_lowest_dv_neos.csv`, `r71_ieva2014_key_numbers.csv`, `r71_ieva2014_table3_mineralogy.csv`, `r71_ieva2014_tables1_2_low_dv_nea_targets.csv`.

Key numbers for both: `extracted_data/delta_v_segments_key_numbers.csv`.

## R3 - shoemaker_helin_1978 [T2, hosted] (2026-09-18)

NASA CP-2053 (NTRS 19780021079), the root of Asterank's `dv`: rendezvous impulse ~1 km/s for low-Δv Amors/Apollos; sample-return round trip 2–3 km/s to easy targets vs 5–6+ km/s for typical main-belt objects; dV = 30F + 0.5 km/s (Eq. 11 p4, Fig. 1 p5; corrected in R70 from "3.0F"). The outbound leg dominates the 6500 m/s row; the belt is 2-3x harder than NEAs. `extracted_data/shoemaker_helin_delta_v_key_numbers.csv`.

taylor2018 (Acta Astronautica 146, DOI 10.1016/j.actaastro.2018.02.014), behind the 10500 m/s main-belt row, is paywalled: context-only.

## R5 - nextc_protoflight_2021 [T2, hosted] (2026-09-18)

NEXT-C flight thruster SN001 (NTRS 20210018563): Isp 1400–4160 s, thrust 25–235 mN at up to 6.85 kW; delivered for DART. The Xenon row's 3000 s is a mid-envelope throttle point of flown hardware. With nextc_ppu_2020 (d05), both thruster and PPU rest on flight-article tests. `extracted_data/nextc_flight_thruster_key_numbers.csv`; R72 Tables 2-8 (320 rows: `r72_nextc_protoflight_2021_tables2_8_component_performance.csv`; the 0.69 sccm margin and 1267 V limit print under TL09 in Tables 3-4 but TL05 in Tables 7-8, kept as printed).

## R12 - sanna_2024 [T1, hosted, CC BY] (2026-09-18)

Gateway (NRHO) → LLO bi-impulsive transfers, ≤48 h: lowest total 666 m/s (polar LLO, free RAAN; Table 1 p10), fixed-RAAN polar 671-851 m/s (Table 4), up to ~1253 m/s at i = 20°. (R12's 648 m/s was a single burn of the 738 m/s RAAN = 0 case; corrected R70, with rc-018's text.) The 730 row cites Whitley & Martinez instead (R49). `r72_sanna_2024_tables2_3_method1_transfers.csv`.

## R13-R31 - Isp anchors for propellants.csv

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

## R35 - Cislunar and Mars Δv (four hosted) (2026-09-21)

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

## R37 - DRA Fig 4-2 per burn; the MOI v∞ (2026-09-21)

Fig 4-2 is vector: 51 bars on a 0.5 km/s grid. Crew (2031–2046): TMI 3.95–4.10, MOI 0.97 (2035) – 1.79 (2031), TEI 1.563 constant; totals 6.27–7.38 km/s, mean 7.17 (inside DRA's 7 ± 1). Cargo (2028–2045): TMI 3.55–4.01, propulsive MOI 0.82–1.35. Our 0.9 MOI is at the low end.

"arrival v∞ of 2.65 km/s (NASA DRA 5.0)" is not in DRA 5.0; Hohmann gives V∞ = 2.6489 km/s and MOI into 250 × 33,793 km = 0.918 km/s, so the value is computed, not sourced.

AAS 19-225 Table 3 (2035): MOI 121.31/122.04 m/s, TEI 121.37/127.21, outbound SEP 3624.05/3615.80; Table 4 (2039, 50° latitude): MOI 367.72/368.16, reorientation 135.27/127.11, TEI 279.35/281.16 (hybrid architecture: context, not our pure-chemical rows). AAS 19-226 Figs 8/10 at |lat| ≈ 50°: MOI ≈ 0.33–0.39 + reorient 0.07–0.11 + TEI 0.08–0.24 km/s; tank capacity 58 t; power at TMI 675/624/574 kW. `extracted_data/r37_mars_per_burn_key_numbers.csv`.

## R42 - ssoBFT per-body Δv (berthier_2023_ssodnet, d1) (2026-09-23)

`delta_v.delta_v` = "Best total velocity range (Delta-V) that a spacecraft must undergo from Earth orbit to match orbit and rendezvous with a target" [km/s].

| population | n | p05 | median | mean | p95 |
|---|---|---|---|---|---|
| whole table | 1,563,628 | — | 10.156 | 10.293 | — (min 3.459, max 37.582) |
| NEA (q<1.3 au) | 42,379 | 5.539 | 8.877 | 10.071 | 18.334 |
| MBA | 1,467,308 | 8.492 | 10.129 | 10.249 | 12.506 |
| other | 53,941 | 8.213 | 11.797 | 11.656 | 14.915 |

The 10,500 m/s main-belt row sits just above the MBA median (p75 = 10.89). Only 0.219% of NEAs (93) are below 4 km/s, 2.2% below 5, 9.1% below 6: the easy/average rows price the accessible tail. Bennu 7.368, Ryugu 6.985, Eros 7.643, Didymos 6.139 km/s (transfer times 233–382 days, 2–3 burns). Join on `number`: (69230) is Hermes, Bennu is 101955. `extracted_data/r42_sso_bft_delta_v_key_numbers.csv`.

## R49 - whitley_martinez_2015_nro_staging_orbits [T2, hosted] (2026-09-23)

IEEE Aerospace 2015 (NTRS 20150019648), behind both cislunar depot rows. Table 3 one-way staging orbit → LLO (m/s): NRO polar 730, NRO equatorial 898, ELO 515, PCO 700, Frozen polar 556 + 252, Frozen equatorial 556 + 408, EM-L2 halo 800, DRO 830. Table 2: NRO round trips 840 m/s (21 d) and 751 m/s (60 d).

- `NRHO → low lunar orbit` = 730: exact (Table 3 and Table 6).
- `TLI → NRHO insertion` = 450: Figure 2 splits the 840 m/s round trip into flyby 178 + NRO insertion 250.5 = 428.5 m/s from TLI (R72); 450 is 5% above. Agrees.

R72: Table 6 gives ELO → polar LLO 953 m/s vs Table 3's 515 + 478 = 993 (kept as printed). `extracted_data/r49_whitley_martinez_nro_staging_orbits_key_numbers.csv`, `r72_whitley_martinez_2015_tables1_6_staging_orbits.csv`.

## R55 - LANDER_DRY_MASS_FRAC = 0.20 (SP-4029) (2026-09-24)

delivery.py's comment "Apollo LM descent stage flew 2,134 kg dry on 8,200 kg of propellant = 0.21" is Apollo 10: dry 4703 lb = 2133.2 kg (+0.04%), loaded 18218.7 lb = 8263.9 kg (−0.77%); 2134/(2134+8200) = 0.2065, so "0.21" rounds up. Fleet δ (p287 press-kit dry, p305 as-flown propellant): A9 0.1912, A10 0.2052, A11 0.1978, A12 0.2092, A13 0.2014, A16 0.2372; median 0.2033. 0.20 is inside the band. `extracted_data/r55_sp4029_lm_stage_mass_key_numbers.csv`.

## R56 - TUG_DRY_MASS_FRAC = 0.10 (SP-4029 p294) (2026-09-24)

S-IVB 'Ground Ignition Weights' (A7–A17; components sum to the printed total within 0.5 lb in 9 of 11): δ structure-only [0.0857, 0.0989], median 0.0963 (A7, the first S-IVB, lowest: 21852 lb dry vs fleet median ~25089); 'other' hardware ~1432–1873 lb; including 'other' hardware [0.0908, 0.1044], median 0.1021. 0.10 is inside (−2.01% vs median), between Centaur V ~0.08 and DCSS ~0.11. `extracted_data/r56_sp4029_sivb_stage_mass_key_numbers.csv`.

## Maintenance (2026-09-26)

Un-hosted: elvis2011, ieva2014, kim_2013, komurasaki_aquarius_ground_2018, krishnan_2010_h2o2_rp1_upper_stage, pietrobon_1999_h2o2_kero_shuttle_boosters, risha_2014_alice_jpp. Tiers: krishnan_2010_h2o2_rp1_upper_stage, spores_2013, borowski_2012 and whitley_martinez_2015_nro_staging_orbits are conference papers (T2). Venue, value and attribution fixes are folded into the text above. 44 rows for 20 hosted sources in `extracted_data/backfill_2026-09-26_key_numbers.csv`.

## R70 / R71 / R72 - Extraction (2026-09-27)

- R70: `r70_asakawa_aquarius_onorbit_2024.csv`, `r70_boddy_1980.csv`, `r70_borowski_2012.csv`, `r70_bowles_dawson_2004.csv`, `r70_boyce_aj10_oral_history.csv`, `r70_chai_merrill_pfrang_qu_aas19_226_landing_site_accessibility.csv`, `r70_cuffe_jacobs_1970.csv`, `r70_dra5_2009_human_exploration_of_mars.csv`, `r70_hepp_landis_kubiak_1991_mars_co2.csv`, `r70_hitt_2001.csv`, `r70_jpl_1968.csv`, `r70_jue_2003.csv`, `r70_linne_1996_co_ox_ignition.csv`, `r70_morren_curran_1991.csv`, `r70_morren_curran_1991_table2_arcjet_performance.csv`, `r70_nextc_protoflight_2021.csv`, `r70_nextc_protoflight_2021_table1_throttle_performance.csv`, `r70_qu_merrill_chai_aas19_225_hybrid_mars_e2e_optimization.csv`, `r70_robbins_1991.csv`, `r70_sanna_2024.csv`, `r70_shoemaker_helin_1978.csv`, `r70_sp4029_apollo_budget_appropriations.csv`, `r70_sp4029_apollo_by_the_numbers_vehicle_summary.csv`, `r70_sp4029_entry_and_key_facts.csv`, `r70_sp4029_ground_ignition_weights.csv`, `r70_sp4029_launch_vehicle_propellant_usage.csv`, `r70_sp4029_lm_ascent_propellant_status.csv`, `r70_sp4029_selected_mission_weights.csv`, `r70_spores_2013.csv`, `r70_ssme_rs25_adaptation_2015.csv`, `r70_thapa_2023.csv`, `r70_thiokol_sts33r_1990.csv`, `r70_woodcock_byers_2003.csv`, `r70_yim_2014.csv`. SP-4029 appropriations: the NASA-total row's years sum to 41,625,782 vs the printed 56,661,332 (kept as printed).
- R71 (un-hosted PDFs restored from git `5dd58d5`): `r71_kim_2013_key_numbers.csv`, `r71_kim_2013_table5_energomash_kerolox_vs_methalox.csv`, `r71_komurasaki_aquarius_ground_2018_key_numbers.csv`, `r71_krishnan_2010_key_numbers.csv`, `r71_krishnan_2010_table1_propellant_properties.csv`, `r71_krishnan_2010_table2_theoretical_performance.csv`, `r71_krishnan_2010_table3_sample_upper_stage_engines.csv`, `r71_krishnan_2010_table4_stage_performance.csv`, `r71_pietrobon_1999_key_numbers.csv`, `r71_pietrobon_1999_table2_engine_performance.csv`, `r71_pietrobon_1999_table3_shuttle_liftoff_masses.csv`, `r71_pietrobon_1999_table4_h2o2_properties.csv`, `r71_risha_2014_key_numbers.csv`, `r71_risha_2014_table4_composite_baselines.csv`, `r71_risha_2014_table7_alice_motor_performance.csv`, `r71_risha_2014_tables5_6_motor_tests.csv` (plus the elvis, ieva and kim files above).
- R72: `r72_kim_2013_table4_aerojet_methane_experience.csv`, `r72_risha_2014_tables1_3_nano_al_characterization.csv`, `r72_woodcock_byers_2003_table2_mission_payloads.csv`, `r72_yim_2014_table2_plume_heat_flux.csv` (plus the files named above).

## R74 - Upstream citations registered (+6)

`nasa_sp125_huzel_huang_design_liquid_rocket_engines` (ascent Δv), `curtis_orbital_mechanics_engineering_students`, `rafalskyi_2021_iodine_ep_in_orbit` (iodine row), `astronautix_encyclopedia_propellant_engine_pages`, `nasa_std_5019_fracture_control_spaceflight_hardware` (COPV factor).

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

## R103 - STD-5019A and SP-125 (2026-10-02)

- `nasa_std_5019_fracture_control_spaceflight_hardware` hosted at NASA-STD-5019A w/Change 4 (2024-07-29): §7.2.2 covers fracture-critical COPVs and defers to ANSI/AIAA S-081-2000. The 392 kJ/kg figure is a material property; context only.
- `nasa_sp125_huzel_huang_design_liquid_rocket_engines` read (47.8 MB, too large to host): engine design only, no ascent or Δv content (for rc-060).

`extracted_data/r103_sp125_content_check.csv`.

Extracted data: `extracted_data/r103_std_5019a_copv_key_numbers.csv`.

## R115 - DRA 5.0 vs five more Mars rows (rc-070 to rc-074)

- 1-sol orbit → Earth 900 m/s vs DRA's constant TEI 1.563 km/s (p36): rc-070.
- TMI note 3.6-4.3 km/s vs the bars' 3.545-4.103: rc-071.
- Mars entry → surface 800 m/s vs DRA Table 4-3 descent 595 + 15 deorbit: rc-072.
- Low Mars orbit → Earth 2,100 (rc-073) and surface → low Mars orbit 4,100 (rc-074) cite DRA 5.0, which gives neither.

`extracted_data/r115_dra5_vs_spacecost_mars_rows.csv`.

## R120 - rafalskyi_2021_iodine_ep_in_orbit hosted (CC BY in file)

Nature 599:411-415, the NPT30-I2 flight behind the iodine row. Also verified live: `astronautix_encyclopedia_propellant_engine_pages` (use the letter-index paths, e.g. /m/mmh.html).

## R129 - Orion nuclear pulse (two hosted)

The `Nuclear pulse (Orion)` row (10,000 s, "Designed in full engineering detail by General Atomics 1958-1965") had no source.

- **general_dynamics_1964_nuclear_pulse_vehicle_study_ga4891** (GA-4891, NTRS 19760065935): "Technical studies on nuclear pulse propulsion were initiated in 1957 ... Early governmental support was awarded in 1958"; direct-launch vehicles of 4,000 tons at 4,000 to 6,000 sec; "a specific impulse between 10,000 and 20,000 sec is predicted for vehicles somewhat larger than the 20-m vehicle"; the Test Ban Treaty "precludes the final development and or operation".
- **schmidt_bonometti_morton_2000_nuclear_pulse_orion_and_beyond** (AIAA 2000-3856): external pusher-plate Isp limits "approximately 3.000 to 10,000 seconds"; NASA ended funding in December 1964; "approximately $11 million had been spent on Orion over nearly seven years".

10,000 s is a range endpoint, not a pin; the "meganewton thrust" clause is unread (GA-4891 Fig 2). `extracted_data/r129_orion_nuclear_pulse_key_numbers.csv`. Meanwhile economicspace@09814da applied rc-030, rc-050, rc-051, rc-052 and rc-057; rc-016 and rc-022 stayed open. Every other swept claim was already registered (`johnson_castillo_rogez_dervan_mcnutt_2017_nea_scout`, `pielke_byerly_2011_shuttle_programme_lifetime_cost`).

## R134 - Lunar descent re-pin verified

spacecost 0.9.0 re-pins `LLO → lunar surface (descent)` 1,870 → 2,050 m/s (mean of 6,813, 6,703, 6,698 ft/s) and adds `Lunar surface → LLO (ascent)` 1,850 m/s (6,066, 6,059, 6,076). All six match SP-4029 (A17 ascent prints 6,075.7). R35's discrepancy closes with no candidate. `extracted_data/r134_spacecost_v090_lunar_repin_verification.csv`.

## R148 - Dawn flight records (queue) (2026-10-10)

NTRS's Dawn IPS records are metadata-only and the EPAG handbook domains are NXDOMAIN. Registered `registered_not_pulled`: `brophy_2011_dawn_ips` (Space Sci Rev 163), `rayman_mase_2014_dawn_cruise_acta` (Acta 103), `garner_rayman_2013_jpc_cruise_yr1`, `garner_rayman_2015_jpc_orbit_ops`, `garner_rayman_2016_jpc_lamo`, `garner_rayman_2018_jpc_final_orb`. They need a library route (DOWNLOADS.md).

## R164 / R165 - Candidates (2026-10-14)

rc-111 (hydrazine: cite JPL 1968), rc-112 (HTP: cite Hitt 2001), rc-113 (arcjet: cite Morren & Curran), rc-114 (NTP: cite Borowski 2012), rc-116 (Orion: 1957-1965, 10,000 s as the upper bound), rc-117 (CO/LOX: cite Hepp and Linne), rc-118 (water resistojet: cite AQUARIUS), rc-138 (cite the 975-day SEP cargo study for `ep_target_thrust_yr`), rc-155 (MMH/NTO 336 s above the measured 309-321), rc-156 (Aerozine-50 to 314.5 s), rc-157 (UDMH/NTO family anchor), rc-158 (kerolox: RD-191 337 s), rc-159 (hydrolox: Jue 2003 and `baumeister_2015_rl10_atlas_to_shuttle_centaur`: RL10A-3-3A 444.4 s), rc-160 (methalox: Kim 2013, `ukai_2019_eucass_jaxa_ihi_lox_methane_full_expander_component_tests`), rc-161 (green monoprop: Spores 2013), rc-162 (solar thermal: 680 s measured, 800-811 s design), rc-163 (xenon: NEXT-C envelope; Hall lower), rc-164 (lunar surface → LEO by flown parts, ~5,930-6,120 m/s). Texts in `revision_candidates.csv` (open) and `revision_candidates_closed.csv`.

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

## R197 - MODEL.md tank-fraction list audited against live pinned rows; rc-175 opened (2026-10-19)

The economicspace model reference documents eight propellant-tank fractions as a fraction of contained propellant mass. That is exactly the ratio the runtime computes (`tank_kg_per_L / density_kg_per_L`, worked_calculation.py line 2409; master.py line 8523 reads the row fields verbatim), so each entry must equal the pinned spacecost v0.12.0 row division. Recomputed all eight live: iodine 0.23, xenon 1.91, APCP solid motor 6.94, hydrolox 9.73, krypton 12.52, cold gas GN2 45.92, bare LH2 (nuclear-thermal row) 52.97 - all seven round to the documented figures; **kerolox is the exception: live rows give 0.027326 / 1.0153 = 2.69 percent while MODEL.md says "xenon 1.9%, kerolox 2.5%"** (quote unique in the file at time of writing; not repeated in README or CITATIONS). Provenance: spacecost propellants.py _STORAGE_CLASS_TANK_MULT comment for mild_cryogen reads 'LOX at 1.141 kg/L -> 2.5%' - the pure-LOX class fraction (0.02875 / 1.141 = 2.52) - and base plus all multipliers are identical between economicspace@260d536, which wrote the sentence on 2026-08-08, and v0.12.0; a class anchor was mislabelled as the blend figure from day one rather than drifting later. Opened **rc-175** (value): change to 2.7 percent or state both figures with their semantics. Documentation-only impact - model output already correct - but it breaks the invariant that MODEL.md can be read as an oracle for what verification_sheet.py prints, understating kerolox tankage by about 0.19 percentage points per kilogram of propellant (+7.6 percent relative) for a reader working from prose.

Same sweep, two consistency results recorded without RCs: (a) the GCAT claim "613 active geostationary satellites (McDowell's GCAT, Jan 2026; 550 until mineral_value 1.13.0)" agrees with registered source mc_dowell_2025_space_activities_gcat - rc-057 was applied upstream and the model re-pinned exactly as the registry predicted; (b) MODEL.md quotes Mars entry survival derivations "MSL landed 899 kg of a 3,153 kg entry mass" and "Perseverance 1,026 of 3,369" - internally consistent with the documented fractions (28.5 percent / 30.5 percent) but spacecost stores only the flat MARS_LANDED_MASS_FRACTION = 0.3; no registered GR source carries institutional entry masses for either mission, so no candidate can be opened on them yet - if a future pull lands JPL mission factsheets with entry masses, re-check this line first (899 kg landed matches r139_edl_mass_budget_key_numbers.csv).

## R203 - rc-177: the GEO coplanar-burn context figure contradicts exact two-body arithmetic and upstream's own docs (2026-10-19)

While sweeping economicspace MODEL.md delivery-table claims against the pinned spacecost v0.12.0 delta-v table, one prose-vs-code seam opened onto a three-way contradiction on the same manoeuvre:

- **Exact two-body** at the geometry upstream itself prints (mu = 398600.4418 km^3/s^2; r_p = 6578 km — fixed by the table's own perigee-burn note, which prints v_LEO 7.784 and v_p(GTO) 10.239, values that only hold for R_E = 6378 + 200; r_a = 42,164 km): GTO apogee speed **1597.4 m/s**, GEO circular **3074.67 m/s**, coplanar circularisation **1477.29 -> "1,477"**, combined burn at 28.5 deg **1836.50** (row value 1,836 is within rounding either way), inclination cost **359.21 -> "359"**.
- **economicspace MODEL.md L191**: "Those are two different numbers for the same manoeuvre, 1,730 and 1,836 m/s against 1,477 coplanar, and the model keeps them apart on purpose." (sentence joined across its line wrap) — matches exact math. The Module 4 docstring (master.py at d77f1ce) agrees: "Coplanar the same burn would be 1.477, so the inclination is worth 253 m/s on arrival and 359 on launch."
- **The consumed constant** `_GEO_COPLANAR_GTO_BURN_M_S = 1_478.0` (master.py L988; duplicated verbatim at modules/mineral_value.py L502) prints "Coplanar that burn would be 1,478, so 358 m/s of this price is the latitude of the launch site" — off by one against both docs and the exact value.
- **spacecost delta_v_segments.csv** GTO->GEO note carries the same pair: "Coplanar it would be 1,478; the 358 m/s difference is what an equatorial launch site is worth" (count==1).

The constant's own comment marks these figures as comparisons and context rather than terms in the price, and `plane_change` feeds only note strings — no pricing chain moves. But three sites print a coplanar figure that does not reproduce under upstream's stated geometry, contradicting MODEL.md and Module 4 within economicspace itself. rc-177 proposes setting it to 1_477 (or deriving from constants) and restating the spacecost note so its coplanar figure reads 1,477 and its equatorial-site difference figure reads 359.

Boundary case recorded for completeness: Module 4's arrival-plane-change figure of 253 m/s recomputes to ~252 from unrounded inputs (arrival combined burn at 23.44 deg = 1729.2; minus coplanar 1477.3) — the same rounded-intermediate family; deliberately not part of the proposal.

Source: curtis_orbital_mechanics_engineering_students (T4, d03), the textbook spacecost's own delta_v_segments header cites for ascent-line values and covering Hohmann transfers with inclined plane change by law of cosines.

## R205 - Sutton & Biblarz registered as RELATIONS-register context (2026-10-19)

economicspace CITATIONS.md section 4 names Sutton and Biblarz (Rocket Propulsion Elements, 9th ed., Wiley 2017) for the rocket equation, exhaust velocity, thrust and jet power relations that campaign/verification_sheet.py prints in its RELATIONS register. No registry row carried it; registered this round as sutton_biblarz_2017_rocket_propulsion_elements_ninth_edition [T4; registered_not_pulled], textbook class alongside curtis_orbital_mechanics_engineering_students (d03) and vallado_fundamentals_astrodynamics_applications (d13). Context-only: no cell pins a figure to it.

## R206 - drift audit of economicspace #150-#153 and provenance correction (2026-10-19)

economicspace moved d77f1ce -> **36bc858** (four commits: verification-worksheet backing part "Backing, row by row", layout fixes, retired-$50-ISRU-rate naming, text pass; no engine or reference-table changes). Audit results:
- The new CITATIONS.md section "Textbook relations the verification worksheet cites" names exactly three works - Sutton & Biblarz 2017 (registered R205), Vallado 4th ed. 2013 (row updated this round, see d13 FINDINGS) and Fowler & Chillemi 1992 in Tedesco et al., PL-TR-92-2049 (hosted since R70). No new registration needed; the inline "(SpaceNews 2024)" and "per Reuters analyst consensus" attributions surfaced by their source-splitter audit are already registered (`spacenews_launch_reporting_2024_2026`, `reuters_2026_gold_analyst_consensus`).
- **Provenance correction (this round):** the R205 Sutton row pinned CITATIONS.md section 4 to @d77f1ce, but both that section and the RELATIONS register of verification_sheet.py arrived with #153 at 36bc858 - `git show d77f1ce:CITATIONS.md` has no Sutton line and its verification_sheet.py contains zero RELATIONS tokens. The sweep had read the parallel session's dirty working tree while HEAD was still d77f1ce. access_status now carries the dated correct pin; registration itself stands unchanged (the source is genuinely cited upstream at HEAD).
- Money-Mass-ematics: their versions.md records that the frozen spacecost 0.5.0 table cited "NASA Money-Mass-ematics 2023" for beneficiation energy and the installed release withdrew it - verified genuine (`spacecost a4cb4fc` "Cut 0.5.1: withdraw two dead citations"). GR never registered or cited it (zero hits in sources.csv); the current beneficiation cell self-declares as an unsourced engineering estimate and its anchor space is already claimed by open rc-097 (doe_2007 mining-energy bandwidth) - no candidate from this seam.
- Open candidates unaffected: MODEL.md tank-fraction text (rc-175), README "~1.2 GB" line (rc-176, root README untouched by the drift; campaign/README.md gained only feature prose) and the GEO coplanar strings (rc-177) all still read as recorded.

**Delta-v backing seam closed (Round 221, do not re-derive):** economicspace campaign/verification_sheet.py DERIVATION_ROWS maps four worked_calculation constants to spacecost delta_v_segments rows and its self-test enforces equality at metre-per-second tolerance. Hand-verified against spacecost@29a7ced: TLI to NRHO insertion 450 = DV_NRHO; NRHO to low lunar orbit 730 plus LLO to lunar surface descent 2,050 = DV_NRHO_TO_LUNAR_SURFACE (constant written as the expression `0.730 + 2.050` — evaluate right-hand sides arithmetically); Mars entry to surface retropropulsion 800 = DV_MARS_RETROPROP; NEA to LEO delivery aerobraked 100 = DV_AEROBRAKE_TRIM. MIL-HDBK-189C (reliability growth) is registered in this repo and cited upstream for its row. Skip until a pin moves or the register gains entries.

**NEA delta-v anchors are dated by design; skip any live-NHATS staleness chase (Round 229):** at spacecost `29a7ced` the LEO-to-NEA rows of delta_v_segments.csv (easy 4500, average 6500, hard 8500 m/s) each carry catalog_date 2026-09-23 and name their sources in-row (Elvis et al. 2011 arXiv:1105.4152 for the ultra-low class ~65 of 6699; Benner compilation peak 6.65 km/s for average). Because the reference population is stamped, drift in the live NHATS service does not stale these rows and no update candidate applies unless upstream re-pulls without re-dating.

## R234 - three identifiers corrected from the page images; 36 spacecost candidates applied (2026-10-21)

The spacecost releases 0.12.1-0.12.4 (merged to main at `7b40d5b`) applied 36 candidates; their rows in `revision_candidates_closed.csv` record what landed. Re-reading the sources before the upstream edits found three identifiers in this domain's registry rows wrong. Each was read from a rendered page image, because the text layer is what misled:

- **bowles_dawson_2004** is NASA **SP-2004-4230** (title page, p2; cataloging data "NASA-SP-2004-4230", p3), by Dawson & Bowles. The registry, INDEX and rc-170 had SP-4176. The hosted file is renamed to match; bytes unchanged.
- **jpl_1968** is JPL **Technical Report 32-1227**, "The Status of Monopropellant Hydrazine Technology", by T. W. Price and D. D. Evans (cover; page iii footer "JPL TECHNICAL REPORT 32-1227"). The cover's text layer reads 32-7227, which the registry, INDEX and rc-111 carried. The hosted file is renamed; bytes unchanged.
- **boddy_1980** is **AFRPL-TR-79-79** (p1 footnote: "Contract F04611-79-C-0007, Final Report, AFRPL-TR-79-79"). The text layer gives 79-7g.

Corrections to candidate proposals, each recorded in its row: rc-101 (Hoffman's ~62 W/kg is array-level, not the system halving), rc-104 (the PPE is "60-kilowatt power generation", IG-21-004 p11), rc-105 (IG-23-010 Table 2 gives $223k-263k per mission watt; no GAO figure or 110 We conversion), rc-159 (the delivery chains fly a typed 465 s, not the RL10's 444 s) and rc-182 ($68,800/kg is not in IG-18-016; p27 gives $63,200 CRS-1 and $71,800 projected CRS-2).

## R283 - rafalskyi_2021_iodine_ep_in_orbit - cost comparison extracted (rc-226 trail) (2026-10-27)

The hosted Methods section carries a propellant cost comparison: total iodine propellant cost approximately US$60 at 99.5% purity, xenon US$1,275 for the same mass, iodine-related hardware below US$200 against xenon hardware about 100 times higher, qualification just under US$4,000 versus about US$9,000 (spans in r283_rafalskyi_propellant_cost_key_numbers.csv). No propellant load mass is printed anywhere in the article body or Methods; the system total mass including propellant is 1.2 kg. The figures are therefore totals of unknown quantity - usable for relative statements only. See d14 FINDINGS and rc-226 for the spacecost-side defect.

## R285 - delta_v_segments.csv notes-to-CITATIONS sweep (spacecost@860bef9) (2026-10-28)

Swept all 34 rows against the self-citation contract. One seam opened as rc-228: row LEO to GTO stores 2,440 m/s attributed to a nonexistent handbook; bisection on two-body perigee burn (mu=398600.4418, R_E=6378) reproduces 2,440 exactly at parking altitude 250.4 km and gives 2,455 at the table-wide 200-km convention - an undocumented orbit-convention difference against the perigee-burn row whose printed constants (v_p(GTO) 10.239 minus v_LEO 7.784) give 2,455; delivery.py consumes only that derived row.
Closure without RC: rows naming Curtis / Taylor et al. 2018 / Elvis et al. 2011 (Benner compilation reaches via Elvis per R209) / DRA 5.0 Fig 4-2 and Table 4-3 / Orloff SP-4029 lunar phase tables / Whitley & Martinez 2016 / Lyons JPL and Long et al. 2007 all resolve to CITATIONS.md section 3 entries with registry rows; composites (NRHO depot, GEO depot, Mars 1-sol depot) are arithmetic on own rows; the two-body rows state their derivation explicitly including honest DRA departures; self-declared estimates follow R282 documented-by-design.
Recorded for a future round: row LEO to hard NEA stores 8,500 m/s with no document named - an upper-decile class figure where the registered hosted ssoBFT table (already cited by the average-NEA note for its 8.88 km/s median) could supply a recomputed decile value; row Asteroid station-keeping cites an OSIRIS-REx budget with no document.

## R287 - hard-NEA upper-decile label contradicted by the cited distribution (2026-10-28)

The row LEO -> hard NEA at spacecost@860bef9 stores a single-point value of 8500 m/s whose payload_note reads, verbatim and count==1 in the committed blob: "Upper-decile NEA (inclined or eccentric); approaches MBA territory." No document is named for either figure - uncited under the self-citation contract standing rule (R282). The only quantitative accessibility distribution in the corpus is ssoBFT, registered and hosted as berthier_2023_ssodnet; the R42 extraction in this domain (r42_sso_bft_delta_v_key_numbers.csv) records NEA perihelion q<1.3 au population n=42,379 with median delta_v 8.877 km/s (p05 5.539, p95 18.334), and MBA p05 = 8.492 km/s. Membership of an upper decile requires a value at or above the 90th percentile, which necessarily exceeds the median - so under the very distribution the sibling LEO -> average NEA row cites verbatim (puts the NEA median at 8.88 km/s), labeling 8,500 m/s as upper-decile is contradicted: it sits below the NEA median. The stored figure instead coincides with MBA p05 to rounding, which is exactly what the second clause of the note describes - an MBA accessibility boundary wearing an NEA decile label.

The exact NEA p90 needed for a re-anchor value was not read: ssoBFT is served only from ssp.imcce.fr, which was unavailable on 2026-10-28. No new source rows were required: berthier_2023_ssodnet is already registered hosted, and the R42 extraction carries the statistics used here.

rc-230: restate the payload_note to what ssoBFT supports, or raise the value toward the recomputed NEA 90th percentile. Text in `revision_candidates.csv`.

## R288 - Asteroid station-keeping row cites a document class that does not exist in the record (2026-10-28)

The row Asteroid station-keeping at spacecost@860bef9 stores dv_m_per_s = 200 with duration_yr = 0.5, and its note reads verbatim and count==1 in the committed blob: "Proximity ops, sample retrieval — OSIRIS-REx station-keeping budget." No document is named - uncited under the self-citation contract standing rule (R282). The attribution was then tested against the institutional record. NTRS full-corpus searches for Bennu station keeping and for OSIRIS-REx delta-V requirements both return zero records (probed 2026-10-28); the twenty-three proximity-operations hits are navigation-performance papers, none of which publishes a station-keeping budget figure. A live sweep of CITATIONS.md confirms no entry covers the leg: OSIRIS-REx appears only for mission cost (PEBD) and Bennu physical properties (Lauretta et al. 2019), while station hits are ISS berthing and geostationary-eclipse context.

The nearest institutional document to what the note gestures at is Antreasian et al., OSIRIS-REx Proximity Operations and Navigation Performance at (101955) Bennu (NTRS 20210025471, conference paper, PUBLIC_USE_PERMITTED), now registered as a witness read via the NTRS machine-extracted fulltext endpoint. It reports momentum-desaturation imparted delta-V that "could be around 0.5 mm/sec" at the three-day cadence and states that from start of Orbital A onward the imparted values remain small - maintenance-class delta-V near Bennu is institutionally recorded per event in millimetres per second, with no published aggregate budget line for station-keeping anywhere in the corpus. That neither confirms nor refutes 200 m/s outright; it shows the cited artifact does not exist.

rc-231 [citation] proposes naming a real document or restating the note as self-declared engineering estimate per documented-by-design convention (the six storage_systems ESTIMATE rows precedent). No value change forced. The duration_yr = 0.5 cell is scenario-parameter material, not an attribution claim - left untouched.

Extracted data: `extracted_data/r288_osirisrex_proxops_dv_key_numbers.csv`.

## R349 - Dawn mission scope and the NSTAR/NEXT distinction (2026-11-03)

`brophy_2011_dawn_ips` publisher abstract (Space Science Reviews 163,
p251) gives a mission IPS budget of nearly 11 km/s and 1.2e7 N s total
impulse, excluding the Mars gravity assist. `garner_rayman_2013_jpc_cruise_yr1`
author abstract (NTRS 20150008021) reports approximately 31,000 operating
hours, 300 kg xenon and 8.3 km/s accumulated through the first year of
cruise to Ceres, with approximately 11 km/s the whole-mission plan.
Neither full article was read; their full-paper requests remain queued.

`nextc_ppu_2020` p1 and Table 2 p4 distinguish Dawn NSTAR from its NEXT
successor. This corrects the NEXT-as-flown description in this registry's
brophy_2011_dawn_ips row and INDEX. At spacecost
860bef9902aa67fec705875cd52fdb8e6def159f, propellants.py L851-868 separately
backs 3,000 s xenon Isp with `nextc_protoflight_2021` and a Hall comparison;
the Dawn distinction is not misidentified there. The 1.5 low-thrust penalty
at L37-54 is a heuristic; the abstract's aggregate mission figures have no
like-for-like impulsive baseline from which to calibrate that ratio.

Verdict: registry classification/scope correction and bounded abstract
extraction; no new upstream value candidate follows from these figures.
`extracted_data/r349_dawn_nstar_mission_scope.csv`.

## R354 - Point-target transfers need a surface-escape validity bound (2026-11-03)

`economicspace_target_surface_escape_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0 and spacecost
860bef9902aa67fec705875cd52fdb8e6def159f. calc.py L2817-2835 matches
heliocentric velocity at the target and reverses that burn for departure.
L3314-3334 passes a/e/i alone and retains a 300 m/s return floor.
MODEL.md L22-34 places mining between rendezvous and return. The source
environment row for Ceres explicitly notes "leaving costs real propellant"
(environments.py L353-354); its adopted mass, radius and spin are
9.3835e20 kg, 469,730 m and 9.074 h. Its escape helper (L116-123) uses
sqrt(2GM/R) and warns that rotation changes departure cost.

Twenty-two constructed raw, direct-entry earth_surface fixtures run the
original full evaluate_asteroid twice each: 44 consumers using current
reference-only Stage 2, source vehicle/chemical-propellant pairs and the
original geometry/architecture functions. N=1; refinery, ISRU, boil-off and
launch windows are off. The physical-scale comparison transports the source
Ceres mass/radius/spin to explicitly synthetic near-Earth circular coplanar
orbits and hypothetical magnetite composition. It is not an actual Ceres
mission or an observed catalogue body.

For a=1.01 AU, e=i=0 at that physical scale, escape speed is
516.3879981392188 m/s. Even maximal prograde equatorial rotation supplies
only 90.34973655932295 m/s. Granting the entire 300 m/s return budget
instantaneously at the surface, with no gravity/steering loss or later-burn
reserve, gives at most 390.34973655932293 m/s and specific energy
-57,141.82389514848 J/kg. At least 426.03826157989585 m/s impulse is
needed merely to reach zero two-body energy under that favorable rotation.
The settled source fuel/dry/cargo/TPS/tank book independently reconstructs
300.00000000000006 m/s by the rocket equation. Nevertheless, the source
returns 7,866.696505173187 kg cargo, 1,036.2367272123474 kg return fuel,
17,400 kg launch and 2,011,640,770.4501808 USD total cost.

Fourteen accepted books fail this optimistic spherical two-body
surface-launch condition. The failures persist across orbital, size,
density, spin, vehicle, propellant and rig sensitivities. Seven returned
cases are not detected by the weak energy bound; that does not establish
their trajectory feasibility. One farther case is an original solver
refusal. All returned source books pass current mass/resource/throughput/
time/return-volume checks and are unprofitable. Original repeated books and
observers match native types/values/float.hex fingerprints; independent
50-digit Decimal energy agrees. No numerical repair is performed.

Verdict: `rc-289`, close local surface departure/material lifting or state
and enforce the point-target approximation's regime. An orbiting/hovering
capsule requires a material-transfer architecture; the observed surface
failure assumes no unmodelled external launch assistance. Rotation/site and
required excess velocity matter, so a blanket additive escape-speed term
is not established. This is not an n-body trajectory, a corrected optimum,
an actual Ceres result, or a population/ranking measurement. Twenty-four
runtime/method blobs match pinned metadata; four live main comparisons are
identical. `extracted_data/r354_target_surface_escape.csv` retains full
inputs/books, energy observers and the reproduction harness.


## R464 — Current surface-escape necessary-condition gate

At economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, `CalcConfig.gate_surface_escape` defaults to `False` (modules/calc.py:721), and the module consumer constructs `CONFIG = CalcConfig()` without an override (line 1468). When enabled, `surface_escape_shortfall_m_s` computes spherical escape speed from `estimated_mass_kg` and mean radius (`diameter_km`), subtracts equatorial rotation from the measured period (or the configured default when missing), and returns zero when mass or diameter is unavailable (lines 2362-2386). `_asteroid_dv_options` then retains only offers with `dv_ret_m_s >= shortfall` (lines 3504-3506). The code comment calls this a necessary test and says passing is not a surface-launch design. The option can screen offers that fail this lower bound, but it does not add a local departure/arrival trajectory, site/vector geometry, gravity/steering losses, hover/orbit transfer, or reserve for later burns. It is default-off, so `rc-289` remains open for the default path and complete transport architecture. Extracted: `extracted_data/r464_current_surface_escape_gate.csv`.


## R488 — NHATS trajectory time varies with the ΔV objective (2026-11-09)

The existing registry source `jpl_nhats_nea_dv_oracle` links the NASA/JPL NHATS API, which reports separate minimum-ΔV and minimum-duration trajectories for 2000 SG344. Its object record, computed 2021-04-19, gives the minimum-ΔV solution as 3.549 km/s over 370 days and the minimum-duration solution as 11.402 km/s over 34 days; both include an 8-day stay. NHATS documentation defines total duration as outbound flight, stay and inbound flight, and its total ΔV as a round-trip mission quantity.

The economicspace `asteroid_mission_duration_yr` function instead applies a fixed 0.00023 years per m/s separately to outbound and return ΔV, with a 0.5-year floor on each leg; its calibration comment lists four duration anchors whose `duration_yr` cells have no cited source. The NHATS pair confirms that time depends on the selected trajectory objective and launch opportunity, but it is one historical human-mission example with a different ΔV boundary. It cannot directly replace the model’s one-way proxy. `rc-354` asks for a documented trajectory basis or explicit scenario-prior treatment, and for duration-dependent boiloff and schedule effects to use a consistent mission clock; no coefficient or anchor is replaced. Extracted: `extracted_data/r488_nhats_delta_v_duration_trade.csv`.

R490 — The current economicspace `modules/calc.py` sets `R_LEO_KM = 6_378.14 + 200.0`, the same radius used by the verification worksheet’s `r_LEO` input. IERS Conventions (2010), Table 1.1, gives “6378136.6 m” as Earth’s equatorial radius; NASA’s SLS capability table defines LEO as a “typical 200 km circular orbit at 28.5 degrees inclination.” The Earth-radius value rounds to 6,378.14 km, and the NASA definition supports the 200 km reference-orbit component. The citations establish a stated LEO scenario, not a uniquely required orbit for every mission. `rc-356` records the missing in-code attribution; no value change inferred. Extracted: `extracted_data/r490_leo_radius_provenance.csv`.

R491 — The current spacecost `reference/delta_v_segments.csv` row `LEO → cislunar NRHO depot` stores 3,600 m/s and describes it only as “TLI + NRHO insertion.” NASA-CR-195527, printed p. 3, §2.3.1 and Table 2.1, gives a 3,140 m/s TLI burn from a 185 km, 33° parking orbit for a four-day lunar transfer. Benson, Asher & Reese (2025), slide 5, give 400–450 m/s “from TLI to NRHO” for fast Gateway transfers. Adding these values gives 3,540–3,590 m/s, near the stored rounded point, but the studies use different trajectory and mission assumptions. They provide component context, not a trajectory-matched replacement or precision validation of the current ±2% band. `rc-357` records the missing component provenance and scope; retain the value pending a matched transfer basis. Extracted: `extracted_data/r491_cislunar_nrho_transfer_dv_components.csv`.

## R495 - Low-thrust delta-v penalty source basis

- **woodcock_2000_in_space_transportation_propulsion_architecture_assessment** (printed p. 7, §5.2.5, Fig. 5.2-8): NASA reports high-thrust Earth-orbit escape at “about 3.2 km/sec” and typical low-thrust numerical results “between 5 and 6 km/sec”; the immediately stated infinite-low-thrust limit is about 7.5 km/sec. The typical Earth-escape ratio is 1.56–1.88. Current `spacecost` applies `dv_penalty_factor=1.5` across electric propellants; the economicspace verification worksheet marks the Krypton (Hall) penalty input as needing backing. These Earth-escape results support the scale only and do not establish a single multiplier for heliocentric or other mission legs. rc-361 records the source and scope gap. `extracted_data/r495_nasa_low_thrust_escape_dv_comparison.csv`.

## R497 — Starlink krypton-use attribution (2026-11-09)

- **spacex_2023_starlink_progress_report_thruster_propellants**: SpaceX states “On the first generation, the satellites used krypton gas” and that second-generation satellites switched “to argon gas” (Technology → Thrusters, printed p. 48). The next sentence reports 2.4× thrust and a 1.5× specific-impulse increase for the second-generation engine. This directly supports first-generation use and the later gas switch; it does not state that every v1.0 thruster used krypton, explain the switch as a xenon supply constraint, or give absolute Isp, efficiency, or specific-mass values. Extracted: extracted_data/r497_spacex_starlink_thruster_propellants.csv.

## R498 — Krypton Hall device-performance comparators (2026-11-09)

- **nasa_s3vi_2026_small_spacecraft_inspace_propulsion**: NASA’s current Small Spacecraft Systems Virtual Institute chapter lists Astra ASE Krypton at 18 mN, 1,300 s, 1.0 kg; ExoTerra Halo Krypton at 12 mN, 900 s, 0.83 kg; and Halo12 Krypton at 55 mN, 1,575 s, 3.4 kg (Table 4-10). Derived listed mass/thrust is 55.6, 69.2 and 61.8 kg/N, respectively. The upstream generic Krypton (Hall) row uses 2,000 s, 0.45 efficiency and 35 kg/N; the published small-spacecraft comparators place 2,000 s above the listed Kr points and 35 kg/N below the listed mass/thrust values. NASA limits Table 4-1’s Hall range (200–1,920 s) to small-spacecraft devices and says the chapter primarily compiles manufacturer data, which should not be assumed independently verified. These are class/scale comparators, not like-for-like asteroid mission replacements; the chapter gives no numeric efficiency for these Kr devices. Extracted: extracted_data/r498_nasa_kr_hall_thruster_comparators.csv.


## R506 — Proximity-operations duration comparator for the stay floor (2026-11-09)

At economicspace `modules/calc.py` `MiningConfig.station_keeping_floor_yr` is 0.25 years; the comment includes approach, characterization, proximity operations and departure phasing, but names no source. Antreasian et al. report that OSIRIS-REx close-proximity operations at Bennu began in December 2018 and ended in May 2021; the abstract describes “over 2 years” of navigation refinement (NASA NTRS 20210025471, abstract and §I, p. 1). The paper describes navigation, site-selection and sample-acquisition campaigns (Figure 1 and §I, p. 1). This sample-return mission is a duration comparator, not a mining stay and not evidence for a universal quarter-year minimum. `rc-372` records the scope gap; no numeric change is inferred. Extracted: `extracted_data/r506_osiris_rex_proximity_operations_duration.csv`.
## R521 — Uncited asteroid-transfer ΔV floors (2026-11-10)

The current economicspace `modules/calc.py` `asteroid_dv_options_km_s` path floors the outbound transfer estimate at 3,000 m/s and the selected return-leg estimate at 300 m/s before applying the configured 20,000 m/s ceiling. The economicspace verification sheet marks both constants as needing backing; the current code comment gives no source or physical interpretation for them.

The registered source `jpl_nhats_nea_dv_oracle` reports NASA/JPL NHATS results for complete human round-trip missions. Its 2000 SG344 record gives a minimum-ΔV total of 3.549 km/s over 370 days (including an 8-day stay). The API labels this a total mission quantity and its trajectory records separate Earth departure, asteroid arrival/departure and Earth return terms; it does not establish either of economicspace’s universal per-leg floors. This is context for the missing attribution, not a trajectory-matched basis for either value. The return floor’s surface-launch limitation is separately covered by `rc-289`. `rc-387` records the citation gap; no value change is inferred. Extracted: `extracted_data/r521_economicspace_delta_v_floor_comparator.csv`.



## R546 — Total mission-duration cutoff comparator

Cohen et al.’s NASA RAP Phase I report requires a spacecraft “capable of operating for mission durations lasting between one and five years” (§5.1, report p. 65); it does not specify the asteroid stay or a maximum feasible mining mission. The NASA/JPL NHATS crewed-NEA filter uses a 450-day round-trip search constraint, a different mission class. At economicspace main `db863923f7793676e9a78583b97462ddd614f29e`, `CalcConfig.max_mission_duration_yr` remains 25.0; its comment gives no basis for the 25-year cutoff. Neither comparator establishes a universal limit. **rc-412** records the citation and scope gap; no value change is inferred. Existing extracts: `19_asteroid_excavation_beneficiation/extracted_data/r505_rap_mission_duration_requirement.csv`; `03_dv_propulsion/extracted_data/r488_nhats_delta_v_duration_trade.csv`.
