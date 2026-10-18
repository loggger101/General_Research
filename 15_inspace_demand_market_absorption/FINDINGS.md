# Domain 15 — In-space demand & market absorption

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY`, `IN_SPACE_UTILITY_BY_DESTINATION`, `IN_SPACE_ANNUAL_DEMAND_KG` and `_DEMAND_SHARE_BY_CLASS`, and `modules/calc.py` `market_model`, `demand_elasticity` and `surplus_price_fraction`: how much of a delivered kilogram sells at each destination, and at what price.

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
| `zhang_2016_xips_station_keeping_failure_mode_eclipse_constraints` | none in the abstract | unread |

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

rc-123: cite the IMF elasticities (below 0.5 short-run) and not the Banque de France supply figure for `demand_elasticity`. Text in `revision_candidates.csv`.
