# Domain 22 — Prior-art techno-economic benchmarks

Backings: economicspace's end-to-end answer rather than an input cell: `campaign/results.csv` `best_obj`, `winner`, `payload_kg` and `programme_missions` per cell, and the Stage 4 cost cascade in `modules/calc.py` that produces them.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Domain 8 is an external oracle for delta-v; nothing plays that role for the profitability answer. economicspace `research/starred-repos/SECOND-PASS.md` calls Asterank "the only direct prior art this project has". Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `campaign/results.csv` `best_obj`, `winner`, `payload_kg`, `programme_missions` | the per-cell headline answer | no external comparison except Asterank (domain 8) |
| Stage 4 cost cascade (`modules/calc.py`) | the structure of the cost lines and their order | upstream design; not compared with any published model |

**What a source has to supply.**

- Published techno-economic models of asteroid mining, and of lunar or cislunar propellant supply (which shares the in-space demand side), that state enough of their inputs (target, delta-v, hardware mass and cost, throughput, prices, discount rate) to map onto pipeline cells, so a disagreement in the headline can be traced to the cell that causes it.
- A model that publishes only its conclusion is registered as context-only.
- Extracted inputs go into comparison CSVs whose rows name the pipeline cell each input maps to.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `asterank_neo_service_shoemaker_helin` (domain 8): the one prior-art ranking upstream names.
- `hein2020` (domain 2): end-to-end techno-economic analysis; parameter tables extracted in R61.
- `lewicki2023` (domain 2): valuation framework.

**Boundary.** Input cells stay with their own domains (a benchmark model's price goes to domain 6, its throughput to 19); this domain holds whole-model comparisons.

## R77 - Sources moved in (2026-09-27; registry unchanged at 267)

These rows were registered in other domains before this one existed; they moved here because the cells they back are this domain's. Their earlier write-ups stay in the old domain's FINDINGS.md under the blocks named.

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `hein2020` | domain 2 | `02_composition_value/FINDINGS.md`: the `hein2020` block; Round-1 status; Round 61 addition; Maintenance; R71; R72 | `extracted_data/r61_hein2020_plant_economics_key_numbers.csv`, `extracted_data/r71_hein2020_key_numbers.csv`, `extracted_data/r71_hein2020_table3_pt_supply_demand_profitability.csv` |
| `metzger_2023` | domain 4 | `04_launch_economics/FINDINGS.md`: Round-12 addition; Maintenance; R71 | `extracted_data/r71_metzger_2023_key_numbers.csv`, `extracted_data/r71_metzger_2023_table1_years_to_absolute_advantage.csv`, `extracted_data/r71_metzger_2023_table2_production_mass_ratio_phi.csv`, `extracted_data/r71_metzger_2023_table3_cost_elasticities.csv`, `extracted_data/r71_metzger_2023_tableA1_lunar_propellant_tea_parameters.csv` |

The cross-reference to `hein2020` in the opening block is now a row of this domain.
## R88 - Third prior-art model: Stenis & Hogland's interplanetary resource-economy optimisation (2026-09-30; registry 314 -> 315)

**stenis_hogland_2017_interplanetary_resource_economy_optimisation** [T2, extraction-only] - Jan Stenis & William Hogland (Linnaeus University), "Optimisation of the resource economy of metals, minerals and energy in an interplanetary perspective", Linnaeus Eco-Tech '14 proceedings / institutional OA journal series (ISSN 2002-8008; DOI 10.15626/eco-tech.2014.030 Crossref-verified live this round). Full text read in full from the author-repository copy (open.lnu.se, 290,020 bytes / 24 pp); **not hosted** - the OJS article page carries only a Copyright notice with no redistribution licence and Crossref's license field is empty.

What it adds to d22: Hein (2020) models plant-level PT economics, Metzger (2023) models lunar propellant TEA + cost elasticities - **this is the only prior-art model in our corpus with a bottom-up per-mission total**: its case study's "total estimated cost for a mission to mine an asteroid of $5 billion" (p14), which the authors themselves flag as *almost certainly low*. The rest of the structure is top-down calibration: 5% of US industrial GDP (~$2T) = $100B initial global allocation to cosmic industry; C_commodity_total = $50B/yr (USA share $25B); tellurium-residual value chain A=$1B / B=$1T / C=$10B with shadow costs R=$100M global -> $50M USA via eq.(39)-(40) (pp14-15). Value-side context (p3): 30-m asteroid = $25-50B platinum, >80-m = >$100B materials, ~200-m metallic = ~$30B at then-current prices - a second independent statement of the "single asteroid worth tens of billions" figure already in our corpus (useful as corroboration for d4/d6 value rows). Macro backdrop: space economy ~$251B in 2007, >60% commercial (p2).

**No re-pin proposed**: all figures are 2017 order-of-magnitude estimates used to calibrate the authors' optimisation model, not measurements - they bracket rather than contradict our rows. Extracted data: `extracted_data/r88_stenis_hogland_2017_key_numbers.csv` (7 rows, page-located). d22 now holds three prior-art models covering plant-level (Hein), lunar-propellant TEA + elasticities (Metzger) and macro interplanetary resource-economy structure with a per-mission cost anchor (Stenis & Hogland).
