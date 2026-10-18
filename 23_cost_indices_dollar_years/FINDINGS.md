# Domain 23 — Cost indices, dollar years & exchange rates

Backings: the `reference_year` column of every spacecost reference table and the escalation factors written into row notes (`operations.py` DSN rate, `vehicles.py` Minotaur IV, Space Shuttle and Saturn V), plus the exchange rates behind prices quoted in other currencies: the rule that turns a value quoted in one year's money into the 2026 dollars every row claims.

Created in Round 76 (2026-09-27). Blocks are appended one per round, newest last.

## R76 - Domain opened (2026-09-27; no sources yet)

Every spacecost table row says `reference_year` 2026, but escalation exists only in row notes, several values carry earlier dollars unescalated, and the written factors name no index. Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `reference_year` in `launch_vehicles.csv`, `operational_costs.csv`, `propellants.csv`, `storage_systems.csv` | 2026 on all 182 rows (76 + 45 + 41 + 20) | a label; no escalation step in the code |
| `launch_vehicles.csv` Atlas V 551 | $153M list price | "ULA RocketBuilder $153M base (2016)"; not escalated |
| `launch_vehicles.csv` Pegasus XL | $40M list price | "$40M (2017)"; not escalated |
| `launch_vehicles.csv` Minotaur IV, high end | ~$50M (2010) x 1.45 | "carried to 2026 dollars by CPI (x1.45)"; index and years not named |
| `launch_vehicles.csv` Space Shuttle, high end | ~$1.5B (2011) x ~1.44 | "carried to 2026 dollars (~x1.44)" |
| `launch_vehicles.csv` Saturn V | ~$185M per vehicle in 1969-73 dollars | no factor or index stated |
| `launch_vehicles.csv` Ariane 5 ECA, PSLV-XL | "€150-190M vehicle cost"; "₹130-200 crore ($16-24M, 2023)" | exchange rate and date not stated |
| `operational_costs.csv` `Deep Space Network time` | $1,530/hr = FY09 $1,057 x 1.45 | "CPI-adjusted" (R50: matches a World Bank chain, x1.4570) |
| `operational_costs.csv` `Spacecraft development (NRE)`, `Mission operations` | $588.5M "actual"; $283M over 9 years | OSIRIS-REx figures, no dollar year |

**What a source has to supply:** official index series with base years (CPI, NASA New Start Inflation Index, a GDP deflator); guidance on which index suits which cost class (PEBD uses NNSI for development and an employment-cost index for operations after 2000); official annual exchange-rate averages.

**Also relevant, registered elsewhere:** `planetary_society_pebd_mission_costs` (d07; NNSI and ECI tables in `r73_pebd_reference_indices.csv`), `jpl_dsn_services_catalog_820_100` (d20).

**Boundary:** dollar values stay with their domains (launch 4, programmes 7, operations 20, hardware 21); this domain holds the indices, exchange rates and the rule for applying them. Commodity spot prices (domain 6) are dated quotes, not escalated costs.

## R78 - First sources (2026-09-27)

