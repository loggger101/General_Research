# Domain 12 — Destination environments & physical constants

Backings: spacecost `reference/environments.csv` (solar flux, array mass factor, gravity, escape velocity, light time, eclipse and dark periods for each destination) and the constants in `spacecost/units.py`.

Created in Round 74 (2026-09-27). Blocks are appended one per round, newest last.

## R74 - Upstream citations registered (2026-09-27; +16 sources, T1x9, T2x1, T3x6; nothing extracted)

Sources the upstream repos cite that this registry did not have, found by reading every per-row `notes` field, code comment and CITATIONS.md in AsteroidCatalog@852bf69, spacecost@e831245 and economicspace@1f470d4. Each is `registered_not_pulled`: its DOI was checked against Crossref, or its landing page against a live request from this machine, and the result is recorded in the row. No full text was sought and no number was extracted; the rows are the queue for a later extraction round.

- `kopp_lean_2011_total_solar_irradiance` (T1): environments.csv solar_flux_w_per_m2 and solar_array_mass_factor for every row (1 AU total solar irradiance).
- `tiesinga_2021_codata_2018_constants` (T1): environments.csv surface_gravity and escape_velocity (Newtonian constant of gravitation).
- `iau_2012_resolution_b2_astronomical_unit` (T3): environments.csv one_way_light_time_min (AU as a defined length).
- `bipm_si_brochure_9th_edition` (T3): environments.csv one_way_light_time_min (defined value of c).
- `nasa_nssdca_moon_fact_sheet` (T3): environments.csv lunar rows: mass, mean radius, synodic day.
- `nasa_nssdca_mars_fact_sheet` (T3): environments.csv Mars surface mass, radius and sol; Phobos row.
- `willner_2014_phobos_shape_topography` (T1): environments.csv Phobos mean radius.
- `watanabe_2019_hayabusa2_ryugu_spinning_top` (T1): environments.csv 162173 Ryugu mass, mean radius, rotation, orbit.
- `yeomans_2000_near_eros_radio_science` (T1): environments.csv 433 Eros mass and mean radius.
- `daly_2023_dart_kinetic_impact` (T1): environments.csv 65803 Didymos mass, radius, rotation.
- `russell_2016_dawn_arrives_at_ceres` (T1): environments.csv 1 Ceres mass and mean radius.
- `nasa_iss_facts_and_figures` (T3): environments.csv Low Earth orbit (400 km) period and eclipse fraction.
- `itu_r_s1003_geostationary_orbit` (T3): environments.csv Geostationary orbit eclipse seasons (cited with "standard GEO mission practice").
- `mazarico_2011_lunar_polar_illumination_lola` (T1): environments.csv Lunar surface (polar ridge) illumination fraction.
- `appelbaum_flood_1989_tm102299_solar_radiation_mars` (T2): environments.csv Mars surface insolation and the dust caveat on that row.
- `warner_harris_pravec_2009_asteroid_lightcurve_database` (T1): environments.csv generic asteroid rows: population-median rotation period.
