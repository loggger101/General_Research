# Domain 28 — Radiation-shielding value of in-space materials

Backings: economicspace `modules/mineral_value.py` `IN_SPACE_UTILITY` and `IN_SPACE_UTILITY_BY_DESTINATION`, the rows whose in-space use is bulk radiation shielding (every silicate and oxide phase, hibonite, and the rock-valued carbonates, oldhamite and phosphates), the shielding part of water's row, and the `"shielding"` default of `_COMMODITY_CLASS`: how much protection a delivered kilogram of each material buys compared with the same mass launched from Earth.

Created in Round 161 (2026-10-13). Blocks are appended one per round, newest last.

## R161 - Domain opened with five NASA shielding reports (2026-10-13)

At the owner's request, Round 161 opened domains for the in-space utility of each material. economicspace prices a delivered kilogram at its utility factor times the launch cost it avoids (`in_space_price_usd_per_kg`); the factors are "ENGINEERING JUDGEMENTS, NOT MEASUREMENTS". Domain 15 holds the market side; domains 28-30 hold the engineering basis, split by upstream's commodity classes (this one: shielding).

**Cells** (economicspace@8dc759f):

| cell | current value | upstream's stated basis |
|---|---|---|
| `IN_SPACE_UTILITY` olivine, pyroxene, orthopyroxene, enstatite, plagioclase, spinel, phyllosilicates, oxides, silicates | 0.25 (base: LEO, cislunar, mars_orbit) | "Usable as bulk radiation shielding and as 3-D-printing / sintering feedstock, but a poor per-kg substitute for engineered structure" |
| `IN_SPACE_UTILITY` hibonite; carbonates, oldhamite, merrillite, chlorapatite | 0.25 | "shielding rock at 0.25" |
| `IN_SPACE_UTILITY` water | 1.00 | "propellant feedstock, radiation shielding, life support and coolant" |
| `geo`, the rock rows | 0.05 | "Bulk shielding is the one real use for rock here ... nobody bolts raw olivine to a comsat" |
| `lunar_surface`, the rock rows | 0.03 | "Shipping silicate rock to a body made of silicate rock" |
| `mars_surface`, the rock rows | 0.02 | "Basalt, everywhere, for free" |
| `_COMMODITY_CLASS` default | `"shielding"` | an import-time assertion requires every row to be classed |

**What a source has to supply:** shielding effectiveness per unit mass of water, silicate rock or regolith and metal under one environment and risk measure, so the rock rows can be stated as a fraction of water's value; the same at a planetary surface.

**Sources (NTRS public use, hosted):**

- `townsend_1990_gcr_shielding_requirements_tm4167` (TM-4167): for 0.5 Sv/yr BFO at solar minimum, 3.5 g/cm2 water, 6.5 g/cm2 aluminium or 1.0 g/cm2 LH2; at 0.25 Sv/yr LH2:water:Al = 1:5:11. Aluminium needs 1.86x water's mass at the first limit, 2.2x at the second.
- `kim_wilson_1994_gcr_shield_materials_performance_tp3473` (TP-3473): performance index varying up to 20x across materials at constant mass; "the unique role of hydrogenous materials". Figs 13 and 15 plot water, LH2, LiH, liquid methane, lunar regolith, regolith + 10% epoxy, iron, copper, aluminium and lead on one axis (figures only, not yet digitised).
- `wilson_1997_gcr_spe_shielding_deep_space_tp3682` (TP-3682): bringing 5-cm dose equivalent at solar minimum to 45 cSv needs ~55 g/cm2 aluminium vs 17 g/cm2 polyethylene (3.2x); aluminium structure as shielding is "clearly not cost-effective".
- `kim_1998_martian_meteorites_regolith_shield_materials_tp1998_208724` (TP-1998-208724): five Martian meteorite groups match the regolith model within 0.5% (dose) and 1% (dose equivalent); 30 wt% epoxy lowers dose equivalent at 50 g/cm2 by 13%. Rock type does not matter; hydrogen does.
- `slaba_mertens_blattnig_2013_radiation_shielding_optimization_mars_tp2013_217983` (TP-2013-217983): in free space the first 20 g/cm2 cuts dose equivalent 45-65% and aluminium-like mass helps little past ~45 g/cm2; on the Martian surface dose equivalent rises 63% from 0 to 100 g/cm2 of aluminium; regolith helps only at several hundred g/cm2.

