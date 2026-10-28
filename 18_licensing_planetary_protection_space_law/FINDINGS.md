# Domain 18 — Licensing, planetary protection & space-resource law

Backings: spacecost `reference/operational_costs.csv` rows `FAA Part 450 licensing compliance` and `FAA Part 450 licensing (launch only)`, the MPL requirement behind `Third-party liability insurance`, and the licence split by `delivery_destination` in economicspace `modules/calc.py`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `FAA Part 450 licensing compliance` | $2.5M [1M, 5M] per programme, launch + re-entry | "FAA does not charge an application fee; cost is internal engineering + legal + safety-case work" (FAA.gov; CRS R48582) |
| `FAA Part 450 licensing (launch only)` | $1.2M [0.6M, 2.5M] per programme | "Roughly half the combined licence"; judgement |
| MPL requirement behind `Third-party liability insurance` | caps of $500M third party / $100M US government | 14 CFR Part 450 (the premium itself is domain 17) |
| `calc.py` `delivery_destination` licence split | `earth_surface` carries the re-entry licence and a recovery campaign; in-space destinations the launch-only licence | modelling choice |
| Planetary-protection category of an asteroid Earth return | not modelled | sets the handling behind domain 7's sample-recovery envelope |
| Legal basis to own and sell extracted material | assumed | the premise under every revenue line |

**What a source has to supply:** the time and cost of a Part 450 launch and re-entry licence (agency, audit or operator data); how MPL is set for re-entry; the planetary-protection category of small-body sample return and its recovery requirements; national space-resource law and international frameworks (context-only unless they change a costed row).

**Boundary:** domain 17 prices the insurance the MPL requires; domain 7 holds the sample-recovery envelope a planetary-protection category would change.

## R77 - Sources moved in (2026-09-27)

`faa_14_cfr_part_450_launch_reentry_licensing` and `crs_r48582_commercial_launch_reentry_regulations` moved here from domain 5 (earlier write-up: `05_inspace_operations/FINDINGS.md` R74; no files).

## R87 - Both licensing premises get sources (2026-09-30)

**crs_r48582_commercial_launch_reentry_regulations** (R48582.3, 2025-06-23; hosted, CRS reports are freely reproducible):

- No FAA user-fee programme exists as of this edition, only proposals (pp19/24/26-27; a June 2025 draft reconciliation bill would authorise one). Civil penalties up to $100,000 per violation, each day separate (p9); e.g. the FAA's proposed $633,009 against SpaceX (Sep 2024).
- MPL caps: $500M third party, $100M (or the maximum available) for US government claims, set by the FAA with other agencies (p12); federal payment above that limited to $1.5B in 1989 dollars plus inflation.
- Legacy licences run to March 10, 2026, then all licences are under Part 450 (pp2/12/15); evaluation has five components (p2). Compliance effort is not quantified, so the $1-5M values are not re-pinned.

**seasly_2022_nasa_revised_planetary_protection_policy** (44th COSPAR, 2022-07-21; NTRS 20220010648): NPD 8020.7G and NPR 8715.24 implement COSPAR Categories I-V; robotic Earth return is Category V(r) restricted or V(u) unrestricted with PPO concurrence (p9); inbound requirements are contamination avoidance before and during entry, containment, and a sample safety assessment (p15). The update was driven partly by "the private sector's emerging capability to plan missions". Context only.

`extracted_data/r87_licensing_planetary_protection_key_numbers.csv`. Still unbacked: the real time and cost of a Part 450 licence.

## R107 - 14 CFR Parts 450 and 440 hosted (2026-10-03)

Both pulled from ecfr.gov (complete through Appendix A; public domain; hosted as text snapshots).

| cell | backed by | what it supplies |
|---|---|---|
| FAA Part 450 licensing rows | faa_14_cfr_part_450_launch_reentry_licensing | "fee" occurs nowhere in Part 450's body, confirming the no-application-fee premise; § 450.31(a)(6) requires the information of Part 440 Appendix A "for the Administrator to conduct a maximum probable loss analysis" |
| Third-party liability insurance (MPL) | faa_14_cfr_part_440_liability_insurance_requirements | § 440.9(c): insurance "based upon the FAA's determination of maximum probable loss; however, it will not exceed the lesser of: ( 1 ) $500 million; or ( 2 ) The maximum liability insurance available on the world market at a reasonable cost"; § 440.9(e) the same for US government property with "$100 million"; § 440.19 indemnification for claims above that "and does not exceed $1,500,000,000 (as adjusted for inflation occurring after January 1, 1989)" |

CRS R48582's caps and GAO-18-57's "$3.1B in 2017 (= $1.5B in 1988)" both reconcile with §§ 440.9(c)/(e) and 440.19: GAO's figure is the statutory $1.5B CPI-adjusted. No candidate.

## R113 - Primary texts for both open premises (2026-10-04)

