# Domain 2 Findings — composition → commodity value mapping

Backings: AsteroidCatalog `taxonomy_composition.csv` material fractions (metal, silicate, carbon, ice), `mineralogy.py` phase splits (`comp_phases_detailed`), `PGM_ENRICHMENT_BY_TYPE`, and economicspace `mineral_value.py` mineralogy and nickel-iron yields.

## Round 1 - First sources

- **hein2020** [T1] (Acta Astronautica 174:59-71; arXiv v11 hosted until 2026-09-26, then un-hosted; moved to d22 in R77): the peer-reviewed TEA of asteroid mining, with water for space and platinum for Earth as separate markets (as the pipeline splits them). Pt demand anchored at $40,449/kg and 254,582 kg/yr, PED -0.6 to -0.5; sensitivity at $30k and $70k/kg. `extracted_data/composition_value_key_numbers.csv`. (Its "150 kg/s/kg" was a misreading: 150 kg is the craft dry mass; see R61.)
- **nat_dms2023** [T1, hosted, CC BY] (Sci Rep 13:6497): metal dissolution from metal-rich meteorite proxies with a deep eutectic solvent (ChCl:2EG). NEAs 1986 DA and 2016 ED85 show 85% surface metal / 15% silicate against the M row's metal 0.50 (surface, not bulk).
- **asime2018** [T2] (Graps et al. 2019 white paper; un-hosted): meteorites hold up to 22% water, so C-complex ice 0.10-0.30 is a population maximum; primitive, water-rich composition correlates with albedo below ~7.5% (a possible guardrail).
- **lewicki2023** [T2] (decadal white paper; un-hosted): a "Mine Project Value Curve" of value vs resource confidence.
- **cannon2023** [T1] (PSS 215:105608; CC BY-NC-ND, skipped by owner decision): which classes carry recoverable precious and structural metal.

## Round 2 - PGM gradient and Vesta

**usgs_pp1802n** [T3] (USGS PP 1802-N; public-domain excerpt quoted here):

| body / phase | Pt abundance | anchors |
|---|---|---|
| Iron meteorites ("best analogs for the composition of Earth's core") | 2.4–16 ppm (Wasson et al. 1989) | M / Xe 2.0×; Xk/E/Xc 1.5–2.0× |
| Upper mantle | ~0.002–0.005 ppm (2–5 ppb; Maier et al. 2012) | A/R/O 0.5× |
| Upper crust (basaltic) | ~0.0005 ppm (0.5 ppb; Rudnick & Gao 2003) | V 0.2× |

The enrichment factors are right to order of magnitude; the ~4-orders gap between metal and crust supports intermediate X values and 1.0 for undifferentiated types.

**toplis2014** [T2, hosted, NTRS]: Vesta's core radius 90–120 km of metal and sulphide; HEDs as parent-body analogues, supporting the differentiated-body model behind the V row.

## Round 3 - bennu_volatiles_2025 [T1, hosted, CC BY]

Nature Astronomy 9:199–210: OSIRIS-REx Bennu samples: total C 4.5–4.7 wt%, N 0.23–0.25 wt%, ammonia ≈40% of N; regional aliphatic/aromatic C up to ~2.5 wt%; Bennu more volatile-rich than Ryugu and most meteorites; CI/CM/CY baseline ~1–3 wt% C, rarely ~5. `extracted_data/bennu_volatiles_key_numbers.csv`. The B row's carbon_fraction 0.30 is 6-7x the measured total C, so it cannot mean elemental carbon (Round 8). Ammonia is a volatile class upstream does not model.

## Round 4 - C-type hydration

- **ryugu_hydrated_2023** [T1, hosted, CC BY] (Nature Astronomy 7:170–181): a dehydrated space-weathered skin (~66% of grains, ≥1.5 µm deep) over an interior retaining structural –OH. Spectral ice estimates for C-types are therefore low bounds. `extracted_data/ryugu_hydrated_interior_key_numbers.csv`.
- **ryugu_soluble_organics_2023** and **ryugu_macromolecular_om_2023** [T1, open_not_pulled] (Science 2023): CHNOS organics of abiotic origin; aqueously altered macromolecular matter with phyllosilicates and carbonates.

## Round 8 - Per-class carbon; the CI endmember

