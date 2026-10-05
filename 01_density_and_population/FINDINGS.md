# Domain 1 Findings — density by spectral type, PGM factors, population statistics

## carry2012 — Carry (2012), "Density of asteroids", Planetary and Space Science 73:98-118 [T1]

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

### harris_dabramo_2021 [T1] — Harris & D'Abramo, "The population of near-earth asteroids revisited and updated", Icarus (2021)
- **Access**: open access per OpenAlex (`is_oa: true`, DOI 10.1016/j.icarus.2021.114452), but the Elsevier PDF endpoint bot-blocks this machine (verified: pdfft route → 403, HTML challenge). Recorded `open_not_pulled` — pullable from a normal interactive browser like `dziadura2023`.
- **Abstract (retrieved via search snippet)**: "In this paper we update, extend, and improve upon the recent paper on Near-Earth Asteroid (NEA) population by Harris and D'Abramo (2015). We update the population estimate taking into account discoveries to August 3, 2020. Shortly after the previous paper was published, we identified a problem in our previous studies due to rounding off of absolute magnitude H by the Minor Planet Center to 0.1 …"
- **Why it matters here**: this is the CORRECTED population estimate — the 2015 numbers are known-bad (MPC rounds H to 0.1 mag, which distorts size-frequency inference). Any completeness claim our pipeline makes should cite THIS paper. It also gives us a dated census boundary (discoveries through 2020-08-03) to pair with `catalog_date` on every output CSV — the same discipline this repo already applies to prices.
- **Pipeline mapping**: backs the *population-statistics* half of domain 1 that rounds 1–2 left open: our ranking quality depends on knowing what fraction of each size class is actually in the catalog, and this paper is the peer-reviewed SFD-completeness method for NEAs. No numbers extracted this round (text not accessible) — recorded as context with abstracts so a later browser pull can fill `extracted_data/`.

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

**Open items carried forward**: (all three R41 items CLOSED by Round 42 — see below)

## Round-42 addition — MP3C + MPC designation links registered; Bus–DeMeo PDS bundle pulled and parsed (R41 open item closed)

**mp3c_minor_planet_physical_properties_catalogue [T3]**: the runtime source behind AsteroidCatalog `fetch_mp3c`. Verified live this round via the package's exact POST route (`dachs.oca.eu/tap/sync` with REQUEST=doQuery&LANG=ADQL — note my first GET probe hit a different endpoint and returned the TAP info page; recorded). Per the service's own request, database version is recorded: **v3.2.0-beta.1, date_created 2024-02-13** (mp3c_gen_db_revision `2acaa66e…`). Counts: mp3c_main.best = **1,335,502 bodies**, name aliases = 6,086,962. Sample rows pulled for headline bodies via the package's join pattern (`best JOIN body USING(bid)`): Eros D=15.77 km / pV=0.385 / **M=6.69e15 kg** vs our environments.csv 6.687e15 → **+0.04%, near-exact**; Bennu D=0.492 km (consistent with r=244.5 m). Schema note for future joins: numbered bodies key through packed MPC aliases in `mp3c_main.name(priority=3)`, not a plain number column — my first sample query failed on exactly this and was corrected against the package's own ADQL.

**mpc_mpcorb_extended_designation_links [T3]**: IAU Minor Planet Center extended orbital file — source of Number/Name/Principal_desig/Other_desigs that `identity.py` uses to resolve designations JPL's own columns cannot place. Verified live this round from this machine: HEAD 200, **182 MB gzip** (Last-Modified Wed 23 Sep 2026 — file of record updated continuously), streamed and first records parsed (Ceres: Principal_desig A801 AA + Other_desigs [A899 OF, 1943 XB]; Pallas likewise) — structure matches what the package expects.

**bus_demeo_2020_pds_taxonomy_bundle [T3; full text hosted]**: **closes R41's carried open item "Bus–DeMeo PDS bundle pull."** All six files of the PDS SBN release (urn:nasa:pds:ast.bus-demeo.taxonomy::1.0, DOI 10.26033/089p-c283; public-domain NASA data) pulled live from sbnarchive.psi.edu this round — demeotax.tab / meanspectra.tab / demeorefs.tab / pcscores.tab / classdesc.asc / taxocard.pdf (per-file sha256(16) in the extracted CSV), committed as `full_texts/bus_demeo_2020_pds_bundle.zip`. **demeotax.tab parsed: 371 classified bodies, base-class distribution exact-summed** → `extracted_data/r42_bus_demeo_class_distribution.csv` (S=144 dominates; L=22, Xk=18, V=17, Ch/D/K/Cgh ~10–16 each … T=4). Coverage against our TAXONOMY_COMPOSITION: **24 of 31 named types have ground-truth members**; Sk and Sl (S/K, S/L transitionals) have none in the reference set, as do Tholen-only rows M/E/P/F/G by construction. classdesc.asc = per-class spectral description + member count from Table 5 of DeMeo et al. 2009 — the "what these letters mean" companion to `demeo_2009_bus_taxonomy_near_ir` (which remains open_not_pulled for the paper text itself).

