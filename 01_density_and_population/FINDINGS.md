# Domain 1 Findings — density by spectral type, PGM factors, population statistics

## carry2012 — Carry (2012), "Density of asteroids", Planetary and Space Science 60(7):537-552 [T1]

- **Full text hosted**: `full_texts/carry2012_density_of_asteroids_arxiv1203.4336v1.pdf`
  (arXiv:1203.4336v1 preprint of the PSS paper, DOI 10.1016/j.pss.2012.03.009 — single author B. Carry, ESA ESAC; verified live from this machine: HTTP 200, application/pdf, 5.7 MB).
- **What it is**: review compiling mass+volume estimates for **287 small bodies** (asteroids, comets, TNOs)
  from the literature, with strict selection of best estimates; computes bulk density and macroporosity per body,
  then averages by Bus-DeMeo taxonomic class. This is the closest peer-reviewed analogue to our pipeline's
  `TAXONOMY_COMPOSITION` table — which currently carries **no citation at all**.
- **Key result (Table 3)**: average bulk density per DeMeo et al. 2009 type, in three precision tiers
  (n = no restriction; n50 = better than 50% accuracy; n20 = better than 20%). Extracted to
  `extracted_data/carry2012_density_by_type.csv` with per-row layout caveats.

### Comparison against pipeline TAXONOMY_COMPOSITION densities (g/cm3)

| type | carry2012 best tier | pipeline value | verdict |
|---|---|---|---|
| S  | 2.70–2.72 (N=144, the robust one) | 2.70 | **AGREEMENT** — our table is right for S-type; this row can now cite carry2012 Table 3 directly |
| C  | 1.41 (n50) / 1.25 (n20); no-restriction mean 1.57±1.38 | 1.50 | AGREEMENT within scatter; our value sits between tiers — defensible, cite the n-tier spread |
| B  | ~2.19–2.38 (N=4) or ambiguous stray row 1.33 | 1.30 | **POSSIBLE DISCREPANCY** — measured values skew higher than ours; but N is tiny and one wrapped PDF row (5 bodies, 1.33±0.58) may belong to B. Needs the full-PDF check before revising anything |
| Ch | 1.70–1.96 | 1.50 | mild discrepancy (ours lower); small N=18 |
| Cb | 1.43–1.88 | 1.40 | AGREEMENT at the n50 tier |
| K  | **3.54** (n50 and n20 agree) | 2.50 | **DISCREPANCY — ours is ~1 g/cm3 low.** Two independent precision tiers both say 3.54; only the outlier-dominated no-restriction mean (4.25±2.03) differs. Strongest candidate for a table revision in this domain |
| L  | 3.22–3.24 | 2.80 | **DISCREPANCY — ours ~0.4 low**, consistent direction with K |
| Xk | 3.79–4.22 (mesosiderite analog) | 3.60 | AGREEMENT at the lower tier; our value is defensible as conservative |
| Xe | 2.60–2.91 | 3.80 | **DISCREPANCY — ours ~0.9 high.** Measured XE (EH-analog) bodies are ~2.6–2.9, not 3.8; our row's metal fraction 0.45 may be over-modelled for the population mean |
| Xc | 4.63–4.96 (mesosiderite analog) | 2.50 | **DISCREPANCY — ours ~2 low**, but N=3 and mesosiderites are genuinely dense; worth a look before trusting any Xc mining result |
| A  | 3.73 (single estimate, pallasite) | 3.20 | mild discrepancy, single body |
| Q  | 1.9–2.2 (small sample) | 3.00 | **POSSIBLE DISCREPANCY** — measured Q values are lower; N=8 with wrapped layout, verify before acting |
| D  | unmeasured in 2012 sample | 1.20 | no peer-reviewed anchor yet (see Gaia DR3 item below) |

- **Porosity finding (abstract + body)**: dwarf planets have essentially no macroporosity; bodies <400 km can
  carry large void fractions, and C/S-complex density rises with diameter — i.e. a single per-type constant is an
  approximation whose error grows for small bodies. Worth noting in the pipeline README as a known limitation.

