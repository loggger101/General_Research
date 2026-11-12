## R669 — Titanium sponge annual-market source and vintage (2026-11-12)

- `spacevalue_titanium_annual_market_code_current_2026`: `catalog.py` sets `ANNUAL_WORLD_PRODUCTION_KG["titanium"] = 3.2e8` kg/year (~320,000 metric tons sponge), attributed to MCS 2025 for 2024 and described as excluding the U.S.
- `usgs_mcs2026_titanium_chapter`: the World Sponge Metal Production table (“World total (rounded)” row, printed p. 197) reports 380,000 metric tons for revised 2024 and 370,000 for 2025e. Footnote 3 excludes Utah production; the U.S. row is zero in 2025.
- Verdict: re-pin the ceiling to a named year and update the exclusion wording. The latest estimate of 370,000 metric tons is 50,000 metric tons (15.6%) above the current value. **rc-531**. Extracted: `extracted_data/r669_titanium_annual_market_basis.csv`.
- `spacevalue_rhenium_annual_market_code_current_2026`: `catalog.py` sets 62,000 kg/year (~62 t), attributed to MCS 2025 for 2024. `usgs_mcs2026_rhenium_chapter` reports 79,800 kg for revised 2024 and 81,000 kg for 2025e in its world mine-production table (printed p. 157); footnote 7 excludes secondary rhenium.
- Verdict: re-pin to the selected year; 81,000 kg is 19,000 kg (30.6%) above the current value. **rc-532**. Extracted: `extracted_data/r669_rhenium_annual_market_basis.csv`.
- `spacevalue_gallium_annual_market_code_current_2026`: `catalog.py` sets 760,000 kg/year of primary gallium, matching MCS 2025 for 2024. `usgs_mcs2026_gallium_chapter` reports 848,000 kg for revised 2024 and 900,000 kg for 2025e in its world low-purity primary-production table (printed p. 83).
- Verdict: re-pin to the selected year and preserve the low-purity primary measure; 900,000 kg is 140,000 kg (18.4%) above the current value. **rc-533**. Extracted: `extracted_data/r669_gallium_annual_market_basis.csv`.

## R668 — Elemental phosphorus annual-production basis (2026-11-12)

- `spacevalue_phosphorus_annual_market_code_current_2026`: `catalog.py` sets `ANNUAL_WORLD_PRODUCTION_KG["phosphorus"] = 1.0e9` kg/year (~1 Mt elemental P₄). A table-level note attributes terrestrial figures broadly to USGS MCS annual primary production.
- `matos_etal_2021_jrc_elemental_phosphorus_energy`: the European Commission JRC report says “The precise world production of elemental phosphorus is not known” and estimates 900–1,200 kt/year (§7.2, printed p. 31).
- `usgs_mcs2026_phosphate_rock_chapter`: the World Mine Production and Reserves table (“World total (rounded)” row, printed p. 143) reports 239,000 thousand metric tons of marketable phosphate rock for 2024 and 250,000 for 2025e; this is a different product measure and does not establish global elemental-P₄ production.
- Verdict: 1 Mt/year is within the JRC range, so no numeric replacement is supported. Identify the elemental-P₄ source and estimate vintage or label the current value as an approximate scenario. **rc-529**. Extracted: `extracted_data/r668_phosphorus_annual_market_basis.csv`.
- `usgs_mcs2026_tungsten_chapter`: the “World total (rounded)” row reports 82,000 metric tons tungsten content for 2024 and 85,000 for 2025e (printed p. 201). `spacevalue_tungsten_annual_market_code_current_2026` records the current 81,000 t/year ceiling, which the code attributes to MCS 2025 for 2024.
- Verdict: use 85,000 t/year and label 2025e if the model intends the latest MCS estimate; this is 4,000 t (computed here), or 4.7%, above the current rounded value. **rc-530**. Extracted: `extracted_data/r668_tungsten_annual_market_basis.csv`.

## R667 — Ammonia annual-market estimate re-pin (2026-11-12)

- `usgs_mcs2026_ammonia_chapter`: *Mineral Commodity Summaries 2026*, Nitrogen (fixed)—ammonia, printed p. 136, defines data in thousand metric tons of nitrogen content. The World Ammonia Production and Reserves table reports 156,000 for 2024 and 160,000 for 2025e; the text notes “Significant revisions were made to the 2024 production” for Egypt and Germany.
- `spacevalue_ammonia_annual_market_code_current_2026`: `catalog.py` sets `ANNUAL_WORLD_PRODUCTION_KG["ammonia"] = 1.5e11` kg N/yr (~150 Mt N), with no source edition or production year on the row. The source row in registry history is MCS 2025 world plant production for 2024e; rc-055 applied the same 150 Mt N re-pin in economicspace.
- Verdict: MCS 2026 revises 2024 production to 156 Mt N and estimates 160 Mt N for 2025. Re-pin the Spacevalue ceiling to a named year and current edition; both values use nitrogen content and world plant production. **rc-528**. Extracted: `extracted_data/r667_ammonia_annual_market_basis.csv`.

## R666 — Sulfur annual-market source and year (2026-11-12)

- `usgs_mcs2026_sulfur_chapter`: the World Production and Reserves table (chapter PDF p. 2) reports 83,900 thousand metric tons for 2024 and 84,000 for 2025e; the text says “World sulfur production in 2025 was an estimated 84 million tons compared with 83.9 million tons in 2024.” The previously registered MCS 2025 sulfur chapter reports 85 million tons for 2024 (printed p. 173).
- `spacevalue_sulfur_annual_market_code_current_2026`: `catalog.py` sets `ANNUAL_WORLD_PRODUCTION_KG["sulfur"] = 8.3e10` (~83 Mt/yr) without a source edition or production year on the row. The table-level note attributes terrestrial figures broadly to MCS annual primary production; INDEX maps this inherited sulfur row to MCS 2025.
- Verdict: the current value is close to the 2026 USGS estimates but does not match the rounded 2024 or 2025 MCS 2026 world totals. Identify its source vintage and whether 83 Mt is a scenario or a stale annual production figure; no numeric replacement inferred. **rc-527**. Extracted: `extracted_data/r666_sulfur_annual_market_basis.csv`.

## R665 — Carbon dioxide terrestrial annual-market basis (2026-11-12)

- `iea_2019_putting_co2_to_use`: IEA, *Putting CO2 to Use* (2019), Executive summary p. 3, estimates “some 230 million tonnes (Mt)” of CO2 are used annually, including 130 Mt for urea and 70–80 Mt for enhanced oil recovery. Printed pp. 5–6 identify IHS Markit (2018) among the inputs and describe the 2015 demand breakdown as mainly EOR and on-site urea production.
- `spacevalue_co2_annual_market_code_current_2026`: Spacevalue `catalog.py` sets `ANNUAL_WORLD_PRODUCTION_KG["carbon dioxide"] = 2.3e11` (~230 Mt/yr), comments “merchant CO2,” and uses this terrestrial ceiling for `shipped to Earth` in `annual_market_kg`. The table-level note describes terrestrial figures as USGS MCS annual primary production, which does not establish this CO2 row’s basis.
- Verdict: the IEA value is a close numerical match but represents total use, not merchant-only production; the report attributes most of it to on-site urea use and EOR. Record the missing source year and market boundary, and establish whether total use is an intentional sales-cap scenario or whether a merchant-specific measure is intended. No numeric replacement inferred. **rc-526**. Extracted: `extracted_data/r665_co2_annual_market_basis.csv`.

# Domain 2 Findings — composition → commodity value mapping

Backings: AsteroidCatalog `taxonomy_composition.csv` material fractions (metal, silicate, carbon, ice), `mineralogy.py` phase splits (`comp_phases_detailed`), `PGM_ENRICHMENT_BY_TYPE`, and spacevalue `catalog.py` mineralogy and nickel-iron yields.

## R663 — Minor-PGM annual market values lack row-level source years and measures (2026-11-12)

- **jm_pgm_market_report_2026**: the tables label the metric “Total primary supply” and report 2025 values of 7.1 t iridium (PDF p. 34), 21.8 t rhodium (p. 32), and 30.2 t ruthenium (p. 33).
- **spacevalue_pgm_annual_production_code_current_2026**: at `spacevalue@f836611f15dbb0ef511fe134bd5ac8192e3bea16`, `catalog.py` lines 897–899 stores 7.5, 23, and 30 tonnes per year, respectively. The table-level comment attributes terrestrial figures to USGS MCS annual primary production; these rows give no edition, year, or specific production measure.

The JM values are close comparators but use a separately named primary-supply series, and are not established as the code values’ source or as like-for-like mine-production replacements. Verdict: retain the numeric cells; identify the source, year, and measure for each row. **rc-524**. Extracted: `extracted_data/r663_pgm_annual_market_basis.csv`.

## R662 — Spacevalue silver market ceiling lacks its specific USGS edition and year (2026-11-12)

- **usgs_mcs2026_silver_chapter**: USGS MCS 2026, Silver chapter, printed pp. 172–173, “World Mine Production and Reserves” table, reports a rounded world total of 25,300 metric tons in 2024 and 26,000 in 2025e; its prose says “World silver mine production increased slightly in 2025 to an estimated 26,000 tons.”
- **spacevalue_silver_annual_market_code_current_2026**: at `spacevalue@f836611f15dbb0ef511fe134bd5ac8192e3bea16`, `spacevalue/catalog.py` sets `ANNUAL_WORLD_PRODUCTION_KG["silver"] = 2.6e7` (~26,000 metric tons) without identifying the USGS edition or production year on the row. The table-level comment names the USGS MCS series generally. Existing rc-302 concerns silver’s reference price and does not cover this annual market-ceiling field. Verdict: cite MCS 2026 and label the value as estimated 2025 world mine production; the published value matches, so no replacement inferred. **rc-523**. Extracted: `extracted_data/r662_silver_annual_market_basis.csv`.

## R601 — L-type conditional silicate split (2026-11-11)

- `asteroidcatalog_l_silicate_split_code_current_2026`: AsteroidCatalog assigns L-type silicates shares of 0.60 olivine, 0.30 pyroxene and 0.10 plagioclase; the adjacent code comments provide no numeric derivation.
- `de_kleer_2026_jwst_spinel_rich_l_type_mineralogy`: the registered abstract reports JWST MIRI surface spectra for five spinel-rich L-types, with Mg-rich olivine and a component interpreted as spinel or amorphous olivine; the spectra resemble oxidized CV3 Allende. It gives no conditional bulk silicate mass shares. The paper’s CAI conclusion concerns accessory phases, not the modeled 60/30/10 split.
- Verdict: request a documented L-type source-to-model mapping or identify the current shares as a scenario. These selected surface spectra do not establish a class-wide bulk mass distribution; no replacement is inferred. **rc-464** records the gap, scoped separately from rc-172’s CAI/accessory-phase question.
- Extracted: `extracted_data/r601_l_type_silicate_split_context.csv`.

## R599 — K/CV conditional silicate split (2026-11-11)

`asteroidcatalog_k_silicate_split_code_current_2026`: AsteroidCatalog@800a4ca377823edc3ea205b9069b29db147f2b63 assigns K the shared `_SIL_CV` split of olivine 0.75, pyroxene 0.20 and plagioclase 0.05; the nearby code comment identifies K with CV/CO chondrites and gives no numerical derivation. Martin et al., “REE and Hf distribution among mineral phases in the CV–CK clan,” *Geochimica et Cosmochimica Acta* 120 (2013), Table 2 (printed p. 500), report for the mapped CV3 sample NWA 5772 olivine 17.0%, low-Ca pyroxene 25.4%, matrix 47.3% and mesostasis 8.7%; the text describes the matrix as “rich in phyllosilicates.” This single CV3 sample is not a CV/CO class-wide conditional mass split, and its matrix/mesostasis categories do not map one-to-one to the model's silicate groups. The study cautions that mapped areas “may not be entirely representative for the whole rock” (printed p. 511). Verdict: request a documented CV/CO source-to-model mapping or label the 75/20/5 shares as a scenario; no replacement inferred. `rc-462`. Extracted: `extracted_data/r599_k_cv_silicate_modal_comparator.csv`.

## R598 — CK/Cgh conditional silicate split (2026-11-11)

