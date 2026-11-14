# Domain 19 — Asteroid excavation throughput & beneficiation

Backings: economicspace `modules/calc.py` mining and beneficiation fields (`mining_rate_kg_per_day_per_kg_rig`, `mining_hardware_kg`, `max_mining_duration_yr`, `station_keeping_floor_yr`, `beneficiation_recovery`, `max_concentration_ratio`) and spacecost `reference/operational_costs.csv` rows `Drilling / excavation energy`, `Beneficiation / on-site processing energy` and `In-space processing plant throughput`; since R76 also spacevalue `spacevalue/catalog.py` `IN_SPACE_PROCESSING_KWH_PER_KG` (in-space refining energy).

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` `mining_rate_kg_per_day_per_kg_rig` | 0.10 (a 2,000 kg rig moves 200 kg/day) | "an engineering assumption, not a measurement"; TAGSAM (~122 g per touch) for scale |
| `calc.py` `mining_hardware_kg` | 2,000 kg | none stated |
| `calc.py` `max_mining_duration_yr` / `station_keeping_floor_yr` | 3.0 yr / 0.25 yr | none stated |
| `calc.py` `beneficiation_recovery` | 0.90 | "Terrestrial PGM / sulphide flotation circuits run 85-95%"; no source, no microgravity heritage |
| `calc.py` `max_concentration_ratio` | 50:1 | "Terrestrial mills run 100:1 to 1000:1 on PGM ores"; no source |
| `Drilling / excavation energy` | 200 Wh/kg [50, 500] of regolith | "Zacny et al. (NIAC studies ...)", not identifiable (R74) |
| `Beneficiation / on-site processing energy` | 500 Wh/kg [100, 2000] of refined product | a school worksheet, withdrawn in spacecost 0.5.1 (R112) |
| `In-space processing plant throughput` | 100 kg/yr per kg of plant [20, 500] | "Terrestrial smelters run 1,000x their own mass per year", derated tenfold |

**What a source has to supply:** measured excavation rates and specific energies in reduced gravity or vacuum with machine mass; recovery and grade of magnetic and electrostatic metal-silicate separation, and terrestrial comminution energies; throughput-to-mass of compact plants; terrestrial autonomous-mining analogues for scale.

**Also relevant, registered elsewhere:** `metzger_zacny_2020` (d05), `hein2020` (d22; R61 recorded a plant-throughput discrepancy).

**Boundary:** domain 5 keeps volatile extraction, ISRU propellant processing and storage; domain 2 what the body contains. This domain covers getting ore out and concentrating it.

## R76 - Scope extended to in-space refining energy (2026-09-27)

| cell | current value | upstream's stated basis |
|---|---|---|
| economicspace `mineral_value.py` `IN_SPACE_PROCESSING_KWH_PER_KG` | kWh per kg of feedstock: Fe, Ni, Co, Cu, nickel-iron, awaruite 5.0; magnetite 7.0; troilite 4.0; carbon, organics 2.0; silicates 1.0; water 0.5 | "Terrestrial electric-arc / direct-reduction steelmaking runs 4-5 kWh/kg; electrowinning iron is similar"; no source |
| economicspace `mineral_value.py` `_INSPACE_PLANT_LIFE_YR` | 15 yr | none stated; same as `Mining rig service life` (domain 16) |

Needed: specific energies of reducing, melting and forming Fe-Ni and sintering silicates, for space or small plants.

## R77 - Sources moved in (2026-09-27)

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `just_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round-10, 43, 44 and 57 additions | `extracted_data/r43_excavation_energy_key_numbers.csv` |
| `zeng_2007` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r70_zeng_2007.csv`, `full_texts/zeng_2007_excavation_force.pdf` |
| `proctor_apex_2019` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition; R71 | `extracted_data/r71_proctor_apex_2019_key_numbers.csv` |
| `zeitlin_asteroid_excavation_project` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 43 addition | `extracted_data/r71_zeitlin_asteroid_excavation_project_key_numbers.csv` |
| `ssap_2021` | domain 5 | `05_inspace_operations/FINDINGS.md`: the `ssap_2021` block; Round-3 additions; Maintenance; R71 | `extracted_data/ssap_2021_table3_theoretical_yields.csv`, `extracted_data/r71_ssap_2021_key_numbers.csv`, `extracted_data/r71_ssap_2021_reactions_energetics.csv` |

rc-026 and rc-027 (Drilling / excavation energy) are written up in domain 5. `metzger_zacny_2020` stays in domain 5 (thermal volatile extraction).

## R112 - Beneficiation citation withdrawn upstream (2026-10-04)

spacecost 0.5.1 (`85da36c`) applied rc-048: the beneficiation row now calls its 500 Wh/kg [100, 2000] an unsourced estimate. The worksheet was rejected by the owner and rc-048 deleted with it. The cell still needs a specific energy for magnetic, electrostatic or thermal concentration per kg of concentrate.

## R113 - Two unread candidates (2026-10-04)

Both paywalled, `registered_not_pulled`: `tang_et_al_2023_asteroid_rock_mechanical_properties` (Engineering Geology 321:107154; asteroid rock mineralogy and strength, for the excavation row and mining rate) and `liu_et_al_2026_asteroid_laser_mining_cryogenic_vacuum` (Chem. Eng. Res. Des. 233:150-161; laser processing of simulants with Fe-Ni enrichment, for recovery and concentration ratio).

## R114 - Measured excavation energy, thermal and optical mining, PGM recovery (2026-10-04; +13)

**Excavation energy:** `giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru` (4.8 kg bucket drum: 777.54 kg/h at 0.022 Wh/kg continuous, 172.02 kg/h at 0.86 Wh/kg batch) and `kafi_2026_spiral_cavity_wheel_excavator_lunar_isru` (29% below a bucket drum) are orders of magnitude under 200 Wh/kg, a floor for loose regolith. `schuler_2022_isru_pilot_excavator_bucket_drum_scaling`: a 30 kg-class excavator for 10,000 kg of regolith (RASSOR 2.0 is 65 kg). `jayathilake_2022_geotechnical_parameters_lunar_regolith_excavations` and `ricardo_2026_trafficability_excavatability_icy_lunar_regolith_cone_penetration` from abstract.

**Thermal and optical mining:** `sowers_2020_niac_phase1_thermal_mining_of_ices` (read in full; the Colorado School of Mines copy, since the owner's copy differs: 'February 2019' vs 'February 2020'), probably the NIAC study the row meant: 126 kg/h of ice; 42.0 kg of annual propellant per kg of plant vs 2.3 for Langley's excavation-based plant (`jones_klovstad_komar_judd_2018_cost_breakeven_cislunar_isru`, d22). `techport_33509_optical_mining_asteroid_excavation_sbir` (a 100 t water claim), `broslav_2025_optical_mining_carbonaceous_chondrite_simulants` (abstract), `sercel_2018_time_dependent_outgassing_model_bulk_heating` (simple heating "too slow for industrial water yield").

**PGM recovery (0.90):** `liddell_adams_2012_kell_hydrometallurgical_process_pgm_base_metals` and `liddell_2019_kell_hydrometallurgical_extraction_piloting_engineering_implementation`: above 95% for value metals; capex 18-33% and opex 51-66% of smelting and refining. `kabemba_2025_geometallurgical_framework_flotation_kinetics_platreef_pgm`: batch flotation 83.25-94.37% (the owner's "90.6%" is the liberated share). `hay_2010_optimising_ug2_flotation_part2_modelling_pgm_recovery_cr2o3_rejection`: title only. All terrestrial analogues.

`extracted_data/r114_gr_links_key_numbers.csv`. No candidate.

## R119 / R120 - Excavation and recovery papers hosted (2026-10-05)

- giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru hosted (CC BY) as full_texts/giel_et_al_2025_bucket_drum_excavator_moonbot_arxiv2511.00492.pdf: "The resulting tool weighs 4.8 kg and has a volume of 14.06 L"; the R114 figures confirmed.
- ricardo_2026_trafficability_excavatability_icy_lunar_regolith_cone_penetration: the journal version's in-file licence is CC BY-NC-ND (Crossref says cc-by), so the CC BY Research Square preprint is hosted as full_texts/ricardo_hodgkinson_rhamdhani_et_al_2026_trafficability_excavatability_icy_lunar_regolith_research_square_rs-9421896_ccby.pdf: cone penetration of unsintered, pressure-sintered, ice-cemented and vapour-deposited icy simulants.
- kafi_2026_spiral_cavity_wheel_excavator_lunar_isru read in full from arXiv (default licence, not hosted).
- `kabemba_2025_geometallurgical_framework_flotation_kinetics_platreef_pgm` hosted (CC BY) as kabemba_mutombo_waters_2025_geometallurgical_framework_flotation_kinetics_platreef_pgm_minerals_15_701_mdpi_ccby.pdf: "P-FPX3 = 83.25%" and "peak recovery (94.37%)".

## R152 - rc-027 unblocked: measured excavation energies and DOE's mining benchmark (2026-10-12)

rc-027 (200 Wh/kg, range 50-500, spacecost@0b716ad) no longer needs just_2019's table. `extracted_data/r152_excavation_specific_energy_key_numbers.csv`:

| source | what was measured | Wh/kg |
|---|---|---|
| schuler_2022_isru_pilot_excavator_bucket_drum_scaling (IPEx, p14 Fig. 15; read from vector markers) | mechanical energy at the drum per kg, three drums, two cut depths, 10 and 30 mm/s | 0.0029-0.0071 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p5 Table IV) | a literature bucket drum, continuous | 0.007-0.02 |
| kafi_2026_spiral_cavity_wheel_excavator_lunar_isru (p5) | spiral-cavity wheel and two baselines, 44.2-83.5 J/kg | 0.012-0.023 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p4-p5) | MoonBot bucket drum, continuous | 0.022 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p5 Table IV) | RASSOR 2.0, batch (just_2019's 0.761) | 0.76 |
| giel_2025_modular_bucket_drum_excavator_moonbot_lunar_isru (p5 Table III) | MoonBot batch cycle incl. unloading and 139 s driving (0.864 recomputed) | 0.86 |
| doe_2007_mining_industry_energy_bandwidth_study (Exhibit 24) | US metal mining: drilling + blasting + digging, 17,700 Btu/ton | 5.72 |
| doe_2007_mining_industry_energy_bandwidth_study | all extraction incl. ventilation and dewatering, 23,000 Btu/ton | 7.43 |
| doe_2007_mining_industry_energy_bandwidth_study | extraction plus diesel haulage, 97,900 Btu/ton | 31.63 |
| doe_2007_mining_industry_energy_bandwidth_study | whole mine incl. crushing, grinding and separation, 168,746 Btu/ton | 54.51 |

**doe_2007_mining_industry_energy_bandwidth_study** (US DOE ITP, BCS Inc., June 2007; new; contractor-prepared, no licence, not hosted): Exhibit 24 read from a page render (text layer scrambled), subtotal 162,148 matches its components; short tons assumed (metric lowers each figure 9.3%); with generation losses (Exhibit 14) metals run 342,200 Btu/ton = 110.5 Wh/kg.

Upstream's 200 Wh/kg is 3.7x a whole terrestrial metal mine including comminution (which spacecost prices separately at 500 Wh/kg; DOE crushing and grinding alone is 19.3 Wh/kg), and 6.3x extraction plus haulage; the 500 end is 9.2x the whole mine. rc-027 re-opened: move to ~1-10 Wh/kg (about 6 for drilling, blasting and digging), range ~0.01-32, or keep 200 and say what beyond excavation it carries. Caveat: lunar figures are loose simulant at 1 g, DOE's terrestrial ore; nothing measures asteroid rock.

## R164 / R165 - Candidates (2026-10-14)

rc-097 (cite DOE's 19.3 Wh/kg beneficiation), rc-122 (cite Kabemba's 83.25-94.37% and Liddell's >95%), rc-136 (give the mining-rate dial its plant-scale references: 42.0 vs 2.3 kg/yr per kg of plant). Texts in `revision_candidates_closed.csv`.

Extracted data: `extracted_data/r165_mining_rate_comparison.csv`.

## R207 - Refinery throughput row vs institutional ISRU bounds (rc-178)

The spacecost `In-space processing plant throughput` row (100 kg processed per year per kg of
plant, band 20-500) is justified only by an uncited analogy: "Terrestrial smelters run 1,000x their
own mass per year" [count==1]. No institutional in-space processing rate is named for it anywhere.

The sister row two lines away, `ISRU propellant plant throughput`, IS institutionally anchored - its
own note prints the derivation 11.67 t / 0.616 yr / 2.6 t = 7.28 from Kleinhenz & Paz PTMSS/SRR 2021,
and CITATIONS.md L138-139 name both K&P papers for it (band high 13.3 from AIAA-2017: 1.7 mT hardware,
6,978 kg CH4 + 22,728 kg O2 over 480 days). Recomputed live from the hosted PDFs' printed figures:

| K&P case | basis | kg processed/yr/kg plant | refinery row multiple |
|---|---|---|---|
| PTMSS ridge chain (2.6 t) | product=feedstock mass | 7.286 | point x13.7 / floor x2.74 |
| PTMSS whole baseline (4.9 mT incl mine) | same | 3.866 | point x25.9 / floor x5.17 |
| AIAA-2017 Mars hardware (1.7 mT) | product side only | 13.297 | point x7.5 / floor x1.50 |

So the refinery band's FLOOR sits ~1.5x above the best institutional figure and its POINT value
runs 8-26x past it, in spacecost's own units. Economicspace consumes the row live as `refinery_rate`
(modules/calc.py L7618; master.py L11125) with an unsourced restated fallback constant at master.py
L1757 (count==1). Their verification_sheet #150 backing ledger flags this input (I89) as needing
backing independently. rc-178 proposes naming both papers as bound references on the note and a
CITATIONS.md entry; value decision left open, no re-pin.

STANDING SEAM NOTE for future rounds: that same backing ledger names 99 inputs needing backing - most map onto
open candidates already (rc-086..177 cover operational/storage/propellant/mineral cells). Remaining unclaimed
classes seen while triaging it: the physics/dv constants restated uncited in campaign/worked_calculation.py L103-124
(mu_E, v_E, r_LEO, R_MOON, DV_NRHO=0.450 - which MATCHES the sourced delta_v_segments NRHO-insertion row 450 m/s),
the search-method dials (ladder rungs, fleet max) and the Cap_* market-routing ceilings; those are judgment or
self-derived by design. The sister-row band [7.28,13.3] is anchored - do not re-litigate it here.

## R212 cross-reference (2026-10-20)

The previously-unclaimed worked_calculation constants MU_EARTH and V_EARTH are now institutionally cited upstream (economicspace CITATIONS.md, PR#154 at origin/main 675f0cf) and registered in domain 12 as iers_petit_luzum_2010_conventions_tn36 and nasa_nssdca_earth_fact_sheet; R_MOON likewise matches the Moon fact sheet semimajor axis exactly (see d12 FINDINGS correction note). DV_NRHO restates a sourced spacecost delta-v row. The remaining unclaimed classes from R207 are unchanged: search-method dials, Cap_* routing and r_LEO as an engineering definition.

## R222 - drift re-run closure (skip unless verification_sheet.py moves) (2026-10-20)

economicspace `be86297` campaign-runner split (#162/#163) touched no engine or sheet code; the full verification-sheet run reproduces the R215 input verdict exactly — 337 tags, inputs 29 named a source / 5 derived here / 2 term not charged / 95 need backing, steps 86 spending an unbacked input. The Round 207 triage of those classes remains current; no new needs-backing seam surfaced since. Related completeness facts: requirements.txt mirrors _MASTER_REQUIRED (requests pandas numpy yfinance tqdm spacecost-as-tagged-ref v0.12.0) with their verify_docs check 7 enforcing it, and the quietqueue citation added to CITATIONS.md is sibling tooling-repo class (github.com/loggger101/quietqueue at tag v0.1.0), documented not registered per Round 220 precedent for carved-out repos.

**Ledger verdicts invariant under CITATIONS restructuring; skip vsheet re-run unless verification_sheet.py itself moves (Round 228):** two structural proofs at economicspace `8ce5c53`. First, verification_sheet.py contains no runtime read of CITATIONS.md — the file is named only in prose labels pointing readers to where sources live; backing content derives from spacecost row notes, Module-2 catalog price-source columns and Stage-1 provenance columns per its own provenance-section comment block. Second, the #164 removal audit holds under independent check: ui.py (line 1481) is the sole importer of orbital in the published tree, and no other file references kepler_E / true_anomaly / propagate_elements / lambert_izzo / _hyp2f1b, so campaign reproduction cannot hit a dangling import. Consequence: the R215-R222 ledger counts (inputs 29 named / 5 derived / 2 term-not-charged / 95 need backing of 131) remain current at `8ce5c53` without re-running, and the roughly one-gigabyte generated profitability_catalog.csv dependency stays untouched in scratch worktree runs.

## R308 - Equatorial lift is not a whole-body regolith exclusion (2026-11-01)

`sanchez_scheeres_2020_cohesive_regolith_fast_rotating_asteroids` (arXiv v1 p18, conclusions):
"the poles are always covered with regolith". The cohesionless limit is explicit on p9; the
model assumes a thin surface layer on a strong sphere (p3) and fixed-axis rotation (p18).

At economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py:8135-8138`
returns `None` before searching any mission when `model_spin_limit=True` and measured period
is below `sqrt(3*pi/(G*rho))`. `MODEL.md:1344-1347` infers from equatorial grain loss that
the body has no loose layer to scoop. The default flag is false.

