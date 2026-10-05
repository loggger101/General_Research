# Domain 15 — In-space demand & market absorption

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY`, `IN_SPACE_UTILITY_BY_DESTINATION`, `IN_SPACE_ANNUAL_DEMAND_KG` and `_DEMAND_SHARE_BY_CLASS`, and `modules/calc.py` `market_model`, `demand_elasticity` and `surplus_price_fraction`: how much of a delivered kilogram sells at each destination, and at what price.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Upstream labels every in-space number here as judgement ("the single biggest soft assumption in the in-space case"), and no domain covered how a market absorbs a delivery once it is a sizeable share of annual supply. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `mineral_value.py` `IN_SPACE_UTILITY` (base profile, used at LEO, cislunar and Mars orbit) | water 1.00; Fe, Ni, Co, Cu, nickel-iron, awaruite 0.70; magnetite 0.40; carbon 0.40; troilite 0.30; silicates 0.25; organics 0.20; everything unlisted, every precious metal included, 0.0 | "ENGINEERING JUDGEMENTS, NOT MEASUREMENTS" |
| `IN_SPACE_UTILITY_BY_DESTINATION` `geo` | water 0.80; Fe, Ni, Co, Cu, nickel-iron, awaruite 0.15; magnetite, troilite, silicates, carbon, organics 0.05 | judgement: a GEO depot exists to refuel and service satellites, and nothing is manufactured there |
| `IN_SPACE_UTILITY_BY_DESTINATION` `lunar_surface` | water 0.60; iron, nickel-iron, awaruite 0.45; magnetite 0.25; silicates 0.03 | judgement: local regolith FeO, ilmenite and polar ice compete with imports |
| `IN_SPACE_UTILITY_BY_DESTINATION` `mars_surface` | water 0.25; iron, nickel-iron, awaruite 0.40; magnetite, troilite 0.15; organics 0.05; silicates, carbon 0.02 | judgement: ground ice, hydrated regolith and the CO2 atmosphere compete with imports |
| `IN_SPACE_ANNUAL_DEMAND_KG` | leo 500,000; cislunar 100,000; mars_orbit 60,000; lunar_surface 50,000; geo 40,000; mars_surface 20,000 kg/yr | "JUDGEMENT, not measurement; no such market exists". The geo row is built from ~550 active GEO satellites at ~70 kg/yr of station-keeping propellant, with no source given; mars_orbit is scaled from DRA 5.0 propellant per opportunity |
| `_DEMAND_SHARE_BY_CLASS` | propellant 0.55, structural 0.25, shielding 0.15, chemical 0.05, trace 0.0005 | "JUDGEMENT, like everything else in this block" |
| `calc.py` `market_model` | `capacity_cap`: constant price up to a kg/yr ceiling per commodity | modelling choice; `elasticity` is the alternative mode |
| `calc.py` `demand_elasticity` | 0.5 in P/P0 = (1 + Q/Q_market)^(-1/eps), read only when `market_model` is `elasticity` | "0.5 is inelastic, which is right for precious metals: doubling world supply quarters the price"; no source |
| `calc.py` `surplus_price_fraction` | 0.5 of full price for each kg past a ceiling (`sell_surplus_at_discount` is True) | "there is no market study behind it" |

**What a source has to supply.**

- For the utility factors: what an in-space buyer would pay for delivered material relative to launching the same mass from Earth, by commodity and destination (propellant depots, satellite servicing, in-space manufacturing feedstock, surface bases).
- For the annual ceilings: quantified demand forecasts, such as propellant demand for LEO and cislunar refuelling, the GEO fleet's station-keeping propellant use (fleet size times kg/yr per satellite), and the consumables and propellant budgets of lunar and Mars base architectures.
- For the class shares: the mass breakdown, by category, of what an outpost or depot imports.
- For the elasticity and the surplus price: measured price elasticities of demand for the PGMs and minor metals, and observed price responses when supply rose sharply relative to annual production.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `hein2020` (domain 2): its registry mapping lists a Pt demand curve and the water-vs-Pt market split.
- `usgs_mineral_commodity_summaries_2026` (domain 6): the terrestrial ceilings in `ANNUAL_WORLD_PRODUCTION_KG`.
- `dra5_2009_human_exploration_of_mars` (domain 3): the propellant-per-opportunity basis of the mars_orbit ceiling.

**Boundary.** Domain 6 holds the prices and the terrestrial annual-production ceilings (`ANNUAL_WORLD_PRODUCTION_KG`). This domain covers how much sells, and at what discount, once a delivery is a sizeable share of a ceiling, and the in-space ceilings, which have no source at all.

## R77 - Cross-references updated (2026-09-27; registry unchanged at 267)

`hein2020`, listed in the opening block under domain 2, is now in domain 22.

## R80 - First sources registered (2026-09-28; registry 277 -> 282)

Five T2 rows, four NTRS-hosted full texts pulled live this machine (sha256 in the manifest), one paywalled companion registered as `registered_not_pulled`. All five venues confirmed by Crossref DOI checks; all four NTRS copyright determinations read off each record.

**What each source supplies against the R75 brief.**

- `lynch_2024_iss_logistics_mass_and_crew_time` (ICES-2024-132, NTRS 20240005648): **the LEO ceiling and class shares**. 'roughly 134 metric tons of logistics were delivered to the ISS' between Oct-2017 and Dec-2023 (~21.5 t/yr) — an order-of-magnitude anchor for `IN_SPACE_ANNUAL_DEMAND_KG['leo'] = 500,000 kg/yr`, which is ~23x the observed ISS logistics rate (the ceiling was always a market-absorption judgement, not an ops figure). The six SAO categories ('six main categories defined by NASA's SAO: consumables, maintenance, spares, outfitting, utilization, and packaging') are the closest published analogue to `_DEMAND_SHARE_BY_CLASS`. Per-delivery splits show consumables dominance in practice: SpX-24 '3.1 metric tons of cargo, of which 2.8 tons were consumables' (~90%); Progress 80 '~3.4 t ... with 3.1 tons being consumables'; NG-17 split across all categories (1.5/1.0/0.85/~0.54 t). Table A-1 (all 79 launches, dates) is in `extracted_data/r80_iss_delivery_history_tableA1.csv`. **Limitation:** Figure 2's per-category percentages are raster-only; vision timed out on this machine R80 — the category split stays figure-level.
- `lynch_et_al_2023_logistics_rates_beyond_leo` (AIAA 2023-4617, NTRS 20230012635): **the lunar-surface ceiling and what an outpost actually imports**. Worked example: 'is 436.7 kg' total delivered mass for a 2-crew x 14-day lunar-surface mission (non-regenerative ECLSS; excludes EVA consumables/spares, vehicle spares/maintenance, utilization) — Tables 16-21 extracted to `extracted_data/r80_lunar_surface_example_tables16-21.csv`. Scaled: ~31 kg/crew-day of delivered logistics for a short surface stay with no regenerative ECLSS; upstream's `lunar_surface = 50,000 kg/yr` ceiling is ~4x that rate — directionally consistent. Per-item rates (Tables 1-15) give the first registered basis for the water-heavy class split: oxygen/water/gas carriers dominate mass (water+carriers 137.4 + gas+carriers 169.4 = 306.8 kg of the 436.7 total, ~70%; solid goods 29.8%).
- `chu_2006_goes_r_stationkeeping_momentum_management` (AAS 06-046, NTRS 20060012315): **the GEO row's physics**. 'north-south maneuvers require about 50 d s velocity change (Av) each year and east-west maneuvers require about 1.3 d s Av each year' — OCR garbles the units ('d s'); arithmetic against the daily figures (~13 cm/s, ~0.35 cm/s per day) confirms m/s annual totals. The paper states NO propellant mass; deriving one (assumption: Isp = 250 s hydrazine, g0 = 9.81): total dv ~51.3 m/s/yr (+~3.7 m/s/yr if the stated daily momentum dumps are included) is ~85-113 kg/yr for a 4,000-5,000 kg spacecraft — brackets upstream's geo-row comment '~550 active GEO satellites at roughly 70 kg/yr' in order of magnitude (the derivation, not the paper, supplies that number). 'Momentum dumps of about 25 Nms are also needed each day for spacecraft with unbalanced solar arrays'.
- `tiffin_friz_2022_space_superhighway_systems_analysis` (AIAA ASCEND 2022, doi 10.2514/6.2022-4203, NTRS 20220013397): **the cislunar architecture**. First registered source for the tug+depot logistics network: 'A fairly conservative 9.2 km/s total DV to reach a 200 km circular LEO has been assumed for now'; 'the fact that the DV to return from NRHO to LEO is over 7 km/s, the reusable tugs still had appreciable performance'; 'Assuming their life cycle is 10 years, each tug only completes 2-3 missions total'. Feeds `cislunar = 100,000 kg/yr` and the mars_orbit depot concept (transport infrastructure, not settlement).
- `tiffin_friz_rosenthal_2022_space_superhighway_cost_analysis` (AIAA ASCEND 2022, doi 10.2514/6.2022-4254): **the $/kg price side** — the cost-analysis companion of the systems paper above; both NTRS copies carry copyright determinationType=MAY_INCLUDE_COPYRIGHT_MATERIAL (not hostable) and arc.aiaa.org returns HTTP 403 from this machine, so it is `registered_not_pulled` until a legal copy is obtained.

**Still open in this domain.** Utility factors by commodity/destination remain judgement — no source prices delivered material relative to launch cost; demand elasticity (eps=0.5) and the 0.5 surplus-price fraction have no registered basis; Figure-2 category percentages await a vision-capable pass or an OCR install.


## R84 - First demand-forecast sources for the JUDGEMENT cells (2026-09-30; +4 rows -> registry 309)

The `IN_SPACE_ANNUAL_DEMAND_KG` and utility-factor cells labelled 'JUDGEMENT, not measurement' got their first external anchors - four new sources, two hosted CC BY full texts (Birch et al. 2026 ROXY economics; Steinert et al. 2024 lunar-depot flight cost), one DARPA LunA-10 study hosted on its public-release distribution statement A, and the Kornuta et al. 2019 collaborative study read in full from a co-author-hosted copy (publisher copy is TDM-only; ScienceDirect bot-blocks this machine).

Against upstream's cells:
- **Kornuta et al. 2019** (REACH, Crossref-checked): near-term annual demand of lunar-derived propellant **450 MT/yr** (= 2,450 MT water -> $2.4B revenue) vs our cislunar row 1e5 kg = ~4.5x; customer-input early need ~**1,640 MT/yr**; Moon-only scenario starts at 100 MT/yr (2x the lunar_surface row). Seven scenarios with demand and price per customer mix ($7,500/kg Moon-only down to $1,482/kg all-customers average); electrolysis 4.41 kWh/kg propellant; NPV positive in every multi-customer scenario at a 10% discount rate; ~$4B initial investment at $35k/kg launch to the surface.
- **LunA-10** (T4 grey): projected annual market value $1.6B-$8B = **500-2,500 MT/yr** of cislunar propellant transport under an explicit Starship price ladder ($300-600/kg LEO -> ~$1,400-2,600/kg GEO -> ~$2,000-3,800/kg Moon); deep-space fuel 100 MT/trip; GEO refueling >300 MT/yr.
- **Steinert et al. 2024** (Frontiers in Space Technologies): the first per-kg flight-cost anchor for cislunar/lunar transport - location-dependent mass cost of ilmenite-reduction O2 to a specific NRHO depot, delta-v band 2,414.35-2,985.65 m/s, base configuration 23.9 t O2/yr, Argonaut reference launcher (closes the standing 'd15 per-kg $ anchors for cislunar/lunar transport' gap at least in kind).
- **Birch et al. 2026** (Aerospace): a ~1 t O2/yr ISRU pilot plant is viable with IRR up to +47.4% when oxygen AND metals are sold - i.e. early lunar-surface demand (life support) precedes propellant scale-up, supporting the shape of the `lunar_surface` utility profile rather than any single cell value.

No re-pin proposed: upstream labels the block judgement and 'no such market exists', so **rc-056 is opened as a note** recording these anchors for whenever the owner revisits the JUDGEMENT block. Extracted data: `extracted_data/r84_cislunar_demand_forecasts_key_numbers.csv` (24 rows).

## R92 - First direct per-satellite station-keeping propellant-mass anchors for the GEO row (2026-10-01; +3 rows -> registry 324)

Upstream's `geo` row of IN_SPACE_ANNUAL_DEMAND_KG is "the only row here anchored on hardware that EXISTS: ~550 active geostationary satellites at roughly 70 kg/yr of station-keeping propellant each" (economicspace@7d99662, comment above the geo cell). The registry's existing d15 source for it - chu_2006_goes_r_stationkeeping_momentum_management - states only a delta-v budget (~50 m/s/yr N/S, ~1.3 m/s/yr E/W) and "states no propellant mass directly". This round registers the three sources that supply both missing halves:

- **Rawlin & Majcher 1991** (NASA-TM-105153 / AIAA 91-2347; T2, full text hosted - NTRS GOV_PUBLIC_USE_PERMITTED): the first source stating per-satellite north-south stationkeeping propellant MASS. Table I defaults: annual NSSK delta-v = 46 m/s/yr over a 15-yr mission for a 1640 kg dry-mass spacecraft; Table VIII outputs: chemical case "SK [N]SSK propellant mass (kg) = 459.3043" (= **30.62 kg/yr** at Isp 310 s, reserve fraction 0.042 - a Tsiolkovsky cross-check from the stated inputs reproduces it within +0.18%) and ion-EP case "NSSK propellant mass (kg) = 69.28853" (= **4.62 kg/yr** at Isp 2,467 s). Both sit below upstream's ~70 kg/sat/yr total-station-keeping figure as expected: N/S is one component of N/S + E/W + margin (the same split chu_2006 documents in delta-v terms); the EP case also quantifies the mass trade - 459.3 -> 69.3 kg propellant at a ~+210.8 kg dry-mass cost.
- **NASA KSC practice PD-ED-1253** (Lewis Research Center, April 1996; T2, full text hosted - US government work, no licence statement anywhere): institutional per-thruster comparison. Table 2 caption verbatim: "N/S stationkeeping propellant mass comparison for a 12 Year, 1700 kg dry mass satellite." - hydrazine monoprop (Isp 220) **532 kg**, biprop MMH/N2H4 (Isp 302) **373 kg**, resistojet (Isp 302) **373 kg**, arcjet (Isp 520) **207 kg** ("*Does not include dry mass penalty of approximately 20 kg") = **44.3 / 31.1 / 31.1 / 17.3 kg/sat/yr**. Same page, verbatim: "a delta velocity of approximately 49 m/s/year must be added in the north or south direction" (for 0.05-0.1 degree positional accuracy) and N/S propellant "can represent up to 80% of the mass of total propellant". The band brackets upstream's ~70 kg/sat/yr from below, consistent with it being a total-station-keeping figure.
- **McDowell 'Space Activities in 2025'** (GCAT Rev 1.2; T3 dataset publication - verified live not pulled: no licence statement anywhere so the copy is recorded by size + sha256 only): anchors the FLEET-COUNT half of the row. Table 22 GEO population as of Jan 2026: active payloads **below GPZ 7 / GPZ+/-100 km 613 / graveyard 18 = total 638** (dead 779, debris 510). Upstream's "~550" is therefore now low by **+11.4%** (in-orbit operational band) to **+16.0%** (all active); at upstream's own implicit per-satellite figure of 72.7 kg/yr (= 40,000 / 550), the row would be ~44,600-46,400 kg/yr.

**rc-057 is opened (kind=value) proposing a re-pin**: update the fleet count in the comment and set `geo` to ~44,600-46,400 kg/yr at upstream's own per-satellite figure; no contradiction on the mass side - every institutional N/S-only figure found this round (17.3-44.3 kg/sat/yr) sits below the total-station-keeping ~70 as it should. Extracted data: `extracted_data/r92_geo_stationkeeping_propellant_key_numbers.csv` (16 rows).

## R113 - NASA's stated ISRU production scale against the demand judgements (2026-10-04; +2 sources, T2x2)

economicspace `modules/mineral_value.py` `IN_SPACE_ANNUAL_DEMAND_KG` (read at economicspace@29a0309): cislunar 100,000, lunar_surface 50,000, mars_orbit 60,000, mars_surface 20,000 kg/yr, labelled JUDGEMENT. R80 anchored the cislunar row on Kornuta et al. (2019)'s 450 t/yr lunar-propellant forecast.

- **`sanders_kleinhenz_2024_isru_space_mining_unoosa`** (NASA JSC, UNOOSA policy symposium; read live, not hosted because NTRS marks it may include copyright material). NASA's space-resources vision (p3; "not currently funded or approved"): 30-60 t per lander mission, 100s-1000s t/yr for cislunar space, 100s t/yr for human Mars transportation, and 10s of t/yr of commodities as the initial commercial goal.
- **`araghi_2022_nasa_lunar_isru_technology_overview`** (NASA JSC, hosted). Capability-gap targets for a first lunar plant (p19): at least 10 t O2/yr from regolith, 15,000 kg/yr of icy-regolith processing, 10,000 kg/yr of oxygen clean-up, electrolysis at 10s of t/yr, each for 3 years.

Against upstream: the cislunar 100 t/yr sits at the bottom of NASA's 100s-1000s t/yr band (and below Kornuta's 450 t/yr), the lunar_surface 50 t/yr matches "10s of t/yr" and five first plants at Araghi's oxygen target, and mars_orbit + mars_surface (80 t/yr) is below "100s of t/yr for human Mars transportation". These are agency vision and plant targets, not market forecasts, so they bracket the judgement cells without pinning them. No revision candidate.

Extracted data: `extracted_data/r113_isru_production_targets.csv` (11 rows).

## R114 - GEO stationkeeping propellant and commodity elasticities (2026-10-04; +9 sources, T1x1, T2x7, T4x1)

The GEO row of `IN_SPACE_ANNUAL_DEMAND_KG` rests on about 550 satellites at about 70 kg/yr of station-keeping propellant, with no source. The owner's list supplied five studies; read against that figure:

| source | stationkeeping propellant | note |
|---|---|---|
| `lamorte_2020_geostationary_satellite_electric_propulsion_master_thesis` (T4) | 65.3 kg/yr chemical; 11.1 kg/yr Hall | one-year simulation, one satellite; chemical is 6.7% below 70 |
| `snyder_2001_iepc_172_dual_mode_spt_geosynchronous_satellites` | 244 kg xenon over 15 years (about 16 kg/yr) | 3,500 kg dry mass, 48.5 m/s per year of north-south delta-v |
| `sovey_pidgeon_1990_advanced_propulsion_leo_geo_platforms` | arcjet 51% and ion 25% of the hydrazine baseline; about 138 kg/yr chemical implied (computed) | 8,000 kg-class 1990 platform; the owner's list misread 51% as a share of platform mass |
| `oleson_1995_advanced_propulsion_geo_insertion_nssk` | assumptions only (Isp 600-3,160 s, tankage 0.07-0.15) | 15-year NSSK model |
| `zhang_2016_xips_station_keeping_failure_mode_eclipse_constraints` | none in the abstract | optimisation method, unread |

Chemical stationkeeping is therefore consistent with 70 kg/yr (65 to about 138 kg/yr by satellite size), but electric propulsion cuts the figure to roughly 11-16 kg/yr, and the row does not say which fleet it assumes. That is a clarification for the owner, not a revision candidate.

`bogmans_2024_power_of_prices_commodity_supply_demand_elasticities` (IMF WP 2024/077) is the first institutional elasticity source for `demand_elasticity` (0.5): minerals are 'particularly inelastic', copper and zinc demand near zero, crude oil and coal below 0.2, and elasticities rise at longer horizons. It does not cover PGMs. `vertier_2025_banque_de_france_eco_notepad_419_price_elasticity_critical_mineral_supply` (found at a new URL after the listed one returned 404) is the first source that includes PGMs: for eight critical minerals a 1% demand-driven price rise raises mine output by about 0.5% over five years (0.2-1% across the horizon). That is a supply elasticity, so the match with `demand_elasticity` 0.5 is in magnitude only. `sanders_2010_iac_lunar_isru_isecg_reference_architecture` adds a demonstration-scale figure (about 250 kg of oxygen a year), and `esa_2019_space_resources_strategy` quotes a 2018 Luxembourg study that expects EUR 73-170B of space-resources revenue over 2018-2045 (EUR 2.7-6.3B a year, computed), for a product mix that excludes propellant oxygen and asteroid PGMs, so it is context for the top-down demand cells, not a check on them. Rejected: a learning-curve explainer built on the solar example (Round 114 log entry). Undecided: a USITC trade-shifts page (Akamai 403) and an AFIT paper (it downloads as a file the app browser would not open). No revision candidate.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.
