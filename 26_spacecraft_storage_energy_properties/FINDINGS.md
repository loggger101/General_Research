## R955 — Economicspace dark-time provenance scoped to Vesta (2026-11-19)

At Economicspace main b6c962c4f06dc5b625fee39044d8d1699ac564c9, `campaign/stage3/PROVENANCE.md` records the 0.50 dark fraction as scenario geometry and scopes Stubbs & Wang 2012 §5.1, printed p. 275, to Vesta's tropical sites, where the solar disk is typically seen about half the time (`stubbs_wang_2012_vesta_illumination_conditions`; rc-811). The paper's Vesta-specific 0.363–0.566 site range does not establish the generic [0.35, 0.55] band, which is identified as a scenario. The stored values remain 0.50 [0.35, 0.55].

Verdict: the comparator's body/site scope and the unsupported generic band are recorded. Extracted data: none new.

## R954 — Spacecost cryocooler range identified as a scenario (2026-11-19)

At Spacecost main 868f42890ac97ee40a50d79f7b33863046edb0ff, the cryocooler specific-mass point remains 5.0 kg/W and the [2.0, 15.0] band is labeled a scenario. Nugent et al. 2022 Table 3, PDF p. 3, reports flight-like acceptance points from 4.7 to 35.5 kg/W (`nugent_2022_rtb_cryocooler_test`; rc-812); those test points do not establish the generic band endpoints.

Verdict: the point and range are distinguished; neither value is changed. Extracted data: none new.
# Domain 26 — Spacecraft storage & energy-system physical properties

Backings: spacecost `reference/storage_systems.csv` — the propellant-storage cells (`Low-pressure liquid propellant tank`, `COPV burst performance factor`, `Multi-layer insulation (passive)`, `Zero-boil-off cryocooler (20 K)`, `Cryocooler specific mass (20 K)`, `Vapour-cooled shield`), the energy-storage cells (`Li-ion battery`, `Regenerative fuel cell`, `Flywheel energy storage`, `RTG specific power`, `Fission surface power (Kilopower class)`) and the depot cell (`Orbital propellant depot (cryogenic)`). Read from spacecost @77c6e11.

Created in Round 104 (2026-10-02). Blocks are appended one per round, newest last. The cargo-containment cells (`Bulk ore restraint` 0.15 kg/kg, `Volatile cargo containment` 0.05 kg/kg) have no institutional source and stay upstream judgement rows.

## R104 - Domain opened; eight NTRS reports hosted (2026-10-02)

All eight are NTRS public-use, hosted, and context-only (read, no numbers extracted yet).

| cell | unit | value (low-high) | status/TRL | backed by |
|---|---|---|---|---|
| COPV burst performance factor | J/kg (PV/W) | 392,000 (250,000-600,000) | operational / 9 | nasa_tm_2026_copv_stress_rupture_mechanics_carbon_fiber; ntrs_2010_copv_stress_rupture_testing; ntrs_2011_copv_flight_rationale_shuttle_program |
| Fission surface power (Kilopower class) | W-elec/kg | 6.7 (0.7-15) | development / 5 | ntrs_2020_kilopower_krusty_fission_power_experiment_missions; ntrs_2020_krusty_reactor_design |
| RTG specific power | W-elec/kg | 5.0 (2.4-5.5) | operational / 9 | nasa_tm_2025_rtg_power_performance_histories |
| Multi-layer insulation (passive) | kg/m² tank surface | 1.2 (0.5-3.0) | operational / 9 | nasa_tm_2011_long_term_cryogenic_storage_microgravity; ntrs_2014_cryogenic_boiloff_reduction_system_testing |
| Orbital propellant depot (cryogenic) | % stored mass lost/day | 0.03 (0.01-0.1) | development / 5 | nasa_tm_2011_long_term_cryogenic_storage_microgravity; ntrs_2014_cryogenic_boiloff_reduction_system_testing |

Also relevant, registered elsewhere: `nugent_2022_rtb_cryocooler_test` and `plachta_2017_cryo_zbo_goals` (d05) for the cryocooler rows; `nasa_std_5019_fracture_control_spaceflight_hardware` (d03, §7.2.2 and ANSI/AIAA S-081) for the COPV factor.

## R105 - The remaining storage_systems.csv cells (2026-10-03)

Eight more NTRS reports, hosted, context-only.

| cell | unit | value (low-high) | status/TRL | backed by |
|---|---|---|---|---|
| Li-ion battery (system level) | Wh/kg | 130 (90-200) | operational / 9 | ntrs_2016_orion_small_cell_battery_design_support |
| Flywheel energy storage | Wh/kg | 100 (40-180) | development / 6 | ntrs_2006_g2_flywheel_module_design; ntrs_2002_energy_storage_flywheels_on_spacecraft |
| Regenerative fuel cell | Wh/kg | 400 (250-700) | development / 5 | ntrs_2020_analysis_100w_regenerative_fuel_cell_demonstration; nasa_cr_1984_regenerative_hydrogen_oxygen_fuel_cell_electrolyzer |
| Sintered / consolidated cargo | Wh/kg ore consolidated | 350 (150-800) | concept / 3 | ntrs_2023_vacuum_sintering_highland_simulant; ntrs_2020_microwave_sintering_lunar_landing_pads |
| Dust mitigation and seals | kg per kg mining hardware | 0.08 (0.03-0.2) | development / 5 | nasa_tm_2005_rev1_effects_lunar_dust_eva_systems_apollo |

The Orion battery deck has only a partial OCR text layer; its body figures are not yet machine-readable.

## R150 - Dust-mitigation cell: three modern NTRS papers (2026-10-10)

All hosted (NTRS public use, no in-file copyright):

- **mcbrayan_francis_sobey_2025_viper_mobility_dust_mitigation** (ICES-2025-147): VIPER's seal matrix (labyrinth, Nomex felt, spring-energised PTFE, grease damming); face-seal compression 20% per MER/MSL heritage vs Tri-ATHLETE's 5-10%.
- **lee_brown_2023_gateway_lunar_dust_mitigation_overview**: Gateway's GOLDMAP contamination framework and two-pronged mitigation strategy (year from the file stamp).
- **jones_et_al_2026_artemis_suit_dust_exposed_fabrics** (ICES-2026-164): end-of-life soiling test for suit fabrics, rotary tumbler with simulant and ceramic media (453.5 g each, eight hours at 80 rpm).

`extracted_data/r150_dust_mitigation_key_numbers.csv`. None gives a mass-per-hardware figure, so the 0.08 kg/kg judgement stands.

## R163 - The Kilopower note overstates KRUSTY (rc-088; 2026-10-14)

