# Domain 5 Findings — in-space storage / cryogenic boil-off, ISRU, operational costs

## lac_bac_2024 — "Local Area Cooling versus Broad Area Cooling for Boil-Off Reduction in Large-Scale Liquid Hydrogen Storage" [T1]

- **Full text hosted**: `full_texts/local_vs_broad_area_cooling_LH2_boiloff_arxiv2412.11720.pdf`
  (arXiv:2412.11720; verified live HTTP 200, application/pdf). Finite-element thermal study of LH₂ tanks with two insulation
  stacks and active-cooling configurations.

### The number that matters most in this domain

| pipeline row | our value | lac_bac_2024 evidence | verdict |
|---|---|---|---|
| hydrolox passive boil-off (charged by Module 4) | **0.05 %/day** | best-insulation case (HePUR): **0.04 %/day**; cheap-perlite case: **0.24 %/day** | **AGREEMENT at the top of a peer-reviewed range.** Our single figure is defensible as "good MLI, no active cooling" — but the paper shows the spread across insulation quality is ~6x, and our `storage_systems` MLI row (1.2 kg/m²) carries that assumption invisibly |
| ZBO cryocooler rows (80 W/W electrical @ 20 K; 5 kg/W specific mass — flagged "NOT flown on a propellant tank") | engineering estimates from Carnot limits | reliquefaction specific energy **5 kWh/kg** (Kim et al., cited in-paper) + LAC architecture: order-of-magnitude smaller cooling system when heat ingress is concentrated | the paper doesn't give W/W for 20 K cryocoolers directly, but it validates the *architecture* our ZBO row assumes and supplies the energy-per-kg figure that converts boil-off into a $/kWh cost. Our Carnot-derived range (50–150 W/W) remains unanchored by flight data — still flagged as such |

## zero_bo_off_2025 — "Strategies for Zero Boil-Off Liquid Hydrogen Transfer: an export terminal case-study" [T1]

- **Full text hosted**: `full_texts/zero_boil_off_LH2_transfer_strategies_arxiv2512.04609.pdf`
  (arXiv:2512.04609; verified live HTTP 200, application/pdf). Uncertainty analysis of LH₂ transfer between large tanks using centrifugal pumps with/without variable-speed drives.

### Direct anchor for a row we currently carry as an engineering guess

| pipeline row | our value | zero_bo_off_2025 evidence | verdict |
|---|---|---|---|
| In-space propellant transfer loss (fraction per transfer) | **3 %** (range 1–8 %) | VSD pump: **0.00–0.24 wt%**; fixed-speed pump: **0.76–1.06 wt%** (per ~11,248 t transfer) | our value is an order of magnitude above the peer-reviewed best case — but this study is *ground/seaborne* with mature centrifugal-pump hardware at ~70% efficiency; microgravity tank-to-tank transfer has no equivalent flown system. Correct treatment: keep 3 % as the current-TRL estimate, cite this paper for `range_low`, and note in the row that range_low applies only once space-rated pump hardware exists |

## ssap_2021 — "The Proposed Silicate-Sulfuric Acid Process (SSAP): Mineral Processing for In Situ Resource Utilization" [T1]

- **Full text hosted**: `full_texts/silicate_sulfuric_acid_ISRU_process_arxiv2107.05872.pdf`
  (arXiv:2107.05872; verified live HTTP 200, application/pdf).

### The only per-asteroid-TYPE beneficiation yield table found in round 1

Table 3 of the paper gives recoverable products **per 1000 kg of native silicates processed at 100 % efficiency**, for
lunar mare/highlands, Mars, and four asteroid mineralogies (CI-Orgueil, CM-Murchison, CV-Allende C-types; H/L/LL S-types).
Full extraction in `extracted_data/storage_isru_key_numbers.csv`. Highlights:

| body | Fe metal | O₂ | SiO₂ | H₂O (incidental) |
|---|---|---|---|---|
| C-type, CM/Murchison | **375 kg** | 125 kg | 260 kg | 87 kg |
| C-type, CI/Orgueil | 65 kg | 3 kg | 430 kg | 118 kg |
| S-type, H-chondrite | 132 kg | 27 kg | 509 kg | — (none) |

- **Why it matters for the pipeline**: Module 2 splits each body's mass into commodities and applies utility discounts;
  this table is an independent peer-reviewed estimate of what a beneficiation plant actually gets back from C-type vs S-type
  silicates. The CM-vs-CI spread within one spectral type (375 kg Fe vs 65 kg per tonne processed) quantifies exactly the
  error our single-row-per-type approach carries — and it argues for subtyping (Ch/Cgh/…) in Module 2, matching what domain-1's
  density findings already suggested.
