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
## R167 - ISS metal-forming demonstrations at program level + institutional logistics anchors (2026-10-14; +1 T2 full_text_hosted)

**Why these.** The R161 opening block left four items open: meteoritic Fe-Ni mechanical properties, 'in-space metal forming demonstrations (such as the ESA metal 3D printer delivered to the ISS in 2024) and their mass and power', carbonyl refining of asteroidal Fe-Ni, and the locally-made share of a habitat's structure. This round closes the second at program level - both NASA-side flight candidates are now on record with named hardware, and ESA's printer is cross-cited from an already-registered source - plus extracts two institutional logistics anchors that were sitting unextracted inside roberts_2023.

**Source registered (NTRS public-use, hosted under `full_texts/`):**

- `prater_et_al_2021_metal_am_processes_for_iss_sampe_nexus` (SAMPE neXus 2021; DOI Crossref-verified this round). The NTRS record is the single-page abstract copy - the full paper's twin record (20205011519) carries MAY_INCLUDE_COPYRIGHT_MATERIAL, so only the public-use presentation version was pulled. 'There are currently two processes in development as payloads for an ISS technology demonstration: wire+arc additive manufacturing (the Vulcan payload from Made in Space, Inc.) and bound metal deposition (the Fabrication Laboratory from Techshot, Inc)' - i.e. at a point when ODMM still had funding, both forming routes behind the 0.70 discount were real flight candidates with named hardware; roberts_2023 then records their fate (furnace module + process gas drawer canceled May-2023).

**Cross-cited extractions from already-registered sources** (by id, per the R147 convention):

