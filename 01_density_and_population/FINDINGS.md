# Domain 1 Findings — density by spectral type, PGM factors, population statistics

Backings: per-spectral-type density and PGM factors in AsteroidCatalog `reference/taxonomy_composition.csv` (`TAXONOMY_COMPOSITION`, loaded by economicspace `catalog.py`); diameter, albedo and taxonomy inputs; ranking quality of the whole pipeline.

## Round 1 - First sources

### carry2012 [T1] — Carry (2012), "Density of asteroids", PSS 73:98-118

Review of mass and volume for 287 small bodies, with bulk density and macroporosity per body averaged by Bus-DeMeo class in three precision tiers (Table 3; `extracted_data/carry2012_density_by_type.csv`). Hosted until 2026-09-26, then un-hosted (arXiv default licence). Round-1 comparison with `TAXONOMY_COMPOSITION` (g/cm3; see the 2026-09-26 correction below):

| type | carry2012 best tier | pipeline value | verdict |
|---|---|---|---|
| S | 2.70–2.72 (N=144) | 2.70 | agree |
| C | 1.41 (n50) / 1.25 (n20); no-restriction 1.57±1.38 | 1.50 | agree within scatter |
| B | ~2.19–2.38 (N=4) or a stray row 1.33 | 1.30 | possible discrepancy (tiny N) |
| Ch | 1.70–1.96 | 1.50 | mild (ours lower), N=18 |
| Cb | 1.43–1.88 | 1.40 | agree at n50 |
| K | 3.54 (n50 and n20); no-restriction 4.25±2.03 | 2.50 | ours ~1 low |
| L | 3.22–3.24 | 2.80 | ours ~0.4 low |
| Xk | 3.79–4.22 | 3.60 | agree at the lower tier |
| Xe | 2.60–2.91 | 3.80 | ours ~0.9 high |
| Xc | 4.63–4.96 | 2.50 | ours ~2 low (N=3) |
| A | 3.73 (one body) | 3.20 | mild |
| Q | 1.9–2.2 | 3.00 | possible discrepancy |
| D | unmeasured | 1.20 | no anchor |

Dwarf planets have little macroporosity; bodies under 400 km can carry large voids, and C/S density rises with diameter, so one constant per type is an approximation that worsens for small bodies.

### simda2024 [T3] — Kretlow, SiMDA (open service)

428 bodies with bulk density and class (live CSV, 2026-09-17; derived statistics committed):

| type | N | SiMDA mean | median | pipeline | verdict (median) |
|---|---|---|---|---|---|
| S | 53 | 3.46 | 2.87 | 2.70 | agree (+0.17) |
| Ch | 47 | 1.98 | 1.68 | 1.50 | mild high |
| C | 33 | 1.83 | 1.63 | 1.50 | mild high |
| B | 10 | 1.97 | 2.10 | 1.30 | ours ~0.8 low |
| Xk | 13 | 4.60 | 3.93 | 3.60 | +0.33 |
| L | 4 | 4.60 | 4.95 | 2.80 | ours ~1 low (N=4) |
| Xe | 4 | 3.56 | 3.89 | 3.80 | agree; contradicts carry2012 |
| K | 2 | 3.16 | 3.48 | 2.50 | supports carry2012 |
| D | 3 | 1.41 | 1.27 | 1.20 | agree; first D anchor |
| V | 3 | 2.82 | 3.41 | 2.90 | mild high |

The table tracks medians for S/X/Cgh/D (±0.2) but sits ~0.7-1 g/cm3 low for B, L and K.

### Other Round-1 sources

- **dziadura2023** [T1] (A&A 680, A77; CC BY): Yarkovsky drift with Gaia DR3 for NEAs; read in R73.
- **lodders_palme2009** [T2] (72nd MetSoc abstract; un-hosted 2026-09-26): CI bulk-rock ppm Ru 0.686, Rh 0.139, Pd 0.558, Ag 0.201, Os 0.493, Ir 0.469, Pt 0.947, Au 0.146; PGM total ≈3.29 ppm. Divided by a metal fraction of ~0.09-0.15 it gives ~22-37 ppm in metal, the chain behind `catalog.py`'s "~37 ppm total PGM+Au in nickel-iron alloy". Per-type enrichment factors remain uncited here (see d02).
- **epsc2022_context** [T2] (EPSC-2022): read in R73.

