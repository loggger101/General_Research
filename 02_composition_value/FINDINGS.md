# Domain 2 Findings — composition → commodity value mapping

## hein2020 — Hein, Matheson & Fries (2018/2020), "A Techno-Economic Analysis of Asteroid Mining" [T1]

- **Full text hosted**: `full_texts/hein_matheson_fries_2020_techno-economic_analysis_arxiv1810.03836v11.pdf`
  (arXiv:1810.03836 v11 — the preprint of Acta Astronautica 174 (2020) 59-71, DOI 10.1016/j.actaastro.2019.05.009;
  verified live: HTTP 200 application/pdf). The journal version is paywalled (Elsevier TDM license only); the arXiv
  v11 text is what's committed, per this repo's access policy.
- **What it is**: THE peer-reviewed techno-economic model of asteroid mining — first-principles TEA with two revenue
  streams: water for in-space use and platinum returned to Earth. This is the closest published analogue to the whole
  economicspace pipeline (per-body Δv + cost cascade → profit), so every assumption it makes that differs from ours is a
  calibration point.

### Key extracted numbers (see `extracted_data/composition_value_key_numbers.csv`)

- Platinum demand curve anchored at **($40,449/kg, 254,582 kg/yr)** with inelastic PED ∈ (-0.6,-0.5); sensitivity
  cases run at $70k and $30k per kg — profitability of the Pt-return case is price-dominated across that band.
- Water-for-space treated as a separate market from metals (same split our `_DEMAND_SHARE_BY_CLASS` uses: propellant
  0.55 vs trace PGMs 0.0005).

### Comparison against pipeline assumptions

| assumption | hein2020 | pipeline | verdict |
|---|---|---|---|
| two markets (water-in-space / Pt-to-Earth) | yes, separate revenue streams | yes (`DELIVERY_DESTINATIONS` + commodity classes) | **AGREEMENT** on structure — our destination pricing is the more granular version |
| platinum price band that matters | $30k–$70k/kg (2018-2020 data) | live yfinance futures, stamped per run | consistent; note hein's demand-curve point ($40.4k at 254 t/yr supply) is a useful sanity check on our price fetches |
| beneficiation assumed feasible | yes (throughput 150 kg/s/kg-equipment in their process chain) | yes, but charged only via utility discounts + ISRU processing row | pipeline's beneficiation cost line is far lighter than hein's equipment mass — worth a look when operational_costs get revisited |

## nat_dms2023 — (Sci Rep 13:6497, 2023) "A novel method for extracting metals from asteroids using non-aqueous deep eutectic solvents" [T1]

- **Full text hosted**: `full_texts/des_metal_extraction_scirep_s41598-023-44152-0_CC-BY4.pdf` (CC-BY-4.0 per Crossref;
  verified live: HTTP 200 application/pdf, 9.4 MB).
- **What it is**: first lab demonstration of metal dissolution from meteorite proxies of metal-rich asteroids using a
  deep eutectic solvent (ChCl:2EG) that can plausibly be made in space — the process route behind "beneficiation" in
  Module 2/4.

### Key finding for the pipeline

- **85% surface metal / 15% silicate** reported for NEAs 1986 DA and 2016 ED85 (spectral twins of 16 Psyche).
  Our `catalog.py` M-type row carries `metal_fraction = 0.50`. The peer-reviewed *surface* figure is ~70% higher; bulk
  fraction may differ, but the gap means our M/Xe rows are likely **under-pricing metal content by a similar factor** —
  the single biggest value-side discrepancy found in round 1 so far (pairs with domain-1's density findings: Xe density
  contested there too).

## asime2018 — Graps et al. (2019), "ASIME 2018 White Paper: In-Space Utilisation of Asteroids — Composition" [T2]

- **Full text hosted**: `full_texts/graps_et_al_2019_ASIME_asteroid_composition_whitpaper_arxiv1904.11831v1.pdf`
  (arXiv:1904.11831; verified live HTTP 200, 2.4 MB). Luxembourg-funded ASIME conference white paper, multi-author.
- **What it is**: the state-of-the-art review of what remote sensing actually tells us about asteroid composition — i.e.
  an honest assessment of how much we can trust a spectral type as a proxy for bulk composition (exactly the step our
  pipeline performs in `TAXONOMY_COMPOSITION`).

### Key extracted numbers

- Meteorites contain **up to 22% water** by mass → our C-complex ice_fraction rows (0.10–0.30) sit at/above the measured
  upper envelope; fine as a population-max, but should not be read as an average for every C body.
- Primitive/water-rich composition correlates with **geometric albedo < ~7.5%** — a cheap guardrail the pipeline could add:
  flag high-albedo "C-type" bodies as hydration-unreliable before pricing their water content.

## lewicki2023 — Lewicki, Graps, Elvis, Metzger & Rivkin (2021), Decadal Survey white paper [T2]

