## R954 — Spacecost package release travels with built tables (2026-11-19)

At Spacecost main 868f42890ac97ee40a50d79f7b33863046edb0ff, `build.py` writes `build_manifest.json` beside the generated tables with `package_version`, `pipeline_version`, `catalog_date` and the output file list (`spacecost_package_release_output_provenance_code_current_2026`; rc-773). The CSV value columns are not changed by this manifest.

Verdict: the package release identifier is available with the build. Extracted data: none new.
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

## R282 - Bulk ore restraint citation seam (2026-10-27)

Seam: the storage_systems.csv row Bulk ore restraint (bag / hopper), value 0.15 kg containment per kg ore [0.08..0.3], is Module 4 return-vehicle structure fraction (return_structure_frac_of_payload) and economicspace consumes it as its calc.py default, feeding the fixed-point mass cascade; verification_sheet input f_str is backed only by cite_config quoting that dial comment. The row note claims Real cargo spacecraft run 0.4:1 to 2:1 payload-to-structure with no document named in spacecost, and CITATIONS.md covers this table only by policy - every storage system cited by the notes field of its own row (fragments count==1 at @860bef9). The note simultaneously asserts recorded here so the cargo side of storage has a citation of its own; under the self-citation contract that claim is empty because no document appears in it.

Evidence state: hosted IG-18-016 physical p.18 spacecraft comparison table prints capacity only - Upmass Per Mission 3,754 (Cygnus), 5,500 with footnote a (Sierra Nevada column; the economicspace dial comment words this figure as Dream Chaser, loose attribution recorded not adjudicated), and for SpaceX pressurized 2,507 plus Trunk: 800 kg unpressurized - while dry mass appears zero times in all 55 pages in both letter cases. The report therefore supports capacity claims but cannot support any payload-to-structure ratio; the applied rc-137 dial comment concedes exactly that for the Cygnus ~1,500 kg anchor (ratio 0.40, has no source here.). Hosted motiwala_2014 p.11 footnote gives structural mass fractions range from 0.038 to 0.45 based on historical data with a stage-level denominator (body text: for each stage) - usable only as context for launch stages, not cargo vehicles.

Standing note for future rounds: audit storage_systems.csv rows against the self-citation contract in CITATIONS.md - a row whose notes name no document is uncited regardless of status token. Six sibling rows carry ESTIMATE declarations (COPV burst performance factor; Multi-layer insulation passive; Zero-boil-off cryocooler 20 K; Volatile cargo containment water ice; Regenerative fuel cell; Flywheel energy storage), and the CITATIONS.md volatile-containment line shows the engineering-estimate route is an accepted upstream pattern (which is an engineering estimate, count==1). Sister row under open rc-184 adds INCREMENTAL to this 0.15 ore-restraint fraction per operations.py.

Extracted data: `extracted_data/r282_bulk_ore_restraint_key_numbers.csv`.

## R318 - Rig procurement is shared but its launch manifest is repeated (2026-11-01)

