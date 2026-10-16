# What still has to be downloaded

The sources below still need a file fetched by hand: through a browser where a publisher blocks this machine, through library access, or as a publisher copy that could then be hosted. What has already been read, and how, is recorded in each source's `access_status` in its domain's `sources_domain.csv`; this file lists only what is left. Remove an item when it is done (Round 152 removed the finished ones; earlier versions are in git history). The rest of the queue is every registry row whose `access_status` starts with `registered_not_pulled`; `python tools/validate.py` counts them in its summary line.

## How to use this list

1. **Save everything to a folder outside the repo**: `C:\Users\Loggg\OneDrive\Documents\GitHub\General_Research_incoming\` (a sibling of this repo). The repo is public and most of these files may not be redistributed. Do not put them in `<domain>/full_texts/`.
2. **Name each file exactly as in its "Save as" line** (the registry id plus extension). That is how the next extraction round matches a file to its source.
3. When a batch is in the folder, tell Claude: *"extract the files in General_Research_incoming"*. Each file will be read in full into `<domain>/extracted_data/`, with page locations, the same way as Round 70.
4. **Hosting is a separate decision.** "May host" below means the licence the publisher or OpenAlex reports would allow it, but the licence printed on the PDF itself decides (AGENTS.md). Claude checks the PDF before proposing to host anything.

Counts in brackets are the rows the repo already has from that source.

---

## A. No download needed: restore from git history (20 PDFs)

These files were hosted here until 2026-09-26 and are still in the repo's history at commit `5dd58d5`, byte for byte. Restore them locally, **before any history purge**. Run in Git Bash from the repo root:

```bash
mkdir -p ../General_Research_incoming
git cat-file -p 5dd58d5:01_density_and_population/full_texts/carry2012_density_of_asteroids_arxiv1203.4336v1.pdf > ../General_Research_incoming/carry2012.pdf
git cat-file -p 5dd58d5:01_density_and_population/full_texts/lodders_palme2009_ci_abundances_metSoc72_abstract.pdf > ../General_Research_incoming/lodders_palme2009.pdf
git cat-file -p 5dd58d5:01_density_and_population/full_texts/chesley_2014_bennu_orbit_bulk_density_icarus235_arxiv1402.5573v1.pdf > ../General_Research_incoming/chesley_2014_bennu_orbit_bulk_density.pdf
git cat-file -p 5dd58d5:02_composition_value/full_texts/hein_matheson_fries_2020_techno-economic_analysis_arxiv1810.03836v11.pdf > ../General_Research_incoming/hein2020.pdf
git cat-file -p 5dd58d5:02_composition_value/full_texts/graps_et_al_2019_ASIME_asteroid_composition_whitpaper_arxiv1904.11831v1.pdf > ../General_Research_incoming/asime2018.pdf
git cat-file -p 5dd58d5:02_composition_value/full_texts/lewicki_et_al_2023_decadal_whitepaper_arxiv2103.02435v1.pdf > ../General_Research_incoming/lewicki2023.pdf
git cat-file -p 5dd58d5:02_composition_value/full_texts/reddy_dunn_thomas_moskovitz_burbine_asteroids4_mineralogy_surface_composition_arxiv1502.05008v1.pdf > ../General_Research_incoming/reddy_asteroids_iv_mineralogy.pdf
git cat-file -p 5dd58d5:02_composition_value/full_texts/lodders_2010_solar_system_abundances_kodaikanal_arxiv1010.2746v1.pdf > ../General_Research_incoming/lodders_2010_solar_abundances.pdf
git cat-file -p 5dd58d5:02_composition_value/full_texts/rubin_altwegg_et_al_2019_67P_elemental_molecular_abundances_MNRAS_stz2086_arxiv1907.11044v3.pdf > ../General_Research_incoming/rubin_2019_67p_abundances.pdf
git cat-file -p 5dd58d5:03_dv_propulsion/full_texts/elvis_mcdowell_hoffman_binzel_2011_ultra-low_delta-v_arxiv1105.4152.pdf > ../General_Research_incoming/elvis2011.pdf
git cat-file -p 5dd58d5:03_dv_propulsion/full_texts/ieva_et_al_2014_low-dv_NEOs_NEOSURFACE_arxiv1406.5027.pdf > ../General_Research_incoming/ieva2014.pdf
git cat-file -p 5dd58d5:03_dv_propulsion/full_texts/kim_et_al_2013_state_of_the_art_methane_oxygen_LPRE_KSPE_17-6-120.pdf > ../General_Research_incoming/kim_2013.pdf
git cat-file -p 5dd58d5:03_dv_propulsion/full_texts/komurasaki_aquarius_ground_test_water_resistojet_2018_jstage.pdf > ../General_Research_incoming/komurasaki_aquarius_ground_2018.pdf
git cat-file -p 5dd58d5:03_dv_propulsion/full_texts/krishnan_h2o2_rp1_upper_stage_aiaa_jpc_2010.pdf > ../General_Research_incoming/krishnan_2010_h2o2_rp1_upper_stage.pdf
git cat-file -p 5dd58d5:03_dv_propulsion/full_texts/pietrobon_jbis_1999_h2o2_kero_shuttle_boosters.pdf > ../General_Research_incoming/pietrobon_1999_h2o2_kero_shuttle_boosters.pdf
git cat-file -p 5dd58d5:03_dv_propulsion/full_texts/alice_nanoal_water_combustion_aiaa_jpp_2014.pdf > ../General_Research_incoming/risha_2014_alice_jpp.pdf
git cat-file -p 5dd58d5:05_inspace_operations/full_texts/local_vs_broad_area_cooling_LH2_boiloff_arxiv2412.11720.pdf > ../General_Research_incoming/lac_bac_2024.pdf
git cat-file -p 5dd58d5:05_inspace_operations/full_texts/silicate_sulfuric_acid_ISRU_process_arxiv2107.05872.pdf > ../General_Research_incoming/ssap_2021.pdf
git cat-file -p 5dd58d5:05_inspace_operations/full_texts/bontempo_brigeman_fain_2020_NEXT-C_PPU_design_build_test_ntrs_20205004248_publicdomain.pdf > ../General_Research_incoming/nextc_ppu_2020.pdf
git cat-file -p 5dd58d5:05_inspace_operations/full_texts/jpl_dsn_services_catalog_820-100_revH_jun2022_publicdomain.pdf > ../General_Research_incoming/jpl_dsn_services_catalog_820_100.pdf
```

Check them with `sha256sum ../General_Research_incoming/*.pdf` against this table. The earlier rounds took only the numbers the repo already used from these files; none has had a full pass.

| ☐ | Save as | Bytes | sha256 | Rows now |
|---|---|---|---|---|
| ☑ | `carry2012.pdf` | 5,680,004 | `1e863e5ffb1c193705a77e821df7a010bfc8f2cf4711a191cea26de682066117` | 29 (per-class Table 3 only; no per-asteroid densities extracted) |
| ☑ | `lodders_palme2009.pdf` | 15,554 | `3444e51aa3fef3c529bc95ac4735b439e31ead8421d182b532878c0b6fe88dd6` | 9 |
| ☑ | `chesley_2014_bennu_orbit_bulk_density.pdf` | 1,231,590 | `55a96542ba2f2116a54f3f2c01eedbdfe2237b51a0f55e325b721608dc1ee7ba` | 6 |
| ☑ | `hein2020.pdf` | 430,126 | `ed8d373c3384f49d0ef2f0fe13b0d6c49f24c079fe681c51219380dc026b5ba0` | 19 |
| ☑ | `asime2018.pdf` | 2,377,086 | `c43015b864f3752413ce1e8ce273f63b75979b5eda64950b411f515c0eb211d7` | 3 |
| ☑ | `lewicki2023.pdf` | 257,123 | `6dde606baf15004c07eb6689669c2c701470c34d09037ecb9944b595b2ab0fda` | 1 |
| ☑ | `reddy_asteroids_iv_mineralogy.pdf` | 2,446,918 | `7e79fa0d1240b571f0b42480ba319e77385147f26ab758d0bc3815c45a1b44a2` | 7 |
| ☑ | `lodders_2010_solar_abundances.pdf` | 248,156 | `2f76d28cbcbb21f28ff104513d56c5cb6c6fbfb2819b0861ae1f551ef88af88a` | 87 |
| ☑ | `rubin_2019_67p_abundances.pdf` | 942,055 | `f40280c2822ece2823ca689e042012853c04e36816077b4e65a1fff8c53acd53` | 20 |
| ☑ | `elvis2011.pdf` | 607,711 | `b4518f4bc18c3a2b888972fd1229f1ec6eeec0f38307d1af407245e927a64ca5` | 3 |
| ☑ | `ieva2014.pdf` | 554,905 | `5f2781cf3f310a2a82feeefe4f30ff2077beafd71bbca6e3f9b7993e359b617d` | 3 |
| ☑ | `kim_2013.pdf` | 1,329,091 | `418173a3aba5ea050402c3f5ee200f1fde11f41f29eee5958b11f102529c097a` | 8 |
| ☑ | `komurasaki_aquarius_ground_2018.pdf` | 2,328,887 | `d94e1e3ab0500c408e3f1ca4d4adbacd070af4d88202df78a5a752c3c90c9478` | 4 |
| ☑ | `krishnan_2010_h2o2_rp1_upper_stage.pdf` | 268,620 | `0641a5e90f7beef229d25b87a1cf031d961ba55483987c82d563c0090fa93d5c` | 7 |
| ☑ | `pietrobon_1999_h2o2_kero_shuttle_boosters.pdf` | 89,348 | `31e72bb5120fb1f97642ad3a5f03ccdf332ac37ec8f2ace23388f1d79c7eb6ca` | 4 |
| ☑ | `risha_2014_alice_jpp.pdf` | 3,108,555 | `fb5eb59116d755b4c9037f71f661c852122cb4951cfecd0713f913c867bc2178` | 3 |
| ☑ | `lac_bac_2024.pdf` | 2,084,796 | `8193ca8eee5292b0416a94292470248fea42cc0d3548a9a8f86fb891ace5411f` | 8 |
| ☑ | `ssap_2021.pdf` | 317,152 | `b0ae503c9a59d10f5b983e3afef5e37dfa7d6558d01292852750e878c3e4436d` | 13 |
| ☑ | `nextc_ppu_2020.pdf` | 7,393,690 | `450c737c6c340735234c4d8c5c72edf12d0892954aad6f905e5f08931ea691e1` | 7 |
| ☑ | `jpl_dsn_services_catalog_820_100.pdf` | 1,543,820 | `48bdf613fb4bbf4291980c135dc5742ae311d7ba21df2383ec3d9c05d3383b6c` | 9 |

None of these 20 may be hosted again; each was un-hosted for its licence.

---

## C. Needs a normal web browser (the publisher blocks automated downloads from this machine)

Open the link, use the site's own "Download PDF" button, and save under the name given.

- [ ] **harris_dabramo_2021** (1) — NEA population revisited (size-frequency, completeness), Icarus 2021. Free to read on ScienceDirect.
  Get: https://doi.org/10.1016/j.icarus.2021.114452
  Save as `harris_dabramo_2021.pdf`. No licence stated, so extract only.
- [ ] **cannon2023** (0) — precious and structural metals on asteroids (per-class recoverable metal), PSS 215.
  Get: https://www.sciencedirect.com/science/article/pii/S0032063322001945/pdf
  Save as `cannon2023.pdf`. CC-BY-NC-ND; per your 2026-09-17 decision, extract numbers only and never host.
- [ ] **just_2019** (4) — parametric review of lunar regolith-excavation techniques, PSS 2019.
  Get: https://www.sciencedirect.com/science/article/pii/S003206331930162X/pdf
  Save as `just_2019.pdf`. CC-BY, so it may be hosted.
- [ ] **tirila_2023** (0) — review of alternative propellants for Hall thrusters, Acta Astronautica 212.
  Get: https://eprints.soton.ac.uk/483809/2/1_s2.0_S0094576523003983_main.pdf (or https://doi.org/10.1016/j.actaastro.2023.07.047)
  Save as `tirila_2023.pdf`. CC-BY per OpenAlex; the Soton file is the submitted version, so check the licence on the PDF before hosting.
- [ ] **farnocchia_2024** (2) — mass, density and radius of 16 Psyche, AJ 168:57.
  Get: https://doi.org/10.3847/1538-3881/ad50ca (then the PDF link)
  Save as `farnocchia_2024.pdf`. CC-BY, so it may be hosted.
- [ ] **mandler_elkins_tanton_2013** (1) — Vesta magma ocean / HED origin, MAPS 48.
  Get: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/maps.12135
  Save as `mandler_elkins_tanton_2013.pdf`. CC-BY, so it may be hosted.
- [ ] **pourpoint_2012_alice_feasibility** (1) — ALICE aluminium-ice propellant flight demonstration.
  Get: https://downloads.hindawi.com/journals/ijae/2012/874076.pdf
  Save as `pourpoint_2012_alice_feasibility.pdf`. CC-BY, so it may be hosted. Alternative copy (also Cloudflare-protected): https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1009&context=perc_articles
- [ ] **demeo_2009_bus_taxonomy_near_ir** (0) — Bus-DeMeo taxonomy definitions, Icarus 202. HAL author version.
  Get: https://hal.science/hal-00545286
  Save as `demeo_2009_bus_taxonomy_near_ir.pdf`. Extract only.
- [ ] **ryugu_soluble_organics_2023** (0) — Get: https://hal.science/hal-04208565/document — save as `ryugu_soluble_organics_2023.pdf`. Extract only.
- [ ] **ryugu_macromolecular_om_2023** (0) — Get: https://cnrs.hal.science/hal-04034418/document — save as `ryugu_macromolecular_om_2023.pdf`. Extract only.

---

## D. Needs library access or purchase (no free copy exists)

- [ ] **taylor2018** (0) — Δv map of the known main-belt asteroids, Acta Astronautica 146:73. Closed access; no preprint on arXiv.
  Get: https://doi.org/10.1016/j.actaastro.2018.02.014 (institutional login)
  Save as `taylor2018.pdf`. Extract only. **High value for the main-belt Δv rows.**
- [ ] **schoenman_1992** (2) — AIAA-92-3800, 490 N engine test experience. NTRS has the abstract only; buy from AIAA. Optional.
  Get: https://arc.aiaa.org/ (search "AIAA-92-3800")

---

## R96 - Domain 10 methalox anchors (registered 2026-10-01; all full texts NOT sought this round)

- [ ] **ueda_et_al_2013_methane_fueled_engine_altitude_hot_fire_jpc** - AIAA JPC 49th proceedings, DOI 10.2514/6.2013-4056 (paywalled). If obtained: extract the altitude-condition thrust/Isp table for a LOX/methane engine; save as `ueda_et_al_2013_methane_fueled_engine_altitude_hot_fire_jpc.pdf`.
- [ ] **judd_et_al_2006_lox_methane_combustion_performance_stability_durability** - AIAA SciTech 44th proceedings, DOI 10.2514/6.2006-1533 (paywalled). If obtained: extract the performance/stability/durability trade-off figures; save as `judd_et_al_2006_lox_methane_combustion_performance_stability_durability.pdf`.
- [ ] **engelen_souverein_twigt_deimos_methane_oxygen_engine_test_results_jbis** - JBIS 62:211-218 (2009), BIS refcode 2009.62.211, ~GBP 5 per copy at https://www.bis-space.com/shop/product/deimos-methane-oxygen-rocket-engine-test-results/ . If obtained: extract the measured thrust/chamber-pressure/mass-flow tables + reusability assessment; save as `engelen_souverein_twigt_deimos_methane_oxygen_engine_test_results_jbis.pdf`.

## R99 - Domain 4 fairing-source sweep (registered 2026-10-02; full texts NOT sought this round)

The 31 sources registered for spacecost v0.5.0's fairing cells: one is now hosted (Atlas V UG Rev 11, public-domain statement in file), sixteen were verified live and read from their PDF text layers but not committed (manufacturer copyright or third-party mirror provenance — see the R99 FINDINGS block for exact figure evidence). The fourteen below still need a normal browser or library access:

- [ ] **douglas_sm47274_saturn_v_payload_planners_guide_nov1965** - Douglas SM-47274 (Nov 1965), prime payload configuration A "about 3,230 cubic feet". archive.org item `SaturnVPayloadPlannersGuide` exists but its files DNS-failed from this machine in three attempts; retry the item's file list or use a NASA history office copy. If obtained: extract the configuration-A volume statement + fairing dimensions; save as `douglas_sm47274_saturn_v_payload_planners_guide_nov1965.pdf`.
- [ ] **isro_vssc_gslv_mkiii_vehicle_specifications_plf_volume** - ISRO/VSSC GSLV MkIII vehicle specifications page ("Heat Shield (Payload Fairing) Diameter 5.0 m, PLF Usable Volume 110m3"). isro.gov.in blocks/times out automated requests from this machine; open in a normal browser and screenshot or save the spec table. If obtained: extract the fairing spec line verbatim; save as `isro_vssc_gslv_mkiii_vehicle_specifications_plf_volume.png` (or .pdf if printable).
- [ ] **orienspace_gravity1_fairing_100m3_tencent_news_2023** - Tencent News report 2023-11-22 quoting Orienspace: the Gravity-1 4.2 m fairing "has 100 cubic metres of payload space". No stable URL in the upstream citation; locate via a Chinese search engine (tencent news archive). If obtained: extract the quoted sentence + date verbatim; save as `orienspace_gravity1_fairing_100m3_tencent_news_2023.html`.
- [ ] **russianspaceweb_angara_a5_14s746_fairing_zak** - RussianSpaceWeb (A. Zak) Angara-5 article: 14S746 fairing first flown 2025-09-19, 17.705 m long x 4.35 m diameter; no usable envelope published. Site is live but its search endpoint did not surface the article from this machine; browse russianspaceweb.com's Angara section directly. If obtained: extract the fairing dimensions + first-flight date verbatim; save as `russianspaceweb_angara_a5_14s746_fairing_zak.html`.
- [ ] **calt_lm2c_users_manual_issue_1999** - CALT LM-2C User's Manual (Issue 1999), ch. 4, Fig 4-2a two-stage fairing static envelope with the 1194A interface. Customer-only Chinese-language manual; caltaerospace.com unreachable from this machine. If obtained: extract Fig 4-2a dimensions; save as `calt_lm2c_users_manual_issue_1999.pdf`.
- [ ] **cgwic_lm3a_series_launch_vehicle_users_manual_issue_2011** - CGWIC LM-3A Series Launch Vehicle User's Manual (Issue 2011), Fig 4-5b 4000F fairing static envelope. Customer-only Chinese-language manual; no open copy found from this machine. If obtained: extract Fig 4-5b dimensions + the s3.5.2.1 LM-3BE GTO-with-4000F performance note; save as `cgwic_lm3a_series_launch_vehicle_users_manual_issue_2011.pdf`.
- [ ] **galactic_energy_ceres1_launch_vehicle_user_manual_2023** - Galactic Energy Ceres-1 (谷神星一号) Launch Vehicle User's Manual (2023), s05 fairing and payload envelope figure. Company site live but serves no public download; request via the company contact form or a customer channel. If obtained: extract the s05 envelope dimensions ("about 5 m" length per upstream); save as `galactic_energy_ceres1_launch_vehicle_user_manual_2023.pdf`.
- [ ] **galactic_energy_pallas1_user_manual_2023** - Galactic Energy Pallas-1 (智神星一号) User's Manual (2023), Fig 6(b) payload envelope under the 4,200 mm fairing. Same access route as Ceres-1 above. If obtained: extract Fig 6(b) dimensions; save as `galactic_energy_pallas1_user_manual_2023.pdf`.
- [ ] **cgwic_lm2d_technical_data_fairing_dimensions** - CGWIC LM-2D technical data: fairing diameter 3.35 m, length 6.983 m (outer dimensions only). Customer-only Chinese-language publication; no open copy found from this machine. If obtained: extract the two dimension values verbatim; save as `cgwic_lm2d_technical_data_fairing_dimensions.pdf`.
- [ ] **sohu_lm5_standard_fairing_calt_design_office_2024** - Sohu report 2024-05-06 quoting CALT's design office: standard LM-5 fairing 5.2 m x 12.267 m (18.5 m and 20.5 m/5B optional). No stable URL in the upstream citation; locate via a Chinese search engine on the date + "长征五号" + "整流罩". If obtained: extract the quoted dimensions verbatim with the outlet/date; save as `sohu_lm5_standard_fairing_calt_design_office_2024.html`.
- [ ] **tencent_news_lm10b_short_fairing_jul2026** - Tencent News report 2026-07-13: the LM-10B's short fairing is 5.2 m x 12.5 m, carried over from the LM-5 (an 18.5 m fairing optional). No stable URL in the upstream citation; locate via a Chinese search engine on the date + "长征十号" + "整流罩". If obtained: extract the quoted dimensions verbatim with the outlet/date; save as `tencent_news_lm10b_short_fairing_jul2026.html`.
- [ ] **reaction_engines_skylon_users_manual_rev1** - Reaction Engines SKYLON Users' Manual Rev 1, Fig 13 payload envelope (2,350 mm maximum radius, 13,000 mm long with 799 mm end clearances). reactionengines.co.uk refused connections from this machine on every attempt; retry later or via a normal browser. If obtained: extract Fig 13 dimensions verbatim; save as `reaction_engines_skylon_users_manual_rev1.pdf`.
## R100 - Domain 14 propellant & consumable prices (registered 2026-10-02; two full texts pulled and hosted this round)

Still blocked / dead this round:
- [ ] **dla_energy_aerospace_standard_prices_fy2020** - FY20/FY24/FY25 PDF URLs and the landing page all answer HTTP 403 from this machine (bot protection, not worked around); web.archive.org is DNS-blocked here. Would anchor hydrazine $30.5/kg, MMH/NTO in one document.
- [ ] **aqua_calc_lox_bulk_price** - still answers HTTP 403 from this machine.
## R109 - Domain 13 deepened: JPL astrodynamics services re-classified (registered 2026-10-03; IOM manual pulled and committed, .bsp kernels URL'd)

NOT committed (size cap ~36 MB; URL + recorded size/date in extracted_data/):
- [ ] sb441-n16.bsp - 615.8 MB, https://ssd.jpl.nasa.gov/ftp/eph/small_bodies/asteroids_de441/sb441-n16.bsp (2021-03-31)
- [ ] sb441-n373s.bsp - 936.6 MB, https://ssd.jpl.nasa.gov/ftp/eph/small_bodies/asteroids_de441/sb441-n373s.bsp (2021-09-02)
- [ ] sb441-n373.bsp - 14.13 GB, https://ssd.jpl.nasa.gov/ftp/eph/small_bodies/asteroids_de441/sb441-n373.bsp (2021-03-31)

Blocked this round: newton.spacedys.com/neodys/ serves an anti-bot interstitial ('Making sure you're not a bot!') from this machine - the NEODyS covariance service stays registered_not_pulled until it answers again.

## R113 - Owner's link list (registered 2026-10-04; eight files committed, the rest below)

Save as `<id>.pdf` in `General_Research_incoming`, as in section A.

- [ ] **bus_binzel_2002_smass2_feature_based_taxonomy** - https://doi.org/10.1006/icar.2002.6856 - Paywalled; this machine gets a CAPTCHA. Save a library copy for extraction only; do not host.
- [ ] **masiero_2021_albedo_uncertainties_thermal_modeling** - https://doi.org/10.3847/PSJ/abda4d - Read from arXiv. Published version is CC BY 4.0 but iopscience.iop.org bot-walls this machine: save the publisher PDF; it may then be hosted (check the licence on the PDF).
- [ ] **myhrvold_2022_four_band_wise_asteroids** - https://doi.org/10.3847/PSJ/ac3232 - Read from arXiv. Published version is CC BY 4.0 but iopscience.iop.org bot-walls this machine: save the publisher PDF; it may then be hosted (check the licence on the PDF).
- [ ] **masiero_2021_neowise_reactivation_years_6_7** - https://doi.org/10.3847/PSJ/ac15fb - Read from arXiv. Published version is CC BY 4.0 but iopscience.iop.org bot-walls this machine: save the publisher PDF; it may then be hosted (check the licence on the PDF).
- [ ] **murray_2023_neural_network_main_belt_albedos** - https://doi.org/10.3847/PSJ/acd381 - Read from arXiv. Published version is CC BY 4.0 but iopscience.iop.org bot-walls this machine: save the publisher PDF; it may then be hosted (check the licence on the PDF).
- [ ] **wang_2026_nea_albedo_from_orbital_elements** - https://doi.org/10.1088/1674-4527/ae37ed - IOP standard licence (not CC) and bot-walled here: save the PDF for extraction only.
- [ ] **mahlke_carry_denneau_2021_atlas_phase_curves** - https://doi.org/10.1016/j.icarus.2020.114094 - Icarus version is CC BY-NC-ND 4.0 but ScienceDirect gets a CAPTCHA here: save the publisher PDF; it may be hosted under that licence.
- [ ] **de_kleer_2026_jwst_spinel_rich_l_type_mineralogy** - https://doi.org/10.3847/PSJ/ae374e - Abstract only so far. Published version is CC BY 4.0 but iopscience.iop.org bot-walls this machine: save the publisher PDF; it may then be hosted (check the licence on the PDF).
- [ ] **wong_2024_jwst_lucy_trojans_oh_organics_co2** - https://doi.org/10.3847/PSJ/ad2fc3 - Read from arXiv (R152). Published version is CC BY 4.0 but iopscience.iop.org bot-walls this machine: save the publisher PDF; it may then be hosted (check the licence on the PDF).
- [ ] **xie_bennett_dempster_2021_nea_mining_target_evaluation** - https://doi.org/10.1016/j.actaastro.2021.01.011 - Paywalled; this machine gets a CAPTCHA. Save a library copy for extraction only; do not host. Its target tables are the d8 comparison to extract.
- [ ] **tang_et_al_2023_asteroid_rock_mechanical_properties** - https://doi.org/10.1016/j.enggeo.2023.107154 - Paywalled; this machine gets a CAPTCHA. Save a library copy for extraction only; do not host. Not yet read at all.
- [ ] **liu_et_al_2026_asteroid_laser_mining_cryogenic_vacuum** - https://doi.org/10.1016/j.cherd.2026.08.007 - Paywalled; this machine gets a CAPTCHA. Save a library copy for extraction only; do not host. Not yet read at all.
- [ ] **paulson_balchanos_mavris_2026_isru_economic_environmental_tradeoffs** - https://doi.org/10.2514/6.2026-2788 - AIAA paywall (abstract read). Save a copy for extraction only; do not host.
- [ ] **mahlke_2022_phd_thesis_asteroid_taxonomy** - https://theses.hal.science/tel-03850762/ - HAL serves a bot check here: save tel-03850762 (2022COAZ4051.pdf) from theses.hal.science; HAL licence is not CC, so extraction only.
- [ ] **lebofsky_et_al_1990_low_albedo_3um_photometry** - https://doi.org/10.1016/0019-1035(90)90003-R - Paywalled; this machine gets a CAPTCHA. Save a library copy for extraction only; do not host. Not yet read at all.
## R117 - Ariane 6 / H3 price-citation re-sourcing: ESA + Arianespace pages hash-recorded, JAXA unreachable (2026-10-05)

- **jaxa_h3_launch_vehicle** [T3] - https://global.jaxa.jp/projects/rockets/h3/ - NOT reachable from this machine R117 (HTTP 403 bot-wall on every route; web.archive.org DNS-blocked locally). Nothing to download here.
## R118 - d01 queue work: both pulled items hosted; one optional follow-up + one blocked item (2026-10-05)

- **tholen_1984_asteroid_taxonomy_dissertation** [T4] - https://repository.arizona.edu/handle/10150/187738 - still HTTP 403 to urllib and curl under browser headers from this machine (re-checked R118). Stays in the queue.
## R119 - queue re-classifications: 3 hosted, 1 not hostable, 1 still blocked (2026-10-05)

- **hayhurst_2016_historical_mass_power_schedule_cost_growth_nasa_spacecraft** [T2] - https://ntrs.nasa.gov/citations/20160003121 - re-checked R119: NTRS determinationType OTHER, no downloadable file in the citation API. Stays in queue; IEEE Aerospace Conference copy paywalled.

## R120 - OpenAlex sweep of queued DOIs: 6 hosted, 3 read-not-hostable (2026-10-05)

- **ricardo_2026** journal version https://doi.org/10.1007/s44461-026-00015-w - pulls live but in-file CC BY-NC-ND 4.0 (Crossref cc-by tag disagrees) -> preprint hosted instead; see d19 FINDINGS.
- Still blocked this round: lodders_2003 (IOP Radware captcha), sinibaldi_haldemann_2026 (Royal Society 403 on all routes), kabemba_2025 (MDPI 403), lauretta_2024_bennu_in_the_laboratory + king_schofield_2015 (Wiley/ORO 403), watanabe_2019 (DLR elib fulltext routes 404, HAL API empty), consolmagno_2008/macke_2010/sercel_2018 (UCF Stars landing pages carry no PDF link).

## R121 - Semantic Scholar + Unpaywall sweep of queued DOIs: 1 hosted, 5 read-not-hostable, 2 retry notes (2026-10-05)

- Still blocked this round (retry notes only): ueda_et_al_2013 (NII record id.nii.ac.jp/1696/00038623 answers HTTP 406 on all routes; AIAA paywall), watanabe_2019_hayabusa2_ryugu_spinning_top (JAXA dspace item page repository.exst.jaxa.jp/dspace/handle/a-is/928996 answers HTTP 406 on all routes; science.org still HTTP 403).
## R122 (2026-10-05) - no-DOI queue sweep
- d13 github_* batch (astroquery, brahe, CamPyRoS, Celestia, mesa, nyx, OpenSCvx, pds4_tools, polars, pygmo2, pymc, Pyomo, python-skyfield, space-datasets, space-map, spacekit, z3) [T4 x17] - each re-verified live via api.github.com/repos/<owner>/<repo> (public; license + last-push recorded in access_status); nothing extracted.
- Still blocked this round (retry notes only): ferrais_2022_kalliope_tiny_mercury (aanda.org HTTP 403 x2, ORO bitstream refused with record page live, HAL bot-challenge), lme_official_reference_prices + cme_comex_nymex_futures (pages live/403 but no usable figures in static HTML; CME still 403) - LME market data is JS-rendered so a T3 landing-page row cannot carry values from this machine, nasa_instrument_cost_model_nicm (JPL page has zero PDF links; docs stay NTRS-only per R106), pearson_1979_anchored_lunar_satellites (no Crossref record in the JAS vol-27 1978/80 window; ADS bot-walled), douglas_sm47274_saturn_v_payload_planners_guide_nov1965 (item page + metadata live (2 PDFs listed, main 62,769,084 B on storage host ia601604.us.archive.org) but every archive.org file/storage host is DNS-blocked from this machine (getaddrinfo failed)), gao_2018_commercial_space_launch_insurance_mpl_methodology (HTTP 429).

## R123 (2026-10-05) - S2 DOI->arXiv sweep of all queued DOIs
- Still blocked this round (retry notes only): ueda_2013 NII record HTTP 406 x all routes; watanabe_2019 JAXA dspace HTTP 406 + science.org unchanged; S2 oa_pdf re-probes: mainzer IOP Radware captcha, macke x2 Wiley 403, ferrais/carvano aanda 403.

## R124 (2026-10-05) - T4 live-read batch + Crossref link-field sweep
- Retry notes only (stay registered_not_pulled): ULA rocket pages live w/o $ figures; firefly Alpha page JS-rendered, no $ in static HTML; NSIL /launch-services has vehicle names but no prices; pypi yfinance now serves a 'Client Challenge' bot page.
- Crossref `link`-field sweep of all 64 queued DOIs: six publisher-registered direct PDF URLs found (pielke_byerly_2011 + patzold_2016 Nature, sinibaldi_haldemann_2026 Royal Society, lauretta_2024 Wiley, smith_stanley_2021 AIAA, wang_2026 IOP) - ALL bot-walled from this machine (cookie-wall / Cloudflare 'Just a moment' / Radware captcha). Negative finding; rows stay registered_not_pulled.
## R125 (2026-10-06) - CC-BY queue sweep: arXiv copies read + institutional routes walled

- king_schofield_2015_ci_modal_mineralogy_xrd: OA copy at oro.open.ac.uk/69573/1/69573.pdf (Open University ORA; CC BY 4.0 in-file per record-page snippet) - Cloudflare 'Just a moment' on all direct fetches from this machine. NOT pulled.
- sinibaldi_haldemann_2026: ORA record oro.open.ac.uk/108579 live-verified via web_extract; Royal Society PDF + ORA bitstream both Cloudflare-walled. NOT pulled.
- broslav_2025 (thesis): repository.mines.edu item abed9ab3-8bf3-4cac-aafa-b81d379ee4d2, DSpace 7 REST anonymous for metadata but HTTP 401 on bitstreams. NOT pulled.
- ferrais_2022 / pentikainen_2026: CC BY 4.0 per Crossref; no arXiv copies exist (exact-title searches empty); EDP aanda.org bot-checks every route incl. DOI resolution. NOT pulled.

## R148 (2026-10-10) - Domain 3 Dawn flight records: six peer-reviewed IPS papers registered, all full texts NOT sought this round

- brophy_2011_dawn_ips: Springer SSR 163(1-4):251-261 (DOI 10.1007/s11214-011-9848-y). Article page + content/pdf route answer an HTML paywall stub from this machine; no OA copy in OpenAlex/Unpaywall/SemanticScholar. Institutional/library PDF needed.
- rayman_mase_2014_dawn_cruise_acta: Elsevier Acta Astronautica 103:113-118 (DOI 10.1016/j.actaastro.2014.06.042). ScienceDirect routes 403 from this machine; no OA copy in the three indexes. NTRS twin 20150007126 is determinationType OTHER with zero files.
- garner_rayman_2013_jpc_cruise_yr1: AIAA JPC paper 6.2013-4112 (DOI 10.2514/6.2013-4112). NTRS twin 20150008021 is determinationType OTHER with zero files (re-probed R148).
- garner_rayman_2015_jpc_orbit_ops: AIAA JPC paper 6.2015-3717 (DOI 10.2514/6.2015-3717). No NTRS twin located in the R148 searches; sister papers of the series are all det=OTHER with zero files.
- garner_rayman_2016_jpc_lamo: AIAA JPC paper 6.2016-4539 (DOI 10.2514/6.2016-4539). NTRS twin 20190002063 is determinationType OTHER with zero files (re-probed R148).
- garner_rayman_2018_jpc_final_orb: AIAA JPC paper 6.2018-4641 (DOI 10.2514/6.2018-4641; Crossref title prints a typo, 'Dwn'). NTRS twin 20210008613 is determinationType OTHER with zero files (re-probed R148).

## Round 149 - d27 foundational queue

- **kessler_cour_palais_1978_collision_frequency_debris_belt** [T1] - Kessler & Cour-Palais, "Collision frequency of artificial satellites: The creation of a debris belt", JGR Space Physics 83(A6):2637-2646 (DOI `10.1029/ja083ia06p02637`, Crossref-verified live R149). THE canonical collision-frequency / debris-belt model behind d27's premise and the Kessler-syndrome literature.
  - NTRS record **19780057167**: determinationType=GOV_PUBLIC_USE_PERMITTED but **zero downloadable files** (probed R149).
  - AGU/Wiley: `https://doi.org/10.1029/ja083ia06p02637` and `.../agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/JA083iA06P02637` both **HTTP 403** from this machine (probed R149).
  - Route: institutional/library pull, or an AGU archive-access session; the paper is also cited verbatim in the now-hosted NASA CP-2360 reference list.

## Round 151 - d15 cislunar-economics queue

- **bennett_xie_dempster_2022_moon_neas_cislunar_propellant** [T1] - Acta Astronautica 190:409-412 (DOI `10.1016/j.actaastro.2021.10.038`, Crossref-verified live R151). Moon vs NEA cislunar propellant sourcing cost - the delivered-material-value source for d15's utility-factor item.
  - Elsevier licence field = TDM-only (no redistribution); OpenAlex isOA=False; Semantic Scholar isOpenAccess=False, no open PDF; NTRS title/author search zero records; doi.org -> linkinghub.elsevier.com stub HTTP 200 with no file (all probed R151).
- **entrena_2017_emerging_cislunar_economy_framework** [T1] - Acta Astronautica 141:209-218 (DOI `10.1016/j.actaastro.2017.10.005`, Crossref-verified live R151). Framework for studying the emerging cislunar economy.
  - Canonical PII **S0094576516311717** (from Crossref link field); ScienceDirect PDF route HTTP 403 from this machine; OpenAlex isOA=False; Semantic Scholar isOpenAccess=False, no open PDF (all probed R151).
- **keravala_tietz_stone_2013_shackleton_propellant_depot_architecture** [T1] - New Space 1(2):91-100 (DOI `10.1089/space.2013.0014`, Crossref-verified live R151). First commercial propellant-depot business case: per-kg delivered-fuel pricing + depot demand.
  - Publisher route via doi.org HTTP 403 from this machine; OpenAlex isOA=False; Semantic Scholar isOpenAccess=False, no open PDF (all probed R151).
- **kutter_sowers_2016_cislunar1000_self_sustaining_space_economy** [T2] - AIAA SPACE 2016 (DOI `10.2514/6.2016-5491`, Crossref-verified live R151). Transportation demand supporting a self-sustaining cislunar economy.
  - NTRS title search zero records (no NASA-hosted twin); OpenAlex isOA=False; Semantic Scholar isOpenAccess=False, no open PDF (all probed R151).

Route for all four: institutional/library pull or an Elsevier/Liebert/AIAA archive-access session. Re-probe publisher routes at least once per few rounds - WAF walls are not permanent (R144 GAO precedent).
## Round 153 - d17 liability-insurance premium queue

- **gao_2012_commercial_space_launches_faa_liability_risk_assessment** [T3] - GAO-12-899 "Commercial Space Launches: FAA Should Update How It Assesses Federal Liability Risk" (Jul 30 2012). The premium-rate source behind d17's third-party liability cell (~1% of coverage x ~$99M avg MPL = ~$0.99M/launch implied; range $0.23-2.67M).
  - Save as: gao-12-899.pdf; route https://www.gao.gov/assets/600/593106.pdf (HTTP 403 Akamai WAF from this machine R153, full browser headers via urllib and curl); product page https://www.gao.gov/products/gao-12-899 also HTTP 403; NTRS title search zero records. Licence: public-domain (work of the U.S. government) - hostable once pulled.
- **gao_2017_commercial_space_launch_insurance_faa_calculation_weakness** [T3] - GAO-17-366 "Commercial Space Launch Insurance: Weakness in FAA's Insurance Calculation May Expose the Federal Government to Excess Risk" (Mar 2017). Later data point on the same cell (~$51M avg MPL across five active licenses of 2016 -> ~$0.5M/launch implied) + $3M cost-of-casualty corroboration.
  - Save as: gao-17-366.pdf; route https://www.gao.gov/assets/690/683915.pdf (HTTP 403 Akamai WAF from this machine R153); product page https://www.gao.gov/products/GAO-17-366 also HTTP 403. Licence: public-domain (work of the U.S. government) - hostable once pulled.

Route for both: institutional/library pull, or re-probe gao.gov when its WAF opens (R144 precedent shows the block is transient in both directions).

## R154 addition (2026-10-12)
- **gao_2017_pu238_rps_production_planning** [T3] - GAO-17-673 "Space Exploration: DOE Could Improve Planning and Communication Related to Plutonium-238 and Radioisotope Power Systems Production Challenges" (Sep 2017). FIRST institutional per-unit MMRTG costs in d05 ($77M/$94M/$117M vs $850M New Frontiers cap; ~$700k/W at BODL) + CRP-era production context.
  - Save as: gao-17-673.pdf; routes https://www.gao.gov/assets/690/688254.pdf AND the alternate canonical https://www.gao.gov/assets/gao-17-673.pdf (both HTTP 403 Akamai WAF from this machine R154, full browser headers via urllib and curl); product page https://www.gao.gov/products/GAO-17-673 also HTTP 403. Key figures already extracted verbatim from GAO's own published text (search-index capture of gao.gov pages) per the R89/R153 precedent.
  - Route: institutional pull, or a future round when gao.gov unblocks (R144 showed an unblock can be transient). Licence: public-domain (work of the U.S. government) - hostable once pulled.
## Round 155 - group-5 open-copy sweep: free or hostable copies behind bot walls

Round 155 sought the 35 never-sought T1/T2 queue rows and read eight. These twelve have a free-to-read (or CC BY) copy that this machine cannot fetch. Save each as `<id>.pdf` in `General_Research_incoming`, as in section A.

- [ ] **macke_2011_carbonaceous_chondrite_density_porosity** - https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1945-5100.2011.01298.x - OpenAlex reports the published version as CC BY; Wiley 403s here. May be hosted if the PDF itself says CC BY.
- [ ] **kopp_lean_2011_total_solar_irradiance** - https://doi.org/10.1029/2010GL045777 (AGU, free to read) or https://apps.dtic.mil/sti/pdfs/ADA535690.pdf (DTIC was under maintenance R155). Extract only unless the file grants reuse.
- [ ] **carvano_2010_sdss_taxonomy_main_belt** - https://www.aanda.org/articles/aa/pdf/2010/02/aa13322-09.pdf - A&A free access; aanda.org 403s here. Extract only.
- [ ] **kargel_1994_metalliferous_asteroids_precious_metals** - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/94JE02141 - AGU archive; 403 here. Extract only.
- [ ] **nichiporuk_brown_1965_pt_pd_iron_meteorites** - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/JZ070i002p00459 - AGU archive. Extract only.
- [ ] **scott_wasson_1975_classification_properties_iron_meteorites** - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/RG013i004p00527 - AGU archive. Extract only.
- [ ] **keil_1968_mineralogical_chemical_enstatite_chondrites** - https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/JB073i022p06945 - AGU archive. Extract only.
- [ ] **pearson_2006_carbon_nitrogen_carbonaceous_chondrites** - https://journals.uair.arizona.edu/index.php/maps/article/download/15367/15355 (University of Arizona MAPS archive; bot check here) or the Wiley DOI. Extract only.
- [ ] **dunn_cressey_2010_xrd_modal_mineral_abundances_ordinary_chondrites** - https://repository.si.edu/handle/10088/20464 (Smithsonian repository; 403 here) or the Wiley DOI. Extract only.
- [ ] **sunshine_connolly_2008_ancient_asteroids_refractory_inclusions** - https://repository.si.edu/items/e39dedbe-b83e-4add-98c6-9d0d9ac7fafd/full - the page loads, but no file link shows in its static HTML. Extract only.
- [ ] **consolmagno_2008_meteorite_density_porosity** - https://stars.library.ucf.edu/facultybib2000/234 (UCF record, no file) - look for a full-text link in a browser. Extract only.
- [ ] **fujiwara_2006_itokawa_rubble_pile** - https://ieeemilestones.ethw.org/w/images/8/82/Reference_E_3_2006Fujiwara_Rubble-Pile_Asteroid_Itokawa_Science.pdf (404 to a browser User-Agent here) - retry in a browser. Extract only.

## R160 - Tagish Lake modal mineralogy (rc-085)

- Zolensky, M.E.; Nakamura, E.; Gounelle, M.; Mikouchi, T.; Kasama, Y.; et al. 'Mineralogy of Tagish Lake: An ungrouped type 2 carbonaceous chondrite', Meteoritics & Planetary Science 37(5):737-761 (May 2002), DOI 10.1111/j.1945-5100.2002.tb00852.x.
  - Why: THE dedicated modal-mineralogy study for Tagish Lake - mode percentages of magnetite, sulfides and carbonates in pristine samples; the figures upstream's _ACC_TL (magnetite ~5 / troilite ~3 / carbonates ~3 wt%) needs a source for. rc-085.
  - Routes tried R160: NTRS 20010044424 = conference ABSTRACT record, determinationType=GOV_PUBLIC_USE_PERMITTED but metadata-only (downloadsAvailable=false, zero files); OpenAlex is_oa=false with no OA location; Wiley/MAPS paywall. Needs an institutional/library pull.
## R173 - d29 meteoritic Fe-Ni strength + nickel LCI queue (2026-10-15)

- knox_1970_yield_strength_meteoritic_iron — THE YIELD STRENGTH OF METEORITIC IRON, Meteoritics 5(2):63-74 (June 1970), DOI 10.1111/j.1945-5100.1970.tb00391.x (Wiley).
  - Why: the original measured yield-strength study for iron meteorites (recrystallized Canyon Diablo, Odessa octahedrite, Brenham metal phase; flow stress at 0.2% plastic strain) - d29's Fe-Ni mechanical-properties item needs its primary source on record; Ueki 2021 and Mulford/EI-Dasher 2011 both descend from this line of work.
  - Routes tried R173: DOI Crossref-verified live (Wiley, Meteoritics vol 5 issue 2 pp 63-74); onlinelibrary.wiley.com article page Cloudflare-challenged ('Just a moment...') with Chrome and Safari UAs; no NTRS record exists for it. Needs an institutional/library pull or Wiley access.

- iyer_kelly_2022_lci_critical_materials_ni_cu_ti_ree — Life-Cycle Inventory of Critical Materials: Nickel, Copper, Titanium, and Rare-Earth Elements, Argonne National Laboratory (OSTI 1905473), DOI 10.2172/1905473 (Dec 2022).
  - Why: THE life-cycle inventory behind GREET's nickel production models including the carbonyl-refining step - d29's 'carbonyl (Mond) refining of asteroidal Fe-Ni' item needs its process + energy source on record. Per OSTI's own record annotation it covers domestic and international geographies with ore-grade variation for Ni and Cu, plus LCIs for all intermediate materials.
  - Routes tried R173: osti.gov/servlets/purl/1905473 Cloudflare-challenged (Chrome + Safari UAs); publications.anl.gov/anlpubs/2022/12/178670.pdf Cloudflare-challenged; osti.gov/biblio/1905473 page loads but is a JS shell with no abstract layer. OpenAlex and Semantic Scholar both flag the work OA (green) via exactly those two URLs - retry after the Cloudflare window or pull institutionally.

## R174 - queue re-probe wave: eight walled rows, all still blocked (2026-10-15)

All routes below were probed live from this machine on 2026-10-15 with browser-style UAs; the exact failure evidence is also appended to each row's access_status cell. No new accessible copy was found for any of them.

- ferrais_2022_kalliope_tiny_mercury (A&A 662:A71, CC BY 4.0): oro.open.ac.uk/83943/1/aa43200-22.pdf HTTP 403; hal.science/hal-03693926/document = Anubis bot-check page (HTTP 200 HTML, no PDF); aanda.org/articles/aa/pdf/2022/06/aa43200-22.pdf HTTP 403. Needs an institutional pull or a browser session through the A&A/HAL challenge.
- pentikainen_2026_gaia_dr3_asteroid_characterization (A&A, CC BY 4.0): doi.org/10.1051/0004-6361/202556127 redirect HTTP 403; OpenAlex gold OA with no mirror PDF in any repository location. Needs a browser session through the A&A WAF or an institutional pull.
- carvano_2010_sdss_taxonomy_main_belt (A&A 510:A43, bronze OA): aanda.org/articles/aa/pdf/2010/02/aa13322-09.pdf HTTP 403; no mirror PDF locations in OpenAlex. Same A&A wall as the two rows above.
- just_2019 (Planetary and Space Science, hybrid OA): sciencedirect.com article page S003206331930162X HTTP 403 Cloudflare; Unpaywall v2 answers HTTP 422 (no OA location data); OpenAlex lists only the ScienceDirect PDF route. d19 parametric-table completeness item (rc-027 was unblocked in R152 - not a blocker).
- dorrington_olsen_2026_parametric_economic_modelling_asteroid_mining_architectures (Acta Astronautica 241:19-47, CC-BY VOR): doi.org lands on the linkinghub.elsevier.com JS redirect stub (HTTP 200 HTML, not a PDF); UNSW Sydney Research Repository DNS still NXDOMAIN for research-repository.unsw.edu.au and openarchive.unsw.edu.au; OpenAlex hybrid OA with no locations. Legally hostable once reachable - institutional pull via the UNSW repository is the named route.
- kopp_lean_2011_total_solar_irradiance (GRL, bronze OA): onlinelibrary.wiley.com/doi/pdfdirect HTTP 403 Cloudflare; the accessible companion rind_lean_jonas_2014 remains the working anchor for the same absolute-TSI question.
- knox_1970_yield_strength_meteoritic_iron (Meteoritics, Wiley): onlinelibrary.wiley.com/doi/pdfdirect HTTP 403 Cloudflare; no NTRS record exists. Needs an institutional/library pull or Wiley access.
- iyer_kelly_2022_lci_critical_materials_ni_cu_ti_ree (ANL OSTI 1905473): osti.gov/servlets/purl/1905473 HTTP 403 Cloudflare; publications.anl.gov/anlpubs/2022/12/178670.pdf HTTP 403. Named source for d29 carbonyl-refining item - pull institutionally (ANL or DOE OSTI access).
