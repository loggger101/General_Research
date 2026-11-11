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

## R324 - Ground recovery is multiplied by the downleg departure mass ratio (2026-11-02)

Source `spacecost_downleg_recovery_mass_ratio_record_2026`:
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f, `spacecost/delivery.py`,
`operations.py` and `reference/operational_costs.csv`;
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011, `spacevalue/catalog.py`
and its committed terrestrial-price fixture;
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0, `modules/calc.py`.
The recovery row's unit is "USD per recovery" (operational CSV L35), with
value 15M USD, explicitly an estimate rather than a published NASA standalone
recovery cost. delivery.py L416 sets a 10,000 kg batch, described as the
"nominal batch the recovery is spread over".

`downleg_cost_usd_per_kg` (L662-686) first calculates recovery as the
per-recovery amount divided by that batch, then returns
`(hardware + recovery) * R`, with `R=exp(departure_dv/(Isp*g0))`.
Its docstring explicitly says all three costs are scaled by departure mass
ratio. Thus this is the implemented costing rule, not an arithmetic typo.
The propellant multiplier also scales the ground recovery of an unchanged
returned-cargo batch. The same operational row is a flat Earth-return cost
in economicspace calc.py L5377-5383.

Eighteen direct configurations call the original helper with nominal, zero
and nominal-plus-1M USD recovery amounts. Zero-recovery subtraction isolates
the component; the perturbation measures sensitivity `R/batch`, rather than
`1/batch`. Independent 50-digit Decimal exponentials reproduce the outputs.
For the unchanged 10,000 kg batch, a source rate of 15M USD becomes:

| downleg origin | departure m/s | R | implied recovery per batch, M USD | additional deduction, USD/kg |
|---|---|---|---|---|
| LEO | 120 | 1.026665 | 15.399968 | 39.9968 |
| GTO | 16 | 1.003515 | 15.052723 | 5.2723 |
| GEO | 1,490 | 1.386452 | 20.796776 | 579.6776 |
| cislunar | 450 | 1.103715 | 16.555732 | 155.5732 |
| lunar surface | 2,700 | 1.807769 | 27.116529 | 1,211.6529 |
| Mars orbit | 900 | 1.218188 | 18.272819 | 327.2819 |
| Mars surface | 6,200 | 3.894719 | 58.420790 | 4,342.0790 |

The comparison holds ground recovery at `C/batch`, preserving the existing
hardware multiplier and all other constants. For Mars surface this changes
the total downleg deduction from 96,394.3034 to 92,052.2244 USD/kg. It is a
recovery-term diagnostic, not a complete departure-stage cost reconstruction.
Seven zero-departure cases agree exactly at R=1. Earth-surface and unknown
destinations retain zero downleg costs. Doubling the nominal batch halves
the per-kg recovery term but still attributes `C*R` to one complete batch.

The unchanged spacevalue route chooser (catalog.py L1235-1242) subtracts
this fee from terrestrial value before choosing the better route and
flooring at zero. A wrapper changing only the recovery term was compared
against the original on all 59 terrestrial-price rows of the committed
2026-10-07 Earth-surface fixture at eight destinations: 472 paired helper
calls, with 38 price increases and no route changes. Earth-surface values
and commodities staying on the in-space-use route remain unchanged.
Mars-surface rhodium moves from 223,605.6966 to 227,947.7756 USD/kg; cislunar
rhodium moves from 292,683.0414 to 292,838.6147 USD/kg. Missing terrestrial
prices remain missing on Earth. These are repricings from recorded inputs,
not new market quotes, regenerated full catalogues or ranking results.

Verdict: the formula turns a per-recovery ground cost into a departure-mass
charge without changing the recovery count or returned batch.
`rc-254`: separate fixed ground recovery from departure-mass costs.
Neither the adopted recovery estimate nor its empirical uncertainty is
revised here. `extracted_data/r324_downleg_ground_recovery_mass_ratio.csv`.

## R379 - DSN rate refreshed through September CPI-U (2026-11-08)

At `spacecost@19e1a31`, the `Deep Space Network time` row is $2,082 per 34-m hour, calculated from the Rev H $1,792/hour rate base using CPI-U through August 2026 (factor 1.1617); its note gives ~$6,245/hour for a 70-m antenna at 3x weighting. The already-registered `fred_cpiuacsl_monthly_usd_series` reports CPIAUCSL 334.131 for August and 336.298 for September 2026. September was the latest published observation on this round's date.

Carrying the stated August factor forward by 336.298 / 334.131 gives an approximate September factor of 1.169234. This yields about $2,095.27 per 34-m hour and $6,285.80 per 70-m hour, 0.64% above the current 34-m value; the result inherits the source note's four-decimal August factor. The $1,000-$4,000 range continues to bracket the point estimate.

Verdict: `rc-297` proposes refreshing the rate note and point estimate to the latest published CPI-U month; no DSN base rate or uncertainty range changes. `extracted_data/r379_dsn_rate_cpi_refresh.csv`.


## R380 - Relay-cost method depends on transmitted-data time (2026-11-08)

At `spacecost@19e1a31`, `Communications relay & data downlink` is $50 per Mbit returned [10, 200], with the note “Ka-band; relevant only for high-rate science / 3-D maps.” No data rate, pass pattern, or service-cost basis is stated.

The registered NASA/JPL `nasa_mocs_2014_dsn_aperture_fee_algorithm` §2.1.5 (PDF p.17) covers data from a landed object relayed through an orbiting spacecraft to a DSN station. It allocates a pro-rata share of DSN station cost using a one-hour minimum and excluding station configuration time; the guide calculates “the time required to return the total amount of relayed data.” This is a NASA DSN planning method for a specific relay architecture, not a commercial $/Mbit quote; it cannot set the upstream row’s numeric rate.

Verdict: `rc-298` asks to separate relay and direct-downlink scope and state transfer-rate/pass assumptions before representing the estimate as a general $/Mbit cost. The value and range remain unchanged. `extracted_data/r380_nasa_mocs_relay_costing_method.csv`.
## R564 — DSN rate uses the latest published CPI-U month (2026-11-10)

At spacecost@d3e594fe0968eeaee4f2c02dd2c76334eab8bb2c, the 34-m DSN hour is $2,095 using the September 2026 CPI-U factor; the 70-m comparator is about $6,286. `rc-297` applies the same-quantity price update; the source is the JPL Rev H hourly rate carried by the BLS CPI-U series.

## R565 — DSN rate rechecked against the applied release (2026-11-10)

Spacecost 0.17.0 / data contract 1.26.0, at main commit `aaed2720ee44610c5cf90fc204db160deb5669bb`, carries the JPL Rev H $1,792 34-m rate to September 2026 CPI-U as $2,095; its 70-m comparator is about $6,286. The current row agrees with the rc-297 proposal. Candidate rechecked against the release commit; applied.
