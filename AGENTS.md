# Working in General_Research

This repo is the evidence registry behind economicspace, spacecost and
AsteroidCatalog. Those repos are **read-only from here**: a contradicting
source becomes a FINDINGS block plus a `revision_candidates.csv` row, never an
upstream edit. README.md explains the layout, tiers and access classes.

## Before every commit

```
python tools/build_registry.py   # regenerates sources.csv, fills manifest hashes
python tools/validate.py         # must exit 0
```

When a round re-checks revision candidates, also run `python tools/validate.py --upstream`
(fetch the sibling clones first). When you change anything under `tools/`, run
`python -m unittest discover -s tools/tests` and `python tools/tests/measure_coverage.py`:
every report code needs a planted-defect case, and every line and branch of the tools must be
reached, so a new place that reports an existing code needs its own case too. A case's report
must hold exactly its code and the codes it lists in `also`; list a code there only when the
planted defect really causes it, never to quiet a misfiring check. `python tools/tests/debug_case.py
CODE --keep` (or `--build CODE`) shows a case's report and keeps its planted repo. Fix a failing
check's cause; never add a fallback, skip or exception that lets the run pass around it. When a
new check fails on the data, decide whether the data or the check is wrong.

## Writing it down

- **FINDINGS.md: one block per round, facts only.** Give the source id, what it
  says (short verbatim quotes with page), the upstream cell and value it bears
  on, the verdict, any `rc-NNN`, and the extracted-data file. Leave out access
  narration (which routes failed, retries, user agents), round status
  summaries, and restatements of earlier blocks. Candidate texts live in
  the candidates files; a FINDINGS block lists the ids with a few words each.
- **The research log (`RESEARCH_LOG.md`) is append-at-top only.** Add one
  entry, `- **Round N** (YYYY-MM-DD): ...`, of one or two sentences above the
  previous one — that exact label, not `**RN**` or a heading. The details
  belong in FINDINGS. Never rewrite or reorder older entries; `validate.py`
  fails if the committed log is not kept as the tail. (The log was condensed
  once, on the owner's instruction, on 2026-10-18.)

## Rules (each one exists because it broke in a past round)

- **Edit `<domain>/sources_domain.csv`, never `sources.csv`.** The aggregate is
  generated; hand-appended rows landed outside their domain block in R42.
- **`access_status` starts with one of the seven classes** in README "Access
  classes", then how it was verified (`open_service`, not `open service`; a
  pulled-but-unhostable full text is `verified_live_not_pulled`).
  `full_text_hosted` needs the file in `full_texts/` *and* a manifest row
  (write `domain_dir,id,file,,,license`; the build fills `bytes,sha256`).
  `.gitattributes` marks `full_texts/` `-text` so `core.autocrlf` cannot
  change a hosted file's bytes. A `registered_not_pulled` row records an
  upstream citation not yet read; when you pull it, re-class it and say what you read.
- **Read the licence off the file or its record**: the PDF's own statement, the
  NTRS `copyright.determinationType`, or the arXiv abs page, never the journal's
  general policy or where the copy came from. arXiv's default licence, an
  author-homepage copy and "free to read" grant no right to redistribute (the
  2026-09-26 audit un-hosted 20 files hosted on those grounds).
- **INDEX.md domain tables list the same ids in the same order as
  `sources_domain.csv`**: append a new source to both. Header
  `| id | tier | source (short) | access | backs / could replace |`, five cells
  per row with a closing `|`, no blank line inside a table. Keep the access and
  backs cells short; detail goes in FINDINGS.
- **Extracted data lives in `<domain>/extracted_data/`**, never a root
  `extracted_data/`: FINDINGS paths are relative to the domain.
- **Write extracted-data CSVs with `csv.writer` on a file opened with
  `newline=''`**, never by joining strings. Use
  `source_id,item,value,unit,location_in_source,notes` where it fits. Every
  CSV needs a `source_id` column: blank only for the pipeline's own value or a
  comparison computed here, `a;b` for a row from two sources. A source no CSV
  cites needs "Context-only: <reason>" in its registry row.
- **Read tables by word coordinates, then check what you read.** The text
  stream mixed wrapped rows of carry2012 Table 3 (rc-006 was built on one and
  withdrawn) and swapped lac_bac_2024's insulation cases. Check each value
  against its row label and that totals add up.
- **Before un-hosting a file, extract every number the repo uses from it**, with
  page locations, and record the removed copy's size and sha256 in its
  `access_status` (a rejected source is the exception: its data is deleted).
- **A rejected source keeps one record: its row in INDEX.md "Rejected
  sources"** (`id`, `source`, `link`, `reason`). Only the owner rejects; README
  "Rejecting a source" lists what to delete, and `validate.py` fails if the id
  is named anywhere but the research log.
- **Record revision candidates.** A source contradicting an upstream cell gets a
  `revision_candidates.csv` row (next `rc-NNN` above the highest in either
  candidates file, status `open`) with the current upstream value and the
  commit read. On re-check, update `status`, `checked_against` and
  `checked_date` rather than adding a row. A row whose status is no longer
  `open` or `blocked` moves to the end of `revision_candidates_closed.csv` in
  the same commit; never delete one (upstream changelogs and code cite the ids).
- **IDs are permanent** and a rejected id is never reused. Write the full
  registry id everywhere (INDEX, FINDINGS, the log, `source_id`, candidates):
  `krishnan_2010` for `krishnan_2010_h2o2_rp1_upper_stage` broke a cross-reference.
