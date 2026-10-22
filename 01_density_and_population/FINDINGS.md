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

`extracted_data/simda2024_density_by_class.csv`.

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

`extracted_data/r41_stage1_backbone_key_numbers.csv`.

## Round 42 - MP3C, MPC links, Bus-DeMeo bundle

- **mp3c_minor_planet_physical_properties_catalogue** [T3]: v3.2.0-beta.1 (2024-02-13); 1,335,502 best rows, 6,086,962 aliases; Eros D 15.77 km, pV 0.385, M = 6.69e15 kg (+0.04%), Bennu D 0.492 km. Numbered bodies key through packed MPC aliases (`mp3c_main.name`, priority 3).
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
- **wilkinson_robinson_2000** (ADS scan): `r73_wilkinson_robinson_2000_tables2_3_sample_bulk_densities.csv` (82), `r73_wilkinson_robinson_2000_table4_group_comparison.csv`, `r73_wilkinson_robinson_2000_table1_standards.csv`, `r73_wilkinson_robinson_2000_table5_shock_stages.csv`, `r73_wilkinson_robinson_2000_table6_asteroid_densities.csv`, `r73_wilkinson_robinson_2000_appendix1_bulk_geochemistry.csv` (44), `r73_wilkinson_robinson_2000_key_numbers.csv`. Group means recompute (H 3.44 +/- 0.19, n = 42; L 3.40 +/- 0.15, n = 30; LL 3.29 +/- 0.17, n = 9); 40 of 42 appendix rows satisfy Fe(T) = Fe(M) + 0.7773 FeO + 0.6353 FeS (Conquista, Macau off ~4.2 wt%); 39 meteorites listed vs 40 in the text. The citation is M&PS 35:1203-1213. Eros has 21-33% porosity (OC 3.40 vs 2.67 +/- 0.03); S 2.7 vs LL/L 3.29/3.40 implies ~20%.
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

rc-140 (method): build the PGM table taxonomy.py proposes: CI 3.29 ppm / metal fraction gives 54.8 ppm for S-complex and Q (factor 1.48 vs 37 ppm), 41.1 for K (1.11), 65.8 for L (1.78). Text in `revision_candidates_closed.csv`.

## Round 175 - Tholen dissertation read (2026-10-16)

`tholen_1984_asteroid_taxonomy_dissertation` read live (UA DSpace REST; 168 pp; author copyright, not hosted): the original source behind the Tholen-class citation.
## Round 195 - AsteroidCatalog README contract verified against data-2026-09-29c (2026-10-19)

Evidence-only sweep; no new sources, no RC opened from it. Every quantitative claim in the
AsteroidCatalog README (the user-facing data contract since commit 84e026e) was re-measured on the
pinned release and reproduces exactly:

- Row count 1,568,882 matches the README opening figure for `data-2026-09-29c`.
- Psyche diameter spread claim ("spreads 30% across the four sources"): published `diameter_spread` = 0.298613 on -29c, provider SsODNet, n_sources=4.
- X-complex split medians (README L389-390, CHANGELOG L188): reproduced with upstream's OWN selection from `tools/density_evidence.py` (`spectral_type_source` in source/tholen, mass_measured AND density_measured flags, relative mass sigma in (0, 0.20], a < 5.5 AU), grouping by label group per README L393: dark band p_V < 0.10 N=15 median 1.4359; moderate band 0.10-0.30 N=17 median 3.4496 - documented as 1.44 (N=15) and 3.45 (N=17).
- JPL Tholen label reproduction ("80 of the 83 bodies it types E, M or P that carry an albedo"): exact on -29c - base N=83, in-bin 80; misses are Tokio (M at p_V 0.0694), Penelope (M at 0.0400), Larissa (P at 0.1690).
- Densest of the masses known to 5% ("77 ... Kalliope (4.18) and Psyche (4.14)", claim build `data-2026-09-26`): -29c count is also exactly 77, top two Kalliope 4.1753 / Psyche 4.1426; next Lydia 3.538.
- README example dicts match live tables at HEAD: `TAXONOMY_COMPOSITION["M"]` (group X-complex, density_est_gcm3 3.9, metal_fraction 0.5); S-type `comp_phases` all eight entries exact; S-type `comp_phases_detailed` documented entries exact (kamacite 0.033 / taenite 0.0228 / tetrataenite 0.0042 / merrillite 0.004 / chlorapatite 0.002).

