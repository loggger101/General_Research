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

