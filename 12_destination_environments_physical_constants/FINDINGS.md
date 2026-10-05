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
## R102 - First hosted sources for the domain (2026-10-02; 7 of 16 rows upgraded registered_not_pulled -> full_text_hosted, +1 NEW source, +1 extraction CSV)

All three upstream repos were re-swept at their current HEADs first and carried no new institutional claims (economicspace's only dirty file is a runtime _queue.log line), so this round opened d12 - the one domain whose entire 16 rows sat in the registered-not-pulled queue with zero hosted or verified sources. Every row was probed live from this machine; seven documents were pulled and committed, nine got dated re-check notes recording exactly which route failed.

- `iau_2012_resolution_b2_astronomical_unit` [T3, full_text_hosted] - IAU 2012 General Assembly Resolution B2 (syrte.obspm.fr mirror of the official text; no rights statement in file). The recommendation fixing the astronomical unit at exactly 149,597,870,700 m is quoted verbatim in extracted_data/r102_key_constants.csv.
- `bipm_si_brochure_9th_edition` [T3, full_text_hosted] - BIPM SI Brochure 9th edition (English), CC BY 4.0 statement on p.2 of the file; defined value c = 299,792,458 m/s quoted verbatim from the text layer.
- `nasa_nssdca_moon_fact_sheet` / `nasa_nssdca_mars_fact_sheet` [T3, full_text_hosted] - NASA NSSDCA planetary fact sheets (US Government work); HTML snapshots of the live pages; mass/radius/gravity/escape-velocity/GM table rows read into the extraction CSV.
- `nasa_iss_facts_and_figures` [T3, full_text_hosted] - NASA ISS facts-and-figures page snapshot at the exact URL upstream cites (article body: 5 agencies / 15 countries; crew of seven; ~90-minute orbit; 356 ft end-to-end).
- `appelbaum_flood_1989_tm102299_solar_radiation_mars` [T2, full_text_hosted] - NTRS 19890018252, determination GOV_PUBLIC_USE_PERMITTED; NASA TM-102299 (August 1989) 'Solar Radiation on Mars' = the direct institutional source for environments.csv solar_flux_w_per_m2 on every Mars row: mean beam irradiance at a clear Martian atmosphere = **590 W/m²** (Eq. (4), p.10, quoted verbatim into the extraction CSV) vs upstream's per-heliocentric-distance 586.2 W/m² on both Mars rows (-0.7% = consistency anchor).
- `daly_2023_dart_kinetic_impact` [T1, full_text_hosted] - Nature 616:443 (DART mission paper), in-file CC BY 4.0 statement p.5; impact site (8.84 ± 0.45° S, 264.30 ± 0.47° E) and system albedo (0.15 ± 0.02 at 0.55 μm) quoted verbatim into the extraction CSV.
- **NEW** `thomas_2023_dimorphos_orbital_period_change` [T1, full_text_hosted] - Nature 616:448 (companion paper to Daly; registered this round because it carries what upstream's Didymos row actually points at): the MEASURED orbital-period change of Dimorphos = **−33.0 ± 1.0 (3σ) min**, determined by two independent methods (pre-impact period 11.92148 h; post-impact 11.372/11.371 h per method); in-file CC BY 4.0 statement p.4.

Still registered_not_pulled after this round's re-checks (route failures recorded per row): kopp_lean_2011_total_solar_irradiance (AGU legacy PDF 403 + Wiley pdfdirect bot-blocked despite the OpenAlex OA flag), tiesinga_2021_codata_2018_constants (APS paywall; NIST CUU value pages behind a Cloudflare JS challenge from this machine), willner_2014_phobos_shape_topography / mazarico_2011_lunar_polar_illumination_lola / warner_harris_pravec_2009_asteroid_lightcurve_database (Elsevier, no open copy in the Crossref record; arXiv title query zero for Mazarico), watanabe_2019_hayabusa2_ryugu_spinning_top / yeomans_2000_near_eros_radio_science / russell_2016_dawn_arrives_at_ceres (science.org PDFs 403 from this machine), itu_r_s1003_geostationary_orbit (ITU landing page live but every free-download endpoint pattern fails: XML path 404, dologin_pub.asp 500).

## R115 - Three environments.csv rows read against hosted sources; three new candidates (2026-10-04; registry unchanged)

The hosted Daly 2023 paper, the Siltala and Granvik extraction and the ISS page were read against spacecost@85da36c `reference/environments.csv`.

- **65803 Didymos (rc-067)**: the row cites Daly et al. 2023 for mass 5.28e11 kg and radius 390 m. Table 1 (PDF p3) has a system mass of (5.6 +/- 0.5)e11 kg (Dimorphos 4.3e9 inferred) and a volume-equivalent diameter of 761 +/- 26 m. Both upstream cells are inside Daly's 1-sigma, but the derived surface gravity is 9.6% low and the escape velocity 3.7% low at Daly's numbers.
- **16 Psyche (rc-068)**: the radius (111 km) is Siltala and Granvik's; the mass 2.29e19 kg is not (their GM of 1.482 km3/s2 gives 2.22e19 kg). 2.29e19 is Kretlow's SiMDA perturber mass, already in the registry.
- **Low Earth orbit (rc-069)**: the ISS page says 'about every 90 minutes' and 16 sunrises and sunsets a day; it gives no 92.7-minute period and no shadow time. The cells are consistent with a 400 km circular orbit; only the attribution is off.
- Checked and agreeing (Phobos within 2%): the Mars fact sheet's Phobos column (10.6e15 kg; axes 13.0 x 11.4 x 9.1 km, i.e. a mean radius of 11.0 km; period 0.31891 d) against the Phobos row (1.0659e16 kg, 11.267 km, 7.653 h); Mars surface gravity and mass; Appelbaum and Flood Table IV daily mean global irradiance on clear days (250-308 W/m2 against the 590 W/m2 beam mean, i.e. 42-52%) against the Mars row's '40-60% of the orbital figure'. The Moon sheet's mass (7.346e22 kg) is 0.05% above the row's 7.342e22, too small to record.

Extracted data: `extracted_data/r115_environment_rows_vs_sources.csv` (10 rows).
