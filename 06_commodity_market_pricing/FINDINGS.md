# Domain 6 — Commodity / mineral market pricing (value side of the pipeline)

Backings: spacevalue `spacevalue/catalog.py` `ref_price_usd_per_kg` for every tradable element and mineral (multiplied by per-asteroid yields into every row of `profitability_catalog.csv`) and `ANNUAL_WORLD_PRODUCTION_KG`. Until R39 the prices carried only "USGS/LME/mineralogy reference", with no registered source.

## R39 - World Bank Pink Sheet

**`worldbank_cmo_pink_sheet`** (T2, hosted): `CMO-Historical-Data-Monthly.xlsx` (monthly nominal USD for 71 commodities, 1960M01 to 2026M08) and `CMO-Pink-Sheet-September-2026.pdf`. It covers gold, platinum, silver, copper, nickel, aluminium, zinc and iron ore, not the minor PGMs. (USGS was unreachable then; it was registered in R81.)

**Audit:** despite one `ref_price_date = 2026-05-29`, each price matches a different month:

| Element | our ref $/kg | best-match WB month | current (Aug-26) $/kg | status |
|---|---|---|---|---|
| Gold | 150,000 | Apr-2026 ($151,783, ratio .988) | 141,817 | current |
| Nickel | 16.5 | Jul-2026 ($16.65, ratio .991) | 16.75 | current |
| Platinum | 45,000 | ~Jul-2025 (ratio 1.006) | 57,228 | stale (~21% low) |
| Copper | 8.8 | ~Jan-2025 ($8.99, ratio .979) | 14.326 | stale (~39% low) |
| Silver | 950 | no month since Jan-2024 (closest $977) | 2,103 | stale (~55% low) |

`extracted_data/r39_commodity_price_verification.csv`.

## R45 - LBMA precious-metal fixings

