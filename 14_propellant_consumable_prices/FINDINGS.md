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