Note for future rounds: the release identity `estimated_mass_kg = density_gcm3 x pi/6 x diameter_km^3`
holds for Eros BY CONSTRUCTION (density is computed from that mass-diameter pair), so rc-174 remains a
diameter-convention claim, not an arithmetic gate violation - README section 5 is accurate as written.

This surface (README prose claims vs release) is now covered; do not re-sweep unless the README or the pinned release changes.
## Round 199 - pinned-catalog release registered; economicspace README provenance contradiction found -> rc-176; measured-diameter false-flag trap closed (2026-10-19)

R198's new completeness rule (grep bare NTRS accession tokens, not only URLs/DOIs) was run across all three upstream repos: 420 files scanned for NTRS accessions, AIAA paper numbers, NASA report designators, GAO and OIG ids - **zero unregistered tokens**; the johnson deck was the last invisible citation. That seam is closed; recorded here so no round repeats the sweep unless upstream drifts. (Tooling note: economicspace/asteroid_pipeline holds multi-GB generated catalogs - 2.2 GB asteroid_catalog.csv, ~10-15 MB transportation summaries across backup snapshots - any repo-wide scan must size-gate before opening files.)

Following the provenance trail into that catalog's own documentation found a live contradiction inside economicspace README.md about its pinned artifact: L491 says Stage 1 downloads "~310 MB gzip [that] decompresses to a ~2.2 GB CSV (the data-2026-09-29c release: 1,568,882 bodies, 102 columns)", and every element of that sentence verifies live this round - the installed file is exactly 2,201,796,047 B; wc gives header + 1,568,882 rows; the header carries 102 columns including comp_phases/comp_phases_detailed; catalog_manifest.json names release_tag data-2026-09-29c with pipeline_version 1.8.1 (the "data contract 1.8.1" of L166); the gzip asset is 325,443,405 B = exactly 310.4 MiB under binary units. But **L999's Output tree still describes that same file as "(~1.2 GB, the pinned release)"** - wrong under either unit convention (decimal ~2.2 / binary ~2.05 GiB), and git log -S shows both this line and a sibling in verify_stage1.py's check_bytes docstring ("a few seconds for ~1.2 GB") were born together in commit 069233c (2026-09-23, Stage-1 pinned-install PR #110) when an earlier build was pinned - and survived the repo's own repin sweep: versions.md records "the pinned release unpacks to 2.2 GB, and code, CI and docs still said 862 MB, 868 MB, 0.9 GB or 1.2 GB in the present tense. Each now says what it means without a figure" (whitespace-normalized count==1). A third survivor sits in SPARK_SETUP.md's budget table: asteroid_catalog.csv | Stage 1 | **823 MB**, born 2026-09-03, with no release named although versions.md claims that table does. Opened as rc-176 [wording] - one fix pass over three sites; proposed either stating ~2.2 GB or dropping the figures per their own stated convention.

**False-flag trap closed:** economicspace README L1209 "In data-2026-09-29c, 149,718 of 1,568,882 bodies have a measured diameter" looks like it transplanted AsteroidCatalog README's figure ("(149,718 of 1,568,641 in data-2026-09-27)") onto the new denominator - but counting `diameter_source == "measured"` (the canonical flag per AC tools/audit_catalog.py) on the release parquet gives **exactly 149,718 of 1,568,882**. The numerator is genuinely unchanged between builds (+241 bodies added in two days carried no new measured diameters); both documents are correct for their stamped releases. Recorded so a future round does not flag L1209 as stale.