Source `economicspace_stationary_rig_repeat_launch_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0 `modules/calc.py`, with
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f original reference rows and
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011 cargo helpers.
The architecture says "A rig stays at the asteroid" (calc.py L4579), while
L5616-5618 describe one unit shared across campaigns. Rig procurement is
divided by `missions_sharing_rig` (L5592-5596). The mass solve nevertheless
includes all `config.mining_hardware_kg` in every outbound stack (L6670-6674,
L6742-6746), and programme pricing reuses that same cascade (L6981-7045).

Nine complete original-evaluator cases retain original numerical functions.
Main synthetic inputs: 1e9 kg body, density 2 g/cm3, no water, 1.2 AU,
100 USD/kg silicate cargo and a nonbinding commodity ceiling; actual Falcon 9
reusable, kerolox and all 46 ops rows; caller delta-v 1,000 m/s per leg,
raw cargo, no ISRU or aerocapture. Windows, refinery, water liberation,
containment and boil-off are disabled for isolation. The entire added
hardware is the 2,000 kg rig: no EP, processing array or refinery is involved.

At fixed N=5, the model selects F=1, W=5. The rig's 600M USD procurement is
charged at 120M per mission, exactly one fully used rig over the programme.
Cargo is 17,794.394348 kg per delivery and each launch is 17,400 kg, including
that full rig. Four later flights therefore repeat the launch manifest of
the rig which the cost book says is already installed at the target.

A separate fixed-cargo diagnostic omits only that installed rig from later
Earth manifests, retaining its on-site throughput and procurement allocation.
From the original tank-closure relation, with H=2,000 kg:
`delta_prop = H*k_out*(R_out-1)` and
`delta_launch = H+delta_prop+tank_frac*delta_prop`.
Here each repeat flight drops 706.139341 kg outbound propellant and 19.005365
kg tankage as well as the rig, giving 14,674.855294 kg launch mass. Four such
flights reduce the programme launch book by 10,900.578825 kg.

| case | N | F | W | repeat rig shipments in current book | aggregate fixed-cargo launch difference (kg) |
|---|---|---|---|---|---|
| fixed five / searched one ship | 5 | 1 | 5 | 4 | 10,900.578825 |
| fixed two | 2 | 1 | 2 | 1 | 2,725.144706 |
| searched fleet cap 64 | 320 | 64 | 5 | 256 | 697,637.044819 |
| numeric defaults, body at 1.8 AU | 320 | 64 | 5 | 256 | 697,637.044819 |
| single mission | 1 | 1 | 1 | 0 | 0 |
| one-trip rig control | 5 | 5 | 1 | 0 | 0 |
| zero outbound delta-v | 5 | 1 | 5 | 4 | 8,000 |
| tank mass off | 5 | 1 | 5 | 4 | 10,797.969151 |

The one-trip control changes only the rig maximum-trips row from five to one.
Every case fits cumulative body supply, the 15-year rig calendar and launch
capacity. Thus the discrepancy does not depend on the separate depletion,
calendar-age or EP/ISRU defects.

Original cost helpers exactly reproduce every evaluator cost field on the
original manifest. Repricing the first/repeat manifests at the same N, W,
cargo and calendar changes the main case's average total cost from
1,020.540131M to 1,009.303614M USD. The rig, capsule, return fuel, NRE and
operations lines remain unchanged. This 11.236518M USD-per-mission difference
uses the model's linear launch USD/kg tariff and contingency; it is not a
quoted saving on a dedicated rocket flight or a new joint payload optimum.

Verdict: stationary rig reuse is represented in manufacturing cost but not
in per-launch mass flow. `rc-248`: distinguish first-use and repeat manifests,
or account consistently for a new rig on every mission. Current-population
incidence and ranking effects were not measured.
`extracted_data/r318_stationary_rig_repeat_launch.csv`.
## R381 - NEXT-C bundled procurement benchmark (2026-11-08)

Source `nasa_2015_nextc_contract_award_price`: NASA Glenn says it awarded Aerojet Rocketdyne a five-year cost-share contract with a total value of $18,410,242 to design, fabricate and test two NEXT-C thrusters and two PPUs for flight; the same release says the contractor team would also design, fabricate and test a prototype PPU before production (release 15-011, Apr. 1, 2015). The current spacecost `Electric propulsion system recurring cost` anchor is an inferred $10-15M per 7-kW flight string, and its note says no registered NASA record prices a string. The contract is a relevant government procurement benchmark, but bundles two flight systems, a prototype PPU and development/testing, with no allocation or recurring production price. Verdict: re-evaluate the $10-15M per-string anchor against this bundle and state the scope distinction; do not divide the contract by two as a recurring unit price. `rc-299` (method). Extracted data: `extracted_data/r381_nasa_nextc_contract_bundle.csv`.
## R382 - CLPS surface-lander price comparator (2026-11-08)

Read upstream at `spacecost@19e1a31`. Sources `nasa_oig_2024_ig_24_013_clps_delivery_costs` and `kuettel_et_al_2024_im1_nova_c_dry_mass`. NASA OIG describes CLPS orders as firm-fixed-price contracts “for the full scope of payload delivery—from payload handover to delivery and operation” (IG-24-013, p.3). For Intuitive Machines TO2-IM/20C/OP, it reports $81.7M initial and $122.0M current value, a 49% increase (p.12); the footnote says 20C and OP added activities to the TO2-IM flight. Kuettel et al. report the IM-1 Nova-C lander “dry mass of 677 kg” (AAS 24-282, p.2). Dividing the current full-service task-order value by that dry mass gives ~$180,207 per dry kg; the initial value gives ~$120,679/kg. The spacecost `Surface lander recurring cost` estimate is $200,000/kg [100,000, 500,000] and is described as a recurring hardware rate. The comparator includes end-to-end delivery, launch, development and operations, and price is not the contractor’s cost; this does not directly refute the hardware estimate. Verdict: test and explain why the recurring hardware point sits above the observed whole-service $/dry-kg comparator, or retain it with a scope-specific justification; do not substitute the package ratio as a hardware price. `rc-300` (method). Extracted data: `extracted_data/r382_clps_lander_cost_comparator.csv`.

## R432 — AEPS contract bundle and optional flight-unit scope (2026-11-09)

NASA Glenn release 16-044 (2016-04-19) says the AEPS contract was a 36-month cost-plus-fixed-fee award with a performance incentive and total value of $67M. Its stated integrated system includes a Hall thruster, power processing unit, low-pressure xenon flow controller and electrical harness; Aerojet was to construct and test an engineering development unit, and an option, if exercised, covered development, verification and delivery of four integrated flight units. The release does not allocate the contract value between development, the engineering unit and any flight units, or state whether the option was exercised. The existing $1.5M/kW [0.5M, 3M] row is a recurring EP train estimate; the contract is therefore a development/qualification bundle and cannot yield a per-kW recurring price. It adds a distinct contract scope comparison to `rc-299`; it does not establish a replacement. Extracted: `extracted_data/r432_nasa_aeps_contract_scope.csv`.

## R434 - NASA Blue Origin Mark 1 PROMISE delivery award (2026-11-09)

`nasa_2026_blue_origin_promise_lunar_delivery_award`, NASA Headquarters news release updated November 7, 2026, reports a $94 million base contract and a performance-based option for an additional $140 million to deliver and deploy the PROMISE rover to the lunar south pole. NASA says the award expands the May 2026 task order for delivery of two lunar terrain vehicles, and identifies Blue Origin’s Mark 1 as the lander. The release gives no lander dry mass and does not allocate price between the earlier and expanded scope.

This is a current commercial lander delivery award, not a recurring hardware cost or mass-normalized unit price. It adds a distinct provider/scope example to `rc-300`; it cannot be converted to dollars per lander kilogram. `rc-300` remains open and no upstream value is changed. Extracted: `extracted_data/r434_nasa_blue_origin_promise_delivery_award.csv`.



## R451 — Lunar ISRU development and production cost factors (2026-11-09)

Johnson, Sowers & Abbud-Madrid, *The value of lunar-derived oxygen and water for an early habitation customer*, define lifecycle cost as DDT&E, production, delivery and operations (Eq. 3, PDF p. 9); DDT&E is initial non-recurring system development. Their industry-factor method uses $63,000/kg for initial ISRU system development and $25,200/kg for flight-unit production in FY2026 dollars (§ Industry cost factors, PDF p. 12), adjusted from Sowers (2021) and Kornuta et al. (2019). The paper applies a complexity factor of 1.0 to ISRU systems. These are heuristic lunar pilot-system factors, not measured asteroid-mining costs. **Verdict:** this sharpens the cost-category comparison for `rc-330` but does not supply a replacement value for the asteroid concept estimate or prove the upstream NRE omission. Extracted: `extracted_data/r451_lunar_isru_development_production_cost_factors.csv`.


## R453 — Earth-return speed and separate Mars EDL TPS sizing (2026-11-09)

`xing_2026_mars_sample_return_tps_sizing` — Xing (2026), published in *Frontiers in Astronomy and Space Sciences* 13:1821180 on 2026-05-21, reports baseline Earth atmospheric entry at 12.0–12.8 km/s and says this is within the 12.9 km/s Stardust sample-return heritage and PICA-class capability (§3.5.1, p. 9). The paper’s separate Mars EDL Monte Carlo case uses a 5.8 km/s entry velocity (Table 6, p. 10). Its Mars EDL TPS estimate is 350–500 kg for a 15 m² wetted area (§4.3.4, p. 11); Table 8 (p. 12) lists 280 kg PICA forebody, 80 kg SLA-561V backshell, and 90 kg structure/bondline, totaling 450 kg. The table labels 90 kg as 15% of TPS mass, although it is 20% of the 450 kg listed total; no reconciliation is given. These are Mars EDL sizing values, not an Earth-return TPS mass, which the paper does not state. The CC BY study therefore sharpens rc-134’s entry-event and sizing-method distinction but supplies no replacement for the upstream 15%-of-returned-payload assumption. Extracted: `extracted_data/r453_xing_2026_tps_mass_and_entry_speed.csv`.


## R456 - Repeat-manifest option in current upstream (2026-11-09)

`economicspace_stationary_rig_repeat_manifest_flag_2026`, economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, defines `CalcConfig.model_repeat_manifest` with default `False` (modules/calc.py, line 749). When enabled, the manifest omits the rig (line 8502), while the programme cost tail subtracts launch, outbound-propellant and outbound-tank savings for N-F repeat flights (lines 5767-5774 and 5991-5997). The configuration comment explicitly says the cargo capacity freed by leaving the rig behind is not re-solved (lines 746-749).

This adds an opt-in partial path for `rc-248`, but the default still charges a rig on each flight and the optional path does not couple the freed capacity to payload, propellant and programme re-optimization. Keep the candidate open for default-configuration review and complete first-use/repeat-manifest sizing. Extracted: `extracted_data/r456_repeat_manifest_flag_audit.csv`.

## R475 — High-velocity Earth-entry TPS sizing (2026-11-09)

`alpert_et_al_2024_high_velocity_earth_entry_tps` — Alpert et al. evaluate Stardust and Mars Sample Return Earth Entry System geometries at 12.8 and 16.5 km/s; the paper calls 16.5 km/s relevant to destinations such as near-Earth asteroids (Trade Study Parameters, p. 1). Their entry-mass sweep covers 30–60 kg for Stardust and 75–135 kg for MSR-EES (p. 1). The sizing method reports thickness from a three-branch root-sum-square procedure with a 1.25 factor of safety (TPS Sizing, p. 2); it does not give heatshield mass or a ratio to returned payload. The NTRS record states “Work of the US Gov. Public Use Permitted.” **Verdict:** this supports sizing TPS by entry conditions and vehicle mass, but supplies no replacement for economicspace’s 15%-of-returned-payload dial. Keep `rc-134` open. Extracted data: `extracted_data/r475_alpert_high_velocity_tps_sizing.csv`.



## R555 — ICPS whole-stage price comparator for tank-cost derivation (2026-11-10)

`nasa_oig_2020_ig-20-012_sls_program_costs_contracts`: NASA OIG reports an opportunity to buy “the hardware for a second ICPS for $29 million” (PDF p. 23). ICPS is a modified Delta Cryogenic Second Stage; the figure is for a whole-stage hardware purchase, not a Centaur III stage or its tank alone. Spacecost’s `Propellant tank recurring cost` note derives about $5,300/kg from an unsupported ~$30M Centaur III stage price less an assumed ~$20M RL10, then adopts $6,000/kg [3,000,25,000]. The OIG figure gives a close stage-level comparator but does not verify the Centaur price or allocate cost among engine, tanks and structure. `rc-421` records the citation and component-allocation gap; no replacement rate is inferred. Extracted: `extracted_data/r555_nasa_oig_icps_price_vs_centaur_tank_cost_anchor.csv`.


## R556 — HEEET cost basis by heat-shield size (2026-11-10)

`nasa_discovery_2014_ao_qa_heeet_cost` — NASA’s Discovery 2014 Announcement of Opportunity Q&A, updated February 6, 2015, asks for projected HEEET TPS cost per kilogram. The response says generic cost-per-kilogram “is not the ideal way” to specify HEEET cost, then gives current best estimates of $3M, $6M and $11M for 1 m, 2 m and 3 m diameter heat shields (T-21, PDF p. 9). Spacecost’s `Heat shield / TPS for Earth return` row uses $50,000/kg [20,000,150,000] for PICA-X/AVCOAT-class material plus manufacturing and already notes the lack of published PICA-X per-kg cost. HEEET is a different material and the Q&A gives no shield mass, so the figures provide a cost-basis comparator but cannot be converted into a replacement rate. **Verdict:** review the per-kg representation and applicability; retain the value as an estimate pending like-for-like evidence. `rc-422`. Extracted: `extracted_data/r556_nasa_discovery_heeet_cost_by_shield_size.csv`.


## R557 — Cygnus cargo-module mass by configuration (2026-11-10)

`orbital_sciences_2014_cygnus_configuration_mass` — Orbital Sciences’ *Commercial Cargo Operations for the ISS* presentation labels Standard Cygnus PCM dry mass as 1,677 kg with 2,000 kg payload, and Enhanced Cygnus PCM dry mass as 1,995 kg with 2,700 kg payload (slide 4, PDF p. 4). The corresponding module-only ratios are 0.8385 and 0.7389 kg/kg. The diagram also labels each service module at 1,700 kg but does not say whether that mass is dry or wet; these values therefore do not establish total spacecraft dry mass. Current economicspace `return_structure_frac_of_payload` comment still says Cygnus’s ~1,500 kg dry mass and 0.40 ratio lack a source, while the model value remains 0.15. **Verdict:** cite and scope the configuration-specific PCM data; do not use it as a whole-vehicle or unpressurized ore-hopper ratio, and retain 0.15 as an engineering estimate pending like-for-like evidence. `rc-423`. Extracted: `extracted_data/r557_orbital_cygnus_pcm_mass_by_configuration.csv`.


## R635 — Stardust capsule mass and cost scope (2026-11-11)

`jpl_2006_stardust_return_capsule_mass_cost_scope` — NASA/JPL’s Stardust press kit reports a “46-kilogram (101-pound) return capsule” and $128.4 million in spacecraft development within a $168.4 million program total excluding launch (Quick Facts, printed p. 6). The source gives no capsule cost allocation or recurring production rate. Spacecost’s `Return capsule recurring cost` row stores $150,000/kg [$50,000, $400,000], described as half the mining-rig rate with Stardust and OSIRIS-REx SRC heritage, but provides no cost derivation. **Verdict:** the source supplies mass and program-cost scope only; no replacement rate can be inferred. Open `rc-497`. Extracted data: `extracted_data/r635_stardust_capsule_mass_program_cost_scope.csv`.


## R653 — Mining-payload recurring cost basis (2026-11-11)

`spacecost_mining_payload_recurring_cost_current_2026` — spacecost’s `Mining payload recurring cost` row stores $300,000/kg [$100,000, $1,000,000] for burdened deep-space mining equipment. Its note says the bracket “has no registered source”; it says the prior SSCM and NICM anchors were removed because they could not be checked, and that NICM is an instrument model rather than a structures or mechanisms model. The SSCM and NICM registry records remain `registered_not_pulled`. **Verdict:** the estimate has no checked CER or cost basis matched to mining hardware; no replacement rate is inferred. Open `rc-517`. Extracted: `extracted_data/r653_mining_payload_recurring_cost_code_audit.csv`.


## R654 — NRE overlap fraction in the cost model (2026-11-11)

`economicspace_nre_recurring_overlap_fraction_code_current_2026` — economicspace sets `nre_recurring_overlap_fraction` to 0.30, described as a “mid-range de-duplication.” The code says the recurring-cost brackets are regressions on total program cost and therefore include development; its cost formula charges the spacecraft NRE at `1 − overlap_fraction` per mission. The related spacecost mining-payload row now says its $100,000–$1,000,000/kg bracket has no registered source, and the SSCM/NICM records remain `registered_not_pulled`. **Verdict:** the 0.30 share has no checked derivation from a cost model or matched hardware class. Open `rc-518`; no replacement fraction inferred. Extracted: `extracted_data/r654_nre_recurring_overlap_fraction_code_audit.csv`.


## R658 — economicspace return-structure candidates rechecked (2026-11-12)

At economicspace main `c1a6333e6e50e0e3658d05e47128a94ce4f07831` (calc 1.45.0), `heat_shield_frac_of_payload` remains 0.15 as a flat returned-payload fraction, with no entry-speed scaling basis (**rc-134**). The current comment still states that Cygnus’s approximately 1,500 kg dry mass has no source; `return_structure_frac_of_payload` remains 0.15 and the configuration-specific PCM mass basis remains unresolved (**rc-423**). Both candidates remain open. Existing extracts: `extracted_data/r453_xing_2026_tps_mass_and_entry_speed.csv`; `extracted_data/r475_alpert_high_velocity_tps_sizing.csv`; `extracted_data/r557_orbital_cygnus_pcm_mass_by_configuration.csv`.


## R677 — Upper-stage and tank recurring-cost anchors rechecked (2026-11-12)

- **spacecost_stage_and_tank_recurring_cost_code_current_2026**: Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` retains an expendable upper-stage rate of $4,800/kg [$1,750,$13,400]. Its note derives the point as the geometric centre of ~$10M (Musk 2018) or an unnamed ~$7M 2026 third-party estimate for a ~4,000 kg Falcon 9 upper stage, and ~$30M for a ~2,250 kg Centaur III; it states no institutional document prices either stage. The tank-only row remains $6,000/kg [$3,000,$25,000], based on ~$30M Centaur III less an assumed ~$20M RL10, divided by ~1,880 kg of structure, then rounded upward; the high end is called plausible rather than sourced.
- **nasa_oig_2020_ig-20-012_sls_program_costs_contracts**: NASA OIG p. 23 reports an opportunity to buy “the hardware for a second ICPS for $29 million.” This is a whole-stage comparator for a different configuration, not a Centaur III price or a tank-component allocation.
- Verdict: keep both numeric rates pending separate matched bases for whole-stage and tank-only costs; no replacement inferred. **rc-421** remains open. Existing extraction: `extracted_data/r555_nasa_oig_icps_price_vs_centaur_tank_cost_anchor.csv`; new extraction: `extracted_data/r677_stage_tank_cost_basis.csv`.


