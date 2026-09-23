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

## Round 45 -> LBMA precious-metals fixings (second value-side anchor)

**`lbma_precious_metals_fixings` [T3; open service, JSON pulled live this round]** — the London Bullion Market Association's official daily benchmark prices. R39 registered the World Bank Pink Sheet as the *first* value-side anchor but it carries **no minor PGMs and only monthly** precious-metals data; LBMA is the actual authority our `mineral_value.py` "yfinance/LBMA path" resolves to, now registered and analyzable (not just cited). Four JSON series pulled live 2026-09-23: gold & silver daily since **1968-01-02** (~14.8k fixings each), platinum & palladium daily since **1990-04-02** (~9.2k AM + ~9.15k PM each). Basis note: Au/Pt/Pd use the **AM London fixing**; Ag uses LBMA's single daily benchmark (no separate am/pm file is published for silver).

### Audit — our static `ref_price_usd_per_kg` vs LBMA at OUR OWN stamp date (2026-05-29)
Compared each catalog value to the LBMA fixing on the *same* trading day it claims (`ref_price_date = 2026-05-29`; gap = 0 days for all four, i.e. a real fix existed that day):

| metal | our ref $/kg (2026-05-29) | LBMA @ 2026-05-29 ($/kg) | diff | LBMA latest 2026-09-22 ($/kg) | status |
|---|---|---|---|---|---|
| gold      | 150,000 | 145,506.2 | **+3.1%**   | 138,671.0 | current (fine) |
| platinum  | 45,000  | **61,472.2** | **-26.8% LOW** | 57,628.6 | STALE — underpriced ~27% even at our own date |
| palladium | 48,000  | 43,853.6  | **+9.5%**   | 41,644.9  | near-current (mildly high) |
| silver    | 950     | **2,436.5** | **-61.0% LOW** | 2,110.2  | STALE — underpriced ~61%; the worst of the four |

Conversion is $/troy-oz / 0.0311034768 (verified against gold's known magnitude: LBMA AM $4,313.15/oz -> $138,671/kg). **Silver at $950/kg when it was actually ~$2,436/kg on our own reference date is a material error** for any profitability cell that prices Ag; platinum's 27% underprice is the second. Both are recorded as revision candidates — NOT applied here (the economicspace target repo is read-only this round). Gold and palladium agree well enough to leave alone.

### Series statistics (for future re-anchoring)
| metal | n fixings (AM/single) | first date | last date | min $/oz troy | max $/oz troy |
|---|---|---|---|---|---|
| gold      | 14,840 | 1968-01-02 | 2026-09-22 | 34.78   | 5,501.70 |
| silver    | 14,851 | 1968-01-02 | 2026-09-22 | 1.272   | 118.45   |
| platinum  | 9,216  | 1990-04-02 | 2026-09-22 | 330     | 2,860    |
| palladium | 9,217  | 1990-04-02 | 2026-09-22 | 78.75   | 3,339    |

Minor PGMs **Rh/Ir/Os/Ru are still not carried by LBMA** (no JSON series) — they remain on the yfinance/USGS path and stay out of scope for this anchor.