**R41's three carried items, disposition**: ssoBFT delta_v → anchored in domain 3 this round; Bus–DeMeo PDS bundle pull → closed above; SBDB per-object query reliability → RESOLVED: the working endpoint is `ssd-api.jpl.nasa.gov/sbdb.api?sstr=<name>` (verified live, used to resolve the Bennu/Hermes identity anomaly in domain 3's mining); R41's "per-object 400s" were a wrong parameter on the bulk-only `sbdb_query.api`. The jpl_sbdb registry row was updated accordingly.

## Maintenance (2026-09-26) — carry2012 Table 3 re-read; three files un-hosted; citation fixes

- **Un-hosted**: carry2012 and chesley_2014_bennu_orbit_bulk_density (arXiv default licence), lodders_palme2009 (LPI abstract, no licence). Un-hosted on 2026-09-26 because the licence does not permit redistribution (details in each registry row); every number this file quotes from them was checked against the PDF first and is in `extracted_data/`.
- **carry2012 Table 3, re-read by word coordinates** (`extracted_data/carry2012_density_by_type.csv`, rewritten with the N of every tier). Round 1's extraction mixed values between wrapped rows: C's 20% tier is 1.33 ± 0.58 (not 1.25), Cb's is 1.25 ± 0.21, Ch's is 1.41 ± 0.29; Q has no density estimate at any tier (the "2.23 / 1.93" were the R and V rows); R = 2.23 ± 1.02 (N=1); V = 1.93 ± 1.07 (3 V-type bodies, not Vesta). The K value 3.54 ± 0.21 in both precision tiers is one body.
- **Effect on the comparison table above**: the B-row "stray 1.33" ambiguity resolves to C; the Q "possible discrepancy" has no basis, so rc-006 is withdrawn; the K discrepancy rests on a single body (rc-001 evidence corrected). C (1.33-1.57 vs ours 1.50) still agrees.
- **Citation**: Carry (2012) is Planetary and Space Science 73:98-118, DOI 10.1016/j.pss.2012.03.009. The registry DOI pointed at an unrelated A&A paper and the heading said 60(7):537-552; both corrected.
- simda2024 re-classed `open_service` (the live SiMDA export is what was used; derived statistics are committed).
- New rows in `extracted_data/backfill_2026-09-26_key_numbers.csv`: siltala_granvik_2021 and kretlow_2022 (page-located in the hosted PDFs); dziadura2023, harris_dabramo_2021, wilkinson_robinson_2000 (abstract-level, not re-checkable here); mp3c (live-service values). epsc2022_context, adam_2017, demeo_2009_bus_taxonomy_near_ir and mpc_mpcorb are marked context-only in the registry, with reasons.

## R70 - Full-extraction pass of the hosted sources (2026-09-27; registry unchanged)

Every hosted full text in this domain was re-read end to end for pipeline-useful numbers; tables were read by word coordinates (or from rendered page images where the text layer fails) and checked against their printed totals. New files (all in `extracted_data/`, every row carries `source_id` and a page location): `r70_berthier_2023_ssodnet.csv` (16); `r70_berthier_2023_ssodnet_table_c8_class_complex.csv` (19); `r70_bus_demeo_2020_pds_taxonomy_bundle_per_body_classes.csv` (371); `r70_fowler_chillemi_1992_iras_mps_diameter_formula.csv` (13); `r70_kretlow_2022_rosa_mass_density.csv` (10); `r70_mainzer_2019_neowise_v2.csv` (14); `r70_siltala_granvik_2021.csv` (13).

