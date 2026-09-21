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

## Round-4 additions — C-type hydration measured, and the spectral-bias it implies

### ryugu_hydrated_2023 [T1] — "A dehydrated space-weathered skin cloaking the hydrated interior of Ryugu", Nature Astronomy 7:170–181 (Feb 2023), DOI 10.1038/s41550-022-01841-6
- **Full text hosted**: `full_texts/ryugu_dehydrated_skin_hydrated_interior_nature_astronomy_2023_s41550-022-01841-6_CC-BY.pdf` (7.2 MB; verified live from this machine via nature.com direct PDF — same route that worked for bennu_volatiles_2025). CC-BY per OpenAlex license record.
- **What it is**: lab study of Hayabusa2 Ryugu grains showing the C-type surface carries a dehydrated, space-weathered skin (dehydroxylation of saponite/serpentine) over an interior that still retains structural –OH — i.e. the bulk body IS hydrated even where spectra look dry.
- **Key numbers** → `extracted_data/ryugu_hydrated_interior_key_numbers.csv`: ~66% (4/6) of examined grains show weathering; dehydration extends ≥1.5 µm below the surface; pristine-grain O/cation ratios confirm interlayer H₂O largely lost but structural –OH retained, consistent with thermogravimetric analysis of Ryugu grains.

### What this settles for `TAXONOMY_COMPOSITION`
- **The ice_fraction rows carry a systematic bias we can now name**: our per-type water fractions are inferred from spectral/physical properties of the *surface* (albedo bands, thermal inertia), but this paper shows C-complex surfaces dehydrate by exactly the same dehydroxylation process our `Water liberation energy` row prices. A weak 2.7 µm band can mean weathered skin rather than bulk dryness — so **spectral-based volatile estimates for C-types are biased LOW**, and our ice_fraction values (0.10–0.20) should be read as *surface-representative lower bounds*, not bulk means.
- This is the C-type companion to bennu_volatiles_2025's B-type result: between the two, both of our best-studied hydrated types now have returned-sample evidence that their interiors hold more volatiles than their surfaces advertise. No table change applied — this changes how the existing numbers should be *interpreted* (and possibly nudged up), which is a user decision like round 3's carbon_fraction flag.

### ryugu_soluble_organics_2023 [T1] — "Soluble organic molecules in samples of the carbonaceous asteroid (162173) Ryugu", Science (2023), DOI 10.1126/science.abn9033
- **Access**: OA per OpenAlex, but both HAL mirror routes bot-block this machine (Anubis challenge page returned instead of PDF — verified). Recorded `open_not_pulled`; pullable from a normal browser.
- **Abstract (as published via OpenAlex)**: Hayabusa2 Ryugu surface samples analyzed for organics; identified CHNOS molecules formed by methylation, hydration, hydroxylation and sulfurization reactions — amino acids, aliphatic amines, carboxylic acids, PAHs and N-heterocycles with properties consistent with abiotic origin.
- **Pipeline mapping**: the C-type organic-inventory companion to bennu_volatiles_2025's B-type numbers; together they bracket what "carbon_fraction" means for both of our hydrated reference types (B vs C).

### ryugu_macromolecular_om_2023 [T1] — "Macromolecular organic matter in samples of the asteroid (162173) Ryugu", Science (2023), DOI 10.1126/science.abn9057
- **Access**: OA per OpenAlex; CNRS HAL mirror bot-blocked from this machine (same Anubis challenge). Recorded `open_not_pulled`.
- **Abstract (as published via OpenAlex)**: Ryugu macromolecular organic matter contains aromatic + aliphatic carbon, ketone and carboxyl groups; spectroscopic features consistent with chemically primitive CCs that experienced parent-body aqueous alteration; morphology = nanoglobules + diffuse carbon associated with phyllosilicate and carbonate minerals; D/N-15 enrichments indicate formation in the early Solar System.
- **Pipeline mapping**: confirms Ryugu's organic carbon is *aqueously altered* — direct sample-level support for treating C-type bodies as hydrated parent-body fragments (the premise behind `ice_fraction` > 0 on every C-complex row).

## Round-4 status (domain 2)
Both reference types now have returned-sample volatile/organic anchors: B = bennu_volatiles_2025 + ryugu_hydrated_2023's comparison data; C = ryugu_hydrated_2023 + the two Science organic papers (OA-pending). The domain-2 question "what does a spectral type actually contain" now has measured answers for both ends of the hydrated range, with one systematic bias (surface weathering) explicitly named.

