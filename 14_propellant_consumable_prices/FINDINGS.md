## R975 — Moran 1991 hydrolox comparator citation and scenario scope (2026-11-19)

`spacecost_hydrolox_moran_energy_comparator_code_current_2026`: Spacecost main `868f42890ac97ee40a50d79f7b33863046edb0ff`, `propellants.py` line 332 attributes 4.41 kWh/kg and “2 MW at 280 kg/hr of water” to Moran’s 1991 subsystem study. `CITATIONS.md` §2 has no Moran entry; the Morren & Curran 1991 reference there is a different 2-kW arcjet study.

`moran_1991_nasa_tm_103730_on_orbit_electrolysis`: NASA NTRS identifies Matthew E. Moran’s *Conceptual Study of On Orbit Production of Cryogenic Propellants by Water Electrolysis* (NASA-TM-103730, NTRS 19910010004; AIAA Paper 91-1844). Table II, printed p. 16, lists “4.41 kWh/kg-H2O” for electrolysis and 398 kW total lunar-processor power. The Mars Missions section, printed p. 6, gives 378.2 kg/h water; the scaled power is 2,790 kW on printed pp. 1 and 17. Their ratio is 7.376 kWh/kg, computed here. The report does not state the code’s exact 2 MW / 280 kg/hr pair.

**Verdict:** open **rc-836** to add a complete report entry and align the comparator’s figures with the source scenario. Applied rc-166 covered the low-end energy-band comparison; the selected 15,200 Wh/kg input is unchanged. Extracted: `extracted_data/r975_spacecost_moran_1991_processor_figures.csv`.

## R950 — Spacecost notes and comments applied upstream; ArgonSC density value candidate (2026-11-19)