- **Fowler & Chillemi C = 1329 km now read directly.** The p27 page image prints Eq.(31) as D = 10^(3.1236 - 0.2H - 0.5 log10 <pH>); 10^3.1236 = 1329.2. R41 recorded the constant as confirmed only by fitting because the text layer garbles the equation; the r41 row is right and needs no edit.
- **NEOWISE v2 statistics computed from the hosted bundle**: NEO fitted pV median 0.135 (p25-p75 0.046-0.252; n = 1,509); 41.7% of NEOs have pV < 0.1 and 18.4% pV > 0.3; median NEATM beaming 1.40.
- **Bus-DeMeo classes for 371 bodies** parsed from the hosted PDS bundle (demeotax.tab), so a per-body class lookup no longer needs the live service.

## R71 - Side-deepening extraction round (2026-09-27; logged in R72; registry unchanged)

Branch `side-deepening`, commit 0729c2d, merged into this branch in R72. It gave the 20 PDFs un-hosted on 2026-09-26 (restored byte for byte from git `5dd58d5`, sha256 matched against `DOWNLOADS.md`) their first full pass, and read seven non-hosted sources from copies the owner downloaded (DOWNLOADS.md section B). The commit wrote no FINDINGS block or log entry; this block and the R71 log entry were written in R72 from the commit and the files themselves. R72 then re-checked every R71 file whose PDF is restorable: every numeric cell was searched for in the PDF text (0 values missing outside cells the R71 notes say were read from page images), the image-read cells were compared against rendered pages, and large tables were checked row by row. New files: `r71_adam_2017_key_numbers.csv` (20); `r71_adam_2017_table2_spin_states.csv` (50); `r71_adam_2017_table4_adam_volume_density.csv` (50); `r71_adam_2017_table6_literature_densities.csv` (11); `r71_carry2012_key_numbers.csv` (40); `r71_carry2012_table1_per_body_mass_diameter_density.csv` (287); `r71_carry2012_table2_meteorite_bulk_density.csv` (19); `r71_carry2012_tableA1_mass_estimates.csv` (981); `r71_carry2012_tableB1_diameter_estimates.csv` (1454); `r71_carry2012_tableC1_indirect_density_estimates.csv` (33); `r71_chesley_2014_bennu_orbit_physical_key_numbers.csv` (30); `r71_chesley_2014_table6_asteroid_perturber_gm.csv` (25); `r71_chesley_2014_table8_earth_close_approaches.csv` (11); `r71_lodders_palme2009_table1_ci_and_solar_system_abundances.csv` (83).

- **carry2012 per-body tables** (Table 1, 287 bodies; Appendix A.1 981 mass estimates; B.1 1,454 diameter estimates; C.1 33 indirect densities; Table 2 meteorite densities). R72 checked Table 1 row by row: all 287 rows match the page with the name adjacent to its mass; seven rows print the mass at the error term's exponent (e.g. 0.47 +/- 5.79 x 10^18 = 4.7e17) and 22P/Kopff's name carries an 'ff' ligature, both correct as recorded.
- **adam_2017** (Tables 2, 4, 6): ADAM volumes and densities for 40 bodies. R72 recomputed density from the printed mass and volume-equivalent diameter for all 41 rows that carry both: every one agrees with the printed density.
- **chesley_2014** Tables 3, 4, 6, 8 and the text; **lodders_palme2009** Table 1 (83 elements, CI ppm and solar-system atoms per 10^6 Si).

## R72 - Tables R70/R71 skipped, verification of R71, upstream re-check (2026-09-27; registry unchanged)

This round's container reached only package registries (arXiv, NTRS, JPL, Google Docs and every publisher returned 403), so nothing new could be fetched; the work used the hosted PDFs and the 20 restored from git `5dd58d5`. Each hosted and restored PDF's table captions were listed and matched against the extracted CSVs; tables no CSV cited were read by word coordinates (columns assigned from header or fully populated rows, so blank cells stay blank) or from rendered page images, and checked against printed totals. Upstream heads re-read: spacecost@e831245, AsteroidCatalog@852bf69, economicspace@1f470d4 (unchanged since 2026-09-26). New files: `r72_chesley_2014_table10_impact_resonances.csv` (8); `r72_chesley_2014_table11_formal_uncertainties.csv` (8); `r72_chesley_2014_table5_model_variations.csv` (35); `r72_chesley_2014_table9_keyholes_2135.csv` (78); `r72_chesley_2014_tables1_2_radar_astrometry.csv` (32).