## Round 3 - harris_dabramo_2021 [T1]

Harris & D'Abramo, Icarus 2021: the corrected NEA population estimate (the 2015 numbers suffered from MPC rounding of H to 0.1 mag), discoveries through 2020-08-03, to pair with `catalog_date`. Paywall-blocked; abstract only.

## Round 5 - adam_2017 [T1]

40 bulk densities from ADAM shape models (A&A, 10.1051/0004-6361/201629956), a second per-body sample and a possible D-type anchor. Read in R71.

## Round 11 - wilkinson_robinson_2000

Ordinary chondrites: H 3.44±0.19, L 3.40±0.15, LL 3.29±0.17 g/cm3 (82 samples, ~1%); the gap to the asteroid-scale S median 2.70 is macro-porosity. Read in R73. Also in d02's Round 11 block.

## Round 12 - Psyche density (M row)

- **siltala_granvik_2021** [T1, hosted]: Psyche 3.88±0.25 g/cm3, ruling out an exposed iron core; the measurement the M row (3.90, metal 0.50) cites.
- **farnocchia_2024** [T1, open_not_pulled]: GM 1.601±0.017 km^3/s^2 from close-approach astrometry; 4.17±0.15 g/cm3. The M row sits at the low end.

## Round 38 - kretlow_2022_rosa_mass_density [T1, hosted, CC BY]

(223) Rosa, a Tholen P-type, D = 83±8 km: M = (3.62±1.25)×10^17 kg from three encounters, rho = 1.2 ± 0.5 g/cm3, "consistent with typical densities for Tholen taxonomy P-type asteroids" (~1.3). SiMDA has no P bodies; catalog.py's P = 1.80 is the older estimate Kretlow says "did not match very well" (rc-007).

## Round 40 - chesley_2014_bennu_orbit_bulk_density [T1]

Icarus 235:5-22: Yarkovsky da/dt = (-19.0±0.1)e-4 au/Myr (284 ± 1.5 m/yr); rho = 1260 ± 70 kg/m^3, M = (7.8±0.9)e10 kg, GM = 5.2±0.6 m^3/s^2 (Table 7, p56). environments.csv's Bennu (7.329e10 kg, r 244.5 m; ~1197 kg/m^3) sits at -0.8 sigma. Un-hosted 2026-09-26. `extracted_data/r40_bennu_mass_density_key_numbers.csv`.

## Round 41 - The AsteroidCatalog data backbone registered

- **berthier_2023_ssodnet** [T1, arXiv hosted]: ssoBFT parquet 1,563,708 rows × 266 columns (855.8 MB, hash-recorded). Eros mass exact (6.687e15 kg); Ryugu +0.44σ, Didymos −0.12σ; Ceres radius +0.01%; Bennu 0.02%. Eros's +14% "density gap" is a radius convention (r=8420 m vs equivalent-sphere D 17.6 km).
- **mainzer_2019_neowise_v2** [T3, bundle hosted]: TAP 183,412 rows vs the release's 183,419; Bennu, Ryugu, Eros, Didymos and Ceres are absent (better radar or spacecraft values exist).
- **jpl_sbdb_small_body_database** [T3]: 1,566,680 asteroids; Ceres D 939.4 km, pV 0.090, H 3.34 (radius 469700 vs 469730 m).
- **fowler_chillemi_1992_iras_mps_diameter_formula** [T2, hosted chapter]: D_km = 1329/sqrt(pV)*10^(-H/5); over 149,277 ssoBFT bodies the implied C is 1328.4 / 1329.0 / 1329.6 (p05/p50/p95). Read directly from the page image in R70: 10^3.1236 = 1329.2.
- **demeo_2009_bus_taxonomy_near_ir** [T1, open_not_pulled]: the class system behind both density anchors.

## Round 42 - MP3C, MPC links, Bus-DeMeo bundle

