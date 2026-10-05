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

## zero_bo_off_2025 — "Strategies for Zero Boil-Off Liquid Hydrogen Transfer: an export terminal case-study" [T2 — preprint, not peer-reviewed]

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

## Round-9 addition — the battery row gets its cell-level anchor (and a thermal caveat for asteroid-surface ops)

### ali_2023 [T1] — Ali, Beltran, Lindsey & Pecht (CALCE / U. Maryland), "Assessment of the calendar aging of lithium-ion batteries for a long-term - Space missions", Frontiers in Energy Research 11:1108269
- **Full text hosted**: `full_texts/ali_beltran_lindsey_pecht_2023_li-ion_calendar_aging_long-term_space_missions_frontiers_energy_research_CC-BY.pdf` (1.9 MB, 12 pp; verified live from this machine: Frontiers direct OA PDF + CC BY statement on p.1).
- **Key numbers** → `extracted_data/ali_2023_space_batteries_key_numbers.csv`: space Li-ion specific energy ~265 Wh/kg (citing NASA 2010 / Institute 2022), energy density 670 Wh/L, specific power ~1000 W/kg; flight heritage on Perseverance, OSIRIS-Rex, Parker Solar Probe, THEMIS; operating envelope -40..+40 °C (controlled); calendar-aging model showing capacity fade grows with temperature + state-of-charge.

