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

## R212 - economicspace PR#154 worksheet backing: two institutional constant sources registered (2026-10-20)

economicspace origin/main moved 36bc858 -> 675f0cf (PR#154, Verification worksheet citations and backing). Its CITATIONS.md now cites documents for three worked_calculation constants that R207 had recorded in d19 as self-derived by design. Neither document was registered; both are added this round:

- iers_petit_luzum_2010_conventions_tn36 [T2, verified_live_not_pulled]: official IERS Conventions Centre PDF read live (179 pp). Table 1.1 prints GM_EARTH = 3.986004418 x 10^14 m^3 s^-2 and worked_calculation MU_EARTH = 398,600.4418 km^3 s^-2 agrees exactly at that precision. In-file publisher copyright on the title page makes it extraction-only per R94; DTIC mirror ADA535671 was bot-walled from this machine when probed.
- nasa_nssdca_earth_fact_sheet [T3, full_text_hosted]: Mean orbital velocity 29.78 km/s (V_EARTH = 29.784 agrees to published figures) and J2000 Semimajor axis 1.00000011 AU (window_phasing_au = 1 au likewise).

R_MOON correction recorded deliberately: the Moon fact sheet publishes Semimajor axis 0.3844 x 10^6 km, so R_MOON = 384,400 km agrees exactly at published precision - there is NO mismatch with this source and no future round should flag one (a 384,500 average-distance figure does not appear on the current page). DV_NRHO restates spacecost delta_v_segments row 'TLI -> NRHO insertion' per PR#154 own note; that row already carries its source - nothing to register.

rc-175 / rc-176 / rc-177 targets (MODEL.md, README.md, master.py and modules/mineral_value.py constants) are untouched by PR#154: the diffstat covers CITATIONS.md, campaign/verification_sheet.py, campaign/worked_calculation.py and versions.md only. The economicspace tree still carries a further WIP batch after #154 - audit published state per R206 rule next round.

## R213 - environments gravity and escape-speed self-consistency clean (2026-10-20)

Recomputed surface_gravity_m_per_s2 as G*M/R^2 and escape_velocity_m_per_s as sqrt(2*G*M/R) from the mass_kg and mean_radius_m each row itself publishes, for all ten body rows of spacecost@29a7ced reference/environments.csv (Lunar equator + polar ridge, Bennu, Ryugu, Eros, Didymos, Mars mid-latitude, Phobos, Ceres, Psyche): every stored value reproduces within 0.02 percent either way - the rounding level of G itself. No candidate; future rounds need not re-run this seam unless those columns move.

## R214 - environments solar-irradiance seam exact (2026-10-20)

Recomputed the product of solar_flux_w_per_m2 and au_mean squared for every row carrying both fields in spacecost@29a7ced reference/environments.csv: all 23 rows reproduce exactly 1361.0 W/m^2 at full stored precision (the CSV keeps au_mean beyond its printed digits). The flux column is derived from one inverse-square law against the 1361 solar constant rather than independent per-body measurements - internally exact, no candidate; skip unless those columns move.

## R238 - Phobos: Willner 2014's own figures, and rc-133 applied (2026-10-21)

Re-read `willner_2014_phobos_shape_topography` from the same DLR elib file R121 read (sha256 585ee394..., not hosted). It gives a mean radius r0 = 10.993 km (PDF p5), a volume of 5741.5 km3 (p4; Table 3: 5742 +/- 35), SH-model axes 13.03 x 11.40 x 9.14 km, and quotes Andert et al. 2011's GM of 0.7127 x 10^-3 km3/s2, which is 1.0678e16 kg. So neither the fact sheet nor Willner holds upstream's 1.0659e16 kg or 11.267 km; the row's pipeline_mapping now says so. spacecost 0.12.6 (PR #29, tag v0.12.6, main `b5eb32a`) applied rc-133: the note labels both values an estimate and gives what each source prints. `extracted_data/r238_willner_2014_phobos_key_numbers.csv`.

**Round 291 - environments.csv physics recompute, skip-note.**

All 23 rows recomputed from committed bytes at spacecost@860bef9 (raw git-show capture, uniform parsed-width proof). Surface gravity equals G*M/R^2 and escape velocity sqrt(2GM/R) on every row with mass plus radius; dark period equals eclipse fraction times cycle period wherever all three are present; blackbody temperature is the rapid-rotator uniform-temperature value (S/4sigma)^0.25 at zero bond albedo in every single row - one convention, no exceptions; solar_array_mass_factor equals au_mean^2 exactly (= 1361/stored flux) in all rows.

The one_way_light_time_min column is formulaic and display-only. Heliocentric rows equal (au_max + 1.0167) AU times 8.316746 min per AU, identical to about 1e-6 across the family - body aphelion plus Earth aphelion, i.e. a strict worst-case conjunction; the CHANGELOG for the table release describes exactly this as "conjunction range and one-way light time", so stored values match their own documented convention. Cislunar rows instead store exact nominal distances from Earth: LEO 400 km reproduces to display precision, GEO within 2.2 km of the 35,786 km ring (0.006 percent), Sun-Earth L2 at 1.5 million km, lunar distance 384,467 km (+0.017 percent against semi-major axis 384,400). Prose notes agree with the stored figures (main belt mean "a 35-minute one-way light time", Jupiter Trojans "a 54-minute one-way light time").

Consumption check: git grep for one_way_light_time and solar_array_mass_factor at HEAD of spacecost and economicspace returns zero hits outside the CSV itself - both columns are data-only pass-throughs. Do not re-sweep the derived physics of this table unless its input columns move.
