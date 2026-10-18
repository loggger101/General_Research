# Domain 7 — Mission program-cost benchmarks

Backings: spacecost `operational_costs.csv` NRE rows (`Spacecraft development (NRE)`, `Autonomous mining control & AI (NRE)`) and the `Sample recovery operations` envelope, which cite real NASA programme costs.

## R48 - planetary_society_pebd_mission_costs [T3; open service]

The Planetary Society's Planetary Exploration Budget Dataset (Casey Dreier), pulled as XLSX on 2026-09-23 (80 sheets then). Values are actual obligations in millions of nominal dollars, italic cells estimates, from NASA budget submissions since 1961; terms require attribution. `extracted_data/r48_pebd_mission_cost_key_numbers.csv`.

| mission | Official LCC ($M) | Formulation+Implementation incl LV ($M) | Launch Vehicle(s) total ($M) | Operations obligations ($M) |
|---|---|---|---|---|
| OSIRIS-REx | 1,057.3 | 785.3 | 183.5 | 232.2 (FY2017–FY2025) |
| Mars Perseverance | 2,725.8 | 2,462.6 | 243.0 | 517.1 (through FY2025) |

- **Spacecraft development (NRE):** OSIRIS-REx FY2011-FY2016 total cost minus launch vehicle = $588.5M, matching the note to the decimal; its "$183.5M launch vehicle" also matches.
- **Autonomous mining control & AI (NRE):** the note's "~$2.4B program" vs Perseverance dev+launch $2,462.6M (-2.5%). PEBD has no software line, so the ~$150M autonomy subset stays secondary.
- **Sample recovery operations:** the note's "$283M / 9 yr" envelope was a pre-return projection; final operations obligations were $232.2M (+21.9% over). No source has a standalone recovery-cost line.

## Round 59 - OIG IG-20-023 cross-validates PEBD (hosted)

NASA OIG "NASA's Planetary Science Portfolio" (2020-09-16), Table 2 (p15): Perseverance LCC 2,725.8 (exact match with PEBD); OSIRIS-REx 622.0 cap basis / 1,121.4 LCC (+6.1% vs PEBD, a vintage difference); MSL 2,476.3. "these cost caps do not reflect the total costs of those missions because they do not include launch vehicle and operations costs": NRE rows compare to the cap basis. InSight 593.9/828.9, Lucy 505.7/981.1, Psyche 626.3/996.4 (all three above the $500M Discovery cap), Dragonfly n/a / 1,800–2,200, Europa Clipper n/a / 4,250.0. No per-recovery figure.

## Round 60 - OIG IG-24-008: Mars Sample Return programme economics (hosted)

"Audit of the Mars Sample Return Program" (2024-02-28):

- p4: life-cycle estimate grew "from $2.5 to $3 billion in July 2020, to $6.2 billion at KDP-B in September 2022, to an unofficial estimate of $7.4 billion as of June 2023" (+196%; "nearly three times NASA’s July 2020 cost estimate"); $3.6 billion at MCR (October 2020).
- p8: $7.4 billion is "almost 20 percent above the top of the preliminary life-cycle cost estimate of $5.9 to $6.2 billion"; the Sept 2023 review saw alternatives "in the range of $8 to $11 billion".
- p18: FY2024 request $949.3 million (+15.4%); Senate committee "not less than $300,000,000 for MSR".
- Scope: estimates exclude ESA investments and a sample receiving facility (fn 33); the Decadal Survey's $5.3B assumed 2% inflation against actual 5 to almost 9% and includes the receiving facility (fn 19).
- p28: "A $180 million increase to provide two Sample Recovery Helicopters": Mars-surface retrieval, not the Earth-side recovery the row prices.

No per-Earth-recovery figure.

## Round 62 - NASA FY2027 Budget Estimates (hosted)

384 pp, April 2026. p159 lists Curation office activities including "(4) recovery and transport of returned materials". p158 *Other Missions and Data Analysis* (Budget Authority, $M):

| line | FY2027 req | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Astromaterial Curation | 16.3 | 17.2 | 17.1 | 17.1 | 17.6 |
| Total Budget (section) | 165.3 | 182.8 | 189.2 | 190.7 | 194.8 |

