# Domain 29 — Structural metals, alloys & in-space manufacturing

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY` and `IN_SPACE_UTILITY_BY_DESTINATION`, the rows in `_COMMODITY_CLASS` class `"structural"` (iron, nickel, cobalt, copper, chromium, titanium, nickel-iron, awaruite, kamacite, taenite, tetrataenite, cohenite, schreibersite, and the ores magnetite, ilmenite, chromite, perovskite, troilite and the Fe/Ni sulfides): how good a substitute raw asteroid metal is for structure launched from Earth, given that the plant that turns it into parts is not costed.

Created in Round 161 (2026-10-13). Blocks are appended one per round, newest last.

## R161 - Domain opened with two NASA sources (2026-10-13)

Round 161 split the engineering basis of the in-space utility factors into domains 28-30 by upstream's commodity classes; this one holds the structural class. Upstream's reason for the 0.70: "raw Fe-Ni is not a pressure vessel, and the melting / forming plant that turns it into one is not costed anywhere in this pipeline." Refining energy and plant cost are separate cells (`IN_SPACE_PROCESSING_KWH_PER_KG`, domain 19).

**Cells** (economicspace@8dc759f):

| cell | base (LEO, cislunar, mars_orbit) | geo | lunar_surface | mars_surface |
|---|---|---|---|---|
| iron, nickel-iron, awaruite, kamacite, taenite, tetrataenite, cohenite, schreibersite | 0.70 | 0.15 | 0.45 | 0.40 |
| nickel, cobalt, copper | 0.70 | 0.15 | 0.70 (no lunar ore) | 0.70 (no martian ore) |
| chromium, titanium | 0.70 | 0.15 | 0.45 | 0.40 |
| magnetite | 0.40 | 0.05 | 0.25 | 0.15 |
| chromite / ilmenite / perovskite | 0.40 | 0.05 | 0.25 / 0.03 / 0.03 | 0.02 |
| troilite, pyrrhotite, pentlandite, niningerite, daubreelite | 0.30 | 0.05 | 0.30 | 0.15 |

Bases: 0.70 is "Discounted for the in-space manufacturing gap"; geo 0.15 because "There is no manufacturing at GEO"; surface overrides reflect local regolith iron, ilmenite and chromite; ores sit lower because they "need reducing first".

**What a source has to supply:** mechanical and compositional fitness of asteroid metal as structural feedstock; state, mass, power and throughput of in-space metal forming; the fraction of an outpost's structure such a plant could supply.

**Sources (hosted):**

- `lewis_1992_asteroid_resources_sp509_vol3` (NASA SP-509 vol. 3): useful asteroid products are volatiles, free metals and bulk dirt. Ordinary-chondrite metal "could be processed to provide very pure iron and nickel for use in structures in LEO", with Co, PGMs, Ga, Ge and As as byproducts; chondrites carry free metals and volatiles at ~100x lunar-soil concentration. Iron meteorites reach crushing strengths of 3600 bar (360 MPa), and "iron asteroids, if found, would present significant processing challenges". C1 chondrites carry up to 11% magnetite.
- `roberts_2023_nasa_tmp_in_space_manufacturing_metals_sff` (MSFC, SFF Symposium 2023; hosted as the .docx NTRS serves): NASA's on-demand metals manufacturing project was cancelled before flight; the FabLab sintering furnace drew ~2250 W against a 2000 W target (12.5% over); ISRU feedstock was the last phase of the plan. ISS logistics: ~13,000 kg of prepositioned spares plus 18,000 kg premanufactured.

**Against the cells:** both support a discount below 1.0 for base 0.70 without sizing it; the absence of a flown plant even at the ISS supports geo 0.15; Lewis's Ga/Ge "high value" refers to Earth's economy, so no conflict with upstream's 0.00 in space. `extracted_data/r161_structural_metals_manufacturing_key_numbers.csv`. No candidate.

**Boundary:** domain 19 holds refining and forming energy and plant cost; domain 25 terrestrial refining terms; domain 15 the demand side.

## R167 - ISS metal-forming demonstrations; logistics anchors (2026-10-14)

- `prater_et_al_2021_metal_am_processes_for_iss_sampe_nexus` (SAMPE neXus 2021; NTRS abstract copy hosted, the full paper's record carries copyright): "two processes in development as payloads for an ISS technology demonstration: wire+arc additive manufacturing (the Vulcan payload from Made in Space, Inc.) and bound metal deposition (the Fabrication Laboratory from Techshot, Inc)". roberts_2023_nasa_tmp_in_space_manufacturing_metals_sff records their cancellation (May 2023).
- From `roberts_2023_nasa_tmp_in_space_manufacturing_metals_sff`: "Current up-mass costs for passive cargo to low-Earth Orbit is $20,000 per kilogram while down-mass costs exceed $40,000 per kilogram"; CLPS "$300,000 per kilogram to lunar orbit and $1.2 M per kilogram to the lunar surface" (Astrobotic's listed prices); "No mechanical testing capabilities or volumetric testing capabilities currently exist for in-space applications".
- From `nasa_2026_isam_state_of_play` p.266: ESA's metal 3D printer "was the first metal printer installed on ISS", melting stainless wire (~1400 C); four reference prints compared with Earth copies; operational from 2024.

Forming in microgravity is demonstrated, but NASA's plant never flew and there is no on-orbit mechanical testing, so 0.70 and geo 0.15 stand. `extracted_data/r167_inspace_metals_manufacturing_key_numbers.csv`. No candidate.

## R173 - Meteoritic Fe-Ni strength; carbonyl-refining source named (2026-10-15)

- `ueki_mine_takashima_2021_taenite_kamacite_microtensile_scirep` [T1, CC BY, hosted]: micro-tensile tests on Canyon Diablo single crystals: kamacite "350 MPa and 19%" (p3), taenite "935 MPa and 65%" (nitrogen strengthening); cohenite cleaves at 2.4 GPa without plastic flow (p2). Bulk tests read "less than ca. 100 MPa" because cohenite cracks dominate (p1).
- `mulford_ei_dasher_2011_fe_ni_meteorite_strength_indentation` [T2, public domain, hosted; LANL/LLNL via OSTI]: indentation and EBSD on Canyon Diablo, Gibeon, Wabar and Laguna Manantiales: composite strength "higher by almost an order of magnitude than values obtained from laboratoryprepared specimens" (p2); "Strength in all of the meteorite samples examined here was higher than predicted for ironnickel alloys prepared in the laboratory, and higher than can be accounted for by inclusion of carbon in these alloys." (p4).
- `knox_1970_yield_strength_meteoritic_iron` [T1, registered_not_pulled]: the original yield-strength study (0.2% flow stress in Canyon Diablo, Odessa, Brenham metal; ~63 / ~47 / ~63 K psi per the indexed abstract, to verify on pull).
- `iyer_kelly_2022_lci_critical_materials_ni_cu_ti_ree` [T3, registered_not_pulled]: Argonne's GREET nickel life-cycle inventory including the carbonyl step (Ni matte + CO -> Ni(CO)4 -> Ni). Both routes refuse this machine (DOWNLOADS.md).

Constituent yields of ~350 MPa (kamacite) to >900 MPa (taenite) and composite strength above fabricated alloys mean the raw metal is structurally competitive: the discount sits in the manufacturing gap, not the material. `extracted_data/r173_fe_ni_mechanical_properties_key_numbers.csv`. No candidate.

## R174 - Locally-made share closed at its accessible limit (2026-10-15)

No institutional source states the share of habitat or depot structural mass that could be made locally: NTRS habitat-structure papers (Ziglar/Boeing 20250009434 and 20240011787; IAC-22-C2.1.12 20220013154) compare Earth-shipped options, and Hammond et al. 20060007799 (In Situ Fabrication) gives plant state only; lewis_1992_asteroid_resources_sp509_vol3 says nothing on manufacturing. The structural rows stay judgement; the domain's opening brief is closed.

Upstream drift checked: spacecost dbb2cde (v0.11.0) and economicspace 4bd500c add a GTO refuelling destination with no reference-CSV change; `_GTO_DEORBIT_DV_M_S` = 16 m/s re-derived from vis-viva (apogee 1.5974 vs 1.5815 km/s, delta 15.9 m/s). No candidate.
