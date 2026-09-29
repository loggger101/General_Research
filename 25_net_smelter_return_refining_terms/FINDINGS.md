# Domain 25 — Net smelter return: refining charges & payable terms

Backings: economicspace `modules/calc.py` `_mineral_implied_value` (mirroring `modules/mineral_value.py` `mineral_to_element_value`), which values every yield-priced phase as the sum of its element yields times the element prices, and the refined-metal basis of those prices (`iron` "Priced as refined steel scrap").

Created in Round 76 (2026-09-27). Blocks are appended one per round, newest last.

## R76 - Domain opened (2026-09-27; no sources yet)

A kilogram of returned alloy or concentrate is credited with all of its contained metal at the refined-metal price: no payable fraction, no treatment or refining charge, no refinery loss. The assumption is not written down upstream, so it has no stated basis at all. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` `_mineral_implied_value` | $/kg = sum of yield x element price (PGM and Au yields scaled by `pgm_enrichment`) | implicit; no payable fraction, charge or refinery-recovery term |
| `mineral_value.py` `nickel-iron` phase | Fe 0.900, Ni 0.090, Co 0.005; Pt 15 ppm, Pd 10 ppm, other PGMs and Au 1-4 ppm | each element valued as refined metal (the yields themselves are domain 2's) |
| `mineral_value.py` `native-pgm` phase | Pt 0.70, Pd 0.15, Ir 0.08, Os 0.05, Ru 0.01, Rh 0.01 | each metal valued at its full refined price |
| `mineral_value.py` `iron` price basis | $0.50/kg | "Asteroid mining produces refined iron from nickel-iron alloy, NOT iron ore" |

**What a source has to supply.**

- Commercial terms for selling nickel-copper-PGM concentrates and mattes: payable percentages by metal, treatment and refining charges, penalty elements.
- Refinery recoveries for PGMs, and for nickel and cobalt from iron-rich feeds.
- What iron-nickel metal with ppm-level PGMs would actually fetch: which terrestrial product it resembles (steel scrap, ferronickel, nickel pig iron) and how that product is priced.
- Terrestrial processing routes suited to metallic meteoritic material.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `nat_dms2023` (domain 2): metal extraction from asteroid proxies.
- `jm_pgm_market_report_2026` (domain 6): refined PGM prices.
- `lbma_precious_metals_fixings` (domain 6): refined precious-metal prices.

**Boundary.** Domain 2 holds the yields (what the body contains); domain 6 holds the refined-metal prices; domain 19 holds recovery at the asteroid (`beneficiation_recovery`). This domain holds the step from contained metal delivered to Earth to cash received.
## R81 - First sources (2026-09-28)

Six rows registered; five full texts hosted under `full_texts/` with manifest rows. The domain's core question - what a kilogram of returned nickel-iron alloy with ppm-level PGMs would actually fetch after payable fractions, treatment/refining charges and refinery losses - now has its first terrestrial benchmark: the South African PGE industry's commercial terms (Cowen et al.), plus the four USGS MCS 2026 chapters that price every element upstream credits at full refined value. Upstream cells re-read from economicspace@e3b3897 (= origin/main; local WIP ahead of it is read-only input and does not touch these cells).

- `cowen_agnello_petit_2012_npsr_pge` (SAImm Platinum 2012, pp. 577-592): **the d25 anchor** - 'Evaluation of net smelter returns in the South African PGE industry by application of base metal concentrate commercial treatment terms'. The paper's own words: 'Metal recovery in PGE smelting is typically reported to be between 92-95 per cent. and in refining over 99 per cent.'; its worked example shows what a real sale deducts - 'A deduction of 10 per cent (or 90 per cent payability) of contained metal value would result in the processor receiving between 1-6 per cent of the contained metal value'. Table IV terms: PGE payability 90%, Ni/Cu 85%; TC US$250/t concentrate; RC Pt/Pd US$25/oz, Rh US$75/oz, Au US$10/oz, Ni 80c/lb, Cu 20c/lb; chromite penalty basis max Cr 1.5%. The paper's cost analysis: 'the cost of South African PGE smelting varies between US$200-US$250 per ton concentrate, and refining US$250-300 per ton'. **Not hostable**: no licence statement anywhere in the PDF (Camera Press watermark only) - extraction-only per AGENTS.md's licence rule; every number is in `extracted_data/r81_refining_terms_key_numbers.csv`. Implication for upstream: `_mineral_implied_value` credits 100% of contained metal value, while a terrestrial PGE sale pays ~90% payability minus TC/RC - i.e. the model overstates realized revenue by roughly the processor's margin (the paper's own worked example puts that at 1-6% of contained value for a 10% deduction).

- `usgs_mcs2026_iron_steel_scrap_chapter` (USGS MCS 2026, ver. 1.3 May-2026): **the iron row's product**. 'The annual average price delivered in 2025 was estimated to increase to $319.00 per ton compared with the full-year average of $314.85 per ton in 2024' (No. 1 heavy melting composite, Fastmarkets AMM) = **$0.319/kg vs upstream's ref_price_usd_per_kg = 0.50 (-36.2%; ours +56.7%)**. Upstream's own note cites 'Q1 2026 mid-range $343/MT US' - the chapter's Jan-Nov-2025 range ('ranged from a high of $366.26 per ton in March to a low of $303.46 per ton in November') brackets that, so 0.50 matches no month; **rc-054 opened** proposing a re-pin to ~$0.32-0.40 (the series itself). Market depth: 'U.S. apparent consumption of iron and steel scrap was an estimated 57 million tons in 2025'.

- `usgs_mcs2026_nickel_chapter` (USGS MCS 2026): LME cash average annual **$15,000/t = $15.0/kg vs upstream's 16.50 (+10% above the reference)** - rc-035 already open on this cell from WB data; the chapter adds what no other registered source has: 'Ferronickel' as a distinct tariff/product class (HTS 7202.60.0000, duty-free) and 'Hydrothermal systems such as iron-nickel alloy' named among world nickel resource types ('Globally, nickel resources have been estimated to contain more than 350 million tons of nickel', with the metallic-iron-nickel class at ~10%) - i.e. the terrestrial product an asteroid's nickel-iron phase would most resemble for sale.
- `usgs_mcs2026_platinum_group_chapter` (USGS MCS 2026): refined PGM prices for the native-pgm phase's elements - 2025 annual averages Pd $1,100/oz, Pt $1,200/oz, Ir $4,400/oz, Rh $5,800/oz, Ru $690/oz. **Osmium still has no price row** in the table (production figures only) - the standing osmium pricing gap persists through MCS 2026 v1.3; upstream's Os ref_price_usd_per_kg = 45,000 remains unsourced by any registered source. Recycling context: 'About 140,000 kilograms of palladium and platinum were recovered globally from new and old scrap in 2025' (incl. ~50,000 kg Pd + 8,600 kg Pt from U.S. catalytic converters) - the terrestrial flow that sets what PGM-bearing material fetches; and 'Small quantities of PGMs also were recovered as byproducts of copper-nickel mining in Michigan; however, this material was exported for refining.' - direct precedent for selling Ni-Cu-PGM material on a refined-metal basis.

- `usgs_mcs2026_cobalt_chapter` (USGS MCS 2026): cobalt average annual prices U.S. spot cathode $21/lb ($46.30/kg) / LME cash $15/lb (**$33.07/kg vs upstream's 33.00 - ours is -0.2% vs the LME basis (within rounding)**).

- `gertsch_1993_asteroid_mining_jsc` (JSC Space Resources Vol. 3: Materials, NTRS 19930007695; GOV_PUBLIC_USE_PERMITTED): context-only for the processing-route question - 'The bag could also serve as a retort for carbonyl or other types of processing during return.' No load-bearing number.

**What is still open in this domain.** (1) A payable-fraction/charge model for asteroid material specifically - Cowen's terms are terrestrial PGE-concentrate benchmarks; no source prices an iron-nickel alloy with ppm-level PGMs directly. (2) The osmium price gap (no published price anywhere reachable, incl. MCS 2026). (3) Refinery recoveries for Ni/Co from iron-rich feeds specifically (Cowen's 92-95% smelting / >99% refining are PGE figures).
