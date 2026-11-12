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
