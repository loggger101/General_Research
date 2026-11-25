# Domain 24 — Aerocapture & aerobraking

Backings: economicspace `modules/calc.py` aero-assisted return model (`use_aerocapture_return`, `aerocapture_dv_savings_m_s`, `DV_AEROBRAKE_TRIM_KM_S`, `DV_GEO_AEROCAPTURE_ARRIVAL_KM_S` and the `aero_allowed` flag per destination) and spacecost `reference/delta_v_segments.csv` rows `NEA → Earth return (aerocap)` and `NEA → LEO delivery (aerobraked)`.

Created in Round 76 (2026-09-27). Blocks are appended one per round, newest last.

## R76 - Domain opened (2026-09-27; no sources yet)

Aero-assisted returns are offered at earth_surface, LEO, GEO, Mars orbit and Mars surface, and `campaign/results.csv` reports an `aerocapture_share` per cell. Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `calc.py` LEO return (`ret_leo_aero`) | 0.100 km/s `DV_AEROBRAKE_TRIM_KM_S`, whatever the arrival v_inf | "At LEO drag can do the whole job and the propulsive residue is 100 m/s" |
| `delta_v_segments.csv` `NEA → LEO delivery (aerobraked)` | 100 m/s | aerocapture then multi-pass aerobraking; "Mars Odyssey / MRO flew this for real, saving ~1.2 km/s over ~6 months of passes (JPL)" |
| `delta_v_segments.csv` `NEA → Earth return (aerocap)` | 1,500 m/s against 5,500 propulsive | "Aerocapture reduces propulsive Δv by ~4 km/s"; no source |
| `calc.py` GEO arrival by aerocapture | 1.737 km/s at every arrival speed | "Drag removes the arrival energy whatever it was, so this is FLAT in v_infinity" |
| `calc.py` Mars 1-sol orbit, aero leg | charged the Earth trim, 0.100 km/s | upstream calls it conservative against a computed ~12 m/s raise |
| `calc.py` `aerocapture_dv_savings_m_s` | 4,000 m/s, used when a body's elements are unusable | none stated |
| `calc.py` `heat_shield_frac_of_payload` | 0.15 of returned payload (a domain 21 cell) | none stated |

**What a source has to supply:** aerocapture feasibility at Earth and Mars at the pipeline's arrival speeds (corridor width, peak heating and deceleration vs v_inf, any entry-speed limit); heat-shield mass scaling with entry speed and payload; flight records of aerobraking campaigns that separate aerobraking after propulsive capture from aerocapture itself.

**Also relevant, registered elsewhere:** `dra5_2009_human_exploration_of_mars` (d03), `stackpoole_2013_pica_pica_x_postflight_eval` (d21), `edquist_2022_mars2020_aerothermal_entry_masses` (d09).

**Boundary:** domain 3 holds the delta-v table and propulsive alternatives; domain 9 delivery fractions and Mars EDL; domain 21 prices and sizes the heat shield. This domain holds whether the aero-assist works at the assumed speeds and masses, and what it saves.

## R79 - First sources: seven NTRS papers, hosted (2026-09-27)

**Flight record** (Long et al. Table 1 by word coordinates; `extracted_data/r79_mars_aerobraking_flight_records.csv`): MRO 431 orbits over 154 days (Apr-Aug 2006); ODY 332 orbits over 76.1 days (Oct 2001-Jan 2002); MGS 891 orbits over 299 days as printed, across a ~498-day span with pauses (Sep 1997-Feb 1999). Long p1: "MRO was the third JPL mission to use the aerobraking technique at Mars, preceded by MGS in 1997-1999 and ODY in 2001-2002". Lyons p2: "atmospheric drag was used to remove about 1200 m/s from the orbits of both MGS and Magellan" (MGS period 45 h -> 1.89 h; Magellan 3.26 h -> 1.5 h). **rc-053:** spacecost credits "~1.2 km/s over ~6 months" to Odyssey/MRO, but the figure is Magellan's and MGS's and no campaign ran ~6 months (ODY 2.5, MRO 5, MGS 10). Table 1's ABM delta-v (19.1 / 26.6 / 32.3 m/s) is propulsive cost during aerobraking; no source states a drag-removed total for ODY or MRO.

