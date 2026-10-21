# Domain 16 — Reliability, learning curves & hardware service life

Backings: spacecost `reference/operational_costs.csv` rows `Launch vehicle reliability`, `Spacecraft mean time between failures`, the three `Mining system` / `Mining reliability` rows, `Mining rig service life`, `Mining rig maximum trips` and `Rig salvage fraction`, and economicspace `modules/calc.py` `learning_curve_rate`.

Created in Round 75 (2026-09-27). Blocks are appended one per round, newest last.

## R75 - Domain opened (2026-09-27; no sources yet)

Read at economicspace@1f470d4 and spacecost@e831245.

| cell | current value | upstream's stated basis |
|---|---|---|
| `Launch vehicle reliability` | 0.97 [0.90, 0.99] | Falcon 9 ">99% success over 300+ flights", a first-flight vehicle "near 0.90"; no source |
| `Spacecraft mean time between failures` | 30 yr [15, 60], P = exp(-T/MTBF) | examples (Voyager 1/2, New Horizons, Dawn, Akatsuki, Hayabusa); no failure dataset |
| `Mining system first-of-kind success probability` | 0.85 [0.70, 0.95] | a tally of flown regolith-contact mechanisms; no source |
| `Mining reliability growth exponent` | alpha = 0.30 [0.10, 0.60] (Duane / AMSAA) | MIL-HDBK-189: 0.3-0.6 active, 0.1-0.2 passive |
| `Mining system mature success probability` | 0.95 [0.85, 0.99] | "solar-array and antenna deployments run ~97-99% across the fleet record"; no source |
| `Mining rig service life` | 15 yr [5, 30] | "ISS-class hardware is rated 15-30 years"; no source |
| `Mining rig maximum trips` | 5 [2, 12] | "JUDGEMENT, and there is no flight heritage for it" |
| `Rig salvage fraction` | 0.5 [0.0, 0.8] of remaining book value | "a deliberately unheroic haircut"; no source |
| `calc.py` `learning_curve_rate` | 0.85 per doubling; `model_learning_curve` False since v1.22.0 | "Wright's law at 85% is standard for aerospace serial production"; no source |

**What a source has to supply:** launch success statistics that handle small samples; spacecraft lifetime-distribution fits; mechanism success rates by type; fitted growth parameters and measured learning slopes; regolith-abrasion wear life; residual value of used heavy mining equipment.

**Boundary:** domain 10 holds engine certified life; domain 17 insurance.

## R77 - Sources moved in (2026-09-27)

`mil_hdbk_189c_reliability_growth_management` and `duane_1964_learning_curve_reliability_monitoring` moved here from domain 5 (earlier write-up: R74 there; no files).

## R86 - Launch reliability (2026-09-30)

Both NTRS, hosted:

- **cross_vesely_2018_lv_first_flight_failure_probability** (PSAM 2018): from every failure on the first two flights of each vehicle model 1980-2017, first-flight failure probability 0.134 (success ~0.866), 0.0898 (~0.910) with heritage credit (solid propulsion, upper-stage engines, TVC); per element-launch: upper-stage liquid engines 2.03E-02, avionics 1.32E-02, stage separation 1.36E-02, TVC 1.95E-03. New vehicles have "significantly higher average failure probability than mature launch vehicles" (p11).
- **al_hassan_novack_2015_bayesian_reliability_data_applicability** (SRE RAM VIII): lognormal priors per block weighted by data applicability over NPRD/EPRD/NUCLARR and MIL-HDBK-217F, Monte Carlo combined; "Higher data applicability improves certainty of estimates" (p16). The method for small-sample estimates here.

The note's "near 0.90" for a first flight now has 0.866 raw / 0.910 credited; 0.97 is consistent with the mature series. `extracted_data/r86_launch_reliability_key_numbers.csv`. No candidate.

## R90 - Fleet failure rates; a measured learning curve (2026-09-30)

Both hosted:

- **jacklin_2019_small_satellite_mission_failure_rates** (NASA/TM—2018–220034): 41.3% of small satellites launched 2000-2016 failed totally or partly (launch vehicle 6.1%, partial 11%, total 24.2%; p17); yearly success ~71% (2000-08) -> ~57% (2009-16), from ~95% (2006) to just over 40% (2009, 2012) (p15); Table 2 counts launch failures 1957-2017 (p10). Failures "can be kept more private", so lower bounds (p12). Small craft, not the deep-space MTBF population.
- **chen_mclennan_2004_learning_curve_impact_three_identical_spacecraft**: an exponential improvement model d(Ct-C0)/dt = -k(Ct-C0) fitted to three identical ST-5 spacecraft at Goddard: constant percentage reduction per unit toward a floor, diminishing returns (p8-9). Confirms the form of `learning_curve_rate`; n=3 cannot pin 0.85.

