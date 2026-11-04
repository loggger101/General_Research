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

Extracted data: `extracted_data/r132_mil_hdbk_189c_growth_rate_key_numbers.csv`.

## R163 - The MTBF row's exponential form (rc-090; 2026-10-14)

spacecost@0b716ad uses P = exp(-T/MTBF). Navard 1993's fitted survival "initially drops at a much faster rate than the theoretical one" and the model "does not model the early failures very well"; Jacklin's 41.3% points the same way. rc-090 (method) asks for an infant-mortality term or a note that the constant hazard is an assumption. The 30-year scale is untested.

## R164 - Candidates (2026-10-14)

rc-093 (cite Cross & Vesely; 0.90 is the credited case), rc-094 (cite Kinnett and Shapiro Vol 2 for the tally), rc-095 (Shapiro's ~10% is per satellite; 97-99% needs a source), rc-096 (cite CR-3349's 5-10% / 60-90% salvage), rc-127 (cite Chen & McLennan; 0.85 is a judgement; Hirschmann's 80% not found). Texts in `revision_candidates_closed.csv`.

## R220 - Wright 1936 registered: the original learning-curve article now backs the beta_LC trail in-corpus (2026-10-20)

economicspace published a six-commit batch (origin/main 675f0cf to 31fb355): starred-repos split out, quietlaunch launcher split, worksheet extension on other architectures. Their CITATIONS.md gained the block quote Wright, T. P. (1936). Factors affecting the cost of airplanes. Journal of the Aeronautical Sciences 3(4), 122-128 with the learning-curve gloss each doubling of units built costs a fixed fraction of the last, and campaign/verification_sheet.py registers the citation mapping that prints Wright 1936 for any step whose formula is log2(b_LC) or k ^ beta_LC. The registry held duane_1964 (T1), hirschmann_1964 (T4 context) and chen_mclennan_2004 (T2 measured anchor) but never the 1936 original; now registered T1 with Crossref-verified volume/issue/pages.

Near-miss documented, NOT registered: MIL-HDBK-189 appears in the same worksheet diff only inside planted-case test scaffolding (a fixture proving the sheet can recognize standards cited by number), not as a source claim of any model value. All three open RC targets re-checked at the new HEAD and untouched: rc-175 documented tank-fraction pair count==1, rc-176 1.2 GB README claim count==1, rc-183 winner-table section present.

## R309 - Rig calendar life omits the idle gaps between campaigns (2026-11-01)

`economicspace_spacecost_rig_calendar_cadence_record_2026`: economicspace
`modules/calc.py:4539-4541` at 54e30b0ae82be71c987f08feb95630502b7f54f0 says the
15-year rig life "is a calendar figure"; spacecost `spacecost/operations.py:899-901`
at 860bef9902aa67fec705875cd52fdb8e6def159f calls it a "CALENDAR bound". The table
holds 15 years and an independent five-campaign duty limit.

`rig_trips_per_ship` divides 15 by `stay_yr` (L4564), but the same body can have
`campaign_cadence_yr=max(stay_yr,synodic_yr)` (L4600-4604). Its call site computes
rig trips before cadence (L6886-6894), and `programme_options` enumerates every
campaign count up to that trip bound (L4951), without checking elapsed rig age.
The wait already included in each stay is half the synodic period (L5917);
there can still be additional idle time between stays.

Executing the pinned helper functions with the actual table values and dataclass defaults
(`capacity_cap`, programme search on, eight fleet rungs, both rig limits on) gives:

| case | stay (yr) | cadence (yr) | permitted campaigns per rig | final completion from first start (yr) | campaigns within 15 yr |
|---|---|---|---|---|---|
| 0.5 yr dig, 4 yr synodic | 2.5 | 4 | 5 | 18.5 | 4 |
| 1.25 yr dig, a=1.05 AU | 6.25 | 10 | 2 | 16.25 | 1 |
| 1.25 yr dig, a=1.13 AU | 4.235009 | 5.970019 | 3 | 16.175047 | 2 |
| stay-bound control | 4.5 | 4.5 | 3 | 13.5 | 3 |
| windows-off control | 0.5 | 0.5 | 5 | 2.5 | 5 |

The 1.05 AU example respects the code's 10-year synodic cap. In the first case,
starts are 0, 4, 8, 12 and 16 years, so the fifth campaign begins after the calendar
life has already expired. Each failing case admits eight over-life coarse programme
options, one per fleet rung. Both controls admit none. Enumerating completion times
independently reproduces `1+floor((life-stay)/cadence)` as the calendar count for
`stay<=life`; the five-cycle cap still applies.

Verdict: the implemented count is a cumulative-stay budget, whereas its stated
meaning is a calendar budget. `rc-239`: include inter-campaign idle time in the rig
life constraint, or explicitly redefine the estimate as duty time. This comparison
starts the age clock at the first stay and omits outbound transit; it does not assign
a new empirical rig lifetime or quantify a change to any full-catalog winner.
`extracted_data/r309_rig_lifetime_vs_campaign_cadence.csv`.

## R320 - Partially filled fleets underallocate rig procurement and credits (2026-11-02)

Source `economicspace_nonrectangular_rig_cost_allocation_record_2026`:
economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0 `modules/calc.py`, with
spacecost@860bef9902aa67fec705875cd52fdb8e6def159f original reference rows and
spacevalue@873b91c1ce51fd2f5fe9ead63ce171d755e73011 cargo helpers. The source
claims "Non-rectangular programmes stop being mis-booked" (L4822), using
seven missions on two ships as its example (L4823-4825). The fixed-N path
sets F=ceil(N/trips), W=ceil(N/F) (L4931-4938), but each mission is then
charged `(rig_cost-credit_at_W)/W` (L5592-5603). Across N missions this buys
N/W rig equivalents, which is less than F when the final fleet is not full.

Ten complete original-evaluator cases use actual Falcon 9 reusable, kerolox
and all 46 ops rows. Main synthetic inputs: 1e9 kg body, density 2 g/cm3,
no water, 1.2 AU, raw silicate cargo at 100 USD/kg and a nonbinding market;
caller delta-v 1,000 m/s per leg, no ISRU or aerocapture. Windows, refinery,
water liberation, containment and boil-off are off for isolation. WACC and
learning remain off by default. Each mission returns 17,794.394348 kg and
the 0.25-year minimum stay binds; every case fits body, rig-calendar and
launch limits.

With programme search off and N=7, the original five-cycle rig limit gives
F=2, W=4. The 2,000 kg rig at 300,000 USD/kg costs 600M USD. The code uses
the four-cycle credit of 60M, charging (600M-60M)/4 = 135M per mission, or
945M for the programme. Seven missions under a four-campaign maximum require
actual rig uses 4+3. Their credits are 60M+120M under the same rules, so the
two rigs cost 1,200M-180M = 1,020M net. The code underallocates 75M before
contingency, or 90M of programme total cost with the original 20% contingency.

| case | rig campaign counts | reported rig cost (M USD/programme) | integer rig cost (M USD/programme) | difference (M USD) |
|---|---|---|---|---|
| N=7 | 4+3 | 945 | 1,020 | 75 |
| N=9 | 5+4 | 1,080 | 1,140 | 60 |
| N=11 | 4+4+3 | 1,485 | 1,560 | 75 |
| N=13 | 5+4+4 | 1,560 | 1,680 | 120 |
| N=7, salvage fraction set to zero | 4+3 | 1,050 | 1,200 | 150 |
| N=6 | 3+3 | 960 | 960 | 0 |
| N=8 | 4+4 | 1,080 | 1,080 | 0 |
| N=10 | 5+5 | 1,200 | 1,200 | 0 |
| single mission | 1 | 600 | 600 | 0 |
| searched one-ship programme | 5 | 600 | 600 | 0 |

The zero-salvage control isolates fractional procurement independently of
any residual-value estimate. Separate calls to the original cost tail, using
each actual rig's campaign count and the unchanged global N for NRE and
learning, reproduce the integer totals when weighted by missions served.
An independent sum of F full procurement costs minus individual credits
agrees. Launch, return fuel, capsule, NRE and operations remain unchanged.
The balanced 5+4+4 allocation is not essential here: the short-stay cycle
credit is linear in campaigns, so the total depends on N and integer F.

Verdict: using the maximum W as every mission's divisor does not buy the
integer fleet required for a partially filled fixed programme. `rc-250`:
aggregate procurement and credits per actual rig before averaging over N,
while retaining global programme terms. Equal-use searched and single-mission
controls match; current-population incidence and ranking effects were not
measured. `extracted_data/r320_nonrectangular_rig_cost_allocation.csv`.

## R321 - Learning-curve family label differs from the implemented unit-cost mean (2026-11-02)

Source `delionback_1975_guidelines_learning_cost_improvement_curves`, NASA
TM X-64968 (1975): Wright's ordinate is "cumulative average cost" (printed p6,
PDF p10); Crawford's ordinate uses "unit values as opposed to a cumulative
average" (p6, continued p7). Appendix B (p31, PDF p34) explains that the same
rate/quantity gives a common line for Wright cumulative average and Crawford
unit cost, while Crawford cumulative average lies above it. These are model
definitions, not a spacecraft slope measurement.

