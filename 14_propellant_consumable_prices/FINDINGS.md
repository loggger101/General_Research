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
