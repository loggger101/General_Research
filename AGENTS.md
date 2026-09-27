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
- **`access_status` starts with one of the seven classes** in README "Access
  classes", followed by how it was verified (write `open_service`, not
  `open service`; a pulled-but-unhostable full text is `verified_live_not_pulled`). `full_text_hosted` needs the file
  in `full_texts/` *and* a row in `full_texts_manifest.csv` (write
  `domain_dir,id,file,,,license` and let the build fill `bytes,sha256`).
  A `registered_not_pulled` row (R74) records an upstream citation that has not
  been read; when you pull it, re-class it and say what you read.
- **Read the licence off the file or its record**: the PDF's own licence
  statement, the NTRS `copyright.determinationType`, or the arXiv abs page.
  Don't take it from the journal's general policy or from where the copy came
  from. arXiv's default licence, an author-homepage copy and "free to read" grant
  no right to redistribute. The 2026-09-26 audit found 20 hosted files hosted
  on those grounds, including one recorded as "CC BY per journal policy" whose
  PDF says "All rights reserved".
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
  Every extracted-data CSV needs a `source_id` column. Leave it blank only for
  the pipeline's own value or a comparison computed here, and write `a;b` for a
  row derived from two sources. A source that no CSV cites needs "Context-only:
  <reason>" in its registry row.
- **Read tables by word coordinates, then check what you read.** Taking numbers
  from the text stream mixed values between wrapped rows of carry2012 Table 3
  (a revision candidate, rc-006, was built on one and later withdrawn) and
  swapped the two insulation cases in lac_bac_2024. Check each value against its
  row label, and where a table has totals, check that they add up.
- **Before un-hosting a file, extract every number the repo uses from it**, with
  page locations, and record the removed copy's size and sha256 in its
  `access_status`. After removal nothing can be re-checked.
- **Record revision candidates.** When a source contradicts an upstream cell,
  add a `revision_candidates.csv` row (next `rc-NNN`, status `open`) with the
  current upstream value and the commit you read it from. When you re-check
  upstream and find it changed, update `status`, `checked_against` and
  `checked_date` rather than adding a new row.
- **IDs are permanent.** Use the registry id everywhere (INDEX, extracted-data
  `source_id`, candidates); do not abbreviate it in INDEX (`krishnan_2010` for
  `krishnan_2010_h2o2_rp1_upper_stage` broke the cross-reference).