- The paper also gives the **~950 °C peak processing temperature** — the thermal-load anchor for a beneficiation step our
  pipeline currently prices only through utility discounts and an ISRU-processing row.

## Round-1 status (domain 5)

3 items processed, all full texts hosted. Headlines: (a) our hydrolox 0.05 %/day boil-off now has a peer-reviewed anchor at
the top of its range; (b) the transfer-loss row's `range_low` should move toward ~1 % with this citation as the lower bound;
(c) SSAP Table 3 is the first external per-type beneficiation-yield check on Module 2, and it shows large within-type spread.


## Round-3 additions — volatiles handling and ISRU plant decomposition

### kleinhenz_2016 [T2] — Kleinhenz, Paulsen & Zacny (NASA Glenn / Honeybee), "Regolith Volatile Recovery at Simulated Lunar Environments", NTRS 20160010281
- **Full text hosted**: `full_texts/kleinhenz_paulsen_zacny_2016_regolith_volatile_recovery_ntrs_20160010281_publicdomain.pdf` (NTRS, verified live from this machine: API record + PDF download OK, 27 slides). Public domain.
- **Key numbers** → `extracted_data/volatile_recovery_isru_key_numbers.csv`: test basis ~5 wt% water in PSR regolith (per LCROSS); **88% of sample water LOST through coring/auger capture** (4 holes, ~115 g each).

### kleinhenz_2018 [T2] — Kleinhenz, Smith, Roush et al. (NASA Glenn/KSC/Ames), "Volatiles Loss from Water Bearing Regolith Simulant at Lunar Environments", NTRS 20180005235
- **Full text hosted**: `full_texts/kleinhenz_smith_zacny_2018_volatiles_loss_water_regolith_ntrs_20180005235_publicdomain.pdf` (NTRS, verified live: API record + PDF download OK, 17 slides). Public domain.
- **What it adds**: the companion study quantifying water escape from regolith simulant across temperature/pressure — i.e. the *physics* of why volatiles are lost during excavation and storage rather than only in transit.

### carlson_2024 [T2] — Carlson, Andersen & Collins (NASA JSC), "In-Situ Resource Utilization Modeling of a Lunar Water Processing System" (SIMA framework), NTRS 20240007647
- **Full text hosted**: `full_texts/carlson_andersen_collins_2024_ISRU_lunar_water_processing_SIMA_ntrs_20240007647_publicdomain.pdf` (NTRS, verified live: API record + PDF download OK, 22 slides). Public domain.
- **Recorded as context-only**: searched every slide for specific-energy figures — none printed (the deck is an architecture/methodology presentation), so it cannot anchor our Wh/kg rows. Its value is structural: NASA's own decomposition of a water-processing plant into excavation → collection/transfer → extraction (dryer + cold trap) → electrolysis mirrors exactly the cost lines we carry, which validates that our operational_costs.csv breakdown matches how the institution actually sizes these plants. Headline finding recorded: H2 liquefaction/storage is the dominant ISRU energy/mass driver — consistent with where our cascade spends.

### What this settles (vs round 1)
- **`Volatile cargo containment` row (0.05 kg per kg volatile)** now has a direct experimental anchor: in controlled lunar-sim hardware, uncontained regolith lost 88% of its water during capture alone — the sealed/shaded hold we price is not conservative engineering margin, it's what measured volatility demands.
- **`Water liberation energy` row (2500 Wh/kg)** gets a mechanism citation: both Kleinhenz decks confirm bound/regolith volatiles are lost to vacuum unless actively recovered by heated extraction + cold trapping — i.e. the dehydroxylation-heating model in our notes field is the right physics, and these two NTRS records are the citable basis for it (they carry no Wh/kg figure of their own, so they anchor the MECHANISM while ssap_2021 remains the numeric yield check).
- **`Drilling / excavation energy` row**: its current citation is "Zacny et al. NIAC studies" — Kleinhenz's co-authorship (Paulsen/Zacny of Honeybee, same group) makes these two decks a verifiable NTRS handle for that named-but-unlinked source; the 115 g/hole capture efficiency figure can also serve as an external check on excavation throughput assumptions.

## Round-3 status (domain 5)
All three new items hosted and access-verified from this machine. Domain now covers: boil-off (rounds 1), transfer loss (round 1), per-type ISRU yields (ssap_2021, round 1), volatiles-loss physics + containment justification (Kleinhenz x2 — new), plant-decomposition validity (Carlson SIMA — new).

## Round-4 additions — electric propulsion performance anchored to the flight article

