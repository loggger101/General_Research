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