`extracted_data/r90_reliability_learning_key_numbers.csv`.

## R93 - Lifetime-distribution fits (2026-10-01)

- **navard_1993_modelling_early_failures_space_station_freedom** (JSC faculty fellowship report, hosted): a Heydorn mixture of exponentials fitted to Kaplan-Meier survival of electronics on 28 satellites since 1976 (165 observations, 14 failures, the 82 largest times truncated). "a mixture of exponential distributions does not adequately explain electronic failures seen in previously flown satellites. In particular, it does not model the early failures very well." (p8). The 30-year scale is not tested.
- **vitali_lutomski_2004_derivation_failure_rates_probability_failures_iss_pra** (PAM, hosted): ISS PRA lognormal priors from MADS and NPRD/EPRD updated with on-orbit failures; Table 2 six-month probability of failure: Electronics 6.10E-03, Electrical 7.00E-03, Electro-Mechanical 2.50E-02, Mechanical 2.80E-02 (from a page render).
- **fox_salazar_habib_agahi_dubos_2013_satellite_mortality_study** (IEEE Aerospace 2013, DOI 10.1109/aero.2013.6497352; open_not_pulled, NTRS 20150008736 has no file): Weibull vs exponential on operating life / design life across a large public dataset, Kaplan-Meier survival and bootstrap uncertainty. The direct source for the MTBF cell once read.

`extracted_data/r93_lifetime_distribution_fits_key_numbers.csv`. No candidate (later rc-090).

## R94 - Regolith wear; used-equipment resale (2026-10-01)

- **kunneparambil_et_al_2026_radiation_conditioned_ti_hbn_space_mechanisms** (hosted): rod-slot, ball-socket and hinge joints in Al6061 and Ti6Al4V abraded with JSC-1A under vacuum: "over 80% reduction in wear depth compared to uncoated components", uncoated showing "severe abrasion, and regolith-induced gouging"; no wear rates (p5).
- **sukumaran_et_al_2024_ti_hbn_wear_neutron_shielding_sct** (Surf. Coat. Technol. 492:131185; Elsevier, read only): "90-95 % reduction in wear rate compared to the Ti CM substrates"; regolith raises wear rate.
- **stein_et_al_2025_icacc_abrasive_effects_of_lunar_regolith_on_material_wear** (read only): ASTM D4060-19 Taber: bare Al6061-T6 3.29 (CS-17) vs 3.64 mg/1000 cycles (LMS-1 wheels, ~10% more); APS alumina 5.19-5.39; 8YSZ 9.20, "nearly twice as much as the alumina".
- **mas_2007_nber13138_labor_unrest_equipment_resale_market** (NBER w13138; read only): >48,000 used construction machines at auction 1994-2002; a quality shock moves resale prices ~5%. A liquid market, unlike an asteroid rig's "market of approximately one buyer".

Service life, trips and salvage stay judgement with a component-level evidence base. `extracted_data/r94_regolith_wear_resale_key_numbers.csv`.

## R95 - Mechanism success rates by type (2026-10-01)

- **shapiro_murray_howarth_fusaro_1995_space_mechanisms_lessons_learned_vol1_summary** (TM-107046, hosted): "Based upon a detailed study of the performance records of almost 400 satellites between 1958 and 1983, it was established that about 10% of the successfully launched satellites had some type of deployment anomaly, the majority of which were mechanical"; "35 out of 84 (42%) of the failures were caused by lack of understanding"; ">2000 units are needed to establish a 99.99% reliability at a 95% confidence level" while tests run on "as few as six assemblies or less".
- **shapiro_murray_howarth_fusaro_1995_space_mechanisms_lessons_learned_vol2_literature_review** (TM-107047, hosted): the same study by type (deployable appendages, rotating, oscillating systems).
- **fusaro_nasa_space_mechanisms_handbook_lessons_learned_documented** (hosted): ~30 mechanism failures 1964-1977: microswitches (Voyager boom, Magellan latch), cold welding (Galileo HGA), lubricant (Voyager scan platform), thermal binding (Hubble, Galileo), harness and blanket interference (Skylab, CRRES).
- **kinnett_green_klein_lin_2022_drill_feed_msl_in_flight_failure_ams** (Caltech copyright, read only): Curiosity's drill feed stalled on sol 1536 (2016-11-30), unreliable by June 2017; feed-extended drilling recovered sampling on sol 2057, "521 sols after the initial feed stall".

Shapiro's ~10% per-satellite anomaly rate (complement ~90%) sits below upstream's 97-99% but measures a different population. Every item of the opening brief now has a source; remaining work is pulling Fox 2013. `extracted_data/r95_mechanism_success_rates_key_numbers.csv`.