Registered the release itself: `asteroidcatalog_release_data_2026_09_29c` [T3 open_service] with r199_catalog_release_key_numbers.csv (7 rows). Registry completeness under all token classes now confirmed against upstream at economicspace@d77f1ce.
## Round 200 - pinned-release artifact integrity proven end-to-end; measured-diameter fact now triple-corroborated (2026-10-19)

The release manifest for `data-2026-09-29c` (manifest.json, 3,599 B, gh release download this round) declares sha256 + byte counts for every asset. Verified against the artifacts actually in use:

| artifact | declared sha256 (prefix) | verified where | result |
|---|---|---|---|
| catalog_csv (decompressed, 2,201,796,047 B) | e3cd21d6645211e3…f1245 | economicspace/asteroid_pipeline/asteroid_catalog.csv (installed working copy; full-file sha256sum this round) | EXACT MATCH |
| asteroid_catalog.parquet (216,789,479 B) | 227b5e06a8a9a01f…354f3f7 | scratch copy used for the R199 measured-diameter count | EXACT MATCH |
| taxonomy.json (37,811 B) | 931767a3fe9c3d57…e275bd | economicspace/asteroid_pipeline/catalog_taxonomy.json (installed copy) | EXACT MATCH |
| rejected_entries.csv (327 B) | 417b1953fbf16f80…0350b0 | same directory | EXACT MATCH |

The installed CSV header also equals the manifest's `columns` list order-exactly (102 columns). Consequences for future rounds:

1. **Installed-copy facts are settled unless the pin moves.** Any claim about what economicspace reads can be checked against this one hash; no need to re-wc or re-parse unless `catalog.catalog_release` changes (README L591 says a repin must record in versions.md - watch that).
2. **R199's measured-diameter reconciliation is now triple-corroborated**: the release manifest itself declares `"measured_diameters": 149718`, agreeing with both economicspace README L1209 and my flag-based count on the (now hash-authenticated) parquet. The do-not-re-flag ruling stands on three independent records.
3. Manifest `sources` provenance counts - JPL SBDB 1,568,882 / SsODNet 1,563,656 / NEOWISE 143,015 / MP3C 1,335,051 - are in-catalog sourcing tallies, not source-table sizes; no tension with R41-era registrations (ssoBFT parquet 1,563,708 rows and NEOWISE V2.0 bundle 183,419 are different tables/views).

No RC opened: every declared value matched reality exactly - the pinned artifact chain is clean from release metadata through to the working files behind every committed pipeline number. rc-176 (the "~1.2 GB" survivors) remains open and untouched; its subject file is now identified to exact hash, strengthening rather than altering that candidate.
## Round 201 - release-history manifest sweep across all eight AsteroidCatalog builds; stamped doc claims verified against their own builds (2026-10-19)

Every published AsteroidCatalog release carries its own manifest.json declaring rows / measured_diameters / sources counts / contract version. Pulled all seven older ones (R200 covered 29c) and cross-checked every stamped figure in README/CHANGELOG against the build it names:

| release | rows | measured_diameters | contract | pkg | SsODNet | cols |
|---|---|---|---|---|---|---|
| data-2026-09-23 | 1,566,618 | **149,740** | 1.3.0 | 0.3.0 | 1,563,644 | 95 |
| data-2026-09-25 | 1,567,469 | 149,718 | 1.4.0 | 0.4.0 | 1,563,656 | 99 |
| data-2026-09-26 | 1,567,657 | 149,718 | 1.4.1 | 0.6.0 | 1,563,656 | 99 |
| data-2026-09-26b | 1,567,859 | 149,718 | 1.5.0 | 0.7.0 | 1,563,656 | 99 |
| data-2026-09-27 | 1,568,641 | 149,718 | 1.6.0 | 0.8.0 | 1,563,656 | 100 |
| data-2026-09-29 | 1,568,748 | 149,718 | 1.7.0 | 0.9.0 | 1,563,656 | 101 |
| data-2026-09-29b | 1,568,882 | 149,718 | 1.8.0 | 0.10.0 | 1,563,656 | 102 |
| data-2026-09-29c (R200) | 1,568,882 | 149,718 | 1.8.1 | 0.10.1 | 1,563,656 | 102 |

