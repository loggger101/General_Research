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
## R120 - ehresmann_2021 CEAS Space Journal hosted, CC BY in-file (2026-10-05; queue -1)

**ehresmann_2021_automated_system_analysis_and_design_tool_for_spacecrafts [T1]** - re-classed registered_not_pulled -> full_text_hosted. The Springer content PDF now pulls live via link.springer.com/content/pdf/10.1007/s12567-021-00383-3.pdf; committed to full_texts/ehresmann_herdrich_fasoulas_2021_automated_system_analysis_design_tool_ceas_space_journal_ccby.pdf (4,442,544 B sha256=c26fb1fa9bc4b800c12f0712285f89c5841afa907400bd45d5c74dca53ab8d36). CEAS Space Journal 14:327-354 (28 pages), in-file Open Access Creative Commons Attribution statement. Verbatim title: "An automated system analysis and design tool for spacecrafts - a generic full-system estimation software applied to actual flight missions; context for d21's estimating-tool rows.

### Round 146 - institutional TPS cost data registered (+2 T2 full_text_hosted): the first dollar figures behind d21's heat-shield cell

The opening brief's 'Heat shield / TPS for Earth return' row ($50k/kg [20k, 150k] of TPS mass) is flagged upstream as an engineering estimate - "NASA / SpaceX have not published a per-kg PICA-X cost". This round registers the two closest institutional sources found on NTRS; neither prints a $/kg material price, so both are context/bound class and no re-pin is proposed.

**peterson_haas_1971_shuttle_tps_refurbishment_cost_study_nasa_cr-iii_30 [T2; full_text_hosted ntrs-public-use]** - Lockheed Missiles & Space Company final report under Contract NAS1-IQ-94 (NASA CR-III_30), 325 pp, NTRS 19710008613, GOV_PUBLIC_USE_PERMITTED + zero in-file copyright statements. The first institutional per-unit-area TPS cost data: p.58 'the operational cost per square foot of TPS material applied to a delta body orbiter is presented', ablators highest at '~$50,000' (nose cone $85,000) over a 10-year life; p.60 '$1300 to $2800 per square foot for metallic and non-metallic TPS system'. These are MAINTENANCE/operational costs per unit AREA - a different quantity from the cell's recurring manufacturing $/kg, but they bracket the same cost family (ablative >> tile) at institutional scale. Microfilm-era OCR layer: every figure verified at word level on pp.58/60 before quoting; one source-scan artifact ('$52,0OO') recorded as printed per R97 convention.

**mcguire_covington_goldstein_arnold_beck_2013_msl_aft_heatshield_trade_studies_ippw10 [T2; full_text_hosted ntrs-public-use]** - NASA Ames IPPW-10 abstract record (June 17-21 2013), NTRS 20130014700, PUBLIC_USE_PERMITTED + zero in-file copyright statements. MSL-class aft heat-shield trade study: 'system studies ... compare masses and estimated manufacturing costs of options for the as-flown MSL aft body' SLA-561V; thickness optimization could cut aft shield mass ~40%; AFRSI (Shuttle lee-side heritage, 'relatively inexpensive manufacturing') would be 60% lighter than as-flown SLA. Manufacturing-cost comparison class - no per-kg figure in the abstract record -> context/bound.

Key numbers committed in extracted_data/r146_tps_costs_key_numbers.csv (7 data rows x 6 cols). Round also ran a queue re-probe wave: kopp_lean_2011 Wiley pdfdirect still 403, dorrington_olsen_2026 all three ScienceDirect routes still 403 with the CANONICAL PII S0094576525007659 (resolved from Crossref this round - earlier probes had no PII), pentikainen_2026 aanda.org full_html route 403, ferrais_2022 ORO bitstream 403. Registry **543 -> 545** sources (T2 +2); queue unchanged at 106.

### Round 159 - heat-shield mass scaling with entry speed: d21's opening-brief item gets its institutional method (+2 T2 full_text_hosted)

The opening brief's second unanchored item asked for sources on how heat-shield mass scales with entry speed, behind upstream's flat `heat_shield_frac_of_payload` / DOWNLEG_TPS_FRAC = 0.15 dial (upstream: 'no TPS-fraction row in these tables to derive it from'). This round registers the two closest institutional sizing records found on NTRS; both size thickness rather than price or fraction, so both are context/bound class and no re-pin is proposed.

