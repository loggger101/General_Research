# General Research

Peer-reviewed (and tiered-authoritative) sources for the **economicspace**
asteroid-mining profitability pipeline and its Stage 3 reference package
**spacecost**. Every source here is one that can actually be *accessed and
analyzed* — full text where legally redistributable, otherwise metadata +
abstract + extracted key tables.

## Why this repo exists

`economicspace/CITATIONS.md` records what the pipeline already cites (SBDB,
ssoBFT, NEOWISE V2.0, USGS/LME/yfinance prices, Izzo 2015 for Lambert). The
weakest-sourced cells of the model are exactly where peer-reviewed backing is
missing:

| weakness rank | domain | pipeline cell(s) it could back or replace |
|---|---|---|
| 1 | Bulk density by spectral type, PGM factors, population statistics | `catalog.py` per-type density/PGM; ranking quality |
| 2 | Composition → commodity value mapping (what an S/C/X/K/Q body actually contains) | `mineral_value.py` in-pipeline mineralogy, destination pricing |
| 3 | Δv budgets and propulsion performance tables | `spacecost/delta_v_segments.csv`, `propellants.csv` Isp rows |
| 4 | Launch $/kg to LEO/GTO — history and projections | `spacecost/launch_vehicles.csv` price rows, cost cascade |
| 5 | In-space storage (boil-off), ISRU, operational costs | `storage_systems.csv`, `operational_costs.csv`, environment penalties |

## Layout

```
README.md              This file: what it is and how to read it
INDEX.md               Master index — every source → tier, access status, pipeline mapping
sources.csv            Machine-readable registry of every item (one row per source)
01_density_and_population/   Domain 1: density by spectral type, PGM factors, population stats
02_composition_value/        Domain 2: composition → commodity value mapping
03_dv_propulsion/            Domain 3: Δv budgets, propulsion performance tables
04_launch_economics/         Domain 4: launch cost per kg — history and projections
05_inspace_operations/       Domain 5: storage/boil-off, ISRU, in-space operational costs

<domain>/full_texts/     Legally redistributable full texts (arXiv PDFs, NASA public-domain docs)
<domain>/extracted_data/ One CSV per source with the actual numbers pulled out of it
```

## Source tiers

- **T1** — Peer-reviewed journal articles.
- **T2** — NASA / ESA technical reports and AIAA / IAC proceedings (institutionally reviewed, not peer-reviewed in the journal sense).
- **T3** — Authoritative government or dataset publications with a DOI (e.g., USGS MCS, PDS releases, NEOWISE V2.0).

Each row of `sources.csv` carries its tier label explicitly.

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

1. It directly relates to one of the five domains above (i.e., it can back or
   replace a specific pipeline table/cell — "space mining is interesting" does
   not qualify).
2. Its access status was actually verified from this machine (a URL that 403s
   at search time but serves full text passes; one that only ever shows an
   abstract bar does not get `full_text_hosted`).
3. The numbers it carries were extracted into a CSV, or the item is recorded
   as context-only with the reason stated in `sources.csv`.

## Provenance of this process

Research rounds are logged at the bottom of `INDEX.md` (round number, date,
what was added). Extraction scripts live next to their domain so any number can
be re-derived from the committed full text.