`asteroidcatalog_ck_cgh_silicate_split_code_current_2026`: AsteroidCatalog@800a4ca377823edc3ea205b9069b29db147f2b63 assigns Cgh the modeled silicate-group shares phyllosilicates 0.50, olivine 0.40 and pyroxene 0.10; its adjacent comment says CK chondrites are olivine-rich but gives no numerical derivation. Martin et al., “REE and Hf distribution among mineral phases in the CV–CK clan,” *Geochimica et Cosmochimica Acta* 120 (2013), Table 2 (printed p. 500), report for the mapped CK4 sample NWA 5798 olivine 54.1%, low-Ca pyroxene 14.6%, high-Ca pyroxene 5.3%, plagioclase 4.2% and matrix 9.4%; the text says the matrix is nearly all recrystallized into olivine. This sample-level modal map is not a class-wide conditional mass split, and its phases do not map one-to-one to the model's three categories. The authors caution that mapped areas “may not be entirely representative for the whole rock” (printed p. 511). Verdict: request a documented CK/Cgh source-to-model mapping or label the 50/40/10 shares as a scenario; no replacement inferred. `rc-461`. Extracted: `extracted_data/r598_ck_cgh_silicate_modal_comparator.csv`.

## R597 — Oxidized-CV sulfide species split (2026-11-11)

`asteroidcatalog_detailed_sulfide_split_code_current_2026`: AsteroidCatalog@800a4ca377823edc3ea205b9069b29db147f2b63 assigns `_SULFIDE_NI` as pentlandite 0.50 / pyrrhotite 0.50 and applies it to Cgh (CK) and K (oxidized CV) detailed-phase rows. The module's own source audit says every sulfide split is unsourced as a number. Howard, Benedix, Bland & Cressey, “Modal Mineralogy of CV3 Chondrites by PSD-XRD,” LPSC 40 (2009), abstract 1235, reports total sulfide modes of 2.4–5.1 vol% for reduced CV3 and 2.9–8.1 vol% for oxidized CV3 (p. 1), and notes that CV3 subgroups are distinguished partly by “the Ni content of sulphide” (p. 1). These aggregate modal abundances and the classification criterion do not report a pyrrhotite/pentlandite ratio or establish the model's conditional mass split. Verdict: review the 50/50 split as an explicit scenario or supply a subtype-matched, species-resolved mass basis; no replacement inferred. `rc-460`. Extracted: `extracted_data/r597_cv3_sulfide_split_context.csv`.

## R592 — Terrestrial price boundary for Fe-Ni alloy phases (2026-11-11)

`spacevalue_unpriced_fe_ni_alloy_code_current_2026`: `spacevalue/catalog.py` states that the three derived Fe-Ni alloy phases have no market price of their own and passes `None` as the reference price for kamacite and taenite. Both rows still carry Fe/Ni and trace-element yield vectors. The archived economicspace Stage 2 1.12.0 Earth-surface table exports both as `unpriced`, with blank terrestrial prices; the verification sheet flags I20 and I23 and states that a missing terrestrial quote is priced as zero. Its generated `USGS/LME/mineralogy reference` label is assigned even when the quote is blank. The registered USGS iron-scrap and World Bank nickel prices are constituent-market benchmarks, not quotes for raw meteoritic kamacite or taenite. Verdict: make the Earth-sale boundary explicit (unpriced by design, or a defined Fe-Ni/trace-metal product with a matched netback source); do not present zero as a quoted market value or infer a replacement from constituent yields. `rc-456`. Extracted: `extracted_data/r592_unpriced_alloy_phase_earth_route.csv`.

## R591 — Generic terrestrial price for silicate phases (2026-11-11)

`spacevalue_silicate_reference_price_code_current_2026`: current `spacevalue/catalog.py` assigns a terrestrial reference price of 0.05 USD/kg to olivine, pyroxene, orthopyroxene, enstatite, and the catch-all silicates row. `fetch_reference_table` writes the same generic `USGS/LME/mineralogy reference` label for every row. Only olivine is described as industrial olivine sand; the rows do not identify a matching grade, sale product, delivery point, or source for the price. The economicspace verification worksheet flags its olivine, enstatite, and silicate price inputs as needing backing in the archived run. The Indian Bureau of Mines December 2025 Table 6(a) lists prices for selected minerals and grades, but no olivine or silicate-phase price; it is context only and does not validate the 0.05 USD/kg values. Verdict: cite a matching product/grade and price date for each row, or label these shared prices as engineering scenarios; no replacement inferred. `rc-455`. Extracted: `extracted_data/r591_silicate_terrestrial_price_basis.csv`.

## R568 — Ordinary-chondrite PGE phase-partition comparator (2026-11-10)

`gilmour_herd_2020_ordinary_chondrite_pge_partition` — Gilmour & Herd, Table 4 (journal pp. 679–702), report taenite/kamacite PGE partition coefficients by chondrite group: H has Ru 3.3, Pd 5.4, Os 2.1, Ir 1.9 and Pt 3.0; L has Ru 1.9, Rh 1.5, Pd 3.3, Os 2.4, Ir 2.2 and Pt 2.2; LL has Ru 3.5, Rh 3.0, Pd 4.5, Os 1.9, Ir 1.9 and Pt 2.2. The study reports higher PGE concentrations in taenite, with within- and between-grain variation. At spacevalue `catalog.py` (`spacevalue@f836611f15dbb0ef511fe134bd5ac8192e3bea16`), `_TAENITE_OVER_KAMACITE` uses Co=0.4, Cu=3.0, Pt=2.0, Pd=3.0, Au=3.0, Rh=1.5 and defaults other elements to 1.0 in deriving alloy-phase yields. The measured PGE coefficients differ from several settings and vary across H/L/LL groups; ordinary-chondrite data do not establish representative coefficients for asteroid metal classes. Verdict: comparator supports review of the generic multipliers, but no universal replacement is inferred; open `rc-433`. Extracted: `extracted_data/r568_gilmour_herd_pge_partition_coefficients.csv`.

## R1 - First sources (2026-09-17)

- **hein2020** [T1] (Acta Astronautica 174:59-71; arXiv v11 hosted until 2026-09-26, then un-hosted; moved to d22 in R77): the peer-reviewed TEA of asteroid mining, with water for space and platinum for Earth as separate markets (as the pipeline splits them). Pt demand anchored at $40,449/kg and 254,582 kg/yr, PED -0.6 to -0.5; sensitivity at $30k and $70k/kg. `extracted_data/composition_value_key_numbers.csv`. (Its "150 kg/s/kg" was a misreading: 150 kg is the craft dry mass; see R61.)
- **nat_dms2023** [T1, hosted, CC BY] (Sci Rep 13:6497): metal dissolution from metal-rich meteorite proxies with a deep eutectic solvent (ChCl:2EG). NEAs 1986 DA and 2016 ED85 show 85% surface metal / 15% silicate against the M row's metal 0.50 (surface, not bulk).
- **asime2018** [T2] (Graps et al. 2019 white paper; un-hosted): meteorites hold up to 22% water, so C-complex ice 0.10-0.30 is a population maximum; primitive, water-rich composition correlates with albedo below ~7.5% (a possible guardrail).
- **lewicki2023** [T2] (decadal white paper; un-hosted): a "Mine Project Value Curve" of value vs resource confidence.
- **cannon2023** [T1] (PSS 215:105608; CC BY-NC-ND, skipped by owner decision): which classes carry recoverable precious and structural metal.

## R2 - PGM gradient and Vesta (2026-09-17/18)

**usgs_pp1802n** [T3] (USGS PP 1802-N; public-domain excerpt quoted here):

| body / phase | Pt abundance | anchors |
|---|---|---|
| Iron meteorites ("best analogs for the composition of Earth's core") | 2.4–16 ppm (Wasson et al. 1989) | M / Xe 2.0×; Xk/E/Xc 1.5–2.0× |
| Upper mantle | ~0.002–0.005 ppm (2–5 ppb; Maier et al. 2012) | A/R/O 0.5× |
| Upper crust (basaltic) | ~0.0005 ppm (0.5 ppb; Rudnick & Gao 2003) | V 0.2× |

The enrichment factors are right to order of magnitude; the ~4-orders gap between metal and crust supports intermediate X values and 1.0 for undifferentiated types.

**toplis2014** [T2, hosted, NTRS]: Vesta's core radius 90–120 km of metal and sulphide; HEDs as parent-body analogues, supporting the differentiated-body model behind the V row.

## R3 - bennu_volatiles_2025 [T1, hosted, CC BY] (2026-09-18)

Nature Astronomy 9:199–210: OSIRIS-REx Bennu samples: total C 4.5–4.7 wt%, N 0.23–0.25 wt%, ammonia ≈40% of N; regional aliphatic/aromatic C up to ~2.5 wt%; Bennu more volatile-rich than Ryugu and most meteorites; CI/CM/CY baseline ~1–3 wt% C, rarely ~5. `extracted_data/bennu_volatiles_key_numbers.csv`. The B row's carbon_fraction 0.30 is 6-7x the measured total C, so it cannot mean elemental carbon (Round 8). Ammonia is a volatile class upstream does not model.

## R4 - C-type hydration (2026-09-18)

- **ryugu_hydrated_2023** [T1, hosted, CC BY] (Nature Astronomy 7:170–181): a dehydrated space-weathered skin (~66% of grains, ≥1.5 µm deep) over an interior retaining structural –OH. Spectral ice estimates for C-types are therefore low bounds. `extracted_data/ryugu_hydrated_interior_key_numbers.csv`.

## R8 - Per-class carbon; the CI endmember (2026-09-18)

- **glavin_2018** [T2, hosted, NTRS]: C ~0.1 wt% (CK) to ~5 wt% (CI); IDPs ~12 wt%; hydration minerals (serpentine, saponite, smectite in CI, CM, CR and Tagish Lake; tochilinite in CM2). The B/C-complex 22–30% defaults are 4–6× the most carbon-rich C-type: "carbon-bearing material", not elemental C. `extracted_data/glavin_2018_chondrite_volatiles_key_numbers.csv`.
- **ryugu_ivuna_2023** [T1] (Science 379:786; author version, not hostable): Ryugu is CI1; structural water like CI, interlayer water largely lost; below ~100 °C since alteration. Free ice is essentially absent, so ice priced at the in-space water proxy is recoverable only through dehydroxylation (d05). `extracted_data/ryugu_ivuna_2023_key_findings.csv`.

## R11 - Meteorite density and the differentiation mechanism (2026-09-18)

- **wilkinson_robinson_2000** (see d01).
- **mandler_elkins_tanton_2013** [T1, open_not_pulled]: Vesta = ~60–70% equilibrium magma-ocean crystallisation with residual melt extracted to shallow chambers: core, mantle (dunites, harzburgites, diogenites) and eucrite crust, whose PGMs went to the core. The mechanism behind `PGM_ENRICHMENT_BY_TYPE`.

## R12 - farnocchia_2024 (2026-09-18)

Second M-type density, registered here because the M row's composition and density feed both domains; the write-up is in domain 1's Round 12 block.

## R36 - Per-type material anchors (2026-09-21)

`extracted_data/r36_per_type_materials_key_numbers.csv`:

- **elkins_tanton_2020_psyche_preflight** [T1] (JGR Planets 125, CC BY-NC; author mirror): the paper the M row cites. Psyche "between ~25 vol% metal and ~60 vol% metal" (p10; Point D ~25/55/20 metal/pyroxene/pores); the M row's 0.50/0.45 mass split is ≈34 vol% metal, inside. Surface endmembers 90 wt% metal → 6 wt% opx → pure metal (p9); 25–80 km silicate veneer on a stripped core (p13); iron 7,000–8,000, pallasite 4,100–7,800, mesosiderite 3,100–7,200 kg/m³ vs Psyche ~4,000 (p10); pallasites ~65 vol% olivine, Ni ~9–12 wt% (p11); CB chondrites ~60 vol% metal vs the Cb row's 0.01 (pp11–12).
- **reddy_asteroids_iv_mineralogy** [T1] (Asteroids IV; arXiv preprint, un-hosted): A-types monomineralic olivine Fo85–93 (p8); R chondrites 65–78% olivine (p9); HED pyroxene Fs23–56 / Wo2–14 (±3 / ±1 mol%, p7); S/Q as ordinary chondrites via Dunn et al. 2010b (<2 mol%, ~50 powders); Itokawa LL with ol/(ol+pyx) 76%, Eros in the L/LL zone; A/S/Q/V analogues are 91% of meteorites (p8).
- **lodders_2010_solar_abundances** [T2] (arXiv preprint, un-hosted): Table 2 CI (Orgueil): C 34,800 ppm (3.48 wt%); Fe/Mg/Si/O/S 18.5/9.6/10.7/45.9/5.35 wt%; PGM 3.29 ppm. Carbon defaults are ~7–9× elemental C; Fe/Mg/Si agree with Cannon's Palme 2014 values within 2%. Full table: `extracted_data/lodders_2010_ci_composition_table2.csv` (incl. Ni 10,800, Co 506, Cr 2,650 ppm).

