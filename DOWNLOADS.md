# What still has to be downloaded

Round 70 (2026-09-27) extracted every file hosted in this repo. The 58 sources below are not hosted, so their extraction is limited to what earlier rounds read live. This file lists exactly what to fetch to finish the job. Tick each box as you go.

**Status after Round 73 (2026-09-27):** Round 71 (branch `side-deepening`) extracted all 20 section-A files and seven section-B downloads, and Round 72 checked them. Round 73 ran in a container with open network access and fetched and extracted the rest of section B (the Planetary Society workbook and the full NHATS table) and six section-C items from open copies (ticked below, with the route used). **Still to fetch, all needing a normal browser or library access:** harris_dabramo_2021, cannon2023, just_2019, tirila_2023, farnocchia_2024, mandler_elkins_tanton_2013, pourpoint_2012_alice_feasibility, demeo_2009_bus_taxonomy_near_ir, ryugu_soluble_organics_2023, ryugu_macromolecular_om_2023 (section C), and all of section D. From a server these hosts answer with bot challenges (Cloudflare, DataDome, Radware, Anubis) even with open network access; Round 73 did not try to get around them. Also wanted: the Ryugu supplementary data files (Data S2-S8 xlsx) from https://www.science.org/doi/10.1126/science.abn7850 (Supplementary Materials), which hold the per-element bulk chemistry.

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

## B. Direct links that work from any machine, including Claude's (no browser needed)

- [x] **planetary_society_pebd_mission_costs** (extracted in R73: all 137 sheets, ~15,800 cells) (13) — **highest value**: NASA planetary-mission costs by development, launch and operations for every mission, at fiscal-year resolution (80 sheets). Only a summary has been extracted.
  Get: https://docs.google.com/spreadsheets/d/12frTU01gfT1CXGWFimN3whf4348F_r3XolTqBt02OyM/export?format=xlsx
  Save as `planetary_society_pebd_mission_costs.xlsx`. The dataset terms require attribution to The Planetary Society; extract only.
- [x] **adam_2017** (extracted in R71) (0) — volumes and bulk densities of 40 asteroids. The arXiv preprint works from here.
  Get: https://arxiv.org/pdf/1702.01996 (published version: https://www.aanda.org/articles/aa/pdf/2017/05/aa29956-16.pdf, which needs a browser)
  Save as `adam_2017.pdf`. arXiv default licence, so extract only.
- [x] **metzger_2023** (extracted in R71) (0) — economics of lunar-derived propellant (Acta Astronautica 2023). Registered but never extracted.
  Get: https://arxiv.org/pdf/2303.09011
  Save as `metzger_2023.pdf`. Extract only.
- [x] **metzger_zacny_2020** (extracted in R71) (5) — thermal extraction of volatiles from regolith.
  Get: https://arxiv.org/pdf/2306.03776
  Save as `metzger_zacny_2020.pdf`. Extract only.
- [x] **proctor_apex_2019** (extracted in R71) (4) — NASA Glenn regolith-excavation power and force facility (2.7 MB).
  Get: https://ntrs.nasa.gov/api/citations/20190027268/downloads/20190027268.pdf
  Save as `proctor_apex_2019.pdf`. The registry records the NTRS copy as public domain, so it may be hostable after an NTRS copyright check.
- [x] **zeitlin_asteroid_excavation_project** (extracted in R71) (1) — asteroid icy-regolith excavation and volatile capture (396 KB).
  Get: https://ntrs.nasa.gov/api/citations/20150016080/downloads/20150016080.pdf
  Save as `zeitlin_asteroid_excavation_project.pdf`. May be hostable after an NTRS copyright check.
- [x] **jpl_nhats_nea_dv_oracle** (extracted in R73: 7,094 bodies) (10) — round-trip Δv and duration for every NHATS-accessible NEA. Only statistics are extracted so far; the per-body table (~7,100 bodies) is not.
  Get: https://ssd-api.jpl.nasa.gov/nhats.api
  Save as `jpl_nhats_nea_dv_oracle.json`.
