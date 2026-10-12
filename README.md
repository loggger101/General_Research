# General Research

Peer-reviewed (and tiered-authoritative) sources for the **economicspace**
asteroid-mining profitability pipeline, its Stage 3 reference package
**spacecost**, and the Stage 1 package **AsteroidCatalog**. Every source here
is one that can actually be *accessed and analyzed*: full text where legally
redistributable, otherwise metadata, abstract and extracted key tables.
Since Round 74 the registry also lists every source those three repos cite,
including the grey ones (tier T4), so each upstream dependency is visible
even before it has been read. The exceptions are sources the owner has
rejected, which are listed only under INDEX.md "Rejected sources".

## Why this repo exists

`economicspace/CITATIONS.md` records what the pipeline already cites (SBDB,
ssoBFT, NEOWISE V2.0, USGS/LME/yfinance prices, Izzo 2015 for Lambert). This
repo backs the cells that citation list leaves weakly sourced, one domain per
group of cells. Domains 1–5 were the weakest-sourced; the rest were added as
research rounds found cells no domain covered (the research log records
when). Each domain's FINDINGS.md lists its target cells, their current values
and what a source has to supply.

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
| 13 | Astrodynamics methods, ephemerides & audited software | economicspace `research/starred-repos/` (Lambert and Kepler solvers, ephemeris oracles, the 17-repository licence audit) |
| 14 | Propellant & consumable prices | `propellants.csv` `ref_cost_usd_per_kg` and its component prices |
| 15 | In-space demand & market absorption | economicspace `mineral_value.py` in-space utility, annual-demand and class-share tables; `calc.py` `demand_elasticity`, `surplus_price_fraction` |
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

## Layout

```
README.md                                This file: what it is and how to read it
INDEX.md                                 Master index: every source → tier, access, pipeline mapping; rejected sources and research log at the bottom
sources.csv                              Machine-readable registry, one row per source (GENERATED — see "Tools")
full_texts_manifest.csv                  Every hosted file → its source id, size, sha256 and licence
revision_candidates.csv                  Upstream cells the evidence says should change, with current status
upstream_commit_map.csv                  Upstream commits cited by checked_against that a history rewrite took off main, mapped to their main equivalents
DOWNLOADS.md                             Checklist of the non-hosted sources still to fetch for a full extraction, with exact links
AGENTS.md                                Working rules for agents running research rounds here
tools/                                   build_registry.py (regenerate derived files), validate.py (consistency checks) and tests/ (planted-defect tests of both, a coverage gate and a debug script)
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

<domain>/sources_domain.csv              The registry rows for that domain (the file you edit)
<domain>/FINDINGS.md                     Prose write-ups and per-number comparisons, one block per round
<domain>/full_texts/                     Legally redistributable full texts (arXiv PDFs, NASA public-domain docs, CC-BY articles)
<domain>/extracted_data/                 CSVs of the numbers pulled out of each source, with page/table locations
```

## Source tiers

- **T1** — Peer-reviewed journal articles.
- **T2** — NASA / ESA technical reports and AIAA / IAC proceedings (institutionally reviewed, not peer-reviewed in the journal sense).
- **T3** — Authoritative government or dataset publications with a DOI (e.g., USGS MCS, PDS releases, NEOWISE V2.0).
- **T4** — Secondary / grey sources that upstream rows cite: company documents and price pages, news reporting,
  encyclopedias, vendor or market-research posts, textbooks, software and market-data APIs (added in Round 74).
  A T4 row marks a cell whose evidence is weak; replacing it with a T1–T3 source is the usual next step.

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
| `registered_not_pulled` | an upstream citation registered so the dependency is visible; its DOI was checked against Crossref or its landing page against a live request, but the full text has not been sought and nothing is extracted. Re-class the row when it is pulled |

## Access rules (this repo is public)