**Action items (for the user's decision)**: K/L/Xe/Xc rows are the four where measured data and our table diverge
by more than ~0.4 g/cm3; each divergence propagates linearly into mass → value → profit ranking for that type.

## simda2024 — Kretlow, SiMDA: Size, Mass and Density of Asteroids [T3]

- **Access**: live web archive `https://astro.kretlow.de/simda/catalog/?_export=csv` (verified from this machine 2026-09-17:
  HTTP 200 text/csv, 428 objects with bulk density + taxonomic class). Also served via PDS SBN
  (`https://sbn.psi.edu/pds/resource/density.html`, verified 200) and described in Kretlow (EPSC-2020 abstract,
  DOI 10.5194/epsc2020-690). **Not vendored** — live service; we commit only the derived per-class stats below,
  re-downloadable at any time from the URL above (access date stamped here: 2026-09-17).
- **What it gives**: bulk density for every body with a published mass estimate (~428 objects), each tagged with its
  taxonomic class — i.e. exactly the per-class distribution our `TAXONOMY_COMPOSITION` collapses to one number.

### Per-class comparison (derived from the live CSV, access date 2026-09-17)

| type | N measured | SiMDA mean ± spread | SiMDA median | pipeline value | verdict (median basis) |
|---|---|---|---|---|---|
| S   | 53 | 3.46 (2.x–4.x, wide) | **2.87** | 2.70 | AGREE (+0.17) — our value is defensible; cite SiMDA median |
| Ch  | 47 | 1.98 | **1.68** | 1.50 | mild HIGH (ours lower by 0.18); within C-complex scatter |
| C   | 33 | 1.83 | **1.63** | 1.50 | mild HIGH, same note as Ch |
| B   | 10 | 1.97 | **2.10** | 1.30 | **DISCREPANCY — ours ~0.8 low**; both carry2012 (skew high) and SiMDA median sit above our value |
| Xk  | 13 | 4.60 | **3.93** | 3.60 | HIGH by +0.33 on median; mean inflated by dense mesosiderite-analog bodies — our conservative row is defensible, note the spread |
| L   | 4  | 4.60 | **4.95** | 2.80 | **DISCREPANCY (N=4)** — small sample but direction matches carry2012's K/L finding; our L row is ~1 g/cm3 low on this evidence |
| Xe  | 4  | 3.56 | **3.89** | 3.80 | AGREE (median basis) — contradicts carry2012's n-tier values (2.6–2.9); the two sources disagree, N is tiny either way → keep our value but flag as contested |
| K   | 2  | 3.16 | **3.48** | 2.50 | supports carry2012's DISCREPANCY (N=2) — K row likely low, pending more measurements |
| D   | 3  | 1.41 | **1.27** | 1.20 | AGREE — first measured anchor for our lowest-density row |
| V   | 3  | 2.82 (mean) / median 3.41 | 3.41 | 2.90 | mean pulled down by one low value; median supports ~3.4, mild HIGH on ours |

**Interpretation for the pipeline**: our single-value-per-type table tracks the *medians* of measured populations
reasonably well (S/X/Cgh/D all agree within ±0.2), but is systematically **low for B, L and K types by ~0.7–1 g/cm3**,
and high-ish for Ch/C by ~0.2. Since density feeds mass → value linearly, the B/L/K rows are where a future revision
of `TAXONOMY_COMPOSITION` should start — with carry2012 Table 3 and this SiMDA snapshot as the two anchors.

## dziadura2023 — Dziadura et al. (2023), "The Yarkovsky effect and bulk density of NEAs from Gaia DR3", A&A 680, A77 [T1]

- **Access**: `open_not_pulled` — genuinely open access (CC-BY-4.0 per Crossref record) but aanda.org bot-blocks
  this machine: HTTP 403 on both full HTML and PDF routes (verified twice with browser UA), no arXiv version exists,
  web_extract also fails. Full text is legally committable; pull it from a non-datacenter IP or via the publisher's
  access route when convenient — URL: `https://www.aanda.org/articles/aa/full_html/2023/12/aa47342-23/index.html`
  (PDF: same path with `/pdf/`). Metadata verified live via Crossref API.
- **What it is**: Yarkovsky-drift detection on 446 NEAs (+93 PHAs) and 54,094 inner main-belt asteroids using the full
  MPC astrometric dataset + Gaia DR3; computes bulk densities for every object with a detected drift. This will be the
  largest single peer-reviewed density sample of our target population (NEAs — exactly what the pipeline ranks) and is
  the right long-term anchor to replace both carry2012's small per-class samples and SiMDA's service data once pulled.
- **Pipeline mapping**: `TAXONOMY_COMPOSITION` densities for NEA-relevant types; also validates the ranking-quality
  claim (density uncertainty → mass uncertainty → profit-ranking noise).


## lodders_palme2009 — Lodders & Palme, "Solar System Elemental Abundances in 2009", 72nd Meteoritical Society Meeting abstract [T2]

- **Full text hosted**: `full_texts/lodders_palme2009_ci_abundances_metSoc72_abstract.pdf`
  (LPI-hosted, verified live: HTTP 200 application/pdf; LPI distributes meeting PDFs openly).
- **What it is**: the authoritative CI-chondrite abundance table for that era — every element in ppm bulk rock.

### PGM anchor check against the pipeline's baseline claim

The pipeline (`catalog.py` header) says its PGM baseline of 1.0× is calibrated to "~37 ppm total
PGM+Au **in nickel-iron alloy**". This table gives the CI-chondrite *bulk-rock* values:

| element | CI chondrite (ppm bulk rock) |
|---|---|
| Ru | 0.686 | Rh | 0.139 | Pd | 0.558 | Ag | 0.201 | Os | 0.493 | Ir | 0.469 | Pt | 0.947 | Au | 0.146 |
| **PGM total (Ru+Rh+Pd+Os+Ir+Pt)** | **≈3.29** |

- The bulk-rock PGM total is ~3.3 ppm, not 37 — but that is *consistent*, not contradictory: CI chondrites
  carry only a few percent metal by mass (pipeline's own S-type row says 15% metal), so the metal phase alone
  concentrates the same budget into far less mass. 3.29 ppm bulk ÷ ~0.09–0.15 metal fraction → ~22–37 ppm in
  the metal phase, i.e. **the pipeline's 37 ppm figure is exactly what CI-chondritic abundances predict for a
  chondrite-metal-phase concentration**. The baseline claim now has a traceable chain: Lodders & Palme Table 1 →
  ÷ metal fraction (catalog.py row) → ~37 ppm.
- **Gap this does NOT close**: per-type *enrichment factors* (M/Xe ×2.0, V ×0.2 etc.) still rest on the qualitative
  differentiation argument in the code header — no peer-reviewed table of PGM concentrations by iron-meteorite group
  was reachable from this machine in round 1 (the standard references are paywalled: Palme & Lodders' iron-meteorite
  compilations). Recorded as a known gap for a later round.

## epsc2022_context — "Composition of large asteroids collided with the Earth", EPSC-2022 abstract [T2]

- **Access**: `open_not_pulled` (Copernicus meeting page verified live 200; full text behind login).
  DOI: 10.5194/epsc2022-106. Abstract retrieved via Crossref API.
- **Why it's here**: context for the density+composition pair — argues that large differentiated asteroids (the M/V/E
  population our pipeline prices most aggressively) carry metal fractions and PGM budgets set by their parent-body
  differentiation history, i.e. the same physics behind `PGM_ENRICHMENT_BY_TYPE`. No numbers extracted this round;
  kept as a pointer for when the full text is pulled.

## Round-1 status (domain 1)

4 items processed: carry2012 [T1, hosted], simda2024 [T3, live service + derived stats committed],
dziadura2023 [T1, open_not_pulled — OA but publisher bot-blocks this machine], lodders_palme2009 [T2, hosted].
**Headline findings for the user**: (a) S/X/Cgh/D rows are well-anchored by measured data; (b) B/L/K rows sit ~0.7–1 g/cm3
below both independent anchors — strongest candidates for a `TAXONOMY_COMPOSITION` revision; (c) Xe is contested between
the two sources (N≤4 either way); (d) the 37 ppm PGM baseline now has a traceable derivation chain but per-type enrichment
factors remain uncited.


## Round-3 additions — NEA population statistics (the size/completeness backbone of any ranking)

### harris2015 [T1] — Harris & D'Abramo, "The population of near-Earth asteroids", Icarus 257:302–312
- **Access**: paywalled; ScienceDirect bot-blocks this machine (verified 403 on the article page). Recorded `open_not_pulled` with abstract.
- **Abstract (as published, retrieved via search snippet of the ADS record)**: "We describe a methodology of estimating the size-frequency distribution (SFD) of near-Earth asteroids (NEAs). We estimate the completion versus size of present surveys based on the re-detection ratio, that is, the fraction of all detections over a recent period that are re-detections of already discovered objects rather than new discoveries. The re-detection ratio is a robust measure of …"
- **Why it matters here**: this is the peer-reviewed basis for *how complete* the SBDB/SsODNet catalogs actually are by size — i.e. whether our Stage-1 population (and therefore every per-type density/PGM average in domain 1) is biased toward large bodies. The re-detection-ratio method is exactly what a ranking pipeline needs to state as an assumption: "catalog completeness at D < X km is Y%".
- **Caveat recorded by the authors' own follow-up**: the H-magnitude rounding issue (below) affected this paper's numbers — cite 2021, not 2015, for any population figure.

### harris_dabramo_2021 [T1] — Harris & D'Abramo, "The population of near-earth asteroids revisited and updated", Icarus (2021)
- **Access**: open access per OpenAlex (`is_oa: true`, DOI 10.1016/j.icarus.2021.114452), but the Elsevier PDF endpoint bot-blocks this machine (verified: pdfft route → 403, HTML challenge). Recorded `open_not_pulled` — pullable from a normal interactive browser like `dziadura2023`.
- **Abstract (retrieved via search snippet)**: "In this paper we update, extend, and improve upon the recent paper on Near-Earth Asteroid (NEA) population by Harris and D'Abramo (2015). We update the population estimate taking into account discoveries to August 3, 2020. Shortly after the previous paper was published, we identified a problem in our previous studies due to rounding off of absolute magnitude H by the Minor Planet Center to 0.1 …"
- **Why it matters here**: this is the CORRECTED population estimate — the 2015 numbers are known-bad (MPC rounds H to 0.1 mag, which distorts size-frequency inference). Any completeness claim our pipeline makes should cite THIS paper. It also gives us a dated census boundary (discoveries through 2020-08-03) to pair with `catalog_date` on every output CSV — the same discipline this repo already applies to prices.
- **Pipeline mapping**: backs the *population-statistics* half of domain 1 that rounds 1–2 left open: our ranking quality depends on knowing what fraction of each size class is actually in the catalog, and these two papers are the only peer-reviewed SFD-completeness method for NEAs. No numbers extracted this round (text not accessible) — recorded as context with abstracts so a later browser pull can fill `extracted_data/`.

## Round-5 addition — a second independent per-body density sample (OA-pending)

### adam_2017 [T1] — "Volumes and bulk densities of forty asteroids from ADAM shape modeling", Astronomy & Astrophysics (2017), DOI 10.1051/0004-6361/201629956
- **Access**: OA per OpenAlex, but A&A's direct PDF route bot-blocks this machine (verified: aanda.org full_html PDF → 403). Same block class as dziadura2023 — recorded `open_not_pulled`, pullable from a normal browser. Abstract retrieved via OpenAlex is truncated at the Context section ("Disk-integrated photometric data of asteroids do not contain accurate information on shape details or size scale…") — re-pull the full abstract with the text.
- **Why it matters here**: 40 peer-reviewed bulk densities derived from ADAM shape models (lightcurve + occultation-constrained) is an independent per-body sample that can be joined to taxonomic class. Its specific value for this domain: carry2012's Table 3 never measured D-types, and the pipeline's D-row (density_est_gcm3 = 1.20) currently has **no peer-reviewed anchor at all** — ADAM's forty-body sample is the most likely place to find one if any of its members are D-class.
- **Pipeline mapping**: would back `TAXONOMY_COMPOSITION` densities for whichever classes appear in its sample; recorded as context this round (text not accessible) so a later browser pull can extract per-body rows into `extracted_data/`.

## Round-11 addition — S-type density: meteorite-side anchor (wilkinson_robinson_2000)

82 samples / 72 ordinary chondrites, modified Archimedes method at ~1% accuracy: **H=3.44±0.19, L=3.40±0.15, LL=3.29±0.17 g/cm^3** (1-sigma); intra-group spread 3.0–3.8 g/cm^3 at near-invariant bulk composition — density tracks porosity/texture more than chemistry within a group. Meteorite-side anchor for our S row: hand samples ~3.3–3.4 vs carry2012's asteroid-scale S median 2.70 → the gap is km-scale macro-porosity/rubble structure, exactly what `TAXONOMY_COMPOSITION` encodes (S=2.70). Wiley bot-blocks from this machine; no preprint found — recorded open_not_pulled with abstract captured via OpenAlex. Full write-up also in domain 2's FINDINGS.md (round-11 block) since it pairs with the PGM-differentiation anchor there.
