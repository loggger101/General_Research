# Domain 30 — Volatiles, process chemicals & catalyst metals in space

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY` and `IN_SPACE_UTILITY_BY_DESTINATION`, the rows in `_COMMODITY_CLASS` classes `"propellant"` (water, ammonia), `"chemical"` (carbon, organics, carbon dioxide, carbonates, sulfur, phosphorus, oldhamite, merrillite, chlorapatite) and `"trace"` (the PGMs and their ores, gold, silver, gallium, germanium, rhenium, tungsten, molybdenum), and the comment that records why PGMs get no catalyst utility at the surface destinations: what each volatile, process chemical and trace metal is used for in space and how well it replaces the launched alternative.

Created in Round 161 (2026-10-13). Blocks are appended one per round, newest last.

## R161 - Domain opened with three NASA sources (2026-10-13)

These classes carry the table's highest utility (water 1.00) and lowest (every precious metal 0.00).

**Cells** (economicspace@8dc759f):

| cell | base (LEO, cislunar, mars_orbit) | geo | lunar_surface | mars_surface | upstream's stated basis |
|---|---|---|---|---|---|
| water | 1.00 | 0.80 | 0.60 | 0.25 | "propellant feedstock, radiation shielding, life support and coolant; electrolysis is the only processing step" |
| ammonia | 0.60 | 0.40 | 0.60 | 0.30 | nitrogen for a habitat "plus a resistojet propellant" |
| carbon dioxide | 0.30 | 0.05 | 0.30 | 0.02 | "the carbon feed for Sabatier methane" |
| carbon / organics | 0.40 / 0.20 | 0.05 / 0.05 | 0.40 / 0.20 | 0.02 / 0.05 | "composites, plastics, agriculture feedstock" |
| carbonates | 0.25 | 0.05 | 0.03 | 0.02 | "the CO2 source, and otherwise shielding rock" |
| sulfur / phosphorus | 0.10 / 0.10 | 0.05 / 0.05 | 0.10 / 0.10 | 0.05 / 0.10 | "process chemicals and fertiliser" |
| PGMs, Au, Ag, PGM ores, Ga, Ge, Re, W, Mo | 0.00 (default) | 0.00 | 0.00 | 0.00 | "nobody in orbit buys them for their own sake"; valued by shipping down |
| rejected alternative | PGMs 0.05 at the two surfaces | | | | "a crewed base runs fuel cells, electrolysers and Sabatier reactors and wants Pt/Pd/Ru catalysts", dropped because the pipeline cannot blend a kg-scale catalyst market with the terrestrial one |

**What a source has to supply:** each volatile's performance as propellant or consumable against the launched alternative; catalyst and process-chemical mass an ISRU plant or habitat consumes; in-space uses of the trace metals.

**Sources (NTRS, hosted):**

- `degroot_1997_electrolysis_propulsion_spacecraft_tm113157` (TM-113157 / AIAA 97-2948): water electrolysed and burned as GH2/GO2 has "performance measured at an Isp of over 350 s", 355 s on a 22-N thruster over 69,000 firings, projected above 380 s, "superior to earth storable chemical alternatives"; water stores at 1.0 g/cc; stoichiometric chambers may need "iridium-coated rhenium".
- `morren_1987_multipropellant_resistojet_space_station_tm100113` (TM-100113 / AIAA 87-2120): the station resistojet was baselined for drag make-up "while disposing of a variety of fluids expected to be present in excess quantities on board": hydrogen, helium, methane, steam, nitrogen, air, argon and CO2 at Isp 93-385 s; steam 184 s with a separate boiler, 159 s without.
- `franco_2019_sabatier_catalyst_mars_isru_ices2019_077` (ICES-2019-077): Sabatier for Mars ISRU uses "transition metal catalysts (such as ruthenium or nickel)": nickel vs 0.5% and 2% Ru on alumina, for a plant of 8.03 kg CH4/day (6978 kg over the campaign).

Also: `lewis_1992_asteroid_resources_sp509_vol3` (d29): C1 chondrites up to 20% bound water, 6% organics, 11% magnetite.

**Against the cells:** water 1.00 is supported as a drop-in for launched storables; CO2 and methane have a direct resistojet use besides the Sabatier feed (non-zero supported, size not); ammonia had no source yet; the catalyst use is real but percent-level Ru coating with Ni as substitute, supporting a kg-scale market (trace share 0.0005, d15) and the dropped 0.05; Ir/Re chambers are an in-space use of Earth-made parts. `extracted_data/r161_volatiles_chemicals_catalysts_key_numbers.csv`. No candidate.

**Boundary:** domains 3, 10 and 14 hold launched propellant performance and price; 5 ISRU and storage; 19 processing energy; 15 demand and class shares.

## R168 - Ammonia arcjet performance; ISS Sabatier catalyst record (2026-10-14)

Hosted:

- `deininger_et_al_1990_30kw_ammonia_arcjet_jpl_pub90_4` (JPL Pub 90-4, 1986-1989 programme): "Since the 30-kW ammonia arcjet is now known to produce less than 800 s specific impulse and 30-percent thrust efficiency, further development is necessary" (p41); earlier results were 20% high because "JPL mass flow measurements" were "20-percent low" (p37).
- `hardy_curran_1987_low_power_dc_arcjet_hydrogen_nitrogen_ammonia_mixtures_tm89876` (TM-89876, 23rd JPC): "typical performance of 450 sec specific impulse at 1 kW with hydrogen/nitrogen mixtures" (p25); ammonia mixtures ~10 s above hydrazine mixtures, every point above 400 sec with 40 to 80 sec spread (p9); a prior 1-kW thruster (920 W, 550 s) "had an expected lifetime of less than 2 hr with ammonia" (p3).
- `nallette_et_al_2013_sabatier_catalyst_poisoning_investigation` (abstract): the ISS Carbon Dioxide Reduction Assembly "has been operational since 2010" and "there is no provision to remove contaminants prior to entering the Sabatier catalyst bed".

Ammonia's propellant use is now institutional at both power classes; PGM catalysts fly in ISS ECLSS (Earth-made), supporting the rejected-alternative reasoning. The 1-kW resistojet records NTRS 19850057477 and 19860052336 have no files. `extracted_data/r168_ammonia_arcjet_sabatier_key_numbers.csv`. No candidate.

## R169 - Habitat nitrogen demand (2026-10-14)

`masangkay_sweterlitsch_frahlman_2026_supplying_nitrogen_moon_mars_ices2026_238` (ICES-2026-238, hosted): nitrogen "is primarily used to maintain cabin pressure ... and is lost nominally to the environment through leaks, airlock usage, and technology venting" (p1), so it scales with EVAs and duration, not crew. "N2 requirements provided/estimated range from around 9 kg to upwards of 4,600 kg" (p7); Table 4: transit 9-295 kg, lunar surface 19-3623 kg, Mars surface 119-4620 kg; Table 5: air save 119-729 kg vs none 1092-4620 kg. Non-compressed-gas options win above ~124 kg (p13); liquid N2 and liquid N2O with power recommended (p14). 119 kg corresponds to ~412,000,000 L of Martian atmosphere (210 K, 6 mbar, 3% N2). Mission totals, not per-crew rates; ammonia 0.60 unchanged. `extracted_data/r169_habitat_nitrogen_demand_key_numbers.csv`.

## R170 - PGM inventory of PEM fuel cells (2026-10-14)

Hosted:

- `murphy_hitchens_manko_1994_high_power_density_pem_fuel_cells_n9423359`: Pt-black loadings of 1, 2.5, 5 or 10 mg cm-2 (p3); "A platinum black loading of 5 mg per cm 2 was found to be optimum"; "the degree of platinum utilization was only 16.6% and the roughness factor of a typical electrode was 274".
- `srinivasan_et_al_1994_pemfc_space_electric_vehicle_dual_use_transfer_vol2`: "at current density of about 500 mA/cm2 the amount of platinum required per kilowatt is only 1.2 grams per kilowatt", ~10x less than state of the art (p3); ≤0.4 mg/cm² demonstrated, 0.1 mg/cm² with high utilisation; Pt alloys tested at 0.3 mg/cm².

So ~1.2 g/kW at low loading vs ~12 g/kW; inventories must count total loaded Pt (~83% inactive). Trace rows unchanged. `extracted_data/r170_pgmcatalyst_key_numbers.csv`.

## R171 - Sulfur poisoning of catalysts (2026-10-14)

Hosted:

- `abney_et_al_2026_sabatier_freon_cs2_cos_mitigation_ices2026_601` (ICES-2026-601): the ISS Sabatier ran from 2010 until October 2017, when operation stopped for performance degradation; teardown "confirmed contaminants had reduced catalyst activity by 70%", "sulfur and silicon were the most detrimental poisons" (from DMSO2 and volatile methyl siloxanes); Freon R-218 at 1500-4500 mg/m3 on ISS; CS2/COS newly identified, a getter would need replacing every 9.9-12.8 hrs (p4).
- `baumgartner_1974_sulfur_poisoning_hydrocarbon_oxidation_palladium_cr155192` (NASA-CR-155192; title page 1974): Pd oxidation of ethane and diethyl ketone "at the 0-30 ppm level in air"; poisoning at ~247 C by H2S, Freon 22 and Gentron 142-B; "Poisoning by Gentron 142-B was much more severe than by hydrogen sulfide."

Contamination, not just feed purity, drives catalyst life on orbit. `extracted_data/r171_sulfur_poisoning_key_numbers.csv`. No re-pin.

## R172 - Phosphorus demand closes the brief (2026-10-14)

Hosted:

- `wade_1989_nutritional_models_celss_linear_mathematical_modeling_cr4229` (NASA CR-4229): "Phosphorus requires total supplementation in Model Diets 4-6"; diversified diets still need "supplements of 785.0, 791.4, and 909.8 mg" per person-day (p60); phytomass was "in excess of 10 times the feasible level (which is about 1 kg/person/day)" (p48); P and vitamin A were the only constrained non-energy nutrients across Model Diets 4-9 (p50).
- `zeitlin_wheeler_lunn_2015_plant_biomass_leaching_nutrient_recovery_ksc_cif` (KSC CIF, 2015; not the same record as d19's `zeitlin_asteroid_excavation_project`): better recovery of Fe, Ca and P "would help further close the mass loop", target 60% recovery.

Some launched P remains needed even at full closure, supporting a small non-zero row. `extracted_data/r172_phosphorus_demand_key_numbers.csv`. The opening brief is closed.


### R218 - rc-184 opened: the Volatile cargo containment note cites a citation that does not exist upstream

The spacecost operational_costs.csv row Volatile cargo containment carries the sentence "Charged on WATER only, which is what the citation covers." while CITATIONS.md at 29a7ced has zero entries covering containment, sublimation, volatiles or depots (token sweep: contain/sublimat/olatile/shaded and Depot all return nothing; the single Water hit is the Kleinhenz & Paz lunar-ISRU title for a different claim). The storage_systems.csv twin Volatile cargo containment (water ice) likewise names no source in its note. The input is load-bearing, not decorative: economicspace consumes it live with model_volatile_containment default True and m_containment = c_frac * m_pay feeding three masses in the denominator, so every water-rich destination multiple rests on this 0.05 kg/kg fraction; their own verification worksheet ledger independently lists I70 c_seal marked needs backing stating that the notes of the row name no published source (consumed by steps S101 and S116). The proposal follows rc-182 shape: add a CITATIONS.md entry naming an institutional document, or reword as self-declared engineering estimate in house style; values untouched.

Registered neighbors recorded for the record, NOT cited as backing: nasa_tm_2011_long_term_cryogenic_storage_microgravity and plachta_2017_cryo_zbo_goals (both hosted) treat cryogenic propellant tanks with zero-boil-off hardware at 1 AU - institutional analogs of volatile storage loss in space, but neither addresses a passive sealed shaded water cargo hold; naming either upstream would need an explicit scope caveat.

Two seams closed negative earlier the same day (recorded so future rounds skip them): (1) AC reference/taxonomy_composition.csv class coverage matches mineral_phases tables exactly except the intentional Unknown row, and every composition row sums to its own declared fraction_sum with none exceeding 1; the low sums for carbonaceous classes are deliberate - README states verbatim The fractions do not sum to 1, and must not be made to (bold warning line), and separately that normalising an intended remainder away invents composition. (2) That contract is honored downstream: no code path in economicspace at 675f0cf divides by fraction_sum or renormalizes the four component columns; they are used raw as price multipliers.
