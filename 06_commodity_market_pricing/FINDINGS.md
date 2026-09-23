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

## Round 46 -> base-metals audit quantified + JM PGM market report (minor-PGM anchor)

**Two additions this round:** (1) the R39/R45 precious-metals staleness finding is now **quantified for every priced element we can compare**, using the committed World Bank xlsx at our own stamp month; (2) a new T2 source — `jm_pgm_market_report_2026` — closes the minor-PGM gap that neither LBMA nor WB covers.

### Base-metals audit vs World Bank CMO monthly (same-month comparison, 2026M05 = our stamp month)
| element | our ref $/kg (stamp 2026-05-29) | WB May-2026 ($/mt -> $/kg) | diff vs same month | status |
|---|---|---|---|---|
| copper  | 8.80   | **13.543** (from $13,543/mt) | **-35.0% LOW** | STALE — R39's "~Jan-2025 match" confirmed; worst base metal |
| nickel  | 16.50  | **18.806** (from $18,806/mt) | **-12.3% LOW** | mildly stale (R39 called it "current"; same-month view says ~12% low) |
| iron    | 0.50   | n/a — WB series is *ore* ($108.6/dmtu, cfr spot), not refined Fe | context only | unit/product mismatch; our row prices element Fe at a refined-metal price |

Aluminum & zinc are carried by the WB sheet but have **no priced row in our catalog** (not tradable elements here) — no comparison needed. Cobalt is priced in our catalog ($33/kg) but appears in neither WB nor JM datasets → recorded as an unanchorable-by-these-sources gap alongside osmium.

### Cross-check: World Bank monthly vs LBMA daily at 2026-05 (independent sources, same month)
| metal | WB May-2026 $/oz troy | LBMA @ 2026-05-29 $/oz troy | diff |
|---|---|---|---|
| gold      | 4,587 | 4,525.75 | +1.35% |
| platinum  | 1,998 | 1,912.00 | +4.50% |
| silver    | 78    | 75.78    | +2.93% |

Two independent institutional series agreeing within ≤4.5% for the same month = high confidence in both anchors (and in our conversion factor).

### New anchor — `jm_pgm_market_report_2026` [T2; full text pulled, NOT hosted]
Johnson Matthey's annual PGM market report (May 2026 edition, 36 pp), the industry-standard institutional source: base-price narrative for Pt/Pd/Rh/Ir/Ru plus complete supply & demand tables in troy oz **and** tonnes (primary production by region + secondary/recycling + industrial demand, 2021–2026). Pulled live this round from matthey.com; **not committed to full_texts/** because JM's terms state the prices "are the property of Johnson Matthey Plc" and prohibit use without consent — extraction-only registration (all numbers below verbatim from the pulled PDF).

**Price audit vs our static `ref_price_usd_per_kg`** (JM quotes are Q1-2026 levels; report covers through March 2026, so these bracket rather than pin our May-29 stamp):
| metal | JM quote (verbatim basis) | ≈ $/kg | ours $/kg | diff | status |
|---|---|---|---|---|---|
| rhodium   | "spiking above **$9,000** during the final days of December" [2025] | ~289,357 | 320,000 | **+10.6%** high | mildly stale (JM: peaked $12,000 late Feb-26, retreated "towards $10,000") |
| iridium   | "new all-time highs of **$8,000** and $1,750" [Q1-2026; Ir listed first] | ~257,206 | 160,000 | **-37.8% LOW** | STALE — revision candidate |
| ruthenium | same sentence (Ru second) **$1,750** [Q1-2026 ATH]; end-2025 "then all-time record of **$1,275**" | ~56,263 (ATH); ~40,992 (end-25 record) | 16,000 | **-71.6% LOW** vs ATH / -61.0% vs end-25 record | STALE — worst PGM gap; revision candidate |
| platinum  | "falling to **$1,908** and $1,448, respectively [Pt/Pd], at the end of March" [2026] | ~61,343 | 45,000 | **-26.6%** low | corroborates R45's LBMA finding (-26.8%) independently |
| palladium | same sentence (**$1,448**) | ~46,554 | 48,000 | +3.1% high | fine at Q1 levels (R45: +9.5% vs May-29 LBMA) |

**Production estimate audit** — our `mineral_value.py` annual-production comments vs JM primary supply **2025**:
| metal | ours (~t/yr, code comment) | JM 2025 primary (tonnes table) | verdict |
|---|---|---|---|
| rhodium   | ~23 t    | **17.6** | **ours +30.7% high — revision candidate** |
| iridium   | ~7.5 t   | **7.1**  | AGREE (within 6%) |
| ruthenium | ~30 t    | **30.2** | AGREE (exact) |

(Platinum/palladium have no production rows in our catalog — nothing to compare.)

### Osmium & cobalt gap (recorded, uncloseable by these sources)
Osmium: NO published reference price series exists at LBMA or JM and the JM report contains **no osmium table** (verified by full-text scan) → our $13k/kg row (~1 t/yr basis) remains anchored to nothing registered; it is the only precious-metal row with no institutional price source reachable from this machine. Cobalt: priced in our catalog ($33/kg) but absent from both WB's 71-commodity sheet and JM's report → same status. Both recorded as standing gaps, not errors.
