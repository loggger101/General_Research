# Domain 10 — Launch vehicle & engine hardware / propellant performance (R64)

Backings: engine-level measured or tested ground truth for spacecost `reference/launch_vehicles.csv` and `reference/propellants.csv`.

## R64 - Domain opened with three NTRS engine documents, hosted

- **baumeister_2015_rl10_atlas_to_shuttle_centaur** (NASA/TM—2015-218736) p9: "Each Centaur RL10A-3-3A engine at space vacuum conditions produced a rated thrust of 16,500 lb and a 444.4±2.5 sec nominal specific impulse at a nominal propellant oxidizer to fuel mixture ratio of 5.0:1." (the ± is U+F0B1 in the text layer). The hydrolox row's "Vac Isp 452 s per RS-25 / RL-10 datasheets" is +1.71% above this measurement: a family-level figure, consistency anchor. 16,500 lb = 73.4 kN. p18 RL10A-3-3B changes: "Reduce thrust level, 15,000 lb instead of 16,500 lb"; "Operate at a higher nominal mixture ratio (O/F) of 6.0:1 instead of 5.0:1".
- **vetcha_2018_rs25_adaptation_hotfire_sls** p2: RS-25 flew "successfully on all 135 Space Shuttle flights"; on SLS it starts at sea level and shuts down "after approximately 500 seconds of operation at a primary thrust level of 512,000 pounds (109 percent of rated thrust)"; the plan "called for a minimum of seven starts and 3500 seconds of hot-fire operation on one development engine"; "almost 9,000 seconds of hot-fire test time were accumulated". Supports the SLS Block 1 row.
- **ballard_2017_rs25_nextgen_sls** p2: "the system was designed to be reusable, providing a certified service life of 55 starts and 27,000 seconds": SLS is an expendable vehicle with reusable-class engines.

None gives an RS-25 vacuum Isp in text (but see R70), and NTRS "Raptor"/"BE-4" hits were false positives, so the methalox row's "SpaceX Raptor public data" stays secondary-sourced. `extracted_data/r64_engine_performance_key_numbers.csv`.

## R65 - NERVA 1968 status documents, hosted

- **nerva_development_status_1968** (NTRS 19700004945) p4: the engine "delivers approximately 75,000 lb of thrust at a specific impulse of 825 sec/lbm" (printed '825 1bf-sec/lbm'); "The reactor produces 1575 Mw of power"; ~91 lb/sec LH2 to the nozzle plenum. p6: "25 starts" across KIWI B4D, B4E, NRX-A2, -A3, Phoebus 1A, NRX/EST (10), NRX-A5, Phoebus 1B, NRX-A6 (the breakdown sums to 25). p12: demonstrations "were at specific impulses when corrected for vacuun conditions of about 800 sec".
- **nerva_program_status_1968** (NTRS 19680011933) p12: the upgraded model "will permit a vacuum thrust of 75,000 lbs. and a vacuum specific impulse of approximately 825 seconds" at 1560 MW / 4500 R (technology baseline 1100 MW / 4090 R).

Both give ~825 s as a rating or plan and ~800 s as demonstrated; XE tests were still "forthcoming" (see the 2026-09-26 correction). The row's `isp_vac_s = 900` is the DRACO target. ETS-1 (NTRS 19670020629, image-only) and the NTP ground-test history (NTRS 20140008771, abstract only) were not usable.

## R66 - BE-4 / Raptor NTRS sweep: none exist

Every NTRS hit for BE-4 (13), Raptor, Blue Origin (48), Commercial Propulsion Development (68) and methalox (2) is unrelated (legacy designations, a "Raptor-Like Codes" paper, KSC ISRU); Blue Origin's only record is a descent/landing report (20210026314). Neither engine has a NASA test campaign.

## Maintenance (2026-09-26) - R65 verdict reversed (rc-042)

R65 read the NERVA documents as backing the note "NERVA's NRX/XE ran on a test stand at 825 s in 1968". They do not: 825 s is the rated or planned figure, ~800 s (vacuum-corrected) was demonstrated by early 1968, and the XE-1/XE-2 series was "forthcoming" (program status p12; development status p11-12). **rc-042** (wording) records it; the registry rows and `r64_engine_performance_key_numbers.csv` say so.

## R70 - Full extraction (2026-09-27)