Doc claims verified against their own builds: README L143-144 "(149,718 of 1,568,641 in data-2026-09-27)" matches the -27 manifest exactly; CHANGELOG "Built from d30a34f: 1,568,882 bodies" for -29b matches its rows; "SsODNet ~1.56 M (1,563,656 bodies of data-2026-09-26)" matches the -26 manifest sources field. **Zero mismatches across every stamped count.**

Parquet-level verification: CHANGELOG claims-correction table says "in data-2026-09-26, 77 masses are known to 5% and the densest are Kalliope 4.18 and Psyche 4.14". Computed on that release's own parquet (downloaded this round): exactly **77** bodies have estimated_mass_sigma_kg/estimated_mass_kg in (0, 0.05], top densities Kalliope 4.175310 and Psyche 4.142608 - the stated 4.18/4.14 are those values rounded up to two decimals; third is 110 Lydia at 3.538, consistent with the same table row's correction about Lydia. Claim verified true for its named build.

Methodology fact recorded: "masses known to X%" in AC docs = mass-only relative-sigma selection (sigma/mass in (0, 0.05]), NOT tools/density_evidence.py measured_bodies() - applying the flagged density-evidence filter at 5% gives 45 bodies on the same build. Future rounds: do not apply measured_bodies() to this statistic.

Refinement of R199's flat-numerator story: measured_diameters was **149,740 in data-2026-09-23** and 149,718 from -25 onward (one correction event between builds; docs never cite a count for -23 so no conflict). The +241-bodies claim (09-27 to 29c) stands unchanged.

No RC opened: the release-history record is internally consistent with its own metadata at every point checked, from manifest counts down to per-body densities on an archived build.
## Round 202 - cross-build CHANGELOG claims verified against published parquets; asset integrity extended to two more releases (2026-10-19)

Continuing the release-history seam from R201: the data-2026-09-25 -> data-2026-09-26 diff paragraph in AsteroidCatalog's CHANGELOG makes several claims that say "(checked against the published parquet)" - this round re-ran those checks independently on fresh downloads of both builds.

Claims verified exactly:
- "188 bodies JPL added, none gone": set difference = +188 / 0 removed; all 188 new rows cite JPL in their sources field.
- "19 H-derived diameters and masses moved because JPL revised those bodies' H and orbit": exactly **19** common bodies have a material diameter change (relative > 1e-6) and the same 19 for mass; `absolute_magnitude_h` differs on exactly those 19 rows - the movers are provisional-designation bodies like 2026 SZ7 (largest shift +2.68%), consistent with fresh JPL H revisions.
- "no body's class, albedo, density, source list or diameter source changed": spectral_type, spectral_type_tholen, measured albedo, sources and diameter_source all show zero changes; `albedo_assumed_for_diameter` zero changes; the 12 rows whose density_gcm3 differs in exact string form are all within rebuild float noise (old == new at display precision).
- "no row of data-2026-09-25 is one" (the blank-class asymmetry between derive.py's three spellings and enrich_composition's eight, `taxonomy._BLANK_CLASSES` = 8 notations): scanning -25 for rows whose Bus column holds one of the five asymmetric notations {"-", "NaN", "none", "NA", "<NA>"} while a Tholen class is present returns **0** rows.

METHODOLOGY FACT recorded (prevents false RCs against this changelog line in future rounds): exact string comparison of derived float columns across builds flags 60,750 diameter and 118,319 mass cells as changed - all but the material 19 are <=1e-9 relative rebuild noise from unifying `physics.H_DIAMETER_CONSTANT` into one definition (the same changelog section describes that refactor). Cross-build claims of "N values moved" must be tested with a relative tolerance; material counts here are exactly 19/19 at any threshold above ~1e-6.