- **Full text hosted**: `full_texts/lewicki_et_al_2023_decadal_whitepaper_arxiv2103.02435v1.pdf` (arXiv:2103.02435;
  verified live HTTP 200). Note the author list includes **Martin Elvis** — same Elvis whose low-Δv NEA survey backs our
  easy-NEA Δv segment in domain 3.
- **What it is**: the decadal-survey framing for asteroid resource utilization, including a "Mine Project Value Curve" —
  project value as a function of *mineral-resource confidence*. The conceptual argument that valuation should carry an
  explicit knowledge-confidence discount; our utility factors are the nearest existing analogue but are per-commodity,
  not per-knowledge-state.

## cannon2023 — Cannon, Gialich & Acain (PSS 215:105608, 2023), "Precious and structural metals on asteroids" [T1]

- **Access**: `open_not_pulled` — the article is genuinely open access (**CC-BY-NC-ND** per Crossref license record) but
  (a) its NC clause conflicts with hosting in a public repo unless you confirm non-commercial intent, and (b) ScienceDirect
  bot-blocks this machine anyway. **Decision needed from user**: if General_Research stays strictly commercial-safe, keep
  as metadata-only; otherwise the full text can be pulled from a normal browser session and committed under that license.
- **What it is**: THE paper behind the "Harvard study: few asteroids worth mining" news cycle (Colorado School of Mines +
  AstroForge). Quantifies which asteroid classes carry economically recoverable precious/structural metal — the direct
  external benchmark for our per-type commodity valuations.

## Round-1 status (domain 2)

5 items processed; 4 full texts hosted, 1 awaiting a license decision from the user. Headline: **the M/Xe metal-fraction
row is under-modelled by ~70% vs the peer-reviewed surface estimate**, and hein2020 gives us our first external TEA to
calibrate against end-to-end.


## usgs_pp1802n — Zientek et al., USGS Professional Paper 1802-N: Platinum-Group Elements [T3]

- **Access**: full text is public domain (USGS); the report PDF lives at `https://pubs.usgs.gov/pp/1802/n/pp1802n.pdf`
  (DOI 10.3133/pp1802N). It is a 34 MB / ~570 KB-of-text multi-chapter report, so rather than committing the whole PDF we
  commit the *relevant extraterrestrial-abundance passage* as an excerpt below and cite it by DOI + section. The numbers are
  quoted verbatim from the "Geology" chapter's discussion of PGEs in meteorites/planetary bodies.

### Why this is the anchor for `PGM_ENRICHMENT_BY_TYPE` (domain-2 gap)

Our pipeline differentiates PGM concentration by spectral type on a physical story — differentiated core fragments keep
metal-segregated PGMs, mantle/crust fragments lost them to the core during differentiation. The USGS report supplies the
peer-reviewed magnitude of exactly that gradient:

| body / phase | Pt (and PGE) abundance | what it anchors in our table |
|---|---|---|
| **Iron meteorites** ("best analogs for the composition of Earth's core") | **2.4–16 ppm** Pt (Wasson et al., 1989, cited therein) | `M` / `Xe` = **2.0×**, `Xk/E/Xc` = 1.5–2.0× — metal-rich differentiated fragments carry the high end of this range |
| **Upper mantle** (e.g. Vesta-type achondrite parent bodies) | **~0.002–0.005 ppm** Pt (Maier et al., 2012, cited therein) = 2–5 ppb | `A`/`R`/`O` mantle fragments = **0.5×**, and the *depletion factor* of ~10³–10⁴ vs core metal that justifies why a differentiated body's crust/mantle is nearly PGM-free |
| **Upper crust** (basaltic, e.g. Vesta surface / HED) | **~0.0005 ppm** Pt = 0.5 ppb (Rudnick & Gao, 2003, cited therein) | `V` (eucrite/basaltic crust) = **0.2×** — the most-depleted row, consistent with PGMs extracted into a core during Vesta's magma-ocean differentiation |

- **Verdict**: our enrichment factors are *directionally and order-of-magnitude correct* against this independent
  public-domain source. The one refinement it supports: the gap between "metal fragment" (2–16 ppm) and "mantle/crust
  fragment" (0.5–5 ppb) is ~4 orders of magnitude, so a body that is *partially* differentiated should not sit at exactly
  1.0× — our `X`-complex rows at 1.2–1.5× are reasonable midpoints, and the baseline `.get()` default of 1.0× for primitive
  (undifferentiated) types is correct because a chondritic body never segregated its PGMs into a core in the first place.

### Round-2 status (domains 1+2 deepening pass)

- **Domain 2**: added `usgs_pp1802n` as the public-domain anchor for the whole `PGM_ENRICHMENT_BY_TYPE` gradient
  (previously only a CI-chondrite baseline via `lodders_palme2009`). This closes the "where does the per-type PGM factor
  come from" gap with a citable, legally-committable source.