spacecost bad5ba80884e6bd6825de83ff8e942619d962a1f (PR #51, package 0.18.4, data contract 1.27.3 to 1.27.4). Notes on 51 rows, comments, CITATIONS.md and README.md; compared column by column, every value column of the six reference tables and the summary sample is identical to 1.27.3.

- Closed as applied: rc-361 (dv_penalty_factor 1.5 named on each row); rc-421, 422, 435, 544, 598, 680, 694, 701, 718, 766 (scenario labels with comparators); rc-525 (HTP / RP-1 320 s beside Krishnan 2010); rc-545 (Ryugu structural OH); rc-576, 577 (LH2 and water prices as scenarios); rc-585, 586 (tank base and class multipliers); rc-596 (Didymos estimates); rc-658 (krypton ratios as assumptions); rc-679 (ArgonSC comment); rc-767 (Berthier et al. 2023 for ssoBFT); rc-774 (MPD, no RIAME test).
- spacecost's notes for rc-656, 657, 659, 660 and 661 are in the same release; those candidates close with their frozen-row half in economicspace.
- New value candidate rc-816: `tegeler_span_wagner_1999_argon_equation_of_state`, as CoolProp 8.0.0 implements it (EOS key Tegeler-JPCRD-1999), gives 313.480 kg/m3 and Z = 0.94109 at 293.15 K / 18 MPa against the stored ArgonSC 0.300 kg/L, 4.49% higher. The value move is held for owner review.

Verdict: 22 closed as applied; rc-816 opened. Extracted data: extracted_data/r950_argon_supercritical_density_tegeler.csv.

## R833 — Latest frozen Stage 3 HTP price provenance

- **economicspace_latest_stage3_htp_price_rows_2026** (Economicspace origin/main e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7, campaign/stage3/spacecost-0.14.0/propellants.csv, pipeline 1.23.6, catalog date 2026-10-17, rows 13-14): HTP monopropellant stores $5.00/kg and labels it an unsourced estimate pending re-sourcing; the HTP/RP-1 row stores $4.6875/kg and says it rests on the same unsourced HTP input.
- **spacecost_htp_price_reference_row_current_2026** (Spacecost origin/main a401930efe30aaad01aafd2b3cb332ad0438c841, reference/propellants.csv, rows 13-14): current component row still labels $5/kg unsourced and links the price comparator to rc-319; the HTP/RP-1 price derives from that component.
- **epic_aerospace_htp_product_price** (official Epic Aerospace capabilities page, lines 53-57): lists 98% HTP at $65/kg, a 280 kg minimum order, and estimated shipping of $3,500-$8,500; no price effective date or bulk/delivered basis is stated.
- **Upstream rows:** Economicspace campaign/stage3/spacecost-0.14.0/propellants.csv; current Spacecost reference/propellants.csv.
- **Verdict:** Open rc-706 for the latest frozen Economicspace snapshot (pipeline 1.23.6). Distinct from rc-705 (earlier frozen 1.22.0 snapshot), rc-319 (current Spacecost price review), and rc-525 (impulse basis). No numeric replacement inferred.
- **Extracted data:** extracted_data/r833_economicspace_latest_htp_price_gap.csv.

## R832 — Frozen Stage 3 HTP price provenance

- **economicspace_frozen_stage3_htp_price_rows_2026** (Economicspace origin/main e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7, campaign/stage3/spacecost-0.10.0/propellants.csv, pipeline 1.22.0, rows 13-14): HTP monopropellant stores $5.00/kg and calls it “an unsourced estimate pending re-sourcing”; the HTP/RP-1 row stores $4.6875/kg and says it rests on the HTP row's unsourced $5/kg.
- **spacecost_htp_price_reference_row_current_2026** (Spacecost origin/main a401930efe30aaad01aafd2b3cb332ad0438c841, reference/propellants.csv, rows 13-14): the current HTP row still labels $5/kg unsourced and links the supplier comparison to open rc-319; the derived HTP/RP-1 row inherits that component.
- **epic_aerospace_htp_product_price** (official Epic Aerospace capabilities page, lines 53-57): lists “98% HTP - Price per Kg | 65 USD,” a 280 kg minimum order, and estimated shipping of $3,500-$8,500. The page gives no price effective date or bulk/delivered basis.
- **Upstream rows:** Economicspace campaign/stage3/spacecost-0.10.0/propellants.csv; current Spacecost reference/propellants.csv.
- **Verdict:** Open rc-705 for the frozen Economicspace HTP input and derived blend row. The Epic offer is a comparator, not a matched replacement. Distinct from open rc-319 (current Spacecost HTP price review) and rc-525 (HTP/RP-1 impulse basis). No numeric replacement inferred.
- **Extracted data:** extracted_data/r832_economicspace_frozen_htp_price_gap.csv.

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

Extracted data: `extracted_data/r101_lh2_production_cost_key_numbers.csv`.

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

## R209 - SpaceInsider carrier identified; rc-180 opened on the Hydrazine pricing clause (2026-10-19)

Inline named-source sweep across all six spacecost reference CSVs against the registry: Benner compilation resolves via elvis2011, ISS Facts and Figures is registered in d12, the Lyons/Long aerobraking pair sits in d24, DLA FY2025 was already extracted at R131 (r131_dla_fy2025_aerospace_prices.csv), and Janhunen/Zubrin/ThrustMe/Accion/ENPULSION/Ad Astra mentions are prose pointers with no load-bearing figures - per the standing convention they stay unregistered.
One clause survived unresolved and is value-bearing: the Hydrazine row backs $75/kg on an unnamed '(AIAA 2024)'. The figure pair traces to Space Insider, How Much Does Rocket Fuel Really Cost? by Julia Seibert (June 13 2023), pulled live this round - hydrazine tops the chart at up to around $75.8/kg and RP-1 presents a cheaper option at $2.3/kg both count==1, while the Defense Working Capital Fund figure of $30.5/kg that upstream attaches to hydrazine is printed in the carrier as an LH2 standard price. The row spaceinsider_rp1_price (R74-era, bare domain) is upgraded to this identified article with saved-copy sha; r209_hydrazine_price_lineage.csv records the spans. Dollar-year vintage circa 2008 noted rc-168 class, not adjudicated.
This surface is covered; skip unless upstream names the AIAA paper or a hydrazine-specific DoD standard price resurfaces.

## R241 - LOX component re-anchor (rc-185) (2026-10-23)

DLA letter E_2024Oct1AerospaceStandardPrices (dla_energy_aerospace_standard_prices_fy2025, FY2025 prices effective Oct 1 2024), verbatim rows already extracted at R131 in r131_dla_fy2025_aerospace_prices.csv: "PROPELLANT,OXYGEN TN $335.89" (NSN 9135009652527/9135016653259) and a second NSN at "$322.28". Short ton = 907.18474 kg gives $0.370/kg and $0.355/kg.

Upstream cell: spacecost/propellants.py _COMPONENTS LOX cost_usd_per_kg = 0.20 at b5eb32a, attributed in the component-price comment to "Astronautix / aqua-calc"; both sources are owner-flagged in INDEX.md "Sources to replace" (R240) with DLA FY2025 named as replacement sought. The component feeds _blend into four published rows; the blend formula reproduces every current ref_cost exactly at b5eb32a, and LOX at $0.37 moves kerolox +13.2% (to 1.015633), hydrolox +9.1% (to 1.745933), methalox +54.7% (to 0.376722; LOX is 64 percent of that blend price) and CO/LOX +8.7% (to 0.771367). economicspace reads these ref_costs through modules/transportation.py.

Verdict: open candidate rc-185; upstream untouched (read-only from here). Extracted data: extracted_data/r241_lox_reanchor_key_numbers.csv.

## R242 - Xenon price citation swap to INL (rc-186) (2026-10-23)

INL/RPT-23-75203 (inl_rpt_23_75203_krypton_xenon_recovery_cost_benefit, hosted in this domain since R100; public-domain DOE report). Sec.1 Introduction verbatim at raw count==1: "prices for Kr and Xe tend to hover around $1/L and $60/L". Sec.2 XENON MARKET ASSESSMENT, PDF p.11 (normalized-whitespace count==1): in the first quarter of 2023, Xe was sold for around $60/L compared to Kr which was trading at approximately $1/L (Wang 2023).

Conversion computed here: molar mass 131.293 g/mol over 22.414 L/mol gives STP gas density 5.8576 g/L, so $60/L = $10,243.04/kg; the upstream Xenon ref_cost_usd_per_kg = 10000.0 at spacecost b5eb32a is -2.4% below that. The identical conversion on Kr (83.798 g/mol, $1/L) gives $267.48/kg and reproduces the upstream krypton comment (about $267/kg), the convention applied when rc-059 was applied in v0.10.0.

Upstream cell: Xenon row notes cite SETS Space 2024 ($5-12k/kg) and "used $10k/kg (2023 EFC reference)" - both sources owner-flagged in INDEX.md Sources to replace (R240) with this INL study named as replacement sought; the 2023 EFC phrase matches zero CITATIONS.md entries at b5eb32a. SETS range brackets the INL-derived figure, so the swap is corroborative not contradictory.

Verdict: open candidate rc-186 (citation; value keep-or-re-pin left to owner); upstream untouched. Extracted data: extracted_data/r242_xenon_inl_price_key_numbers.csv.

## R243 - LCH4 price bracketed by hosted Pink Sheet series (rc-187) (2026-10-23)

Hosted workbook domain 06: sheet Monthly Prices, columns Natural gas US and Liquefied natural gas Japan (both $/mmbtu), Sept 2026 edition through 2026M08. Computed here from the committed file: US hub 2025 mean $3.525/MMBtu over n=12; Japan LNG delivered liquid 2025 mean $12.036/MMBtu (2026 January-August means: US $3.595, Japan $12.793).

Conversion arithmetic computed here: methane gross calorific 55.5 MJ/kg; MMBtu(IT) = 1055.06 MJ; therefore 19.01 kg CH4 per MMBtu and hub gas content $0.185/kg versus delivered liquid $0.633/kg at the 2025 means.

Upstream: propellants.py _COMPONENTS carries LCH4 cost_usd_per_kg = 0.40 with trailing comment "~$400/tonne open market", the component block names Mobius Market Research 2024, and the methalox CSV notes repeat "LCH4 ~$400/tonne open-market per Mobius Market Research 2024." The INDEX Sources to replace row (R240) marks that source news class with replacement sought: a natural-gas or LNG price series. The cell sits between the two institutional anchors - defensible as a US-liquefaction-at-hub midpoint, unsourced as written.

Verdict: open candidate rc-187 (citation; owner keeps value decision inside the bracket); upstream untouched. Extracted data: extracted_data/r243_lch4_pink_sheet_key_numbers.csv.

## R257 - Drift audit of spacecost caed8ce..5ea3f24 (v0.14.0 quote surface) (2026-10-26)

Drift audit at this round's pins: spacecost caed8ce..5ea3f24 = v0.14.0 recorded-quote surface only (quotes.py 367 lines, SHA256SUMS + two fuel snapshots; consumer-contract and README prose commits); economicspace d5bbe63..0d08128 moves Stage-2 pricing to the spacevalue sibling and stops fetching live prices (#179), plus samebytes verification passes - no tracked dollar row moved in either diff for our claim map; AsteroidCatalog unchanged at 61768e0.

New seam opened as rc-200: the quote-snapshot doctrine (quotes.py docstring, spans count==1) says a snapshot is THE FORMAT IS THE QUOTE AS THE SOURCE GAVE IT and that fetches are recorded once; but fuel-2026-10-17.csv was not fetched - its own note says both values were recovered from the economicspace Stage 3 tables, i.e. back-solved — and today's same source disagrees on that session for both tickers (HO=F recorded 4.559800 vs current 4.755300; NG=F recorded 3.13499999 vs current exactly 3.0), in opposite directions, while the directly-recorded fuel-2026-10-26.csv matches today feed bit-for-bit on HO=F/NG=F/CL=F. Divergence is dated and sha-backed; source-revision vs recovery-error cannot be adjudicated without an independent settlement print.

Skip-note for future rounds: the Oct-26 snapshot is proven faithful to Yahoo as of 2026-10-26 - do not re-flag those three values. Remaining launch-row payload-band targets (Soyuz-5 / Long March 12 / Kuaizhou family) still unprobed.

Extracted data: `extracted_data/r257_quote_snapshot_key_numbers.csv`.

## R283 - propellants.csv Iodine row - self-citation contract audit result (rc-226 opened) (2026-10-27)

The row stores a value-bearing price cell, Cost $60/kg., naming no document; CITATIONS.md at spacecost@860bef9 has zero entries for iodine anywhere in the file. The same note attributes the flight record to Rafalskyi et al., Nature 599, 2021 - registered in this repo as rafalskyi_2021_iodine_ep_in_orbit with a hosted CC-BY full text - yet that work likewise has no CITATIONS.md entry. Market context now on file: USGS Mineral Commodity Summaries for iodine (February 2026, newly registered this round, public domain) puts the crude import unit value at an estimated $68 per kilogram for 2025 with a five-year series rising from $32.72 in 2021, and crystal spot prices averaging about $73 per kilogram over the first ten months of 2025 against a $70.24 average for 2024. The stored $60/kg therefore reads as circa-2022 to 2023 market level, roughly 12 percent below the current institutional estimate - a dollar-vintage observation in the rc-168 family, not adjudicated here. Caveat recorded on both key-numbers files: the Rafalskyi paper states only total propellant cost figures (US$60 for iodine at 99.5% purity; US$1,275 of xenon for the same mass) with no mass basis printed anywhere in it and a system total mass including propellant of 1.2 kg, so neither figure converts to a per-kilogram price from that document alone; under any consistent unit-price reading its xenon value contradicts the Xenon row stored $10k/kg by roughly an order of magnitude. Future rounds: do not cite Rafalskyi as a per-kg iodine or xenon price source without resolving this convention question with the owner.

Extracted data: `extracted_data/r283_usgs_iodine_price_key_numbers.csv`.

## R293 - spacecost propellants.csv physics layer, skip-note (2026-10-28)

Recomputed every internal relation in reference/propellants.csv at @860bef9 from raw committed bytes (41 rows x 34 columns, uniform parsed width). Exhaust velocity vs Isp: ve = isp x G0_M_S2 with G0 = 9.80665 holds exactly on every finite row; the code derives the column by construction - each device dict writes exhaust_vel_m_per_s as its Isp times G0_M_S2 - so CSV-vs-code consistency is structural.

The mass-driver row (Mass driver regolith reaction mass) is the single intentional exception: exhaust velocity 3_000 m/s stored as the physical input with isp_vac_s = 306 carrying the code comment "3 km/s slug velocity / g0; see notes", and the CSV note prints verbatim: Isp is a derived equivalence, not a chemistry: a 3 km/s slug velocity is 3,000/9.807 = 306 s. The ratio residual of -0.027 percent against G0 is display rounding on the derived column, documented in code and data; do not open an RC against it.

Cost cross-relations: ref_cost_usd_per_L reproduces ref_cost_usd_per_kg x density_kg_per_L with relative residual identically zero on every row (a literal float product, including the antimatter-catalysed row at 6.25e+16 per kg); trailing cost_usd_per_kg / cost_usd_per_L columns are string-identical duplicates of the ref pair on 41/41 rows (a deliberate legacy mirror); live_cost columns empty at this tip - quotes moved to the v0.14.0 snapshot surface under rc-200; solar-sail, magnetic/electric sail and momentum-exchange tether rows carry inf Isp with nan density by construction in code.

Do not re-sweep unless isp_vac_s, exhaust_vel_m_per_s, density or the cost columns move at a future spacecost tip.

## R301 - rc-200 dated reconfirmation; snapshot-stability proof (2026-10-29)

Fresh chart-API pulls on 2026-10-29 (saved copies, full sha256 in the r301 key-numbers file): HO=F close for 2026-09-28 reads 4.755300045013428 and NG=F reads exactly 3.0 - identical to the R257 pulls, so the divergence from the two back-solved closes in spacecost quotes/fuel-2026-10-17.csv persists on a third calendar day with unchanged magnitudes (-4.11 percent / +4.50 percent). New fact this round: all three closes of fuel-2026-10-26.csv (the 2026-10-23 session) still equal the current feed bit-for-bit six days after recording - once a close is written into a snapshot it never drifts in this source, which weakens a later revision of the Sep-28 rows by the feed as the explanation and strengthens a build-vintage difference: the Stage 3 tables of 2026-10-17 were built from closes that differ from what the feed shows for that date. Adjudication still needs an independent settlement print. Separately, the snapshot integrity mechanism itself checks out at spacecost@860bef9: recomputed sha256 of both quoted CSVs equals their SHA256SUMS lines exactly and no file lacks a line. rc-200 stays open for the owner; nothing in this round changes its status.

Extracted data: `extracted_data/r301_yahoo_quote_reconfirmation_key_numbers.csv`.

## R302 - rc-200 conversion-consistency audit; front-month roll mechanism hypothesis (2026-10-29)

Cross-repo audit of the only remaining degrees of freedom in the back-solve: the $/kg conversions. spacecost units.py has exactly two commits across its whole history (44c5970 extraction 2026-09-07, 500fb66 environments 2026-09-17), both predating the Oct-17 Stage-3 build; COMMODITY_DENSITY_KG_PER_L prints heating_oil 0.845 and natural_gas 0.422, and _per_mmbtu_to_per_kg_ng multiplies by 0.04739 (1 kg LNG about 50 MJ). economicspace@ea28403 (Oct-17, master v1.55.0) pins spacecost v0.12.0 and its modules/transportation.py is a thin adapter that fetches live fuel quotes then merges onto the installed tables - no EC-side density constants exist in that blob. So the conversion applied when the Sep-28 closes were consumed equals the current one, and the R301 back-solve methodology is sound: if Yahoo reported X on Sep-28 the tables must print what X implies - they do not match today feed for Sep-28 while Oct-23 rows match six days on. Mechanism hypothesis (recorded, NOT opened): HO=F and NG=F are continuous front-month futures series; each contract roll re-splices the historical bars Yahoo serves for older dates. A September row has been behind several rolls since; a late-October row behind none yet at check time - which fits an opposite-sign, same-order pair of divergences without any error by either repo. Proving it needs an archived Yahoo response from before the divergence window (none exists here) or CME settlement prints. rc-200 stays open for the owner; recorded closes versus archived bars would settle it outright.

## R304 - spacevalue metals snapshot self-declares recovery; disclosure contrast for the rc-200 trail (2026-10-29)

spacevalue CITATIONS.md at pinned tag v0.2.0 states that its quote file metals-2026-10-07 was not recorded at the time and holds closes recovered exactly from economicspace Stage 2 tables of that date, saying so in its note column. The fuel-side counterpart under rc-200 stamps close_date 2026-09-28 onto back-solved closes; whether that amounts to equivalent disclosure is precisely the open question of rc-200 - recorded here only to note that the sibling package demonstrates an explicit formulation, so the owner can compare wording directly. rc-200 itself untouched per standing rule.

## R305 - spacevalue metals snapshots bit-exact against the live feed; schema asymmetry noted for the rc-200 trail (2026-10-29)

All five forward-recorded Oct-23 closes in metals-2026-10-26.csv (GC=F 4007.89990234375 troy_oz, HG=F 6.47599983215332 lb, PA=F 1046.5999755859375, PL=F 1554.199951171875, SI=F 53.71099853515625 troy_oz) match the live Yahoo chart-API bars bit-for-bit on re-pull, values in extracted_data/r305_metals_snapshot_bit_exact_key_numbers.csv. Combined with the R301 fuel-side result (Oct-23 HO=F and NG=F closes matched exactly six days after recording), the forward-recording mechanism is now proven sound across two packages and eight tickers: snapshots never drift once written, and recorded observations reproduce. The single anomaly anywhere remains that fuel-2026-10-17.csv stamps back-solved Sep-28 values onto close_date 2026-09-28 where the same feed now prints different closes for that date - a divergence specific to derived values, consistent with either front-month roll re-splicing of continuous history or an actual older-date feed revision; adjudication still requires archived feed state (rc-200 untouched per standing rule). Schema asymmetry recorded as fact: spacevalue snapshots separate close_date from recorded_date in two columns while the fuel snapshot schema carries a single date column, so back-solved values there sit in the field that elsewhere means observed observation-date. Also verified this round at pinned tag v0.2.0: README per-destination table reproduces exactly from the delivery chain of spacecost v0.14.0 (all seven destinations to display rounding), SHA256SUMS bidirectionally clean, release assets resolve; post-pin commits on spacevalue main are tests-only tooling and no tag newer than v0.2.0 exists, so the economicspace pin is current.


## R341 - Henry Hub quote heating-value basis (2026-11-03)

`cme_comex_nymex_futures`, NYMEX Chapter 220 PDF p1, 220101,
binds the methane-based Henry Hub grade to the then-effective Sabine
FERC tariff. `sabine_2026_gas_tariff_heating_value`, Section 7.1 v1.0.0
effective March 1, 2026, defines Btu(IT) on printed p2/12 (PDF p16).
Its heating-value definition on printed pp4-5/12 (PDF pp18-19) has
combustion water "condensed to the liquid state": a gross/HHV basis.

`ashrae_2021_fundamentals_fuel_heating_values`, 2021 Fundamentals SI
Chapter 28 Table 3, Methane/CH4 row, gives "55.533" MJ/kg under Higher
Heating Values and "49.997" MJ/kg under Lower Heating Values. The
six-column header and row align in the HTML DOM and online table;
footnote a states 15.6 C, 101.4 kPa, dry. Its Heating Value subsection
defines the condensed-water distinction. `thompson_taylor_2008_nist_sp811_si`,
online Appendix B.8, Btu_IT-to-joule row, gives 1.055056 E+03 J/Btu_IT:
one MMBtu_IT is 1055.056 MJ at the printed precision.

`spacecost_methane_quote_heating_basis_record_2026` reads spacecost
860bef9902aa67fec705875cd52fdb8e6def159f. `units.py` L69-75 multiplies
the USD/MMBtu close by 0.04739 and describes one kg of LNG as about 50 MJ.
The implied 49.99910384 MJ/kg matches the net value, whereas the quote's
tariff uses gross heat. `tests/test_prices.py` L100-110 asserts the same
factor and 50-MJ arithmetic. `prices.py` L113-205 uses this helper for
both live closes and stored snapshots; the only natural-gas proxy row
is methalox. Its fuel mass fraction is 1/(1+3.6), with LOX held at 0.20 USD/kg.

A pure-CH4 gross proxy is 55.533/1055.056 = 0.05263512078979694 MMBtu/kg:
11.06799% above the existing factor, or a 9.96506% shortfall in the current
methane-only price relative to that diagnostic. With the unchanged stored
October 23 NG=F close 2.640000104904175 USD/MMBtu, methane 0.125109604971409
becomes 0.138956724406708 USD/kg; the full blend 0.183719479341611 becomes
0.186729722697110 USD/kg (+1.63850%). The other stored profile changes
the blend 0.188819054249577 to 0.192393718081314 USD/kg (+1.89317%).

Five unit cases and eight original/repeat/factor-only adapter triples
include four positive NG cases and four unchanged zero/missing/wrong-unit/
empty controls. Nine complete builds cover reference and both stored
fuel profiles, each with an exact original repeat and the in-memory factor
diagnostic. The reference profile is wholly identical. Each snapshot
changes four price cells in one methalox row and three cost columns across
2,052 of 84,132 summary rows; the five other tables are identical. All 63 CSV
exports preserve the full missing masks and populated cells on readback;
original repeats preserve dtypes, values and output bytes. Snapshot CSVs
and SHA256SUMS remain byte-identical and their integrity checks pass.

Verdict: `rc-275`, use and document a gross heating-value mass conversion
for the Henry Hub methane proxy, including the test's basis. The numerical
example assumes pure CH4 and the stated reference conditions; it does not
calibrate every gas mixture or delivered LNG, add liquefaction/handling
costs, settle `rc-187` or `rc-200`, or measure a profitability-ranking effect.
Fourteen local blobs match pinned GitHub metadata and all four live main
comparisons are identical to the commits read.
`extracted_data/r341_methane_quote_heating_basis.csv`.
Contract extract: `06_commodity_market_pricing/extracted_data/r341_henry_hub_contract_basis.csv`.

## R374 - USGS 2025 iodine crystal price is above the propellant reference (2026-11-08)

`usgs_mineral_commodity_summaries_2026_iodine`, PDF p. 2, says “spot prices for iodine crystal averaged about $73 per kilogram during the first 10 months of 2025”; it attributes the price to industry publications. PDF p. 1 gives a distinct 2025 estimated crude-iodine import unit value of $68/kg CIF. At spacecost@19e1a31, `reference/propellants.csv`, row `Iodine  (Hall / gridded)`, stores `ref_cost_usd_per_kg=60` and `reference_year=2026`; its note labels the value an estimate, and says Rafalskyi et al.'s US$60 is a total propellant cost with no mass stated. The crystal benchmark is 21.7% above the stored value, but the report does not establish propellant-grade purity or a procurement quote. Verdict: `rc-292` proposes considering ~$73/kg (2025 crystal spot) as the market reference, or retaining $60 only with a stated grade, year and discount basis; no value is changed here. Extracted: `extracted_data/r374_usgs_iodine_reference_price.csv`.

## R428 — Producer iodine sales price cross-check (2026-11-09)

SQM's 2025 Annual Report, p. 111, states average iodine prices reached approximately US$71.7/kg in 2025, 7.4% above 2024. On p. 114 it reports an average annual iodine price of US$72/kg, consistent after rounding, and describes iodine sales as spot orders or supply contracts with periodic price adjustment to prevailing market conditions. Reported 2025 iodine-and-derivatives revenue was US$1,042.8M on 14.5 kt sales; because the segment includes derivatives, its revenue/volume ratio is not treated as a pure iodine transaction price. The approximately $71.7/kg producer benchmark is 19.5% above spacecost@19e1a31's $60/kg iodine propellant reference. SQM is a primary producer source and independently corroborates the USGS $73/kg 2025 crystal-spot benchmark, but its general iodine sales mix does not establish propellant-grade purity, procurement scale, delivery or qualification premiums. rc-292 remains open for a grade and procurement-basis decision; no upstream value is changed. Extracted: `extracted_data/r428_sqm_iodine_producer_price.csv`.

## R392 — DLA technical-argon standard price comparator (2026-11-08)

The DLA FY2026 Aerospace Energy price letter (effective 1 October 2025) lists “ARGON,TECHNICAL” at $1.14/lb (attachment schedule, p. 2), or about $2.51/kg. Spacecost’s Argon (Hall / ion) row at spacecost@19e1a31 uses $10/kg, the midpoint of SETS Space’s quoted $7–15/kg bulk-industrial range. The DLA benchmark is 74.9% below the midpoint and 64.1% below that range’s low end; the schedule also lists liquid argon at $0.65/lb under a separate item.

The price channels and grades are not established as equivalent: DLA’s DoD technical-argon standard may differ in packaging, purity and procurement scope from the SETS bulk-industrial estimate, and liquid argon is not the upstream supercritical storage form. Open `rc-310` to reconcile the $10/kg reference basis; no propellant price is changed. Extracted: `extracted_data/r392_argon_dla_fy2026_price_check.csv`.

## R393 — FY2026 DLA oxygen-price refresh for LOX blends (2026-11-08)

The DLA FY2026 Aerospace Energy schedule (effective 1 October 2025) lists two `PROPELLANT,OXYGEN` NSN pairs at $296.77/TN and $319.64/TN (attachment, p. 2). For the same respective NSN pairs, the FY2025 schedule listed $335.89/TN and $322.28/TN. Using the prior registry’s U.S.-short-ton conversion, the current pair normalizes to about $0.327–$0.352/kg; spacecost’s LOX component is $0.37/kg, the FY2025 higher-price value. One matched NSN pair fell 11.65%, while the other fell 0.82%.

Open `rc-311` to review whether the LOX component and its kerolox, hydrolox, methalox and CO/LOX blend prices should track the newer DLA standard, with the ton definition and procurement basis checked. No component or blend value is changed. Extracted: `extracted_data/r393_lox_dla_fy2026_price_check.csv`.

## R394 — DLA FY2026 RP-1 Bulk price comparator (2026-11-08)

The DLA FY2026 Aerospace Energy schedule (effective 1 October 2025) lists “PROPELLANT,KEROSENE RP-1 Bulk” at $10.62/GL (attachment, p. 2). Using the upstream RP-1 density of 0.810 kg/L and 3.785411784 L per U.S. gallon gives about $3.46/kg. Spacecost’s component price is $2.50/kg; its code comment describes Haltermann Solutions / SpaceInsider as typical $2–3/kg in bulk. The DLA standard is 38.5% above the component point and 15.5% above the comment’s upper end.

DLA’s standard is a forecasted DoD price, and the $2–3/kg comment draws on a commercial supplier and a SpaceInsider table tied to defense moving-average prices; the quote channels and date basis need reconciliation before any update. Open `rc-312` to review the RP-1 component and dependent kerolox / HTP-RP-1 blends. No values are changed. Extracted: `extracted_data/r394_rp1_dla_fy2026_price_check.csv`.

## R398 — Xenon composite-price review signal (2026-11-08)

`epignosis_2026_rare_gas_price_tracker` reports a xenon composite declining from $3,050/kg in January 2026 to $2,650/kg in August 2026 (Monthly Price Data Table, Xenon Composite row). Its “Methodology and Source Note” calls these “directional, analyst-informed estimates rather than transactable market prices” and says costs vary by “purity grade, contract structure, order volume, and delivery region” (web report, lines 63–67). The listed source categories are not itemized citations.

At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/propellants.csv` uses $10,000/kg for Xenon (Hall / ion), citing SETS’s $5,000–$12,000/kg aerospace-grade range and INL’s Q1-2023 $60/L survey. Open `rc-314` to review this dated but non-like-for-like composite against the existing aerospace reference; resolve grade and procurement basis before any update. No price is changed. Extracted: `extracted_data/r398_xenon_composite_price_tracker.csv`.


## R409 - HTP supplier price comparator (2026-11-09)

Epic Aerospace’s official Capabilities page, under “HIGH TEST PEROXIDE,” lists: “98% HTP - Price per Kg | 65 USD” (product-properties block, lines 53–55). The same block gives a 280 kg minimum order and estimated shipping of $3,500–$8,500 (lines 56–57); the price effective date and shipping route/quantity basis are not stated. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/propellants.csv` stores `HTP  (98% peroxide monoprop)` `ref_cost_usd_per_kg=5.0`, with the row note identifying it as an unsourced estimate. The supplier’s $65/kg material quote is 13x that reference, a direct but scope-sensitive review signal; it does not establish delivered cost. **rc-319 remains open** for price-date, order-size and freight reconciliation. Extracted: `extracted_data/r409_epic_htp_supplier_price.csv`.


## R416 — DLA FY2026 MMH/NTO component-price comparison (2026-11-09)

The DLA FY2026 Aerospace Energy schedule, effective 2025-10-01, lists MMH at $219.10/lb and nitrogen tetroxide MON-3 at $95.53/lb (attachment, p. 2). Normalized using 0.45359237 kg/lb, those are about $483.03/kg and $210.61/kg. At spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9, `reference/propellants.csv`, row `MMH / NTO (hypergolic)`, stores $59.5283/kg blend, derived from $100/kg MMH and $35/kg NTO (DOD FY20 standards); the upstream oxidizer/fuel ratio is 1.65. Weighting the DLA component prices at that same ratio gives about $313.41/kg blend, 5.26 times the fallback. DLA prices are DoD standard prices for forecasted requirements, so they are procurement comparators rather than commercial delivered prices.

Open `rc-326` to reconcile the FY2020 fallback basis with the FY2026 DLA standards, including procurement scope and price-year basis, before any change. No upstream value is changed. Extracted: `extracted_data/r416_dla_mmh_nto_price_review.csv`.


## R417 - DLA technical nitrogen comparator for GN2 cold gas (2026-11-09)

The DLA FY2026 Aerospace Energy schedule, effective 2025-10-01, lists "NITROGEN,TECHNICAL" at $0.16/lb (attachment, p. 2). This converts to about $0.353/kg using 0.45359237 kg/lb. At spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9, `reference/propellants.csv`, row `Cold gas (GN2)`, stores $1.00/kg with reference_year 2026. The DLA standard is 64.7% below that point, but its grade, packaging and delivery form are not shown to match high-pressure nitrogen used as propulsion mass.

Open `rc-327` to review the $1/kg reference against the DLA comparator and reconcile procurement, purity and packaging basis before any change. No upstream value is changed. Extracted: `extracted_data/r417_dla_technical_nitrogen_comparator.csv`.


## R426 - DLA FY2026 hydrazine HPH comparator refresh (2026-11-09)

The DLA FY2026 Aerospace Energy schedule lists “PROPELLANT,HYDRAZINE. HPH” at $121.54/lb for NSN 9135012321852 and H70 hydrazine at the same price (attachment, p. 2). The corresponding FY2025 HPH standard was $165.75/lb. Converted at 0.45359237 kg/lb, the DoD comparator moves from $365.42/kg to $267.95/kg, a 26.7% nominal decrease.

At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, the hydrazine row keeps a $75/kg commercial reference from Space Insider and labels DLA pricing as a separate DoD comparison. The FY2026 schedule is for forecasted DoD requirements and does not establish a new commercial quote. Open `rc-336` to decide whether to refresh the note’s government comparator; no price value is changed. Extracted: `extracted_data/r426_hydrazine_dla_fy2026_price_check.csv`.

## R435 - SQM Q2 2026 iodine average price update (2026-11-09)

`sqm_2026_q2_results_presentation_iodine_average_price`, SQM’s 2Q2026 results presentation, slide 6, charts quarterly iodine sales volume and average price. The chart reports $72.3/kg for 1Q2026 and $73.4/kg for 2Q2026, with corresponding sales volumes of 3.8 and 4.1 thousand metric tons. The presentation also says iodine average sales prices were up 3% year-on-year (slide 4).

At `spacecost@19e1a31`, `reference/propellants.csv`, row `Iodine  (Hall / gridded)`, the reference is $60/kg for 2026. SQM’s 2Q average is 22.3% above that figure and 2.4% above SQM’s reported 2025 average of about $71.7/kg. These are producer-reported prices for its broad iodine sales mix; the presentation does not identify propellant-grade purity or procurement terms. The new benchmark strengthens the market-price comparison in `rc-292` but does not establish a grade-adjusted propellant cost. No upstream value is changed. Extracted: `extracted_data/r435_sqm_q2_2026_iodine_average_price.csv`.

## R436 - NASA Glenn xenon purchase: procurement scope and award amount (2026-11-09)

`nasa_glenn_2026_xenon_solicitation_80nssc26933373q`, NASA Glenn's amended SOW dated June 12, 2026, specifies xenon for electric-propulsion testing with purity of at least 99.999%. It asks for all-inclusive pricing, including cylinders and shipping, at 10,000, 15,000 and 20,000 liters (Specifications §1; §2 and Table 1). `highergov_2026_nasa_xenon_award_80nssc26p1064`, the HigherGov federal award record for NASA Shared Services Center purchase order 80NSSC26P1064, reports a fixed-price $117,500 award to Spectech Solutions dated August 4, 2026. The award record does not report the selected quantity.

This procurement is a relevant aerospace-propulsion-grade purchasing example for the $10,000/kg xenon row, but its award total bundles gas, cylinders and shipping, and the accessible award record does not identify the selected quantity. Therefore no unit price is derived. The record adds a high-purity public procurement comparator to `rc-314` but does not settle the $/kg reference or its commercial basis. No upstream value is changed. Extracted: `extracted_data/r436_nasa_xenon_purchase_award_scope.csv`.



## R454 - DLA aerospace schedule currency check (2026-11-09)

DLA Energy’s Standard Prices page lists the current aerospace products standard-price PDF as effective October 1, 2025. The page says it is updated when standard prices are officially changed during a fiscal year; it lists no later aerospace schedule. The FY2026 MMH, MON-3 and technical-nitrogen prices recorded in R416 and R417 therefore remain the latest published DLA aerospace standard-price comparators found for rc-326 and rc-327. This confirms comparator currency, but supplies no FY2027 or commercial price and does not resolve grade, delivery or procurement-scope differences. No upstream value is changed. Extracted: `extracted_data/r454_dla_aerospace_schedule_currency.csv`.


## R706 — Liquid-hydrogen component price basis (2026-11-12)

At `spacecost/propellants.py`, `_COMPONENTS["LH2"].cost_usd_per_kg` is 10.00; its adjacent note says “NASA contract pricing 2024-25, ~$6/kg base + handling overhead” but names no contract or handling amount. The current hydrolox reference row is $1.745714/kg, computed from this input, the $0.37/kg LOX input and O/F=6.

`spaceinsider_rp1_price` reports LH2 at about $6.1/kg on a moving-average U.S. defense-price basis; `dla_energy_aerospace_standard_prices_fy2025` lists “PROPELLANT,HYDROGEN LB $10.69” (~$23.57/kg, computed), a distinct DoD aerospace-standard basis. NASA CR 159163’s escalated $3.32-$4.19/kg 2024 estimate is a plant-gate production cost, not procurement plus handling. These comparators do not establish a matched replacement. `rc-576` requests the contract, dollar year, delivery boundary and handling basis; retain $10/kg pending that review, with no numeric replacement inferred. Extracted: `extracted_data/r706_lh2_component_price_basis.csv`.

## R707 — Water component price basis (2026-11-12)

`spacecost_water_component_price_code_current_2026` records `_COMPONENTS["Water"].cost_usd_per_kg = 2.00` in `spacecost/propellants.py` (line 571). The value feeds the Water electrothermal/resistojet and gridded-ion/ECR `ref_cost_usd_per_kg` rows and the water component of the ALICE blend. The two spacecraft water-propulsion reference rows state `ref_cost_usd_per_kg = 2.0` and `reference_year = 2026`, but their notes cite propulsion performance and applications rather than a water procurement price.

The existing candidates `rc-118` and `rc-378` concern Water resistojet specific impulse; `rc-435` concerns asteroid-water ISRU processing fees. None supports this terrestrial water component price. No propellant-grade water quote or matched delivered-price evidence was identified in this review. `rc-577` requests the source and basis for the $2/kg input; no replacement value is inferred. Extracted: `extracted_data/r707_water_component_price.csv`.


## R759 — Hydrolox tug-propellant worksheet citation gap (2026-11-15)

Economicspace’s current verification-sheet code at `campaign/verification_sheet.py` uses an equality-gated lookup for the current Spacecost Hydrolox row. When that row does not equal the run’s propellant rate, the I15 fallback cites `spacecost/delivery.py`’s `TUG_PROPELLANT_USD_PER_KG` but does not name the frozen Stage 3 table or row; the current check flags I15 = 1.5999999999999999 USD/kg NEED BACKING with “the model’s own constant, with no reference given.”

The frozen `campaign/stage3/spacecost-0.5.0/propellants.csv` Hydrolox row stores 1.5999999999999999 USD/kg and says “LH2 base price $3-6/kg (NASA contracts); bulk-handling overhead lifts effective cost to ~$10/kg.” Spacecost’s current `reference/propellants.csv` Hydrolox row stores 1.7457142857142856 USD/kg with a more detailed but still broad component-price note. `spacecost/delivery.py` retains 1.5999999999999999 as its pre-v0.16.0 compatibility constant. The historic row, the current row and the tug code constant have distinct roles; the historic note does not identify a contract or document the blend calculation.

Open `rc-626` for the missing worksheet citation lineage and historical-price basis; no numeric replacement is inferred. Extracted: `extracted_data/r759_hydrolox_tug_price_worksheet_gap.csv`.

## R761 — Krypton Hall price worksheet citation gap (2026-11-15)

The current economicspace verification-sheet check flags I116=$300/kg NEED BACKING. It reads `campaign/stage3/spacecost-0.5.0/propellants.csv`, where the frozen Krypton (Hall) row stores $300/kg and has no published price source in its note.

Spacecost’s current `reference/propellants.csv` row stores $794/kg and describes it as the geometric centre of a band from bulk krypton near $300/kg to flight-grade quotes beginning at $2,100/kg. `inl_rpt_23_75203_krypton_xenon_recovery_cost_benefit` is cited for the bulk comparator “hover around $1/L” (2023, §1; approximately $267/kg using the row’s 3.75 kg/L density); `sets_space_2024_hall_propellant_prices` is cited for the $2,100-$4,800/kg flight-grade range. The historic $300/kg value and current $794/kg midpoint have different procurement scopes.

Open `rc-630` for the frozen-row citation and version boundary; no numeric replacement is inferred. Extracted: `extracted_data/r761_krypton_hall_historical_price_worksheet_gap.csv`.


## R781 — FEEP indium price basis and worksheet citation gap (2026-11-15; rc-651)

The economicspace Mars verification sheet consumes I73=$250/kg from its frozen Stage 3 FEEP row and flags the input NEED BACKING. The frozen row labels the price reference-year 2026 and price-basis `reference`; Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` repeats $250/kg in `_COMPONENTS["Indium"]` and the FEEP reference row, while the nearby code comment and row notes name no price source.

USGS `usgs_mineral_commodity_summaries_2026_indium` (printed pp. 99–100) gives the annual average U.S. warehouse FOB refined-indium price as $250/kg in 2022, $351/kg in 2024, and $370/kg in 2025e; its footnote specifies 99.99%-minimum purity. The Events section separately reports $390/kg as the estimated 2025 annual average. The $250 value matches the USGS 2022 table entry but does not establish the provenance of the modeled price or a FEEP-specific procurement grade. **Verdict:** citation, date, grade, and procurement basis remain unresolved; keep the modeled value pending a matched source and infer no replacement. `rc-651`. Extracted: `extracted_data/r781_feep_indium_price_basis.csv`.

## R798 — Spacecost gallon and petroleum-barrel conversion citation gap (2026-11-16; rc-668)

Spacecost main at a401930efe30aaad01aafd2b3cb332ad0438c841 defines LITRES_PER_GAL = 3.785_411_784 and LITRES_PER_BBL = 158.987_294_928 in spacecost/units.py:18-19. _per_gal_to_per_kg and _per_bbl_to_per_kg use these factors with fluid density; prices.py:133-137 routes per-gallon and per-barrel quote closes through those helpers. tests/test_prices.py:92-95 checks that a barrel factor equals 42 gallons. CITATIONS.md names NIST SP 811 Appendix B.8 for the methane energy conversion but has no source mapping for these volume factors.

nist_hb133_2026_appendix_e_volume_conversion (Appendix E, p. 248) reports 3.785 411 784 liters per gallon. thompson_taylor_2008_nist_sp811_si (Appendix B.9, Volume table) defines a petroleum barrel as 42 gallons (U.S.). The derived value 42 × 3.785411784 = 158.987294928 L/bbl matches the stored barrel factor. Verdict: both stored factors match the identified units; add the citations beside the constants and in CITATIONS.md. No numeric replacement is inferred. Extracted: extracted_data/r798_unit_conversion_factors.csv.


## R800 — Spacecost live quote density basis (2026-11-16; rc-670, rc-671)

`spacecost_volume_conversion_citation_gap_code_current_2026` records Spacecost main at `a401930efe30aaad01aafd2b3cb332ad0438c841`; its `units.py`, `prices.py` and `CITATIONS.md` snapshot defines `COMMODITY_DENSITY_KG_PER_L` and contains no source mapping for that dictionary. `heating_oil` is 0.845 kg/L; `prices.py` maps `HO=F` per-gallon quotes to that density, converts them to USD/kg, and applies the result to the kerolox fuel blend.

`iea_energy_prices_2022_product_specifications` (p. 146, Product specifications > Oil products) lists “Fuel oil domestique” at 0.845 kg/L in the France household light-fuel-oil column. The table does not state a measurement temperature. `cme_comex_nymex_futures` (NYMEX Rulebook Chapter 150, p. 1, §§150101 and 150102.B–C) identifies HO as NY Harbor ULSD meeting Colonial Pipeline Fungible Grade 62; the contract volume is determined at 60°F and the price is quoted per gallon. The matching number does not establish that the IEA product or temperature basis applies to the Spacecost HO proxy. **Verdict:** open `rc-670` for the matched product and reference-temperature citation; no numeric replacement inferred.

The same dictionary stores `crude_oil=0.870 kg/L` with comment “WTI ~32° API.” Spacecost maps `CL=F` to that density, while `prices.py` calls CL=F a cross-check that “prices nothing.” CME’s NYMEX Light Sweet Crude Oil futures FAQ, contract quality specifications (Gravity item), gives the deliverable WTI range as “Not less than 37 degrees API, nor more than 42 degrees API.” The code names neither a density source nor a reference temperature. **Verdict:** open `rc-671` to cite a temperature-matched WTI density and reconcile the API comment with the contract range; this is diagnostic-only and no propellant-price replacement is inferred. Extracted: `extracted_data/r800_spacecost_quote_density_basis.csv`.


## R802 — Spacecost cryogenic component-density citations (2026-11-16; rc-673, rc-674)

Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841` sets `_COMPONENTS["LCH4"].density_kg_per_L=0.422` in `spacecost/propellants.py:522`. `_blend` calculates the combined density from reciprocal component volumes (`spacecost/propellants.py:407-415`), and the generated methalox row stores `0.8326100293211036 kg/L` (`reference/propellants.csv`, row 4). The component notes identify the LCH4 price basis but no density source or temperature; `CITATIONS.md` has no LCH4-density citation. The frozen economicspace Stage 3 row carries the same combined density, and the verification worksheet derives tank fraction as `tank_kg_per_L / density_kg_per_L` (`campaign/verification_sheet.py:2404-2417`).

IMO Resolution MSC.420(97), Annex 18, Table 3, printed p. 7, lists methane “Liquid density (kg/m³)” as 422.5 and its boiling temperature as 111.6 K; the table identifies ISO Annex A, Table A.3 as the reference and footnote * says the liquid property is at normal boiling point. This is 0.4225 kg/L, 0.0005 kg/L (about 0.12%) above Spacecost's stored component value. The table supports a near-boiling pure-methane reference but does not establish the code's exact temperature, pressure, composition, or rounding convention. **Verdict:** open `rc-673` to cite the LCH4 density with its phase and reference conditions, and reconcile the displayed precision while retaining the existing value pending a matched basis. No numeric replacement is inferred. Extracted: `extracted_data/r802_lch4_density_citation_scope.csv`.

The same IMO table gives hydrogen’s “Liquid density” as 70.8 kg/m³ at 20.3 K, the normal boiling point; this converts exactly to Spacecost’s `LH2=0.0708 kg/L`, which feeds hydrolox density.

NIST S 7101.52 Ver. 3, Appendix B, Table 1, printed p. 17, labels the measurement “Liquid Density (g/L)” and lists oxygen 1,141 g/L at 90.2 K and argon 1,395 g/L at 87.3 K, at sea level (101.325 kPa). The Spacecost component constants are LOX 1.141 kg/L and ArgonLIQ 1.395 kg/L; the first feeds kerolox, hydrolox, methalox, and CO/LOX blend densities, while the second feeds the VASIMR and cryogenic-argon rows. Both values match after unit conversion. **Verdict:** open `rc-674` to cite the source and state the reference conditions beside these component inputs and generated rows; keep the existing values pending confirmation that the model uses the same storage state. No numeric replacement is inferred. Extracted: `extracted_data/r802_cryogen_component_density_citation_scope.csv`.

## R803 — Spacecost storable propellant density citations (2026-11-16; rc-675, rc-676)

Spacecost main a401930efe30aaad01aafd2b3cb332ad0438c841 sets _COMPONENTS["RP-1"].density_kg_per_L=0.810 in spacecost/propellants.py:520 without a density citation. The value feeds kerolox and HTP/RP-1 blend calculations; reference/propellants.csv publishes kerolox density as 1.0152772969374169 kg/L. Spacecost CITATIONS.md names RP-1 price references but no density source. The economicspace verification sheet at e1fee40f41c6778b5e4f8de91acf28ef4c17e6c7 derives tank fraction using tank_kg_per_L / density_kg_per_L (campaign/verification_sheet.py:2404-2417).

DoD Manual 4145.26, Appendix 2 Table AP2.T18, printed p. 214, gives RP-1 as 0.81 kg/L at 20.0°C; the stored 0.810 matches at the source's precision. Verdict: open rc-675 for a direct density citation, reference-condition statement, and source trail through the generated blend rows; no numeric replacement inferred. Extracted: extracted_data/r803_spacecost_storable_propellant_density_citation.csv.

The same table reports “Monomethyl hydrazine” at 0.87, nitrogen tetroxide at 1.45, hydrazine at 1.01, and UDMH at 0.79 kg/L, each at 20.0°C. Spacecost stores MMH 0.870, N2O4 1.450, hydrazine 1.010, and UDMH 0.793 kg/L; the first three match at table precision, while the table does not establish the third decimal of UDMH. These inputs feed MMH/NTO, UDMH/NTO, Aerozine-50/NTO, hydrazine monopropellant, and hydrazine arcjet density rows. The current citation guide lists DoD price references for hypergolic components but no density source. Verdict: open rc-676 to cite the ambient storable-liquid density basis and reconcile UDMH precision before changing any value. No numeric replacement inferred. Extracted: extracted_data/r803_spacecost_storable_propellant_density_citation.csv.


## R804 — Spacecost HTP-98 density citation and reference condition (2026-11-16; rc-677)

Spacecost main a401930efe30aaad01aafd2b3cb332ad0438c841 sets _COMPONENTS["HTP-98"].density_kg_per_L=1.431 in spacecost/propellants.py:567 without a density citation. The input feeds the HTP monopropellant row and the HTP/RP-1 blend; reference/propellants.csv publishes densities of 1.431 kg/L and 1.3058555133079848 kg/L, respectively. CITATIONS.md cites Hitt et al. for HTP impulse but not density.

nasa_ntrs_20030020732_98pct_h2o2_density (Appendix A section 6.2, Table 6.1, printed p. 165) gives “Density of 98 % hydrogen peroxide at different temperatures” and 1,430.9 kg/m3 at 25°C. The surrounding text says the 98% H2O2 property data at 1 atm and ambient temperature are from an FMC Chemicals technical bulletin. The report’s bibliography identifies [29] as C. W. Raleigh, Technical Bulletin 67, Hydrogen Peroxide Physical Properties (FMC Chemicals, 1969; printed p. 213). Converting 1,430.9 kg/m3 gives 1.4309 kg/L, which rounds to Spacecost’s 1.431 kg/L. The report supports a 25°C table match but does not show that Spacecost intended that temperature.

Verdict: open rc-677 to cite the HTP-98 component density and record its reference temperature. The table is secondhand from the FMC bulletin, and the separate RP-1 density condition remains covered by rc-675; neither source independently establishes the HTP/RP-1 mixture basis. Keep the current input pending a matched condition. No numeric replacement inferred. Extracted: extracted_data/r804_htp98_density_reference_conditions.csv.


## R805 — Spacecost Aerozine-50 density citation and selected basis (2026-11-16; rc-678)

Spacecost main a401930efe30aaad01aafd2b3cb332ad0438c841 sets _COMPONENTS[Aerozine50].density_kg_per_L=0.903 in spacecost/propellants.py:566 without a density citation. The component feeds the Aerozine-50/NTO blend; reference/propellants.csv publishes the generated blend density as 1.2064035626535627 kg/L. CITATIONS.md has Aerozine-50 engine-performance sources but no component-density basis.

arnett_1969_nasa_tm_x53859_aerozine50_properties (NASA TM-X-53859, Table 1, printed p. 8) identifies “Aerozine 50 (50/50 UDMH and hydrazine)” and lists specific gravity “0.894 to 0.903 (0.9 @ std. atm)” and liquid density “56.1 lb/cu. ft. @ 77°F.” The stored 0.903 equals the range maximum; the tabulated 77°F density converts to 0.898635795279 kg/L, about 0.486% below the stored value. The report therefore gives a possible basis for 0.903 as the high end of a range and a distinct 77°F density value, but does not show which basis Spacecost intended.

Verdict: open rc-678 to cite the component and document which density point and temperature the model uses. The Aerozine-50/NTO row also depends on N2O4, whose density basis is tracked separately in rc-676. Keep the current input pending the basis check. No numeric replacement inferred. Extracted: extracted_data/r805_aerozine50_density_source_basis.csv.


## R806 — Spacecost supercritical-argon density method and source (2026-11-16; rc-679)

Spacecost main a401930efe30aaad01aafd2b3cb332ad0438c841 sets ArgonSC density to 0.300 kg/L at 18 MPa. Its code comment says a Peng-Robinson calculation at 293.15 K / 18 MPa gives Z=0.919 and 0.321 kg/L, while a generalized-compressibility reading at Tr=1.945 and Pr=3.70 gives Z≈0.99 and 0.298 kg/L; it calls 0.300 “the round figure between them.” The operational Argon Hall row exports 0.300 kg/L, and CITATIONS.md does not name sources for either density method.

tegeler_span_wagner_1999_argon_equation_of_state (Journal of Physical and Chemical Reference Data 28(3), abstract printed p. 779) presents a reference equation of state for argon. The abstract states the density uncertainty is “less than ±0.03%” for pressures up to 30 MPa and temperatures from 235 to 520 K, which includes the code’s 293.15 K / 18 MPa state. The equation-of-state article provides a reference for checking the input but has not yet been used here to calculate a replacement density.

Verdict: open rc-679 to source the methods and document how their results produce the stored round value, or compare the input with the reference EOS at the modeled state. Keep 0.300 kg/L pending that check. No numeric replacement inferred. Extracted: extracted_data/r806_supercritical_argon_density_eos_basis.csv.


## R813 - Krypton supercritical density basis (2026-11-16; rc-686)

Spacecost code source `spacecost_krypton_supercritical_density_code_current_2026` sets `_COMPONENTS["Krypton"]` to 0.550 kg/L at 18.0 MPa (`spacecost/propellants.py:569`); it states no temperature or density reference. The `Krypton (Hall)` output row carries density 0.55 kg/L and tank mass per litre 0.06887755102040816 kg/L. Its note compares 0.55 kg/L supercritical krypton with xenon at 2.0 kg/L and states a 12.5% COPV mass fraction, without a source or temperature for the krypton density.

The source `economicspace_propellant_tank_fraction_sheet_code_current_2026` records verification-sheet input I58 as 0.0688775510204 / 0.55 = 0.125231910946 kg tank per kg propellant. Open rc-585 and rc-586 cover tank mass per volume and storage-class multipliers; rc-679 covers ArgonSC density. None addresses the krypton density state or its reference condition.

**Verdict:** cite the equation-of-state/property basis and state the temperature/pressure condition for 0.550 kg/L, or identify it as an engineering scenario and bracket the dependent tank fraction. Preserve current output pending a matched basis; no replacement inferred. **rc-686**. Extracted: `extracted_data/r813_krypton_supercritical_density_scope.csv`.


## R814 - GN2 supercritical density basis (2026-11-16; rc-687)

Spacecost code source `spacecost_gn2_supercritical_density_code_current_2026` sets `_COMPONENTS["GN2"]` density to 0.250 kg/L at 30.0 MPa (`spacecost/propellants.py:568`); it states no temperature or density source. The `Cold gas (GN2)` row uses the supercritical-gas tank model at 30 MPa, exports tank_kg_per_L=0.11479591836734694 kg/L, and reports a 46% COPV mass fraction without citing the density basis. The implied fraction from the row values is 0.459183673469 kg tank per kg propellant.

Open rc-327 targets the nitrogen price and reference year; rc-586 covers the storage-class tank mass per litre; rc-679 covers ArgonSC density; rc-686 covers Krypton density. None addresses the GN2 density state or its reference temperature.

**Verdict:** cite the equation-of-state/property basis for 0.250 kg/L at 30 MPa and state the temperature, or identify it as an engineering scenario and bracket the dependent tank fraction. Preserve current output pending a matched basis; no replacement inferred. **rc-687**. Extracted: `extracted_data/r814_gn2_supercritical_density_scope.csv`.


## R815 - Xenon supercritical density basis (2026-11-16; rc-688)

Spacecost code source `spacecost_xenon_supercritical_density_code_current_2026` sets `_COMPONENTS["Xenon"]` to 2.000 kg/L at 10.0 MPa (`spacecost/propellants.py:527`). The `Xenon (Hall / ion)` row labels storage supercritical at ambient temperature but states no numeric temperature or density source. The row exports tank_kg_per_L=0.038265306122448974 kg/L and density 2.0 kg/L; their ratio is 0.019132653061 kg tank per kg propellant, matching the code comment's 1.9% comparison.

The row note cites `inl_rpt_23_75203_krypton_xenon_recovery_cost_benefit` for a $60/L to $10,243/kg price conversion "at STP". That citation does not establish the 10 MPa supercritical storage density. Applied rc-186 concerns price attribution; rc-585/rc-586 cover tank mass per litre; rc-679 covers ArgonSC density; rc-686 and rc-687 cover Krypton and GN2 density. None targets Xenon density.

**Verdict:** cite an equation-of-state/property source for 2.000 kg/L at 10 MPa and define the ambient reference temperature, or identify the density as an engineering scenario and bracket its effect on tank fraction. Preserve current output pending a matched basis; no replacement inferred. **rc-688**. Extracted: `extracted_data/r815_xenon_supercritical_density_scope.csv`.


## R816 - Conceptual propellant density and storage-state gaps (2026-11-16; rc-689, rc-690)

The `Direct fusion drive` and `Antimatter-catalysed` rows in Spacecost source `spacecost_concept_propellant_density_code_current_2026` each set `density_kg_per_L=0.100` and use `storage_class="supercritical_gas"` with the 10.0 MPa COPV tank model. The exported rows each carry `tank_kg_per_L=0.038265306122448974` kg/L; divided by the density, this implies 0.382653 kg tank per kg row propellant. Neither density has a cited property source or numeric reference temperature.

The Direct fusion drive note identifies D-He3 / PFRC-2 and Isp context but does not give the blend ratio or storage-density basis. The Antimatter-catalysed note says a few micrograms initiate a much larger microfission charge, without identifying which material the row density represents. Existing rc-575 concerns D-He3 cost and blend mass basis and already calls for gas-density/pressure documentation as a per-litre cost basis; rc-689 separately records how that density sets the COPV tank-mass ratio. Rc-540 concerns antimatter production cost and does not target the microfission-charge density boundary.

**Verdict:** define the composition or mass boundary and storage state for each row, then cite a matched property basis or label the density as a scenario and bracket its effect on tank mass. Preserve current values pending a defined basis; no replacement inferred. **rc-689** (D-He3 density/state); **rc-690** (antimatter propellant boundary/density). Extracted: `extracted_data/r816_concept_propellant_density_scope.csv`.

## R862 — Krypton price worksheet locator check (2026-11-17)

- **economicspace_current_bestcase_verification_sheet_2026**: p. 29 maps I112 to Iodine (Hall / gridded) at $60/kg and I116 to the learning-curve factor, not Krypton price.
- **economicspace_krypton_price_stage3_frozen_row_current_2026**: the frozen `spacecost-0.5.0` Krypton row retains $300/kg without a published price source in its note.
- Verdict: the current sheet no longer selects Krypton price; the historical row remains a procurement-basis gap. Keep **rc-630** open; the current $794/kg midpoint does not supply a like-for-like replacement. Extracted: `extracted_data/r862_krypton_price_current_sheet_locator_check.csv`.

## R967 — ALICE silicate-to-aluminium ISRU processing energy (2026-11-19; rc-827)

Spacecost source `spacecost_alice_isru_processing_energy_gate_current_2026` at main 868f42890ac97ee40a50d79f7b33863046edb0ff sets the ALICE processing-energy mapping to NaN and comments “the metal half has no refining source; gated out” (`spacecost/propellants.py:346`). Its exported row has `isru_feed_kg_per_kg=0.5`, `isru_feed_material=water`, and a blank `isru_processing_wh_per_kg`; the row note calls the feed a placeholder for the water half because metal refining is not modeled (`reference/propellants.csv:42`). The processing-energy gate prevents an unsupported value from entering the default ISRU search. Existing ALICE records cover propulsion performance, component water price, and tank-mass scenarios, not the energy to recover metallic Al from silicate feed.

**Verdict:** Keep NaN and the gate until a sourced or validated Al-recovery energy boundary is available; no numeric replacement inferred. **rc-827**. Extracted: `extracted_data/r967_alice_isru_processing_energy_gap.csv`.

## R978 - Spacecost laser-thermal Isp note mis-scopes its 900 s source (2026-11-19)

- `spacecost_beamed_laser_thermal_isp_citation_gap_code_current_2026`: Spacecost main `868f42890ac97ee40a50d79f7b33863046edb0ff`, `spacecost/propellants.py` lines 2118-2135 sets `isp_vac_s=900` for Beamed laser-thermal (H2) and says Kare's work and a 2022 Mars study put it near 900 s. The Kare work is not identified by title or year; current `CITATIONS.md` section 2 has no Kare or Duplay et al. 2022 entry.
- `duplay_etal_2022_rapid_transit_mars_laser_thermal`: the article abstract (p. 1) states 3000 s; section 3.1 (p. 7) gives a 1000-3000 s performance range and assumes 3000 s for the conceptual design. These are design calculations, not a tested engine. Extracted: `extracted_data/r978_spacecost_laser_thermal_isp_citation_scope.csv`.

**Verdict:** open `rc-842` to add the full Duplay et al. citation, identify the exact Kare source, and correct the source scope. Retain 900 s pending a matched source or an explicit scenario label; no numeric replacement inferred.

## R985 — Spacecost Moran and laser-thermal citations corrected upstream (2026-11-19)

At Spacecost main 5ae7f70855d24c71dc54fc3a916624f325c034e8 (PR #53, 0.18.6), CITATIONS.md section 2 gains `moran_1991_nasa_tm_103730_on_orbit_electrolysis`, and the propellants.py comment gives its 4.41 kWh/kg (Table II) and Mars-scaled 2,790 kW at 378.2 kg/h, noting that the 2 MW at 280 kg/hr pair is not in the report (rc-836). The beamed laser-thermal note labels 900 s a scenario: `duplay_etal_2022_rapid_transit_mars_laser_thermal` assumes 3,000 s and no Kare publication is identified (rc-842). Values unchanged.

Verdict: rc-836, rc-842 closed as applied. Extracted data: none new.

## R990 — Spacecost bottled-gas densities checked against reference equations of state (2026-11-19)

At Spacecost main a6901495d257cbcd018b31e238498c94f301c865 (PR #54, 0.18.7, data contract 1.27.7; notes and comments only), the krypton, nitrogen and xenon rows label their stored densities scenarios with the equation-of-state figure beside them, and the DFD and antimatter rows label 0.100 kg/L a scenario with a tank-fraction bracket (rc-686 to rc-690). `lemmon_span_2006_short_eos_industrial_fluids` (krypton, xenon) and `span_etal_2000_nitrogen_reference_equation_of_state` (nitrogen), as CoolProp 8.0.0 implements them, give at 293.15 K: krypton 0.8724 kg/L at 18 MPa (stored 0.550, +58.6%; the stored figure holds at 369.6 K), nitrogen 0.3024 kg/L at 30 MPa (stored 0.250, +21.0%; 349.6 K), xenon 1.8679 kg/L at 10 MPa (stored 2.000, -6.6%; 284.4 K). Opened value candidates rc-857, rc-858 and rc-859 for the moves, held for owner review.

Verdict: rc-686, rc-687, rc-688, rc-689, rc-690 closed as applied; rc-857, rc-858, rc-859 opened. Extracted data: extracted_data/r990_bottled_gas_density_eos.csv.
