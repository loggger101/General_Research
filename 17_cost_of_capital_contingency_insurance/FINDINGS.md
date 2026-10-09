# Domain 17 — Cost of capital, contingency & insurance

Backings: spacecost `reference/operational_costs.csv` rows `Cost of capital (WACC)`, `Contingency reserve`, `Launch insurance` and `Third-party liability insurance`, and economicspace `modules/calc.py` `contingency_fraction`, `apply_wacc_compounding` and `charge_insurance`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

These are the financing and risk-transfer lines of the cost cascade. Their three sources so far sit in domain 5, and the contingency figure has none. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Cost of capital (WACC)` | 0.10 [0.075, 0.15] per year | Boeing 7.5% and Howmet 8.3% (ValueInvesting.io 2026) as the industrial floor; a "startup risk premium to ~10-15%" attributed to Damodaran's industry tables |
| `Contingency reserve` and `calc.py` `contingency_fraction` | 20% [15, 50] of total mission cost; applied after every other line and before WACC | "Industry-standard; first-of-kind missions carry the upper end"; no source |
| `calc.py` `apply_wacc_compounding` | False since v1.22.0 (compounded up-front costs over `mission_duration_yr`) | scope decision: "a discount rate is a statement about whose money this is" |
| `Launch insurance` | 10% [5, 15] of launch + payload value | Gallagher "Plane Talking" Q1 2024: ~6% in early 2023, ~10% after the Intelsat 33e loss |
| `Third-party liability insurance` | $1.5M [0.5M, 3M] per launch | the statutory MPL caps are cited; the premium figure has no source |
| `calc.py` `charge_insurance` | False since v1.20.0 | scope decision |

**What a source has to supply.**

- Discount rates and required returns actually used for early-stage space ventures and remote mining projects, so the 10-15% premium has a basis.
- Historical cost growth of planetary and first-of-kind missions, and agency reserve policy, to size the contingency line and its range.
- Space insurance premium rates by vehicle maturity and loss history.
- Premium levels for third-party liability cover on launch and re-entry.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `damodaran_cost_of_capital_by_industry` (domain 5): industry WACC tables.
- `valueinvesting_io_2026_boeing_howmet_wacc` (domain 5): the industrial WACC floor.
- `gallagher_plane_talking_space_market_updates` (domain 5): the launch-insurance rate.

**Boundary.** Domain 18 holds the regulatory requirement (the licence and how the MPL is set); this domain holds what the cover and the capital cost. Reliability, which insurance does not replace, is domain 16.

## R77 - Sources moved in (2026-09-27; registry unchanged at 267)

These rows were registered in other domains before this one existed; they moved here because the cells they back are this domain's. Their earlier write-ups stay in the old domain's FINDINGS.md under the blocks named.

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `damodaran_cost_of_capital_by_industry` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 44 addition | `extracted_data/r47_damodaran_cost_of_capital_key_numbers.csv`, `extracted_data/r47_damodaran_cost_of_capital_full_table_96_industries.csv` |
| `valueinvesting_io_2026_boeing_howmet_wacc` | domain 5 | `05_inspace_operations/FINDINGS.md`: R74 | none |
| `gallagher_plane_talking_space_market_updates` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 44 addition; Round 57 addition | `extracted_data/r57_plane_talking_series_key_numbers.csv` |

Revision candidates on these sources, written up in their old domains: rc-031 (open, Launch insurance).

The cross-references to `damodaran_cost_of_capital_by_industry`, `valueinvesting_io_2026_boeing_howmet_wacc`, `gallagher_plane_talking_space_market_updates` in the opening block are now rows of this domain.
## R89 - The MPL methodology behind 'Third-party liability insurance' gets its primary source pair (2026-09-30; registry 315 -> 317)

**faa_2017_report_to_congress_updated_mpl_method** [T3, full_text_hosted] - FAA Office of Commercial Space Transportation, "Report to Congress: FAA's Development of an Updated Maximum Probable Loss Method" (April 21 2017; CSLCA PL 114-90 Sec. 102 mandate), pulled live from faa.gov (work of the U.S. government). This is **the primary source for how our 'Third-party liability insurance' row's per-license MPL amount is actually computed**: risk profile method adopted April 2015 (replacing the early-1990s overlay method), probability thresholds 1-in-10,000,000 third-party / 1-in-100,000 government property ('10-7/10-5', p20), three-element calculation = casualties x cost-of-casualty + property damage, and **cost of a casualty fixed at $3 million since the first issued license in 1988** (p14/p17) - with FAA's own record that STPI was contracted in fall 2015 to reassess it and 'STPI's research suggested that the FAA should adjust its cost of casualty value upward, to approximately double its current value. The FAA is currently reviewing the study' (p17).

**gao_2018_commercial_space_launch_insurance_mpl_methodology** [T3, registered_not_pulled] - GAO-18-57 "Commercial Space Launch Insurance: FAA Needs to Fully Address Mandated Requirements" (Jan 16 2018), the independent assessment CRS R48582 cites. gao.gov is Akamai-blocked from this machine (verified with full browser headers; wayback unreachable too) so it stays registered-not-pulled, but its key figures were extracted verbatim from GAO's own product-page summary text: the same 1-in-10M / 1-in-100k thresholds, the $3M cost-of-casualty (with 'not doing so could understate the amount of insurance launch companies are required to purchase'), the property-damage factor change **50% -> 25%** of casualty cost, and - most usefully for this repo - the federal indemnification cap above MPL estimated at **$3.1 billion in 2017 (= $1.5B in 1988)**: that is the provenance of CRS R48582's '$1.5B in 1989 dollars' figure, which was previously unattributed. Four recommendations to FAA (re-examine probability thresholds; analyze direct cost impact incl. premiums + indemnification liability; consult industry/insurers on the updated casualty value; set a completion date for per-scenario MPL guidance); DOT concurred.

**No re-pin proposed**: statutory caps in our rows are unchanged by either source ($500M third-party / $100M USG remain as R87 recorded from CRS). What this pair adds is the methodology context: per-license MPL values - and hence required insurance coverage for a specific trajectory - track vehicle-specific casualty/property risk profiles at 10-7/10-5 probability levels, with a casualty value an independent study recommended doubling. Extracted data: `extracted_data/r89_mpl_methodology_key_numbers.csv` (10 rows). rc-031 (Launch insurance wording) is unaffected - it concerns the 2023 rate-reset attribution, not MPL.

## R108 - Contingency reserve + venture cost-of-capital get their first institutional sources (2 NTRS T2 hosted)

The two d17 cells that had no source at all in the R75 brief: `Contingency reserve` ('Industry-standard; first-of-kind missions carry the upper end'; **no source**) and the venture-level basis of `Cost of capital (WACC)` (industrial floor only). Both now have institutional sources, both NTRS T2 full_text_hosted.

| cell | current value | R108 backing |
|---|---|---|
| `Contingency reserve` + calc.py `contingency_fraction` | 20% [15, 50] of total mission cost; applied last | whitley_shinn_2012_economics_nasa_mission_cost_reserves - first empirical study of what happens to reserves. CADRe data set: "within our data set, only one mission had total cost increase within the value of the reserves reported at PDR. All twelve other missions spent as much or more than their reserves over the PDR estimate." and "There did not appear to be evidence that mission cost increases are throttled as reserves run out." The dollar relationship is real even where the percentage one is not: "Findings demonstrated strong positive correlation between total mission cost increases and total dollars reserved, as shown in Figure 7." For spacecraft specifically, spending throttles as increases approach total reserves for missions that stay within them (8) but accelerates once reserves are exhausted (5). The paper's own recommendation argues against upstream's flat practice verbatim: "One solution may be to alter reserve policies so that reserves are calculated as a function of overall mission risk rather than setting reserves at a fixed percentage of total costs" - i.e. institutional evidence that fixed-percentage-of-cost reserves is the wrong sizing rule; no re-pin proposed (the 20% centre and [15,50] band remain defensible as a first-order default, now with its failure mode documented). |
| `Cost of capital (WACC)` | 0.10 [0.075, 0.15]/yr; industrial floor Boeing 7.5% / Howmet 8.3%, "startup risk premium to ~10-15%" attributed to Damodaran's tables | scottoline_coleman_1999_loan_guarantees_tax_incentives_launch_ventures - first institutional bracket for that startup premium: "Reduces the Cost of Debt Financing by Greater than 2X - Without Loan Guarantees: Interest Rate = 14% or More - With Loan Guarantees: Interest Rate : 7%" and, on capital availability itself, "Kelly, Rotary. and Pioneer reported that they had raised only 5% of their combined required capital as of May 1999." The upstream 0.10 centre sits between the ~7% guaranteed-debt rate and the >=14% unguaranteed one; consistency anchor, no re-pin. |

Both sources read in full from the committed PDFs (quotes programmatic-sliced from the text layers); key figures verified present above. No revision candidate opened: both cells gain backing without contradiction.

## R114 - Space-resource hurdle rates and NASA cost growth (2026-10-04; +3 sources, T1x2, T2x1)

`mckeown_2024_hurdle_rate_commercial_space_resource_projects` (abstract read in full) is the first registered source on discount rates for space-resource projects specifically: hurdle rates 'in the range of 25%' and a 'standard' discount rate of 10% for comparing projects. Upstream's WACC is 0.10 (range 0.075-0.15), anchored so far to Damodaran's industry rates (7.6% aerospace, 8.2% metals and mining); the paper's 10% matches the value and its 25% is a project hurdle rate, a different quantity from WACC. `nrc_2010_controlling_cost_growth_nasa_earth_and_space_science_missions` (Summary chapter only) puts prior studies' average NASA cost growth at 23-77%, most of it after critical design review, which bears on the contingency fraction; it states no 20% standard in the passages read.

`parkinson_1999_hidden_costs_of_reliability_and_failure_in_launch_systems` is registered from its record only (the owner's note, 'up to 20% of launch cost', is unchecked). A PPIAF cost-of-capital method report for emerging-market PPP contracts was rejected (it prices no space or mining project). Four secondary insurance pages (explainers, a newsletter, a blog and an unsourced opinion piece) were rejected: they restate the Aon and Gallagher figures that the registered Gallagher series already carries, or give figures with no source (Round 114 log entry). The Gallagher Q1 2026 page and Damodaran's WACC page on the list are already registered. No revision candidate.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.

**valueinvesting_io_2026_boeing_howmet_wacc [T4]** - re-classed registered_not_pulled -> verified_live_not_pulled. Boeing (BA) WACC page read live; the valuation tables are embedded server-side in JSON: verbatim "(/) WACC", low/high scenario "10.2%" / "6.6%", summary table "WACC / Discount Rate" with range "6.3% - 8.6%" and selected "7.5%"; long-term growth rate band "2.0% - 4.0%" (selected 3.0%). Live-verified the WACC anchor behind spacecost's 'Cost of capital (WACC)' row.
## R125 (2026-10-06) - CC-BY queue sweep: mckeown_2024 licence re-confirmed + UNSW newsroom corroboration; no full-text route

- **mckeown_2024_hurdle_rate_commercial_space_resource_projects** [T1]: CC BY 4.0 re-confirmed via Crossref licence field (R124 data); no arXiv copy (S2 externalIds + exact-title search both empty). UNSW BusinessThink newsroom page verified live and corroborates the headline figure verbatim: "hurdle rates in the range of 25% could be appropriate for potential commercial space resource development projects" - same number as the R114 abstract extraction, now independently attested by a second live source. No full-text route reachable from this machine (ScienceDirect Cloudflare; no institutional PDF located). Retry note appended; stays registered_not_pulled.

## R144 - GAO-18-57 pulled from the full text: queue row closed, all five key numbers re-verified against the document itself (2026-10-09)

**gao_2018_commercial_space_launch_insurance_mpl_methodology [T3; registered_not_pulled -> full_text_hosted]** — gao.gov was Akamai-blocked from this machine in R89, R122 (HTTP 429), R130 and R131 (all HTTP 403); on the R144 re-probe `https://www.gao.gov/assets/gao-18-57.pdf` pulled live (695,627 B, 24 pp, zero in-file licence statement -> work of the U.S. government, hosted public-domain). Every key number r89_mpl_methodology_key_numbers.csv recorded from GAO's product-page summary was re-checked verbatim against the full text: $3M average loss per casualty (p.9); property-damage factor "recently changed from 50 percent to 25 percent" (p.9); both regulatory threshold definitions in one sentence on p.11 — third parties "no less than a probability of occurrence of no less than 1 in 10 million", and for **government property or personnel** "no less than 1 in 100,000" (the full text's government-side scope is broader than the R89 product-page paraphrase 'government property'; noted on the row); the understatement warning ("Not doing so could understate the amount of insurance launch companies are required to purchase, exposing the federal government to excess risk", summary p.2 — GAO-17-366 recommended updating the $3M figure and FAA has not done so); indemnification cap "up to **$3.1 billion in 2017 (the equivalent to $1.5 billion in 1988)**" (p.6) = provenance of CRS R48582's '$1.5B' figure, unchanged. No re-pin: statutory caps ($500M third-party / $100M USG) untouched; the row now carries the document itself instead of a summary-derived record.