Using the paper's 35-degree friction (p4) and zero cohesion, its force components (p4,
Eqs.(3)-(4)) and Coulomb condition (p5, Eq.(9)) give, for latitude delta and
`k=(P_lift/P)^2`, downward acceleration `g*(1-k*cos(delta)^2)` and tangential magnitude
`g*k*abs(sin(delta)*cos(delta))`. Solving the friction boundary yields these static regions
for a sphere of density 2 g/cm3 (`P_lift=2.33407713 h`):

| measured period | current gate rejects | stable absolute latitude above | two polar caps / surface |
|---|---|---|---|
| 2 h | yes | 64.706755 deg | 9.586707% |
| 1 h | yes | 83.142557 deg | 0.715370% |
| 0.467 h | yes | 88.423542 deg | 0.037850% |

The closed-form boundaries also match independent numerical bisection of the force inequality.
At 2 h and latitude 80 degrees, downward acceleration remains positive and friction capacity
exceeds the tangential force. These are derived static counterexamples to universal surface
loss, not measurements of regolith inventory. Shape, tumbling and disturbance during digging
can change retention; the paper specifically warns about tumbling (p18), and supplies no
excavatable mass or throughput. Verdict: the equatorial formula is correct, but whole-body
rejection requires an additional screening assumption. `rc-238`: scope the spin gate and
its physical claim. `extracted_data/r308_spin_cutoff_polar_regolith.csv`.

