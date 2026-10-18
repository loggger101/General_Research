# Domain 25 — Net smelter return: refining charges & payable terms

Backings: economicspace `modules/calc.py` `_mineral_implied_value` (mirroring `modules/mineral_value.py` `mineral_to_element_value`), which values every yield-priced phase as the sum of its element yields times the element prices, and the refined-metal basis of those prices (`iron` "Priced as refined steel scrap").

Created in Round 76 (2026-09-27). Blocks are appended one per round, newest last.

## R76 - Domain opened (2026-09-27; no sources yet)

Returned alloy or concentrate is credited with all its contained metal at refined prices: no payable fraction, treatment or refining charge, or refinery loss, and upstream does not state the assumption. Read at economicspace@1f470d4.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` `_mineral_implied_value` | $/kg = sum of yield x element price (PGM and Au scaled by `pgm_enrichment`) | implicit; no payable, charge or recovery term |
| `mineral_value.py` `nickel-iron` phase | Fe 0.900, Ni 0.090, Co 0.005; Pt 15 ppm, Pd 10 ppm, other PGMs and Au 1-4 ppm | each element valued as refined metal (yields are domain 2's) |
| `mineral_value.py` `native-pgm` phase | Pt 0.70, Pd 0.15, Ir 0.08, Os 0.05, Ru 0.01, Rh 0.01 | full refined price |
| `mineral_value.py` `iron` price basis | $0.50/kg | "Asteroid mining produces refined iron from nickel-iron alloy, NOT iron ore" |

**What a source has to supply:** commercial terms for Ni-Cu-PGM concentrates and mattes (payables, TC/RC, penalties); refinery recoveries for PGMs and for Ni/Co from iron-rich feeds; what Fe-Ni metal with ppm PGMs would fetch and which terrestrial product it resembles; processing routes for metallic meteoritic material.

**Also relevant, registered elsewhere:** `nat_dms2023` (d02), `jm_pgm_market_report_2026` and `lbma_precious_metals_fixings` (d06).

**Boundary:** domain 2 holds yields, domain 6 refined prices, domain 19 recovery at the asteroid; this domain the step from metal delivered to Earth to cash received.

## R81 - First sources (2026-09-28)

Read at economicspace@e3b3897.

- `cowen_agnello_petit_2012_npsr_pge` (SAImm Platinum 2012, pp. 577-592; no licence in the PDF, read only): "Metal recovery in PGE smelting is typically reported to be between 92-95 per cent. and in refining over 99 per cent."; "A deduction of 10 per cent (or 90 per cent payability) of contained metal value would result in the processor receiving between 1-6 per cent of the contained metal value". Table IV: PGE payability 90%, Ni/Cu 85%; TC US$250/t; RC Pt/Pd US$25/oz, Rh US$75/oz, Au US$10/oz, Ni 80c/lb, Cu 20c/lb; chromite penalty above Cr 1.5%. Smelting US$200-US$250 and refining US$250-300 per ton concentrate. `_mineral_implied_value` therefore overstates realised revenue by the processor's take. `extracted_data/r81_refining_terms_key_numbers.csv`.
- `usgs_mcs2026_iron_steel_scrap_chapter` (MCS 2026 v1.3, hosted): No. 1 heavy melting composite averaged $319.00/ton in 2025 ($314.85 in 2024), i.e. $0.319/kg vs upstream's 0.50 (upstream +56.7%); 2025 range $366.26 (March) to $303.46 (November), so 0.50 matches no month. **rc-054** proposes ~$0.32-0.40. US consumption ~57 million tons in 2025.
- `usgs_mcs2026_nickel_chapter`: LME cash $15,000/t = $15.0/kg vs upstream 16.50 (rc-035 already open); ferronickel is its own product class (HTS 7202.60.0000, duty-free), the product an asteroid Ni-Fe phase most resembles; world resources over 350 million tons Ni, ~10% in metallic Fe-Ni.
- `usgs_mcs2026_platinum_group_chapter`: 2025 averages Pd $1,100/oz, Pt $1,200/oz, Ir $4,400/oz, Rh $5,800/oz, Ru $690/oz; no osmium price (upstream's Os 45,000 unsourced). ~140,000 kg Pd+Pt recovered from scrap in 2025 (~50,000 kg Pd and 8,600 kg Pt from US catalytic converters); Michigan Cu-Ni byproduct PGMs "exported for refining".
- `usgs_mcs2026_cobalt_chapter`: US spot cathode $21/lb ($46.30/kg), LME cash $15/lb ($33.07/kg) vs upstream 33.00 (-0.2%).
- `gertsch_1993_asteroid_mining_jsc` (JSC; context only): "The bag could also serve as a retort for carbonyl or other types of processing during return."

`extracted_data/r81_terrestrial_product_prices.csv`. Open: (1) payable terms for asteroid material itself; (2) osmium price; (3) Ni/Co recovery from iron-rich feeds.

## R91 - Iron-rich-feed recoveries (2026-10-01)

Read at economicspace@7d99662 (`_NICKEL_IRON_YIELDS` Fe 0.900 / Ni 0.090 / Co 0.005, no recovery term).

- `taskinen_avarmaa_2021_sustainability_slag_matte_equilibria` [T1, CC BY in-file, hosted]: recovery of small metals "is not feasible in current technologies. They include, e.g., cobalt and platinum group metals in nickel sulphides"; "recovery rates of >90% will be one of the major industrial challenges". Context only.
- `dreisinger_2000_hydrometallurgical_treatment_pgm_sulfide_concentrates` [T2, read only: no licence, PolyMet data by permission]: Northmet ore (0.43% Cu / 0.12% Ni / 0.009% Co, Fe 10.8%): flotation recovers Cu 93.7 / Ni 77.1 / Co 46.4% (concentrate Fe 28.7%), PGMs ~76%; pressure oxidation extracts Cu 99.3 / Ni 95.9 / Co >92% with iron left in the residue (40.8% Fe); PLATSOL at 220 C up to Au/Pt/Pd 96/98/96%; integrated pilot plant Pt 96.0 / Pd 94.6 / Au 89.4 / Co 96.0 / Cu 99.6 / Ni 98.9%. "Toll smelting of nickel/copper concentrates containing PGMs does not produce acceptable returns." `extracted_data/r91_iron_rich_feed_recoveries.csv`.

On a feed this iron-rich, flotation alone loses ~half the cobalt and a quarter of each PGM before any TC/RC or payability. Closes open item (3).

## R98 - PGM world production: Ir, Rh, Ru measured; osmium absent (2026-10-01)

**USGS Minerals Yearbook 2021 PGM chapter** [T3, hosted], Table 5, the latest per-element world table (no later yearbook has a PGM chapter; MCS 2026 covers only Pd and Pt):

| element | upstream cell | USGS 2021 | delta |
|---|---|---|---|
| iridium | ~7,500 kg/yr | 7,880 (SA 7,006 / Russia 230 / Zimbabwe 641; 2017-21: 7,180, 7,540, 8,010, 7,270, 7,880) | measured +5.1% |
| rhodium | ~23,000 kg/yr | 24,400 (SA 20,875 / Russia 1,648 / Zimbabwe 1,334; Canada 500) | measured +6.1% |
| ruthenium | ~30,000 kg/yr | 33,700 (SA 31,463 / Russia 1,000 / Zimbabwe 1,278) | measured +12.3% |

World PGM mine production 472,000 kg (+12%), South Africa 61%, Russia 23%. USGS publishes no separate osmium figure (Census combines Ir/Os/Ru), so the 1.0e3 kg/yr osmium cell needs a non-USGS source. **rc-058** proposes re-pinning Ir/Rh/Ru to ~7.9e3 / ~2.44e4 / ~3.37e4.

`extracted_data/r98_pgm_world_production_key_numbers.csv`.

## R114 - PGM concentrate flowsheet recoveries (2026-10-04)

`dowling_2022_capital_efficient_upgrading_of_pgm_concentrates` (Glencore, SAIMM 2022): ISASMELT + Albion design recoveries on a ~100 g/t Platreef concentrate, 98% Pt/Pd/Au/Rh and 97% Cu/Ni (Table VII), at Pt $950/oz, Pd $2,000/oz, Au $1,600/oz, Rh $5,000/oz, Cu $7,500/t, Ni $15,000/t. Design values, not contract terms. `usitc_hts_7502_20_00_00_nickel_alloys_duty_rates`: nickel alloys duty "Free" (6.6 cents/kg in column 2). `extracted_data/r114_gr_links_key_numbers.csv`. No candidate.

## R164 / R165 - Candidates (2026-10-14)

rc-121 (apply net-smelter-return terms, or state the refined-price assumption) and rc-143 (cite MCS 2026 for cobalt). Texts in `revision_candidates.csv`.

## R182 - Osmium closed via domain 6 (2026-10-16)

`ipa_sfa_2026_osmium_pgm_factsheet` (d06): "Annual global production of osmium is likely to therefore have been limited to about 500kg-550kg/annum over 2024 and 2025." (upstream 1.0e3, ~2x; **rc-125**); no exchange quote exists, the industrial price "fixed in the 300-400$/oz range since the 2000s" (upstream $13,000/kg = $404/oz; **rc-126**). Quotes in `06_commodity_market_pricing/extracted_data/r182_osmium_production_price_key_numbers.csv`. Only open item (1) remains: no source prices Fe-Ni alloy with ppm PGMs directly; Cowen's terms stay the benchmark.
