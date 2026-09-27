# Domain 25 — Net smelter return: refining charges & payable terms

Backings: economicspace `modules/calc.py` `_mineral_implied_value` (mirroring `modules/mineral_value.py` `mineral_to_element_value`), which values every yield-priced phase as the sum of its element yields times the element prices, and the refined-metal basis of those prices (`iron` "Priced as refined steel scrap").

Created in Round 76 (2026-09-27). Blocks are appended one per round, newest last.

## R76 - Domain opened (2026-09-27; no sources yet)

A kilogram of returned alloy or concentrate is credited with all of its contained metal at the refined-metal price: no payable fraction, no treatment or refining charge, no refinery loss. The assumption is not written down upstream, so it has no stated basis at all. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` `_mineral_implied_value` | $/kg = sum of yield x element price (PGM and Au yields scaled by `pgm_enrichment`) | implicit; no payable fraction, charge or refinery-recovery term |
| `mineral_value.py` `nickel-iron` phase | Fe 0.900, Ni 0.090, Co 0.005; Pt 15 ppm, Pd 10 ppm, other PGMs and Au 1-4 ppm | each element valued as refined metal (the yields themselves are domain 2's) |
| `mineral_value.py` `native-pgm` phase | Pt 0.70, Pd 0.15, Ir 0.08, Os 0.05, Ru 0.01, Rh 0.01 | each metal valued at its full refined price |
| `mineral_value.py` `iron` price basis | $0.50/kg | "Asteroid mining produces refined iron from nickel-iron alloy, NOT iron ore" |

**What a source has to supply.**

- Commercial terms for selling nickel-copper-PGM concentrates and mattes: payable percentages by metal, treatment and refining charges, penalty elements.
- Refinery recoveries for PGMs, and for nickel and cobalt from iron-rich feeds.
- What iron-nickel metal with ppm-level PGMs would actually fetch: which terrestrial product it resembles (steel scrap, ferronickel, nickel pig iron) and how that product is priced.
- Terrestrial processing routes suited to metallic meteoritic material.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `nat_dms2023` (domain 2): metal extraction from asteroid proxies.
- `jm_pgm_market_report_2026` (domain 6): refined PGM prices.
- `lbma_precious_metals_fixings` (domain 6): refined precious-metal prices.

**Boundary.** Domain 2 holds the yields (what the body contains); domain 6 holds the refined-metal prices; domain 19 holds recovery at the asteroid (`beneficiation_recovery`). This domain holds the step from contained metal delivered to Earth to cash received.