**dec_braun_2006_approximate_ablative_tps_sizing_tool [T2; full_text_hosted ntrs-public-use]** - Dec & Braun (NASA LaRC + Georgia Tech), 'An Approximate Ablative Thermal Protection System Sizing Tool for Entry System Design', AIAA 2006-780, 44th AIAA Aerospace Sciences Meeting and Exhibit, Reno NV Jan 9-13 2006; NTRS 20080013535 CONFERENCE_PAPER record, determinationType=PUBLIC_USE_PERMITTED + zero in-file copyright statements across all 15 pages. DOI 10.2514/6.2006-780 Crossref-verified live this round - the 'AIAA 2005-5915' printed inside the paper is a self-citation to Putnam et al. (ref 16), not this paper's number; venue taken from Crossref. THE institutional sizing method: required thickness from trajectory data via heat-of-ablation recession coupled to a one-dimensional finite-difference thermal response, iterated until bondline temperature matches criteria; 'Given the vehicle geometry and the TPS material density, the total mass of the heatshield can be calculated'. Table 2 gives exactly the entry-speed scaling d21 asked for - Apollo capsule at lunar-return 11 km/s vs short-transfer Mars-return 14 km/s: PICA stagnation total thickness CMA 8.324 -> 10.873 cm (recession 0.726 -> 3.828), FM5055 5.770 -> 6.473 (approximate solution 5.961/6.983): shield mass grows super-linearly with entry speed, recession-dominated for PICA. Verified against the Pathfinder SLA-561V and Stardust PICA project sizings; Stardust case: peak heat rate 1126 W/cm2, total load 28,000 J/cm2, stagnation thickness 4.8 cm with 1.2 cm recession.

**mahzari_et_al_2022_mars2020_tps_development_sizing [T2; full_text_hosted ntrs-public-use]** - Mahzari, Beck, Hwang, Monk, Morgan, Williams (NASA Ames) + Edquist (LaRC), 'Development and Sizing of the Mars 2020 Thermal Protection System', AIAA Aviation 2022 presentation dated Jun-30-2022 on p.1; NTRS 20220009403 PRESENTATION record (conference version), determinationType=PUBLIC_USE_PERMITTED + explicit in-file statement 'This material is a work of the U.S. Government and is not subject to copyright protection in the United States.' Institutional record of the sizing method in practice: Mars 2020 thicknesses frozen to MSL heritage ('No major changes to the TPS materials and thicknesses compared to MSL'); goal 'to demonstrate that the design thicknesses were sufficient to maintain the TPS/structure bondline temperature below specified limits' with RSS'd trajectory/heating/material uncertainties, 'Similar sizing methodology to the one used for MSL and Orion missions'; six arc-jet tests (IHF 348 / PTF 158 etc.) + FIAT thermal-response model verification against measured recession/bondline data.

Key numbers committed in extracted_data/r159_tps_sizing_key_numbers.csv (9 rows x 6 cols; every quoted span count==1 re-verified pre-write). No rc/no re-pin - context/bound class behind the flat dial: Dec & Braun shows PICA stagnation thickness growing ~30%+ from 11 to 14 km/s, so a single mission-class fraction is an approximation of exactly this curve; Mahzari documents why NASA itself freezes it per heritage. Registry **576 -> 578** sources (T2 +2); queue unchanged at 114.

### Round 162 - the institutional MER pair behind d21's opening-brief item 'mass estimating relationships for cargo carriers and return vehicles' (+2 T2 full_text_hosted)

d21's R75 brief asked, as its third bullet: 'Mass-estimating relationships for cargo carriers and return vehicles: structure and TPS mass as a fraction of cargo.' The NTRS search space answers it with two institutional sizing documents, both PUBLIC_USE_PERMITTED with zero in-file copyright -> hosted ntrs-public-use.

**kibbey_2015_rho_isp_stage_mass_estimating_jpc [T2; full_text_hosted]** - Kibbey (Jacobs ESSSA), 'Rho-Isp Revisited and Basic Stage Mass Estimating for Launch Vehicle Conceptual Sizing Studies', AIAA 51st Joint Propulsion Conference paper **2015-3791** (NTRS 20150016561); DOI Crossref-verified live this round. VENUE TRAP: the 'AIAA 2014-4021' printed on p13 of the PDF is a SELF-CITATION to Donahue & Klaus (SLS Capabilities for Beyond Earth Missions, JPC 2014) - ref 5 in its own reference list - not this paper's number. Content: decomposes a stage's inert mass into three fractions - engine+structure (thrust-dependent), oxidizer tank and fuel tank (volume- and load-dependent) - with the tank constants derived from an Atlas V core reference ('This results in f’i,ot,0 = 0.0180 and f’i,ft,0 = 0.0255'), then validated against Delta IV CBC: 'However, starting with Atlas V’s 0.93, the equation predicts a Delta IV CBC propellant mass fraction of 0.82, while its published mass fraction is actually 0.887' - the gap that motivates the next-order two-free-factor inert-mass model. This is the institutional method behind d21's `Expendable upper stage recurring cost` ($4,800/kg of stage dry mass) and `Propellant tank recurring cost` cells: it converts propellant properties into the very structure fractions those $/kg rates are quoted against.

