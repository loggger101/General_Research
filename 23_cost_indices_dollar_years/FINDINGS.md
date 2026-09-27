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
