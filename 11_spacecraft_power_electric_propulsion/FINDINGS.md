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

## R67 — RTG cost + Pu-238 production anchors (+2 T2 OIG docs)

**Targets** (re-read fresh from spacecost/reference/operational_costs.csv this round): 'RTG (radioisotope power)' $500k/W-electric [200k-1M] (note: Pu-238 supply-constrained, NASA/DOE target 1.5 kg/yr by 2026 — cited Space.com/NASA NIAC; Russian Pu-238 ~$2.5M/kg); 'RTG specific power' note cites GPHS 5.2 + MMRTG 110 We at 45 kg = 2.4 W/kg.

### nasa_oig_2017_ig-17-009_mars2020_project — Mars 2020 Project audit (Jan 30 2017)
- p14 verbatim (Table 3, 'Real Year Dollars in Millions'): "Multi-Mission Radioisotope Thermoelectric Generator 66 66 70" under columns Mission Concept Review / KDP-A / KDP-C.
- **Anchor**: institutional MMRTG project line item $66-70M at 110 We BODL = **$600-$636k per W-electric** if the full line is one unit (Table 3 does not distinguish unit count — envelope, not pin). Our row centre $500k/W sits 16.7%-21.4% below that single-unit reading and inside band [$200k, $1M] -> consistency anchor, no revision forced. First institutional $ figure for this cell (the note's Pu-238 fuel-cost arithmetic — Russian ~$2.5M/kg + 6-8% conversion — stays secondary-sourced).

### nasa_oig_2023_ig-23-010_rps_program_management — RPS Program audit (Mar 20 2023)
- p13 verbatim (Table 1 rows): "MMRTG Multi-Mission RTG 4.8 32 110 63 44" and "Next-Gen Mod-1 Next-Generation RTG— Mod-1 9.6 64 245 177 56" — columns: Pu-238 Required (kg) / Fueled Clads / BODL Watts / EODL Watts / System Mass (kg).
- p27 verbatim: "DOE plans to steadily increase Pu-238 production until reaching an annual CRP goal of 1.5 kg per year by 2026." and "although DOE planned to produce a total of 1.5 kg from 2018 through 2021, they produced only 0.77 kg—about half the projected amount".
- p3 verbatim: "NASA has not produced a viable new RPS technology since the Program began in 2010 despite an average investment of $40 million per year." (context; ~$500M total allocated to new RPS tech development since 2010).
- **Anchors**: 'RTG specific power' note: institutional MMRTG system mass = **44 kg** at 110 We BODL -> our note's '45 kg' is +2.3% high (implied SP 2.44 vs institutional 2.5 W/kg, -2.22% low) — NOTE-level revision candidate only; target repo read-only. Our RTG row value 5.0 W/kg stands on GPHS-class hardware and the NETS companion's historical 5.3 (R66), unaffected by this MMRTG note fix.
- **Anchors**: 'RTG (radioisotope power)' note: our production-target citation '(NASA / DOE target 1.5 kg/yr production by 2026)' is now the p27 institutional sentence verbatim — upgraded from secondary to anchored; actuals context recorded (0.77 kg produced vs 1.5 planned, 2018-2021) = supply-constraint claim corroborated.
- Cross-check: Table 1 MMRTG BODL 110 We AGREES exactly with schmitz_2023's RPS table (also 110); NextGen-M1 mass 56 kg @ 245 We = 4.38 W/kg vs Schmitz's projected 4.4 -> AGREE; DRPS system mass range 150-200 kg recorded for future reference.
- Negative probe: NO per-W or program $ cost data in either doc beyond the Mars 2020 line item + RPS-program budget context — Pu-238 fuel unit price still absent from all registered sources (standing gap).
