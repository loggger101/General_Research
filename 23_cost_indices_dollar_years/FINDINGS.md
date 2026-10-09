# Domain 23 — Cost indices, dollar years & exchange rates

Backings: the `reference_year` column of every spacecost reference table and the escalation factors written into row notes (`operations.py` DSN rate, `vehicles.py` Minotaur IV, Space Shuttle and Saturn V), plus the exchange rates behind prices quoted in other currencies: the rule that turns a value quoted in one year's money into the 2026 dollars every row claims.

Created in Round 76 (2026-09-27). Blocks are appended one per round, newest last.

## R76 - Domain opened (2026-09-27; no sources yet)

Every row of the four spacecost tables says `reference_year` 2026, and the only escalation in the code base is in row notes. Several values are quoted in an earlier year's dollars with no escalation, and the factors that are written down name no index. R50 (domain 5) pulled BLS CPI-U and a World Bank inflation chain to audit the DSN rate, and R73 (domain 7) extracted PEBD's NASA New Start Inflation Index, but neither index series is registered as a source. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `reference_year` in `launch_vehicles.csv`, `operational_costs.csv`, `propellants.csv`, `storage_systems.csv` | 2026 on all 182 rows (76 + 45 + 41 + 20) | a label; no escalation step appears in the code, only in row notes |
| `launch_vehicles.csv` Atlas V 551 | $153M list price | "ULA RocketBuilder $153M base (2016)"; not escalated |
| `launch_vehicles.csv` Pegasus XL | $40M list price | "$40M (2017)"; not escalated |
| `launch_vehicles.csv` Minotaur IV, high end | ~$50M (2010) x 1.45 | "carried to 2026 dollars by CPI (x1.45)"; index and years not named |
| `launch_vehicles.csv` Space Shuttle, high end | ~$1.5B (2011) x ~1.44 | "carried to 2026 dollars (~x1.44)"; the row mixes dollar years on purpose |
| `launch_vehicles.csv` Saturn V | ~$185M per vehicle in 1969-73 dollars, "carried to 2026 dollars" | no factor or index stated |
| `launch_vehicles.csv` Ariane 5 ECA, PSLV-XL | "€150-190M vehicle cost"; "₹130-200 crore ($16-24M, 2023)" | exchange rate and date not stated |
| `operational_costs.csv` `Deep Space Network time` | $1,530/hr = FY09 $1,057 x 1.45 | "CPI-adjusted"; R50 found the factor matches a World Bank chain (x1.4570) |
| `operational_costs.csv` `Spacecraft development (NRE)`, `Mission operations` | $588.5M "actual"; $283M over 9 years | OSIRIS-REx figures with no dollar year stated |

**What a source has to supply.**

