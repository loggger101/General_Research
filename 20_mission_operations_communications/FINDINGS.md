# Domain 20 — Mission operations, communications & ground segment

Backings: spacecost `reference/operational_costs.csv` rows `Mission operations`, `Deep Space Network time`, `Communications relay & data downlink` and `Depot berthing & handover operations`, which the economicspace cost cascade charges per mission-year or per delivery.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Mission operations` | $31.4M per mission-year [15M, 100M] | OSIRIS-REx prime operations, $283M over 9 years ("NASA / Planetary Society") |
| `Deep Space Network time` | $1,530 per 34-m hour [1,000, 4,000] | FY09 MOCS rate of $1,057/hr, CPI-adjusted to 2026 |
| `Communications relay & data downlink` | $50 per Mbit returned [10, 200] | none stated |
| `Depot berthing & handover operations` | $2M per delivery [0.5M, 8M] | "ESTIMATE", scaled from ISS visiting-vehicle berthing operations |

**What a source has to supply:** annual operations cost of deep-space missions by class and phase (budget actuals preferred); current DSN aperture fees and commercial ground-station and relay pricing; rendezvous, berthing and handover operations cost; how onboard autonomy changes operations staffing.

**Also relevant, registered elsewhere:** `planetary_society_pebd_mission_costs` (d07; OSIRIS-REx operations actuals).

**Boundary:** domain 7 holds one-time costs (autonomy NRE, sample-recovery envelope); this domain the recurring cost per mission-year or delivery.

## R77 - Sources moved in (2026-09-27)

`jpl_dsn_services_catalog_820_100` moved here from domain 5 (earlier write-ups: `05_inspace_operations/FINDINGS.md` Round 44 addition, Maintenance, R71), with `extracted_data/r71_jpl_dsn_820_100_key_numbers.csv` and `extracted_data/r71_jpl_dsn_820_100_table5_1_station_rf_capabilities.csv`. rc-030 (open, Deep Space Network time) is written up in domain 5.

## R85 - First operating-cost anchors: two OIG DSN audits (2026-09-30)

Both hosted (public domain):

- **nasa_oig_2023_ig-23-016_dsn_audit** (2023-07-12): demand exceeds supply by as much as 40 percent across ~60 missions; DAEP life-cycle cost $419M (2010) -> $706M (+68%) by end FY2022; committed $363.2M FY2010-FY2022 ($184M DSN wedge + $179.2M Construction of Facilities); Phase 1 planned $173.2M by Sep-2018 vs partial completion at $120.8M (Table 2, p21).
- **nasa_oig_2015_ig-15-013_dsn_management** (2015-03-26): FY2014 DSN budget $210M (operations, maintenance, upgrades; p8); Canberra site $19M (~100 staff); SCaN cut -$101.3M over FY2013-2019 with a $91.7M offset plan (Table 4, p18) and $18.6M inflation exposure; DAEP life-cycle cost through FY2025 $393.1M (+$30.7M vs 2009, p21). NASA missions do not pay for DSN use unless a unique technology is added (p12), so the chargeable line fits this repo's commercial case.

Neither audit gives a per-mission operations split or a per-hour fee, so rc-030 still rests on the 820-100 Rev H base ($1,792/hr) plus CPI-U. `extracted_data/r85_dsn_oig_audits_key_numbers.csv`.

## R113 - A commercial antenna price for the downlink row (2026-10-04)

**`aws_ground_station_price_list`** (AWS Price List API offer file, 2026-09-11, 47 products): on-demand antenna time $10/min narrowband (<40 MHz) and $22/min wideband at most sites, $15 and $25 at Dubbo. AWS serves LEO/MEO only, so it prices near-Earth phases; deep-space downlink still rests on DSN pricing. With no data rate, $/minute cannot be converted to the row's $/Mbit without a link-rate assumption. `extracted_data/r113_aws_ground_station_prices.csv`. No candidate.

## R114 - DSN aperture-fee history and two mission-level DSN bills (2026-10-04)

`nasa_mocs_2014_dsn_aperture_fee_algorithm`, the document upstream cites: AF = RB [AW (0.9 + FC/10)] with RB "$1057/hr. for FY09" and AW 0.80 (34 m beam waveguide), 1.00 (other 34 m), 4.00 (70 m or four-dish array) (p17). At one contact a week a 34 m hour was $1,057 in FY09; Rev H's $1,792 (2022) is 70% higher. Mission bills from the JPL tool: `nasa_2021_uranus_orbiter_and_probe_decadal_mission_concept_study` $21.3M of Phase E DSN; `clark_2023_compass_jupiter_heliophysics_mission_concept_study` $28.5M for a 5.5-year cruise at three 8-hour passes a week (no hourly rate recoverable). `remer_1992_modeling_dsn_costs_future_space_missions_major_cost_drivers` registered from its record. `extracted_data/r114_gr_links_key_numbers.csv`.

## R137 - DSN per-mission preparation cost (2026-10-09)

**remer_sherif_buchanan_1992_dsn_modification_costs_model_spaceops** (SpaceOps 1992, NTRS 19940019495, hosted), the sister of the journal paper registered in R114, which NTRS holds without a file: a cost model for DSN modification and enhancement driven by eight mission cost drivers, fitted to Voyager (Uranus), Voyager (Neptune) and Magellan and tested on Viking and MJS. Table 6 actual preparation costs: Voyager(U) $35.9M, Voyager(N) $36.0M, Magellan $32.5M (1987$); Model B within +17.5%/-22.5%, mean error -3.4%. Table 7: a five-year programme with all nine drivers $56,079K actual vs $55,573K modelled (-1%). MJS ten-year actual 97.5 ($M) vs 111.15 predicted (~14% high); Viking five-year actual 49.7 ($M), 3.8% off. A ceiling-class source for DSN preparation a mission must fund; the operational_costs rows price recurring service. `extracted_data/r137_dsn_modification_costs_key_numbers.csv`.

## R142 - Berthing/handover: CRS per-mission actuals (2026-10-09)

**nasa_oig_2018_ig-18-016_commercial_resupply_services_audit** (2018-04-26, hosted): CRS-1's 31 missions $5.9B, average $191.3M; CRS-2 maximum value $14B, SpaceX $152.1M average over 20 missions, Orbital ATK $262.6M over 11; Sierra Nevada's Atlas V list price $175M; NASA's cadence option would cut the average to $68,800/kg (from $71,800) and $12M per mission. The $2M/delivery handover cell sits far inside a $150-260M delivery; no per-handover line exists, so no re-pin. `extracted_data/r142_crss_berthing_key_numbers.csv`.

**nasa_2026_isam_state_of_play** (NASA LaRC, NTRS 20260008638, 454 pp, hosted): catalogue of RPOD and servicing programmes with budgets, e.g. Astroscale K Program $77M over 5 years (chemical refuelling, GEO EP refuelling), Lockheed Martin CDM $89.7M (cryogenic fluid management), Flight Works PUMA $5.7M. Capability-side context only.

## R215 - verification-worksheet seam: depot handover ops row (rc-182) (2026-10-20)

The deferred economicspace verification-sheet run completed 2026-10-20; its full ledger declares 95 NEED BACKING inputs out of 131. Claim-mapping the live-consumed class against all open candidates left one gap, opened as rc-182: the Depot berthing & handover operations row (USD per delivery) feeds economicspace end-of-mission economics at worked_calculation.py line 2672 with zero citations upstream, and its note self-declares ESTIMATE while scaling from ISS visiting-vehicle berthing ops without naming a document; the sibling Sample recovery operations row it scales against concedes NASA has not published a standalone figure. The pair is mutually-referencing estimates - IG-18-016 CRS per-delivery actuals (rows above) are the ceiling anchors proposed as bound references, values untouched.

Also recorded without registering: the Volatile cargo containment note at spacecost@29a7ced says its charge is 'Charged on WATER only, which is what the citation covers', but no entry in CITATIONS.md @29a7ced covers cargo containment or sublimation loss (the only Water token anywhere is the title of the Kleinhenz and Paz ISRU production paper) - a dangling referent. The value itself (0.05 kg containment per kg volatile cargo) is an engineering ratio argued from sublimation physics in the note, so no candidate was opened this round; if a future round finds the intended citation or its replacement, that seam is live.
