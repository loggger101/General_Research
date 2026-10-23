# Domain 14 — Propellant & consumable prices

Backings: spacecost `reference/propellants.csv` `ref_cost_usd_per_kg` and the component prices in the comment block above the combined rows in `spacecost/propellants.py`.

Created in Round 74 (2026-09-27). Blocks are appended one per round, newest last.

## R74 - Upstream citations registered (2026-09-27; +8 sources)

All `registered_not_pulled`: `dla_energy_aerospace_standard_prices_fy2020` (T3; hydrazine, MMH, N2O4 and every combined row built from them), `sets_space_2024_hall_propellant_prices` (xenon, argon), `mobius_2024_fueling_starships_methane` (LCH4), `haltermann_solutions_rp1` and `spaceinsider_rp1_price` (RP-1), `efc_gases_xenon_krypton_space_propulsion` (xenon $10k/kg "2023 EFC reference"), `aqua_calc_lox_bulk_price` (LOX).

## R100 - First institutional anchors (2026-10-02; rc-059 opened)

- `inl_rpt_23_75203_krypton_xenon_recovery_cost_benefit` [T2, hosted, US government work]: "The market survey found that prices for Kr and Xe tend to hover around $1/L and $60/L, respectively" (Q1-2023). Table 3 capture costs from reprocessing (not market prices): Xe $71.50 / $101.31 / $131.13 per L; Kr $830.15 / $1,176.34 / $1,522.52 per L (low/mid/high, 300 MTHM/yr plant).
- `iea_global_hydrogen_review_2024` [T3, hosted, CC BY 4.0]: LH2 production cost for the hydrolox ($1.60/kg) and $10/kg NTP/NEP/solar-thermal cells; values are in vector charts, so context-only until extracted.

**Xe/Kr check** (22.414 L/mol at STP): Xe $60/L = $10,243/kg vs upstream $10k (-2.4%); Kr ~$1/L = ~$267/kg vs upstream ~$300 (+12%). SETS Space 2024 gives krypton $2,100-$4,800/kg (aerospace grade, small lots), 8-18x the bulk figure, and the Krypton row cites no source: **rc-059** records both and leaves the segment choice to the owner.

**Iodine:** USGS MCS import CIF values (both volumes in d06): $59/kg (2024) and $68/kg (2025e); 2020-2025e series 31.57 / 32.72 / 45.81 / 61.55 / 61.84 / 68. Upstream's $60/kg sits between the two latest. No re-pin.

**Dead or unverifiable citations:** peroxidepropulsion.com is hijacked (the Evonik HTP quote is gone); DLA FY20/FY24/FY25 PDFs refuse this machine; EFC, Haltermann and SpaceInsider pages carry no prices in static HTML; Mobius is client-rendered. `sets_space_2024_hall_propellant_prices` was read in full: `extracted_data/r100_noble_gas_price_key_numbers.csv`.

## R101 - LH2 production cost; hydrazine citation not found (2026-10-02)

- `nasa_cr_73226_study_cost_system_analysis_lh2_production` (Air Products for NASA Ames, June 1968; hosted): "estimated average product cost of 7.7 to 8.8 cents per pound" for large-scale HST hydrogen; Table 5-2: steam reforming 11.8 / partial oxidation 11.6 / coal gasification 19.9 / electrolysis 18.4 cents/lb, the last two "not economically competitive". The 10 cents/lb in the storage section is a loss-accounting value.
- `nasa_cr_159163_economics_hydrogen_production_liquefaction_updated_1980` (Linde for NASA Langley, Nov 1979; hosted): mid-1980 dollars, LH2 product $1.10/kg ($0.499/lb), gaseous feedstock $0.586/kg ($0.266/lb) at 3¢/kWh and fuel gas $2.84/GJ; a fixed "$0.50 per lb" for lost product cross-checks the dollar year.

Escalated with the d23 World Bank chain (`world_bank_usa_annual_cpi_inflation`): 1968..2024 x9.018 gives $1.53-$1.75/kg; 1980/1984..2024 x3.807/x3.020 gives $3.32-$4.19/kg, inside the hydrolox note's "LH2 base price $3-6/kg (NASA contracts)"; the note's ~$10/kg with handling is above both plant-gate figures, as it says. No candidate.

