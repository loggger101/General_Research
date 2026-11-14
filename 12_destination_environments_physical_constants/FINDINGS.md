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
