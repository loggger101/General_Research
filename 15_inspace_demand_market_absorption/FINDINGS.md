# Domain 15 — In-space demand & market absorption

Backings: spacevalue `spacevalue/catalog.py` `IN_SPACE_UTILITY`, `IN_SPACE_UTILITY_BY_DESTINATION`, `IN_SPACE_ANNUAL_DEMAND_KG` and `_DEMAND_SHARE_BY_CLASS`, and `modules/calc.py` `market_model`, `demand_elasticity` and `surplus_price_fraction`: how much of a delivered kilogram sells at each destination, and at what price.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last. Since R161 the engineering basis of each utility row is in domains 28-30; this domain keeps the market side.

## R75 - Domain opened (2026-09-27; no sources yet)

Upstream calls these "the single biggest soft assumption in the in-space case". Read at economicspace@1f470d4.

| cell | current value | upstream's stated basis |
|---|---|---|
| `mineral_value.py` `IN_SPACE_UTILITY` (base: LEO, cislunar, Mars orbit) | water 1.00; Fe, Ni, Co, Cu, nickel-iron, awaruite 0.70; magnetite 0.40; carbon 0.40; troilite 0.30; silicates 0.25; organics 0.20; everything else, precious metals included, 0.0 | "ENGINEERING JUDGEMENTS, NOT MEASUREMENTS" |
| `IN_SPACE_UTILITY_BY_DESTINATION` `geo` | water 0.80; metals 0.15; magnetite, troilite, silicates, carbon, organics 0.05 | a GEO depot refuels and services; nothing is manufactured there |
| `IN_SPACE_UTILITY_BY_DESTINATION` `lunar_surface` | water 0.60; iron, nickel-iron, awaruite 0.45; magnetite 0.25; silicates 0.03 | local FeO, ilmenite and polar ice compete |
| `IN_SPACE_UTILITY_BY_DESTINATION` `mars_surface` | water 0.25; iron, nickel-iron, awaruite 0.40; magnetite, troilite 0.15; organics 0.05; silicates, carbon 0.02 | ground ice, hydrated regolith and CO2 compete |
| `IN_SPACE_ANNUAL_DEMAND_KG` | leo 500,000; cislunar 100,000; mars_orbit 60,000; lunar_surface 50,000; geo 40,000; mars_surface 20,000 kg/yr | "JUDGEMENT, not measurement; no such market exists". geo = ~550 GEO satellites at ~70 kg/yr (no source); mars_orbit scaled from DRA 5.0 |
| `_DEMAND_SHARE_BY_CLASS` | propellant 0.55, structural 0.25, shielding 0.15, chemical 0.05, trace 0.0005 | "JUDGEMENT, like everything else in this block" |
| `calc.py` `market_model` | `capacity_cap`: constant price up to a kg/yr ceiling | modelling choice; `elasticity` is the alternative |
| `calc.py` `demand_elasticity` | 0.5 in P/P0 = (1 + Q/Q_market)^(-1/eps), only in `elasticity` mode | "0.5 is inelastic, which is right for precious metals: doubling world supply quarters the price"; no source |
| `calc.py` `surplus_price_fraction` | 0.5 of full price past a ceiling | "there is no market study behind it" |

**What a source has to supply:** what an in-space buyer would pay relative to launching the mass, by commodity and destination; quantified demand forecasts (depot propellant, GEO station-keeping, base consumables); the class mix of what an outpost imports; measured PGM and minor-metal demand elasticities and price responses to supply shocks.

**Also relevant, registered elsewhere:** `hein2020` (d22), `usgs_mineral_commodity_summaries_2026` (d06), `dra5_2009_human_exploration_of_mars` (d03).

**Boundary:** domain 6 holds prices and terrestrial production ceilings; this domain how much sells, at what discount, and the in-space ceilings.

## R80 - First sources (2026-09-28)

Four NTRS papers hosted, one companion registered:

- `lynch_2024_iss_logistics_mass_and_crew_time` (ICES-2024-132): "roughly 134 metric tons of logistics were delivered to the ISS" Oct-2017 to Dec-2023 (~21.5 t/yr); the leo ceiling of 500,000 kg/yr is ~23x that. The six SAO categories (consumables, maintenance, spares, outfitting, utilization, packaging) are the nearest analogue to the class shares; consumables dominate (SpX-24 2.8 of 3.1 t; Progress 80 3.1 of ~3.4 t; NG-17 1.5/1.0/0.85/~0.54 t). Figure 2's percentages are raster-only. `extracted_data/r80_iss_delivery_history_tableA1.csv`.
- `lynch_et_al_2023_logistics_rates_beyond_leo` (AIAA 2023-4617): 436.7 kg for 2 crew x 14 days on the lunar surface (non-regenerative ECLSS), ~31 kg per crew-day; water and gas with carriers 306.8 kg (~70%). The lunar_surface ceiling is ~4x that rate. `extracted_data/r80_lunar_surface_example_tables16-21.csv`.
- `chu_2006_goes_r_stationkeeping_momentum_management` (AAS 06-046): N-S ~50 m/s and E-W ~1.3 m/s per year (OCR prints "d s"; the daily figures confirm m/s); no propellant mass. At an assumed Isp 250 s that is ~85-113 kg/yr for a 4,000-5,000 kg spacecraft (+~3.7 m/s/yr with daily 25 Nms momentum dumps), the same order as upstream's ~70.
- `tiffin_friz_2022_space_superhighway_systems_analysis` (AIAA ASCEND 2022): cislunar tug-and-depot network; "A fairly conservative 9.2 km/s total DV to reach a 200 km circular LEO"; NRHO-to-LEO return "over 7 km/s"; each tug completes 2-3 missions in 10 years.
- `tiffin_friz_rosenthal_2022_space_superhighway_cost_analysis`: the cost companion, read in full in R134.

`extracted_data/r80_inspace_demand_key_numbers.csv`.

## R84 - First demand forecasts (2026-09-30)

- **Kornuta et al. 2019** (`kornuta_2019_commercial_lunar_propellant_architecture`, read from a co-author copy): near-term lunar propellant demand 450 t/yr (2,450 t water, $2.4B revenue), ~4.5x the cislunar row; early customer need ~1,640 t/yr; Moon-only scenario 100 t/yr (2x lunar_surface). Seven scenarios priced from $7,500/kg (Moon only) to $1,482/kg (all customers); electrolysis 4.41 kWh/kg; NPV positive in every multi-customer case at 10%; ~$4B initial investment at $35k/kg to the surface.
- **NG LunA-10** (`northrop_grumman_2024_luna10_lunar_rail_network`, T4, public release, hosted): $1.6B-$8B a year = 500-2,500 t/yr of cislunar propellant transport under a Starship price ladder ($300-600/kg LEO, ~$1,400-2,600/kg GEO, ~$2,000-3,800/kg Moon); 100 t per deep-space trip; GEO refuelling >300 t/yr.
- **Steinert et al. 2024** (`steinert_2024_lunar_depot_flight_cost_location`, CC BY, hosted): delivered cost of ilmenite-reduction oxygen to an NRHO depot; delta-v 2,414.35-2,985.65 m/s; base 23.9 t O2/yr.
- **Birch et al. 2026** (`birch_2026_roxy_pilot_plant_economics`, CC BY, hosted): a ~1 t O2/yr pilot plant reaches IRR up to +47.4% selling oxygen and metals: life support precedes propellant.

**rc-056** opened as a note recording these. `extracted_data/r84_cislunar_demand_forecasts_key_numbers.csv`.

## R567 — Demand-class shares lack a mass-allocation basis (2026-11-10)

Kornuta et al., “Commercial Lunar Propellant Architecture,” p. 3, reports near-term lunar-derived propellant demand of 450 MT/yr and customer-input demand of nearly 1,640 MT/yr. Northrop Grumman’s LunA-10 study, p. 5, gives 100 MT of projected construction mass and 500–2,500 MT/yr of propellant transport under its Starship price assumptions. At spacevalue main `f836611f15dbb0ef511fe134bd5ac8192e3bea16`, `_DEMAND_SHARE_BY_CLASS` assigns 0.55 to propellant, 0.25 to structural, 0.15 to shielding, 0.05 to chemical, and an additive 0.0005 to trace; the code calls these judgments and says the four bulk shares partition the import budget. The cited forecasts do not provide those destination-level class shares or the trace fraction. **rc-432** records the citation and scenario-allocation gap; no share change is inferred. Existing extraction: `extracted_data/r84_cislunar_demand_forecasts_key_numbers.csv`.

