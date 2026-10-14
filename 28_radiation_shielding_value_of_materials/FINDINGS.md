# Domain 28 — Radiation-shielding value of in-space materials

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY` and `IN_SPACE_UTILITY_BY_DESTINATION`, the rows whose in-space use is bulk radiation shielding (every silicate and oxide phase, hibonite, and the rock-valued carbonates, oldhamite and phosphates), the shielding part of water's row, and the `"shielding"` default of `_COMMODITY_CLASS`: how much protection a delivered kilogram of each material buys compared with the same mass launched from Earth.

Created in Round 161 (2026-10-13). Blocks are appended one per round, newest last.

## R161 - Domain opened with five NASA shielding reports (2026-10-13; +5 T2, all full_text_hosted)

**Why this domain.** The owner asked for domains covering the utility of each element, compound and alloy in space, so that in-space prices are more accurate. economicspace prices a kilogram delivered to an in-space destination at its utility factor times the launch cost it avoids (`in_space_price_usd_per_kg`), and the utility factors are labelled "ENGINEERING JUDGEMENTS, NOT MEASUREMENTS". Domain 15 holds those tables as market cells (demand, class shares, elasticity). No domain held the engineering question underneath each factor: what a kilogram of the material can do in its role. Round 161 opened three domains split by upstream's own commodity classes: this one (shielding), 29 (structural metals and alloys) and 30 (volatiles, process chemicals and catalyst metals).

**Cells, read at economicspace@8dc759f** (`modules/mineral_value.py`):

| cell | current value | upstream's stated basis |
|---|---|---|
| `IN_SPACE_UTILITY` olivine, pyroxene, orthopyroxene, enstatite, plagioclase, spinel, phyllosilicates, oxides, silicates | 0.25 (base profile: LEO, cislunar, mars_orbit) | "Usable as bulk radiation shielding and as 3-D-printing / sintering feedstock, but a poor per-kg substitute for engineered structure" |
| `IN_SPACE_UTILITY` hibonite; carbonates, oldhamite, merrillite, chlorapatite | 0.25 | "shielding rock at 0.25" (their S, P and CO2 are priced as those elements) |
| `IN_SPACE_UTILITY` water | 1.00 | "propellant feedstock, radiation shielding, life support and coolant" (shielding is one of four uses) |
| `IN_SPACE_UTILITY_BY_DESTINATION` `geo`, the same rock rows | 0.05 | "Bulk shielding is the one real use for rock here ... nobody bolts raw olivine to a comsat" |
| `IN_SPACE_UTILITY_BY_DESTINATION` `lunar_surface`, the same rock rows | 0.03 | "Shipping silicate rock to a body made of silicate rock" |
| `IN_SPACE_UTILITY_BY_DESTINATION` `mars_surface`, the same rock rows | 0.02 | "Basalt, everywhere, for free" |
| `_COMMODITY_CLASS` default | `"shielding"` for any unclassified name | an import-time assertion now requires every row to be classed |

**What a source has to supply.** Shielding effectiveness per unit mass of water, silicate rock or regolith, and metal, under one radiation environment and one risk measure, so that the rock rows can be stated as a fraction of water's shielding value; and the same at a planetary surface, where local regolith competes.

**Sources registered (all NTRS, all `GOV_PUBLIC_USE_PERMITTED`, no copyright statement in any file; hosted under `full_texts/`):**

- `townsend_1990_gcr_shielding_requirements_tm4167` (NASA TM-4167). For the 0.5 Sv/yr blood-forming-organ limit at solar minimum: 3.5 g/cm2 of water, 6.5 g/cm2 of aluminum or 1.0 g/cm2 of liquid hydrogen; at 0.25 Sv/yr the mass ratio is 1:5:11 for LH2:water:aluminum. Aluminum needs 1.86 times the mass of water at the first limit and 2.2 times at the second (computed here).
- `kim_wilson_1994_gcr_shield_materials_performance_tp3473` (NASA TP-3473). A shield performance index that varies by up to a factor of 20 across materials at constant mass, and "the unique role of hydrogenous materials". Its Figs 13 and 15 plot water, liquid hydrogen, lithium hydride, liquid methane, lunar regolith, regolith with 10% epoxy, iron, copper, aluminum and lead on one axis; they are figures only, so no number is taken from them yet.
- `wilson_1997_gcr_spe_shielding_deep_space_tp3682` (NASA TP-3682). To bring the 5-cm-depth dose equivalent at solar minimum to 45 cSv takes about 55 g/cm2 of aluminum but 17 g/cm2 of polyethylene (3.2 times, computed; "approximately a factor of 3" in the text), and aluminum construction used as shielding is "clearly not cost-effective".
- `kim_1998_martian_meteorites_regolith_shield_materials_tp1998_208724` (NASA/TP-1998-208724). Five groups of Martian meteorites give the same dose as the Martian regolith model within 0.5% and the same dose equivalent within 1%; 30 wt% epoxy in the regolith lowers dose equivalent at 50 g/cm2 by 13%. Rock type does not matter; hydrogen does.
- `slaba_mertens_blattnig_2013_radiation_shielding_optimization_mars_tp2013_217983` (NASA/TP-2013-217983). In free space the first 20 g/cm2 of shielding cuts dose equivalent 45-65%, and aluminum-like material gives no significant benefit past about 45 g/cm2. On the Martian surface dose equivalent rises 63% as aluminum goes from 0 to 100 g/cm2, and regolith helps only at several hundred g/cm2.

`lewis_1992_asteroid_resources_sp509_vol3` (registered in domain 29) names "bulk dirt needed for shielding in low Earth orbit" as one of the three asteroid products with an in-space use; it is cited here by id.

**Against the cells.**

- Water: the sources rank hydrogen-rich material first per kilogram, and give aluminum 1.86-2.2 times the shield mass of water for the same limit. Water's 1.00 bundles shielding with three other uses, so this bounds its shielding share without pinning the row.
- Silicate rows (0.25): `kim_1998_martian_meteorites_regolith_shield_materials_tp1998_208724` supports valuing every silicate phase alike, as upstream does. No source here gives silicate or regolith against water per kilogram in text. `kim_wilson_1994_gcr_shield_materials_performance_tp3473` plots it (Fig 13), and digitising that figure is the next step for this domain. The ratio upstream implies (water 1.00 against rock 0.25, a factor of 4) is therefore neither confirmed nor contradicted. It sits above the 1.9-2.2 that water holds over aluminum, so it is consistent with rock being no better than aluminum per kilogram, which nothing registered contradicts.
- `mars_surface` 0.02 and `lunar_surface` 0.03: `slaba_mertens_blattnig_2013_radiation_shielding_optimization_mars_tp2013_217983` finds that on Mars surface aluminum-like mass raises exposure and that regolith is useful only in amounts that need large-scale excavation, and `kim_1998_martian_meteorites_regolith_shield_materials_tp1998_208724` finds imported meteoritic rock equivalent to local regolith. Imported rock buys almost nothing at a surface base; consistent with the overrides.
- `geo` 0.05: `slaba_mertens_blattnig_2013_radiation_shielding_optimization_mars_tp2013_217983`'s free-space curve (most of the benefit in the first 20 g/cm2, none past 45 g/cm2 for aluminum-like material) means a satellite gains little from bulk rock; consistent with the near-zero value.
- Metal rows: `wilson_1997_gcr_spe_shielding_deep_space_tp3682` finds aluminum a poor GCR shield and credits hydrogen content, which metals lack; `kim_wilson_1994_gcr_shield_materials_performance_tp3473` plots iron and copper beside aluminum (Fig 13, figure-only). The structural metal rows (domain 29) should take no credit for shielding, and upstream gives them none.

**No revision candidate.** The cells are labelled judgement, and every finding above bounds or supports them. Extracted data: `extracted_data/r161_shielding_by_material_key_numbers.csv`.

**Still open.** A text-stated (or digitised) per-kg ratio of silicate regolith to water; solar-particle-event shielding by material (the GEO and LEO cases are SPE- and trapped-belt-dominated, not GCR-dominated); and asteroid-specific compositions (CI/CM rock with bound water would shield better than dry silicate).

**Boundary.** Domain 15 keeps the market side of the same tables (`IN_SPACE_ANNUAL_DEMAND_KG`, `_DEMAND_SHARE_BY_CLASS`, elasticity, surplus price) and the economic studies that price delivered material. This domain holds the physics of what a kilogram shields.
