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

rc-119 (cite Zapata 2017 for the Delta IV Heavy and Atlas V 551 payloads), rc-128 (Falcon 9 expendable band at escalated LSP/GPS prices $124M and $131M), rc-129 (Falcon Heavy expendable low end escalated to $202M), rc-130 (cite Zapata for the Delta IV Heavy price, $453M escalated). Texts in `revision_candidates.csv`; `extracted_data/r165_launch_prices_escalated.csv`.

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
