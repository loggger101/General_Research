# General Research

The evidence registry behind the **economicspace** asteroid-mining profitability
pipeline, its Stage 3 reference package **spacecost**, and its Stage 1 package
**AsteroidCatalog**. Each source here was accessed and read: the full text is
hosted where it may be redistributed; otherwise the metadata, abstract and
extracted numbers are kept. Since Round 74 the registry also lists every source
those repos cite, grey sources (T4) included, so each upstream dependency is
visible before it is read. Rejected sources appear only in INDEX.md "Rejected
sources".

## Domains

This repo backs the cells that `economicspace/CITATIONS.md` leaves weakly
sourced, one domain per group of cells; domains 1–5 were the weakest, the rest
were added as rounds found uncovered cells. Each domain's FINDINGS.md names its
cells, their values and what a source must supply.

| # | domain | pipeline cell(s) it could back or replace |
|---|---|---|
| 1 | Bulk density by spectral type, PGM factors, population statistics | AsteroidCatalog `taxonomy_composition.csv` density/PGM columns; ranking quality |
| 2 | Composition → commodity value mapping (what an S/C/X/K/Q body actually contains) | `taxonomy_composition.csv` material fractions, `mineral_value.py` mineralogy |
| 3 | Δv budgets and propulsion performance tables | `spacecost/reference/delta_v_segments.csv`, `propellants.csv` Isp rows |
| 4 | Launch $/kg to LEO/GTO — history and projections | `spacecost/reference/launch_vehicles.csv` price rows, cost cascade |
| 5 | In-space storage (boil-off), ISRU, operational costs | `storage_systems.csv`; the volatile-ISRU, power and electric-propulsion rows of `operational_costs.csv` (power and EP overlap domain 11; the sources for its finance, licensing, operations, mining and hardware-rate rows moved to 16–21 in Round 77); environment penalties |
| 6 | Commodity market prices (the value side) | `mineral_value.py` `ref_price_usd_per_kg`, which feeds every profitability row |
| 7 | Mission program-cost benchmarks (NRE / development) | `operational_costs.csv` NRE rows (spacecraft development, autonomous mining control), sample-recovery ops envelope |
| 8 | NEA accessibility oracles (round-trip Δv ground truth) | distribution/rank reference for the NEA rows of `delta_v_segments.csv` (economicspace `probe_nhats.py`) |
| 9 | In-space delivery mass fractions & EDL survival | spacecost `delivery.py` constants such as `MARS_LANDED_MASS_FRACTION` |
| 10 | Launch vehicle & engine hardware / propellant performance | engine-level ground truth for `propellants.csv` and `launch_vehicles.csv` |
| 11 | Spacecraft power & electric propulsion | power and electric-propulsion rows of `operational_costs.csv` |
| 12 | Destination environments & physical constants | spacecost `environments.csv` (flux, gravity, escape velocity, light time, eclipse) and `units.py` constants |
| 13 | Astrodynamics methods, ephemerides & audited software | economicspace `orbital.py` (Lambert and Kepler solvers) and [starred-repos](https://github.com/loggger101/starred-repos), split from economicspace `research/starred-repos/` (ephemeris oracles, the 17-repository licence audit) |
| 14 | Propellant & consumable prices | `propellants.csv` `ref_cost_usd_per_kg` and its component prices |
| 15 | In-space demand & market absorption | economicspace `mineral_value.py` in-space utility (market side; the engineering basis of each row is in 28–30 since Round 161), annual-demand and class-share tables; `calc.py` `demand_elasticity`, `surplus_price_fraction` |
| 16 | Reliability, learning curves & hardware service life | `operational_costs.csv` launch reliability, spacecraft MTBF, mining success and growth, rig life, trips and salvage rows; `calc.py` `learning_curve_rate` |
| 17 | Cost of capital, contingency & insurance | `operational_costs.csv` WACC, contingency, launch and third-party insurance rows; `calc.py` `contingency_fraction` |
| 18 | Licensing, planetary protection & space-resource law | `operational_costs.csv` FAA Part 450 licensing rows and the MPL behind third-party liability; the Earth-return and right-to-sell premises (context-only) |
| 19 | Asteroid excavation throughput & beneficiation | `calc.py` mining rate, rig mass, beneficiation recovery and concentration cap; `operational_costs.csv` drilling and beneficiation energy, plant throughput; `mineral_value.py` in-space refining energy |
| 20 | Mission operations, communications & ground segment | `operational_costs.csv` mission operations, DSN time, downlink and depot berthing rows |
| 21 | Spacecraft mass & recurring-cost estimating relationships | `operational_costs.csv` recurring $/kg rows by hardware class; `calc.py` return-structure and heat-shield fractions, NRE/recurring overlap |
| 22 | Prior-art techno-economic benchmarks | economicspace's headline answer (`campaign/results.csv` `best_obj`, `winner`): an external oracle for profitability, as domain 8 is for Δv |
| 23 | Cost indices, dollar years & exchange rates | the `reference_year` of every spacecost table, the CPI factors in row notes, and the exchange rates behind non-US prices |
| 24 | Aerocapture & aerobraking | `calc.py` aero-assisted returns (LEO/Mars trim, GEO aerocapture, fallback saving); `delta_v_segments.csv` aerocapture and aerobraked rows |
| 25 | Net smelter return: refining charges & payable terms | `calc.py` `_mineral_implied_value` (100% of contained metal at refined prices) and the refined-metal basis of element prices |
| 26 | Spacecraft storage & energy-system physical properties (propellant tankage / COPV / MLI / cryocooler; RTG / fission surface power) | `storage_systems.csv` propellant-storage + energy-storage cells (COPV burst performance factor, MLI passive, orbital-depot boil-off, RTG specific power, Kilopower-class fission W-elec/kg); the cargo-containment cells stay upstream judgement rows for now |
| 27 | Orbital debris & collision risk | the debris environment behind `operational_costs.csv` launch-insurance premium drivers (domain 17), economicspace's satellite-lifetime and disposal assumptions, and the depot mission durations of domain 26 |
| 28 | Radiation-shielding value of in-space materials | the rock rows of economicspace `mineral_value.py` `IN_SPACE_UTILITY` (silicates, oxides, rock-valued carbonates and phosphates), the shielding part of water's row, and their destination overrides |
| 29 | Structural metals, alloys & in-space manufacturing | the structural-class rows of `IN_SPACE_UTILITY` (Fe, Ni, Co, Cu, Cr, Ti, Fe-Ni alloy phases and their ores): the manufacturing-gap discount and its destination overrides |
| 30 | Volatiles, process chemicals & catalyst metals in space | the propellant, chemical and trace-class rows of `IN_SPACE_UTILITY` (water, ammonia, CO2, carbon, organics, S, P, PGMs and other trace metals) and the rejected PGM catalyst utility |

## Layout

```
README.md                                This file
INDEX.md                                 Every source by domain: tier, access, what it backs; rejected sources last
RESEARCH_LOG.md                          One entry per research round, newest first
sources.csv                              Machine-readable registry, one row per source (GENERATED by tools/build_registry.py)
full_texts_manifest.csv                  Every hosted file: source id, size, sha256, licence
revision_candidates.csv                  Upstream cells the evidence says should change, with status
upstream_commit_map.csv                  Upstream commits cited by checked_against that a history rewrite took off main, mapped to their main equivalents
DOWNLOADS.md                             Non-hosted sources still to fetch, with links
AGENTS.md                                Working rules for research rounds
tools/                                   build_registry.py, validate.py, tests/ (planted-defect tests, coverage gate, debug script)
01_density_and_population/               Domain 1: density by spectral type, PGM factors, population stats
02_composition_value/                    Domain 2: composition → commodity value mapping
03_dv_propulsion/                        Domain 3: Δv budgets, propulsion performance tables
04_launch_economics/                     Domain 4: launch cost per kg — history and projections
05_inspace_operations/                   Domain 5: storage/boil-off, ISRU, in-space operational costs
06_commodity_market_pricing/             Domain 6: commodity/mineral market prices
07_mission_program_costs/                Domain 7: mission program-cost benchmarks (NRE / development anchors)
08_nea_accessibility_oracles/            Domain 8: NEA accessibility oracles (round-trip Δv ground truth)
09_delivery_mass_fractions_edl_survival/ Domain 9: in-space delivery mass fractions & EDL survival
10_launch_vehicle_engine_hardware/       Domain 10: launch vehicle & engine hardware / propellant performance
11_spacecraft_power_electric_propulsion/ Domain 11: spacecraft power & electric propulsion
12_destination_environments_physical_constants/ Domain 12: destination environments & physical constants
13_astrodynamics_methods_ephemerides_software/  Domain 13: astrodynamics methods, ephemerides & audited software
14_propellant_consumable_prices/          Domain 14: propellant & consumable prices
15_inspace_demand_market_absorption/      Domain 15: in-space demand & market absorption
16_reliability_learning_service_life/     Domain 16: reliability, learning curves & hardware service life
17_cost_of_capital_contingency_insurance/ Domain 17: cost of capital, contingency & insurance
18_licensing_planetary_protection_space_law/ Domain 18: licensing, planetary protection & space-resource law
19_asteroid_excavation_beneficiation/     Domain 19: asteroid excavation throughput & beneficiation
20_mission_operations_communications/     Domain 20: mission operations, communications & ground segment
21_mass_cost_estimating_relationships/    Domain 21: spacecraft mass & recurring-cost estimating relationships
22_prior_art_techno_economic_benchmarks/   Domain 22: prior-art techno-economic benchmarks
23_cost_indices_dollar_years/             Domain 23: cost indices, dollar years & exchange rates
24_aerocapture_aerobraking/               Domain 24: aerocapture & aerobraking
25_net_smelter_return_refining_terms/     Domain 25: net smelter return: refining charges & payable terms
26_spacecraft_storage_energy_properties/     Domain 26: spacecraft storage & energy-system physical properties
27_orbital_debris_collision_risk/          Domain 27: orbital debris & collision risk
28_radiation_shielding_value_of_materials/ Domain 28: radiation-shielding value of in-space materials
29_structural_metals_inspace_manufacturing/ Domain 29: structural metals, alloys & in-space manufacturing
30_volatiles_chemicals_catalysts_inspace_use/ Domain 30: volatiles, process chemicals & catalyst metals in space

<domain>/sources_domain.csv              The registry rows for that domain (the file you edit)
<domain>/FINDINGS.md                     Findings, one block per round
<domain>/full_texts/                     Redistributable full texts
<domain>/extracted_data/                 CSVs of extracted numbers with page/table locations
```

## Source tiers

- **T1**: peer-reviewed journal articles.
- **T2**: NASA / ESA technical reports and AIAA / IAC proceedings.
- **T3**: authoritative government or dataset publications with a DOI (USGS MCS, PDS releases, NEOWISE V2.0).
- **T4**: grey sources that upstream rows cite (company documents, price pages, news, encyclopedias, textbooks,
  software and market-data APIs). A T4 row marks weak evidence; a T1–T3 replacement is the usual next step.

## Access classes

The first word of every `access_status` is one of these; the rest says how it was verified.

| class | meaning |
|---|---|
| `full_text_hosted` | committed under `<domain>/full_texts/` and listed in `full_texts_manifest.csv` |
| `public_domain_excerpt_hosted` | public-domain document too large to commit; the passage is quoted in `FINDINGS.md` |
| `verified_live_not_pulled` | fetched and read from this machine, not committed |
| `open_not_pulled` | open access, but the publisher blocks this machine or the licence forbids hosting; metadata + abstract recorded |
| `open_service` | a live database or API, verified from this machine; derived numbers committed |
| `skipped` | deliberately not hosted; the owner's decision is in the row |
| `registered_not_pulled` | an upstream citation, DOI or landing page checked, not yet read; re-class it when pulled |

## Access rules (this repo is public)

1. Full texts are committed only when redistributable: CC-licensed arXiv versions, public-domain or CC-licensed
   NASA/ESA documents, and open-access articles whose licence permits it. The licence is read off the file or its
   record (PDF statement, NTRS copyright determination, arXiv abs page) into `full_texts_manifest.csv`. arXiv's
   default licence does not qualify. `validate.py` warns on any hosted file whose licence does not permit it.
2. Paywalled items get metadata, the abstract and any numbers from the accessible portion, with page/table locations.
3. Every extracted number carries its source id and location.

## How an item earns a place here

1. It can back or replace a specific pipeline cell.
2. Its access was verified from this machine.
3. Its numbers are in an extracted-data CSV, or its registry row says "Context-only: <reason>".

A `registered_not_pulled` row is exempt from 2 and 3 until a round reads it.

## Adding a domain

Open one when upstream cells have no domain behind them. It needs:

1. A folder `NN_short_name/` (next number) with a header-only `sources_domain.csv` and a `FINDINGS.md` holding a title,
   a `Backings:` line, and a first block tabling the cells, their values and the upstream commit read.
2. A `## Domain N — title` section in INDEX.md above `## Rejected sources`, with a `_Backings:_` line and the
   five-column table header.
3. A row in the domain table above and a line in "Layout".
4. A research-log entry.

## Moving a source between domains

When the cells its `pipeline_mapping` names belong to another domain (procedure from Round 77; the id never changes):

1. Move its `sources_domain.csv` row, and its INDEX row to the end of the new domain's table.
2. `git mv` its hosted files (update `domain_dir` in the manifest) and every extracted-data CSV citing only it; a
   shared CSV stays and is named with the old domain's folder.
3. Add a block to each FINDINGS.md: the old one lists the moved ids and new paths, the new one what arrived.
4. Leave `domain_dir` in `revision_candidates.csv` alone: it names the FINDINGS.md with the write-up.

## Rejecting a source

Only the owner rejects a source. Its row in INDEX.md "Rejected sources" (`id`, `source`, `link`, `reason`) becomes
its only record and its id stays reserved. Then delete its registry and INDEX rows, hosted files and manifest rows,
extracted-data files and rows (`a;b` rows included), FINDINGS write-ups and mentions, DOWNLOADS entry, and every
revision candidate resting on it alone (for shared ones, drop the id and rewrite the evidence; deleted `rc-NNN`
numbers are not reused). Past log entries stay; add one naming the id, reason and deleted candidates. `validate.py`
fails if the id is registered or named anywhere but the research log.

## Revision candidates

This repo never edits the pipeline repos. A contradicting source becomes a FINDINGS block and a
`revision_candidates.csv` row: target file and row, current value and the upstream commit it was read from, proposed
change, evidence and status (`open`, `applied`, `declined`, `superseded`, `blocked`, or `withdrawn` when this repo's
evidence was wrong). Re-check open rows when upstream releases.

## Tools

```
python tools/build_registry.py          # regenerate sources.csv; fill manifest sizes + hashes (--check: fail if stale)
python tools/validate.py                # consistency checks; exit 1 on any error (--strict, --verbose, --upstream)
python -m unittest discover -s tools/tests   # the tools' own tests
python tools/tests/measure_coverage.py  # fail unless every line and branch of the tools is tested (needs coverage.py)
python tools/tests/debug_case.py CODE   # plant a code's cases and show each report (--keep, --list, --build CODE)
```

`validate.py` checks encoding and line ends; that the root and domain folders hold only what "Layout" lists; the
registry files and `sources.csv`; INDEX tables against the registry; the research log (Round 0 to the latest, no
gaps, real dates, and the committed log kept unchanged as its tail, also across merges); hosted files against the
manifest and `.gitattributes`; extracted-data CSVs and the citation of every read source; revision candidates and
`upstream_commit_map.csv`; that every cited `extracted_data/` or `full_texts/` path exists; and rejected ids. It
only warns where the decision is the owner's (licence, file size, an `access_status` sha256 matching no hosted
file). `--upstream` checks cited commits and files in the sibling clones of the three upstream repos (fetch them
first).

Nothing fails silently: a malformed file stops its reader, a crashing check reports `check-crashed`, one that
examined nothing `nothing-checked`, and every finding carries a code. `tools/tests` plants a defect for every code in
a throwaway fixture repo and requires each report to hold exactly its code plus the codes it declares; it also
rejects swallowed exceptions and fallback idioms in the tools. Standard library and git only (coverage.py for
`measure_coverage.py`); Python 3.8+.

## Provenance

Rounds are logged in `RESEARCH_LOG.md`, newest first. Extraction was interactive and is not committed as scripts;
every extracted number records the page or table it came from so it can be re-checked.

## License

MIT, see [`LICENSE`](LICENSE), for this repository's own work (index, registry and tracking CSVs, FINDINGS,
`extracted_data/`, `tools/`). Files under `full_texts/` are third-party documents redistributed under the terms in
"Access rules"; each keeps the licence its `sources.csv` row identifies.