## Round-8 addition — per-class carbon anchor + the C/CI endmember of our volatile range (both returned samples)

### glavin_2018 [T2] — Glavin, Alexander, Aponte, Dworkin, Elsila & Yabuta, "The Origin and Evolution of Organic Matter in Carbonaceous Chondrites and Links to Their Parent Bodies" (NASA chapter; NTRS 20180004493)
- **Full text hosted**: `full_texts/glavin_et_al_2018_origin_evolution_organic_matter_carbonaceous_chondrites_NTRS_20180004493_publicdomain.pdf` (2.1 MB, 67 pp; verified live from this machine: NTRS API + PDF download OK). Public domain as a US-government work.
- **Key numbers** → `extracted_data/glavin_2018_chondrite_volatiles_key_numbers.csv`: carbon abundance across C-types runs **~0.1 wt% (CK) up to ~5 wt% (CI)**; IDPs average ~12 wt% C (~half organic); per-class hydration mineralogy table (serpentine/saponite/smectite present in CI, CM, CR + Tagish Lake; tochilinite concentrated in CM2s).

### What this settles
- **The `carbon_fraction` rows now have their first measured per-class anchor — and it shows the defaults encode a different definition than bulk elemental carbon.** TAXONOMY_COMPOSITION carries 22–30% carbon for B/C-complex; the most carbon-rich real C-type (CI) is ~5 wt%. That 4–6× gap means our fractions must be read as 'carbon-bearing material' (organics + inorganic carbonates + fine-grained dust), not elemental C. This round's data gives any future re-calibration a measured starting point per class instead of the current defaults.
- **The `ice_fraction` rows get their mineralogical grounding**: for C-types, 'ice' is actually phyllosilicate-bound water (serpentine/saponite/smectite) — real and class-specific, with the hydration gradient CI > CM > CV matching our B-row-sits-above-C-rows ordering.

### ryugu_ivuna_2023 [T1] — Yokoyama et al., "Samples returned from the asteroid Ryugu are similar to Ivuna-type carbonaceous meteorites", Science 379(6634):786 (DOI 10.1126/science.abn7850)
- **Access**: full text verified live this round via Hokudai's HUSCAP institutional repository (the HAL route was Anubis-blocked in round 4 — a different, working path). BUT the repository copy is explicitly an **author's version posted "by permission of AAAS for personal use, not for redistribution"** → recorded `open_not_pulled` with metadata + key findings; NOT hosted (hosting would violate the stated rights).
- **Key findings** → `extracted_data/ryugu_ivuna_2023_key_findings.csv`: Ryugu = Ivuna-type CI1 endmember; structural water similar to CI chondrites, but **interlayer/free water is largely absent — lost to space**; samples stayed below ~100 °C from alteration to present.

### What this settles
- **Both ends of our volatile range now rest on returned samples**: B = bennu_volatiles_2025 (round 3), C/CI = ryugu_ivuna_2023 + the two Ryugu organics papers (rounds 4, recorded OA-pending).
- **The critical caveat for `ice_fraction` pricing**: returned C-type samples contain essentially no free ice. Any value priced at the $2500/kg in-space water proxy overstates what is extractable from a C-complex body without structural-water liberation processing (the kleinhenz_2016/2018 energy chain, domain 5). The pipeline's `ice_fraction` should be read as 'hydrated-mineral content', with the recoverable fraction gated by that processing step — this round makes that distinction explicit and sourced.

## Round-8 status (domain 2)
Domain 2 is now anchored at both ends of its volatile range (B + C/CI returned samples), has a measured per-class carbon baseline, AND names the exact mineralogy behind `ice_fraction`. Remaining open items in this domain are unchanged: epsc2022_context (Copernicus login wall) and the PGM-enrichment differentiation argument still rests on usgs_pp1802n alone.

## Round-11 addition — S-type density gets a meteorite-side anchor; PGM gradient gets its differentiation mechanism

**wilkinson_robinson_2000 (T1, open_not_pulled)**: 82 samples / 72 ordinary chondrites measured to ~1% accuracy by modified Archimedes method. H group **3.44±0.19**, L **3.40±0.15**, LL **3.29±0.17 g/cm^3** (1-sigma); intra-group spread 3.0–3.8 at near-invariant bulk composition — density tracks porosity/texture, not chemistry, within a group. This is the meteorite-side anchor for our S row: hand samples of chondritic material sit ~3.3–3.4 g/cm^3 while carry2012's asteroid-scale S median is 2.70 — the gap is km-scale macro-porosity/rubble structure, exactly what `TAXONOMY_COMPOSITION` encodes (S=2.70). Wiley bot-blocks; no preprint found.