## R315 - Programme extraction has no cumulative body-mass bound (2026-11-01)

Source `economicspace_programme_cumulative_resource_budget_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py` and
`MODEL.md`; original spacecost@860bef9902aa67fec705875cd52fdb8e6def159f reference
rows and spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011 cargo functions.
`campaign_cadence_yr` says "A rig stays at the asteroid" (calc.py L4579), while
the programme description says "N enters nothing in the mass cascade"
(MODEL.md L580). The per-mission cap is body mass times `max_mining_fraction`
(L5911); the returned feed is bounded against it at L6570-6603. Programme
options and selection then price this same mass book for different N, without
bounding their combined extraction (L4945-4951, L6875-6902, L7026-7290).

Nine complete original-evaluator cases retain every numerical function and
use the actual Falcon 9 reusable, kerolox and all 46 operational-cost rows.
Synthetic inputs are a 1,000 kg body of density 2 g/cm3, raw silicate cargo at
100 USD/kg, a nonbinding 1e12 kg/yr commodity ceiling and caller delta-v
1,000 m/s per leg. ISRU, beneficiation and aerocapture are off for the tested
architecture. The one-ship isolation cases disable launch windows, refinery,
water liberation, volatile containment and boil-off; other numeric defaults
remain. With the default capacity market the returned mission extracts the
whole body, but the selected programme repeats it five times:

| original case | body mass (kg) | feed per mission (kg) | selected N | total feed (kg) |
|---|---|---|---|---|
| one ship, searched | 1,000 | 1,000 | 5 | 5,000 |
| single-mission market | 1,000 | 1,000 | 1 | 1,000 |
| fixed five missions | 1,000 | 1,000 | 5 | 5,000 |
| cargo capped at half the body | 1,000 | 500 | 5 | 2,500 |
| cargo capped at one fifth | 1,000 | 200 | 5 | 1,000 |
| larger body, cargo capped at 1,000 kg | 1,000,000 | 1,000 | 5 | 5,000 |
| fleet cap 64, other isolation settings | 1,000 | 1,000 | 320 | 320,000 |
| unbounded market, one ship | 1,000 | 1,000 | 5 | 5,000 |
| default numeric configuration, body at 1.8 AU | 1,000 | 1,000 | 320 | 320,000 |

The one-ship five-mission result charges NRE at 82.39M USD per mission and
total cost at 498.893366M USD, versus 411.95M and 1,662.365366M respectively
at N=1, while gross value remains 0.1M per mission. These are per-mission
accounts. Every mission fits its separate body, throughput and launch budgets.
All cases also fit the stated 15-year rig calendar life: final dig completion
from the first dig start is 1.25 years for the five-campaign isolation cases
and 7.930317 years for the default-settings case. Thus the excess does not
require the separate rig-age, ISRU-feed or EP-sizing defects.

Four additional diagnostics filter only the F=1 programme ladder by
`N * fixed_raw_feed <= body_mass`, retaining the original masses, costs and
selection. Whole-, half- and fifth-body loads then select N=1, 2 and 5;
the large-body control retains N=5 and identical output. These diagnose the
missing bound; they do not optimise a new smaller-payload programme.

Verdict: the per-mission material cap does not conserve the finite target
across its selected programme. `rc-245`: impose a cumulative cargo/fuel-feed
budget across all ships and campaigns, with joint resizing where appropriate.
`max_mining_fraction` is documented as a per-mission fraction; the contradiction
above uses its default 1.0 and exceeds the entire body, independently of how
a smaller fraction is interpreted. Actual-population incidence and ranking
effects were not measured. `extracted_data/r315_programme_cumulative_resource_budget.csv`.

## R334 - Nominal-purity cutoff excludes better market-capped missions (2026-11-02)

Source `economicspace_concentration_market_search_bound_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`,
`MODEL.md`; spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011,
`spacevalue/cargo.py` and its 2026-10-07 cislunar price fixture;
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f, original launch,
propellant and operational CSVs. The bound says "Above this the knapsack
has nothing better to load" (calc.py L7673), using only the fraction of the
highest nominal-price phase, recovery and the configured maximum (L7679-7683).
`evaluate_combo` limits every coarse/refined ratio to that result (L7772-7814).
MODEL.md L511 likewise says "there is nothing better to add". Market caps
instead free space for lower nominal-price phases (cargo.py L1228-1230),
whose full-price kilograms can outrank the dearer phase's discounted surplus.

Twelve fixed-hold comparisons isolate this without mission costs, timing or
engineering feedback. A 1,000 kg hold, phases 90% silicates at 100 USD/kg and
10% carbon at 90 USD/kg, recovery 0.9, fixed full-price allowances of 10 and
1,000 kg, and half-price surplus give:

| feed:hold ratio | reason | carbon loaded kg | total value USD |
|---|---|---|---|
| 1.234567901235 | nominal-purity search ceiling | 111.111111 | 54,944.444444 |
| 10 | admissible extra feed | 900 | 86,500 |

The same mechanism appears at 80%/20% composition and surplus fractions
0, 0.25, 0.5 and 0.75. Independent tier arithmetic matches all eight
improvements. Four uncapped/full-price controls return 100,000 USD at both
ratios. Thus the nominal highest-price phase's physical purity point is
not a bound on market-adjusted cargo value.

Seventeen complete original `evaluate_combo` pairs retain the actual Falcon
9 reusable row, kerolox and all 46 ops rows. The synthetic body is 1e9 kg,
2 g/cm3, 1.2 AU and 8 h rotation; caller delta-v is 1,000 m/s each leg.
Recovery 0.9, maximum ratio 50 and all physical/cost coefficients remain
unchanged. Programmes have one mission; ISRU, aero, boil-off, refinery,
WACC, reliability and learning are off. Only additional original solver
calls above the normal bound are considered, retaining the original winner:

| inputs | normal chosen ratio | added ratio | normal cost/revenue | with added point |
|---|---|---|---|---|
| synthetic 90%/10%, 100/90 USD/kg, binding rich-phase market, half-price surplus | 1 (raw) | 10 | 2,354.421336 | 1,553.806592 |
| snapshot carbon 90% / silicates 10%, original prices and markets | 1.234567901235 | 2.659147948472 | 49.354569 | 48.804609 |

The snapshot retains carbon's 2,682.567488 USD/kg and 5,000 kg/yr, and
silicates' 1,603.050708 USD/kg and 15,000 kg/yr. Its body/composition remain
synthetic. This witness includes the original mission-duration/market-window
feedback; it is not the fixed-window scalar comparison above. Six synthetic
market-setting pairs and six snapshot pairs improve. Increasing the normal
search from 7 to 25 or 101 steps cannot help: recorded requested ratios all
remain at or below the same nominal bound. Five ample-market, unbounded,
single-mission, full-price-surplus and beneficiation-off controls retain
the complete original result.

Six complete `evaluate_asteroid` pairs include its original orbital,
architecture and power search with the one source vehicle/propellant.
Adding original ratio-10/20/50 solves changes the binding-cap fixture from
raw cargo to ratio 20: cost/revenue falls from 85,550.144082 to 54,621.779334.
Payload changes from 391.142165 to 370.773648 kg; gross value rises from
21,330.408099 to 33,411.374586 USD, with cost 1,824,819,486.230986 versus
1,824,988,729.869837 USD. Both mission durations are 4.174623535088 yr,
and both mining durations 0.25 yr. The 101-step consumer gives the same
miss; four complete consumer controls preserve the original result.
Every normal search/consumer repeats with an identical full-result type/
float.hex signature. The diagnostic adds candidates; it changes no original
numerical helper or physical/price field and claims no global optimum.

Verdict: the nominal-purity ratio is an unsafe search cutoff under binding
market caps. `rc-265`: use a valid market-aware bound or cover the configured
range while retaining existing candidates. This concerns which ratios are
offered to the original evaluator, separately from `rc-252`'s cargo ledger
and `rc-261`'s shared class budgets. No actual-population incidence, ranking
effect or correction to adopted rates is claimed.
`extracted_data/r334_concentration_market_search_bound.csv`.


## R344 - Flown refining routes and raw excavation power (2026-11-03)

`spacevalue_flown_refinery_route_preselection_record_2026` reads spacevalue
873b91c1ce51fd2f5fe9ead63ce171d755e73011 with economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0. `_phase_terms` says "The route
is decided on NET prices" (cargo.py L454-459), then passes that route's
gross value and energy to the flown-refinery mission. In the unchanged
59-row LEO input, magnetite's refined/as-is net values are 1128.280467/
779.411210 USD/kg; gross values 1295.104956/1022 USD/kg and process energies
10620/7000 Wh/kg. Independent yield/energy sums reproduce both routes.

Twenty-four route cases run original, exact repeat, as-is alternative,
and both routes with raw excavation charged: 120 complete consumer/kernel
runs. Nine full `evaluate_asteroid` cases and four direct RTG cases improve
the configured cost/revenue objective, including three restored feasible
RTG options. At 5 AU, a homogeneous magnetite fixture using explicit 1000 m/s
reference burns each way returns 1988.710239 kg at cost/revenue 656.124242.
Retaining its as-is alternative returns 2821.290144 kg at 593.020922, with
launch 17280.833/17191.508 kg both below the actual Falcon 9 reusable 17400 kg
capacity. All input rates, yields, prices and constraints stay fixed.

