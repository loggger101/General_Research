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

## Round-34 addition — launch_vehicles.csv payload-mass side gets an official NASA capability anchor (zapata_2017_state_of_play_us_space_systems, NTRS 20170009967)

**Source**: Edgar Zapata (NASA Kennedy Space Center), "The State of Play US Space Systems Competitiveness: Prices, Productivity, and Other Measures of Launchers & Spacecraft", presentation to the Future In-Space Operations (FISO) Seminar, October 11, 2017. NTRS record 20170009967; full text hosted in `full_texts/` (NTRS = public domain). Tier T2 (NASA technical report / seminar presentation — same tier as the two Round-33 papers and askins_2021).

**What it anchors**: page 15 ("Launch Systems – Multiple Measures") is a per-launcher capability chart whose header states the orbit convention verbatim: *"Maximum Payload Capability of Launcher, kg to LEO, 200km/28.5 circ."* — identical to our `launch_vehicles.csv` LEO definition (the same footnote SLS documents use). Values verified from PDF word coordinates (page 15), not flat text; each value was mapped to its column label by x-position:

| Vehicle in chart | Max payload to LEO (kg) | Our CSV row (`payload_leo_kg`) | Match quality |
|---|---|---|---|
| Delta IV Heavy, NRO | **28,790** | delta_iv_heavy `28790` | EXACT |
| Atlas V 551, Private Sector Customer | **18,856** | atlas_v_551 `18850` | near-exact (Δ = 6 kg / 0.03%; our value is the rounded figure) |
| Falcon 9 (all four customer classes: private, NASA ISS, DoD GPS, NASA LSP Class-C) | **22,800** each | falcon_9_reusable `17400` | family ceiling — see note |
| Falcon Heavy, Private Sector Customer | **63,800** | falcon_heavy (reusable side cores) `57000` | expendable rating vs our derated reusable-cores figure — consistent, not a pin |

Also on the same page: per-launcher $/kg and price-per-launch in 2017$ (Falcon 9 private ~$2,719–$4,232/kg; Delta IV Heavy $8,644/kg; SLS no-EUS $54,627/kg) — a second independent cost-side cross-check alongside jones2018 and zapata_2017_cots_crs.

**Honest scoping of the two "ceiling" rows**:
- **Falcon 9 (reusable)**: the chart's 22,800 kg is Falcon 9's *rated maximum* LEO capability across customer classes; our reusable row carries 17,400 kg, which sits below it as expected for a reusability-derated rating. This source anchors the F9 family ceiling and confirms 17.4 t is physically consistent (not an overclaim), but does not pin the exact reusable figure — that remains vendor-rated.
- **Falcon Heavy (reusable side cores)**: the chart's 63,800 kg is the expendable-side-core rating; our row carries 57,000 kg for the reusability-derated configuration. Same relationship: ceiling anchor + consistency check, not an exact pin.

**Net effect on launch_vehicles.csv anchoring**:
- **delta_iv_heavy**: payload mass now EXACTLY anchored (28,790 kg); cost side = hf_dataset + this chart's $/kg.
- **atlas_v_551**: payload mass now near-exactly anchored (18,856 vs 18,850 — within rounding); cost side still vendor-listed.
- **falcon_9_reusable** / **falcon_heavy (reusable cores)**: family ceilings + consistency anchors added; exact reusable figures remain vendor-rated.

**Remaining unanchored in launch_vehicles.csv**: Vulcan Centaur 27 t LEO and New Glenn ~45 t LEO — both postdate this 2017 document; need their own peer-reviewed anchors (Vulcan: ULA design papers / AIAA ICES; New Glenn: Blue Origin program documents).

## nasa_oig_2021_ig-22-003_artemis_missions + nasa_oig_2023_ig-24-001_sls_epoc_transition - NASA OIG SLS cost audits (T2, full text hosted)

**Why these two**: the `launch_vehicles.csv` SLS rows cite "NASA OIG" numbers in their notes without a report ID or registry entry. Both underlying audits are now registered + hosted; every quote below was re-read verbatim from the pulled PDFs this round (hash-verified against canonical oig.nasa.gov URLs).

