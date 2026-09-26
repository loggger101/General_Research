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

## Rules (each one exists because it broke in a past round)

- **Edit `<domain>/sources_domain.csv`, never `sources.csv`.** The aggregate is
  generated; hand-appended rows landed outside their domain block in R42.
- **`access_status` starts with one of the six classes** in README "Access
  classes", followed by how it was verified (write `open_service`, not
  `open service`; a pulled-but-unhostable full text is `verified_live_not_pulled`). `full_text_hosted` needs the file
  in `full_texts/` *and* a row in `full_texts_manifest.csv` (write
  `domain_dir,id,file` and let the build fill `bytes,sha256`).
- **INDEX.md domain tables list the same ids in the same order as
  `sources_domain.csv`**: a new source is appended to both. Every table uses
  the header `| id | tier | source (short) | access | backs / could replace |`,
  five cells per row with a closing `|`, and no blank line inside the table.
  (A blank line split the domain-6 table; 20 rows in domains 4 and 8–11 had
  only three cells, and domains 8–11 had three-column headers, which make
  GitHub drop any wider row's extra cells.)
- **The research log is append-at-top only.** Add one entry,
  `- **Round N** (YYYY-MM-DD): ...`, above the previous one — that exact label,
  not `**RN**` or a `### RN` heading. Never rewrite, trim or reorder older
  entries: R43's rewrite deleted Rounds 0–41 and R46's deleted R45 (all
  restored from git on 2026-09-26), and R53's commit claimed an entry it never
  wrote.
- **Extracted data lives in `<domain>/extracted_data/`**, never a root
  `extracted_data/`: FINDINGS paths are relative to the domain, so R47–R57's
  root-level files were unreachable until moved.
- **Write extracted-data CSVs with `csv.writer` on a file opened with
  `newline=''`**, never by joining strings: ten older files had unquoted commas
  that shifted cells, and R53's file had doubled carriage returns. Keep the
  `source_id,item,value,unit,location_in_source,notes` columns where they fit.
- **Record revision candidates.** When a source contradicts an upstream cell,
  add a `revision_candidates.csv` row (next `rc-NNN`, status `open`) with the
  current upstream value and the commit you read it from. When you re-check
  upstream and find it changed, update `status`, `checked_against` and
  `checked_date` rather than adding a new row.
- **IDs are permanent.** Use the registry id everywhere (INDEX, extracted-data
  `source_id`, candidates); do not abbreviate it in INDEX (`krishnan_2010` for
  `krishnan_2010_h2o2_rp1_upper_stage` broke the cross-reference).