**motiwala_mathias_mattenberger_2014_conceptual_lv_spacecraft_design_risk [T2; full_text_hosted]** - Motiwala, Mathias & Mattenberger (Stanford / NASA Ames), 'Conceptual Launch Vehicle and Spacecraft Design for Risk Assessment', **NASA/TM-2014-218366** June 2014 (NTRS 20150000182; no DOI - NTRS is the canonical record). The component-level MER sizing methodology: optimal staging first defines each stage's Isp and structural mass fraction, then ALL components (tanks, engines) are sized by their own MERs to determine 'the vehicle’s total expected inert mass', iterating on assumed structural fractions until design margin closes; the institutional range statement is verbatim: 'Typical structural mass fractions range from 0.038 to 0.45, based on historical data'. This brackets upstream's `return_structure_frac_of_payload = 0.15` - with the caveat that Motiwala's ratio is stage inert/propellant while upstream's dial is structure per kg of RETURNED PAYLOAD, so it bounds rather than pins (context/bound class).

No re-pin proposed: both are context/bound for cells whose values remain engineering estimates or heritage-bracketed. Key numbers in extracted_data/r162_stage_mer_key_numbers.csv (5 rows x 6 cols; every quoted span count==1 against the hosted PDFs, verified pre-write). Registry **580 -> 582** sources (T2 +2); queue unchanged at 115.

## R165 (2026-10-14) - 4 revision candidate(s) from sources already registered (registry unchanged)

A second cross-reference pass (economicspace config dials and price/production tables, spacecost launch prices, physical constants and propellant Isp, AsteroidCatalog PGM factors) over sources registered in earlier rounds (spacecost@0b716ad, economicspace@f7fe1c6, AsteroidCatalog@86cfc54), and a candidate opened wherever a registered source contradicts the cell, or backs a figure the upstream note leaves uncited or attributes to something else. Registry unchanged. Candidates from this domain's sources:

- **rc-134 (method, economicspace `modules/calc.py` MiningConfig.heat_shield_frac_of_payload (L856)).** Scale the heat-shield fraction with entry speed (and so with the asteroid's arrival v-infinity, which the model already computes per body) instead of a flat 15%: the registered sizing method puts required ablator thickness, and so shield mass, up super-linearly with entry speed. At minimum, say the 0.15 is for a lunar-return-class entry (~11 km/s) and is optimistic for faster returns.
- **rc-135 (method, spacecost `spacecost/delivery.py` DOWNLEG_TPS_FRAC (L400-403)).** Same as the economicspace candidate on heat_shield_frac_of_payload: a depot-to-Earth downleg enters at LEO, GEO or lunar-return speeds, which differ by several km/s, and the registered sizing method makes shield mass rise with entry speed; give the fraction an entry-speed basis per destination or a note stating the speed it assumes.
- **rc-137 (wording, economicspace `modules/calc.py` MiningConfig.return_structure_frac_of_payload (L203-227)).** Cite the registered figures: NASA OIG puts Cygnus upmass at 3,754 kg per mission (not 3,500), Dragon 2 at 2,507 kg returned plus 800 kg trunk, and Dream Chaser at 5,500 kg; and NASA's MER methodology gives historical structural mass fractions of 0.038 to 0.45. The Cygnus dry mass (~1,500 kg) has no registered source.
- **rc-139 (citation, spacecost `reference/operational_costs.csv` Mining payload recurring cost;Berthing adapter recurring cost).** Neither model states a $/kg bracket in anything the registry could read: the SSCM landing page refuses this machine (HTTP 403) and NICM is distributed only through NASA's ONCE portal; NICM is an INSTRUMENT cost model, not a model of structures or mechanisms. Mark the $100k-$1M/kg bracket as an estimate, or cite the document and table it comes from.
