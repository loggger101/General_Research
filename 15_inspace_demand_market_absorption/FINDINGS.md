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
