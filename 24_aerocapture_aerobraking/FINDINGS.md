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

## R77 - Cross-references updated (2026-09-27; registry unchanged at 267)

`stackpoole_2013_pica_pica_x_postflight_eval`, listed in the opening block under domain 5, is now in domain 21.

## R79 - First sources: seven NTRS-hosted full texts (2026-09-27; registry 270 -> 277)

All five brief items now have at least one registered source, and the aerobraked row's flight record is in hand. Every PDF was pulled live from ntrs.nasa.gov this round, byte-checked against its NTRS download link, and committed under `full_texts/` (NTRS copyright determinations: GOV_PUBLIC_USE_PERMITTED or PUBLIC_USE_PERMITTED for all seven — see the manifest).

**The flight record (brief item 3).** Long et al. Table 1, read by word coordinates, is now the authoritative three-mission summary in this repo (`extracted_data/r79_mars_aerobraking_flight_records.csv`): MRO aerobraded 431 orbits over 154 days (Apr-Aug 2006), ODY 332 orbits over 76.1 days (~2.5 months, Oct-2001-Jan-2002) and MGS 891 orbits over 299 days as printed against a ~498-day calendar span (Sep-1997-Feb-1999; the phase included pauses — Lyons documents the mid-campaign redesign after a solar-panel yoke broke). p1 of Long et al. is explicit: "MRO was the third JPL mission to use the aerobraking technique at Mars, preceded by MGS in 1997-1999 and ODY in 2001-2002". Lyons (p2 verbatim) supplies the delta-v figure the spacecost note quotes: "atmospheric drag was used to remove about 1200 m/s from the orbits of both MGS and Magellan" — with MGS's period falling 45 h -> 1.89 h and Magellan's 3.26 h -> 1.5 h. **This is rc-053**: spacecost attributes "~1.2 km/s over ~6 months of passes (JPL)" to "Mars Odyssey / MRO", but the number belongs to Magellan/MGS, the named pair omits the first Mars aerobraking mission, and no campaign ran ~6 months (ODY 2.5, MRO 5, MGS as-printed 10). Note that Table 1's ABM delta-v column (19.1 / 26.6 / 32.3 m/s) is the propulsive maneuver cost during aerobraking — none of these sources states a total drag-removed figure for ODY or MRO, so rc-053 keeps the number where it has evidence (Magellan/MGS).

**Aerocapture at Earth (brief items 1 and 2).** The ARRIVAL paper is now the domain's only source on aerocapture AT EARTH: entry at 10.8 km/s (lunar-return option) or ~9.9 km/s (GTO option), both targeting an exit velocity approaching 7.5 km/s in a single pass — i.e. roughly 3.3-3.4 km/s of the arrival energy removed by drag, which is the same order as economicspace's flat `aerocapture_dv_savings_m_s` = 4,000 m/s and consistent with spacecost's "reduces propulsive Δv by ~4 km/s" note on the NEA -> Earth return row. Vehicle: 1.1-m-diameter 70-degree sphere-cone aeroshell inside a 255 kg vehicle+payload MPV; C-PICA frontbody sized to 4.8 cm (GTO) / 5.4 cm (lunar return) at the nose, aftbody areal densities MERINO 2.55 vs C-PICA 6.5 kg/m^2. The flat `heat_shield_frac_of_payload` = 0.15 cell is NOT yet testable: ARRIVAL states thickness and areal density but no total TPS mass — that extraction (or a companion paper with the mass budget) is the next step for that cell.

**Smallsat design point at Venus.** Lugo et al.: 1 m / 150 kg capsule, 60-degree sphere-cone shield, entry 11 km/s FPA -5 deg at 150 km to a 500-km apoapsis; NPCG vs FNPAG guidance compared with 8,000-sample Monte Carlos. Useful as the smallsat end of the mass range for any future heat-shield-vs-payload scaling cell (domain 21 owns that pricing).

**Aerobraking economics.** The Hanna preprint (registered T2 with an explicit not-peer-reviewed caveat) carries the first registered number here: a 1,000 kg class spacecraft on a Delta-class booster "saves 90% of the post-MOI fuel otherwise required to circularize" by aerobraking. Dauro's 1987 MSFC paper is context-only — the pre-flight principles reference covering orbital capture on return to Earth; its scan OCR is garbled and no number was extracted from it.

**Gaps that remain.** (a) Total drag-removed delta-v for ODY and MRO specifically — not stated in any of these seven; (b) ARRIVAL total TPS mass, needed to test the 15% heat-shield fraction; (c) corridor-width / peak-deceleration-vs-v_inf curves as functions of entry speed (ARRIVAL's trajectory space is a figure, not tabulated); (d) MGS's published aerobraking overview (Lyons et al., J. Spacecraft & Rockets 1999/2000 — Crossref shows the companion journal papers exist; pull them if ODY/MRO totals stay unfindable).

## R114 - Aerocapture mass savings, Earth-return entry and Venus insertion (2026-10-04; +6 sources, T1x1, T2x5)

Six sources. `munk_kremic_2008_aerocapture_summary_and_risk_discussion_opag`: the Venus systems-analysis case needs 3,975 m/s all-propulsive and aerocapture provides 3,885 m/s (97.7%), and its mission-set table shows aerocapture raising deliverable mass 79% at Venus (4.6 km/s insertion) and 15% at Mars. `muth_2000_earth_return_aerocapture_transhab_ellipsled`: a nominal 0.7 degree corridor for entry speeds up to 14.0 km/s, the Earth-return case. `wright_2006_mars_aerocapture_systems_study_tm_2006_214522`: substantial mass savings for sample-return and large delivered masses, and a carbon-carbon heat shield 30-40% lighter than Genesis's. `cassell_2019_aeroassist_technologies_small_satellite_missions` lists small sample-return capsules at about 11-12.8 km/s. `girija_2023_aerocapture_design_reference_missions_venus_to_neptune` (arXiv abstract) has an Earth reference mission and `braun_powell_lyne_1992_earth_aerobraking_strategies_manned_return_from_mars` is title-only; neither delta-v saving is yet known. The owner's list quoted '1500 vs 5500 m/s' and '2300 m/s' for Earth return and '3-4x launch mass' for Mars; none of those figures was found in the passages read.

The NTRS 20000102372 record and its PDF on the list are one source, and NTRS 20110014670 (Woodcock & Dankanich, JPC 2006) is a second record of an already registered paper. The Delta-v budget Wikipedia page was rejected (Round 114 log entry). No revision candidate.

Extracted data: `extracted_data/r114_gr_links_key_numbers.csv`.

## R119 - girija_2023 pulled live from arXiv and hosted, CC BY-SA 4.0 (2026-10-05; queue -1)

**girija_2023_aerocapture_design_reference_missions_venus_to_neptune [T2]** - re-classed registered_not_pulled -> full_text_hosted. PDF pulled live via export.arxiv.org/pdf/2308.10384v1; committed to full_texts/girija_2023_aerocapture_design_reference_missions_arxiv2308.10384.pdf (1,617,130 B sha256=d2e4a37e0908361e12f3f6c92df9652af16fa14dcd8b9fc15ae592160e3d87c3). 12 pages, no in-file copyright statement so the abs-page CC BY-SA 4.0 governs (checked live). Verbatim: "Aerocapture is applicable to all atmosphere-bearing destinations with the exception of Jupiter and Saturn, whose extreme entry conditions make aerocapture infeasible." - the design reference missions at Venus/Earth/Mars/Titan/Uranus/Neptune compiled with AMAT now sit behind d24's aerocapture context rows (no numeric re-pin).
