# Domain 14 — Propellant & consumable prices

Backings: spacecost `reference/propellants.csv` `ref_cost_usd_per_kg` and the component prices in the comment block above the combined rows in `spacecost/propellants.py`.

Created in Round 74 (2026-09-27). Blocks are appended one per round, newest last.

## R74 - Upstream citations registered (2026-09-27; +8 sources, T3x1, T4x7; nothing extracted)

Sources the upstream repos cite that this registry did not have, found by reading every per-row `notes` field, code comment and CITATIONS.md in AsteroidCatalog@852bf69, spacecost@e831245 and economicspace@1f470d4. Each is `registered_not_pulled`: its DOI was checked against Crossref, or its landing page against a live request from this machine, and the result is recorded in the row. No full text was sought and no number was extracted; the rows are the queue for a later extraction round.

- `dla_energy_aerospace_standard_prices_fy2020` (T3): propellants.csv ref_cost for hydrazine, MMH and N2O4 (and every combined row built from them).
- `sets_space_2024_hall_propellant_prices` (T4): propellants.csv xenon and argon ref_cost.
- `mobius_2024_fueling_starships_methane` (T4): propellants.csv LCH4 component price behind the methalox row.
- `haltermann_solutions_rp1` (T4): propellants.csv RP-1 component price behind the kerolox row.
- `spaceinsider_rp1_price` (T4): propellants.csv RP-1 component price behind the kerolox row.
- `evonik_peroxide_propulsion_htp_quotes_2024` (T4): propellants.csv HTP and HTP/RP-1 ref_cost.
- `efc_gases_xenon_krypton_space_propulsion` (T4): propellants.csv xenon ref_cost ($10k/kg "2023 EFC reference").
- `aqua_calc_lox_bulk_price` (T4): propellants.csv LOX component price behind every LOX bipropellant row.
## R100 - First institutional anchors for propellant & consumable prices (2026-10-02; +2 sources T2x1/T3x1, both hosted; 1 extraction CSV; rc-059 opened)

All three upstream repos were re-swept at their current HEADs first and carried no new institutional claims (economicspace@29a0309 = internal model docs only; AsteroidCatalog #17/#18 cite Keil/Mittlefehldt, already registered), so this round pivoted to the thinnest domain: d14 had 8 grey-source rows and zero verified or hosted sources. Both new sources were pulled from this machine, read in full, and committed.

- `inl_rpt_23_75203_krypton_xenon_recovery_cost_benefit` [T2, full_text_hosted] - INL/RPT-23-75203 (Sept 2023), Idaho National Laboratory + PNNL for DOE Systems Analysis & Integration; OSTI record 2377416. p.2 carries the standard U.S.-government-work disclaimer, so it is public domain and hostable. Verbatim: 'The market survey found that prices for Kr and Xe tend to hover around $1/L and $60/L, respectively.' (Sec.1) and 'in the first quarter of 2023, Xe was sold for around $60/L compared to Kr which was trading at approximately $1/L (Wang 2023)' (Sec.2). Table 3 per-unit capture costs: Xe $71.50 / $101.31 / $131.13 per L; Kr $830.15 / $1,176.34 / $1,522.52 per L (low/mid/high at a 300 MTHM/yr plant) - these are institutional capture costs from aqueous reprocessing, NOT market prices, and the report says so explicitly for Kr ('far exceeds the range of market prices').
- `iea_global_hydrogen_review_2024` [T3, full_text_hosted] - IEA Global Hydrogen Review 2024 (published 02 October 2024), 'IEA. CC BY 4.0.' on every page; first institutional LH2 production-cost source for the hydrolox ($1.60/kg) and $10/kg NTP/NEP/solar-thermal cells. The cost figures sit in vector charts whose text layer carries only axis labels (USD/kg H2), so this is a Context-only row: extraction of chart values is the follow-up step.

**Krypton / xenon consistency check** (STP-gas basis, 22.414 L/mol at 0 C/1 atm): Xe $60/L = $10,243/kg vs upstream's $10k/kg (-2.4%); Kr ~$1/L = ~$267/kg vs upstream's ~$300/kg (+12%). Both upstream cells sit inside the institutional figure, so no re-pin for xenon; krypton is different because SETS Space 2024 (the same source upstream cites for Xe and Ar) gives 'krypton can cost $2,100-$4,800' per kg - roughly 8-18x the INL-derived bulk figure, plausibly aerospace-grade/small-lot pricing vs bulk industrial STP gas. The Krypton row's notes cite no source at all. **rc-059 opened** (value): record both anchors, flag the segment ambiguity for a user decision; no re-pin proposed.

**Iodine consistency anchor** (no new registration - both volumes already hosted in domain 6): USGS MCS iodine chapters give import CIF unit values of $59/kg (2024 actual, MCS 2025) and $68/kg (2025e, MCS 2026), series 31.57 / 32.72 / 45.81 / 61.55 / 61.84 / 68 across 2020-2025e - upstream's $60/kg iodine cell sits between the two most recent actuals, within ~12%. Consistency anchor only; no re-pin.

**Dead-source findings recorded in the rows**: peroxidepropulsion.com (Evonik HTP ~$5/kg quote) has been hijacked - it now serves casino/baby-products spam and the original quote is gone, so that upstream citation points to a dead source; DLA Aerospace Standard Prices FY20/FY24/FY25 all still answer HTTP 403 from this machine (bot protection) with web.archive.org DNS-blocked here; EFC Gases, Haltermann Solutions and SpaceInsider pages answer 200 but carry no $ figures in static HTML (quote-request forms / nav only), so upstream's RP-1 and '$10k/kg 2023 EFC reference' citations are not verifiable from the live pages; Mobius Substack body is client-side rendered, leaving the ~$400/tonne LCH4 claim unverifiable. `sets_space_2024_hall_propellant_prices` was read in full and re-classed to verified_live_not_pulled with its three price ranges extracted into `extracted_data/r100_noble_gas_price_key_numbers.csv`.
