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
