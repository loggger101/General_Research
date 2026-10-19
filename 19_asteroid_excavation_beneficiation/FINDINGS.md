# Domain 19 — Asteroid excavation throughput & beneficiation

Backings: economicspace `modules/calc.py` mining and beneficiation fields (`mining_rate_kg_per_day_per_kg_rig`, `mining_hardware_kg`, `max_mining_duration_yr`, `station_keeping_floor_yr`, `beneficiation_recovery`, `max_concentration_ratio`) and spacecost `reference/operational_costs.csv` rows `Drilling / excavation energy`, `Beneficiation / on-site processing energy` and `In-space processing plant throughput`; since R76 also economicspace `modules/mineral_value.py` `IN_SPACE_PROCESSING_KWH_PER_KG` (in-space refining energy).

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` `mining_rate_kg_per_day_per_kg_rig` | 0.10 (a 2,000 kg rig moves 200 kg/day) | "an engineering assumption, not a measurement"; TAGSAM (~122 g per touch) for scale |
| `calc.py` `mining_hardware_kg` | 2,000 kg | none stated |
| `calc.py` `max_mining_duration_yr` / `station_keeping_floor_yr` | 3.0 yr / 0.25 yr | none stated |
| `calc.py` `beneficiation_recovery` | 0.90 | "Terrestrial PGM / sulphide flotation circuits run 85-95%"; no source, no microgravity heritage |
| `calc.py` `max_concentration_ratio` | 50:1 | "Terrestrial mills run 100:1 to 1000:1 on PGM ores"; no source |
| `Drilling / excavation energy` | 200 Wh/kg [50, 500] of regolith | "Zacny et al. (NIAC studies ...)", not identifiable (R74) |
| `Beneficiation / on-site processing energy` | 500 Wh/kg [100, 2000] of refined product | a school worksheet, withdrawn in spacecost 0.5.1 (R112) |
| `In-space processing plant throughput` | 100 kg/yr per kg of plant [20, 500] | "Terrestrial smelters run 1,000x their own mass per year", derated tenfold |

**What a source has to supply:** measured excavation rates and specific energies in reduced gravity or vacuum with machine mass; recovery and grade of magnetic and electrostatic metal-silicate separation, and terrestrial comminution energies; throughput-to-mass of compact plants; terrestrial autonomous-mining analogues for scale.

**Also relevant, registered elsewhere:** `metzger_zacny_2020` (d05), `hein2020` (d22; R61 recorded a plant-throughput discrepancy).

**Boundary:** domain 5 keeps volatile extraction, ISRU propellant processing and storage; domain 2 what the body contains. This domain covers getting ore out and concentrating it.

## R76 - Scope extended to in-space refining energy (2026-09-27)

| cell | current value | upstream's stated basis |
|---|---|---|
| economicspace `mineral_value.py` `IN_SPACE_PROCESSING_KWH_PER_KG` | kWh per kg of feedstock: Fe, Ni, Co, Cu, nickel-iron, awaruite 5.0; magnetite 7.0; troilite 4.0; carbon, organics 2.0; silicates 1.0; water 0.5 | "Terrestrial electric-arc / direct-reduction steelmaking runs 4-5 kWh/kg; electrowinning iron is similar"; no source |
| economicspace `mineral_value.py` `_INSPACE_PLANT_LIFE_YR` | 15 yr | none stated; same as `Mining rig service life` (domain 16) |

Needed: specific energies of reducing, melting and forming Fe-Ni and sintering silicates, for space or small plants.

## R77 - Sources moved in (2026-09-27)

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `just_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round-10, 43, 44 and 57 additions | `extracted_data/r43_excavation_energy_key_numbers.csv` |
| `zeng_2007` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r70_zeng_2007.csv`, `full_texts/zeng_2007_excavation_force.pdf` |
| `proctor_apex_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition; R71 | `extracted_data/r71_proctor_apex_2019_key_numbers.csv` |
| `zeitlin_asteroid_excavation_project` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r71_zeitlin_asteroid_excavation_project_key_numbers.csv` |
| `ssap_2021` | domain 5 | `05_inspace_operations/FINDINGS.md`: the `ssap_2021` block; Round-3 additions; Maintenance; R71 | `extracted_data/ssap_2021_table3_theoretical_yields.csv`, `extracted_data/r71_ssap_2021_key_numbers.csv`, `extracted_data/r71_ssap_2021_reactions_energetics.csv` |

rc-026 and rc-027 (Drilling / excavation energy) are written up in domain 5. `metzger_zacny_2020` stays in domain 5 (thermal volatile extraction).

## R112 - Beneficiation citation withdrawn upstream (2026-10-04)

spacecost 0.5.1 (`85da36c`) applied rc-048: the beneficiation row now calls its 500 Wh/kg [100, 2000] an unsourced estimate. The worksheet was rejected by the owner and rc-048 deleted with it. The cell still needs a specific energy for magnetic, electrostatic or thermal concentration per kg of concentrate.

## R113 - Two unread candidates (2026-10-04)

Both paywalled, `registered_not_pulled`: `tang_et_al_2023_asteroid_rock_mechanical_properties` (Engineering Geology 321:107154; asteroid rock mineralogy and strength, for the excavation row and mining rate) and `liu_et_al_2026_asteroid_laser_mining_cryogenic_vacuum` (Chem. Eng. Res. Des. 233:150-161; laser processing of simulants with Fe-Ni enrichment, for recovery and concentration ratio).

## R114 - Measured excavation energy, thermal and optical mining, PGM recovery (2026-10-04; +13)

**Excavation energy:** `giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru` (4.8 kg bucket drum: 777.54 kg/h at 0.022 Wh/kg continuous, 172.02 kg/h at 0.86 Wh/kg batch) and `kafi_2026_spiral_cavity_wheel_excavator_lunar_isru` (29% below a bucket drum) are orders of magnitude under 200 Wh/kg, a floor for loose regolith. `schuler_2022_isru_pilot_excavator_bucket_drum_scaling`: a 30 kg-class excavator for 10,000 kg of regolith (RASSOR 2.0 is 65 kg). `jayathilake_2022_geotechnical_parameters_lunar_regolith_excavations` and `ricardo_2026_trafficability_excavatability_icy_lunar_regolith_cone_penetration` from abstract.

**Thermal and optical mining:** `sowers_2020_niac_phase1_thermal_mining_of_ices` (read in full; the Colorado School of Mines copy, since the owner's copy differs: 'February 2019' vs 'February 2020'), probably the NIAC study the row meant: 126 kg/h of ice; 42.0 kg of annual propellant per kg of plant vs 2.3 for Langley's excavation-based plant (`jones_klovstad_komar_judd_2018_cost_breakeven_cislunar_isru`, d22). `techport_33509_optical_mining_asteroid_excavation_sbir` (a 100 t water claim), `broslav_2025_optical_mining_carbonaceous_chondrite_simulants` (abstract), `sercel_2018_time_dependent_outgassing_model_bulk_heating` (simple heating "too slow for industrial water yield").

**PGM recovery (0.90):** `liddell_adams_2012_kell_hydrometallurgical_process_pgm_base_metals` and `liddell_2019_kell_hydrometallurgical_extraction_piloting_engineering_implementation`: above 95% for value metals; capex 18-33% and opex 51-66% of smelting and refining. `kabemba_2025_geometallurgical_framework_flotation_kinetics_platreef_pgm`: batch flotation 83.25-94.37% (the owner's "90.6%" is the liberated share). `hay_2010_optimising_ug2_flotation_part2_modelling_pgm_recovery_cr2o3_rejection`: title only. All terrestrial analogues.

`extracted_data/r114_gr_links_key_numbers.csv`. No candidate.

## R119 / R120 - Excavation and recovery papers hosted (2026-10-05)

- giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru hosted (CC BY) as full_texts/giel_et_al_2025_bucket_drum_excavator_moonbot_arxiv2511.00492.pdf: "The resulting tool weighs 4.8 kg and has a volume of 14.06 L"; the R114 figures confirmed.
- ricardo_2026_trafficability_excavatability_icy_lunar_regolith_cone_penetration: the journal version's in-file licence is CC BY-NC-ND (Crossref says cc-by), so the CC BY Research Square preprint is hosted as full_texts/ricardo_hodgkinson_rhamdhani_et_al_2026_trafficability_excavatability_icy_lunar_regolith_research_square_rs-9421896_ccby.pdf: cone penetration of unsintered, pressure-sintered, ice-cemented and vapour-deposited icy simulants.
- kafi_2026_spiral_cavity_wheel_excavator_lunar_isru read in full from arXiv (default licence, not hosted).
- `kabemba_2025_geometallurgical_framework_flotation_kinetics_platreef_pgm` hosted (CC BY) as kabemba_mutombo_waters_2025_geometallurgical_framework_flotation_kinetics_platreef_pgm_minerals_15_701_mdpi_ccby.pdf: "P-FPX3 = 83.25%" and "peak recovery (94.37%)".

## R137 - NASA's ISRU staging ladder (2026-10-09)

**mueller_sibille_sanders_jones_2014_arrm_concepts_of_operations_isru_ladder** (NTRS 20140017854, hosted; context only): resource operations for "radiation protection, propulsion, life support, shelter and manufacturing", within a campaign preparing for Mars: "the development and demonstration approach progresses from resource prospecting (understanding the resource, and mapping the 'ore body'), mining/extraction feasibility and product assessment, pilot operations, to full in-situ resource utilization (ISRU)." No cost, mass or delta-v figures.

## R152 - rc-027 unblocked: measured excavation energies and DOE's mining benchmark (2026-10-12)

rc-027 (200 Wh/kg, range 50-500, spacecost@0b716ad) no longer needs just_2019's table. `extracted_data/r152_excavation_specific_energy_key_numbers.csv`:

| source | what was measured | Wh/kg |
|---|---|---|
| schuler_2022_isru_pilot_excavator_bucket_drum_scaling (IPEx, p14 Fig. 15; read from vector markers) | mechanical energy at the drum per kg, three drums, two cut depths, 10 and 30 mm/s | 0.0029-0.0071 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p5 Table IV) | a literature bucket drum, continuous | 0.007-0.02 |
| kafi_2026_spiral_cavity_wheel_excavator_lunar_isru (p5) | spiral-cavity wheel and two baselines, 44.2-83.5 J/kg | 0.012-0.023 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p4-p5) | MoonBot bucket drum, continuous | 0.022 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p5 Table IV) | RASSOR 2.0, batch (just_2019's 0.761) | 0.76 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p5 Table III) | MoonBot batch cycle incl. unloading and 139 s driving (0.864 recomputed) | 0.86 |
| doe_2007_mining_industry_energy_bandwidth_study (Exhibit 24) | US metal mining: drilling + blasting + digging, 17,700 Btu/ton | 5.72 |
| doe_2007_mining_industry_energy_bandwidth_study | all extraction incl. ventilation and dewatering, 23,000 Btu/ton | 7.43 |
| doe_2007_mining_industry_energy_bandwidth_study | extraction plus diesel haulage, 97,900 Btu/ton | 31.63 |
| doe_2007_mining_industry_energy_bandwidth_study | whole mine incl. crushing, grinding and separation, 168,746 Btu/ton | 54.51 |

**doe_2007_mining_industry_energy_bandwidth_study** (US DOE ITP, BCS Inc., June 2007; new; contractor-prepared, no licence, not hosted): Exhibit 24 read from a page render (text layer scrambled), subtotal 162,148 matches its components; short tons assumed (metric lowers each figure 9.3%); with generation losses (Exhibit 14) metals run 342,200 Btu/ton = 110.5 Wh/kg.

Upstream's 200 Wh/kg is 3.7x a whole terrestrial metal mine including comminution (which spacecost prices separately at 500 Wh/kg; DOE crushing and grinding alone is 19.3 Wh/kg), and 6.3x extraction plus haulage; the 500 end is 9.2x the whole mine. rc-027 re-opened: move to ~1-10 Wh/kg (about 6 for drilling, blasting and digging), range ~0.01-32, or keep 200 and say what beyond excavation it carries. Caveat: lunar figures are loose simulant at 1 g, DOE's terrestrial ore; nothing measures asteroid rock.

## R164 / R165 - Candidates (2026-10-14)

rc-097 (cite DOE's 19.3 Wh/kg beneficiation), rc-122 (cite Kabemba's 83.25-94.37% and Liddell's >95%), rc-136 (give the mining-rate dial its plant-scale references: 42.0 vs 2.3 kg/yr per kg of plant). Texts in `revision_candidates.csv`.

## R207 - Refinery throughput row vs institutional ISRU bounds (rc-178)

The spacecost `In-space processing plant throughput` row (100 kg processed per year per kg of
plant, band 20-500) is justified only by an uncited analogy: "Terrestrial smelters run 1,000x their
own mass per year" [count==1]. No institutional in-space processing rate is named for it anywhere.

The sister row two lines away, `ISRU propellant plant throughput`, IS institutionally anchored - its
own note prints the derivation 11.67 t / 0.616 yr / 2.6 t = 7.28 from Kleinhenz & Paz PTMSS/SRR 2021,
and CITATIONS.md L138-139 name both K&P papers for it (band high 13.3 from AIAA-2017: 1.7 mT hardware,
6,978 kg CH4 + 22,728 kg O2 over 480 days). Recomputed live from the hosted PDFs' printed figures:

| K&P case | basis | kg processed/yr/kg plant | refinery row multiple |
|---|---|---|---|
| PTMSS ridge chain (2.6 t) | product=feedstock mass | 7.286 | point x13.7 / floor x2.74 |
| PTMSS whole baseline (4.9 mT incl mine) | same | 3.866 | point x25.9 / floor x5.17 |
| AIAA-2017 Mars hardware (1.7 mT) | product side only | 13.297 | point x7.5 / floor x1.50 |

So the refinery band's FLOOR sits ~1.5x above the best institutional figure and its POINT value
runs 8-26x past it, in spacecost's own units. Economicspace consumes the row live as `refinery_rate`
(modules/calc.py L7618; master.py L11125) with an unsourced restated fallback constant at master.py
L1757 (count==1). Their verification_sheet #150 backing ledger flags this input (I89) as needing
backing independently. rc-178 proposes naming both papers as bound references on the note and a
CITATIONS.md entry; value decision left open, no re-pin.

STANDING SEAM NOTE for future rounds: that same backing ledger names 99 inputs needing backing - most map onto
open candidates already (rc-086..177 cover operational/storage/propellant/mineral cells). Remaining unclaimed
classes seen while triaging it: the physics/dv constants restated uncited in campaign/worked_calculation.py L103-124
(mu_E, v_E, r_LEO, R_MOON, DV_NRHO=0.450 - which MATCHES the sourced delta_v_segments NRHO-insertion row 450 m/s),
the search-method dials (ladder rungs, fleet max) and the Cap_* market-routing ceilings; those are judgment or
self-derived by design. The sister-row band [7.28,13.3] is anchored - do not re-litigate it here.
