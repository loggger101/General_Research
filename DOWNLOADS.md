# What still has to be downloaded

Sources this machine cannot fetch, with the route to fetch each by hand. Every other `registered_not_pulled` row is
also queued (`python tools/validate.py` counts them); each row's `access_status` records the routes already tried.
Remove an item when it is done.

## How to use this list

1. Save files to `C:\Users\Loggg\OneDrive\Documents\GitHub\General_Research_incoming\`, outside the repo (it is public
   and most of these may not be redistributed). Never into `<domain>/full_texts/`.
2. Name each file `<id>.pdf` (or `.html`/`.png` where noted), so the next round matches it to its row.
3. Then ask Claude to "extract the files in General_Research_incoming": each is read in full into
   `<domain>/extracted_data/` with page locations.
4. "May host" means the publisher reports a licence that would allow it; the licence printed on the file decides
   (AGENTS.md), and Claude checks it before proposing to host.

## A. Free or open copy behind a bot wall (open in a normal browser)

- [ ] **harris_dabramo_2021** (d01) - https://doi.org/10.1016/j.icarus.2021.114452 - free to read; extract only.
- [ ] **cannon2023** (d02) - https://www.sciencedirect.com/science/article/pii/S0032063322001945/pdf - CC BY-NC-ND; by owner decision extract only, never host.
- [ ] **just_2019** (d19) - https://www.sciencedirect.com/science/article/pii/S003206331930162X/pdf - CC BY; may host. Technique-resolved excavation energies.
- [ ] **tirila_2023** (d03) - https://eprints.soton.ac.uk/483809/2/1_s2.0_S0094576523003983_main.pdf or https://doi.org/10.1016/j.actaastro.2023.07.047 - CC BY per OpenAlex; the Soton file is the submitted version.
- [ ] **farnocchia_2024** (d02) - https://doi.org/10.3847/1538-3881/ad50ca - CC BY; may host.
- [ ] **mandler_elkins_tanton_2013** (d02) - https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/maps.12135 - CC BY; may host.
- [ ] **pourpoint_2012_alice_feasibility** (d03) - https://downloads.hindawi.com/journals/ijae/2012/874076.pdf (or the Purdue docs.lib copy) - CC BY; may host.
- [ ] **demeo_2009_bus_taxonomy_near_ir** (d01) - https://hal.science/hal-00545286 - extract only.
- [ ] **ryugu_soluble_organics_2023** (d02) - https://hal.science/hal-04208565/document - extract only.
- [ ] **ryugu_macromolecular_om_2023** (d02) - https://cnrs.hal.science/hal-04034418/document - extract only.
- [ ] **masiero_2021_albedo_uncertainties_thermal_modeling** (d01) - https://doi.org/10.3847/PSJ/abda4d - read from arXiv; publisher version CC BY, may host.
- [ ] **masiero_2021_neowise_reactivation_years_6_7** (d01) - https://doi.org/10.3847/PSJ/ac15fb - as above.
- [ ] **myhrvold_2022_four_band_wise_asteroids** (d01) - https://doi.org/10.3847/PSJ/ac3232 - as above.
- [ ] **murray_2023_neural_network_main_belt_albedos** (d01) - https://doi.org/10.3847/PSJ/acd381 - as above.
- [ ] **wong_2024_jwst_lucy_trojans_oh_organics_co2** (d02) - https://doi.org/10.3847/PSJ/ad2fc3 - as above.
- [ ] **de_kleer_2026_jwst_spinel_rich_l_type_mineralogy** (d02) - https://doi.org/10.3847/PSJ/ae374e - abstract only so far; CC BY, may host.
- [ ] **mahlke_carry_denneau_2021_atlas_phase_curves** (d01) - https://doi.org/10.1016/j.icarus.2020.114094 - read from arXiv; Icarus version CC BY-NC-ND, may host under it.
- [ ] **mahlke_2022_phd_thesis_asteroid_taxonomy** (d02) - https://theses.hal.science/tel-03850762/ (file 2022COAZ4051.pdf) - extract only.
- [ ] **ferrais_2022_kalliope_tiny_mercury** (d01) - https://www.aanda.org/articles/aa/pdf/2022/06/aa43200-22.pdf or oro.open.ac.uk/83943 - CC BY; may host.
- [ ] **pentikainen_2026_gaia_dr3_asteroid_characterization** (d01) - https://doi.org/10.1051/0004-6361/202556127 - CC BY; may host.
- [ ] **carvano_2010_sdss_taxonomy_main_belt** (d01) - https://www.aanda.org/articles/aa/pdf/2010/02/aa13322-09.pdf - free access; extract only.
- [ ] **macke_2011_carbonaceous_chondrite_density_porosity** (d01) - https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1945-5100.2011.01298.x - CC BY per OpenAlex; host only if the PDF says so.
- [ ] **kopp_lean_2011_total_solar_irradiance** (d12) - https://doi.org/10.1029/2010GL045777 or https://apps.dtic.mil/sti/pdfs/ADA535690.pdf - extract only.
- [ ] **kargel_1994_metalliferous_asteroids_precious_metals** (d02) - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/94JE02141 - extract only.
- [ ] **nichiporuk_brown_1965_pt_pd_iron_meteorites** (d02) - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/JZ070i002p00459 - extract only.
- [ ] **scott_wasson_1975_classification_properties_iron_meteorites** (d02) - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/RG013i004p00527 - extract only.
- [ ] **keil_1968_mineralogical_chemical_enstatite_chondrites** (d02) - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/JB073i022p06945 - extract only.
- [ ] **kessler_cour_palais_1978_collision_frequency_debris_belt** (d27) - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/JA083iA06P02637 - extract only.
- [ ] **pearson_2006_carbon_nitrogen_carbonaceous_chondrites** (d02) - https://journals.uair.arizona.edu/index.php/maps/article/download/15367/15355 - extract only.
- [ ] **dunn_cressey_2010_xrd_modal_mineral_abundances_ordinary_chondrites** (d02) - https://repository.si.edu/handle/10088/20464 - extract only.
- [ ] **sunshine_connolly_2008_ancient_asteroids_refractory_inclusions** (d02) - https://repository.si.edu/items/e39dedbe-b83e-4add-98c6-9d0d9ac7fafd/full - find the file link in a browser; extract only.
- [ ] **consolmagno_2008_meteorite_density_porosity** (d01) - https://stars.library.ucf.edu/facultybib2000/234 - find the full-text link; extract only.
- [ ] **fujiwara_2006_itokawa_rubble_pile** (d01) - https://ieeemilestones.ethw.org/w/images/8/82/Reference_E_3_2006Fujiwara_Rubble-Pile_Asteroid_Itokawa_Science.pdf - extract only.
- [ ] **king_schofield_2015_ci_modal_mineralogy_xrd** (d02) - https://oro.open.ac.uk/69573/1/69573.pdf - CC BY per the record; may host.
- [ ] **sinibaldi_haldemann_2026_planetary_protection_is_expensive_esa_perspective** (d18) - https://oro.open.ac.uk/108579 - extract only unless the file grants reuse.
- [ ] **dorrington_olsen_2026_parametric_economic_modelling_asteroid_mining_architectures** (d22) - https://doi.org/10.1016/j.actaastro.2025.11.006 (PII S0094576525007659) - CC BY; may host.
- [ ] **iyer_kelly_2022_lci_critical_materials_ni_cu_ti_ree** (d29) - https://www.osti.gov/servlets/purl/1905473 or https://publications.anl.gov/anlpubs/2022/12/178670.pdf - US government report.
- [ ] **gao_2012_commercial_space_launches_faa_liability_risk_assessment** (d17) - https://www.gao.gov/assets/600/593106.pdf - public domain; may host.
- [ ] **gao_2017_commercial_space_launch_insurance_faa_calculation_weakness** (d17) - https://www.gao.gov/assets/690/683915.pdf - public domain; may host.
- [ ] **gao_2017_pu238_rps_production_planning** (d05) - https://www.gao.gov/assets/gao-17-673.pdf - public domain; may host.
- [ ] **douglas_sm47274_saturn_v_payload_planners_guide_nov1965** (d04) - archive.org item `SaturnVPayloadPlannersGuide` (its file hosts do not resolve from this machine) - configuration-A volume "about 3,230 cubic feet".
- [ ] **isro_vssc_gslv_mkiii_vehicle_specifications_plf_volume** (d04) - isro.gov.in GSLV MkIII page - save the spec table as `.png` or `.pdf` (PLF usable volume 110 m3).
- [ ] **reaction_engines_skylon_users_manual_rev1** (d04) - reactionengines.co.uk - Fig 13 payload envelope.

## B. Library access or purchase

- [ ] **taylor2018** (d03) - https://doi.org/10.1016/j.actaastro.2018.02.014 - closed, no preprint; high value for the main-belt delta-v rows.
- [ ] **schoenman_1992** (d03) - AIAA-92-3800 from arc.aiaa.org; optional.
- [ ] **ueda_et_al_2013_methane_fueled_engine_altitude_hot_fire_jpc** (d10) - DOI 10.2514/6.2013-4056 - altitude thrust/Isp table.
- [ ] **judd_et_al_2006_lox_methane_combustion_performance_stability_durability** (d10) - DOI 10.2514/6.2006-1533.
- [ ] **engelen_souverein_twigt_deimos_methane_oxygen_engine_test_results_jbis** (d10) - JBIS 62:211-218, ~GBP 5 at https://www.bis-space.com/shop/product/deimos-methane-oxygen-rocket-engine-test-results/
- [ ] **smith_stanley_2021_experimental_investigation_rotating_detonation_rocket_engines** (d10) - https://doi.org/10.2514/1.B37959
- [ ] **bus_binzel_2002_smass2_feature_based_taxonomy** (d01) - https://doi.org/10.1006/icar.2002.6856
- [ ] **lebofsky_et_al_1990_low_albedo_3um_photometry** (d02) - https://doi.org/10.1016/0019-1035(90)90003-R - not yet read at all.
- [ ] **wang_2026_nea_albedo_from_orbital_elements** (d01) - https://doi.org/10.1088/1674-4527/ae37ed
- [ ] **gounelle_zolensky_2001_mineralogy_of_tagish_lake** (d02) - Zolensky et al., MAPS 37:737-761, DOI 10.1111/j.1945-5100.2002.tb00852.x - the modal mineralogy rc-085 needs.
- [ ] **knox_1970_yield_strength_meteoritic_iron** (d29) - DOI 10.1111/j.1945-5100.1970.tb00391.x
- [ ] **xie_bennett_dempster_2021_nea_mining_target_evaluation** (d08) - https://doi.org/10.1016/j.actaastro.2021.01.011 - its target tables are the d08 comparison.
- [ ] **bennett_xie_dempster_2022_moon_neas_cislunar_propellant** (d15) - DOI 10.1016/j.actaastro.2021.10.038
- [ ] **entrena_2017_emerging_cislunar_economy_framework** (d15) - DOI 10.1016/j.actaastro.2017.10.005
- [ ] **keravala_tietz_stone_2013_shackleton_propellant_depot_architecture** (d15) - DOI 10.1089/space.2013.0014
- [ ] **kutter_sowers_2016_cislunar1000_self_sustaining_space_economy** (d15) - DOI 10.2514/6.2016-5491
- [ ] **tang_et_al_2023_asteroid_rock_mechanical_properties** (d19) - https://doi.org/10.1016/j.enggeo.2023.107154 - not yet read.
- [ ] **liu_et_al_2026_asteroid_laser_mining_cryogenic_vacuum** (d19) - https://doi.org/10.1016/j.cherd.2026.08.007 - not yet read.
- [ ] **broslav_2025_optical_mining_carbonaceous_chondrite_simulants** (d19) - Colorado School of Mines repository item abed9ab3-8bf3-4cac-aafa-b81d379ee4d2 (files need a login).
- [ ] **paulson_balchanos_mavris_2026_isru_economic_environmental_tradeoffs** (d22) - https://doi.org/10.2514/6.2026-2788
- [ ] **hayhurst_2016_historical_mass_power_schedule_cost_growth_nasa_spacecraft** (d21) - IEEE Aerospace 2016, DOI 10.1109/aero.2016.7500553 (NTRS has no file).
- [ ] **brophy_2011_dawn_ips** (d03) - DOI 10.1007/s11214-011-9848-y
- [ ] **rayman_mase_2014_dawn_cruise_acta** (d03) - DOI 10.1016/j.actaastro.2014.06.042
- [ ] **garner_rayman_2013_jpc_cruise_yr1**, **garner_rayman_2015_jpc_orbit_ops**, **garner_rayman_2016_jpc_lamo**, **garner_rayman_2018_jpc_final_orb** (d03) - AIAA JPC papers 6.2013-4112, 6.2015-3717, 6.2016-4539, 6.2018-4641.
- [ ] **calt_lm2c_users_manual_issue_1999**, **cgwic_lm3a_series_launch_vehicle_users_manual_issue_2011**, **cgwic_lm2d_technical_data_fairing_dimensions** (d04) - customer-only Chinese manuals; fairing envelope figures.
- [ ] **galactic_energy_ceres1_launch_vehicle_user_manual_2023**, **galactic_energy_pallas1_user_manual_2023** (d04) - request through the company; fairing envelopes.

## C. Locate first (the upstream citation gives no URL)

- [ ] **orienspace_gravity1_fairing_100m3_tencent_news_2023** (d04) - Tencent News 2023-11-22; save the article as `.html`.
- [ ] **sohu_lm5_standard_fairing_calt_design_office_2024** (d04) - Sohu 2024-05-06 ("长征五号" "整流罩"); `.html`.
- [ ] **tencent_news_lm10b_short_fairing_jul2026** (d04) - Tencent News 2026-07-13 ("长征十号" "整流罩"); `.html`.

## D. Live services and pages that refuse this machine (nothing to save; retry later)

dla_energy_aerospace_standard_prices_fy2020, aqua_calc_lox_bulk_price, lme_official_reference_prices,
cme_comex_nymex_futures, neodys_orbit_covariance_service, jaxa_h3_launch_vehicle, watanabe_2019_hayabusa2_ryugu_spinning_top,
macke_2010_enstatite_chondrite_density_porosity, sercel_2018_time_dependent_outgassing_model_bulk_heating,
nasa_instrument_cost_model_nicm, pearson_1979_anchored_lunar_satellites.
