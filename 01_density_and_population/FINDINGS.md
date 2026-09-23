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

## Round-12 addition — M-type density gets TWO independent peer-reviewed anchors (one hosted)

**siltala_granvik_2021 (T1, full text hosted)**: arXiv:2103.01707 preprint of the ApJL paper. Bulk density of 16 Psyche = **3.88±0.25 g/cm^3** — mass from their method validated against Dawn's Ceres/Vesta masses, volume from latest shape estimates. Explicitly RULES OUT an exposed solid iron core; consistent with ferrovolcanism / metal-silicate mix. This is the measurement our `TAXONOMY_COMPOSITION["M"]` already cites (v1.0.8 revision: density 3.90, metal_fraction 0.50) — now hosted and verifiable in-repo.

**farnocchia_2024 (T1, open_not_pulled)**: JPL team (Farnocchia et al., Astron J, CC-BY but IOP bot-blocks + no other PDF route found). Independent method: GM = 1.601±0.017 km^3/s^2 from least-squares astrometry on asteroids passing within 0.05 au (incl. Gaia FPR); occultation/radar volume => **4.17±0.15 g/cm^3**. Our M-row value of 3.90 sits at the LOW end of this independent pair — defensible, but flagged for re-check if Psyche mission data revises either estimate.

## Round-38 addition — P-type density: first direct measurement (kretlow_2022_rosa_mass_density)

**T1, full text hosted** (arXiv:2210.03993v1; A&A 668:A141, CC-BY). First direct bulk-density determination of a confirmed Tholen P-type asteroid — (223) Rosa, outer main belt, D = 83±8 km, pV < 0.05: mass from gravitational deflection of test asteroids in three close encounters (two independent estimates, weighted mean M = (3.62±1.25)×10^17 kg) gives **rho = 1.2 ± 0.5 g/cm^3**, which the paper states is "consistent with typical densities for Tholen taxonomy P-type asteroids" (their reference line: ~1.3).

**Why it matters here**: simda2024's per-class table has **zero measured bodies in class P** — this was a genuine hole in our density evidence base, and Rosa fills it as the first direct anchor for `TAXONOMY_COMPOSITION["P"]`. It also exposes an outdated value: our catalog.py P-row carries density_est_gcm3 = 1.80, which matches the pre-2022 literature estimate Kretlow explicitly says "did not match very well" with the P classification (p.1). **Revision candidate**: P-row → ~1.2 g/cm^3; NOT applied (target repo read-only), recorded in registry pipeline_mapping + `extracted_data/`.


## Round-40 addition — Bennu mass/density anchor: environments.csv's best-characterized body gets an independent peer-reviewed check (chesley_2014_bennu_orbit_bulk_density)

**T1, full text hosted** (arXiv:1402.5573v1; Icarus 235:5-22, DOI 10.1016/j.icarus.2014.02.020 — accepted by Icarus Feb 19 2014). Chesley, Farnocchia, Nolan et al., JPL/Arecibo: optical astrometry 1999-2013 + Arecibo radar delay (1999/2005/2011) constrains the Yarkovsky drift da/dt = (-19.0+/-0.1)e-4 au/Myr (= 284 +/- 1.5 m/yr); combined with thermal-force modeling of the known shape this yields **rho = 1260 +/- 70 kg/m^3**, M = (7.8+/-0.9)e10 kg, GM = 5.2+/-0.6 m^3/s^2 (Table 7, p.56).
**Why it matters here**: `environments.csv`'s Bennu row (mass 7.329e10 kg, mean radius 244.5 m) cites "Lauretta et al. 2019, Nature" in notes — a post-mission characterization whose paper was never registered and is not reachable from this machine. Chesley 2014 provides an **independent pre-OSIRIS-REx (2014) determination**: our mass sits at -0.8 sigma INSIDE the paper's error bars, and our implied bulk density (~1197 kg/m^3 for a sphere of r = 244.5 m) is ~6% below the central estimate but inside its +1-sigma band — agreement without any OSIRIS-REx data. No revision needed; recorded as verification evidence (→ `extracted_data/r40_bennu_mass_density_key_numbers.csv`, 7 rows).

**Remaining open items in this file**: Ryugu row still cites Watanabe et al. 2019 Science unregistered; Eros (Yeomans et al. 2000), Didymos (Daly et al. 2023) and Ceres (Russell et al. 2016) characterization papers likewise not yet pulled — all paywalled/bot-blocked from this machine as of R40, so they stay `open_not_pulled` candidates for a future round rather than being registered on title alone.

## Round-41 addition — Stage-1 data backbone registered: SsODNet/ssoBFT + NEOWISE V2.0 + JPL SBDB (the runtime sources behind economicspace's externalized AsteroidCatalog package)

