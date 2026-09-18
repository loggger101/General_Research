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