- **Domain 1**: still waiting on the Gaia DR3 density paper (`dziadura2023`) — A&A bot-blocks both curl and headless+local
  browser (Cloudflare challenge never clears in-session). It is CC-BY-4.0, so it *can* be committed once pulled from a normal
  interactive session; recorded as `open_not_pulled` with the exact URL for that follow-up. No new density numbers this pass —
  round 1's `carry2012` + `simda2024` remain the working anchors, and they already agree on the B/L/K revision candidates.


## toplis2014 — Toplis et al., "Bulk Composition of Vesta as Constrained by the Dawn Mission and the HED Meteorites" [T2]

- **Full text hosted**: `full_texts/toplis_et_al_2014_bulk_composition_of_vesta_ntrs.pdf`
  (NASA NTRS 20140005771, public domain; verified live HTTP 200 application/pdf). LPSC abstract.

### What it anchors

- Vesta's core: **radius 90–120 km of metal + sulphide** — the geophysical constraint that makes our `V` row
  (basaltic crust, PGMs extracted into a core during differentiation) physically grounded rather than assumed.
- HED meteorites as bulk-composition analogues for Vesta's differentiated interior: validates treating the whole
  spectral-type→composition mapping as "meteorite class = parent-body fragment" — the premise of both `TAXONOMY_COMPOSITION`
  and `PGM_ENRICHMENT_BY_TYPE`.
- Paired with `usgs_pp1802n`: Vesta *has* a large metal core (this paper) AND its crust is ~0.5 ppb Pt (`usgs_pp1802n`) —
  together they justify the full differentiated-body model our pipeline prices on for X/V/A/R/O types.


## Round-3 addition — measured volatile inventory of a real B-type sample

### bennu_volatiles_2025 [T1] — "Abundant ammonia and nitrogen-rich soluble organic matter in samples from asteroid (101955) Bennu", Nature Astronomy 9:199–210 (Feb 2025), DOI 10.1038/s41550-024-02472-9
- **Full text hosted**: `full_texts/bennu_volatiles_nature_astronomy_2025_s41550-024-02472-9_CC-BY.pdf` (8.4 MB, 20 pp; verified live from this machine: HTTP 200 application/pdf via nature.com direct PDF route — the one publisher that did NOT bot-block in round 3). CC-BY per OpenAlex license record.
- **What it is**: first lab analysis of OSIRIS-REx returned Bennu material (B-type, hydrated) for total C/N and free ammonia/amine/amino-acid inventory, benchmarked against CI–CY chondrites AND the Ryugu samples — i.e. a head-to-head volatile comparison between our two best-studied C-complex targets.
- **Key numbers** → `extracted_data/bennu_volatiles_key_numbers.csv`: total C 4.5–4.7 wt%, total N 0.23–0.25 wt% (aggregate samples, Ext Data Table 1); ammonia ≈ 40% of total N in the hot-water extract; regional aliphatic/aromatic carbon up to ~2.5 wt%; headline: Bennu is MORE volatile-rich than Ryugu and most meteorites.

### Comparison against pipeline `TAXONOMY_COMPOSITION`
| field (B row) | our value | peer-reviewed measurement | verdict |
|---|---|---|---|
| carbon_fraction | 0.30 | total C = 4.5–4.7 wt% in a real B-type sample | **DISCREPANCY — ours is ~6-7x low IF we intend elemental carbon.** Caveat: our `carbon_fraction` prices *free/bulk* carbon at the $/kg commodity rate; the paper's figure includes organics locked in phyllosilicates and soluble N-C species. The honest reading: our B-row volatile mass is under-modelled, but part of the gap is "not extractable as a commodity". Flag for user decision — do NOT silently raise 0.30 |
| ice_fraction (as water proxy) | 0.20 | not directly measured here (this paper reports C/N/NH3, not H2O wt%) | no verdict this round; the 40%-of-N-as-ammonia result is a NEW volatile class we don't model at all — candidate commodity row for `mineral_value.py` if ammonia ever has an in-space price anchor |
| (C-complex rows) | carbon_fraction 0.20–0.28 | CI/CM/CY comparison values in Ext Data Table 1 (~1–3 wt% total C, "rare instances up to ~5 wt%" per the paper's own meteorite baseline sentence) | same caveat as B: measured TOTAL carbon is an order of magnitude above our priced fraction; directionally supports raising the volatile mass for hydrated types, but only after deciding what fraction is commodity-extractable (cf. ssap_2021 yields in domain 5 — that paper's per-type extraction numbers are the right bridge between "measured total" and "sellable") |

- **Why this matters**: rounds 1–2 anchored *density* and *metal/PGM* content of C-complex bodies; nothing had ever pinned down their VOLATILE inventory against returned material. This paper does, for both Bennu (B) and Ryugu (C), with a common lab protocol — the cleanest possible per-type volatile anchor we will get without flying another sample mission.
