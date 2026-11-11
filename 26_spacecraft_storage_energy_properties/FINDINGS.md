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
