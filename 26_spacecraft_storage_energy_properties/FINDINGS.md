# Domain 26 — Spacecraft storage & energy-system physical properties

Backings: spacecost `reference/storage_systems.csv` — the propellant-storage cells (`Low-pressure liquid propellant tank`, `COPV burst performance factor`, `Multi-layer insulation (passive)`, `Zero-boil-off cryocooler (20 K)`, `Cryocooler specific mass (20 K)`, `Vapour-cooled shield`), the energy-storage cells (`Li-ion battery`, `Regenerative fuel cell`, `Flywheel energy storage`, `RTG specific power`, `Fission surface power (Kilopower class)`) and the depot cells (`Orbital propellant depot (cryogenic)`). Read from spacecost @77c6e11; `storage_systems.csv` last touched by 8412c2e.

Created in Round 104 (2026-10-02). Blocks are appended one per round, newest last. The cargo-containment cells of the same file (`Bulk ore restraint`, `Volatile cargo containment`, `Sintered / consolidated cargo`, `Dust mitigation and seals`) have no institutional source yet — they stay upstream judgement rows; this domain opens for the propellant-tankage/COPV/MLI/cryocooler and RTG/fission energy cells, which had no domain home (d5 holds only cryocooler *program* docs and d11 power-*budget* docs).

## R104 - Domain opened; eight NTRS government technical reports hosted (2026-10-02; +8 sources, all T2 full_text_hosted)

The first round for this domain. Every source was pulled live from ntrs.nasa.gov on this machine, verified as a valid PDF (magic `%PDF`, SHA-256 recorded in `full_texts_manifest.csv`), and read with PyMuPDF to confirm it backs the named cell before registration. All carry an NTRS Public Use Permitted determination -> license class `ntrs-public-use`. Each row is **Context-only** per the R99/R100 convention (gathering over extracting): its relevant figure/discussion was read this round but no number has yet been extracted into an `extracted_data/` CSV — that extraction pass is the follow-up step.

Cells and their current upstream values (spacecost @77c6e11, `storage_systems.csv`), with the R104 source(s) now backing each:

| cell | unit | value (low-high) | status/TRL | backed by (R104 id) |
|---|---|---|---|---|
| COPV burst performance factor | J/kg (PV/W) | 392,000 (250,000-600,000) | operational / 9 | nasa_tm_2026_copv_stress_rupture_mechanics_carbon_fiber; ntrs_2010_copv_stress_rupture_testing; ntrs_2011_copv_flight_rationale_shuttle_program |
| Fission surface power (Kilopower class) | W-elec/kg | 6.7 (0.7-15) | development / 5 | ntrs_2020_kilopower_krusty_fission_power_experiment_missions; ntrs_2020_krusty_reactor_design |
| RTG specific power | W-elec/kg | 5.0 (2.4-5.5) | operational / 9 | nasa_tm_2025_rtg_power_performance_histories |
| Multi-layer insulation (passive) | kg/m² tank surface | 1.2 (0.5-3.0) | operational / 9 | nasa_tm_2011_long_term_cryogenic_storage_microgravity; ntrs_2014_cryogenic_boiloff_reduction_system_testing |
| Orbital propellant depot (cryogenic) | % stored mass lost/day | 0.03 (0.01-0.1) | development / 5 | nasa_tm_2011_long_term_cryogenic_storage_microgravity; ntrs_2014_cryogenic_boiloff_reduction_system_testing |

Already registered in other domains and relevant here (referenced by id, not moved): `nugent_2022_rtb_cryocooler_test` + `plachta_2017_cryo_zbo_goals` (domain 5) back the two cryocooler rows; `nasa_std_5019_fracture_control_spaceflight_hardware` (domain 3, §7.2.2 Fracture-Critical COPVs + ANSI/AIAA S-081) is the standards chain behind the same COPV burst factor. No revision candidate opened: these are new backing for currently unbacked judgement cells, not corrections to an existing value. See `full_texts/` (8 PDFs).

## R105 - Domain extended to the remaining storage_systems.csv cells (2026-10-03; +8 sources, all T2 full_text_hosted)

Round 104 left four cell groups of `storage_systems.csv` without institutional backing (noted at the end of the R104 block). This round closes them: every source was pulled live from ntrs.nasa.gov on this machine, verified as a valid PDF (`%PDF` magic + SHA-256 in the manifest) and read with PyMuPDF before registration. All NTRS Public Use Permitted -> `ntrs-public-use`; all Context-only (gathering over extracting).