### IG-22-003 - NASA's Management of the Artemis Missions (Nov 15, 2021)
Hosted: `full_texts/nasa_oig_2021_ig-22-003_artemis_missions.pdf` (9,941,240 bytes; sha256 dc885a69ef128063...; canonical URL https://oig.nasa.gov/docs/IG-22-003.pdf)

Verbatim anchors (sliced programmatically from the hosted PDF this round):
- we estimate the single-use SLS will cost $2.2 billion to produce, including two rocket stages, two solid rocket boosters, four RS-25 engines, and two stage adapters.
- KSC ground systems (VAB, Crawler-Transporter, Mobile Launcher 1, Launch Pad, LCC): $568 million per year due to the large support structure that must be maintained.
- production and operations cost of a single SLS/Orion system at $4.1 billion per launch for Artemis I through IV, although the Agency’s ongoing initiatives aimed at increasing affordability seek to reduce that cost.
- 47 Building and launching one Orion capsule costs approximately $1 billion, with an additional $300 million for the Service Module supplied by the ESA through a barter agreement in exchange for ESA’s responsibility for ISS common system operating costs, transportation costs to the ISS, and other ISS supporting services.

Verdicts (SLS Block 1 row):
- Note's "~$4.1B ... per Artemis flight and includes Orion and its service module" = **EXACT pin (+0.00%)** - scope matches exactly (rocket + ground ops + Orion), which is why the note correctly warns it is NOT a launch price. Also backs the SLS Block 1B row's historical "$4.1B" price tag (same figure, same report).
- Note's "$2.2B SLS production + $568M ground systems per launch (IG-22-003)" = **verbatim match on both components**.

### IG-24-001 - NASA's Transition of the Space Launch System to a Commercial Services Contract (Oct 12, 2023)
Hosted: `full_texts/nasa_oig_2023_ig-24-001_sls_epoc_transition.pdf` (1,849,898 bytes; sha256 c943d8da528561e3...; canonical URL https://oig.nasa.gov/wp-content/uploads/2023/10/ig-24-001.pdf)

Verbatim anchors (sliced programmatically from the hosted PDF this round):
- Our analysis shows a single SLS Block 1B will cost at least $2.5 billion to produce—not including Systems Engineering and Integration costs—and NASA’s aspirational goal to achieve a cost savings of 50 percent is highly unrealistic.
- Footnote 20: the price has increased to $2.5 billion, an amount that reflects only costs of the major SLS contracts and does not include anticipated SE&I costs. The $2.5 billion reflects only the production costs for the Artemis IV mission and not the billions spent in development costs.
- a single SLS will cost more than $2 billion through the first 10 SLS rockets produced under EPOC.

Verdicts (SLS Block 1 row):
- Note's "'at least $2.5B' recurring (Oct 2023)" = **true pin (+0.00%) with honest scope label**: the audit figure is a Block 1B/EPOC *production* cost floor excluding SE&I - our note already carries that qualifier ("recurring"), so no correction needed; recorded for precision.
- Our launch-only band ($2.5-2.8B) vs OIG's own trajectory: low end +13.6% above the Nov-'21 $2.2B production figure, high end +12.0% above the Oct-'23 >=$2.5B floor - **consistency anchor** (scope and dollar-year differ between our band and each audit figure; NOT presented as an exact match).

### Space Shuttle row - citation-integrity check on "(Pielke & Byerly)"
- The note attributes ~$1.5B/flight (2011 dollars) + $54,500/kg to "Pielke & Byerly" without a venue. Their Shuttle-cost work is: **Nature 472:38, 'Shuttle programme lifetime cost', R.A. Pielke Jr. & Radford Byerly, published Apr 6 2011** (DOI 10.1038/472038d) - a News & Views piece; landing page verified live this round (abstract + citation metadata). The abstract cites their earlier Shuttle cost analysis as "Space Policy Alternatives Ch. 14, pp. 223-245; 1992" - the true primary source for the per-flight/per-kg methodology.
- **No Pielke/Byerly Shuttle paper exists in Environmental Science & Policy vol 14 issue 5** (or anywhere in that journal's entire 2011 volume): full TOC pulled via Crossref ISSN 1462-9011 for all of 2011 - 122 items across issues 1-8; the only Pielke hit is an Australian emissions-policy paper. If the citation was intended as ESP, it is a misattribution (revision candidate).
- The $54,500/kg figure itself holds independently: already-registered **jones2018** (T2) states "Shuttle $54.5k/kg" - **EXACT cross-anchor (+0.00%)**.
- Full text of the Nature N&V is paywalled and unreachable from this machine (browser daemon down all session; web.archive.org DNS-blocked here) -> **honest gap: full text not pulled**; number stands on jones2018 + abstract-level verification only.

**Revision candidates recorded (target repos read-only)**: Space Shuttle row citation should name Nature 472:38 / Space Policy Alternatives Ch.14 instead of bare "(Pielke & Byerly)". No value changes - all SLS numbers verified as cited.
### Round-52 deepening of the two hosted NASA OIG audits [T2; full text hosted] — criterion #2 completion pass over IG-22-003 + IG-24-001, plus anchors for the rows added by spacecost PR #3 (v1.16.0 launch-table re-audit, merged e831245)

Context: PR #3 grew launch_vehicles.csv from 36 to 76 rows and changed every price; delta_v_segments.csv values are UNCHANGED (R49's 730 m/s pin stays valid); operational_costs.csv gained one new row ('Expendable upper stage recurring cost', $4,800/kg). The SLS rows now cite the OIG reports correctly in-repo. This round completes the extraction of both audits and records what they settle about the NEW rows:

**(a) Space Shuttle row — first institutional anchor for the ~$1.5B whole-programme cost.** IG-24-001 p23 (case study, verbatim): "we estimate Space Shuttle operations costs increased approximately 38 percent to $1.45 billion per launch." This is a registered-source corroboration of the note's "~$1.5B in 2011 dollars" claim (-3.3% vs $1.45B) even though R51 established that its "(Pielke & Byerly)" citation is a misattribution — going forward the OIG case study, not Nature 472:38 (still paywalled), is the primary institutional anchor for this row's high end ($2.1B = $1.5B-2011 carried to 2026$; OIG figure sits -31.0% below that band top, consistent with an operations-cost scope vs a whole-programme one).

**(b) Falcon Heavy (expendable) row — institutional price ABOVE our band.** IG-24-001 p24: "the Agency contracted with Space X for a Falcon Heavy rocket at a cost of $178 million.36 In the near ter" (footnote 36 = the FY2021 NASA funding bill that removed the SLS requirement for Europa Clipper). vs our $154M centre +15.6%, vs band high $159M +11.9% -> **revision candidate**: a NASA institutional contract (2023$, full launch services for a TMI-class mission) sits above the whole vendor-derived band; zapata_2017's p15 '$90,000,000 Price to Private Customer' is the low anchor of that spread.

**(c) New 'Expendable upper stage recurring cost' row ($4,800/kg) + its sibling tank row — the RL10 assumption was 46-65% too high.** The note derives Centaur III structure as "~$30M for the stage against ~$20M for the RL10 it carries" -> $10M of structure. Both OIG audits give actual RL10-class engine prices far below that: IG-24 Table 1 (verbatim): "RL10 Engines Aerojet 10 flight engines for Artemis II through IV $68.9M" = **$6.89M/engine** (-65.5% vs the assumption); IG-22-003 p32: "NASA purchases the RL-10 engines on a contract separate from the Stages and Stages Production and Evolution Contract contracts at a cost of $10.8 million each; therefore, the cost for the Block 1B upper stages engines will rise approximately $32.4 million." If the ~$30M stage figure holds, implied structure is **$19.2M-$23.1M** (+92% to +131% vs $10M), i.e. $10,213-$12,293/kg on ~1880 kg of structure — roughly **2x the tank row's value=6,000**, which is quoted as a LOWER BOUND -> **revision candidate** for 'Propellant tank recurring cost'. Honest gap recorded: the Centaur III stage price (~$30M) itself has NO institutional anchor in any reachable source (searched OIG/GAO/NTRS corpora + web); the F9 low end of the new row ("~$10M to build (Musk 2018)") is likewise a vendor statement, not an audited figure.

**(d) Full Table 1 element breakdown now extracted** (criterion #2): per Block 1B launch — EUS for Artemis IV, verbatim from Table 1: "Exploration Upper Stage for Artemis IV $482M "; core stages + long-lead materials + EUS V/VI ~$1.0B (Stages Production & Evolution Contract); SRBs **$336.2M**, down by the time Artemis IV launches — verbatim: "booster costs are projected to decrease by 29 percent from $470 million to $336 million by the time Artemis IV launches; however, th" (computed -28.5% — the only element with real cost reduction); RS-25 Restart & Production $582.7M = $24.3M/engine over 24 (vs Shuttle-era manufacturing cost **$104.5M** per engine, -76.8%); RL10 $68.9M; Universal Stage Adapter $19.9M; **totals $2.5B per launch / $20.4B contract value**. Program scale: EPOC total could reach **$25B over 10 launches** ("NASA's most expensive Moon to Mars endeavor"); production stays >$2B for the first 10 rockets and ~$2.5B through Artemis VIII; the 50%-reduction target ($1.25B) judged "highly unrealistic". Data rights: duplicating core+EUS without them would exceed **$4.5B + 10 years**; engine duplication >**$3B**. Commercial context from the same report: Atlas V base price rose ~$50M/launch (LSP I->II) then fell ~$30M once Falcon 9 v1.1 could compete; crew seats $55M SpaceX vs $80M Roscosmos.

**(e) Program-level context from IG-22-003** (criterion #2): Artemis campaign **$93B FY2012-FY2025** in BOTH reports (mutual validation; SLS program = 26% / $23.8B per IG-24 p7); Orion development contract grew from a $3.9B Constellation base to **$13.8B by Aug 2021**, Production & Operations Contract $2.7B (~$1B/capsule + $300M ESA SM barter — the components of R51's $4.1B pin); HLS FY2021 funding gap ($850M received vs $3.4B requested) led to sole-source SpaceX at ~$2.9-3.0B potential total (initial awards Blue Origin $479.7M / Dynetics $239.7M / SpaceX $139.6M); CLPS max $2.6B through 2028 (VIPER $230.8M Astrobotic, PRIME-1 $47.0M Intuitive Machines, Masten $79.9M); Gateway PPE+HALO $1.6B + SpaceX logistics services $7.0B/15 yr; six major SLS element contracts = $20.4B (agrees with IG-24 Table 1 total).

**Anchor validity after PR #3**: delta_v_segments unchanged -> R49 pin valid; operational_costs values unchanged except the new row audited above; environments.csv stamps only; all four launch_vehicles SLS/Shuttle rows re-read and consistent with their OIG citations.