Curation is 9.9% of its section. p160: with OSIRIS-REx ending in 2026 the office completes sample processing and distribution. The $15M per-recovery centre sits 8.0% below the $16.3M annual line, inside [5-30]M: a consistency anchor (the line is broader and recurring). No OSIRIS-APEX line exists ("APEX" occurs 0 times). Psyche FY2027 $35.8M -> $41.9M (FY2031); Europa Clipper $89.2M -> $187.7M.

## R70 - Full extraction (2026-09-27)

Files in `extracted_data/`: `r70_nasa_fy2027_budget_all_budget_authority_lines.csv` (444), `r70_nasa_fy2027_budget_development_cost_commitments.csv` (9), `r70_nasa_fy2027_budget_development_cost_details_by_element.csv` (55), `r70_nasa_fy2027_budget_funds_distribution_by_center.csv` (100), `r70_nasa_oig_2020_ig-20-023_appendix_b_mission_lifecycle_costs.csv` (21), `r70_nasa_oig_2020_ig-20-023_planetary_science_portfolio.csv` (16), `r70_nasa_oig_2020_ig-20-023_table1_psd_budget_by_program.csv` (9), `r70_nasa_oig_2024_ig-24-008_mars_sample_return_audit.csv` (11), `r70_nasa_oig_2024_ig-24-008_table1_msr_milestones.csv` (10), `r70_nasa_oig_2024_ig-24-008_table4_funding_fy2021_2024.csv` (10).

- FY2027 budget: every "Total Budget" equals its lines (0 mismatches); agency request $18,829.1M; centre funds sum to it. Development commitments: Orion $6,768.4M -> $10,171.8M (+50.3%); Roman $2,898M -> $3,038M; NEO Surveyor $1,228.6M -> $1,208.3M; US Deorbit Vehicle $1,042.7M; HLS Initial Capability $2,338.9M; X-59 $709.2M -> $766.9M; GRACE-C, MUSE, SEP.
- IG-20-023 Appendix B: e.g. DART $314M, Lucy $981M, Psyche $996M, Europa Clipper $4.3B, MRO $1.0B, New Horizons $720M. Table 1 FY2021 rows sum to 2,659.1 vs printed 2,659.6 (kept as printed).
- IG-24-008: milestone slips, FY2021-2024 funding; CCRS mass allocation 500 -> 625 kg; ERO mass margin 5.6% vs 10%.

## R72 - FY2027 MPAR summary table (2026-09-27)

`r72_nasa_fy2027_mpar_summary_table.csv` (13 projects over $250M, as of 2026-02-27). Orion +9.4% against the 2021 rebaseline ($9,301.2M -> $10,174.4M) vs +50.3% against the 2015 baseline in its section; kept as printed where the table and sections differ: Roman base year 2020, JCL 78%, $3,120.2M (+7.7%) vs 2021, >70%, $3,038M (+5%); SEP $223.2M vs "TBD"; HLS IC $2,339.0M vs $2,338.9M; X-59 absent from the table.

## R73 - Full extraction of the PEBD workbook (2026-09-27)

Re-pulled (137 sheets; last update 2025-11-13). Every cell in long form with italic (estimate) and bold (programme line) flags: `r73_pebd_budget_history.csv` (482), `r73_pebd_consistency_checks.csv` (102), `r73_pebd_decadal_totals.csv` (224), `r73_pebd_fiscal_year_sheets.csv` (6,248), `r73_pebd_funding_by_destination.csv` (1,319), `r73_pebd_key_numbers.csv` (33), `r73_pebd_major_programs.csv` (1,135), `r73_pebd_mission_costs_sheet.csv` (823), `r73_pebd_per_mission_sheets.csv` (4,286), `r73_pebd_reference_indices.csv` (637), `r73_pebd_timeline.csv` (575).

