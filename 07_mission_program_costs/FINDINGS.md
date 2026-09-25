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
## Round 60 addition — IG-24-008 registered (+1 T2, hosted sha-verified): FIRST institutional source for sample-return program economics (Mars Sample Return)

**Context**: d7's anchors so far cover completed/operational missions (PEBD + IG-20-023 Table 2). The two remaining estimate rows in `operational_costs.csv` ('Sample recovery operations' $15M; 'Depot berthing & handover' $2M) both concern sample-return logistics. NASA OIG audit **IG-24-008** ('Audit of the Mars Sample Return Program', Feb 28, 2024) is the Agency's own institutional record of what a full sample-return program costs.

**MSR life-cycle cost trajectory — the institutional record for sample-return program economics.** p4 verbatim: "The trajectory of the MSR Program’s life-cycle cost estimate, which has grown from $2.5 to $3 billion in July 2020, to $6.2 billion at KDP-B in September 2022, to an unofficial estimate of $7.4 billion as of June 2023" Computed growth: **$2.5B -> $7.4B = +196.0%** over ~3 years (the report's own words, p28: "This figure is nearly three times NASA’s July 2020 cost estimate and more than double the amount estimated at Mission Concept Review."); intermediate step verbatim: "By Mission Concept Review in October 2020, the estimate had grown to $3.6 billion, and by KDP-B in September 2022 the estimate was revised to $6.2 billion".

**KDP-B range breach.** p8 verbatim: "the unofficial life-cycle cost estimate of $7.4 billion as of June 2023 is almost 20 percent above the top of the preliminary life-cycle cost estimate of $5.9 to $6.2 billion established in September 2022" — computed +19.4% above the $5.9–6.2B preliminary range top; an independent review (Sept 2023 IRB) recommended evaluating alternatives that "delay launch dates and could lead to cost estimates in the range of $8 to $11 billion".

**Congressional cost-control record.** p18 verbatim: "NASA requested $949.3 million for MSR, a 15.4 percent increase over its FY 2023 funding level"; and — "the Senate Appropriations Committee’s recommended funding level for FY 2024 was “not less than $300,000,000 for MSR,”" with a descope-or-cancel directive tied to the Decadal Survey's $5.3B profile (footnote 19). Institutional evidence that sample-return programs face hard congressional cost floors, relevant to any per-recovery or program-scale estimate in our tables.

**Scope notes — read before cross-comparing.** Footnote 33 verbatim: "MSR Program cost estimates do not include costs related to ESA investments or a future sample receiving facility"; footnote 19 on the Decadal Survey's $5.3B figure: it "includes an assumption of inflation at 2 percent which is far below actual inflation rates in the range of 5 to almost 9 percent from mid-2021 to early 2023", and "The Decadal Survey’s estimate also includes a sample receiving facility, which is not included in the MSR Program’s scope or cost estimates" — i.e. the two published program figures differ partly by SCOPE (receiving facility) and by inflation assumption, not just estimation vintage.

**Mars-side vs Earth-side recovery — do not conflate.** p28 verbatim: "A $180 million increase to provide two Sample Recovery Helicopters. Costs for a backup sample retrieval method were shifted from ESA to NASA when ESA’s fetch rover, initially planned for sample retrieval on the Martian surface, was removed in 2022 and replaced by two helicopters to be provided by NASA." These are MARS-surface retrieval assets (MSR's backup for the descoped ESA fetch rover). Our 'Sample recovery operations' row prices EARTH-side capsule search-and-recovery (modelled on OSIRIS-REx UTTR, Utah 2023) — a different scope entirely.

**Row-33 status re-checked**: IG-24-008 scanned end-to-end for any per-Earth-recovery figure — none exists in it (its cost discussion is program-level). The $15M OOM estimate therefore stands as written. Standing gap now spans ALL THREE institutional sources scanned to date: PEBD, IG-20-023, IG-24-008.

**Verdict**: no registered number changes. d7 now carries the complete institutional set for sample-return program economics (completed-mission LCCs + an in-formulation program's cost trajectory and its scope caveats). The per-Earth-recovery figure remains a standing gap.

## Round 62 addition — NASA FY 2027 Budget Estimates registered (+1 T2, hosted sha-verified): first institutional budget line whose stated scope includes sample recovery & transport; closes the row-33 'no published figure' gap at envelope level

**Source**: NASA HQ, *FY 2027 BUDGET ESTIMATES* (released Apr 2026), 384 pp., public-domain government work — hosted in full_texts/, sha-verified against two independent fresh pulls of the canonical nasa.gov URL and its ?emrc= variant (byte-identical, 19304ffc1317c018...).

**Why this source**: R59/R60 scanned PEBD, IG-20-023 and IG-24-008 end-to-end — none carries a per-recovery figure; row 33's note said 'NASA has not published a standalone recovery-ops figure'. This document is NASA's own budget justification: it funds, as an ENUMERATED activity of the Astromaterials Acquisition and Curation Office, exactly that operation.

**Verbatim scope statement (p159, count==1)** — from 'Activities conducted by the Curation office include:':
> SA control. Curation is an integral part of sample return missions. Activities conducted by the Curation office include: (1) research into advanced curation techniques to support future missions; (2) sample return mission planning; (3) archiving of witness, engineering, and reference materials related to sample return missions; (4) recovery and transport of returned materials; (5) initial characterization of newly 

**The funding line** (p158 table *Other Missions and Data Analysis*, Planetary Science Research section; header verbatim: 'Budget Authority (in $ millions)', columns FY2025..FY2031 with the two leftmost marked Enacted): extracted by word-coordinate column verification — value bands evenly spaced ~41pt, every row fills all five request-year bands exactly once:

| line | FY2027 req | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| **Astromaterial Curation** | **16.3** | 17.2 | 17.1 | 17.1 | 17.6 |
| Total Budget (section) | 165.3 | 182.8 | 189.2 | 190.7 | 194.8 |

(FY2025/FY2026 cells are '--' = enacted, no data for this forward-looking line. Curation is 9.9% of its parent section's FY2027 request — computed in code.)

**Timing context (p160, count==1)**:
> With the OSIRIS-REx mission ending in 2026, the Astromaterials Acquisition and Curation Office will complete the processing of returned samples from the Sample Analysis Team and continue global distribution of this precious material to the scientific community, expandin
— i.e. this line is POST-recovery: the Sept 2023 UTTR event that row 33 models has already happened; FY2027 funds ongoing curation including any future recovery/transport events (MSR capsule, MMX).

**Comparison vs our row 33 (`Sample recovery operations`, USD per recovery, centre $15M, range [5-30]M)**:
- Institutional FY2027 line = **$16.3M/yr**; our one-time event centre of $15M sits **-8.0% BELOW** the annual institutional line (computed in code), inside our [5-30] band.
- Verdict: **CONSISTENCY ANCHOR, not an exact pin** — anchor-honesty rule applied twice: NASA's scope is broader than a single recovery event (the line also funds curation labs, sample distribution and cleanroom storage across ten collections) and it is RECURRING budget authority rather than per-event cost. But the institutional number brackets our centre from above by only ~8% — directionally validated; **no revision forced**.
- The standing gap 'no published figure anywhere' (spanning PEBD + IG-20-023 + IG-24-008 after R59/R60) is now closed at ENVELOPE level: any future Earth-recovery event will draw on this line or its successor, and our $15M OOM centre sits inside it.

**Negative probe (criterion #2 completeness)**: 'APEX' count = **0** across all 384 pages; 'OSIRIS-' appears only in narrative — no OSIRIS-APEX extended-ops mission line item exists anywhere in this document, so the curation envelope cannot be conflated with an APEX budget.

**Mission-line context (same verified extraction method, d7 program-level reference)**: Psyche FY2027 $35.8M -> $41.9M (FY2031); Europa Clipper FY2027 $89.2M -> $187.7M (FY2031, operations ramp-up). Not anchors for existing rows — recorded so future d7 work has the full program table on file.