- [x] **usgs_pp1802n** (extracted in R71) (3) — the full USGS Professional Paper 1802-N (platinum-group elements). Only an excerpt is hosted now.
  Get: https://pubs.usgs.gov/pp/1802/n/pp1802n.pdf
  Save as `usgs_pp1802n.pdf`. USGS public domain, so it may be hosted if under 50 MB.
- [x] **cowen_agnello_petit_2012_npsr_pge** (extracted in R81: full 16-page paper, terms table + recovery rates) - net-smelter-return mechanics for the South African PGE industry; registered in domain 25.
- [ ] **dreisinger_2000_hydrometallurgical_treatment_pgm_sulfide_concentrates** (extracted in R91: full 25-page deck read live; NOT hostable - no licence statement, PolyMet data under permission) - measured flotation + pressure-leach recoveries for an iron-rich Cu-Ni-PGM feed (Northmet); registered in domain 25.
  Get: https://propertyfile.gov.bc.ca/reports/PF700051.pdf
  Save as `dreisinger_2000_hydrometallurgical_treatment_pgm_sulfide_concentrates.pdf`. No licence statement anywhere in the PDF, so extract only; never host.
  Get: https://saimm.co.za/Conferences/Pt2012/577-592_Cowen.pdf
  Save as `cowen_agnello_petit_2012_npsr_pge.pdf`. No licence statement anywhere in the PDF (Camera Press watermark only), so extract only; never host.
- [ ] **mc_dowell_2025_space_activities_gcat** (extracted in R92: full 70-page report read live; NOT hostable - no licence statement anywhere) - GCAT Rev 1.2 GEO population table (Table 22): 613 active payloads GPZ+/-100 km / 638 total as of Jan 2026, anchoring upstream's '~550 geostationary satellites'; registered in domain 15.
  Get: https://planet4589.org/space/papers/space25.1.2.pdf
  Save as `mc_dowell_2025_space_activities_gcat_rev1.2.pdf`. No licence statement anywhere in the PDF, so extract only; never host.
- [x] **jm_pgm_market_report_2026** (extracted in R71) (10) — Johnson Matthey PGM market report, May 2026: full supply and demand tables.
  Get: https://matthey.com/documents/161599/509428/pgm-market-report-26.pdf/a2d115af-bf7c-f589-29e9-6beacf8a4452
  Save as `jm_pgm_market_report_2026.pdf`. JM terms forbid reuse without consent, so extract only; never host.

---

- [x] **kornuta_2019_commercial_lunar_propellant_architecture** (read in full R84) - Commercial Lunar Propellant Architecture, REACH 13:100026. The co-authors' own copy works from any machine; the publisher copy is TDM-only and ScienceDirect bot-blocks this machine.
Get: http://publish.illinois.edu/kokiholab/files/2018/11/Commercial-Lunar-Propellant-Architecture.pdf
Save as `kornuta_2019_clpa.pdf`. No redistribution licence on either copy, so extract only.
- [ ] **sukumaran_et_al_2024_ti_hbn_wear_neutron_shielding_sct** (extracted in R94: full 16-page paper read live; NOT hostable - "copyright 2024 Elsevier B.V. All rights are reserved" printed on p.1) - Ti-hBN coating sliding wear with JSC-1A third-body abrasion, 90-95% lower wear rate than uncoated substrate; registered in domain 16.
  Get: https://ntrs.nasa.gov/api/citations/20240011143/downloads/ECI%202_Ti-hBN%20SCT.pdf (publisher copy behind Elsevier paywall)
  Save as `sukumaran_et_al_2024_ti_hbn_wear_neutron_shielding_sct.pdf`. Elsevier all-rights-reserved in-file, so extract only; never host. DOI: https://doi.org/10.1016/j.surfcoat.2024.131185