**`lbma_precious_metals_fixings`** [T3, open service]: gold and silver daily since 1968-01-02, platinum and palladium since 1990-04-02 (AM fixing; silver's single benchmark). $/kg = $/oz / 0.0311034768.

| metal | our ref $/kg (2026-05-29) | LBMA @ 2026-05-29 ($/kg) | diff | LBMA 2026-09-22 ($/kg) |
|---|---|---|---|---|
| gold | 150,000 | 145,506.2 | +3.1% | 138,671.0 |
| platinum | 45,000 | 61,472.2 | -26.8% | 57,628.6 |
| palladium | 48,000 | 43,853.6 | +9.5% | 41,644.9 |
| silver | 950 | 2,436.5 | -61.0% | 2,110.2 |

Series ($/oz): gold 14,840 fixings, 34.78-5,501.70; silver 14,851, 1.272-118.45; platinum 9,216, 330-2,860; palladium 9,217, 78.75-3,339. `extracted_data/r45_lbma_precious_metals_key_numbers.csv`.

## R46 - Base metals at the stamp month; Johnson Matthey PGM report

World Bank May-2026: copper $13.543/kg vs 8.80 (-35.0%); nickel $18.806/kg vs 16.50 (-12.3%); iron is ore ($108.6/dmtu), not comparable with refined Fe. WB vs LBMA in May-2026 ($/oz): gold 4,587 vs 4,525.75 (+1.35%), platinum 1,998 vs 1,912.00 (+4.50%), silver 78 vs 75.78 (+2.93%).

**`jm_pgm_market_report_2026`** [T2; read, not hosted: JM's terms forbid reuse] (May 2026, 36 pp):

| metal | JM quote | ≈ $/kg | ours $/kg | diff |
|---|---|---|---|---|
| rhodium | above $9,000 in late December 2025 (peak $12,000 Feb-26) | ~289,357 | 320,000 | +10.6% |
| iridium | all-time high $8,000 (Q1-2026) | ~257,206 | 160,000 | -37.8% |
| ruthenium | all-time high $1,750 (Q1-2026); end-2025 record $1,275 | ~56,263 / ~40,992 | 16,000 | -71.6% / -61.0% |
| platinum | $1,908 at end March 2026 | ~61,343 | 45,000 | -26.6% |
| palladium | $1,448 at end March 2026 | ~46,554 | 48,000 | +3.1% |

Production vs JM 2025 primary: iridium ~7.5 t vs 7.1 and ruthenium ~30 vs 30.2 agree; rhodium (see R71). Osmium has no LBMA or JM price, and cobalt is in neither dataset. `extracted_data/r46_price_audit_key_numbers.csv`.

## R70 / R71 / R72 - Extraction and verification (2026-09-27)

- R70: `r70_worldbank_pink_sheet_monthly_energy_fertilizer_metals.csv` (800 months x 24 series), `r70_worldbank_pink_sheet_annual_means_2016_2025.csv` (240), `r70_worldbank_pink_sheet_sept2026_report_summary_table.csv` (64 commodities, 17 indexes); published 2025 means match the xlsx (copper 9,947 vs 9,947.42 $/mt; platinum 1,278 vs 1,278.33 $/toz).
- R71: JM supply and demand tables for Pt, Pd, Rh, Ru, Ir 2021-2026f in oz and tonnes (`r71_jm_pgm_2026_supply_demand_tables.csv`, `r71_jm_pgm_2026_key_numbers.csv`). **Correction:** R46's 17.6 t rhodium was South Africa only; total primary supply is 21.8 t in 2025, so upstream's 23 t is 5.5% high; **rc-038 withdrawn**.
- R72: JM totals, supply = primary + secondary and balance all check; oz and tonne rows agree within 0.14 t. Upstream market depth: platinum 180 t vs JM 172.9 t (+4.1%), palladium 210 vs 205.0 (+2.4%); no candidate.

## R74 - Upstream citations registered (+7)

`usgs_mineral_commodity_summaries_2026` (curated fallback prices and world production), `lme_official_reference_prices` (Ni, Co), `cme_comex_nymex_futures` (live Au/Ag/Cu/Pt/Pd basis; spacecost RP-1 and methane proxies), `yahoo_finance_yfinance`, `metals_dev_api`, `reuters_2026_gold_analyst_consensus` (gold context).

## R83 - USGS MCS 2025 hosted; world-production audit (2026-09-30)

economicspace@7d99662 cites *Mineral Commodity Summaries 2025* for the mineral_value 1.11.0 rows; v1.2 hosted. Against `ANNUAL_WORLD_PRODUCTION_KG` (`extracted_data/r83_mcs2025_world_production_key_numbers.csv`):

- Exact: gallium 760,000 kg, molybdenum 260,000 t, rhenium 62,000 kg, tungsten 81,000 t W; phosphate rock 240 Mt matches the phosphorus comment.
- Within rounding: chromium 47,000 kt vs 4.4e10 kg (-6.4%); sulfur 85,000 kt vs 8.3e10 kg (-2.4%); titanium sponge 320,000 t excl. US vs 3.0e8 kg (-6.2%).
- **rc-055:** ammonia 1.8e11 kg N is +20% above 150,000 kt (2024e) and contradicts its own comment "~150 Mt N as ammonia".
- Germanium has no world table ("global production data were limited").

v1.0 and v1.1 carry identical values, so no discrepancy is edition drift.

## R114 - An osmium price source (2026-10-04)

**`ipa_sfa_2026_osmium_pgm_factsheet`** (IPA/SFA Oxford, May 2026; read): osmium has no exchange benchmark or market transparency, is priced per transaction, and has been "fixed in the 300-400$/oz range since the 2000's" (~$9,600-12,900/kg); output is hundreds of kilograms a year. Upstream's $13,000/kg is $404/oz. Cobalt's gap stays open. `extracted_data/r114_gr_links_key_numbers.csv`.

## R115 - Prices against the hosted USGS summaries; five candidates (2026-10-04)

Against economicspace@29a0309 (v1.11.0 elements stamped 2025-01-31, citing MCS 2025):

- **titanium (rc-062):** sponge import value $10.60-13/kg over 2020-2024e vs cell $9 and note $7-10.
- **tungsten (rc-063):** MCS 2025 withholds the price; MCS 2026 gives APT $331 -> $675 per mtu through 2025 ($41.7 -> $85.1 per kg W), the cell ~47% below end-2025.
- **gallium (rc-064):** 2024e $500 (range $450-625); cell $600, the note's $700 not printed.
- **ammonia (rc-065):** $440 per short ton read as $450 per metric ton (it is $485/t).
- **cobalt production (rc-066):** 2.3e8 kg vs 3.10e8 for 2025e (-25.8%; it is Congo alone).
- Agreeing: chromium $12.35/kg vs $10-12; rhenium $1,370 vs $1,200-1,600; molybdenum $47 vs $44; germanium $2,100 vs $2,000-3,000; sulfur $69-116 per long ton vs $80-100/t.

`extracted_data/r115_usgs_new_element_prices_cobalt_production.csv`. Also read live: `metals_dev_api` (live LBMA/LME/MCX feed, free tier).

## R164 / R165 - Candidates (2026-10-14)

rc-125 (osmium market depth), rc-126 (cite the factsheet for the osmium price), rc-141 (palladium to LBMA 2026-05-29 $43,853.6/kg), rc-142 (gold to $145,506/kg), rc-144, rc-145, rc-146 (cite USGS for carbonates, plagioclase, iron ore), rc-147, rc-148, rc-149, rc-150, rc-151, rc-152, rc-153 (re-pin gold, nickel, palladium, platinum, copper, chromium and titanium production to MCS 2026), rc-154 (cite MCS 2026 pig iron). Texts in `revision_candidates.csv` (open) and `revision_candidates_closed.csv`.

Extracted data: `extracted_data/r165_price_cells_vs_registered_sources.csv`.

## R182 - Osmium production and price in full (2026-10-16)

The IPA/SFA factsheet re-read (16 pp):

- p10: "Annual global production of osmium is likely to therefore have been limited to about 500kg-550kg/annum over 2024 and 2025." (companies report none); rc-125 now cites it.
- No exchange, LBMA or JM price exists; Engelhard's (BASF) Industrial Bullion sheet: "Osmium prices have historically been very stable (due to lack of market liquidity), fixed in the 300-400$/oz range since the 2000s."; SFA's 2019-2025 sponge-price reconstruction is a chart (200-500 $/oz axis). Priced "at each transaction between the seller and buyer, including the nominal metal price plus associated fabrication, storage, transport and related costs." rc-126 stays open.
- Losses: nitric acid or peroxide oxidation "forms osmium tetroxide (OsO₄) that goes to vent scrubbers, so any operation that loses ruthenium also loses osmium"; Amplats recovered potassium osmate "until around the year 1990;" and later "concluded recovery was not to be pursued due to complexity and hazard."
- A vendor quote of EUR 54.30/g (EUR 1,688.92/oz, 2026-09-24) runs 4-5x the industrial band; not registered.

`extracted_data/r182_osmium_production_price_key_numbers.csv`.

## R190 - Catalogue audited cell by cell (economicspace@d77f1ce; no candidate)

`asteroid_pipeline/mineral_value_catalog.csv` (59 rows):

- Prices: copper 13,543/t and nickel 18,806/t are WB May-2026 exactly; iridium $257,206/kg and ruthenium $56,263.8/kg are JM's $8,000 and $1,750/oz; platinum 61,472.2 is LBMA via applied rc-034; gold, silver, palladium remain open as rc-142 and rc-141; tungsten 45.0 is the start-2025 level deferred in applied rc-063 (end-2025 ~$85/kg is the owner's call).
- Production: Ga/Mo/Re/W exact (R83); Rh/Ir/Ru within ~6% of JM (R71).
- Yields: the nickel-iron phase carries Pt 15 / Pd 10 / Ru 3 / Ir 4 / Os 2 / Rh 1.5 / Au 1 ppm (~36.5 total); the R72 ratio audit stands.

Do not re-audit unless upstream changes a value or note.

## R336 - Metals.Dev provider timestamps become the retrieval day (2026-11-02)

Sources `metals_dev_api` and `spacevalue_metals_dev_timestamp_record_2026`:
provider documentation at https://www.metals.dev/docs, Latest Endpoint / API
Response and general response-property table; spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011,
`spacevalue/catalog.py`, README, original snapshot and LICENSE;
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f, original quote/delivery dependencies.
The provider calls a timestamp the "date & time the data is collected".
Its latest example carries `timestamps.metal=2023-07-05T06:16:02.829Z`;
the general table also names `timestamp`. This is collection provenance,
not a trading-session close. The adapter instead reads `date` or
`timestamp_iso`, then the current UTC day (catalog.py L2239), and writes
that selection into `live_price_date` (L2253-2257).

Twelve original adapter comparisons replay a field subset of the documented
example through a local HTTP stub. No real credential or live price request
is used. Six supported metals are accepted. With the unchanged provider
example, only the simulated retrieval clock changes:

| simulated retrieval UTC | provider metal date | original live_price_date |
|---|---|---|
| 2026-11-02 12:00 | 2023-07-05 | 2026-11-02 |
| 2026-11-03 12:00 | 2023-07-05 | 2026-11-03 |

The same price payload therefore acquires a different quoted date on replay.
A constructed midnight-boundary response with metal timestamp 2026-11-01
23:59:30Z, read at 2026-11-02 00:00:20Z, is likewise labelled November 2.
Constructed root-timestamp and different metal/currency-date cases also fail
to retain the metal collection date. These five cases isolate field mapping;
they do not report the freshness of an actual API response.

Seven controls cover the already-read legacy date fields, a same-calendar-day
provider timestamp, DEMO/empty keys, HTTP failure and a payload without rates.
Exposing the provider date through the adapter's existing `date` input restores
the expected metadata while every other result column remains exactly equal.
Every original adapter result repeats exactly. All accepted numerical prices
match the unchanged rate-times-troy-ounce conversion independently.

Four complete `build_mineral_value_catalog` pairs include merge, destination
handling, validation and CSV export/readback. Each affected 59-row build has
six `metals.dev` rows whose wrong date survives to disk. Repeating the original
build gives an identical frame; the metadata-only input diagnostic changes
only `live_price_date`, both in memory and after CSV reread. `catalog_date`
continues to record the build day separately. DEMO-key and recorded-snapshot
catalogs are unchanged controls. Two builds from `metals-2026-10-07` at the
two simulated clocks are wholly identical and make no HTTP call.

Verdict: the optional keyed adapter drops available provider collection time
and replaces it with retrieval-day metadata. `rc-267`: preserve the documented
metal timestamp and keep retrieval/catalog time separate. This finding changes
quote provenance, with no numerical price discrepancy in these tests; default
unkeyed and recorded-release behaviour remain effective controls. No current
market-price level, live-service staleness, or published-release corruption is
claimed. `extracted_data/r336_metals_dev_timestamp_provenance.csv`.


## R341 - Henry Hub contract heating-basis link (2026-11-03)

`cme_comex_nymex_futures`, NYMEX Chapter 220 PDF p1, 220101,
calls the gas "consisting essentially of methane" and requires the
then-effective Sabine FERC tariff. Sections 220102.B/C state a 10,000-MMBtu
trading unit and USD/MMBtu pricing. The read establishes the Henry Hub
contract link; it does not establish any market close or the metals,
heating-oil or crude-oil contract specifications.

At spacecost 860bef9902aa67fec705875cd52fdb8e6def159f,
`spacecost/units.py` L69-75 converts this quote with 0.04739 MMBtu/kg,
an implied 50-MJ/kg net basis. The linked tariff's condensed-water definition
and the methane gross/net comparison are recorded in domain 14's R341 block.
Verdict: `rc-275`, gross versus net basis in the methane proxy.
Contract extraction: `extracted_data/r341_henry_hub_contract_basis.csv`.
Calculation record: `14_propellant_consumable_prices/extracted_data/r341_methane_quote_heating_basis.csv`.

## R355 - Open candidates re-checked at current upstream (2026-11-03)

Read at economicspace 54e30b0, spacecost 860bef9, spacevalue 873b91c and
AsteroidCatalog 66fb47a: the 72 open candidates last checked at older commits.
None has been applied or superseded; all stay `open`. Every open row now
stands at those commits. Row-by-row verdicts and locations are in
`extracted_data/r355_candidate_recheck.csv`.

- **Retargeted from economicspace to spacevalue (16), values unchanged.**
  economicspace `modules/mineral_value.py` now says "STAGE 2 DOES NOT PRICE
  ANYTHING ANY MORE" (L4) and re-exports `ANNUAL_WORLD_PRODUCTION_KG` from
  spacevalue (L176). `spacevalue/catalog.py` holds rc-125 and rc-147 to rc-153
  (production depths, L883-L903) and rc-126, rc-141, rc-142, rc-143, rc-145 and
  rc-146 (price rows). rc-121 is now `catalog.py` L2688 with `cargo.py` L137; a
  search of those two files and economicspace `calc.py` still finds no payable
  fraction or treatment or refining charge. rc-177's constant is
  `catalog.py` L342 and is gone from `master.py`; the spacecost figure pair is
  unchanged.
- **Line references updated.** rc-091 is `calc.py` L5320-5329 and L5343 and
  `master.py` no longer holds a copy; the $800/W row is unchanged. rc-134 is
  `calc.py` L845, and its `current_value` no longer sets "flat, whatever the
  entry speed" inside the source comment, which never contained it. rc-135 is
  `delivery.py` L409-412.
- **Notes rewritten, point at issue unchanged.** rc-107: the third-party
  liability note now cites 14 CFR 440.9 but gives no premium basis; value
  1,500,000. rc-166: the hydrolox note re-sources its Isp sentence; 15,200 Wh/kg
  unchanged and no plant-level bound added.
- **Inputs behind wording candidates unchanged.** rc-233 and rc-234:
  `MEASURED_CELL_SECONDS` stays 735, 1,439, 4,737 and 11,676. rc-236: stage
  hardware is 8.0% (gto), 10.3% (cislunar), 11.1% (geo) and 11.4% (mars_orbit).
- **All other reference-table rows** match the checked commit in every cell but
  `pipeline_version`. The secondary homes of rc-185 to rc-190 are byte-identical.

## R356 - Candidates applied upstream (2026-11-04)

104 candidates applied and moved to `revision_candidates_closed.csv`; 35 stay
`open`. Each row's `checked_against` is the merge commit below.

- **AsteroidCatalog 99781b6** (PR #31, 0.13.0, data contract 1.11.0, tag
  `v0.13.0`): 13 candidates.
- **spacevalue 2f0b4f2** (PR #7, 0.3.0, data contract 1.18.0, tag `v0.3.0`): 21
  candidates. rc-177's spacecost half is in spacecost 4c53b6a.
- **spacecost 4c53b6a** (PR #40, 0.15.0, data contract 1.24.0, tag `v0.15.0`):
  62 candidates. Its `CHANGELOG.md` 0.15.0 lists each with the value taken.
  rc-155 took 321 s. Where a candidate offered a value or a note the note was
  taken and the value did not move: rc-090, rc-107, rc-128, rc-129, rc-135,
  rc-166, rc-186, rc-187, rc-230.
- **economicspace d10f4e5** (PR #191, no release): rc-183, rc-233, rc-234,
  rc-235, rc-236, rc-238, rc-240, rc-251, in prose, comments and printed labels.
  No computed value moved.

No catalog, price or quote release was cut and economicspace repinned nothing:
its Stage 1 to 3 inputs stand at their earlier pins until it does.

Still open, not applied:

- rc-134: upstream now says the flat 0.15 is lunar-return class and optimistic
  for faster returns; the entry-speed scaling is not applied.
- rc-185, rc-254: move delivery chains `tests/test_delivery.py` pins for
  economicspace.
- rc-027: what the row covers is undecided.
- rc-202: $12.2M is the geometric centre of the $10-15M band, so the premise
  does not hold as written.
- rc-261, rc-263, rc-279: move cargo floats, so need a calc release; rc-263 also
  needs an eligibility decision.
- The other 27 economicspace method candidates are unchanged.

## R357 - Candidates applied upstream (2026-11-05)

10 candidates applied and moved to `revision_candidates_closed.csv`; 25 stay
`open`. Each row's `checked_against` is the merge commit below.

- **spacecost 19e1a31** (PR #41, 0.16.0, data contract 1.25.0, not tagged):
  rc-185, rc-254. economicspace does not pin this release, so neither moves a
  pipeline number until a tag and a repin.
- **economicspace 2c3dfb4** (PR #192, master 1.62.0, calc 1.35.0): rc-247,
  rc-249, rc-250, rc-255, rc-262, rc-264, rc-278, rc-286. No default number
  moves; each changes a non-default path.

## R358 - Candidates merged upstream (2026-11-05)

2 candidates applied and moved to `revision_candidates_closed.csv`; 23 stay
`open`. `checked_against` on the rows below is the merge commit named here.

- **spacevalue e8ac659** (PR #8, 0.4.0, data contract 1.19.0, not tagged): rc-261,
  rc-263 applied. economicspace pins spacevalue v0.2.0, and rc-261 reaches no
  installed table until a `prices-*` release and a repin.
- **economicspace 4d6525f** (PRs #193 to #196, master 1.66.0, calc 1.39.0): a flag
  that is off by default for each of rc-091, rc-239, rc-241, rc-244, rc-245,
  rc-246, rc-248, rc-252, rc-253, rc-265, rc-266, rc-280, rc-281, rc-282, rc-284,
  rc-285, rc-287, rc-288, rc-289. All 19 stay `open`: the default path each row
  describes has not moved, and `verify.py check --tag pre-gates` matches 151/151
  columns on all four cells. Each flag's measured effect is in upstream
  `versions.md`, releases v1.63.0 to v1.66.0.
- **rc-246**: `carry_ep_home` models one shared stage. On 60 sampled rows, 53
  evaluable, 31 stop closing. The candidate's separate return unit is not built.
- **rc-252**: `price_engineered_hold` takes the candidate's constrained-pricing
  option. R322's six recorded exported-hold sale values replay exactly. The
  market-shaped hold is not built.
- **spacecost 0.16.0** is now tagged `v0.16.0`, which supersedes R357's "not
  tagged". economicspace still pins spacecost v0.14.0.