## R38 - D/T/P anchors (2026-09-21)

- **marschall_2025_67p_refractory_ice_ratio** [T1] (PSS 259:106061): 67P refractory/ice 0.5 < chi < 1.7, water 28–52 wt% (~35–40% preferred), formed at 25–35 au. D ice 0.25 and P 0.15 sit below.
- **rubin_2019_67p_abundances** [T1] (MNRAS 489:594; un-hosted): per-water CO2 4.7±1.4, CO 3.1±0.9, O2 3.1±1.1; CH4 0.34, C2H6 0.29, CH3OH 0.21, H2CO 0.32; near-solar O/Si and C/Si, N depleted (as Halley).

Every one of the 32 types now has a material anchor. `extracted_data/r38_primitive_type_materials_key_numbers.csv`.

## R61 - hein2020 plant economics (2026-09-25)

Tables 1-2: breakeven throughput "2.3*10-4 kg/s/kg, meaning that for each kg of spacecraft dry mass, 0.23 grams of material are processed per second" (7258 kg/yr per kg of craft), ~73x the plant-throughput centre (100) and above its 500 maximum even per kg of plant (24194-72582). Platinum (grade 1e-5) needs 0.35 kg/s/kg: "The spacecraft would need to be able to process the equivalent of its own mass within 3 seconds." Water $20,000/kg, Pt $70,000/kg; production cost $1,000,000 / $10,000 per kg; operations $5,700,000 / $100,000; development $5,453,333 / $500,000 per kg; refined/processed 0.05. These are profitability requirements, not plant capability: recorded, not a candidate. `22_prior_art_techno_economic_benchmarks/extracted_data/r61_hein2020_plant_economics_key_numbers.csv`.

## Maintenance (2026-09-26)

Un-hosted (arXiv default licence): hein2020, asime2018, lewicki2023, reddy, lodders_2010_solar_abundances, rubin_2019_67p_abundances; numbers extracted first. rubin_2019_67p_abundances Table 2 extras and Tables 4-5 central values in `extracted_data/unhosted_sources_key_numbers.csv` (dust + volatiles = combined in every column). New backfill rows for toplis2014 (p2), usgs_pp1802n, mandler, farnocchia.

## R70 / R71 / R72 - Extraction (2026-09-27)

- R70: `r70_bennu_volatiles_2025.csv` (15), `r70_bennu_volatiles_2025_ed_table1_CNH.csv` (13), `r70_glavin_2018.csv` (17), `r70_marschall_2025_67p_refractory_ice_ratio.csv` (95), `r70_nat_dms2023.csv` (15), `r70_ryugu_hydrated_2023.csv` (8), `r70_toplis2014.csv` (6).
- R71: `r71_asime2018_key_numbers.csv`, `r71_lewicki2023_key_numbers.csv`, `r71_lodders_2010_key_numbers.csv`, `r71_lodders_2010_table3_ci_solar_recommended_abundances.csv` (83), `r71_lodders_2010_table6_protosolar_abundances.csv` (83), `r71_lodders_2010_table8_nuclide_abundances.csv` (287), `r71_reddy_asteroids_iv_key_numbers.csv`, `r71_reddy_asteroids_iv_spectral_calibrations.csv`, `r71_rubin_2019_key_numbers.csv`, `r71_rubin_2019_table2_67p_bulk_ice_composition.csv` (44), `r71_rubin_2019_table3_67p_elemental_ratios_to_oxygen.csv`, `r71_rubin_2019_table4_67p_elements_per_si.csv`, `r71_rubin_2019_table5_67p_dust_ice_split.csv`, and USGS PP1802-N Tables N2-N5, N7, N10 (`r71_usgs_pp1802n_tableN2_nonmagmatic_pge_occurrences.csv`, `r71_usgs_pp1802n_tableN3_placer_platinum_production.csv`, `r71_usgs_pp1802n_tableN4_identified_pge_resources.csv`, `r71_usgs_pp1802n_tableN5_pge_intrusions.csv`, `r71_usgs_pp1802n_tableN7_crustal_pge_concentrations.csv`, `r71_usgs_pp1802n_tableN10_pge_deposit_grade_tonnage.csv`, 137 deposits; `r71_usgs_pp1802n_key_numbers.csv`). rubin's image-read error superscripts checked against pages.
- R72: `r72_lodders_2010_tables4_5_7_solar_mass_fractions.csv` (73; X+Y+Z = 1; Table 5 Z 1.41 / 1.22 / 1.69 %). economicspace's nickel-iron yields (IIIAB, 35.5 ppm PGM) relative to Pt: Ru 0.20, Os 0.13, Ir 0.27, Pd 0.67, Rh 0.10 vs CI 0.72, 0.52, 0.50, 0.59, 0.15; CI PGM in metal (19.6 wt% Fe+Ni+Co) ~17 ppm; iron meteorites fractionate Ir/Os/Ru, so no candidate. Hein's elasticity sweep 0.08-0.95 ("not below 0.25") agrees with 0.5.

## R73 - Elkins-Tanton and Ryugu read (2026-09-27)

- `elkins_tanton_2020_psyche_preflight` (post-erratum): `r73_elkins_tanton_2020_key_numbers.csv`, `r73_elkins_tanton_2020_table1_psyche_diameter_volume.csv`, `r73_elkins_tanton_2020_table2_psyche_mass_density.csv`; densities = mass / Viikinkoski volume (226 km) within 0.2%; adopted 3,780 +/- 340 kg/m3 (3,400-4,100). **rc-009 withdrawn**: the abstract, summary and conclusions say ~30 vol% (Sec 2.5 ~25; p5 27%), matching upstream's "roughly 30-60%".
- ryugu_ivuna_2023: H2O 6.84 +/- 0.34 wt% (interlayer 0.30 +/- 0.01, structural 6.54 +/- 0.32); Ivuna 12.73 (6.58 interlayer); C 4.63 +/- 0.23 wt% (organic 3.08 +/- 0.30); alteration at 37 +/- 10 C, 5.2 Myr after CAIs. Supports rc-014 (ice is structural water). Upstream C carbon 0.04 sits between organic 3.1 and total 4.6 wt%. `r73_ryugu_ivuna_2023_key_numbers.csv`.

## R74 - Upstream citations registered (+8)

`pearson_2006_carbon_nitrogen_carbonaceous_chondrites` and `lauretta_2024_bennu_in_the_laboratory` (C-complex carbon); `jarosewich_1990_meteorite_chemical_analyses` (S/Q metal); `kargel_1994_metalliferous_asteroids_precious_metals` (PGM baseline caveat); `fornasier_2010_m_type_spectroscopic_survey` (Xk/Xe and M mapping); `lodders_2003_solar_abundances_condensation_temperatures`, `wright_fleischer_1965_usgs_b1214a_geochemistry_platinum_metals`, `nichiporuk_brown_1965_pt_pd_iron_meteorites` (nickel-iron PGM yields).

## R77 - hein2020 moved to d22

Files now at `22_prior_art_techno_economic_benchmarks/extracted_data/r61_hein2020_plant_economics_key_numbers.csv`, `22_prior_art_techno_economic_benchmarks/extracted_data/r71_hein2020_key_numbers.csv`, `22_prior_art_techno_economic_benchmarks/extracted_data/r71_hein2020_table3_pt_supply_demand_profitability.csv`. Shared CSVs staying here: `extracted_data/composition_value_key_numbers.csv`, `extracted_data/unhosted_sources_key_numbers.csv`.

## R83 - Mineralogy-phase citations registered (+11)

From AsteroidCatalog@6a2cfbc `mineralogy.py` and economicspace CITATIONS.md, all `registered_not_pulled`:

- `scott_wasson_1975_classification_properties_iron_meteorites`: iron-meteorite trace metals (Ga/Ge/Mo/W/Re) behind nickel-iron yields.
- `dunn_cressey_2010_xrd_modal_mineral_abundances_ordinary_chondrites`: S/Sq/Q silicate split (olivine ~0.58, orthopyroxene ~0.24, pyroxene ~0.06, plagioclase ~0.12), troilite, chromite.
- `king_schofield_2015_ci_modal_mineralogy_xrd`: CI split (phyllosilicate ~81-84 wt%, magnetite, sulfide, carbonate).
- `howard_alexander_2015_hydrous_meteorite_phyllosilicate_classification`: CM phyllosilicate 70-90 wt%.
- `alexander_fogel_2007_macromolecular_organic_matter_chondrites`: IOM:soluble carbon 0.70:0.30.
- `mittelfehldt_2015_hed_clan_vesta`: V phases (pyroxene ≈ plagioclase; chromite, ilmenite ~1 wt%; Ni-free metal).
- `sunshine_connolly_2008_ancient_asteroids_refractory_inclusions`: L-types have the most CAIs (spinel).
- `hiro_i_zolensky_2001_tagish_lake_possible_d_type_sample`: D/Z/P accessories (magnetite ~5, sulfide ~3, carbonate ~3 wt%; see rc-085).
- `keil_1968_mineralogical_chemical_enstatite_chondrites`, `keil_2010_aubrites_and_their_asteroidal_parent_bodies`: Xe sulfides (troilite ~5, niningerite ~2, oldhamite ~0.7, daubreelite ~0.3 wt%), low-Ni kamacite.
- `jones_mccubbin_2014_phosphate_minerals_ll_chondrites`: merrillite ~0.4, chlorapatite ~0.2 wt%.

## R113 - Class-to-meteorite mapping (2026-10-04)

- `burbine_2024_testing_bus_demeo_with_meteorite_spectra` (CC BY; hosted from R152): ~1,500 meteorite spectra classified: HEDs fall in V, ordinary chondrites in S/Q, D and X mostly CM with many irons; C, B, L and Xc mix very different meteorites, so class sets the analogue well for V and S/Q only.
- `de_kleer_2026_jwst_spinel_rich_l_type_mineralogy`: five spinel-rich L-types show Mg-rich olivine plus spinel, little hydration, like CV3 Allende: supports the L row.
- `lebofsky_et_al_1990_low_albedo_3um_photometry` (unread).

## R114 - Carbonaceous bulk composition (2026-10-04)