- **`cospar_2026_planetary_protection_policy`** (Space Research Today 224, January 2026; read, not hosted: no licence). Supersedes 2020, 2021 and 2024. Outbound to undifferentiated or metamorphosed asteroids: Category I; carbonaceous-chondrite asteroids: Category II. Small-body sample return is Category V "Unrestricted Earth return" unless the six questions of section 6.5.2 are answered "no" or "uncertain", making it "Restricted" with containment. A mining return from an S-, M- or C-type body would normally be unrestricted, so domain 7's recovery campaign needs no restricted-return containment.
- **`usc_title51_chapter513_space_resource_utilization`** (51 U.S.C. 51301-51303, 2023 edition; hosted). § 51303: a US citizen in commercial recovery "shall be entitled to any asteroid resource or space resource obtained, including to possess, own, transport, use, and sell" it. The revenue premise holds for US citizens only.
- **`pl_114_90_hr2262_enrolled_space_act`** (hosted). Sec. 402 is the chapter above; sec. 403, absent from the codified chapter, disclaims sovereignty or ownership over any celestial body, so the right covers extracted resources, not the asteroid. Title I moved the 50915(f) indemnification date to September 30, 2025 (later extensions not checked).

`extracted_data/r113_space_law_and_planetary_protection.csv`. No candidate.

## R114 - FAA 2026 user fee, a CRS overview, planetary-protection cost (2026-10-04)

- `faa_2026_launch_reentry_licensing_user_fees_policy_statement` (91 FR 21591, 2026-04-22): from 2026 each licensed launch or reentry owes the 51 U.S.C. 50924 user fee (Pub. L. 119-21), the lesser of a per-pound schedule and a maximum; payload weight reported 60 days ahead, payment 30 days after notification. No dollar rate in the notice; a secondary article gives $0.25 per pound capped at $30,000 for 2026 (the statute was not read). Too small to move the $2.5M / $1.2M rows.
- `crs_r48144_2024_space_resource_extraction_overview_and_issues_for_congress` (read): the Outer Space Treaty has over 100 signatories and is read both ways on extraction. Context for the right-to-sell premise.
- `sinibaldi_haldemann_2026_planetary_protection_is_expensive_esa_perspective` (abstract): planetary-protection cost share is nil for categories I-II, under 1% for category III orbiters, up to about 5% for category IV Mars landers; category V return is integral to the mission.

`extracted_data/r114_gr_links_key_numbers.csv`. No candidate.

## R163 - Two notes contradict sources already here (2026-10-14)

Read against spacecost@0b716ad:

- **rc-086 (citation):** 'Third-party liability insurance' puts the $500M/$100M caps "per 14 CFR Part 450"; they are in Part 440 (§ 440.9(c), (e)), and the hosted Part 450 text (`full_texts/ecfr_title-14_chapter-I_subchapter-F_part-450.txt`) contains neither figure. The $1.5M value is not in question.
- **rc-087 (wording):** 'FAA does not charge an application fee' is still true of applications, but since 2026-01-01 every licensed launch or reentry owes the 50924 user fee (R114); the note now misleads. The rate is still only secondary-reported.

### Round 290 - FAA Part 450 licensing compliance row: internal-cost figure and the R48582 support gap (rc-232)

Upstream note reads (count==1 at spacecost@860bef9): "FAA does not charge an application fee; cost is internal engineering + legal + safety-case work for 14 CFR Part 450 compliance (FAA.gov / Congress.gov R48582)." The 2,500,000 USD point value is the only cell in operational_costs.csv that names no document and does not self-declare as an estimate; every other unsourced value carries an explicit ESTIMATE or JUDGEMENT marker. Today re-pull of CRS R48582 (R48582.3, Jun 23 2025) is byte-identical to the hosted copy (full sha e67e8544357606cff484e6b25fd6042dd8a8a26140b834a8f43da1f9f06e138c, 780,356 B): exhaustive search finds zero application-processing-fee statements - the word charg occurs exactly 3 times in the whole text layer: ACUS being charged with efficiency duties, and two contexts describing a prospective user fee that would direct the Secretary of Transportation to charge a fee for each launch and reentry. The report therefore cannot support the no-application-fee clause; it documents licensing scope (safety review, policy review, payload review, financial responsibility requirements, environmental review) with no dollar figure attached.

- **Institutional component registered:** FAA Paperwork Reduction Act notice 2019-09588 (Federal Register public inspection, May 8 2019; hosted, sha 0f5e2ad6d2b8b9205fd800bd9139ea5afbfc79c005581a34374cc0b32deba357, US government work): "Each initial application is estimated to take 2,903 hours" - the FAA own estimate of Part 450 application paperwork burden. At any loaded professional wage this yields a few hundred thousand dollars per application: a lower-bound component for engineering + legal labor only; reaching 2.5M requires undeclared assumptions (COLA analyses, environmental review support, design-to-criteria work) that the note does not state.
- **Dated self-correction (R87-era claim):** the Round 87 log line records the hosted R48582 as supporting no FAA application fee. That parenthetical conflates two different things: the r87 extraction itself was accurate - user_fees_currently_absent quoted only prospective language (Congress may authorize AST to collect user fees) - but absence of enacted USER fees is not a statement that initial applications are free, and the report never discusses application processing charges. The upstream parenthetical reliance on this document fails; rc-232 records it with today evidence. No prior-round artifact other than the log line needs amendment; r87 key csv rows stand as written.
- **Consumer impact:** spacecost/operations.py L239 embeds the category directly; economicspace campaign/stage3/operational_costs.csv carries an embedded copy of the row at reference_year=2026 (catalog_date 2026-09-17). Proposal changes attribution only, no value moved.