## R114 - Deployables, salvage, repair, ISS life (2026-10-04)

`nasa_oig_2014_ig-14-031_iss_operational_life_extension`: ISS "designed and tested for a 15-year life span", may run 26 years, ~$75B invested. `rivera_stewart_2021_study_of_spacecraft_deployables_failures`: about one deployment failure or anomaly a year since 1961 (one every two years lately); a $146M claim on a $245M policy. `nasa_cr_3349_1980_sps_salvage_and_disposal_alternatives`: salvage 5-10% of a power satellite's capital cost (~$500M-1B), 60-90% for a demonstration unit, the closest anchor for the salvage fraction. `katzberg_garrison_1995_selv_based_in_space_operations_workshop`: replace success 85%, repair 80%, median insured spacecraft $31.6M. Abstract or opening only: `nakamura_2025_sample_return_missions_rosetta_stones_small_bodies`, `hirschmann_1964_profit_from_the_learning_curve`. The owner's "97-99%, $800M claims" and "$150M AMC-14 payout" were not found. `extracted_data/r114_gr_links_key_numbers.csv`.

## R120 - nakamura_2025_sample_return_missions_rosetta_stones_small_bodies hosted (CC BY; 2026-10-05)

Hosted as full_texts/nakamura_et_al_2025_sample_return_missions_rossetta_stones_small_bodies_ssr22144_ccby.pdf (Space Sci. Rev. 221:44): review of sample-return missions; context.

## R132 - MIL-HDBK-189C hosted; rc-084 (2026-10-07)

All 149 pages pulled from the reliabilityanalytics.com page library (ASSIST and DOT&E refuse this machine) and merged (33,567,638 B; "Approved for public release; distribution is unlimited"). The Duane framework (C(t)=A t^a, §5.2.6) is there; the handbook defines a growth rate in (0,1) but has no active/passive split. **rc-084** (citation).

**Correction (applying rc-084):** the handbook does give a band, printed "0.27-0.64": Table II "Historical Growth Rate Estimates" (§5.2.6.2, p32), one-shot systems 0.27-0.64 (median 0.47), time-based 0.23-0.53 (median 0.32), with Duane's universal 0.5 rejected; the 0.1-0.2 passive band is absent. spacecost 0.6.1 cites Table II and keeps alpha = 0.30. Probe sweeps should search for the quantity's name and table captions, not just the claimed number.

## R163 - The MTBF row's exponential form (rc-090; 2026-10-14)

spacecost@0b716ad uses P = exp(-T/MTBF). Navard 1993's fitted survival "initially drops at a much faster rate than the theoretical one" and the model "does not model the early failures very well"; Jacklin's 41.3% points the same way. rc-090 (method) asks for an infant-mortality term or a note that the constant hazard is an assumption. The 30-year scale is untested.

## R164 - Candidates (2026-10-14)

rc-093 (cite Cross & Vesely; 0.90 is the credited case), rc-094 (cite Kinnett and Shapiro Vol 2 for the tally), rc-095 (Shapiro's ~10% is per satellite; 97-99% needs a source), rc-096 (cite CR-3349's 5-10% / 60-90% salvage), rc-127 (cite Chen & McLennan; 0.85 is a judgement; Hirschmann's 80% not found). Texts in `revision_candidates.csv`.


### R220 - Wright 1936 registered: the original learning-curve article now backs the beta_LC trail in-corpus

economicspace published a six-commit batch (origin/main 675f0cf to 31fb355): starred-repos split out, quietlaunch launcher split, worksheet extension on other architectures. Their CITATIONS.md gained the block quote Wright, T. P. (1936). Factors affecting the cost of airplanes. Journal of the Aeronautical Sciences 3(4), 122-128 with the learning-curve gloss each doubling of units built costs a fixed fraction of the last, and campaign/verification_sheet.py registers the citation mapping that prints Wright 1936 for any step whose formula is log2(b_LC) or k ^ beta_LC. The registry held duane_1964 (T1), hirschmann_1964 (T4 context) and chen_mclennan_2004 (T2 measured anchor) but never the 1936 original; now registered T1 with Crossref-verified volume/issue/pages and a documented HTTP 403 at doi.org from this machine.

Near-miss documented, NOT registered: MIL-HDBK-189 appears in the same worksheet diff only inside planted-case test scaffolding (a fixture proving the sheet can recognize standards cited by number), not as a source claim of any model value. All three open RC targets re-checked at the new HEAD and untouched: rc-175 documented tank-fraction pair count==1, rc-176 1.2 GB README claim count==1, rc-183 winner-table section present.