Asset integrity extended: fresh downloads of the data-2026-09-25 and data-2026-09-26 parquets hash to their manifests' declared sha256 (older builds key the asset map as `files`, newer releases as `assets` - same content). Together with R200 (29c) and R201 (-26 manifest sweep), three releases now have independently proven artifact integrity.

No RC opened: every re-runnable claim in this changelog section reproduces exactly against the published artifacts.

## R216 - winner-table currency seam at economicspace README (rc-183) (2026-10-20)

The section 'Every destination at this release' asserts it is the current answer to where it is best to deliver, yet three of its seven rows carry v1.40-era values that the same file's own release table supersedes with explicit figures: cislunar 4.8379x on krypton Hall against their later note moving the winner to iodine at 4.61562x (v1.53.0); earth_surface 6,154.06x against 5,374.37x recorded at v1.46.0; lunar_surface 2005 QP87 at 2.9353x against 2014 YN becoming the winner (v1.51.0) and then reading 2.61433x (v1.52.0). Their v1.50.0 note amends every in-space row again by 0.55% to 5.04%, so no row can be current without a fresh full cell - opened as rc-183, values untouched pending adjudication or re-run; MODEL.md's 'comes within 9% of breakeven' inherits the same staleness (post-v1.50 mars_surface is 1.08536x).

Documented without registering: five of six headline winners checked from the hash-verified pinned parquet rest on estimated physics - 2018 DT carries derived_diameter_is_estimate=True, albedo_assumed_for_diameter=0.133 (taxonomy albedo for class M), density_measured=False and zero rotation-period sources; likewise 2015 DS, 350751, 2005 QP87 and the v1.51 lunar winner 2014 YN are all derived_h_taxonomy_albedo with unmeasured density, while the geo winner 2016 GS2 alone is diameter_source=measured (40 m) though its density is likewise unmeasured; EC documents the provenance vocabulary at README L1206 ('only measured is a size somebody observed') but never states that its own winners are estimate-sized. Because minable mass scales as diameter cubed, the assumed-albedo uncertainty propagates cubically into every headline multiple (at half the assumed albedo the body doubles in diameter and an eightfold revenue swing follows). This strengthens rc-183's currency claim; a separate disclosure RC was not opened this round - if the winner table is refreshed per rc-183, adding each row's diameter_source alongside the figure closes both concerns.

## Round 237 - Vesta and Bennu take their mission volumes upstream (2026-10-21)

AsteroidCatalog 1.10.0 (`6915077`, published as data-2026-10-21b) extends merge.SHAPE_MODEL_VOLUMES, rc-174's per-body table, to the two bodies R235 recorded as just outside JPL's uncertainty. Both sources registered this round and read in full:

- park_2025_vesta_small_core_dawn, Methods p830: "the volume of (7.49 ± 0.01) × 10^7 km3 from the SPC shape", mass 2.59028e20 kg, bulk density 3.458 ± 0.005 g/cm3. Release: 522.991 km, 3.4579 g/cm3 (was 525.4 km, 3.4106, SsODNet's Russell et al. 2012 mean diameter).
- daly_2020_bennu_hemispherical_shape_ola, Table 1: volume 0.061354 ± 0.00006 km3, bulk density 1194 ± 3 kg/m3. Release: 0.489345 km, 1.1948 g/cm3 (was 0.488 km, 1.2047). JPL SBDB's 0.48444 km is twice Daly's average radius, not the equal-volume sphere, so upstream's test checks density, not that diameter.

Verdict: both agree with their papers to the stated digits; no candidate. tools/density_evidence.py on the release moves only the V and B rows (weighted means 3.41 to 3.46 and 1.21 to 1.20) and fails no row. Extracted: extracted_data/r237_mission_shape_volumes.csv.
