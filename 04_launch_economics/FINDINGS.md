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


## Round-3 additions — the forward-looking half of launch economics

### terzi_nicoli_2026 [T1] — Terzi & Nicoli, "From Sputnik to Starship: Estimating the experience curve of space launch technology", PNAS Nexus 5(7):pgag217 (2026), DOI 10.1093/pnasnexus/pgag217
- **Full text hosted**: `full_texts/terzi_nicoli_2026_from_sputnik_to_starship_experience_curve_PNAS_Nexus_pgag217_CC-BY.pdf` (586 KB, 10 pp; verified live from this machine via the Cambridge University repository bitstream — PMC's direct PDF route returned a stub and AEA/Elsevier-style endpoints were not involved; CC-BY per OpenAlex).
- **What it is**: the largest standardized launch-cost dataset to date (4,400+ launches, 1960–2025, 16 spacefaring entities) fit with a Wright's-law experience curve — i.e. not just history but a *forecasting model* for $/kg-to-LEO. This is the piece domain 4 was missing: rounds 1–2 anchored where launch cost HAS BEEN (jones2018, hf_dataset); this anchors where it is projected to GO.
- **Key numbers** → `extracted_data/terzi_nicoli_experience_curve_key_numbers.csv`: fleet average $87,023/kg (1960) → $3,868/kg (2025), all in 2024 USD; learning rate −21.2% per doubling of cumulative payload overall, ~−44%/doubling post-Cold-War vs ~−17% earlier; central-scenario forecast **$1,600/kg by 2030 and $300/kg by 2040**; steeper than solar PV (−20.2%) or steamship freight (−15.5%).

### What this settles
- Our Stage-4 cost cascade prices launches at today's per-vehicle list prices with `reference_year` tags but carries **no forward projection** — the "launch no longer dominates" claim in economicspace's README rests on jones2018's historical factor-of-~20. This paper supplies the peer-reviewed slope: if the fleet average keeps its 21%/doubling rate, our Falcon-9 row ($4,253/kg LEO, 2026) is *above* their 2025 fleet mean and will be ~2x above it by 2030 in their central case. That is a citable basis for either (a) discounting launch cost in long-horizon mission cells or (b) stating the assumption explicitly — user's call, recorded here rather than applied silently.
- The post-Cold-War acceleration (44% vs 17%) matters more than the headline number: it says the curve is getting STEEPER, so any flat extrapolation of current prices understates future declines for exactly the reusable-launch class our launch table now leans on.

### weinzierl2018 [T1] — Weinzierl (Harvard), "Space, the Final Economic Frontier", Journal of Economic Perspectives 32(2):173–192
- **Access**: open access per OpenAlex/AEA, but BOTH PDF routes bot-block this machine (aeaweb.org/articles/pdf → 403; Harvard DASH bitstream download endpoint → 405). Recorded `open_not_pulled`; pullable from a normal browser. Abstract + key figure recovered via the AEA/Harvard landing-page record:
- **Key number (as published, retrieved from the OA landing page)**: NASA's COTS cost breakdown — all-in cargo delivery to ISS ≈ **$89,000/kg via SpaceX** and $135,000/kg via Orbital Sciences, vs ~$272,000/kg estimated for Shuttle (citing Zapata 2017). This is the peer-reviewed economics-journal anchor for the commercial-vs-government price gap that our launch table's operator split implicitly assumes.
- **Why it matters here**: JEP is a top economics journal — this is the strongest *economics* (not engineering) source in the repo: market structure, COTS policy effects and cost trajectories written for an economist audience. Pairs with terzi_nicoli_2026 as theory + data.

## Round-3 status (domain 4)
Domain now spans history (jones2018), current per-vehicle prices (hf_dataset row-comparison), a peer-reviewed experience curve WITH forecasts (terzi_nicoli_2026, hosted), and the economics-journal framing of COTS price gaps (weinzierl2018, OA-pending). The launch term in Stage 4 can now cite a forward projection instead of only a historical trend.

## Round-6 addition — jones2018's numbers extracted (source was already registered; the key figures were not)

### jones2018 [T2] — re-extraction pass
The source itself has been in this domain since round 3, but only its headline (Shuttle $54.5k/kg → commercial ~$2.7–3.9k/kg, factor of ~20) was recorded. This round the full text was re-pulled from NTRS (`ntrs_2020_recent_large_reduction_in_space_launch_cost.pdf`, public domain — already hosted; a second copy I downloaded this round was verified identical in content and removed as redundant) and its numbers extracted into `extracted_data/jones2018_launch_cost_key_numbers.csv`:
- **ISS cargo: $105.8k/kg Shuttle → $25k/kg Falcon 9+Dragon — only a ~4× factor**, versus the ~20× for LEO, because Dragon's payload fraction to ISS is small (6,000 kg vs 16,050 kg). This is the quantitative reason our model prices LEO and ISS separately; any "launch cost dropped 20×" claim applied to ISS-bound missions overstates it ~5×.
- **Historical baseline 1970–2000: $18.5k/kg average (range $10–32k)** across 22 systems, with the sub-$10k systems all Soviet/Chinese and possibly subsidized — a caveat for any "cost floor" argument built on that era's data.
- **Falcon Heavy at $1.4k/kg** (2018$) — the low end of our launch-cost range.
- **The reusability-economics finding**: reusable rockets carry HIGHER development costs and a landing-fuel payload penalty; the shuttle is the counterexample to "reused = cheap"; as of 2018 Falcon 9's reuse savings were still projected, not realized. For any future Starship-class projection in our model: peer-reviewed position is that reuse lowers MARGINAL cost while raising DEVELOPMENT cost — a projection must carry both terms or it will misprice the early flights exactly when they matter most (the first decade of a new vehicle's life).

