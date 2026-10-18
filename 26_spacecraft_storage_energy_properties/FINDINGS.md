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

rc-109 (regenerative fuel cell round trip 47.4%), rc-110 (four storage figures not in the R104/R105 reports), rc-115 (NEP row repeats the KRUSTY overstatement). Texts and evidence in `revision_candidates.csv`.
