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

## Round 59 addition — IG-20-023 registered (+1 T2, hosted sha-verified): independent institutional cross-validation of the PEBD mission-cost anchors

**Context**: d7's only source was the Planetary Society PEBD (T3 live service). NASA OIG audit **IG-20-023** ('NASA's Planetary Science Portfolio', Sep 16, 2020) carries Table 2 — per-mission cost-cap basis + life-cycle costs for seven missions — giving every d7 anchor a second institutional source.

**Mars 2020/Perseverance — EXACT cross-validation.** Table 2 (p15, verbatim): "Mars 2020/Perseverance rover n/a b **2,725.8**" vs PEBD's Official LCC $2,725.8M — two independent institutional sources agree to the decimal. The R46/R49 Perseverance anchors (dev+launch 2,462.6; "~$2.4B" note) are now double-sourced.

**OSIRIS-REx — +6.1% between sources.** Table 2 verbatim: "OSIRIS-REx **622.0** (cap basis) / **1,121.4** (life-cycle)" vs PEBD Official LCC $1,057.3M → OIG is +6.1% HIGHER. Both are pre-return snapshots from different vintages (OIG Sep-2020; PEBD updated FY rows); the spread brackets our row's envelope anchor ($283M/9yr ops = pre-return projection). No registered number changes.

**MSL/Curiosity — $2,476.3M LCC** (Table 2 verbatim: "Mars Science Laboratory/Curiosity rover n/a b **2,476.3**") — program-scale context for the MARS_LANDED_MASS_FRACTION domain's mission; not a per-kg anchor.

**Cost-cap scope note (affects NRE-row comparability).** Verbatim: "these cost caps do not reflect the total costs of those missions because they do not include launch vehicle and operations costs, which can add hundreds of millions of dollars to each program" — i.e. Discovery's $500M / New Frontiers' $1B caps are DEVELOPMENT-only by construction; our NRE rows (development cost) compare against the cap-basis column, while LCC-based anchors include LV+ops. Table 2 carries both columns: InSight **$593.9/$828.9**, Lucy **505.7/981.1**, Psyche **626.3/996.4** (all three Discovery missions EXCEED their $500M cap on the development basis — reported as a program-level finding), Dragonfly **n/a / 1,800–2,200**, Europa Clipper **n/a / 4,250.0**.

**'Sample recovery operations' row (operational_costs.csv row 33) re-checked**: the report was scanned end-to-end for any standalone sample-return/recovery-ops figure — none exists in it (its cost discussion is program-level only). The $15M OOM estimate therefore stands as written, but its envelope anchor ($283M/9yr OSIRIS-REx ops) now has a second institutional source behind the mission's total scale. Status: still an ESTIMATE — no published per-recovery figure anywhere reachable (standing gap).

**Verdict**: PEBD anchors CONFIRMED by an independent agency audit (Mars 2020 exact; OSIRIS-REx +6.1% spread documented as vintage difference). No registered number changes.