The 'Fission surface power (Kilopower class)' note (spacecost@0b716ad) says "KRUSTY demonstrated a 1 kWe uranium-molybdenum reactor with Stirling conversion in 2018". Both R104 papers describe a ground test of a 5 kW(thermal) prototype for a 1 kWe-class system: Poston et al. p5, "The electrical capacity/efficiency goal was partially met via two Stirling converters, while using dummy heat rejection for the remainder of the system"; McClure et al. p2, "a ground technology demonstrator of a 1-kW(electric)–class fission power system". Fuel specified U-8Mo, delivered U-7.65Mo. Neither gives the ~1,500 kg 10 kWe flight-unit mass the note cites, so the 6.7 W/kg value is untested.

## R164 - Candidates (2026-10-14)

rc-109 (regenerative fuel cell round trip 47.4%), rc-110 (four storage figures not in the R104/R105 reports), rc-115 (NEP row repeats the KRUSTY overstatement). Texts and evidence in `revision_candidates_closed.csv`.

## R238 - Six storage and power candidates applied upstream; two author slips (2026-10-21)

spacecost 0.12.5 (PR #28, tag v0.12.5, main `b5eb32a`) applied rc-088, rc-089, rc-108, rc-109, rc-110 and rc-115, notes only, no value moved; each row's evidence says what landed. Two registry slips found while re-reading the title pages: `ntrs_2006_g2_flywheel_module_design` is by Ralph H. **Jansen** (University of Toledo) and Timothy P. Dever, NASA/CR-2006-213862 / AIAA-2004-5603, not "Jensen"; `ntrs_2020_analysis_100w_regenerative_fuel_cell_demonstration` (NASA/TM-20205000357) is by Bennett, Smith **and Jakupca**, titled "Analysis of 100-W Regenerative Fuel Cell Demonstration" (no "a"). Both rows corrected; ids unchanged.

## R350 - Body density does not bound the volume of separated water cargo (2026-11-03)

`economicspace_return_cargo_volume_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0, spacecost
860bef9902aa67fec705875cd52fdb8e6def159f and spacevalue
873b91c1ce51fd2f5fe9ead63ce171d755e73011. calc.py L6542-6552 sets a
quarter-fairing allowance using the parent body's density; L6606 reports
payload divided by that same density before the final cargo mix at
L6815-6826. MODEL.md L1377-1379 acknowledges the proxy and concludes
"the volume constraint is conservative". The mineral catalog separately
sets water density to 1.0 g/cm3 (catalog.py L1595-1598).

Twenty-one constructed fixtures run original, repeat, a scoped cargo-volume
guard and its repeat: 84 complete evaluate_asteroid consumers, retaining
original numerical function bodies, reference-only Stage 2 prices, real
source vehicles/kerolox and geometric transfer options. The guard feeds an
additional payload cap through the original kernel and lets the original
objective reselect ratios/architectures. Twelve selected native books exceed
the unchanged allowance on water alone; twelve guarded books close it.
Nine selected-book controls are exact, including raw, equal/lower body
density, smaller vehicle, longer transfer, low water, metal, pure ice and a
zero-mass refusal. Coarse/detailed phases and disabled boil-off/eclipse
sensitivities retain the finding. No packing assumption for the other
material is needed to establish the twelve water-only excesses.

The main fixture is 20% water/80% silicates, body density 1.8 g/cm3,
a=1.01 AU, e=i=0 and 10 h rotation, with a declared 3,000 kg rig sensitivity.
SLS Block 1 has 95,000 kg LEO capacity and a 216 m3 fairing, hence a 54 m3
return allowance. Native geometric burns are 3298.408532/617.064275 m/s.
The selected book carries 57,746.596841 kg water, requiring 57.746597 m3
at its adopted density, while reporting 32.081443 m3 and volume_fits=True.
The guard selects 54,000 kg water at just below 54 m3. Original-kernel
recomputation lowers launch 95,000 to 89,157.614501 kg, feed 320,814.426897
to 300,000 kg and cost 6,047,419,401.070768 to 5,789,776,426.154996 USD.
At the default 2,000 kg rig, a=1.001 AU Falcon Heavy case, water alone is
39.447 m3 against 39.25 m3 allowed, before its accompanying silicate.

Verdict: `rc-285`, use explicit returned-material/state/packing assumptions
in joint cargo allocation and sizing, keep the volume report consistent,
and qualify the conservative-direction claim. Body density and the 0.25
allowance are not re-pinned. The diagnostic is a restricted feasible repair,
not a global two-resource knapsack solution. All examples remain
unprofitable; no observed-trajectory, population-incidence or ranking claim
is made. Both repeated pairs match native types/values/float.hex digests.
All returned books pass current source mass/resource/throughput/time checks
to their tolerance; guarded books also pass the added material-volume check.
Twenty-four blobs, including all 22 imported local modules, match fresh
pinned metadata and all four live main comparisons are identical.
`extracted_data/r350_return_cargo_volume.csv`.

## R353 - Earth-loaded liquid can exceed the entire launch payload envelope (2026-11-03)

`economicspace_outbound_propellant_volume_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0 and spacecost
860bef9902aa67fec705875cd52fdb8e6def159f. calc.py L6530-6531 shares the
fairing with "mission hardware and propellant tanks", but L6551-6552
only caps returned cargo at a quarter of the envelope. Propellant density
enters tank mass (L3629-3645), and settled Earth-loaded fuel is computed at
L6646-6674 without a launch-volume gate. The source blend adds separate
fuel and oxidiser volumes (propellants.py L398-424). All comparisons retain
the source densities, tankage, fairing and quarter-return allowance.

Twenty-three constructed raw single-phase fixtures run original, repeat,
liquid-only guard and repeat: 92 complete evaluate_asteroid consumers, using
original numerical bodies, reference-only Stage 2, actual source
vehicle/propellant rows and geometric transfers. N=1; refinery, ISRU and
launch windows are off. The guard reduces only the existing payload cap
for an offending candidate through 48 original-kernel bracket steps, then
lets the original objective reselect architectures. It grants the entire
usable fairing to Earth-loaded liquids alone, assigning zero volume to tank
walls, ullage, the empty return capsule and all other hardware. This is an
optimistic necessary condition, not a complete packing solution.

The main synthetic 1-km nickel-iron body has bulk density 3 g/cm3,
a=1.2 AU, e=i=0, 10 h spin and the default 2,000 kg rig. The source SLS
Block 1/hydrolox book flies 61,110.66841672852 kg outbound propellant and
19,997.212052254883 kg Earth-loaded return propellant. At the adopted
0.36114420743389963 kg/L, liquid alone needs 224.58585462381703 m3
against the 216 m3 envelope. The 8.585854623817028 m3 excess remains even
before any hardware occupies space. Returned cargo reports only
7.785081767826991 m3 against 54 m3, and the 95,000 kg launch limit passes.
The source vehicle is government_only and its cargo fairing is explicitly
an unflown reference configuration; this does not describe a flown SLS
cargo mission or a presently bookable commercial launcher.

The restricted diagnostic selects 22,447.925536475905 kg cargo instead of
23,355.245303480973 kg and reduces liquid from 81,107.8804689834 to
78,007.14880564413 kg, just below 216 m3. Original-kernel recomputation
reduces launch to 91,461.582494966 kg and cost from
5,053,885,877.562077 to 4,922,996,444.801831 USD. This only closes the
liquid lower bound; a complete stack needs further volume provision.
Fourteen native selected books fail that lower bound and fourteen
diagnostics close it. Distance, rig, body-density and mineral sensitivities,
disabled eclipse and three disabled-boil-off cases retain the finding.
Nine full-book controls are exact, including closer bodies, denser
propellants, a smaller vehicle, body-limited cargo and two original refusals.
Both repeated pairs match native types/values/float.hex fingerprints;
50-digit Decimal volume checks agree. All returned books pass the source
mass/resource/throughput/time/return-volume checks exercised by the harness
and remain unprofitable.

Verdict: `rc-288`, close the outgoing envelope using Earth-loaded liquid,
tanks and other stowed hardware, or explicitly model an alternative ascent/
orbital-assembly architecture with its capacity and cost basis. A scalar
volume condition is necessary, not sufficient for geometry. No actual-body
incidence, catalogue ranking, global packing optimum or full engineering
feasibility is established. Twenty-four runtime/method blobs match pinned
metadata; all four live main comparisons are identical.
`extracted_data/r353_outbound_propellant_volume.csv` contains full inputs,
books, brackets, volume observers and the reproduction harness.


## R410 - Cryogenic MLI areal-density comparator (2026-11-09)

NASA KSC author Wesley Johnson reports in Table 3 (PDF p. 6) that the 60-layer Ball MLI test blanket A141 had an areal density of 2.98 kg/m²; the 40-layer A139 measured 2.41 kg/m² and the 20-layer Quest IMLI A142 measured 1.00 kg/m². The paper states that A139’s seam construction made it slightly heavier, and describes mass over the calorimeter surface. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/storage_systems.csv` uses 1.2 kg/m² for “Multi-layer insulation (passive)” and describes a 60-layer aluminised-Mylar blanket. The 60-layer comparison is about 2.48 times the stored value. The test articles do not establish a like-for-like flight-tank areal mass because their blanket construction and seam configuration may differ. **rc-320 remains open** for configuration and mass-boundary reconciliation. Extracted: `extracted_data/r410_johnson_mli_areal_density.csv`.


## R463 — Current cargo and launch-volume options

At economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, `CalcConfig.model_cargo_volume` (line 725) and `model_launch_liquid_volume` (line 730) both default to `False`; the module-level consumer constructs `CONFIG = CalcConfig()` without an override (line 1468). For `rc-285`, when enabled and phase data are present, the evaluator derives returned cargo volume from each selected phase's `phase_density_kg_per_L` after mix selection and refits a mix whose unpacked phase-volume sum exceeds the 0.25-fairing hold (lines 7390-7402; phase densities are loaded at 9054-9055). The initial mass cap still uses parent-body density (7051-7058), the check is default-off, and the source comment describes the phase volumes as unpacked; packing/state and a fully joint material-volume solve remain unrepresented. For `rc-288`, the opt-in branch sums outbound plus Earth-loaded return propellant liquid (excluding ISRU-made return fuel), compares that to the full fairing volume times the single propellant density, and refits payload when needed (lines 7322-7341). It does not include tank walls, ullage, return vessel, other stowed hardware, or geometric packing, and is also default-off. Both candidates remain open with their constraints distinguished. Extracted: `extracted_data/r463_current_cargo_and_launch_volume_flags.csv`.


## R507 - Shuttle water-tank mass comparator for volatile containment (2026-11-09)

Harry W. Jones (NASA Ames) estimates 0.2 kg of tank per kg of water and cites a Shuttle water tank weighing 21.2 kg for 103 kg of water (ICES-2017-87, §IV.C, PDF p. 4). The cited Shuttle figures imply 0.206 kg tank/kg water. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/operational_costs.csv` assigns “Volatile cargo containment” 0.05 kg/kg, with a 0.03–0.12 range; its note defines this as incremental sealed/shaded-hold mass beyond the ore-restraint fraction. The Shuttle value is for a potable-water tank, not the incremental passive shading and sealing structure, so it benchmarks scale without validating the row's fraction. **rc-373 remains open** for a source or derived mass budget with the same boundary. Extracted: `extracted_data/r507_jones_water_tank_mass_comparator.csv`.


## R545 — ISS eclipse duration as the LEO power-system baseline (2026-11-10)

`kascak_2001_iss_eclipse_nasa_tm_2001_211138` — Kascak et al.’s NASA technical memorandum says the ISS solar array cannot generate during the “35 minute eclipse period of the 92 minute ISS Earth orbit” (NASA/TM-2001-211138, p. 1). Converting 35 minutes gives 0.5833 hours, consistent with the 0.58 h baseline stored by spacecost. The memorandum supports an ISS eclipse comparator; it does not establish that 0.58 h is a standard design duration for conventional deep-space PV trains. Open **rc-410** to add the citation and qualify that broader wording while retaining the current value. Extracted: `extracted_data/r545_iss_eclipse_baseline.csv`.


## R546 — Chemical-battery dark-period cap comparator (2026-11-10)

Fincannon’s NASA technical memorandum reports “73 to 117 hours required for energy storage (depending on power system type)” at the worst-case lunar day for the Shackleton rim site (NASA/TM-2007-215025, abstract, printed p. 1 / PDF p. 4); a linked-site case reports 68 hours. Its introduction says lunar surface systems use storage “either batteries or fuel cell type systems” (printed p. 2 / PDF p. 5), so these figures do not establish battery-only endurance. At economicspace main `db863923f7793676e9a78583b97462ddd614f29e`, `CalcConfig.max_dark_period_h` is 72.0 h and the comment describes that as the outside edge for a chemically powered battery. The lunar analysis is a system-dependent storage comparator, not an asteroid-mining battery limit; no numeric replacement is inferred. **rc-411** records the uncited scope claim for review. Extracted: `extracted_data/r546_fincannon_lunar_storage_hours.csv`.


## R548 — RFC system-level specific-energy comparator (2026-11-10)

Jeffrey Csank’s NASA presentation reports that RFC systems range from approximately 100–600 Wh/kg depending on power level and duration (slide 12). Its system-level comparison table lists 400 Wh/kg and 300 kg for a 1 kW, 120-hour lunar-polar RFC case; the 1 kW lunar-equatorial case is 550 Wh/kg at 350 hours, while the Mars mid-latitude case is 200 Wh/kg at 13 hours. The table therefore supports 400 Wh/kg as a specific design comparator and shows mission dependence; it does not establish a generic asteroid RFC value or the full [250,700] range. At spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9, `reference/storage_systems.csv` labels 400 Wh/kg an estimate with no source, and `reference/operational_costs.csv` repeats it as the RFC comparator. **rc-414** records the citation and applicability review. Extracted: `extracted_data/r548_csank_rfc_specific_energy.csv`.


## R550 — G2 flywheel module specific-energy comparator (2026-11-10)

`ntrs_2006_g2_flywheel_module_design` — NASA/CR-2006-213862 reports 525 Wh usable energy and 218 lb module mass (printed p. 2, Table 1; confirmed in the summary on printed p. 12), yielding 5.31 Wh/kg at the full-module boundary. Its rotor table gives 50 lb (printed p. 3, Table 2), yielding 23.1 Wh/kg if only rotor mass is counted. The report says the module was for laboratory use and that weight was not a significant factor; these values are scale comparators, not like-for-like replacements for an optimized spacecraft or asteroid system. The spacecost `Flywheel energy storage` row estimates 100 Wh/kg with a [40,180] range and says the value has no source. Open **rc-416** to review the value, range, and mass boundary. Extracted: `extracted_data/r550_g2_flywheel_specific_energy.csv`.


## R551 — NASA cryogenic COPV burst performance-factor comparator (2026-11-10)

`ray_2008_cryogenic_copv_development_tests` — NASA’s test article table specifies a “minimum burst pressure” of 1.5×MOP (printed p. 4), and Tables 2–3 report a “Performance Efficiency Rating” of burst P_b V/W (printed pp. 6–7). Rechecking the six cryogenic tests reproduces each tabulated value from burst pressure, volume, and mass; conversion gives 326.5–416.6 kJ/kg. Spacecost’s COPV factor is 392 kJ/kg, within this interval, but the tests cover two liner materials in 1.8 ft³ cryogenic helium-pressurization vessels, not a generic supercritical-gas tank. The NASA data directly address the same parameter and replace the upstream note’s claim that no registered source gives PV/W; they do not establish the generic value or [250,600] range. Open **rc-417** for citation and applicability review. Extracted: `extracted_data/r551_nasa_copv_pressure_volume_weight_performance.csv`.
## R562 — storage duration comparator and scenario scope applied (2026-11-10)

At economicspace@e2ad48767b0e81489031b724417b1a03e6dfc1fb, the 72 h dark-period note cites Fincannon’s lunar storage requirements and describes 72 h as a scenario cap rather than a battery limit (rc-411). Citation and scope request applied; value unchanged.
## R564 — Storage and tank comparators now carry scope limits (2026-11-10)

At spacecost@d3e594fe0968eeaee4f2c02dd2c76334eab8bb2c, Jones’s Shuttle water-tank mass is identified as pressurized-tank mass, not passive shade/seal mass (rc-373); Kascak et al.’s 35-minute eclipse is limited to a 92-minute ISS orbit (rc-410); NASA’s 400 Wh/kg RFC result is scoped to a 1 kW, 120 h lunar-polar design rather than a general system value (rc-414); and Ray’s six cryogenic COPV tests are distinguished from a generic vessel (rc-417). The storage and containment estimates remain unchanged.


## R626 — Vapor-cooled shield performance and maturity basis (2026-11-11)

- **spacecost_vapour_cooled_shield_row_current_2026**: Spacecost’s reference row stores 0.40 [0.25,0.60] as the “fraction of passive boil-off removed,” and marks it operational, TRL 8; the note names no evidence or conditions. **johnson_et_al_2021_shiiver_vapor_cooling_tp**: NASA’s SHIIVER report describes a 4-m tank using boil-off vapor to intercept heat on a structural skirt. Its NTRS abstract reports that at 50% fill vapor cooling reduced boil-off by less than 3% without dome MLI and left it essentially unchanged with MLI (record lines 16–20); Table 46 (printed p. 175) reports separate fill-level and test-series reductions, including 14% at 80% fill in one baseline comparison and 33% at 80% in a preacoustic comparison. **johnson_stephens_2018_cfm_technology_roadmaps**: NASA’s 2018 technology roadmap lists vapor cooling at TRL 5 with a ground-test path to TRL 6 (p. 5). These sources show the result depends on system boundary and conditions; neither establishes the row’s generic passive whole-tank fraction or current TRL 8. Verdict: request the matched performance basis and maturity citation; no replacement inferred. **rc-489**. Extracted: `extracted_data/r626_vapor_cooled_shield_performance_scope.csv`.


## R627 - Cryogenic depot boil-off rate scope (2026-11-11)

- **spacecost_hydrolox_depot_boiloff_row_current_2026**: The Hydrolox propellant row stores 0.05%/day; the source-code comment gives a long-duration range of 0.03-0.1%/day but names no evidence or conditions. The reference-only orbital cryogenic depot row stores 0.03 [0.01,0.10]%/day, also with no tank, fuel, orbit or thermal configuration. **honour_kwas_oneil_kutter_2012_long_duration_cryo_depot_thermal**: A NASA conceptual Centaur-based LEO depot study uses passive thermal control, shields and ten MLI layers; its integrated thermal model reports total boil-off below 0.05%/day (printed pp. 3, 12). **perrin_casler_2016_fuel_depot_architecture_study**: A separate NASA depot model assumes 60 MLI layers and gives 0.5-1.0%/month for LO2 and 2.5-5.0%/month for LH2; Table 11 varies kg/hr across LEO, GEO, L1 and tank configurations (printed p. 15). These are model-specific results and do not support a universal rate. Verdict: request the matched configuration and denominator; retain current values as explicit scenarios unless a like-for-like source establishes them. No replacement inferred. **rc-490**. Extracted: `extracted_data/r627_cryogenic_depot_boiloff_scope.csv`.

## R629 - Sintered-cargo energy estimate lacks a measured basis (2026-11-11)

- **spacecost_sintered_consolidated_cargo_row_current_2026**: Spacecost `storage.py` stores 350 Wh/kg of ore consolidated with a range of 150-800 Wh/kg; the row names no source, calculation or uncertainty basis. The `tables.py` loader states `storage_systems.csv` is reference output and Stage 4 does not load it. **ntrs_2023_vacuum_sintering_highland_simulant**: NASA's vacuum-sintering presentation describes about 100 g samples and a 0.003 Torr furnace (slide 6); its preliminary conclusions compare lower and higher heat input qualitatively (slide 15), without reporting energy per mass. **ntrs_2020_microwave_sintering_lunar_landing_pads**: NASA identifies determining an optimized mass-sintered-per-hour process from -200 C to sintering temperature as work to be done (PDF p. 7); it gives no specific energy. The sources support lunar-simulant sintering as process context, not the row's numeric value or range, and neither addresses asteroid feedstock or billet product boundaries. Verdict: request a derivation or like-for-like energy evidence and define the ore/product and system energy boundary; retain the figures only as explicit scenario assumptions pending that basis. No numeric replacement inferred. **rc-492**. Extracted: `extracted_data/r629_sintered_cargo_energy_basis.csv`.

## R717 — Low-pressure liquid tankage baseline and verification input (2026-11-13)

At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `spacecost/propellants.py` lines 101-124 describes `_TANK_BASE_KG_PER_L=0.025` as selected from three flight articles: Shuttle ET 0.0129, Falcon 9 Stage 2 about 0.033 and Centaur III about 0.035 kg/L. The code gives no source record or exact Falcon/Centaur configuration. `reference/storage_systems.csv` row 2 stores 0.025 [0.013, 0.035] kg/L; it says the latter two article masses include thrust structure and avionics mounts.

**nasa_sp_2009_4012_external_tank_characteristics**: NASA's Table 2-86 calls 26,535 kg the "inert weight of super lightweight tank" (printed pp. 165-166) and separately lists LOX and LH2 tank volumes of 553,963 L and 1,515,461 L. Their 2,069,424 L sum gives 0.01282 kg/L, about 0.61% below the code's 0.0129 ratio using 2,058,000 L. This closely reproduces the Shuttle anchor's scale but leaves the code denominator basis unexplained; it does not demonstrate an error in the 0.025 base.

At economicspace main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, `campaign/verification_sheet.py` lines 2404-2417 derives `tank_frac` as `tank_kg_per_L / density_kg_per_L` from the frozen `campaign/stage3/spacecost-0.5.0/propellants.csv` row, while its citation helper names only `storage_class` for that value. Verdict: identify the source and exact configuration for each article, define numerator and propellant-volume boundaries, explain selection of the base and range, and propagate that provenance to the worksheet. Retain current values pending a matched basis; no numeric replacement inferred. **rc-585**. Extracted: `extracted_data/r717_low_pressure_tankage_basis.csv`.

## R718 — Storage-class tank multipliers lack row-level backing (2026-11-13)

At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `spacecost/propellants.py` lines 373-401 sets the non-base, non-COPV multipliers to 0.90 for benign liquids, 1.15 for mild cryogens, 1.50 for deep cryogens, 0.45 for sublimating solids and 5.00 for solid motors. The comments derive illustrative propellant fractions or give qualitative rationales, but do not name source records/configurations for water, LOX, LH2/Centaur or iodine. `CITATIONS.md` section 2 lists Shuttle ET, Falcon 9 second stage and Centaur III as the base flight anchors, while section 8 points to the `_TANK_BASE_KG_PER_L` comment block; it does not identify a source for each class factor.

**spacecost_propellant_tankage_rows_current_2026**: representative generated rows carry 0.0225 kg/L for water, 0.0273256 for kerolox, 0.0351261 for hydrolox, 0.01125 for iodine and 0.125 for APCP. Their notes discuss other hardware or engine evidence but do not attribute the tank coefficients. **ng_propulsion_products_catalog_2016** reports “Total inert = 274.2” and “Total inert = 289.6” lbm for the short- and long-nozzle Star 48B variants (pp. 102-103); with the catalog’s 4,431.2 lbm propellant load, the ratios are 6.19% and 6.54%. This supports the solid-motor comparator only. rc-179 applied the Northrop citation to economicspace `MODEL.md`; the Spacecost APCP row still states the 6.4% comparison without identifying the catalog.

At economicspace main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, `campaign/verification_sheet.py` lines 2404-2417 derives the tank fraction from the exported row and its citation helper names only `storage_class`. Verdict: identify each non-base class anchor and its mass/volume boundary, or label the factor as an explicit engineering scenario; propagate that source or label into the exported rows consumed by the worksheet. Retain current factors pending review; no numeric replacement inferred. This is distinct from **rc-585**, which tracks the 0.025 kg/L base, and **rc-179**, which corrected economicspace documentation. **rc-586**. Extracted: `extracted_data/r718_storage_class_tank_multiplier_basis.csv`.

## R760 — Surface power-storage worksheet citation gaps (2026-11-15)

The current economicspace verification-sheet check flags I61=0.50 [0.35, 0.55], I62=0.90 [0.80, 0.95], I63=104 Wh/kg [70, 160], and I64=0.58 h [0, 1.2] NEED BACKING. The sheet reads the frozen Module 3 rows in `campaign/stage3/spacecost-0.5.0/operational_costs.csv`.

The current Spacecost rows contain the source notes added under applied rc-342, rc-410, rc-413 and rc-414. `stubbs_wang_2012_vesta_illumination_conditions` reports the solar disk “typically seen about half the time in the tropics” on Vesta (p. 275); the row calls 0.50 a scenario and says no source sets the asteroid range. `schmitz_2023_rps_vs_solar_array_comparison` is cited for NASA Li-ion charge/discharge efficiency (Table 3). `bennett_baldwin_2010_drats_liion_battery_pack_specific_energy` supplies a protected D-RATS pack comparator (Table 5), which the current row labels an engineering analogy rather than spacecraft-battery evidence. `kascak_2001_iss_eclipse_nasa_tm_2001_211138` supplies the 0.58 h ISS eclipse comparator (p. 1); the current note says no source establishes that duration for deep-space PV trains. These source and scope notes are absent from the frozen rows used by the worksheet.

Open `rc-627` for the worksheet citation path and scope; no model value or range is changed. Extracted: `extracted_data/r760_power_storage_verification_sheet_citation_gap.csv`.


## R775 - Frozen volatile-containment worksheet attribution (2026-11-15)

`economicspace_volatile_containment_verification_sheet_code_current_2026`: the current 2018 DT cislunar worksheet flags I70=0.05 kg/kg NEED BACKING. `economicspace_volatile_containment_stage3_frozen_row_current_2026`: the frozen Stage 3 row says "Charged on WATER only, which is what the citation covers" but names no citation.

`spacecost_volatile_cargo_containment_row_current_2026`: the current Spacecost row labels 0.05 [0.03, 0.12] kg/kg an engineering estimate and says no published source gives the containment fraction or the stability of a passive sealed, shaded water hold over a multi-year cruise. `jones_2017_resupply_life_support_water_tank_mass` p. 4 reports a Shuttle potable-water tank at 21.2 kg for 103 kg of water; it is a pressurized-tank comparator, not the incremental passive-hold fraction. `nasa_tm_2011_long_term_cryogenic_storage_microgravity` and `plachta_2017_cryo_zbo_goals` concern cryogenic propellant tanks with zero-boil-off hardware. Applied rc-184 and rc-373 changed Spacecost notes, not the frozen economicspace row or worksheet input.

Verdict: carry the estimate status and comparator limits into I70 and remove the frozen row's unsupported citation claim. Preserve 0.05 [0.03, 0.12]; no numeric replacement inferred. **rc-645**. Extracted: `extracted_data/r775_volatile_cargo_containment_worksheet_gap.csv`.

## R824 — Current dark-period worksheet input recheck (2026-11-17)

- **economicspace_power_storage_verification_sheet_code_current_2026**: the current 2026-11-16 best-case worksheet maps dark_0=0.58 h to I69 and marks it NEED BACKING, with the generic reason that the row notes name no source.
- **spacecost_power_storage_rows_current_2026**: the current Spacecost row notes cite Kascak et al. (NASA/TM-2001-211138, p. 1) for a 35-minute eclipse in a 92-minute ISS orbit, then state that no source shows deep-space trains are specified against that duration. This supports the ISS comparator, not a deep-space 1-AU baseline.
- **Verdict**: extend rc-627 to current I69. Preserve the 0.58 h comparator and distinguish its unsupported deep-space baseline use; no numeric replacement inferred.
- Extracted: extracted_data/r824_dark_period_live_sheet_i69.csv.

## R825 — Current worksheet input numbers for storage and containment (2026-11-17)

The current sheet's I61=20,000 m/s is the outbound delta-v ceiling, not the frozen power-storage I61=0.50 geometry factor. In the live sheet, `dark_0` is I69=0.58 h; frozen Stage 3 storage input I64 is the earlier 0.58 h row. Current I70=10.222 h is the rotation-period fallback, while frozen Stage 3 I70 is volatile cargo containment at 0.05 kg/kg. **rc-627** remains scoped to frozen I61-I64 plus current I69; **rc-645** remains scoped to the frozen containment row. Extracted: `extracted_data/r825_live_sheet_input_id_collisions.csv`.


## R945 — Current Economicspace dark-fraction row and sheet (2026-11-18)

At Economicspace main `e477b00ffa7810a6f2daad76290d428eee8b70b3`, `campaign/stage3/operational_costs.csv` row 35 (pipeline 1.15.0) stores `Eclipse / night-side dark fraction` at 0.50 [0.35, 0.55]. Its note explains rotating-body geometry and site variation but names no source. The supplied `verification_sheet.pdf` p. 21 maps the row to current I66 and marks it NEED BACKING. It displays Stubbs & Wang’s Vesta comparator: “typically seen about half the time in the tropics” (§5.1, printed p. 275), calls 0.50 scenario geometry, says no source sets the generic range, and points to rc-413. The paper’s 0.363–0.566 range is Vesta-specific and does not establish a generic asteroid-site band.

Verdict: open **rc-811** for the current 1.15.0 Stage 3 row and I66 citation scope. Cite the comparator only for its Vesta tropical scope; identify [0.35, 0.55] as a model scenario unless matched evidence supports it. Preserve the values; no numeric replacement inferred. This is distinct from applied rc-413 (Spacecost current rows) and open rc-627 (Economicspace frozen 0.5.0 I61-I64 plus current I69). Extracted: `extracted_data/r945_economicspace_dark_fraction_current_sheet_scope.csv`.


## R946 — Spacecost cryocooler specific-mass band (2026-11-18)

At Spacecost main `ef0120748780a519187836c655d877e3daee1a3a`, `reference/storage_systems.csv` physical lines 9-10 store 5.0 kg/W [2.0, 15.0] at 20 K, development TRL 5. The row note cites Nugent, Grotenrath & Johnson, NTRS 20220009350, Table 1, for a 5.5 kg/W flight-like projection and 4.4 kg/W project goal; it says 5.0 sits between test and goal but gives no endpoint basis. Table 1 lists “18.7”, “5.5” and “4.4” kg/W (PDF p. 2). Table 3 acceptance-test values include “4.7”, “15.2” and “35.5” kg/W across test points (PDF p. 3); 2.0 is below the extracted minimum, and the row does not map 15.0 to a defined design envelope. The current `CITATIONS.md` entry identifies 5.5 kg/W specific mass, not the [2.0, 15.0] band.

Verdict: open **rc-812** for the range endpoints and mass/lift scope. Applied rc-108 covered the midpoint citation and left the range untouched; open rc-701 concerns the separate W/W specific-power band. Preserve the values pending a traceable band basis; no numeric replacement inferred. Extracted: `extracted_data/r946_spacecost_cryocooler_specific_mass_band.csv`.

## R958 — Bulk ore-restraint fraction basis in Spacecost and Economicspace (2026-11-19)

At Spacecost main 868f42890ac97ee40a50d79f7b33863046edb0ff, reference/storage_systems.csv row 12 stores 0.15 kg/kg with range 0.08–0.30 and calls it “ENGINEERING ESTIMATE”; its note says no registered source sets the ratio and assumes dense ore in a body-mounted hopper (spacecost_bulk_ore_restraint_row_current_2026). NASA OIG IG-18-016 p. 18 gives cargo capacities but no dry masses. Motiwala et al. (NASA/TM-2014-218366) p. 11 gives “0.038 to 0.45” stage-level structural fractions, a different denominator. Orbital Sciences’ slide 4 lists Cygnus PCM masses against payload masses; those component figures do not describe a whole spacecraft or loose-regolith hopper (nasa_oig_2018_ig-18-016_commercial_resupply_services_audit, motiwala_mathias_mattenberger_2014_conceptual_lv_spacecraft_design_risk, orbital_sciences_2014_cygnus_configuration_mass).

At Economicspace main b6c962c4f06dc5b625fee39044d8d1699ac564c9, modules/calc.py line 190 sets return_structure_frac_of_payload to 0.15; lines 147–150 describe 15% of haul above the 500 kg dry-mass floor, and line 7554 applies the fraction to payload (economicspace_return_structure_fraction_code_current_2026). campaign/verification_sheet.py lines 2872–2874 labels f_str “ore restraint per kg of payload” and reads that config value (economicspace_return_structure_verification_sheet_code_current_2026). Moving the fraction across its stored 0.08–0.30 interval changes the direct dry-mass term by 0.22 kg per kg payload, before cascade effects.

Verdict: open rc-821 for a traceable, denominator-matched mass budget or design and sensitivity of the modeled return mass over the stated range. Keep the values explicitly identified as an engineering estimate; no numeric replacement inferred. Distinct from applied rc-137 and rc-225 (citation/comment corrections) and rc-423 (Cygnus PCM configuration mass). Extracted: extracted_data/r958_bulk_ore_restraint_fraction_scope.csv.

## R979 — Spacecost bibliography entry for NASA SP-2009-4012 (2026-11-19)

**nasa_sp_2009_4012_external_tank_characteristics**: NASA Historical Data Book, Vol. VII, Table 2-86 identifies the Shuttle SLWT "inert weight" as 58,500 lb (26,535 kg) (printed p. 165) and lists separate LOX/LH2 tank volumes (printed pp. 165-166). `spacecost/propellants.py` cites NASA SP-2009-4012, Table 2-86, for the 0.0129 kg/L Shuttle anchor; `reference/storage_systems.csv` row 2 retains a 0.025 kg/L base [0.013, 0.035] scenario. Spacecost `CITATIONS.md` line 144 has the generic entry "Shuttle External Tank, Falcon 9 second stage, Centaur III" but omits the report title, number, author, date, and URL.

Verdict: open rc-844 for a full bibliography entry scoped to the Shuttle tank anchor. This is distinct from applied rc-585's tankage-basis review; no numeric replacement inferred. Extracted: extracted_data/r717_low_pressure_tankage_basis.csv.

## R985 — Spacecost Shuttle tank anchor referenced upstream (2026-11-19)

At Spacecost main 5ae7f70855d24c71dc54fc3a916624f325c034e8 (PR #53, 0.18.6), CITATIONS.md section 2 gains `nasa_sp_2009_4012_external_tank_characteristics`, Table 2-86, scoped to the Shuttle SLWT anchor only (rc-844). The 0.025 kg/L base is unchanged.

Verdict: rc-844 closed as applied. Extracted data: none new.

## R990 — Spacecost ore-restraint band and sensitivity stated upstream (2026-11-19)

At Spacecost main a6901495d257cbcd018b31e238498c94f301c865 (PR #54, 0.18.7, data contract 1.27.7; notes and comments only), the bulk ore restraint note labels its [0.08, 0.30] band a scenario, gives the 0.22 kg/kg dry-mass spread before the cascade, and scopes the stage-level and Cygnus comparators as non-matching (rc-821). Value unchanged.

Verdict: rc-821 closed as applied. Extracted data: none new.

## R1017 — Shadow fraction omitted from the solar night calculation in the worksheet (2026-11-22)

- `economicspace_stage3_eclipse_dark_fraction_current_row_2026` gives the Stage 3 “Eclipse / night-side dark fraction” base 0.50 with endpoints 0.35 and 0.55 (operational_costs.csv, line 35, at the pinned Economicspace revision). `economicspace_worksheet_dark_fraction_formula_code_2026` passes that fraction into the calculator’s `dark_period_hours` (modules/calc.py lines 2533–2557, 6641–6655). The worked calculation uses half a rotation (worked_calculation.py lines 2641–2672). The worksheet shows “min(P_rot / 2, dark_max)” and lists the rotation and cap as its only dependencies (verification_sheet.py lines 2990–2995).
- With 2018 DT’s 10.222 h prior, the 72 h cap and Stage 3 solar inputs, the calculator gives 3.5777, 5.1110 and 5.6221 h at the three fractions. The worksheet gives 5.1110 h for all three. At 0.35 the resulting effective rating is 14.6024 W/kg in the calculator and 12.0156 W/kg in the worksheet. **rc-880** asks the worked calculation and worksheet to use and cite the selected fraction in the night step.

Extracted data in `extracted_data/r1017_worksheet_dark_fraction_scenarios.csv`.

## R1041 — Phase-density return-cargo refit in the verification worksheet (2026-11-23)

- economicspace_worksheet_return_cargo_refit_code_2026 pins Economicspace `15c629b7b827d5a382c8c09f5f2702b839b99d71`. The worked calculation caps initial mass at 0.25 × fairing volume × body density (lines 3915–3943), then reports the concentrate’s phase volume (lines 4055–4059). Calculator lines 7972–7984 apply that phase-volume sum and call `_solved_under` when it exceeds the usable hold. The verification sheet reports the phase volume at lines 4221–4249.
- With the SLS Block 1 fairing at 216 m³ and water at 1.0 kg/L from spacevalue_installed_prices_release_manifests_2026, the controlled fixture’s 54 m³ allowance leaves the worksheet at 57,746.6 kg and 57.7466 m³. The calculator branch asks for a 53,999.999946 kg cap. A cap-only callback yields 53.999999946 m³. The raw, phase-volume-off, smaller water hold and denser iron hold controls match without refit.
- economicspace_return_cargo_volume_record_2026 records the original calculator comparison behind rc-285. **rc-915** records the absent worksheet re-settlement and the source inputs needed to show the binding hold limit.

Extracted data in `extracted_data/r1041_worksheet_return_cargo_refit.csv`.


## R1046 — Launch-liquid refit in the verification worksheet (2026-11-23)

- economicspace_worksheet_launch_liquid_refit_code_2026 pins Economicspace 15c629b7b827d5a382c8c09f5f2702b839b99d71. The calculator's `model_launch_liquid_volume` branch compares Earth-loaded outbound and return fuel against fairing volume times propellant density and calls `_solved_under` when liquid exceeds the envelope (calc.py L7904–7920). The worksheet settles both propellant legs and checks that “the launch stack exceeds the vehicle's capacity to LEO” (worked_calculation.py L3950–3958 and L4006–4027). It then computes mission duration without replaying the liquid check.
- The installed Electron row gives 1.19 m³ and 300 kg. The installed development LH2 row gives 0.0708 kg/L. At 140 kg cargo, a controlled fixture with fixed sizing gives 245.258 kg launch mass and 125.033 kg Earth-loaded liquid. The calculator branch requests a 68.356 kg payload cap against the 84.252 kg liquid limit. Reapplying the settled worksheet mass equations at that cap gives 84.252 kg liquid. Gate-off, 50 kg cargo, on-site return fuel and hydrolox controls request no refit. **rc-926** records the worksheet replay gap. The fixture executes the cap branch and fixed mass equations with a cap-only callback.

Extracted data in extracted_data/r1046_worksheet_launch_liquid_refit.csv.


## R1072 — Carbon dioxide and ammonia cargo containment and volume (2026-11-24)

- economicspace_spacevalue_nonwater_volatile_cargo_paths_2026 records the Economicspace charge of 0.05 kg containment per kg of water. The settlement calculation gives zero increment for a 200 kg CO2/NH3 hold and 10 kg for a 200 kg water hold. nasa_sts129_press_kit_2009_ammonia_tank_assembly, p. 34, records an ammonia tank assembly at “approximately 1,702 pounds” with 600 lb NH3, or 1.84 kg of full non-ammonia assembly per kg NH3. macatangay_2009_iss_liquid_ammonia_inventory, p. 3, reports “liquid NH₃ as refrigerant” at about 2 MPa. clark_trevathan_2001_mars_co2_collection, abstract, describes CO2 thawed in a “closed pressure vessel” after freezing. These are pressurized hardware and process examples. **rc-974** records the cargo state and containment boundary.
- economicspace_spacevalue_nonwater_volatile_cargo_paths_2026 records Spacevalue's “Solid density” values 1.56 kg/L for CO2 and 0.82 kg/L for NH3. Economicspace uses these in the concentrate phase-volume sum. span_wagner_1996_carbon_dioxide_eos, p. 1561 Table 34, gives saturated liquid CO2 at 290 K as 804.67 kg/m³ and 5.3177 MPa. macatangay_2009_iss_liquid_ammonia_inventory, p. 3, gives 272 kg in 394 L at 1.7–3.9 °C for the liquid ammonia per loop. A hold of 100 kg of each species moves from 0.1861 m³ at the solid densities to 0.2691 m³ at the separate liquid comparator states. Both figures are material volumes. **rc-975** records the state-specific density citations.

Extracted data in extracted_data/r1072_ammonia_and_co2_cargo_state_and_containment.csv.


## R1080 — Mining dust evidence and mitigation mass basis

- `spacecost_economicspace_dust_mitigation_and_mass_code_2026` — Spacecost `storage_systems.csv` line 16 attributes ended Apollo EVAs and a jammed InSight mole to fines, claims hours of observed ejecta at Ryugu, and lists 0.08 [0.03, 0.20] kg/kg of mining hardware. The note says the figure is included in the rig recurring rate. Economicspace's `verification_sheet.py` lines 4884–4894 multiply the rig and plant masses by the `Mining payload recurring cost` input, a $300,000/kg scenario in Spacecost `operational_costs.csv` line 3. On a gross 2,000 kg rig basis, 0.08 implies 160 kg of mitigation hardware.
- `nasa_tm_2005_rev1_effects_lunar_dust_eva_systems_apollo` — Printed p. 6 gives 0.15 and 0.25 psi/min after Conrad's first and second EVAs, respectively, against 0.30 psi/min limit. A third EVA is discussed as “had it been scheduled.” `spohn_etal_2022_insight_hp3_mole_penetration_lessons` section 6 attributes failed penetration to inadequate hull-to-soil friction to balance hammer recoil and to high penetration resistance. `kikuchi_etal_2026_ryugu_sci_ejecta_and_reimpact` analyzes 14 DCAM3 images from 4–497 seconds after impact and models re-impact and deposition. Verdict: the notes conflate seal degradation, soil mechanics and ballistic ejecta (rc-990).
- `buhler_etal_2025_blue_ghost_dust_shield_demonstration` — Printed p. 2, Figure 4 reports 97% dust removal from the glass coupon and 82% from the radiator coupon on Blue Ghost. `mcbrayan_francis_sobey_2025_viper_mobility_dust_mitigation` describes seal selection for lunar mobility. Verdict: these demonstrations explain mitigation options, while Spacecost's rig-level mass and cost coverage needs a documented basis (rc-991).
- Extracted data: `extracted_data/r1080_mining_dust_evidence_and_mass_basis.csv`.


## R1081 — Payload-wide return structure and ore restraint

- `economicspace_return_structure_ore_restraint_scope_code_2026` — Economicspace `verification_sheet.py` lines 3055–3060 call 0.15 “ore restraint per kg of payload.” `calc.py` lines 164–190 include “tankage, primary structure, cargo restraint, the parachute or the berthing mechanism” in the allowance and apply it to total payload in lines 7762–7772. A 1,000 kg fixture adds 150 kg of base structure whether it carries 0 or 1,000 kg of water. The separate 0.05 kg/kg Spacecost water hold term adds 0–50 kg on top.
- `brown_etal_1990_lunar_regolith_bagging_system` — Appendix H item 6 uses 1.50 lb per empty bag and reports 628 kg across 924 bags. Appendix D uses 29,702 in³ of regolith per bag at 1.2 g/cm³, about 584 kg of fill, yielding a calculated bag-only ratio of 0.00117 kg/kg in the lunar surface design. Appendix H item 26 reports 687 kg including the filling equipment. Verdict: component scope and payload denominator need to be explicit in the worksheet and its citation (rc-992).
- Extracted data: `extracted_data/r1081_return_structure_and_ore_restraint_scope.csv`.


## R1082 — Launch fairing share assigned to the return hold

- `economicspace_fairing_to_return_hold_allowance_code_2026` — Economicspace `calc.py` lines 7644–7668 introduce “say 25%” of the launch fairing as the return hold. The 0.25 also enters the search bound at lines 9247–9248. `verification_sheet.py` lines 3316–3332 cite the fairing input, then call the result “what the hold can physically carry.” At pinned Spacecost fairing volumes of 157 and 216 m³ the quarter rule gives 39.25 and 54 m³. The 100 m³ default gives 25 m³.
- `spacex_falcon_payload_users_guide` — Printed p. 16, section 4.1.3 defines the “payload static envelope, or keep-in volume” for launch integration, accounting for adapter fit and relative deflections. `nasa_2026_commercial_crew_dragon_capsule_trunk_architecture` — In “Dragon Design and Development,” NASA describes the unpressurized trunk as the Falcon 9 ascent interface and says it is jettisoned before reentry. The pressurized cargo is in the capsule. Verdict: the worksheet needs an independent basis or explicit scenario label for converting an ascent envelope to internal return capacity (rc-993).
- Extracted data: `extracted_data/r1082_fairing_to_return_hold_allowance.csv`.


## R1095 — Battery discharge depth and cycle life (2026-11-24)

- spacecost_economicspace_battery_depth_and_cycle_scope_2026 gives 104 Wh/kg usable energy from 130 Wh/kg at 80% depth of discharge. The pinned eclipse equation uses that value to size the increment for one night. The archived 2018 DT worksheet gives a 10.222 h rotation, 3 yr digging and 4.937696 yr on the body. One cycle per rotation implies about 2,573 cycles during digging and 4,234 if storage remains active throughout the wait.
- schmitz_2023_rps_vs_solar_array_comparison, p. 8 Table 3, lists 175 Wh/kg and 80% depth with no associated cycle count. herman_smart_2021_opportunity_battery_cycle_life, slide 10, gives “approximately a 44-50% DOD duty cycle” and “over 5,000 cycles” across Opportunity’s battery wet life. west_smart_herman_2021_perseverance_battery_requirements, rover battery driving requirements, calls for over 2,010 cycles in three years at a maximum 60% depth.
- In the pinned kernel, a 50% discharge sensitivity at the archived 5.111 h night and 0.58 h baseline increases incremental storage from 43.57 to 69.71 kg per kW of continuous load. **rc-1009** records the missing pack-life and end-of-life energy basis.

Extracted data in extracted_data/r1095_battery_depth_of_discharge_and_cycle_life.csv.
