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

## R70 - Full-extraction pass of the hosted sources (2026-09-27; registry unchanged)

Every hosted full text in this domain was re-read end to end for pipeline-useful numbers; tables were read by word coordinates (or from rendered page images where the text layer fails) and checked against their printed totals. New files (all in `extracted_data/`, every row carries `source_id` and a page location): `r70_worldbank_pink_sheet_annual_means_2016_2025.csv` (240); `r70_worldbank_pink_sheet_monthly_energy_fertilizer_metals.csv` (800); `r70_worldbank_pink_sheet_sept2026_report_summary_table.csv` (81).

- **Pink Sheet monthly series**: 800 months (1960M01-2026M08) x 24 energy, fertiliser, base-metal and precious-metal series in one CSV, plus 2016-2025 annual means computed here (240 rows).
- **September 2026 report summary table**: 64 commodities and 17 indexes x 11 periods (2023-2025 annual, four quarters, June-August 2026). The published 2025 annual averages match the means computed from the xlsx (copper 9,947 vs 9,947.42 $/mt; platinum 1,278 vs 1,278.33 $/toz).

## R71 - Side-deepening extraction round (2026-09-27; logged in R72; registry unchanged)

Branch `side-deepening`, commit 0729c2d, merged into this branch in R72. It gave the 20 PDFs un-hosted on 2026-09-26 (restored byte for byte from git `5dd58d5`, sha256 matched against `DOWNLOADS.md`) their first full pass, and read seven non-hosted sources from copies the owner downloaded (DOWNLOADS.md section B). The commit wrote no FINDINGS block or log entry; this block and the R71 log entry were written in R72 from the commit and the files themselves. R72 then re-checked every R71 file whose PDF is restorable: every numeric cell was searched for in the PDF text (0 values missing outside cells the R71 notes say were read from page images), the image-read cells were compared against rendered pages, and large tables were checked row by row. New files: `r71_jm_pgm_2026_key_numbers.csv` (14); `r71_jm_pgm_2026_supply_demand_tables.csv` (148).

- **jm_pgm_market_report_2026**: full supply and demand tables (primary supply by region, secondary supply, demand by sector, balance) for Pt, Pd, Rh, Ru and Ir, 2021-2026f, in both troy ounces and tonnes.
- **Correction and withdrawal (R71)**: R46's rhodium supply figure of 17.6 t was the South Africa row of the p32 table. Total primary supply is 21.8 t in 2025, so economicspace's 23 t is 5.5% high, the margin R46 accepted for iridium. **rc-038 is withdrawn**, and `r46_price_audit_key_numbers.csv` was corrected in place.

## R72 - Tables R70/R71 skipped, verification of R71, upstream re-check (2026-09-27; registry unchanged)

This round's container reached only package registries (arXiv, NTRS, JPL, Google Docs and every publisher returned 403), so nothing new could be fetched; the work used the hosted PDFs and the 20 restored from git `5dd58d5`. Each hosted and restored PDF's table captions were listed and matched against the extracted CSVs; tables no CSV cited were read by word coordinates (columns assigned from header or fully populated rows, so blank cells stay blank) or from rendered page images, and checked against printed totals. Upstream heads re-read: spacecost@e831245, AsteroidCatalog@852bf69, economicspace@1f470d4 (unchanged since 2026-09-26). no new files in this domain.

- **R71's JM tables verified**: every total equals the sum of its rows in both units; combined supply = primary + secondary; balance = supply - demand; and each ounce row converts to its tonne row within 0.14 t (JM rounds each table separately).
- **Upstream market sizes** (`ANNUAL_WORLD_PRODUCTION_KG`, economicspace@1f470d4): platinum 180 t vs JM 2025 primary supply 172.9 t (+4.1%); palladium 210 t vs 205.0 t (+2.4%). Both agree; no candidate.

## R74 - Upstream citations registered (2026-09-27; +7 sources, T3x3, T4x4; nothing extracted)