## R773 - NRE overlap disclosure in the verification worksheet (2026-11-15)

`economicspace_nre_overlap_verification_sheet_current_2026`: the current 2018 DT cislunar worksheet lists I126 as `overlap`, value 0.30, and flags it NEED BACKING. The input cites the configuration field but describes it only as "recurring overlap deducted from NRE".

`economicspace_nre_recurring_overlap_fraction_code_current_2026`: `modules/calc.py` now says the recurring hardware bracket has no registered source and calls 0.30 a scenario with no derivation. The worksheet formula applies `NRE_bus * (1 - overlap) / mission_count` to spacecraft development NRE. `spacecost_mining_payload_recurring_cost_current_2026` records the related $300,000/kg [$100,000, $1,000,000] recurring mining-payload estimate; its matched cost basis remains open under rc-517. Closed rc-518 applied the code-comment clarification but did not target the worksheet input; rc-330 concerns a separate mining-technology development term.

Verdict: carry the scenario status and missing-derivation limit into I126, and expose sensitivity to the overlap assumption. Preserve 0.30; no numeric replacement inferred. **rc-644**. Extracted: `extracted_data/r773_nre_overlap_verification_sheet_gap.csv`.

## R777 — NRE mission-count input is a run scenario (2026-11-15)

`economicspace_nre_mission_count_verification_sheet_current_2026`: the cislunar worksheet input I63 is 1 mission and is flagged NEED BACKING. `economicspace_nre_amortization_config_current_2026`: `CalcConfig.nre_amortization_missions` defaults to 1; its comment says “If 1, the first mission carries the full NRE; raise N to spread across a fleet” (lines 1055–1057). The comment describes the setting's effect but gives no empirical basis for choosing one mission as the run's programme size.