- **chesley_2014 Tables 9-10 (keyholes and resonances)**, which R71 left out as impact-hazard only: 78 keyholes parsed from the two side-by-side halves of p58 by word coordinates (zeta increases monotonically down each half). Their impact probabilities sum to **3.68 x 10^-4**, the paper's cumulative 3.7 x 10^-4, and exactly 8 exceed 10^-5, the eight impacts Table 10 lists. Also Tables 1-2 (22 delay and 7 Doppler radar measurements, 2011 runs), 5 (35 orbit-model variations, columns taken from the header positions after a first parse mixed labels into the number columns) and 11. The R71 key-numbers note now points to these files.
- **adam_2017 vs AsteroidCatalog densities** (SMASS classes; small N, large errors): C median 1.60 (upstream 1.5), S 2.70 (2.7), M-like X bodies Psyche and Kalliope 3.7 (3.9) agree. **P: (87) Sylvia, Tholen P, 1.39 +/- 0.08** is a far tighter P-type value than Rosa's 1.2 +/- 0.5, so it is appended to rc-007's evidence (upstream P 1.8, still unchanged). K: (89) Julia 4.5 +/- 1.3 points the same way as rc-001 but adds one noisy body; rc-001 unchanged. B: Pallas 2.72 +/- 0.17 is the large-B case rc-003 was declined over; unchanged. Ch: adam ~1.9 (five bodies) and simda2024 1.98 against carry2012's best-precision tier 1.41 +/- 0.29 (N = 9): upstream 1.5 sits inside that spread, no candidate.

## R73 - Blocked downloads fetched and extracted (2026-09-27; registry unchanged)

This container's network was widened, so the DOWNLOADS.md sections B-D were retried. Publisher sites (aanda.org, ScienceDirect, Wiley, IOP, HAL) still answer with bot challenges (DataDome, Cloudflare, Radware, Anubis), so open repository copies were used where they exist. New files: `r73_dziadura2023_key_numbers.csv` (33); `r73_dziadura2023_table2_observation_data.csv` (57); `r73_dziadura2023_tableA1_reference_key.csv` (57); `r73_dziadura2023_tableA1_yarkovsky_densities.csv` (57); `r73_epsc2022_context_key_numbers.csv` (10); `r73_wilkinson_robinson_2000_appendix1_bulk_geochemistry.csv` (44); `r73_wilkinson_robinson_2000_key_numbers.csv` (23); `r73_wilkinson_robinson_2000_table1_standards.csv` (9); `r73_wilkinson_robinson_2000_table4_group_comparison.csv` (18); `r73_wilkinson_robinson_2000_table5_shock_stages.csv` (16); `r73_wilkinson_robinson_2000_table6_asteroid_densities.csv` (8); `r73_wilkinson_robinson_2000_tables2_3_sample_bulk_densities.csv` (82).

