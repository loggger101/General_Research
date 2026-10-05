# Domain 21 — Spacecraft mass & recurring-cost estimating relationships

Backings: spacecost `reference/operational_costs.csv` recurring $/kg rows (mining payload, return capsule, berthing adapter, surface lander, heat shield / TPS, expendable upper stage, propellant tank) and economicspace `modules/calc.py` sizing fields `return_vehicle_dry_kg`, `return_structure_frac_of_payload`, `heat_shield_frac_of_payload` and `nre_recurring_overlap_fraction`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Every hardware kilogram in the cascade is priced by one of these rates and sized by one of these fractions. The rates are brackets or engineering estimates, and the fractions have no source. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Mining payload recurring cost` | $300k/kg [100k, 1M] | SSCM and NICM "bracket recurring deep-space hardware at $100k-$1M/kg" |
| `Return capsule recurring cost` | $150k/kg [50k, 400k] | half the mining-rig rate; Stardust and OSIRIS-REx SRC heritage |
| `Berthing adapter recurring cost` | $60k/kg [30k, 150k] | "near the low end of the NICM/SSCM recurring bracket" |
| `Surface lander recurring cost` | $200k/kg [100k, 500k] | set between the capsule and the rig; Apollo LM and CLPS landers named |
| `Heat shield / TPS for Earth return` | $50k/kg [20k, 150k] of TPS | "NASA / SpaceX have not published a per-kg PICA-X cost; figure is an engineering estimate" |
| `Expendable upper stage recurring cost` | $4,800/kg [1,750, 13,400] of stage dry mass | Falcon 9 upper stage (Musk 2018) at the low end |
| `Propellant tank recurring cost` | $6,000/kg [3,000, 25,000] of tank dry mass | derived from Centaur III |
| `calc.py` `return_vehicle_dry_kg` | 500 kg floor | "irreducible avionics, comms, beacon and separation hardware" |
| `calc.py` `return_structure_frac_of_payload` | 0.15 | Cygnus PCM ~0.43 and Dragon ~1.3:1 quoted as heritage; 0.15 chosen at the light end; no source |
| `calc.py` `heat_shield_frac_of_payload` | 0.15 (TPS mass as a share of returned payload) | none stated |
| `calc.py` `nre_recurring_overlap_fraction` | 0.30 | "a mid-range de-duplication" of development cost already inside the recurring brackets |

**What a source has to supply.**

- Published cost-estimating relationships in $ per kg by hardware class, with their fit ranges and what cost they include.
- Actual unit costs of capsules, landers, stages and tanks, and TPS material and fabrication cost per kg.
- Mass-estimating relationships for cargo carriers and return vehicles: structure and TPS mass as a fraction of cargo.
- How parametric models split development from production cost, which is what the overlap fraction stands in for.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `aerospace_corp_small_satellite_cost_model` (domain 7): the recurring bracket.
- `nasa_instrument_cost_model_nicm` (domain 7): the recurring bracket.
- `stackpoole_2013_pica_pica_x_postflight_eval` (domain 5): TPS heritage; no cost data.
- `musk_2018_falcon9_upper_stage_cost_statement` (domain 4): upper-stage low end.
- `nasa_oig_2020_ig-20-012_sls_program_costs_contracts` (domain 4): an ICPS unit price.

**Boundary.** Domain 7 holds programme totals and NRE; domain 9 holds the delivery-chain mass fractions in `spacecost/delivery.py`; domain 11 holds power and electric-propulsion $/W and kg/kW. This domain holds per-kg rates by hardware class and the structure and TPS sizing fractions.

## R77 - Sources moved in (2026-09-27; registry unchanged at 267)

These rows were registered in other domains before this one existed; they moved here because the cells they back are this domain's. Their earlier write-ups stay in the old domain's FINDINGS.md under the blocks named.

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `aerospace_corp_small_satellite_cost_model` | domain 7 | `07_mission_program_costs/FINDINGS.md`: R74 | none |
| `nasa_instrument_cost_model_nicm` | domain 7 | `07_mission_program_costs/FINDINGS.md`: R74 | none |
| `musk_2018_falcon9_upper_stage_cost_statement` | domain 4 | `04_launch_economics/FINDINGS.md`: R74 | none |
| `stackpoole_2013_pica_pica_x_postflight_eval` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 56 addition | `extracted_data/r70_stackpoole_2013_pica_pica_x_postflight_eval.csv`, `full_texts/pica_pica_x_stardust_dragon_postflight_eval_ntrs_20140005558_publicdomain.pdf` |

The cross-references to `aerospace_corp_small_satellite_cost_model`, `nasa_instrument_cost_model_nicm`, `stackpoole_2013_pica_pica_x_postflight_eval`, `musk_2018_falcon9_upper_stage_cost_statement` in the opening block are now rows of this domain.

## R106 - First hosted sources for the recurring $/kg brief (2026-10-03; +4 rows: 3 full_text_hosted, 1 extraction-only)

The R75 block above is this domain's brief. This round supplies its first institutional answers on three of the four asks: what the two parametric models actually cover (SSCM/NICM scope documentation), flight-heritage cost direction for TPS, and institutional mass-fraction sizing inputs for lander-class hardware. All pulled live from ntrs.nasa.gov on this machine; every PDF verified (`%PDF` magic + SHA-256 in the manifest) and read with PyMuPDF before registration.

| cell | unit | value (low-high) | backed by (R106 id) | what it supplies |
|---|---|---|---|---|
| Mining payload recurring cost / Berthing adapter recurring cost | USD per kg of hardware | 300k [100k, 1M] / 60k [30k, 150k] | foreman_lemoine_deweck_2016_cer_survey_distributed_spacecraft_missions | institutional documentation of the SSCM + NICM/NICM-E scope, versions and access routes that upstream's bracket notes cite (p.6 model table) - the brackets' provenance is now registered even though both models remain access-restricted from this machine |
| Heat shield / TPS for Earth return | USD per kg of TPS mass | 50k [20k, 150k] | koenig_stewart_2019_orion_tps_manufacturability_em1; borner_venkatapathy_2024_low_cost_tps_materials (extraction-only) | EM-1 Avcoat-block producibility: 'cost and schedule savings and a reduction in overall heat shield weight' vs EFT-1 (p.3); ablator cost trends across Discovery/SIMPLEx/CLPS program caps - direction only, no per-kg figure anywhere reachable -> value stays an engineering estimate |
| Surface lander recurring cost (+ calc.py sizing fields) | USD per kg of lander dry mass / structure fraction | 200k [100k, 500k] / return_structure_frac_of_payload 0.15 | clark_pensado_jones_grande_judd_2021_lander_function_allocation_propellant | institutional inert-mass-fraction baselines for lunar transport vehicles: SSL/AE 0.25, DE 0.20, RTE 0.10 at Isp 450 s; sensitivity ranges 0.20-0.30 / 0.15-0.25 / 0.05-0.15 (Tables 7/9) - the sizing side of the same hardware class |

Notes: borner_venkatapathy_2024 is extraction-only because its NTRS determination is MAY_INCLUDE_COPYRIGHT_MATERIAL and the in-file scan found no redistribution licence (repo rule: such docs are read, never hosted). The two NICM queue rows gained dated re-check notes - NTRS holds NICM VI / NICM-E / NICM 8.5 records but all carry determination OTHER with **no public download files** (access-restricted via the NASA ONCE portal), and the OCFO URL in the row now returns HTTP 404 while JPL's landing page still answers 200; SSCM stays registered_not_pulled (landing page bot-blocks this machine). No revision candidate opened: new backing for bracket/judgement cells, nothing contradicts upstream values. Still unbacked after R106: per-kg unit costs of capsules/landers/stages/tanks themselves and the TPS fabrication $/kg - no institutional figure located; those stay engineering estimates.

## R114 - Subsystem mass shares and cost-growth sources (2026-10-04; +4 sources, T1x1, T2x2, T4x1)

`nanostar_systems_engineering_mass_budget_subsystem_percentages` (T4) reproduces Table 15, 'extracted from [WL99]' (Wertz & Larson, SMAD): subsystem shares of dry mass for no-propulsion, LEO-with-propulsion, high-Earth-orbit and planetary spacecraft. Structure and mechanism is 20-27%, propulsion 0-13% and payload 15-41% of dry mass, and propellant is 27%, 72% and 110% of dry mass for the three propelled types. It is the only registered table of the shares behind `return_structure_frac_of_payload` and `heat_shield_frac_of_payload`, and a secondary copy of a textbook this repo does not hold. `spadoni_1982_cost_estimation_model_advanced_planetary_programs_fourth_edition` (front matter read), `ehresmann_2021_automated_system_analysis_and_design_tool_for_spacecrafts` (abstract) and `hayhurst_2016_historical_mass_power_schedule_cost_growth_nasa_spacecraft` (abstract) are registered as context. Two more items on the list could not be read (an ICEAA slide deck on satellite mass growth returned 404). No revision candidate.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.
