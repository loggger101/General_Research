# Domain 13 — Astrodynamics methods, ephemerides & audited software

Backings: economicspace `research/starred-repos/`: the Lambert and Kepler solvers in `orbital.py`, the ephemeris oracles its probes are measured against, and the licence record of the 17 repositories audited there (economicspace CITATIONS.md sections 3-5).

Created in Round 74 (2026-09-27). Blocks are appended one per round, newest last.

## R74 - Upstream citations registered (2026-09-27; +23 sources)

Every source the upstream repos cite that the registry lacked, each `registered_not_pulled`:

- `izzo_2015_revisiting_lamberts_problem` (T1): the algorithm behind economicspace's Lambert oracle (probe_lambert.py, F4).
- `vallado_fundamentals_astrodynamics_applications` (T4): the oracle's published validation case.
- `mathar_2021_kepler_equation_first_estimates` (T4): the Kepler-equation starter in orbital.py `kepler_E`.
- `jpl_horizons_api`, `neodys_orbit_covariance_service`, `jpl_de441_small_body_perturber_kernels` (T3): recommended upstream for bounding the oracle's two-body error and for orbit covariances; not yet used.
- 17 audited GitHub repositories (T4). Code was adapted only from `github_python_skyfield` (kepler_E, true_anomaly, elements_to_state) and `github_space_datasets` (the SDSS taxonomy PDS3 layout and the NHATS endpoint). `github_astroquery` pointed to NEODyS, `github_space_map` showed SBDB's field list, `github_spacekit` is the technique behind the ui.py orbit diagram, `github_brahe` is recommended for SPICE/Horizons; `github_nyx` is copyleft, so Lambert was implemented from the paper. Nothing was taken from `github_z3`, `github_pyomo`, `github_pymc`, `github_mesa`, `github_openscvx`, `github_pygmo2`, `github_polars`, `github_pds4_tools`, `github_campyros` or `github_celestia`.

**rc-049:** economicspace CITATIONS.md lists the Horizons API as `https://ssd-api.jpl.nasa.gov/horizons.api`, which answers 404; the live endpoint is `https://ssd.jpl.nasa.gov/api/horizons.api`. Nothing in the pipeline calls it yet.

## R109 - The three JPL service rows re-classified; SB441 manual registered (2026-10-03)

| row | result |
|---|---|
| jpl_horizons_api | **open_service**: Horizons API v1.3 answered a Mars OBSERVER query (radius 3389.92 +/- 0.04 km, density 3.933 g/cm^3) and a Bennu VECTORS query (A=1.12639 au, EC=.20375 at EPOCH 2455562.5). Snapshots: extracted_data/r109_horizons_mars_observer_ephemeris.json, r109_horizons_bennu_101955_vectors_ephemeris.json; key numbers in r109_jpl_astrodynamics_services_key_numbers.csv. v1.3 (2025 June) renamed `EPH_TYPE` to `EPHEM_TYPE`. The dead URL behind rc-049 still answers 404. |
| jpl_de441_small_body_perturber_kernels | **open_service**: sb441-n16.bsp 615.8 MB, sb441-n373s.bsp 936.6 MB, sb441-n373.bsp 14.13 GB, too large to commit (URLs and sizes in extracted_data/). The I/O manual SB441_IOM392R-21-005 (Farnocchia, 2021-03-30) is hosted as `jpl_sb441_iom_perturber_manual` [T2, public domain]. |
| neodys_orbit_covariance_service | stays registered_not_pulled: the service serves an anti-bot page to this machine. |

## R119 - mathar_2021_kepler_equation_first_estimates read in full, not hostable (2026-10-05)

`mathar_2021_kepler_equation_first_estimates` read from arXiv 2108.03215v3 (default arXiv licence, so not hosted): a starting guess for Kepler's equation from e and M, the starter `kepler_E` cites. Context only.

## R121 - izzo_2015_revisiting_lamberts_problem hosted from the arXiv CC0 copy (2026-10-05)

`izzo_2015_revisiting_lamberts_problem` hosted as full_texts/izzo_2015_revisiting_lamberts_problem_celestial_mech_dynam_astron_arxiv1403.2705.pdf (arXiv abs page: CC0 dedication). The algorithm behind economicspace's lambert_izzo oracle; its time-of-flight relations are not yet extracted.
