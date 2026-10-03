# Domain 13 — Astrodynamics methods, ephemerides & audited software

Backings: economicspace `research/starred-repos/`: the Lambert and Kepler solvers in `orbital.py`, the ephemeris oracles its probes are measured against, and the licence record of the 17 repositories audited there (economicspace CITATIONS.md sections 3-5).

Created in Round 74 (2026-09-27). Blocks are appended one per round, newest last.

## R74 - Upstream citations registered (2026-09-27; +23 sources, T1x1, T3x3, T4x19; nothing extracted)

Sources the upstream repos cite that this registry did not have, found by reading every per-row `notes` field, code comment and CITATIONS.md in AsteroidCatalog@852bf69, spacecost@e831245 and economicspace@1f470d4. Each is `registered_not_pulled`: its DOI was checked against Crossref, or its landing page against a live request from this machine, and the result is recorded in the row. No full text was sought and no number was extracted; the rows are the queue for a later extraction round.

- `izzo_2015_revisiting_lamberts_problem` (T1): economicspace Lambert oracle (probe_lambert.py, F4): the algorithm implemented from the paper.
- `vallado_fundamentals_astrodynamics_applications` (T4): validation case for the Lambert oracle (published worked example).
- `mathar_2021_kepler_equation_first_estimates` (T4): Kepler-equation starter and quartic Newton step in orbital.py kepler_E (reached via skyfield).
- `jpl_horizons_api` (T3): recommended oracle for bounding the two-body error in the F4 Lambert oracle; not yet used upstream.
- `neodys_orbit_covariance_service` (T3): recommended per-object orbit covariance source; not yet used upstream.
- `jpl_de441_small_body_perturber_kernels` (T3): recommended offline harness to bound the Lambert oracle two-body assumption; not yet used upstream.
- `github_python_skyfield` (T4): economicspace repository audit: code adapted: kepler_E, true_anomaly and elements_to_state in research/starred-repos/orbital.py.
- `github_space_datasets` (T4): economicspace repository audit: the PDS3 column layout for the SDSS taxonomy table, and the JPL NHATS endpoint used by probe_nhats.py.
- `github_astroquery` (T4): economicspace repository audit: nothing taken; showed the IRSA async-TAP approach and pointed to the NEODyS covariance service.
- `github_space_map` (T4): economicspace repository audit: nothing taken; showed that SBDB publishes a field list (how condition_code was found missing).
- `github_z3` (T4): economicspace repository audit: nothing taken yet.
- `github_pyomo` (T4): economicspace repository audit: nothing taken.
- `github_pymc` (T4): economicspace repository audit: nothing taken yet.
- `github_mesa` (T4): economicspace repository audit: nothing taken (listed upstream as mesa/mesa).
- `github_openscvx` (T4): economicspace repository audit: nothing taken.
- `github_pygmo2` (T4): economicspace repository audit: nothing taken.
- `github_polars` (T4): economicspace repository audit: nothing taken.
- `github_spacekit` (T4): economicspace repository audit: nothing taken; its per-body Kepler solve is the technique behind the ui.py orbit diagram.
- `github_brahe` (T4): economicspace repository audit: nothing taken yet; recommended for its SPICE reader and Horizons SPK client.
- `github_pds4_tools` (T4): economicspace repository audit: nothing taken.
- `github_nyx` (T4): economicspace repository audit: nothing taken (copyleft; Lambert deliberately implemented from the paper instead).
- `github_campyros` (T4): economicspace repository audit: nothing taken.
- `github_celestia` (T4): economicspace repository audit: nothing taken.

**Dead endpoint in economicspace CITATIONS.md (rc-049).** The Horizons API is listed as `https://ssd-api.jpl.nasa.gov/horizons.api`, which answers 404 with or without query parameters. The live endpoint is `https://ssd.jpl.nasa.gov/api/horizons.api` (an OBJ_DATA query for Mars returned JSON on 2026-09-27). Nothing in the pipeline calls it yet, so only the reference changes.

## R109 - The three JPL service rows get live re-classified + the SB441 I/O manual registered (2026-10-03; registry 399 -> 400)

R74 registered the services upstream's probes recommend but never use, all as `registered_not_pulled`. This round each was re-checked from this machine and moved to its true access class:

| row | R109 result |
|---|---|
| jpl_horizons_api | **open_service** - Horizons API v1.3 at https://ssd.jpl.nasa.gov/api/horizons.api answered live JSON for a Mars OBSERVER ephemeris (PHYSICAL DATA: radius 3389.92+-0.04 km, density 3.933 g/cm^3) and a Bennu VECTORS query (osc elements A=1.12639 au / EC=.20375 at EPOCH 2455562.5; the exact shape upstream's F4 Lambert-oracle probe would issue). Evidence snapshots: extracted_data/r109_horizons_mars_observer_ephemeris.json + r109_horizons_bennu_101955_vectors_ephemeris.json, key numbers in r109_jpl_astrodynamics_services_key_numbers.csv. **v1.3 breaking change (2025 June): parameter `EPH_TYPE` renamed `EPHEM_TYPE`** - pre-2025 query examples now 400 with 'one or more query parameter was not recognized'. rc-049 re-checked: upstream's dead URL (ssd-api.jpl.nasa.gov/horizons.api) still HTTP 404; the corrected endpoint is now live-proven twice.
| jpl_de441_small_body_perturber_kernels | **open_service** - kernel directory re-pulled live: sb441-n16.bsp 615.8 MB / sb441-n373s.bsp 936.6 MB / sb441-n373.bsp 14.13 GB, all beyond the ~36 MB repo cap -> URL'd + size/date-recorded in extracted_data/, not committed. The I/O manual SB441_IOM392R-21-005 (Farnocchia, JPL interoffice memorandum, 2021-03-30) pulled live and **hosted** under full_texts/ as its own registry row `jpl_sb441_iom_perturber_manual` [T2, public-domain; no in-file copyright statement].
| neodys_orbit_covariance_service | stays **registered_not_pulled** - newton.spacedys.com/neodys/ now serves an anti-bot interstitial ('Making sure you're not a bot!', 3,629 B challenge page) from this machine instead of the JS app shell recorded in R74; no API surface reachable without solving it.

No revision candidate opened or closed by this round (rc-049 stays open - upstream's CITATIONS.md is read-only and still carries the dead URL; its evidence column now records both re-checks).