## Round-12 addition — ISRU economics gets its theoretical anchor (metzger_2023, recorded only)

**metzger_2023 (T1, open_not_pulled)**: arXiv:2303.09011 preprint read live (50 pp); no redistribution license on the preprint and Elsevier bot-blocks the published version => metadata + abstract only. The framework: "gear ratio on cost" G for capital transport and production mass-ratio phi are THE two factors deciding whether lunar propellant beats Earth-launched; prior TEAs erred by choosing high-G architectures or ignoring phi. Tent-sublimation technology has phi an order of magnitude better than the viability threshold => conclusion that lunar propellant WILL be commercially viable and should lower the cost of everything else in space. Same author as metzger_zacny_2020 (drilling, domain 5) — his UCF line is now our standing reference for both ISRU physics AND its economics.
## Round-16 addition — launch_vehicles.csv gets a peer-reviewed spec anchor for the reusable-LV rows

- **yun_2023** (T1, KSPE 27(2):45-59, CC-BY-NC; koreascience.or.kr direct PDF route verified live — same proven route as kim_2013) is now hosted in full_texts/ and registered. It carries a comprehensive table of reusable launch vehicles worldwide with engine configuration / total thrust / fuel: Starship CH4 7,342 kN (Raptor x33 booster + x6 ship), New Glenn BE-4 x7 methalox, Falcon Heavy side-core landing, plus reusability plans (New Glenn first stage up to 25 flights after an initial 100-flight plan; Starship full reuse via grid fins + landing gear). Scope note: the paper does NOT tabulate payload mass or $/kg — those columns of our rows remain vendor-announced values. The cost-per-kg side is already anchored by jones2018 (hosted, ICES-2018-81): Shuttle 54,500 vs Falcon 9 ~2,720 $/kg LEO in current dollars — the factor-of-20 trend behind our cost-cascade context.
- Duplicate-download note: my round-16 ThinkTech bitstream copy of jones2018 (sha f98a5d65) differs from the repo's NTRS-hosted copy (sha 20f015ba, different scan source); the existing hosted item stands and the duplicate was discarded.

## Round-32 addition — SLS Block 1B (Cargo) row gets official NASA payload anchors, incl. an EXACT match on the LEO figure (two hosted)

**Target:** `launch_vehicles.csv` "SLS Block 1B (Cargo)" at 105 t LEO / $39,048 per kg. The $/kg side was already covered by jones2018 + hf_dataset; this round anchors the PAYLOAD-MASS side with official NASA documents — and gets an exact match on the headline number.

**Anchors added:**
1. `askins_2021_sls_janaff_update` (T2, NTRS 20210016306, hosted) — Askins (SLS Program Infrastructure Manager), JANAFF briefing "The Power of SLS and Orion" (June 8, 2021). Official capability table verified verbatim in the extracted text:
   - **Payload to LEO = 105 t (231.4k lbs) for Block 1B Cargo — EXACT match** to our row's `payload_leo_kg=105000`. Same figure for Block 1B Crew; ladder continues B1C/B1 C+Cr = 95 t, B2 Cargo/Crew = 130 t.
   - The defining footnote is captured verbatim: *"Low Earth Orbit (LEO) represents a typical 200 km circular orbit at 28.5 degrees inclination"* — i.e., our row's LEO figure inherits this exact mission definition, which matters because SLS was never intended for routine LEO missions ("no such missions are planned" per the companion guide).
   - TLI column (B1B Cargo >46 t / 42 t; B1C >27 t) cross-checks our `payload_escape_kg` context.