**Hydrazine:** the row's "commercial $75.8/kg (AIAA 2024)" resolves to no paper (Crossref sweep of AIAA JPC proceedings and NTRS searches); the DLA FY20 $30.5/kg stays its only anchor.

## R110 - Peroxide (HTP) programme context; rc-061 opened (2026-10-03)

The Evonik quote behind the HTP ~$5/kg is unrecoverable (hijacked domain, no archive reachable). Three NASA peroxide-programme decks, hosted, none with a per-kg price (context only):

- nasa_hydrogen_peroxide_propulsion_perspective_ungers_draft (MSFC draft, undated): solicitations under NRA8-19 and NRA8-21 from 1997 "to bring peroxide back into a level of legitimate consideration for upper stage and on-orbit applications".
- anderson_et_al_1999_peroxide_propulsion_turn_of_the_century (MSFC / Boeing Rocketdyne / Orbital, 1999): interest "driven by the need for lower cost propulsion systems and the need for storable reusable propulsion systems".
- mcneal_anderson_1999_the_peroxide_pathway (MSFC, 1999-02-17): "NASA, the Air Force, and industry will invest more than $50million in the development of peroxide technology in the next decade" (an investment, not a price).

**rc-061** (citation) proposed re-sourcing the HTP price or marking it unverified.

## R112 - HTP citation withdrawn upstream (2026-10-04)

spacecost 0.5.1 (tag `v0.5.1`, `85da36c`) applied rc-061: the `HTP-98` comment and the HTP rows now call the ~$5/kg unsourced; values unchanged (5.0 and 4.6875). The dead source was rejected by the owner. A replacement needs a dated $/kg for >=90% hydrogen peroxide from a supplier, procurement record or institutional study.

## R114 - Krypton vs xenon in mission-cost studies (2026-10-04)

`edwards_gabriel_1993_propellant_selection_uk25_ion_thruster_missions` (read in full) assumed $2,400/kg xenon, $450/kg krypton and $840/kg for a 1:4 mixture (p3): Kr/Xe 0.19, against 0.03 for upstream ($300/$10,000) and 0.02-0.03 for INL. Early-1990s planning values, not market prices. `fazio_2019_mission_cost_gridded_ion_engines_alternative_propellants` (abstract only) states no price. rc-059 unchanged. `extracted_data/r114_gr_links_key_numbers.csv`.

## R127 - RP-1 price: the SpaceInsider article read (2026-10-06)

**spaceinsider_rp1_price** (2023-06-13; re-classed verified_live_not_pulled): "RP-1 presents a cheaper option at $2.3/kg" against LH2 "$6.1 a kilogram", CH4 "$8.8/kg", LOX "$0.27/kg", from US defence moving-average prices; Falcon 9 example (312,200 kg LOX + 186,006 kg RP-1) ~$512,108 per launch. First T4 anchor for the kerolox RP-1 component.

## R131 - Current DLA standard prices; rc-083 opened (2026-10-07)

The FY2025 DLA Energy letter `E_2024Oct1AerospaceStandardPrices` was read through server-side extraction (dla.mil refuses this machine) and registered as `dla_energy_aerospace_standard_prices_fy2025` [T3, read, not hosted]. `extracted_data/r131_dla_fy2025_aerospace_prices.csv`:

- MMH $225.40/LB = ~$496.9/kg; hydrazine HPH / H70 $165.75/LB = ~$365.4/kg; NTO MON-3 $106.42/LB = ~$234.6/kg (MON-10 $132.48, MON-15 $262.40, MON-25 $545.48 per LB); LH2 $10.69/LB ≈ $23.6/kg; LOX ~$322-336/tonne.

**rc-083** (value, spacecost@cd66898): the MMH/NTO components (MMH $100/kg + N2O4 $35/kg, "Pricing from DOD FY20 standards.") and the hydrazine row ("DOD FY20 standard $30.5/kg, commercial $75.8/kg (AIAA 2024). Used $75/kg conservative for aerospace.") sit ~5x below current DLA prices. The FY2019 letter is no longer indexed; an Oct-2025 successor letter is live but not yet read.

**Round 209 - SpaceInsider carrier identified; rc-180 opened on the Hydrazine pricing clause.**

