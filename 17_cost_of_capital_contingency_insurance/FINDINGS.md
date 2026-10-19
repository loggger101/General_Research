# Domain 17 — Cost of capital, contingency & insurance

Backings: spacecost `reference/operational_costs.csv` rows `Cost of capital (WACC)`, `Contingency reserve`, `Launch insurance` and `Third-party liability insurance`, and economicspace `modules/calc.py` `contingency_fraction`, `apply_wacc_compounding` and `charge_insurance`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Cost of capital (WACC)` | 0.10 [0.075, 0.15] per year | Boeing 7.5% and Howmet 8.3% (ValueInvesting.io 2026) as the industrial floor; a "startup risk premium to ~10-15%" attributed to Damodaran's industry tables |
| `Contingency reserve` and `calc.py` `contingency_fraction` | 20% [15, 50] of total mission cost; applied after every other line and before WACC | "Industry-standard; first-of-kind missions carry the upper end"; no source |
| `calc.py` `apply_wacc_compounding` | False since v1.22.0 | scope decision: "a discount rate is a statement about whose money this is" |
| `Launch insurance` | 10% [5, 15] of launch + payload value | Gallagher "Plane Talking" Q1 2024: ~6% in early 2023, ~10% after the Intelsat 33e loss |
| `Third-party liability insurance` | $1.5M [0.5M, 3M] per launch | MPL caps cited; the premium has no source |
| `calc.py` `charge_insurance` | False since v1.20.0 | scope decision |

**What a source has to supply:** discount rates used for early-stage space ventures and remote mining; cost growth of first-of-kind missions and agency reserve policy; space insurance premiums by vehicle maturity and loss history; third-party liability premium levels.

**Boundary:** domain 18 holds the regulatory requirement (licence, how MPL is set); this domain what the cover and capital cost. Reliability is domain 16.

## R77 - Sources moved in (2026-09-27)

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `damodaran_cost_of_capital_by_industry` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 44 addition | `extracted_data/r47_damodaran_cost_of_capital_key_numbers.csv`, `extracted_data/r47_damodaran_cost_of_capital_full_table_96_industries.csv` |
| `valueinvesting_io_2026_boeing_howmet_wacc` | domain 5 | `05_inspace_operations/FINDINGS.md`: R74 | none |
| `gallagher_plane_talking_space_market_updates` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 44 addition; Round 57 addition | `extracted_data/r57_plane_talking_series_key_numbers.csv` |

rc-031 (open, Launch insurance) is written up in domain 5.

## R89 - MPL methodology behind third-party liability (2026-09-30)

- **faa_2017_report_to_congress_updated_mpl_method** [T3, hosted] (2017-04-21, PL 114-90 Sec. 102): the risk-profile method (since April 2015) with thresholds 1-in-10,000,000 third party and 1-in-100,000 government property (p20); MPL = casualties x cost of casualty + property damage; cost of a casualty fixed at $3 million since the first licence in 1988 (p14/p17); STPI's study "suggested that the FAA should adjust its cost of casualty value upward, to approximately double its current value. The FAA is currently reviewing the study" (p17).
- **gao_2018_commercial_space_launch_insurance_mpl_methodology** [T3] (GAO-18-57, 2018-01-16): same thresholds and $3M; property-damage factor 50% -> 25% of casualty cost; federal indemnification above MPL up to $3.1 billion in 2017 (= $1.5B in 1988), the source of CRS R48582's figure; four recommendations, DOT concurred. Hosted since R144.

Premiums track vehicle-specific risk profiles at these thresholds; the caps are unchanged. `extracted_data/r89_mpl_methodology_key_numbers.csv`. No re-pin.

## R108 - Contingency and venture cost of capital (2026-10-03)

| cell | backing (both NTRS, hosted) |
|---|---|
| `Contingency reserve` / `contingency_fraction` | whitley_shinn_2012_economics_nasa_mission_cost_reserves (CADRe): "only one mission had total cost increase within the value of the reserves reported at PDR. All twelve other missions spent as much or more than their reserves"; no evidence that cost growth slows as reserves run out; "strong positive correlation between total mission cost increases and total dollars reserved"; recommends reserves "calculated as a function of overall mission risk rather than setting reserves at a fixed percentage of total costs". The 20% [15, 50] stays a defensible default with its failure mode documented. |
| `Cost of capital (WACC)` | scottoline_coleman_1999_loan_guarantees_tax_incentives_launch_ventures: "Without Loan Guarantees: Interest Rate = 14% or More - With Loan Guarantees: Interest Rate : 7%"; Kelly, Rotary and Pioneer had raised only 5% of their required capital by May 1999. The 0.10 centre sits between the two. |

No candidate.

## R114 - Space-resource hurdle rates; NASA cost growth (2026-10-04)

- `mckeown_2024_hurdle_rate_commercial_space_resource_projects` (abstract; CC BY): hurdle rates "in the range of 25%" and a standard 10% discount rate for comparing projects; the 10% matches upstream's WACC, the 25% is a different quantity.
- `nrc_2010_controlling_cost_growth_nasa_earth_and_space_science_missions` (Summary): prior studies' average NASA cost growth 23-77%, mostly after CDR.
- `parkinson_1999_hidden_costs_of_reliability_and_failure_in_launch_systems`: record only ("up to 20% of launch cost" unchecked).
- `valueinvesting_io_2026_boeing_howmet_wacc` (read live, re-classed): Boeing WACC low/high "10.2%" / "6.6%", range "6.3% - 8.6%", selected "7.5%"; growth 2.0-4.0% (3.0% selected).

`extracted_data/r114_gr_links_key_numbers.csv`.

## R144 - GAO-18-57 hosted and re-verified (2026-10-09)

The full report (24 pp) was reachable this round. Re-checked against R89: $3M per casualty and the 50% -> 25% factor (p9); thresholds "no less than 1 in 10 million" for third parties and "no less than 1 in 100,000" for **government property or personnel** (p11, broader than the R89 paraphrase); "Not doing so could understate the amount of insurance launch companies are required to purchase" (p2); cap "up to $3.1 billion in 2017 (the equivalent to $1.5 billion in 1988)" (p6). No re-pin.

## R153 - Third-party liability premium: two GAO reports (2026-10-12)

- **gao_2012_commercial_space_launches_faa_liability_risk_assessment** (GAO-12-899): "the cost of third party liability insurance for launch companies has been about 1 percent of the dollar amount of coverage they purchased", against an average MPL of "about $99 million" (range ~$23-267 million), so ~$0.99M per launch, inside [0.5, 3]M near the 1.5M centre; "The insurance market is generally willing and able to provide up to $500 million per launch".
- **gao_2017_commercial_space_launch_insurance_faa_calculation_weakness** (GAO-17-366): five active licences in 2016 averaged "about $51 million" MPL ($10-99 million), so ~$0.5M per launch at 1%; the $3M casualty value is "likely too low", and STPI recommended $5-6M (premiums would rise by about a third).

gao.gov refused this machine again, so both are registered from GAO's published summaries. The band covers both points. `extracted_data/r153_liability_premium_key_numbers.csv`.

## R164 - Candidates (2026-10-14)

rc-098 (WACC citation: Damodaran backs the floor only), rc-099 and rc-124 (contingency citations: Whitley & Shinn, NRC 2010), rc-107 (liability premium ~$1.0M per GAO). Texts in `revision_candidates.csv`.

**Round 205 - near-miss: Slingshot Aerospace pairing.**
spacecost CITATIONS.md section 4 pairs 'Plane Talking (Gallagher) / Slingshot Aerospace, 2024' for the launch-insurance market rate. Live search on 2026-10-19 found no separate Slingshot artifact: Plane Talking issues are hosted at specialty.ajg.com (Q1/Q3/Q4-2024 located; the Q1-2024 issue is what the insurance row's cell cites), and spacecost/operations.py names only Plane Talking in the row note itself. The registered gallagher_plane_talking_space_market_updates already covers the cited cell; per R96 convention this pairing is documented as a near-miss, not registered.