Files in `extracted_data/`: `r70_ballard_2017_rs25_nextgen_sls.csv` (17), `r70_baumeister_2015_rl10_atlas_to_shuttle_centaur.csv` (14), `r70_baumeister_2015_table1_rl10_performance_upgrades.csv` (5), `r70_baumeister_2015_table3_centaur_vehicle_engine_characteristics.csv` (3), `r70_nerva_development_status_1968.csv` (20), `r70_nerva_program_status_1968.csv` (8), `r70_nerva_program_status_1968_fig6_nrx_reactor_test_comparisons.csv` (5), `r70_vetcha_2018_rs25_adaptation_hotfire_sls.csv` (15).

- RL10: Table 1 upgrades RL10A-1 to A-3-3A, 424 -> 446.4 s, 300 -> 465 psia, 40:1 -> 61:1; thrust / flow gives 443.5 and 438.6 s at O/F 5.0 and 6.0. Kept as printed: Table 1's 446.4 s vs 444.4 +/- 2.5 s in the text and Table 3.
- RS-25 (Vetcha p3): rated vacuum thrust 470,000 +/- 6,000 lbf, minimum vacuum Isp 451.3 s at 109%, mass 8,280 lbm (3,756 kg), 94 x 167 in, 65-109% throttle, life 6 starts / 2,500 s. The Fig. 9 bars sum to ~7,900 s vs "almost 9,000 s".
- Ballard: restart RS-25 cost-reduction targets: MCC -60%; injector, preburners, hot-gas manifold, nozzle -30%; turbopumps -25%; low-pressure pumps and valves -20%; overall one-third.
- NERVA Figure 6: endurance x power reproduces integrated power for all five reactors (NRX-A6 62.9 min at 1,150 MW = 4.3e6 MW-s); 75,000 / 91 lb/s = 824 s. Kept as printed: the starts table totals 24 vs 25 in the text (NRX-A6 1 vs 2); NRX-A2 0.8 min at full power vs "about two minutes".

## R96 - Methalox test anchors; no peer-reviewed Raptor/BE-4 report exists (2026-10-01)

Crossref title search ('Raptor' 20 hits, all unrelated; 'BE-4 engine' 0; JPP methane queries 0) confirms no indexed peer-reviewed report on either engine: their public figures are grey by construction. Registered (`registered_not_pulled`):

| source | what it carries |
|---|---|
| ueda_et_al_2013_methane_fueled_engine_altitude_hot_fire_jpc (AIAA JPC) | altitude-simulated LOX/methane hot fire |
| judd_et_al_2006_lox_methane_combustion_performance_stability_durability (AIAA) | combustion, stability and durability of a LOX/methane engine |
| engelen_souverein_twigt_deimos_methane_oxygen_engine_test_results_jbis (JBIS 62:211-218) | DEIMOS CH4/LOX campaign: design point 1800 N / 287 s at 40 bar; provisional tests averaged 3.8% of design thrust; reusability assessment |

The methalox `isp_vac_s = 380` stays as is.

## R114 - Methalox and rotating-detonation sources (2026-10-04; +9)

NASA MSFC ECI RDRE report: best hot fire ~5,300 lbf at ~740 psia, Isp 246 s (p32). ISECG review: ASI MIRA 100 kN LOX/LCH4 expander (11+ tests, 600+ s, p7); IHI/JAXA 30 kN at ~350 s (p11). JAXA/IHI injectors reached the equivalent of 370 s at 30 kN (EUCASS 2019). Tan 2024: LOX/kerosene theoretical Isp ~3% below LOX/methane, LOX/LH2 density Isp ~10% below. Abstracts: Smith & Stanley 2021 (RDRE at 68-85% of ideal deflagration Isp), Hemming 2024 (RDE meta-analysis), Meyer 2012. Teasley 2025 and Morehead 2017 give hardware scale only. None sets the methalox row. `extracted_data/r114_gr_links_key_numbers.csv`.

## R119 - meyer_2012_lox_lch4_reaction_control_thruster_altitude_combustion_stand hosted (2026-10-05)

`meyer_2012_lox_lch4_reaction_control_thruster_altitude_combustion_stand` (NASA/TM-2012-217643) hosted as full_texts/meyer_arrington_kleinhenz_marshall_2012_lox_lch4_rcs_altitude_combustion_stand_ntrs20120009210.pdf: Glenn's Altitude Combustion Stand (activated 2009, up to 2000 lbf / 8.9 kN) ran the LOX/LCH4 RCS programme 2009-2010 and "delivered up to 24 hot fire tests in a single test day". Context only.