- Conventions: USD millions, nominal obligations unless headed inflation-adjusted (2025 dollars, NNSI; NAICS ECI for operations after 2000).
- Checks: 40 of 54 sheets with a Totals row match their fiscal-year sums; the 27 mismatching columns are in the consistency file. In the 'Mission Costs' summary, development + launch + operations ≠ total for 6 of 51 missions and annual rows ≠ total for 13. All kept as printed.
- R48 corrections: the FY2011-FY2016 Total Cost sum is 772.0 (not 955.5; 772.0 - 183.5 = 588.5 holds) and Perseverance operations (517.1) run through FY2025 (FY2026 request 67.9 outside).
- **rc-047:** the 'Mission operations' anchor "$283M over 9 yr = $31.4M/yr" vs final obligations $210.0M over FY2017-FY2023 ($30.0M/yr) and $232.2M through FY2025 ($25.8M/yr); the value is within 5% of the prime rate, so only the note changes. The summary sheet's $153.1M disagrees with the mission sheet.
- Small-body anchors (LCC; dev+launch / ops / total, $M): NEAR 220.5; 168.4 / 61.9 / 230.3. Dawn 472; 373 / 129.1 / 502.1. Psyche 975.7; 929.2 / 46.5 / 975.7. Lucy 989.1; 674.5 / 93.4 / 989.1. DART 315.4; 308 / 18.3 / 326.3. NEO Surveyor 1,595.1; 1,336.7 / 103.2 / 1,439.9.

## R74 / R77 - Cost models registered, then moved

`aerospace_corp_small_satellite_cost_model` and `nasa_instrument_cost_model_nicm` (the recurring $/kg bracket) were registered in R74 and moved to domain 21 in R77 (no files).

## R136 - Mission-cost anchors beyond PEBD and OIG (2026-10-08)

- **drake_2008_mars_dra5_study_executive_summary** (hosted; the executive deck of DRA 5.0, distinct from d03's `dra5_2009_human_exploration_of_mars`): slide 10 (rotated page, unambiguous pairs only): IMLEO 1,252 t chemical vs 825 t NTR; Ares V cargo launches 10-12 vs 7-9 "on 30-day centers".
- **sparx_2026_sdt_report_lunar_sample_return_baseline_cost** (420 pp; copyright material, read only): baseline $840M FY25 incl. reserves (rover $543M, instruments $137M at $25M x 5, operations $160M), "well below the TOR recommended cap of $1.5B"; CLPS lander ~$200M; Team-X sample-return link/ERV/SRC/ops $716M FY25$; ~$700M per robotic sample-return mission; $2B-$4B for 10-20 landers.
- **kremic_hurford_mandell_arnold_2015_out_of_this_world_science_down_to_earth_prices** (poster, hosted): image-only, unread.

`extracted_data/r136_mission_cost_key_numbers.csv`.

## R144 - GAO-26-108556 major-projects assessment (hosted)

`gao_2026_assessments_of_major_projects`, July 2026, 119 pp: 36 projects over $250M, "at least $70 billion" in LCCs (p2); cumulative cost growth +~$311M, $4.4B -> $4.7B, "Increased Slightly" (PDF p26); Dragonfly within $3.4B with ~$216M of HQ-held funding (April 2026) for a July 2028 launch, 82% of drawings released at CDR vs the 90% practice (PDF p73-74); Psyche +~$132M after a one-year delay, cascading >=3 years to VERITAS (PDF p43). Growth and reserve-pressure context; PEBD stays the pin. `extracted_data/r144_gao_major_projects_key_numbers.csv`.

## R163 - The sample-recovery note still cites the pre-return plan (rc-092; 2026-10-14)

rc-047 (applied in spacecost 0.5.2) fixed the Mission operations note with PEBD actuals ($210.0M FY2017-FY2023; $232.2M through FY2025; `extracted_data/r73_pebd_per_mission_sheets.csv`), but the 'Sample recovery operations' row still derives its $15M from "$283M / 9 yr" at spacecost@0b716ad. rc-092 (wording) carries the correction across.

## R164 - Candidate (2026-10-14)

rc-106: cite PEBD for the Perseverance programme figure and mark the $150M autonomy figure unsourced. Text in `revision_candidates.csv`.