- [ ] **stein_et_al_2025_icacc_abrasive_effects_of_lunar_regolith_on_material_wear** (extracted in R94: full 15-page deck read live; NOT hostable - NTRS determinationType=MAY_INCLUDE_COPYRIGHT_MATERIAL + no licence statement) - Taber abrasion wear indices with LMS-1 regolith wheels vs standard CS-17 media; registered in domain 16.
  Get: https://ntrs.nasa.gov/api/citations/20250000687/downloads/ICACC2025_WearResistance_Stein_v3.pdf
  Save as `stein_et_al_2025_icacc_abrasive_effects_of_lunar_regolith_on_material_wear.pdf`. Extract only; never host.
- [ ] **mas_2007_nber13138_labor_unrest_equipment_resale_market** (extracted in R94: full 50-page working paper read live; NOT hostable - "copyright 2007 by Alexandre Mas. All rights reserved") - >48,000 used construction-equipment auction sales with condition-indexed pricing; the terrestrial analogue for `Rig salvage fraction`; registered in domain 16.
  Get: https://www.nber.org/system/files/working_papers/w13138/w13138.pdf
  Save as `mas_2007_nber13138_labor_unrest_equipment_resale_market.pdf`. Extract only; never host.
- [ ] **kinnett_green_klein_lin_2022_drill_feed_msl_in_flight_failure_ams** (extracted in R95: full 14-page paper read live; NOT hostable - "copyright 2022. California Institute of Technology" printed on p.1) - Curiosity drill-feed in-flight failure + recovery, the drilling component of d16's mechanism tally; registered in domain 16.
  Get: https://esmats.eu/amspapers/pastpapers/pdfs/2022/kinnett.pdf (NTRS record 20230005798 is a preprint with no downloadable file)
  Save as `kinnett_green_klein_lin_2022_drill_feed_msl_in_flight_failure_ams.pdf`. Caltech copyright in-file, so extract only; never host.

## C. Needs a normal web browser (the publisher blocks automated downloads from this machine)

Open the link, use the site's own "Download PDF" button, and save under the name given.