Verdict: identify I63=1 as the fixed scenario used by this archived row and carry the configuration explanation into the worksheet; preserve 1 and do not present it as an externally estimated fleet size. Applied `rc-249` and `rc-250` concern programme search and fixed-N cost accounting; open `rc-644` concerns the separate NRE-overlap input I126. Open `rc-647`; no numeric replacement inferred. Extracted: `extracted_data/r777_nre_amortization_mission_scenario.csv`.

## R824 — NRE-overlap current worksheet input recheck (2026-11-17)

- **economicspace_nre_overlap_verification_sheet_current_2026**: the current best-case worksheet maps nre_recurring_overlap_fraction=0.30 to I122 and marks it NEED BACKING. Its current I126 is contingency_fraction=0.20 with a separate NASA mission cost-growth citation; the prior rc-644 input number I126 no longer names the overlap.
- **economicspace_nre_recurring_overlap_fraction_code_current_2026**: modules/calc.py lines 1163-1168 call 0.30 a scenario with no derivation because the recurring hardware bracket has no registered source.
- **Verdict**: keep rc-644 open and carry its scenario/sensitivity scope into current I122; preserve 0.30.
- Extracted: extracted_data/r824_nre_overlap_live_sheet_i122.csv.

## R826 — Current worksheet mapping for propellant-tank cost (2026-11-17)

**economicspace_current_bestcase_verification_sheet_2026**: input I119 maps to operational_costs.csv, row “Propellant tank recurring cost,” is marked NEED BACKING, and prints $6,000/kg tank dry mass [3,000, 25,000].