1. Full texts are committed **only when legally redistributable**: arXiv
   preprints under their licenses, NASA/ESA documents in the public domain or
   CC-licensed, and journal articles that are genuinely open access with a
   license permitting redistribution. Each hosted file's licence is recorded
   in the `license` column of `full_texts_manifest.csv`, read from the file
   or its record (PDF licence statement, NTRS copyright determination, arXiv
   abs page). arXiv's default licence (`nonexclusive-distrib/1.0`) lets arXiv
   distribute a paper but does not let anyone else, so only CC-licensed arXiv
   versions qualify. `validate.py` warns on every hosted file whose licence
   does not permit redistribution.
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

A `registered_not_pulled` row is the one exception to 2 and 3: it records
that an upstream cell cites the source, and it moves to one of the other
classes when an extraction round reads it.

## Adding a domain

Open a domain when upstream cells have no domain behind them, not for a topic.
A new domain needs:

1. A folder `NN_short_name/` (the next two-digit number; lowercase letters,
   digits and underscores) with `sources_domain.csv` holding only the header
   line, and `FINDINGS.md` holding a title, a `Backings:` line naming the
   upstream files and cells, and a first block that tables those cells with
   their current values and the upstream commit they were read from.
2. A `## Domain N — title` section in INDEX.md, above `## Rejected sources`, with a
   `_Backings:_` line and the five-column table header and separator. A table
   with no rows is valid until a round registers a source.
3. A row in the domain table at the top of this file and a line in "Layout"
   (`validate.py` fails if a domain folder is not mentioned in this file).
4. A research-log entry for the round.

A source already registered in another domain moves to the new one when the
cells it backs are the new domain's (next section); otherwise the new domain's
FINDINGS.md refers to it by id.

## Moving a source between domains

Move a source when the cells its `pipeline_mapping` names belong to another
domain. Its id never changes. Round 77 set the procedure:

1. Move its row from one `sources_domain.csv` to the other, and its INDEX row
   to the end of the new domain's table.
2. `git mv` its hosted files (and change `domain_dir` in
   `full_texts_manifest.csv`) and every extracted-data CSV that cites only this
   source. A CSV that also cites sources staying behind stays where it is; if
   the moved row names it, write the path with the old domain's folder.
3. Append a block to the old domain's FINDINGS.md listing each moved id and
   the new paths of its files, and one to the new domain's saying what arrived
   and which old blocks hold its history. Older blocks and the research log
   stay as written, even where their relative paths no longer resolve.
4. Leave `domain_dir` in `revision_candidates.csv` alone: it names the
   FINDINGS.md that holds the write-up.

## Rejecting a source

The owner decides which sources are rejected. A rejected source leaves the
registry, and a row in INDEX.md "Rejected sources" becomes its only record:
`id`, `source` (authors, year, title), `link` (DOI or URL) and `reason` (why,
and in which round). No data from it is kept. The procedure, set 2026-09-28:

1. Add its row to "Rejected sources". The id stays reserved, so no new source
   may reuse it.
2. Delete its row from `<domain>/sources_domain.csv` and from its INDEX domain
   table.
3. `git rm` its hosted files and delete their `full_texts_manifest.csv` rows.
   The rule on extracting every number before un-hosting a file does not apply.
4. Delete every extracted-data CSV that cites only this source, and in CSVs
   shared with other sources delete each row that cites it, `a;b` rows
   included.
5. Delete its FINDINGS.md write-ups, its DOWNLOADS.md entry, and each mention
   of its id in other sources' registry rows and FINDINGS blocks. This is the
   one case where older FINDINGS blocks are edited.
6. Delete each revision candidate whose `source_ids` is this source alone. For
   one that also cites others, remove the id from `source_ids` and rewrite
   the evidence without it. A deleted `rc-NNN` number is not reused.
7. Leave past research-log entries as written, and add one naming the rejected
   id, the reason and any deleted `rc-NNN`.

`validate.py` fails if a rejected id is still registered, or if any file path
or any CSV or Markdown file other than the research log names it.

## Revision candidates

This repo never edits the pipeline repos. When a source contradicts a cell in
spacecost, AsteroidCatalog or economicspace, the finding goes into that
domain's `FINDINGS.md` and a row in `revision_candidates.csv`: target file and
row, current value, proposed change, evidence and status (`open`, `applied`,
`declined`, `superseded`, `blocked`, or `withdrawn` when this repo's own
evidence turns out to be wrong). Each row records the upstream commit its
current value was read from, so a stale status is visible. Re-check the open
rows against the upstream repos whenever they release.