- [x] **dziadura2023** (extracted in R73 from the publisher PDF in the Universidad de Alicante repository, https://rua.ua.es/server/api/core/bitstreams/4a71f48e-3b3d-4e8f-a0e7-f4e37baa1de5/content) (1) — NEA bulk densities from the Yarkovsky effect (Gaia DR3), A&A 680 A77.
  Get: https://www.aanda.org/articles/aa/pdf/2023/12/aa47342-23.pdf
  Save as `dziadura2023.pdf`. CC-BY, so it may be hosted.
- [ ] **harris_dabramo_2021** (1) — NEA population revisited (size-frequency, completeness), Icarus 2021. Free to read on ScienceDirect.
  Get: https://doi.org/10.1016/j.icarus.2021.114452
  Save as `harris_dabramo_2021.pdf`. No licence stated, so extract only.
- [x] **wilkinson_robinson_2000** (extracted in R73 from the NASA ADS scan, https://articles.adsabs.harvard.edu/pdf/2000M%26PS...35.1203W; the paper is M&PS 35:1203-1213) (1) — bulk densities of ordinary-chondrite meteorites (MAPS 35).
  Get: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1945-5100.2000.tb01509.x
  Save as `wilkinson_robinson_2000.pdf`. Free to read, no licence, so extract only.
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
- [x] **elkins_tanton_2020_psyche_preflight** (extracted in R73 from the benweiss.mit.edu author mirror) (7) — pre-flight composition assessment of 16 Psyche, JGR Planets (4.4 MB).
  Get: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7375145/ (or https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2019JE006296)
  Save as `elkins_tanton_2020_psyche_preflight.pdf`. CC-BY-NC, so extract only.
- [ ] **demeo_2009_bus_taxonomy_near_ir** (0) — Bus-DeMeo taxonomy definitions, Icarus 202. HAL author version.
  Get: https://hal.science/hal-00545286
  Save as `demeo_2009_bus_taxonomy_near_ir.pdf`. Extract only.
- [ ] **ryugu_soluble_organics_2023** (0) — Get: https://hal.science/hal-04208565/document — save as `ryugu_soluble_organics_2023.pdf`. Extract only.
- [ ] **ryugu_macromolecular_om_2023** (0) — Get: https://cnrs.hal.science/hal-04034418/document — save as `ryugu_macromolecular_om_2023.pdf`. Extract only.
- [x] **ryugu_ivuna_2023** (extracted in R73 from the Hokudai copy; supplementary xlsx still wanted, see status note) (4) — Get: https://eprints.lib.hokudai.ac.jp/dspace/bitstream/2115/90313/1/Science.pdf — save as `ryugu_ivuna_2023.pdf`. AAAS author copy, personal use only; never host.
- [x] **weinzierl2018** (extracted in R73 from Harvard DASH via https://dash.harvard.edu/server/api/core/bitstreams/2ba7bfe5-bb7a-491c-9a77-878ad3191b30/content) (1) — "Space, the Final Economic Frontier", JEP 32(2).
  Get: https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.32.2.173
  Save as `weinzierl2018.pdf`. Free from AEA. R73: the DASH copy's cover page says it is posted under DASH 'Other Posted Material (LAA)' terms, not CC BY, so extract only.
- [x] **epsc2022_context** (extracted in R73: the HTML abstract page is now readable without login) (0, context-only) — Get: https://doi.org/10.5194/epsc2022-106 — save as `epsc2022_context.pdf`. CC-BY abstract; low value.

---

## D. Needs library access or purchase (no free copy exists)

- [ ] **taylor2018** (0) — Δv map of the known main-belt asteroids, Acta Astronautica 146:73. Closed access; no preprint on arXiv.
  Get: https://doi.org/10.1016/j.actaastro.2018.02.014 (institutional login)
  Save as `taylor2018.pdf`. Extract only. **High value for the main-belt Δv rows.**
- [ ] **harris2015** (0, context-only) — Icarus 257, closed, and superseded by harris_dabramo_2021. Optional.
  Get: https://doi.org/10.1016/j.icarus.2015.05.004
- [ ] **schoenman_1992** (2) — AIAA-92-3800, 490 N engine test experience. NTRS has the abstract only; buy from AIAA. Optional.
  Get: https://arc.aiaa.org/ (search "AIAA-92-3800")
- [ ] **next_highpower_2025** (0) — JANNAF 2025 NEXT high-power paper. NTRS has a one-page abstract (re-checked R73: still `NEXTDischargeJANNAFvF3.pdf`, one page, no numbers); the full paper comes from JANNAF or the authors. Optional.
  Record: https://ntrs.nasa.gov/citations/20250006541

---

## E. Nothing to download

These are live services or datasets already pulled and used. Re-pull them only to refresh values.

`simda2024`, `jpl_sbdb_small_body_database`, `mp3c_minor_planet_physical_properties_catalogue`, `mpc_mpcorb_extended_designation_links` (182 MB, used only for designation links), `damodaran_cost_of_capital_by_industry` (103 rows), `gallagher_plane_talking_space_market_updates`, `lbma_precious_metals_fixings`, `asterank_neo_service_shoemaker_helin`, `jpl_msl_factsheet_curiosity_mass`.

---

## F. Registered in Round 74 and later, not yet sought (queue now 134 after R83)

R81 pulled one row out of this queue: `usgs_mineral_commodity_summaries_2026` is now full_text_hosted (pubs.usgs.gov reachable from this machine; full report + four chapters committed). R83 added eleven more rows to the queue (the domain-2 mineralogy citations, all Crossref-checked) and pulled `usgs_mineral_commodity_summaries_2025` out of it into full_text_hosted.


Round 74 registered every source the three upstream repos cite that this registry lacked. None has been fetched, so none is listed item by item here yet: the queue is every row of `sources.csv` whose `access_status` starts with `registered_not_pulled`, and each row already records its DOI or landing URL and what answered from this machine (Crossref metadata, HTTP status, or a bot block). 42 are T1 journal articles (Icarus, Nature, Science, A&A, MAPS) that will mostly land in section C or D; 55 are T4 grey sources (company pages, news, Wikipedia, vendor posts, software), which usually need no download, only a dated read of the page.

---

*Written 2026-09-27 after Round 70; updated after Rounds 72, 73 and 74. When a file has been extracted, its box is ticked and a research-log entry records the round.*

## R96 - Domain 10 methalox anchors (registered 2026-10-01; all full texts NOT sought this round)

- [ ] **ueda_et_al_2013_methane_fueled_engine_altitude_hot_fire_jpc** - AIAA JPC 49th proceedings, DOI 10.2514/6.2013-4056 (paywalled). If obtained: extract the altitude-condition thrust/Isp table for a LOX/methane engine; save as `ueda_et_al_2013_methane_fueled_engine_altitude_hot_fire_jpc.pdf`.
- [ ] **judd_et_al_2006_lox_methane_combustion_performance_stability_durability** - AIAA SciTech 44th proceedings, DOI 10.2514/6.2006-1533 (paywalled). If obtained: extract the performance/stability/durability trade-off figures; save as `judd_et_al_2006_lox_methane_combustion_performance_stability_durability.pdf`.
- [ ] **engelen_souverein_twigt_deimos_methane_oxygen_engine_test_results_jbis** - JBIS 62:211-218 (2009), BIS refcode 2009.62.211, ~GBP 5 per copy at https://www.bis-space.com/shop/product/deimos-methane-oxygen-rocket-engine-test-results/ . If obtained: extract the measured thrust/chamber-pressure/mass-flow tables + reusability assessment; save as `engelen_souverein_twigt_deimos_methane_oxygen_engine_test_results_jbis.pdf`.

## R99 - Domain 4 fairing-source sweep (registered 2026-10-02; full texts NOT sought this round)

The 31 sources registered for spacecost v0.5.0's fairing cells: one is now hosted (Atlas V UG Rev 11, public-domain statement in file), sixteen were verified live and read from their PDF text layers but not committed (manufacturer copyright or third-party mirror provenance — see the R99 FINDINGS block for exact figure evidence). The fourteen below still need a normal browser or library access:

- [ ] **nasa_nsts_21492_space_shuttle_payload_bay_users_guide** - NASA program document NSTS 21492 (Space Shuttle Program Payload Bay Payload User's Guide, s4.0: max payload dimensions 720 in x 180 in, "a volume of 10,600 cubic feet"). Not located via NTRS search from this machine under the document number or title phrases tried; try a NASA history office / shuttle program library route. If obtained: extract s4.0 verbatim incl. the metric conversions upstream flags as self-inconsistent; save as `nasa_nsts_21492_space_shuttle_payload_bay_users_guide.pdf`.
- [ ] **douglas_sm47274_saturn_v_payload_planners_guide_nov1965** - Douglas SM-47274 (Nov 1965), prime payload configuration A "about 3,230 cubic feet". archive.org item `SaturnVPayloadPlannersGuide` exists but its files DNS-failed from this machine in three attempts; retry the item's file list or use a NASA history office copy. If obtained: extract the configuration-A volume statement + fairing dimensions; save as `douglas_sm47274_saturn_v_payload_planners_guide_nov1965.pdf`.
- [ ] **vega_users_manual_issue4_apr2014** - Arianespace Vega User's Manual Issue 4 (Apr 2014), Fig 5.3.2a usable volume inside the Vega fairing. Original URL now HTTP 410 Gone; post-migration ariane.group path 404; web.archive.org unreachable from this machine — try from any other network or an Arianespace document request. If obtained: extract Fig 5.3.2a dimensions; save as `vega_users_manual_issue4_apr2014.pdf`.
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

Pulled + committed to `14_propellant_consumable_prices/full_texts/` (queue now 149 after R100):
- [x] **inl_rpt_23_75203_krypton_xenon_recovery_cost_benefit** - INL/RPT-23-75203, Cost-Benefit Assessment of Krypton and Xenon Recovery from Aqueous Reprocessing (Sept 2023), pulled from inldigitallibrary.inl.gov via the OSTI record osti.gov/biblio/2377416. U.S.-government-work disclaimer on p.2 -> public domain, hosted.
- [x] **iea_global_hydrogen_review_2024** - IEA Global Hydrogen Review 2024 (published 02 October 2024), pulled from iea.blob.core.windows.net via the official landing page; 'IEA. CC BY 4.0.' on every page -> hosted, context-only for now (cost figures are vector charts).

Still blocked / dead this round:
- [ ] **dla_energy_aerospace_standard_prices_fy2020** - FY20/FY24/FY25 PDF URLs and the landing page all answer HTTP 403 from this machine (bot protection, not worked around); web.archive.org is DNS-blocked here. Would anchor hydrazine $30.5/kg, MMH/NTO in one document.
- [ ] **aqua_calc_lox_bulk_price** - still answers HTTP 403 from this machine.
- [x] **evonik_peroxide_propulsion_htp_quotes_2024** (dead source, nothing to download) - peroxidepropulsion.com has been hijacked and now serves casino/baby-products spam; the original Evonik HTP ~$5/kg quote is gone. Upstream's citation points at a dead URL; re-source from an active supplier before this row can back anything.
## R101 - Domain 14 LH2 production-cost anchors (registered 2026-10-02; both full texts pulled and hosted this round)

Pulled + committed to `14_propellant_consumable_prices/full_texts/` (queue unchanged at 149 after R101):
- [x] **nasa_cr_73226_study_cost_system_analysis_lh2_production** - NASA CR 73226, Study/Cost/System Analysis of Liquid Hydrogen Production (June 1968), pulled from NTRS record 19680018755; determination GOV_PUBLIC_USE_PERMITTED -> hosted.
- [x] **nasa_cr_159163_economics_hydrogen_production_liquefaction_updated_1980** - NASA CR 159163, Economics of Hydrogen Production and Liquefaction Updated to 1980 (Nov 1979), pulled from NTRS record 19800002991; determination GOV_PUBLIC_USE_PERMITTED -> hosted.

Documented negative finding this round: the 'commercial $75.8/kg (AIAA 2024)' hydrazine citation in spacecost's propellants.csv resolves to no indexed paper anywhere reachable from this machine (Crossref AIAA JPC sweep + NTRS searches) - nothing to download until a specific DOI is identified; the DLA FY20 row above remains the only institutional anchor for that cell.
## R102 - Domain 12 first hosted sources (registered 2026-10-02; eight rows pulled and committed this round incl. one NEW source, queue 149 -> 142)

Pulled + committed to `12_destination_environments_physical_constants/full_texts/`:
- [x] **iau_2012_resolution_b2_astronomical_unit** - IAU Resolution B2 PDF (syrte.obspm.fr mirror of the official text).
- [x] **bipm_si_brochure_9th_edition** - SI Brochure 9th edition, English (BIPM; CC BY 4.0 statement on p.2 of the file).
- [x] **nasa_nssdca_moon_fact_sheet** / **nasa_nssdca_mars_fact_sheet** / **nasa_iss_facts_and_figures** - HTML snapshots of the live US Government pages at the exact URLs upstream cites.
- [x] **appelbaum_flood_1989_tm102299_solar_radiation_mars** - NASA TM-102299 from NTRS record 19890018252 (GOV_PUBLIC_USE_PERMITTED).
- [x] **daly_2023_dart_kinetic_impact** - Nature 616:443 PDF via the publisher's own article link (in-file CC BY 4.0 statement p.5).
- [x] **thomas_2023_dimorphos_orbital_period_change** (NEW source registered this round) - Nature 616:448 companion paper, PDF via the publisher's own article link (in-file CC BY 4.0 statement p.4); carries the measured −33.0 min orbital-period change upstream's Didymos row points at.

Still blocked from this machine after R102 re-checks (routes recorded per row in the domain CSV): science.org PDFs HTTP 403 x3; Elsevier no-open-copy x3; Kopp & Lean TSI - AGU legacy 403 + Wiley pdfdirect bot-blocked despite OpenAlex OA flag; CODATA RMP APS paywall + NIST CUU Cloudflare challenge; ITU-R S.1003 free-download endpoints all failing (landing page live).