**spacecost_stage_and_tank_recurring_cost_code_current_2026**: the current row derives its lower bound from an approximately $30M Centaur III stage anchor less an assumed approximately $20M RL10 cost; the sheet notes that the stage-cost anchor has no institutional source.

Verdict: rc-421 remains open for the tank-only cost basis; the current sheet adds a live input mapping but no replacement value. Extracted: extracted_data/r826_live_sheet_propellant_tank_cost_i119.csv.


## R849 — Titan IV Centaur unit-cost comparator (2026-11-17)

`gao_nsiad_1990_titan_iv_centaur_unit_cost`: GAO’s *Space Launch: Cost Increases and Schedule Delays in the Air Force’s Titan IV Program* (NSIAD-90-113), Table 3.1 (printed p. 16), labels the column “Estimated unit cost” and lists $52.0 million for General Dynamics’ Centaur upper stage; the same table lists a $951.8 million subcontract price, with footnote a dating that subcontract price as of May 1989. Table 3.2 (printed p. 17) lists $128.9 million for a complete Titan IV vehicle with Centaur, not for the Centaur component alone. On printed p. 12, GAO attributes per-vehicle cost differences partly to RDT&E cost sharing and the Centaur cost being spread over more vehicles and launches.

At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/operational_costs.csv` still stores $4,800/kg [$1,750, $13,400] for “Expendable upper stage recurring cost” and $6,000/kg [$3,000, $25,000] for “Propellant tank recurring cost”; the tank note derives its point from an unsupported Centaur III stage estimate less an assumed RL10 cost.

Verdict: the GAO figure is a historical Titan IV contract comparator for a Centaur upper stage, not a current Centaur III price and not a tank-only allocation. It does not establish a replacement for either stored rate; keep `rc-421` open. Extracted: `extracted_data/r849_titan_iv_centaur_unit_cost_comparator.csv`.

## R851 — Archived mining-payload cost citation boundary (2026-11-17)

**economicspace_stage3_archive_table_selection_code_current_2026**: At Economicspace main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, `campaign/worked_calculation.py` `transport_tables_for()` selects the newest frozen Stage 3 set an archived row could have read. It identifies `campaign/stage3/spacecost-0.4.0/` as the set frozen when Spacecost v0.5.0 was adopted on 2026-09-28.

**economicspace_stage3_spacecost_0_4_0_mining_payload_row_2026**: The frozen `Mining payload recurring cost` row stores $300,000/kg with a $100,000–$1,000,000 range and says “Aerospace Corp Small Mission Cost Model and NASA NICM bracket recurring deep-space hardware at $100k-$1M/kg.”

**spacecost_mining_payload_recurring_cost_current_2026**: Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` keeps the same values but says no published cost-estimating relationship or recurring unit cost matches mining hardware and labels the point and range a scenario. Its note says the prior SSCM and NICM anchors could not be checked and NICM is an instrument model, not a structures or mechanisms model. Applied rc-517 covers this current Spacecost row.

**economicspace_current_bestcase_verification_sheet_2026**: The supplied 2026-11-16 verification sheet maps I113 to the current Mining payload recurring cost row and prints the scenario qualification on p. 29. It does not select the archived `spacecost-0.4.0` copy.

Upstream: Economicspace's timestamped Stage 3 `spacecost-0.4.0/operational_costs.csv`, row `Mining payload recurring cost`, remains selected for archived runs that could have read that set. Verdict: carry the current no-matched-CER and scenario disclosure into the frozen row; preserve $300,000/kg [$100,000, $1,000,000] for historical reproducibility. No numeric replacement inferred. **rc-727**. Extracted: `extracted_data/r851_frozen_mining_payload_cost_note.csv`.

## R852 — Archived Stage 3 electric-cost and battery-source lineage (2026-11-17)

**economicspace_stage3_archive_table_selection_code_current_2026**: At Economicspace main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, `campaign/worked_calculation.py` `transport_tables_for()` selects the newest frozen Stage 3 set an archived row could have read. The selected set can be `campaign/stage3/spacecost-0.4.0/`, frozen when Spacecost v0.5.0 was adopted on 2026-09-28.

**economicspace_stage3_spacecost_0_4_0_electric_propulsion_recurring_cost_row_2026**: The frozen Electric propulsion system recurring cost row stores $1,500,000/kW [$500,000, $3,000,000]. Its note derives $1.5–2M/kW from a claimed $10–15M NEXT-C flight string but does not say that the per-string price has no published source.

**spacecost_electric_propulsion_system_recurring_cost_current_2026**: Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` retains the same values and now says no published source prices a NEXT-C string. NASA Glenn release 15-011 reports an $18,410,242 cost-share contract for design, fabrication and testing of two flight thrusters, two PPUs, and a prototype PPU. NASA OIG IG-24-003 Table 1 (printed p. 6) lists a $730.9M fixed-price Gateway Power and Propulsion Element contract. These contract scopes do not establish a recurring per-string price. The current verification sheet maps I118 to the live row and carries the caveat on p. 30. Open rc-299 addresses the live Spacecost row, not the frozen copy. **rc-728**.

**economicspace_stage3_spacecost_0_4_0_energy_storage_usable_specific_energy_row_2026**: The frozen Energy storage usable specific energy row stores 104 Wh/kg [70, 160], calculated from 130 Wh/kg at system level times 0.80 depth of discharge. The frozen note attributes 130 Wh/kg to halving 250–300 Wh/kg cell values for packaging, harness, balancing and thermal, without naming a measured pack source.

**spacecost_energy_storage_usable_specific_energy_current_2026**: The current Spacecost row identifies 130 Wh/kg as an engineering analogy from five protected NASA D-RATS spacesuit-simulator packs: 124–133 Wh/kg, mean 129.6 (Bennett & Baldwin 2010, Table 5). It says these are not spacecraft batteries. Schmitz et al. (2023), Table 3, report 175 Wh/kg at 80% depth of discharge and 90% charge/discharge efficiency, or 140 Wh/kg usable. The current verification sheet carries the source limits for I68 on pp. 21 and 40; these are absent from the frozen copy. Applied rc-342 updated the current Spacecost row, not this frozen copy. **rc-729**.

Upstream: Economicspace's timestamped Stage 3 `spacecost-0.4.0/operational_costs.csv`, rows Electric propulsion system recurring cost and Energy storage usable specific energy, remains a possible input to archived runs selected by table date. Verdict: carry forward the current per-string price limitation and the D-RATS battery analogy's provenance and scope into the frozen rows. Preserve historical values and ranges; no numeric replacement inferred. Extracted: `extracted_data/r852_frozen_stage3_operational_cost_note_gaps.csv`.


## R853 — Latest frozen Stage 3 stage and tank cost anchors (2026-11-17)

**economicspace_stage3_spacecost_0_14_0_expendable_upper_stage_row_2026**: The `spacecost-0.14.0` row stores $4,800/kg [$1,750, $13,400] of stage dry mass. Its note takes a geometric centre from ~$10M (Musk 2018) or an unnamed ~$7M Falcon 9 upper-stage estimate and ~$30M for Centaur III, then says no institutional document prices either anchor.

**economicspace_stage3_spacecost_0_14_0_propellant_tank_recurring_cost_row_2026**: The frozen row stores $6,000/kg [$3,000, $25,000] of tank dry mass. It derives about $5,300/kg from a ~$30M Centaur III stage less an assumed ~$20M RL10, states that the ~$30M has no institutional source, and calls the upper range endpoint plausible. Current Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` retains the same nominal values; open **rc-421** covers the price-anchor and tank-allocation gap.