**Aerocapture at Earth** (ARRIVAL, Morgan et al.): entry 10.8 km/s (lunar return) or ~9.9 km/s (GTO), exit approaching 7.5 km/s in one pass, so ~3.3-3.4 km/s removed, the same order as the flat 4,000 m/s saving and spacecost's "~4 km/s". Vehicle: 1.1 m 70-degree sphere-cone in a 255 kg MPV; C-PICA nose 4.8 cm (GTO) / 5.4 cm (lunar return); aftbody MERINO 2.55 vs C-PICA 6.5 kg/m^2. No total TPS mass, so the 15% heat-shield fraction is untested. `extracted_data/r79_aerocapture_design_points_and_savings.csv`.

**Others:** Lugo et al. smallsat at Venus (1 m / 150 kg, 60-degree shield, entry 11 km/s at FPA -5 deg from 150 km to a 500 km apoapsis); the Hanna preprint (not peer reviewed): aerobraking a 1,000 kg spacecraft "saves 90% of the post-MOI fuel otherwise required to circularize"; Dauro 1987 (context only; scan OCR garbled).

**Open:** drag-removed delta-v for ODY and MRO; ARRIVAL total TPS mass; corridor and deceleration vs entry speed (a figure, not a table); the Lyons et al. MGS journal papers.

## R114 - Aerocapture savings, Earth-return entry, Venus insertion (2026-10-04)

- `munk_kremic_2008_aerocapture_summary_and_risk_discussion_opag`: Venus needs 3,975 m/s all-propulsive and aerocapture supplies 3,885 m/s (97.7%); deliverable mass +79% at Venus (4.6 km/s insertion), +15% at Mars.
- `muth_2000_earth_return_aerocapture_transhab_ellipsled`: nominal 0.7 degree corridor for entry up to 14.0 km/s (Earth return).
- `wright_2006_mars_aerocapture_systems_study_tm_2006_214522`: substantial savings for sample return and large masses; carbon-carbon shield 30-40% lighter than Genesis's.
- `cassell_2019_aeroassist_technologies_small_satellite_missions`: small sample-return capsules at about 11-12.8 km/s.
- `girija_2023_aerocapture_design_reference_missions_venus_to_neptune` and `braun_powell_lyne_1992_earth_aerobraking_strategies_manned_return_from_mars`: savings not yet read.

The owner's list quoted '1500 vs 5500 m/s', '2300 m/s' and '3-4x launch mass'; none was found in the passages read. Two list links are not new sources: NTRS 20000102372 and its PDF are one record, and NTRS 20110014670 (Woodcock & Dankanich, JPC 2006) is a second record of an already registered paper. `extracted_data/r114_gr_links_key_numbers.csv`. No candidate.

## R119 - girija_2023_aerocapture_design_reference_missions_venus_to_neptune hosted (CC BY-SA 4.0; 2026-10-05)

Hosted as full_texts/girija_2023_aerocapture_design_reference_missions_arxiv2308.10384.pdf. "Aerocapture is applicable to all atmosphere-bearing destinations with the exception of Jupiter and Saturn, whose extreme entry conditions make aerocapture infeasible." Reference missions at Venus, Earth, Mars, Titan, Uranus and Neptune (AMAT). Context only.

## R157 - Peer-reviewed Mars-orbit aerocapture trade (2026-10-12)