- Official price-index series with their base years (a consumer price index, NASA's New Start Inflation Index, a GDP deflator), so every escalation can name its index and the years it spans. These are T3 datasets.
- Guidance on which index suits which cost: launch services, spacecraft hardware, labour-dominated operations. PEBD, for one, uses NNSI for development and an employment-cost index for operations after 2000.
- Official exchange-rate series (annual averages) for the currencies non-US prices are quoted in.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `planetary_society_pebd_mission_costs` (domain 7): NNSI and employment-cost index tables extracted in `r73_pebd_reference_indices.csv`.
- `jpl_dsn_services_catalog_820_100` (domain 5): the DSN rate R50 re-escalated with CPI-U.

**Boundary.** The dollar values stay with their own domains (launch prices in 4, programme costs in 7, operations in 20, hardware rates in 21); this domain holds the indices, the exchange rates and the rule for applying them. Commodity spot prices (domain 6) are dated quotes, not escalated costs.

## R77 - Cross-references updated (2026-09-27; registry unchanged at 267)

`jpl_dsn_services_catalog_820_100`, listed in the opening block under domain 5, is now in domain 20.
## R78 - First sources registered (2026-09-27; registry 267 -> 270)

The four index and exchange-rate services the upstream notes rely on were pulled live from this machine, verified against every written escalation factor, and registered as T3 `open_service` rows. The BLS publicAPI v2 endpoint is keyless-broken from here ('Invalid Series' for CPIAUCSL in both GET and POST forms); FRED's fredgraph.csv serves the same series with full history (1947..Aug-2026) and reproduces R50's data.bls.gov values within ~0.1% vintage drift, so it is now the canonical route to CPI-U.

**Registered.** `fred_cpiuacsl_monthly_usd_series` (FRED/BLS monthly index), `world_bank_usa_annual_cpi_inflation` (WDI FP.CPI.TOTL.ZG, per-year actuals through 2024; the id PC.PIX.FACD from earlier notes is rejected by the current API) and `world_bank_official_fx_averages_deu_ind` (IFS PA.NUS.FCRF for DEU + IND). Key factors committed in `extracted_data/r78_index_factors_and_fx_averages.csv`.

**The written factors, re-derived.** The World Bank annual chain reproduces every factor upstream has written down: 2009..2024 = x1.4570 (R50's DSN factor, exact), 2010..2024 = x1.4622 (Minotaur IV note ~x1.45) and 2011..2024 = x1.4386 (Shuttle note ~x1.44). The notes' method is thus identified — a World Bank annual-inflation chain read through Dec-2024, not CPI-U to the present.

**What changes when the same method runs to Aug-2026.** Minotaur IV: x1.5155 (CPI-U) vs the note's 1.45 — under-escalated by ~4% (**rc-050**). Atlas V 551 and Pegasus XL carry earlier-year quotes with NO escalation at all despite `reference_year` 2026: $153M (2016) -> ~$211M x1.3771 (**rc-051**), $40M (2017) -> ~$54M x1.3484 (**rc-052**). Saturn V's 'carried to 2026 dollars' names no factor; Dec-avg(1970..73)->Aug-2026 = x~7.88, i.e. $185M -> ~$1,457M (no candidate: the row already carries a mixed-year band and its low end is explicitly a 2020-dollar figure). The DSN note's own FY09->CPI method stays internally consistent at -0.65% vs R50; rc-030 remains open on supersession by Rev H's official $1,792 rate.

**Exchange rates.** PSLV-XL's 'Rs 130-200 crore ($16-24M, 2023)' implies INR/USD 81.25-83.33 and matches the official 2023 period average (82.60) — consistent with its stated year. Ariane 5 ECA's $ band on a EUR 150-190M cost implies USD/EUR 1.100-1.158; the row states no date, and official averages were >=1.10 only pre-2022 (last: 2021 x1.183) and again from 2025 (x1.130), with 2023 = 1.081 and 2024 = 1.082 — the band is plausible for several years but pinned to none of them.

**Still open in this domain.** Which index suits which cost class (PEBD's NNSI-for-development / employment-index-for-operations split is extracted under `planetary_society_pebd_mission_costs`, domain 7, and remains the only guidance registered); NASA New Start Inflation Index as a standalone series; escalation of the OSIRIS-REx 'actual' figures in operational_costs.csv (no dollar year stated upstream).

## R113 - The NASA New Start Inflation Index as a standalone series (2026-10-04; +1 source, T3x1)

The opening block names NNSI as the missing index; until now it was available here only as PEBD's copy (`r73_pebd_reference_indices.csv`).

**`nasa_new_start_inflation_index_fy26`**: NASA OCFO's workbook (FY25 tables for use in FY26, actuals through September 2025), linked from the PP&C Models & Tools page and hosted. Annual rates: FY2024 3.25%, FY2025 3.79%, FY2026 3.21% (projected), FY2027 2.47%. Cumulative factors: FY2009 to FY2024 x1.4261; to FY2026 from FY2009 x1.5278, FY2010 x1.5071, FY2011 x1.4832; FY1969 to FY2026 x11.0714.

Against the escalations upstream writes into row notes: R78 showed they follow a World Bank CPI chain read through 2024 (2009..2024 x1.4570). Over that span NNSI gives x1.4261, **2.1% lower** than CPI. The larger difference is the end year: every row claims 2026 dollars, and NNSI carries FY2009 to FY2026 at x1.5278, 4.9% above the CPI-to-2024 factor upstream used. Which index suits which cost class (NNSI for development, an employment-cost index for operations, as PEBD does) is still the open question in this domain; no revision candidate until upstream picks an index.

The FY2018 NNSI table on the owner's list was rejected as superseded by this release (Round 113 log entry).

Extracted data: `extracted_data/r113_nasa_nnsi_fy26_factors.csv` (13 rows; the CPI comparison row is computed here).

## R140 - The operations-cost index PEBD actually uses: BLS ECI CIU1010000000000A (2026-10-09; +1 source, T3x1)

The R76 opening block and the R113 NNSI note both flagged that d23 was missing its third index class: CPI-U for general escalation, NNSI for development costs - but PEBD escalates OPERATIONS with an employment-cost index it embeds in its own workbook (the NAICS sheet), which had no standalone source row. That sheet's metadata block names the series exactly: BLS Employment Cost Index (NAICS) CIU1010000000000A, 'Total compensation for All Civilian workers in All industries and occupations', United States National, 12-month percent change, not seasonally adjusted.

The keyless api.bls.gov publicAPI v2 endpoint serves this series from this machine (no API key; each request is capped at a 10-year window - three windows pulled: Q1-2001..Q2-2026 = 102 points). Identity with PEBD's copy was verified point-by-point after re-pulling the live workbook (sha256 a6e7b08b...; 'Last Update' stamp still 2025-11-13, so the byte drift from R73's b04ec625... pull is export variance, not data change): all 98 overlapping quarterly values are EXACT (max difference 0.0000 pct-pts). The cumulative column then cracked open: PEBD's 'Wage Inflation Factor' for FY y is EXACTLY the product of its own rounded annual 'Average' factors from CY y through CY2024 - verified with zero deviation across all 24 rows. Recomputing that same convention from the live API deviates by at most 0.36% (FY2002; BLS vintage revisions since their snapshot).

One convention trap worth recording: BLS ECI quarterly values are ANNUALIZED percent changes (each quarter reports the % change over the prior twelve months), so compounding them naively quarter-by-quarter OVERSTATES growth by roughly an order of magnitude on long horizons - a true per-quarter factor is (1+pct/100)^(1/4). PEBD sidesteps this entirely: its cumulative column compounds ANNUAL mean factors, and the two conventions agree within ~0.01% on FY2009-2017 horizons anyway.

Escalation factors computed from the live series (key-numbers CSV): FY2017 -> Q4-2025 x1.3536, FY2014 -> x1.4417, FY2009 -> x1.5825; through the latest point (Q2-2026) x1.376 / x1.466 / x1.609 respectively. In PEBD's own annual-mean-factor convention through CY2024: FY2017 x1.353651, FY2014 x1.441792, FY2009 x1.582508 - the conventions agree within 0.01% at these horizons. Series extremes over 2001..2026: peak Q2-2022 at 5.1%, trough Q4-2009 at 1.4%.

Match quality: no re-pin - both operational_costs.csv rows ('Mission operations' and 'Deep Space Network time') already sit at reference_year=2026, so this row registers the institutional index behind any future dollar-year conversion of those anchors (and closes d23's third index class). For context on which index suits which cost class: over FY2009..FY2024 a World Bank CPI chain gives x1.4570 while ECI gives x1.5286 - the two differ by ~4.9% at that horizon, so picking the right series for an operations row is not cosmetic; NNSI stays the development-cost series (R113).