Inline named-source sweep across all six spacecost reference CSVs against the registry: Benner compilation resolves via elvis2011, ISS Facts and Figures is registered in d12, the Lyons/Long aerobraking pair sits in d24, DLA FY2025 was already extracted at R131 (r131_dla_fy2025_aerospace_prices.csv), and Janhunen/Zubrin/ThrustMe/Accion/ENPULSION/Ad Astra mentions are prose pointers with no load-bearing figures - per the standing convention they stay unregistered.
One clause survived unresolved and is value-bearing: the Hydrazine row backs $75/kg on an unnamed '(AIAA 2024)'. The figure pair traces to Space Insider, How Much Does Rocket Fuel Really Cost? by Julia Seibert (June 13 2023), pulled live this round - hydrazine tops the chart at up to around $75.8/kg and RP-1 presents a cheaper option at $2.3/kg both count==1, while the Defense Working Capital Fund figure of $30.5/kg that upstream attaches to hydrazine is printed in the carrier as an LH2 standard price. The row spaceinsider_rp1_price (R74-era, bare domain) is upgraded to this identified article with saved-copy sha; r209_hydrazine_price_lineage.csv records the spans. Dollar-year vintage circa 2008 noted rc-168 class, not adjudicated.
This surface is covered; skip unless upstream names the AIAA paper or a hydrazine-specific DoD standard price resurfaces.

**Round 241 - LOX component re-anchor (rc-185)**

DLA letter E_2024Oct1AerospaceStandardPrices (dla_energy_aerospace_standard_prices_fy2025, FY2025 prices effective Oct 1 2024), verbatim rows already extracted at R131 in r131_dla_fy2025_aerospace_prices.csv: "PROPELLANT,OXYGEN TN $335.89" (NSN 9135009652527/9135016653259) and a second NSN at "$322.28". Short ton = 907.18474 kg gives $0.370/kg and $0.355/kg.

Upstream cell: spacecost/propellants.py _COMPONENTS LOX cost_usd_per_kg = 0.20 at b5eb32a, attributed in the component-price comment to "Astronautix / aqua-calc"; both sources are owner-flagged in INDEX.md "Sources to replace" (R240) with DLA FY2025 named as replacement sought. The component feeds _blend into four published rows; the blend formula reproduces every current ref_cost exactly at b5eb32a, and LOX at $0.37 moves kerolox +13.2% (to 1.015633), hydrolox +9.1% (to 1.745933), methalox +54.7% (to 0.376722; LOX is 64 percent of that blend price) and CO/LOX +8.7% (to 0.771367). economicspace reads these ref_costs through modules/transportation.py.

Verdict: open candidate rc-185; upstream untouched (read-only from here). Extracted data: extracted_data/r241_lox_reanchor_key_numbers.csv.

**Round 242 - Xenon price citation swap to INL (rc-186)**

INL/RPT-23-75203 (inl_rpt_23_75203_krypton_xenon_recovery_cost_benefit, hosted in this domain since R100; public-domain DOE report). Sec.1 Introduction verbatim at raw count==1: "prices for Kr and Xe tend to hover around $1/L and $60/L". Sec.2 XENON MARKET ASSESSMENT, PDF p.11 (normalized-whitespace count==1): in the first quarter of 2023, Xe was sold for around $60/L compared to Kr which was trading at approximately $1/L (Wang 2023).

Conversion computed here: molar mass 131.293 g/mol over 22.414 L/mol gives STP gas density 5.8576 g/L, so $60/L = $10,243.04/kg; the upstream Xenon ref_cost_usd_per_kg = 10000.0 at spacecost b5eb32a is -2.4% below that. The identical conversion on Kr (83.798 g/mol, $1/L) gives $267.48/kg and reproduces the upstream krypton comment (about $267/kg), the convention applied when rc-059 was applied in v0.10.0.

Upstream cell: Xenon row notes cite SETS Space 2024 ($5-12k/kg) and "used $10k/kg (2023 EFC reference)" - both sources owner-flagged in INDEX.md Sources to replace (R240) with this INL study named as replacement sought; the 2023 EFC phrase matches zero CITATIONS.md entries at b5eb32a. SETS range brackets the INL-derived figure, so the swap is corroborative not contradictory.

Verdict: open candidate rc-186 (citation; value keep-or-re-pin left to owner); upstream untouched. Extracted data: extracted_data/r242_xenon_inl_price_key_numbers.csv.
