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

## R77 - Sources moved in (2026-09-27; registry unchanged at 267)

These rows were registered in other domains before this one existed; they moved here because the cells they back are this domain's. Their earlier write-ups stay in the old domain's FINDINGS.md under the blocks named.

| id | from | earlier write-ups | files moved here |
|---|---|---|---|
| `faa_14_cfr_part_450_launch_reentry_licensing` | domain 5 | `05_inspace_operations/FINDINGS.md`: R74 | none |
| `crs_r48582_commercial_launch_reentry_regulations` | domain 5 | `05_inspace_operations/FINDINGS.md`: R74 | none |

The cross-references to `faa_14_cfr_part_450_launch_reentry_licensing`, `crs_r48582_commercial_launch_reentry_regulations` in the opening block are now rows of this domain.
## R87 - Both licensing premises get sources (2026-09-30; registry 313 -> 314)

**crs_r48582_commercial_launch_reentry_regulations** [T3, now full_text_hosted] - the report upstream's licensing rows cite was read in full this round (R48582.3 edition of Jun 23 2025 pulled live from congress.gov; CRS reports are freely reproducible per their own p.1 note). What it supplies:

- the 'FAA does not charge an application fee' premise in both Part 450 rows - confirmed as of this edition: no user-fee program exists, only future policy options (pp19/24/26-27; a June 2025 draft reconciliation bill would authorize one); civil penalties up to $100,000 per violation with each continuing day separate (p9), worked example: the FAA's proposed $633,009 against SpaceX in Sep 2024.
- **the MPL requirement behind 'Third-party liability insurance'** - statutory caps of $500M for third-party claims and $100M (or max available insurance) for U.S. government claims; the FAA determines the MPL amount in consultation with other agencies (p12); U.S. government payment toward successful third-party claims above the required amount is limited to $1.5B in 1989 dollars + inflation.
- transition context: legacy licenses run until **March 10, 2026**, after which Part 450 applies to all launch and reentry licenses (pp2/12/15); the license evaluation process has five major components (p2) - that is what our internal engineering + legal + safety-case cost buys. The report does NOT quantify compliance effort, so no re-pin of the $1-5M values.

**seasly_2022_nasa_revised_planetary_protection_policy** [T2, new] - NASA's Revised Planetary Protection Policy and Implementation (Dr. Elaine Seasly, Deputy PPO; presentation to the 44th COSPAR Scientific Assembly Jul 21 2022; NTRS 20220010648 GOV_PUBLIC_USE_PERMITTED). This is **the source for d18's second regulatory premise - planetary protection on Earth return**, which the opening block recorded as having none: NPD 8020.7G + NPR 8715.24 implement COSPAR Categories I-V; robotic Earth-return missions are categorised **V(r) restricted / V(u) unrestricted** with PPO concurrence (p9), and the inbound requirements chain is contamination avoidance prior to/during Earth entry, during Earth containment, plus a sample safety assessment (p15). The abstract names 'the private sector's emerging capability to plan missions' as part of what drove the update - commercial small-body sample return sits inside this framework. Context-only per d18's brief: it changes no costed row.

Extracted data: `extracted_data/r87_licensing_planetary_protection_key_numbers.csv` (10 rows). No revision candidate opened or closed by this round. Still unbacked cells recorded in FINDINGS: the actual time-and-cost of obtaining a Part 450 licence (agency/audit/operator data on licensing effort - R48582 confirms the structure but not the cost), and national space-resource legislation / international frameworks for the right to sell what is mined.