- **dziadura2023** (publisher PDF from the Universidad de Alicante repository; CC BY 4.0 on its p1). Table A.1 is printed rotated; it was read by word coordinates with column bands set per page and checked cell by cell against rendered pages (57 rows = the 49 accepted + 8 marginal NEAs the text reports). Table 2 checks exactly: N_total = N_MPC + N_radar + N_Gaia in all 57 rows, and it flags 20 PHAs and 3 binaries, as the text says. **Source inconsistencies, kept as printed**: Table 1 gives 154 094 inner-main-belt and Mars-crossing asteroids where the abstract and Sec 5 say 54 094; four rows (1998 KK17, 2000 NL10, Ryugu, 2002 FB3) print a da/dt equal to their diameter and error, and five rows print no density; (4769) Castalia prints a negative density; the text gives (88710) 2001 SL9 as 2249.96 kg/m3 where Table A.1 prints 2032.
- **Yarkovsky densities vs AsteroidCatalog**: S-type NEAs median 1.37 g/cm3 (N = 23, range 0.73-3.70) against upstream S 2.7; Q-type median 1.47 (N = 9) against Q 3.0. Per-body errors are 30-60% and the method returns non-physical values for some bodies, so no value change is proposed; **rc-045 and rc-046** ask for a small-NEA caveat in the S and Q notes, as the Sq and B rows already carry (Itokawa 1.9, Bennu 1.19). Upstream read at AsteroidCatalog@852bf69, unchanged.
- **Correction**: the domain-1 backfill row recorded 446 / 93 / 54,094 as 'bodies with detected Yarkovsky drift'. Those are the bodies whose orbits were fitted; detections are 49 NEAs. The row and the registry author list (K. Dziadura, D. Oszkiewicz, F. Spoto, B. Carry, P. Tanga, P. Bartczak) are corrected.
- **wilkinson_robinson_2000** (NASA ADS scan, read from page images). All 82 samples of Tables 2-3 pass two checks: % error = SD / mean within rounding, and low <= median, mean <= high. The group means recompute from the samples to the printed Table 4 values (H 3.44 +/- 0.19, n = 42; L 3.40 +/- 0.15, n = 30; LL 3.29 +/- 0.17, n = 9; H4 counts Dhajala H3-4). In Appendix 1, 40 of 42 rows satisfy Fe(T) = Fe(M) + 0.7773 FeO + 0.6353 FeS within 0.3 wt%; Conquista and Macau differ by about 4.2 wt% as printed. The appendix lists 39 of this study's meteorites where the text says 40. The registry citation 35(6):1479-1488 was wrong; the paper is M&PS 35:1203-1213.
- **Meteorite vs asteroid density**: the paper's own bound puts 433 Eros at 21-33% bulk porosity (average OC 3.40 against Eros 2.67 +/- 0.03). Upstream S 2.7 against LL/L meteorites at 3.29/3.40 implies ~20% macroporosity, consistent with that bound.
- **epsc2022_context**: the Copernicus page now shows the full abstract without login (CC BY 4.0). It gives the chondritic Ru/Ir ratio 1.51 +/- 0.05 and projectile fractions in large-crater melts, but no absolute PGE concentrations, so the iron-meteorite PGE gap noted in R72 stays open. The 'Context-only' note in its registry row is replaced.
- **Still blocked**: harris_dabramo_2021 (ScienceDirect Cloudflare), demeo_2009_bus_taxonomy_near_ir (HAL Anubis; TCD 403). Their registry rows record what was tried.

## R74 - Upstream citations registered (2026-09-27; +22 sources, T1x20, T3x1, T4x1; nothing extracted)

Sources the upstream repos cite that this registry did not have, found by reading every per-row `notes` field, code comment and CITATIONS.md in AsteroidCatalog@852bf69, spacecost@e831245 and economicspace@1f470d4. Each is `registered_not_pulled`: its DOI was checked against Crossref, or its landing page against a live request from this machine, and the result is recorded in the row. No full text was sought and no number was extracted; the rows are the queue for a later extraction round.

- `pravec_harris_2007_binary_angular_momentum` (T1): AsteroidCatalog D-from-H formula: Appendix A derives the 1329 km constant from V_sun; backs every H-derived diameter (derived_diameter_is_estimate rows).
- `campins_1985_absolute_calibration_1_5um` (T1): AsteroidCatalog D-from-H formula: the solar V magnitude (-26.762) behind the 1329 km constant; the ~1% diameter systematic.
- `mainzer_2011_neowise_thermal_model_calibration` (T1): AsteroidCatalog merge.py cross-source agreement tolerances for diameter and albedo (radar/spacecraft calibration of NEOWISE).
- `pravec_2012_absolute_magnitudes_wise_albedos` (T1): AsteroidCatalog H-magnitude tolerance in merge.py and the catalog-H offset near H~14 (README section 4 albedo offset).
- `buratti_2004_ds1_borrelly_photometry` (T1): AsteroidCatalog physics.py ALBEDO_FLOOR: darkest measured whole-body geometric albedo.
- `ferrais_2022_kalliope_tiny_mercury` (T1): AsteroidCatalog density ceiling (5.0 g/cm3) and the M/Xk DENSITY_EVIDENCE entry for 22 Kalliope.
- `consolmagno_2008_meteorite_density_porosity` (T1): AsteroidCatalog physics.py carbonaceous-class density ceiling (3.6 g/cm3) from meteorite grain densities.
- `macke_2011_carbonaceous_chondrite_density_porosity` (T1): AsteroidCatalog physics.py carbonaceous-class density ceiling (CI to CB grain densities).
- `macke_2010_enstatite_chondrite_density_porosity` (T1): taxonomy_composition.csv Xe row density_est_gcm3 (enstatite-chondrite bulk density less macroporosity).
- `patzold_2016_67p_homogeneous_nucleus_gravity` (T1): AsteroidCatalog physics.py density floor (comet-nucleus density).
- `thomas_2013_tempel1_nucleus_two_flybys` (T1): AsteroidCatalog physics.py density floor (second comet-nucleus density).
- `lauretta_2019_bennu_unexpected_surface` (T1): taxonomy_composition.csv B-row density (Bennu) and spacecost environments.csv 101955 Bennu mass and mean radius.
- `fujiwara_2006_itokawa_rubble_pile` (T1): taxonomy_composition.csv Sq-row density note (small S-types are rubble piles).
- `pravec_harris_2000_fast_slow_rotation` (T1): AsteroidCatalog physics.py breakup (spin-barrier) rotation period as a function of density.
- `holsapple_2007_spin_limits` (T1): AsteroidCatalog physics.py: size above which gravity rather than strength sets the spin limit.
- `emery_2011_trojan_nir_two_groups` (T1): AsteroidCatalog default taxonomy for unclassified Jupiter Trojans (D-type majority).
- `gil_hutton_brunini_2008_hilda_sdss_colors` (T1): AsteroidCatalog default taxonomy for unclassified Hildas (P/D bimodality).
- `mahlke_2022_asteroid_taxonomy_spectra_albedo` (T1): taxonomy_composition.csv Z row (Mahlke Z class mapped to D composition).
- `tholen_1984_asteroid_taxonomy_dissertation` (T4): taxonomy_composition.csv Tholen rows (M, E, P, F, G) mapped onto Bus-DeMeo classes.
- `hasselmann_2012_sdss_taxonomy_v1_1_pds` (T3): economicspace second-pass taxonomy check: independent SDSS class per numbered asteroid (research probe, not a stage input).
- `carvano_2010_sdss_taxonomy_main_belt` (T1): method paper for the SDSS taxonomy table economicspace commits (hasselmann_2012_sdss_taxonomy_v1_1_pds).
- `ivezic_2001_sdss_solar_system_objects` (T1): underlying survey of the SDSS taxonomy table economicspace commits.

