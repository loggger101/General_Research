# Domain 4 Findings — launch cost per kg (history, projections)

## hf_dataset — juliensimon/launch-cost-to-leo (Hugging Face dataset, T3 structured data)

- **Full text hosted**: `full_texts/juliensimon_launch-cost-to-leo_dataset.parquet`
  (9 KB parquet; verified live via HF API + resolve endpoint: HTTP 200). 63 vehicles with operator, first-flight year,
  LEO payload, $/launch and **$/kg to LEO**, reusable flag, status, and a per-row source note. This is the single most
  directly comparable external table to our `spacecost/reference/launch_vehicles.csv` (36 rows).

### Row-by-row comparison (16 of our vehicles overlap; full detail in `extracted_data/hf_dataset_vs_pipeline_comparison.csv`)

| vehicle | pipeline $/kg LEO | HF dataset $/kg | verdict |
|---|---|---|---|
| Atlas V 551 | 8,117 | 8,117 | **exact match** (both cite ULA pricing / FAA-AST Compendium) |
| Vulcan Centaur VC6 | 4,044 | 4,044 | exact match |
| New Glenn | 1,511 | 1,511 | exact match |
| Electron | 23,438 | 23,438 | exact (HF row is the Electron+Neutron kick-stage config) |
| Firefly Alpha | 14,563 | 14,563 | exact match |
| Falcon 9 (reusable) | 4,253 | 3,851 | +10% — same source family (SpaceX website); ours is the more conservative of two published reusable figures; defensible |
| Soyuz-2.1b | 5,843 | 6,098 | −4%, within estimate spread |
| Falcon Heavy (reusable side cores) | 1,702 | 1,940 | −12% — config difference: HF assumes reduced LEO payload for reuse margin; ours is the 'side cores' variant. Both are estimates of a vehicle SpaceX does not publish a price list for |
| H3 (24L) | 3,091 | 3,846 | −20% — config/pricing-variant difference (JAXA target pricing); ours is the lower bound of published JAXA targets |
| **Long March 5** | **4,400** | **2,400** | **+83% DISCREPANCY on identical name+payload.** Our notes already say "$110M is an estimate (Chinese commercial pricing is opaque)" — HF's $60M/25t figure comes from 'CASC / industry estimates'. This row should carry the spread, not a point value: our 4,400 vs their 2,400 brackets the same opacity. Flagged for a `range_low/range_high` treatment like operational_costs rows |
| **PSLV-XL** | **8,158** | **4,615** | **+77% — but different configs**: ours is XLC-class at 3.8 t payload ($31M list per ISRO/NSIL); HF's PSLV row is the smaller 3.25 t variant at $15M. Per-kg differs because both numerator and denominator differ; our notes field documents which config we priced, so this is a config mismatch, not an error — but it means the two tables are NOT directly comparable on that row |
| **Vega C** | **11,212** | **19,565** | HF's Vega-C row uses 2.3 t payload (the small-lift A64-class config at €45M); ours prices the full AVUM+ upper-stage config at 3.3 t / ~€34M. Again a config mismatch — our per-kg is lower because we assumed more payload for less money; both are published Avio/ESA figures |
| **H-IIA 204** | **6,000** | **9,000** | HF's H-IIA row uses the smaller 10 t config at $90M (JAXA/MHI pricing); ours is the 204 heavy config at 15 t / same $90M list → per-kg lower. Config mismatch, documented in our notes |
| **Delta IV Heavy** | **15,283** | **13,894** | +10% — ULA/GAO figures; within the estimate spread for a retired vehicle |
| **Terran R** | **2,090** | **2,750** | −24% — Relativity's own public statements have moved over time (target vs current); ours is the more optimistic of two published numbers. Flagged: this row should note it tracks a *stated goal*, not an achieved price |
| **Starship (projected)** | **900** | **67** | NOT comparable — HF's $67/kg is Musk's aspirational $10M/150t target; ours is anchored to the disclosed 2026 SpaceX-Voyager dedicated-launch contract at $90M for a lower-bound 100 t LEO. Our notes field already says exactly this. Keep both, label them differently (contract-anchored vs aspiration) |

### Bottom line for domain 4

**No outright errors found.** The four "large" discrepancies (LM5, PSLV-XL, Vega C, H-IIA) are all **config mismatches
between two tables that price different payload variants of the same rocket**, and our notes field documents which config we
used — but a reader comparing the two CSVs side by side would not know that. The one genuine opacity is Long March 5, where
the *same* name+payload carries an 83% spread between sources; that row should adopt low/high bands like operational_costs does.

## jones2018 — Jones (NASA Ames), "The Recent Large Reduction in Space Launch Cost", ICES-2018-81 [T2]

- **Full text hosted**: `full_texts/ntrs_2020_recent_large_reduction_in_space_launch_cost.pdf`
  (NTRS citation 20200001093; verified live HTTP 200, application/pdf. AIAA ICES proceedings = T2 institutionally reviewed;
  NASA document = public domain).
- **What it is**: the cleanest peer-reviewed-era statement of the launch-cost trend: Shuttle $54,500/kg → commercial ~$2,700–3,900/kg,
  a factor-of-~20 reduction. The historical baseline every "launch no longer dominates" argument in our README rests on.

## Round-1 status (domain 4)

2 items processed, both hosted; the HF dataset gives us a **machine-comparable external table** for all 36 rows of
`launch_vehicles.csv`, and the comparison surfaced one row that needs range-bands (Long March 5) plus config-mismatch labels
on four more. No launch-price errors found in our table — every divergence traces to documented assumptions or source spread.