**fraysse_powell_rousseau_striepe_2000_msr_orbiter_aerocapture_iac** (IAF-00-A.6.05, 51st IAC, Rio de Janeiro, Oct 2000; NTRS 20010007232; IAF copyright, so read, not hosted). For a 3.2 km/s arrival, propulsive capture needs "generally greater than 1.5 km/s to reach the desired apoapsis", while aerocapture "reduces the total mass requirement by -45% for the same payload". Target 1400 +/- 100 km x 250 km at 45 deg; corridor ~1.2 deg (FPA -10.5 deg); periapsis raised +165 then +250 km. The PDF header's "Oct, 2001" is an OCR artefact. It measures Mars MOI, not the NEA-to-Earth cell, whose ~4 km/s stays unsourced. `extracted_data/r157_msr_orbiter_aerocapture_key_numbers.csv`.

## R158 - ARRIVAL programme decks (2026-10-12)

**dutta_et_al_2026_aerocapture_earth_demonstration_design_scitech** (SciTech 2026) and **dutta_2024_aerocapture_demo_mission_at_earth_pesto** (PESTO, 2024-10-23), hosted. GTO (~9.8-9.9 km/s) and lunar-return (10.8 km/s) entries exit at ~7.4-7.5 km/s in one pass, dissipating 2.4 and 3.2 km/s (`morgan_2026_arrival_earth_aerocapture_tps`). "Can reduce necessary propellant – 50-80% more useful mass on-orbit depending on the orbit" against a propulsive baseline that "(requires ΔV of 1-2 km/s)"; PESTO: "increase on-orbit mass by 40%", "reduce trip time by 3-5 years", "99%+ capture success rate"; GTO design point 9.8 km/s at 125 km, ~400 W/cm2, ~4.5 g, ~30 hours. NEA returns at ~9-12 km/s fall in this band; the propulsive residue brackets the 1,500 m/s aero row from below. No re-pin. `extracted_data/r158_arrival_earth_demo_key_numbers.csv`.

## R375 - NASA NEO-return chart does not support the row's stated 4 km/s saving (2026-11-08)

`nasa_ispt_2010_aerocapture_discovery_mission_briefing`, PDF p. 12, chart “Examples for Circular Orbit Insertion,” places the Mars Return / NEO Return marker at approximately 4–5 km/s on the propulsive ΔV x-axis; its y-axis is initial/final mass ratio, and the aerocapture line near 1–2 is that ratio, not ΔV. At spacecost@19e1a31, `reference/delta_v_segments.csv`, row `NEA → Earth return (aerocap)`, stores 1,500 m/s and says aerocapture reduces propulsive ΔV by about 4 km/s, implying a 5,500 m/s baseline if combined arithmetically. NASA's chart is a broad circular-insertion class marker, not a trajectory-matched budget for this row, and gives no aerocapture ΔV residual. Verdict: `rc-293` proposes qualifying or removing the unsourced savings figure until the target orbit and return trajectory are specified; the 1,500 m/s value remains unchallenged. Extracted: `extracted_data/r375_nasa_2010_neoreturn_aerocapture_chart.csv`.

## R564 — Aerocapture saving claim removed pending a defined return trajectory (2026-11-10)

NASA ISPT 2010, chart “Examples for Circular Orbit Insertion” (p. 12), gives an approximately 4–5 km/s all-propulsive Mars/NEO return marker, not an aerocapture ΔV residual. Spacecost@d3e594fe0968eeaee4f2c02dd2c76334eab8bb2c removes the unsourced ~4 km/s saving from the 1,500 m/s aerocapture row note; the value remains unchanged. `rc-293` is applied. Extracted: `extracted_data/r375_nasa_2010_neoreturn_aerocapture_chart.csv`.

## R822 — NEA Earth-return aerocapture residual remains a placeholder (2026-11-16)

At Spacecost main `a401930efe30aaad01aafd2b3cb332ad0438c841`, the `NEA → Earth return (aerocap)` row stores 1,500 m/s and says the residual is unsourced and the endpoint orbit is undefined. **nasa_ispt_2010_aerocapture_discovery_mission_briefing** places Mars/NEO return at approximately 4–5 km/s on its all-propulsive circular-insertion chart (PDF p. 12); it gives no aerocapture residual. **dutta_et_al_2026_aerocapture_earth_demonstration_design_scitech** says fully-propulsive insertion “requires ΔV of 1–2 km/s” (p. 3), a program comparator rather than the NEA row’s post-aerocapture value. Verdict: open **rc-694** for the distinct 1,500 m/s value/endpoint citation gap. Existing **rc-293** corrected the note, and **rc-519** tracks Economicspace’s separate fallback; no numeric replacement inferred. Extracted: `extracted_data/r822_nea_earth_aerocapture_residual_basis.csv`.

