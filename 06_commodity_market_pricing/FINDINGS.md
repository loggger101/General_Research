# Domain 6 — Commodity / mineral market pricing (value side of the pipeline)

**Why this domain exists.** Domains 1–5 anchor every *physics and cost* number in `spacecost`/`economicspace` (densities, Δv, launch $/kg, ISRU energy). But the economicspace pipeline's **profitability output is driven by a second, equally load-bearing input: commodity market prices.** `modules/mineral_value.py` prices every tradable element and mineral (`ref_price_usd_per_kg`) and multiplies that by per-asteroid yields to produce all of `profitability_catalog.csv`. Until R39 those price inputs carried only the citation "USGS/LME/mineralogy reference" with **no registered, analyzable source** — a gap as real as any unanchored Δv row.

## Round 38→39 trigger (criterion #1)
R39 began by auditing whether domains 4/5 were exhausted before standing up new ones: domain-4's remaining gaps (Vulcan Centaur / New Glenn LEO payload masses) are **vendor-datasheet values** — every reachable source traces to ULA/Blue Origin, so no peer-reviewed anchor exists; domain-5's ZBO cryocooler W/W has no flight data and its NRE/capital rows are management assumptions by nature. With those confirmed non-paper-closeable, the audit then surfaced this genuinely unanchored value side → **new domain 6**, per criterion #1 ("begin looking for other domain gaps").

## The anchor — World Bank Commodity Price Data ("Pink Sheet")
**`worldbank_cmo_pink_sheet` (T2, full text hosted)** — institutional primary source from the World Bank Commodity Markets Group. Two artifacts committed to `full_texts/`:
- `CMO-Historical-Data-Monthly.xlsx` (587 KB) — **monthly nominal-USD prices for 71 commodities, 1960M01 → present** (file updated 2026-09-02; latest data month **2026M08**). Parsed live with openpyxl: sheets `Monthly Prices` / `Monthly Indices` / `Description` (per-series provenance) / `Index Weights`.
- `CMO-Pink-Sheet-September-2026.pdf` (239 KB) — the published CMO report for the same period.

**Why WB and not USGS:** our code's fallback citation names "USGS/LME", but **pubs.usgs.gov is bot-blocked from this machine** (403 on special-topics, 404 on every MCS PDF path shape tried) — so I could *not* access/analyze the Mineral Commodity Summary and therefore did NOT register it. The World Bank Pink Sheet satisfies the standing requirement ("actually able to access and analyze") fully: downloaded, parsed, cross-checked against our catalog this round. Tier T2 (institutional government data compilation, not a peer-reviewed journal — same tier logic as `hf_dataset`/NTRS statistical references).

**Coverage vs our 13 tradable elements:** WB carries **gold, platinum, silver, copper, nickel, aluminum, zinc, iron-ore**. It does **NOT** carry the minor PGMs (Rh/Ir/Os/Ru/Pd) — those remain on the yfinance/LBMA path and are out of scope for this anchor.

## Audit finding — our `ref_price_usd_per_kg` is a MIXED-DATED snapshot
Despite a uniform `ref_price_date = 2026-05-29`, each element's value matches a *different* market month (verified by scanning the full WB series for the closest-ratio period):

| Element | our ref $/kg | best-match WB month | current (Aug-26) $/kg | status |
|---|---|---|---|---|
| Gold | 150,000 | Apr-2026 ($151,783, ratio .988) | 141,817 | **current** |
| Nickel | 16.5 | Jul-2026 ($16.65, ratio .991) | 16.75 | **current** |
| Platinum | 45,000 | ~Jul-2025 (ratio 1.006) | 57,228 | **stale (~21% low)** |
| Copper | 8.8 | ~Jan-2025 ($8.99, ratio .979) | 14.326 | **stale (~39% low)** |
| Silver | 950 | no month since Jan-2024 (closest $977) | 2,103 | **stale (~55% low)** |

**Interpretation:** the column was evidently refreshed element-by-element over time and then stamped with one date. Gold/nickel are fine; silver/copper/platinum understate current market by 21–55%. This is a **correction candidate for `mineral_value.py`/`mineral_value_catalog.csv`, NOT applied** (target repo read-only). It matters because those prices flow directly into every row of the profitability output — an understated silver price makes silver-bearing asteroids look less profitable than they are. All numbers → `extracted_data/r39_commodity_price_verification.csv`.