**Context**: the 2026-09-22 refactor of `economicspace` moved Stage-1 catalog building into a new external package (`AsteroidCatalog`, pip-installed), whose CITATIONS.md marks two upstream sources **citation-required (🔔)** — SsODNet/ssoBFT and NEOWISE V2.0 — plus JPL SBDB as the orbital/physical backbone, with the Fowler & Chillemi 1992 diameter formula and Bus–DeMeo taxonomy as reference tables. None of these was registered in General_Research before this round; all five are now anchored below (5 new registry rows → sources.csv 94→99).

**berthier_2023_ssodnet [T1]** (A&A 671:A151; arXiv v4 preprint hosted, hash-matched): the bulk ssoBFT parquet was **parsed live this round — 1,563,708 rows × 266 columns** (sha256=6e2d73d2…b202; 855.8 MB exceeds the repo's ~36MB max committed file so it is hash-recorded + URL'd rather than git-committed). Cross-check of all five `environments.csv` bodies: **Eros mass EXACT** (both 6.687e15 kg); Ryugu +0.44σ, Didymos −0.12σ, Ceres D=939.4 km → our radius agrees to +0.01%; Bennu absolute diff only 0.02% (the −2.65σ flag is an artifact of ssoBFT's over-tight post-mission error bar — recorded as agreement). The Eros density "gap" (+14%) resolved as a radius-convention difference: our r=8420 m vs ssoBFT equivalent-sphere D_mean=17.6 km for an elongated (a/b~3) body at identical mass — not a data conflict.

**mainzer_2019_neowise_v2 [T3]** (PDS SBN release urn:nasa:pds:neowise_diameters_albedos::2.0, DOI 10.26033/18S3-2Z54; entire bundle zip committed hash-matched): TAP table `neowisesbpropv2` verified live from this machine (count=183,412 vs the committed PDS release's 183,419 rows — version drift). **Key finding**: all five headline bodies (Bennu/Ryugu/Eros/Didymos/Ceres) are ABSENT from every one of the bundle's seven data tables — verified by zero-padded MPC designation across each table. This is consistent with NEOWISE V2.0 excluding objects that have better radar/spacecraft/lightcurve diameter determinations, so our target rows source their diameters/albedos from ssoBFT + SBDB instead; the dataset still anchors the bulk of the catalog (183k bodies).

**jpl_sbdb_small_body_database [T3]** (JPL Solar System Dynamics, live service): full-table scan + field-discovery endpoint verified from this machine — count=1,566,680 asteroids; Ceres D=939.4 km / pV=0.090 / H=3.34 → implied radius 469700 m vs our environments.csv 469730 m (+0.01%). Per-object queries intermittently return HTTP 400 from this machine — recorded in the registry access_status rather than papered over (the full-table path, which is what a bulk pipeline would use, works).

**fowler_chillemi_1992_iras_mps_diameter_formula [T2]** (NASA PL-TR-92-2049 "The IRAS Minor Planet Survey", NTRS public-domain scan; ch.4 "IRAS Asteroid Data Processing" extracted as a 28-page PDF, hash-matched against the full report's p36–p63 window): anchors the diameter-from-H formula `D_km = 1329/sqrt(pV)*10^(-H/5)` used by AsteroidCatalog. The NTRS scan's OCR layer garbles equation glyphs (exponent digits render as stray marks), so text-layer verification of C=1329 was impossible — instead the constant was **verified numerically**: fitting C = D·sqrt(pV)·10^(H/5) over n=149,277 (H / pV / D) triples from ssoBFT gives implied-C p05/p50/p95 = 1328.4 / **exactly 1329.0** / 1329.6 — airtight against ~149k real bodies.

**demeo_2009_bus_taxonomy_near_ir [T1]** (Icarus 202(1):160–180; DOI + bibliographic record verified via Crossref this round) — open_not_pulled: Elsevier bot-blocks this machine and no arXiv preprint exists. This is the class system keying BOTH anchors already in this domain (carry2012's per-class density Table 3 and economicspace's TAXONOMY_COMPOSITION are indexed by Bus–DeMeo types S/Cgh/B/V/A/M/Xc/Cb/D/T/P…); registering it closes the "what do these letters mean" gap for every class row. PDS bundle urn:nasa:pds:ast.bus-demeo.taxonomy is the machine-readable companion (not yet pulled — open item).

**Open items carried forward**: ssoBFT's per-body `delta_v` column ("best total Δv to rendezvous", e.g. Bennu 7.368 / Ryugu 6.985 km/s) = future anchor candidate for spacecost approach/transfer rows — not yet anchored into domain 3; Bus–DeMeo PDS bundle pull; SBDB per-object query reliability from this machine.