Upstream: economicspace@54e30b0ae82be71c987f08feb95630502b7f54f0,
`learning_curve_factor` (calc.py L4440-4456), configuration comments L423-450
and MODEL.md L721-733. The helper describes a Wright cumulative-average
multiplier but calculates `sum(k**b for k in 1..N)/N`, where
`b=log(rate)/log(2)`. It is a cumulative mean of Crawford unit costs. Under
Wright cumulative-average theory the corresponding normalized mean is
`N**b`, without averaging those already cumulative-average values again.

Twenty-one unchanged original-helper cases cover rates 0.80 and 0.85 at
N=1,2,4,8,10,16,32,64,100,320, plus rate 1.0 at N=100. Independent 50-digit
Decimal unit-power sums match the original helper; Wright means agree with
the telescoping sum of marginal total costs. At the current 0.85 judgement:

| N | implemented Crawford-unit mean | same-rate Wright cumulative average |
|---|---|---|
| 1 | 1.000000000 | 1.000000000 |
| 2 | 0.925000000 | 0.850000000 |
| 4 | 0.836353709 | 0.722500000 |
| 10 | 0.711606273 | 0.582820402 |
| 100 | 0.437538671 | 0.339679621 |
| 320 | 0.335746969 | 0.258600509 |

The N=100 learned recurring-cost factor differs by 28.8092%; this is a
comparison of model families, not a measured error in actual factory cost.
MODEL.md's rounded 0.44 is consistent with the existing calculation. The
unit costs obey the 0.85 doubling rate, while their cumulative mean does not:
the first doubling changes that mean from 1.0 to 0.925. Both models agree at
N=1 and with no learning. The default flag remains False, resolving the
cost model's learning rate to 1.0 (calc.py L5470).