At 1100 kg direct RTG cargo, the original return trace rejects 5330.595 W
at calc.py L6474 under the 5000 W limit. As-is needs 3513.575 W and remains
feasible. All 13 gains persist with excavation charged: the 5 AU pair is
684.740246 versus 603.831611 and the RTG pair 5430.983 W rejected versus
3613.963 W accepted. Eleven non-improving/tied cases retain the original
choice, including exact legacy/coarse/already-as-is cases and a profit-
objective control. Lower cost/revenue is not a claim of improved profit;
all examples remain unprofitable. The compositions and reference burns
are controlled fixtures, not observed asteroid trajectories or incidence.
`extracted_data/r344_flown_refinery_route_preselection.csv`.

`economicspace_raw_excavation_energy_record_2026` reads the same consumer.
The spacecost Drilling / excavation energy row is 200 "Watt-hours per kg
of regolith extracted" (operations.py L676-688), separate from beneficiation.
MODEL.md L553-559 says these energies size the flown power system. Both
the sizing and settlement code instead initialize process power to 0 and
call `processing_power_w` only "if beneficiate or isru" (calc.py L6385-6391,
L6700-6706). Raw non-ISRU feed is mined and timed but pays neither extraction
power nor its plant mass/cost; refinery/water draws are separate additions.

Fourteen excavation cases run original, exact repeat and the two-gate
diagnostic: 42 full runs. Ten change; zero-rate, zero-feed, beneficiation-on
and ISRU-on controls remain exact. At 1000 kg raw Earth cargo and 0.25 yr
stay, with no other process draw, the original has 0 W and 0 kg power plant.
The adopted 200 Wh/kg implies 91.2616929044 W, with 13.4049386616 kg solar
hardware in the same solver. Launch mass 4425.967992 becomes 4444.233191 kg;
total cost 1662365366.256608 becomes 1662547118.001492 USD, with cargo and
duration fixed. In raw LEO cases, that draw adds to the existing 456.308465 W
refinery load. Two full `evaluate_asteroid` cases with use_beneficiation=True
reproduce the omission in the raw alternative the normal search selects.
The 200 Wh/kg magnitude remains the separate `rc-027` question.
`extracted_data/r344_raw_excavation_energy.csv`.

Verdict: `rc-279`, keep sale-route alternatives through mission evaluation;
`rc-280`, apply excavation energy to all extracted feed. Original repeats
match exactly, and all feasible recorded results satisfy body, launch,
throughput, duration, volume and RTG limits. Nineteen local source/input
blobs match pinned GitHub metadata; all four live main comparisons are
identical. No full-catalog ranking or population effect is measured.


## R370 - Lunar mineral-beneficiation testbed energy versus the unsourced asteroid estimate (rc-291; 2026-11-08)

`kulkarni_2024_lunar_regolith_beneficiation_testbed_energy`, Kulkarni et al.,
*Optimizing lunar regolith beneficiation for ilmenite enrichment*, Frontiers in
Space Technologies 4:1328341. Table 4 (PDF p.8) gives Phase C yield 1.29 wt%,
recovery 31.93 wt% and grade 11.95 wt% at 14 kV; the article defines yield as
ilmenite mass in the output per input mass (Table 2, PDF p.3). Its conclusion
(PDF p.10) reports 61 Wh for processing 300 g “for the entire testbed.”
Those values imply 32.38 g of concentrate (0.300 kg × 0.0129 / 0.1195) and
1,883.6 Wh/kg of concentrate, 3.77 times spacecost's 500 Wh/kg center for
“Beneficiation / on-site processing energy.” The model row describes a target
of about 50% purity; the testbed reached 11.95 wt% ilmenite. It is also a
small-scale TRL 4 system: the authors say it has scalability limitations and
expect residual losses to fall with throughput (Discussion, PDF p.9). Thus this
measurement is a direct mineral-beneficiation benchmark but does not by itself
set the asteroid-scale 50%-purity value. rc-291 remains open to re-estimate the
center/range or document a quantified scale and purity adjustment.
`extracted_data/r370_kulkarni_beneficiation_energy.csv`.


## R371 - Integrated lunar excavation and beneficiation energy (rc-027; 2026-11-08)

Arumugam et al., “Integrated robotic feedstock preparation for lunar oxygen
production: system-level efficiency and design implications from analogue
trials,” *npj Space Exploration* 2:33 (2026), DOI
10.1038/s44453-026-00051-y. The full article is available on the publisher
record and its CC BY 4.0 statement is explicit. Table 1 (PDF p.3) reports a
2.5 h, 37-cycle LUNA trial: 10.8 kg excavated, 10.0 kg delivered to the
beneficiator, 2.1 kg under 100 μm, and 265 Wh total system energy. The paper
separates excavation energy intensity (24.5 Wh/kg excavated, including rover
mobility), target-fraction energy intensity (126.2 Wh/kg target product), and
specific beneficiation energy (14.3 Wh/kg target fraction). The 24.5 Wh/kg
integrated excavation figure is below the current spacecost `Drilling /
excavation energy` row's 50 Wh/kg low bound, but it is a 1-g lunar simulant
campaign with different tool, gravity, and included-mobility boundaries; it
does not directly set asteroid energy. It independently strengthens rc-027's
case to lower or re-scope the row, while the asteroid-specific magnitude
remains unresolved. Extracted data:
`extracted_data/r371_integrated_lunar_excavation_energy.csv`.


## R383 — NASA oxygen-production plant mass estimates

Sanders, Kleinhenz & Linne, *NASA Plans for In Situ Resource Utilization (ISRU) Development, Demonstration, and Implementation* (COSPAR presentation, 14 July 2022), slide 11, table “Oxygen from Regolith Plant Mass and Power Estimates.” The four O2 production-rate cases are 1, 3.5, 7, and 10.5 t/year; the corresponding “Oxygen Production Plant” masses are 946, 1,679, 3,459, and 4,142 kg. The presentation says these results were scaled from a COMPASS study. Normalized product rates are 1.057, 2.085, 2.024, and 2.535 kg O2/year per kg of the named plant row. Source: `nasa_sanders_2022_isru_oxygen_plant_mass_estimates`.

These conceptual lunar oxygen-production cases are materially below spacecost’s `In-space processing plant throughput` point of 100 kg processed/year/kg plant (range 20–500), but they report O2 product rather than raw feed processed and the table separates supporting-system and ISRU-system masses. They therefore motivate a basis and boundary review; they do not directly establish an asteroid mineral-refinery throughput or a replacement value. rc-301 asks for that reconciliation. Extracted data: `extracted_data/r383_nasa_isru_oxygen_plant_mass_estimates.csv`.


## R384 — Lunar LUNOX raw-feed plant scales

Borowski et al., “Robust Exploration and Commercial Missions to the Moon Using LANTR Propulsion and In-Situ Propellants Derived from Lunar Polar Ice Deposits” (NASA Glenn-hosted paper, NTRS 20180000405), Table 7 (printed p.30) and adjacent discussion. The table gives 1,000 t/year LUNOX plants: ilmenite feed at 3.3×10^5 t regolith/year with 244 t plant mass (mining, beneficiation, processing and power); iron-rich volcanic-glass feed at 2.5×10^4 t/year with 105 t plant mass (mining, processing and power). Those table values normalize to about 1,352 and 238 kg raw feed/year/kg plant. The discussion states the volcanic-glass case includes mining and processing equipment and a fission-reactor power source. Source: `borowski_ryan_burke_mccurdy_fittje_2018_lunox_scale`.

These are conceptual lunar oxygen-production plants, not asteroid mineral refineries, but unlike the NASA 2022 cases in R383 they report raw regolith feed and plant mass. Their normalized rates exceed spacecost’s `In-space processing plant throughput` point of 100 kg/year/kg by factors of about 2.4 and 13.5. Thus R383’s low product-per-plant-mass comparison does not contradict the raw-feed estimate. rc-301 is withdrawn; the original mineral-refinery rate remains an estimate without an asteroid-specific plant design. Extracted data: `extracted_data/r384_lunox_raw_feed_throughput.csv`.


## R390 — Liu et al. 2026 laser-mining abstract (2026-11-08)

`liu_et_al_2026_asteroid_laser_mining_cryogenic_vacuum`, publisher abstract: continuous-wave fiber-laser tests at 300, 600 and 900 W for 30 s were run on C- and S-type simulants at 10^-2 Pa and 253 K. The abstract reports Fe-Ni content increasing from 16.7% in original simulant to 69.6% in ejected fine particles. It gives no sample mass loss, total ejected mass or energy normalized by output mass; the full article was not pulled. No mass-specific processing-energy value can be extracted from the abstract. Extracted: `extracted_data/r390_liu_laser_mining_abstract.csv`.

## R391 — Whole-system regolith excavation rate analogue (2026-11-08)

Mueller et al., *Design of an Excavation Robot: Regolith Advanced Surface Systems Operations Robot (RASSOR) 2.0* (NASA NTRS 20210011366), report a 66 kg system and “a minimum of 2.7 metric tons of regolith per day” (abstract, p. 1). Its Concept of Operations specifies 16 hours of mining and eight hours of recharge per 24-hour Earth day, and assumes 1,000,000 kg regolith/year for a 10,000 kg/year oxygen case at 1% yield (p. 2). The published ratio is about 40.91 kg/day/kg system mass, roughly 409 times economicspace’s 0.10 kg/day/kg rig assumption. Its published 0.38 kg system per (kg/hour) rate metric is consistent within rounding with 2.7 t/day over 16 mining hours and 66 kg system mass.