Registered as T3 open services: `fred_cpiuacsl_monthly_usd_series` (CPI-U via FRED's fredgraph.csv, 1947 to Aug-2026; the BLS keyless API rejects the series), `world_bank_usa_annual_cpi_inflation` (WDI FP.CPI.TOTL.ZG; the older id PC.PIX.FACD is rejected by the API) and `world_bank_official_fx_averages_deu_ind` (IFS PA.NUS.FCRF, DEU and IND). Factors in `extracted_data/r78_index_factors_and_fx_averages.csv`.

**Upstream's method identified:** the World Bank annual chain reproduces every written factor: 2009..2024 = x1.4570 (DSN, exact), 2010..2024 = x1.4622 (Minotaur IV ~x1.45), 2011..2024 = x1.4386 (Shuttle ~x1.44). The notes use a World Bank chain read through Dec-2024, not CPI-U to the present.

**Run to Aug-2026:** Minotaur IV x1.5155, so the note is ~4% low (**rc-050**); Atlas V 551 $153M (2016) -> ~$211M at x1.3771 (**rc-051**); Pegasus XL $40M (2017) -> ~$54M at x1.3484 (**rc-052**). Saturn V 1970-73 -> Aug-2026 = x~7.88 ($185M -> ~$1,457M); no candidate, since the row's band is already mixed-year. rc-030 (DSN) stays open on the superseding Rev H rate of $1,792.

**Exchange rates:** PSLV-XL implies INR/USD 81.25-83.33 against the official 2023 average of 82.60, consistent. Ariane 5 ECA implies USD/EUR 1.100-1.158 with no stated year; official averages were >=1.10 only before 2022 (2021: 1.183) and from 2025 (1.130), 2023 = 1.081 and 2024 = 1.082, so the band fits several years and is pinned to none.

## R113 - NASA New Start Inflation Index as a standalone series (2026-10-04)

**`nasa_new_start_inflation_index_fy26`** (NASA OCFO workbook, actuals through September 2025, hosted). Annual rates: FY2024 3.25%, FY2025 3.79%, FY2026 3.21% (projected), FY2027 2.47%. Cumulative: FY2009 to FY2024 x1.4261; to FY2026 from FY2009 x1.5278, FY2010 x1.5071, FY2011 x1.4832; FY1969 to FY2026 x11.0714.

Over 2009-2024 NNSI is 2.1% below the CPI chain upstream used (x1.4570); carried to FY2026 it is 4.9% above upstream's CPI-to-2024 factor. No candidate until upstream picks an index per cost class. `extracted_data/r113_nasa_nnsi_fy26_factors.csv`.

## R140 - The operations index PEBD uses: BLS ECI CIU1010000000000A (2026-10-09)

**bls_eci_total_compensation_us_all_industries_ciu1010000000a** [T3 open service]: total compensation, all civilian workers, 12-month % change, the series PEBD's NAICS sheet names. Pulled from the keyless BLS API (10-year windows; Q1-2001 to Q2-2026, 102 points). All 98 quarters overlapping PEBD's copy match exactly; PEBD's cumulative "Wage Inflation Factor" is exactly the product of its rounded annual mean factors through CY2024 (24 rows); recomputed from the live API it differs by at most 0.36% (FY2002, vintage revisions).

**Convention trap:** ECI quarterly values are annualised 12-month changes; compounding them quarter by quarter overstates growth; a per-quarter factor is (1+pct/100)^(1/4). PEBD compounds annual means instead.

Factors: FY2017 -> Q4-2025 x1.3536, FY2014 x1.4417, FY2009 x1.5825 (to Q2-2026: x1.376 / x1.466 / x1.609); in PEBD's convention through CY2024: x1.353651 / x1.441792 / x1.582508. Peak Q2-2022 5.1%, trough Q4-2009 1.4%. Over FY2009-2024 ECI gives x1.5286 vs the World Bank CPI chain's x1.4570 (~4.9% apart), so the index choice matters for operations rows. No re-pin.

`extracted_data/r140_eci_series_key_numbers.csv`.

## R145 - GDP deflator: FRED GDPDEF (2026-10-09)

**fred_gdpdef_quarterly_usd_series** [T3 open service]: BEA implicit price deflator, Q1-1947 to Q1-2026 (318 obs). GDPC1 is real GDP, not the deflator. Factors to Q1-2026 (`extracted_data/r145_gdpdef_key_numbers.csv`): FY2009 x1.5067, 2014 x1.3928, 2016 x1.3684, 2017 x1.3423, each ~4% below CPI-U to the same quarter (FY2009: x1.5724). Consumer-price escalation overstates production-side cost growth by ~4% on long spans. No cell names GDPDEF yet, so no re-pin.

## R185 - OSIRIS-REx development anchor (rc-168; 2026-10-17)

The $588.5M 'Spacecraft development (NRE)' anchor is nominal FY2011-FY2016 obligations per PEBD (Total Cost 772.0 minus Launch Vehicle 183.5) while the row says reference_year 2026. rc-168 proposes CPI-U Sep-2026/Dec-2014 x1.4235 (dollar-weighted centre calendar 2014) -> ~$837.7M, following rc-051's precedent (applied in spacecost 0.6.0).

## R186 - OSIRIS-REx operations anchor (rc-169; 2026-10-17)

'Mission operations' $31.4M/yr comes from the "$283M over 9 yr" plan, nominal FY2017-FY2025 obligations (PEBD per-FY 26.2 ... 5.4, Totals 232.2). rc-047 fixed the note wording only; rc-092 is the matching wording item on the sample-recovery row. rc-169 proposes CPI-U Sep-2026/Dec-2019 x1.2992 (centre calendar 2019.95) -> ~$40.8M/yr (Dec-2018 base x1.3228, Dec-2020 x1.2834: ~$41.5M / ~$40.3M). FRED was down, so L(Sep-2026)=336.298 comes from rc-168's pull and L(Dec-2024)=317.604 from r78, bridged to Dec-2019 by the World Bank chain x1.226989 (the same convention reproduces r78's x1.4622 / x1.4570 and agrees with FRED within 0.15% over 2016-2024). Replace the bridge with a direct FRED pull when it answers.