**mandler_elkins_tanton_2013 (T1, open_not_pulled)**: CC-BY per OpenAlex but only the Wiley route exists and it 403s from this machine. Best-fit Vesta model = ~60–70% equilibrium crystallization of a magma ocean + continuous extraction of residual melt into shallow chambers; predicts metallic core / mantle (dunites, harzburgites, diogenites) / basaltic crust (eucrites). This is the **mechanism** behind `PGM_ENRICHMENT_BY_TYPE`: eucrites are late-stage residual melts from a body whose metal segregated into its core, so their HSE/PGM budget is depleted vs primitive chondritic material by exactly that process. With usgs_pp1802n (measured Pt numbers) the whole gradient now has both legs: USGS = abundances, this paper = why they differ by type.

## Round-12 addition — second M-type density (farnocchia_2024) + ISRU economics anchor

**farnocchia_2024**: see domain 1's round-12 block for the full write-up; it is registered here too because M-row composition/density feeds both domains.

## Round-36 addition — per-type MATERIAL anchors (criterion #3: "asteroid composition and the materials we can find in each type, plus its ratios")

**The gap this round closed.** Densities per spectral class were already anchored (carry2012 Table 3 + simda2024 medians), but `TAXONOMY_COMPOSITION`'s *material* content — the metal/silicate/carbon/ice mass fractions and the minerals lists for ~30 types — had no citable source anywhere in this repo. The three items below change that, each verified from full text on this machine (page citations in `extracted_data/r36_per_type_materials_key_numbers.csv`, 18 rows).

### elkins_tanton_2020_psyche_preflight — JGR Planets 125:e2019JE006296 [T1, open_not_pulled]
- **Why it matters first**: `catalog.py`'s M-row note already cites "Elkins-Tanton et al. 2020" for the claim that Psyche's metal content is "roughly 30–60%" — but this paper was never registered in General_Research, so a load-bearing citation pointed at nothing verifiable here. Registered now; gap closed.
- **Access**: CC-BY-**NC** license (verified in PDF front matter) + AGU landing page 403s from this machine ⇒ `open_not_pulled` per the repo legend (same class as cannon2023). Analyzed from the author mirror https://benweiss.mit.edu/s/Elkins-Tanton_2020_JGR.pdf — HTTP 200, application/pdf, 4.4 MB, verified live this round; NTRS search returned no index entry for it.
- **Key extracted numbers** (all verbatim from the full text):
  - p10 (Sec 2.5): Psyche predicted **"between ~25 vol% metal and ~60 vol% metal"**; Point D = ~25 vol% metal + ~55 vol% magnesian pyroxene + ~20% pore space.
  - **Comparison against pipeline**: our M-row mass fractions (metal 0.50 / silicate 0.45) convert to ≈34 vol% metal at ρ_metal≈7.8 vs ρ_sil≈3.6 g/cm³ → **INSIDE the peer-reviewed band; row AGREEs.** Note: catalog.py paraphrases "30–60%" but the paper's verbatim band is ~25–60 vol% — a future spacecost edit could quote it exactly (read-only for this process).
  - Surface endmembers, p9: 90 wt.% metal / 10 wt.% opx (Hardersen) → only 6 wt.% opx (Sanchez) → strictly metal powder (Fornasier); pairs with nat_dms2023's 85/15 surface figure as the high end of the *surface* range.
  - Retained silicate veneer scenario, p13: **25–80 km** of silicate rock on a stripped core (Johnson et al., 2019).
  - Meteorite-analog density table, p10: iron 7,000–8,000 / pallasite 4,100–7,800 / mesosiderite 3,100–7,200 kg/m³ vs Psyche ~4,000 (range 3,400–4,100) — the density argument that rules out a solid-metal M-type; pallasites = Fe-Ni metal + olivine Fa11-20 at **~65 vol% olivine** with Ni ~9–12 wt% (p11).
  - CB chondrites, pp11–12: **~60 vol% metal**, skeletal olivine Fa2-4 + cryptocrystalline pyroxene Fs2 — the high-metal carbonaceous endmember relevant to our Xc/Cb rows (our Cb row carries only 1% metal; flagged as a candidate revision, not applied).