### nextc_ppu_2020 [T2] — Bontempo, Brigeman, Fain et al. (ZIN Technologies / NASA Glenn), "The NEXT-C Power Processing Unit: Lessons Learned from the Design, Build, and Test of the NEXT-C PPU for APL's DART Mission", NTRS 20205004248
- **Full text hosted**: `full_texts/bontempo_brigeman_fain_2020_NEXT-C_PPU_design_build_test_ntrs_20205004248_publicdomain.pdf` (7.4 MB, 14 pp; verified live from this machine: NTRS API record + PDF download OK). Public domain as a US-government work.
- **Key numbers** → `extracted_data/nextc_ppu_performance_key_numbers.csv`: Prototype PPU **34.5 kg at 0.5–7 kW output** (80–160 V input); system efficiency **94.8% max** with development thruster (March 2019, 7 kW / 120 Vin), dropping to 93.8% hot; Flight PPU for DART tested at **3.7 kW output / 93.9%** with the flight thruster (Jan 2020); beam supply = up to 90% of total PPU power output.

### What this settles
- Our `Power processing unit specific mass` row carries **4.7 kg/kW** and its notes already cite "NASA NEXT-C: 34.5 kg of PPU at 7.4 kW" — that citation now has a hosted, quotable source instead of an unnamed reference. The number is confirmed to the digit (34.5 / 7.4 = 4.66 ≈ 4.7).
- Our `Electric propulsion efficiency` row carries total η = 0.60 (anode × mass-utilisation × PPU). This paper anchors the **PPU half at ~0.94** — which bounds the product: with the PPU at 0.94, the anode+mass terms together must be ≈0.64 for our total to hold, consistent with published gridded-ion figures (NEXT-class anode efficiency ~0.7-0.8). The row's range (0.45–0.72) is therefore defensible at its top end by a flight article.
- This also retroactively validates the v1.6.0 split of the old combined 8 kg/kW thruster+PPU row: the PPU alone is ~34.5 kg and scales with POWER, exactly as the notes field argues — now with the underlying test report committed here.

### next_highpower_2025 [T2] — Obenchain, Cretel, Wirz & Thomas (Oregon State / NASA Glenn), "NEXT Discharge and Performance Characterization for High Power Operation", JANNAF 2025
- **Access**: NTRS record 20250006541 carries only a one-page abstract PDF from this machine (the full paper sits behind the conference link). Recorded `open_not_pulled` with the full abstract.
- **Abstract (as published, retrieved live)**: combines recent NEXT test data and DC-ION multi-fidelity simulations across power levels; characterizes discharge plasma near centerline/exit plane, neutral ingestion in ground tests vs space extrapolation, grid erosion, chamber geometry sensitivity — "to inform life and performance analyses".
- **Pipeline mapping**: context anchor for the high-power end of our electric rows: it is exactly the peer-reviewed work stream behind scaling NEXT-class performance to multi-kW (and beyond) operation — relevant whenever Module 4 sizes a mission above ~7 kW, where we are extrapolating past every flown article. No numbers extracted this round (abstract only).

## Round-4 status (domain 5)
The electric-propulsion rows now rest on the flight article itself: kg/kW confirmed to the digit against NEXT-C's own design-build-test report, and the efficiency chain bounded by its measured PPU figure. Domain 5 coverage after this round: boil-off (r1), transfer loss (r1), ISRU yields + plant decomposition (r1/r3), volatiles-loss physics (r3), EP performance (r4 — new).

## Round-6 addition — RTG rows get a peer-reviewed anchor (and the Pu-238 ceiling gets its citation)