| cell | unit | value (low-high) | status/TRL | backed by (R105 id) |
|---|---|---|---|---|
| Li-ion battery (system level) | Wh/kg | 130 (90-200) | operational / 9 | ntrs_2016_orion_small_cell_battery_design_support |
| Flywheel energy storage | Wh/kg | 100 (40-180) | development / 6 | ntrs_2006_g2_flywheel_module_design; ntrs_2002_energy_storage_flywheels_on_spacecraft |
| Regenerative fuel cell | Wh/kg | 400 (250-700) | development / 5 | ntrs_2020_analysis_100w_regenerative_fuel_cell_demonstration; nasa_cr_1984_regenerative_hydrogen_oxygen_fuel_cell_electrolyzer |
| Sintered / consolidated cargo | Wh/kg ore consolidated | 350 (150-800) | concept / 3 | ntrs_2023_vacuum_sintering_highland_simulant; ntrs_2020_microwave_sintering_lunar_landing_pads |
| Dust mitigation and seals | kg per kg mining hardware | 0.08 (0.03-0.2) | development / 5 | nasa_tm_2005_rev1_effects_lunar_dust_eva_systems_apollo |

Notes: the Orion battery document is a JSC workshop presentation with a partial OCR text layer (title page + section headings intact; body figures not yet machine-readable - extraction follow-up). The MSCC microwave-sintering item is NTRS's PDF render of a .pptx. With R105, every propellant-storage and energy-storage cell group in `storage_systems.csv` now has at least one institutional source behind it; the cargo cells' *containment-mass* figures (Bulk ore restraint 0.15 kg/kg, Volatile cargo containment 0.05 kg/kg) remain upstream judgement rows - no institutional mass-per-kg figure located yet. No revision candidate opened: new backing for currently-unbacked cells, not corrections.

## R150 (2026-10-10) - dust-mitigation cell deepened: three modern peer-reviewed NTRS-hosted sources for the 'Dust mitigation and seals' kg-per-kg cell

**Why this round.** d26's opening brief left `storage_systems.csv` "Dust mitigation and seals" (upstream value 0.08 kg per kg mining hardware, development/TRL5) backed by a single Apollo-era record (`nasa_tm_2005_rev1_effects_lunar_dust_eva_systems_apollo`, R105). A whole-corpus grep found zero hits for 'viper', 'goldmap' or the ICES dust papers - no modern institutional source on lunar-dust mitigation hardware was registered anywhere. NTRS searches surfaced a cluster of peer-reviewed IESS/ICES conference papers, all with public-use determinations and downloadable files; R150 locked onto the three strongest for this cell.

**Registered and hosted (3).** All carry zero in-file copyright statements -> `ntrs-public-use` per the R131 precedent:
- **mcbrayan_francis_sobey_2025_viper_mobility_dust_mitigation** [T2; full_text_hosted] - ICES-2025-147, 54th IESS Prague Jul 13-17 2025 (NTRS 20250005201, GOV_PUBLIC_USE_PERMITTED). 15 pp / ~1.2 MB committed. The FIRST modern institutional seal matrix for a lunar mobility system: labyrinth / Nomex felt / spring-energized PTFE seals with individual mechanisms plus grease damming in the sealed chassis; face-seal compression practice (VIPER 20% per MER/MSL heritage vs Tri-ATHLETE's suggested 5-10%).
- **lee_brown_2023_gateway_lunar_dust_mitigation_overview** [T2; full_text_hosted] - NTRS 20230003126 (PUBLIC_USE_PERMITTED). Single-page overview committed. The institutional Gateway dust-mitigation program record: GOLDMAP physics-based contamination framework + a two-pronged mitigation strategy with cross-program coordination. Year 2023 assigned from the file revision stamp (RL 3.8.23) + NTRS accession year - no structured date field, flagged per the R138 lesson.
- **jones_et_al_2026_artemis_suit_dust_exposed_fabrics** [T2; full_text_hosted] - ICES-2026-164, 55th IESS Rio Grande PR Jul 12-16 2026 (NTRS 20260002937, PUBLIC_USE_PERMITTED). 13 pp / ~535 KB committed. Measured EOL dust-soiling test process for Artemis suit fabrics: rotary tumbler abrasion with lunar simulant + ceramic media reproducing cumulative surface-operations wear (453.5 g each, eight-hour tumble at 80 rpm, drum flipped halfway).

**Key numbers.** `extracted_data/r150_dust_mitigation_key_numbers.csv` - 5 rows x 7 cols; every verbatim quote span re-verified count==1 against the committed PDF copies inside this apply script before any file write.

**No re-pin, no rc opened.** All three sources are context/bound class: none states a dust-mitigation mass-per-hardware figure, so the 0.08 kg/kg upstream judgement row stands unchanged - but it now sits beside institutional seal-matrix practice (VIPER), an environment-characterization framework (GOLDMAP) and a measured cumulative-wear test recipe (Artemis suit tumbler) rather than a single Apollo anecdote.
