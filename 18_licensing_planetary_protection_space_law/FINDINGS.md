# Domain 18 — Licensing, planetary protection & space-resource law

Backings: spacecost `reference/operational_costs.csv` rows `FAA Part 450 licensing compliance` and `FAA Part 450 licensing (launch only)`, the MPL requirement behind `Third-party liability insurance`, and the licence split by `delivery_destination` in economicspace `modules/calc.py`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

The licensing rows cite FAA.gov and CRS R48582 (registered, not read), so it is not known whether either supports the dollar figures. Two regulatory premises of the pipeline, planetary protection on Earth return and the right to sell what is mined, have no source. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `FAA Part 450 licensing compliance` | $2.5M [1M, 5M] per programme, launch + re-entry | "FAA does not charge an application fee; cost is internal engineering + legal + safety-case work" (FAA.gov; CRS R48582) |
| `FAA Part 450 licensing (launch only)` | $1.2M [0.6M, 2.5M] per programme | "Roughly half the combined licence"; judgement |
| MPL requirement behind `Third-party liability insurance` | caps of $500M third party / $100M US government | 14 CFR Part 450 (the premium itself is domain 17) |
| `calc.py` `delivery_destination` licence split | `earth_surface` carries the re-entry licence and a recovery campaign; in-space destinations carry the launch-only licence | modelling choice |
| Planetary-protection category of an asteroid Earth return | not modelled | nothing upstream; it sets the handling behind domain 7's sample-recovery envelope |
| Legal basis to own and sell extracted material | assumed | nothing upstream; it is the premise under every revenue line |

**What a source has to supply.**

- The time and cost to obtain a Part 450 launch and re-entry licence: agency, audit or operator data on the licensing effort, not the rule text alone.
- How MPL values are set for re-entry missions.
- The planetary-protection categorisation of small-body sample return, and what it requires at recovery.
- National space-resource legislation and international frameworks. These do not back a numeric cell, so they are registered as context-only unless they change a costed row (a licensing or supervision fee, say).

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `faa_14_cfr_part_450_launch_reentry_licensing` (domain 5): the rule text.
- `crs_r48582_commercial_launch_reentry_regulations` (domain 5): the CRS overview the licensing rows cite.

**Boundary.** Domain 17 prices the insurance the MPL requires; domain 7 holds the sample-recovery operations envelope that a planetary-protection category would change.
