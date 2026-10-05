# Domain 20 — Mission operations, communications & ground segment

Backings: spacecost `reference/operational_costs.csv` rows `Mission operations`, `Deep Space Network time`, `Communications relay & data downlink` and `Depot berthing & handover operations`, which the economicspace cost cascade charges per mission-year or per delivery.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Mission operations is charged for every year of every mission, and no registry row names it in its mapping. The downlink row cites nothing, and the berthing row calls itself an estimate. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Mission operations` | $31.4M per mission-year [15M, 100M] | OSIRIS-REx prime operations, $283M over 9 years ("NASA / Planetary Society") |
| `Deep Space Network time` | $1,530 per 34-m hour [1,000, 4,000] | FY09 MOCS rate of $1,057/hr, CPI-adjusted to 2026 |
| `Communications relay & data downlink` | $50 per Mbit returned [10, 200] | none stated |
| `Depot berthing & handover operations` | $2M per delivery [0.5M, 8M] | "ESTIMATE", scaled from ISS visiting-vehicle berthing operations |

**What a source has to supply.**

- Annual operations cost of deep-space missions by class and phase (cruise against proximity operations), preferably budget actuals.
- Current DSN aperture fees, and commercial ground-station and relay pricing.
- Operations cost of visiting-vehicle rendezvous, berthing and cargo handover.
- Evidence on how onboard autonomy changes operations staffing and cost.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `planetary_society_pebd_mission_costs` (domain 7): OSIRIS-REx operations actuals.
- `jpl_dsn_services_catalog_820_100` (domain 5): DSN aperture pricing.

**Boundary.** Domain 7 holds one-time costs, including the autonomy-software NRE and the sample-recovery envelope; this domain holds the recurring cost per mission-year or per delivery.

## R77 - Sources moved in (2026-09-27; registry unchanged at 267)

These rows were registered in other domains before this one existed; they moved here because the cells they back are this domain's. Their earlier write-ups stay in the old domain's FINDINGS.md under the blocks named.

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `jpl_dsn_services_catalog_820_100` | domain 5 | `05_inspace_operations/FINDINGS.md`: Round 44 addition; Maintenance; R71 | `extracted_data/r71_jpl_dsn_820_100_key_numbers.csv`, `extracted_data/r71_jpl_dsn_820_100_table5_1_station_rf_capabilities.csv` |

Revision candidates on these sources, written up in their old domains: rc-030 (open, Deep Space Network time).

The cross-reference to `jpl_dsn_services_catalog_820_100` in the opening block is now a row of this domain.
## R85 - First operating-cost anchors (2026-09-30; registry 309 -> 311)

Two NASA OIG audits, both pulled live from oig.nasa.gov this round and hosted under `full_texts/` (US government work, public domain - the same precedent as the twelve other hosted OIG rows in domains 4-7):

- **nasa_oig_2023_ig-23-016_dsn_audit** [T2] - Audit of NASA's Deep Space Network (Jul 12 2023): DSN oversubscribed (demand exceeds supply by as much as 40 percent; ~60 missions supported); DAEP life-cycle cost **$419M (2010) -> $706M (+68%)** by end FY2022; committed $363.2M FY2010-FY2022 ($184M DSN wedge + $179.2M Construction of Facilities); Phase 1 planned $173.2M (Sep-2018) vs actual partial completion at $120.8M (Table 2, p21).
- **nasa_oig_2015_ig-15-013_dsn_management** [T2] - NASA's Management of the Deep Space Network (Mar 26 2015): **FY2014 DSN budget = $210M** (operations + maintenance + upgrades, JPL Project Office); CSIRO Canberra site ops $19M FY2014 (~100 staff); SCaN cut -$101.3M for FYs 2013-2019 with a $91.7M offset plan (Table 4, p18) and $18.6M inflation exposure; updated DAEP life-cycle cost through FY2025 = **$393.1M** (+$30.7M vs the 2009 estimate, p21); NASA missions do not pay for DSN use unless a unique technology is added (p12).

What they supply this domain's cells:

| cell | anchor |
|---|---|
| `Mission operations` ($31.4M/yr OSIRIS-REx) | IG-15-013 p8: FY2014 DSN budget $210M = the network-wide ops+maintenance+upgrades figure; per-mission share of it is what a chargeable 'mission operations' line approximates - no per-mission breakdown exists in either audit |
| `Deep Space Network time` ($1,530/hr) | IG-23-016: the 40-percent oversubscription explains why DSN time is priced and scarce; **neither audit contains a per-hour aperture fee**, so rc-030's route stays the 820-100 Rev H rate base ($1,792/hr at publication) + BLS CPI-U chain |
| (context) | IG-15-013 p12: NASA missions do not pay for DSN use unless a unique technology is added - the chargeable line applies to non-NASA/unique-tech cases, which is exactly the commercial context of this repo's rows |

Extracted data: `extracted_data/r85_dsn_oig_audits_key_numbers.csv` (12 rows). No revision candidate opened or closed by this round.

## R113 - A commercial antenna price for the downlink row (2026-10-04; +1 source, T4x1)

spacecost `reference/operational_costs.csv` `Communications relay & data downlink` is $50 per Mbit [10, 200] with no source (read at spacecost@85da36c).

**`aws_ground_station_price_list`**: the AWS Ground Station pricing page loads its figures by script, so the public AWS Price List API offer file was pulled live (publicationDate 2026-09-11, 47 products). On-demand antenna time is **$10 per minute narrowband** (<40 MHz instantaneous bandwidth) and **$22 per minute wideband** at most sites, $15 and $25 at Dubbo (Sydney region); reserved pricing is by contract.

Two limits. AWS serves LEO/MEO spacecraft, not deep space, so it prices only near-Earth phases (delivery to LEO or a GEO depot); the cruise and proximity-operations downlink still rests on DSN pricing (`jpl_dsn_services_catalog_820_100`). And the price list gives no data rate, so converting $/minute to the row's $/Mbit needs a link-rate assumption this repo does not make. Two secondary GSaaS price guides on the owner's list were rejected in favour of this primary price list (Round 113 log entry). No revision candidate.

Extracted data: `extracted_data/r113_aws_ground_station_prices.csv` (22 on-demand rates + the upstream cell).

## R114 - DSN aperture-fee history and two mission-level DSN bills (2026-10-04; +4 sources, T1x1, T2x3)

rc-030 (`Deep Space Network time`, $1,530/hr, 26.5% below the Rev H-based $2,082) is unchanged. `nasa_mocs_2014_dsn_aperture_fee_algorithm` supplies the document upstream's note cites: AF = RB [AW (0.9 + FC/10)] with RB '$1057/hr. for FY09' and AW 0.80 (34 m high-speed beam waveguide), 1.00 (other 34 m), 4.00 (70 m or a four-dish array) (p17). At one contact a week the fee is RB x AW, so a standard 34 m hour was $1,057 in FY09; with the registered Rev H base of $1,792 (2022) that is a 70% rise over thirteen years (computed here). Two NASA concept studies carry mission-level bills from the JPL tool: `nasa_2021_uranus_orbiter_and_probe_decadal_mission_concept_study` ($21.3M of Phase E DSN charges) and `clark_2023_compass_jupiter_heliophysics_mission_concept_study` ($28.5M for a 5.5-year cruise with three 8-hour passes a week). Both describe the pass pattern in prose, so no hourly rate can be backed out of them.

`remer_1992_modeling_dsn_costs_future_space_missions_major_cost_drivers` is registered from its record (probably a capital-cost model). Undecided: the PERSEUS Uranus mission paper (Springer challenge), two yumpu copies of the Rev C/E catalogs (bot check). Rejected: the DSN 'fees' page (it now serves the home page), the mission-documents landing page, the Stack Exchange answer that restates the MOCS formula, and two satellite-price pages (Round 114 log entry).

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.