## R92 - Per-satellite GEO station-keeping mass (2026-10-01)

- **rawlin_majcher_1991_nssk_mass_comparisons_ep_systems** (TM-105153, hosted): 46 m/s/yr NSSK over 15 years, 1640 kg dry: chemical 459.3043 kg (30.62 kg/yr, Isp 310 s; Tsiolkovsky check within +0.18%), ion 69.28853 kg (4.62 kg/yr, Isp 2,467 s) at ~+210.8 kg dry mass.
- **ksc_pd_ed_1253_arcjet_thruster_design** (hosted): "N/S stationkeeping propellant mass comparison for a 12 Year, 1700 kg dry mass satellite": hydrazine 532 kg, biprop 373, resistojet 373, arcjet 207 (+~20 kg dry) = 44.3 / 31.1 / 31.1 / 17.3 kg/yr; ~49 m/s/yr N/S, up to 80% of total station-keeping propellant.
- **mc_dowell_2025_space_activities_gcat** (read, no licence): Jan 2026 GEO active payloads 613 within GPZ +/-100 km, 638 including 18 in graveyard (dead 779, debris 510), so "~550" is low by 11.4-16.0%.

All N/S-only figures sit below the ~70 kg total as they should. **rc-057** proposes ~44,600-46,400 kg/yr at upstream's own 72.7 kg per satellite. `extracted_data/r92_geo_stationkeeping_propellant_key_numbers.csv`.

## R113 - NASA's ISRU production scale (2026-10-04)

- `sanders_kleinhenz_2024_isru_space_mining_unoosa` (read, not hosted): NASA's unfunded vision: 30-60 t per lander mission, 100s-1000s t/yr cislunar, 100s t/yr for Mars transportation, 10s of t/yr as the first commercial goal.
- `araghi_2022_nasa_lunar_isru_technology_overview` (hosted): first-plant targets of at least 10 t O2/yr, 15,000 kg/yr icy-regolith processing, 10,000 kg/yr oxygen clean-up, 10s of t/yr electrolysis, each for 3 years.

cislunar 100 t/yr is at the bottom of NASA's band; lunar_surface 50 t/yr matches "10s of t/yr"; Mars rows (80 t/yr) sit below "100s". Bounds only. `extracted_data/r113_isru_production_targets.csv`.

## R114 - GEO station-keeping studies; commodity elasticities (2026-10-04)

| source | station-keeping propellant | note |
|---|---|---|
| `lamorte_2020_geostationary_satellite_electric_propulsion_master_thesis` (T4) | 65.3 kg/yr chemical; 11.1 kg/yr Hall | one satellite, one year |
| `snyder_2001_iepc_172_dual_mode_spt_geosynchronous_satellites` | 244 kg xenon over 15 years (~16 kg/yr) | 3,500 kg dry, 48.5 m/s/yr N/S |
| `sovey_pidgeon_1990_advanced_propulsion_leo_geo_platforms` | arcjet 51%, ion 25% of the hydrazine baseline; ~138 kg/yr chemical implied | 8,000 kg-class platform |
| `oleson_1995_advanced_propulsion_geo_insertion_nssk` | assumptions only (Isp 600-3,160 s, tankage 0.07-0.15) | 15-year NSSK model |
Chemical fits 70 kg/yr (65 to ~138 by size), electric cuts it to ~11-16 kg/yr, and the row does not say which fleet it assumes: a clarification for the owner.

`bogmans_2024_power_of_prices_commodity_supply_demand_elasticities` (IMF WP 2024/077): minerals "particularly inelastic", copper and zinc demand near zero, oil and coal below 0.2, rising with horizon; no PGMs. `vertier_2025_banque_de_france_eco_notepad_419_price_elasticity_critical_mineral_supply`: for eight critical minerals incl. PGMs a 1% demand-driven price rise raises output ~0.5% over five years (0.2-1%), a supply elasticity. `sanders_2010_iac_lunar_isru_isecg_reference_architecture`: ~250 kg O2/yr demonstration scale. `esa_2019_space_resources_strategy`: Luxembourg study's EUR 73-170B space-resources revenue over 2018-2045 (EUR 2.7-6.3B/yr), excluding propellant oxygen and asteroid PGMs. `extracted_data/r114_gr_links_key_numbers.csv`.

## R134 - Superhighway cost companion read (2026-10-07)

