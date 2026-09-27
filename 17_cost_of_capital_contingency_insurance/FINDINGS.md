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