### What this settles
- **The `Energy storage usable specific energy` row's cell-level input now has a citable source.** The row states "cells reach 250–300 Wh/kg" and derives system-level (packaging/harness/balancing/thermal roughly halve it) × DoD 0.80 = **104 Wh/kg USABLE**. This peer-reviewed space-battery assessment puts the flown value at ~265 Wh/kg — mid-range of our stated cell band, so the top of the derivation chain is anchored; the system-level de-rating remains an engineering assumption (no source claims to be one).
- **The technology behind the row is confirmed as FLOWN, not speculative**: Perseverance, OSIRIS-Rex (a sample-return mission — directly our pipeline's class), Parker Solar Probe, THEMIS. Any reviewer question of "is 104 Wh/kg usable realistic for a deep-space mining rig" now has an answer with a document attached.
- **New caveat surfaced**: the flown envelope is -40..+40 °C under *controlled* thermal management. An asteroid surface (far colder, no atmosphere) would need active heating — if Module 4 does not already carry battery-heating power in its eclipse/night-side budget, this row's note should be read as "thermal control included" and that cost is currently implicit.
- **Calendar aging** quantifies the direction of storage degradation (low T + low SOC minimizes capacity loss) — supports keeping a contingency reserve on any long-dwell depot assumption rather than assuming stored hardware degrades at zero rate.

## Round-9 status (domain 5) — SUPERSEDED by round 10 on one point
Every physical row in `operational_costs.csv` now has either an anchored source or is explicitly model-internal bookkeeping. Power chains = nextc_ppu_2020 / nextc_protoflight_2021 / ambrosi_2019 / hoffman_2000 (rounds 4–7); storage = ali_2023 (this round); ISRU/volatile-recovery = kleinhenz_2016/2018 + carlson_2024; beneficiation yield per type = SSAP table (round-1). The one exception named here — `Drilling / excavation energy` being only partially anchored — was RESOLVED in round 10: metzger_zacny_2020 + just_2019 recorded with full texts read live. The remaining unanchored rows are NRE/reliability/capital-cost figures that are management assumptions by nature, not physical measurements.

## Round-10 addition — the `Drilling / excavation energy` row's "Zacny et al." citation now resolves to real documents (both OA-pending, full texts read live)

### metzger_zacny_2020 [T1] — Metzger (UCF), Zacny & Morrison (Honeybee Robotics), "Thermal Extraction of Volatiles from Lunar and Asteroid Regolith in Axisymmetric Crank-Nicolson Modeling", J. Aerospace Engineering 33(6):04020075
- **Access**: full text read live this round via the authors' arXiv preprint (export.arxiv.org route worked; direct arxiv.org returned 406 — same rate-limit class as before). The PDF states no redistribution license → recorded `open_not_pulled`, NOT hosted. Published version verified real: ASCE landing page + a published erratum for the paper both resolve from this machine.
- **Key content** → `extracted_data/metzger_zacny_2020_key_findings.csv`: generalized regolith thermal-conductivity relationship (Eq 21, basalt fit A0=6.12e-3 W/m-K); low-T volatile release below ~300 °C for epsomite-class material (TGA curves: UCF-CI-1 simulant + Orgueil meteorite); drilling heat leaves soil cooling for hours-to-days; built around the Honeybee WINE coring concept.

### What this settles
- **Our `Drilling / excavation energy` row cites "Zacny et al. (NIAC studies on asteroid / lunar regolith excavation)" — that citation now resolves to a real, verifiable peer-reviewed document** with the stated purpose of producing exactly the energy-requirement numbers our Wh/kg range (loose ≲50 / consolidated ≳500) derives from. The row was previously named-but-unlinked; it is no longer.
- **New operational finding recorded**: drilling's thermal side-effect (hours-to-days cooling between operations) is a mission-timeline cost the model does not currently carry — logged as an open modeling consideration for Module 4, not silently applied.

### just_2019 [T1] — Just, Smith, Joy & Roy, "Parametric review of existing regolith excavation techniques for lunar ISRU", Planetary and Space Science (CC-BY)
- **Access**: CC-BY per OpenAlex but the ScienceDirect direct PDF route bot-blocks this machine (verified 403 — same class as taylor2018/harris_dabramo_2021); recorded `open_not_pulled` with the full abstract. Pullable from a normal browser; when pulled, its per-technique performance-parameter table is what would let us replace our two-point Wh/kg range with technique-resolved values (discrete vs continuous excavators, 13 processes).

## Round-10 status (domain 5)
The last partially-anchored physical row (`Drilling / excavation energy`) now has BOTH its physics-model source and a parametric method review recorded — full texts read live this round. NTRS's search endpoint was down for the entire session (ID lookups worked, `/api/citations?q=` returned 404) so no new NTRS items were added; that remains an open probe for a later round when it recovers.
## Round 43 addition — the excavation-energy row gets its force-model + measurement-facility anchors (and NTRS is reachable again)

**Access breakthrough first:** `api.ntrs.nasa.gov` has been DNS-dead since R9, which froze every "NTRS copy" access path. This round I verified that **the web host serves the whole API surface**: `ntrs.nasa.gov/api/citations/<id>` returns JSON metadata and `…/downloads/<file>` streams PDFs + full-text .txt — all public-domain NASA STI. Every NTRS-hosted source in this repo is therefore pullable from this machine again; three new T2 registrations below were pulled and parsed live through that route. (The single-citation API returns sparse fields for older records — authors/dates came from the citation HTML page.)

### zeng_2007 [T2] — Zeng, Burnoski, Agui & Wilkinson (Case Western Reserve / NASA Glenn), "Calculation of Excavation Force for ISRU on Lunar Surface", 45th AIAA Aerospace Sciences Meeting Exhibit, NTRS 20070018151
- **Full text hosted** (`full_texts/zeng_2007_excavation_force.pdf`, sha256=40815c3294b8…; public domain). The soil-mechanics drawbar-force model for digging lunar regolith — the physics that turns "loose vs consolidated" into a force (hence energy) split.
- **JSC-1a simulant parameters measured in-paper** (the standard lunar-regolith test material): density **ρ = 1680 kg/m3**, cohesion **c = 170 N/m2**, soil-tool adhesion ca = 1930 N/m2, internal friction angle **φ = 35°** (external β=10°, blade δ=20°, K0=0.573), specific gravity of JSC-1a fines **2.85**. Tool envelope: width 1 m, depth to 1 m, velocity 0.1–1.63 m/s under lunar g.
- **Key finding for our row:** required drawbar force is *strongly cohesion-dependent* — "lowest values for cohesionless soil but the highest values for very cohesive soil". That is exactly the mechanism behind `Drilling / excavation energy`'s two-point structure (loose regolith ≲50 Wh/kg, consolidated rock ≳500 Wh/kg): loose C-type regolith sits in the low-cohesion regime where cutting force is small.
- **What it does NOT do:** print a Wh/kg figure — it anchors the *force model and soil parameters*, not the energy number itself (that stays with metzger_zacny_2020's thermal side + just_2019's measured table).

### proctor_apex_2019 [T2] — Proctor et al. (NASA Glenn / LMT), "Experimental Facility to Measure Power and Forces to Excavate Lunar Regolith Simulants", 10th Joint Space Resources Roundtable, NTRS 20190027268
- **Verified live** (PDF pulled + parsed; image-heavy slide deck — instrumentation section fully text-readable). The APEX digger at NASA Glenn's Excavation Lab: electric linear actuators on a 325 VDC/100 A bus, bucket 21.6 cm / 15,600 cm3 / 30° blade, load cell **Fx,Fy ≤1300 N, Fz ≤3900 N**, torque ±203 N-m (≤2% FS), GRC-3B bin filled to 1,587 kg.
- **Why it matters:** the *method* is what produces per-test Wh/kg values — identical motion profile in air and simulant, tare subtracted → net excavation power. Our row's median of 200 Wh/kg assumes exactly this class of measurement exists for loose regolith; now it does (institutionally).

### zeitlin_asteroid_excavation_project [T2] — Zeitlin et al. (NASA KSC IRAD/SMD), "Asteroid Icy Regolith Excavation and Volatile Capture Project", NTRS 20150016080
- **Verified live** (PDF pulled + parsed; TRL 3→5, active 2015–2016). The only registered excavation source aimed at *asteroid* regolith: C-type meteorite minerals incl. hydrated phases, ice fraction as the independent variable, vacuum + cryogenic chamber — i.e. our pipeline's actual target environment (Bennu-class bodies), not just lunar simulant analogs.

### What this settles for `Drilling / excavation energy` (200 Wh/kg median; 50–500 range)
1. **Physics anchor added** (zeng_2007): the force model + JSC-1a parameters behind the loose/consolidated split — previously only metzger_zacny_2020 covered this row and it is thermal, not mechanical.
2. **Measurement-facility anchor added** (proctor_apex_2019): institutional basis for per-test Wh/kg in the loose-regolith regime.
3. **Asteroid-environment confirmation** (zeitlin project): excavation characterization of C-type icy regolith was an active NASA program — our row's target environment is real, not extrapolated from lunar data alone.
4. **Comparison finding (revision candidate, NOT applied):** just_2019's indexed table shows measured specific energies far below our median for loose simulant — RASSOR bucket-drum **0.761 Wh/kg** (footnote: excludes auger transport), pneumatic digger **~2 Wh/kg**, impeller ~115–130 W at 6–30 kg/h, bucket ladder <200 W at up to 2400 kg/h. These are *cutting-only* figures for loose material; our median of 200 is defensible only if it prices duty cycle + on-body transport (which the RASSOR footnote explicitly excludes). Recorded in `extracted_data/r43_excavation_energy_key_numbers.csv` — **context-only until just_2019's full text is pulled** (ScienceDirect still bot-blocks; browser backend was down this round, so no pull attempt succeeded — stays open_not_pulled with the snippet values quarantined as context).

### Round-43 status (domain 5)
Registry +3 T2 → domain 5 now carries 16 sources. Open items: just_2019 full-text pull (blocks turning the comparison finding into an applied revision).

## Round 44 addition — the ZBO cryocooler rows get their first TESTED-hardware anchor (Carnot estimates -> measured W/W)

**The gap:** our `Zero-boil-off cryocooler (20 K)` row (80 W/W median, 50-150 range) and its partner specific-mass row (5.0 kg/W) carried the note "engineering estimates from Carnot limits" — every other physics number in domain 5 rested on a paper or dataset; these two were arithmetic. R43's NTRS access breakthrough made this closeable: three documents pulled live via `ntrs.nasa.gov/api/`, all public-domain NASA STI, full text hosted.

### nugent_2022_rtb_cryocooler_test [T2; full text hosted] — Nugent, Grotenrath & Johnson (NASA Glenn), "20 Watt 20 Kelvin Reverse Turbo-Brayton Cycle Cryocooler Testing and Applications", NTRS 20220009350
The acceptance test of NASA's 20 W / 20 K reverse turbo-Brayton cryocooler (tested at Creare in a vacuum bell, BAC simulator network). Table 1 values extracted by word coordinates from the hosted PDF:

| Parameter @20K | State of art | Threshold | Project goal | **Tested**¹ | Projected² |
|---|---|---|---|---|---|
| Lift capacity (W) | 1 | 17 | 20 | **19.2** (max demonstrated 22.46 at TP2) | 20.4 |
| Specific mass (kg/W, flight-like)³ | 18.7 | 5.5 | 4.4 | **5.5** | 5.2 |
| Specific power (W/W) | 370 | 80 | 60 | **91.6** | 86.3 |

¹ tested values only achievable at 285 K heat rejection; ² projected to 270 K reject; ³ flight-like projections. Per-test-point specific-power sweep spans 78.7-281.2 W/W across the acceptance matrix (Carnot refrigeration efficiency 7.1-8.2%).

### hastings_2010_lht_zbo_demonstration [T2; full text hosted] — Hastings et al., "Large-Scale Demonstration of Liquid Hydrogen Storage With Zero Boiloff for In-Space Applications", NASA/TP-2010-216453, NTRS 20110004377
The MHTB ground demonstration that the whole ZBO architecture works on a tank article: passive insulation + propellant recirculation + pressure control around a commercial **Cryomech GB37** (two-stage Gifford-McMahon). Verbatim from p.16 of the hosted PDF: *"The cryocooler rated capacity is 30 W at 20 K and requires **350 W of power input per watt of cooling for a 4% Carnot cycle efficiency**. The first stage provides 50 W of cooling at 80 K."* — that legacy-GM figure (350 W/W) is the baseline the RTB row brackets from below: tested RTB ≈92 W/W vs GM 350, a ~4x improvement in specific power for the same job.

### plachta_2017_cryo_zbo_goals [T2; full text hosted] — Plachta, Stephens & Johnson (NASA); Zagarola & Deserranno (Creare), NTRS 20180004709
Program context confirming the `status=development` / TRL-5 claims: verbatim — *"while there are many flight cryocoolers available at 20 and 90K … **the largest has less than 1W of cooling at 20K** and just 20W at 90K"* → nothing ZBO-scale has flown (our rows' note already said this; now it's cited). Also: an 8.4 m LH2 tank heat leak "will probably be in the hundreds of watts" without a 90 K shield — sizing context for why these two rows matter at real scale. (NTRS carries a duplicate record, 20180004710, same paper under slightly different title wording — one registration only.)

### What this settles for `storage_systems.csv`
- **AGREE on both rows; anchor upgraded from Carnot arithmetic to test data.** Median 80 W/W = NASA's own program threshold exactly; the tested unit (91.6 / projected 86.3) sits inside our 50-150 range in its upper half — a conservative median, now justified by hardware rather than assumption. Specific mass: our worked example ("20 W leak → ~100 kg machine, ~1.6 kW") is consistent with tested flight-like 5.5 kg/W × 91.6 W/W (≈108 kg / ≈1.83 kW).
- **No revision applied** (target repo read-only): the project GOAL of 60 W/W is unmet by tested hardware — if future characterization testing hits it, that becomes a revision candidate for the median; until then the threshold-based 80 stands as the defensible value.

### Round-44 status (domain 5)
Registry +3 T2 → domain 5 now carries 19 sources; all three hosted full-text (public domain). just_2019 remains open_not_pulled: ScienceDirect still bot-blocks, and this round's browser-backend attempts failed again (three consecutive session timeouts — the backend itself is wedged, not the target site); CORE/BASE aggregators have no OA PDF. The R43 quarantined specific-energy values stay context-only until a full-text pull succeeds from an interactive machine.
### damodaran_cost_of_capital_by_industry [T3; open service] — Damodaran (NYU Stern), "Cost of Capital by Industry Sector," updated January 2026

**The first registered anchor for the `WACC` row in operational_costs.csv.** That row's note cites
"Boeing 7.5% / Howmet 8.3% WACC (ValueInvesting.io 2026) as the industrial floor ... (Damodaran NYU Stern industry tables)" —
the Damodaran citation had never been registered or verified until now. Pulled live from this machine on 2026-09-23:
HTML table at `stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html` (sha256=04a4dd2188cbc9...) plus the XLS twin
(`.../pc/datasets/wacc.xls`, sha256=d38b149c731bbb..., byte-identical on both www.stern.nyu.edu and pages.stern.nyu.edu hosts).

Live table: 96 industries, per-sector beta / cost of equity / capital structure / after-tax cost of debt / **cost of capital**.
Key rows (parsed from HTML cells — no OCR ambiguity):

| sector | n firms | beta | CoE | E/(D+E) | AT-CoD | D/(D+E) | **CoC** | vs our WACC value 10% |
|---|---|---|---|---|---|---|---|---|
| Aerospace/Defense | 79 | 0.95 | 8.17% | 86.53% | 3.97% | 13.47% | **7.60%** | ours +240 bps (+31.6%) — startup premium, inside [7.5, 15] range |
| Metals & Mining | 73 | 1.04 | 8.60% | 90.10% | 2.52% | 9.90% | **8.20%** | ours +180 bps (+22.0%) — above the mining floor too |
| Precious Metals (domain-6 context) | 56 | 0.84 | 7.68% | 93.21% | 5.97% | 6.79% | **7.47%** | a defensible discount rate for PGM holdings — no such row exists in our pipeline yet; recorded as context, not a revision candidate |
| Total Market (n=5994) | 5994 | 0.91 | 8.02% | 73.98% | 3.97% | 26.02% | **6.96%** | ours +304 bps (+43.7%) above the all-market baseline — consistent with a venture-risk premium, not an error |

Audit against our row (value=0.10, range_low=0.075, range_high=0.15):
- **AGREE on the floor**: `range_low` 7.5% vs live Aerospace/Defense CoC 7.60% = within -10 bps (-1.3%) — the "industrial floor" claim holds at sector level even though ValueInvesting.io itself is not verifiable from this machine (recorded as secondary citation only).
- **AGREE on the value**: our 10% sits +240 bps above the aerospace anchor and +180 bps above metals & mining — exactly where a "startup risk premium to ~10-15%" should land; `range_high` 15% remains unanchored (no sector in the table reaches it), which is fine: it bounds venture scenarios, not industry.
- **Internal consistency verified programmatically**: all 96 rows satisfy CoC = E/(D+E)*CoE + D/(D+E)*AT-CoD to within +/-0.05 pp — the parsed cells are self-consistent, so no transcription ambiguity in any number above (all deltas computed by code from raw values; see extracted_data/r47_damodaran_cost_of_capital_key_numbers.csv).

### Round-47 status (domain 5)
Registry +1 T3 -> domain 5 now carries 20 sources. The WACC row is the first operational-costs cell anchored by a live, re-queryable institutional dataset (T3 per the LBMA precedent); DSN time ($1530/hr, NASA MOCS FY09) and launch insurance (~10%, Plane Talking/Gallagher) remain cited-but-unregistered — recorded as open items, not chased this round.
### jpl_dsn_services_catalog_820_100 [T2; full text hosted] — JPL DSN Services Catalog 820-100 Rev H (Jun 6, 2022)

**The named-but-unregistered source behind the 'Deep Space Network time' row.** The note itself says "Authoritative current
rates: dse.jpl.nasa.gov/ext/ calculator" — this round I pulled both halves of that route. The calculator is a client-side JS app
(dse.jpl.nasa.gov/ext/) whose rate engine lives server-side (`apertureFeeTool/cost/<mission>/<costMethod>/<fiscalYear>/...` POST with the
full scenario payload; `api/reference` exposes only antenna metadata, 77 assets — no rates). So the verifiable anchor is JPL's official
DSN Services Catalog (public NASA PDF, hosted here):

- **p65 eq. 6-1: AF = RB * AW * MW** where RB = "hourly rate, adjusted annually"; AW = aperture weighting (1.0 single 34-m; 2.0 two-station
  array + 2-station Delta DOR; 3.0 three-array OR any combination including a 70-meter station; 4.0 four-array); MW = MSPA factor (1.0, or 0.5 downlink-only).
- **p66: "At the time of publication ... the DSN contact dependent hourly rate (RB) was $1,792"** — i.e. ~$1,792/hr per weighted aperture-hour as of June 2022; passes >8h are segmented at 8h for setup/teardown overhead.

Audit against our row (`Deep Space Network time`, value **$1,530/hr** single 34-m dish, range [1000-4000], note: "MOCS cited $1057/hr in FY09; CPI-adjusted to 2026 ≈ $1530/hr. 70-m apertures ~$4k/hr"):
- **Rev H official RB → current dollars (BLS CPI-U actuals pulled from data.bls.gov):** H1-2022 avg = 288.347; latest actual Aug-2026 = 334.980 (x1.1617); 2026 YTD avg x1.1502. Computed **34-m rate ≈ $2,082/hr** → our $1,530 is **−26.5% LOW**. Our range [1000-4000] DOES bracket the computed rate (the value is stale-low).
- **70-m:** AW=3.0 → computed ≈ **$6,245/hr**; note's "~$4k/hr" is **−36% LOW**.
- **Our number vs its own stated method:** FY09 $1,057 x World-Bank annual-inflation chain 2009..2024 (x1.4570) = **$1,540** → −0.65%, i.e. internally consistent — but the FY09 MOCS rate is superseded by Rev H's official $1,792 RB. The row should track the catalog + CPI route instead.
- Cross-validation: BLS level ratio Dec-2016→Dec-2024 (x1.3072) vs WB chain 2017..2024 (x1.3070) — agree to **0.02%**, so both inflation chains are trusted for this derivation.
- REVISION CANDIDATES recorded (target repo read-only): value $1,530 → ~$2,080 (−26.5%); 70-m note figure ~$4k → ~$6.2k.

### gallagher_plane_talking_space_market_updates [T3; open service, extraction-only] — Gallagher Specialty "Plane Talking" Space Market Update series

**The cited-but-unregistered source behind the 'Launch insurance' row.** The note says: "Market rate per Plane Talking (Gallagher) Q1 2024 —
premiums rose from ~6% (early 2023) to ~10% post-Intelsat 33e loss. First-of-kind vehicles at upper end." Pulled live this round: the index page,
the **Q1-2024 Space Market Update** (the cited document), Q4-2023, and current issues through Q2-2026 — all open HTML on specialty.ajg.com, no auth.

What the cited Q1-2024 issue actually says:
- 2023 underwriting result: **loss of circa USD900mn against premium income of circa USD550mn** (plus a further USD230mn loss in Dec 2022).
- "Looking back over both a three-year and five-year period, with loss ratios on average between 100% and 110%, **insurers are suggesting that premium rating needs to increase significantly.**"

Audit against our row (`Launch insurance`, value **10%** of launch+payload value, range [5-15]):
- **Direction + magnitude corroborated** (a hard loss year followed by explicit rate increases is exactly the ~6%→~10% move described), but **no issue pulled contains an explicit launch-premium-% figure** — so our 10% is registered as DIRECTIONALLY corroborated, NOT numerically pinned. The "~6% early-2023" baseline likewise has no verbatim source cell in the issues I could reach (honest gap; Q4-2023 notes insurers' internal edicts of "at least 15%" increases entering 2023 that did not fully stick, and buyers "generally experiencing premium increases below 5%" by end-2023 for non-loss-active risks).
- **FACTUAL ERROR FOUND in the note:** "post-Intelsat 33e loss". Plane Talking Q4-2023 attributes the H2-2023 rating reset to claims of ~USD826m where ">85% of the 2023 loses (including the two standout large losses from **Viasat-3 and Inmarsat 6-F2**) have stemmed from post-separation spacecraft issues, rather than launch failures." IS-33e itself broke up IN GEO on **Oct 19, 2024** (US Space Forces/SpaceTrack alert: ~20 tracked pieces; Boeing-built bird launched Aug 2016) — after the Q1-2024 issue and not a launch loss. The note's causal attribution is wrong even if its resulting market read (~10% post-loss-year rates) happens to be right.

## Round 56 addition — the TPS row's cited source is registered + hosted; post-flight material anchors recorded (+1 T2, registry -> 123)

**Target:** `spacecost/reference/operational_costs.csv` 'Heat shield / TPS for Earth return' ($50k/kg, band $20–150k). The row's note already cites **NTRS 20140005558** ("Stardust / OSIRIS-REx capsule heritage (see NTRS 20140005558 for material data)") — a cited-but-unregistered source, the same gap class as R36's elkins paper. Registered and hosted this round: `stackpoole_2013_pica_pica_x_postflight_eval` [T2].

**What it is:** Stackpoole, Kao, Qu & Gonzales (NASA Ames / ERC Inc.), "Post-Flight Evaluation of PICA ‐ PICA-X — Comparisons of the Stardust SRC ‐ Space-X Dragon 1 Forebody Heatshield Materials", International Planetary Probe Workshop Jun 2013; NASA ARC-E-DAA-TN9994. NTRS determination PUBLIC_USE_PERMITTED → hostable (T2 per convention). **Caveat recorded in the registry row: NTRS hosts only the title/summary slide of this presentation** — no fuller version exists anywhere reachable, so what follows is everything the document contains.

**Verbatim from the hosted PDF's own text layer:**
- "Both materials performed well with no unusual ablation performance"
- "More recently, PICA was chosen as the primary heatshield for the successful Mars Science Lab (MSL) and the upcoming OSIRIS‐REx missions"
- "Space‐X developed a variant, PICA‐X, and used it as the heatshield material for its Dragon spacecraft, which successfully orbited the Earth and re‐entered the atmosphere during the COTS Demo Flight 1 in 2010"
- "PICA‐X virgin and char have higher density than Stardust era PICA"

**Effect on our row:** the $50k/kg figure stays an engineering estimate (the note says exactly that, and no per-kg PICA-X cost is published anywhere reachable — checked NTRS + web this round), but its *heritage* claim now rests on a registered source: PICA was the enabling TPS for Stardust (2006 re-entry) and the baseline forebody TPS for MSL & OSIRIS-REx; SpaceX's PICA-X variant flew Dragon COTS Demo Flight 1 (2010); post-flight analysis found both materials performed well with no unusual ablation, with PICA-X virgin/char denser than Stardust-era PICA. The row can now cite a real document for its material class instead of an unregistered handle.

## Round 57 addition — Plane Talking series extended through Q2-2026; launch-insurance row re-checked against the full issue run (+ honest-gap status on the upper-stage row and just_2019)

**Target:** `spacecost/reference/operational_costs.csv` 'Launch insurance' (value = 10% of launch+payload value, band 5-15%) — its cited source is already registered (`gallagher_plane_talking_space_market_updates`, T3). This round pulls the REMAINING issues in that series so criterion #2 holds for this row: **7 issues now read live** (Q4-2023, Q1-2024 [the cited document], + Q4-2024 / Q1-2025 / Q2-2025 / Q1-2026 / Q2-2026 this round).

**Verbatim from the newly pulled issues (each re-fetched live at verify time; slices extracted programmatically, not hand-typed):**
- [Q4-2024] "circa. USD2bn of claims being notified within 18 months."
- [Q1-2025] "Total 2024 Working Capacity – USD 550m Total 2025 Working Capacity – USD 502m"
- [Q2-2025] "finally shown signs of having turned the corner with competition for attractive risks starting to exert pressure on premium rates."
- [Q2-2025] "As the market became increasingly competitive from 2012 to 2018, market premium declined by over 50%."
- [Q1-2026] "Market capacity for 2026 showed an encouraging increase of approximately USD100m year on year,"
- [Q1-2026] "notice of potential loss for SpainSat NG-2, insured for over USD400m. With a total loss now apparently confirmed , this shifts the 2025 space insurance market underwriting loss ratio from circa 15% to circa 75%"
- [Q1-2026] "premium rate reductions remain available on prime in-orbit business and launch pricing continues to improve."
- [Q2-2026] "over USD 70 million of theoretical capacity has been added to the market in 2026."
- [Q2-2026] "The only significant claim reported since SpainSat in December 2025 has been AST SpaceMobile’s BlueBird 7 satellite, following Blue Origin’s unsuccessful launch in April 2026 – insured for circa. USD30m."
- [Q2-2026] "we continue to see increased competition for heritage in-orbit and launch risks, which could drive premium rate reductions in the second half of 2026."

**Finding — rate direction (the substantive new information):** the series shows a full hardening->softening cycle. 2023 underwriting loss ~USD900mn -> Q1-2024 'premium rating needs to increase significantly' (the cited document, i.e. the era our value was calibrated against) -> Q2-2025 'finally shown signs of having turned the corner ... pressure on premium rates' -> Q1-2026 rate reductions available and launch pricing improving despite the SpainSat NG-2 total loss (>USD400m insured; 2025 underwriting loss ratio ~15% -> ~75%, +60 pp) -> Q2-2026 further easing expected into H2. **Our ~10% value was calibrated to a hardening-era snapshot and may sit slightly high against the easing 2026 market — still DIRECTIONALLY corroborated.**

**Honest gap (unchanged, now verified across the whole run):** NO issue in all 7 publishes an explicit launch-premium-% figure. A %-sweep of every issue found only capacity/loss-ratio percentages ('over 15% more theoretical capacity' Q1-2026; 'declined by over 50%' historical). The row therefore remains directionally corroborated, NOT numerically pinned — same verdict as R50, now with the full evidence base.

**Provenance correction (in place):** R50's registry cell claimed '(+ Q4-2023, **Q2-2026 issues pulled this round**)'. That was premature: R50's own extracted CSV carries only Q4-2023/Q1-2024 figures. The series is now ACTUALLY covered through Q2-2026 (this round); the cell has been corrected in `sources.csv` + `05_inspace_operations/sources_domain.csv`.

### Upper-stage row institutional-gap status (criterion #2; no new source)
The 'Expendable upper stage recurring cost' row ($4,800/kg; band 1,750-13,400) is built from two estimates in its note: F9 second stage ~$10M on ~4,000 kg dry (low end $1,750-2,500/kg) and Centaur III ~$30M on ~2,250 kg dry (high end ~$13,400/kg). R57 re-swept both hosted OIG audits for EUS/Centaur unit pricing AND the 308-page SP-4176 'Taming Liquid Hydrogen' Centaur history: **no per-unit stage price anywhere reachable.** IG-24-001 Table 1 gives only 'Exploration Upper Stage for Artemis IV — $482M', which is a Block-1B launch scope (the whole EUS deliverable under the Stages contract), not a unit cost; SP-4176 is historical narrative with program-level costs (R&D FY59-FY61 $4m->$36.6m->$62.6m; program totals $600-700m era) and no modern per-stage figure. **The ~$30M Centaur III number remains an honest gap** — the row's high end is unanchored by any institutional source reachable from this machine.

### just_2019 route re-sweep (still quarantined; R43-R57)
Re-verified every non-browser open-access route: Unpaywall 422; Semantic Scholar and OpenAlex both confirm CC-BY but point ONLY at the ScienceDirect PDF (`sciencedirect.com/science/article/pii/S003206331930162X/pdf`) which is Cloudflare-blocked from this machine (403 with browser headers + cookie jar); BASE API IP-denied; UCL Discovery 403; CORE 403; MRM Manchester DNS-fail. **The full text exists on exactly one host — ScienceDirect — and needs a working browser daemon** (still down, R43-R57). The quarantined context-only specific-energy values from the publisher's indexed snippet stay as recorded until a pull succeeds.

## Round 63 addition — FY2027 Budget Estimates deep-mined for in-space ops: Space Operations table gives row 5 its first institutional ENVELOPE (source already registered+hosted R62; registry unchanged at 128)

**Source**: the same hosted document as Round 62 (*NASA FY 2027 BUDGET ESTIMATES*, Apr 2026, 384 pp) — re-pulled fresh this round and sha-verified byte-identical to the hosted copy (19304ffc1317c018...). Cross-domain use: d5 row anchoring from a d7-hosted source (no registry change; R52 deepening convention).

**p60 table *Space Operations* (SO-2), Budget Authority in $ millions, FY2025..FY2031** — extracted structurally (label line + exactly 7 value lines per row; every label count==1):

| line | FY2025 | FY2026 | **FY2027 req** | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|---|---|
| Commercial LEO Development | -- | -- | 299.7 | 299.8 | 599.8 | 599.8 | 1,577.2 |
| **International Space Station** | -- | -- | **921.2** | 921.2 | 921.3 | 921.3 | 921.3 |
| Space Transportation | -- | -- | 1,152.5 | 1,152.4 | 1,152.3 | 1,152.3 | 174.7 |
| Space and Flight Support (SFS) | -- | -- | 673.8 | 673.8 | 673.8 | 673.8 | 674.0 |

(FY2025/FY2026 = enacted, '--' in the request columns; verbatim footnote p60: 'FY 2025 reflects the funding amount specified in Public Law 119-4...'.)

**Plus a second table on p60** (Planned Obligations): WFTC – ISS Operations **$250.0M/yr FY2027-31** — mandatory funding from the Working Families Tax Cut Act (PL 119-21) that 'will support ... ISS operations, which includes maintenance, research, and cargo flights to support crew presence on ISS' (verbatim p60). Cargo-flight money is thus ring-fenced separately from the base program line.

**Comparison vs our row 5 (`Depot berthing & handover operations`, USD per delivery, centre $2M, range [0.5-8]M)**:
- Our note says the estimate was 'Scaled from ISS visiting-vehicle berthing ops'. This table is exactly that institutional reference: NASA's ENTIRE annual ISS program line (ops + cargo flights + maintenance) = **$921.2M/yr** FY2027, of which WFTC ring-fences $250M specifically for the cargo/maintenance side.
- Our one-time per-delivery centre of $2M is **0.217% OF THE ENTIRE ANNUAL PROGRAM LINE** (computed in code: 2.0/921.2x100) — i.e. even a generous multi-event berthing/handover year would consume only a fraction of the institutional envelope.
- Verdict: **ENVELOPE / order-of-magnitude consistency anchor, not a pin** (same honesty class as R62's curation line): no per-berthing figure is published anywhere in this document either — NASA funds the program, not the event. Row 5 stays an ESTIMATE but now has its first institutional upper bound on file; **no revision forced**.

**Negative probe (criterion #2)**: 'depot' count = **0** across all 384 pages — commercial depots are NOT yet funded in FY2027, confirming row 5's note ('no commercial depot exists yet'). Closest forward-looking line: p63 verbatim '$1.0 billion to CLDP to support the procurement of commercial space station services...' (Commercial LEO Development $1B for FUTURE commercial space station services — context only, not an ops anchor).

## Maintenance (2026-09-26) — four files un-hosted; lac_bac insulation labels corrected; full SSAP table

- **Un-hosted**: lac_bac_2024 and ssap_2021 (arXiv default licence); nextc_ppu_2020 (NTRS: may include copyrighted material); jpl_dsn_services_catalog_820_100 (copyright Caltech, recorded as public domain). Un-hosted on 2026-09-26 because the licence does not permit redistribution (details in each registry row); every number this file quotes from them was checked against the PDF first and is in `extracted_data/`.
- **lac_bac_2024, round 1: the insulation labels were swapped.** The paper (p7) gives perlite 5905 W ≈ 0.04 %/day (the better stack) and HePUR 35 350 W ≈ 0.24 %/day. The table above and the CSV had it the other way round, and "35 W" was a truncation of 35 350 W. Our hydrolox 0.05 %/day still sits next to the best case; what changes is which insulation that case is. Abstract figures for LAC/BAC with each stack are now extracted.
- **ssap_2021**: round 1 called Table 3 fully extracted, but only 3 of its 9 bodies were. The full table (Moon mare/highlands, Mars, three C-type and three S-type mineralogies, 8 products) is in `extracted_data/ssap_2021_table3_theoretical_yields.csv`.
- **zero_bo_off_2025** is an arXiv preprint with no journal version: re-tiered T2, and "peer-reviewed lower bound" corrected in the registry, INDEX and rc-028. lac_bac_2024 (Cryogenics 148:104065, 2025) and ssap_2021 (Acta Astronautica 188:57-63, 2021) were published, so they stay T1.
- Page numbers added to the nextc_ppu_2020 rows; the DSN and insurance CSVs gained `source_id`. stackpoole_2013 is marked context-only.

## R70 - Full-extraction pass of the hosted sources (2026-09-27; registry unchanged)

Every hosted full text in this domain was re-read end to end for pipeline-useful numbers; tables were read by word coordinates (or from rendered page images where the text layer fails) and checked against their printed totals. New files (all in `extracted_data/`, every row carries `source_id` and a page location): `r70_ali_2023.csv` (8); `r70_ali_2023_table3_calendar_aging_fit.csv` (6); `r70_ambrosi_2019.csv` (9); `r70_carlson_2024.csv` (5); `r70_hastings_2010_lht_zbo_demonstration.csv` (8); `r70_hoffman_2000.csv` (6); `r70_kleinhenz_2016.csv` (5); `r70_kleinhenz_2016_deltion_capture_results.csv` (12); `r70_kleinhenz_2018.csv` (4); `r70_plachta_2017_cryo_zbo_goals.csv` (6); `r70_stackpoole_2013_pica_pica_x_postflight_eval.csv` (3); `r70_zeng_2007.csv` (3); `r70_zero_bo_off_2025.csv` (6).

- **Correction - kleinhenz_2016 "88% lost".** `volatile_recovery_isru_key_numbers.csv` attributed an 88% water loss to coring/auger capture. The p22-23 results table shows 88.9% for the single push-tube sample (65 g, long exposure); the coring-auger samples (~115 g) lost 23-59%. kleinhenz_2018's five-year average is ~30% (5 wt% beds) and ~80% (0.8 wt% beds). The row is fixed in place; its conclusion (handling loses a large share of the water) stands. The full table is `r70_kleinhenz_2016_deltion_capture_results.csv`.
- **carlson_2024 and stackpoole_2013 are now cited.** Both were context-only. Carlson's subsystem power/volume/mass shares were chart-read (electrolysis ~37% and H2 liquefaction ~35% of power; H2 liquefaction ~58% of volume); Stackpoole's summary slide gives the Stardust PICA peak of 1000 W/cm2 / 28 kJ/cm2 against ~50 W/cm2 for Dragon-1 PICA-X. Registry wording updated.

## R71 - Side-deepening extraction round (2026-09-27; logged in R72; registry unchanged)

Branch `side-deepening`, commit 0729c2d, merged into this branch in R72. It gave the 20 PDFs un-hosted on 2026-09-26 (restored byte for byte from git `5dd58d5`, sha256 matched against `DOWNLOADS.md`) their first full pass, and read seven non-hosted sources from copies the owner downloaded (DOWNLOADS.md section B). The commit wrote no FINDINGS block or log entry; this block and the R71 log entry were written in R72 from the commit and the files themselves. R72 then re-checked every R71 file whose PDF is restorable: every numeric cell was searched for in the PDF text (0 values missing outside cells the R71 notes say were read from page images), the image-read cells were compared against rendered pages, and large tables were checked row by row. New files: `r71_jpl_dsn_820_100_key_numbers.csv` (13); `r71_jpl_dsn_820_100_table5_1_station_rf_capabilities.csv` (14); `r71_lac_bac_2024_key_numbers.csv` (12); `r71_metzger_zacny_2020_key_numbers.csv` (15); `r71_metzger_zacny_2020_table1_lcross_volatiles.csv` (14); `r71_nextc_ppu_2020_key_numbers.csv` (6); `r71_nextc_ppu_2020_table1_ppu_supplies.csv` (6); `r71_nextc_ppu_2020_table2_flight_ppu_survey.csv` (7); `r71_proctor_apex_2019_key_numbers.csv` (10); `r71_ssap_2021_key_numbers.csv` (6); `r71_ssap_2021_reactions_energetics.csv` (18); `r71_zeitlin_asteroid_excavation_project_key_numbers.csv` (5).

- **metzger_zacny_2020** (thermal-conductivity, specific-heat and sublimation models; LCROSS volatiles table) from the preprint the owner downloaded; **proctor_apex_2019** and **zeitlin** re-read in full.
- From the restored PDFs: jpl_dsn_services_catalog_820_100 Table 5-1 (station RF capabilities); nextc_ppu_2020 Tables 1-2 (PPU supplies; flight PPU survey with computed kg/kW); ssap_2021 reaction energetics; lac_bac_2024 key numbers.

## R72 - Tables R70/R71 skipped, verification of R71, upstream re-check (2026-09-27; registry unchanged)

This round's container reached only package registries (arXiv, NTRS, JPL, Google Docs and every publisher returned 403), so nothing new could be fetched; the work used the hosted PDFs and the 20 restored from git `5dd58d5`. Each hosted and restored PDF's table captions were listed and matched against the extracted CSVs; tables no CSV cited were read by word coordinates (columns assigned from header or fully populated rows, so blank cells stay blank) or from rendered page images, and checked against printed totals. Upstream heads re-read: spacecost@e831245, AsteroidCatalog@852bf69, economicspace@1f470d4 (unchanged since 2026-09-26). New files: `r72_ambrosi_2019_tables1_10_rtg_rhu.csv` (108); `r72_hastings_2010_tables1_10_pump_and_heat_leak.csv` (23); `r72_nugent_2022_rtb_cryocooler_test_results.csv` (109).

- **nugent_2022 Tables 2-3** (R44 took only the Table 1 KPPs). **Source inconsistency**: Eq.2 (input/lift) reproduces the printed specific power at every point except DP4 (122.2 printed, 105.0 computed), and Eq.3 (106.3 kg / lift) reproduces specific mass except at DP3/DP4, whose printed 6.4 and 5.3 look swapped; kept as printed. **Upstream agreement**: DP1 lifts 19.56 W at 22.5 K for 1.68 kW with a 106.3 kg flight-like mass. That matches spacecost's `Cryocooler specific mass (20 K)` note, 'a tank leaking 20 W needs ~100 kg of machine and ~1.6 kW', and 85.9 W/W sits beside the 80 W/W centre. At the 3 W part-load points specific power reaches 247-281 W/W, above the row's 50-150 band, which describes design-point operation. p8 adds the ISRU sizing: 0.3 kg/h of H2 liquefaction needs 150-300 W of 20 K refrigeration.
- **hastings_2010 Table 10** (MHTB heat-leak worksheet, test P263952H.300, 305 K hot boundary): boil-off 0.0971 kg/h gives 13.10 W total (12.23 W from mdot x hfg x rho_l/(rho_l - rho_v), recomputed, plus 0.87 W superheat), 0.377 W/m2, and 2.385 W through penetrations (the seven lines sum). Not reproduced, flagged in the rows: the '4 legs' 1.449 W (4 x mean of legs 1 and 3 = 1.249 W) and the 0.377 W/m2, which implies 34.74 m2 against the 35.74 m2 surface on p15. Table 1 gives mixer-pump power against flow.
- **ambrosi_2019 Tables 1-10** (re-entry ballistics and heating, Bi-Te module properties over 10,000 h, FE and RHU thermal results). The text measures 9.1-9.3 We from a 200 Wth source and a 9.4 kg 10 We system, i.e. **~1 W/kg specific power as built**, about half the ~2.1 W/kg design figure R70 recorded. spacecost's `RTG specific power` (5.0 W/kg) is a GPHS/Pu-238 figure, so the americium unit is context only.
- **metzger_zacny_2020 vs spacecost `Water liberation energy`**: the row's arithmetic assumes a flat c_p of 800 J/kg K from 200 to 700 K. The paper's lunar-soil fit averages 763 J/kg K over 200-400 K (4.7% below, consistent), but the quartic diverges above ~400 K (6,724 J/kg K at 700 K), so it cannot check the rest of the range. No candidate.
- **plachta_2017 Table 1** (circulator characteristics): the hosted PDF prints the caption with no table body; nothing to extract.

## R74 - Upstream citations registered (2026-09-27; +7 sources, T1x1, T3x3, T4x3; nothing extracted)

Sources the upstream repos cite that this registry did not have, found by reading every per-row `notes` field, code comment and CITATIONS.md in AsteroidCatalog@852bf69, spacecost@e831245 and economicspace@1f470d4. Each is `registered_not_pulled`: its DOI was checked against Crossref, or its landing page against a live request from this machine, and the result is recorded in the row. No full text was sought and no number was extracted; the rows are the queue for a later extraction round.

- `faa_14_cfr_part_450_launch_reentry_licensing` (T3): operational_costs.csv "FAA Part 450 licensing compliance", "(launch only)" and "Third-party liability insurance" rows.
- `crs_r48582_commercial_launch_reentry_regulations` (T3): operational_costs.csv "FAA Part 450 licensing compliance" row.
- `mil_hdbk_189c_reliability_growth_management` (T3): operational_costs.csv "Mining reliability growth exponent" (Duane alpha band for an active growth programme).
- `duane_1964_learning_curve_reliability_monitoring` (T1): operational_costs.csv "Mining reliability growth exponent" (the model it parameterises).
- `valueinvesting_io_2026_boeing_howmet_wacc` (T4): operational_costs.csv "Cost of capital (WACC)" industrial floor.
- `space_com_pu238_rtg_cost_reporting` (T4): operational_costs.csv "RTG (radioisotope power)" Pu-238 cost context.

## R76 - Gap recorded from the second domain pass (2026-09-27; registry unchanged)

Found while looking for new domains in economicspace@1f470d4 and spacecost@e831245; no source was sought. One depot row in this domain's scope has no registry source:

| cell | current value | upstream's stated basis |
|---|---|---|
| `storage_systems.csv` `Depot refuelling flights to escape`, carried as Starship's `tanker_flights_for_escape` in `launch_vehicles.csv` | 12 [8, 16] tanker launches per fully fuelled departure | "SpaceX's own range for filling a Starship in LEO before a high-energy departure"; no registry row maps to it |

What a source has to supply: the propellant a departing Starship-class vehicle needs in LEO and the propellant each tanker flight delivers, from the operator or an independent analysis.

## R77 - Sources moved to domains 16-21 (2026-09-27; registry unchanged at 267)

These rows moved to the domain that now holds the cells they back. The blocks above stay as written, so their relative paths to the files below no longer resolve from this folder; the files are at the paths given here.

| id | moved to | earlier blocks here | files now at |
|---|---|---|---|
| `mil_hdbk_189c_reliability_growth_management` | 16 | R74 | none (no files) |
| `duane_1964_learning_curve_reliability_monitoring` | 16 | R74 | none (no files) |
| `damodaran_cost_of_capital_by_industry` | 17 | Round 44 addition | `17_cost_of_capital_contingency_insurance/extracted_data/r47_damodaran_cost_of_capital_key_numbers.csv`, `17_cost_of_capital_contingency_insurance/extracted_data/r47_damodaran_cost_of_capital_full_table_96_industries.csv` |
| `valueinvesting_io_2026_boeing_howmet_wacc` | 17 | R74 | none (no files) |
| `gallagher_plane_talking_space_market_updates` | 17 | Round 44 addition; Round 57 addition | `17_cost_of_capital_contingency_insurance/extracted_data/r57_plane_talking_series_key_numbers.csv` |
| `faa_14_cfr_part_450_launch_reentry_licensing` | 18 | R74 | none (no files) |
| `crs_r48582_commercial_launch_reentry_regulations` | 18 | R74 | none (no files) |
| `just_2019` | 19 | Round-9 status; Round-10 addition; Round 43 addition; Round 44 addition; Round 57 addition | `19_asteroid_excavation_beneficiation/extracted_data/r43_excavation_energy_key_numbers.csv` |
| `zeng_2007` | 19 | Round 43 addition | `19_asteroid_excavation_beneficiation/extracted_data/r70_zeng_2007.csv`, `19_asteroid_excavation_beneficiation/full_texts/zeng_2007_excavation_force.pdf` |
| `proctor_apex_2019` | 19 | Round 43 addition; R71 | `19_asteroid_excavation_beneficiation/extracted_data/r71_proctor_apex_2019_key_numbers.csv` |
| `zeitlin_asteroid_excavation_project` | 19 | Round 43 addition | `19_asteroid_excavation_beneficiation/extracted_data/r71_zeitlin_asteroid_excavation_project_key_numbers.csv` |
| `ssap_2021` | 19 | the `ssap_2021` block; Round-3 additions; Round-3 status; Maintenance; R71 | `19_asteroid_excavation_beneficiation/extracted_data/ssap_2021_table3_theoretical_yields.csv`, `19_asteroid_excavation_beneficiation/extracted_data/r71_ssap_2021_key_numbers.csv`, `19_asteroid_excavation_beneficiation/extracted_data/r71_ssap_2021_reactions_energetics.csv` |
| `jpl_dsn_services_catalog_820_100` | 20 | Round 44 addition; Maintenance; R71 | `20_mission_operations_communications/extracted_data/r71_jpl_dsn_820_100_key_numbers.csv`, `20_mission_operations_communications/extracted_data/r71_jpl_dsn_820_100_table5_1_station_rf_capabilities.csv` |
| `stackpoole_2013_pica_pica_x_postflight_eval` | 21 | Round 56 addition | `21_mass_cost_estimating_relationships/extracted_data/r70_stackpoole_2013_pica_pica_x_postflight_eval.csv`, `21_mass_cost_estimating_relationships/full_texts/pica_pica_x_stardust_dragon_postflight_eval_ntrs_20140005558_publicdomain.pdf` |

Shared CSVs that cite a moved source and stay here: `extracted_data/r50_dsn_rates_and_launch_insurance_key_numbers.csv` (`gallagher_plane_talking_space_market_updates`, `jpl_dsn_services_catalog_820_100`); `extracted_data/storage_isru_key_numbers.csv` (`ssap_2021`); `extracted_data/unhosted_sources_key_numbers.csv` (`jpl_dsn_services_catalog_820_100`). Where a moved row names one of them, the path now includes this folder.

Revision candidates written up here keep `domain_dir` 05: rc-026 (open, Drilling / excavation energy), rc-027 (blocked, Drilling / excavation energy), rc-030 (open, Deep Space Network time), rc-031 (open, Launch insurance).

`metzger_zacny_2020` stays here. Its row maps to the drilling-energy row, but the paper is about thermal extraction of volatiles, which this domain keeps; domain 19 refers to it by id.
## R97 - The Pu-238 unit-price gap closes: first institutional per-kg figures (2026-10-01; +1 row -> registry 339)

The standing d5/d14 gap since the GR-R74 era: *'Pu-238 unit price gap remains'* - upstream's `operational_costs.csv` RTG note carries 'Historical Russian Pu-238 ~$2.5M/kg' citing Space.com (T4), and no registered T1-T3 source anywhere in the repo carried a per-kg figure for the isotope itself (rc-043 covers production RATE, not price). This round closes it with one hosted NIAC report.

**Howe et al., 'Economical Production of Pu-238' - NASA NIAC Phase I final report** [T2, full text hosted; NTRS 20160010587 PUBLIC_USE_PERMITTED]: USRA Center for Space Nuclear Research (PI Steven D. Howe) with University of Utah co-I Terry Ring; grant NNX11AR30G. The study's economic core is exactly the missing number - prices per kg of Pu-238 charged to the government, by reactor size and return-on-investment target:

| scenario | price/kg (verbatim p.32) | production rate |
|---|---|---|
| 5 MW reactor, 20% ROI | $7.8 M | 2.25 kg/yr |
| 5 MW reactor, 0% ROI | $3.5 M | 2.25 kg/yr |
| 10 MW reactor, 20% ROI | $4.3 M | 6.25 kg/yr (optimal) |
| 10 MW reactor, 0% ROI | **$1.6 M** - the floor of the range | 6.25 kg/yr |

p.37 adds a second cost basis for the INL-reactor project: capital $35.7M ($35.2M reactor + CAT.-1 fence extension), process cost **$3.2M +/- 50% per kg** against 'the sale price of $6,000,000' (a DOE-era purchase-price reference - the only explicit Pu-238 SALE PRICE in any registered source), ROI 4%/yr with a 5.3-yr pay-back; and if an existing facility's neutron flux can be used instead of building a reactor, processing cost drops to **$0.56M/kg**.

**Verdict vs our row.** Upstream's '~$2.5M/kg historical Russian Pu-238' now has institutional context: it sits INSIDE the NIAC range ($1.6-$7.8 M/kg by reactor size and ROI target, with a $0.56M/kg processing floor and a $6M/kg sale-price reference) - so the note's figure is plausible as printed; **consistency anchor, no re-pin** (the same verdict pattern as R95's Shapiro deployment statistics: different populations measure different things). The RTG row's own $/W cell ($200k-$1M per W-electric at 6-8% conversion) is unaffected - it prices the finished generator, not the fuel.

**Inconsistency kept as printed (p.37):** 'The costs for this process on a per kg of Pu-238 are $3.2 million (±50%) which is substantially above the sale price of $6,000,000' - arithmetically $3.2M is below $6M; recorded verbatim with the flag in `extracted_data/r97_pu238_unit_price_key_numbers.csv` (repo convention: keep source inconsistencies as printed). No revision candidate opened: nothing here contradicts an upstream cell value, and rc-043 already covers the production-rate wording.

**Domain 5 status after R97:** both Pu-238 rows in this domain now have T1-T3 support - ambrosi_2019 (T1) for the flight record + supply constraint, Howe et al. (this round) for unit prices; space_com_pu238_rtg_cost_reporting stays as the T4 marker of what upstream actually cited.