- **mp3c_minor_planet_physical_properties_catalogue** [T3]: v3.2.0-beta.1 (2024-02-13); 1,335,502 best rows, 6,086,962 aliases; Eros M = 6.69e15 kg (+0.04%), Bennu D 0.492 km. Numbered bodies key through packed MPC aliases (`mp3c_main.name`, priority 3).
- **mpc_mpcorb_extended_designation_links** [T3]: 182 MB gzip, structure as AsteroidCatalog's `identity.py` expects.
- **bus_demeo_2020_pds_taxonomy_bundle** [T3, hosted as `full_texts/bus_demeo_2020_pds_bundle.zip`]: 371 classified bodies (S=144; L 22, Xk 18, V 17, Ch/D/K/Cgh ~10-16, T 4); 24 of 31 named types covered (none for Sk, Sl or Tholen-only M/E/P/F/G). `extracted_data/r42_bus_demeo_class_distribution.csv`.

SBDB per-object queries work at `ssd-api.jpl.nasa.gov/sbdb.api?sstr=<name>` (R41's 400s were the bulk endpoint).

## Maintenance (2026-09-26) - carry2012 Table 3 re-read

- Un-hosted: carry2012, chesley_2014_bennu_orbit_bulk_density (arXiv default licence), lodders_palme2009 (no licence); numbers extracted first.
- carry2012 Table 3 by word coordinates: C's 20% tier 1.33 ± 0.58 (not 1.25), Cb 1.25 ± 0.21, Ch 1.41 ± 0.29; Q has no density at any tier (the 2.23/1.93 were R = 2.23 ± 1.02, N=1, and V = 1.93 ± 1.07, 3 bodies); K's 3.54 ± 0.21 is one body. The B "stray 1.33" is C's; the Q discrepancy has no basis (**rc-006 withdrawn**); the K case rests on one body (rc-001 corrected). C still agrees.
- carry2012 is PSS 73:98-118, DOI 10.1016/j.pss.2012.03.009 (the registry DOI and heading were wrong).
- simda2024 re-classed open_service. Backfill rows in `extracted_data/backfill_2026-09-26_key_numbers.csv`.

## R70 - Full extraction (2026-09-27)

`r70_berthier_2023_ssodnet.csv` (16), `r70_berthier_2023_ssodnet_table_c8_class_complex.csv` (19), `r70_bus_demeo_2020_pds_taxonomy_bundle_per_body_classes.csv` (371), `r70_fowler_chillemi_1992_iras_mps_diameter_formula.csv` (13), `r70_kretlow_2022_rosa_mass_density.csv` (10), `r70_mainzer_2019_neowise_v2.csv` (14), `r70_siltala_granvik_2021.csv` (13). NEOWISE v2 NEO pV median 0.135 (p25-p75 0.046-0.252; n = 1,509); 41.7% below 0.1, 18.4% above 0.3; beaming median 1.40.

## R71 - The un-hosted PDFs and owner copies (2026-09-27)

Files: `r71_adam_2017_key_numbers.csv` (20), `r71_adam_2017_table2_spin_states.csv` (50), `r71_adam_2017_table4_adam_volume_density.csv` (50), `r71_adam_2017_table6_literature_densities.csv` (11), `r71_carry2012_key_numbers.csv` (40), `r71_carry2012_table1_per_body_mass_diameter_density.csv` (287), `r71_carry2012_table2_meteorite_bulk_density.csv` (19), `r71_carry2012_tableA1_mass_estimates.csv` (981), `r71_carry2012_tableB1_diameter_estimates.csv` (1454), `r71_carry2012_tableC1_indirect_density_estimates.csv` (33), `r71_chesley_2014_bennu_orbit_physical_key_numbers.csv` (30), `r71_chesley_2014_table6_asteroid_perturber_gm.csv` (25), `r71_chesley_2014_table8_earth_close_approaches.csv` (11), `r71_lodders_palme2009_table1_ci_and_solar_system_abundances.csv` (83). R72 checked carry2012 Table 1 row by row (seven rows print the mass at the error's exponent) and recomputed adam_2017's 41 densities (all agree).

## R72 - Remaining tables; densities against AsteroidCatalog (2026-09-27)

`r72_chesley_2014_table10_impact_resonances.csv` (8), `r72_chesley_2014_table11_formal_uncertainties.csv` (8), `r72_chesley_2014_table5_model_variations.csv` (35), `r72_chesley_2014_table9_keyholes_2135.csv` (78), `r72_chesley_2014_tables1_2_radar_astrometry.csv` (32). The 78 keyholes sum to 3.68 x 10^-4 (paper: 3.7 x 10^-4) and 8 exceed 10^-5, matching Table 10.

adam_2017 vs AsteroidCatalog: C median 1.60 (1.5), S 2.70 (2.7), Psyche/Kalliope 3.7 (3.9) agree. **(87) Sylvia, Tholen P, 1.39 +/- 0.08** added to rc-007 (P 1.8). (89) Julia 4.5 +/- 1.3 leans with rc-001; Pallas 2.72 +/- 0.17 is the large-B case rc-003 was declined over; Ch (adam ~1.9, SiMDA 1.98, carry2012 1.41 +/- 0.29) brackets 1.5.

## R73 - Blocked downloads read (2026-09-27)

- **dziadura2023** (publisher PDF from Univ. Alicante; CC BY): `r73_dziadura2023_tableA1_yarkovsky_densities.csv` (57 = 49 accepted + 8 marginal NEAs), `r73_dziadura2023_table2_observation_data.csv` (57; N_total = N_MPC + N_radar + N_Gaia on every row; 20 PHAs, 3 binaries), `r73_dziadura2023_tableA1_reference_key.csv`, `r73_dziadura2023_key_numbers.csv`. Kept as printed: Table 1's 154 094 vs 54 094 in the text; four rows print da/dt equal to their diameter; five print no density; (4769) Castalia negative; (88710) 2249.96 vs 2032 kg/m3. Yarkovsky S-type NEAs median 1.37 g/cm3 (N = 23, 0.73-3.70) vs S 2.7, Q median 1.47 (N = 9) vs Q 3.0; errors 30-60%, so **rc-045** and **rc-046** ask only for a small-NEA caveat. The backfill's 446 / 93 / 54,094 are fitted orbits; detections are 49 NEAs.
- **wilkinson_robinson_2000** (ADS scan): `r73_wilkinson_robinson_2000_tables2_3_sample_bulk_densities.csv` (82), `..._table4_group_comparison.csv`, `..._table1_standards.csv`, `..._table5_shock_stages.csv`, `..._table6_asteroid_densities.csv`, `..._appendix1_bulk_geochemistry.csv` (44), `..._key_numbers.csv`. Group means recompute (H 3.44 +/- 0.19, n = 42; L 3.40 +/- 0.15, n = 30; LL 3.29 +/- 0.17, n = 9); 40 of 42 appendix rows satisfy Fe(T) = Fe(M) + 0.7773 FeO + 0.6353 FeS (Conquista, Macau off ~4.2 wt%); 39 meteorites listed vs 40 in the text. The citation is M&PS 35:1203-1213. Eros has 21-33% porosity (OC 3.40 vs 2.67 +/- 0.03); S 2.7 vs LL/L 3.29/3.40 implies ~20%.
- **epsc2022_context** (CC BY): chondritic Ru/Ir 1.51 +/- 0.05; no absolute PGE concentrations. `r73_epsc2022_context_key_numbers.csv`.

## R74 - Upstream citations registered (+22)

All `registered_not_pulled`, each tied to an AsteroidCatalog or taxonomy cell: `pravec_harris_2007_binary_angular_momentum` and `campins_1985_absolute_calibration_1_5um` (the 1329 km constant); `mainzer_2011_neowise_thermal_model_calibration` and `pravec_2012_absolute_magnitudes_wise_albedos` (merge tolerances, H offset); `buratti_2004_ds1_borrelly_photometry` (albedo floor); `ferrais_2022_kalliope_tiny_mercury` (density ceiling, Kalliope); `consolmagno_2008_meteorite_density_porosity`, `macke_2011_carbonaceous_chondrite_density_porosity` (carbonaceous ceiling); `macke_2010_enstatite_chondrite_density_porosity` (Xe density); `patzold_2016_67p_homogeneous_nucleus_gravity`, `thomas_2013_tempel1_nucleus_two_flybys` (density floor); `lauretta_2019_bennu_unexpected_surface` (B density, Bennu row); `fujiwara_2006_itokawa_rubble_pile` (Sq note); `pravec_harris_2000_fast_slow_rotation`, `holsapple_2007_spin_limits` (spin barrier); `emery_2011_trojan_nir_two_groups` (Trojan default D); `gil_hutton_brunini_2008_hilda_sdss_colors` (Hilda default); `mahlke_2022_asteroid_taxonomy_spectra_albedo` (Z row); `tholen_1984_asteroid_taxonomy_dissertation` (Tholen rows); `hasselmann_2012_sdss_taxonomy_v1_1_pds`, `carvano_2010_sdss_taxonomy_main_belt`, `ivezic_2001_sdss_solar_system_objects` (the SDSS taxonomy check).

## R113 - Taxonomy and albedo lineage (2026-10-04; +9)

AsteroidCatalog@6a2cfbc takes class from JPL `spec_B`, then `spec_T`, then SsODNet; diameter from H and albedo (measured, else `ALBEDO_BY_SPECTRAL_TYPE`, then `ALBEDO_BY_SEMI_MAJOR_AXIS_AU`, `_NEO`, fallback). Three list entries had wrong metadata (A&A 665:A26 is the registered Mahlke 2022; A&A 580:A98 is Carvano & Davalos; the Icarus PII is Mahlke, Carry & Denneau 2021).

| id | access | what it supplies |
|---|---|---|
| `bus_binzel_2002_smass2_feature_based_taxonomy` | registered | the SMASSII classes JPL serves as `spec_B` |
| `popescu_2018_movis_nir_taxonomy` | read (arXiv) | 18,265 MOVIS asteroids (6,496 final); source of the `Ad`, `Bk`, `Cgx`, `Ds`, `Kl`, `Xt` keys; WISE albedo peaks S 0.26 +/- 0.10, V 0.352 +/- 0.121, D 0.08 +/- 0.03 |
| `tinaut_ruano_2026_gaia_dr3_taxonomy` | hosted (CC BY) | 14,042 asteroids in 13 classes from Gaia DR3 (of 60,518); near-UV separates B and F |
| `masiero_2021_albedo_uncertainties_thermal_modeling` | read (arXiv) | 0.3 mag in H with 10% IR diameter gives 32-36% albedo error; ~1 mag gives ~70% albedo and ~42% diameter error (p5) |
| `myhrvold_2022_four_band_wise_asteroids` | read (arXiv) | 4,420 asteroids from 82,548 WISE observations; median diameter error 9.3% (max 37.7%) vs 24 occultations |
| `masiero_2021_neowise_reactivation_years_6_7` | read (arXiv) | 199 NEOs + 5,851 MBAs (year 6), 175 + 5,861 (year 7); ~30% NEO diameter uncertainty |
| `murray_2023_neural_network_main_belt_albedos` | read (arXiv) | ~37% lower error than a mean albedo; 585,174 main-belt predictions |
| `wang_2026_nea_albedo_from_orbital_elements` | abstract | NEA albedo by source region |
| `mahlke_carry_denneau_2021_atlas_phase_curves` | abstract (read R120) | H, G1, G2 for 94,777 asteroids from ATLAS |

Catalog medians agree with Popescu's peaks (S 0.2340, V 0.3355, D 0.0820). `extracted_data/r113_taxonomy_albedo_key_numbers.csv`. No candidate.

## R114 - PDS density and taxonomy tables (2026-10-04)

`britt_2002_pds_asteroid_densities` (23 bodies; Psyche 2.00 +/- 0.60, Kalliope 2.50 +/- 0.30 g/cm3), `neese_2010_pds_asteroid_taxonomy_v3_0` (1,198 bodies; 985 with a Tholen class: S 338, C 139, X 52, M 38, D 35, P 33, F 28, XC 23), `pentikainen_2026_gaia_dr3_asteroid_characterization` (abstract; a second Gaia DR3 class source). LCDB V3.0 is the registered `warner_harris_pravec_2009_asteroid_lightcurve_database` (d12). `extracted_data/r114_gr_links_key_numbers.csv`.

## R115 - Xe note vs Carry Table 2 (rc-077)

The Xe note's 3.55 g/cm3 enstatite-chondrite bulk density vs Carry Table 2 EH 3.47 +/- 0.21, EL 3.46 +/- 0.32 (mean 3.465, 2.4% apart); Xe cell (2.90) unaffected. `extracted_data/r115_xe_enstatite_bulk_density_check.csv`.

## R118 - Mahlke 2022 and the SDSS taxonomy hosted (2026-10-05)

- **mahlke_2022_asteroid_taxonomy_spectra_albedo** (CC BY, arXiv 2203.11229 hosted): D-types have "featureless and strongly red-sloped spectrum"; Z-types a "diffuse cluster of feature-less, extremely red objects"; "23 asteroids (1.1 %) are classified as Z-types". No carbon abundance (context for rc-075).
- **hasselmann_2012_sdss_taxonomy_v1_1_pds** (hosted as `full_texts/sdsstax_v1_1_ast_table_pds_bundle.zip`): 63,468 classified bodies, matching economicspace's copy; the raw observation table excluded.

`extracted_data/r118_d01_queue_pull_key_numbers.csv`.

## R120 / R121 / R125 - Queue reads (2026-10-05/06)

- `thomas_2013_tempel1_nucleus_two_flybys` hosted (NTRS; Icarus 222:453-466): second comet density for the floor; density not yet extracted.
- `mahlke_carry_denneau_2021_atlas_phase_curves` read (94,777 asteroids, 127,012 phase curves), not hostable.
- `lauretta_2019_bennu_unexpected_surface` read (KU Leuven copy): "a density of 1190 ± 13 kg/m3"; ~50% macroporosity, "a microgravity aggregate".
- `emery_2011_trojan_nir_two_groups`, `ivezic_2001_sdss_solar_system_objects` and `mainzer_2011_neowise_thermal_model_calibration` (50 radar or in-situ objects calibrate NEATM) read from arXiv, not hostable.

## R155 - D-from-H constant and H tolerance confirmed (2026-10-12)

- `campins_1985_absolute_calibration_1_5um` (ADS): Sun V -26.768 +/- 0.02 (synthetic), -26.75 +/- 0.03 (measured), combined 26.762 +/- 0.017 (minus sign missing in print); inverse-variance mean -26.7625 +/- 0.0166.
- `pravec_harris_2007_binary_angular_momentum`: K = 2 AU x 10^(Vsun/5) = 1329 +/- 10 km (~1% systematic); 1329.09 km with the IAU 2012 AU. AsteroidCatalog@86cfc54's V_SUN -26.762 and 1329 match exactly.
- `pravec_2012_absolute_magnitudes_wise_albedos` (preprint): catalog H bias under 0.1 mag for large bodies and -0.4 to -0.5 near H = 14, as merge.py (0.30 mag) and physics.py (0.75 mag) quote; revised WISE albedos 0.057 (C/G/B/F/P/D), 0.197 (S/A/L).
- `gil_hutton_brunini_2008_hilda_sdss_colors`: 122 Hildas: D 51, X (P) 49, C 19; small Hildas split evenly D/P; consistent with the catalog's default (Elsevier copy, not hostable).

`extracted_data/r155_queue_open_copies_key_numbers.csv`.

## R165 - Candidate (2026-10-14)

rc-140 (method): build the PGM table taxonomy.py proposes: CI 3.29 ppm / metal fraction gives 54.8 ppm for S-complex and Q (factor 1.48 vs 37 ppm), 41.1 for K (1.11), 65.8 for L (1.78). Text in `revision_candidates.csv`.

## Round 175 - Tholen dissertation read (2026-10-16)

`tholen_1984_asteroid_taxonomy_dissertation` read live (UA DSpace REST; 168 pp; author copyright, not hosted): the original source behind the Tholen-class citation.
