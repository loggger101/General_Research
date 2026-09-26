# General Research

Peer-reviewed (and tiered-authoritative) sources for the **economicspace**
asteroid-mining profitability pipeline, its Stage 3 reference package
**spacecost**, and the Stage 1 package **AsteroidCatalog**. Every source here
is one that can actually be *accessed and analyzed*: full text where legally
redistributable, otherwise metadata, abstract and extracted key tables.

## Why this repo exists

`economicspace/CITATIONS.md` records what the pipeline already cites (SBDB,
ssoBFT, NEOWISE V2.0, USGS/LME/yfinance prices, Izzo 2015 for Lambert). The
weakest-sourced cells of the model are exactly where peer-reviewed backing is
missing:

Domains 1–5 were ranked by how weakly sourced their cells were; 6–11 were
added later, in the order the research rounds found the next gap.

| # | domain | pipeline cell(s) it could back or replace |
|---|---|---|
| 1 | Bulk density by spectral type, PGM factors, population statistics | AsteroidCatalog `taxonomy_composition.csv` density/PGM columns; ranking quality |
| 2 | Composition → commodity value mapping (what an S/C/X/K/Q body actually contains) | `taxonomy_composition.csv` material fractions, `mineral_value.py` mineralogy |
| 3 | Δv budgets and propulsion performance tables | `spacecost/reference/delta_v_segments.csv`, `propellants.csv` Isp rows |
| 4 | Launch $/kg to LEO/GTO — history and projections | `spacecost/reference/launch_vehicles.csv` price rows, cost cascade |
| 5 | In-space storage (boil-off), ISRU, operational costs | `storage_systems.csv`, `operational_costs.csv`, environment penalties |
| 6 | Commodity market prices (the value side) | `mineral_value.py` `ref_price_usd_per_kg`, which feeds every profitability row |
| 7 | Mission program-cost benchmarks (NRE / development) | `operational_costs.csv` NRE rows (spacecraft development, autonomous mining control), sample-recovery ops envelope |
| 8 | NEA accessibility oracles (round-trip Δv ground truth) | distribution/rank reference for the NEA rows of `delta_v_segments.csv` (economicspace `probe_nhats.py`) |
| 9 | In-space delivery mass fractions & EDL survival | spacecost `delivery.py` constants such as `MARS_LANDED_MASS_FRACTION` |
| 10 | Launch vehicle & engine hardware / propellant performance | engine-level ground truth for `propellants.csv` and `launch_vehicles.csv` |
| 11 | Spacecraft power & electric propulsion | power and electric-propulsion rows of `operational_costs.csv` |

## Layout

```
README.md                                This file: what it is and how to read it
INDEX.md                                 Master index: every source → tier, access, pipeline mapping; research log at the bottom
sources.csv                              Machine-readable registry, one row per source (GENERATED — see "Tools")
full_texts_manifest.csv                  Every hosted file → its source id, size and sha256
revision_candidates.csv                  Upstream cells the evidence says should change, with current status
AGENTS.md                                Working rules for agents running research rounds here
tools/                                   build_registry.py (regenerate derived files) and validate.py (consistency checks)
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

<domain>/sources_domain.csv              The registry rows for that domain (the file you edit)
<domain>/FINDINGS.md                     Prose write-ups and per-number comparisons, one block per round
<domain>/full_texts/                     Legally redistributable full texts (arXiv PDFs, NASA public-domain docs, CC-BY articles)
<domain>/extracted_data/                 CSVs of the numbers pulled out of each source, with page/table locations
```

## Source tiers

- **T1** — Peer-reviewed journal articles.
- **T2** — NASA / ESA technical reports and AIAA / IAC proceedings (institutionally reviewed, not peer-reviewed in the journal sense).
- **T3** — Authoritative government or dataset publications with a DOI (e.g., USGS MCS, PDS releases, NEOWISE V2.0).

Each row of `sources.csv` carries its tier label explicitly.

## Access classes

The first word of every `access_status` is one of these; the rest of the field
says how it was verified or why it could not be.

| class | meaning |
|---|---|
| `full_text_hosted` | full text committed under `<domain>/full_texts/` and listed in `full_texts_manifest.csv` |
| `public_domain_excerpt_hosted` | public-domain document too large to commit; the relevant passage is quoted in `FINDINGS.md` |
| `verified_live_not_pulled` | fetched and read from this machine, but not committed |
| `open_not_pulled` | open access, but the publisher blocks this machine or the licence forbids hosting; metadata + abstract recorded |
| `open_service` | a live database or API, verified from this machine; derived numbers committed, not the service itself |
| `skipped` | deliberately not hosted; the user decision is recorded in the row |

## Access rules (this repo is public)

1. Full texts are committed **only when legally redistributable**: arXiv
   preprints under their licenses, NASA/ESA documents in the public domain or
   CC-licensed, and journal articles that are genuinely open access with a
   license permitting redistribution.
2. Paywalled items get: full metadata, abstract (as published), and any key
   tables/numbers extractable from the accessible portion — recorded in
   `extracted_data/` with page/table references so they can be verified later.
3. Every extracted number carries its source id + location (page / table) so a
   claim downstream is traceable to the paper, not to this repo's summary.

## How an item earns a place here

A candidate must satisfy all of:

1. It directly relates to one of the domains above (i.e., it can back or
   replace a specific pipeline table/cell — "space mining is interesting" does
   not qualify).
2. Its access status was actually verified from this machine (a URL that 403s
   at search time but serves full text passes; one that only ever shows an
   abstract bar does not get `full_text_hosted`).
3. The numbers it carries were extracted into a CSV, or the item is recorded
   as context-only with the reason stated in `sources.csv`.

## Revision candidates

This repo never edits the pipeline repos. When a source contradicts a cell in
spacecost, AsteroidCatalog or economicspace, the finding goes into that
domain's `FINDINGS.md` and a row in `revision_candidates.csv`: target file and
row, current value, proposed change, evidence and status (`open`, `applied`,
`declined`, `superseded`, `blocked`). Each row records the upstream commit its
current value was read from, so a stale status is visible. Re-check the open
rows against the upstream repos whenever they release.

## Tools

```
python tools/build_registry.py          # regenerate sources.csv; fill manifest sizes + hashes
python tools/build_registry.py --check  # fail if either is out of date
python tools/validate.py                # consistency checks; exit 1 on any error
```

`validate.py` checks that `sources.csv` matches the per-domain files, that each
INDEX.md table lists exactly its domain's sources in registry order with five
cells per row, that the research log runs from Round 0 to the latest with no
gaps, that every hosted file is in the manifest with the right hash, that every
extracted-data CSV is rectangular and cites registered ids, and that
`revision_candidates.csv` uses known statuses and sources. Standard library
only; Python 3.8+.

## Provenance of this process

Research rounds are logged at the bottom of `INDEX.md` (round number, date,
what was added), newest first. Extraction was done interactively during each
round and is not committed as scripts. Instead, every extracted number records
the page or table it came from, so it can be re-checked against the hosted full
text or the publisher's copy.

## License

MIT, see [`LICENSE`](LICENSE). That covers this repository's own work: the
index, the registry and tracking CSVs, the `FINDINGS.md` write-ups, the
records in `extracted_data/` and the scripts in `tools/`. It does not cover the
documents committed under `full_texts/`. Those are third-party papers and
reports redistributed under the terms set out in "Access rules" above, and
each keeps the license its row in `sources.csv` identifies.
