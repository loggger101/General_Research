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
