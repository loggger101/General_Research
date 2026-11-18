# Domain 12 — Destination environments & physical constants

Backings: spacecost `reference/environments.csv` (solar flux, array mass factor, gravity, escape velocity, light time, eclipse and dark periods for each destination) and the constants in `spacecost/units.py`.

Created in Round 74 (2026-09-27). Blocks are appended one per round, newest last.

## R74 - Upstream citations registered (2026-09-27; +16 sources)

All `registered_not_pulled`, each backing an environments.csv cell:

| id | cell |
|---|---|
| `kopp_lean_2011_total_solar_irradiance` (T1) | solar flux and array mass factor, every row (1 AU TSI) |
| `tiesinga_2021_codata_2018_constants` (T1) | surface gravity, escape velocity (G) |
| `iau_2012_resolution_b2_astronomical_unit`, `bipm_si_brochure_9th_edition` (T3) | one-way light time (AU, c) |
| `nasa_nssdca_moon_fact_sheet`, `nasa_nssdca_mars_fact_sheet` (T3) | lunar and Mars mass, radius, day; Phobos row |
| `willner_2014_phobos_shape_topography` (T1) | Phobos mean radius |
| `watanabe_2019_hayabusa2_ryugu_spinning_top`, `yeomans_2000_near_eros_radio_science`, `daly_2023_dart_kinetic_impact`, `russell_2016_dawn_arrives_at_ceres` (T1) | Ryugu, Eros, Didymos, Ceres mass, radius, rotation |
| `nasa_iss_facts_and_figures` (T3) | LEO (400 km) period and eclipse fraction |
| `itu_r_s1003_geostationary_orbit` (T3) | GEO eclipse seasons |
| `mazarico_2011_lunar_polar_illumination_lola` (T1) | polar-ridge illumination fraction |
| `appelbaum_flood_1989_tm102299_solar_radiation_mars` (T2) | Mars surface insolation and its dust caveat |
| `warner_harris_pravec_2009_asteroid_lightcurve_database` (T1) | generic asteroid rotation period |

## R102 - First hosted sources (2026-10-02)

Hosted: `iau_2012_resolution_b2_astronomical_unit` (AU = 149,597,870,700 m exactly); `bipm_si_brochure_9th_edition` (CC BY 4.0; c = 299,792,458 m/s); the Moon and Mars NSSDCA sheets and `nasa_iss_facts_and_figures` (HTML snapshots; ISS: 5 agencies / 15 countries, crew of seven, ~90-minute orbit, 356 ft); `appelbaum_flood_1989_tm102299_solar_radiation_mars` (NASA TM-102299): clear-atmosphere mean beam irradiance 590 W/m² (Eq. 4, p10) vs upstream's 586.2 W/m² on both Mars rows (-0.7%); `daly_2023_dart_kinetic_impact` (Nature 616:443, CC BY): impact site 8.84 ± 0.45° S, 264.30 ± 0.47° E, albedo 0.15 ± 0.02 at 0.55 μm.

New: **`thomas_2023_dimorphos_orbital_period_change`** (Nature 616:448, CC BY, hosted), what the Didymos row actually points at: period change −33.0 ± 1.0 (3σ) min by two methods (11.92148 h pre-impact; 11.372/11.371 h after). `extracted_data/r102_key_constants.csv`. The other nine rows stayed unreached (routes in each row).

## R115 - Three rows against hosted sources; three candidates (2026-10-04)

Against spacecost@85da36c:

- **65803 Didymos (rc-067):** the row cites Daly 2023 for 5.28e11 kg and 390 m; Table 1 (p3) gives system mass (5.6 +/- 0.5)e11 kg (Dimorphos 4.3e9) and volume-equivalent diameter 761 +/- 26 m. Both cells are within 1-sigma, but derived gravity is 9.6% and escape velocity 3.7% low at Daly's numbers.
- **16 Psyche (rc-068):** radius 111 km is Siltala and Granvik's, but mass 2.29e19 kg is Kretlow's SiMDA figure (their GM 1.482 km3/s2 gives 2.22e19 kg).
- **Low Earth orbit (rc-069):** the ISS page gives "about every 90 minutes" and 16 sunrises a day, not the 92.7-minute period or shadow time; the cells fit a 400 km orbit, only the attribution is off.
- Agreeing: Phobos (sheet 10.6e15 kg, axes 13.0 x 11.4 x 9.1 km = 11.0 km mean, 0.31891 d vs row 1.0659e16 kg, 11.267 km, 7.653 h; within 2%); Mars gravity and mass; Appelbaum and Flood Table IV clear-day daily means 250-308 W/m2 (42-52% of 590) vs the row's "40-60%"; Moon mass 7.346e22 vs 7.342e22 (0.05%).

`extracted_data/r115_environment_rows_vs_sources.csv`.

## R116 - GEO eclipse citation re-sourced (rc-079; 2026-10-04)

ITU-R S.1003-2 read in full (route: `recommendation.asp?lang=en&parent=R-REC-S.1003-<edition>`; "All rights reserved", not hostable). It concerns GSO disposal orbits ("ΔH > 235 + 1 000 Cr A/M (4) for eccentricities < 0.003") and contains no occurrence of "eclipse": the citation is a misattribution.

**`ecss_e_hb_31_01_part15a_existing_satellites`** [T3; read, no licence statement, not hosted], ECSS thermal design handbook Part 15A: the OTS case study (a geostationary satellite over Gabon, apogee 35779 km, perigee 35072 km) lists "Maximum eclipse of 72 minutes" (p35), matching upstream's "up to 72 min a day", and "During the equinox there are operational RF mode changes, extra switching of heaters in pre‐eclipse periods..." (p44). The ~45-day season and 1.2% annual average are standard geometry. rc-079 proposes citing Part 15A for the maximum. `extracted_data/r116_geo_eclipse_key_numbers.csv`.

## R121 - CODATA and Phobos shape read, not hostable (2026-10-05)

- `tiesinga_2021_codata_2018_constants` (PMC9890581; text mining and fair use only): Table I "Newtonian constant of gravitation G 6.674 30(15)", relative uncertainty 2.2 x 10^-5, matching units.py `NEWTON_G_M3_PER_KG_S2 = 6.674_30e-11` exactly.
- `willner_2014_phobos_shape_topography` (DLR elib copy; "© 2013 Elsevier Ltd. All rights reserved"): the degree-45 Phobos shape model behind the Phobos radius row.

## R133 - Lunar pole illumination: upstream's ~86% traced (2026-10-07)