## R113 - Taxonomy and albedo lineage: nine sources from the owner's link list (2026-10-04; +9 sources, T1x9)

The owner supplied a list of candidate sources for domain 1. Each was checked against the registry, its DOI resolved on Crossref and its text read where this machine could reach it. Three entries in the list carried wrong metadata: the A&A 665:A26 taxonomy paper is Mahlke, Carry & Mattei (already registered as `mahlke_2022_asteroid_taxonomy_spectra_albedo`, which backs the `Z` row), A&A 580:A98 is Carvano & Davalos, and the Icarus PII listed as an LSST/NEOSM phase-curve paper is Mahlke, Carry & Denneau (2021), Icarus 354:114094. Items that back no cell were rejected; they are listed in INDEX.md "Rejected sources" and the Round 113 log entry.

Upstream read at AsteroidCatalog@6a2cfbc. The catalog takes its class from JPL `spec_B` (Bus/SMASSII letters), then `spec_T` (Tholen), and from SsODNet `taxonomy.class`; it derives diameter from H and the geometric albedo, using a measured albedo where one exists and otherwise `ALBEDO_BY_SPECTRAL_TYPE`, then `ALBEDO_BY_SEMI_MAJOR_AXIS_AU` (`_NEO` for near-Earth objects), then a fallback.