The archived table selector chooses the newest date-compatible frozen Stage 3 set; `spacecost-0.14.0` is pipeline 1.23.6, catalog date 2026-10-17. The supplied verification sheet p. 47 maps I119 to “Propellant tank recurring cost” and states “(needs backing) the row’s notes name no published source.” GAO NSIAD-90-113 Table 3.1 reports a $52.0M report-era Centaur unit-cost comparator (printed p. 16); NASA OIG IG-20-012 reports a $29M second-ICPS hardware-purchase opportunity (p. 23). Neither is a current Centaur III unit price or a tank-only allocation.

Upstream: Economicspace `campaign/stage3/spacecost-0.14.0/operational_costs.csv`, rows Expendable upper stage recurring cost and Propellant tank recurring cost. Verdict: retain the historical values as estimates; no numeric replacement inferred. **rc-730**. Extracted: `extracted_data/r853_stage3_upper_stage_and_tank_cost_rows.csv`.


## R854 — Frozen return-capsule recurring-cost basis (2026-11-17)

**spacecost_return_capsule_recurring_cost_current_2026**: Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` retains $150,000/kg [$50,000, $400,000] and says “no capsule unit cost is published”; the point and range are an engineering scenario, not a derived recurring rate. The note limits JPL’s Stardust press-kit evidence to capsule mass and whole-spacecraft/program costs (Quick Facts, printed p. 6; **rc-497**).

**economicspace_stage3_spacecost_0_14_0_return_capsule_recurring_cost_row_2026**: The frozen 1.23.6 row stores the same $150,000/kg [$50,000, $400,000], describes the value as half the mining-payload rate and names Stardust/OSIRIS-REx SRC heritage, but omits the current no-published-unit-cost and scenario qualification. The row is selected for compatible archived runs by the Stage 3 table selector.

Upstream: Economicspace `campaign/stage3/spacecost-0.14.0/operational_costs.csv`, row Return capsule recurring cost. Verdict: preserve the historical rate, carry forward the current scenario and source-scope note, and infer no numeric replacement. **rc-731**. Extracted: `extracted_data/r854_frozen_stage3_return_capsule_cost_note.csv`.


## R855 — Frozen Stage 3 mining-payload cost qualification (2026-11-17)

**economicspace_stage3_archive_table_selection_code_current_2026**: `transport_tables_for()` selects the newest date-compatible frozen Stage 3 set for archived rows; the selector includes `spacecost-0.14.0` (pipeline 1.23.6, catalog date 2026-10-17).

**economicspace_stage3_spacecost_0_14_0_mining_payload_row_2026**: The frozen Mining payload recurring cost row stores $300,000/kg [$100,000, $1,000,000] and says “the $100k-$1M/kg bracket has no registered source.” It retains the earlier SSCM/NICM framing but omits the current no-matched-CER scenario qualification.

**economicspace_current_bestcase_verification_sheet_2026**: The supplied verification sheet, p. 29, maps I113 to Mining payload recurring cost and reproduces the current no-matched-CER scenario qualification.

**spacecost_mining_payload_recurring_cost_current_2026**: The current row retains the same value and range; it says no published cost-estimating relationship or recurring unit cost matches mining hardware, labels the value a scenario input, and says generic spacecraft or instrument CERs are not applied without showing they fit (rc-517).

Upstream: Economicspace `campaign/stage3/spacecost-0.14.0/operational_costs.csv`, row Mining payload recurring cost. Verdict: preserve the historical value and range while carrying the current source and fit limits into the frozen row; no numeric replacement inferred. **rc-732**. Extracted: `extracted_data/r855_frozen_stage3_mining_cost_source_caveat.csv`.


## R856 — Frozen Stage 3 surface-lander cost comparator scope (2026-11-17)

**economicspace_stage3_archive_table_selection_code_current_2026**: The archived-row selector includes `spacecost-0.14.0`, pipeline 1.23.6, catalog date 2026-10-17.

**economicspace_stage3_spacecost_0_14_0_surface_lander_row_2026**: The frozen Surface lander recurring cost row stores $200,000/kg [$100,000, $500,000] and names Apollo LM and CLPS landers as heritage; it has no CLPS cost comparator or whole-service/hardware boundary.

**nasa_oig_2024_ig_24_013_clps_delivery_costs**: CLPS task orders cover full-scope payload delivery through operation; OIG reports the TO2-IM value at $81.7M initially and $122.0M after growth (IG-24-013, pp. 3, 12).

**kuettel_et_al_2024_im1_nova_c_dry_mass**: Nova-C dry mass is 677 kg (AAS 24-282, p. 2).

**spacecost_surface_lander_recurring_cost_current_2026**: The current row adds derived CLPS ratios of ~$120.7k/kg initially and ~$180.2k/kg after growth, labels them “whole-service prices rather than hardware,” and cites rc-300. These package-price comparisons do not give recurring lander hardware rates.

Upstream: Economicspace `campaign/stage3/spacecost-0.14.0/operational_costs.csv`, row Surface lander recurring cost. Verdict: carry the comparator’s scope into the frozen note; preserve the historical value and range, with no numeric replacement inferred. **rc-733**. Extracted: `extracted_data/r856_frozen_stage3_surface_lander_scope.csv`.

## R857 — Frozen Stage 3 FAA compliance-cost qualification (2026-11-17)

**economicspace_stage3_archive_table_selection_code_current_2026**: The archived-row selector includes `spacecost-0.14.0`, pipeline 1.23.6, catalog date 2026-10-17.

**economicspace_stage3_spacecost_0_14_0_faa_part450_compliance_row_2026**: The frozen FAA Part 450 licensing compliance row stores $2,500,000/program [$1,000,000, $5,000,000], describes internal engineering, legal and safety-case work, and cites R48582 for the no-application-fee premise; it does not call the amount an estimate.

**spacecost_faa_part450_compliance_cost_code_current_2026**: The current Spacecost note says “no document gives this amount” and cites 2,903 FAA paperwork hours per initial application as an effort floor before safety-case engineering (rc-538). **faa_pra_notice_2019_streamlined_license_burden_hours**: the notice reports 2,903 paperwork hours per initial application (printed p. 4913), not a dollar cost. **crs_r48582_commercial_launch_reentry_regulations**: the report supplies no application-processing fee amount (rc-232).

Upstream: Economicspace `campaign/stage3/spacecost-0.14.0/operational_costs.csv`, row FAA Part 450 licensing compliance. Verdict: carry the estimate declaration and workload/source limits into the frozen note; retain the separate statutory per-launch fee boundary and the historical value/range, with no numeric replacement inferred. **rc-734**. Extracted: `extracted_data/r857_frozen_stage3_faa_cost_basis.csv`.

## R863 — Spacecost downleg TPS mass fraction scope (2026-11-17)

At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `delivery.py` calls 0.15 a modelling choice and says, “One fraction for every destination, at no stated entry speed.” Its downleg calculation uses 0.15 × (1 + 0.10) = 0.165 kg TPS per kg of delivered cargo. The code cites Dec & Braun (2006) inline, but Spacecost `CITATIONS.md` has no entry for the paper. **dec_braun_2006_approximate_ablative_tps_sizing_tool** (AIAA 2006-780), Table 2 (hosted PDF p. 12), labels “Lunar Return 11 km/s” and “Short-Transfer Mars Return 14 km/s”; PICA total thickness is 8.324 and 10.873 cm, with recession 0.726 and 3.828 cm. These trajectory-specific thicknesses do not provide a generic TPS mass-per-cargo fraction. **rc-134** tracks Economicspace’s separate 0.15 dial; this candidate covers Spacecost’s independently applied value. Verdict: add the bibliographic entry and keep the fraction as a scenario pending a trajectory/geometry basis or sensitivity; no numeric replacement inferred. **rc-739**. Extracted: `extracted_data/r863_spacecost_downleg_tps_fraction_scope.csv`.

## R894 — Spacecost CSV citation omits the package release identifier (2026-11-18)

- `spacecost_package_release_output_provenance_code_current_2026` [T4]: Spacecost `CITATIONS.md` §9 instructs users to cite both package release `vX.Y.Z` and data contract `pipeline_version` (lines 320-329). The guide identifies `spacecost.__version__` as the package release and states that output CSVs carry the data contract.
- At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `build.py` stamps each output with `catalog_date` and `pipeline_version` only (lines 98-105). `config.py` says a package release can change without changing the data contract; `__init__.py` defines the current package release as 0.17.1 and data contract as 1.26.1. The adjacent `reference/summary_meta.json` contains no version fields.

Verdict: the output tables carry the data-contract identifier but not the separate package release the citation guide asks users to cite. Open `rc-773` for per-build package-version provenance; table values are unchanged. Extracted: `extracted_data/r894_spacecost_package_release_csv_provenance.csv`.

## R897 — Economicspace Stage 4 Git-commit citation metadata

- **economicspace_profitability_output_git_commit_provenance_code_current_2026**: At Economicspace main `@b7b7591ccb61b4825b4089a692b5b2c7501491f4`, `CITATIONS.md` lines 376–379 says quoted results need `pipeline_version`, `catalog_date` and the Git commit. `modules/calc.py` lines 10357–10373 stamps `catalog_date` and `pipeline_version` before writing `profitability_catalog.csv`. `ui.py` lines 937–965 records run time, selected stages, destination, changes, stage versions and configuration in the GUI run manifest, without a commit field. `README.md` lines 1013–1028 lists the Stage 4 CSV output.
- **Upstream fields:** Economicspace Stage 4 `profitability_catalog.csv` and GUI run-manifest metadata.
- **Verdict:** Open rc-777 for a Git commit identifier carried with Stage 4 results. The documented CSV stamps and GUI manifest do not preserve it. No model values are changed.
- **Extracted data:** `extracted_data/r897_economicspace_stage4_commit_identifier_gap.csv`.

## R902 — Verification worksheet Git-commit provenance (2026-11-18)

- **economicspace_verification_sheet_commit_provenance_code_current_2026**: At Economicspace main `@e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, `CITATIONS.md` §8 requires the Git commit alongside the version and catalog date when quoting a result. The `campaign/verification_sheet.py` footer emits the generated date and source CSV name (lines 6573–6580), with no commit field. The supplied worksheet p. 1 identifies the catalog and price releases, Stage 3 contract, calc 1.46.0 and build date; p. 48 says “Generated 2026-11-16 from lunar_surface__benef__search-on__calc-1.46.0.csv.gz.” Neither page gives a commit.