`tiffin_friz_rosenthal_2022_space_superhighway_cost_analysis` (NTRS 20220012942, 18 pp; copyright flag, so read only, though the PPTX title slide says US government work: hosting is the owner's call): "The combined demand for propellant resupply and payload delivery in cislunar space for NASA’s Moon to Mars campaign in addition to commercial ventures will likely exceed 1,000 t in the upcoming decades" (a decade-scale total); reusable SEP tugs need ~2x dV and deliver 40-83% less per mission, breaking even at 1,000 t to NRHO; tug life 10 -> 15 years cuts cost up to 10%; halving LV reuse cost (assumed 10% of production) cuts it 3/9/21% for 250 / 1,000 / 10,000 t campaigns; Xe "thousands of dollars per kg" vs Kr hundreds; chemical propellant <0.1% of campaign cost. `extracted_data/r134_superhighway_cost_key_numbers.csv`.

## R151 - Cislunar-economics papers registered (2026-10-10)

All closed to this machine, `registered_not_pulled` (DOWNLOADS.md):

- **bennett_xie_dempster_2022_moon_neas_cislunar_propellant** (Acta 190:409-412): Moon vs NEA propellant sourcing cost, for the utility factors.
- **entrena_2017_emerging_cislunar_economy_framework** (Acta 141:209-218): framework for the `market_model` choice.
- **keravala_tietz_stone_2013_shackleton_propellant_depot_architecture** (New Space 1(2):91-100): first commercial depot business case, per-kg fuel pricing.
- **kutter_sowers_2016_cislunar1000_self_sustaining_space_economy** (AIAA SPACE 2016): cislunar transport demand scale.

Held back: Barry 2024 (paid proceedings) and Kuhns 2021 (lunar-ice production, not demand).

## R156 - FAA Aerospace Forecast commercial-space chapters (2026-10-12)

Both hosted (US government work):

- **faa_2025_aerospace_forecast_commercial_space** (FY2025-2045): FY2024 had 148 licensed operations, "the highest posted in U.S. history" (824 since 1989; p4); forecast 174-183 (FY2025) to 259-566 (FY2034), totalling 2,067 / 4,010 (p5); SpaceX 83% of FY2024's 142 launches (118; Rocket Lab 12, Virgin Galactic 4, Blue Origin 3, ULA 2, Firefly 2, Stratolaunch 1); the space economy "between $1.4 trillion and $2.3 trillion by 2035, up from $630 billion in 2023", launch costs "fallen 10-fold over the last 20 years" (p8). ISAM and cislunar operations named as demand drivers.
- **faa_2024_aerospace_forecast_commercial_space** (FY2024-2044): "from a low-high range of 134-156 in FY2024 to a low-high range of 195-338 by FY2028" (p5); actuals 2015: 14, 2016: 17, 2017: 22, 2018: 35, 2019: 32, 2020: 33, 2021: 64, 2022: 74, 2023: 113.

Demand-scale context, no per-kg price. `extracted_data/r156_faa_launch_demand_forecast_key_numbers.csv`.

## R164 - Candidate (2026-10-14)

rc-123: cite the IMF elasticities (below 0.5 short-run) and not the Banque de France supply figure for `demand_elasticity`. Text in `revision_candidates_closed.csv`.

## R310 - A positive surplus-price floor does not guarantee a bounded fleet optimum (2026-11-01)

`economicspace_spacevalue_capacity_market_implementation_2026`: economicspace
`MODEL.md:777-784` at 54e30b0ae82be71c987f08feb95630502b7f54f0 says surplus sales leave
the objective turning over on its own and calls `1.0` "the only setting that would
genuinely remove the ceiling". The active surplus fraction is 0.5 (`modules/calc.py:526`);
`max_fleet_ships` is 64 (L946). The price floor permits unlimited surplus quantity at that
fraction, so declining marginal revenue does not itself prove an interior optimum.

The original cost tail, programme-options and selection-key functions from calc.py and
`_delivery_window_yr` / `_capped_sale_value` from spacevalue cargo were executed together.
The latter two functions have the same blob at the consumer pin v0.2.0 and current main
873b91c1ce51fd2f5fe9ead63ce171d755e73011. This is a reduced mathematical ledger, not a
simulated asteroid: each delivery contains 2 kg of one commodity at normalized price 1;
its annual full-price ceiling is 1 kg/yr, mission duration 5 yr, cadence 1 yr, and each rig
can fly five campaigns. Recurring cost is 1.5 per delivery and one-time NRE is 10.
All other monetary ledger fields are zero, contingency multiplier is 1, WACC is zero,
and the learning factor is 1; the complete cost-tail input tuple is in the CSV.

| maximum fleet | surplus fraction | selected F | selected W | cost / revenue |
|---|---|---|---|---|
| 64 | 0.5 | 64 | 5 | 1.5077285512 |
| 128 | 0.5 | 128 | 5 | 1.5038850768 |
| 256 | 0.5 | 256 | 5 | 1.5019478082 |
| 64, 128 or 256 | 0 (wall control) | 1 | 5 | 1.9444444444 |

Each coarse ladder has forty options. Exhaustive enumeration of every integer fleet
through each cap crossed with W=1..5 gives the same selection using the original
`cost_revenue_ratio` key. All options are unprofitable, so that key minimizes cost/revenue.
The counterexample has a finite positive ceiling and five 1-year stays within a 15-year rig
life; it uses no missing-market exemption.

For W=5 the implemented window is `2/F-0.2/F^2`, revenue per delivery is
`1+1/F-0.1/F^2`, and cost is `1.5+2/F`. The ratio is therefore
`R(F)=(1.5*F^2+2*F)/(F^2+F-0.1)`. Exact-rational differentiation gives numerator
`-0.5*F^2-0.3*F-0.2` over the positive squared denominator: it strictly decreases for
all F>=1 and approaches 1.5. The fleet optimum is the search cap in this example.
Verdict: an interior optimum is contingent, and positive discounted marginal revenue can
leave fleet growth favourable indefinitely. `rc-240`: qualify the fleet-bound guarantee.
`extracted_data/r310_surplus_price_floor_fleet_bound.csv`.

The same record explicitly declares finite-programme window averaging (`cargo.py:996-1001`).
Its quantitative effect was checked separately: N=5,F=1,T=5,cadence=1 gives average window
1.8. Five 2-kg raw loads at price 1 and annual ceiling 1 yield total value 9.5 at half-price
surplus under pooled capacity, versus 8.0 when the documented first window of 5 and four
later windows of 1 are each cleared independently; with no surplus sale the totals are
9 and 6. Cargo 0.5 kg (no window binds) and 6 kg (every window binds) give equal totals
under both treatments. The averaging is an explicitly declared capacity-pooling assumption.
`extracted_data/r310_declared_window_averaging_comparison.csv`.

## R322 - Market-shaped cargo is priced after the engineering hold is fixed (2026-11-02)

Source `economicspace_market_capped_hold_engineering_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`
and `MODEL.md`; spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011,
`spacevalue/cargo.py` and the committed cislunar price fixture; original
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f reference rows.
MODEL.md L786-787 says the discount "changes what the ship carries, not just
what it is paid". calc.py L7343 calls the exported composition "What the
optimiser actually chose to load".

The settled engineering book uses the uncapped hold: refinery energy and
cargo water at calc.py L6622-6631, containment and return dry mass at L6632-6642,
then processing power, plant mass and launch mass at L6701-6746. The refinery
helper asks for an uncapped mix (cargo.py L523-548). The later programme-price
call supplies market caps (calc.py L7177-7200), but retains only revenue,
clearing, unsold and surplus fields. Its changed mix never replaces these
physical books or the original composition exported at L7344-7350.

Nine original full-evaluator cases use the actual Falcon 9 reusable, kerolox
and all 46 operational-cost rows. The synthetic body is 1e9 kg, half iron and
half water, density 2 g/cm3, at 1.2 AU; delta-v is 1,000 m/s per leg. The
concentrated cases process three times their cargo mass with recovery 0.9.
ISRU and aerocapture are off, propulsion is chemical, and launch windows,
boil-off and programme-scale search are disabled. The first cases disable
refinery to isolate cargo-water engineering; water liberation and volatile
containment remain enabled. Iron is 100 USD/kg with a 10 kg/yr full-price
market; water is 80 USD/kg with a nonbinding market. Default surplus fraction
is 0.5. The priced and physically booked loads differ:

| original case | exported/engineered hold | mix priced for sale | booked / required processing W |
|---|---|---|---|
| 1,000 kg solar | 1,000 kg iron | 12.5 kg iron + 987.5 kg water | 501.939 / 1,628.451 |
| 10,000 kg RTG | 10,000 kg iron | 14.1068 kg iron + 9,985.8932 kg water | 3,055.556 / 9,990.204 |

The solar result books no cargo water or containment, while the priced hold
requires 49.375 kg containment under the same 0.05 kg/kg water row. Its gross
value is 80,250 USD; selling the exported iron hold under the same ceiling,
window and discount gives 50,625 USD. The RTG result passes the configured
5,000 W limit despite its priced mix requiring 9,990.204 W at the same mining
duration. These term-level comparisons hold cargo/feed fixed; they are not
fully redesigned mass stacks.

Three fixed-N=1 diagnostics supply the same market caps to the engineering
mix calls, preserving the original numerical helpers. The solar case then
books 987.5 kg water, 49.375 kg containment and 1,628.451 W, with the same
80,250 USD revenue; its complete launch mass rises from 4,473.247 to
4,671.025 kg and total cost by 10.992M USD. The RTG diagnostic rejects at the
trial power check. The nonbinding-market diagnostic preserves the complete
original output. Original controls also retain a pure-iron hold when its
discounted price exceeds water's full price, and preserve the raw-ore path.
Disabling both water models removes those physical terms but leaves the
price/exported-mix disagreement. A zero-surplus hard-cap case also reshapes
the priced hold without updating engineering.

Two further original cases enable refinery and use the actual committed
cislunar fixture rows: iron/water pre-processing prices 5,065.7565/7,236.3403
USD/kg, annual markets 25,000/55,000 kg and refining energies 5/0.5 kWh/kg.
At N=1 the 1,000 kg pure-water hold faces no binding ceiling. At fixed N=320
(64 ships, five campaigns each), the same physical book remains pure water,
while the priced hold is 804.9927 kg water plus 195.0073 kg iron. Refining
energy is booked at 500,000 Wh versus 1,377,532.959 Wh for that mix. After
its smaller water-heating term, required processing is 2,048.832 W versus
1,870.865 W booked. Containment is conversely overbooked at 50 kg versus
40.2496 kg. Thus the mismatch can change physical requirements in either
direction and occurs with actual price, demand and energy inputs.

All accepted cases fit their separate body, cumulative-feed, throughput and
launch budgets; no electric-stage or ISRU discrepancy is needed. Independent
two-tier allocation, direct sale sums and phase-energy calculations reproduce
the six capped cases. Verdict: price, exported cargo and engineering do not
describe one mission. `rc-252`: couple priced, physical and exported cargo.
A power-infeasible maximum-revenue mix does not prove that every alternative
cargo is infeasible.
These are synthetic-body witnesses; population incidence and ranking effects
were not measured. `extracted_data/r322_market_capped_hold_engineering.csv`.

## R330 - Substitute commodities spend the same class import budget separately (2026-11-02)

Source `spacevalue_shared_class_market_budget_record_2026`:
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011, `spacevalue/catalog.py`,
`spacevalue/cargo.py`, committed cislunar/Earth price fixtures and
`tests/test_tables.py`; economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0,
`modules/calc.py`; AsteroidCatalog@66fb47aaeb17aa7e11c023773a39765c1aa793fb,
`reference/taxonomy_composition.csv` and `reference/mineral_phases_detailed.csv`.

The market definition says "within a class they are substitutes" and
"The four bulk classes partition the budget" (catalog.py L995-997). Cislunar
annual imports are 100,000 kg; shielding receives 0.15, structural 0.25,
propellant 0.55 and chemical 0.05 (L959,L1004-1010). These are declared
assumptions, not measured destination demand. `annual_market_kg` returns the
whole class allowance for each name (L1084-1087), then the exported table
records that number without the class market identity (L2604-2611).
`phase_market_key` returns a commodity's own name whenever it is in the
market table (cargo.py L856-859). Its explicit silicate-residual alias is
pooled, but olivine, pyroxene and other substitutes remain different keys.
The consumer carries those keys into its raw sale, nonbinding test and
beneficiation caps (calc.py L6961-6964,L7150-7186).

Thirty-three original raw-sale/knapsack calls use the committed net-price
fixtures and a one-year delivery window. Every allocation is observed
without changing the functions, and each output exactly matches an untraced
call. All 118 fixture annual-cap values match the current original cap
function. An independent continuous allocation first reproduces the original
market keys, then changes only full-price grouping to the declared in-space
classes, retaining Earth-sale markets. All 66 solutions satisfy supply,
payload and market constraints and have residual-potential optimality
certificates. The equal-price two-mineral result also has a closed-form check.

At the fixture price 1,603.050708496265 USD/kg, a raw 20,000 kg load split
equally between olivine and pyroxene sells all 20,000 kg at full price:
each 10,000 kg is below its separate 15,000 kg allowance. Together they
exceed the shielding class budget by 5,000 kg. Under the default half-price
surplus rule the same declared class budget gives:

| calculation | full-price kg | half-price kg | value USD |
|---|---|---|---|
| original separate commodity keys | 20,000 | 0 | 32,061,014.169925 |
| one shared shielding budget | 15,000 | 5,000 | 28,053,387.398685 |

The 4,007,626.771241 USD difference occurs in both raw and beneficiated
helpers. With a hard wall the values are 32,061,014.169925 and
24,045,760.627444 USD instead. These synthetic load sizes preserve the
original prices and annual-demand assumptions.

Using the committed S-type detailed composition, a 20,000 kg raw hold sells
17,280 kg of shielding phases at full price against the same 15,000 kg
class budget, although no individual commodity cap binds. Value is
38,161,839.329710 versus 36,334,361.522025 USD with the shared budget.
At a 100,000 kg hold, original raw pricing gives 54,900 kg full-price
shielding and 165,561,147.989735 USD, versus 133,580,286.355235 USD shared.
The beneficiated case, with 500,000 kg feed and recovery 0.9, gives full-price
structural/shielding/chemical mass 52,000/38,800/7,200 kg against
25,000/15,000/5,000 kg class budgets. Its original value is
292,737,345.009292 versus 227,684,295.005964 USD shared. The original C, D,
M and V reference compositions also give revenue differences in both paths.

Nineteen comparisons differ in value; fourteen revenue controls agree:
one product, nonbinding supply, the existing silicates/residual alias,
different classes, terrestrial markets, in-space downleg sales and equal
full/discount prices. Equal-tier prices can leave allocation labels tied;
observed full-price mass exceeds a class budget in twenty cases, including
the raw discount=1 case whose revenue does not change. Earth-sold Pt/Au
remain separate terrestrial markets despite sharing the trace label.

Verdict: per-commodity keys replicate a declared shared class allowance.
`rc-261`: preserve market identity and enforce shared class full-price budgets.
The adopted class shares, prices and programme window are unchanged. Tests
checking each exported cap against its own function (test_tables.py L45-56)
do not test aggregate class spending. This is a capacity-pricing witness;
complete mission redesign, prevalence in the catalogue and ranking effects
were not measured. `extracted_data/r330_shared_class_market_budget.csv`.

## R352 - Market accumulation extends beyond the programme calendar (2026-11-03)

`economicspace_spacevalue_programme_market_clock_record_2026` reads
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0 and
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011. calc.py L4640
states a wave sells at `T + w × cadence`; L5725-5726 and L7491 report
programme span `T+(W-1)*cadence`. In contrast, cargo.py L990 totals
`duration + (N - 1) x cadence / F` market years, described as "years in
total" (L992), before dividing across N deliveries (L1041-1045).
calc.py L7141-7142 consumes this window; MODEL.md L751-759 repeats it.

For rectangular N=F*W, the market horizon exceeds the cost/reporting horizon
by `cadence*(1-1/F)`. A uniformly staggered fleet can produce the longer
horizon, but its within-fleet offsets do not appear in the stated wave
calendar or reported end. The diagnostic retains the existing wave
calendar and finite-programme capacity pooling, changing only the imported
window to `[T+(W-1)*cadence]/N` for F>1. It introduces no demand, price,
surplus, physical or financing coefficient.

Twenty-five synthetic raw single-phase fixtures run native, repeat,
clock-only diagnostic and repeat: 100 complete evaluate_asteroid consumers,
using original numerical function bodies, reference-only Stage 2, actual
source vehicles/kerolox and geometric transfers. Reliability, WACC, launch
windows, refinery and ISRU are off. Each selected tuple is asserted present
in the original ladder before restricting it; this is a mechanism test,
not an unrestricted fleet optimum. Independent 50-digit Decimal enumeration
of W sale epochs, each containing F deliveries, verifies the horizon
identity and rate-times-end budget.

For the 1-km magnetite fixture (3 g/cm3, a=1.2 AU, e=i=0, 10 h spin),
Falcon 9 reusable/kerolox with (N,F,W)=(64,64,1) is one of forty original
choices at the current 64-ship limit. Mission and programme duration are
both 1.8008760870758898 yr, but native market accumulation lasts
2.0469698370758898 yr. At the adopted 25,000 kg/yr full-price rate,
the programme sells 51,174.245926897245 kg at full price against
45,021.902176897245 kg accumulated by its reported end: 6,152.34375 kg
extra. The clock-only diagnostic closes that budget. Current half-price
surplus sales give per-mission gross 3,156,059.9973833505 versus
2,987,794.2024844512 USD, a 5.631773% uplift. Payload
1,003.4617809559003 kg, launch 17,400 kg and per-mission cost
653,609,865.2011702 USD stay exact.

Fifteen native books exceed the rate-times-reported-end budget, and all
fifteen diagnostics close it. Changes persist across F=50..1000, W=2/3/5,
distance, vehicle, mineral and hard-wall sensitivities. Ten full-book
controls are exact: N=1, serial F=1, small nonbinding parallel fleets,
elasticity and unbounded modes. Both repeated pairs match native
types/values/float.hex fingerprints; every field outside seven
price/clearing/profit metrics is exact. All returned books pass the source
checks exercised by the harness, and all examples remain unprofitable.

Verdict: `rc-287`, share one schedule across full-price accumulation,
programme end and dated programme costs. Retaining the longer staggered
schedule is an alternative if the associated calendar and reporting are
made consistent. The evidence does not reject capacity pooling or re-pin
demand; it measures no observed-body incidence or catalogue ranking.
Twenty-four runtime/method blobs match pinned metadata; all four live main
comparisons are identical. `extracted_data/r352_programme_market_clock.csv`
contains full inputs/books, clock certificates and the reproduction harness.

## R361 - Current GEO active-fleet count (2026-11-08)

The `geo` row of `spacevalue/catalog.py` `IN_SPACE_ANNUAL_DEMAND_KG` is
44,600 kg/yr. Its comment derives this from 613 active GEO payloads in GCAT's
January 2026 Table 22 and the prior row's implied 72.76 kg/payload/yr.

`celestrak_satcat_gpz_active_2026`: the current CelesTrak SATCAT query for
active payloads in the GEO Protected Zone returned 565 records on 2026-11-08;
the SATCAT page says its data are current through 2026-11-07 22:58:29 UTC.
The response has 536 operational, 21 partially operational, 7 backup and 1
spare payloads. CelesTrak defines the GEO Protected Zone as GEO altitude
plus/minus 200 km. The GCAT Table 22 row is labelled GPZ plus/minus 100 km;
Figure 8 clarifies that this means GEO plus/minus 300 km, not GEO plus/minus
100 km. The GCAT band is therefore wider, and the 565 and 613 counts are not
from matched spatial bands.

Holding the existing per-payload rate fixed, 44,600 x 565 / 613 = 41,108
kg/yr, 3,492 kg/yr (7.83%) below the current ceiling is only an arithmetic
diagnostic: because the spatial bands differ, it is not a like-for-like demand
revision. The count comparison does not independently validate the assumed
72.76 kg/payload/yr. `rc-290` asks for matched-band fleet reconciliation before
any re-pin. `extracted_data/r361_geo_satcat_active_count.csv` records the query
count, status split and qualified arithmetic diagnostic.

## R364 - GCAT's GEO count uses a wider band than CelesTrak GPZ (rc-290; 2026-11-08)

`mc_dowell_2025_space_activities_gcat`, *Space Activities in 2025*, Figure 8
p.65, defines the dashed GPZ+/-100 km result limits as GEO+/-300 km; Table 22
p.66 labels its 613 active payload count `GPZ+/-100`. The registered
`celestrak_satcat_gpz_active_2026` live query uses CelesTrak's GEO Protected
Zone at GEO altitude+/-200 km. `celestrak_satcat_format_docs_2026`, updated
2026-09-23, lists APOGEE and PERIGEE fields and query selectors/flags but no
custom altitude-band selector. A matched count needs record-level filtering under a shared orbit
boundary and status rule. The old 565/613 scaling is retained only as a
diagnostic, not as an annual-demand correction. rc-290 is revised to require
that matched comparison before changing the 44,600 kg/yr ceiling.
`extracted_data/r361_geo_satcat_active_count.csv`.

## R365 - Current record-level count within the GEO+/-300 km band (rc-290; 2026-11-08)

`celestrak_satcat_active_group_2026`: one CelesTrak SATCAT active-group CSV
query retrieved 2026-11-08 22:48:42 UTC returned 17,418 records. Using the
documented `APOGEE` and `PERIGEE` fields, the 17,352 Earth-orbit payloads with
both values present were filtered by full orbital envelope. GEO is 35,786 km;
the 585 records with perigee >=35,486 km and apogee <=36,086 km are inside
GEO+/-300 km. Their status codes are 554 operational, 22 partially operational,
7 backup and 2 spare. The same whole-orbit filter at GEO+/-200 km yields 564,
one fewer than `celestrak_satcat_gpz_active_2026`'s 565-query count, a useful
consistency check. A mean-altitude filter instead yields 602 at GEO+/-300 km,
so the altitude convention remains material.

`mc_dowell_2025_space_activities_gcat` Table 22 p.66 gives 613 active payloads
in its `GPZ+/-100` row, which Figure 8 p.65 defines as GEO+/-300 km. Holding the
existing implied 72.7569 kg/payload/yr fixed, scaling 44,600 by 585/613 gives
42,562.8059 kg/yr (42,563 rounded), 2,037.1941 kg/yr (4.5677%) below the
current ceiling. The catalog snapshots differ by about ten months and use
separate status sources; this does not remeasure per-payload demand. rc-290
now carries a concrete alternate fleet basis while remaining open on the exact
altitude-classification rule. `extracted_data/r365_geocount_matched_300km.csv`.


## R366 - CelesTrak active-status definition for GEO count (rc-290; 2026-11-08)

`celestrak_satcat_operational_status_2026`, Operational Status page, updated
2026-10-12, defines active as statuses `+`, `P`, `B`, `S` or `X` and says
active status does not require power or communications. The R365 whole-orbit
GEO+/-300 km count contains 554 `+`, 22 `P`, 7 `B`, 2 `S` and no `X`
records (585 total), so its status split is compatible with CelesTrak's
`ACTIVE=1` definition. This defines the CelesTrak side only; it does not
establish that CelesTrak and GCAT use the same active-status rules.
`extracted_data/r366_celestrak_active_status_definition.csv`.


## R367 - GCAT current-orbit GEO active count (rc-290; 2026-11-08)

`mc_dowell_2026_gcat_active_current_catalog`: GCAT Release 1.8.9 data
updated 2026-11-07 publishes `active.tsv` and `currentcat.tsv`. The active
catalog documentation says entries are payloads that are or may be still
transmitting and that active status is infrequently updated and sometimes a
guess. The current-catalog documentation defines `Active=A` as active
satellite and says its perigee/apogee are from the most recent available
current orbit. In `currentcat.tsv`, 17,039 payloads have `Active=A`; 564 have
`OpOrbit` beginning `GEO`, all with numerical current perigee/apogee. Requiring
the entire current orbit to lie within GEO+/-300 km (35,486-36,086 km) gives
524 payloads; classifying by the perigee/apogee midpoint gives 544. At
GEO+/-200 km, the same rules give 511 and 541.

Scaling the existing 44,600 kg/yr at the fixed rate implied by GCAT Table 22's
613 January payloads gives 38,124.633 kg/yr from the full-envelope count and
39,579.772 kg/yr from the midpoint count. The `active.tsv` release itself has
575 `GEO*` representative early-operational-orbit entries; its full-envelope
filter yields 496 and its midpoint filter 545, illustrating why currentcat's
latest orbit is used for the current-orbit comparison. GCAT warns its active
status is infrequently updated and sometimes guessed. Its November currentcat
count differs from CelesTrak's 585 whole-envelope active payloads; the
catalog/status and orbit-selection rules remain unresolved. No per-payload
demand change is inferred, and `rc-290` stays open.
`extracted_data/r367_gcat_current_geocount.csv`.


## R461 — Current programme market-clock option

At economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, `CalcConfig.model_market_wave_clock` defaults to `False` (modules/calc.py:688), and the module-level consumer constructs `CONFIG = CalcConfig()` without an override (line 1468). The default branch continues to call `_delivery_window_yr(n_missions, fleet, mission_duration_yr, cadence_yr)` (line 7727). With the flag enabled, the market window becomes `(mission_duration_yr + (waves - 1) * cadence_yr) / n_missions`, where `waves` is the campaigns-per-ship count or its ceiling (lines 7722-7726); for rectangular `N=F*W`, multiplying this window by N matches the cost calendar's reported span `T+(W-1)*cadence`. The change is opt-in and only alters the market-window calculation, leaving rc-287's default discrepancy and its broader shared treatment of programme timing unresolved. `rc-287` remains open. Extracted: `extracted_data/r461_current_market_clock_flag.csv`.


## R467 — Current engineered-hold capped-market option

At economicspace main commit `0c9e1bb49fe5d6c48b76e94c7bc135ca70d91939`, `CalcConfig.price_engineered_hold` defaults to `False` (modules/calc.py:753), and the module-level consumer constructs `CONFIG = CalcConfig()` without an override (line 1468). In the capped-market branch, the default concentration path re-runs `optimal_payload_mix` with market caps after physical sizing (lines 7750-7789), so the sold mix can differ from the engineered `payload_mix`. With `price_engineered_hold=True`, the branch instead applies `_capped_sale_value` to `sale_terms` from the engineered hold (lines 7790-7797); it constrains pricing to the hold already flown but does not market-redesign the hold. The v1.66.0/calc v1.39.0 release notes say six of nine R322 cases with a recorded engineered-hold sale match this path; examples include the 1,000 kg solar case falling from $80,250 to $50,625 and the hard-ceiling case from $80,250 to $1,250. Across 53 sampled evaluable rows, two changed cost/kg (1.001x and 1.019x) with no evaluability change; three market-aware diagnostics were not replayed. The correction is opt-in, so `rc-252` remains open for default-path resolution and the remaining market-aware interaction checks. Extracted: `extracted_data/r467_current_engineered_hold_market_flag.csv`.


## R515 — LEO annual propellant-demand comparator

Howard’s NASA DSEV concept assumes 90 t of Starship’s predicted 100 t payload can be transferred as propellant and says 12 Xenon plus 27 LOX/CH4 tanker flights are needed to fuel one Mars mission (Section IV.B, p. 4); Section VIII.A (p. 13) repeats the 39-flight total. Table 1 (p. 4) lists four Mars departures in the 2028–2037 analysis window. Applying the assumed 90 t to all 39 flights gives 3,510 t per mission; evenly spread over four departures and ten years, that is 1,404 t/yr. Spacevalue’s `IN_SPACE_ANNUAL_DEMAND_KG["leo"]` is 500,000 kg/yr. This NASA concept’s schedule-based transfer capacity is 2.81 times the stored ceiling, but it is a single architecture and not a general or observed market forecast. `rc-381` records the annualization and scope review; no replacement value is established. Extracted: `extracted_data/r515_leo_mars_dsev_propellant_demand_comparator.csv`.


## R525 — Mars-orbit annual-demand scale comparator (2026-11-10)

`sanders_kleinhenz_2024_isru_space_mining_unoosa`: NASA JSC’s presentation gives “100s metric tons per year for human Mars transportation” as a notional production scale (NTRS 20240002713, PDF p. 3); the same slide states the activities shown are not currently funded or approved.

Upstream: spacevalue `spacevalue/catalog.py` `IN_SPACE_ANNUAL_DEMAND_KG["mars_orbit"]` = 60,000 kg/yr. Its comment frames this as one crewed mission’s in-space propellant per approximately 2.14-year synodic period. Verdict: the NASA transportation scale is larger, but is a notional production vision, not a Mars-orbit depot demand forecast; retain the mission-cycle value as a conservative scenario pending a like-for-like market basis. `rc-391`. Extracted: `extracted_data/r113_isru_production_targets.csv`.


## R526 — Mars-surface demand scale citation (2026-11-10)

`sanders_kleinhenz_2024_isru_space_mining_unoosa`: the NASA JSC presentation gives “10’s of metric tons of commodities per year for initial commercial usage” (NTRS 20240002713, PDF p. 3) and labels the slide a notional future direction, with depicted activities “not currently funded or approved.”

Upstream: spacevalue `spacevalue/catalog.py` `IN_SPACE_ANNUAL_DEMAND_KG["mars_surface"]` = 20,000 kg/yr; the module labels the in-space demand table judgment, not measurement. Verdict: the NASA goal supports the order of magnitude as a scenario citation, but it is not a Mars-specific market forecast or measured absorption rate. Retain 20 t/yr as a judgment-based surface-base ceiling. `rc-392`. Extracted: `extracted_data/r113_isru_production_targets.csv`.


## R527 — GTO launch-based demand ceiling scope (2026-11-10)

`mcdowell_2026_space_activities_2025_gto_launches`: Table 14(e) counts 34 launches in the 2025 “GTO Transfer” category (p. 38). `toson_etal_2016_draise_geo_platform_mass`: the IAF abstract describes chemical GEO communications platforms as typically about 6 tons, with about half their total weight as propellant (p. 1). `byers_1989_advanced_onboard_propulsion_tm103174`: NASA TM-103174 says apogee propellant for GEO satellites is 40–50% of mass injected into GTO (p. 1; Fig. 1).

Upstream: spacevalue `spacevalue/catalog.py` `IN_SPACE_ANNUAL_DEMAND_KG["gto"]` = 81,600 kg/yr, calculated as 34 × 6,000 × 0.40. Verdict: the cited sources support the launch count, a typical chemical GEO-platform mass, and the apogee-propellant fraction separately; they do not establish that every GTO Transfer launch carried one chemical GEO communications platform. Keep the arithmetic only as an idealized scenario pending a payload-cohort and mass-basis check; no replacement annual value is established. `rc-393`. Extracted: `extracted_data/r527_gto_launch_mass_propellant_comparator.csv`.


## R602 — Surplus-price fraction lacks market basis (2026-11-11)

`economicspace_surplus_price_fraction_code_current_2026`: economicspace `CalcConfig.surplus_price_fraction` is 0.5. Its code describes this as a deliberately round number and says no market study supports it; the fraction is applied only when surplus discounting is enabled under the `capacity_cap` market model.

`economicspace_surplus_price_fraction_verification_current_2026`: the current verification-sheet extraction marks input I110, 0.5, NEED BACKING. Its archived Stage 2/3 tables are not current market evidence. Verdict: ask for price-response or market-clearing evidence with commodity and destination scope, or identify 0.5 explicitly as a scenario dial and show sensitivity bounds. Preserve the value; no replacement inferred. This is distinct from rc-240’s fleet-optimum wording issue. **rc-465** records the missing basis. Extracted: `extracted_data/r602_surplus_price_fraction_basis.csv`.


## R643 — Spacevalue elasticity comment retains unsupported PGM claim

`bogmans_2024_power_of_prices_commodity_supply_demand_elasticities`: the registered IMF study reports demand-elasticity estimates for copper, zinc, lead and tin, not PGMs. `vertier_2025_banque_de_france_eco_notepad_419_price_elasticity_critical_mineral_supply`: its approximately 0.5 estimate is a mine-output supply response, not demand elasticity.

Upstream: `spacevalue/cargo.py` `saturation_price_multiplier` retains the statement “Precious-metal demand is inelastic, ε ≈ 0.5” above the constant-elasticity formula; the helper receives `elasticity` as an argument. The file says the elasticity path remains the v1.14.0 curve in the no-caps compatibility path. The independent economicspace copy was corrected under rc-123; this spacevalue copy still has the prior claim. Verdict: the registered sources do not establish PGM demand elasticity. Treat 0.5 as a scenario if used; retain the formula and caller input pending PGM-specific evidence, with no replacement inferred. **rc-507**. Existing extraction: `extracted_data/r114_gr_links_key_numbers.csv`.


## R658 — economicspace surplus-price fraction rechecked (2026-11-12)

At economicspace main `c1a6333e6e50e0e3658d05e47128a94ce4f07831` (calc 1.45.0), `surplus_price_fraction` remains 0.5 while `sell_surplus_at_discount` is enabled. The new default market-wave clock changes programme timing, but no empirical price-response basis for the half-price assumption was added. **rc-465** remains open. Existing extract: `extracted_data/r602_surplus_price_fraction_basis.csv`.


## R765 - Frozen cislunar annual-market ceiling worksheet lineage (2026-11-15)

**spacevalue_annual_demand_class_share_code_current_2026**: Current Spacevalue code sets cislunar import demand to 100,000 kg/yr and labels the destination table judgment. Its class shares are allocation scenarios; the comment says Kornuta et al. and LunA-10 provide demand forecasts but do not apportion the import budget among commodity classes. `annual_market_kg` multiplies the destination total by the commodity-class share. Existing **kornuta_2019_commercial_lunar_propellant_architecture** and **northrop_grumman_2024_luna10_lunar_rail_network** provide forecast context, not a measurement of those shares.

**economicspace_frozen_stage2_market_ceiling_rows_current_2026**: The frozen Stage 2 1.12.0 cislunar rows store 5,000 kg/yr for carbon, 25,000 for cohenite, nickel-iron, schreibersite and troilite, and 15,000 for enstatite, olivine, plagioclase and silicates. Their notes describe the minerals, not the `annual_market_kg` field.

**economicspace_market_ceiling_verification_sheet_code_current_2026**: The current worksheet flags I101-I109 NEED BACKING while explaining that the values come from the frozen Stage 2 rows. `rc-432` records the current code-level class-share scenario note; `rc-261` addresses sharing class allowances across substitutes, while `rc-290` and `rc-381` review GEO and LEO destination totals. This candidate is limited to the frozen worksheet's annual-market citation lineage. Verdict: carry the current scenario and scope notes into I101-I109; no market value or class share change inferred. `rc-636`. Extracted: `extracted_data/r765_cislunar_market_ceiling_worksheet_lineage.csv`.

## R767 — Cislunar utility worksheet omits the base-profile fallback (2026-11-15)

**spacevalue_cislunar_utility_lookup_current_2026**: at Spacevalue main `5f84fbf36709e3c2b09356a65cb34c9890ff8904`, `IN_SPACE_UTILITY_BY_DESTINATION["cislunar"]` is `{}` and the code labels it “base profile, no local resources” (line 724). `in_space_utility()` checks the destination override, then returns `IN_SPACE_UTILITY` when the override has no value (lines 916–919). The base map values for kamacite, taenite, cohenite and schreibersite are 0.70; olivine, enstatite, plagioclase and silicates 0.25; carbon 0.40; troilite 0.30. **economicspace_frozen_stage2_cislunar_utility_rows_current_2026**: the frozen Stage 2 1.12.0 cislunar rows store those same values.

**economicspace_utility_verification_sheet_code_current_2026**: `campaign/verification_sheet.py` lines 1406–1413 builds the input citation as `spacevalue/catalog.py` and `IN_SPACE_UTILITY_BY_DESTINATION` for the destination, without stating that cislunar's empty override falls back to the base map. The worksheet marks I19, I22, I25, I28, I31, I34, I37, I40, I43 and I46 NEED BACKING; the factors remain engineering judgments, not calibrated market values. Verdict: identify the empty override and base-profile fallback in those input citations, retain the scenario caveats and NEED BACKING flags, and leave all factors unchanged. This is distinct from applied `rc-472` and `rc-483` code-comment updates and open `rc-296` on the silicate utility basis. `rc-638`. Extracted: `extracted_data/r767_cislunar_utility_source_path.csv`.

## R783 — Mars-surface annual-market worksheet lineage (2026-11-15)

**spacevalue_annual_demand_class_share_code_current_2026**: At Spacevalue main 5f84fbf36709e3c2b09356a65cb34c9890ff8904, IN_SPACE_ANNUAL_DEMAND_KG[mars_surface] is 20,000 kg/yr. Its code calls the destination total a judgment; the Mars-surface note uses NASA's order-of-magnitude slide as context, not a Mars market forecast. The class-share comment says no source apportions the import budget by class, and annual_market_kg multiplies the total by the share. The registered NASA source gives “10’s of metric tons of commodities per year for initial commercial usage” (NTRS 20240002713, PDF p. 3); the slide describes a notional, unfunded future direction.

**economicspace_frozen_stage2_mars_surface_market_ceiling_rows_current_2026**: At economicspace main 1cf2617f1a34e013e7f49bd9d908099e3e47354, the frozen Stage 2 1.9.0 Mars-surface catalog stores annual_market_kg values of 1,000 for carbon, 5,000 for nickel-iron and 3,000 for silicates. The row notes describe each material but provide no source for that column. These are 5%, 25% and 15% of the 20,000 kg/yr destination total.

**economicspace_market_ceiling_verification_sheet_code_current_2026**: campaign/verification_sheet.py --cell mars_surface__benef__search-off --check passes its worksheet checks and flags I66-I68 NEED BACKING among 51 of 94 inputs. The worksheet names Spacevalue's destination-demand and class-share fields in its routing explanation, but the backing ledger flags I66-I68 because the frozen row notes provide no published-source lineage for annual_market_kg. The worksheet does not carry the current code comments identifying the total and class shares as allocation scenarios.

Upstream: economicspace worksheet inputs I66 carbon=1,000 kg/yr, I67 nickel-iron=5,000 kg/yr and I68 silicates=3,000 kg/yr. Verdict: keep the historical values for reproducibility and carry the scenario provenance into these worksheet inputs; the NASA slide is scale context, not evidence for a measured Mars market or the class allocation. rc-392 covers the destination-total comment and rc-432 the current class-share scenario note; rc-636 is limited to the frozen cislunar worksheet rows. No numeric replacement inferred. rc-653. Extracted: extracted_data/r783_mars_surface_market_ceiling_worksheet_lineage.csv.

## R785 — Frozen Mars-orbit market-ceiling worksheet lineage (2026-11-15)

**spacevalue_annual_demand_class_share_code_current_2026**: At Spacevalue main 9d5d0af0d7581ff74cb9a2f360f910d7b15c245d, spacevalue/catalog.py SHA-256 DBC7D95A940857BCC463E7E89D396C77BF4901C616B201021357ABBD92A1E1FD sets IN_SPACE_ANNUAL_DEMAND_KG["mars_orbit"] to 60,000 kg/yr. The code calls it a conservative one-mission scenario, not a depot market forecast. _DEMAND_SHARE_BY_CLASS assigns 5% to chemical, 25% to structural and 15% to shielding, and annual_market_kg multiplies the destination total by the class share.

**sanders_kleinhenz_2024_isru_space_mining_unoosa**: NASA JSC's slide says “100s metric tons per year for human Mars transportation” (NTRS 20240002713, PDF p. 3) and describes the activities as not funded or approved. This is scale context, not a Mars-orbit depot-demand forecast. The quote is already extracted in extracted_data/r113_isru_production_targets.csv.

**economicspace_frozen_stage2_mars_orbit_market_ceiling_rows_current_2026**: At economicspace main 1cf2617f1a34e013e7f49bd9d908099e3e47354, the Stage 2 1.9.0 Mars-orbit catalog SHA-256 D5FCDCA5BFF3B4E0188C2CE79FF79E344995ABABE4378BFDF8B34C1833F9848D stores annual_market_kg values of 3,000 for carbon, 15,000 for nickel-iron and 9,000 for silicates. Those values equal 5%, 25% and 15% of 60,000 kg/yr; the rows are marked “used in space,” while their notes describe the materials and do not cite the annual_market_kg column.

**economicspace_market_ceiling_verification_sheet_code_current_2026**: The mars_orbit__raw__search-off worksheet check passes and flags I65-I67 NEED BACKING among 50 of 90 flagged inputs. Its routing explanation names Spacevalue's destination-demand and class-share fields, but the frozen row notes do not carry that scenario lineage.

Upstream: economicspace inputs I65 carbon=3,000 kg/yr, I66 nickel-iron=15,000 kg/yr and I67 silicates=9,000 kg/yr. Verdict: retain the frozen values for reproducibility and carry the 60,000 kg/yr one-mission scenario and class-allocation provenance into the worksheet; NASA's human-Mars transportation scale does not establish depot-market absorption. Distinct from rc-391's current Mars-orbit total review, rc-392's Mars-surface total, rc-432's current class-share note, rc-636's frozen cislunar rows and rc-653's frozen Mars-surface rows. No numeric replacement inferred. **rc-655**. Extracted: 15_inspace_demand_market_absorption/extracted_data/r785_mars_orbit_market_ceiling_worksheet_lineage.csv.


## R818 — Frozen Mars market worksheet rechecks (2026-11-16)

At fetched economicspace origin/main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, the frozen Mars-surface rows retain annual-market ceilings of 1,000 kg/yr carbon, 5,000 nickel-iron and 3,000 silicates; the Mars-orbit rows retain 3,000 carbon, 15,000 nickel-iron and 9,000 silicates. Their notes still describe the materials without citing the `annual_market_kg` field, so **rc-653** and **rc-655** remain open; the current code’s 20,000 kg/yr Mars-surface and 60,000 kg/yr Mars-orbit totals and class shares remain scenario allocations. Existing extractions: `extracted_data/r783_mars_surface_market_ceiling_worksheet_lineage.csv` and `extracted_data/r785_mars_orbit_market_ceiling_worksheet_lineage.csv`.

## R825 — Lunar-surface utility and annual-market worksheet inputs (2026-11-17)

- Current worksheet inputs I23/I26/I29/I32 use 0.45 for kamacite, taenite, cohenite and schreibersite; I35/I38/I41/I50 use 0.03 for olivine, enstatite, plagioclase and silicates. These are explicit `lunar_surface` overrides in Spacevalue. Carbon I44=0.40 and troilite I47=0.30 are not in the destination override and inherit the base `IN_SPACE_UTILITY` values. All ten are flagged NEED BACKING. Spacevalue's code describes local ice, FeO/ilmenite, regolith silicate and carbon-scarcity context, and labels utility values as engineering judgments; those qualitative facts do not derive the per-kg substitution fractions. The sheet's citation path incorrectly attributes carbon and troilite to the destination override. **rc-696** records this current calibration and lookup-path gap. Extracted: `extracted_data/r825_lunar_surface_utility_inputs.csv`.
- Current lunar_surface annual-market inputs I103/I104/I105 are 2,500/7,500/12,500 kg/yr. They are the 50,000 kg/yr destination total multiplied by chemical/shielding/structural shares of 5%/15%/25%. The current worksheet exposes the path and the model records the total and shares as judgments/scenarios under applied **rc-056** and **rc-432**. The open **rc-636** remains limited to frozen cislunar mineral rows I101-I109; current I109 is max_fleet_ships, not the older cislunar row.
- Extracted: `extracted_data/r825_lunar_surface_market_ceiling_inputs.csv`.

## R826 — Current worksheet mapping for the surplus-price dial (2026-11-17)

**economicspace_current_bestcase_verification_sheet_2026**: input I106 is 0.5, cites CalcConfig.surplus_price_fraction, and is marked NEED BACKING.

**economicspace_surplus_price_fraction_code_current_2026**: at economicspace main e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7, the code labels 0.5 a scenario dial and says no price-response or market-clearing evidence supports it; 0.0 and 1.0 are the stated bounds.

Verdict: the current worksheet confirms the empirical-backing gap while the code still identifies the number as a scenario. Applied rc-465 remains the scope record; no numeric replacement inferred. Extracted: extracted_data/r826_live_sheet_surplus_price_fraction_i106.csv.

## R850 — Current lunar-surface annual-market worksheet lineage (2026-11-17)

**spacevalue_annual_demand_class_share_code_current_2026**: Spacevalue main `9d5d0af0d7581ff74cb9a2f360f910d7b15c245d`, `catalog.py` SHA-256 `DBC7D95A940857BCC463E7E89D396C77BF4901C616B201021357ABBD92A1E1FD`, sets `IN_SPACE_ANNUAL_DEMAND_KG["lunar_surface"]` to 50,000 kg/yr. The code labels destination totals as judgments, not measurements. `_DEMAND_SHARE_BY_CLASS` says no source apportions the import budget by class and assigns 5% to chemical, 15% to shielding and 25% to structural; `annual_market_kg` multiplies the destination total by the share. The code's Kornuta and LunA-10 comparators concern lunar propellant demand and transport, not the total all-commodity market or those class shares.

**sanders_kleinhenz_hilburger_2024_long_term_lunar_infrastructure**: NASA NTRS 20240008379, *Using ISRU and Surface Construction to Define Long-Term Lunar Infrastructure Needs* (AIAA ASCEND 2024), describes Table 1 as approximate development guidance for phase-specific mission-consumable production (printed p. 6) and gives an initial production-capacity range of 10–50 metric tons on p. 14. The report's NTRS copyright field says portions may include protected material; no copy is hosted. Production capacity does not establish market absorption or class allocations.

**economicspace_lunar_surface_stage2_release_rows_current_2026**: At Economicspace main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, the current Stage 2 release file SHA-256 `516F1ED38A053DFA61BDFC42A9BBEBC6CCED6B945ACF2EAC447648774B157722` stores `annual_market_kg` values of 2,500 for carbon, 7,500 for silicates and 12,500 for nickel-iron. The row notes describe materials without sourcing annual market absorption.

**economicspace_current_bestcase_verification_sheet_2026**: The supplied verification sheet, generated 2026-11-16, lists I103/I104/I105 as 2,500/7,500/12,500 kg/yr on p. 27 and marks each NEED BACKING. On p. 45 it says “the row’s notes name no published source for this column.” Page 48 reports 63 inputs and 51 steps marked NEED BACKING. These three outputs are 50,000 kg/yr multiplied by 5%/15%/25%, respectively.

Upstream: current Economicspace worksheet inputs I103 chemical=2,500 kg/yr, I104 shielding=7,500 kg/yr and I105 structural=12,500 kg/yr. Verdict: carry the code-level scenario provenance into these current output rows and worksheet inputs; preserve the values, with no numeric replacement inferred. Applied rc-056 and rc-432 cover the Spacevalue code comments; open rc-636 covers frozen cislunar worksheet rows, not this current lunar-surface output. **rc-726**. Extracted: `extracted_data/r850_lunar_surface_market_ceiling_lineage.csv`.


## R908 — Spacevalue LEO demand comparator bibliography (2026-11-18)

**howard_2021_common_habitat_dsev_leo_propellant_demand**: Howard, A Common Habitat Deep Space Exploration Vehicle for Transit and Orbital Operations (AIAA ASCEND 2021; NASA NTRS 20210021084), p. 4, says “90 tons of Starship’s predicted 100-ton payload [4] capacity is transferrable propellant.” The registered extraction records 12 xenon and 27 LOX/CH4 tanker flights and four Mars departures in the paper's 2028–2037 schedule.

**spacevalue_leo_dsev_citation_gap_code_current_2026**: At Spacevalue main 80ec7549164fc1ed6c800ab0ef6205cde08ae9fd, spacevalue/catalog.py cites Howard, pp. 4 and 13, as a 1,404 t/yr comparator for IN_SPACE_ANNUAL_DEMAND_KG["leo"] = 500,000 kg/yr; the comment calls it “one architecture's modelled capacity, not a market.” The CITATIONS.md In-space demand section lists other demand sources but has no Howard or NTRS 20210021084 entry.

Verdict: add the complete Howard reference to the Spacevalue bibliography and label the DSEV figure as architecture-specific modeled capacity. The 500,000 kg/yr scenario value is unchanged; rc-381 separately reviews its annualization and scope. rc-788. Extracted: extracted_data/r908_spacevalue_dsev_bibliography_gap.csv.

## R963 — Water utility factors by destination (2026-11-19)

spacevalue_water_utility_factors_code_main_2026: At Spacevalue main 69549f772a43d155dc27d5ae5f01f90a7e4ce996, `catalog.py` line 512 calls the utility values “ENGINEERING JUDGEMENTS, NOT MEASUREMENTS” and states that no market exists to calibrate them. Water is 1.00 in the base map (line 527), 0.80 at GEO (line 709), 0.60 at `lunar_surface` (line 772), and 0.25 at `mars_surface` (line 827); LEO, cislunar and Mars orbit inherit the base value, and GTO aliases GEO. The helper at lines 932–944 returns the destination override or base factor; lines 1421–1422 apply that fraction to launch cost avoided and subtract processing cost in the in-space price calculation.

Verdict: open rc-823 for a destination-matched derivation or calibration of the four water coefficients. The code comments give qualitative use and local-supply rationales, not a derivation for the numeric fractions. This is distinct from rc-296’s silicate-versus-water shielding/feedstock comparison and rc-638’s frozen cislunar worksheet source-path review. No numeric replacement inferred. Extracted: `extracted_data/r963_water_utility_factor_scope.csv`.

## R987 — Frozen Stage 2 market ceilings and utility path scoped upstream (2026-11-19)

At Economicspace main e354cdda8d5471a04a78509de78def8f4ef2a6b9 (PR #214, master 1.84.0), the new `campaign/stage2/PROVENANCE.md`, mirroring the Stage 3 file, records the frozen annual_market_kg rows as destination budgets times class shares, allocation scenarios: cislunar 100,000 kg/yr (rc-636), Mars surface 20,000 (rc-653) and Mars orbit 60,000 (rc-655), with Kornuta 2019, LunA-10 and NASA NTRS 20240002713 as context only; and cislunar utility as the base IN_SPACE_UTILITY profile, its override being empty (rc-638). The verification worksheet prints the entry beside any Stage 2 input whose row carries the recorded value, in a span its backing check strips, so each input stays NEED BACKING. No frozen CSV byte or value moves.

Verdict: rc-636, rc-638, rc-653, rc-655 closed as applied. Extracted data: none new.

## R992 — Spacevalue water utility factors labelled scenarios (2026-11-19)

spacevalue_083_main_water_silicate_scenario_review_2026: at Spacevalue main 8d165b08e6702cc9245ef23437587e9a6ecfa013 (PR #20, package 0.8.3, data contract 1.22.1), catalog.py calls the base and destination water factors 1.00, 0.80, 0.60 and 0.25 “SCENARIOS,” states they lack a buyer/local-supply/market calibration, and gives the price sensitivity: every 0.10 factor change moves water's price by 0.10 times that destination's launch cost avoided. Values and generated prices are unchanged.

Verdict: rc-823 applied by scenario labeling and explicit sensitivity; no numeric replacement inferred. Extracted: extracted_data/r992_spacevalue_water_utility_scenario_sensitivity.csv.

## R995 — Spacevalue water-propellant pathway scope (2026-11-19)

`spacevalue_083_main_water_silicate_scenario_review_2026`: Spacevalue main `8d165b08e6702cc9245ef23437587e9a6ecfa013` says water is propellant feedstock and that “electrolysis is the only processing step between raw ice and a fuelled depot.” The comment names no architecture or source for this universal pathway claim.

`spacecost_water_resistojet_reference_row_current_2026`: Spacecost main `a6901495d257cbcd018b31e238498c94f301c865`, water row 20 describes water as a propellant directly, without electrolysis. Sekine et al., Table 3 (printed p. 282), report on-orbit AQUARIUS water-resistojet operation on EQUULEUS. NASA's PTD-1 release describes the different HYDROS-C path: water electrolysis followed by combustion of hydrogen and oxygen. These sources establish distinct routes, not the extraction energy for water from asteroid ice.

**Verdict:** open **rc-864** to scope the electrolysis statement to a specified chemical-propellant architecture, cite the relevant route, and distinguish water extraction/conditioning from propellant conversion. The utility factors remain unchanged; closed **rc-823** covers their scenario labels and sensitivity. Extracted: `extracted_data/r995_spacevalue_water_propellant_path_scope.csv`.