This is a conceptual Mars/Lunar regolith design whose basic simulant-excavation function was demonstrated in a lab-scale gravity-offload test (abstract, p. 1); its annual production case is not a sustained flight result. It is a whole-system throughput comparator, unlike the tool-only MoonBot test or IPEx’s uncadenced mass target. Open `rc-309` to review whether the asteroid mining-rate coefficient should remain this far below a planetary regolith system analogue, with target-body gravity, material strength, duty cycle and maturity kept explicit. The comparison does not establish a replacement value. Extracted: `extracted_data/r391_rassor2_system_throughput.csv`.


## R420 — RAP separates mining-system development from production cost (2026-11-09)

Cohen et al., NASA NIAC Robotic Asteroid Prospector Phase I report, §6.3 and Table 6.1, presents a first-approximation 2013-dollar cost model. It states spacecraft development is “exclusive of the costs of the mining equipment” and estimates separate $1,000M development for mining technology and $300M recurring production cost for first-spacecraft mining equipment; the table lists $2,500M total NRE, including distinct $500M spacecraft, $1,000M propulsion and $1,000M mining-technology components. The report describes the mining-system estimate as highly uncertain and does not supply the equipment mass needed to normalize its recurring cost to dollars per kilogram. In the current economicspace evaluator, program NRE includes only spacecraft development and autonomous-control NRE; recurring mining hardware is charged separately by mass. rc-330 asks whether mining-equipment development NRE is intentionally inside either existing NRE input or is omitted. No direct value replacement is supported. `extracted_data/r420_rap_mining_system_cost_scope.csv`.

## R431 — Integrated beneficiation energy boundary cross-check (2026-11-09)

Arumugam et al., *Integrated robotic feedstock preparation for lunar oxygen production* (npj Space Exploration 2:33, 2026), Table 1 (p. 3), reports specific beneficiation energy of 14.3 Wh/kg of target fraction and 126.2 Wh/kg target fraction for the integrated excavation-and-feed-preparation system. The target fraction is screened material below 100 μm; the study reports a 21% beneficiation yield ratio, not a mineral grade or refined-purity assay. Spacecost's `Beneficiation / on-site processing energy` estimate is 500 Wh/kg refined product, with a note targeting approximately 50% purity. The numerical difference (14.3 vs 500 Wh/kg) therefore compares different product definitions and a 1-g lunar simulant field trial with an asteroid-scale estimate; it is a boundary/scaling signal, not a replacement value. rc-291 remains open for an explicit scale and purity conversion. Extracted: `extracted_data/r431_integrated_beneficiation_energy_crosscheck.csv`.


## R458 — Current economicspace cumulative-resource-budget flag

At economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, `CalcConfig.model_body_resource_budget` defaults to `False` (modules/calc.py:694), and the module-level consumer constructs `CONFIG = CalcConfig()` without overriding it (line 1468). With the flag enabled, the programme code computes `max_n = body_kg / (feed_kg + isru_feed_kg)` (line 7838) and tries smaller loads for over-budget rungs, but its filter explicitly retains every one-mission rung (`p[0] == 1`) even when `max_n < 1` (lines 7849-7852). A separate per-mission feed-budget flag also defaults off. Thus the current default still permits cumulative over-extraction, and the opt-in programme guard does not itself enforce the body-mass limit when one mission's feed exceeds the body. `rc-245` remains open; this check identifies a single-mission edge case in addition to the default-off programme behavior. Extracted: `extracted_data/r458_current_resource_budget_flag.csv`.


## R462 — Current raw-excavation power option

At economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, `CalcConfig.model_raw_excavation_power` defaults to `False` (modules/calc.py:664), and the module-level consumer constructs `CONFIG = CalcConfig()` without an override (line 1468). In the default sizing and settlement paths, `processing_power_w` is called only when beneficiation or ISRU is active (lines 6877-6883 and 7229-7234), so raw non-ISRU excavation feed does not size an array for the configured drilling/excavation energy. With the flag enabled, both calls include raw feed (`trial_feed + new_isru_feed` during sizing; `feed_kg + isru_feed_kg` at settlement), with beneficiation payload energy still conditional on concentration. The correction is opt-in; it does not independently re-anchor the 200 Wh/kg energy input tracked in `rc-027`. `rc-280` remains open for the default path and full branch/control review. Extracted: `extracted_data/r462_current_raw_excavation_power_flag.csv`.


## R468 — Current concentration search past purity option

At economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, `CalcConfig.search_concentration_past_purity` defaults to `False` (modules/calc.py:711), and the module consumer uses the default `CONFIG = CalcConfig()` (line 1468). When enabled, `_past_purity` runs only when `market_model` resolves to `capacity_cap`; it adds a geometric set of ratios above `saturation_ratio` through `max_concentration_ratio` and refines around its best added ratio (lines 8650-8677). It runs after the ordinary concentration grid and its refinement, preserving those earlier candidates; the `r_max <= 1` path also invokes it (lines 8679-8680, 8719). The release note reports that 24 of 53 sampled rows changed with the flag on, while the ample-market, unbounded and beneficiation-off controls did not move. This materially addresses the omitted-region mechanism, but only as an opt-in approximation: the default still leaves `rc-265` active, the extension samples a finite grid, and the sample does not establish population-wide coverage or prove that all beneficial ratios are found. `rc-265` remains open. Extracted: `extracted_data/r468_concentration_past_purity_flag.csv`.


## R472 — Current flown-refinery route preselection

At spacevalue main commit `a13e378efece102d3724ada18d3810a62f29432f`, `_phase_terms` returns exactly one `(gross price, refining energy)` pair per phase. With a refinery route available, it chooses as-is when `as_is_net` is missing or at least as high as the yield-derived `net`; otherwise it returns refined gross value and energy (spacevalue/cargo.py:482-511). `asteroid_refinery` builds one phase-energy map from those chosen terms (lines 514-559). Current economicspace calls `asteroid_refinery` once for the asteroid and passes that single configuration into both trial and settled hold-refining paths (modules/calc.py:6898, 7142, 9074); no mission-level as-is/refined alternatives are retained. This recheck confirms `rc-279`'s preselection mechanism remains in current main. No new numeric cases were run, so the R344 controlled outcomes remain the recorded quantitative evidence. `rc-279` remains open. Extracted: `extracted_data/r472_current_flown_refinery_route_selection.csv`.


## R473 — Integrated excavation-energy denominator cross-check

At spacecost main commit `19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/operational_costs.csv` still gives `Drilling / excavation energy` as 200 Wh/kg with a 50–500 Wh/kg range, per kg of regolith extracted. Arumugam et al., Table 1 (PDF p. 3), labels the measured row “Excavation energy intensity” at 24.5 Wh/kg, below that range's lower endpoint; the same table reports “Total system energy” of 265 Wh and 10.8 kg excavated. The table arithmetic checks: 265/10.8 = 24.54 Wh/kg. It also reports “Beneficiation energy” of 30 Wh and 2.1 kg target fraction, giving 14.29 Wh/kg, which matches its 14.3 Wh/kg specific-beneficiation value. The paper states (p. 2) that “Beneficiation consumed 11% of total system energy, while excavation and rover mobility accounted for the large remainder.” Thus 24.5 Wh/kg is an integrated-system-energy metric normalized by excavated mass, not an isolated excavation-energy measurement; the 1-g LUNA trial is an architecture-specific analogue. It raises a real scope question for the 50 Wh/kg lower bound but does not justify a direct asteroid-row substitution. `rc-027` remains open pending a matched excavation-only boundary and scale basis. Extracted: `extracted_data/r473_excavation_energy_boundary_comparison.csv`.


## R474 — End-to-end lunar oxygen model omits separator energy

