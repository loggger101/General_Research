# Domain 19 — Asteroid excavation throughput & beneficiation

Backings: economicspace `modules/calc.py` mining and beneficiation fields (`mining_rate_kg_per_day_per_kg_rig`, `mining_hardware_kg`, `max_mining_duration_yr`, `station_keeping_floor_yr`, `beneficiation_recovery`, `max_concentration_ratio`) and spacecost `reference/operational_costs.csv` rows `Drilling / excavation energy`, `Beneficiation / on-site processing energy` and `In-space processing plant throughput`; since R76 also economicspace `modules/mineral_value.py` `IN_SPACE_PROCESSING_KWH_PER_KG` (in-space refining energy).

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

These fields size the haul, and upstream calls the mining rate "an engineering assumption, not a measurement". The beneficiation-energy row cites a school worksheet (rc-048; withdrawn upstream in spacecost 0.5.1, see R112), and the drilling-energy row cites NIAC studies too vague to register in R74. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` `mining_rate_kg_per_day_per_kg_rig` | 0.10 (a 2,000 kg rig moves 200 kg/day) | "an engineering assumption, not a measurement"; OSIRIS-REx TAGSAM (~122 g per touch) quoted for scale |
| `calc.py` `mining_hardware_kg` | 2,000 kg | none stated |
| `calc.py` `max_mining_duration_yr` / `station_keeping_floor_yr` | 3.0 yr / 0.25 yr | none stated |
| `calc.py` `beneficiation_recovery` | 0.90 | "Terrestrial PGM / sulphide flotation circuits run 85-95%"; no source, and no microgravity heritage |
| `calc.py` `max_concentration_ratio` | 50:1 feed to concentrate | "Terrestrial mills run 100:1 to 1000:1 on PGM ores"; no source |
| `Drilling / excavation energy` | 200 Wh/kg [50, 500] of regolith extracted | "Zacny et al. (NIAC studies ...)", not identifiable (R74) |
| `Beneficiation / on-site processing energy` | 500 Wh/kg [100, 2000] of refined product | "NASA Money-Mass-ematics 2023", a grades 7-8 worksheet (rc-048; withdrawn upstream in spacecost 0.5.1, see R112) |
| `In-space processing plant throughput` | 100 kg/yr per kg of plant [20, 500] | "Terrestrial smelters run 1,000x their own mass per year", derated tenfold by judgement |

**What a source has to supply.**

- Measured excavation rates and specific energies for loose regolith and consolidated rock in reduced gravity or vacuum (drills, bucket wheels, pneumatic systems), from tests rather than concept claims, with the machine mass so a rate per kg of rig can be formed.
- Recovery and grade data for magnetic and electrostatic separation of metal from silicate, on meteorite or simulant feeds, and terrestrial comminution and separation specific energies.
- Throughput-to-mass ratios of compact or modular processing plants.
- Terrestrial remote and autonomous mining analogues, recorded for scale.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `metzger_zacny_2020` (domain 5): excavation.
- `zeng_2007` (domain 5): excavation.
- `just_2019` (domain 5): excavation.
- `hein2020` (domain 2): beneficiation cost structure; R61 recorded a plant-throughput discrepancy against the row.

**Boundary.** Domain 5 keeps volatile extraction (water-liberation energy, volatile recovery), ISRU propellant processing (`isru_processing_usd_per_kg`) and storage; domain 2 keeps what the body contains. This domain covers getting ore out of the body and concentrating it.

## R76 - Scope extended to in-space refining energy (2026-09-27; registry unchanged)

Found while looking for new domains in economicspace@1f470d4 and spacecost@e831245; no source was sought. The energy to turn raw feedstock into a usable in-space product sits next to this domain's plant-throughput row (the same code reads both), so it joins this domain rather than opening its own:

| cell | current value | upstream's stated basis |
|---|---|---|
| economicspace `mineral_value.py` `IN_SPACE_PROCESSING_KWH_PER_KG` | kWh per kg of feedstock: Fe, Ni, Co, Cu, nickel-iron, awaruite 5.0; magnetite 7.0; troilite 4.0; carbon, organics 2.0; silicates 1.0; water 0.5 | metals: "Terrestrial electric-arc / direct-reduction steelmaking runs 4-5 kWh/kg; electrowinning iron is similar"; no source |
| economicspace `mineral_value.py` `_INSPACE_PLANT_LIFE_YR` | 15 yr, over which the refinery is amortised | none stated; the same figure as `Mining rig service life` (domain 16) |

What a source has to supply: specific energies of reducing, melting and forming iron-nickel metal and of sintering silicates, measured or designed for space or for small terrestrial plants.

## R77 - Sources moved in (2026-09-27; registry unchanged at 267)

These rows were registered in other domains before this one existed; they moved here because the cells they back are this domain's. Their earlier write-ups stay in the old domain's FINDINGS.md under the blocks named.

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `just_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round-9 status; Round-10 addition; Round 43 addition; Round 44 addition; Round 57 addition | `extracted_data/r43_excavation_energy_key_numbers.csv` |
| `zeng_2007` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r70_zeng_2007.csv`, `full_texts/zeng_2007_excavation_force.pdf` |
| `proctor_apex_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition; R71 | `extracted_data/r71_proctor_apex_2019_key_numbers.csv` |
| `zeitlin_asteroid_excavation_project` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r71_zeitlin_asteroid_excavation_project_key_numbers.csv` |
| `ssap_2021` | domain 5 | `05_inspace_operations/FINDINGS.md`: the `ssap_2021` block; Round-3 additions; Round-3 status; Maintenance; R71 | `extracted_data/ssap_2021_table3_theoretical_yields.csv`, `extracted_data/r71_ssap_2021_key_numbers.csv`, `extracted_data/r71_ssap_2021_reactions_energetics.csv` |

Revision candidates on these sources, written up in their old domains: rc-026 (open, Drilling / excavation energy), rc-027 (blocked, Drilling / excavation energy).

The cross-references to `zeng_2007` and `just_2019` in the opening block are now rows of this domain. `hein2020`, listed in the opening block under domain 2, is now in domain 22.

`metzger_zacny_2020` stays in domain 5: its row maps to the drilling-energy row, but the paper is about thermal extraction of volatiles, which domain 5 keeps.
## R85 - just_2019 retry (2026-09-30; registry unchanged by this note)

Retried the three routes that could host `just_2019`: OpenAlex best_oa_location (= the ScienceDirect PDF route itself, Cloudflare challenge still blocks this machine), UoM Research Explorer publication record (page 404 / no file behind it) and a USRA Lunar ISRU workshop proceedings copy of the conference version (1-page abstract only - not the full text and without the specific-energy tables rc-027 needs). Status unchanged: open_not_pulled; **rc-027 remains blocked**.

## R112 - Beneficiation-energy citation withdrawn upstream; worksheet rejected (2026-10-04; registry -1)

spacecost 0.5.1 (data contract 1.17.1, tag `v0.5.1`, merge commit `85da36c`) applied rc-048: the `Beneficiation / on-site processing energy` row of `operational_costs.csv` no longer cites "NASA Money-Mass-ematics 2023" and now calls its 500 Wh/kg [100, 2000] of refined product an unsourced engineering estimate. No value moved.

The worksheet was rejected by owner decision (INDEX.md "Rejected sources"). rc-048 rested on it alone, so it was deleted with the rejection, as README "Rejecting a source" step 6 requires; its number is not reused. The cell is unchanged in this domain's brief: it still needs a measured or designed specific energy for magnetic, electrostatic or thermal concentration, per kg of concentrate.

## R113 - Two unread candidates for the excavation and beneficiation cells (2026-10-04; +2 sources, T1x2)

From the owner's list. Both DOIs were verified on Crossref; ScienceDirect serves a CAPTCHA to this machine and both are paywalled, so neither abstract nor full text was read and both are `registered_not_pulled`.

- `tang_et_al_2023_asteroid_rock_mechanical_properties` (Engineering Geology 321:107154): by its title, mineral make-up and macroscale strength of asteroid rock, the property the `Drilling / excavation energy` row (200 Wh/kg, its NIAC citation unidentifiable since R74) and `mining_rate_kg_per_day_per_kg_rig` lack.
- `liu_et_al_2026_asteroid_laser_mining_cryogenic_vacuum` (Chemical Engineering Research and Design 233:150-161): the owner's list marked it unverified and doubted its relevance; the Crossref title shows laser processing of asteroid simulants with Fe-Ni enrichment in cryogenic vacuum, the in-space concentration step behind `beneficiation_recovery` (0.90) and `max_concentration_ratio` (50:1).

What each supplies is unknown until read; both are on DOWNLOADS.md.

## R114 - Measured excavation energy, optical and thermal mining, and PGM recovery (2026-10-04; +13 sources, T1x7, T2x6)

Thirteen sources from the owner's excavation and beneficiation blocks. **Excavation energy.** The `Drilling / excavation energy` row is 200 Wh/kg. Two 2025-26 preprints report measured specific energies for light lunar excavators in loose regolith: `giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru` (a 4.8 kg bucket drum: 777.54 kg/h at 0.022 Wh/kg continuous, 172.02 kg/h at 0.86 Wh/kg batch) and `kafi_2026_spiral_cavity_wheel_excavator_lunar_isru` (a wheel with 29% lower specific energy than a bucket drum). Both are orders of magnitude under 200 Wh/kg, which is a hard-rock figure, so they set a floor for loose regolith rather than contradict the row and no revision candidate is opened; `schuler_2022_isru_pilot_excavator_bucket_drum_scaling` gives the rig-mass side (a 30 kg-class excavator for 10,000 kg of regolith; RASSOR 2.0 is 65 kg). `jayathilake_2022_geotechnical_parameters_lunar_regolith_excavations` and `ricardo_2026_trafficability_excavatability_icy_lunar_regolith_cone_penetration` are registered from record or abstract only.

**Thermal and optical mining.** `sowers_2020_niac_phase1_thermal_mining_of_ices` (read in full) is probably the NIAC study the row cited; its point design collects 126 kg/h of ice and its plant efficiency is 42.0 kg of annual propellant per kg of plant mass against 2.3 for the Langley excavation-based plant (`jones_klovstad_komar_judd_2018_cost_breakeven_cislunar_isru`, domain 22). The owner's link was a third-party copy that differs from the Colorado School of Mines file (10,405,776 against 10,436,681 bytes; title page 'February 2019' against 'February 2020'), so the CSM copy was used. `techport_33509_optical_mining_asteroid_excavation_sbir` (a 100 t water claim), `broslav_2025_optical_mining_carbonaceous_chondrite_simulants` (measured excavation rates, abstract only) and `sercel_2018_time_dependent_outgassing_model_bulk_heating` (simple heating 'too slow for industrial water yield') cover the volatile-rich case.

**PGM recovery** (`beneficiation_recovery` 0.90): `liddell_adams_2012_kell_hydrometallurgical_process_pgm_base_metals` and `liddell_2019_kell_hydrometallurgical_extraction_piloting_engineering_implementation` report above 95% for value metals and capex 18-33% and opex 51-66% of smelter-refining; `kabemba_2025_geometallurgical_framework_flotation_kinetics_platreef_pgm` reports 83.25-94.37% batch flotation recovery (the owner's '90.6% recovery' is the liberated share of PGMs, not a recovery); `hay_2010_optimising_ug2_flotation_part2_modelling_pgm_recovery_cr2o3_rejection` is title-only. All are terrestrial ores, analogues at best.

Rejected: a 16-page slide deck with no numbers, a press release, a trade explainer, a personal blog, a model-only conference abstract and an off-topic lightcurve paper (Round 114 log entry). Undecided: a J-STAGE paper (connection reset), a dead blog URL and an unresolved 2016 Sercel programme paper. The list's Just 2019 and Zeng 2007 entries are already registered.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.
## R116 - just_2019 retry (2026-10-04; registry unchanged by this note)

Retried the routes that could host `just_2019`: the Elsevier TDM API (`api.elsevier.com/content/article/PII:S003206331930162X?httpAccept=text/plain&view=fulltext` -> HTTP 401 AUTHENTICATION_ERROR - a registered API key is required and none exists on this machine), UCL Discovery (intermittent: one search query returned a results page but no `just_2019` record; all subsequent queries now get an HTTP 403 Cloudflare challenge, and the EPrints REST endpoint `/cgi/rest` answers 404 - the eprint route is dead from this machine) and Manchester Pure (publication URL still HTTP 404). Status unchanged: open_not_pulled; **rc-027 remains blocked**.

## R119 - giel_2025 pulled live from arXiv and hosted, CC BY 4.0 (2026-10-05; queue -1)

**giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru [T2]** - re-classed registered_not_pulled -> full_text_hosted. PDF pulled live via export.arxiv.org/pdf/2511.00492v1; committed to full_texts/giel_et_al_2025_bucket_drum_excavator_moonbot_arxiv2511.00492.pdf (495,736 B sha256=6093a7e0b692f49f0d58cd3c1c227eebc106c0c7fef109b51648cbb2afa3e96a). 6 pages, no in-file copyright statement so the abs-page CC BY 4.0 governs (checked live). The R114 abstract figures are now backed by the hosted full text: "The resulting tool weighs 4.8 kg and has a volume of 14.06 L." and "It is capable of continuous excavation at a rate of 777.54 kg/h, with a normal-ized energy consumption of 0.022 Wh/kg. (the word normalized is split across a line break in the PDF text layer), with batch operation at 172.02 kg/h / 0.86 Wh/kg - a measured excavation specific energy for the lightweight-tool case behind d19's `Drilling / excavation energy` row (context; no re-pin).
## R120 - ricardo_2026 preprint hosted (journal version is BY-NC-ND); kafi_2026 read in full, not hostable (2026-10-05; queue -2)

**ricardo_2026_trafficability_excavatability_icy_lunar_regolith_cone_penetration [T1]** - re-classed registered_not_pulled -> full_text_hosted. The Springer journal version now pulls live, but its IN-FILE licence is 'Creative Commons Attribution-NonCommercial-NoDerivatives 4.0' while Crossref tags it cc-by (discrepancy flagged per the R97 source-inconsistency convention) - so we host the explicitly CC BY 4.0 Research Square preprint instead: pulled from researchsquare.com/article/rs-9421896/latest.pdf and committed to full_texts/ricardo_hodgkinson_rhamdhani_et_al_2026_trafficability_excavatability_icy_lunar_regolith_research_square_rs-9421896_ccby.pdf (7,430,744 B sha256=b3b407473d3f43c3ba1c59e5d511d37b29a342ca79d98d7bd4990d2b446a1b97). 53 pages; in-file 'This work is licensed under a Creative Commons Attribution 4.0 International License'. Verbatim title: "Trafficability and excavatability of icy lunar regolith simulants quantified using cone penetration. Cone-penetration data on unsintered / pressure-sintered / ice-cemented / vapour-deposited icy lunar regolith simulants - already cited by r114_gr_links_key_numbers.csv.

**kafi_2026_spiral_cavity_wheel_excavator_lunar_isru [T2]** - re-classed registered_not_pulled -> verified_live_not_pulled. PDF pulled live via export.arxiv.org/pdf/2609.25724 and read in full, but NOT hostable (default non-exclusive distribution licence only); hash recorded (10,103,383 B sha256=3a8ed7620d7e8f381a3b1108b43944985a7000f17ea8f03c1d4c15da81fa0e42). Verbatim: {Q+q_kafi} - benchtop spiral-cavity wheel data behind d19's excavation-energy row.