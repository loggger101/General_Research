# Domain 24 — Aerocapture & aerobraking

Backings: economicspace `modules/calc.py` aero-assisted return model (`use_aerocapture_return`, `aerocapture_dv_savings_m_s`, `DV_AEROBRAKE_TRIM_KM_S`, `DV_GEO_AEROCAPTURE_ARRIVAL_KM_S` and the `aero_allowed` flag per destination) and spacecost `reference/delta_v_segments.csv` rows `NEA → Earth return (aerocap)` and `NEA → LEO delivery (aerobraked)`.

Created in Round 76 (2026-09-27). Blocks are appended one per round, newest last.

## R76 - Domain opened (2026-09-27; no sources yet)

Aero-assisted returns are offered at earth_surface, LEO, GEO, Mars orbit and Mars surface, and `campaign/results.csv` reports an `aerocapture_share` for every cell. No registry source covers aerocapture at Earth; domain 3 holds only DRA 5.0's Mars aerocapture-versus-propulsive capture figures. Values below were read from economicspace@1f470d4 and spacecost@e831245 (unchanged since R73). No source was sought; the table is the brief for the first research round here.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` LEO return (`ret_leo_aero`) | 0.100 km/s `DV_AEROBRAKE_TRIM_KM_S`, whatever the arrival v_inf | "At LEO drag can do the whole job and the propulsive residue is 100 m/s" |
| `delta_v_segments.csv` `NEA → LEO delivery (aerobraked)` | 100 m/s | aerocapture into a high ellipse, then multi-pass aerobraking; "Mars Odyssey / MRO flew this for real, saving ~1.2 km/s over ~6 months of passes (JPL)" |
| `delta_v_segments.csv` `NEA → Earth return (aerocap)` | 1,500 m/s against 5,500 propulsive | "Aerocapture reduces propulsive Δv by ~4 km/s"; no source |
| `calc.py` GEO arrival by aerocapture | 1.737 km/s at every arrival speed | "Drag removes the arrival energy whatever it was, so this is FLAT in v_infinity" |
| `calc.py` Mars 1-sol orbit, aero leg | charged the Earth trim, 0.100 km/s | upstream calls it conservative against a computed ~12 m/s raise |
| `calc.py` `aerocapture_dv_savings_m_s` | 4,000 m/s, used when a body's elements are unusable | none stated |
| `calc.py` `heat_shield_frac_of_payload` | 0.15 of returned payload (a domain 21 cell) | none stated |

**What a source has to supply.**

- Aerocapture feasibility at Earth and Mars for the arrival speeds the pipeline produces: corridor width, peak heating and deceleration as a function of v_inf, and whether an upper limit on entry speed applies.
- How heat-shield mass scales with entry speed and payload mass, to test the flat 15% fraction.
- Flight records of aerobraking campaigns (passes, duration, delta-v saved) that separate aerobraking after a propulsive capture from aerocapture itself. The aerobraked row cites Odyssey and MRO; a source should confirm which of the two those missions flew.

**Already registered in other domains.** These ids stay where they are; cite them from here by id.

- `dra5_2009_human_exploration_of_mars` (domain 3): Mars cargo aerocapture-versus-propulsive capture delta-v.
- `stackpoole_2013_pica_pica_x_postflight_eval` (domain 5): TPS flight heritage.
- `edquist_2022_mars2020_aerothermal_entry_masses` (domain 9): Mars entry aerothermal environments.

**Boundary.** Domain 3 holds the delta-v table as a whole and the propulsive alternatives; domain 9 holds the delivery-chain mass fractions and Mars EDL survival; domain 21 prices and sizes the heat shield. This domain holds whether the aero-assist works at the speeds and masses the pipeline assumes, and what delta-v and time it saves.