Verdict: the implementation's family label and its cumulative-average
interpretation conflict with the formal Wright/Crawford distinction.
`rc-251`: identify the existing calculation as the cumulative mean of a
Crawford unit curve, preserving its arithmetic and the 0.85 judgement. A
switch to Wright cumulative-average theory would be a separate numerical
model decision requiring its own justification. Neither family is shown
empirically superior for asteroid spacecraft, and population/ranking effects
were not measured. `extracted_data/r321_learning_curve_model_identity.csv`.

## R351 - Parallel first-flight growth has no specified feedback schedule (2026-11-03)

`mil_hdbk_189c_reliability_growth_management`, printed p8 (PDF p16),
section 4.9.1 describes a "feedback loop": discovery, problem feedback,
analysis, approval and implementation of corrective actions. It permits
improvement in product or manufacturing-process design, including preflight
work. Printed p9 (PDF p17), sections 4.9.3/4.9.5 link growth to corrections
and their turnaround, including "physical implementation of approved
corrective actions". These passages do not supply a new mining success
probability, growth exponent or maturity ceiling.

`economicspace_parallel_reliability_growth_record_2026` reads economicspace
54e30b0ae82be71c987f08feb95630502b7f54f0. calc.py L4405-4437 correctly
averages the adopted curve over missions 1..N and describes designed-out
failure modes from flight heritage. Its cache (L4515-4524) and revenue
consumer (L7232-7235) use N without fleet, wave or corrective-action timing.
The source ladder (L4944-4951) permits W=1, F=N; all those missions share a
single mission-duration programme span. MODEL.md L908-930 uses the same
growth/heritage interpretation. Reliability is disabled by default (L568).

The declared counterexample has no additional preflight analytical/test
maturation and no in-cohort corrective changes. Twenty-one constructed
fixtures run original, repeat, a scoped first-wave diagnostic and its repeat:
84 complete evaluate_asteroid consumers using current reference-only Stage 2,
real source vehicles/kerolox, geometric transfers, raw cislunar cargo and
capacity caps. Each chosen (N,F,W) is asserted present in the original
ladder before selecting that single tuple. This tests the cohort mechanism,
not an unrestricted programme optimum or an observed asteroid population.
The diagnostic uses the unchanged original helper at N=1 only for parallel
W=1 cohorts; it changes no source probability, alpha, ceiling or unit rate.

For the 1-km synthetic magnetite body (3 g/cm3, a=1.2 AU, e=i=0,
10 h spin), Falcon 9 reusable/kerolox with (N,F,W)=(25,25,1) spans
1.8008760870758898 years, exactly one mission. Native p_mining is
0.9227022785808684 versus the adopted first-of-kind 0.85 in the declared
no-added-maturation scenario. p_success is 0.842874617849371 versus
0.7764621826596845; expected gross per mission is 2,960,936.0673144935
versus 2,727,635.6801548093 USD, an 8.553209% uplift. Per-mission cost
671,509,402.7011702 USD is exact. All fields outside the five risk/revenue/
profit/ROI metrics are exact. Ten cases change, including N=2..100 and
distance, vehicle and mineral sensitivities. Eleven full-book controls are
exact: N=1, risk off, growth off and four serial cases. The serial cases are
outside the conditional diagnosis; unchanged output does not certify their
feedback timing. Both repeated pairs match native types/values/float.hex
fingerprints, and returned books pass the source checks exercised by the
harness. All examples remain unprofitable.

Verdict: `rc-286`, qualify growth by available cohort feedback or explicitly
justify additional preflight maturation and its resource/calendar basis.
The existing curve arithmetic and defaults need not change. No universal
absence of preflight learning, newly measured probability, current-population
incidence or ranking effect is asserted. Twenty-four source blobs match
pinned metadata; all four live main comparisons are identical.
`extracted_data/r351_parallel_reliability_growth.csv` includes complete
inputs, books, fingerprints and the self-contained reproduction harness.