Sources the upstream repos cite that this registry did not have, found by reading every per-row `notes` field, code comment and CITATIONS.md in AsteroidCatalog@852bf69, spacecost@e831245 and economicspace@1f470d4. Each is `registered_not_pulled`: its DOI was checked against Crossref, or its landing page against a live request from this machine, and the result is recorded in the row. No full text was sought and no number was extracted; the rows are the queue for a later extraction round.

- `usgs_mineral_commodity_summaries_2026` (T3): mineral_value.py curated fallback prices for metals yfinance lacks, and every terrestrial market depth in ANNUAL_WORLD_PRODUCTION_KG.
- `lme_official_reference_prices` (T3): mineral_value.py ref_price_usd_per_kg for nickel and cobalt (and the other LME base metals).
- `cme_comex_nymex_futures` (T3): mineral_value.py live price basis for Au/Ag/Cu/Pt/Pd; spacecost live RP-1 and methane price proxies.
- `yahoo_finance_yfinance` (T4): mineral_value.py live futures prices; spacecost optional live propellant price proxies.
- `metals_dev_api` (T4): mineral_value.py optional live LME and precious-metal quotes.
- `heraeus_2026_precious_metals_forecast` (T4): mineral_value.py platinum ref_price_usd_per_kg (midpoint of the 2026 forecast range).
- `reuters_2026_gold_analyst_consensus` (T4): mineral_value.py gold ref_price_usd_per_kg context.
## R83 - USGS Mineral Commodity Summaries 2025 registered + hosted, world-production audit (2026-09-30; +1 T3 row)

economicspace@7d99662 CITATIONS.md names *Mineral Commodity Summaries 2025* as the source of "the order of the 2024 prices and world production behind the rows mineral_value 1.11.0 added (sulfur, chromium, titanium, gallium, germanium, rhenium, tungsten, molybdenum, ammonia)" - a citation this registry did not have (the 2026 edition is registered as `usgs_mineral_commodity_summaries_2026`). The full report v1.2 (March-2025, 216 p., 10.4 MB) was pulled live from pubs.usgs.gov this machine and committed under `full_texts/` with its manifest row; USGS public domain.

World-production tables read by word coordinates (chromium p62, gallium p78, germanium pp83-84, molybdenum p126, nitrogen-fixed-ammonia pp131-132, phosphate rock p138, rhenium p150, sulfur p176, titanium p190, tungsten p194) and audited against `ANNUAL_WORLD_PRODUCTION_KG` at economicspace@7d99662 - full rows in `extracted_data/r83_mcs2025_world_production_key_numbers.csv`:

- EXACT: gallium 760,000 kg (primary), molybdenum 260,000 t, rhenium 62,000 kg, tungsten 81,000 t W-content; phosphate rock 240 Mt matches the phosphorus row's own comment.
- Within '~rounded' tolerance (consistency notes only): chromium world mine production 47,000 kt vs our 4.4e10 kg (-6.4%); sulfur 85,000 kt vs our 8.3e10 kg (-2.4%); titanium sponge '320,000^8' (footnote: excludes U.S.) vs our 3.0e8 kg (-6.2%).
- **rc-055 opened**: ammonia cell 1.8e11 kg N is +20% above the chapter's world plant production of 150,000 kt (2024e) AND contradicts its own inline comment '~150 Mt N as ammonia'.
- Gap: germanium carries no published world table in the chapter ('global production data were limited' - prose only), so our 1.4e5 kg refinery row stays unanchored by MCS.

Edition check: v1.0 and v1.1 (both pulled this round) carry identical values on every audited total, so none of the discrepancies is edition drift; the hosted copy is v1.2 as printed in CITATIONS.md's publication date window.

## R114 - A source for the osmium price (2026-10-04; +1 source, T2x1)

