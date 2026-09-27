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