`trigo_rodriguez_2025_metal_and_rare_earth_mining_potential_undifferentiated_asteroids_carbonaceous_chondrites` (MNRAS 2025): ICP-MS bulk composition of CI, CM, CR, CO, CV, CK and a ureilite; CI Orgueil Fe 25.93 wt%, Ni 7,719 ppm; Ni 2,779-15,469 ppm across CO and CV; no PGM columns. `schubert_2025_economical_extraction_platinum_main_belt_asteroids`: record only (the owner's "20-100 ppm" unchecked). `extracted_data/r114_gr_links_key_numbers.csv`.

## R115 - Primitive-class carbon and metal; AsteroidCatalog re-checked (2026-10-04)

At AsteroidCatalog@6a2cfbc:

- **rc-075:** v1.5.0 cut C-complex carbon to 0.04 (rc-010) but left D and Z at 0.30, T and P at 0.25; Tagish Lake (the D/Z/P analogue) carries 4.11 and 4.13 wt% C, so the cells are 7.3x and 6.1x; 67P dust (~45 wt% organic-like) is the counter-case: the owner's call (as rc-013 for ice).
- **rc-076:** B, C, Cb and F carry 0.01 metal; Ryugu has "no metal grains", so 0.01 is a ceiling.
- rc-007, rc-045, rc-046 applied; rc-001 declined; rc-002, rc-012, rc-013, rc-014 open (Xc metal 0.25 -> 0.32 as an albedo mixture).
- Agreeing: every DENSITY_EVIDENCE body with a Carry value matches Carry Table 1 (Ceres 2.13, Pallas 2.86, Interamnia 1.96, Mathilde 1.32, Pulcova 1.00, Daphne 2.03, Hermione 1.27, Elektra 1.84, Eugenia 1.34, Antiope 0.86, Lundia 1.64, Frostia 0.88, Klotho 4.16, Hestia 5.81, Eunomia 3.54, Juno 3.68, Parthenope 3.27, Ostro 2.59, Kleopatra 4.27, Lutetia 3.44, Sylvia 1.31, Camilla 2.28, Psyche 3.38, Patroclus 0.88); CV/CO 2.79/3.03; 67P ices 100 : 4.7 : 0.67.

`extracted_data/r115_taxonomy_carbon_metal_checks.csv`.

## R120 / R121 / R125 / R133 - Queue reads (2026-10-05 to 10-07)

- `wright_fleischer_1965_usgs_b1214a_geochemistry_platinum_metals` hosted (Bulletin 1214 chapter A, public domain): PGM abundances in rocks and meteorites summarised from the literature.
- `fornasier_2010_m_type_spectroscopic_survey` read from arXiv (not hostable): the M-type survey behind the Xk/M notes.
- `jones_mccubbin_2014_phosphate_minerals_ll_chondrites`: only the electronic appendix (X-ray maps for five LL chondrites) is open; no wt% figures.
- `lauretta_2024_bennu_in_the_laboratory` read from arXiv (CC BY-NC-ND there, not hostable): hummocky stones 1.55 ± 0.07 g/cm3, angular 1.69 ± 0.04 (Table 2, 12 stones); 637 Ryugu particles 1.79 ± 0.31.
- `lodders_bergemann_palme_2025_solar_system_abundances_ssreview` (read only): protosolar X=0.7060, Y=0.2753, Z=0.0187; "no obvious correlation of CI-chondritic to solar elemental abundance ratios with condensation temperatures is observed". `r133_lodders_2025_abundances_key_numbers.csv`.

## R152 - Candidate re-check (2026-10-12)

At AsteroidCatalog@86cfc54 (6a2cfbc is now 82a2905 after a history rewrite; `upstream_commit_map.csv`): cells unchanged (Cb metal 0.01; D/Z/T/P ice 0.25/0.25/0.10/0.15, carbon 0.30/0.30/0.25/0.25; B/C/Cb/F nickel-iron 0.01).

- **burbine_2024_testing_bus_demeo_with_meteorite_spectra** hosted; its Table A1 (1,489 RELAB spectra with group and class) in `extracted_data/r152_burbine_2024_table_a1.csv`.
- **rc-012 withdrawn:** of 10 CB/CH spectra one is Cb, six L, two X, one S; the seven Cb spectra are four L5 chondrites, Mighei (CM2), Y-82162 and Isheyevo; the one NEOWISE Cb albedo is 0.043 vs ~0.3 for iron-rich meteorites.
- **rc-076 narrowed to C:** howard_2010_cv3_modal_mineralogy_psd_xrd (CV3 metal 2-2.2 vol% reduced, 0.2-1.1 oxidised) and howard_2011_cm_modal_mineralogy_psd_xrd_part2 (CM metal under ~1 vol%) leave 0.01 standing for CV/CM-paired rows; B's 107 spectra run CV3 19, aubrite 16, lunar 14, CM2 12, L5 9.
- **rc-075 / rc-013 deepened:** Burbine's D matches CM 50%, iron 39%, CO 5% (collection bias); one of six Tagish Lake spectra is D. `wong_2024_jwst_lucy_trojans_oh_organics_co2` (arXiv): less-red and red Trojans "roughly correspond" to P and D; no 2 um band, ice depleted to ~10 m (~10 cm at poles); if the 3 um band is ice, P-like Trojans hold more (opposite to D 0.25 > P 0.15); aliphatic organics deeper on red (same order as D 0.30 > P 0.25). Surface-reachable ice is near zero.

`extracted_data/r152_taxonomy_analogue_checks.csv`.

## R155 - Jarosewich, Lodders 2003, Hiroi (2026-10-12; rc-085)

- `jarosewich_1990_meteorite_chemical_analyses` (ADS scan) Table 4 falls: Fe(m)+Ni+Co H 17.80, L 8.33, LL 3.56 wt%; the S/Sq/Q metal 0.06 "mean of LL (3.56 wt%) and L (8.33 wt%)" matches (5.945). CM2 C 1.82, CV3 0.43 wt%.
- `lodders_2003_solar_abundances_condensation_temperatures` Table 3 CI ppm: Ru 0.692, Rh 0.141, Pd 0.588, Os 0.486, Ir 0.470, Pt 1.004, Au 0.146; Fe 182,800, Ni 10,640, Co 502; all PGM in metal (19.39 wt%) = 17.4 ppm, half economicspace's IIIAB 35.5 ppm (Pt/Ir 3.75 vs CI 2.14; Pd/Pt 0.667 vs 0.586). Lodders backs only the chondritic half of the row's citation; its "~37 ppm" is 35.5 (36.5 with Au).
- **rc-085:** `hiro_i_zolensky_2001_tagish_lake_possible_d_type_sample` gives C 4-5 wt% and reflectivity 2-4% but no magnetite or sulfide figure, deferring to Brown 2000; the accessory modes upstream attributes to it are not there.

`extracted_data/r155_queue_open_copies_key_numbers.csv`.

## R160 - Tagish Lake composition pair (rc-085)

- `brown_2000_tagish_lake_fall_recovery_orbit_composition` (Science 290:320-325; UWO copy, not hostable): qualitative only: "magnetite is far more abundant than in most CMs", "In many places, magnetite has partially or completely replaced sulfides."; "Around 3.7 wt % carbon derives from carbonates" (vs 0.2-0.5 in CI/CM); total C 5.4 wt%.
- `gounelle_zolensky_2001_mineralogy_of_tagish_lake` (MAPS 37:737-761): the modal study; paywalled (DOWNLOADS.md).

`extracted_data/r160_tagish_lake_composition_key_numbers.csv`. rc-085 open: pull Zolensky, or upstream lists the split as unsourced.

## R177 - The LPSC-2001 abstract (2026-10-16)

Abstract #1616 (Gounelle, Zolensky, Tonui, Mikouchi; LPSC XXXII): "an abondant carbonate-poor lithology and a less common carbonate-rich lithology"; no modes. rc-085 unchanged. The row's author initial corrected to Nakamura K.

## R192 - The detailed-phase split ratios declare themselves unsourced (rc-172)

- `mineralogy.py` at AsteroidCatalog@84e026e, verbatim (count==1): "WHAT HAS NO SOURCE: every
  sulfide split as a number (the sources name the species, not a ratio this table could quote);
  the K alloy split; the CAI oxide fractions; and the metal of every class not named above --
  the C complex, P, D, Z, T, A, R, O and L."
- Class K keeps `_ALLOY_CV = {"taenite": 0.60, "kamacite": 0.40}` (`"K": _detail(_ALLOY_CV,
  _SULFIDE_NI),` count==1) while the module's own 1.8.1 fix moved every class with no source for
  its metal to `_ALLOY_OCTAHEDRITE = {"kamacite": 0.89, "taenite": 0.11}     # ~9 wt% Ni: no
  change`. K is not on that fix list although the same file names its alloy split unsourced.
- Arithmetic (computed here): lever-rule neutral taenite share = 0.106; _ALLOY_CV puts it
  at 0.60, about 5.6x neutral; Ni in K-class metal reads ~20.6 wt% against the ~9 wt%
  the coarse column assumed. taxonomy_composition.csv gives class K metal_fraction 0.08,
  so this moves value: economicspace master.py prices each alloy phase by its own derived
  composition (`_KAMACITE_NI` 0.065, `_TAENITE_NI` 0.30) and prints the neutral share itself:
  "(9.0 - 6.5) / (30 - 6.5) = 0.106".
- CAI accessories move numbers too: perovskite and hibonite take different base recoveries
  (0.40 vs 0.25), so the K/L perovskite-hibonite fractions are load-bearing unsourced values.
  The sulfide species ratios are attribution-only today: `_UTILITY_FAMILIES` asserts every Fe/Ni
  sulfide at one utility level, but the split decides where nickel sits if ore mineralogy ever
  prices differently.
- Registered sources that could supply them, all queued full texts:
  `king_schofield_2015_ci_modal_mineralogy_xrd` (ORO bitstream 403, re-probed R175),
  `howard_2011_cm_modal_mineralogy_psd_xrd_part2` and `howard_2010_cv3_modal_mineralogy_psd_xrd`
  (Elsevier closed per R152). No full text read this round; nothing extracted.

**rc-172** opened (citation): source the split ratios from institutional pulls of the three
queued studies, or apply NO SOURCE MEANS NO CHANGE to class K and label the rest as assumptions.

## R204 - completeness registration of the X-type survey (2026-10-19)

AsteroidCatalog CITATIONS.md section 3 (the literature behind its reference values) was swept work-by-work against sources.csv on 2026-10-19; author-year-only entries were invisible to every earlier DOI/URL/NTRS-accession token sweep, so this seam had never been checked end-to-end. Forty-six of the forty-seven works already carry registry rows, three of them under ids without the first-author surname: Hanus 2017 as adam_2017 (flagged as such by AC itself), Yokoyama et al. 2023 as ryugu_ivuna_2023, and Glavin et al. 2025 Nature Astronomy 9:199 as bennu_volatiles_2025. The single gap was Fornasier, Clark & Dotto (2011), Spectroscopic survey of X-type asteroids, Icarus 214:131-146 - the paper behind the upstream taxonomy.X_SPLIT_BOUNDS albedo convention. Registered this round as fornasier_2011_x_type_spectroscopic_survey [T1; registered_not_pulled]; DOI verified live against Crossref (10.1016/j.icarus.2011.04.022), no arXiv mirror found, publisher route paywalled - full text deferred to an institutional pull.

## R213 - AC two-tier phase table seam closed negative (2026-10-20)

Cross-tier consistency audit of reference/mineral_phases.csv vs mineral_phases_detailed.csv at AsteroidCatalog@84e026e (all 278 coarse rows, all 364 detailed rows): every refined child sums to its parent within rounding, and the only cross-tier deltas are documented design. README section 'Detailed phases: the alloy and the sulfides resolved' states that mineralogy.PHASE_DETAIL divides comp_phases entries into shares while DETAIL_ACCESSORIES adds new accessories inside the residual - exactly what the data show: perovskite + hibonite (K at 0.002+0.003, L at 0.003+0.005) and merrillite + chlorapatite (Q and every S-complex subclass at 0.004+0.002) carry empty refines fields as accessory markers, and the README's own comp_phases_detailed JSON sample matches the table values exactly.

Residual-fit invariant holds for all 32 spectral types: detailed totals never exceed 1.0 (tightest L at 0.998), so every accessory fits inside its coarse residual - no mass overflow exists anywhere in the pair.

Benign rounding class recorded to prevent a future false flag: X troilite children sum +1e-6 against their parent (0.022458 vs 0.022457) and Xc sums -1e-6, because five independent child values are each rounded at the sixth decimal; that is display precision of a share split, not an arithmetic violation. rc-172 stays open on its own claim (the split ratios have no source); nothing in this seam bears on it.

## R237 - the end-member candidates decided upstream (2026-10-21)

The owner chose the Tagish Lake end-member for the primitive types. AsteroidCatalog 1.10.0 (`6915077`, published as data-2026-10-21b, compared by value with data-2026-10-21):

- rc-075 applied: D, Z, T and P carbon_fraction 0.04 (bennu_volatiles_2025 Extended Data Table 1: Tagish Lake 4.11 and 4.13 wt%); X and Xc follow P, 0.08 to 0.02. Carbon and both phase columns moved on exactly the 40,394 predicted bodies.
- rc-013 declined: D and P ice stay 0.25 and 0.15; upstream's header now carries wong_2024_jwst_lucy_trojans_oh_organics_co2's reachable-ice point and the P-over-D ordering.
- rc-076 declined: the C row's 0.01 metal kept and labelled an upper bound in its notes.

AsteroidCatalog candidates: none open.

## R304 - spacevalue sibling citation seam opened and closed; two density-reference rows registered (2026-10-29)

economicspace PIP_SPEC at tip pins spacevalue at tag v0.2.0 alongside spacecost at v0.14.0; the package holds Stage 2 pricing (formerly modules/mineral_value.py) and from their #183 also Stage 4 cargo valuation, so its citation list is load-bearing for economicspace outputs but had never been swept against this registry - the same blind-seam class as the R204 author-year pass. Work-level resolution at tag d12f626: yfinance, USGS Mineral Commodity Summaries 2025 and 2026 editions (the 2025 row was present at HEAD; strict grep after a truncated first-pass hit list), World Bank Pink Sheet = worldbank_cmo_pink_sheet, LBMA fixings = lbma_precious_metals_fixings, Johnson Matthey PGM Market Report May 2026 = jm_pgm_market_report_2026, McDowell Space Activities in 2025 Table 22 = mc_dowell_2025_space_activities_gcat, Northrop Grumman LunA-10 rail network study = northrop_grumman_2024_luna10_lunar_rail_network, the eight meteorite analogue papers all already registered (verified at R302), Mars fact sheet row present - leaving only the density/formula cluster: Klein and Hurlbut Manual of Mineralogy plus Mindat.org and Webmineral.com, now registered as klein_hurlbut_manual_of_mineralogy T4 and mindat_webmineral_online_mineral_data_databases T3. spacevalue pyproject pins spacecost v0.14.0, identical to the economicspace pin: dependency graph consistent across all three repos at these tips.

## R312 - The pyroxene metadata formula omits one metal-site cation (2026-11-01)

`morimoto_1988_nomenclature_pyroxenes`, Bulletin de Minéralogie p535, specifies normalization
"to six oxygens, or to four cations". Page536 gives the standard M2M1T2O6 formula and
site-allocation sums T=2, M1=1 and M2=1. M2 and M1 denote two distinct cation sites.

At spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011, `spacevalue/catalog.py:1970`
stores the `pyroxene` formula as `(Mg,Fe,Ca)Si2O6`. This has only one metal-site cation
and two Si, three cations per six O. For the divalent Mg/Fe/Ca shorthand, the consistent
formula is `(Mg,Fe,Ca)2Si2O6`: two metal cations and two Si. A charge check with divalent
Mg/Fe/Ca, Si4+ and O2- gives -2 for the stored formula and zero for the corrected one.
The neighbouring orthopyroxene `(Mg,Fe)2Si2O6` already has four cations; enstatite
`MgSiO3` has the correct reduced stoichiometry and normalizes to the same count.

All eight committed `tests/data/prices-2026-10-07/mineral_value_catalog.*.csv` destination
fixtures carry the erroneous pyroxene formula. The formula field is serialized in catalog.py
(L2290); neither `spacevalue/cargo.py` nor economicspace `modules/calc.py` reads it.
The independent pyroxene yield is `iron:0.07`. Verdict: a metadata formula correction,
with no new yield, density or price derived. `rc-242`: restore the missing coefficient in
the current source and regenerated price metadata, preserving archived provenance.
`extracted_data/r312_pyroxene_formula_cation_count.csv`.

## R332 - Wholly residual bodies miss the bulk-silicate valuation floor (2026-11-02)

Source `spacevalue_full_residual_valuation_record_2026`:
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011, `spacevalue/cargo.py`
and the committed Earth/cislunar price fixtures;
AsteroidCatalog@66fb47aaeb17aa7e11c023773a39765c1aa793fb, original
merge/derive/validate/enrich and supporting numerical modules;
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`;
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f, original reference CSVs.

The catalogue contract explicitly says Unknown has four None fractions,
"so the residual is the whole body" (taxonomy.py L10-13; Unknown row
L561-570). Unknown phase cells are missing (mineralogy.py L337-346,
L566-571). Cargo's bulk residual comment says "value at silicate floor so it
doesn't vanish" (cargo.py L798), but the next line requires
`0.0 < frac_sum < 1.0`. The phase-table residual repeats the same strict
lower bound (L921-929). A zero total therefore gets neither the value nor a
loadable residual phase. `asteroid_best_phase_usd_per_kg` also returns zero
through its bulk floor (L1467-1468). Economicspace returns None at `bulk_value <= 0`
before checking mass or candidate feasibility (calc.py L8121-8123).

Twenty-four original valuation cases compare both destinations. All-zero,
all-None, all-NaN and absent coarse fractions, empty coarse/detailed phase
objects and a zero-fraction phase each produce bulk value 0, best value 0
and an empty phase table. The existing fixture quotes are 0.05 USD/kg on
Earth and 1,603.050708496265 USD/kg cislunar. Even a silicate fraction of
1e-12 restores the entire rock value under the existing remainder rule:

| representation | original Earth USD/kg | original cislunar USD/kg |
|---|---|---|
| zero named fraction, all mass residual | 0 | 0 |
| 1e-12 silicate, remainder residual | 0.05 | 1,603.050708496265 |
| explicitly 100% silicate | 0.05 | 1,603.050708496265 |

An in-memory diagnostic changes only the two lower comparisons to include
zero. Fourteen empty/zero cases then receive the declared whole-body
residual floor and one residual phase of fraction 1. Ten nonempty controls
retain their original bulk, best and phase values: epsilon, half/full
silicate, half metal and an explicit silicate phase at each destination.
Original replays agree, and phase-weighted values reproduce the diagnostic
bulk values. No price or material fraction is recalibrated.

Four complete original catalogue chains use a synthetic 2.7 km body at
a=1.2 AU, e=0.1, inclination 1 degree, H=15 and rotation 8 h. U is an
unrecognised synthetic source label; S is the recognised comparison. Each
is run with and without a supplied 1e13 kg mass. All four rows survive
validation and have no reported physical-row problems. U with measured mass
retains 1e13 kg and density 0.9703090571 g/cm3, takes comp_class Unknown,
and has missing fractions/phase cells. Its original cargo value is zero.

Eight complete consumer pairs run those original in-memory catalogue rows
through `evaluate_asteroid`, with actual Falcon 9 reusable, kerolox, all 46
operational rows, raw cargo, a single mission and no ISRU or aerocapture.
The finite-mass U body is originally rejected at the zero-value gate. After
the two guard changes it returns accepted, unprofitable mission results:

| destination | returned cargo kg | gross value USD | total cost USD |
|---|---|---|---|
| Earth surface | 391.142165 | 19.557108 | 1,746,081,377.494511 |
| cislunar | 3,261.850862 | 5,228,912.335548 | 1,683,342,646.289729 |

An original-code control explicitly supplying one full silicate phase gives
identical mission fields, including finite float.hex values and NaN
positions; only the two expected phase-provenance flags differ. The
diagnostic retains the unknown classification and invents no density or
mass. U without a measured mass still rejects after the mass-context check.
The four S consumer fixtures retain exactly matching results. Thus two
consumer dispositions change and six controls retain their outcomes.

Verdict: the residual floor disappears at exactly zero named fraction,
contrary to the stated whole-body residual contract. `rc-263`: include the
wholly residual case consistently in bulk, phase and best valuation while
preserving missing-mass exclusions and malformed-input reporting. This
checks the model's declared rock-floor assumption, not the true composition
of an unknown asteroid. Population incidence and ranking effects were not
measured. `extracted_data/r332_full_residual_valuation.csv`.


## R424 — Bennu B-type bound-water fraction review (2026-11-09)

`lauretta_2024_bennu_in_the_laboratory` identifies Bennu as a B-type asteroid and reports the sample as “hydrated (0.84–0.95 wt% H)” (Conclusions, p. 2481); Table 4 reports 0.90 ± 0.04 wt% H for fines, 0.93 ± 0.05 for intermediates, and 0.93 ± 0.01 for an aggregate (p. 2471). If all measured hydrogen were in H2O, the range corresponds to 7.51–8.49 wt% H2O-equivalent. AsteroidCatalog’s B row assigns ice_fraction=0.20 and mineralogy.py maps that entire group to water, which the downstream cargo valuation prices as water. The measured sample H therefore motivates review of the 20% B-row water proxy; hydrogen is not a direct water/ice assay, and returned regolith does not determine the asteroid interior or all B types. Verdict: bounded review candidate rc-334; no replacement value inferred. `extracted_data/r424_bennu_bound_water_vs_b_type_fraction.csv`.


## R437 — Bennu OH/H2O spectral distinction and sample context (2026-11-09)

Kaplan et al. (first published 2026-10-14), in “New Evidence from the Sample,” distinguish Bennu’s OH-bearing 2.74-μm global surface feature from the H2O-related 3.0-μm feature. The returned bulk aggregate has a narrower hydration feature with a 2.710 ± 0.002 μm minimum, compared with 2.74 ± 0.01 μm for global OVIRS observations, and lacks the 3.0-μm H2O bending-mode overtone. The authors infer that the subsurface sample contains “less adsorbed and/or structural water” than the optical surface and is primarily hydroxyl-dominated. Their conclusion treats the possible phosphate origin of the surface 3.0-μm feature as inconclusive.

This adds sample-versus-surface evidence to `rc-334`: Bennu’s hydration signatures do not establish a 20 wt% bulk water/ice fraction, and hydroxyl-bearing minerals must not be equated with free water. The paper does not quantify bulk H2O/ice abundance or establish Bennu’s interior or the B-type population. No replacement fraction is inferred. Extracted: `extracted_data/r437_bennu_water_hydroxyl_spectral_evidence.csv`.


## R438 — Bennu interlayer water evidence (2026-11-09)

King et al. (2026), “Hydration State of Bennu,” p. 1088, report pristine-sample smectite basal spacing of 12.6–12.4 Å, interpret it as monohydrated, and estimate “up to ~2 wt% water in the interlayer space” for saponite. They state that their XRD characteristics are consistent with a 1.25 wt% interlayer-water result reported by Yurimoto et al. (2026); that underlying study was not independently read in this round. On p. 1089, King et al. note OSIRIS-REx excavated material from as deep as ~50 cm and that this subsurface provenance could enhance apparent water relative to Bennu’s bulk surface.

These are local, bound-water and sample-specific results, not a whole-asteroid or B-class ice fraction. They strengthen the evidentiary review in `rc-334` but do not supply a replacement for `ice_fraction=0.20`. Extracted: `extracted_data/r438_bennu_xrd_interlayer_water.csv`.


## R477 — Tagish Lake accessory modes are sample-dependent (2026-11-09)

Izawa et al. (2010), Table 3, reports XRD/Rietveld modal abundances for seven Tagish Lake samples and a comparison sample. Across the seven study samples, magnetite spans 6–17 wt%, siderite 4–24 wt%, and pyrrhotite 10–18 wt%; calcite and pentlandite are reported at or below the table’s detection/reporting threshold in several samples. The paper identifies distinct magnetite/sulfide-rich and carbonate-rich, siderite-dominated lithologies and describes the meteorite as heterogeneous. These measurements show why the D/Z/P `_ACC_TL` entries (magnetite 0.05, troilite 0.03, carbonates 0.03) cannot be treated as a uniquely established Tagish Lake bulk recipe. Pyrrhotite is not troilite, the samples are not a demonstrated population-level D/Z/P composition, and replacing values from selected modes risks double-counting against the model’s coarse fractions.

`rc-343` asks for the upstream provenance and scope of these three absolute accessory fractions to be resolved; this paper supplies a relevant, quantitative comparator but no direct replacement for the modeled asteroid classes. The previously open `rc-085` was applied as a source-attribution correction and remains historical; this is new evidence. Extracted: `extracted_data/r477_izawa_tagish_lake_modal_ranges.csv`.


## R478 — CI meteorite modal data bear on an unsourced silicate split (2026-11-09)

King et al. (2015) used PSD-XRD on bulk samples of Alais, Orgueil and Ivuna. The abstract reports a “mixed serpentine/saponite phyllosilicate (81–84 vol%)” assemblage (printed p. 148). Table 1 (printed p. 154) gives Orgueil averages of 83.0 vol% phyllosilicate and 1.0 vol% olivine, and Ivuna averages of 82.5 and 2.0 vol%, respectively. The paper reports modal volume percentages for individual CI meteorite samples; AsteroidCatalog’s `_SIL_CI` is 95% phyllosilicates and 5% olivine as mass shares conditional on the silicate group, applied across CI-analogue classes. Those bases are not interchangeable without phase-density conversion and an explicit mapping of the modeled silicate subtotal.

`rc-344` records a citation/basis review of `_SIL_CI`; the paper supports phyllosilicate dominance but does not directly establish the exact 95/5 model mass split. Keep the values unchanged pending a documented conversion or a source that reports the needed mass-share basis. The PDF states CC BY on printed p. 149. Extracted: `extracted_data/r478_king_ci_modal_mineralogy.csv`.


## R479 — A Murchison comparator for the unsourced CM silicate split (2026-11-09)

Lee and Lindgren (2016), Table 4 (printed p. 1007), reproduce XRD modal results attributed to Howard et al. (2011) for Murchison: 72.5 vol% phyllosilicates and 23.4 vol% olivine plus orthopyroxene, with sulfide 1.8%, calcite 1.2%, and magnetite 1.1%. The article identifies Murchison as among the least-altered CMs and reports its phyllosilicate class as type 1.5. Normalizing only its reported phyllosilicate and anhydrous-silicate modes gives 75.6 vol% phyllosilicates; this comparison is calculated here and remains a volume share.

AsteroidCatalog `_SIL_CM` sets phyllosilicates/olivine/pyroxene to 0.85/0.10/0.05 as conditional mass shares and applies that fixed mix to Cg/Ch/G. The Murchison result is a sample-specific volume comparator, not a mass-based replacement or a measurement of all CM subclasses. `rc-345` asks for the missing source and the analogue/basis mapping to be documented; values remain unchanged pending evidence on that basis. The publisher footer states all rights reserved, so the paper is not hosted. Extracted: `extracted_data/r479_murchison_cm_modal_mineralogy.csv`.


R480 — DeMeo and Carry (2015), pp. 16–18, describe X-complex spectra as “compositionally degenerate” because they span the darkest to brightest asteroid surfaces, with albedos from a few percent to 50%. They distinguish spectral classification from compositional inference and note that surface spectra are affected by grain size, temperature, geometry and space weathering. AsteroidCatalog assigns bulk `silicate_fraction` 0.44, 0.47, 0.65 and 0.45 to X, Xc, Xe and Xk. The source does not supply these bulk fractions; albedo and spectral grouping alone do not validate them. `rc-346` records this support/mapping gap without proposing replacement values. The cited PDF is hosted by MIT; no redistribution licence was identified, so no copy is hosted. Extracted: `extracted_data/r480_x_complex_taxonomic_degeneracy.csv`.

R482 — Abell and Gaffey’s NASA NTRS record for their LPSC XXXI paper reports that 349 Dembowska has a surface OPX:olivine ratio of 45:55, with variation of approximately 20%. AsteroidCatalog’s unsourced R-type conditional silicate split assigns 0.60 olivine and 0.30 orthopyroxene, or 33.3:66.7 when normalized to those two phases; it also assigns 0.05 each to pyroxene and plagioclase. The reported Dembowska surface ratio differs from the model’s two-phase ratio, but it is one asteroid’s surface spectrum and does not determine bulk mass fractions or the whole R-type mix. `rc-348` records the comparison and asks for the surface-to-bulk and modal-to-mass mapping; no replacement is inferred. The NTRS record says the work is public use permitted but has no available download. Extracted: `extracted_data/r482_dembowska_surface_opx_olivine_ratio.csv`.


R484 — Smith et al. (2004) report that CV chondrite carbon abundance ranges from 0.3 to 1.8 wt%, mean 0.77 wt% (printed p. 2028, citing Kerridge 1985 and Pearson 2003); their CV-affinity meteorite NWA 1152 was measured at 1.1 wt% bulk carbon on p. 2028. AsteroidCatalog labels K-type as a CV/CO chondrite analogue but sets bulk `carbon_fraction=0.08` (8 wt%) without a source. The comparison raises a substantial analogue/value gap, but a single CV-affinity meteorite and a literature range do not establish the composition of K-type asteroids or the CO end of the analogue. `rc-350` records the challenge without inferring a replacement. The paper cites the earlier sources for the group range; those references were not independently assessed in this round. Extracted: `extracted_data/r484_cv_carbon_comparator.csv`.


R485 — Scott et al. (2015), Asteroids IV, p. 578, state that magnesian A-types tend to be olivine-rich at approximately 70–90% abundance, while ferroan A-types have spectra consistent with a monomineralic interpretation. AsteroidCatalog’s unsourced A-type conditional silicate split is 95% olivine and 5% orthopyroxene. The literature distinguishes A-type subgroups; the 95% assumption may fit some ferroan cases but exceeds the stated magnesian range and does not represent the group’s reported diversity. The chapter discusses spectral abundance, not bulk mass fraction, so it does not provide a direct replacement. `rc-351` records the need for a subtype- and basis-specific mapping. Extracted: `extracted_data/r485_a_type_olivine_abundance.csv`.


R486 — Cloutis et al. (2006) infer from 3628 Božněmcová’s 0.35–1.65 µm reflectance spectrum that the surface contains about 55–75 wt% clinopyroxene, 20–33 wt% plagioclase, and 0–20 wt% olivine (printed p. 1159). The paper identifies 3628 Božněmcová as the archetype assigned to the O class (p. 1148). AsteroidCatalog assigns the O class an unsourced conditional silicate split of 50% olivine and 50% orthopyroxene, with no plagioclase or clinopyroxene specified. The spectral interpretation directly challenges that phase mapping, but this is one asteroid’s surface composition, not proof of the whole O class or bulk interior. `rc-352` records the missing archetype-to-phase and surface-to-bulk mapping; no replacement is inferred. The paper notes limited spectral coverage and observational quality. Extracted: `extracted_data/r486_boznemcova_o_type_surface_mineralogy.csv`.


R487 — Kwon et al. (2022), p. A173 (printed p. 11), state that Tagish Lake “has been suggested as one of the best meteorites for D-, T-, and P-type red asteroids because their slopes are similar,” but their comparison finds Tagish Lake much darker and its VNIR/LNIR slopes unlike the large T-type spectrum. Their CI spectra best match the large T-type spectra across the compared VNIR–LNIR shape and OH-band properties (pp. A173, 11–12). The paper studied large T-type surface spectra and says T type is relatively ill-constrained as an independent group (p. A173, p. 1); these observations do not measure bulk carbon abundance. AsteroidCatalog assigns T carbon_fraction 0.04 and its note attributes that value to the D-type Tagish Lake 4.1 wt% reading while stating T has no meteorite analogue of its own. `rc-353` records the analogue-to-class and surface-spectrum-to-bulk-carbon mapping gap; no replacement value is inferred. The article states CC BY 4.0 (p. A173, p. 1). Extracted: `extracted_data/r487_large_t_type_surface_analogue.csv`.


R501 — C-type returned-sample water comparator (2026-11-09)

AsteroidCatalog at `9d971b5` assigns `reference/taxonomy_composition.csv` C `ice_fraction` = 0.15 and maps the C-class ice phase to water in `asteroid_catalog/mineralogy.py` `PHASE_SHARES`. Yokoyama et al. report for the returned C-type asteroid Ryugu sample “The total H2O is 6.84 wt.%” and distinguish 0.30 wt.% interlayer H2O from 6.54 wt.% structural-OH H2O (Science 379(6634), p. 8). Ryugu is a sample-level CI-like comparator, not a class mean; the result is mostly chemically bound water rather than free ice. It therefore does not directly replace or falsify the 15% class estimate, but exposes a boundary and representativeness gap in treating that estimate as an ice fraction. `rc-367` records the comparator and asks that the class-level proxy and water state be made explicit; no replacement value is inferred. Extracted: `extracted_data/r501_yokoyama_ryugu_c_type_water_content.csv`.


R502 — Iron-meteorite PGM distribution comparator (2026-11-09)

AsteroidCatalog `asteroid_catalog/taxonomy.py` sets `_PGM_BASELINE_PPM = 37.0`; the preceding comment calls it approximately 37 ppm total PGM+Au and a “mean iron meteorite” figure, while the code says this baseline has no source. Cannon, Gialich & Acain compile measured iron-meteorite PGM data and statistically resample ten samples per group 100 times (section 2.2, p. 4). Their Table 2 reports a 40.78 ppm median total PGM grade and 14.70–107.86 ppm 10th–90th percentiles (p. 4); these totals exclude Au, and the discussion says the iron-meteorite values represent 100% metal upper values and cannot locate a particular asteroid within the distribution (p. 6). This is a measured PGM-only comparator, not an Au-inclusive mean or a taxonomy-specific estimate. `rc-368` records the attribution and boundary gap; retain 37.0 ppm pending a compatible PGM+Au baseline and do not derive class factors from this distribution alone. Extracted: `extracted_data/r502_cannon_iron_meteorite_pgm_percentiles.csv`.


R503 — Taxonomic PGM factors lack a published calibration (2026-11-09)

AsteroidCatalog `asteroid_catalog/taxonomy.py` assigns fixed PGM factors of 2.0 to M/Xk/X/Xc, 1.5 to Xe/E, 0.5 to A/R/O, and 0.2 to V; its comment says none of the table’s own numbers has a source. Cannon, Gialich & Acain report broad iron-meteorite PGM-grade percentiles (Table 2, p. 4) and state that there is “no known way to remotely identify where an asteroid falls along the wide distributions” (p. 6). Their analysis supplies distributional context but no mapping from asteroid spectral classes to these factors. `rc-369` records the calibration gap; retain the factors only as explicit model scenarios pending a class-matched published basis. Extracted: `extracted_data/r503_cannon_pgm_remote_inference_limit.csv`.


## R514 — CM sulfide split compared with ALH 83100 XRD modes (2026-11-10)

`lindgren_lee_et_al_2020_alh83100_cm_sulfide_modal_xrd` — Lindgren et al., Table 2 (printed p. 74), report XRD modal mineralogy for unheated ALH 83100: pyrrhotite 0.9 vol%, pentlandite 1.2 vol%, and total Fe(Ni) sulphide 2.1 vol%. The paper labels ALH 83100 as petrologic type 1.2 and says the measurements are typically accurate to less than 5 vol% (pp. 74–75). The present-study modal values imply a 42.9/57.1 pyrrhotite/pentlandite split by volume within the reported sulphide modes; the paper notes the earlier Howard et al. (2011) analysis did not individually quantify the three sulphide minerals. AsteroidCatalog's `_SULFIDE_CM` applies a 65/35 split across CM-related taxonomy rows; the sample's volume modes differ, but they do not establish class-wide mass shares. Open **rc-380** to review the fixed split or label it as an assumed distribution; no replacement is inferred. Extracted: `extracted_data/r514_alh83100_cm_sulfide_modal_xrd.csv`.


## R518 — Tagish Lake soluble-organic share comparator (2026-11-10)

Grady et al. (2002), abstract (p. 713), report that a small pristine Tagish Lake chip contained 5.81 wt% total carbon, about 2.6 wt% organic carbon, and that “around 2% of the organic material is thermally labile and solvent soluble.” The abstract cautions that the chip’s carbon abundance may be artificially high because carbonate decomposition dominated its carbon inventory. AsteroidCatalog `asteroid_catalog/mineralogy.py` assigns `_CARBON_PRIMITIVE` shares of 0.60 to `organics` (soluble organic matter) and 0.40 to `carbon` (insoluble macromolecular organic matter) for P, D, Z and T; the 0.60 share is 30 times the Tagish Lake sample comparator. This single, heterogeneous meteorite sample does not establish a class-wide D/Z/P/T split or prove the measurement definitions match the model phases. rc-384 records the unsourced split for review; no replacement is inferred. `extracted_data/r518_tagish_lake_organic_matter_split.csv`.


## R541 — Tagish Lake accessory-mode comparator (2026-11-10)

`schrader_etal_2024_tarda_tagish_lake_modal_mineralogy`: §3.1.2 reports one Tagish Lake sample, ASU1684_C1, as most similar to the carbonate-rich lithology; Table 2 gives “Ca-carbonate (~3.2 vol.%; dolomite and calcite), magnetite (~4.6 vol.%), Fe-sulfide (~1.9 vol.%; pyrrhotite and pentlandite)” (accepted manuscript p. 42). The method is digital point counting; the paper treats area percent as equivalent to volume percent and notes identified mineral abundances are lower limits where fine-grained matrix falls below mapping resolution (§2.1; Table 2 notes).

Upstream: AsteroidCatalog `asteroid_catalog/mineralogy.py` at `AsteroidCatalog@99781b65fb792a844140c49cdadfa123ebc9b505` keeps `_ACC_TL` at 0.05 magnetite, 0.03 troilite and 0.03 carbonates for D/Z/P; the module defines these as absolute body mass fractions. Verdict: this peer-reviewed study adds a direct, quantitative Tagish Lake sample comparator and strengthens the open basis review in `rc-343`; it reports volume modes for one carbonate-rich sample, with pyrrhotite/pentlandite rather than troilite, and does not establish representative D/Z/P mass fractions. No conversion or replacement value is inferred. Extracted: `extracted_data/r541_schrader_tagish_lake_modal_comparator.csv`.


## R552 — CI sulfide species-split citation gap (2026-11-10)

`harrison_etal_2025_ryugu_ci_sulfide_mineralogy` — Harrison et al. report 0.3–0.4 area% total Fe-sulfide in Orgueil and Ivuna; their Results describe Fe-sulfides as “predominantly pyrrhotite” and say “Pentlandite is rare” (printed p. 510). The article identifies rare cubanite as well, but gives no quantitative pyrrhotite/pentlandite ratio. At AsteroidCatalog@99781b65fb792a844140c49cdadfa123ebc9b505, `_SULFIDE_CI` assigns pyrrhotite 0.70 and pentlandite 0.30 to detailed-phase rows B, C, Cb and F. The measurements are sample-level, coarse-grain observations and do not set a class-wide mass ratio. Open **rc-418** to document the split’s basis or label it an estimate; no replacement is inferred. Extracted: `extracted_data/r552_harrison_ci_sulfide_species.csv`.


## R553 — S-complex subtype phase-share basis (2026-11-10)

DeMeo & Carry (2015), Table 1 (printed p. 17), maps the Gaffey seven-class mineralogical scheme to Bus and Bus-DeMeo S-complex taxonomy and describes the Gaffey system as primarily separating olivine-to-orthopyroxene ratio. The chapter distinguishes detailed mineralogical characterization from taxonomy (p. 14). AsteroidCatalog `asteroid_catalog/mineralogy.py` assigns conditional silicate mass shares of 75/12/3/10 to Sa, 45/35/8/12 to Sr, and 30/30/20/20 to Sv (olivine/orthopyroxene/pyroxene/plagioclase). The source supports mineralogical diversity but does not report these Bus-DeMeo subtype bulk mass fractions or the conversion basis. `rc-419` records the review gap; no replacement values are inferred. Extracted: `extracted_data/r553_s_complex_subtype_taxonomy_vs_phase_splits.csv`.


## R554 — Aubrite sulfide-share sample comparison (2026-11-10)

Wilbur et al. (2022), Table 2, report modal sulfide abundances for 16 aubrite meteorite samples in vol.% with stated uncertainty of ±2.3–7.2 vol.%; total sulfides range from 0.1 to 61 vol.%. Modes include alabandite in addition to troilite, daubréelite and oldhamite. Bishopville A reports 0.6 vol.% troilite and 1.9 vol.% oldhamite; Norton County 983 reports 3.7 troilite, 5.6 alabandite, 0.5 daubréelite and 51 oldhamite vol.%. AsteroidCatalog `PHASE_DETAIL[E]` applies 0.60/0.30/0.10 conditional mass shares to troilite/oldhamite/daubréelite and omits alabandite. These sample-specific volume modes show heterogeneity and do not set representative mass shares for E-type bodies. `rc-420` records the scope and conversion review; no replacement is inferred. Extracted: `extracted_data/r554_wilbur_aubrite_sulfide_modal_modes.csv`.


## R558 — CV/CO CAI population comparator (2026-11-10)

Dunham et al. (2023), Table 3, compile 3,027 CAIs from 12 CV chondrites (mean 5.4 area%, range 0.7–13.1) and 1,332 CAIs from 15 CO chondrites (mean 1.5 area%, range 0.5–3.6); hibonite-rich CAIs are classed as rare in CV and common in CO. At AsteroidCatalog@800a4ca377823edc3ea205b9069b29db147f2b63, `asteroid_catalog/mineralogy.py` maps K to CV/CO and L to a CV3 possibility; `DETAIL_ACCESSORIES` assigns perovskite/hibonite absolute body mass fractions of 0.002/0.003 for K and 0.003/0.005 for L. Total CAI area abundance and qualitative hibonite-rich frequency do not quantify those individual phases or convert area to body mass. Verdict: population context only; no contradiction or replacement value is established, so no new revision candidate is opened; the unsourced CAI oxide fractions remain within the prior scope of rc-172. Extracted: `extracted_data/r558_dunham_2023_cai_population_cv_co.csv`.

## R581 — T-type ice-fraction basis (2026-11-11)

`asteroidcatalog_ttype_ice_fraction_code_current_2026`: AsteroidCatalog assigns T-type `ice_fraction` 0.10. The taxonomy module says every ice fraction lacks a source, and the T-row note gives no basis for this value; it only says the carbon fraction borrows from D-type Tagish Lake and that T has no meteorite analogue of its own. Kwon et al., “Probing the surface environment of large T-type asteroids,” *A&A* 666 (2022), A173, observes OH absorption but no diagnostic water-ice bands above noise on (96) Aegle and (570) Kythera (Abstract, printed p. 1). The authors suggest that large T types may have had “abundant water ice at their birth” before heating melted it (§4.1, printed p. 11). This supports a possible water-bearing history, not a quantitative present-day bulk or mineable ice fraction. Verdict: request a T-type-specific mass-fraction basis that distinguishes accretion-era ice, present interior water, hydrated minerals, and accessible surface material; retain 0.10 as an explicitly unverified scenario until such evidence exists. No replacement inferred. **rc-444**. Extracted: `extracted_data/r581_ttype_ice_fraction_context.csv`.

## R582 — C-complex subtype water-fraction basis (2026-11-11)

`asteroidcatalog_c_subtype_ice_fraction_code_current_2026`: AsteroidCatalog assigns class-level `ice_fraction` values of 0.18/0.12/0.10/0.10/0.15/0.12 to Cb/Cg/Cgh/Ch/F/G; its taxonomy header says every ice fraction lacks a source. The C-complex estimates stand for bound/interior water, and `mineralogy.py` maps them to water. Beck et al. (2021), “Water” abundance at the surface of C-complex main-belt asteroids, calibrate a combined 2.75/2.80-μm metric against meteorite thermogravimetric measurements; the Abstract reports a high calibration uncertainty of 4 wt% H2O and a 4.5 wt% volume-average surface-equivalent water content for C-complex MBAs excluding Ceres. That population-scale surface estimate does not supply subtype-specific values or whole-body interior fractions. Verdict: request a subtype-specific empirical or modeled basis and explicit water boundary; retain the current values only as unverified scenarios, with no replacement inferred. **rc-445**. Extracted: `extracted_data/r582_c_subtype_water_fraction_context.csv`.

## R583 — S-complex zero-water scope (2026-11-11)

`asteroidcatalog_s_complex_zero_water_code_current_2026`: AsteroidCatalog assigns `ice_fraction=0.00` to S, Sa, Sk, Sl, Sq, Sr and Sv, and `mineralogy.py` maps this group to water. McAdam et al. (2024), *The Planetary Science Journal* 5:254, report 27 of 33 observations with detectable 3 μm features at ≥1% band depth within error (Abstract, printed p. 1); the discussion identifies OH/H2O signatures on 23 nominally anhydrous S-type asteroids (§4.3, printed p. 13). The article says the 3 μm region cannot distinguish OH from H2O and lists endogenic hydrated minerals, solar-wind OH and exogenic hydrated minerals as possible origins (§2, printed p. 201). These surface detections challenge an unqualified zero-water interpretation but establish no bulk or class-level extractable-water amount. Verdict: define what the zero excludes and retain it only for that stated boundary until matched evidence is available; no replacement inferred. **rc-446**. Extracted: `extracted_data/r583_s_complex_hydration_context.csv`.


## R585 — P/D/Z interior ice fraction basis (2026-11-11)

`asteroidcatalog_dz_ice_fraction_code_current_2026` and `asteroidcatalog_p_ice_fraction_code_current_2026`: AsteroidCatalog assigns D and Z `ice_fraction=0.25` and P `ice_fraction=0.15`; its module describes the fractions as approximate defaults where direct measurements are absent. Jones et al. (1990) report that only 1 of 10 sampled P/D spectra shows even a weak H₂O absorption (summary, printed p. 190), yet infer that D asteroids, especially Trojans, “may have had a substantial (≈ 50%) ice component” by comparison with Galilean-satellite ice/rock ratios (printed p. 187). They say the P/D objects may retain interior ice, but this is a formation and thermal-evolution hypothesis, not a measured present-day D/Z bulk or accessible-water fraction. Verdict: request class-specific bases for D/Z and P that distinguish accreted ice from present interior and mineable water; retain 0.25 and 0.15 only as unverified scenarios. No replacement inferred. **rc-448** reviews D/Z; **rc-449** reviews P. Extracted: `extracted_data/r585_dz_interior_ice_fraction_context.csv`.


## R603 — Ordinary-chondrite modal comparator for S-complex silicate shares (2026-11-11)

Dunn et al. (2010), Table 5 (printed p. 131), report XRD whole-rock modal means and 1σ for 48 equilibrated type 4–6 H, L and LL meteorites. The table lists olivine, low- and high-Ca pyroxene, plagioclase and troilite as separate phases; its conclusion says olivine plus low-Ca pyroxene comprise 50–75 wt% of ordinary chondrites (printed p. 133). AsteroidCatalog@800a4ca377823edc3ea205b9069b29db147f2b63 assigns `_SIL_OC` shares 0.58/0.24/0.06/0.12 to S, Sq, Q, Sk and Sl. The meteorite group means are whole-rock values and do not document the mapping to those taxonomy classes or the conditional four-phase vector. Verdict: comparator only; no contradiction or replacement value inferred. **rc-466**. Extracted: `extracted_data/r603_ordinary_chondrite_modal_averages.csv`.


## R604 — HED sample modal ranges and the V-type silicate vector (2026-11-11)

Li and Milliken (2015), in the study description and Tables 1–2, report modal mineral ranges across 14 eucrites and 13 diogenites: clinopyroxene 0.3–36.5%, orthopyroxene 5–97.8%, olivine 0–91%, and plagioclase 0–61%. AsteroidCatalog@800a4ca377823edc3ea205b9069b29db147f2b63 assigns V-type conditional silicate shares of 0.45 pyroxene, 0.15 orthopyroxene, 0.37 plagioclase and 0.03 olivine. The sample ranges show lithologic variation and do not state the mixture weights or volume-to-mass conversion for a representative V-type body. Verdict: comparator only; no contradiction or replacement value inferred. **rc-467**. Extracted: `extracted_data/r604_hed_modal_mineral_ranges.csv`.


## R605 — X-complex mixture and ice-fraction basis (2026-11-11)

AsteroidCatalog@800a4ca377823edc3ea205b9069b29db147f2b63 `taxonomy.py` assigns X and Xc ice fractions of 0.05 and 0.04. The same module describes X as a P/M/E mixture of 58%/37%/4% by object count and Xc as 54%/36%/9%; component ice fractions are P 0.15 and M/E 0.00. Its module note says every ice fraction lacks a source. The code gives no meaning or mass-basis rule that derives the X/Xc values from those components, and number shares do not themselves define a bulk mass fraction. Verdict: document a matched aggregation basis or label the values as scenarios; no replacement inferred. **rc-468**. Extracted: `extracted_data/r605_x_complex_ice_fraction_mixture.csv`.


## R606 — Q-class zero-water boundary and C-class recheck (2026-11-11)

`rc-367` already records and applies the C-class `ice_fraction=0.15` scope note: `yokoyama_2023_ryugu_c_type_sample_water_content` and current AsteroidCatalog `taxonomy.py` cite the Ryugu sample at 6.84 wt% H₂O, predominantly structural OH (p. 8), as a bound-water comparator. `beck_etal_2021_c_complex_surface_water_abundance` reports “On average C-complex Main-Belt Asteroids (MBA) have water contents of 4.5 wt%” (Abstract, printed p. 1; volume average excludes Ceres), a surface-population estimate that does not contradict the scoped C-class scenario. No duplicate C candidate opened.

`asteroidcatalog_q_zero_ice_fraction_code_current_2026`: AsteroidCatalog assigns Q `ice_fraction=0.00` and describes Q as a fresh/unweathered ordinary-chondrite analog; the taxonomy module says “every ice fraction” has no source. `mineralogy.py` gives Q metal, silicate and carbon groups but no ice group. Verdict: request a Q-specific basis and state what the hard zero excludes; no numerical replacement inferred. This is distinct from `rc-446` (S-complex zeros) and the applied C-class `rc-367`. **rc-469**. Extracted: `extracted_data/r606_q_zero_water_fraction.csv`; `extracted_data/r606_c_class_water_fraction_context.csv`.


## R607 — M-class zero-water scope (2026-11-11)

`asteroidcatalog_m_class_zero_ice_fraction_code_current_2026`: AsteroidCatalog assigns M `ice_fraction=0.00`; its taxonomy module says every ice fraction lacks a source. Rivkin et al. (2000), *Icarus* 145, abstract printed p. 351, report “over 35% of them have absorption features at 3 μm diagnostic of water of hydration” in a combined 27-object M-class sample; detections are size-dependent (75% above 65 km, 10% below). These are surface hydration observations, not a bulk or accessible-water mass fraction. Verdict: request a defined water boundary and source qualification; retain zero only as a scoped model assumption pending matched evidence. No numeric replacement inferred. **rc-470**. Extracted: `extracted_data/r607_m_class_hydration_zero_water_scope.csv`.


## R608 — Tholen E-class zero-water scope (2026-11-11)

`asteroidcatalog_e_zero_ice_fraction_code_current_2026`: AsteroidCatalog assigns Tholen E `ice_fraction=0.00`; its taxonomy module says every ice fraction lacks a source. Rivkin et al. (1995), *Icarus* 117(1), report a confirmed 3-μm absorption band on E-class 44 Nysa and a possible band on E-class 64 Angelina (Abstract, printed p. 90). The observations concern surface hydration, not a whole-body or accessible-water mass fraction. Verdict: define what the hard zero excludes and retain it only as a scoped model assumption pending matched bulk evidence; no numeric replacement inferred. The Tholen E row is distinct from Bus-DeMeo Xe. **rc-471**. Extracted: `extracted_data/r608_e_class_hydration_zero_water_scope.csv`.

## R617 — T-type accessory phase shares lack a numeric basis (2026-11-11)

`asteroidcatalog_ttype_accessory_phase_code_current_2026`: AsteroidCatalog `mineralogy.py` assigns T-type accessories of 0.08 troilite and 0.03 magnetite. The T row in `reference/taxonomy_composition.csv` lists troilite, organics and silicates and states that T has no meteorite analogue of its own; it gives no numeric derivation for these accessory shares. `kwon_et_al_2022_t_type_asteroid_surface_environment` (p. 1) reports Subaru spectra of two large T-type asteroids, (96) Aegle and (570) Kythera, notes OH and organic spectral features, and says their spectra “appear most similar to those of CI chondrites” (p. 1). The study reports surface spectra, not bulk mass percentages for troilite or magnetite across the T class. Verdict: document a source-to-model basis for the 8%/3% accessory assignments and clarify magnetite’s relationship to the coarse mineral list, or label them as explicit scenario shares; no replacement inferred. `rc-480`. Extracted: `extracted_data/r617_ttype_accessory_phase_basis.csv`.

## R618 — X/Xc albedo-split representativeness (2026-11-11)

`asteroidcatalog_x_complex_albedo_mix_code_current_2026`: AsteroidCatalog builds no-albedo X and Xc rows from the P/M/E proportions among bodies with measured albedo in `data-2026-09-26b` inside 5.5 AU: X 4,741/3,022/350 and Xc 40/27/7. Density is number-weighted; fractions, PGM factor and mineral phase/accessory mixtures are mass-weighted from those counts. The code itself warns that the measured sample “over-represents dark bodies” and that bodies without albedo “may lean more M” (`taxonomy.py`, lines 1022–1028; see also `derive.py`, lines 55–63). Verdict: establish whether those measured-albedo shares represent the no-albedo population, or retain them as a stated prior/scenario with sensitivity for the affected density and material-mixture fields; no replacement weights inferred. This is distinct from rc-468’s ice-fraction derivation and rc-346’s silicate-fraction attribution. **rc-481**. Extracted: `extracted_data/r618_x_complex_albedo_split_representativeness.csv`.


## R644 — Carbon terrestrial reference price lacks a matched basis

`spacevalue_carbon_reference_price_code_current_2026`: `MINERAL_REFERENCE["carbon"]` assigns 0.20 USD/kg, calls the material “bulk industrial carbon black,” and gives the catalog review date 2026-05-29 without a price source or quote date.

`usgs_mcs2025_natural_graphite_amorphous_price`: USGS MCS 2025, Graphite (Natural), printed p. 83, lists the 2024 U.S. amorphous natural-graphite import average unit value as $640/metric ton at foreign ports ($0.64/kg). `sp_global_2025_us_n330_carbon_black_spot_price`: Platts reports N330 carbon black at $0.83/lb ex-works US Gulf Coast on May 30, 2025 (~$1.83/kg). These comparators have different product and delivery bases and do not establish an asteroid-carbon price. Verdict: request a matched product, grade, date, and delivery basis; preserve $0.20/kg as an explicit scenario pending that basis, with no replacement inferred. **rc-508**. Extracted: `extracted_data/r644_carbon_reference_price_comparators.csv`.


## R645 — Organics terrestrial reference price has no product basis

`spacevalue_organics_reference_price_code_current_2026`: `MINERAL_REFERENCE["organics"]` assigns 0.50 USD/kg and describes the item as “Complex organic macromolecules (kerogen-like).” The row gives the catalog review stamp 2026-05-29 but no saleable product form, price source, grade, quote basis, or quote date.

Verdict: request a matched terrestrial product and price basis, or identify 0.50 USD/kg as a scenario with sensitivity bounds. The existing candidates rc-384, rc-429, and rc-437 address asteroid composition shares, in-space utility, and processing energy; they do not establish this terrestrial reference price. Retain the value pending that basis; no replacement inferred. **rc-509**. Extracted: `extracted_data/r645_organics_reference_price_basis.csv`.


## R646 — Three mineral reference prices lack product-matched bases

`spacevalue_other_mineral_reference_price_code_current_2026`: `MINERAL_REFERENCE` sets spinel to 0.50 USD/kg (“Mg-Al oxide; high-T refractory”), phyllosilicates to 0.05 USD/kg (“hydrated clays, priced as dehydrated rock”), and generic oxides to 0.10 USD/kg (“Generic metal-oxide bulk”). Each row carries the catalog review date but names no price source, grade, or quote basis.

Verdict: these are distinct products, so identify and cite each matching terrestrial product and price basis; otherwise retain each value only as an explicit scenario with sensitivity bounds. rc-455 covers five other silicate rows and rc-145 covers plagioclase; neither covers these rows. No replacement values inferred. **rc-510**. Extracted: `extracted_data/r646_other_mineral_reference_price_basis.csv`.


## R649 — Awaruite trace yields lack a host-population basis

- `spacevalue_awaruite_trace_yields_code_current_2026`: Spacevalue `catalog.py` at main commit `f836611f15dbb0ef511fe134bd5ac8192e3bea16` assigns awaruite Pt 75, Pd 50, Ir 20, Ru 15, Os 10, Rh 7.5 and Au 5 ppm by mass; these sum to 182.5 ppm. The code calls the PGM levels “~5× the nickel-iron baseline” and describes terrestrial ophiolite PGM enrichment as 10–100× chondritic, without identifying the population or showing how either statement yields these numbers.
- `kutyrev_et_al_2023_awaruite_pge_behavior`: Kutyrev et al., “Behavior of platinum-group elements during hydrous metamorphism: constraints from awaruite (Ni3Fe) mineralization,” *Lithosphere* 2023(1):126, abstract: three studied ophiolite awaruite populations had “no significant PGE concentrations measured,” despite associated, separate PGM inclusion groups. The abstract reports rare Galmoenan awaruite analyses up to 3 ppm Pd and notes the new data differ from earlier reports of up to the first 10 ppm PGE. This is a locality-specific comparator and does not establish an asteroid awaruite composition.
- Upstream cell: `spacevalue.catalog.MINERAL_DB["awaruite"]["yields"]`. Verdict: identify whether the yields describe trace elements dissolved in the Ni3Fe host or separate included PGM, provide the population and derivation for the 5× vector, or label it as a scenario with sensitivity. The terrestrial studies are not direct asteroid composition measurements; no replacement inferred. Distinct from rc-368 (bulk PGM enrichment), rc-433 (kamacite/taenite trace partition), and rc-512 (native-PGM alloy composition). **rc-513**.
- Extracted: `extracted_data/r649_awaruite_trace_yield_scope.csv`.

## R648 — Native-PGM alloy yield vector lacks a traceable population basis

- `spacevalue_native_pgm_yield_vector_code_current_2026`: Spacevalue `catalog.py` at main commit `f836611f15dbb0ef511fe134bd5ac8192e3bea16` defines `native-pgm` yields of Pt 0.70, Pd 0.15, Ir 0.08, Os 0.05, Ru 0.01 and Rh 0.01. Its comment calls this a “Composition midpoint of placer-class native platinum compositions”; the record names no dataset or averaging method and says the phase is reserved for high-confidence per-asteroid overrides.
- `cabri_harris_weiser_1996_pgm_placer_compositions`: Cabri, Harris & Weiser, “Mineralogy and distribution of platinum-group mineral (PGM) placer deposits of the world,” *Exploration and Mining Geology* 5(2) (1996), printed p. 83, report 211 Liard River grains: 197 Pt–Fe alloys, 3 native platinum, 10 Os–Ir–Ru–Pt alloys and 1 sperrylite. They report grain maxima including 5.6% Pd, 12.6% Ir, 3.2% Os, 4.1% Rh and 1.6% Ru. On printed p. 96, 178 Nawngpusawng grains are 70% Pt–Fe, 26% Os–Ir–Ru–Pt and 4% sulfide/sulfarsenide; Pt–Fe compositions have variable minor elements. These are locality-specific grain populations and maxima, not a single generic yield vector.
- Upstream cell: `spacevalue.catalog.MINERAL_DB["native-pgm"]["yields"]`, consumed in the per-mineral value path. Verdict: identify the cited population and averaging method for the midpoint, or label the vector as an explicit scenario and show sensitivity for override use. The cited placer survey does not establish this vector as a universal native-PGM composition; no replacement inferred. Distinct from rc-368 (bulk PGM enrichment), rc-433 (Fe-Ni trace partition), and rc-511 (cohenite yield boundary). **rc-512**.
- Extracted: `extracted_data/r648_native_pgm_composition_scope.csv`.

## R647 — Cohenite terrestrial value omits its formula carbon

`spacevalue_cohenite_product_value_code_current_2026`: `catalog.py` describes cohenite as `(Fe,Ni)3C`, says “The carbon is not a yield” (lines 1907–1912), and supplies only iron=0.904 and nickel=0.029 yields, with no direct price. `cargo.py` computes mineral value by summing only the listed yield components against their elemental prices (lines 157–200). The yield fractions total 0.933, leaving 0.067 outside the price sum; the formula’s stoichiometric carbon fraction is 0.0668, computed from the code’s atomic masses.

Upstream cell: `MINERAL_REFERENCE["cohenite"]` (`ref_price_usd_per_kg=None`) and `cargo._mineral_implied_value`. Verdict: define whether Earth return sells cohenite as carbide or separates Fe/Ni, and account for or explicitly exclude the carbon under that product boundary. No matched cohenite price or netback is given in the code; no numeric replacement inferred. Distinct from rc-456 (kamacite/taenite Earth-sale route), rc-452 (cohenite processing energy), and rc-508 (carbon reference price). **rc-511**. Extracted: `extracted_data/r647_cohenite_earth_sale_value_basis.csv`.