- **glavin_2018** [T2, hosted, NTRS]: C ~0.1 wt% (CK) to ~5 wt% (CI); IDPs ~12 wt%; hydration minerals (serpentine, saponite, smectite in CI, CM, CR and Tagish Lake; tochilinite in CM2). The B/C-complex 22–30% defaults are 4–6× the most carbon-rich C-type: "carbon-bearing material", not elemental C. `extracted_data/glavin_2018_chondrite_volatiles_key_numbers.csv`.
- **ryugu_ivuna_2023** [T1] (Science 379:786; author version, not hostable): Ryugu is CI1; structural water like CI, interlayer water largely lost; below ~100 °C since alteration. Free ice is essentially absent, so ice priced at the in-space water proxy is recoverable only through dehydroxylation (d05). `extracted_data/ryugu_ivuna_2023_key_findings.csv`.

## Round 11 - Meteorite density and the differentiation mechanism

- **wilkinson_robinson_2000** (see d01).
- **mandler_elkins_tanton_2013** [T1, open_not_pulled]: Vesta = ~60–70% equilibrium magma-ocean crystallisation with residual melt extracted to shallow chambers: core, mantle (dunites, harzburgites, diogenites) and eucrite crust, whose PGMs went to the core. The mechanism behind `PGM_ENRICHMENT_BY_TYPE`.

## Round 12 - farnocchia_2024

Second M-type density, registered here because the M row's composition and density feed both domains; the write-up is in domain 1's Round 12 block.

## Round 36 - Per-type material anchors

`extracted_data/r36_per_type_materials_key_numbers.csv`:

- **elkins_tanton_2020_psyche_preflight** [T1] (JGR Planets 125, CC BY-NC; author mirror): the paper the M row cites. Psyche "between ~25 vol% metal and ~60 vol% metal" (p10; Point D ~25/55/20 metal/pyroxene/pores); the M row's 0.50/0.45 mass split is ≈34 vol% metal, inside. Surface endmembers 90 wt% metal → 6 wt% opx → pure metal (p9); 25–80 km silicate veneer on a stripped core (p13); iron 7,000–8,000, pallasite 4,100–7,800, mesosiderite 3,100–7,200 kg/m³ vs Psyche ~4,000 (p10); pallasites ~65 vol% olivine, Ni ~9–12 wt% (p11); CB chondrites ~60 vol% metal vs the Cb row's 0.01 (pp11–12).
- **reddy_asteroids_iv_mineralogy** [T1] (Asteroids IV; arXiv preprint, un-hosted): A-types monomineralic olivine Fo85–93 (p8); R chondrites 65–78% olivine (p9); HED pyroxene Fs23–56 / Wo2–14 (±3 / ±1 mol%, p7); S/Q as ordinary chondrites via Dunn et al. 2010b (<2 mol%, ~50 powders); Itokawa LL with ol/(ol+pyx) 76%, Eros in the L/LL zone; A/S/Q/V analogues are 91% of meteorites (p8).
- **lodders_2010_solar_abundances** [T2] (arXiv preprint, un-hosted): Table 2 CI (Orgueil): C 34,800 ppm (3.48 wt%); Fe/Mg/Si/O/S 18.5/9.6/10.7/45.9/5.35 wt%; PGM 3.29 ppm. Carbon defaults are ~7–9× elemental C; Fe/Mg/Si agree with Cannon's Palme 2014 values within 2%. Full table: `extracted_data/lodders_2010_ci_composition_table2.csv` (incl. Ni 10,800, Co 506, Cr 2,650 ppm).

## Round 38 - D/T/P anchors

- **marschall_2025_67p_refractory_ice_ratio** [T1] (PSS 259:106061): 67P refractory/ice 0.5 < chi < 1.7, water 28–52 wt% (~35–40% preferred), formed at 25–35 au. D ice 0.25 and P 0.15 sit below.
- **rubin_2019_67p_abundances** [T1] (MNRAS 489:594; un-hosted): per-water CO2 4.7±1.4, CO 3.1±0.9, O2 3.1±1.1; CH4 0.34, C2H6 0.29, CH3OH 0.21, H2CO 0.32; near-solar O/Si and C/Si, N depleted (as Halley).

Every one of the 32 types now has a material anchor. `extracted_data/r38_primitive_type_materials_key_numbers.csv`.

## Round 61 - hein2020 plant economics

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
- `mahlke_2022_phd_thesis_asteroid_taxonomy` (abstract) and `lebofsky_et_al_1990_low_albedo_3um_photometry` (unread).

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