| id | access | what it supplies |
|---|---|---|
| `bus_binzel_2002_smass2_feature_based_taxonomy` | registered, not pulled | The Bus (SMASSII) classes that JPL serves as `spec_B`, the catalog's primary class. Not read: Elsevier paywall and a ScienceDirect CAPTCHA. |
| `popescu_2018_movis_nir_taxonomy` | read live (arXiv) | Classes for 18,265 MOVIS asteroids (6,496 final). Its NIR notation is where the catalog's `Ad`, `Bk`, `Cgx`, `Ds`, `Kl` and `Xt` keys come from. WISE-albedo peaks per class: S 0.26 +/- 0.10, V 0.352 +/- 0.121, low-albedo D 0.08 +/- 0.03. |
| `tinaut_ruano_2026_gaia_dr3_taxonomy` | hosted (CC BY 4.0) | 14,042 asteroids in 13 classes from Gaia DR3 spectra (of 60,518 with spectra); near-UV separates B and F within the C-complex. A newer homogeneous class source than the catalog's inputs carry. |
| `masiero_2021_albedo_uncertainties_thermal_modeling` | read live (arXiv) | Albedo error is dominated by H: 0.3 mag in H with a 10% infrared diameter gives 32-36% in albedo; ~1 mag on Earth-like orbits gives ~70% in albedo and ~42% in a diameter computed from H and an assumed albedo (p5). |
| `myhrvold_2022_four_band_wise_asteroids` | read live (arXiv) | Re-fit of 4,420 asteroids from 82,548 WISE observations: median diameter error 9.3% (max 37.7%) against 24 occultations, about twice as close as NEOWISE, and a size-dependent NEOWISE diameter bias. |
| `masiero_2021_neowise_reactivation_years_6_7` | read live (arXiv) | Thermal fits for 199 NEOs + 5,851 MBAs (year 6) and 175 NEOs + 5,861 MBAs (year 7), newer than NEOWISE V2.0; Reactivation NEO diameters carry ~30% relative uncertainty. |
| `murray_2023_neural_network_main_belt_albedos` | read live (arXiv) | Neural-network albedos from proper elements, ~37% lower average error than a mean albedo; predictions for 585,174 main-belt asteroids. Could replace the semi-major-axis bins for main-belt bodies. |
| `wang_2026_nea_albedo_from_orbital_elements` | registered, abstract read | NEA albedo distributions from main-belt source regions; could replace `ALBEDO_BY_SEMI_MAJOR_AXIS_AU_NEO`. |
| `mahlke_carry_denneau_2021_atlas_phase_curves` | registered, abstract read | H, G1, G2 for 94,777 asteroids from ATLAS; could replace the H that Masiero shows dominates the albedo error. |

**Checks against upstream.** The catalog's derived medians agree with Popescu's independent WISE-albedo peaks within the stated spreads: S 0.2340 against 0.26 +/- 0.10, V 0.3355 against 0.352 +/- 0.121, D 0.0820 against 0.08 +/- 0.03. Masiero's figures put a number on derive.py's warning that a 2x albedo error is a 2.8x mass error: for a typical NEA with a ~1 mag H error the albedo alone is uncertain by ~70%. No revision candidate: nothing contradicts a cell.

Extracted data: `extracted_data/r113_taxonomy_albedo_key_numbers.csv` (20 rows, PDF pages of the arXiv versions).

## R114 - PDS density and taxonomy tables, and a second Gaia DR3 class source (2026-10-04; +3 sources, T1x1, T3x2)

The owner's rewritten link list (GR_links.txt, 197 URLs across most domains) opened with a domain 1 block of 16 URLs. Registered: `britt_2002_pds_asteroid_densities` (the PDS table behind Britt's Asteroids III chapter: 23 bodies with a best bulk density and class; the two M-types are Psyche 2.00 +/- 0.60 and Kalliope 2.50 +/- 0.30 g/cm3), `neese_2010_pds_asteroid_taxonomy_v3_0` (1,198 bodies with Tholen, Barucci, Tedesco, Howell and Xu classes; 985 carry a Tholen class, most commonly S 338; C 139; X 52; M 38; D 35; P 33; F 28; XC 23) and `pentikainen_2026_gaia_dr3_asteroid_characterization` (abstract only: a second Gaia DR3 class source with a Ch-class focus, beside `tinaut_ruano_2026_gaia_dr3_taxonomy`).

The NASA Open Data records on the list for the first two say 'This dataset has no data'; the data are in the PDS archive at sbnarchive.psi.edu and were read there. LCDB V3.0 on the list is the PDS release of the lightcurve database registered as `warner_harris_pravec_2009_asteroid_lightcurve_database` (domain 12), so it was not registered a second time. The two 2001 Kaasalainen lightcurve-inversion papers have no abstract in Crossref, OpenAlex or Semantic Scholar and ScienceDirect blocks this machine; a retry found their abstracts through ADS and Semantic Scholar summaries, and both were rejected as spin and shape methods (Round 114 log entry). The remaining entries were rejected (Round 114 log entry). No revision candidate.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.

## R115 - One note figure in the Xe row against Carry's Table 2 (2026-10-04; registry unchanged)

The Xe row's note says enstatite chondrites average 3.55 g/cm3 in bulk (Macke et al. 2010). Carry (2012) Table 2, which cites Macke 2010 for both groups, has EH 3.47 +/- 0.21 and EL 3.46 +/- 0.32, mean 3.465. rc-077 records the 2.4% difference as a wording candidate; the Xe density cell (2.90) does not move on it. Macke's own paper is not in the registry.

Extracted data: `extracted_data/r115_xe_enstatite_bulk_density_check.csv` (3 rows).