Upstream: generated verification worksheet provenance. Verdict: a separate output artifact lacks the required commit identifier; **rc-782**. No figures changed. Extracted: `extracted_data/r902_economicspace_verification_sheet_commit_gap.csv`.

## R903 — Spacecost TPS heritage source omitted from its bibliography (2026-11-18)

- **spacecost_tps_bibliography_gap_code_current_2026**: At Spacecost main a401930efe30aaad01aafd2b3cb332ad0438c841, spacecost/operations.py line 146 cites “NTRS 20140005558 for material data” in the Heat shield / TPS note. CITATIONS.md identifies itself as the project bibliography; §4 Operational costs (lines 166–233) has no Stackpoole entry. A whole-file search at this commit finds no Stackpoole or 20140005558.
- **stackpoole_2013_pica_pica_x_postflight_eval**: General_Research registers Stackpoole, Kao, Qu & Gonzales (2013), NASA ARC-E-DAA-TN9994 / NTRS 20140005558. NTRS hosts only the title/summary slide; the recorded PICA and PICA-X material heritage/performance figures do not include a per-kg cost.
- **Upstream row**: Spacecost reference/operational_costs.csv, “Heat shield / TPS for Earth return”; the source note is in spacecost/operations.py.
- **Verdict**: rc-783 requests a complete bibliography entry in CITATIONS.md §4 scoped to material heritage/performance. No TPS cost value or range is changed.
- **Extracted data**: extracted_data/r903_spacecost_tps_citation_bibliography_gap.csv.

