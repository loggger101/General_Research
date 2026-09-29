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