**glaser_oberst_mazarico_et_al_2017_lunar_pole_illumination** (PSS 162:170-178; NTRS accepted manuscript, hosted). Its Table 1 quotes Mazarico 2011: Shackleton S (-89.78, 204.27) maximum average illumination **86.7%** over a 20-year cycle, matching the polar-ridge row's "~86%" (Glaser's own run at -89.7849 / 203.97 gives 81.0%). Connecting Ridge C1 reaches 89.0% with a maximum shadow of 141.12 h (~5.9 days), consistent with "worst continuous darkness of a few days". `mazarico_2011_lunar_polar_illumination_lola` itself stays unreached (NTRS has a file-less record). `extracted_data/r133_lunar_polar_illumination_key_numbers.csv`. No re-pin.

## R136 - TSI companion paper (2026-10-08)

**rind_lean_jonas_2014_tsi_impact_on_climate_model_simulations** (J. Climate 27; AMS copyright, read only), companion to the unreached kopp_lean_2011_total_solar_irradiance: GISS GAM3 with 1990s-radiometer vs SORCE irradiance differs by "a global temperature change of 0.48C, comparable to the cooling estimated for the Maunder Minimum" before energy-balance adjustment. `extracted_data/r136_tsi_impact_key_numbers.csv`.

## R155 - Ceres from Russell et al. 2016 (2026-10-12)

`russell_2016_dawn_arrives_at_ceres` (author copy, AAAS copyright; read only), p1008: mass (9.384 +/- 0.001) x 10^20 kg; axes 483.1 x 481.0 x 445.9 km, geometric mean 469.7 km (469.68 recomputed); density 2162 +/- 3 kg/m3; rotation 9.074170 h. spacecost@0b716ad's Ceres row (9.3835e20 kg, 469.73 km, 9.074 h) agrees to -0.005% and +0.006%. `extracted_data/r155_queue_open_copies_key_numbers.csv`.

## R165 - Candidates (2026-10-14)

rc-131 (Moon mass 7.346e22 per the cited sheet), rc-132 (Mars mass 6.4169e23), rc-133 (Phobos mass and radius not from the cited sheet), rc-165 (Mars atmosphere 95.1% CO2, 2.59% N2, 636 Pa). Texts in `revision_candidates.csv` (open) and `revision_candidates_closed.csv`.

Extracted data: `extracted_data/r165_environment_constants_vs_factsheets.csv`.

## R212 - economicspace PR#154 worksheet backing: two institutional constant sources registered (2026-10-20)