The owner's list added an osmium block: two dealer price pages, two dead price-tracker sites, and the IPA/SFA (Oxford) osmium factsheet of May 2026, registered as `ipa_sfa_2026_osmium_pgm_factsheet`. It closes the 'Osmium & cobalt gap' recorded in this domain's FINDINGS above, for osmium: p5 says osmium has no exchange-traded benchmark and no market transparency, is priced at each transaction, and has been 'fixed in the 300-400$/oz range since the 2000's' (about $9,600-12,900/kg); global output is hundreds of kilograms a year. The economicspace osmium row of $13,000/kg is $404/oz, a hair above that band; no revision candidate. The cobalt gap stays open.

The two dealer pages quote EUR 2,351.81 per gram (about 200 times the factsheet's band) for 99.9995% crystalline bars, a retail price for a fabricated product from one vendor network, and were rejected (Round 114 log entry). The three price-tracker URLs (platinumbased.co.uk, dailyplatinum.com, dailypl.com) are dead and stay undecided.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.

## R115 - Prices and a production cell checked against the hosted USGS summaries; five new candidates (2026-10-04; registry unchanged)

Both Mineral Commodity Summaries editions were already hosted (R83, R81) but R83 compared only the world-production figures of the v1.11.0 rows. This round read their price lines against economicspace@29a0309 `modules/mineral_value.py`, which stamps the ten v1.11.0 elements 2025-01-31 and cites 'USGS MCS 2025' for each.

- **titanium (rc-062)**: the cited table's sponge price is the landed duty-paid import value, $10.60-13/kg over 2020-2024e; the cell is $9 and the note says $7-10. All five years are above the note's ceiling.
- **tungsten (rc-063)**: MCS 2025 withholds the price ('W') in every year and quotes no APT figure; the $340/mtu is not in the cited edition. MCS 2026 reports APT at $331 rising to $675 per mtu through 2025 ($41.7 to $85.1 per kg W), so the cell is about 47% below the end-2025 level.
- **gallium (rc-064)**: 2024e high-purity import value is $500 (range $450-625 over five years); the cell is $600 and the note's '$500-700' upper end is not printed.
- **ammonia (rc-065)**: $440 per SHORT ton is read as $450 per metric ton (it is $485/t).
- **cobalt world production (rc-066)**: 2.3e8 kg against 3.10e8 for 2025e (-25.8%); it equals Congo's output alone. R81 had recorded the gap without a row.
- Agreeing with their notes, so no row: chromium metal $5.60/lb = $12.35/kg against $10-12; rhenium pellets $1,370 against $1,200-1,600; molybdenum $47/kg against $44; germanium $2,100 against $2,000-3,000; sulfur Tampa contract $69-116 per long ton against $80-100/t.

Extracted data: `extracted_data/r115_usgs_new_element_prices_cobalt_production.csv` (13 rows, page-located; percentages computed in code).

**heraeus_2026_precious_metals_forecast [T4]** - re-classed registered_not_pulled -> verified_live_not_pulled. Forecast page read live; verbatim table rows "Platinum $1,300 – $1,800", "Gold $3,750 – $5,000", "Silver $43 – $62", "Palladium $950 – $1,500", "Rhodium $6,000 – $9,000" (per ounce). First institutional per-ounce precious-metals forecast range in d06 - the platinum row is cited upstream by economicspace's mineral_value.py.
**metals_dev_api [T4]** - re-classed registered_not_pulled -> verified_live_not_pulled. metals.dev docs read live; verbatim "Live Feed of Gold, Silver, Platinum & Palladium Spot Prices. Real-time prices from leading Authorities & Markets like LBMA , LME , MCX" + free-tier line "Get started for free. No credit card required." with endpoint GET api.metals.dev/v1/latest shown on-page.
**yahoo_finance_yfinance [T4]** - retry note only. pypi.org/project/yfinance/ now serves a 'Client Challenge' bot page from this machine instead of the package page - stays registered_not_pulled.
