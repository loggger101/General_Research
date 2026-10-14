# Domain 29 — Structural metals, alloys & in-space manufacturing

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY` and `IN_SPACE_UTILITY_BY_DESTINATION`, the rows in `_COMMODITY_CLASS` class `"structural"` (iron, nickel, cobalt, copper, chromium, titanium, nickel-iron, awaruite, kamacite, taenite, tetrataenite, cohenite, schreibersite, and the ores magnetite, ilmenite, chromite, perovskite, troilite and the Fe/Ni sulfides): how good a substitute raw asteroid metal is for structure launched from Earth, given that the plant that turns it into parts is not costed.

Created in Round 161 (2026-10-13). Blocks are appended one per round, newest last.

## R161 - Domain opened with two NASA sources (2026-10-13; +2 T2, both full_text_hosted)

**Why this domain.** See the domain 28 opening block: Round 161 split the engineering basis of the in-space utility factors into three domains by upstream's commodity classes. This one holds the structural class. Upstream's reason for the 0.70 is the gap between raw metal and a usable part: "raw Fe-Ni is not a pressure vessel, and the melting / forming plant that turns it into one is not costed anywhere in this pipeline." The energy and plant cost of refining are separate cells (`IN_SPACE_PROCESSING_KWH_PER_KG`, domain 19); the 0.70 is what is left once those are paid.

**Cells, read at economicspace@8dc759f** (`modules/mineral_value.py`):

| cell | base (LEO, cislunar, mars_orbit) | geo | lunar_surface | mars_surface |
|---|---|---|---|---|
| iron, nickel-iron, awaruite, kamacite, taenite, tetrataenite, cohenite, schreibersite | 0.70 | 0.15 | 0.45 | 0.40 |
| nickel, cobalt, copper | 0.70 | 0.15 | 0.70 (no lunar ore) | 0.70 (no martian ore) |
| chromium, titanium | 0.70 | 0.15 | 0.45 | 0.40 |
| magnetite | 0.40 | 0.05 | 0.25 | 0.15 |
| chromite / ilmenite / perovskite | 0.40 | 0.05 | 0.25 / 0.03 / 0.03 | 0.02 |
| troilite, pyrrhotite, pentlandite, niningerite, daubreelite | 0.30 | 0.05 | 0.30 | 0.15 |

Stated bases: the base 0.70 is "Discounted for the in-space manufacturing gap"; geo's 0.15 is because "There is no manufacturing at GEO" (the plant is "implausible", not merely uncosted); the surface overrides are local regolith iron, ilmenite and chromite competing with imports; ores sit lower because they "need reducing first".

**What a source has to supply.** Mechanical and compositional fitness of asteroid metal (Fe-Ni alloys, kamacite/taenite) as structural feedstock; the state, mass, power and throughput of in-space metal forming and additive manufacturing; and what fraction of an outpost's structural mass could come from such a plant.

**Sources registered (both NTRS public-use, hosted under `full_texts/`):**

- `lewis_1992_asteroid_resources_sp509_vol3` (NASA SP-509, Space Resources vol. 3, chapter "Asteroid Resources", `GOV_PUBLIC_USE_PERMITTED`). Asteroid material worth exploiting is volatiles, free metals and bulk dirt. Ordinary-chondrite metal "could be processed to provide very pure iron and nickel for use in structures in LEO", with cobalt, the PGMs, gallium, germanium and arsenic as byproducts; chondrites carry free metals and volatiles at about 100 times their concentration in lunar soil. Iron meteorites reach crushing strengths of 3600 bar (360 MPa, computed) at room temperature, and "iron asteroids, if found, would present significant processing challenges".
- `roberts_2023_nasa_tmp_in_space_manufacturing_metals_sff` (NASA MSFC, Solid Freeform Fabrication Symposium 2023, `PUBLIC_USE_PERMITTED`; hosted as the .docx NTRS serves, the record has no PDF). NASA's on-demand manufacturing of metals project was cancelled before flight; its FabLab bound-metal printer's sintering furnace drew about 2250 W against a 2000 W target (12.5% over, computed); deriving feedstock from in-situ resources is the third and last (infusion) phase of the plan. It cites ISS logistics of about 13,000 kg of prepositioned spares plus 18,000 kg premanufactured on the ground.

**Against the cells.**

- Base 0.70: the use is real (Lewis: pure Fe and Ni for LEO structures), and so is the gap. Raw meteoritic metal is a feedstock, hard to process, and NASA's own in-space metals manufacturing never reached flight. Both support a discount below 1.0; neither gives its size. No source registered here quantifies the fraction of a launched structural kilogram that an asteroid kilogram replaces.
- geo 0.15: the forming plant that the base row assumes away does not yet exist in flight form even at the ISS, which supports upstream's argument that one at GEO is implausible.
- Ores (0.40, 0.30): Lewis notes C1 chondrites carry up to 11% magnetite, and that free metal is the attractive form; reduction energy for the ores is domain 19's cell.
- Byproducts: Lewis lists Ga and Ge as "high value and utility in an industrial economy", which upstream holds at 0.00 in space ("nobody in orbit buys them for their own sake"); his claim is about Earth's economy, so there is no conflict.

**No revision candidate.** Extracted data: `extracted_data/r161_structural_metals_manufacturing_key_numbers.csv`.

**Still open.** Tensile and fracture properties of meteoritic Fe-Ni (kamacite, taenite, tetrataenite) against structural steels; in-space metal forming demonstrations (such as the ESA metal 3D printer delivered to the ISS in 2024) and their mass and power; carbonyl (Mond) refining of asteroidal Fe-Ni; the share of a habitat or depot's structural mass that could be locally made.

**Boundary.** Domain 19 holds the refining and forming energy and plant cost (`IN_SPACE_PROCESSING_KWH_PER_KG`, plant $/kg); domain 25 holds terrestrial refining terms; domain 15 holds the demand side.
