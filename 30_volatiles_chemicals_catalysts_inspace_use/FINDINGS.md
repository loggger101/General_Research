# Domain 30 — Volatiles, process chemicals & catalyst metals in space

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY` and `IN_SPACE_UTILITY_BY_DESTINATION`, the rows in `_COMMODITY_CLASS` classes `"propellant"` (water, ammonia), `"chemical"` (carbon, organics, carbon dioxide, carbonates, sulfur, phosphorus, oldhamite, merrillite, chlorapatite) and `"trace"` (the PGMs and their ores, gold, silver, gallium, germanium, rhenium, tungsten, molybdenum), and the comment that records why PGMs get no catalyst utility at the surface destinations: what each volatile, process chemical and trace metal is used for in space and how well it replaces the launched alternative.

Created in Round 161 (2026-10-13). Blocks are appended one per round, newest last.

## R161 - Domain opened with three NASA sources (2026-10-13; +3 T2, all full_text_hosted)

**Why this domain.** See the domain 28 opening block. This domain holds upstream's propellant, chemical and trace classes, which together carry the highest utility in the table (water 1.00) and the lowest (every precious metal 0.00).

**Cells, read at economicspace@8dc759f** (`modules/mineral_value.py`):

| cell | base (LEO, cislunar, mars_orbit) | geo | lunar_surface | mars_surface | upstream's stated basis |
|---|---|---|---|---|---|
| water | 1.00 | 0.80 | 0.60 | 0.25 | "propellant feedstock, radiation shielding, life support and coolant; electrolysis is the only processing step" |
| ammonia | 0.60 | 0.40 | 0.60 | 0.30 | nitrogen for a habitat "plus a resistojet propellant" |
| carbon dioxide | 0.30 | 0.05 | 0.30 | 0.02 | "the carbon feed for Sabatier methane" |
| carbon / organics | 0.40 / 0.20 | 0.05 / 0.05 | 0.40 / 0.20 | 0.02 / 0.05 | "composites, plastics, agriculture feedstock" |
| carbonates | 0.25 | 0.05 | 0.03 | 0.02 | "the CO2 source, and otherwise shielding rock" |
| sulfur / phosphorus | 0.10 / 0.10 | 0.05 / 0.05 | 0.10 / 0.10 | 0.05 / 0.10 | "process chemicals and fertiliser" |
| PGMs, Au, Ag, PGM ores, Ga, Ge, Re, W, Mo | 0.00 (default) | 0.00 | 0.00 | 0.00 | "nobody in orbit buys them for their own sake"; valued by shipping down |
| rejected alternative | PGMs 0.05 at the two surfaces | | | | "a crewed base runs fuel cells, electrolysers and Sabatier reactors and wants Pt/Pd/Ru catalysts", dropped because the pipeline cannot blend a kg-scale catalyst market with the terrestrial one |

**What a source has to supply.** Performance of each volatile as propellant or life-support consumable against the launched alternative (Isp, storability, processing steps); the mass of catalyst and process chemical an ISRU plant or habitat consumes; and evidence on in-space uses of the trace metals.

**Sources registered (all NTRS public-use, hosted under `full_texts/`):**

- `degroot_1997_electrolysis_propulsion_spacecraft_tm113157` (NASA TM-113157 / AIAA 97-2948, `GOV_PUBLIC_USE_PERMITTED`). Water electrolysed on board and burned as GH2/GO2 has "performance measured at an Isp of over 350 s", 355 s on a 22-N thruster over 69,000 firings, projected above 380 s with radiation-cooled chambers, "superior to earth storable chemical alternatives"; water stores at 1.0 g/cc in light low-pressure tanks. Stoichiometric GH2/GO2 may need "iridium-coated rhenium" chambers.
- `morren_1987_multipropellant_resistojet_space_station_tm100113` (NASA TM-100113 / AIAA 87-2120, `GOV_PUBLIC_USE_PERMITTED`; the file declares itself a work of the U.S. Government not subject to copyright). The space-station resistojet was baselined to provide drag make-up "while disposing of a variety of fluids expected to be present in excess quantities on board", measured on hydrogen, helium, methane, steam, nitrogen, air, argon and carbon dioxide at Isp 93-385 s; steam reached 184 s with a separate boiler and 159 s with the thruster as boiler.
- `franco_2019_sabatier_catalyst_mars_isru_ices2019_077` (ICES-2019-077, NASA KSC, `PUBLIC_USE_PERMITTED`). Sabatier methanation for a Mars ISRU plant uses "transition metal catalysts (such as ruthenium or nickel)"; the tests compared a nickel catalyst with 0.5% and 2% Ru coatings on alumina, for a plant sized at 8.03 kg CH4/day (6978 kg over the campaign).

`lewis_1992_asteroid_resources_sp509_vol3` (domain 29) gives C1 chondrites up to 20% bound water, 6% organic matter and 11% magnetite, with nitrogen, sulfur and carbonates present; cited here by id.

**Against the cells.**

- Water 1.00: one kilogram of delivered water is at least as good as one kilogram of launched storable propellant (`degroot_1997_electrolysis_propulsion_spacecraft_tm113157`), and stores more easily than cryogens. Supports the base row as a drop-in substitute; the destination overrides are about local supply and are outside these sources.
- Carbon dioxide 0.30 and organics 0.20: `morren_1987_multipropellant_resistojet_space_station_tm100113` documents a direct low-Isp propellant use (resistojet drag make-up) for CO2 and methane on top of the Sabatier feed use upstream cites; a non-zero value is supported, its size is not.
- Ammonia 0.60: no source yet. `morren_1987_multipropellant_resistojet_space_station_tm100113`'s fluids do not include ammonia; the resistojet and nitrogen make-up uses upstream cites still need an anchor.
- Trace class 0.00 and the rejected 0.05: `franco_2019_sabatier_catalyst_mars_isru_ices2019_077` shows that the catalyst use is real but a percent-level Ru coating on an alumina support, with nickel as the substitute, which supports upstream's kilogram-scale catalyst market (trace share 0.0005 in domain 15) and its reasoning for dropping the 0.05. `degroot_1997_electrolysis_propulsion_spacecraft_tm113157`'s Ir/Re chambers are a second real in-space use of PGM-group and refractory metals, but as parts made on Earth.

**No revision candidate.** Extracted data: `extracted_data/r161_volatiles_chemicals_catalysts_key_numbers.csv`.

**Still open.** Ammonia and nitrogen consumption by habitats (ECLSS make-up rates) and ammonia arcjet/resistojet performance; catalyst inventories of ECLSS (ISS Sabatier, oxygen generation) and of fuel cells, in kg of PGM per system; sulfur and phosphorus demand by in-space processing and agriculture.

**Boundary.** Domains 3, 10 and 14 hold launched propellant performance and price; domain 5 holds ISRU and storage; domain 19 holds processing energy; domain 15 holds demand and class shares.
