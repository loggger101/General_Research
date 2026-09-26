# Domain 11 — Spacecraft power & electric propulsion

Institutional ground truth for the power + EP rows of `spacecost/reference/operational_costs.csv`.

## R66 — Domain stood up (+4 T2, all hosted)

**Targets** (re-read fresh from spacecost/reference/operational_costs.csv this round): 'Electric propulsion efficiency' 0.6 [0.45-0.72]; 'Electric thruster + PPU specific mass' 8 kg/kW [5-15] (note: NEXT-C ~7, Gateway AEPS similar class); 'Power processing unit specific mass' 4.7 kg/kW; 'RTG specific power' 5.0 W/kg [2.4-5.5] (notes cite GPHS 5.2 + MMRTG 110 We/45 kg = 2.4); 'Power system specific mass' 60 W/kg [30-150] (note cites ROSA/iROSA ~150 at the wing).

### thomas_2025_advanced_next_iepc — Advanced NEXT, IEPC-2025
- p4 verbatim: "6.0 A Beam Current; 1200 V Beam PS Voltage Characteristics (Est's): 8.2 kW; ~3,400 sec Isp; ~330 mN, F/P = 40 mN/kW"
- p15 verbatim: "the thruster demonstrated a 40% increase in thrust (330 mN), with a thrust-to-power ratio of 40 mN/kW" and "The AdvNEXT system delivers improved performance capability while maintaining comparable mass and volume relative to the NEXT-C system"
- p13/p15: PPU "efficiencies ranging from 92% - 95%" across all ten throttle levels (PPU-only figure — NOT a total-system eta; do not conflate with our row value).
- **Anchors**: extends the high-power end of every NEXT-C data point in this registry (nextc_protoflight_2021 caps at <=6.85 kW / 235 mN); 'comparable mass and volume' institutionally supports keeping our PPU row value unchanged.
- Companion records 20250008168 + 20250001749 = same paper (processing/extended-abstract) — registered once per convention.

### shastry_2024_aeps_hall_qualification_production — AEPS HCT, IEPC-2024
- p4 verbatim: "The overall envelope of the thruster is 210mm in height by 530mm in diameter, with a total mass of 53kg."
- p4 verbatim: "providing around 600mN of thrust and a specific impulse of around 2800s at a 12kW operating point" — 'highest power electric propulsion device in production'.
- p7 QM1 ATP table (verbatim rows): 600 V/9 kW = 444 mN / 2605 s; 10 kW = 491 / 2651; 11 kW = 540 / 2704; **12 kW = 586 mN / 2736 s**; "Uncertainty +/- 5 [mN] +/- 25 [s]".
- **Anchor**: HCT-only mass at the 12 kW point = 4.42 kg/kW — our 'Electric thruster + PPU specific mass' row value of 8 covers head + PPU + feed system, so it sits ABOVE the measured head-alone figure -> consistency anchor, no revision forced.

### frieman_2021_aeps_etu2_extended_characterization — AEPS ETU-2, AIAA P&E 2021
- p6 RFC table (verbatim row): "600 V/12.50 kW 611 611 2817 2830 67.1 69.4" — thrust mN / Isp s / total efficiency % at RFC vs PPE-char mean; full span across the four throttle levels: 60.3% (6.25 kW) -> 67.1/69.4%.
- p9 PPE-RFC table (verbatim row): "600 V/12.00 kW 591 2812 67.5" with the low end at "300 V/2.60 kW 159 1745 51.4" — measured Hall total efficiency spans **51.4%-69.4%**.
- **REVISION CANDIDATE (note-level only; target repo read-only)**: our row note says 'Hall thrusters run 0.50-0.60' — the top of that sub-range is +15.7% BELOW the measured 12.5 kW point (69.4% PPE-char mean). Row value 0.6 and band [0.45, 0.72] contain every measurement -> no cell revision forced; note should read ~0.51-0.70 for modern high-power Hall.

### schmitz_2023_rps_vs_solar_array_comparison — RPS vs solar/battery, IEEE Aerospace 2023
- p4 verbatim (RPS table): "BOL specific power, W/kg 2.7 4.4 3.7" under columns MMRTG / NextGen RTG Mod-1 / DRPS (8/16/6 GPHS modules; PbTe/SiGe/Stirling convertors).
- p8 verbatim (Lucy Ultra-Flex array spec): "Areal power density at 1 AU, W/m2 415 Specific power at 1 AU, W/kg 184" with 32% conversion efficiency.
- **Anchors**: 'RTG specific power' row value 5.0 is +13.6% above the best PROJECTED current-gen unit (NextGen-M1 4.4) and matches GPHS-class hardware per the NETS-2022 companion record's historical "BOL specific power of 5.3 W/kg" -> consistency anchor, no revision forced. Note-level: our 'MMRTG ... = 2.4' computes 2.44 vs institutional 2.7 (ours -9.5% low). 'Power system specific mass' note cites ROSA ~150 at the wing; current-gen Lucy arrays reach **184 W/kg** (+22.7%) — our citation is conservative, no revision forced.
- Negative probe: NO per-W cost data anywhere in either RPS version (no $ figures extracted) -> 'RTG (radioisotope power)' row's Pu-238 fuel-cost note stays secondary-sourced; institutional envelope for that cell still absent from all registered sources.