## Tools

```
python tools/build_registry.py          # regenerate sources.csv; fill manifest sizes + hashes
python tools/build_registry.py --check  # fail if either is out of date
python tools/validate.py                # consistency checks; exit 1 on any error
python tools/validate.py --strict       # exit 1 on warnings too
python tools/validate.py --verbose      # also print how many items each check examined
python tools/validate.py --upstream     # also check cited commits in the sibling upstream clones
python -m unittest discover -s tools/tests   # the tools' own tests
python tools/tests/measure_coverage.py  # which lines and branches of the tools no test reaches (needs coverage.py)
python tools/tests/debug_case.py CODE   # plant one test case's defect and show the full report (--keep, --list)
```

`validate.py` checks:

- that every CSV, Markdown, JSON and Python file, and `.gitignore`, is UTF-8 with no byte-order mark, no stray carriage returns and a final newline;
- that the root and the domain folders hold only what "Layout" lists, that domains are numbered 01..N with no gap or repeat, and that `.gitignore` hides nothing but `__pycache__/` (a hidden file is invisible to every check);
- that every `sources_domain.csv` is rectangular with no empty or padded cell and a well-formed year, and that `sources.csv` matches them;
- that each INDEX.md table lists exactly its domain's sources in registry order, with five non-empty cells per row;
- that the research log runs from Round 0 to the latest with no gaps, real dates and no mislabelled entries, and that the committed log survives unchanged as its tail (entries are only ever added at the top; this compares with HEAD, so it catches a rewrite before it is committed);
- that every hosted file is in the manifest with the right hash and a licence;
- that every extracted-data CSV is rectangular, has a `source_id` column and cites registered ids, that every JSON file parses, and that every read source is cited by an extracted-data file of its domain or marked "Context-only: <reason>";
- that `revision_candidates.csv` uses known statuses, sources, repos and dates, that a candidate names its upstream file (only a `method` candidate may name a model stage instead), that open and blocked candidates were checked against their own target repo, and that `upstream_commit_map.csv` agrees with it and holds no unused row;
- that no rejected source is still registered or named anywhere but the research log.

It warns, without failing, only where the decision is the owner's: hosted files
whose licence does not permit redistribution, files over GitHub's 50 MB warning
size, and an `access_status` sha256 that matches none of the source's hosted
files (it may record an earlier, removed copy). `registered_not_pulled` rows are
exempt from the citation check and counted in the summary line instead.
`--upstream` reads the clones of AsteroidCatalog, spacecost and economicspace
next to this repo. It checks that every commit a candidate cites exists, that
the file it names exists there, that open and blocked candidates were checked
against `origin/main`, and that an off-main commit on a closed candidate has a
row in `upstream_commit_map.csv` whose commits have identical trees, whose
`tree` and `subject` columns are right and whose old commit is really off main.
`--verbose` names the `origin/main` commit of each clone it compared with; fetch
the clones first.

Nothing fails silently. The readers stop on a malformed file instead of reading
around it. A check that crashes is reported as `check-crashed`, one that
examined nothing as `nothing-checked`, and git that cannot be run as
`git-unavailable`. Every finding carries a code. When a file another check
depends on is unreadable, that failure is reported and the dependent
cross-checks are skipped rather than reported a second time as false errors.

`tools/tests` builds a throwaway fixture repository (with sibling upstream
clones), plants a defect for every code (one case for each place that reports
it) and fails if a code has no case. It also checks that valid variants pass
(CRLF line ends, a lazy-continuation paragraph in a log entry, a blank
`source_id`), that no planted defect crashes a check, that every check function
is registered, and that the tools hold no `except` that swallows an error and
none of the fallback idioms that hid defects here before (`dict.get` with a
default, `hasattr`, `utf-8-sig`, `errors="replace"`). `measure_coverage.py`
runs the suite under coverage.py and fails unless every line and branch of the
three tools is reached; run it after changing `tools/`. Standard library and
git only (coverage.py for `measure_coverage.py` alone); Python 3.8+.

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
