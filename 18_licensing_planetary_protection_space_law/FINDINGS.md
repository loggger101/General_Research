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

## R107 - Primary regulatory text hosted: 14 CFR Parts 450 + 440 (2026-10-03; Part 450 row upgraded registered_not_pulled -> full_text_hosted, Part 440 added)

R87 had backed d18's licensing rows with CRS R48582 and the FAA's own MPL-methodology report (domain 17), but the rule text itself was still `registered_not_pulled` - R74 recorded that eCFR redirected this machine to a bot 'unblock' page. This round both parts pulled live from ecfr.gov without any workaround: HTTP 200, full part verified complete through each Appendix A (Part 450 §§ 450.1-450.219; Part 440 §§ 440.1-440.19). US government work -> public-domain; hosted as cleaned plain-text snapshots (SHA-256 in the manifest) with the canonical eCFR URL recorded for re-pull.

| cell | backed by (R107 id) | what it supplies (verbatim from the pulled text) |
|---|---|---|
| FAA Part 450 licensing compliance / (launch only) | faa_14_cfr_part_450_launch_reentry_licensing | decisive negative finding: **zero occurrences of 'fee' anywhere in Part 450's body** - the rule text itself confirms CRS R48582's 'no application fee' premise behind both rows; licensing cost is internal engineering + legal + safety-case work, as upstream states. Application content (incl. the MPL analysis requirement) sits at § 450.31(a)(6): 450.47 ; and ( 6 ) Provide the information required by appendix A of part 440 for the Administrator to conduct a maximum probable loss analysis for the applicable licensed operation. ( b ) An applicant may apply for the approvals and determinations in paragraphs (a)(2) through (6) of this section… |
| Third-party liability insurance (MPL requirement) | faa_14_cfr_part_440_liability_insurance_requirements | the PRIMARY regulatory source of upstream's caps - § 440.9(c): "The amount of insurance required is based upon the FAA's determination of maximum probable loss; however, it will not exceed the lesser of: ( 1 ) $500 million; or ( 2 ) The maximum liability insurance available on the world market at a reasonable cost, as determined by the FAA." and § 440.9(e) (US government property): "The FAA will prescribe for each licensee or permittee the amount of insurance required to compensate claims for property damage under paragraph (d) of this section resulting from a licensed or permitted activity in connection with any particular launch or reentry. The amount of insurance is based upon a determination of maximum probable loss; however, it will not exceed the lesser of: ( 1 ) $100 million; or ( 2 ) The maximum available on the world market at a reasonable cost, as determined by the FAA."; plus the federal indemnification base, §§ 440.5/440.19: "...r its agents; ( 2 ) Any covered claim of a third party for bodily injury or property damage arising out of any particular licensed activity exceeds the amount of financial responsibility required under § 440.9(c) of this part and does not exceed $1,500,000,000 (as adjusted for inflation occurring after January 1, 1989) above such amount" |

Consistency check against already-registered sources: CRS R48582's '$500M third-party / $100M USG' caps and GAO-18-57's 'federal indemnification cap above MPL = $3.1B in 2017 (= $1.5B in 1988)' both reconcile exactly with §§ 440.9(c)/(e) and 440.19 - the statutory base is **$1,500,000,000 'as adjusted for inflation occurring after January 1, 1989'**, so GAO's $3.1B-in-2017 figure is that base CPI-adjusted (provenance of CRS R48582's previously-unattributed '$1.5B in 1989 dollars'). No revision candidate opened: primary-source backing added, nothing contradicts upstream values.

## R113 - Both open premises get primary texts (2026-10-04; +3 sources, T2x1, T3x2)

The opening block left two cells with nothing upstream: the planetary-protection category of an asteroid Earth return, and the legal basis to own and sell what is mined. R87 added NASA's implementation of the COSPAR categories (`seasly_2022_nasa_revised_planetary_protection_policy`); this round adds the policy itself and the statute.

- **`cospar_2026_planetary_protection_policy`** (Space Research Today 224, January 2026; read live, not hosted because the file carries no licence). The current version, superseding 2020, 2021 and 2024. Outbound missions to undifferentiated, metamorphosed asteroids are Category I and to carbonaceous-chondrite asteroids Category II. Sample return from small Solar System bodies is Category V: "Unrestricted Earth return" unless all six questions of section 6.5.2 (the 1998 NRC Space Studies Board framework) are answered "no" or "uncertain", which makes it "Restricted" and requires containment. A mining return from an S-, M- or C-type body would normally be unrestricted, so the recovery campaign domain 7 prices would not need restricted-return containment.
- **`usc_title51_chapter513_space_resource_utilization`** (51 U.S.C. 51301-51303, 2023 edition from govinfo; hosted; uscode.house.gov returns 403 here). Section 51303: a US citizen engaged in commercial recovery of an asteroid or space resource "shall be entitled to any asteroid resource or space resource obtained, including to possess, own, transport, use, and sell" it, in accordance with applicable law and US international obligations. This is the premise under every revenue line, for US citizens; it does not bind other states.
- **`pl_114_90_hr2262_enrolled_space_act`** (the enrolled bill, hosted). Its sec. 402 is the chapter above, word for word. What the codified chapter does not carry is sec. 403, the "Disclaimer of extraterritorial sovereignty": the sense of Congress that the Act does not assert sovereignty, exclusive rights, jurisdiction or ownership over any celestial body. So the right in sec. 51303 is to resources extracted, not to the asteroid. The bill's Title I also moved the 50915(f) launch-liability indemnification date to September 30, 2025 (part of the federal payment above MPL behind `Third-party liability insurance`); whether later law extended it was not checked here.

The owner's list also offered the 2020 and 2021 policy texts and ESA's ECSS-U-ST-20C; all three were rejected as superseded by the 2026 COSPAR text (Round 113 log entry). No revision candidate.

Extracted data: `extracted_data/r113_space_law_and_planetary_protection.csv` (8 rows).

## R114 - The FAA 2026 user fee, a CRS overview and planetary-protection cost (2026-10-04; +3 sources, T1x1, T3x2)

`faa_2026_launch_reentry_licensing_user_fees_policy_statement` (91 FR 21591, 22 April 2026): from 2026 each licensed or permitted launch or reentry owes the user fee Congress created in Pub. L. 119-21 (51 U.S.C. 50924), the lesser of a per-pound payload schedule and a maximum schedule; payload weight is reported 60 days ahead and payment is due 30 days after notification. The notice gives no dollar rate; a secondary article on the owner's list reports $0.25 per pound with a $30,000 cap for 2026, and those figures are in the statute, which was not read. The licensing rows of `operational_costs.csv` ($2.5M and $1.2M per programme, 'FAA does not charge an application fee') are unaffected in order of magnitude. The public-inspection PDF and the govinfo HTML on the list are the same document; FAA Order 8800.4 answered 403 and was not read.

`crs_r48144_2024_space_resource_extraction_overview_and_issues_for_congress` (24 pages, read) is registered as context for the right-to-sell premise: the Outer Space Treaty has over 100 signatories and is read both ways on extraction. `sinibaldi_haldemann_2026_planetary_protection_is_expensive_esa_perspective` (abstract) gives the planetary-protection cost share from ESA missions: none for category I-II, under 1% for category III orbiters, up to about 5% for category IV Mars landers, and category V Earth return an integral part of the mission. The 2015 edition of 51 U.S.C. chapter 513 on the list is an older codification of the registered chapter. Rejected: a House committee report, an environmental-impact framework and impact-assessment principles, none with a number (Round 114 log entry). No revision candidate.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.
