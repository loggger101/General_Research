# Domain 22 — Prior-art techno-economic benchmarks

Backings: economicspace's end-to-end answer rather than an input cell: `campaign/results.csv` `best_obj`, `winner`, `payload_kg` and `programme_missions` per cell, and the Stage 4 cost cascade in `modules/calc.py` that produces them.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Domain 8 is an external oracle for delta-v; nothing plays that role for profitability. economicspace `research/starred-repos/SECOND-PASS.md` calls Asterank "the only direct prior art this project has". Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `campaign/results.csv` `best_obj`, `winner`, `payload_kg`, `programme_missions` | the per-cell headline answer | no external comparison except Asterank (domain 8) |
| Stage 4 cost cascade (`modules/calc.py`) | the structure and order of the cost lines | upstream design; not compared with any published model |

**What a source has to supply:** published techno-economic models of asteroid mining or lunar/cislunar propellant supply that state enough inputs (target, delta-v, hardware mass and cost, throughput, prices, discount rate) to map onto pipeline cells, so a disagreement in the headline can be traced to its cell. A model that publishes only its conclusion is context-only. Extracted inputs go into comparison CSVs whose rows name the cell each maps to.

**Also relevant, registered elsewhere:** `asterank_neo_service_shoemaker_helin` (d08), `lewicki2023` (d02).

**Boundary:** input cells stay with their own domains (a model's price goes to domain 6, its throughput to 19); this domain holds whole-model comparisons.

## R77 - Sources moved in (2026-09-27)

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `hein2020` | domain 2 | `02_composition_value/FINDINGS.md`: the `hein2020` block; Round 61 addition; Maintenance; R71; R72 | `extracted_data/r61_hein2020_plant_economics_key_numbers.csv`, `extracted_data/r71_hein2020_key_numbers.csv`, `extracted_data/r71_hein2020_table3_pt_supply_demand_profitability.csv` |
| `metzger_2023` | domain 4 | `04_launch_economics/FINDINGS.md`: Round-12 addition; Maintenance; R71 | `extracted_data/r71_metzger_2023_key_numbers.csv`, `extracted_data/r71_metzger_2023_table1_years_to_absolute_advantage.csv`, `extracted_data/r71_metzger_2023_table2_production_mass_ratio_phi.csv`, `extracted_data/r71_metzger_2023_table3_cost_elasticities.csv`, `extracted_data/r71_metzger_2023_tableA1_lunar_propellant_tea_parameters.csv` |

## R88 - Stenis & Hogland's interplanetary resource-economy optimisation (2026-09-30)

**stenis_hogland_2017_interplanetary_resource_economy_optimisation** [T2, read, not hosted: no redistribution licence] - Linnaeus Eco-Tech '14, DOI 10.15626/eco-tech.2014.030.

The only prior-art model here with a bottom-up per-mission total: "total estimated cost for a mission to mine an asteroid of $5 billion" (p14), which the authors call almost certainly low. The rest is top-down calibration: 5% of US industrial GDP (~$2T) = $100B global allocation; C_commodity_total $50B/yr (USA $25B); tellurium-residual chain A=$1B / B=$1T / C=$10B with shadow costs $100M global -> $50M USA (eq. 39-40, pp14-15). Value context (p3): a 30 m asteroid holds $25-50B of platinum, >80 m >$100B of materials, a ~200 m metallic body ~$30B. Order-of-magnitude calibration values, so no re-pin. `extracted_data/r88_stenis_hogland_2017_key_numbers.csv`.

## R113 - A lunar ISRU TEA with stated inputs (2026-10-04)

**`paulson_balchanos_mavris_2026_isru_economic_environmental_tradeoffs`** (AIAA 2026-2788; abstract only, paywalled). Earth resupply vs ISRU for a 4-person lunar crew over 3 years: resupply reaches $500M by year 3; ISRU needs $800M setup plus $10,000/day maintenance and pays back only after 30 years; a 15% carbon tax or 30% maintenance subsidy does not change that; the ice comes from 0.761 km2 of a permanently shadowed region. Its demand is crew consumption, so it bounds lunar ISRU payback at small demand rather than serving as a comparator. Context-only until its input tables are read.

## R114 - Three ISRU and PGM-market benchmarks (2026-10-04)

- `jones_klovstad_komar_judd_2018_cost_breakeven_cislunar_isru` (NASA Langley, FY2018$): for 59 t/yr of H2/O2 over 14 years the cheapest option is commercial delivery from Earth at $40,000/kg in cislunar space; lunar ISRU breaks even at 35 years.
- `miyajima_2022_cost_analysis_in_situ_space_resources_moon_mars_habitation`: propellant at $4,000, $12,000 and $36,000/kg delivered from Earth to LEO, EML1 and the Moon; $3,000/kg from the Moon to LEO if lunar production costs under $500/kg.
- `nachtrieb_smith_2026_will_astroforge_collapse_the_pgm_market` (arXiv, CC BY): PGM prices fall toward mining cost only after the entire supply has moved off-world; quotes 100-187 ppm PGM for metallic asteroids vs 4-10 ppm in ores, above the maxima in `usgs_pp1802n` and `cannon2023` and resting on one reference, so recorded, not adopted.

`extracted_data/r114_gr_links_key_numbers.csv`.

## R141 - The $7B break-even's primary source, plus a parametric model (2026-10-09)

**calla_fries_welch_2019_asteroid_mining_small_spacecraft_economic_feasibility** [T2, read from arXiv 1808.05099v2; default licence, not hosted]. The primary behind every "$7B asteroid-mining break-even" figure: spacecraft <500 kg deliver 100 kg of water per trip from NEAs within ~0.03 AU (437 m/s one-way); microwave extraction at 2 Wh/g; SSCM unit cost $113.6M, first unit $145.7M + a $90M Falcon Heavy. Break-even needs more than 100 spacecraft over five years; the most likely feasible case is ~200 craft selling water in cislunar space for ~$7 billion up front, profitable after ~10 years (7 at best). It brackets the shape of economicspace's answer (fleet scale, cislunar market) but pins no cell. `extracted_data/r141_calla_key_numbers.csv`.

**dorrington_olsen_2026_parametric_economic_modelling_asteroid_mining_architectures** [T1, registered_not_pulled] - Acta Astronautica 241:19-47 (2026), CC BY: the first peer-reviewed parametric model of asteroid-mining architectures, exactly this domain's brief. Every ScienceDirect route refuses this machine; hostable once fetched (DOWNLOADS.md).