At spacecost main commit `19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `Beneficiation / on-site processing energy` remains 500 Wh/kg refined product (range 100–2,000), with a note targeting approximately 50% purity. Leger et al., *PNAS* 122(8), e2306146122, model an electrostatic ilmenite-beneficiation route using sixfold enrichment, 50.5% ilmenite recovery, and a maximum 99 wt% concentrate grade (Methods, PDF p. 9). The authors state that electrostatic-separation energy “is negligible relative to other process units in the model and is therefore neglected”; they also exclude particle-size separation and crushing (Methods, p. 9). Their Table 2 gives 0.13 kWh/kg LOX for the beneficiation module (PDF p. 6), but Eq. 11 shows this module energy as lifting and gangue-transport handling, not measured separator energy (PDF p. 9). The numerator and denominator therefore do not match the spacecost row's physical separation energy per kg refined product. This source provides a grade/recovery scenario near the row's ~50% target but no direct process-energy value. `rc-291` remains open: current 500 Wh/kg still lacks a matched scale-and-grade measurement or a quantified scaling bridge. Extracted: `extracted_data/r474_pnas_beneficiation_energy_boundary.csv`.


## R500 — Hydrogen direct-reduction energy comparator (2026-11-09)

At spacevalue main commit `a13e378efece102d3724ada18d3810a62f29432f`, `spacevalue/catalog.py` `IN_SPACE_PROCESSING_KWH_PER_KG` assigns 5.0 kWh/kg to iron, nickel, cobalt, copper, nickel-iron and awaruite; its comment analogizes this to terrestrial electric-arc/direct-reduction steelmaking and electrowinning without citing a source. Vogl, Åhman & Nilsson report hydrogen direct reduction requiring “3.48 MWh electricity per tonne of liquid steel” (abstract, p. 736), equivalent to 3.48 kWh/kg liquid steel, chiefly for electrolyser hydrogen production. This is a boundary-specific terrestrial route and a useful comparator, not an asteroid refining measurement or a direct validation of the code’s feedstock-based allowance, which also contemplates melting and forming. `rc-366` records the missing citation and boundary qualification; no numeric replacement is supported. Extracted: `extracted_data/r500_vogl_hydrogen_dri_steel_energy.csv`.


## R504 — Mining-rig mass scale comparator (2026-11-09)

At economicspace `modules/calc.py` `MiningConfig.mining_hardware_kg` remains 2,000 kg and is described as the mining rig, communications and structure that stay at the asteroid; the domain opening records no stated basis for that mass (economicspace main snapshot `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`). Mueller et al. report a 66 kg RASSOR 2.0 system and “a minimum of 2.7 metric tons of regolith per day” (abstract, p. 1). This is a lunar/Martian regolith excavator concept, not an asteroid miner with the same anchoring, communications or processing scope; it does not validate or replace 2,000 kg. `rc-370` asks that the mass and included subsystems be sourced or kept explicitly as an engineering scenario. Existing extraction: `extracted_data/r391_rassor2_system_throughput.csv`.


## R505 — Whole-mission duration comparator for the mining-stay cap (2026-11-09)

At economicspace `modules/calc.py` `MiningConfig.max_mining_duration_yr` is 3.0 years; its comment calls this a hard ceiling on time spent at the asteroid and says it also limits operating cost and WACC accumulation. Cohen et al.’s NASA NIAC Robotic Asteroid Prospector system requirements state that the spacecraft should be “capable of operating for mission durations lasting between one and five years” (§5.1, report p. 65). The requirement is for the complete mission concept, whose ConOps includes outbound and return transfers; it does not isolate the asteroid stay. This provides a duration-scale comparator but does not support a three-year stay limit. `rc-371` records the citation and scope gap; no numeric change is inferred. Extracted: `extracted_data/r505_rap_mission_duration_requirement.csv`.


## R510 — Asteroid sample-return spacecraft dry-mass comparator (2026-11-09)

Bierhaus et al. report that the OSIRIS-REx spacecraft’s approximately 2,100 kg wet launch mass includes “∼880 kg” dry spacecraft mass (§3.1.1, PDF p. 6). The article describes a whole asteroid sample-return spacecraft with science, propulsion, power, thermal-control, telecommunications and sample-acquisition/return systems (§3.1). At economicspace `modules/calc.py`, `MiningConfig.return_vehicle_dry_kg` remains a 500 kg floor for irreducible vehicle hardware, with payload-scaled structure added separately. OSIRIS-REx is a capability-rich mission comparator, not a matched cargo carrier or a direct lower bound for that floor. **rc-376 remains open** pending a cargo-return architecture or subsystem mass budget; no numeric replacement is supported. Extracted: `extracted_data/r510_bierhaus_osirisrex_dry_mass.csv`.


## R517 — Lunar beneficiation plant throughput comparator (2026-11-10)

NASA’s LuSTR 2021 overview chart for Han’s lunar regolith beneficiation project (Development Objectives, p. 1; NASA page dated 2022-03-15) sets an expected final-brassboard throughput of ≥3 kg/h and mass of <35 kg for electrostatic sieving and magnetic separation of lunar simulant, targeting >70 wt% anorthite in 20–200 μm grains. The NASA page says the subsystems would be tested separately before integration, so these are design objectives rather than an integrated system’s measured annual performance. Continuous nameplate annualization is >750.9 kg/year/kg plant at 8,760 h/year; at the conservative 35 kg and 3 kg/h limits, the current spacecost point of 100 corresponds to <1,166.7 operating h/year and the 500 upper bound to <5,833.3 h/year. This is a relevant lunar beneficiation comparator, not an asteroid refinery or a duty-cycle measurement; it makes the annual operating basis and the still-unsourced 1,000× terrestrial analogy reviewable but does not establish a replacement value. rc-383 records that citation and boundary review. `extracted_data/r517_lustr_beneficiation_throughput_comparator.csv`.
## R522 — PGM concentrator feed-to-concentrate ratio comparator (2026-11-10)

The registered source `sibanye_stillwater_2026_rustenburg_technical_report`, the SEC-filed Sibanye-Stillwater Rustenburg Technical Report Summary, states that “The 2021 to 2025 data presented reflect the actual annual performance” (printed p. 154, §14.1.1.2) and Table 57 gives annual total feed and concentrate production for 2021–2025. Dividing feed by concentrate gives 62.44:1, 61.49:1, 59.94:1, 59.51:1 and 61.64:1, respectively.

Current economicspace `CalcConfig.max_concentration_ratio` is 50:1. Its comment says terrestrial PGM mills run at 100:1–1000:1 and calls 50:1 deliberately conservative, but the cited plant’s measured annual ratios are below that stated range. At 50:1, concentrate mass may reach 2.0% of feed; the report’s five actual annual mass pulls are about 1.60–1.68%. This is an operating comparator for one conventional PGM concentrator, not an asteroid mineral-separation result or a like-for-like mineral-purity target. `rc-388` records the unsupported range statement and asks for a scoped citation; no cap change is inferred. Extracted: `extracted_data/r522_rustenburg_pgm_concentrator_mass_ratio.csv`.



## R523 — FFC-Cambridge titanium extraction energy comparator (2026-11-10)

`hu_dolganov_etal_2018_ffc_titanium_energy`: Hu et al. report “21.5 kWh/kg” for optimized FFC-Cambridge TiO2 electro-reduction yielding titanium at 1900 ppm oxygen and 32.3% current efficiency (JOM 70(2), p. 133); an inert-anode configuration is reported at about 17 kWh/kg and about 40% current efficiency (pp. 134–135). The 12.5 kWh/kg figure is stated as a projected target. These are laboratory extraction results; they do not establish asteroid ore preparation, beneficiation, or downstream melting/forming energy.

Upstream: spacevalue `spacevalue/catalog.py` `IN_SPACE_PROCESSING_KWH_PER_KG["titanium"]` = 20 kWh/kg; comment identifies FFC-Cambridge electrolysis but gives no supporting source or boundary. Verdict: citation/scope gap; the 20 kWh/kg allowance is consistent in scale with published FFC extraction results, but exact value and full processing boundary remain unvalidated. No numeric change proposed. `rc-389`. Extracted: `extracted_data/r523_ffc_titanium_electrolysis_energy.csv`.


## R524 — Lunar-regolith sintering energy comparator (2026-11-10)

`liu_li_etal_2025_lunar_regolith_microwave_sintering_energy`: Liu et al. report microwave sintering specific energy of 69 MJ/kg for mare simulant CLRS-1 and 98 MJ/kg for highlands simulant SC-080 (Journal of the European Ceramic Society 45(3), article 117047, Abstract). Converted values are 19.17 and 27.22 kWh/kg. The samples were consolidated for construction material using a domestic microwave and ceramic-fiber microwave kiln.

Upstream: spacevalue `spacevalue/catalog.py` `IN_SPACE_PROCESSING_KWH_PER_KG["silicates"]` and mapped silicate phases = 1 kWh/kg; the code comment says sintering for shielding blocks or print feedstock but gives no source or defined route. Verdict: large comparator gap, not a direct contradiction; lunar microwave construction processing does not establish asteroid refining energy. Keep 1 kWh/kg only as a scoped low-energy scenario pending a like-route basis. `rc-390`. Extracted: `extracted_data/r524_lunar_regolith_sintering_energy_comparator.csv`.


## R528 — Phosphorus processing-energy citation and boundary (2026-11-10)

`matos_etal_2021_jrc_elemental_phosphorus_energy`: the European Commission JRC report describes elemental P₄ production from phosphate rock (apatite), coke and silica in an electric furnace at 1500–1700 °C, reporting “up to 14 MWh per tonne of P₄” (§7.1, p. 30). This converts to 14 kWh/kg P₄. The report’s page 2 states reuse is authorized under CC BY 4.0.

Upstream: spacevalue `spacevalue/catalog.py` `IN_SPACE_PROCESSING_KWH_PER_KG["phosphorus"]` = 8 kWh/kg, without a source or defined product/feedstock boundary. Verdict: the JRC industrial thermal-process figure is a relevant comparator, but does not directly validate or replace the asteroid processing allowance. Keep 8 kWh/kg as a scoped engineering scenario until its process boundary is defined and supported by a like-boundary calculation. `rc-394`. Extracted: `extracted_data/r528_jrc_phosphorus_production_energy.csv`.


## R529 — Carbonate processing-energy source and boundary (2026-11-10)

`mcmillan_etal_2016_nrel_lime_calcination_energy`: NREL/INL Appendix N reports a theoretical lime-kiln minimum of 3.18 GJ/t CaO assuming complete limestone conversion (p. 162); its approximate 100:56 CaCO₃-to-CaO mass relation (p. 165) converts this to 0.4947 kWh/kg CaCO₃, computed here. The report separately lists kiln net heat of 3,600–7,500 kJ/kg lime and electricity of 10–45 kWh/t by kiln type (Table N-1, p. 161).

Upstream: spacevalue `spacevalue/catalog.py` `IN_SPACE_PROCESSING_KWH_PER_KG["carbonates"]` = 1 kWh/kg; its comment says carbonate calcination is approximately 0.5 kWh/kg CaCO₃ in a lime kiln but names no source or energy boundary. Verdict: the comment’s 0.5 figure matches the theoretical-minimum conversion, while actual kiln heat and electricity are distinct. These industrial values do not directly establish an asteroid-carbonate process allowance. Retain 1 kWh/kg only as an engineering scenario pending a defined process boundary. `rc-395`. Extracted: `extracted_data/r529_nrel_lime_calcination_energy.csv`.
## R562 — economicspace comparator comments applied to excavation candidates (2026-11-10)

At economicspace@e2ad48767b0e81489031b724417b1a03e6dfc1fb, RASSOR 2.0 is identified as a planetary-excavator comparator while 2,000 kg remains a scenario (rc-370); RAP mission duration is distinguished from asteroid stay (rc-371); OSIRIS-REx dry mass is distinguished from a 500 kg floor (rc-376); and Rustenburg plant ratio replaces the unsupported PGM ratio generalization with scope limits (rc-388). These citation/scope requests are applied without changing values. The 0.10 mining-rate review remains open: the RASSOR comparator is not a matched asteroid throughput measurement (rc-309).
## R563 — Default per-mission mining cap remains an unmeasured bound (2026-11-10)

At economicspace@e2ad48767b0e81489031b724417b1a03e6dfc1fb, `verification_sheet.py --check` flags I12 `max_mining_fraction=1.0` as needing backing; the configured 100% is a model cap on per-mission extraction, not a measured accessible fraction for a body. **rc-245** remains open and distinguishes this per-mission cap from cumulative programme depletion.


## R569 — NASA lunar-water purification boundary (2026-11-10)

`paz_2023_lunar_water_propellant_processing_assessment`: NASA’s assessment says water from a lunar permanently shadowed region must be separated and purified before electrolysis (PDF p. 1). It identifies freeze distillation and sub-micronic filtration; PEM electrolysis requires ultrapure/deionized water, while SOE does not, and system comparisons should include purification and gas drying (PDF pp. 1–2). The two-page assessment gives no specific energy per kilogram.

Upstream: spacevalue `spacevalue/catalog.py` sets `IN_SPACE_PROCESSING_KWH_PER_KG["water"]` to 0.5 kWh/kg and describes “filtration and phase change only,” without a cited calculation. Verdict: process-boundary citation gap; NASA’s lunar assessment clarifies purification steps but supplies no numerical comparator for this allowance. Keep the value pending a sourced calculation with a defined feed/product boundary; no replacement inferred. **rc-434**. Extracted: `extracted_data/r569_nasa_lunar_water_purification_boundary.csv`.

## R573 — Carbon and organic in-space processing-energy allowances (2026-11-10)

`spacevalue_carbon_organic_processing_energy_current_2026`: at spacevalue main `f836611f15dbb0ef511fe134bd5ac8192e3bea16`, `IN_SPACE_PROCESSING_KWH_PER_KG` assigns 2.0 kWh/kg to carbon and organics. The table describes energy to turn raw feedstock into a usable product; the adjacent comment names “pyrolysis / compounding” for carbon but gives no route-specific basis for organics. `CITATIONS.md` lists comparators for water, metals, silicates, phosphorus, and carbonates, but not these two entries. The coefficient feeds `in_space_processing_cost_usd_per_kg`, is subtracted from the in-space price, and is exported as `refining_kwh_per_kg` for the flown-refinery path consumed by `cargo.py`. Verdict: a live model input with missing source/calculation and feed/product boundaries. Keep both numbers as explicitly labeled engineering scenarios pending like-boundary evidence; no replacement inferred. **rc-437**. Extracted: `extracted_data/r573_carbon_organic_processing_energy.csv`.

## R574 — Sulfide processing-energy transfer (2026-11-10)

`spacevalue_sulfide_processing_energy_code_current_2026`: spacevalue `catalog.py` assigns 4.0 kWh/kg to troilite and transfers the same value to pyrrhotite, pentlandite, niningerite, daubreelite, and oldhamite. The v1.12.0 comment says roasting frees sulfur and the metal pays its own, but gives no energy calculation, cited source, or product boundary. The map defines the measure per kg of raw feedstock; `in_space_processing_cost_usd_per_kg` and the exported `refining_kwh_per_kg` use it in value and cargo calculations. Verdict: a live six-entry model input whose common value and process scope lack a source. Request a sulfide-specific calculation or like-boundary evidence; keep the value as a labeled estimate pending review. No replacement inferred. **rc-438**. Extracted: `extracted_data/r574_sulfide_processing_energy.csv`.

## R575 — Ammonia and carbon-dioxide processing-energy transfer (2026-11-10)

`spacevalue_volatile_processing_energy_code_current_2026`: `IN_SPACE_PROCESSING_KWH_PER_KG` assigns 0.5 kWh/kg to ammonia and carbon dioxide. The nearby comment proposes “fractional distillation of the ice, like water,” without specifying a commodity-specific route, calculation, or feed/product boundary. The coefficients enter in-space price deductions and are exported for the flown-refinery cargo path. The separate water assessment recorded under rc-434 identifies purification steps but reports no energy figure for water, ammonia, or CO₂. Verdict: analogy is documented, but the two values have no like-boundary process-energy basis. Retain as engineering scenarios pending evidence; no replacement inferred. **rc-439**. Extracted: `extracted_data/r575_volatile_processing_energy.csv`.

## R576 — Oxide processing-energy transfer (2026-11-10)

`spacevalue_oxide_processing_energy_code_current_2026`: spacevalue assigns 7.0 kWh/kg raw feedstock to magnetite and applies the same value to chromite and ilmenite as oxide-reduction analogies. The coefficient feeds in-space processing-cost and cargo/refinery calculations. NASA-CR-171982-VOL-1, Fig. 2-3 (printed p. 20), reports 7,639 kWh thermal plus 43,200 kWh electrical for producing 10 MT O2 from 662.2 MT lunar mare through hydrogen reduction of ilmenite. NASA Tech Brief MFS-32933-1 reports 30–60 MJ/kg O for a distinct high-temperature regolith oxygen-extraction concept. These comparators are on oxygen output and use different feed/process boundaries; neither establishes the catalog’s per-kg raw-feed allowance. Verdict: request oxide-specific route, yield, and energy boundaries; retain 7.0 only as a scenario pending like-boundary evidence. No replacement inferred. **rc-440**. Extracted: `extracted_data/r576_oxide_processing_energy_comparators.csv`.

## R577 — Chromium processing-energy route and boundary (2026-11-11)

`spacevalue_chromium_processing_energy_code_current_2026`: spacevalue assigns 10.0 kWh/kg to chromium in its raw-feed processing-energy map and names “aluminothermic / electrolytic reduction,” without a calculation, yields, or route-specific feed/product boundary. The coefficient enters in-space processing-cost and cargo/refinery calculations. Bleiwas, USGS Open-File Report 2011–1253, Table 19 (printed p. 48), estimates 18,500 kWh/t (18.5 kWh/kg) for electrolysis to recover chromium metal; the footnote (printed p. 49) says this follows electric-furnace ferrochrome production and iron removal from chromium sulfate solution. This is a downstream electrolytic-step comparator, not a chromite-to-metal total or a like-boundary replacement for the raw-feed allowance. Verdict: request separate process-energy bases for aluminothermic and electrolytic routes, with feed/product and upstream-step boundaries; retain 10.0 kWh/kg as an engineering scenario pending matched evidence. No replacement inferred. **rc-441**. Extracted: `extracted_data/r577_chromium_processing_energy.csv`.

## R578 — Sulfur processing-energy boundary (2026-11-11)

`spacevalue_sulfur_processing_energy_code_current_2026`: spacevalue assigns 1.0 kWh/kg to sulfur in the map defined per kg of raw feedstock; its v1.11.0 comment says “melting and filtering” but gives no feed composition or calculation. Li et al., “Recovery of elemental sulfur from zinc concentrate direct leaching residue using atmospheric distillation,” *Journal of the Air & Waste Management Association* 64(1) (2014), pp. 95–103, reports a 1,200 kg batch at 460°C with 96.22% sulfur purity and recovery above 85%; the abstract gives 0.59 kWh/kg residue handled and 1.24 kWh/kg elemental sulfur produced (journal p. 95). These figures are close in scale to 1.0 but have different denominators and describe a water-rich industrial zinc residue processed by atmospheric distillation. Verdict: use as a route comparator and request an asteroid-feed composition, recovery yield, and raw-feed/product energy conversion before validating the coefficient; no replacement inferred. **rc-442**. Extracted: `extracted_data/r578_sulfur_processing_energy.csv`.

## R579 — Perovskite processing-energy transfer (2026-11-11)

`spacevalue_oxide_processing_energy_code_current_2026`: a recheck of the same spacevalue main revision found that `IN_SPACE_PROCESSING_KWH_PER_KG` also assigns 7.0 kWh/kg raw feedstock to perovskite; the v1.12.0 note describes it as “perovskite as the Ti ores.” This rate feeds the same in-space processing-cost and cargo/refinery calculations covered by rc-440. The value has no perovskite-specific process calculation or feed/product boundary. The existing candidate rc-440 has been expanded to include perovskite; the upstream code revision and SHA256 are unchanged. No replacement inferred. Extracted: `extracted_data/r576_oxide_processing_energy_comparators.csv`.

## R580 — Schreibersite processing-energy route (2026-11-11)

`spacevalue_schreibersite_processing_energy_code_current_2026`: spacevalue assigns 6.0 kWh/kg raw feedstock to schreibersite and describes its route as “as the alloy it is, plus leaching out the P,” without a calculation or a product boundary. Gull, Feng and Pasek, “Results of an Eight-Year Extraction of Phosphorus Minerals within the Seymchan Meteorite,” *Life* 12(10) (2022), article 1591, reports that actual schreibersite-bearing meteorite shavings corroded in ultrapure water over eight years and released soluble phosphate, phosphite, pyrophosphate and hypophosphate; the study also used Fe3P analogues (Abstract and §2, article pp. 1, 3). The experiment’s EDTA treatment and filtration were analytical recovery steps, and the paper reports no process-energy intensity. Verdict: request a route calculation defining whether the modeled product is alloy, dissolved P species, or purified phosphorus and accounting for leachant, separation, purification, and metal residue; retain 6.0 kWh/kg as an engineering scenario pending energy evidence. No replacement inferred. **rc-443**. Extracted: `extracted_data/r580_schreibersite_processing_energy.csv`.


## R588 — Cohenite processing-energy boundary (2026-11-11)

`spacevalue_cohenite_processing_energy_code_current_2026`: `catalog.py` assigns cohenite 5.0 kWh/kg in `IN_SPACE_PROCESSING_KWH_PER_KG` and defines the mineral as `(Fe,Ni)3C`. The nearby general metal note describes reduction, melting and forming and cites Vogl, Åhman & Nilsson’s 3.48 kWh/kg liquid-steel comparator; the v1.12.0 phase mapping treats cohenite with nickel-iron alloys but gives no carbide-specific route or carbon/product boundary. The liquid-steel comparator does not establish the energy to process cohenite-bearing feed into the modeled usable product. Verdict: retain 5.0 kWh/kg only as an engineering allowance pending a cohenite-matched process calculation or evidence; no replacement inferred. `rc-452`. Extracted: `extracted_data/r588_cohenite_processing_energy_boundary.csv`.


## R589 — Phosphate-phase and hibonite processing energy (2026-11-11)

`spacevalue_phosphate_grinding_energy_code_current_2026`: `catalog.py` assigns 1.0 kWh/kg to merrillite, chlorapatite, and hibonite. Its v1.12.0 note groups phosphates and hibonite as rock “by grinding,” then says phosphorus pays the separate 8.0 kWh/kg allowance when taken apart. Bleiwas, USGS OFR 2011–1253, Table 35 (printed p. 83), reports phosphate-rock crushing and grinding at 10–20 kWh/t without flotation and 20–30 kWh/t with flotation, equivalent to 0.010–0.030 kWh/kg. The upstream 1.0 kWh/kg equals 1,000 kWh/t; the industrial comparator is 33–100 times lower, but covers terrestrial phosphate-rock operations and does not establish processing energy for meteoritic merrillite/chlorapatite or asteroid conditions. It also does not cover hibonite, an aluminous oxide. Verdict: define the route and boundary separately for the phosphate phases and hibonite, and retain the 1.0 values as engineering scenarios until matched evidence or calculations are available; no replacement inferred. `rc-453`. Extracted: `extracted_data/r589_phosphate_phase_processing_energy.csv`.

## R619 — In-space refining-energy capital-cost lifetime and utilization (2026-11-11)

`spacevalue_inspace_energy_lifetime_utilization_code_current_2026`: `catalog.py` converts the $800/W power-system cost to a capital cost per kWh by assuming a 15-year life and 8,766 full-output hours each year: 131,490 Wh per installed watt and about $6.084/kWh. The formula applies no availability, degradation, or maintenance factor (`catalog.py`, lines 1140–1164 and 1237–1256). The resulting rate multiplies each listed material’s process-energy intensity in `in_space_processing_cost_usd_per_kg`. The refreshed economicspace verification sheet (2026-11-11) continues to flag the archived Stage 2 v1.12.0 refining-cost and refining-energy inputs as NEED BACKING, while noting that this run’s tables predate the live tables. Verdict: document the lifetime and useful-output assumptions behind the denominator, or label full utilization as a scenario with sensitivity; no replacement inferred. This is distinct from rc-374’s power-system price estimate, rc-383’s plant throughput, rc-347’s mining-rig service life, and rc-437–453’s material-specific process-energy values. **rc-482**. Extracted: `extracted_data/r619_inspace_energy_cost_lifetime_utilization.csv`.


## R628 - Maximum mining fraction and resource-assessment scope (2026-11-11)

- **economicspace_max_mining_fraction_current_2026**: Economicspace defaults `CalcConfig.max_mining_fraction` to 1.0 and passes asteroid mass times this fraction as the per-mission mineable-mass ceiling. Its comment says the whole body is on the table but also limits actual mission mass by throughput, return volume and the rocket equation. The verification worksheet flags input I12 as needing backing. **usgs_keszthelyi_etal_2017_asteroid_resource_assessment_feasibility**: USGS Open-File Report 2017-1041 describes a feasibility study for adapting resource-assessment methods to asteroids; its abstract says it is not a complete and robust uncertainty analysis and identifies further work needed for resource assessment. It provides no universal one-mission extraction fraction. Verdict: clarify 1.0 as a no-depletion upper-bound convention or provide a body- and mission-specific recoverable-resource basis. No replacement inferred. **rc-491**. Extracted: `extracted_data/r628_mining_fraction_scope.csv`.


## R658 — economicspace mining-rate, extraction-cap and NRE candidates rechecked (2026-11-12)

At economicspace main `c1a6333e6e50e0e3658d05e47128a94ce4f07831` (calc 1.45.0), `MiningConfig.mining_rate_kg_per_day_per_kg_rig` remains 0.10 kg/day/kg rig, with no sustained asteroid-mining flight heritage (**rc-309**). `CalcConfig.max_mining_fraction` remains 1.0; the now-default body-resource budget is a separate bound and does not establish this universal extraction ceiling (**rc-491**). The worked calculation still charges spacecraft development NRE and autonomous-mining-control NRE, with no distinct mining-hardware development NRE term (**rc-330**). All three candidates remain open. Existing extracts: `extracted_data/r391_rassor2_system_throughput.csv`; `extracted_data/r628_mining_fraction_scope.csv`; `extracted_data/r420_rap_mining_system_cost_scope.csv`; `21_mass_cost_estimating_relationships/extracted_data/r451_lunar_isru_development_production_cost_factors.csv`.


## R673 — In-space processing plant throughput recheck (2026-11-12)

At spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` (v0.17.1, data contract 1.26.1), `reference/operational_costs.csv` still stores 100 [20, 500] kg processed/year/kg plant. Its note says terrestrial smelters run at 1,000× their own mass per year and explicitly states “no source is given for this”; it describes 100× as a derating judgement. The registered NASA LuSTR source, **han_2022_lustr_lunar_regolith_beneficiation_system**, reports a ≥3 kg/h, <35 kg expected brassboard target, not measured integrated annual operation. This does not establish the terrestrial anchor or the asteroid plant duty cycle. **rc-383** remains open; no numeric replacement inferred. Existing extraction: `19_asteroid_excavation_beneficiation/extracted_data/r517_lustr_beneficiation_throughput_comparator.csv`.

