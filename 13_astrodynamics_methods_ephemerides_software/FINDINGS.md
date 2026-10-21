# Domain 13 — Astrodynamics methods, ephemerides & audited software

Backings: economicspace `orbital.py` (`elements_to_state` alone since 8ce5c53, for the dashboard's orbit diagram) and [starred-repos](https://github.com/loggger101/starred-repos), split out of economicspace `research/starred-repos/` on 2026-10-20: the Lambert and Kepler solvers in its `orbital.py`, the ephemeris oracles its probes are measured against, and the licence record of the 17 repositories audited there (starred-repos CITATIONS.md sections 1 and 3-5; economicspace's section 3 credits skyfield for elements_to_state).

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

**Round 206 - Vallado edition stated upstream.**

economicspace@36bc858 CITATIONS.md now names *Fundamentals of Astrodynamics and Applications*, **4th ed., Microcosm Press, 2013**, for vis-viva, circular and escape speed, the combined plane change, Kepler's third law and the synodic period (RELATIONS register). The registry row carried "n.d. (upstream gives no edition)" from R74; year set to 2013 with a dated access_status note. No cell semantics change - validation-case mapping for the Lambert oracle is untouched.

## R219 - economicspace research/starred-repos/ is its own repository (2026-10-20)

economicspace PR#159 (876cd44) moved `research/starred-repos/` to loggger101/starred-repos with its six commits replayed (each replayed tree equals the folder's tree at its source commit; patch-ids, authors and dates unchanged), and moved `orbital.py` to economicspace's root, byte-identical apart from one docstring pointer. PR#160 (31fb355) fixed the section reference that remained in its CITATIONS.md section 5. At starred-repos c1d554c, `sdsstax_ast.tab` is byte-identical to the economicspace copy and its citation is section 2 of that repo's CITATIONS.md; economicspace CITATIONS.md section 2 now says no data is committed there, and sections 3-4 still cite skyfield, Izzo and Mathar for `orbital.py`. No value or verdict moves. Pinned `Cited upstream` cells keep the path as read and carry an R219 note: hasselmann_2012_sdss_taxonomy_v1_1_pds and carvano_2010_sdss_taxonomy_main_belt (domain 01), izzo_2015_revisiting_lamberts_problem, mathar_2021_kepler_equation_first_estimates and vallado_fundamentals_astrodynamics_applications. github_python_skyfield's mapping and the domain 13 backings line (here, INDEX.md, README.md) name the new homes. Older blocks, including domain 22's R75, keep the path as read at their pinned commits.

## R224 - economicspace's orbital.py is elements_to_state alone (2026-10-21)

economicspace PR#164 (8ce5c53) cut its root `orbital.py` to `elements_to_state` and `MU_SUN_KM3_S2`, which its dashboard's orbit diagram uses; the Kepler solver, propagator and `lambert_izzo` are now only in starred-repos' `orbital.py` (PR#2, 223bfef), beside `probe_lambert.py`, their one caller. Its CITATIONS.md section 1 (probe sources) and section 5 (the 17-repository licence table) became pointers to starred-repos' same sections; section 3 credits skyfield for `elements_to_state` alone; section 4 points to starred-repos for Izzo, Mathar and Vallado Example 7-5 and keeps Vallado 4th ed. for the RELATIONS register. Pinned cells carry an R224 note: izzo_2015_revisiting_lamberts_problem, mathar_2021_kepler_equation_first_estimates and vallado_fundamentals_astrodynamics_applications; izzo's, mathar's and github_python_skyfield's mappings and the domain 13 backings (here, INDEX.md, README.md) name the new homes. No value or verdict moves.

**#164 split-audit bit-identity claim independently verified (Round 226, skip unless orbital.py moves again):** economicspace versions.md claims for the `be86297 -> 8ce5c53` narrowing were re-run from published blobs at GR: the extracted elements_to_state function text is byte-equal across old file, narrowed file and starred-repos HEAD (1,277 characters each); a seeded sampler of 5,000 random elliptical orbits (a in [7e6, 1.5e9] km, e < 0.95) at 361 true-anomaly points gives 1,805,000 state vectors with zero mismatches and equal sha256 stream hashes between the two module loads; a one-ulp input perturbation is caught by the same comparison, so the method has the detection power their planted-bug test claims. Related registry facts: skyfield, Izzo 2015, arXiv:2108.03215 and spacekit all resolve to registered rows at current HEAD; parallel Round 224 recorded the pointer side of the same drift.

**Carve-out integrity proven; skip unless starred-repos or its assets move again (Round 227):** two closures recorded. (1) Migration fidelity: the sole data asset that moved in the split, sdsstax_ast.tab (7,552,692 bytes), carries git blob sha1 `bf816438efee4bbb71eba70db6e7b82178bf1f2b` identically at economicspace history path research/starred-repos/sdsstax_ast.tab (commit `fc16598`, 2026-09-03) and starred-repos HEAD (`223bfef`) — content-addressed equality is byte-level proof of a faithful carve-out. The General_Research hosted file in d01 (sdsstax_v1_1_ast_table_pds_bundle.zip, sha256 6a2234d7cf24a04c708550b9986ab6918831c8553a4c91e92550c2c4f31f1f0f per full_texts_manifest.csv) is the upstream PDS bundle, a different artifact from the economicspace copy of the extracted table; no tension. (2) Reference completeness: every one of the 37 corpus mentions of probe_nhats / probe_lambert / research-starred-repos / quietlaunch tokens either names starred-repos as current home (d08 sources_domain.csv oracle row, INDEX backings line 342 via parallel Rounds 223-224) or is a location-neutral functional mention; no checked cell asserts an old path in present tense. The d13 intro line crediting the Izzo 2015 algorithm to the economicspace Lambert-oracle audit (probe_lambert.py, F4) was reviewed and kept: it attributes the audit methodology, not a file location, and R224 notes elsewhere in this domain name the new home.