### reddy_asteroids_iv_mineralogy — Asteroids IV chapter, UAPress 2015 pp.43–63 [T1, full_text_hosted]
- **What it is**: the definitive review of asteroid mineralogical interpretation (Reddy, Dunn, Thomas, Moskovitz & Burbine; book DOI 10.2458/azu_uapress_9780816532131). Hosted copy = arXiv:1502.05008v1 author preprint (arXiv comment field verbatim: "Chapter to appear in the Space Science Series Book: Asteroids IV, 51 pages"); abs-page metadata verified live this round.
- **Key extracted numbers** — first per-type material anchors for `TAXONOMY_COMPOSITION`:
  - A-types = **monomineralic olivine Fo85–93**, p8 (RMS 5 mol% calibration) → anchors our A-row minerals list [olivine] + metal_fraction=0.05 (monomineralic ⇒ essentially no free metal).
  - R chondrites carry **65–78% olivine by volume** ("higher abundances of olivine than the ordinary chondrites"), p9 → anchor for A/R silicate-dominant rows (our A/R: silicate_fraction=0.90 — consistent).
  - HED/V-type pyroxene range **Fs23–56 / Wo2–14**, Burbine et al. 2007 calibrations accurate to within 3 mol% Fs and 1 mol% Wo, p7 → anchor for V-row minerals [pyroxene, plagioclase, olivine].
  - S/Q = ordinary-chondrite analogs via Dunn et al. 2010b Fa/Fs calibrations (<2 mol% error) built on ~50 measured OC powders (PSD-XRD modes down to 1 wt%), pp7–9 → anchor for S-row minerals [olivine, pyroxene, nickel-iron].
  - **Ground truth**: Itokawa = LL chondrite with Shkuratov model ol/(ol + low-Ca pyx) = **76%** (Fig.5 caption p26; Hayabusa sample-confirmed); Eros plots in the L/LL zone with identical Fs/Fa from NEAR NIS and ground-based spectra (Fig.6 captions pp26–27). Two spacecraft verifications of "S-row = ordinary chondrite".
  - Context, p8: A/S/Q/V meteorite analogs constitute **91% of the terrestrial meteorite collection** — i.e., our table is anchored where most ground truth exists; rows without such coverage (D/T/P/Xc) legitimately remain approximate.

### lodders_2010_solar_abundances — Kodaikanal lecture notes [T2, full_text_hosted]
- **What it is**: Lodders' solar-system abundance compilation with the complete CI-chondrite composition table (Orgueil as representative CI). Hosted copy = arXiv:1010.2746v1 (marked "2010 Preprint" on p.1; published in Astrophys. Space Sci. Proc. 57:379–417, Springer 2010) — preprint of a peer-reviewed proceedings volume ⇒ T2 per repo convention.
- **Key extracted numbers** (Table 2, pp8–10): total C = **34,800 ppm = 3.48 wt%**; Fe/Mg/Si/O/S = 185,000/95,800/107,000/459,000/53,500 ppm (18.5/9.6/10.7/45.9/5.35 wt%); PGM suite Ru 0.686 + Rh 0.139 + Pd 0.558 + Os 0.493 + Ir 0.469 + Pt 0.947 = **exactly 3.29 ppm** CI bulk.
- **Comparison against pipeline**: (a) our B/C-complex carbon_fraction defaults of 0.25–0.30 are ~7–9× bulk *elemental* C — independently confirms the glavin_2018 flag that those fractions encode a broader "carbon-bearing material" definition, not elemental C; (b) Fe/Mg/Si cross-checks Cannon et al.'s Table 3 CI values (Fe 18.88 / Mg 9.54 / Si 10.70 from Palme et al. 2014) — two independent compilations agree to <2%; (c) the PGM sum independently reproduces the lodders_palme2009 baseline in domain 1 that anchors `PGM_ENRICHMENT_BY_TYPE` calibration — the whole PGM chain now has a second, element-by-element verifiable leg.

### Open items after R36
- Xc/Cb metal fractions: CB-chondrite ~60 vol% metal endmember (above) vs our Cb=0.01/Xc=0.25 — candidate revision when spacecost is editable; not applied silently.
- M-row paraphrase "30–60%" → verbatim "~25–60 vol%" quote available for a future edit.
- D/T/P rows remain unanchored at material level (no comparable ground truth exists in the hosted literature set) — honest gap, recorded rather than papered over.
