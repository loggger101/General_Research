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

rc-098 (WACC citation: Damodaran backs the floor only), rc-099 and rc-124 (contingency citations: Whitley & Shinn, NRC 2010), rc-107 (liability premium ~$1.0M per GAO). Texts in `revision_candidates.csv` (open) and `revision_candidates_closed.csv`.

Extracted data: `extracted_data/r164_liability_premium_vs_upstream.csv`.

## R205 - near-miss: Slingshot Aerospace pairing (2026-10-19)

spacecost CITATIONS.md section 4 pairs 'Plane Talking (Gallagher) / Slingshot Aerospace, 2024' for the launch-insurance market rate. Live search on 2026-10-19 found no separate Slingshot artifact: Plane Talking issues are hosted at specialty.ajg.com (Q1/Q3/Q4-2024 located; the Q1-2024 issue is what the insurance row's cell cites), and spacecost/operations.py names only Plane Talking in the row note itself. The registered gallagher_plane_talking_space_market_updates already covers the cited cell; per R96 convention this pairing is documented as a near-miss, not registered.

## R244 - WACC floor anchored on registered Damodaran table (rc-188) (2026-10-23)

Upstream row at b5eb32a: Cost of capital (WACC) value 0.1, range_low 0.075, range_high 0.15; notes open with "Boeing 7.5% / Howmet 8.3% WACC (ValueInvesting.io 2026) as the industrial floor" and then quote Damodaran sector averages Aerospace/Defense 7.60 percent and Metals & Mining 8.20 percent Jan 2026.

In-repo institutional evidence: r47_damodaran_cost_of_capital_full_table_96_industries.csv (extracted live at R47 from the registered page and XLS twin, both hosts byte-identical) carries Aerospace/Defense n=79 Cost of Capital 7.60 percent with delta -10 bps against range_low, Metals & Mining n=73 at 8.20 percent; value 0.10 sits +240 bps above the aerospace anchor per the same file.

Attribution seam: CITATIONS.md line reads "| Damodaran (NYU Stern), Cost of Capital by Industry Sector (Jan 2026); Boeing and Howmet filings | cost-of-capital floor: industry averages, with no startup premium |" - but a sweep of sources.csv id and title fields finds no SEC filing for either company anywhere in the registry; the upstream note itself says those two figures come from ValueInvesting.io model output. The INDEX Sources to replace flag (R240) names price-page class with Damodaran replacement sought, which the note already quotes.

Verdict: open candidate rc-188 (citation; values untouched); upstream untouched. Extracted data: extracted_data/r244_wacc_floor_damodaran_anchor_key_numbers.csv.

## R331 - Terminal salvage still receives the launch-to-sale carry factor (2026-11-02)

Source `economicspace_terminal_salvage_timing_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`
and `MODEL.md`; spacecost@860bef9902aa67fec705875cd52fdb8e6def159f,
original vehicle, propellant and operational-cost CSVs;
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011, `spacevalue/cargo.py`.
The calendar contract says "The rig's salvage credit is received once, at
the END of the programme" (calc.py L4648-4649). MODEL.md L1130-1133 likewise
places it at the end and rejects forward compounding of a refund. The
prologue defines year-zero, effective-midpoint and end-of-mission buckets,
with end multiplier 1 and upfront multiplier Q=(1+r)^T (L5425-5453).

The tail first nets the terminal value against rig procurement
(calc.py L5592-5594), putting the credit in upfront hardware. Its later
calendar delta changes the credit by the reciprocal factor but also multiplies
that delta by the upfront Q (L5676-5680). Consequently the combined credit is
`(S/W)*cal_credit*(1+contingency)*Q`, not the stated end-date receipt
`(S/W)*cal_credit*(1+contingency)`. Here S is one rig's nominal terminal
value and W its campaign count. Under the existing per-sale averaging,
sale j is at T+j*cadence and the receipt at T+(W-1)*cadence: T cancels
from the discount exponent, so it cannot supply this extra Q.

Eighteen original `mission_cost_usd` cases are each paired with the same
input and salvage fraction zero. They retain the actual Falcon 9 reusable,
kerolox and all 46 operational rows, with explicitly labelled rate/salvage
controls and a synthetic finite mass book. Totals-only and full-breakdown
costs agree exactly. A principal case has two rigs flying one campaign each,
1-year stay, 5-year mission, 10% WACC, 600M USD procurement per rig and
the unchanged 0.50 salvage estimate. Utilisation is 1/5 of duty life,
so terminal value is 240M USD per rig. All receipts coincide with the sale:

| per-mission terminal credit | before contingency USD | with unchanged 20% contingency USD |
|---|---|---|
| receipt at the stated year 5 date | 240,000,000 | 288,000,000 |
| original credit multiplied by 1.1^5 | 386,522,400 | 463,826,880 |
| excess credit / total-cost undercharge | 146,522,400 | 175,826,880 |

There is no staggered-fleet allocation in this one-campaign witness. Other
positive-rate cases span 1-12 years and 10-20% rates. Multi-campaign cases
retain the original reciprocal calendar series; independently summing dated
receipt shares at 50-digit Decimal precision reproduces its correctly dated
credit and isolates the same extra Q. A 150 kg refinery addition on the rig
shares the timing error. Turning the calendar flag off does not remove the
baseline error when WACC remains on.

Six further paired cases execute the complete original evaluator on a
synthetic 1e9 kg, 2 g/cm3 body, raw silicate cargo at 100 USD/kg, a 1,000 kg
payload cap and 1,000 m/s per leg. They use the actual chemical vehicle and
propellant, no ISRU or aerocapture, a nonbinding one-commodity market and
unchanged numerical functions. The main WACC-on result is one rig serving
two campaigns: mission 1.25 years, cadence 0.25 years, sale dates 1.25/1.50
and terminal receipt at 1.50. Its reported total is 937,819,491.876605
USD/mission. The zero-salvage pair isolates a 120,232,353.131616 USD credit,
against 106,728,520.842521 USD under the stated receipt dates. Correcting
only this timing gives 951,323,324.165700 USD/mission, 13,503,832.289095
USD higher. The mass book and duration are identical in the paired run.
Finite result floats match their untraced replay by float.hex, with identical
field types and NaN positions.

Ten direct and two full-evaluator pairs show excess credits. Eight direct
and four full controls are inert with zero rate, the WACC flag off, zero
salvage, an exhausted rig, no modelled rig life or a single mission receiving
no credit. WACC is off by default (calc.py L1017), so this does not change
the reported default run. The main full fixture is a rectangular programme;
fractional procurement or cumulative extraction beyond body mass is not
needed for the finding.

Verdict: the stated end receipt is still valued as though it existed at
launch. `rc-262`: retain the terminal credit's date in the cost buckets and
calendar calculation. The diagnostic preserves the nominal salvage rule,
rate, contingency and current averaging convention. It does not replace
that convention with NPV, redesign the mission or measure catalogue/ranking
effects. `extracted_data/r331_terminal_salvage_timing.csv`.