## R1076 — Mars depot capture heritage and periapsis-raise budget (2026-11-24)

- economicspace_mars_orbit_aerocapture_heritage_and_trim_code_2026 records the Economicspace Mars depot comment “Odyssey and MRO flew exactly this” for direct aerocapture into a one-sol orbit. jpl_2001_odyssey_orbit_insertion_status, 23 October 2001 flight status, records Odyssey “fired its main engine” for capture. taylor_lee_shambayati_2006_mro_telecommunications, section 1.3.3, records MRO's main-thruster burn of about 27 minutes and about 35 hours for the initial orbit. long_2007_mro_aerobraking_daily_ops, p. 2 Table 1, gives subsequent aerobraking campaigns of 76.1 days for Odyssey and 154 days for MRO. **rc-983** records the flight-sequence attribution.
- economicspace_mars_orbit_aerocapture_heritage_and_trim_code_2026 records 100 m/s for the Mars-orbit worksheet input labelled “periapsis raise after aerocapture,” with an Earth aerobrake reference. polsgrove_etal_2016_mars_lander_aerocapture_periapsis_raise, aerocapture sequence, gives a “change in velocity of 15 m/s” to raise periapsis to about 250 km at 33,800 km apoapsis altitude. cerimele_etal_2017_mars_aerocapture_onesol_cleanup, p. 9 section 2, targets 250 × 33,793 km and gives a “40 m/s” post-aerocapture cleanup budget from its Monte Carlo assessment. Holding apoapsis fixed, ideal 50, 100 and 150 km initial periapses give 11.53, 8.61 and 5.71 m/s to reach 250 km. The pinned transfer function drops 60 m/s in a 40 m/s sensitivity. **rc-984** records the Mars-specific orbit and cleanup boundary.

Extracted data in extracted_data/r1076_mars_orbit_aerocapture_heritage_and_trim.csv.

## R1077 — Mars option arrival excess and heat-shield basis

- `economicspace_mars_arrival_excess_and_tps_basis_code_2026` — Economicspace `modules/calc.py` lines 3255–3260 describe `v_inf` as “arrival hyperbolic excess back at Earth.” Lines 3673–3678 select the Mars delta-v but copy that Earth value into `v_inf_km_s` for both Mars destinations. The verification worksheet lines 2433–2436 use `v_inf_mars`. Circular coplanar fixtures at 1.1 and 2.5 AU emit 0.701 and 5.815 km/s for either Mars destination, compared with Mars excesses of 2.034 and 2.769 km/s. Verdict: destination mismatch in option metadata (rc-985).
- `economicspace_mars_arrival_excess_and_tps_basis_code_2026` — Economicspace applies the config's 0.15 kg/kg to Mars surface and orbit aerocapture (lines 1041–1045 and 3689–3692). Line 7774 multiplies it by payload, return dry mass and carried electric-propulsion propellant. The worksheet's “heat shield per kg of returned stack” cites the config (lines 3136–3144).
- `cerimele_etal_2017_mars_aerocapture_onesol_cleanup` — Printed p. 20 Table 4 lists “TPS” of 3,032 kg and “Inert Mass” of 46,736 kg for a vehicle that aerocaptures and subsequently enters. Its TPS is 6.94% of inert mass less TPS. Verdict: the common Mars allowance lacks a Mars vehicle and trajectory basis (rc-986). The design comparison uses its own inert-mass denominator.
- Extracted data: `extracted_data/r1077_mars_arrival_excess_and_tps_basis.csv`.