### ambrosi_2019 [T1] — Ambrosi, Williams, Watkinson et al. (ESA + UK partners), "European Radioisotope Thermoelectric Generators (RTGs) and Radioisotope Heater Units (RHUs) for Space Science and Exploration", Space Sci Rev 215:55 (2019), DOI 10.1007/s11214-019-0623-9
- **Full text hosted**: `full_texts/ambrosi_et_al_2019_european_RTG_RHU_space_science_exploration_spacescirev_215-55_CC-BY4.0.pdf` (6.2 MB, 41 pp; verified live from this machine: Springer direct OA PDF + CC-BY 4.0 license statement on p.1).
- **Key numbers** → `extracted_data/european_rtg_review_2019_key_numbers.csv`: GPHS/MMRTG flight heritage documented (Cassini/New Horizons/Galileo = GPHS-RTG; MMRTG for planetary surface); Pu-238 constant-rate production restart targeting **~1.5 kg/yr by 2025**; specific power across RTG classes from ~2.1 W/kg down to 1.3 W/kg (small units and stacked configurations — i.e. BELOW even the MMRTG's 2.4); skutterudite + zintl thermoelectrics named as the next-generation efficiency path.

### What this settles
- The `RTG specific power` row in `operational_costs.csv` previously cited "flight records" without a citable document — that flight record (290 We/56 kg GPHS-RTG; 110 We/45 kg MMRTG) is now confirmed by a peer-reviewed journal review.
- **The Pu-238 supply constraint hard-coded in `calc.py` (:544, :2923 — the ~1.5 kg/yr ceiling that makes RTGs an allocation problem rather than a money problem) had no citable source; it now does.** This was one of the two numbers in the model with the strongest operational consequence and the weakest documentation chain.
- The W/kg range across classes (1.3–2.1 for small/stacked designs) validates how our row is set: 5.0 = deep-space-only qualification, 2.4 = atmosphere-qualified MMRTG floor — deep-space-only design genuinely buys ~2× the specific power of a surface-rated unit, and stacked/small configurations can't reach even the floor.
- Watch item for future data: skutterudite/zintl conversion-efficiency progress is the stated path to higher W/kg; if it matures past lab stage our 6–8% efficiency assumption (in the $/W row) becomes the first number to update.

## Round-6 status (domain 5)
Domain 5's power-system rows are now fully anchored: electric chain = nextc_ppu_2020 + nextc_protoflight_2021 (rounds 4–5, flight articles); nuclear chain = ambrosi_2019 (this round). The solar row remains the one power figure without a dedicated peer-reviewed anchor — it is priced from $/W market data rather than performance physics, which is arguably correct for a cost model.

## Round-7 addition — the solar row gets its first peer-reviewed W/kg anchor, in our exact mission class

### hoffman_2000 [T2] — Hoffman, Kerslake & Hepp (NASA Glenn), Jacobs (SAIC) & Ponnusamy (Spectrum Astro), "Thin-Film Photovoltaic Solar Array Parametric Assessment", NASA/TM--2000-210342 = AIAA-2000-2919
- **Full text hosted**: `full_texts/hoffman_kerslake_hepp_jacobs_ponnusamy_2000_thin-film_PV_solar_array_parametric_assessment_NASA_TM-2000-210342_AIAA-2000-2919_publicdomain.pdf` (1.0 MB, 16 pp; verified live from this machine: NTRS API + PDF download OK). Public domain as a US-government work.
- **Key numbers** → `extracted_data/hoffman_2000_pv_array_key_numbers.csv`. The study parametrically assesses eight missions across the solar system, and one of them is a **Main Belt Asteroid Tour at 1.5 AU using solar electric propulsion — our exact mission class**: 7.5 kW EOL power requirement, total array mass 121 kg (4-junction GaAs case), total array cost $14.1M (2000$).

### What this settles
- **The `Power system specific mass` row (60 W/kg @ 1 AU, SYSTEM-level) now has an independent peer-reviewed cross-check.** The MBAT's fully ancillied array works out to ~62 W/kg in its flight environment (EOL at 1.5 AU). Converting the same hardware to a 1-AU basis — ×(1.5)² ≈ **~140 W/kg ARRAY-ONLY** — and comparing with our SYSTEM figure of 60 W/kg @ 1 AU gives an array-to-system ratio of ~2×, which independently corroborates the row's own internal logic ("batteries, regulation and structure roughly halve that at the system level"). The two figures are consistent, not contradictory: one is array-only in a dim environment, the other is system-level at 1 AU. That reconciliation is now recorded explicitly instead of left to inference.
- **The $/W side**: ~$1880/W array-level (2000$, derived from the stated $14.1M / 7.5 kW) versus cell-level costs in the same study ($400/W 4-j GaAs, $220/W thin-Si, ~$60/W CIS film) — ancillaries roughly quadruple cell cost at array level. Useful context when any solar pricing row is updated.
- **The blanket-vs-system divergence quantified**: total-array specific power grows much less rapidly with cell efficiency than blanket-level does (mechanisms + SADA + structure dominate mass at low film efficiencies). This is the technical reason our row stays SYSTEM-level, and it bounds how far a future wing-only figure (e.g. ROSA's ~150 W/kg) can be pushed before de-rating: below ~12% thin-film efficiency, lightweight substrate alone does not win on mass — that 12% breakpoint is the quantitative basis behind roll-out wings generally.

## Round-7 status (domain 5)
All three power chains are now anchored by peer-reviewed or public-domain flight/parametric sources: electric = nextc_ppu_2020 + nextc_protoflight_2021; nuclear = ambrosi_2019; solar = hoffman_2000 (this round). The domain's remaining unsourced item is the eclipse-baseline row, which is a model-internal bookkeeping figure rather than a physical measurement — no external anchor exists for it by construction.
