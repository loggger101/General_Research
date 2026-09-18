# Master Index — General Research

Every source in this repo, what tier it is, how much of it we can actually use,
and which pipeline table/cell it backs or could replace. `sources.csv` holds the
same data machine-readable (one row per item, with domain dir); each domain also
keeps its own `<domain>/FINDINGS.md` with the prose and per-number comparison
tables.

Legend for **access**:
- `full_text_hosted` — full PDF committed under `<domain>/full_texts/`, legally redistributable (arXiv preprints, NASA public-domain docs, CC-BY articles).
- `open_not_pulled` — open access but not downloadable from this machine (bot-block) or license needs a user decision; recorded with URL + reason.

## Domain 1 — Density by spectral type, PGM factors, population statistics

_Backings: `catalog.py` per-spectral-type density and PGM factors; ranking quality of the whole pipeline._

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| carry2012 | T1 | Carry, "Density of asteroids" (PSS 60:537; arXiv preprint hosted) | full text hosted | **Table 3 = measured avg density per Bus-DeMeo class** — the direct anchor for all 32 `TAXONOMY_COMPOSITION` rows. S/X/Cgh/D agree; B/L/K sit ~0.7–1 g/cm³ below our values (revision candidates) |
| simda2024 | T3 | SiMDA live archive (Kretlow; PDS SBN dataset) + derived per-class stats committed | open service, derived CSV hosted | 428 measured bodies with taxonomic class → median-based anchors for 20 classes; corroborates the B/L/K discrepancy and D-row agreement |
| dziadura2023 | T1 | Dziadura et al., Gaia DR3 Yarkovsky + bulk density of NEAs (A&A 680 A77, CC-BY-4.0) | open not pulled (publisher bot-blocks this machine; no arXiv version) | largest peer-reviewed density sample of the *target population* (NEAs); long-term anchor to replace both above once pulled from a normal browser session |
| lodders_palme2009 | T2 | Lodders & Palme, CI-chondrite abundance table (72nd MetSoc abstract, LPI-hosted) | full text hosted | PGM baseline chain: CI bulk-rock PGM ≈3.29 ppm ÷ metal fraction → ~37 ppm in the metal phase — validates `catalog.py`'s 1× calibration claim with a traceable derivation |
| epsc2022_context | T2 | "Composition of large asteroids collided with the Earth" (EPSC-2022) | open not pulled (Copernicus login wall; abstract via Crossref) | context for `PGM_ENRICHMENT_BY_TYPE` differentiation argument — no numbers extracted this round |

## Domain 2 — Composition → commodity value mapping

_Backings: `mineral_value.py` in-pipeline mineralogy, destination pricing._

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| hein2020 | T1 | Hein, Matheson & Fries, "A Techno-Economic Analysis of Asteroid Mining" (Acta 174:59; arXiv v11 hosted) | full text hosted (arXiv preprint; journal version paywalled) | the external TEA to calibrate against end-to-end: Pt demand curve anchored at ($40,449/kg, 254 t/yr), water-vs-Pt market split matches our commodity classes |
| nat_dms2023 | T1 | DES metal extraction from asteroid proxies (Sci Rep 13:6497, CC-BY-4.0) | full text hosted | **85% surface metal / 15% silicate** for Psyche-like NEAs vs our M-row `metal_fraction=0.50` — the biggest value-side discrepancy found in round 1; also first lab proof of space-feasible beneficiation chemistry |
| asime2018 | T2 | Graps et al., ASIME white paper on asteroid composition (arXiv:1904.11831) | full text hosted | reliability bounds for the spectral-type→composition step: water up to 22% in meteorites; hydration correlates with albedo <7.5% — a guardrail our pipeline lacks |
| lewicki2023 | T2 | Lewicki et al., decadal white paper (arXiv:2103.02435) | full text hosted | "Mine Project Value Curve": valuation should carry an explicit knowledge-confidence discount — conceptual basis for revisiting our utility factors |
| cannon2023 | T1 | Cannon, Gialich & Acain, "Precious and structural metals on asteroids" (PSS 215:105608) | **open not pulled — OA but CC-BY-NC-ND; user decision pending** + publisher bot-blocks this machine | THE external benchmark for per-class recoverable-metal economics ("Harvard study" news cycle); commit full text only if you accept the NC clause for a public repo |

## Domain 3 — Δv budgets and propulsion performance tables