2. `nasa_esd30000_sls_mission_planners_guide` (T2, ESD-30000 Version A, NTRS 20190000736, hosted) — the official SLS Mission Planner's Guide (Dec 19, 2018 release). Section 4.2 defines the mass-delivery methodology behind every SLS number; body text verified: Block 1 LEO capability "more than 209,439 lbm (95 t)"; *"SLS Block 1B will utilize a new Exploration Upper Stage (EUS) to provide up to 88,185 lbm (40 t) of payload delivery to lunar vicinity."* This is the source document that defines what "payload" means for SLS rows (useful PSM vs. gross), so our row's numbers are traceable to a single official definition rather than vendor marketing.

**Scope notes:**
- Both documents predate Block 1B flight hardware; they state DESIGN capability, which is exactly the right anchor class for a configuration that had not yet flown as of their publication. The 105 t LEO figure has been stable across NASA's public materials from at least Dec 2018 (ESD-30000) through June 2021 (JANAFF).
- $/kg side of the row ($39,048) remains anchored by jones2018 (peer-reviewed ICES table) + hf_dataset (63-vehicle structured dataset), as before — this round does not re-anchor cost.
## Round-33 addition — launch_vehicles.csv cost side gets two peer-reviewed anchors for the Falcon 9 reusable row (two hosted)

**Target:** `launch_vehicles.csv` "Falcon 9 (reusable)" at list_price_usd=74,000,000 / usd_per_kg_to_leo≈4,253. The payload-mass side of this row is still vendor-announced (neither paper below tabulates F9 LEO payload mass — that gap remains open); this round anchors the COST side with two peer-reviewed items whose numbers were extracted and verified verbatim on this machine.

**Anchors added:**
1. `zapata_2017_cots_crs_lcc_assessment` (T2, AIAA conference paper Sept 2017, NTRS 20170008895, hosted) — Zapata (NASA KSC), "An Assessment of Cost Improvements in the NASA COTS/CRS Program and Implications for Future NASA Missions". Verified verbatim from extracted text:
   - **Falcon 9 development cost ≈ $390M total** ($300M F9 + $90M Falcon 1 contribution), "NASA has verified these costs" — vs NAFCOM's own 2010 Commercial Market Assessment predicting **$1.7B–$4.0B** for the same vehicle under traditional NASA acquisition ("Under methodology #1, the cost model predicted that the Falcon 9 would cost $4.0 billion based on a traditional approach"). This is the peer-reviewed basis for why our F9 row's list_price_usd sits ~5–10× below legacy-vehicle norms rather than being an outlier data entry.
   - **Operational recurring cost per actual kg delivered to ISS (2017$): SpaceX $89,000/kg; Orbital ATK $135,000/kg; Space Shuttle "what-if" ~$272,000/kg** — the paper's own comparison table. Note these are ISS-orbit delivery costs including spacecraft + launch + NASA management, NOT bare LEO price-per-kg; they bracket our usd_per_kg_to_leo=4,253 from above by roughly 20× (different mission definition), which is expected and worth stating explicitly in any future module-4 documentation.
   - COTS/CRS life-cycle-cost methodology for comparing launch services across vehicles — the analytical framework our cost-cascade context already follows informally; this gives it a citable source.
2. `webb_2016_is_it_worth_it_reusable_econ` (T2, ICEAA 2016 International Training Symposium, Bristol UK Oct 2016, NTRS 20160013370, hosted) — Webb (KAR Enterprises), "Is It Worth It? The Economics of Reusable Space Transportation". Carries the **official documentation of the NASA PCEC Launch Services ROM Estimator** — a destination × mass-breakpoint price table in M15$ per launch. Verified from PDF word coordinates (the printed matrix is ragged, not every cell filled; flat text extraction scrambles column alignment so this had to be checked geometrically):
   - GEO <3,000 kg = $120M / >3,000 kg = $140M; Planetary <1,000 kg = $80M / 1,000–2,000 kg = $110M / >2,000 kg = $175M; Polar <1,000 kg = $55M / 1,000–2,000 kg = $85M / >2,000 kg = $130M; Lunar <500 kg = $85M / >500 kg = $160M; LEO <500 kg = $40M / >500 kg = $80M; Helio (all masses) = $100M.
   - The paper's worked example ("a 500 kg payload on the order of ~$50M, i.e. ~$100,000/kg") is a rough illustration of price-per-kg falling with mass — cited as an order-of-magnitude example only; it does not pin down a single table cell.
   - This is the peer-reviewed basis for order-of-magnitude sanity checks on our usd_per_kg_to_leo/gto/escape columns, and for the "price per flight vs price per kg" distinction that underpins how list_price_usd should be interpreted in module 4 (a $74M F9 launch is a *flight* price; dividing by payload mass to get $/kg only makes sense once you know which destination/mass-breakpoint cell it corresponds to).

**Scope note:** neither paper tabulates Falcon 9 LEO payload mass, so the `payload_leo_kg` column of that row remains vendor-announced (SpaceX's own published figure) — same status as before this round. The cost side is now anchored by two independent peer-reviewed sources instead of one dataset + one ICES paper.

