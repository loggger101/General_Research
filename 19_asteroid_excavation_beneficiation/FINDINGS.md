# Domain 19 — Asteroid excavation throughput & beneficiation

Backings: economicspace `modules/calc.py` mining and beneficiation fields (`mining_rate_kg_per_day_per_kg_rig`, `mining_hardware_kg`, `max_mining_duration_yr`, `station_keeping_floor_yr`, `beneficiation_recovery`, `max_concentration_ratio`) and spacecost `reference/operational_costs.csv` rows `Drilling / excavation energy`, `Beneficiation / on-site processing energy` and `In-space processing plant throughput`; since R76 also economicspace `modules/mineral_value.py` `IN_SPACE_PROCESSING_KWH_PER_KG` (in-space refining energy).

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

These fields size the haul, and upstream calls the mining rate "an engineering assumption, not a measurement". The beneficiation-energy row cites a school worksheet (rc-048), and the drilling-energy row cites NIAC studies too vague to register in R74. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` `mining_rate_kg_per_day_per_kg_rig` | 0.10 (a 2,000 kg rig moves 200 kg/day) | "an engineering assumption, not a measurement"; OSIRIS-REx TAGSAM (~122 g per touch) quoted for scale |
| `calc.py` `mining_hardware_kg` | 2,000 kg | none stated |
| `calc.py` `max_mining_duration_yr` / `station_keeping_floor_yr` | 3.0 yr / 0.25 yr | none stated |
| `calc.py` `beneficiation_recovery` | 0.90 | "Terrestrial PGM / sulphide flotation circuits run 85-95%"; no source, and no microgravity heritage |
| `calc.py` `max_concentration_ratio` | 50:1 feed to concentrate | "Terrestrial mills run 100:1 to 1000:1 on PGM ores"; no source |
| `Drilling / excavation energy` | 200 Wh/kg [50, 500] of regolith extracted | "Zacny et al. (NIAC studies ...)", not identifiable (R74) |
| `Beneficiation / on-site processing energy` | 500 Wh/kg [100, 2000] of refined product | "NASA Money-Mass-ematics 2023", a grades 7-8 worksheet (rc-048, open) |
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
- `nasa_money_mass_ematics_2023_worksheet` (domain 5): context-only; the worksheet rc-048 is about.
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
| `nasa_money_mass_ematics_2023_worksheet` | domain 5 | `05_inspace_operations/FINDINGS.md`: R74 | none |
| `just_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round-9 status; Round-10 addition; Round 43 addition; Round 44 addition; Round 57 addition | `extracted_data/r43_excavation_energy_key_numbers.csv` |
| `zeng_2007` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r70_zeng_2007.csv`, `full_texts/zeng_2007_excavation_force.pdf` |
| `proctor_apex_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition; R71 | `extracted_data/r71_proctor_apex_2019_key_numbers.csv` |
| `zeitlin_asteroid_excavation_project` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r71_zeitlin_asteroid_excavation_project_key_numbers.csv` |
| `ssap_2021` | domain 5 | `05_inspace_operations/FINDINGS.md`: the `ssap_2021` block; Round-3 additions; Round-3 status; Maintenance; R71 | `extracted_data/ssap_2021_table3_theoretical_yields.csv`, `extracted_data/r71_ssap_2021_key_numbers.csv`, `extracted_data/r71_ssap_2021_reactions_energetics.csv` |

Revision candidates on these sources, written up in their old domains: rc-026 (open, Drilling / excavation energy), rc-027 (blocked, Drilling / excavation energy), rc-048 (open, Beneficiation / on-site processing energy).

The cross-references to `zeng_2007`, `just_2019`, `nasa_money_mass_ematics_2023_worksheet` in the opening block are now rows of this domain. `hein2020`, listed in the opening block under domain 2, is now in domain 22.

`metzger_zacny_2020` stays in domain 5: its row maps to the drilling-energy row, but the paper is about thermal extraction of volatiles, which domain 5 keeps.