- `roberts_2023_nasa_tmp_in_space_manufacturing_metals_sff` carries two logistics anchors unextracted until this round: 'Current up-mass costs for passive cargo to low-Earth Orbit is $20,000 per kilogram while down-mass costs exceed $40,000 per kilogram', and CLPS lunar delivery at '$300,000 per kilogram to lunar orbit and $1.2 M per kilogram to the lunar surface' (Astrobotic Peregrine's publicly listed prices as cited by NASA) - institutional-grade context for d15's transport cells; plus 'No mechanical testing capabilities or volumetric testing capabilities currently exist for in-space applications', which is why the gap behind 0.70 does not close with hardware alone.
- `nasa_2026_isam_state_of_play` p.266 PGM07: ESA's Metal 3D printer 'was the first metal printer installed on ISS that demonstrated the simplicity of metallic part production under microgravity environment' - high-power lasers melting stainless-steel wire (~1400 C), four reference prints compared against Earth copies, Status Operational from 2024. This is the demonstration d29's open list named.

**Against the cells.**

- Base 0.70: both forming routes were flight candidates with named hardware (Vulcan, FabLab) and one foreign analogue has now actually flown (MELT, operational from 2024) - the use is real AND demonstrated in microgravity; but NASA's own plant was canceled before flight and no NDE/mechanical-testing capability exists on-orbit, so the discount stays. Consistent with upstream's 'the melting / forming plant that turns it into one is not costed anywhere'; no re-pin.
- geo 0.15: unchanged - none of the three demonstrations operated at GEO; 'no manufacturing at GEO' still holds as a statement about what exists, not just what was planned.

**No revision candidate.** Extracted data: `extracted_data/r167_inspace_metals_manufacturing_key_numbers.csv` (5 rows x 6 cols). Still open from R161's list: meteoritic Fe-Ni mechanical properties vs structural steels; carbonyl refining of asteroidal Fe-Ni; the locally-made share of a habitat or depot's structure.
## R173 - Meteoritic Fe-Ni mechanical properties closed + carbonyl-refining source named (2026-10-15; +2 T1/T2 full_text_hosted, +1 T1 and +1 T3 registered_not_pulled)

**Why these.** The R167 closing block left three items open: meteoritic Fe-Ni tensile/fracture properties against structural steels, carbonyl (Mond) refining of asteroidal Fe-Ni, and the locally-made share of a habitat or depot's structure. This round closes the first with measured data at both scales (constituent-level micro-tensile + government-lab indentation), names THE source for the second (the GREET nickel life-cycle inventory that models the carbonyl step), and documents why the third has no institutional source yet.

**Sources registered:**

- `ueki_mine_takashima_2021_taenite_kamacite_microtensile_scirep` [T1, full_text_hosted cc-by 4.0; Scientific Reports 11:4750 (26 Feb 2021), DOI Crossref-verified live this round]. The first constituent-level micro-tensile study of meteoric iron: FIB-machined single-crystal gauges from Canyon Diablo give kamacite yield '350 MPa and 19%' elongation-to-failure (p3) - in agreement with the Gibeon tensile-test estimate cited there - while taenite reaches '935 MPa and 65%', i.e. ~2.7x the kamacite yield at HIGHER ductility, attributed to nitrogen solid-solution strengthening in a Ni-rich FCC matrix (p1). Cohenite cleaves on (011) without plastic deformation at a maximum tensile strength of 2.4 GPa (p2), which is exactly why bulk measurements read low: 'Most measurements of their mechanical properties determined tensile strengths less than ca. 100 MPa, which are relatively low values compared to that of artificial iron-nickel alloys' (p1).
- `mulford_ei_dasher_2011_fe_ni_meteorite_strength_indentation` [T2, full_text_hosted public-domain; LANL/LLNL LA-UR presentation for the International Symposium on Plasticity, Puerto Vallarta Jan 2-8 2011; pulled from OSTI purl/1038894 - no NTRS record exists]. Government-lab Vickers/spherical-indentation + EBSD study across Canyon Diablo, Gibeon, Wabar and Laguna Manantiales: 'indicated that the strength of the composite was higher by almost an order of magnitude than values obtained from laboratoryprepared specimens' (p2; OCR-compressed spacing as printed), and the conclusion is unqualified - 'Strength in all of the meteorite samples examined here was higher than predicted for ironnickel alloys prepared in the laboratory, and higher than can be accounted for by inclusion of carbon in these alloys.' (p4). The unexpectedly high yields correlate with localized crystallite strain seen in EBSD.
- `knox_1970_yield_strength_meteoritic_iron` [T1, registered_not_pulled; Meteoritics 5(2):63-74 June 1970, DOI Crossref-verified live this round]. THE original measured yield-strength study - flow stresses required to produce 0.2% plastic strain in a recrystallized Canyon Diablo specimen, the Odessa octahedrite and the metal phase of Brenham (per publisher abstract as indexed by search engines: ~63 / ~47 / ~63 K psi; verify on pull). Wiley's article page is Cloudflare-challenged from this machine; queued in DOWNLOADS.md R173.
- `iyer_kelly_2022_lci_critical_materials_ni_cu_ti_ree` [T3, registered_not_pulled; Argonne National Laboratory report, OSTI 1905473 / DOI Crossref-verified live this round]. THE life-cycle inventory behind GREET's nickel production models - process description plus energy and material flows for the carbonyl-refining step (CO reaction with Ni matte to form Ni(CO)4, then thermal decomposition back to Ni), covering domestic and international geographies with ore-grade variation per OSTI's own record annotation. Both full-text routes (osti.gov/servlets/purl/1905473 + publications.anl.gov/anlpubs/2022/12/178670.pdf) are Cloudflare-challenged from this machine; OpenAlex and Semantic Scholar both flag the work OA via exactly those URLs. Queued in DOWNLOADS.md R173 - once pulled, d29's carbonyl item is anchored with its process + energy source on record.

**Against the cells.** No re-pin: none of upstream's structural-metal cells carries an absolute strength or processing-energy value that these sources would contradict - Lewis 1992 already records 'crushing strengths up to 3600 bar' for iron meteorites and the IN_SPACE_UTILITY rows are manufacturing-gap discounts (base 0.70 / geo 0.15), not material-property cells. The new data is context/bound class: it shows measured constituent yield running from ~350 MPa (kamacite) to >900 MPa (taenite) with composite strength an order of magnitude above fabricated alloys - i.e. the raw metal is structurally competitive, so the discount behind those rows really does sit in the manufacturing gap, not the material.

**Still open.** The locally-made share of a habitat or depot's structural mass: no institutional source quantifies it yet (it is a forward-looking design estimate; NASA's own ISAM record - roberts_2023 and nasa_2026_isam_state_of_play, both already registered here - documents the plant state but not a share). Remains an upstream judgement row.

**No revision candidate.** Extracted data: `extracted_data/r173_fe_ni_mechanical_properties_key_numbers.csv` (6 rows x 6 cols; all quoted spans verified count==1 against the in-repo hosted copies before writing artifacts).