## R940 — economicspace frozen Stage 3 provenance file (2026-11-18)

economicspace 75253b5a744f2155cce9b9a0abbd829578a44a6e (PR #209, master 1.79.0; no stamp moves). The owner decided that candidates asking to carry current notes into frozen `campaign/stage2/` or `campaign/stage3/` copies are applied without editing the frozen CSVs: `campaign/stage3/PROVENANCE.md` now records each flagged row's correction (unsourced anchor, scenario label, comparator scope or open review) beside the current spacecost treatment. `git diff --stat` of `campaign/stage3/` at that merge is the new file only, so every archived cell still reproduces.

- `spacecost-0.4.0/operational_costs.csv`: rc-727, rc-728, rc-729.
- `spacecost-0.10.0/`: rc-704, rc-705.
- `spacecost-0.14.0/launch_vehicles.csv`: rc-707, rc-708, rc-709, rc-710, rc-711, rc-712, rc-721, rc-723, rc-725.
- `spacecost-0.14.0/operational_costs.csv`: rc-730, rc-731, rc-732, rc-733, rc-734, rc-735, rc-738.
- `spacecost-0.14.0/propellants.csv`: rc-706, rc-775; top-level `launch_vehicles.csv`: rc-722.

Verdict: all twenty-four closed as applied. Extracted data: none new.

## R941 — economicspace worksheet quotes frozen rows' current counterparts (2026-11-18)

economicspace e477b00ffa7810a6f2daad76290d428eee8b70b3 (PR #210, master 1.80.0; no stamp or number moves). `campaign/verification_sheet.py` now quotes, beside any row read from a frozen Stage 3 set, the installed spacecost release's row of the same name, in a span the backing ledger does not read; `campaign/stage3/PROVENANCE.md` gains the 0.5.0 and top-level 1.15.0 entries. Measured before and after with `--check`: backing counts unchanged (default 2018 DT page 40 sourced, 84 need backing; `mars_orbit__raw__search-off` 40 and 45), and 32 frozen rows on the default page now quote their counterpart.

- rc-584, rc-624, rc-625, rc-629, rc-631, rc-645, rc-646, rc-684 (spacecost-0.5.0 rows) and rc-652 (top-level row 52).

Verdict: all nine closed as applied. Extracted data: none new.

## R965 — Frozen Stage 3 tank-cost citation gap (2026-11-19)

**economicspace_stage3_spacecost_0_5_0_propellant_tank_recurring_cost_row_2026**: Economicspace main `b6c962c4f06dc5b625fee39044d8d1699ac564c9`, `campaign/stage3/spacecost-0.5.0/operational_costs.csv:11`, stores $6,000/kg [$3,000, $25,000] of tank dry mass. Its note derives about $5,300/kg from 1,880 kg of structure, an approximately $30M Centaur III stage, and an assumed approximately $20M RL10; it names no source for those anchors or the tank-only allocation.

**economicspace_verification_sheet_c_tank_mapping_current_2026**: The current default 2018 DT worksheet maps `c_tank` to input I123. `verification_sheet.py` builds the input from the selected operations row and removes the installed Spacecost counterpart span before backing classification; I123 remains NEED BACKING because the frozen row itself names no published source. The `spacecost-0.5.0` section of `campaign/stage3/PROVENANCE.md` does not list the tank row. Existing rc-421 targets current Spacecost; rc-730 targets frozen `spacecost-0.14.0`.

- **Verdict**: Preserve the frozen value and range for reproducibility; qualify the tank-only rate as an estimate pending sources for the Centaur III price, RL10 subtraction, and tank allocation. No numeric replacement inferred. **rc-825**.
- **Extracted data**: `extracted_data/r965_frozen_spacecost_0_5_0_tank_row_i123.csv`.

## R973 — Spacecost operating-cost bibliography omits NASA OIG IG-20-012 (2026-11-19)

- `spacecost_citations_report_reference_gaps_current_2026`: At Spacecost main `868f42890ac97ee40a50d79f7b33863046edb0ff`, `spacecost/operations.py` lines 170–179 cite NASA OIG IG-20-012 p. 23 for a second-ICPS hardware comparator; `CITATIONS.md` §4 has no report entry.
- `nasa_oig_2020_ig-20-012_sls_program_costs_contracts`: NASA OIG reports an opportunity to buy “the hardware for a second ICPS for $29 million” (p. 23). This is a whole-stage comparator, not a tank-only allocation.
- **Verdict:** open **rc-833**; add the full title, IG-20-012 identifier, date, official URL, and p. 23 locator. Bibliography completeness only; no recurring-rate replacement inferred. Distinct from rc-421 and rc-730.
- **Extracted data**: `extracted_data/r555_nasa_oig_icps_price_vs_centaur_tank_cost_anchor.csv`.

## R985 — Tank-cost scope recorded upstream; IG-20-012 referenced (2026-11-19)

At Economicspace main bed74f10d0d26069690780b87b3d82f36235dd40 (PR #213, master 1.83.0), `campaign/stage3/PROVENANCE.md` records the propellant tank recurring cost in the top-level and 0.4.0 to 0.10.0 sets, $6,000/kg [3,000, 25,000], as an engineering estimate whose Centaur III and RL10 anchors and tank-only allocation have no source; the worksheet prints the same beside `c_tank` (I123), which stays NEED BACKING (rc-825). At Spacecost main 5ae7f70855d24c71dc54fc3a916624f325c034e8 (PR #53), CITATIONS.md section 4 gains `nasa_oig_2020_ig-20-012_sls_program_costs_contracts` with its p. 23 locator as a whole-stage comparator (rc-833). Frozen bytes and values unchanged.

Verdict: rc-825, rc-833 closed as applied. Extracted data: none new.

## R990 — Spacecost lander rate scoped as hardware-only upstream (2026-11-19)

At Spacecost main a6901495d257cbcd018b31e238498c94f301c865 (PR #54, 0.18.7, data contract 1.27.7; notes and comments only), the surface lander note labels $200,000/kg [100,000, 500,000] a hardware-only scenario that the CLPS whole-service ratios neither set nor bound (rc-300). Value unchanged.

Verdict: rc-300 closed as applied. Extracted data: none new.