economicspace origin/main moved 36bc858 -> 675f0cf (PR#154, Verification worksheet citations and backing). Its CITATIONS.md now cites documents for three worked_calculation constants that R207 had recorded in d19 as self-derived by design. Neither document was registered; both are added this round:

- iers_petit_luzum_2010_conventions_tn36 [T2, verified_live_not_pulled]: official IERS Conventions Centre PDF read live (179 pp). Table 1.1 prints GM_EARTH = 3.986004418 x 10^14 m^3 s^-2 and worked_calculation MU_EARTH = 398,600.4418 km^3 s^-2 agrees exactly at that precision. In-file publisher copyright on the title page makes it extraction-only per R94.
- nasa_nssdca_earth_fact_sheet [T3, full_text_hosted]: Mean orbital velocity 29.78 km/s (V_EARTH = 29.784 agrees to published figures) and J2000 Semimajor axis 1.00000011 AU (window_phasing_au = 1 au likewise).

R_MOON correction recorded deliberately: the Moon fact sheet publishes Semimajor axis 0.3844 x 10^6 km, so R_MOON = 384,400 km agrees exactly at published precision - there is NO mismatch with this source and no future round should flag one (a 384,500 average-distance figure does not appear on the current page). DV_NRHO restates spacecost delta_v_segments row 'TLI -> NRHO insertion' per PR#154 own note; that row already carries its source - nothing to register.

rc-175 / rc-176 / rc-177 targets (MODEL.md, README.md, master.py and modules/mineral_value.py constants) are untouched by PR#154: the diffstat covers CITATIONS.md, campaign/verification_sheet.py, campaign/worked_calculation.py and versions.md only.

Extracted data: `extracted_data/r212_worksheet_constants_key_numbers.csv`.

## R213 - environments gravity and escape-speed self-consistency clean (2026-10-20)

Recomputed surface_gravity_m_per_s2 as G*M/R^2 and escape_velocity_m_per_s as sqrt(2*G*M/R) from the mass_kg and mean_radius_m each row itself publishes, for all ten body rows of spacecost@29a7ced reference/environments.csv (Lunar equator + polar ridge, Bennu, Ryugu, Eros, Didymos, Mars mid-latitude, Phobos, Ceres, Psyche): every stored value reproduces within 0.02 percent either way - the rounding level of G itself. No candidate; future rounds need not re-run this seam unless those columns move.

## R214 - environments solar-irradiance seam exact (2026-10-20)

Recomputed the product of solar_flux_w_per_m2 and au_mean squared for every row carrying both fields in spacecost@29a7ced reference/environments.csv: all 23 rows reproduce exactly 1361.0 W/m^2 at full stored precision (the CSV keeps au_mean beyond its printed digits). The flux column is derived from one inverse-square law against the 1361 solar constant rather than independent per-body measurements - internally exact, no candidate; skip unless those columns move.

## R238 - Phobos: Willner 2014's own figures, and rc-133 applied (2026-10-21)

Re-read `willner_2014_phobos_shape_topography` from the same DLR elib file R121 read (sha256 585ee394..., not hosted). It gives a mean radius r0 = 10.993 km (PDF p5), a volume of 5741.5 km3 (p4; Table 3: 5742 +/- 35), SH-model axes 13.03 x 11.40 x 9.14 km, and quotes Andert et al. 2011's GM of 0.7127 x 10^-3 km3/s2, which is 1.0678e16 kg. So neither the fact sheet nor Willner holds upstream's 1.0659e16 kg or 11.267 km; the row's pipeline_mapping now says so. spacecost 0.12.6 (PR #29, tag v0.12.6, main `b5eb32a`) applied rc-133: the note labels both values an estimate and gives what each source prints. `extracted_data/r238_willner_2014_phobos_key_numbers.csv`.

## R291 - environments.csv physics recompute, skip-note (2026-10-28)

All 23 rows recomputed from committed bytes at spacecost@860bef9 (raw git-show capture, uniform parsed-width proof). Surface gravity equals G*M/R^2 and escape velocity sqrt(2GM/R) on every row with mass plus radius; dark period equals eclipse fraction times cycle period wherever all three are present; blackbody temperature is the rapid-rotator uniform-temperature value (S/4sigma)^0.25 at zero bond albedo in every single row - one convention, no exceptions; solar_array_mass_factor equals au_mean^2 exactly (= 1361/stored flux) in all rows.

The one_way_light_time_min column is formulaic and display-only. Heliocentric rows equal (au_max + 1.0167) AU times 8.316746 min per AU, identical to about 1e-6 across the family - body aphelion plus Earth aphelion, i.e. a strict worst-case conjunction; the CHANGELOG for the table release describes exactly this as "conjunction range and one-way light time", so stored values match their own documented convention. Cislunar rows instead store exact nominal distances from Earth: LEO 400 km reproduces to display precision, GEO within 2.2 km of the 35,786 km ring (0.006 percent), Sun-Earth L2 at 1.5 million km, lunar distance 384,467 km (+0.017 percent against semi-major axis 384,400). Prose notes agree with the stored figures (main belt mean "a 35-minute one-way light time", Jupiter Trojans "a 54-minute one-way light time").

Consumption check: git grep for one_way_light_time and solar_array_mass_factor at HEAD of spacecost and economicspace returns zero hits outside the CSV itself - both columns are data-only pass-throughs. Do not re-sweep the derived physics of this table unless its input columns move.


## R421 — Phobos GM-derived mass comparison (2026-11-09)

Guo et al., “Phobos’ degree-1 ellipsoidal harmonic gravity field recovery from two Mars Express flybys,” MNRAS 548(2), stag578 (2026), reprocesses Doppler tracking from the 2010 and 2013 Mars Express flybys. The abstract reports “An improved estimate of the Phobos GM” and Table 3 gives (7.09962 ± 0.001970812) × 10^5 m³/s² (3σ). Using G=6.67430×10⁻¹¹ m³ kg⁻¹ s⁻² gives 1.063725×10¹⁶ kg, about 0.2045% below the explicitly estimated 1.0659×10¹⁶ kg in the upstream Phobos row; the GM-based 3σ uncertainty is about 0.0278%. This article updates mass evidence only; it does not update the row’s mean radius. rc-331 records a review of the mass and dependent gravity/escape-velocity fields. `extracted_data/r421_phobos_gm_mass_update.csv`.

## R429 — JPL Phobos parameter-table version cross-check (2026-11-09)

NASA/JPL Solar System Dynamics' Planetary Satellite Physical Parameters table lists Phobos GM as 0.0007087 ± 0.0000006 km³/s² and mean radius as 11.08 ± 0.04 km; the GM row explicitly references MAR097 (table row). The same page separately identifies MAR099 as the current planetary-satellite ephemeris and cites Brozović, Jacobson & Park (2025) for the revised Martian-satellite ephemerides (page lines 87–92). Converting the table GM at G=6.67430×10⁻¹¹ gives 1.061834×10¹⁶ kg, 0.3814% below the upstream estimated mass and 0.1778% below Guo et al. (2026)'s GM-derived central mass. The table therefore adds an official but older-reference comparator; it does not supersede either the specific Guo flyby reanalysis or the upstream estimate by itself. rc-331 remains open for a source/version and dependent-field review. Extracted: `extracted_data/r429_jpl_phobos_parameter_comparison.csv`.


## R422 — Psyche high-precision mass estimate (2026-11-09)

Farnocchia et al., “Mass, density, and radius of asteroid (16) Psyche from high-precision astrometry,” *The Astronomical Journal* 168(1):21 (2024), reports baseline GM = 1.601 ± 0.017 km³/s² and corresponding mass (2.399 ± 0.025) × 10¹⁹ kg (1σ; Table 2, p. 4). The official AAS DPS abstract says the result is “robust against variations in the orbit determination setup and specific data set used” and gives an equivalent radius of 111 (+2, −0.5) km. Current `spacecost/reference/environments.csv` stores 2.29 × 10¹⁹ kg, 4.76% below the newer central estimate; its 111 km radius is consistent. If the mass is adopted, recompute formula-derived surface gravity and escape velocity (0.1299541 m/s² and 169.8523 m/s at the stored radius). rc-332 tracks review of the mass and dependent fields. `extracted_data/r422_psyche_mass_update.csv`.


## R423 — Bennu OLA mean-radius comparison (2026-11-09)

`daly_2020_bennu_hemispherical_shape_ola`, Table 1 (p. 2), gives an average radius of 244 ± 0.09 m for the previous GDTM and 242.22 ± 0.15 m for the OLA GDTM. The article calls the OLA model higher fidelity, says its accuracy is better than ±20 cm, and describes it as a geometric baseline for size and geopotential quantities (p. 2). The upstream `spacecost/reference/environments.csv` row stores 244.5 m and attributes it to Lauretta et al. 2019; the OLA Table 1 value is 2.28 m (0.93%) lower. The same article says OLA is “41 ± 20 cm smaller” than the SPC model, while its Table 1 values differ by 1.78 m. Verdict: model/version and radius definition require reconciliation before any replacement; if the OLA value is adopted, recompute gravity and escape velocity. rc-333 records review. `extracted_data/r423_bennu_ola_radius_comparison.csv`.


## R425 — Lunar polar-ridge illumination review (2026-11-09)

Barker et al. (2021), *Planetary and Space Science* 203:105119, identify Site 1 as the connecting ridge between Shackleton and de Gerlache (p. 3). Their 5 m/pixel LOLA analysis reports for seven Site 1 regions of interest (Table 2, p. 8) 1st-percentile average illumination of 67.36–71.15% at 1 m height and 82.79–89.26% at 5 m; 99th-percentile longest continuous shadow is 12.74–22.23 days and 4.00–8.41 days, respectively. The paper calls the height effect “dramatic” (p. 13) and models 100 terrain realizations to represent topographic uncertainty. The upstream polar-ridge row stores `eclipse_fraction=0.14` and `dark_period_hr=99.218` (~4.13 days), traced in R133 to Mazarico et al.’s Shackleton S point at 86.7% illumination. Barker’s regional ROIs, 2024–2026 interval, height offsets, and uncertainty percentiles do not directly reproduce that point over an 18.6-year cycle; resolve site and asset height before changing either cell. Verdict: bounded review candidate rc-335; no replacement value inferred. `extracted_data/r425_lunar_polar_illumination_review.csv`.


## R516 — Asteroid rotation-period fallback comparison (2026-11-10)

Marciniak et al. (2015), “Against the biases in spins and shapes of asteroids,” Table 1 (p. 257), reports a median rotation period of 10.986 h for 1,230 asteroids selected from Warner et al.’s LCDB with period quality code ≥2−. The abstract (p. 256) and discussion (p. 257) describe selection effects, including underrepresentation of long-period asteroids; the analyzed sample is bright (H≤11) main-belt asteroids. economicspace `modules/calc.py` sets `CalcConfig.default_rotation_period_h = 10.222` h for objects without a measured period, 0.764 h (7.47%) below this filtered-sample median. The populations are not established as equivalent, so this is a scope and citation review, not a replacement value. rc-382 records the comparison. `extracted_data/r516_asteroid_rotation_period_median_comparator.csv`.


## R547 — Surface solar dark-fraction comparator (2026-11-10)

Stubbs and Wang’s Vesta illumination model reports that the Sun is typically visible about half the time in the tropics, as expected for diurnal variation (§5.1, printed p. 275). Their annual mean solar-visibility values range from 0.363 to 0.566 across Vesta, with departures tied to latitude, axial tilt, shape, and topography. This supports 0.50 as a scoped equatorial/tropical comparator; it does not establish the same fraction or the [0.35, 0.55] range as a generic asteroid-site value. At spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9, `reference/operational_costs.csv` stores `Eclipse / night-side dark fraction` = 0.50 [0.35, 0.55], and `reference/storage_systems.csv` duplicates it as `Eclipse / night-side power fraction`; both notes describe the geometry without naming a source for the baseline or range. rc-413 records the attribution and scope review. Extracted: `extracted_data/r547_vesta_surface_solar_visibility.csv`.
## R562 — rotation-period citation and population scope applied (2026-11-10)

At economicspace@e2ad48767b0e81489031b724417b1a03e6dfc1fb, the fallback rotation-period comment cites Marciniak et al.’s 10.986 h median and flags the population mismatch against the model’s generic value (rc-382). Citation and scope request applied; no numeric replacement inferred.
## R564 — Phobos and Psyche masses refreshed; illumination scope qualified (2026-11-10)

At spacecost@d3e594fe0968eeaee4f2c02dd2c76334eab8bb2c, Guo et al.’s Mars Express Phobos GM gives a mass of 1.063725×10¹⁶ kg and the dependent gravity/escape values are recomputed (rc-331); Farnocchia et al.’s Psyche GM gives 2.399×10¹⁹ kg and dependent values are recomputed at the existing radius (rc-332). `stubbs_wang_2012_vesta_illumination_conditions` is cited as a Vesta comparator and 0.50 is described as a scenario baseline rather than a generic asteroid-site fraction (rc-413).

## R565 — Phobos and Psyche mass candidates rechecked (2026-11-10)

Spacecost 0.17.0 / data contract 1.26.0, at main commit `aaed2720ee44610c5cf90fc204db160deb5669bb`, carries the Guo et al. (2026) Phobos GM mass of 1.063725×10¹⁶ kg and the Farnocchia et al. (2024) Psyche GM mass of 2.399×10¹⁹ kg, with dependent gravity and escape values updated. The current rows agree with rc-331 and rc-332; candidate records rechecked against the release commit and remain applied.


## R687 - Ryugu physical constants and returned-sample note citation (2026-11-12)

Watanabe et al. (2019), author-version PDF p. 3, reports shape-model volume 0.377 km³ and estimated mass 4.50 × 10^11 kg (1.3% uncertainty). The volume-equivalent spherical radius calculated from that volume is 448.3 m, consistent with the upstream 448 m after rounding; no mass or radius revision is indicated. The copy’s first page says “Copyright Owner: Authors” and that it is posted “for personal use, not for redistribution,” so no copy is hosted.

In the current spacecost Ryugu row, the Watanabe citation accompanies physical parameters, followed by an uncited statement that the two returned samples agree on hydrated carbonaceous composition and that this is empirical evidence for asteroid water as a resource. The 2019 paper predates sample return; the sample-composition assertion therefore needs a post-return source and a defined comparison. Existing registry sources ryugu_ivuna_2023 and yokoyama_2023_ryugu_c_type_sample_water_content report returned-sample chemistry, including predominantly structural-OH water; those measurements alone do not establish free or extractable water or resource yield. Opened rc-545 for citation and scope review; no replacement value inferred. Extracted: `extracted_data/r687_watanabe_2019_ryugu_physical_parameters.csv`.


Yeomans et al. (2000), Table 1 p. 4, reports Eros mass (6.687 ± 0.003) × 10^18 g and volume 2503 ± 25 km³. The volume-equivalent radius calculated from the volume is 8.42 km, consistent with upstream mean_radius_m=8420 m after rounding. The paper reports local escape speeds 3.1–17.2 m/s (p. 2), bracketing the row’s 10.296 m/s spherical estimate. The retrieved author-version PDF footer limits use to personal, non-commercial use; no copy is hosted. This check found no candidate. Extracted: `extracted_data/r687_yeomans_2000_eros_physical_parameters.csv`.


## R709 — Rotation-period fallback statistic and catalog vintage (2026-11-12)

economicspace main `46e0315d12f3fc876b022fdb5270016c7c539080`, `modules/calc.py` lines 676–684, sets `default_rotation_period_h=10.222` and describes it as the median of 29,288 catalog bodies with a measured period on 2026-08-08; the code does not name that catalog release or give the selection calculation. The installed AsteroidCatalog Stage 1 release is `data-2026-10-21b` (1,575,889 rows). Reading its `rotation_period_h` field with no class or size filter gives 46,159 non-null values and a median of 8.068 h. Current `verification_sheet.py --check` marks input I65 as NEED BACKING among 85 inputs for the archived 2018 DT sheet; the worksheet uses frozen Stage 2 `mineral_value 1.12.0` and Stage 3 `spacecost 0.5.0` exports.

- **rc-579**: pin the 10.222 h statistic to its data release and population/filter, and assess whether the fallback should remain a historical prior against the later catalog distribution. No replacement inferred.

Extracted: `extracted_data/r709_rotation_period_fallback_population.csv`.


## R719 — Phobos mean-radius convention (2026-11-13)

quillen_lane_nakajima_wright_2020_excitation_phobos_deimos_tumbling (Quillen et al. 2020, Icarus 340:113641), §1.1, Table 1, reports “Mean Radius, R, 11.2667 km” and a Phobos mass of 1.0659×10^16 kg; the table does not state the radius derivation. The radius rounds to Spacecost’s current 11,267 m.

ernst_et_al_2023_phobos_deimos_spc_shape_models (Ernst et al. 2023, Earth, Planets and Space 75:103), Abstract and Phobos model section/Table 5, reports best-fit ellipsoid radii of 12.95 ± 0.04 × 11.30 ± 0.04 × 9.16 ± 0.03 km and an “average radius of 11.08 ± 0.04 km” computed from an equivalent-volume sphere. The 11.08 km equivalent-volume radius is 187 m (1.660%) below Spacecost’s current radius. Holding the current mass fixed, replacing the radius with 11,080 m changes the formula-derived surface gravity from 0.005592661 to 0.005783032 m/s² and escape speed from 11.226087 to 11.320423 m/s. These sources report different radius conventions; the comparison does not by itself establish an error. rc-587: review the intended radius convention and dependent fields. Extracted: extracted_data/r719_phobos_mean_radius_convention.csv.

## R720 — Rotation-period fallback recheck (2026-11-13)

At economicspace main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, `modules/calc.py` lines 676–684 still sets `default_rotation_period_h=10.222` and describes a median of 29,288 measured-period catalog bodies dated 2026-08-08; the file SHA-256 is unchanged from the registered code snapshot. `modules/catalog.py` line 121 pins Stage 1 to `data-2026-11-13`. The registered source `asteroidcatalog_release_data_2026_11_13` points to the installed manifest, which reports pipeline 1.11.0, package 0.13.2, AsteroidCatalog source commit `a2c527c09eb39618d7fd26b2b180f730ea906b8b`, and 1,580,325 rows. The unfiltered `rotation_period_h` field has 46,159 non-null values and median 8.068 h, unchanged from `data-2026-10-21b`; the gap from the fallback remains 2.154 h (21.1%). The archived 2018 DT verification sheet still marks I65 NEED BACKING and reports 85 NEED BACKING inputs; its Stage 2 and 3 tables are frozen historical exports. rc-579 remains open; no replacement inferred. Extracted: `extracted_data/r720_rotation_period_release_recheck.csv`.


## R729 — Didymos mass and radius still lack a row-specific source (2026-11-13)

`spacecost_didymos_mass_radius_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` row 65803 records mass 5.28e11 kg and mean radius 390.0 m. Its note says neither figure is in Daly et al. (2023) and the source is not recorded; `CITATIONS.md` likewise calls the mass and radius unsourced.

`daly_2023_dart_kinetic_impact`: Table 1, PDF p. 3, gives “Mass of the Didymos system” as (5.6 ± 0.5) × 10^11 kg and “Diameter of volume-equivalent sphere for Didymos” as 761 ± 26 m. Those system and shape comparators place the stored values within the reported 1σ bands but do not document their exact source or primary/system basis. The current mass and radius yield the row’s surface gravity 2.3169e-4 m/s² and escape velocity 0.4251 m/s.

Verdict: identify a primary-body-specific source and radius convention for the stored mass and radius, or label them as estimates with an uncertainty and method; keep Daly’s system-level quantities separate. Recompute dependent gravity and escape velocity if either input changes. No numeric replacement inferred. Distinct from rc-067, which corrected the Daly attribution but left the row values’ source unresolved. **rc-596**. Extracted: `extracted_data/r729_didymos_mass_radius_citation_gap.csv`.


## R736 — Mars semimajor-axis provenance (2026-11-14)

`economicspace_mars_semimajor_axis_code_current_2026`: at pinned economicspace main commit `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7`, `modules/calc.py` sets `A_MARS_AU = 1.523679` and reuses it as `window_phasing_au` for the Mars-orbit and Mars-surface architectures. The `a_dest` note in `campaign/verification_sheet.py` says the Mars figure is not the fact sheet value to five places and is left uncited.

`jpl_tr_32_77_mean_planet_elements_1966`: Table 2-1, printed p. 12, is headed “Mean planet elements”; its Mars row gives semimajor axis `1.523679 au`. The table footnote says T is measured in Julian centuries from 1950.0; it does not identify this semimajor-axis value as a J2000 figure.

`nasa_nssdca_mars_fact_sheet`: the current page section “Mars Mean Orbital Elements (J2000)” gives `1.52366231 AU`, distinct from the stored code value.

Verdict: identify the intended planetary-element basis and cite it for the Mars phasing input; the exact historical match supplies provenance but does not establish the code’s intended convention. No numeric replacement inferred. **rc-603**. Extracted: `extracted_data/r736_mars_semimajor_axis_provenance.csv`.

## R784 — Mars gravitational-parameter ephemeris attribution (2026-11-15)

**economicspace_mars_gravitational_parameter_code_current_2026**: At economicspace main 1cf2617f1a34e013e7f49bd9d908099e3e47354, modules/calc.py sets MU_MARS_KM3_S2=42,828.37 km³/s² and campaign/worked_calculation.py repeats MU_MARS=42,828.37. Both comments identify Mars GM but name no source or ephemeris.

**jpl_ssd_planetary_satellite_physical_parameters_phobos_gm**: JPL's Planet and Pluto GM table lists “Mars | 42828.37362 ± 0.0008 | MAR097” (line 264). This rounds to the code's 42,828.37.

**jpl_ssd_astrodynamic_parameters_mars_system_gm_de440_2026**: JPL's Astrodynamic Parameters page states that its planetary-mass values are from DE440 (lines 96-100) and lists Mars-system GM as 42,828.375816 km³/s² (line 106), which rounds to 42,828.38.

**economicspace_mars_gm_verification_sheet_code_current_2026**: The mars_orbit__raw__search-off worksheet check passes and flags I27 NEED BACKING, reporting the derivation constant has no reference.

Upstream: economicspace MU_MARS_KM3_S2, worked_calculation.MU_MARS and verification input I27 are 42,828.37 km³/s². Verdict: identify the intended ephemeris. The current two-decimal value is consistent with MAR097; DE440 rounds one hundredth higher. That numeric match does not establish which ephemeris was intended. Preserve the numeric value if MAR097 is the intended basis; no replacement inferred. **rc-654**. Extracted: extracted_data/r784_mars_gm_ephemeris_basis.csv.

## R799 — Spacecost blackbody-temperature constant citation gap (2026-11-16; rc-669)

At Spacecost main a401930efe30aaad01aafd2b3cb332ad0438c841, spacecost/units.py:37-42 states the rapid-rotator equilibrium relation (S/4sigma)^(1/4), sets S=1361 W/m2, gives sigma=5.670374419e-8 W m-2 K-4, and stores BLACKBODY_TEMP_1AU_K=278.3 K. environments.py:89-96 scales that constant by 1/sqrt(au) into blackbody_temp_k; the current reference/environments.csv has 23 environment rows. CITATIONS.md's Physical constants table maps Kopp & Lean to solar irradiance, CODATA 2018 to Newtonian G, and BIPM/IAU to AU and c; it does not identify sigma.

nist_sp959_2018_codata_constants (NIST SP 959, p. 1) lists the Stefan-Boltzmann constant as 5.670 374 419 ... x 10^-8 W m^-2 K^-4. Using the code's 1361 W/m2 and first ten significant digits of the CODATA value gives 278.321399 K from (S/(4sigma))^(1/4), which rounds to the stored 278.3 K. Verdict: cite CODATA for sigma and document the stored precision and one-decimal rounding; no numeric replacement is inferred. Extracted: extracted_data/r799_blackbody_sigma_source.csv.

## R809 — AsteroidCatalog Newtonian-constant citation gap (2026-11-16)

asteroidcatalog_gravitational_constant_code_current_2026: At AsteroidCatalog main a2c527c09eb39618d7fd26b2b180f730ea906b8b, asteroid_catalog/physics.py line 197 sets G_SI = 6.67430e-11; min_rotation_period_h uses it at line 312. CITATIONS.md lists Pravec & Harris (2000) and Holsapple (2007) for spin-limit literature but no G/CODATA source.

nist_sp961_2022_codata_constants: NIST SP 961 (May 2024), p. 1 lists “Newtonian constant of gravitation G 6.674 30(15) × 10⁻¹¹” m³ kg⁻¹ s⁻².

Verdict: cite the Newtonian constant used by the spin-limit calculation; the current value matches CODATA 2022 at stored precision. No numeric replacement inferred. rc-681. Extracted: extracted_data/r809_asteroidcatalog_newtonian_g_citation.csv.

## R810 — Lunar capture radius matches its cited source (2026-11-16)

- **nasa_nssdca_moon_fact_sheet**: the orbital-parameters table (“for orbit about the Earth”) lists “Semimajor axis (10^6 km)” as 0.3844, equivalent to 384,400 km. The existing `extracted_data/r212_worksheet_constants_key_numbers.csv` records this value against the Economicspace `R_MOON` input.
- Economicspace main `bc11908b8683836e25d572cbb5b54249f8cecb6d`, `modules/calc.py` line 2857 sets `R_MOON_ORBIT_KM=384_400.0`; `_cislunar_capture_dv_km_s` uses it at line 2941 to form the capture ellipse.
- Economicspace `CITATIONS.md` lines 299-303 names the NASA NSSDCA Moon Fact Sheet as the source for `R_MOON`. `campaign/verification_sheet.py` lines 1945-1946 maps the worksheet input through `cite_here` and states that the fact sheet gives 0.3844 million km.
- Verdict: the current value matches the registered source at its printed precision, and both Economicspace documentation and the verification sheet cite it. Draft rc-682 was withdrawn as a false positive; the registry mapping and INDEX now record this existing use.


## R818 — Mars GM attribution and lunar-radius citation rechecks (2026-11-16)

`economicspace_mars_gravitational_parameter_code_current_2026`: fetched economicspace origin/main `e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7` still sets `MU_MARS_KM3_S2` and `MU_MARS` to 42,828.37 km³/s². The MAR097 and DE440 source values still round differently at the stored precision; **rc-654** remains open pending the intended ephemeris basis. Existing extraction: `extracted_data/r784_mars_gm_ephemeris_basis.csv`.

`nasa_nssdca_moon_fact_sheet`: current fetched main still names the Moon Fact Sheet for `R_MOON` in `CITATIONS.md`, and the verification sheet states 0.3844 million km. This confirms the rc-682 false-positive withdrawal; no revision gap remains. Existing extraction: `extracted_data/r212_worksheet_constants_key_numbers.csv`.

## R819 — Mars 1-sol orbit worksheet backing (2026-11-16)

**dra5_2009_human_exploration_of_mars** PDF p. 36 (printed p. 22) states: “At Mars, the vehicles are inserted into a 1-sol orbit (250 km × 33,793 km).” **nasa_nssdca_mars_fact_sheet**, Mars/Earth Comparison, Bulk parameters table, lists “Equatorial radius (km) 3396.2.”

At economicspace origin/main e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7, `modules/calc.py` lines 2898-2899 form periapsis and apoapsis radii by adding 250 km and 33,793 km to 3,396.2 km. `campaign/verification_sheet.py` lines 2062-2067 record I28=3,646.2 km (“250 km altitude”) and I29=37,189.2 km (“33,793 km altitude”); the `mars_orbit__raw__search-off` check flags both NEED BACKING. The DRA altitude pair and NSSDCA equatorial radius support the stored values, but the worksheet does not name the sources or radius convention.

**Verdict:** cite DRA 5.0 and the NSSDCA equatorial radius in the worksheet inputs, and preserve the derived values. **rc-693**. Extracted: `extracted_data/r819_mars_one_sol_orbit_worksheet_citation.csv`.

## R825 — Current rotation-period fallback input (2026-11-17)

The current worksheet maps I70=10.222 h to `CalcConfig.default_rotation_period_h` and explicitly says the 2018 DT period is not measured; the model uses the median of 29,288 AsteroidCatalog periods. It flags the fallback NEED BACKING. **rc-579** now carries the live input mapping. The earlier frozen Stage 3 I70 cargo-containment row in **rc-645** is a different field and remains a separate frozen-row issue. Extracted: `extracted_data/r825_rotation_period_live_input_i70.csv`.

## R866 — Venus/Mercury orbit eclipse inputs lack geometry citation (2026-11-17; rc-742)

`spacecost_venus_mercury_orbit_eclipse_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` stores Venus orbit `cycle_period_hr=3.30`, `eclipse_fraction=0.40`, and derived `dark_period_hr=1.32`; Mercury orbit stores `12.0`, `0.15`, and `1.80`. `environments.py` defines `planet_orbit` as “Around a planet.” Its Venus note refers to an “inner gravity-assist leg”; its Mercury note names MESSENGER and BepiColombo for solar-array pointing. `CITATIONS.md` contains no source entry for these two rows’ cycle or eclipse inputs.

`nasa_nssdca_magellan_mission_plan`: The Mission Plan page states the initial Magellan orbit period was “3 hours, 15 minutes” and gives its elliptical periapsis and apoapsis altitudes as 294 and 8,540 km; after aerobraking, its period was 94 minutes. This supports a mission-specific 3.25-h Venus-orbit comparator, not the row’s eclipse fraction.

`mcnutt_et_al_2012_messenger_early_orbital_operations`: printed p. 2 describes MESSENGER’s “nominal 12-h orbit,” with 200-km periapsis and 82.5° inclination. Printed p. 3 says each 88 days contains “one long-eclipse season, and one short-eclipse season.” This supports a mission-specific period and shows eclipse geometry varies by season; it does not establish a fixed 0.15 fraction.

**Verdict:** identify whether each row represents a specific planetary orbiter, a generic planetocentric orbit, or a heliocentric gravity-assist environment. Cite and derive the eclipse fractions from the applicable orbit and solar-shadow geometry, or label them as scenario assumptions with an averaging basis. Preserve the current values pending that definition; no replacements inferred. **rc-742**. Extracted: `extracted_data/r866_venus_mercury_orbit_eclipse_scope.csv`.

## R867 — Mars 1-sol staging-orbit eclipse fraction basis (2026-11-17; rc-743)

`spacecost_mars_1sol_eclipse_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, the Mars 1-sol staging-orbit row stores `cycle_period_hr=24.62`, `eclipse_fraction=0.05`, and `dark_period_hr=1.231`. The code note describes the fraction as “representative rather than fixed” and orientation-dependent. **CITATIONS.md** lists NASA DRA 5.0 for the staging orbit, but does not give a derivation or averaging basis for 0.05.

`dra5_2009_human_exploration_of_mars` PDF p. 36 (printed p. 22) states: “At Mars, the vehicles are inserted into a 1-sol orbit (250 km × 33,793 km).” This supports the orbit dimensions; the report does not state the stored 5% eclipse fraction. The dark-period value is the arithmetic product 24.62 × 0.05 = 1.231 h.

**Verdict:** retain DRA 5.0 for the orbit dimensions and document the orbit-plane/Sun geometry, season or epoch, and averaging interval used for the eclipse fraction, or label 0.05 as a representative scenario with sensitivity. Preserve the current value pending that basis; no numeric replacement inferred. **rc-743**. Extracted: `extracted_data/r867_mars_1sol_eclipse_scope.csv`.

## R868 — Low lunar orbit eclipse geometry and citation (2026-11-17; rc-744)

`spacecost_low_lunar_orbit_eclipse_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` stores `cycle_period_hr=1.965`, `eclipse_fraction=0.40`, and `dark_period_hr=0.786` for “Low lunar orbit (100 km).” The code note says “118-min period, ~40% of it behind the Moon.” **CITATIONS.md** Section 5 lists the NASA Moon Fact Sheet for lunar mass, radius, and synodic day; its “Illumination and orbits” list names LEO, GEO, NRHO, the lunar polar ridge, and Mars, but no low-lunar-orbit eclipse source.

`nasa_nssdca_moon_fact_sheet`, Moon/Earth Comparison, Bulk parameters table, gives “Volumetric mean radius (km) 1737.4.” With the row’s 100-km altitude, a circular-orbit zero-beta cylindrical-shadow check gives `asin(1737.4 / 1837.4) / π = 0.3945`, near the stored 0.40. This comparison is consistent with one idealized geometry; the row does not state its inclination, solar beta angle, shadow model, or averaging interval. The stored dark period is the arithmetic product 1.965 × 0.40 = 0.786 h.

**Verdict:** state the orbit and lunar-shadow geometry, solar beta angle, and averaging interval behind 0.40, with a citation or calculation; label it as an idealized scenario if that is the intended basis. Preserve the current values pending that definition; no numeric replacement inferred. **rc-744**. Extracted: `extracted_data/r868_low_lunar_orbit_eclipse_scope.csv`.

## R869 — Small-body environment dark-fraction basis (2026-11-17; rc-745)

`spacecost_small_body_environment_illumination_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` stores `eclipse_fraction=0.50` for eleven `neo`, `main_belt`, and `trojan` rows: the generic low-dv NEA, Bennu, Ryugu, Eros, Didymos, the three main-belt zones, Ceres, Psyche, and the Jupiter Trojans. Their cycle periods range from 2.26 to 10.0 h, producing dark periods of 1.13 to 5.00 h.

`warner_harris_pravec_2009_asteroid_lightcurve_database`: **CITATIONS.md** maps the database to the 6–10 h rotation period used for generic asteroid rows. It does not identify a source or site-illumination method for the shared 0.50 fraction in `reference/environments.csv`.

`stubbs_wang_2012_vesta_illumination_conditions`: §5.1, printed p. 275, says the solar disk is “typically seen about half the time in the tropics” on Vesta. Its annual mean visibility ranges from 0.363 to 0.566 across the body and varies with latitude, axial tilt, shape, and topography. This is a Vesta-specific comparator. Closed **rc-413** concerns the separate `operational_costs.csv` and `storage_systems.csv` inputs; it does not target the environment-table rows.

**Verdict:** specify whether the cycle period is a surface solar-day proxy and document the latitude, body orientation, and averaging assumptions behind 0.50, or label it as a scenario with sensitivity. Preserve current values pending that scope; no numeric replacement inferred. **rc-745**. Extracted: `extracted_data/r869_small_body_dark_fraction_scope.csv`.

## R870 — Sun-Earth L2 eclipse-free orbit scope (2026-11-17; rc-746)

`spacecost_sun_earth_l2_eclipse_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` stores `eclipse_fraction=0.0` for “Sun-Earth L2”; `environments.py` describes a halo orbit chosen so the spacecraft “never enters Earth’s umbra” and names JWST and Gaia. **CITATIONS.md** does not list an L2 source in its illumination/orbits section.

`nasa_webb_faq_l2_eclipse_avoidance`: NASA’s Webb FAQ states the mission avoids “Earth and Moon eclipses” during flight to L2 and the 10-year mission (lines 415–419). This is a mission-specific design basis.

`esa_gaia_operations_l2_orbit`: ESA describes Gaia’s “Lissajous-type orbit” around L2 and says it “is not affected by Earth eclipses” (Operational Orbit section, lines 284–286). This is a separate mission-specific orbit family and only states Earth-eclipse scope.

**Verdict:** cite the two mission-specific orbit records and define which eclipse-avoiding orbit the generic row represents; state whether the zero fraction includes both Earth and Moon shadows. Preserve 0.0 for that scoped orbit; no numeric replacement inferred. **rc-746**. Extracted: `extracted_data/r870_sun_earth_l2_eclipse_scope.csv`.

## R871 — Gateway NRHO eclipse-fraction attribution (2026-11-18; rc-747)

`spacecost_nrho_gateway_eclipse_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` stores `cycle_period_hr=157.4`, `eclipse_fraction=0.01`, and `dark_period_hr=1.574` for “Cislunar NRHO (Gateway).” `environments.py` defines the fraction as local-cycle time spent in darkness and derives the dark period by multiplying the cycle by that fraction. **CITATIONS.md** maps Whitley & Martinez 2016 to the NRHO period and qualitative near-continuous illumination, but does not identify a quantitative eclipse-duration source.

`nasa_tm_2020_220481_ppe_reference_trajectory`, §3.1, printed p. 5, describes the Gateway reference as an L2 Southern 9:2 lunar-synodic NRHO with an average period of 6.56 days and says: “Eclipses by the moon are encountered regularly, but last less than 90 minutes.” The same page says the 15-year reference avoids Earth eclipses except for two partial events in years 14 and 15. A 90-minute single-event bound divided by 6.56 days is 0.00953; the row’s rounded 157.4-hour cycle multiplied by 0.01 implies 94.44 minutes. This is compatible with a rounded single-event upper-bound scenario, but the source does not state the event count or a cycle- or year-averaged duty fraction.

**Verdict:** cite the NASA trajectory report and specify whether the 1% is a per-orbit lunar-eclipse interval or total dark time averaged over a period, and whether the two partial Earth eclipses are included. Preserve the current value pending that scope; no numeric replacement inferred. **rc-747**. Extracted: `extracted_data/r871_nrho_eclipse_fraction_scope.csv`.

### Jupiter Trojan heliocentric distance basis (rc-748)

`spacecost_jupiter_trojan_distance_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, the “Jupiter Trojans (L4/L5)” row stores `au_min=4.9`, `au_mean=5.2044`, and `au_max=5.5`. `environments.py` defines `au_mean` as a semimajor-axis proxy, `au_min` and `au_max` as perihelion and aphelion, and computes solar flux, solar-array mass factor, and blackbody temperature from `au_mean`. The row note identifies Lucy and the L4/L5 population but gives no source or selection method for the class bounds or mean. **CITATIONS.md** maps JPL Small-Body Database orbital elements to named bodies, but not to this generic Trojan population.

**Verdict:** cite the data and method for the 4.9–5.5 AU class envelope and 5.2044 AU mean; distinguish Jupiter’s orbit from a Trojan-population summary or a scenario band, and state the selection vintage if a catalog sample was used. Preserve the current values pending that basis; no numeric replacement inferred. **rc-748**. Extracted: `extracted_data/r871_jupiter_trojan_distance_basis.csv`.

### Main-belt heliocentric distance bands (rc-749)

`spacecost_main_belt_distance_bands_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, the inner, mean, and outer main-belt rows store `au_min` / `au_mean` / `au_max` bands of 2.06/2.2/2.5, 2.2/2.7/3.2, and 3.0/3.2/3.5 AU. `environments.py` defines `au_mean` as a semimajor-axis proxy and `au_min`/`au_max` as perihelion/aphelion; the mean drives solar flux, array mass factor, and blackbody temperature. The inner-row note names the 3:1 Kirkwood gap at 2.5 AU, the mean-row note points to `DELTA_V_REFERENCE` at 2.7 AU, and the outer-row note names the 2:1 Kirkwood gap. These notes do not state a source or method for the full bands, means, or class selection. **CITATIONS.md** maps JPL Small-Body Database elements to named bodies, but not to generic main-belt class bands.

**Verdict:** cite and define the source and method for the three class ranges and their means; distinguish resonance boundaries and the internal 2.7 AU destination from a population summary, or label the bins as scenarios. Preserve the current values pending that basis; no numeric replacement inferred. **rc-749**. Extracted: `extracted_data/r871_main_belt_distance_bands.csv`.

## R872 — Low-dv NEA heliocentric distance band (2026-11-18; rc-750)

`spacecost_low_dv_neo_distance_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` row “Near-Earth asteroid (low-dv class)” stores `au_min=1.0`, `au_mean=1.2`, and `au_max=1.5`. `environments.py` defines `au_mean` as the semimajor-axis proxy and `au_min`/`au_max` as perihelion/aphelion; the mean drives solar flux, solar-array mass factor, and blackbody temperature. The row note identifies the 4500 m/s `DELTA_V_REFERENCE` class as Earth-like, low-eccentricity, and low-inclination, and cites Elvis et al. 2011 for accessibility, but does not state the generic distance-band or representative-value method.

`elvis2011`: §5, PDF p. 5, reports mean inclination 2.3° for its ultra-low-delta-v NEO set and says none exceed 7°. Table 1, PDF p. 6, lists six lowest-delta-v examples with semimajor axes 1.027–1.093 AU. These are selected examples and an inclination statistic; they do not identify a population summary or support the row’s 1.0–1.5 AU perihelion/aphelion envelope and 1.2 AU representative value. **CITATIONS.md** maps Elvis et al. to the NEO delta-v accessibility distribution and 6.65 km/s peak, and JPL Small-Body Database orbital elements to named bodies; neither map supplies a generic low-dv class distance selection.

**Verdict:** cite and define the population selection or scenario method behind the 1.0–1.5 AU bounds and 1.2 AU representative value, distinguishing perihelion/aphelion bounds from the representative semimajor axis. Preserve the current values pending that basis; no numeric replacement inferred. **rc-750**. Extracted: `extracted_data/r872_low_dv_neo_distance_basis.csv`.

## R873 — Mars surface day/night fraction attribution (2026-11-18; rc-751)

`spacecost_mars_surface_dark_period_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` row “Mars surface (mid-latitude)” stores `cycle_period_hr=24.66`, `eclipse_fraction=0.50`, and `dark_period_hr=12.33`. The environment note says the sol is 24.66 h and describes a roughly 12 h night. `environments.py` derives `dark_period_hr` by multiplying the cycle by the fraction. **CITATIONS.md** maps the NASA Mars Fact Sheet to mass, radius, and rotation, and Appelbaum & Flood to surface insolation and dust; neither entry maps a source to this row’s illuminated-time fraction.

`nasa_nssdca_mars_fact_sheet`: The orbital-parameters table lists a mean “Length of day” of 24.6597 h, consistent with the stored 24.66 h cycle.

`rucker_2024_mars_surface_power_generation_challenges`: NASA NTRS 20230015763 records Rucker’s *Mars Surface Power Generation Challenges and Considerations*, a 2023 Moon to Mars Architecture Concept Review white paper. PDF p. 2 says typical mid-latitude missions have a 25-hour day/night cycle, with “approximately 50 percent of the time spent under illumination.” The report supports the stored 0.50 as a representative mission scenario and its rounded cycle; it is not a site- and season-independent illumination value. The NTRS record states that the work is a US Government work and public use is permitted.

**Verdict:** cite the NASA white paper for the typical mid-latitude illumination scenario, keep 24.66 h tied to the NASA Mars Fact Sheet, and identify 12.33 h as the derived dark period. Preserve the current values; no numeric replacement inferred. **rc-751**. Extracted: `extracted_data/r873_mars_surface_dark_period_basis.csv`.

## R874 — Phobos surface cycle and dark-fraction scope (2026-11-18; rc-752)

`spacecost_phobos_surface_illumination_code_current_2026`: At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/environments.csv` row “Phobos” stores `cycle_period_hr=7.653`, `eclipse_fraction=0.50`, and `dark_period_hr=3.8265`. The `environments.py` note says Phobos is tidally locked with a 7.65 h orbit and rotation; the code derives the dark period by multiplying the cycle by the fraction. **CITATIONS.md** maps the NASA Mars Fact Sheet to Phobos mass and axes, and Guo et al. 2026 to the GM, but does not map a source to the row’s dark-fraction basis.

`nasa_nssdca_mars_fact_sheet`: The “Satellites of Mars” table gives Phobos sidereal orbital and rotation periods as 0.31891 days each (7.65384 h by conversion), supporting synchronous rotation and a cycle close to the stored value. It does not define the surface illumination fraction or whether it includes Mars occultations.

**Verdict:** cite the fact sheet for Phobos’s synchronous period and state whether 0.50 represents the surface night alone or includes Mars eclipses; identify the geometry and averaging basis. Preserve the current values pending that scope; no numeric replacement inferred. **rc-752**. Extracted: `extracted_data/r874_phobos_surface_illumination_basis.csv`.
