# Domain 7 — Mission program-cost benchmarks

_NRE / development anchors for the `operational_costs.csv` rows that cite real NASA program costs._

### planetary_society_pebd_mission_costs [T3; open service] — The Planetary Society, "Planetary Exploration Budget Dataset," updated through the FY2026 request (Casey Dreier)

**The first registered anchor for all three NRE rows in operational_costs.csv.** Those rows cite real NASA program costs
(OSIRIS-REx spacecraft development $588.5M; Mars 2020/Perseverance autonomy stack ≈$150M of a ~$2.4B program; OSIRIS-REx UTTR sample-recovery ops) but none had been
registered or verified until this round. Pulled live from this machine on 2026-09-23: the full 80-sheet XLSX at
`docs.google.com/spreadsheets/d/12frTU...M/export?format=xlsx` (sha256=df737f5d3ea0...). Methodology per the Introduction sheet: values are **actual contractual obligations in millions of nominal dollars**; italic cells are estimates; data compiled from NASA budget estimates submitted to Congress 1961→present. Dataset terms require attribution to The Planetary Society (recorded, not a redistribution restriction — it is a public dataset).

Per-mission sheets carry `Official LCC` + fiscal-year rows split into Formulation / Implementation(incl LV) / Launch Vehicle(s) / Operations, with a Totals row and the dev/ops share. Key figures parsed from the live file (all deltas computed in code; see extracted_data/r48_pebd_mission_cost_key_numbers.csv):

| mission | Official LCC ($M) | Formulation+Implementation incl LV ($M) | Launch Vehicle(s) total ($M) | Operations obligations ($M) |
|---|---|---|---|---|
| OSIRIS-REx | **1,057.3** | 785.3 | **183.5** (exact match to our note) | 232.2 (FY2017–FY2026) |
| Mars Perseverance | **2,725.8** | **2,462.6** (= dev+launch; ≈ our '~$2.4B') | 243.0 | 517.1 (through FY2026) |

Audit against the three NRE rows:
- **'Spacecraft development (NRE)' — AGREE, EXACT.** Our note anchors on "OSIRIS-REx spacecraft development = $588.5M actual." PEBD's sum of Total Cost FY2011–FY2016 minus the Launch Vehicle total = **$588.5M to the decimal (delta 0.00%)**. The note's companion figure "$183.5M launch vehicle" is also exact. This row's value ($588.5M) and its low/high range are now backed by a live, re-queryable institutional dataset rather than an unregistered secondary citation.
- **'Autonomous mining control & AI (NRE)' — program-scale AGREE; subset NOT in PEBD.** Our note says "≈$150M of $2.4B program" for the autonomy stack. PEBD's Mars Perseverance dev+launch = **$2,462.6M**, i.e. our "~$2.4B program" is −2.5% (AGREE). But PEBD is mission-level only — it has no software/autonomy NRE line item, so the ~$150M subset figure remains a secondary citation; what IS now verified is the program total that ratio rests on.
- **'Sample recovery operations' — envelope anchored as projection-vs-final.** Our note derives its $15M/recovery OOM estimate from "the broader $283M / 9 yr operations envelope." PEBD's final OSIRIS-REx operations obligations (FY2017–FY2026) = **$232.2M**, i.e. the note's $283M was a pre-return projection, +21.9% above what was ultimately obligated. No source carries a standalone sample-recovery cost line (confirmed by sheet-structure inspection), so our row's own caveat ("NASA has not published a standalone recovery-ops figure") stands and is now backed.

### Round-48 status (domain 7)
Domain 7 established with its first T3 anchor — the mission-cost side of the pipeline, previously unanchored. The three NRE rows are now grounded in a live institutional dataset; two honest gaps recorded (no autonomy-stack line, no recovery-ops line in PEBD).