Also: `lewis_1992_asteroid_resources_sp509_vol3` (d29) names "bulk dirt needed for shielding in low Earth orbit".

**Against the cells:** hydrogen-rich material ranks first per kg, aluminium needing 1.86-2.2x water's mass, which bounds water's shielding share without pinning its 1.00. Kim 1998 supports valuing all silicates alike; no text gives rock vs water per kg, so upstream's implied factor 4 (1.00 vs 0.25) is neither confirmed nor contradicted, but it is consistent with rock being no better than aluminium. The surface overrides (0.02, 0.03) and geo 0.05 are consistent with Slaba and Kim. Metal rows rightly take no shielding credit. `extracted_data/r161_shielding_by_material_key_numbers.csv`. No candidate.

**Boundary:** domain 15 keeps the market side (demand, class shares, elasticity, surplus price); this domain the physics of what a kilogram shields.

## R166 - SPE shielding at a surface site; water in regolith (2026-10-14)

Hosted:

- `nealy_wilson_townsend_1989_solar_flare_shielding_regolith_lunar_base_tp2869` (TP-2869; quotes from NTRS's extracted fulltext, which matches the garbled PDF layer): BRYNTRN doses for the Feb-1956, Nov-1960 and Aug-1972 flares in regolith-shielded modules: "for 50 cm of regolith shield, the computed dose is well below 1 rein, which would be considered nonhazardous" (Aug-1972; unshielded "at or near the lethal dose (_ 500 rem at 5-cm tissue depth)"); "the maximum interior dose is slightly in excess of 9 rem for the 1956 solar flare" (half-buried sphere); "larger thicknesses may be more desirable". Soil density "assumed to be 1.5 g/cm 3, based on the density range of 0.8 to 2.15 g/cm 3"; BFO limits "25 rein/month and 50 rem/year" ("rein" = rem). "the use of lunar soil as a shielding material is attractive in that shielding materials need not be transported to the lunar base".
- `johnson_gersey_wilkins_zhou_2011_radiation_shielding_regolith_polyethylene_water_ntrs20110012713` (abstract; year from NTRS): "adding 2 wt% water to regolith particles could increase shielding of the regolith materials by about 6%", against LCROSS's "up to 5.6 +/-2.8 weight percent (wt%)".

Imported rock buys nothing at a lunar base (0.03 consistent); the water result supports a shielding credit in lunar water's 0.60. TP-2869's GCR side ("relatively large thicknesses (_ 10 cm) are required") leaves geo 0.05 unchanged. `extracted_data/r166_spe_shielding_key_numbers.csv`. No candidate.

## R178 - The GCR performance index (TM-4444) (2026-10-16)

`wilson_wood_shinn_cucinotta_nealy_1993_gcr_performance_index_tm4444` (TM-4444, signed 1993-04-20, issued August 1993; hosted), TP-3473's reference 12, which defines what Fig 15 plots: a relative performance index P_rel ∝ [(L4)/(L2)]^2 (eqs 12-15), "inversely related to biological injury for different materials at a fixed shield mass". "iron is a slightly poorer shield material than aluminum" (Fig 4); polyethylene best. p8: "relative performance index for polyethylene of _1.8, which corresponds to a cell-death ratio of _1.7" at 10 g/cm2; "the 80-percent increase in relative perfornmncc corresponds to a 70-t)ercent decrease in biological injury" (OCR as printed). Table 1 is too garbled to extract.

PE ~1.8x aluminium matches Townsend's 1.86-2.2: hydrogenous material is worth about double metal per kg. No regolith or water row, so the rock-vs-water ratio still waits on digitising TP-3473 Fig 15 or TP-2869's curves. `extracted_data/r178_gcr_performance_index_key_numbers.csv`.

## R179 - Transport methods and mission-scale shield mass (2026-10-16)

From TM-4444's references, hosted:

- `wilson_townsend_et_al_1991_transport_methods_interactions_space_radiations_rp1257` (RP-1257, 620 pp): the Boltzmann transport-methods monograph behind BRYNTRN/HZETRN and every dose curve here ("a relatively complete summary of technical capability as of the summer of 1990").
- `wilson_nealy_schimmerling_1993_radiobiological_uncertainty_shield_design_tm4422` (TM-4422; TM-4444 misprints it "TM-,I,122"): the additional shield mass to cover GCR radiobiological uncertainty "is found to be as large as a factor of 3 for a lunar transfer vehicle"; S = 3 means dose equivalent "300 percent greater"; risk predictions "accurate only within an order of magnitude (factor of 10)", so a design for under 3% excess cancer risk may really be for 30%. Mission: an LTV shell and a half-buried lunar habitat over 60 days (45 on the surface, 5 transit each way, 5 in LEO). LEO BFO limits 0.25 Sv per 30 days, 0.50 Sv a year. Payload cost "about 30000 dollars/lb or 66 million dollars metric ton" (1993).

The x3 factor bounds the radiation-driven share of habitat mass; no per-kg value pinned. TM-4444's refs 4 (TP-3312) and 6 were not found on NTRS (ref 6 later found, R181). `extracted_data/r179_gcr_shield_uncertainty_key_numbers.csv`.

## R180 - BRYNTRN and the CAM phantom (2026-10-16)

From TM-4422's references, hosted:

- `wilson_townsend_nealy_1989_bryntrn_baryon_transport_model_tp2887` (TP-2887, 84 pp): "an interaction data base and a numerical solution to the transport of baryons through an arbitrary shield material based on a straight ahead approximation of the Boltzmann equation"; good results with "a relatively coarse energy grid (30 points) and large spatial increments (1 cm in H2O)" at "a very small fraction of the computer resources required for Monte Carlo codes"; validated against Monte Carlo and neutron data at 0.5/2/10 MeV. (Its summary is reprinted as the documentation-page abstract, so those spans occur twice.)
- `billings_yucker_1973_computerized_anatomical_man_cam_model_cr134043` (CR-134043, McDonnell Douglas for JSC, contract NAS9-13228; the CR number comes from TM-4422 and NTRS): "a 50-percentile standing USAF man ... comprises some 1100 unique geometric surfaces and some 2450 solid regions", organs, voids, bone and marrow modelled explicitly. Table 7 OCR-damaged, not extracted.

Method and anatomy provenance for every dose here; no value pinned. `extracted_data/r180_bryntrn_cam_key_numbers.csv`.

## R181 - The HZETRN chain (2026-10-16)

Found by NTRS title search on "HZETRN" (142 hits), hosted:

- `shinn_john_tripathi_1992_fully_energy_dependent_hzetrn_tp3243` (TP-3243): R179's missing ref 6, misprinted "FZETRN" in TM-4444. Replaces nucleon-only energy dependence with energy-dependent fragmentation; total fluxes and computing time barely change, but "The high LET components are significantly higher in the new code and have important implications on biological risk estimates for heavy-ion exposure."
- `wilson_tripathi_badavi_cucinotta_2006_standardized_shield_design_method_2005_hzetrn`: "HZETRN code provides the current basis for shield design methods according to NASA STD-3000 (2005)", the only code so identified; the 1995 research code became the 2005 engineering code.
- `wilson_shinn_singlettery_1999_spaceflight_validation_hzetrn_code` (year from NTRS): validated against "TEPC, CR-39, charge particle telescopes, and Bonner spheres" and STS-57 spectra; the August 4, 1972 event (50 h of IMP8 data) took "only 18 hours on a VAX 4000 machine" vs two years for Monte Carlo.

Why shielding utility tracks dose equivalent, not flux; no value pinned. `extracted_data/r181_hzetrn_chain_key_numbers.csv`.

**Still open in this domain:** a text-stated or digitised per-kg ratio of silicate regolith to water; asteroid-specific compositions (CI/CM rock with bound water should shield better than dry silicate).
