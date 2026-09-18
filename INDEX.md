# Master Index — General Research

Every source in this repo, what tier it is, how much of it we can actually use,
and which pipeline table/cell it backs or could replace. `sources.csv` holds the
same data machine-readable; this file adds the prose.

Legend for **access**:
- `full text hosted` — full PDF committed under `<domain>/full_texts/`, legally redistributable.
- `metadata + abstract` — paywalled/closed; bibliographic record and published abstract only, with any extractable key tables in `extracted_data/`.
- `open (not yet pulled)` — verified accessible at search time but not yet downloaded this round.

## Domain 1 — Density by spectral type, PGM factors, population statistics

_Backings: `catalog.py` per-spectral-type density and PGM factors; ranking quality of the whole pipeline._

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| — round 1 in progress — |||||

## Domain 2 — Composition → commodity value mapping

_Backings: `mineral_value.py` in-pipeline mineralogy, destination pricing._

_(rounds pending)_

## Domain 3 — Δv budgets and propulsion performance tables

_Backings: `spacecost/delta_v_segments.csv`, Isp rows of `propellants.csv`._

_(rounds pending)_

## Domain 4 — Launch cost per kg (history, projections)

_Backings: price rows of `spacecost/launch_vehicles.csv`; the Stage 4 cost cascade._

_(rounds pending)_

## Domain 5 — In-space storage / ISRU / operational costs

_Backings: `storage_systems.csv`, `operational_costs.csv`, environment penalties._

_(rounds pending)_

---
## Research log

- **Round 0** (2026-09-17): repo scaffolded; domains, tiers and access rules defined. No sources yet.
