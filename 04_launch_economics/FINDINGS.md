# Domain 4 Findings — launch cost per kg (history, projections)

Backings: spacecost `reference/launch_vehicles.csv` (prices, payloads, fairing volumes) and the `Expendable upper stage recurring cost` row of `operational_costs.csv`; economicspace's "launch no longer dominates" framing.

## Round 1 - hf_dataset and jones2018

**hf_dataset** [T3, hosted: `full_texts/juliensimon_launch-cost-to-leo_dataset.parquet`]: 63 vehicles with LEO payload, $/launch and $/kg. 16 overlap our table (`extracted_data/hf_dataset_vs_pipeline_comparison.csv`; full table `r70_hf_dataset_full_table.csv`):

| vehicle | pipeline $/kg LEO | HF $/kg | verdict |
|---|---|---|---|
| Atlas V 551, Vulcan VC6, New Glenn, Electron, Firefly Alpha | 8,117 / 4,044 / 1,511 / 23,438 / 14,563 | same | exact |
| Falcon 9 (reusable) | 4,253 | 3,851 | +10%, ours the more conservative published figure |
| Soyuz-2.1b | 5,843 | 6,098 | −4% |
| Falcon Heavy (reusable side cores) | 1,702 | 1,940 | −12%, config difference |
| H3 (24L) | 3,091 | 3,846 | −20%, JAXA target-price variant |
| Long March 5 | 4,400 | 2,400 | +83% on the same name and payload: should carry a range |
| PSLV-XL | 8,158 | 4,615 | config mismatch (3.8 t / $31M vs 3.25 t / $15M) |
| Vega C | 11,212 | 19,565 | config mismatch (3.3 t / ~€34M vs 2.3 t / €45M) |
| H-IIA 204 | 6,000 | 9,000 | config mismatch (15 t vs 10 t at $90M) |
| Delta IV Heavy | 15,283 | 13,894 | +10% |
| Terran R | 2,090 | 2,750 | −24%; tracks a stated goal |
| Starship (projected) | 900 | 67 | not comparable: contract-anchored vs Musk's $10M/150 t aspiration |

No outright errors; the large gaps are config mismatches except Long March 5.

