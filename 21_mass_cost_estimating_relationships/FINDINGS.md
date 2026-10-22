# Domain 21 — Spacecraft mass & recurring-cost estimating relationships

Backings: spacecost `reference/operational_costs.csv` recurring $/kg rows (mining payload, return capsule, berthing adapter, surface lander, heat shield / TPS, expendable upper stage, propellant tank) and economicspace `modules/calc.py` sizing fields `return_vehicle_dry_kg`, `return_structure_frac_of_payload`, `heat_shield_frac_of_payload` and `nre_recurring_overlap_fraction`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Mining payload recurring cost` | $300k/kg [100k, 1M] | SSCM and NICM "bracket recurring deep-space hardware at $100k-$1M/kg" |
| `Return capsule recurring cost` | $150k/kg [50k, 400k] | half the mining-rig rate; Stardust and OSIRIS-REx SRC heritage |
| `Berthing adapter recurring cost` | $60k/kg [30k, 150k] | "near the low end of the NICM/SSCM recurring bracket" |
| `Surface lander recurring cost` | $200k/kg [100k, 500k] | between capsule and rig; Apollo LM and CLPS landers named |
| `Heat shield / TPS for Earth return` | $50k/kg [20k, 150k] of TPS | "NASA / SpaceX have not published a per-kg PICA-X cost; figure is an engineering estimate" |
| `Expendable upper stage recurring cost` | $4,800/kg [1,750, 13,400] of stage dry mass | Falcon 9 upper stage (Musk 2018) at the low end |
| `Propellant tank recurring cost` | $6,000/kg [3,000, 25,000] of tank dry mass | derived from Centaur III |
| `calc.py` `return_vehicle_dry_kg` | 500 kg floor | "irreducible avionics, comms, beacon and separation hardware" |
| `calc.py` `return_structure_frac_of_payload` | 0.15 | Cygnus PCM ~0.43 and Dragon ~1.3:1 as heritage; 0.15 at the light end; no source |
| `calc.py` `heat_shield_frac_of_payload` | 0.15 | none stated |
| `calc.py` `nre_recurring_overlap_fraction` | 0.30 | "a mid-range de-duplication" |

**What a source has to supply:** published $/kg CERs by hardware class with fit ranges; actual unit costs of capsules, landers, stages, tanks and TPS per kg; mass-estimating relationships for cargo carriers and return vehicles; how parametric models split development from production.

**Also relevant, registered elsewhere:** `nasa_oig_2020_ig-20-012_sls_program_costs_contracts` (d04; an ICPS unit price).

**Boundary:** domain 7 holds programme totals and NRE; domain 9 delivery fractions; domain 11 power and EP $/W and kg/kW. This domain holds per-kg rates by hardware class and the structure and TPS fractions.

## R77 - Sources moved in (2026-09-27)

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `aerospace_corp_small_satellite_cost_model` | domain 7 | `07_mission_program_costs/FINDINGS.md`: R74 | none |
| `nasa_instrument_cost_model_nicm` | domain 7 | `07_mission_program_costs/FINDINGS.md`: R74 | none |
| `musk_2018_falcon9_upper_stage_cost_statement` | domain 4 | `04_launch_economics/FINDINGS.md`: R74 | none |
| `stackpoole_2013_pica_pica_x_postflight_eval` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 56 addition | `extracted_data/r70_stackpoole_2013_pica_pica_x_postflight_eval.csv`, `full_texts/pica_pica_x_stardust_dragon_postflight_eval_ntrs_20140005558_publicdomain.pdf` |

## R106 - First hosted sources (2026-10-03)

| cell | backed by | what it supplies |
|---|---|---|
| Mining payload / Berthing adapter recurring cost | foreman_lemoine_deweck_2016_cer_survey_distributed_spacecraft_missions (hosted) | the scope, versions and access routes of SSCM and NICM/NICM-E (p6 table); both models stay access-restricted |
| Surface lander + `return_structure_frac_of_payload` | clark_pensado_jones_grande_judd_2021_lander_function_allocation_propellant (hosted) | inert mass fractions for lunar transport stages: SSL/AE 0.25, DE 0.20, RTE 0.10 at Isp 450 s; sensitivity 0.20-0.30 / 0.15-0.25 / 0.05-0.15 (Tables 7, 9) |

NICM VI / NICM-E / NICM 8.5 records on NTRS carry no public files (ONCE portal only); SSCM's landing page refuses this machine. Per-kg unit costs of capsules, landers, stages, tanks and TPS remain unsourced estimates.

## R114 - Subsystem mass shares; cost-growth sources (2026-10-04)

`nanostar_systems_engineering_mass_budget_subsystem_percentages` (T4) reproduces SMAD's Table 15: structure and mechanisms 20-27% of dry mass, propulsion 0-13%, payload 15-41%; propellant 27%, 72% and 110% of dry mass for the three propelled types. The only registered table behind the structure and TPS fractions (a secondary copy of a textbook not held here). Context: `spadoni_1982_cost_estimation_model_advanced_planetary_programs_fourth_edition`, `ehresmann_2021_automated_system_analysis_and_design_tool_for_spacecrafts`, `hayhurst_2016_historical_mass_power_schedule_cost_growth_nasa_spacecraft`. `extracted_data/r114_gr_links_key_numbers.csv`.

## R120 - ehresmann_2021_automated_system_analysis_and_design_tool_for_spacecrafts hosted (CC BY; 2026-10-05)

Hosted as full_texts/ehresmann_herdrich_fasoulas_2021_automated_system_analysis_design_tool_ceas_space_journal_ccby.pdf (CEAS Space Journal 14:327-354): a full-system spacecraft estimation tool applied to flown missions. Context.

## R146 - TPS cost data (2026-10-09)

- **peterson_haas_1971_shuttle_tps_refurbishment_cost_study_nasa_cr-iii_30** (Lockheed for NASA, 325 pp, hosted): p58 operational cost per square foot of TPS on a delta-body orbiter, ablators highest at ~$50,000 (nose cone $85,000) over 10 years; p60 "$1300 to $2800 per square foot for metallic and non-metallic TPS". Maintenance cost per area, not manufacturing $/kg; one scan artefact "$52,0OO" kept as printed.
- **mcguire_covington_goldstein_arnold_beck_2013_msl_aft_heatshield_trade_studies_ippw10** (IPPW-10 abstract, hosted): MSL aft-shield trades: thickness optimisation could cut SLA-561V mass ~40%; AFRSI ("relatively inexpensive manufacturing") 60% lighter.

`extracted_data/r146_tps_costs_key_numbers.csv`. No $/kg, so no re-pin.

## R159 - Heat-shield mass vs entry speed (2026-10-13)

- **dec_braun_2006_approximate_ablative_tps_sizing_tool** (AIAA 2006-780, hosted; the "AIAA 2005-5915" inside is a self-citation): thickness from trajectory via heat-of-ablation recession and 1-D thermal response iterated to bondline limits; "Given the vehicle geometry and the TPS material density, the total mass of the heatshield can be calculated". Table 2, Apollo capsule at 11 vs 14 km/s: PICA stagnation thickness 8.324 -> 10.873 cm (recession 0.726 -> 3.828), FM5055 5.770 -> 6.473 (approximate 5.961/6.983): mass grows super-linearly with speed. Stardust check: peak 1126 W/cm2, load 28,000 J/cm2, 4.8 cm with 1.2 cm recession.
- **mahzari_et_al_2022_mars2020_tps_development_sizing** (AIAA Aviation 2022, US government work, hosted): "No major changes to the TPS materials and thicknesses compared to MSL"; bondline sizing with RSS'd uncertainties, "Similar sizing methodology to the one used for MSL and Orion missions"; six arc-jet tests plus FIAT verification.

The flat 0.15 approximates this curve for one entry class. `extracted_data/r159_tps_sizing_key_numbers.csv`.

## R162 - Stage mass-estimating relationships (2026-10-13)

- **kibbey_2015_rho_isp_stage_mass_estimating_jpc** (AIAA 2015-3791, hosted; the "AIAA 2014-4021" on p13 is a self-citation to Donahue & Klaus): stage inert mass split into engine+structure, oxidiser-tank and fuel-tank fractions; from Atlas V "f’i,ot,0 = 0.0180 and f’i,ft,0 = 0.0255"; "starting with Atlas V’s 0.93, the equation predicts a Delta IV CBC propellant mass fraction of 0.82, while its published mass fraction is actually 0.887". The method behind the structure fractions the upper-stage and tank $/kg rates are quoted against.
- **motiwala_mathias_mattenberger_2014_conceptual_lv_spacecraft_design_risk** (NASA/TM-2014-218366, hosted): component MERs iterated to the vehicle's inert mass; "Typical structural mass fractions range from 0.038 to 0.45, based on historical data". Stage inert/propellant, not structure per returned payload, so it bounds `return_structure_frac_of_payload` without pinning it.

`extracted_data/r162_stage_mer_key_numbers.csv`.

## R165 - Candidates (2026-10-14)

rc-134 and rc-135 (scale the heat-shield fraction with entry speed in economicspace and spacecost), rc-137 (return-structure heritage figures: Cygnus 3,754 kg), rc-139 (the SSCM/NICM $/kg bracket is unreadable; NICM is an instrument model). Texts in `revision_candidates.csv` (open) and `revision_candidates_closed.csv`.