## R721 — Bound-water liberation energy (2026-11-13)

At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` (v0.17.1, data contract 1.26.1), `reference/operational_costs.csv` row 32 stores Water liberation energy (bound water) = 2,500 Wh/kg [1,000, 5,000]. `spacecost/operations.py` lines 493–505 gives the same value and scenario arithmetic: 10 kg rock per kg water heated from about 200 K to 700 K at 800 J/kg·K (4.0 MJ), a serpentine dehydroxylation term of 250 kJ/kg rock (2.5 MJ), and 2.26 MJ/kg for “vaporise and capture.” These terms sum to 8.76 MJ/kg water (about 2,433 Wh/kg); the code note rounds this to about 8.8 MJ or 2,440 Wh/kg. It separately says the estimate “Matches the 1–3 kWh/kg range in the asteroid-ISRU literature (Colorado School of Mines / NASA ISRU studies)” without naming the comparison sources or their energy boundary. **spacecost_water_liberation_energy_code_current_2026**.

**weber_greer_1965_serpentine_heat_of_dehydration**: Weber and Greer measured 33 serpentine samples by differential thermal analysis at 15 psi water-vapor pressure. Table 2 (printed p. 457) reports mean heats of dehydration of “87.6, 98.9 and 135 cal/gm” for antigorite, chrysotile and lizardite, respectively, equivalent to about 366.5, 413.8 and 564.8 kJ/kg of sample. These polymorph-specific measurements are above Spacecost’s 250 kJ/kg-rock term; the natural sample composition and test conditions do not establish a direct asteroid-feed replacement.

**calla_fries_welch_2019_asteroid_mining_small_spacecraft_economic_feasibility**: Section 3.3.1 reports “2 Wh/g, 7 Wh/g and 17 Wh/g” from microwave experiments using Mars simulants. **ethridge_2016_leag_rf_water_extraction_poster** (unpaginated poster, p. 1): a Mars-simulant test with 10% water ice reports about 2 Wh-hr/g; a separate carbonaceous-chondrite simulant run recovered all 15 ml of added water plus “3 ml of water chemically bound in the clay and other minerals.” The poster assigns no separate energy rate to that bound-water portion, and Calla’s reported rate does not isolate it.

Verdict: the current point can be reconstructed from its stated scenario, but its serpentine reaction term is below the primary sample means and the cited 1–3 kWh/kg comparison is not scoped to isolated chemical-bound-water recovery. Reconcile the mineral phase, sample/feed mass basis, hydration fraction, initial and final temperatures, and whether the 2.26 MJ/kg vaporization term is already included in the reaction enthalpy for water vapor. Keep the current value and range as an explicit scenario pending a matched source; no numeric replacement inferred. **rc-588**. Extracted: `extracted_data/r721_water_liberation_energy_scope.csv`.