_Backings: `spacecost/delta_v_segments.csv`, Isp rows of `propellants.csv`._

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| elvis2011 | T1 | Elvis et al., "Ultra-Low Delta-v Objects…" (arXiv:1105.4152) | full text hosted | easy-NEA segment (<4.5 km/s boundary, 65/6699 NEOs) **confirmed exactly**; also the true source of our average-NEA value — population Δv distribution peaks at 6.65 km/s (Benner/Shoemaker-Helin compilation); hydrolox Isp cross-check (RL-10/J-2X, v_ex=4.4 km/s) |
| ieva2014 | T1 | Ieva et al., NEOSURFACE low-Δv NEO survey (arXiv:1406.5027) | full text hosted | ⚠️ **currently MIS-CITED** on our average-NEA row: this is a 13-object targeted survey (all <10.5 km/s), it contains no population median — re-point that citation to elvis2011; valid source for easy-NEA class characterization |

## Domain 4 — Launch cost per kg (history, projections)

_Backings: price rows of `spacecost/launch_vehicles.csv`; the Stage 4 cost cascade._

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| hf_dataset | T3 | juliensimon/launch-cost-to-leo — 63-vehicle structured dataset (parquet committed, access date 2026-09-17) | full text hosted | machine-comparable external table for all 36 of our rows: **5 exact matches**, config-mismatch labels on 4 rows (PSLV-XL/Vega C/H-IIA/FH), Long March 5 flagged — same name+payload carries an 83% spread between sources → adopt low/high bands |
| jones2018 | T2 | Jones (NASA Ames), "The Recent Large Reduction in Space Launch Cost" (ICES-2018-81, NTRS) | full text hosted | historical baseline: Shuttle $54,500/kg → commercial ~$2,700–3,900/kg, factor of ~20 — the trend every "launch no longer dominates" claim in our README rests on |

## Domain 5 — In-space storage / ISRU / operational costs

_Backings: `storage_systems.csv`, `operational_costs.csv`, environment penalties._

| id | tier | source (short) | access | backs / could replace |
|---|---|---|---|---|
| lac_bac_2024 | T1 | Local vs broad area cooling for LH₂ boil-off reduction (arXiv:2412.11720) | full text hosted | **anchors our hydrolox 0.05%/day** at the top of a peer-reviewed range (HePUR insulation: 0.04%/day; perlite: 0.24%/day); reliquefaction energy 5 kWh/kg for ZBO economics; LAC architecture = why depots can afford active boil-off control |
| zero_bo_off_2025 | T1 | Zero-boil-off LH₂ transfer strategies, export-terminal case study (arXiv:2512.04609) | full text hosted | peer-reviewed lower bound for our 3% in-space transfer-loss row: 0–0.24 wt% with VSD pump / 0.76–1.06 wt% fixed-speed — `range_low` should move toward ~1 once space-rated hardware exists (ground-seaborne caveat recorded) |
| ssap_2021 | T1 | Silicate-Sulfuric Acid Process for ISRU (arXiv:2107.05872) | full text hosted | **first per-asteroid-type beneficiation yield table** (per 1000 kg silicates, 4 asteroid mineralogies + Moon/Mars): external check on Module 2's commodity split; CM-vs-CI spread within one type (375 vs 65 kg Fe) argues for subtyping; ~950 °C processing-temperature anchor |

---
## Research log

- **Round 1** (2026-09-17): all five domains processed. 17 sources: T1×10, T2×5, T3×2; full texts hosted for 13 items (arXiv preprints, NASA NTRS public-domain docs, CC-BY articles, LPI-hosted abstracts), 4 recorded as `open_not_pulled` with reasons. Every item was access-verified live from this machine before recording. Headline findings:
  - **Domain 1**: B/L/K density rows sit ~0.7–1 g/cm³ below two independent anchors (carry2012 Table 3 + SiMDA medians) — top candidates for a `TAXONOMY_COMPOSITION` revision; S/X/Cgh/D well-anchored.
  - **Domain 2**: M/Xe metal fraction likely under-modelled by ~70% vs the peer-reviewed surface estimate (85%); PGM baseline now has a traceable derivation chain.
  - **Domain 3**: citation correction — average-NEA row cites arXiv:1406.5027 but its value comes from Elvis/Benner's population peak (6.65 km/s).
  - **Domain 4**: no launch-price errors; Long March 5 needs range bands (83% source spread); Starship row correctly labeled contract-anchored vs aspiration.
  - **Domain 5**: hydrolox boil-off anchored at top of peer-reviewed range; transfer-loss `range_low` has a cited lower bound (~1 wt%).
- **Round 0** (2026-09-17): repo scaffolded; domains, tiers and access rules defined. No sources yet.