**jones2018** [T2, hosted: `full_texts/ntrs_2020_recent_large_reduction_in_space_launch_cost.pdf`] (ICES-2018-81, NTRS 20200001093): Shuttle $54,500/kg → commercial ~$2,700–3,900/kg, a factor of ~20. R6 extraction (`extracted_data/jones2018_launch_cost_key_numbers.csv`): ISS cargo $105.8k/kg Shuttle → $25k/kg Falcon 9 + Dragon, only ~4x (Dragon's payload to ISS 6,000 kg vs 16,050 kg), so LEO and ISS are priced separately; 1970–2000 average $18.5k/kg (range $10–32k, 22 systems; the sub-$10k systems Soviet or Chinese); Falcon Heavy $1.4k/kg (2018$); reuse lowers marginal cost but raises development cost.

`extracted_data/jones2018_leo_cost_history.csv`.

## Round 3 - Experience curve and economics framing

- **terzi_nicoli_2026** [T1, hosted, CC BY] (PNAS Nexus 5(7):pgag217): 4,400+ launches 1960–2025, Wright's-law fit. Fleet average $87,023/kg (1960) → $3,868/kg (2025, 2024 USD); learning rate −21.2% per doubling (~−44% post-Cold-War vs ~−17% before); central forecast $1,600/kg by 2030 and $300/kg by 2040. Our Falcon 9 row ($4,253/kg) is above the 2025 fleet mean. Stage 4 carries no forward projection: whether to discount long-horizon launch costs is the owner's call. `extracted_data/terzi_nicoli_experience_curve_key_numbers.csv`.
- **weinzierl2018** [T1] (JEP 32(2):173–192; Harvard DASH author copy, LAA terms, extract only): COTS all-in ISS cargo ≈ $89,000/kg SpaceX, $135,000/kg Orbital Sciences, ~$272,000/kg Shuttle (citing Zapata 2017; p181). R73 extraction: Figure 2 space-sector revenue $176B (2005) → $330B (2014) / $322B (2015); Table 1, 37 New Space companies. `r73_weinzierl2018_figure2_space_sector_revenue.csv`, `r73_weinzierl2018_key_numbers.csv`, `r73_weinzierl2018_table1_new_space_companies.csv`.

## Round 12 - metzger_2023 (moved to d22)

arXiv:2303.09011, read only: the gear ratio on cost G and production mass ratio phi decide whether lunar propellant beats Earth-launched; tent sublimation's phi is an order of magnitude past the threshold. R71 extracted Tables 1-3 and A1 (now in `22_prior_art_techno_economic_benchmarks/extracted_data/`).

## Round 16 - yun_2023 [T1, hosted, CC BY-NC]

KSPE 27(2):45-59: reusable-LV table (engines, total thrust, fuel): Starship 7342 (Raptor x33 + x6; the unit is tf, not kN: corrected 2026-09-26; 230 x 33 = 7590 as printed), New Glenn BE-4 x7, first stage up to 25 flights. No payload or $/kg columns.

## Round 32 - SLS payload anchors (both hosted)

- **askins_2021_sls_janaff_update** (NTRS 20210016306): Block 1B Cargo LEO 105 t (231.4k lbs) = our `payload_leo_kg` exactly (row priced at $39,048/kg); footnote "Low Earth Orbit (LEO) represents a typical 200 km circular orbit at 28.5 degrees inclination"; TLI B1B Cargo >46 t / 42 t, B1 >27 t; ladder B1 95 t, B2 130 t.
- **nasa_esd30000_sls_mission_planners_guide** (ESD-30000 Rev A, NTRS 20190000736): Block 1 LEO "more than 209,439 lbm (95 t)"; EUS "up to 88,185 lbm (40 t) of payload delivery to lunar vicinity"; defines what "payload" means for SLS rows. R99: the 8.4 m PLF Short volume 21,930 ft3 = 621 m3, upstream's Block 1B value exactly. `r70_nasa_esd30000_table4_1_payload_vs_c3.csv`.

## Round 33 - Falcon 9 cost anchors (both hosted)

- **zapata_2017_cots_crs_lcc_assessment** (NTRS 20170008895): Falcon 9 development ≈ $390M ($300M F9 + $90M Falcon 1), "NASA has verified these costs", vs NAFCOM's $1.7B–$4.0B ("the cost model predicted that the Falcon 9 would cost $4.0 billion based on a traditional approach"); recurring cost per kg delivered to ISS (2017$) SpaceX $89,000, Orbital ATK $135,000, Shuttle what-if ~$272,000. R72 Tables 5-6: Shuttle what-if 1 to 5 MPLM flights a year costs $5,046M to $6,640M ($/kg 364,582 → 95,943); amortized non-recurring adds $28,213/kg (Antares/Cygnus), $23,850 (Falcon 9/Dragon), $34,322 (Shuttle); NASA cargo investment $953M (Table 5) vs 437 + 495 = $932M (Table 6), unreconciled. `r72_zapata_2017_cots_crs_tables5_6_cost_data.csv`.
- **webb_2016_is_it_worth_it_reusable_econ** (ICEAA 2016, NTRS 20160013370): NASA PCEC Launch Services ROM estimator (M15$ per launch, read by word coordinates): GEO <3,000 kg $120M / >3,000 $140M; Planetary <1,000 $80M / 1,000–2,000 $110M / >2,000 $175M; Polar $55M / $85M / $130M; Lunar <500 $85M / >500 $160M; LEO <500 $40M / >500 $80M; Helio $100M. A flight price, not a $/kg.

## Round 34 - zapata_2017_state_of_play_us_space_systems [T2, hosted]

FISO seminar, Oct 11 2017 (NTRS 20170009967), p15 "Maximum Payload Capability of Launcher, kg to LEO, 200km/28.5 circ." (word coordinates):

| vehicle | chart LEO kg | our row | match |
|---|---|---|---|
| Delta IV Heavy (NRO) | 28,790 | 28790 | exact |
| Atlas V 551 | 18,856 | 18850 | 0.03% |
| Falcon 9 (all customer classes) | 22,800 | 17400 (reusable) | family ceiling |
| Falcon Heavy | 63,800 | 57000 (reusable side cores) | expendable rating |

Same page (2017$): Falcon 9 private ~$2,719–$4,232/kg, Delta IV Heavy $8,644/kg, SLS no-EUS $54,627/kg. Vulcan and New Glenn postdate it. `r70_zapata_2017_state_of_play_launch_prices.csv`.

## R51 / R52 - NASA OIG SLS audits (hosted)

**IG-22-003** (`nasa_oig_2021_ig-22-003_artemis_missions`, Nov 15 2021): "the single-use SLS will cost $2.2 billion to produce"; KSC ground systems "$568 million per year"; "$4.1 billion per launch for Artemis I through IV"; Orion ~$1 billion plus $300 million for the ESA service module. The SLS Block 1 note's ~$4.1B (rocket + ground + Orion, not a launch price) and $2.2B + $568M match exactly. RL10 "$10.8 million each" (p32, fn54).

**IG-24-001** (`nasa_oig_2023_ig-24-001_sls_epoc_transition`, Oct 12 2023): Block 1B "at least $2.5 billion to produce", excluding SE&I; "more than $2 billion through the first 10 SLS rockets produced under EPOC"; 50% savings "highly unrealistic". Table 1 per Block 1B launch: EUS $482M + stages ~$1.0B + boosters $336.2M + RS-25 $582.7M + RL10 $68.9M + USA $19.9M = $2,489.7M; contract value $20.4B. Shuttle operations "increased approximately 38 percent to $1.45 billion per launch" (p23; −3.3% vs the note's ~$1.5B); Falcon Heavy for Europa Clipper "$178 million" (p24; +15.6% vs our $154M centre). EPOC could reach $25B over 10 launches; Artemis $93B FY2012-FY2025; Orion contract $3.9B → $13.8B; Atlas V base price up ~$50M then down ~$30M once Falcon 9 competed.

R70 correction of R52: Table 1 is per launch, so RL10 is ~$17.2M per engine per launch (~$25.7M by contract value), RS-25 ~$146M per engine per launch (~$150M by contract value), not $6.89M and $24.3M. With the OIG RL10 range $10.8-25.7M bracketing spacecost's ~$20M, and the implied Centaur III structure ~2,300-10,200 $/kg bracketing the 6000 (3000-25000) tank value, **rc-023 and rc-024 withdrawn**. `r51_nasa_oig_sls_shuttle_cost_key_numbers.csv`, `r52_oig_deep_dive_key_numbers.csv`.

Space Shuttle note "(Pielke & Byerly)": their work is Nature 472:38 (2011, DOI 10.1038/472038d), citing Space Policy Alternatives Ch. 14 (1992); no such paper in Environmental Science & Policy 2011. The $54,500/kg holds on jones2018.

## Round 58 - IG-20-012 and IG-23-015 (hosted)

**IG-20-012** (Mar 10 2020): "missed an opportunity to buy the hardware for a second ICPS for $29 million and instead plans to spend at least $42 million" (p23), the institutional point for the ~$30M Centaur III high end (+3.4%; hardware only, an ICPS unit); "first ICPS flight unit and associated structural test unit cost $46 million" (p36); Artemis I ICPS spend $358M vs $157M at KDP-C 2014; follow-on contract $527M by Oct 2019; task orders $5M → $377M; "more than $500 million on EUS development". Table 5 booster years sum to 2,878 vs printed 2,849 and FY2021 to 2,288 vs 2,257 (kept as printed).

**IG-23-015** (May 25 2023): RS-25 "estimated manufacturing cost per engine, after Artemis VI, is $70.5 million" vs Shuttle-era $104.5 million; $2.3B overhead excluded from the 30% savings; "$13.1 billion through 2031 on boosters and engines"; "$144 million through Artemis IV, increasing a single Artemis launch to at least $4.2 billion". R72 Tables 2-5: RS-25 CLIN 3 award fees reconcile ($32,305,787 final; 31.25% of $28,752,150 = $8,985,047, questioned $19,767,103); Boosters PLI $253M REA / $224.5M paid / $24.5M questioned. `r72_ig23015_tables2_5_award_fees_questioned_costs.csv`.

## R69 - nasa_oig_2022_ct-2022-01_artemis_status_testimony [T2, hosted]

Jan 20 2022: "$53 billion on the Artemis program between fiscal years (FY) 2021 and 2025"; fn1 $93 billion FY2012-FY2025; fn2 scope: "The $4.1 billion total cost represents production of the SLS, Orion, and ground operations ... does not include money spent concurrently on the development of next-generation technologies such as the SLS's Exploration Upper Stage, Orion's docking system, or Mobile Launcher 2". Vehicle-only $2.65B vs IG-22-003's $2.2B + $568M = $2.77B (−4.26%, in band). ABC exceeded by at least 33% at end FY2019 (43% projected by Nov 2021); >$17B on SLS by end FY2020 (~$6B untracked); PPE +$78.5M since May 2019.

## Maintenance (2026-09-26) and R70-R73 extraction

- Backfill rows in `extracted_data/backfill_2026-09-26_key_numbers.csv` (askins, esd30000, both Zapata papers, webb, IG-20-012, IG-23-015, CT-2022-01, yun).
- R70 files: `r70_askins_2021_sls_janaff_update.csv`, `r70_hf_dataset_full_table.csv`, `r70_jones2018.csv`, `r70_jones2018_table_a1_launch_cost_history.csv`, `r70_nasa_esd30000_sls_mission_planners_guide.csv`, `r70_nasa_esd30000_table4_1_payload_vs_c3.csv`, `r70_nasa_oig_2020_ig-20-012_sls_program_costs_contracts.csv`, `r70_nasa_oig_2020_ig-20-012_table1_sls_contracts.csv`, `r70_nasa_oig_2020_ig-20-012_table5_sls_costs_by_fy.csv`, `r70_nasa_oig_2021_ig-22-003_artemis_missions.csv`, `r70_nasa_oig_2021_ig-22-003_table1_artemis_phase1_funding.csv`, `r70_nasa_oig_2021_ig-22-003_table2_artemis_cost_fy2012_2025.csv`, `r70_nasa_oig_2021_ig-22-003_table4_artemis_contracts.csv`, `r70_nasa_oig_2022_ct-2022-01_artemis_status_testimony.csv`, `r70_nasa_oig_2023_ig-23-015_booster_engine_contracts.csv`, `r70_nasa_oig_2023_ig-24-001_sls_epoc_transition.csv`, `r70_nasa_oig_2023_ig-24-001_table1_block1b_contracts.csv`, `r70_terzi_nicoli_2026.csv`, `r70_webb_2016_is_it_worth_it_reusable_econ.csv`, `r70_yun_2023.csv`, `r70_yun_2023_table2_reusable_vehicles.csv`, `r70_zapata_2017_cots_crs_lcc_assessment.csv`, `r70_zapata_2017_state_of_play_launch_prices.csv`, `r70_zapata_2017_state_of_play_us_space_systems.csv`.
- Jones 2018: the abstract's ~54.5 k$/kg uses $1.5B per launch; Table A2 gives 61.72 k$/kg ($1,697M 2018$ / 27,500 kg).

## R74 - Upstream citations registered (+25)

Queue rows for `launch_vehicles.csv`: `pielke_byerly_2011_shuttle_programme_lifetime_cost`, `nasa_oig_2024_ig-24-015_sls_block_1b`, `satbase_2026_spacex_falcon9_price_increase`, `voyager_technologies_10k_2026_starship_contract`, `spacex_falcon_payload_users_guide`, `ula_rocketbuilder_and_published_pricing`, `blue_origin_new_glenn`, `rocket_lab_form_10q_fy2026_q1`, `glavkosmos_tass_2018_soyuz_price`, `isro_nsil_launch_pricing_and_user_manuals`, `cas_space_2026_kinetica2_price_per_kg`, `esa_ariane6_overview`, `jaxa_h3_launch_vehicle`, `firefly_alpha_published_price`, `isar_aerospace_spectrum_price_target`, `wikipedia_launch_vehicle_articles`, `spacenews_launch_reporting_2024_2026`, `spaceflight_now_launch_reporting_2025_2026`, `nasaspaceflight_launch_reporting_2025_2026`, `satnews_2026_artemis_restructuring`, `the_week_2026_isro_pslv_reporting`, `casc_long_march_9_10_disclosures`, `pearson_1979_anchored_lunar_satellites`, `eubanks_radley_2016_lunar_elevator_scientific_return`; and `musk_2018_falcon9_upper_stage_cost_statement` (moved to d21 in R77).

## R99 - Fairing sources (+31)

spacecost v0.5.0 `fairings.py` cites ~28 user guides for 42 `fairing_volume_m3` cells; all registered.

- Hosted: `atlas_v_launch_services_users_guide_rev11_mar2010` ("cleared for public release ... placed in the public domain"; Fig. 6-4).
- Verified live, not hosted (copyright, or a mirror): `vulcan_launch_systems_users_guide_oct2023` (Fig. 4.3.1-1), `ariane6_users_manual_issue2_rev0_feb2021`, `vega_c_users_manual_issue0_rev0_may2018`, `minotaur_iv_v_vi_user_guide_release_2p5_nov2025`, `pegasus_user_guide_release_8p2_sep2020`, `mhi_hii_users_manual_yet04001_ver4_feb2015` (H2A204 GTO 5,950 kg), `soyuz_csg_users_manual_issue2_rev0_mar2012`, `ariane5_users_manual_issue5_rev1_jul2011`, `boeing_delta_iv_technical_summary_payload_fairing_envelopes` (p3 Heavy 5-m row: 1194-5 PAF, 62.7 ft / 19.1 m, upstream's SLS Block 1 reference), `starship_users_guide_rev1p0_mar2020`, `new_glenn_payload_users_guide_rev_c_oct2018` (text "at least 450 m3 (16,000 ft3)" vs upstream's figure-read 458 m3), `electron_payload_users_guide` (v8.0 geometry unchanged from the cited Jun 2022 7.0: standard-fairing profile 566.1 / 717.0 / 868.0 ... mm station for station), `neutron_payload_users_guide_v1p0_jan2025` (proprietary, never commit), `alpha_payload_users_guide_v2p0_aug2019`, `khi_h3_payload_fairings_page` (S 10.4 m / L 16.4 m, 5.2 m dia), `mhi_technical_review_vol58_no4_h3_development_status_dec2021` (W fairing ~16.4 m, 5.2 → 5.4 m).
- `spacex_falcon_payload_users_guide`: the live PDF is Rev 8 (March 2025), newer than upstream's Sep-2021 citation; Fig 12-5's static-envelope dimensions (4,572.5 / 6,818.9 / 11,363.5 mm) are vector graphics, not in the text layer.
- Registered, not pulled: Saturn V SM-47274, Vega UM Issue 4, ISRO GSLV MkIII page ("PLF Usable Volume 110m3"), `orienspace_gravity1_fairing_100m3_tencent_news_2023` ("100 cubic metres"; corroborated: 4.2 m x 9.3 m per Xinhuanet), CALT LM-2C, CGWIC LM-3A, Galactic Energy Ceres-1 / Pallas-1, the LM-5 and LM-10B fairing reports, SKYLON Users' Manual.

No candidate: every fairing cell traces to the document that draws it.

## Round 103 - nasa_oig_2024_ig-24-015_sls_block_1b (hosted)

Block 1B development ~$5.7 billion before Artemis IV (2028), $700 million above the ~$5 billion ABC; Boeing's EUS contract $962 million (2017) → over $2 billion, ~$2.8 billion by 2028; >$3 billion since FY2014 without a baseline; $26M/month EUS burn Feb-Aug 2023. Pre-cancellation context for the Block 1B row (cancelled Feb 2026). `r103_oig_ig-24-015_sls_block1b_key_numbers.csv`.

## R114 - nasa_oig_2026_ig-26-004_hls_contracts

HLS: $6.9B obligated since 2019, $18.3B through FY2030 (pp 3, 7); SpaceX ~$3B (July 2021) + ~$1B option (Nov 2022), ~$4.3B, grown 6%; Blue Origin ~$3.1B (May 2023), grown under 1%. Development contracts, context only. `extracted_data/r114_gr_links_key_numbers.csv`.

## R115 - Pegasus XL (rc-078)

Zapata 2017 prices Pegasus XL for NASA LSP (ICON) at $56M (2017$) for 443 kg ($127,088/kg) vs the row's $40M: rc-078 (28.6%). Delta IV Heavy NRO $336M (2017$) = $453M at rc-052's factor vs $440M (−2.9%). `extracted_data/r115_zapata_pegasus_price_check.csv`.

## R117 - Ariane 6 and H3 prices (rc-080)

- `esa_ariane6_overview` (read live): payloads only ("Ariane 62 ... 4.5 tonnes into geostationary transfer orbit or 10.3 tonnes into low Earth orbit"; A64 11.5 / 21.6 t), zero price figures, so the notes' "€100M (2024 est.)" and "€115M (2018 est.)" are misattributed (the class of rc-079).
- `arianespace_ariane6_vehicle_page` (new): no list price; prices are contract-negotiated. rc-080 (citation).
- `jaxa_h3_launch_vehicle`: bot-walled; the ¥5B H3-30 target unverified.

`extracted_data/r117_esas_ariane6_price_check.csv`.

## R120 / R126 / R127 - Queue rows read live

- `eubanks_radley_2016_lunar_elevator_scientific_return` (arXiv:1609.00709, default licence): "A Lunar Space Elevator (LSE), however, can be built with current technology using commercially available tether polymers."
- `satbase_2026_spacex_falcon9_price_increase`: "SpaceX has increased Falcon 9 launch pricing to $74 million and raised rideshare rates to $7,000 per kilogram" (Feb 28 2026).
- `cas_space_2026_kinetica2_price_per_kg` (SatNews 2026-04-02): competitive standard "approximately $7,000 to $11,000 per kilogram for medium-lift vehicles".
- `wikipedia_launch_vehicle_articles`: the comparison table has no price column, so the notes' "Source: Wikipedia" prices are weaker than they read.
- `russianspaceweb_angara_a5_14s746_fairing_zak`: 14S746 fairing "17.705 meters, a diameter of 4.35 meters and a mass of 2.28 tons" (fifth flight, 2025-06-19).
- `satnews_2026_artemis_restructuring` (Feb 27 2026): "The agency will cancel the planned Block 1B upgrade of the Space Launch System (SLS)"; Artemis III a mid-2027 LEO docking flight.
- Located via search index only: `the_week_2026_isro_pslv_reporting` (C-61 and C-62 third-stage failures, losses "$200 million to $250 million"); `spacenews_launch_reporting_2024_2026` on Atlas V mission assurance ("$30 and $80 million more"; baseline $109M vs historical $184M).

## R128 - SEC filings (rc-081, rc-082)

EDGAR works with curl and a contact User-Agent (accession dashes stripped in the path). All four filings read in full, hash-recorded, not hosted. Mid-round, spacecost@d799cba applied rc-030, rc-050, rc-051 and rc-052 without touching these rows. `extracted_data/r128_sec_filings_key_numbers.csv`.

- `voyager_technologies_10k_2026_starship_contract`: one "Starship" mention, no dollar figure.
- `voyager_technologies_424b4_prospectus_starlab_commitments` (new; Jun 11 2025): "a commitment for one launch at a future estimated launch date for $90.0 million" (as of March 31 2025); cancellation would cost $13.5 million. **rc-082** (citation): cite the prospectus, not a 2026 10-K.
- `rocket_lab_form_10q_fy2026_q1`: "revenue per launch was $9.3 million and $7.1 million" (Q1-2026 / Q1-2025), cost per launch $5.4M / $5.7M; no $7.5M anywhere. **rc-081** proposes $9,300,000.
- `spacex_spcx_ipo_registration_statement` (new; S-1): Space segment FY2025 revenue $4,086M; Starship R&D $930M (Q1-2026) and $3,004M (2025); Falcon launches 134 → 165; "average price per launch remained relatively flat"; F9 v1 ~$2,700/kg vs the historical $18,500/kg; Starship goal to cut cost to orbit by 99% or more.
- `spacex_spcx_10q_q2_fy2026` (new): Falcon launches 37 / 45 (Q2-26 / Q2-25), 77 / 81 (H1), customer launches 10 / 9 / 17 / 21; H1-2026 revenue $12,508M vs $8,138M.

## R132 - nasa_nsts_21492_space_shuttle_payload_bay_users_guide (hosted)

US government work, 255 pp: "The maximum payload dimensions by design are 720 inches (18.46 m) long by 180 inches (4.6 m) in diameter, or a volume of 10,600 cubic feet (306.6 m3)." The inches give ~300 m3 and 10,600 ft3 = 300.2 m3, bracketing upstream's 300.0; upstream's note on the inconsistent metric pair is right. `extracted_data/r132_sts21492_fairing_key_numbers.csv`.

## R164 / R165 - Candidates (2026-10-14)

rc-119 (cite Zapata 2017 for the Delta IV Heavy and Atlas V 551 payloads), rc-128 (Falcon 9 expendable band at escalated LSP/GPS prices $124M and $131M), rc-129 (Falcon Heavy expendable low end escalated to $202M), rc-130 (cite Zapata for the Delta IV Heavy price, $453M escalated). Texts in `revision_candidates.csv` (open) and `revision_candidates_closed.csv`; `extracted_data/r165_launch_prices_escalated.csv`.

## Round 175 - glavkosmos_tass_2018_soyuz_price

tass.com/science/1024055 (Oct 3 2018): "The basic price to launch Russia's Soyuz-2.1 carrier rocket with the Fregat booster will stand at about $48.5 million"; without Fregat about $35 million; 1 kg "$20,000-30,000". Extraction only. `extracted_data/r175_soyuz_price_key_numbers.csv`.

## Round 187 - Upper-stage cost row (rc-170)

`operational_costs.csv` 'Expendable upper stage recurring cost' is the only row with no CITATIONS.md entry: '~$10M (Musk 2018)' unlinked, '~$7M (2026 third-party estimate)' unnamed, 'Centaur III, ~$30M' sourced nowhere, and the tank row derives from it. SP-4176 has programme costs only. **rc-170** (citation). Detail in d03 (`03_dv_propulsion/extracted_data/r187_centaur_cost_history_key_numbers.csv`).

## Round 188 - H-IIA 204 price (rc-171)

The row's $90M carries "JAXA/MHI pricing" with no document. JAXA: "the cost was reduced by almost half, down to 9.3 billion yen (H-IIA F4)"; MHI Tech Report Vol. 39 No. 1: below 8.5 billion yen per unit, Table 3 standard type 75-85 hundred million yen at $=JPY 120 ($62.5M-$70.8M); The Space Review (Mar 7 2023): "about 10 billion yen (about $75 million)". At the World Bank's 2024-2025 official rates these are $61-75M; $90M needs JPY/$ ≤ 111.1, last seen in the annual series in 2021. **rc-171** (value): ~$68M [$62M, $75M] in 2026 dollars, with the yen figure and rate in the notes; vehicles.py duplicates the value. `extracted_data/r188_hii_price_key_numbers.csv`.

Exchange rates: `23_cost_indices_dollar_years/extracted_data/r188_usd_jpy_official_rates_key_numbers.csv`.
## Round 196 - spacecost README contract verified against live v0.12.0 tables (2026-10-19)

Evidence-only sweep of the spacecost README (rewritten at bda6415 "README carries the current answer", shipped close after v0.12.0); no new sources, no RC opened - every quantitative claim re-measured on live tables reproduces exactly:

- Status counts 48 operational / 12 development / 9 concept / 7 retired exact; Pegasus XL $143,722/kg, lunar mass driver $10/kg and New Glenn $1,922/kg (status=operational, availability=open) all match their rows.
- LEO anchor claim: leo_anchor_candidates() ranks published/contract-basis operational rows only; Falcon Heavy (expendable) wins at exactly $2,555/kg as documented, and the import-time assert means any table edit that flips the winner fails loudly - structurally unrottable while imports succeed.
- Propellant table: 15 distinct types, 8 storage classes exact; isp min 70 s (cold gas); largest FINITE isp is exactly 1e5 s (Antimatter-catalysed) matching "speculative concepts at 10^5 s" - the inf rows are propellantless sails and a tether, correctly excluded from that claim.
- Environments: 23 rows; au_mean spans 0.3871 (Mercury orbit) to 5.2044 (Jupiter Trojans L4/L5), matching "spanning 0.39 to 5.20 AU, from Mercury orbit to the Jupiter Trojans".
- Shuttle row: centre $972M with band [450M, 2.1B]; documented midpoint arithmetic ($1.28B) exact.
- Lunar-night cluster reproduces from stored values exactly: dark_period_hr = 354.35 ("354 hours"); ratio to the LEO row's stored 0.5871 h is 603.6 ("604 times"); battery mass 100 W x 354.35 h / 104 Wh/kg usable = 340.7 kg, quoted "341 kg"; the 104 Wh/kg usable row exists in OPERATIONAL_COSTS as cited (130 system-level x 0.80 DoD).
- Fairings: New Glenn 458 m3 and SLS Block 1B (Cargo) 621 m3 exact; FILL_RATIOS range Atlas V 0.2678 to Alpha 0.6305 matches the documented 0.27-to-0.63 calibration span.
- Tank physics prose reproduces: stored densities LH2 0.0708 / kerolox 1.0153 give the quoted fourteen-fold volume ratio per kg; with the colder storage class priced, 14.3 x (0.0375/0.0273) = 19.6 - "twenty times the tank" exact as stated on single-propellant semantics; mixture-aware hydrolox fraction ((6/7)/rhoLOX + (1/7)/rhoLH2) x 0.0351 kg/L = 9.7 percent reproduces the Centaur anchor to the digit. Semantics recorded so a future auditor does not mis-flag them against naive per-propellant arithmetic.
- Didymos "a factor of 5 in available power": stored au_min/au_max ratio squared (2.2758/1.0128)^2 = 5.04 - the claim is about POWER and says so; distance ratio alone would be 2.25, which is not what it asserts.
- Delivery surfaces: lander $200k/kg = STAGE_HARDWARE_USD_PER_KG[0.2] exact; aeroshell $50k/kg = ENTRY_SYSTEM_USD_PER_KG exact.

Corpus-level note: this is the second consecutive repo whose user-facing prose re-measures exactly against its own tables (AsteroidCatalog README at Round 195); both findings so far came from data-vs-data comparisons instead - upstream docs discipline holds under adversarial re-measurement, and RC hunting should keep prioritising cross-table and convention seams over prose claims. This surface is covered; skip unless the README or v0.12.x tables change.

**Round 208 - Northrop Grumman Propulsion Products Catalog registered; rc-179 opened.**

The economicspace MODEL.md propellant-tankage table asserts "Star 48B measures 6.4%" with no source named anywhere upstream. The manufacturer catalog (public release OSR No. 16-S-1432, dated 05 April 2016; 9752514 B sha 5b52adf1) gives both flight-proven variants on pp.102-103: propellant load 4,431.2 lbm identical across variants [appears twice], total inert 274.2 lbm (TE-M-711-17 short nozzle) and 289.6 lbm (TE-M-711-18 long nozzle). Inert-over-propellant = 6.19% / 6.54%, mean 6.36% - the printed 6.4 is true within variant spread but uncited; rc-179 proposes the citation, no number change.
Sister context: spacecost APCP class anchor prints 6.9% (reproduces from pinned rows per Round 197) - conservative above both measured variants.
This surface is covered; skip unless a new catalog edition appears or the MODEL.md row changes.

**EC README quantitative contract swept clean (Round 225, skip unless the README moves):** every current-state claim at `be86297` reproduces — module version table versus versions.md Current-versions heading and verify_docs check 2; the seven-place spacecost pin enumeration is exactly four code pins plus three named prose mentions (requirements.txt URL, build_master _MASTER_PIP_SPEC, transportation and mineral_value _PIP_SPEC); insurance dial description mirrors master.py default 1_500_000 dollars liability flat with charge_insurance off since calc v1.20.0; steam-versus-hydrolox water feed ratios reproduce arithmetically (WATER_KG_PER_KG_HYDROLOX = 9.0 times hydrogen fraction one-seventh gives hydrolox 1.286; steam is feed-as-is at 1.00); runtime tables are dated historical records exempt per the R210 precedent. Known open exceptions live under rc-176 (output-block size figure) and rc-183 (destinations currency). Related closure: AC CITATIONS.md has four sections; sweep-history references to a section five were misnumbered, and all five named upstream data sources in section 1 have registry rows.

**spacecost CITATIONS.md fully swept work-level at R231; skip unless its source tables change:** all ten sections resolved against sources.csv. Section 1 provider table maps to specific ids (IG-24-001 = the Oct-2023 OIG audit beside IG-22-003, identified by hosted path /uploads/2023/10/ig-24-001.pdf; rocket_lab_form_10q_fy2026_q1 read at R128). Section 3: taylor2018, elvis2011, curtis_orbital_mechanics_engineering_students, dra5_2009 + drake_2008 (SP-2009-566), sp4029 Orloff; NTRS/JPL design-handbooks line = generic class pointer per prose-pointer convention. Section 4: autonomy row claimed by open rc-106, refinery throughput row by open rc-178, remainder resolves (jpl_dsn_services_catalog_820_100, damodaran_cost_of_capital_by_industry, planetary_society_pebd_mission_costs, IG-23-010, frieman_2021, kleinhenz_paz pair, MIL-HDBK-189C). Section 5 every input named has a dedicated row; sections 7 to 10 tooling and meta class - documented NOT registered (quietqueue precedent R222).


## Round 245 - Atlas V LEO band re-anchored to the hosted Rev 11 user guide

The Atlas V row note declares its own LEO figure unsourced ("whose own source is not recorded"). The GR-hosted Rev 11 Launch Services User Guide (cleared OSR 10-S-0689, pulled live at R99) settles it: Table 2.6.5-2f prints the Single Burn figure at 200 km as Payload Systems Weight 18,814 kg [41,478 lb], conditions CCAFS SLC-41 with the 5-m Short fairing, park orbit perigee at least 167 km, confidence level 2.33 sigma GCS - exactly the band low end upstream carries. A full-document scan of all 420 pages finds zero occurrences of 18,850, so the high end matches nothing in the guide; rc-189 cites the table and asks for the upper figure to be adopted away or documented. PSW semantics (adapter included) are flagged in the proposal.


### Round 247 (2026-10-23): PSLV failure record moves onto ISRO mission status pages (rc-191)

INDEX replace-flag for the_week_2026_isro_pslv_reporting named two institutional replacement classes: NSIL price statements and ISRO
failure-analysis releases. The second class is now resolvable at primary level from this machine: www.isro.gov.in serves both mission status
pages live (apex domain fails DNS here; the www host answers). C61 page states "Due to an observation in 3 rd stage, the mission could not be
accomplished" and flight-63/XL-count context; C62 page states the PS3 anomaly sentence verbatim with no failure verdict. The launcher list marks
C61 Not accomplished but carries no outcome mark for C62 - so the institutional record supports a failure statement for C61 only, plus an
initiated-analysis status for C62. Upstream causal clause (flight control near stage separation) is committee/news-level detail not on these pages;
rc-191 proposes citing the three registered T3 rows and restating to institutional wording. The pricing half of the flag stays open: nsilindia.co.in
(carved-out domain, resolves where nsil.isro.gov.in does not) publishes no tariff PDF in launch-services or brochures pages, and the 60-page ISRO
Space-in-Parliament compendium carries zero per-launch unit-cost statements.

**Round 248 - Vega C payload cells move onto the guide that already carries its fairing citation**

Owner replace-flag wikipedia_launch_vehicle_articles executed for the Vega C row. The Arianespace Vega C Users Manual Issue 0 Rev 0 (May 2018) was re-fetched live from ariane.group and byte-matches the R99 access_status record exactly (sha in r248 key-numbers file). The guide publishes its payload figures as text at exactly two points: Table 2.4.2.a polar orbit 500 km at inclination 88 deg = 2,250 kg including adapter, and the section 2.4.3 equatorial elliptical statement of 1,700 kg at apogee 5,700 km - both spans count==1; SSO performance exists only as Figure 2.4.1.e chart (rendered reading about 2,150 to 2,250 kg at 700 km, axes capped at 2,700 kg). Consequences recorded in rc-192: the row low end of 2,250 kg is confirmed directly by the manufacturer document (vehicles.py comment "500 km polar" matches Table 2.4.2.a), while the 3,300 kg high end occurs zero times in all 118 pages and exceeds even the chart ceiling; stored headline LEO of 2,720 kg is above every circular-orbit figure this guide publishes; single-point anchoring at 2,250 kg moves usd_per_kg_to_leo from 16580.88 to 20044.44 (+20.9 percent) at the unchanged price cell. GTO stays zero - no GTO capability statement exists in the document. Vision backend recovered this round (single chart render passed), so the Figure 2.4.1.e reading is recorded with a chart-reading flag; future rounds: Vega C row mined at text and chart level, do not re-open except on manual revision.

**Round 249 - Minotaur IV payload figures traced to Wikipedia infobox with orbit parameters dropped upstream**

The row cites Wikipedia for price and the NG guide for fairing volume, but the three payload numbers (headline 1660 kg, band [1591..1735]) are attributed nowhere. Live fetch today shows en.wikipedia.org Minotaur IV infobox stating Capacity Payload to LEO Altitude 200 km (120 mi) Orbital inclination 28.5 deg Mass IV: 1,591 kg (3,508 lb) - the stored low end matches exactly and wiki supplies orbit parameters that upstream dropped; wiki itself cites the NG guide for its sub-orbital figure. Guide Release 2.5 was re-fetched byte-identical to R99 with the registered sha and its text layer holds zero occurrences of any stored number: all Minotaur IV performance is curves only, Figures 3.3-1 and 3.3-2 fleet comparison for SSO out of KLC/PSCA and 28.5 deg inclination out of CCSFS plus per-site Figures 3.3.1-1 through 3.3.1-4. The section 3.3 definition (count==1) says curve values are total mass above the standard, non-separating interface with separation system and any payload adapter included in the payload allocation - a different convention from satellite-mass semantics. High end 1735 kg is found in neither current Wikipedia nor guide; headline 1660 differs from its own band midpoint 1663, violating the v1.16.0 centre policy by 3 kg. Only prose capability figure in the whole guide belongs to Minotaur VI+ (3360 kg), count==1. rc-193 records all of this; chart digitisation of Figures 3.3-2/3.3.1-x deferred - vision backend timed out twice this round, so no curve values were read.

**Round 250 - Electron capacity sentence traced into the guide that already carries its fairing citation; high end 320 unsourced**

The row attributes price to Rocket Lab Form 10-Q FY2026 Q1 and fairing volume to Payload User Guide v7.0 p26, but the sentence Current published capacity 300 kg LEO / 200 kg SSO names no document. The registered guide (re-fetched live byte-identical to the R99 record) publishes both figures as verbatim text: two prose spans for up to 300 kg / 660 lbm LEO and a specs block span NOMINAL PAYLOAD 200 kg / 440 lbm To 500 km SSO, each count==1; the performance section adds Electron is designed to place payloads of up to 200 kg into a circular SSO at 500 km altitude (count==1) on a page that prints legacy footer Launch: Payload User Guide V 7.0 inside the v8.0 file, consistent with upstream citing the earlier edition for identical content. The stored band high end 320 kg exists nowhere in the document as a mass figure - zero occurrences of 320 kg / 310 kg / up to 320 across all 72 pages; bare 320 appears only as fairing millimetre dimensions and standalone 310 is an axis tick on the Elliptical Orbit Payload vs Apogee chart. Arithmetic: payload headline equals its band midpoint (310) so the centre policy holds there, but price headline 8130000 deviates -0.854 percent from midpoint of its own [7100000..9300000] band; usd_per_kg_to_leo=26226 is consistent with stored cells (8130000/310). Single-point re-anchor at the published 300 kg moves usd_per_kg_to_leo to 27100 (+3.3 percent) - recorded in rc-194 for adjudication together with a proposal to cite the guide directly and to document or drop the unsourced high end.

**Round 251 - band_centre is GEOMETRIC mean to 3 significant figures; full-table audit finds zero violations and voids three arithmetic-midpoint observations of my own**

Reading spacecost/vehicles.py at b5eb32a for the centre-policy statement before flagging anything exposed an error in how Rounds 248-250 framed internal consistency: v1.16.0 derives headline price and payload as band_centre(low, high) = float("%.3g" % sqrt(low x high)) clamped inside the band - "Geometric rather than arithmetic because launch prices and payloads are uncertain by FACTORS, not by fixed amounts" (docstring verbatim at L1981-1982). The docstring itself names the Atlas V narrow-band clamp case: 18,814-18,850 kg centres at 18,832 which rounds to 18,800 - exactly reproducing why rc-189 found the stored headline equal to the band low end. Reproducing that function exactly over all 152 banded headline cells in reference/launch_vehicles.csv gives ZERO violations: Minotaur IV sqrt(1591 x 1735) = 1661.4 -> 1660 stored; Vega C sqrt(2250 x 3300) = 2724.9 -> 2720 stored; Electron price sqrt(7100000 x 9300000) = 8125884 -> 8130000 stored - each an exact match to the documented centre. Consequence: the arithmetic-midpoint inconsistency observations recorded in rc-192 (band centre 2775 vs headline 2720), rc-193 (midpoint 1663 vs headline 1660) and rc-194 (price -0.854 percent below midpoint 8200000) were false positives of my own misreading; dated SELF-CORRECTION clauses have been appended inside those cells with all original text preserved, statuses remain open on their payload-provenance findings which are unaffected (unsourced high ends 3300 / 1735 / 320 stand). STANDING RULE for this domain: never test headline-vs-band consistency arithmetically; use band_centre() semantics exactly. That invariant holds perfectly across the table - no upstream value change is warranted by centre policy anywhere in launch_vehicles.csv.

## Round 252 (2026-10-25): Ariane 6 LEO payload bands - attribution and capacity currency (rc-195)

The A62 and A64 rows store LEO bands [10300..10350] and [21500..21650] kg with no document named for the payload column in either note. Re-fetching the ESA overview page (registered row esa_ariane6_overview) re-verified its two official figures verbatim count==1: A62 approximately 10.3 t and A64 approximately 21.6 t to LEO. The stored values sit on those points exactly - the A64 headline reproduces the official figure under the geometric-mean band_centre policy (fact #62) - but none of the three endpoints appears in any fetched document, formatted or bare: synthetic padding of the class documented for Vega C (rc-192), Minotaur IV (rc-193) and Electron (rc-194). The ArianeGroup VA269 launch kit dated 17 June 2026 (registered this round as arianegroup_va269_launch_kit_jun_2026) publishes the P160C booster upgrade raising official A64 capacity to approximately 22 tons LEO, above the stored band high end; no upstream file mentions it. The User Manual Issue 2 Rev 0 re-fetched byte-identical to the R99 copy and its text layer across all 171 pp carries no LEO mass figures at all (page 39 is a mission-phase timeline), so it cannot anchor the bands either. rc-195 proposed attribution plus currency restatement; price cells untouched.


## Round 253 (2026-10-25) - Saturn V LEO band provenance (rc-196)

Sixth instance of the unsourced-band-endpoint seam family (after Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195). Saturn V payload columns carry no document attribution upstream; two NTRS records now hosted here supply official provenance: press-kit statement 285,000 lb to LEO (= headline) and rated comparison figure 262,000 lb / 118.8 mT (= low end). The high end 140,000 kg matches no NASA document found; Skylab-era delivered mass was about 77 t in orbit.

Class-family status for future rounds: banded rows whose notes name NO payload document remain - Proton-M (Wikipedia only), Soyuz-5, Starship projected band [35000..100000], and several historical smallsats carriers; Soyuz-2.1a/2.1b rows do cite the CSG User Manual token - check that manual covers both variants before flagging. H3 24L carries a JAXA token (jaxa.gov WAF-blocked since R175).

## Round 254 (2026-10-25) - Vulcan Centaur LEO band provenance (rc-197)

Seventh instance of the unsourced-band-endpoint seam family (after Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195, Saturn V rc-196); the Round 253 class list did not yet include the three Vulcan rows. The R99 follow-up extraction is now complete: the registered Oct 2023 user guide (re-fetch byte-identical, sha in registry row) publishes all three stored Vulcan LEO figures in Table 2.2.1-1 for the ISS representative orbit at 407 km and inclination 51.6 deg - VC2S 16,300 / VC4L 21,400 / VC6L 25,600 kg, each span count==1; the strings 27,200 RL10E and upgraded Centaur have zero occurrences in all 85 pp. The VC6 band high end comes from a different ULA document: the one-page Vulcan Centaur technical summary sheet (registered this round as read-not-hosted), which defines LEO as a 200 km circular orbit at inclination 28.7 deg and prints the across-configuration capacity line 10,800 – 27,200 kg count==1; word coordinates map that line to the LEO label, separating it from the GTO range above. Wikipedia cites the same sheet URL for its infobox figure, so upstream notes of figures via Wikipedia resolve onto both documents once named - rc-197 proposes attribution and orbit-parameter restatement with no value change. Seam-family status: banded rows resolved so far are Vega C / Minotaur IV / Electron / Ariane 6 / Saturn V / Vulcan; remaining banded rows whose notes name no payload document include Proton-M, Soyuz-2.1a/2.1b (check CSG manual coverage first), Soyuz-5, Long March 12 and Kuaizhou-1A - next-round targets.

## Round 255 (2026-10-26)

Eighth instance of the unsourced-band-endpoint seam family (after Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195, Saturn V rc-196, Vulcan Centaur rc-197). The Proton-M row attributes its LEO capacity to Wikipedia only. Resolution is unusually clean because the document spacecost already cites for fairings — ILS PMPG Rev 7 (LKEB-9812-1990, July 2009) — publishes the payload figures itself: Table 2.2-1 Summary Proton M Performance (PSM) to Reference Orbits lists circular LEO at H = 180 km as 23.0 MT for i = 51.5 deg, 22.0 MT for i = 64.8 deg and 21.0 MT for i = 72.6 deg (three-stage Proton M; the Breeze-M column shows an em dash for LEO). Row-band word coordinates on PDF p.47 prove each label-value pairing rather than relying on reading order, and all three numbers match the stored headline plus both band endpoints exactly — unlike rc-197 no second document is needed because one table carries the whole range; the inclination qualifier (and the H = 180 km orbit definition) is what upstream drops.

Document facts for future rounds: PMPG Rev 7 fetched live from ilslaunch.com (20342733 B, sha256 18f4472216699242840e2a893685abade30cbfae266c501892d5355acafe4d32); running footer Cleared for Public Release Through OFOISR; no in-file copyright grant (page-2 revision notice records the DOD Office of Security Review case and supersedes Revision 6 dated December 2004). The guide text layer is searchable but the capability figures are plain text here, not image-only — earlier probes for comma forms (23,000 kg) failed because the table uses MT notation; future span work should search both formats. Khrunichev own site (khrunichev.ru) fails DNS from this machine (HTTP 000), same class as the UNSW NXDOMAIN case.

Noted for a later round, NOT opened here: upstream payload_gto_kg = 6600 matches none of Table 2.2-1 GTO rows (GSO 3250 kg; GTO with 1500 m/s to GSO 6150 kg at i = 23.2 deg Hp 4120 km; GTO with 1800 m/s to GSO 6920 kg at i = 31.1 deg Hp 2175 km) — the Wikipedia infobox carries 6,920 and 6,300 variants; a future round should trace which variant the stored figure intends before proposing anything.

## Round 256 (2026-10-26)

Ninth probe of the launch-vehicle payload seam family and a new class: data-vs-data inside upstream's own named source. The Soyuz-2.1a row cites Wikipedia payloads by launch site, and its stored band [6800..7430] reproduces that infobox exactly as Plesetsk-A (i = 72 deg) minimum and Baikonur-A maximum — but the same table prints Vostochny A = 7,460 kg at the identical 51.6 deg class, so the stored high end silently drops the cited source's own maximum by 30 kg while the note claims coverage across launch sites. rc-199 proposes either adopting 7,460 (headline 7120 via band_centre; usd_per_kg_to_leo $4557 to $4551) or stating a Baikonur-only selection rule. The -1b row is unaffected: Baikonur B 8,670 exceeds Vostochny B 8,600.

Third-site context extracted this round and recorded in the CSG manual registry row (closing its R99 flagged extraction follow-up): Arianespace prints Kourou LEO performance of 4,850 kg at Za = Zp = 920 km inclination 52 deg — far below the Baikonur figures because a 52 deg orbit from the equatorial site is high-energy; future rounds must not treat CSG manual performance numbers as comparable to Baikonur-based bands.

Stale-reference finding (documented, NOT registered): Wikipedia reference 19 for the payload sentence points at the STARSSEM Soyuz User's Manual, fetched live from starsem.com — it is dated April 2001 (ST-GTD-SUM-01 Issue 3 Rev 0; © Starsem 2001 All rights reserved; 8,855,821 B sha256 550768027ceb84a73c12a3643901e487d3c7617a37eb525e10fe0d54a8196064), predates the Soyuz-2 first flight and mentions neither the -1a nor any of these figures. Access failures dated for retry: khrunichev.ru fails DNS from this machine (HTTP 000); progress-tsma.ru connection failure; UNOOSA space-launch-vehicle pages return 404 on both legacy oost path and the current members path.

Next seam-family targets unchanged: Soyuz-5, Long March 12, Kuaizhou-1A.

## Round 258 (2026-10-26)

Tenth probe of the payload-band seam family, first with institutional Chinese sources reachable from this machine. The Long March 12 row attributes capacity to Wikipedia payloads; tracing both endpoints lands on named documents: low end equals the SAST design target reported by Straits Times Feb-26-2024 (span count==1) and high end equals the Xinhua background page at first flight carried on english.www.gov.cn Dec-1-2024. New wrinkle for this family: the official figure is a floor - no less than 12 tonnes in low Earth orbit - so using it as band maximum understates capability; rc-201 asks notes to say so and name the documents, values unchanged (headline reproduces geometric-mean convention at 11000; usd_per_kg_to_leo consistent at $5745). english.www.gov.cn answers plain curl with Chrome UA - unlike khrunichev.ru DNS failure and progress-tsma.ru failures logged R256. Xinhua also prints no less than 6 tonnes to a 700 km sun-synchronous orbit; upstream has no SSO column, recorded in the key CSV for context.

Skip-note: straitstimes.com serves full article HTML to plain curl (117 KB) - reachable witness class. Remaining family targets: Soyuz-5 (crew/uncrewed variant mix into one band, institutional sources DNS-blocked), Kuaizhou family (ExPace figures only).

## Round 259 (2026-10-26)

Eleventh probe of the payload-band family, this time on price cells: Kuaizhou-11 notes quote Wikipedia's rate (roughly $10,000/kg, i.e. ~$15M full) and the registered saved copy prints exactly that in its spec table ($10,000/kg ($4,500/lb), span count==1) - but the stored list_price_usd is $12200000 and usd_per_kg_to_leo 8133, so three numbers on one row disagree with each other; rc-202 [value] proposes aligning to the cited rate (price $15000000, per-kg $10000) or naming a different document. Payload side stays proven: prose 1,500 kg LEO equals stored payload_leo_kg exactly.

Noted NOT opened for a future round (single-candidate discipline): KZ-1A band [300..400] versus the same table printing 450 kg for KZ-1A Pro (first flight 4 Dec 2024, span count==1) and wiki prose itself inconsistent (400 in table vs 450 in upgrade sentence); also SSO figures exist that upstream has no column to receive: article prints KZ-1A 200 kg @700 km SSO and KZ-11 1,000 kg @700 km. Wikipedia family pages are dense spec-table witnesses: parse the table rows, not just infoboxes.

## Round 260 (2026-10-26)

Twelfth probe of the payload-band family and the resolution of R259's noted item: for Kuaizhou-1A the institutional record runs against the stored band ceiling. CASIC's own statement, carried by China Daily on Oct 27 2021 (saved copy sha in registry), prints official point values - SSO 200 kg and LEO 300 kg - exactly equal to the stored floor; the Gansu bureau report for the same mission says designed to launch low-orbit satellites weighing under 300 kg (count==1). The ceiling of 400 rests only on wiki table cells [20][21]; SpaceNews coverage that day attributes 660 pounds (300 kilograms) LEO to Expace, matching CASIC. rc-203 [citation]: cite both saved pages in notes with semantics recorded; no value change - headline 346 reproduces the geometric-mean convention exactly and sits 15.3 percent above the official point value.

Provenance map now complete for this vehicle: LEO floor = CASIC official (matches); ceiling = aggregator wiki cells (unbacked); per-kg rate $20,000/kg printed in the same wiki table and reproduced exactly by stored usd_per_kg_to_leo 20029; KZ-1A Pro at 450 kg remains an upstream content decision (new variant not listed), NOT a sourcing defect - R259 note stands. Chinese state media domains are reachable witnesses where the .gov.cn mirrors fail DNS: global.chinadaily.com.cn and its bureau subdomains both served plain curl with Chrome UA.

## Round 261 (2026-10-26)

Thirteenth probe of the payload-band family and its first pure SEMANTICS hit: for Nuri (KSLV-II) there is no numeric contradiction between upstream and its cited Wikipedia article - both print 3,300 kg to LEO - but the article ties that figure to an altitude of 200 km while KARI, the national agency that built the vehicle, states a 1.5-ton-class satellite to low Earth orbit at 600-800 km (and the same figure for sun-synchronous orbits at approximately that band; saved copies shas in registry). Upstream stores the single point unqualified, so usd_per_kg_to_leo $11121 prices a rocket at an orbit its own agency never claims for it: 2.2-fold capacity overstatement and roughly half the per-kg cost relative to institutional semantics (about $24467/kg on 1.5 t). rc-204 [citation]: cite both KARI pages, record the altitude qualifier; no value change - owner adjudicates column semantics.

Family learning: aggregator infoboxes carry orbit-altitude conventions that institutional statements do not share; when a stored LEO figure is single-point with no qualifier in notes, check whether its cited article ties it to an altitude the operator contradicts. Attribution-quality sweep of all 75 rows at spacecost@2bd5e20 (notes classified URL / named-doc / wiki-only / vague) now drives target selection from evidence rather than memory; remaining wiki-only queue after this round: Angara A5, Zhuque-2E and -3 (LandSpace self-published), Long March 10B/2D/4C/6A/7/8A, Gravity-1, Hyperbola-3, Jielong-3, Kinetica family, Soyuz-5 (institutional DNS-blocked class). Long March 5 corroborated: its stored 25 t matches the official near-Earth figure carried on gov.cn pages - documented here as consistent, no RC.

## Round 262 (2026-10-26)

rc-205 [citation] on Zhuque-3: two defects live in one note cell. First, mode semantics - the table convention is explicit mode rows (Falcon 9 reusable at 17,400 kg beside Falcon 9 expendable at 22,800 kg), yet this unqualified row stores only the down-range-recovery figure while its own note quotes expendable 11.8 t; usd_per_kg_to_leo $4425 therefore prices one mode silently (about $3000/kg at the expendable figure). Second, variant attribution - upstream says 21 t / 18.3 t belong to an enlarged ZQ-3E still in development; that split is Wikipedia-only: LandSpace own release calls the rocket Zhuque-3 (model code ZQ-3), gives full length 76.6 m and states expendable LEO capacity reaching 21.3 t with down-range recovery at 18.3 t (Chinese spans count==1, translation in registry rows). The Global Times debut report shows the flown vehicle stands 66.1 meters tall - a shorter configuration than the maker spec page carries those figures on. Proposal cites all three witnesses and records mode semantics; no value change.

Witness-class notes: english.news.cn served an EXPIRED TLS certificate from this machine (SEC_E_CERT_EXPIRED, 2026-10-26) - the Xinhua witness for the August flight is unavailable and not registered; landspace.com English pages are JS shells with zero static specs while Chinese news-detail pages serve clean server-rendered text - future LandSpace probes should go straight to news-detail.html itemids. Family status: mode/variant semantics joins altitude conventions as a recurring aggregator artifact in this table; remaining wiki-only queue after this round: Angara A5, Long March 10B/2D/4C/6A/7/8A, Gravity-1, Hyperbola-3 (i-Space domain DNS-dead from this machine), Jielong-3, Kinetica family, Soyuz-5.

## Round 263 (2026-10-26)

rc-206 [citation] on Angara A5: price cell was bare Wikipedia; the manufacturer financial disclosure exists and brackets it - BBC Russian quoting the Khrunichev 2019 report puts production cost at 7 billion rubles (about $108.1M at WB 2019 official rate, or $95.0M converted at 2021) against stored $100M - within five percent either way, citation moves and no value changes. Payload side fully corroborated: Khrunichev page quoted by BBC gives exactly 24,5 тонны (= stored 24,500 kg); a Roscosmos-quoted spec line reads the band 24 to 24.5 t; Interfax counted the Vostochny debut as the fourth A5 flight and upstream own fairing note names the Jun-19-2025 Plesetsk launch (the fifth) - five-flights claim reconciles against institutional tallies.

SYSTEMIC CONVENTION FINDING (do not re-litigate per row): every one of 76 rows in launch_vehicles.csv carries reference_year=2026 while thirteen notes state explicit source years from 2010 to 2023 - the field is a table-vintage as-of stamp, not a dollar-year; dollar-year RCs against this file belong only where conversion math itself is wrong (rc-171 class). Also recorded: Proton-M contract cost of 2.33 billion rubles per unit via RIA state procurement in the same BBC article (about $32.3M at WB 2020 rate) - institutional context for the Angara-expensive note; no Proton row exists upstream to attach it to.

Family queue after this round: Long March variants, Gravity-1, Hyperbola-3 (i-Space DNS-dead), Jielong-3, Kinetica family, Soyuz-5.

## Round 264 (2026-10-26)

rc-207 [citation] on Long March 5: the note clause attributing the stored LEO figure to the Long March 5B contradicts the institutional record - SCIO pages fetched live give LM-5 own capacity as 25 t to LEO and 14 t to GTO (CALT figures, span count==1) while the 5B official figure quoted from the same development team is 22 t. Stored values match LM-5 itself exactly; clause moves, no value changes.

SELF-CORRECTION of a Round 261 line: that block asserted “Long March 5 corroborated: its stored value of 25 t matches the official near-Earth figure carried on gov.cn pages” without ever fetching such a page - ungrounded at writing time, now superseded. The live fetch shows the attribution ran the other way than that sentence implied: 25 t is LM-5 own published capability and the upstream note misattributes it to the 5B; rc-207 carries the grounded finding.

WITNESS BANKED for future rounds (same SCIO family, seen via search snippets only this round - fetch and verify before use): Hyperbola-3 company targets of a 12.9-tonne LEO configuration and 8.5 tonnes in reusable mode per the Aug-2024 SCIO commercial-space article; Long March-8A approximate 7 t LEO plus at least 6.4 t to 700 km SSO and Long March-10 figures of 70 t LEO and 27 tonnes lunar-transfer per the Jan-2025 SCIO missions article - both against rows whose notes name no document (Hyperbola-3, Long March variants).

## Round 265 (2026-10-26)

rc-208 [citation] on Hyperbola-3: stored single point equals the reusable-mode capability (both witnesses agree at 8.5 t exactly), so the row prices recovery-mode payload while its own note concedes expendable 13.4 t - $/kg swing from $4988 to $3164 depending on configuration; propose mode-labelled rows per Falcon convention, no value change.

WITNESS CONFLICT recorded for adjudication: company statement via SCIO (Aug-2024) describes a 12.9-tonne LEO first-flight configuration while Wikipedia design specification says 13.4 t expendable - specs moved during development and the two dates bound the number; do not treat either as final without an i-Space current product sheet (i-space domain unreachable from this machine per R262 notes).

Wiki-title trap for future rounds: Hyperbola_3 does not exist, Hyperbola_(rocket_family) soft-404s; the article is at exactly Hyperbola_rocket_series - resolve titles via opensearch API before fetching i-Space family pages.

## Round 266 (2026-10-26)

rc-209 [value] on Long March 8A: stored LEO single point 10 t is contradicted by both current witnesses and absent from its own named source (zero occurrences in the fetched Wikipedia article) - CALT via SCIO gives approximately 7 tonnes for this variant; re-anchor proposal recomputes $/kg family live ($5,290 -> $7557). This is the first outright value contradiction of the wiki-family seam (previous rounds found provenance gaps and mode semantics); pattern suggests other rows may carry figures from superseded wiki revisions - sweep remaining China rows against current institutional statements in future rounds.

Corroboration recorded: SCIO Jan-2025 article also carries the Long March-10 disclosure (70 t LEO, lunar-transfer 8.2 to 27 tonnes) matching the existing Long March 10 row note class - that row gains a witness without an RC since figures agree exactly.

Staleness noted without RC: wiki launch statistics line shows twelve flights for variant 8A against eleven stored (catalog_date 2026-09-23 predates the latest flight). Flight-count currency is table-vintage material, not sourcing defects.

## Round 267 (2026-10-26) - Gravity-1 capacity attribution onto manufacturer disclosure

Orienspace publishes its own Gravity-1 parameter block on www.orienspace.com (server-rendered, reachable from this machine): 运载能力-近地轨道 吨 6.5 and 运载能力-太阳同步轨道(500km) 吨 4.2, each count==1 on the saved copy (sha in registry row). The standalone Wikipedia article Gravity-1 reproduces both capacities in its infobox with orbit altitudes - Payload to LEO (200km) Mass 6,500 kg and Payload to SSO (500km) Mass 4,200 kg - and carries the cost sentence The launch cost for Gravity-1 is around US$39 million. each span count==1; its capacity reference resolves to the Orienspace maiden-flight bulletin of 2024-01-11.

Upstream cells: spacecost@c633a57 reference/launch_vehicles.csv row Gravity-1, payload_leo_kg 6500 single point and note clause attributing price and both capacities to Wikipedia. All three figures are present in the named source family, so unlike rc-209 this is not a superseded-figure case; the defect is that no document is named beyond bare Wikipedia while the manufacturer publishes both capacity figures directly, and the LEO altitude qualifier (200 km) printed by the cited infobox was dropped. Launch record currency verified: article infobox shows 4 launches / 4 successes with last flight 15 September 2026, matching stored note text.

Verdict rc-210 [citation]: name both documents in the note (manufacturer page for capacities; cited article for cost), record the LEO altitude qualifier; no value change. Extracted data: extracted_data/r267_gravity_1_capacity_key_numbers.csv.

Witness banked, not extracted: the same Orienspace page carries Gravity-2 program parameters (GTO figure visible); spacecost has no Gravity-2 row yet - future-round target if upstream adds one.

## Round 268 (2026-10-26) - Kinetica-1 payload attribution onto manufacturer disclosure

CAS Space publishes the Lijian-1 parameter block on its official site: 运载能力 1.5t(500kmSSO) 2t(LEO), count==1 on the saved copy (sha in registry row). The state portal restates both figures with orbit qualifiers in prose - can send a payload of 1.5 tonnes to a 500-km sun-synchronous orbit, or a payload of 2 tonnes to low Earth orbit - count==1. The Wikipedia article reproduces the same pair in its infobox (Payload to LEO Mass 2,000 kg / Payload to SSO Mass 1,500 kg) and dates the launch record: Total launches 16 with last flight 20 September 2026.

Upstream cells: spacecost@c633a57 reference/launch_vehicles.csv row Kinetica-1, payload_leo_kg 2000 single point; note attributes payloads to bare Wikipedia and drops the SSO altitude qualifier. Unlike rc-209 all figures are present in a resolvable article - but only at the spaced slug Kinetica 1: the hyphenated slug serves missing-article placeholder text, recorded so future rounds do not false-flag it as an unsourced figure. The price band is self-declared estimated and no witness carries any cost statement, so it remains documented-by-design.

Verdict rc-211 [citation]: name the manufacturer page and the state statement in the note, record the SSO 500 km qualifier; no value change. Extracted data: extracted_data/r268_kinetica_1_capacity_key_numbers.csv.

## Round 269 (2026-10-26) - GSLV Mk II attribution onto ISRO plus flight-record contradiction

ISRO publishes both stored payload figures on its own vehicle page: Payload to GTO: 2,250 kg and Payload to LEO (Low Earth Orbit) : 6,000 kg, each count==1 on the saved copy. The GTO band high end of 2,500 appears nowhere in that record - another unsourced-band-endpoint instance; the stored headline 2,370 is the geometric mean of a band whose top ISRO does not carry.

The ISRO launch manifest itself lists nineteen GSLV missions from GSLV-D1 on Apr 18 2001 through GSLV-F17/EOS-05 on Sept 04 2026, with four rows marked Mission unsuccessful. The stored note says thirteen flights and two failures; the current Wikipedia family infobox reads Total launches 19 / Success(es) 13 / Failure 4 / Partial failure 2 - the stored number equals the success count, recorded as a conflation provenance hypothesis.

Claims verified accurate and left untouched: NISAR did fly on this vehicle (manifest row GSLV-F16/NISAR Mission dated Jul 30 2025; an earlier suspicion that it flew LVM3 was checked against the agency record and discarded), the price line Cost per launch US$47 million is present in the cited article, and the fairing statement matches ISRO publishing only the 3.4 m metallic PLF and 4 m ogive PLF diameters.

Verdict rc-212 [citation]: name the vehicle page and manifest in notes, restate the flight record per agency data (nineteen launches through Sept 04 2026 with four unsuccessful), flag the GTO high end as unsupported; payload columns unchanged. Extracted data: extracted_data/r269_gslv_mk_ii_key_numbers.csv.

## Round 269 (2026-10-26) - attribution-quality sweep of launch_vehicles.csv banked

All 76 rows classified from the notes field at spacecost@c633a57: forty-three name a document, nineteen cite bare Wikipedia or company-via-Wikipedia, fourteen are self-declared estimates. Bare-wiki rows already claimed by open RCs through this round: Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195, Vulcan rc-197, Proton-M rc-198, Long March 12 rc-201, Kuaizhou-11 rc-202, Kuaizhou-1A rc-203, Nuri rc-204, Zhuque-3 rc-205, Hyperbola-3 rc-208, Long March 8A rc-209, Gravity-1 rc-210, Kinetica-1 rc-211, GSLV Mk II rc-212. Remaining unclaimed bare-wiki targets for future rounds: Long March 4C (price estimated against sister 4B), Long March 6A, Long March 7 (names CASC but no document), Zhuque-2E (LandSpace Chinese news-detail route per R262 works), New Glenn 9x4 / Terran R / Nova / Tianlong-3 (company statements via Wikipedia; company pages need reachability probes first), Soyuz-5 (institutional DNS-blocked class, wiki-infobox route per rc-199 is the method). Jielong-3 self-discloses its SSO-as-LEO substitution = documented-by-design skip.

## Round 270 (2026-10-26) - Long March 7 payload attribution onto CALT statements

Both stored figures trace to China Academy of Launch Vehicle Technology statements carried by state media. For the two-stage vehicle: can send 13.5 tons of payloads to the low-Earth orbit and 5.5 tons to Sun-synchronous orbit (Jul 2025 mission report, count==1) - the stored LEO single point 13,500 equals the official figure exactly, and the SSO number on the same line has no upstream column. For the three-stage variant: is capable of placing a 7-ton spacecraft to geosynchronous transfer orbit (Aug 2026 failure report, count==1) - stored GTO 7,000 kg exact.

Flight-record boundary: the same Aug 2026 report closes with second launch failure for the Long March 7A, which has been used in 17 space missions. Current Wikipedia statistics read sixteen flights two failures for the variant - wiki lags the institutional count here, so the stored note text of two failures in eighteen is plausibly correct or ahead and is left untouched; no clean mission-by-mission manifest was reachable from this machine to date the final flight.

The upstream attribution CASC / Wikipedia payload figures names the right agency but no document. The wiki infobox additionally carries orbit parameters (LEO altitude 200 to 400 km at inclination 42 degrees) that the CALT statements do not print; recorded so a future qualifier edit does not lose them.

Verdict rc-213 [citation]: name both China Daily carriers of CALT statements in notes with variant qualifiers; no value change. Extracted data: extracted_data/r270_lm7_capability_key_numbers.csv.

## Round 271 (2026-10-26) - Zhuque-2E latest-flight date contradicted by its own launch total

Two state-media-carried LandSpace reports bracket the family flight record. The May 2025 report states that mission was the fifth of the ZQ-2 series (count==1); with base flights December 2022 failed plus July and December 2023 successful, that puts the ZQ-2E Y3 loss on Aug 15 2025 at family flight six. The September 2026 report calls its launch the sixth flight of the ZQ 2E variant [appears twice] - a success carrying ten satellites - which makes the family total nine with two failures, exactly matching stored counts.

But that same arithmetic contradicts the stored latest-flight clause: if nine launches through September 2026 are counted then the latest flight is Sep 2026, not Aug 2025 as the note text says; and if counting stopped at August 2025 the total would be six. The row is internally inconsistent whichever way it was compiled - rc-214 [value] proposes redating the latest-flight clause to September 2026 or dropping the month claim, counts unchanged.

Verified accurate and untouched: the failure cause text second-stage voltage fault matches the company review-board wording quoted by trade press (second-stage servo power bus voltage abnormally dropped); the milestone first methalox rocket to reach orbit with year 2023 is verified verbatim against the cited Wikipedia article for the July 2023 flight; SSO figure 4 t gains a company statement via state media with the 500 km altitude qualifier restored.

Evidence boundary recorded: no institutional statement of a ZQ-2E LEO capacity figure was found this round - the stored single point 6,000 kg remains Wikipedia-sourced; LandSpace English pages are JS shells (R262) and Chinese product-page probes did not surface an LEO number.

Verdict rc-214 [value]: redate latest-flight clause per Sep 2026 report, cite both carriers for the record chain and SSO figure; launch counts, failure cause text, milestone claim unchanged. Extracted data: extracted_data/r271_zq2e_launch_record_key_numbers.csv.

## Round 272 (2026-10-26) - Long March 6A debris and payload claims vindicated by institutional records; citation move

The LM-6A note carries two unsourced clauses beyond its bare Wikipedia payloads attribution. Both check out against institutional sources, so this round opens a citation-move candidate rather than a value defect.

Debris history: NASA Orbital Debris Quarterly News vol 27 issue 3 Table 1 (reference date 01 June 2023) lists the YUNHAI 3 CZ-6A R/B breakup of 12 November 2022 with Cataloged to Date 781 and On Orbit 722 fragments - stored phrasing 700+ tracked pieces is correct against NASA records, and the same article ranks the event behind only Fengyun-1C, Cosmos 1408 and Cosmos 2251 in cataloged debris produced. The several flights phrasing also holds: the registered Wikipedia article documents three further upper-stage events after November 2022 (launches of 26 March 2024, 4 July 2024 and 6 August 2024), with the US SDA confirmation for the August event cited there; SpaceNews independently reported the pattern in July 2024 (witness recorded not registered per R271 convention). ODQN v28 issues two and three were scanned this round: zero CZ-6A mentions - NASA has no published account of the later events.

Payload pair: current Wikipedia carries both stored figures exactly (LEO 8,000 kg; SSO at 500 km 6,500 kg), but its LEO citation is a Zhihu column post. CASC own product page publishes only one capacity figure - SSO at 700 km not less than 4 tonnes (span count==1) - and no official LEO statement exists; the zh-wiki article attributes LEO payload capacity of 8 t and above to the Zhang Weidong et al technical paper in International Space. Boundary recorded: stored LEO 8 t is consistent with that literature chain, not with a CASC product-page figure.

Launch record untouched: note self-dates twenty-six for twenty-six to Jul 2026; current wiki statistics read Total launches 28 Success(es) 28 with first flight 29 March 2022 matching the stored variant history - consistent under the R270 flight-record boundary rule.

ODQN vol 27 issue 3 hosted in full_texts (public-domain US government work; zero copyright tokens across all pages). Verdict rc-215 [citation]: name ODQN + CASC page + wiki article for the debris and payload clauses, values untouched. Extracted data: extracted_data/r272_lm6a_debris_record_key_numbers.csv.

**Round 273 - Long March 4C payload attribution and institutional SSO spec (rc-216)**

The stored row keeps LEO 4,200 kg and GTO 1,500 kg attributed to bare Wikipedia. Current article verified: both figures exact against the infobox capacity block, but every citation there is a skyrocket.de snapshot accessed April 27, 2008 - one aging reference carries all three numbers of an active rocket. The institutional record only ever speaks sun-synchronous: the CASC product page (dated September 15, 2015) prints its spec sentence with SSO-transfer wording at 2.8 tonnes at 800 km, and current launch reports through April 17, 2026 print 3 tonnes at 700 km. Upstream has no SSO column for this launcher, so the one officially published capacity figure is invisible in spacecost while two unofficial ones are stored - recorded as semantics context, values untouched per citation-move convention.

Launch record: infobox statistics Total launches 59 (Successes 57) with Last flight April 17, 2026; the same-day CASC report corroborates no flights since. Stored ~59 is current exactly. The stored price cell self-declares estimated against the sister Long March 4B figure of 50 million dollars dated 2006 - documented-by-design class (zero cost statements on any fetched institutional page), untouched.

Witness hosts: three T4 verified_live_not_pulled rows registered d04 with full sha256 in access_status; no hosted files this round. Extracted data r273_lm4c_payload_attribution_key_numbers.csv.

**Round 274 - Tianlong-3 failure timing clause vs company investigation record (rc-217)**

The stored note says the maiden flight FAILED shortly after liftoff. That phrase has count==0 in the cited Wikipedia article and contradicts the institutional record: Space Pioneer published a return-to-zero investigation statement (fetched live from its official WeChat account, sha recorded) whose timeline spans each verify count==1 - design MaxQ at T+110 s, all scheduled first-stage sequences completed at T+177.2 s, normal stage separation at T+182.2 s, second-stage ignition at T+185.9 s, loss of control from lower-than-expected altitude at T+189.5 s and commanded flight termination about three minutes in. The China Daily report of April 4, 2026 carries the company failure announcement (was unsuccessful on Friday afternoon; flight became abnormal before it could reach its preset orbital altitude) - neither source supports a liftoff-adjacent early-failure characterization, which matters because first-stage success is exactly what reusability progress modeling would key on. Proposal restates per institutional record and names all three witnesses; payload pair (LEO 17 t / SSO 14 t exact vs current wiki), single-flight status (Total launches 1 Failure 1), June 2024 test-stand runaway clause (consistent with Reuters-backed reporting) and the self-declared price estimate are untouched.

Witness hosts: three T4 verified_live_not_pulled rows registered d04 with full sha in access_status; WeChat statement page is server-rendered HTML fetched live (3.5 MB, extraction-only - no license grant); China Daily on the accessible state-media carrier class proven in R260/R271. Extracted data r274_tl3_failure_status_key_numbers.csv.
