## R730 - Default fairing volume for blank vehicle rows (2026-11-14)

economicspace_missing_fairing_volume_fallback_code_current_2026: economicspace modules/calc.py line 3950 states `DEFAULT_FAIRING_VOLUME_M3 = 100.0`; _vehicle_consts() line 3974 selects `DEFAULT_FAIRING_VOLUME_M3` when the Spacecost row's fairing_volume_m3 is missing. model_launch_liquid_volume defaults to true (line 779), and the launch-volume check uses the substituted envelope (line 7437).

spacecost_launch_vehicle_fairing_rows_current_2026: Spacecost reference/launch_vehicles.csv has 34 of 76 rows with blank fairing_volume_m3, including 17 of 48 operational vehicles. The affected rows are listed in extracted_data/r730_missing_fairing_volume_fallback.csv.

Upstream cell/value: economicspace modules/calc.py DEFAULT_FAIRING_VOLUME_M3, 100.0 m³, used as the usable fairing envelope for a row with no volume. The code gives no source or derivation for the fallback.

Verdict: provide a source for each usable fairing envelope or derive a documented vehicle-specific value from published geometry and a justified packing method. If matched evidence is unavailable, expose this as a scenario with uncertainty and sensitivity, or treat the volume as unknown; no replacement inferred. Distinct from rc-436 (six estimates built from known outer dimensions) and rc-288 (launch-volume closure method). Open rc-597. Extracted: extracted_data/r730_missing_fairing_volume_fallback.csv.

## R725 — Long March 5 price estimate and band basis (2026-11-13)

`faa_ast_2018_compendium_long_march_5_price` — FAA AST’s 2018 *Annual Compendium of Commercial Space Transportation*, Long March 5 fact sheet, “Launch Vehicle Specifications” table: the “Estimated Price per Launch” entry is “Undisclosed”; the same table pairs that price row with 25,000 kg to LEO and 14,000 kg to GTO. This records a 2018 disclosure status, not a current price.

`spacecost_lm5_launch_price_code_current_2026` — at `spacecost@a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/launch_vehicles.csv` stores Long March 5 at $133M [$110M,$160M], `reference_year=2026`, `price_basis=estimate`, and derived $5,320/kg to LEO. Its note attributes the high end to a Wikipedia estimate and says $110M is what the row used to carry. `CITATIONS.md` says estimate bands are “chosen against the nearest vehicle that does have a price”; the row does not identify that comparator or the band calculation.

`hf_dataset` — the hosted dataset’s Long March 5 row (row 4, extracted in `extracted_data/r70_hf_dataset_full_table.csv`) lists $60M and $2,400/kg with source “CASC / industry estimates.” Its recorded source note says the dataset mixes years and list-price versus estimate bases; it is not a like-for-like replacement without a dated source and boundary.

Verdict: document the source/calculation for both endpoints, the named comparator, price year and vehicle-cost versus launch-service boundary; retain the current values only as explicit scenario estimates until that basis is recorded. No replacement inferred. Distinct from **rc-019** (dataset $/kg comparison), **rc-207** (payload variant attribution), and **rc-436** (fairing-volume transfer). Open **rc-592**. Extracted: `extracted_data/r725_long_march_5_price_basis.csv`.

## R708 — Space Shuttle launch-price band has mixed cost boundaries (2026-11-12)

`spacecost_space_shuttle_price_band_code_current_2026`: Spacecost `reference/launch_vehicles.csv` records `list_price_usd=$972M`, low/high `$450M/$2.1B`, and `reference_year=2026`. Its note describes the low endpoint as the marginal cost of one more flight and the high endpoint as whole-programme cost per flight, escalated from ~$1.5B in 2011 dollars by ~1.44. It explicitly says the band mixes dollar years. NASA’s Resource Significance Framework says “By 2011, the incremental cost-per-flight ... was estimated at $450 million” (Space Shuttle Program, p. B-17); it does not state a price-year convention in that passage. NASA OIG IG-24-001 separately estimates Shuttle operations cost increased “to $1.45 billion per launch” (p. 17), without stating the dollar year there. The note does not label the low endpoint’s dollar year or identify the CPI series and observation dates for its high-end conversion. The stored $972M centre is the geometric midpoint of the listed endpoints, which mix distinct cost boundaries and dollar-year treatment.

- **rc-578**: define a comparable cost boundary and dollar year for the band, or explain the deliberately mixed interval and how `reference_year=2026` and the $972M centre should be interpreted; identify the inflation conversion. No replacement inferred.

Extracted: `extracted_data/r708_shuttle_price_band_basis.csv`.

## R693 — Six target launch-price rows lack a traceable basis (2026-11-12)

`spacecost_target_launch_prices_code_current_2026`: Spacecost `reference/launch_vehicles.csv` records `price_basis=target`, `reference_year=2026` and a single-point price for SpinLaunch Orbital, Skylon / SABRE, Sea Dragon, Lunar mass driver, Lunar space elevator and Earth space elevator. Their row notes do not give a numeric price source or calculation. SpinLaunch's code note calls its amount a “published target” (line 1826) without identifying a publication. `vehicles.py` annotates the three infrastructure payload fields as per year (lines 1944, 1975, 2003); the exported table derives $/kg from the stored price and payload columns.

- **rc-556** SpinLaunch Orbital: $1.25M / 200 kg = $6,250/kg; the note calls it a published target without identifying the publication.
- **rc-557** Skylon / SABRE: $15M / 15,000 kg = $1,000/kg.
- **rc-558** Sea Dragon: $300M / 550,000 kg = about $545/kg.
- **rc-559** Lunar mass driver: $1M and 100,000 kg/year, exported as $10/kg.
- **rc-560** Lunar space elevator: $500,000 and 50,000 kg/year, exported as $10/kg.
- **rc-561** Earth space elevator: $2M and 20,000 kg/year, exported as $100/kg.

Verdict: document each target's source, calculation, dollar year and service/cost boundary; resolve annual-throughput versus per-launch units for the infrastructure rows. No replacement inferred. Extracted: `extracted_data/r693_target_launch_price_rows.csv`.

## R691 - Falcon Heavy reusable-side-core price basis (2026-11-12)

- **nasa_xhab_2025_spacex_falcon_heavy_price**: X-Hab 2025 report Table 19, printed p. 109, identifies its cost inputs as SpaceX website data from 2022-2024 and lists Falcon Heavy at $97M (2022) and $107.9M adjusted to 2025 dollars. The table does not state its adjustment method.
- **spacecost_falcon_heavy_reusable_price_code_current_2026**: at `spacecost@a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/launch_vehicles.csv` stores $100M [$97M,$103M], `price_basis=published`, `reference_year=2026`. Its note identifies $97M (2022) for up to 8 t GTO with boosters recovered, then carries forward Falcon 9's $70M-to-$74M increase to produce $103M; $100M is the band midpoint. The existing Falcon 9 price-increase source does not establish a Falcon Heavy increase. Verdict: document the 2026 basis and service/configuration boundary; distinguish the dated $97M anchor from derived endpoints and midpoint. No replacement inferred. **rc-554**, distinct from rc-408 (payload configuration). Extracted: `extracted_data/r691_falcon_heavy_reusable_price_basis.csv`.

## R690 — SSLV per-launch price attribution and conversion basis (2026-11-12)

- **indianexpress_2022_sslv_30crore_quote**: paragraph 34 attributes to former ISRO chairman K. Sivan a 2019 press-conference statement that the SSLV “cost will be only around Rs 30 crore.” This supports an approximate ₹30 crore statement, not the ₹35 crore upper endpoint or a 2026 USD conversion.
- **isro_2021_sslv_development_cost_parliament**: Rajya Sabha Unstarred Question 2164, answer (b), reports ₹169.07 crore for SSLV development, qualification and three development flights; this is a project total, not a per-launch price.
- **spacecost_estimated_launch_prices_code_current_2026**: at `spacecost@a401930efe30aaad01aafd2b3cb332ad0438c841`, `reference/launch_vehicles.csv` row `SSLV` stores $3.74M [$3.5M,$4M], `price_basis=reported`, `reference_year=2026`, and says “Source: ISRO, Rs 30-35 crore (~$3.5-4M) per launch.” The located statement does not establish the range endpoint, commercial-service boundary, FX date/method, or 2026 dollar treatment. Verdict: cite and date both INR endpoints and define the price boundary and conversion basis; no replacement inferred. **rc-553**. Extracted: `extracted_data/r690_sslv_price_attribution.csv`.

## R689 — Spacecost launch-price estimates without a recorded basis (2026-11-12)

- **spacecost_estimated_launch_prices_code_current_2026** [T4]: Spacecost@a401930 stores 2026 list-price estimates for Zhuque-2E ($26.5M, $20M–$35M), Zhuque-3 ($35.4M, $25M–$50M), Hyperbola-3 ($42.4M, $30M–$60M), Soyuz-5 ($49M, $40M–$60M), Nova ($24.5M, $20M–$30M), and Eclipse ($80M, a zero-width band). Their notes call the prices estimates or state that the provider publishes no price, but give no numerical method.
- **carrier_space_zhuque2e_price_request_current_2026** [T4]: the Zhuque-2E listing says “Price on request”; it provides no amount and does not support Spacecost’s estimate.

The six price estimates need a traceable price basis and a configuration/service boundary; payload, flight-history, and configuration citations do not supply one. **rc-547** Zhuque-2E; **rc-548** Zhuque-3; **rc-549** Hyperbola-3; **rc-550** Soyuz-5; **rc-551** Nova; **rc-552** Eclipse. No replacement prices inferred. Extracted: `extracted_data/r689_launch_price_estimate_rows.csv`.

## R661 — H3-30 target price year and range are unresolved (2026-11-12)

- **jaxa_h3_launch_vehicle**: JAXA’s “High cost-performance” section says its target is “about 5 billion yen” for the light configuration without solid boosters, mainly for LEO; the page gives no target date or USD conversion. **spacecost_h3_30_target_price_code_current_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` row `H3 (30)` stores `$36.3M` [$33M,$40M], `$9,075/kg`, `reference_year=2026` and `price_basis=target`; the note converts ¥5B to about $33M at 2024 rates, without explaining the 2026 treatment or the $40M endpoint. The separate **rc-379** concerns the H3 (24L) estimate relative to this target, not this target row’s conversion or band. Verdict: state the price year and FX basis and explain the interval, or label it as scenario sensitivity; no replacement inferred. **rc-522**. Extracted: `extracted_data/r661_h3_30_target_price_basis.csv`.

## R660 — Spectrum target price is dated and its source attribution needs correction (2026-11-12)

- **eu_commission_eic_isaero_2022_factsheet**: the European Commission’s ISAERO factsheet, printed p. 2, describes pricing “at around €10 000 per kilogram” and payload capacity up to 1,000 kg; its footer is © European Union, 2022, and its facts panel still says first test flight planned for end-2022. This supports a historical target, not a 2026 offer.
- **isar_aerospace_spectrum_price_target**: the current Isar Aerospace homepage and Spectrum page advertise launch configurations and pricing options but state no numeric price or target. The registered homepage URL therefore does not itself document the upstream €10,000/kg figure.
- **spacecost_spectrum_price_code_current_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` row `Spectrum` stores `$11,500,000` and `$11,500/kg`, `reference_year=2026`, `price_basis=target`; its note converts the approximate €10,000/kg target at `$1.15/€` but gives no exchange-rate date/source. Verdict: cite the 2022 factsheet as the historical target, state the FX date/source and price-year treatment, and distinguish it from a current offer; no replacement inferred. **rc-521**. Extracted: `extracted_data/r660_spectrum_price_target_basis.csv`.

## R659 - New Glenn 9x4 price estimate has no public basis (2026-11-12)

- **blueorigin_new_glenn_9x4_page**: Blue Origin’s current 9x4 product page describes a nine-engine first stage, four-engine second stage, 70 t LEO, 14 t direct-to-GSO and 20 t TLI performance, but publishes no commercial price; it directs customers to contact sales. At `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv`, row `New Glenn 9x4`, stores `$194,000,000` with `$150,000,000`–`$250,000,000` bounds, `reference_year=2026`, and `price_basis=estimate`; the note explicitly says no price is published. The separate 7x2 row’s reported `$68M`–`$110M` range and rc-328 do not establish a 9x4 price or estimate method. Verdict: document a variant-specific price derivation and boundary, or retain the band only as a scenario estimate with sensitivity; no replacement inferred. **rc-520**. Extracted: `extracted_data/r659_new_glenn_9x4_price_basis.csv`.

## R642 — Nuri price band extends beyond its cited approximate point (2026-11-11)

- **spacecost_nuri_price_estimate_code_current_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` row 29 stores $36.7M [$30M,$45M], `reference_year=2026`, and `price_basis=estimate`. Its note attributes an estimate “around $30M” and says there is room above it for an unpriced government vehicle. **wikipedia_nuri_rocket_article** (Usage section) likewise says “The launch cost is estimated to be around US$30 million,” citing an SBS report dated 30 October 2021; that is an approximate historical point, not support for the $45M endpoint or a 2026 adjustment. **kari_nuri_vehicle_page** supplies vehicle-capability context but no launch price (R261). The $36.7M center is the geometric midpoint of the endpoints, not an independent price observation. Verdict: document the point source and year, 2026 treatment, price boundary, and high-end rationale, or identify the band as a scenario; retain values pending a comparable basis. No replacement inferred. **rc-506**. Extracted: `extracted_data/r642_nuri_launch_price_basis.csv`.

## R641 — Long March 4C price proxy lacks a traceable 2026 basis (2026-11-11)

- **spacecost_lm4c_price_proxy_code_current_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` row 33 stores $38.7M [$30M,$50M], `reference_year=2026`, and `price_basis=estimate`; its note anchors the proxy to a Long March 4B $50M price in 2006 but identifies no quote, inflation adjustment, or 4B-to-4C derivation. R273 resolved the capacity attribution and reports that the available **casc_cz4c_product_page_2015** and **casc_cz4c_launch_report_20260417** give no cost statement; the registered Wikipedia article likewise supports capacity and launch history, not a price. Verdict: document the anchor, configuration analogy, 2026 conversion and range derivation; retain current values pending a comparable basis. No replacement inferred. **rc-505**. Extracted: `extracted_data/r641_lm4c_price_proxy_basis.csv`.

## R640 — Kinetica-1 price estimate has no stated basis (2026-11-11)

- **spacecost_kinetica1_price_estimate_code_current_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` row 44 stores $11M [$8M,$15M], `reference_year=2026`, and `price_basis=estimate`; the price note says only “price estimated.” Existing sources **cas_space_kinetica_1_product_page** and **gov_cn_lijian_1_y5_statement** support payload-capacity fields, while **wikipedia_kinetica_1_article** carries no price statement (R268). They do not establish the point, endpoints, 2026 dollar basis, or vehicle-cost versus launch-service boundary. Verdict: document the calculation and price scope or retain the band as an explicit scenario; no replacement inferred. **rc-504**. Extracted: `extracted_data/r640_kinetica1_price_estimate_basis.csv`.

## R639 — Soyuz-2.1a and Long March 8A price-estimate bases (2026-11-11)

- **spacecost_soyuz_21a_price_estimate_code_current_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` row 15 stores $32.4M [$30M,$35M], `reference_year=2026`, and `price_basis=estimate`; its note says it is estimated against a 2018 $35M quote for a Soyuz-2.1b without an upper stage. **glavkosmos_tass_2018_soyuz_price** reports “The launch of the Soyuz-2.1 without the Fregat booster would cost about $35 million” (TASS article body, read in R175), without identifying the 2.1a variant, defining full service scope, or providing the adjustment to 2026. It does not establish the current point or range. Verdict: document variant comparability, price boundary, 2026 conversion and endpoint derivation; retain current estimate pending a like-for-like basis. No replacement inferred. **rc-502**. Extracted: `extracted_data/r639_soyuz_21a_price_proxy_basis.csv`.
- **spacecost_lm8a_price_estimate_code_current_2026**: at the same pinned Spacecost snapshot, row 37 stores $52.9M [$40M,$70M], `reference_year=2026`, `price_basis=estimate`; the note says only “Price estimated.” The geometric center rounds to the stored point but supplies no evidence for the endpoints. **ccgp_2026_extp_launch_budget** reports a proposed RMB 245.2M eXTP launch-service budget and names China Long March Rocket Co. as intended provider, but no variant; **pbc_2026_06_08_usd_cny_midpoint** gives the date-matched parity used in R408’s approximately $35.95M conversion. This procurement budget is not an awarded price and does not establish a Long March 8A vehicle price or scope. Verdict: provide the point/range derivation, configuration, price year and vehicle-price versus service boundary; keep it as a documented scenario pending comparable evidence. No replacement inferred. **rc-503**. Extracted: `extracted_data/r639_lm8a_price_estimate_basis.csv`.

## R593 — Ariane 62 institutional contract-value comparator (2026-11-11)

- **esa_copernicus_mff21_article14_2025_contract_awards** (ESA Copernicus Space Component contract list, 2025, p. 1): under “Contract value on Copernicus 2025 (€),” ARIANESPACE is listed for “SENTINEL-1D ALTERNATIVE LAUNCHER SERVICE” at €82,070,773. ESA’s 28 Jan 2025 announcement identifies the Sentinel-1D contract as a two-booster Ariane 62 launch; that announcement states no price. The contract-list amount is a reported contract value, not a published Arianespace tariff, and the list does not itemize its service scope.
- At `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` stores Ariane 6 (A62) at $95.9M with an $80M–$115M estimated range. Its note ties the high end to a €100M (2024) estimate and says Arianespace publishes no list price. ESA’s contract value (€82.07M) is near the modeled low end, but its service and price-year scope is not itemized and cannot be treated as a replacement launch-list price. Verdict: cite and reconcile the institutional contract comparator while retaining the estimate as an estimate unless a like-for-like scope is established; **rc-457** remains open. Extracted: `extracted_data/r593_ariane62_contract_value_comparator.csv`.

## R543 — Falcon Heavy reusable-side-core LEO payload conflict (2026-11-10)

- **spacex_2026_eu_prospectus_falcon_heavy_payload** (SpaceX EU Prospectus, June 5, 2026): §4.3.10.1 (printed p. 59) reports Falcon Heavy at “approximately 64 metric tons” to LEO and describes it as partially reusable. §4.3.10.2 (printed p. 96) identifies the reusable components, including the side boosters, and lists a 63,800 kg LEO capacity. The prospectus does not specify the exact recovery profile attached to that capacity.
- At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/launch_vehicles.csv` stores 30,000 kg for “Falcon Heavy (reusable side cores)” and its low/high payload bounds; its note attributes 30 t to Wikipedia’s launcher comparison and says SpaceX publishes no LEO figure for this configuration. The prospectus is a direct company statement for a partially reusable Falcon Heavy, 33,800 kg above the stored value, but configuration scope remains unresolved. Review the payload value, public-source note, and dependent USD/kg cells together; **rc-408** remains open.
- Extracted: extracted_data/r543_spacex_falcon_heavy_payload_capacity.csv.

# Domain 4 Findings — launch cost per kg (history, projections)

Backings: spacecost `reference/launch_vehicles.csv` (prices, payloads, fairing volumes) and the `Expendable upper stage recurring cost` row of `operational_costs.csv`; economicspace's "launch no longer dominates" framing.

## R1 - hf_dataset and jones2018 (2026-09-17)

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

## R3 - Experience curve and economics framing (2026-09-18)

- **terzi_nicoli_2026** [T1, hosted, CC BY] (PNAS Nexus 5(7):pgag217): 4,400+ launches 1960–2025, Wright's-law fit. Fleet average $87,023/kg (1960) → $3,868/kg (2025, 2024 USD); learning rate −21.2% per doubling (~−44% post-Cold-War vs ~−17% before); central forecast $1,600/kg by 2030 and $300/kg by 2040. Our Falcon 9 row ($4,253/kg) is above the 2025 fleet mean. Stage 4 carries no forward projection: whether to discount long-horizon launch costs is the owner's call. `extracted_data/terzi_nicoli_experience_curve_key_numbers.csv`.
- **weinzierl2018** [T1] (JEP 32(2):173–192; Harvard DASH author copy, LAA terms, extract only): COTS all-in ISS cargo ≈ $89,000/kg SpaceX, $135,000/kg Orbital Sciences, ~$272,000/kg Shuttle (citing Zapata 2017; p181). R73 extraction: Figure 2 space-sector revenue $176B (2005) → $330B (2014) / $322B (2015); Table 1, 37 New Space companies. `r73_weinzierl2018_figure2_space_sector_revenue.csv`, `r73_weinzierl2018_key_numbers.csv`, `r73_weinzierl2018_table1_new_space_companies.csv`.

## R12 - metzger_2023 (moved to d22) (2026-09-18)

arXiv:2303.09011, read only: the gear ratio on cost G and production mass ratio phi decide whether lunar propellant beats Earth-launched; tent sublimation's phi is an order of magnitude past the threshold. R71 extracted Tables 1-3 and A1 (now in `22_prior_art_techno_economic_benchmarks/extracted_data/`).

## R16 - yun_2023 [T1, hosted, CC BY-NC] (2026-09-18)

KSPE 27(2):45-59: reusable-LV table (engines, total thrust, fuel): Starship 7342 (Raptor x33 + x6; the unit is tf, not kN: corrected 2026-09-26; 230 x 33 = 7590 as printed), New Glenn BE-4 x7, first stage up to 25 flights. No payload or $/kg columns.

## R32 - SLS payload anchors (both hosted) (2026-09-18)

- **askins_2021_sls_janaff_update** (NTRS 20210016306): Block 1B Cargo LEO 105 t (231.4k lbs) = our `payload_leo_kg` exactly (row priced at $39,048/kg); footnote "Low Earth Orbit (LEO) represents a typical 200 km circular orbit at 28.5 degrees inclination"; TLI B1B Cargo >46 t / 42 t, B1 >27 t; ladder B1 95 t, B2 130 t.
- **nasa_esd30000_sls_mission_planners_guide** (ESD-30000 Rev A, NTRS 20190000736): Block 1 LEO "more than 209,439 lbm (95 t)"; EUS "up to 88,185 lbm (40 t) of payload delivery to lunar vicinity"; defines what "payload" means for SLS rows. R99: the 8.4 m PLF Short volume 21,930 ft3 = 621 m3, upstream's Block 1B value exactly. `r70_nasa_esd30000_table4_1_payload_vs_c3.csv`.

## R33 - Falcon 9 cost anchors (both hosted) (2026-09-18)

- **zapata_2017_cots_crs_lcc_assessment** (NTRS 20170008895): Falcon 9 development ≈ $390M ($300M F9 + $90M Falcon 1), "NASA has verified these costs", vs NAFCOM's $1.7B–$4.0B ("the cost model predicted that the Falcon 9 would cost $4.0 billion based on a traditional approach"); recurring cost per kg delivered to ISS (2017$) SpaceX $89,000, Orbital ATK $135,000, Shuttle what-if ~$272,000. R72 Tables 5-6: Shuttle what-if 1 to 5 MPLM flights a year costs $5,046M to $6,640M ($/kg 364,582 → 95,943); amortized non-recurring adds $28,213/kg (Antares/Cygnus), $23,850 (Falcon 9/Dragon), $34,322 (Shuttle); NASA cargo investment $953M (Table 5) vs 437 + 495 = $932M (Table 6), unreconciled. `r72_zapata_2017_cots_crs_tables5_6_cost_data.csv`.
- **webb_2016_is_it_worth_it_reusable_econ** (ICEAA 2016, NTRS 20160013370): NASA PCEC Launch Services ROM estimator (M15$ per launch, read by word coordinates): GEO <3,000 kg $120M / >3,000 $140M; Planetary <1,000 $80M / 1,000–2,000 $110M / >2,000 $175M; Polar $55M / $85M / $130M; Lunar <500 $85M / >500 $160M; LEO <500 $40M / >500 $80M; Helio $100M. A flight price, not a $/kg.

## R34 - zapata_2017_state_of_play_us_space_systems [T2, hosted] (2026-09-18)

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

## R58 - IG-20-012 and IG-23-015 (hosted) (2026-09-25)

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

## R103 - nasa_oig_2024_ig-24-015_sls_block_1b (hosted) (2026-10-02)

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

All four filings read in full, hash-recorded, not hosted. spacecost@d799cba applied rc-030, rc-050, rc-051 and rc-052 without touching these rows. `extracted_data/r128_sec_filings_key_numbers.csv`.

- `voyager_technologies_10k_2026_starship_contract`: one "Starship" mention, no dollar figure.
- `voyager_technologies_424b4_prospectus_starlab_commitments` (new; Jun 11 2025): "a commitment for one launch at a future estimated launch date for $90.0 million" (as of March 31 2025); cancellation would cost $13.5 million. **rc-082** (citation): cite the prospectus, not a 2026 10-K.
- `rocket_lab_form_10q_fy2026_q1`: "revenue per launch was $9.3 million and $7.1 million" (Q1-2026 / Q1-2025), cost per launch $5.4M / $5.7M; no $7.5M anywhere. **rc-081** proposes $9,300,000.
- `spacex_spcx_ipo_registration_statement` (new; S-1): Space segment FY2025 revenue $4,086M; Starship R&D $930M (Q1-2026) and $3,004M (2025); Falcon launches 134 → 165; "average price per launch remained relatively flat"; F9 v1 ~$2,700/kg vs the historical $18,500/kg; Starship goal to cut cost to orbit by 99% or more.
- `spacex_spcx_10q_q2_fy2026` (new): Falcon launches 37 / 45 (Q2-26 / Q2-25), 77 / 81 (H1), customer launches 10 / 9 / 17 / 21; H1-2026 revenue $12,508M vs $8,138M.

## R132 - nasa_nsts_21492_space_shuttle_payload_bay_users_guide (hosted)

US government work, 255 pp: "The maximum payload dimensions by design are 720 inches (18.46 m) long by 180 inches (4.6 m) in diameter, or a volume of 10,600 cubic feet (306.6 m3)." The inches give ~300 m3 and 10,600 ft3 = 300.2 m3, bracketing upstream's 300.0; upstream's note on the inconsistent metric pair is right. `extracted_data/r132_sts21492_fairing_key_numbers.csv`.

## R164 / R165 - Candidates (2026-10-14)

rc-119 (cite Zapata 2017 for the Delta IV Heavy and Atlas V 551 payloads), rc-128 (Falcon 9 expendable band at escalated LSP/GPS prices $124M and $131M), rc-129 (Falcon Heavy expendable low end escalated to $202M), rc-130 (cite Zapata for the Delta IV Heavy price, $453M escalated). Texts in `revision_candidates.csv` (open) and `revision_candidates_closed.csv`; `extracted_data/r165_launch_prices_escalated.csv`.

## R175 - glavkosmos_tass_2018_soyuz_price (2026-10-16)

tass.com/science/1024055 (Oct 3 2018): "The basic price to launch Russia's Soyuz-2.1 carrier rocket with the Fregat booster will stand at about $48.5 million"; without Fregat about $35 million; 1 kg "$20,000-30,000". Extraction only. `extracted_data/r175_soyuz_price_key_numbers.csv`.

## R187 - Upper-stage cost row (rc-170) (2026-10-18)

`operational_costs.csv` 'Expendable upper stage recurring cost' is the only row with no CITATIONS.md entry: '~$10M (Musk 2018)' unlinked, '~$7M (2026 third-party estimate)' unnamed, 'Centaur III, ~$30M' sourced nowhere, and the tank row derives from it. SP-4176 has programme costs only. **rc-170** (citation). Detail in d03 (`03_dv_propulsion/extracted_data/r187_centaur_cost_history_key_numbers.csv`).

## R188 - H-IIA 204 price (rc-171) (2026-10-18)

The row's $90M carries "JAXA/MHI pricing" with no document. JAXA: "the cost was reduced by almost half, down to 9.3 billion yen (H-IIA F4)"; MHI Tech Report Vol. 39 No. 1: below 8.5 billion yen per unit, Table 3 standard type 75-85 hundred million yen at $=JPY 120 ($62.5M-$70.8M); The Space Review (Mar 7 2023): "about 10 billion yen (about $75 million)". At the World Bank's 2024-2025 official rates these are $61-75M; $90M needs JPY/$ ≤ 111.1, last seen in the annual series in 2021. **rc-171** (value): ~$68M [$62M, $75M] in 2026 dollars, with the yen figure and rate in the notes; vehicles.py duplicates the value. `extracted_data/r188_hii_price_key_numbers.csv`.

Exchange rates: `23_cost_indices_dollar_years/extracted_data/r188_usd_jpy_official_rates_key_numbers.csv`.

## R196 - spacecost README contract verified against live v0.12.0 tables (2026-10-19)

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

This surface is covered; skip unless the README or v0.12.x tables change.

## R208 - Northrop Grumman Propulsion Products Catalog registered; rc-179 opened (2026-10-19)

The economicspace MODEL.md propellant-tankage table asserts "Star 48B measures 6.4%" with no source named anywhere upstream. The manufacturer catalog (public release OSR No. 16-S-1432, dated 05 April 2016; 9752514 B sha 5b52adf1) gives both flight-proven variants on pp.102-103: propellant load 4,431.2 lbm identical across variants [appears twice], total inert 274.2 lbm (TE-M-711-17 short nozzle) and 289.6 lbm (TE-M-711-18 long nozzle). Inert-over-propellant = 6.19% / 6.54%, mean 6.36% - the printed 6.4 is true within variant spread but uncited; rc-179 proposes the citation, no number change.
Sister context: spacecost APCP class anchor prints 6.9% (reproduces from pinned rows per Round 197) - conservative above both measured variants.
This surface is covered; skip unless a new catalog edition appears or the MODEL.md row changes.

**EC README quantitative contract swept clean (Round 225, skip unless the README moves):** every current-state claim at `be86297` reproduces — module version table versus versions.md Current-versions heading and verify_docs check 2; the seven-place spacecost pin enumeration is exactly four code pins plus three named prose mentions (requirements.txt URL, build_master _MASTER_PIP_SPEC, transportation and mineral_value _PIP_SPEC); insurance dial description mirrors master.py default 1_500_000 dollars liability flat with charge_insurance off since calc v1.20.0; steam-versus-hydrolox water feed ratios reproduce arithmetically (WATER_KG_PER_KG_HYDROLOX = 9.0 times hydrogen fraction one-seventh gives hydrolox 1.286; steam is feed-as-is at 1.00); runtime tables are dated historical records exempt per the R210 precedent. Known open exceptions live under rc-176 (output-block size figure) and rc-183 (destinations currency). Related closure: AC CITATIONS.md has four sections; sweep-history references to a section five were misnumbered, and all five named upstream data sources in section 1 have registry rows.

**spacecost CITATIONS.md fully swept work-level at R231; skip unless its source tables change:** all ten sections resolved against sources.csv. Section 1 provider table maps to specific ids (IG-24-001 = the Oct-2023 OIG audit beside IG-22-003, identified by hosted path /uploads/2023/10/ig-24-001.pdf; rocket_lab_form_10q_fy2026_q1 read at R128). Section 3: taylor2018, elvis2011, curtis_orbital_mechanics_engineering_students, dra5_2009 + drake_2008 (SP-2009-566), sp4029 Orloff; NTRS/JPL design-handbooks line = generic class pointer per prose-pointer convention. Section 4: autonomy row claimed by open rc-106, refinery throughput row by open rc-178, remainder resolves (jpl_dsn_services_catalog_820_100, damodaran_cost_of_capital_by_industry, planetary_society_pebd_mission_costs, IG-23-010, frieman_2021, kleinhenz_paz pair, MIL-HDBK-189C). Section 5 every input named has a dedicated row; sections 7 to 10 tooling and meta class - documented NOT registered (quietqueue precedent R222).

Extracted data: `extracted_data/r208_star48b_case_fraction_key_numbers.csv`.

## R245 - Atlas V LEO band re-anchored to the hosted Rev 11 user guide (2026-10-23)

The Atlas V row note declares its own LEO figure unsourced ("whose own source is not recorded"). The GR-hosted Rev 11 Launch Services User Guide (cleared OSR 10-S-0689, pulled live at R99) settles it: Table 2.6.5-2f prints the Single Burn figure at 200 km as Payload Systems Weight 18,814 kg [41,478 lb], conditions CCAFS SLC-41 with the 5-m Short fairing, park orbit perigee at least 167 km, confidence level 2.33 sigma GCS - exactly the band low end upstream carries. A full-document scan of all 420 pages finds zero occurrences of 18,850, so the high end matches nothing in the guide; rc-189 cites the table and asks for the upper figure to be adopted away or documented. PSW semantics (adapter included) are flagged in the proposal.

Extracted data: `extracted_data/r245_atlas_v_leo_key_numbers.csv`.

## R247 - PSLV failure record moves onto ISRO mission status pages (rc-191) (2026-10-23)

INDEX replace-flag for the_week_2026_isro_pslv_reporting named two institutional replacement classes: NSIL price statements and ISRO
failure-analysis releases. The second class resolves at primary level: ISRO publishes mission status pages for both flights. C61 page states "Due to an observation in 3 rd stage, the mission could not be
accomplished" and flight-63/XL-count context; C62 page states the PS3 anomaly sentence verbatim with no failure verdict. The launcher list marks
C61 Not accomplished but carries no outcome mark for C62 - so the institutional record supports a failure statement for C61 only, plus an
initiated-analysis status for C62. Upstream causal clause (flight control near stage separation) is committee/news-level detail not on these pages;
rc-191 proposes citing the three registered T3 rows and restating to institutional wording. The pricing half of the flag stays open: NSIL (nsilindia.co.in) publishes no tariff PDF in launch-services or brochures pages, and the 60-page ISRO
Space-in-Parliament compendium carries zero per-launch unit-cost statements.

Extracted data: `extracted_data/r247_pslv_failure_status_key_numbers.csv`.

## R248 - Vega C payload cells move onto the guide that already carries its fairing citation (2026-10-24)

Owner replace-flag wikipedia_launch_vehicle_articles executed for the Vega C row. The Arianespace Vega C Users Manual Issue 0 Rev 0 (May 2018) byte-matches the R99 access_status record (sha in r248 key-numbers file). The guide publishes its payload figures as text at exactly two points: Table 2.4.2.a polar orbit 500 km at inclination 88 deg = 2,250 kg including adapter, and the section 2.4.3 equatorial elliptical statement of 1,700 kg at apogee 5,700 km - both spans count==1; SSO performance exists only as Figure 2.4.1.e chart (rendered reading about 2,150 to 2,250 kg at 700 km, axes capped at 2,700 kg). Consequences recorded in rc-192: the row low end of 2,250 kg is confirmed directly by the manufacturer document (vehicles.py comment "500 km polar" matches Table 2.4.2.a), while the 3,300 kg high end occurs zero times in all 118 pages and exceeds even the chart ceiling; stored headline LEO of 2,720 kg is above every circular-orbit figure this guide publishes; single-point anchoring at 2,250 kg moves usd_per_kg_to_leo from 16580.88 to 20044.44 (+20.9 percent) at the unchanged price cell. GTO stays zero - no GTO capability statement exists in the document. The Figure 2.4.1.e reading carries a chart-reading flag.

Extracted data: `extracted_data/r248_vega_c_performance_key_numbers.csv`.

## R249 - Minotaur IV payload figures traced to Wikipedia infobox with orbit parameters dropped upstream (2026-10-24)

The row cites Wikipedia for price and the NG guide for fairing volume, but the three payload numbers (headline 1660 kg, band [1591..1735]) are attributed nowhere. The Wikipedia Minotaur IV infobox states Capacity Payload to LEO Altitude 200 km (120 mi) Orbital inclination 28.5 deg Mass IV: 1,591 kg (3,508 lb) - the stored low end matches exactly and wiki supplies orbit parameters that upstream dropped; wiki itself cites the NG guide for its sub-orbital figure. Guide Release 2.5 (byte-identical to the R99 copy) has a text layer that holds zero occurrences of any stored number: all Minotaur IV performance is curves only, Figures 3.3-1 and 3.3-2 fleet comparison for SSO out of KLC/PSCA and 28.5 deg inclination out of CCSFS plus per-site Figures 3.3.1-1 through 3.3.1-4. The section 3.3 definition (count==1) says curve values are total mass above the standard, non-separating interface with separation system and any payload adapter included in the payload allocation - a different convention from satellite-mass semantics. High end 1735 kg is found in neither current Wikipedia nor guide; headline 1660 differs from its own band midpoint 1663, violating the v1.16.0 centre policy by 3 kg. Only prose capability figure in the whole guide belongs to Minotaur VI+ (3360 kg), count==1. rc-193 records all of this; no curve values were read from Figures 3.3-2/3.3.1-x.

Extracted data: `extracted_data/r249_minotaur_iv_payload_key_numbers.csv`.

## R250 - Electron capacity sentence traced into the guide that already carries its fairing citation; high end 320 unsourced (2026-10-24)

The row attributes price to Rocket Lab Form 10-Q FY2026 Q1 and fairing volume to Payload User Guide v7.0 p26, but the sentence Current published capacity 300 kg LEO / 200 kg SSO names no document. The registered guide (byte-identical to the R99 copy) publishes both figures as verbatim text: two prose spans for up to 300 kg / 660 lbm LEO and a specs block span NOMINAL PAYLOAD 200 kg / 440 lbm To 500 km SSO, each count==1; the performance section adds Electron is designed to place payloads of up to 200 kg into a circular SSO at 500 km altitude (count==1) on a page that prints legacy footer Launch: Payload User Guide V 7.0 inside the v8.0 file, consistent with upstream citing the earlier edition for identical content. The stored band high end 320 kg exists nowhere in the document as a mass figure - zero occurrences of 320 kg / 310 kg / up to 320 across all 72 pages; bare 320 appears only as fairing millimetre dimensions and standalone 310 is an axis tick on the Elliptical Orbit Payload vs Apogee chart. Arithmetic: payload headline equals its band midpoint (310) so the centre policy holds there, but price headline 8130000 deviates -0.854 percent from midpoint of its own [7100000..9300000] band; usd_per_kg_to_leo=26226 is consistent with stored cells (8130000/310). Single-point re-anchor at the published 300 kg moves usd_per_kg_to_leo to 27100 (+3.3 percent) - recorded in rc-194 for adjudication together with a proposal to cite the guide directly and to document or drop the unsourced high end.

Extracted data: `extracted_data/r250_electron_payload_key_numbers.csv`.

## R251 - band_centre is a geometric mean to 3 significant figures; full-table audit finds no violations (2026-10-24)

spacecost/vehicles.py at b5eb32a corrects how Rounds 248-250 framed internal consistency: v1.16.0 derives headline price and payload as band_centre(low, high) = float("%.3g" % sqrt(low x high)) clamped inside the band - "Geometric rather than arithmetic because launch prices and payloads are uncertain by FACTORS, not by fixed amounts" (docstring verbatim at L1981-1982). The docstring itself names the Atlas V narrow-band clamp case: 18,814-18,850 kg centres at 18,832 which rounds to 18,800 - exactly reproducing why rc-189 found the stored headline equal to the band low end. Reproducing that function exactly over all 152 banded headline cells in reference/launch_vehicles.csv gives ZERO violations: Minotaur IV sqrt(1591 x 1735) = 1661.4 -> 1660 stored; Vega C sqrt(2250 x 3300) = 2724.9 -> 2720 stored; Electron price sqrt(7100000 x 9300000) = 8125884 -> 8130000 stored - each an exact match to the documented centre. Consequence: the arithmetic-midpoint inconsistency observations recorded in rc-192 (band centre 2775 vs headline 2720), rc-193 (midpoint 1663 vs headline 1660) and rc-194 (price -0.854 percent below midpoint 8200000) were misreadings; dated SELF-CORRECTION clauses have been appended inside those cells with all original text preserved, statuses remain open on their payload-provenance findings which are unaffected (unsourced high ends 3300 / 1735 / 320 stand). Headline-vs-band consistency is tested with band_centre() semantics, not arithmetic midpoints; that invariant holds perfectly across the table - no upstream value change is warranted by centre policy anywhere in launch_vehicles.csv.

## R252 - Ariane 6 LEO payload bands - attribution and capacity currency (rc-195) (2026-10-25)

The A62 and A64 rows store LEO bands [10300..10350] and [21500..21650] kg with no document named for the payload column in either note. Re-fetching the ESA overview page (registered row esa_ariane6_overview) re-verified its two official figures verbatim count==1: A62 approximately 10.3 t and A64 approximately 21.6 t to LEO. The stored values sit on those points exactly - the A64 headline reproduces the official figure under the geometric-mean band_centre policy (fact #62) - but none of the three endpoints appears in any fetched document, formatted or bare: synthetic padding of the class documented for Vega C (rc-192), Minotaur IV (rc-193) and Electron (rc-194). The ArianeGroup VA269 launch kit dated 17 June 2026 (registered this round as arianegroup_va269_launch_kit_jun_2026) publishes the P160C booster upgrade raising official A64 capacity to approximately 22 tons LEO, above the stored band high end; no upstream file mentions it. The User Manual Issue 2 Rev 0 re-fetched byte-identical to the R99 copy and its text layer across all 171 pp carries no LEO mass figures at all (page 39 is a mission-phase timeline), so it cannot anchor the bands either. rc-195 proposed attribution plus currency restatement; price cells untouched.

Extracted data: `extracted_data/r252_ariane6_leo_payload_key_numbers.csv`.

## R253 - Saturn V LEO band provenance (rc-196) (2026-10-25)

Sixth instance of the unsourced-band-endpoint seam family (after Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195). Saturn V payload columns carry no document attribution upstream; two NTRS records now hosted here supply official provenance: press-kit statement 285,000 lb to LEO (= headline) and rated comparison figure 262,000 lb / 118.8 mT (= low end). The high end 140,000 kg matches no NASA document found; Skylab-era delivered mass was about 77 t in orbit.

Extracted data: `extracted_data/r253_saturn_v_leo_capability_key_numbers.csv`.

## R254 - Vulcan Centaur LEO band provenance (rc-197) (2026-10-25)

Seventh instance of the unsourced-band-endpoint seam family (after Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195, Saturn V rc-196). The registered Oct 2023 user guide (sha in registry row) publishes all three stored Vulcan LEO figures in Table 2.2.1-1 for the ISS representative orbit at 407 km and inclination 51.6 deg - VC2S 16,300 / VC4L 21,400 / VC6L 25,600 kg, each span count==1; the strings 27,200 RL10E and upgraded Centaur have zero occurrences in all 85 pp. The VC6 band high end comes from a different ULA document: the one-page Vulcan Centaur technical summary sheet (registered this round as read-not-hosted), which defines LEO as a 200 km circular orbit at inclination 28.7 deg and prints the across-configuration capacity line 10,800 – 27,200 kg count==1; word coordinates map that line to the LEO label, separating it from the GTO range above. Wikipedia cites the same sheet URL for its infobox figure, so upstream notes of figures via Wikipedia resolve onto both documents once named - rc-197 proposes attribution and orbit-parameter restatement with no value change.

Extracted data: `extracted_data/r254_vulcan_leo_key_numbers.csv`.

## R255 - Proton-M LEO band onto ILS PMPG Rev 7 Table 2.2-1 (rc-198) (2026-10-26)

Eighth instance of the unsourced-band-endpoint seam family (after Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195, Saturn V rc-196, Vulcan Centaur rc-197). The Proton-M row attributes its LEO capacity to Wikipedia only. Resolution is unusually clean because the document spacecost already cites for fairings — ILS PMPG Rev 7 (LKEB-9812-1990, July 2009) — publishes the payload figures itself: Table 2.2-1 Summary Proton M Performance (PSM) to Reference Orbits lists circular LEO at H = 180 km as 23.0 MT for i = 51.5 deg, 22.0 MT for i = 64.8 deg and 21.0 MT for i = 72.6 deg (three-stage Proton M; the Breeze-M column shows an em dash for LEO). Row-band word coordinates on PDF p.47 prove each label-value pairing rather than relying on reading order, and all three numbers match the stored headline plus both band endpoints exactly — unlike rc-197 no second document is needed because one table carries the whole range; the inclination qualifier (and the H = 180 km orbit definition) is what upstream drops.

PMPG Rev 7 (ilslaunch.com; 20342733 B, sha256 18f4472216699242840e2a893685abade30cbfae266c501892d5355acafe4d32); running footer Cleared for Public Release Through OFOISR; no in-file copyright grant (page-2 revision notice records the DOD Office of Security Review case and supersedes Revision 6 dated December 2004). The capability figures are searchable text, not image-only, and use MT notation (23.0 MT), not comma forms (23,000 kg).

Not opened: upstream payload_gto_kg = 6600 matches none of Table 2.2-1 GTO rows (GSO 3250 kg; GTO with 1500 m/s to GSO 6150 kg at i = 23.2 deg Hp 4120 km; GTO with 1800 m/s to GSO 6920 kg at i = 31.1 deg Hp 2175 km) — the Wikipedia infobox carries 6,920 and 6,300 variants; which one the stored figure intends is untraced.

Extracted data: `extracted_data/r255_proton_leo_key_numbers.csv`.

## R256 - Soyuz-2.1a band drops its cited Vostochny maximum (rc-199) (2026-10-26)

Ninth probe of the launch-vehicle payload seam family and a new class: data-vs-data inside upstream's own named source. The Soyuz-2.1a row cites Wikipedia payloads by launch site, and its stored band [6800..7430] reproduces that infobox exactly as Plesetsk-A (i = 72 deg) minimum and Baikonur-A maximum — but the same table prints Vostochny A = 7,460 kg at the identical 51.6 deg class, so the stored high end silently drops the cited source's own maximum by 30 kg while the note claims coverage across launch sites. rc-199 proposes either adopting 7,460 (headline 7120 via band_centre; usd_per_kg_to_leo $4557 to $4551) or stating a Baikonur-only selection rule. The -1b row is unaffected: Baikonur B 8,670 exceeds Vostochny B 8,600.

Third-site context extracted this round and recorded in the CSG manual registry row (closing its R99 flagged extraction follow-up): Arianespace prints Kourou LEO performance of 4,850 kg at Za = Zp = 920 km inclination 52 deg — far below the Baikonur figures because a 52 deg orbit from the equatorial site is high-energy; CSG manual performance numbers are not comparable to Baikonur-based bands.

Stale-reference finding (documented, NOT registered): Wikipedia reference 19 for the payload sentence points at the STARSSEM Soyuz User's Manual (starsem.com), dated April 2001 (ST-GTD-SUM-01 Issue 3 Rev 0; © Starsem 2001 All rights reserved; 8,855,821 B sha256 550768027ceb84a73c12a3643901e487d3c7617a37eb525e10fe0d54a8196064), predates the Soyuz-2 first flight and mentions neither the -1a nor any of these figures.

Extracted data: `extracted_data/r256_soyuz_leo_key_numbers.csv`.

## R258 - Long March 12 band onto SAST and Xinhua figures (rc-201) (2026-10-26)

Tenth probe of the payload-band seam family. The Long March 12 row attributes capacity to Wikipedia payloads; tracing both endpoints lands on named documents: low end equals the SAST design target reported by Straits Times Feb-26-2024 (span count==1) and high end equals the Xinhua background page at first flight carried on english.www.gov.cn Dec-1-2024. New wrinkle for this family: the official figure is a floor - no less than 12 tonnes in low Earth orbit - so using it as band maximum understates capability; rc-201 asks notes to say so and name the documents, values unchanged (headline reproduces geometric-mean convention at 11000; usd_per_kg_to_leo consistent at $5745). Xinhua also prints no less than 6 tonnes to a 700 km sun-synchronous orbit; upstream has no SSO column, recorded in the key CSV for context.

Extracted data: `extracted_data/r258_lm12_payload_key_numbers.csv`.

## R259 - Kuaizhou-11 price cells disagree with the cited rate (rc-202) (2026-10-26)

Eleventh probe of the payload-band family, this time on price cells: Kuaizhou-11 notes quote Wikipedia's rate (roughly $10,000/kg, i.e. ~$15M full) and the registered saved copy prints exactly that in its spec table ($10,000/kg ($4,500/lb), span count==1) - but the stored list_price_usd is $12200000 and usd_per_kg_to_leo 8133, so three numbers on one row disagree with each other; rc-202 [value] proposes aligning to the cited rate (price $15000000, per-kg $10000) or naming a different document. Payload side stays proven: prose 1,500 kg LEO equals stored payload_leo_kg exactly.

Not opened: KZ-1A band [300..400] versus the same table printing 450 kg for KZ-1A Pro (first flight 4 Dec 2024, span count==1) and wiki prose itself inconsistent (400 in table vs 450 in upgrade sentence); the article also prints SSO figures upstream has no column for: KZ-1A 200 kg @700 km SSO and KZ-11 1,000 kg @700 km.

Extracted data: `extracted_data/r259_kz11_price_key_numbers.csv`.

## R260 - Kuaizhou-1A band ceiling against the CASIC statement (rc-203) (2026-10-26)

Twelfth probe of the payload-band family and the resolution of R259's noted item: for Kuaizhou-1A the institutional record runs against the stored band ceiling. CASIC's own statement, carried by China Daily on Oct 27 2021 (saved copy sha in registry), prints official point values - SSO 200 kg and LEO 300 kg - exactly equal to the stored floor; the Gansu bureau report for the same mission says designed to launch low-orbit satellites weighing under 300 kg (count==1). The ceiling of 400 rests only on wiki table cells [20][21]; SpaceNews coverage that day attributes 660 pounds (300 kilograms) LEO to Expace, matching CASIC. rc-203 [citation]: cite both saved pages in notes with semantics recorded; no value change - headline 346 reproduces the geometric-mean convention exactly and sits 15.3 percent above the official point value.

Provenance map now complete for this vehicle: LEO floor = CASIC official (matches); ceiling = aggregator wiki cells (unbacked); per-kg rate $20,000/kg printed in the same wiki table and reproduced exactly by stored usd_per_kg_to_leo 20029; KZ-1A Pro at 450 kg remains an upstream content decision (new variant not listed), NOT a sourcing defect - R259 note stands.

Extracted data: `extracted_data/r260_kz1a_official_capacity_key_numbers.csv`.

## R261 - Nuri LEO figure stored without its altitude qualifier (rc-204) (2026-10-26)

Thirteenth probe of the payload-band family and its first pure SEMANTICS hit: for Nuri (KSLV-II) there is no numeric contradiction between upstream and its cited Wikipedia article - both print 3,300 kg to LEO - but the article ties that figure to an altitude of 200 km while KARI, the national agency that built the vehicle, states a 1.5-ton-class satellite to low Earth orbit at 600-800 km (and the same figure for sun-synchronous orbits at approximately that band; saved copies shas in registry). Upstream stores the single point unqualified, so usd_per_kg_to_leo $11121 prices a rocket at an orbit its own agency never claims for it: 2.2-fold capacity overstatement and roughly half the per-kg cost relative to institutional semantics (about $24467/kg on 1.5 t). rc-204 [citation]: cite both KARI pages, record the altitude qualifier; no value change - owner adjudicates column semantics.

Attribution-quality sweep of all 75 rows at spacecost@2bd5e20: notes classified URL / named-doc / wiki-only / vague. Long March 5 corroborated: its stored 25 t matches the official near-Earth figure carried on gov.cn pages - documented here as consistent, no RC.

Extracted data: `extracted_data/r261_nuri_capacity_semantics_key_numbers.csv`.

## R262 - Zhuque-3 mode and variant attribution (rc-205) (2026-10-26)

rc-205 [citation] on Zhuque-3: two defects live in one note cell. First, mode semantics - the table convention is explicit mode rows (Falcon 9 reusable at 17,400 kg beside Falcon 9 expendable at 22,800 kg), yet this unqualified row stores only the down-range-recovery figure while its own note quotes expendable 11.8 t; usd_per_kg_to_leo $4425 therefore prices one mode silently (about $3000/kg at the expendable figure). Second, variant attribution - upstream says 21 t / 18.3 t belong to an enlarged ZQ-3E still in development; that split is Wikipedia-only: LandSpace own release calls the rocket Zhuque-3 (model code ZQ-3), gives full length 76.6 m and states expendable LEO capacity reaching 21.3 t with down-range recovery at 18.3 t (Chinese spans count==1, translation in registry rows). The Global Times debut report shows the flown vehicle stands 66.1 meters tall - a shorter configuration than the maker spec page carries those figures on. Proposal cites all three witnesses and records mode semantics; no value change.

Extracted data: `extracted_data/r262_zhuque3_capacity_attribution_key_numbers.csv`.

## R263 - Angara A5 price onto the Khrunichev 2019 report (rc-206) (2026-10-26)

rc-206 [citation] on Angara A5: price cell was bare Wikipedia; the manufacturer financial disclosure exists and brackets it - BBC Russian quoting the Khrunichev 2019 report puts production cost at 7 billion rubles (about $108.1M at WB 2019 official rate, or $95.0M converted at 2021) against stored $100M - within five percent either way, citation moves and no value changes. Payload side fully corroborated: Khrunichev page quoted by BBC gives exactly 24,5 тонны (= stored 24,500 kg); a Roscosmos-quoted spec line reads the band 24 to 24.5 t; Interfax counted the Vostochny debut as the fourth A5 flight and upstream own fairing note names the Jun-19-2025 Plesetsk launch (the fifth) - five-flights claim reconciles against institutional tallies.

Convention finding: every one of 76 rows in launch_vehicles.csv carries reference_year=2026 while thirteen notes state explicit source years from 2010 to 2023 - the field is a table-vintage as-of stamp, not a dollar-year; dollar-year RCs against this file belong only where conversion math itself is wrong (rc-171 class). Also recorded: Proton-M contract cost of 2.33 billion rubles per unit via RIA state procurement in the same BBC article (about $32.3M at WB 2020 rate) - institutional context for the Angara-expensive note; no Proton row exists upstream to attach it to.

Extracted data: `extracted_data/r263_angara_price_corroboration_key_numbers.csv`.

## R264 - Long March 5 capacity misattributed to the 5B (rc-207) (2026-10-26)

rc-207 [citation] on Long March 5: the note clause attributing the stored LEO figure to the Long March 5B contradicts the institutional record - SCIO pages give LM-5 own capacity as 25 t to LEO and 14 t to GTO (CALT figures, span count==1) while the 5B official figure quoted from the same development team is 22 t. Stored values match LM-5 itself exactly; clause moves, no value changes.

SELF-CORRECTION of a Round 261 line: that block asserted “Long March 5 corroborated: its stored value of 25 t matches the official near-Earth figure carried on gov.cn pages” without ever fetching such a page - ungrounded at writing time, now superseded. The live fetch shows the attribution ran the other way than that sentence implied: 25 t is LM-5 own published capability and the upstream note misattributes it to the 5B; rc-207 carries the grounded finding.

Seen in SCIO search snippets only, not fetched or verified: Hyperbola-3 company targets of a 12.9-tonne LEO configuration and 8.5 tonnes in reusable mode per the Aug-2024 SCIO commercial-space article; Long March-8A approximate 7 t LEO plus at least 6.4 t to 700 km SSO and Long March-10 figures of 70 t LEO and 27 tonnes lunar-transfer per the Jan-2025 SCIO missions article - both against rows whose notes name no document (Hyperbola-3, Long March variants).

Extracted data: `extracted_data/r264_long_march_5_leo_attribution_key_numbers.csv`.

## R265 - Hyperbola-3 stores the reusable-mode capacity (rc-208) (2026-10-26)

rc-208 [citation] on Hyperbola-3: stored single point equals the reusable-mode capability (both witnesses agree at 8.5 t exactly), so the row prices recovery-mode payload while its own note concedes expendable 13.4 t - $/kg swing from $4988 to $3164 depending on configuration; propose mode-labelled rows per Falcon convention, no value change.

WITNESS CONFLICT recorded for adjudication: company statement via SCIO (Aug-2024) describes a 12.9-tonne LEO first-flight configuration while Wikipedia design specification says 13.4 t expendable - specs moved during development and the two dates bound the number; neither is final without a current i-Space product sheet.

The Wikipedia article is at Hyperbola_rocket_series (Hyperbola_3 does not exist).

Extracted data: `extracted_data/r265_hyperbola_3_modes_key_numbers.csv`.

## R266 - Long March 8A LEO figure contradicted by CALT (rc-209) (2026-10-26)

rc-209 [value] on Long March 8A: stored LEO single point 10 t is contradicted by both current witnesses and absent from its own named source (zero occurrences in the fetched Wikipedia article) - CALT via SCIO gives approximately 7 tonnes for this variant; re-anchor proposal recomputes $/kg family live ($5,290 -> $7557). This is the first outright value contradiction in the wiki-family rows (earlier rounds found provenance gaps and mode semantics).

Corroboration recorded: SCIO Jan-2025 article also carries the Long March-10 disclosure (70 t LEO, lunar-transfer 8.2 to 27 tonnes) matching the existing Long March 10 row note class - that row gains a witness without an RC since figures agree exactly.

Staleness noted without RC: wiki launch statistics line shows twelve flights for variant 8A against eleven stored (catalog_date 2026-09-23 predates the latest flight). Flight-count currency is table-vintage material, not sourcing defects.

Extracted data: `extracted_data/r266_long_march_8a_leo_key_numbers.csv`.

## R267 - Gravity-1 capacity attribution onto manufacturer disclosure (2026-10-26)

Orienspace publishes its own Gravity-1 parameter block on www.orienspace.com: 运载能力-近地轨道 吨 6.5 and 运载能力-太阳同步轨道(500km) 吨 4.2, each count==1 on the saved copy (sha in registry row). The standalone Wikipedia article Gravity-1 reproduces both capacities in its infobox with orbit altitudes - Payload to LEO (200km) Mass 6,500 kg and Payload to SSO (500km) Mass 4,200 kg - and carries the cost sentence The launch cost for Gravity-1 is around US$39 million. each span count==1; its capacity reference resolves to the Orienspace maiden-flight bulletin of 2024-01-11.

Upstream cells: spacecost@c633a57 reference/launch_vehicles.csv row Gravity-1, payload_leo_kg 6500 single point and note clause attributing price and both capacities to Wikipedia. All three figures are present in the named source family, so unlike rc-209 this is not a superseded-figure case; the defect is that no document is named beyond bare Wikipedia while the manufacturer publishes both capacity figures directly, and the LEO altitude qualifier (200 km) printed by the cited infobox was dropped. Launch record currency verified: article infobox shows 4 launches / 4 successes with last flight 15 September 2026, matching stored note text.

Verdict rc-210 [citation]: name both documents in the note (manufacturer page for capacities; cited article for cost), record the LEO altitude qualifier; no value change. Extracted data: extracted_data/r267_gravity_1_capacity_key_numbers.csv.

Not extracted: the same Orienspace page carries Gravity-2 program parameters (GTO figure visible); spacecost has no Gravity-2 row.

## R268 - Kinetica-1 payload attribution onto manufacturer disclosure (2026-10-26)

CAS Space publishes the Lijian-1 parameter block on its official site: 运载能力 1.5t(500kmSSO) 2t(LEO), count==1 on the saved copy (sha in registry row). The state portal restates both figures with orbit qualifiers in prose - can send a payload of 1.5 tonnes to a 500-km sun-synchronous orbit, or a payload of 2 tonnes to low Earth orbit - count==1. The Wikipedia article reproduces the same pair in its infobox (Payload to LEO Mass 2,000 kg / Payload to SSO Mass 1,500 kg) and dates the launch record: Total launches 16 with last flight 20 September 2026.

Upstream cells: spacecost@c633a57 reference/launch_vehicles.csv row Kinetica-1, payload_leo_kg 2000 single point; note attributes payloads to bare Wikipedia and drops the SSO altitude qualifier. Unlike rc-209 all figures are present in a resolvable article - but only at the spaced slug Kinetica 1 (the hyphenated slug is a missing-article placeholder). The price band is self-declared estimated and no witness carries any cost statement, so it remains documented-by-design.

Verdict rc-211 [citation]: name the manufacturer page and the state statement in the note, record the SSO 500 km qualifier; no value change. Extracted data: extracted_data/r268_kinetica_1_capacity_key_numbers.csv.

## R269 - GSLV Mk II attribution onto ISRO plus flight-record contradiction (2026-10-26)

ISRO publishes both stored payload figures on its own vehicle page: Payload to GTO: 2,250 kg and Payload to LEO (Low Earth Orbit) : 6,000 kg, each count==1 on the saved copy. The GTO band high end of 2,500 appears nowhere in that record - another unsourced-band-endpoint instance; the stored headline 2,370 is the geometric mean of a band whose top ISRO does not carry.

The ISRO launch manifest itself lists nineteen GSLV missions from GSLV-D1 on Apr 18 2001 through GSLV-F17/EOS-05 on Sept 04 2026, with four rows marked Mission unsuccessful. The stored note says thirteen flights and two failures; the current Wikipedia family infobox reads Total launches 19 / Success(es) 13 / Failure 4 / Partial failure 2 - the stored number equals the success count, recorded as a conflation provenance hypothesis.

Claims verified accurate and left untouched: NISAR did fly on this vehicle (manifest row GSLV-F16/NISAR Mission dated Jul 30 2025; an earlier suspicion that it flew LVM3 was checked against the agency record and discarded), the price line Cost per launch US$47 million is present in the cited article, and the fairing statement matches ISRO publishing only the 3.4 m metallic PLF and 4 m ogive PLF diameters.

Verdict rc-212 [citation]: name the vehicle page and manifest in notes, restate the flight record per agency data (nineteen launches through Sept 04 2026 with four unsuccessful), flag the GTO high end as unsupported; payload columns unchanged. Extracted data: extracted_data/r269_gslv_mk_ii_key_numbers.csv.

## R269 - attribution-quality sweep of launch_vehicles.csv banked (2026-10-26)

All 76 rows classified from the notes field at spacecost@c633a57: forty-three name a document, nineteen cite bare Wikipedia or company-via-Wikipedia, fourteen are self-declared estimates. Bare-wiki rows already claimed by open RCs through this round: Vega C rc-192, Minotaur IV rc-193, Electron rc-194, Ariane 6 rc-195, Vulcan rc-197, Proton-M rc-198, Long March 12 rc-201, Kuaizhou-11 rc-202, Kuaizhou-1A rc-203, Nuri rc-204, Zhuque-3 rc-205, Hyperbola-3 rc-208, Long March 8A rc-209, Gravity-1 rc-210, Kinetica-1 rc-211, GSLV Mk II rc-212. Unclaimed bare-wiki rows: Long March 4C (price estimated against sister 4B), Long March 6A, Long March 7 (names CASC but no document), Zhuque-2E, New Glenn 9x4 / Terran R / Nova / Tianlong-3 (company statements via Wikipedia), Soyuz-5. Jielong-3 self-discloses its SSO-as-LEO substitution = documented-by-design skip.

## R270 - Long March 7 payload attribution onto CALT statements (2026-10-26)

Both stored figures trace to China Academy of Launch Vehicle Technology statements carried by state media. For the two-stage vehicle: can send 13.5 tons of payloads to the low-Earth orbit and 5.5 tons to Sun-synchronous orbit (Jul 2025 mission report, count==1) - the stored LEO single point 13,500 equals the official figure exactly, and the SSO number on the same line has no upstream column. For the three-stage variant: is capable of placing a 7-ton spacecraft to geosynchronous transfer orbit (Aug 2026 failure report, count==1) - stored GTO 7,000 kg exact.

Flight-record boundary: the same Aug 2026 report closes with second launch failure for the Long March 7A, which has been used in 17 space missions. Current Wikipedia statistics read sixteen flights two failures for the variant - wiki lags the institutional count here, so the stored note text of two failures in eighteen is plausibly correct or ahead and is left untouched; no mission-by-mission manifest was found to date the final flight.

The upstream attribution CASC / Wikipedia payload figures names the right agency but no document. The wiki infobox additionally carries orbit parameters (LEO altitude 200 to 400 km at inclination 42 degrees) that the CALT statements do not print.

Verdict rc-213 [citation]: name both China Daily carriers of CALT statements in notes with variant qualifiers; no value change. Extracted data: extracted_data/r270_lm7_capability_key_numbers.csv.

## R271 - Zhuque-2E latest-flight date contradicted by its own launch total (2026-10-26)

Two state-media-carried LandSpace reports bracket the family flight record. The May 2025 report states that mission was the fifth of the ZQ-2 series (count==1); with base flights December 2022 failed plus July and December 2023 successful, that puts the ZQ-2E Y3 loss on Aug 15 2025 at family flight six. The September 2026 report calls its launch the sixth flight of the ZQ 2E variant [appears twice] - a success carrying ten satellites - which makes the family total nine with two failures, exactly matching stored counts.

But that same arithmetic contradicts the stored latest-flight clause: if nine launches through September 2026 are counted then the latest flight is Sep 2026, not Aug 2025 as the note text says; and if counting stopped at August 2025 the total would be six. The row is internally inconsistent whichever way it was compiled - rc-214 [value] proposes redating the latest-flight clause to September 2026 or dropping the month claim, counts unchanged.

Verified accurate and untouched: the failure cause text second-stage voltage fault matches the company review-board wording quoted by trade press (second-stage servo power bus voltage abnormally dropped); the milestone first methalox rocket to reach orbit with year 2023 is verified verbatim against the cited Wikipedia article for the July 2023 flight; SSO figure 4 t gains a company statement via state media with the 500 km altitude qualifier restored.

Evidence boundary recorded: no institutional statement of a ZQ-2E LEO capacity figure was found this round - the stored single point 6,000 kg remains Wikipedia-sourced; no LandSpace page read carries an LEO number.

Verdict rc-214 [value]: redate latest-flight clause per Sep 2026 report, cite both carriers for the record chain and SSO figure; launch counts, failure cause text, milestone claim unchanged. Extracted data: extracted_data/r271_zq2e_launch_record_key_numbers.csv.

## R272 - Long March 6A debris and payload claims vindicated by institutional records; citation move (2026-10-26)

The LM-6A note carries two unsourced clauses beyond its bare Wikipedia payloads attribution. Both check out against institutional sources, so this round opens a citation-move candidate rather than a value defect.

Debris history: NASA Orbital Debris Quarterly News vol 27 issue 3 Table 1 (reference date 01 June 2023) lists the YUNHAI 3 CZ-6A R/B breakup of 12 November 2022 with Cataloged to Date 781 and On Orbit 722 fragments - stored phrasing 700+ tracked pieces is correct against NASA records, and the same article ranks the event behind only Fengyun-1C, Cosmos 1408 and Cosmos 2251 in cataloged debris produced. The several flights phrasing also holds: the registered Wikipedia article documents three further upper-stage events after November 2022 (launches of 26 March 2024, 4 July 2024 and 6 August 2024), with the US SDA confirmation for the August event cited there; SpaceNews independently reported the pattern in July 2024 (witness recorded not registered per R271 convention). ODQN v28 issues two and three were scanned this round: zero CZ-6A mentions - NASA has no published account of the later events.

Payload pair: current Wikipedia carries both stored figures exactly (LEO 8,000 kg; SSO at 500 km 6,500 kg), but its LEO citation is a Zhihu column post. CASC own product page publishes only one capacity figure - SSO at 700 km not less than 4 tonnes (span count==1) - and no official LEO statement exists; the zh-wiki article attributes LEO payload capacity of 8 t and above to the Zhang Weidong et al technical paper in International Space. Boundary recorded: stored LEO 8 t is consistent with that literature chain, not with a CASC product-page figure.

Launch record untouched: note self-dates twenty-six for twenty-six to Jul 2026; current wiki statistics read Total launches 28 Success(es) 28 with first flight 29 March 2022 matching the stored variant history - consistent under the R270 flight-record boundary rule.

ODQN vol 27 issue 3 hosted in full_texts (public-domain US government work; zero copyright tokens across all pages). Verdict rc-215 [citation]: name ODQN + CASC page + wiki article for the debris and payload clauses, values untouched. Extracted data: extracted_data/r272_lm6a_debris_record_key_numbers.csv.

## R273 - Long March 4C payload attribution and institutional SSO spec (rc-216) (2026-10-27)

The stored row keeps LEO 4,200 kg and GTO 1,500 kg attributed to bare Wikipedia. Current article verified: both figures exact against the infobox capacity block, but every citation there is a skyrocket.de snapshot accessed April 27, 2008 - one aging reference carries all three numbers of an active rocket. The institutional record only ever speaks sun-synchronous: the CASC product page (dated September 15, 2015) prints its spec sentence with SSO-transfer wording at 2.8 tonnes at 800 km, and current launch reports through April 17, 2026 print 3 tonnes at 700 km. Upstream has no SSO column for this launcher, so the one officially published capacity figure is invisible in spacecost while two unofficial ones are stored - recorded as semantics context, values untouched per citation-move convention.

Launch record: infobox statistics Total launches 59 (Successes 57) with Last flight April 17, 2026; the same-day CASC report corroborates no flights since. Stored ~59 is current exactly. The stored price cell self-declares estimated against the sister Long March 4B figure of 50 million dollars dated 2006 - documented-by-design class (zero cost statements on any fetched institutional page), untouched.

Witness hosts: three T4 verified_live_not_pulled rows registered d04 with full sha256 in access_status; no hosted files this round. Extracted data r273_lm4c_payload_attribution_key_numbers.csv.

## R274 - Tianlong-3 failure timing clause vs company investigation record (rc-217) (2026-10-27)

The stored note says the maiden flight FAILED shortly after liftoff. That phrase has count==0 in the cited Wikipedia article and contradicts the institutional record: Space Pioneer published a return-to-zero investigation statement (official WeChat account; sha recorded) whose timeline spans each verify count==1 - design MaxQ at T+110 s, all scheduled first-stage sequences completed at T+177.2 s, normal stage separation at T+182.2 s, second-stage ignition at T+185.9 s, loss of control from lower-than-expected altitude at T+189.5 s and commanded flight termination about three minutes in. The China Daily report of April 4, 2026 carries the company failure announcement (was unsuccessful on Friday afternoon; flight became abnormal before it could reach its preset orbital altitude) - neither source supports a liftoff-adjacent early-failure characterization, which matters because first-stage success is exactly what reusability progress modeling would key on. Proposal restates per institutional record and names all three witnesses; payload pair (LEO 17 t / SSO 14 t exact vs current wiki), single-flight status (Total launches 1 Failure 1), June 2024 test-stand runaway clause (consistent with Reuters-backed reporting) and the self-declared price estimate are untouched.

Witness hosts: three T4 verified_live_not_pulled rows registered d04 with full sha in access_status; the WeChat statement page (3.5 MB HTML) carries no licence grant, so extraction only. Extracted data r274_tl3_failure_status_key_numbers.csv.

## R275 - Terran R capacity attribution (rc-218) (2026-10-27)

- Manufacturer publishes all three Terran R capacity figures mode-labelled (downrange landing versus expendable configuration), each span count==1, matching stored values 23500 / 5500 / 33500 exactly; the note concession that GTO is not re-stated for the reusable config is outdated as of this fetch.
- Wikipedia current-revision trap: the Terran_R infobox Capacity block prints only the expendable figure (Payload to LEO Mass 33,500 kg); the reusable-mode figure lives in prose.
- Boundary recorded: stored payload_escape_kg=4000 has zero support on either current page; upstream note concedes legacy status - leave as documented-by-design unless an institutional restatement surfaces.
- Extracted data 04_launch_economics/extracted_data/r275_terran_r_capacity_key_numbers.csv (6 rows).

## R276 - Stoke Space Nova configuration attribution (rc-219) (2026-10-27)

- Configuration split is institutional in both records: Nova = program name; Pathfinder = technology demonstrator versus Block 2 scaled version (manufacturer sentence count==1 and Wikipedia excerpt article Stoke Space Nova agrees). Stored figures belong to the demonstrator while Block 2 publishes up to 15 t LEO fully reusable / 23 t expended plus GTO 4 t.
- Printed-label ambiguity recorded: manufacturer Pathfinder page diagram label reads Fairing 2,500 kg to LEO Reusable against wiki 3 t for the demonstrator; do not treat either as authoritative without a dated press release.
- Propellant-class context: Andromeda second stage burns LH2/LOX while Zenith first stage burns LNG - stored core_propellant=methalox describes the booster only and the table schema allows one value.
- Heat-shield wording verified against manufacturer page text (regeneratively cooled metallic reentry heat shield) - the note claim on that point is supported.
- Extracted data 04_launch_economics/extracted_data/r276_stoke_nova_configurations_key_numbers.csv (7 rows).

## R277 - Kinetica-2 cost-versus-price attribution (rc-220) (2026-10-27)

Defect class: unnamed-source price cell with semantics error. The stored note attributes the rate to 'CAS Space, Apr 2026' but no document is named in CITATIONS.md beyond a bare label; the figure traces to commander-in-chief Yang Haoliang interview carried by Cailianshe dated March 31, 2026 stating non-recoverable single-launch launch COST of 30,000 yuan/kg versus Falcon 9 at 5,000 USD/kg. TMTPost analysis explicitly distinguishes cost wording from published prices in the Chinese commercial market and places common customer quotes at 50k-100k yuan/kg - so price_basis=published plus list_price_usd derived from a cost statement is a category mismatch for owner adjudication (values untouched). Arithmetic sound: 12 t x ¥30,000 = ¥360M; World Bank official CNY average 7.1898 (latest published year) reproduces the ~$50M conversion at $50.07M - no rc-171-class FX defect.
Flight-currency check: Kinetica-2 Y2 completed factory acceptance Aug 25 with an October launch plan but is unflown at audit; Wikipedia lists one flight only, so the stored One-flight clause is current.

Extracted data: `extracted_data/r277_kinetica2_cost_basis_key_numbers.csv`.

## R278 - New Glenn 9x4 fairing-volume contradiction (rc-221) (2026-10-27)

Defect class: manufacturer publishes more than upstream claims. The stored note for the development-status 9x4 row asserts that Blue Origin gave only the 8.7 m diameter and no readable envelope or volume; the company live product page states 'Its 8.7 meter fairing packs 29,000 cubic feet of volume' (count==1) - a directly published internal volume equal to about 821.2 cubic metres (x0.0283168466 computed in-script). The same page prints the capability triple as point values - 70 t LEO, 14 t Geostationary Orbit Direct, 20 t TLI - matching stored payload_leo_kg=70000 exactly; Wikipedia renders them with floor signs (>70,000 kg etc), a rendering difference recorded but not adjudicated. GTO-NaN rationale survives: no GTO figure exists in any witness; only direct-to-GSO. Base-variant sibling check clean on the vehicle page (more than 13 t GTO and 45 t LEO count==1) - no RC there.
Saved copies of the Blue Origin pages are sha-recorded (copyright notice inside: extraction only). Flight-record currency recheck at audit date: Wikipedia statistics still three flights, last April 19, 2026 - stored clause current. The NG-4 vehicle lost on the pad in a May 2026 static-fire test (maintenance tag and Berger reference inside wiki revision) is not a launch failure and does not count against success statistics.

Extracted data: `extracted_data/r278_new_glenn_9x4_fairing_key_numbers.csv`.

## R279 - Soyuz-5 institutional witness conflict at 17 t (rc-222) (2026-10-27)

Witness-conflict class (rc-208 precedent): every reachable institutional statement gives an up-to-17-tonne LEO figure for Soyuz-5 while the Wikipedia revision behind the stored row prints uncrewed 18,000 kg / crewed 15,500 kg. Interfax quoting the Roscosmos press service (Feb 27, 2025): 'The Soyuz-5 can take up to 17 tonnes to the support orbit.' (count==1). The institutional statement predates first flight; wiki postdates it - governing configuration left open for owner.
Arithmetic note: stored headline 16,700 is exactly band_centre of the two Wikipedia figures (geometric mean sqrt(18000 x 15500) = 16,703 to three significant figures), and it sits below the institutional cap - so no headline contradiction; only the 18 t band endpoint exceeds the Roscosmos figure. GTO has no institutional witness at all: stored 5,000 kg remains a Wikipedia-only boundary.
Corroboration bonus from same Interfax copy: 'Its head developer is the Energia Rocket and Space Corporation' (count==1) validates the existing fairing clause that assigns publication responsibility to RSC Energia; wiki manufacturer line lists RKTs Progress co-listed with Energia. TASS schedule context: fully operational in 2028 [appears twice] consistent with stored development status.
The Wikipedia article is at the hyphenated slug Soyuz-5_(rocket); the unhyphenated URL is a missing-article placeholder.

Extracted data: `extracted_data/r279_soyuz5_capacity_witnesses_key_numbers.csv`.

## R280 - Eclipse GTO cell has no witness at all (rc-223) (2026-10-27)

Value contradiction class (rc-209 family): the stored Eclipse payload_gto_kg=3,100 matches nothing fetchable. Firefly own vehicle page spec block prints LEO 16,300 kg / GTO 3,200 kg / TLI 2,300 kg (compound span count==1) and Wikipedia current revision agrees on all three; the figure 3,100 has zero occurrences in either witness. Proposal re-anchors to the manufacturer value (+3.2%); owner decides.
Attribution: notes say 'Source: Firefly / Northrop' - no document named (last unclaimed bare-attribution real vehicle in launch_vehicles.csv after this round). Manufacturer page names Eclipse as joint Firefly/Northrop development, designed for RTLS first-stage reuse; sixth-flight full-reuse clause verified verbatim on Wikipedia.
Exclusions done before comparison: wiki 8,000 kg LEO / 5,800 kg SSO figures belong to the historical Firefly Beta design (2017-2021 era), not Eclipse.
Sweep closure: with rc-223 opened, every real vehicle row in launch_vehicles.csv either names a document or carries an open RC; remaining bare-note rows are concept-class vehicles whose prose cites proposal literature (documented-by-design).

Extracted data: `extracted_data/r280_eclipse_capacity_key_numbers.csv`.

## R281 - tanker-flight band has no publishing hand behind it (rc-224) (2026-10-27)

Attribution class: the storage_systems row Depot refuelling flights to escape says SpaceX's own range and the Starship vehicle note repeats 8-16 quoted, but the fetchable record contains only point figures - OIG IG-26-004 March 2026 plans more than 10 tankers at one every 6 days (p.11), Wikipedia reports Musk's August-2021 tweet of eight launches maybe four.
High-end hypothesis recorded unconfirmed: GAO B-419783 reportedly counted SpaceX HLS concept as depot + 14 tankers + lander = 16 campaign launches; if true, the stored high end 16 is a campaign-total misread as tanker count. GAO B-419783 itself was not read.
Values untouched: 12 stays inside the institutional plan (>10); owner adjudicates whether ASAP October-2026 estimates near 22 flights for Artemis IV refueling widen the band - those figures are NOT in the registered Wikipedia revision and were excluded from evidence cells to keep every quote span verifiable.
storage_systems.csv attribution audit result: unlike launch_vehicles, this table self-declares ESTIMATE on nearly every unsourced cell (COPV PV/W, MLI areal density, fuel-cell Wh/kg, flywheel Wh/kg all carry named near-miss reports). The tanker row was the outlier claiming a publishing hand with no document. Remaining unanchored-but-undeclared cells: Vapour-cooled shield 0.4 fraction (not modelled downstream - context only) and Bulk ore restraint ratio 0.15 feeding return_structure_frac_of_payload.

Extracted data: `extracted_data/r281_depot_tanker_flights_key_numbers.csv`.

## R289 - launch_vehicles.csv derived unit-cost layer proven self-consistent at spacecost@860bef9 (2026-10-28)

All 76 rows of reference/launch_vehicles.csv were swept against their own inputs: for each mode in leo, gto, escape the headline cell usd_per_kg_to_MODE was recomputed as list_price_usd divided by band_centre(payload_low, payload_high) when a payload band exists (the geometric-mean-to-3-significant-figures convention of fact 62, vehicles.py L1978-2004), or the point payload otherwise; bound cells were recomputed as price-low over payload-high and price-high over payload-low. Result: zero mismatches within a 1.5 percent rounding tolerance - no unit-cost cell contradicts its own price or payload inputs, and no headline violates band_centre (extending R251 from the payload headlines to the derived price layer). The table also applies a clean design rule where capability is absent: payload zero with blank unit cost on 76 of the row-mode combinations that lack GTO or escape capability - consistent by construction, not defects. No row carries $/kg bounds without a corresponding payload band, so no bound cell escapes testability.

This derived layer is arithmetically closed at @860bef9; provenance questions on individual prices are covered by the open RCs and the attribution sweep.


## R340 - Propellant launch mass in the composite transfer total (2026-11-03)

`spacecost_summary_propellant_uplift_record_2026` pins spacecost at
`860bef9902aa67fec705875cd52fdb8e6def159f`. `build_transportation_summary` emits
`total_usd_per_kg_payload_to_segment_end` (`tables.py` L123, L160-185) as
L+p*c: one kg of payload launched at the LEO rate L, plus purchase of
p=exp(delta-v/(Isp*g0))-1 kg of transfer propellant at rate c. It does not
charge to lift that propellant. The original `mission_cost_breakdown`
includes outbound propellant in launch mass (`query.py` L217-246).

Use the same reference Falcon 9 reusable and kerolox rates, L=4253 USD/kg,
c=0.896969696969697 USD/kg and Isp=340 s, for a raw 6500-m/s single leg.
The original summary returns p=6.024875312747583 kg and
4258.404130583555 USD/kg. Isolating the original mission helper to one kg
payload, zero hardware, zero return burn, zero operations duration and zero
contingency gives launch mass=7.024875312747583 kg and
total=29882.198835699026 USD. Both purchase exactly
5.404130583555408 USD of propellant. The 25623.79470511547-USD gap is the
unchanged LEO rate times the omitted propellant mass.

Independent mass accounting gives L*(1+p)+c*p; the missing term is L*p.
Sixteen original helper pairs contain eight positive omissions and eight
zero-term controls: four zero-delta-v cases and four propellantless raw
metric limits. Those limits are controls of the arithmetic, not feasible
propulsion recommendations. A standard-library exponential independently
reproduces the original NumPy scalar propellant masses and costs.

The committed `reference/summary_sample.csv` has 868 finite, priced rows:
805 have positive L*p and 63 have zero terms. Its first stored row, Falcon
9 reusable / LEO-to-GTO / kerolox, reports p=1.0788115101939009 kg and a
4253.967661233386-USD/kg total, again charging the payload launch plus
0.9676612333860444 USD of propellant purchase alone.

Two original full-build profiles, reference and recorded fuel-2026-10-26,
each produce 84,132 finite, priced rows: 77,976 have positive omitted
uplift terms and 6,156 have zero terms. Each profile repeats exactly,
including all seven CSV byte hashes and in-memory frames. Readback checks
every populated cell and the full missing-value mask; CSV absence does not
retain the in-memory distinction between pd.NA and NaN. These counts
diagnose the cost identity and do not establish feasibility of every raw
vehicle/segment/propellant combination.

Verdict: `rc-273`, include transfer propellant in the Earth-launched
single-leg cost basis and identify any retained bare-cost proxy explicitly.
No tanks, electric plant, boiloff, return hardware or complete mission
operations are added to this lower-bound comparison. The current Stage-4
loader does not consume this summary (the separate `spacecost_summary_consumer_contract_record_2026`
trace); no profitability or ranking change is claimed. Nineteen local
source/reference blobs match pinned GitHub records; all four upstream main
comparisons remain identical. `extracted_data/r340_transportation_summary_launch_mass.csv`.

## R362 - FAA estimate corroborates the Kuaizhou-11 price basis (rc-202; 2026-11-08)

`faa_ast_2017_compendium_kuaizhou_11_price`, Kuaizhou 11 fact-sheet table
(unnumbered sheet; the accessible text has no printed page number), lists
LEO capacity as 1,500 kg and estimated launch price as "$15M est"; its planned
first-launch field is 2017. The report says its data are maintained in FAA
AST's STAR database and credits preparation to The Tauri Group. This is a
historical preflight estimate, not a current transaction price. It independently
agrees with the ~$15M amount quoted in the current spacecost note and strengthens
rc-202's evidence that the stored $12.2M / $8,133 per kg pair is inconsistent
with that note. No current price is inferred. `extracted_data/r362_kuaizhou11_faa_estimate.csv`.

## R363 - Kuaizhou-11's quoted ceiling does not pin an exact rate (rc-202; 2026-11-08)

`cnsa_2018_kuaizhou_11_price_quote`, CNSA article dated 2018-03-05 and
credited to Xinhua, body paragraph 3, says “报价不到1万美元” (“quoted below
US$10,000”) in the per-kilogram price comparison; paragraph 2 gives a 1.5 t
maximum LEO payload. This ceiling is compatible with spacecost's stored
$8,133/kg ($12.2M / 1,500 kg, rounded), but it does not establish that exact
price. Together with FAA AST's distinct 2017 $15M preflight estimate and the
Wikipedia table's $10,000/kg figure, the sources show different price
expressions, not a resolved current transaction price. rc-202 remains open to
identify the stored value's provenance and make the note's price basis explicit;
the $15M value is not an automatic correction. `extracted_data/r363_kuaizhou11_price_quote.csv`.


## R368 - Later Kuaizhou-11 price report has an unspecified basis (rc-202; 2026-11-08)

`beijing_business_daily_2023_kuaizhou_11_price_cap`, Beijing Business Daily
report republished by China News Service Jingwei on 2023-07-10, paragraph 53,
reports the Kuaizhou-11 launch price as “不超过600万美元” (not more than
US$6 million) and the price per kilogram as “不到1万美元” (below US$10,000).
The paragraph gives no payload capacity, exact quote date, mission configuration,
or whether “price” means an advertised offer, contract, or cost. It is a later
price report than the FAA's 2017 $15M preflight estimate, but cannot by itself
reconcile either the stored $12.2M/$8,133 per kg pair or the note's ~$15M/full
arithmetic. rc-202 stays open for the exact stored-price provenance and price
basis; no replacement value is inferred. `extracted_data/r368_kuaizhou11_price_cap.csv`.


## R369 - Kuaizhou-11 designer states a conditional bulk-order rate (rc-202; 2026-11-08)

`hubei_daily_2022_kuaizhou_11_bulk_price_quote`, Hubei Daily's 2022-12-08
interview with Kuaizhou-11 chief designer Liang Jiqiu, price paragraph, says
KZ-11 “能做到每公斤1万美元以下，订单多的情况下，甚至可以做到6000美元以下”
(can reach below US$10,000/kg, and below US$6,000/kg when order volume is high).
This is a conditional rate attributed directly to the designer, but the article
gives no exact payload, contracted price, or offer configuration. The $8,133/kg
stored rate is within the general ceiling and above the stated high-volume
ceiling; without a confirmed volume condition or exact quote, this does not
establish an error in the generic row or the $12.2M source. rc-202 stays open.
`extracted_data/r369_kuaizhou11_bulk_price_quote.csv`.


## R372 - Kuaizhou-11 database price conflicts with reported quotes (rc-202; 2026-11-08)

The live Next Spaceflight launch-details record for Kuaizhou-11's March 16,
2026 mission lists a vehicle “Price” of US$28.30 million and “Payload to LEO:
1,500 kg”; its May 21, 2024 Kuaizhou-11 record repeats US$28.3 million and
1,500 kg. Dividing the listed vehicle price by the listed LEO capacity gives
US$18,867/kg. That is 2.32 times the stored US$8,133/kg and exceeds the
reported KZ-11 ceilings of below US$10,000/kg and no more than US$6M per
launch. The site does not identify the price's source, whether it is a list
price or transaction, or whether its mass is applicable to the mission's SSO
payload. The two records are the same provider's static vehicle figure, not
independent observations. Treat this as an explicit competing database
estimate, not a verified transaction price; rc-202 stays open to reconcile the
price basis before any value change. Extracted:
`extracted_data/r372_kuaizhou11_nextspaceflight_listing.csv`.

## R373 - CNSA distinguishes Kuaizhou-11 maiden-flight capacity from its catalog maximum (2026-11-08)

CNSA's Xinhua-sourced 26 April 2024 report says the Kuaizhou-11 “made its maiden flight in 2022 with improved carrying capacity of one tonne” (paragraph beginning “The Kuaizhou-11”). The spacecost row read for rc-202 stores `payload_leo_kg=1500`; the report gives no orbit or maximum-capacity qualifier for the one-tonne figure. Verdict: this does not contradict the 1,500 kg LEO maximum, but it shows that the price-per-kg denominator must not be read as a flown mission payload. It does not resolve the provenance or basis of the stored $12.2M. rc-202 remains open. Extracted: `extracted_data/r373_kuaizhou11_capacity_context.csv`.

## R402 - Electron revenue-per-launch range check against Q2 2026 SEC filing (2026-11-08)

`rocket_lab_form_10q_fy2026_q2`, MD&A p. 37, defines revenue per launch as
the “average transaction price attributable to launch contract performance
obligations” in the launch period, regardless of revenue-recognition method;
the filing says the metric varies with orbit, payload handling, launch
location and mission timing. Q2 revenue per launch was $9.1M in 2026 and
$7.9M in 2025; first-half values were $9.2M and $7.5M. At
`spacecost@19e1a31`, Electron stores $8.13M with a $7.1M–$9.3M band, based on
Q1 reported values. The new quarterly and first-half values fall within that
band. No revision candidate. Extracted:
`extracted_data/r402_rocket_lab_q2_2026_electron_launch_economics.csv`.


## R403 - Long March 2D customer batch-fee review signal (2026-11-08)

The Shanghai Stock Exchange-hosted Changguang Satellite IPO inquiry reply says the company bought Long March 2D launch service from China Great Wall Industry Corporation for wide-format satellite batches. Its p. 8-2-95 table reports batch rocket launch fees of RMB 81.0M (2020), RMB 82.5M (2021), and RMB 85.9M (2022), corresponding to listed batch satellite masses of 1,254, 1,389, and 1,421 kg. The note says each batch also carried other satellites. The next paragraph identifies these as Long March 2D services; the filing treats launch monitoring/control separately. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/launch_vehicles.csv` stores Long March 2D `price_usd=30,000,000`, with notes attributing it to a $30M Wikipedia price. The customer batch fees are materially different, but do not establish a like-for-like list-price replacement because customer, batch, rideshare, contract and year bases differ. Open rc-315 to reconcile those bases before changing the row. Extracted: `extracted_data/r403_lm2d_customer_batch_fees.csv`.


## R404 - Long March 3B/E contract price scope (2026-11-08)

Wu Xingyu’s 2025 *Aerospace China* article (pp. 49–50), based on publicly disclosed company contracts, defines domestic Long March “launch service price” as rocket price plus launch monitoring/control fees. It reports ChinaSat-6C’s Long March 3B/E rocket fee at RMB 260M and monitoring/control at RMB 115M; for ChinaSat-6D, 6E and 26, it reports planned rocket fees of RMB 260M, RMB 290M and RMB 290M, each with RMB 115M monitoring/control. Table 1 totals are RMB 375M, 375M, 405M and 405M; the article gives a four-mission average of RMB 390M. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, Long March 3B/E has `list_price_usd=59,200,000` and a $50M–$70M band, with notes citing Wikipedia. The bundled contract totals are in the same broad range after currency conversion, while rocket-only fees are materially lower. This does not establish a replacement list price: one fee is reported as contracted, three are planned, and contract year, exchange rate, and scope differ. Open rc-316 to resolve whether the upstream value represents rocket-only price or bundled launch service. Extracted: `extracted_data/r404_lm3be_chinasat_contract_fees.csv`.


## R405 - Long March 2D bundled service-price cross-check (2026-11-08)

Wu Xingyu’s *Aerospace China* paper (p. 50) states: “2022年采购‘长征’二号D火箭及测控费用为1.129亿元” (in 2022, the purchase of a Long March 2D rocket plus monitoring/control fees was RMB 112.9M). The article pairs this with 4 tonnes to LEO and calculates RMB 28,200/kg for launch service. The upstream `Long March 2D` row at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9` remains `list_price_usd=30,000,000`; the bundled customer amount is a material lower comparator, while R403’s rocket-only fees exclude monitoring/control. It is not a drop-in list-price replacement because it is a dated customer service bundle. **rc-315 remains open** for price and scope reconciliation. Extracted: `extracted_data/r405_lm2d_combined_service_fee.csv`.


## R406 - Gravity-1 dedicated-charter price signal (2026-11-09)

After the Gravity-1 Y2 launch, Jiemian News reports Orienspace co-founder and vice president Peng Haomin saying the vehicle could offer RMB 30,000/kg; he clarifies that this is the dedicated “包车” rate and rideshare service costs more. In the adjacent paragraph the article gives 6,500 kg to LEO and 4,200 kg to 500 km SSO, without specifying which orbit the quote prices. The PBOC/CFETS central parity on 2025-10-10 was RMB 7.1048/USD. Multiplying the dedicated rate by the full stated LEO capacity and converting at that midpoint gives about $27.45M, versus `price_usd=39,000,000` for Gravity-1 at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`; this capacity-scaled comparison is about 29.6% lower. The price quote is a meaningful review signal but not a drop-in replacement: its orbit and utilization basis are unstated and the report does not identify a signed contract. Open rc-317 to reconcile the quote against the stored estimate. Extracted: `extracted_data/r406_gravity1_charter_price.csv`.


## R407 - Long March 12 reported unit-price signal (2026-11-09)

Guangzhou Daily’s Economic Weekly section “火箭发射成本：每公斤正从2万元向1万元迈进” reports: “根据公开信息，目前国产一次性火箭性价比较高的是长征十二号，单位报价已低于2万元/公斤” (according to public information, Long March 12’s unit quote is below RMB 20,000/kg; paragraph 2). It does not identify the underlying source or specify orbit, utilization, quote date basis or service scope. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, the Long March 12 row stores `list_price_usd=63,200,000` (range $50M–$80M; `price_basis=estimate`) and an 11,000 kg LEO midpoint. The per-kg report is a material price-scale review signal, but cannot establish a like-for-like replacement without its pricing basis. **rc-318 remains open** for scope reconciliation. Extracted: `extracted_data/r407_lm12_unit_quote.csv`.


## R408 - eXTP Long March launch-service budget comparator (2026-11-09)

The China Government Procurement Network’s 8 June 2026 pre-procurement consultation for the National Space Science Center’s eXTP launch service lists a proposed budget of RMB 245.2M and China Long March Rocket Co. as the intended provider; the notice does not name a rocket variant. The PBOC central parity on 2026-06-08 was RMB 6.8198/USD, giving a date-matched comparator of $35.95M. Polaris Intelligence’s eXTP launch forecast lists “Long March 3B/G5 or equivalent,” but this is a secondary model attribution. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, Long March 3B/E stores `list_price_usd=59,200,000` with a $50M–$70M reported band. The proposed budget is about 28% below that band’s lower bound, but it is not an awarded price and the exact vehicle/variant is unresolved. This is a scope-sensitive review signal, not a replacement value; **rc-316 remains open**. Extracted: `extracted_data/r408_extp_launch_budget_comparator.csv`.


## R411 - ULA NSSL mission-service price comparator (2026-11-09)

The Space Systems Command release dated 3 October 2025 assigns ULA two FY26 NSSL Phase 3 Lane 2 missions, NROL-88 and USSF-88/GPS IIIF-4, and reports “a total price of $428 million” (paragraph 2). The release gives no individual mission prices or exact Vulcan configurations. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/launch_vehicles.csv` lists Vulcan Centaur VC4 `list_price_usd=$120M`, with an estimated $110M-$130M range; its note says $110M is ULA’s starting price and $130M is an estimate. The combined NSSL price averages arithmetically to $214M per assigned mission, 1.78 times the VC4 estimate. NSSL launch-service scope, orbit, integration, assurance and configuration are not shown as like-for-like with the vehicle price. **rc-321 remains open** for scope and configuration reconciliation. Extracted: `extracted_data/r411_ssc_vulcan_nssl_mission_prices.csv`.


## R412 - Firefly Alpha dedicated-launch price comparator (2026-11-09)

Firefly’s official Alpha Payload User’s Guide v5.2 lists its revision date as July 2025 (PDF p. 2, revision-history table). Page 3 says Alpha is offered “at a price of $19M for a dedicated commercial launch service.” Table 1 on page 3 gives 1,030 kg to 300 km LEO and 630 kg to 500 km SSO. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/launch_vehicles.csv` lists Alpha at $16.2M with a published $15M-$17.6M range. The guide price is 17.3% above the midpoint and 8.0% above the high endpoint. Both sources describe dedicated commercial launch service; the guide does not state a price effective date and may predate a later upstream observation. **rc-322 remains open** for price-date reconciliation. Extracted: `extracted_data/r412_firefly_alpha_guide_price.csv`.

## R413 - NASA Dragonfly Falcon Heavy award comparator (2026-11-09)

NASA Contract Release C24-042, paragraph 2 (25 November 2024), says the Dragonfly firm-fixed-price contract is approximately $256.6M, “which includes launch services and other mission related costs,” for a mission assigned to Falcon Heavy. At `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9`, `reference/launch_vehicles.csv` lists Falcon Heavy (expendable) at $163M with a $150M-$178M band; its row note identifies the high end as NASA’s Europa Clipper full-service price. The Dragonfly award total is 44.2% above that high and 57.4% above the midpoint, but the NASA release does not separate launch service from other mission-related costs or specify the Falcon Heavy configuration. Its 2024 award date also differs from the upstream 2026 reference year. This is a review signal, not a replacement value. **rc-323 remains open** for scope, configuration and year reconciliation. Extracted: `extracted_data/r413_nasa_dragonfly_falcon_heavy_award.csv`.


## R418 - NASA ESCAPADE New Glenn launch contract comparator (2026-11-09)

GeekWire reports NASA's VADR task order for Blue Origin to provide New Glenn launch service for the two ESCAPADE spacecraft had a total contract value of $20 million, with $6 million obligated at the time (2023-02-09 article, lines 8-20). NASA's ESCAPADE mission page lists the flight as Nov. 13, 2025, on Blue Origin New Glenn 2. At spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9, `reference/launch_vehicles.csv` lists New Glenn at $68M-$110M (2026, reported). The $20M award is 70.6% below the range's low end. It is an early, mission-specific VADR award made while the vehicle was in development, so it does not establish a current commercial rate.

Open `rc-328` to determine whether the reported range should include or explicitly distinguish this early-flight contract, and reconcile award date, risk discount and current commercial pricing before any change. No upstream value is changed. Extracted: `extracted_data/r418_escapade_new_glenn_price_comparator.csv`.

## R442 — NSSL Lane 1 Falcon 9 task-order average versus published list row (2026-11-09)

`ssc_2026_sbst_falcon9_lane1_task_orders` — Space Systems Command’s July 29, 2026 announcement says two NSSL Phase 3 Lane 1 task orders total $1.6 billion and assure 18 Falcon 9 launches from Vandenberg through the end of 2027. Dividing the rounded aggregate by 18 gives an approximate $88.9 million per covered launch. The reusable Falcon 9 row at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9` is $74 million, so the implied average is about 20.1% higher. SSC does not publish per-launch allocations, task-order values, or the services included in the aggregate. This is a government mission-service scope review signal, not a replacement for the commercial list price. Open `rc-338` to reconcile scope and price basis. Extracted: `extracted_data/r442_ssc_falcon9_nssl_lane1_price_comparator.csv`.


## R443 — NASA NEO Surveyor Falcon 9 award comparator (2026-11-09)

`nasa_2025_neo_surveyor_falcon9_launch_award` — NASA Contract Release C25-005 (Feb. 21, 2025), paragraph 3, reports a firm-fixed-price NLS II task order with an approximate total cost of $100 million for NEO Surveyor launch service on Falcon 9 from Florida, targeted no earlier than September 2027. NASA says the total includes “other mission related costs.” The Falcon 9 (reusable) row at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9` lists $74 million as its 2026 published price; the NASA award total is 35.1% higher. It is a scope-sensitive government award, not an isolated vehicle price. Together with the separate NSSL Lane 1 total in R442, it adds another check for `rc-338` while leaving the commercial list price unresolved. Extracted: `extracted_data/r443_nasa_neo_surveyor_falcon9_award.csv`.

## R444 — Starship Flight 14 updates projected-vehicle status note (2026-11-09)

`spacex_starship_flight_14_postflight_2026` — SpaceX’s post-flight page dates Flight 14 to September 28, 2026, calls it the first orbital Starship flight, and says it delivered 26 Starlink V3 satellites to orbit. The upstream `Starship (projected)` row at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9` still says “13 test flights to Jul 2026, 8 successful, all suborbital by design.” Flight 14 makes that flight-count and all-suborbital status note stale. It does not establish an operational service, a revised payload rating, or a launch price; keep the development status and price/payload projections unchanged pending separate evidence. Open `rc-339` to update the dated flight-status note. Extracted: `extracted_data/r444_starship_flight_14_update.csv`.

## R445 — Neutron inaugural launch schedule update (2026-11-09)

`rocket_lab_neutron_schedule_oct2026` — Rocket Lab’s October 14, 2026 SEC-filed release says Neutron’s inaugural launch “is now expected to occur in 2027” (paragraph 1). The upstream `Neutron` row at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9` still says “First flight has slipped from 2024 to NET Q4 2026.” The 2027 guidance supersedes that near-term schedule note, but remains a company expectation rather than a guarantee; no quarter is specified. Keep the development status, payload, and price estimates unchanged. Open `rc-340` to update the expected launch schedule. Extracted: `extracted_data/r445_rocket_lab_neutron_schedule.csv`.

## R446 — Current Firefly Alpha guide omits price signal (2026-11-09)

`firefly_alpha_payload_users_guide_v5p3_sep2026` — Firefly’s official Alpha Payload User’s Guide v5.3 revision history (PDF p. 2) dates the release to September 2026. Table 1 (PDF p. 4) lists 1,030 kg to 300 km LEO and 630 kg to 500 km SSO, matching the existing Alpha row’s payload point values. The 38-page guide contains no price entry; its Alpha section says the vehicle is for dedicated commercial launch service but does not state a price. This newer guide does not negate v5.2’s $19M price statement; it establishes only that v5.3 provides no newer price confirmation. `rc-322` remains open to reconcile the price date and basis. Extracted: `extracted_data/r446_firefly_alpha_guide_v5p3.csv`.

## R447 — Firefly Alpha launch-count cutoff and success terminology (2026-11-09)

`firefly_2025_10k_alpha_launch_history` — Firefly’s FY2025 Form 10-K says Alpha “has conducted seven launches” and describes “five launches completed successfully” (Item 1, Business, pp. 1–2). The filing also presents the seven-launch count as of December 31, 2025. `firefly_alpha_flta007_mission_page` — Firefly’s official Flight 7 page dates that mission to March 11, 2026. The upstream Alpha note at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9` dates seven flights to March 2026 and distinguishes three successes, two partial failures, and two failures. The filing’s year-end count conflicts with its own numbered Flight 7 date, and its unqualified five-success wording is not directly comparable to the upstream full/partial outcome categories. Open `rc-341` to reconcile the date cutoff and success definition; no outcome count is changed on this evidence alone. Extracted: `extracted_data/r447_firefly_alpha_launch_history.csv`.

## R448 — NASA selects Starship for cislunar communications demonstration (2026-11-09)

`nasa_2026_starship_cislunar_comms_selection` — NASA’s Nov. 7, 2026 release says it selected SpaceX under an existing lunar-logistics contract to launch communications satellites aboard Starship to cislunar space in 2028 (paragraph 300). This is a new mission selection and planned use; it does not establish operational service, a revised payload rating, or a launch price. The Starship projected-row notes at `spacecost@19e1a31ae280301c6fd5c3a7b57b73f44122e1d9` already need the Flight 14 status update in open `rc-339`; add this NASA selection to the dated note while keeping status and price/payload projections unchanged. Extracted: `extracted_data/r448_nasa_starship_cislunar_comms_selection.csv`.

## R449 — Arrow-led Falcon 9 and orbital-transfer award comparator (2026-11-09)

`quantum_space_nasa_moonbase_falcon9_vadr_award_2026` — Quantum Space’s Nov. 7 release reports a $185 million NASA Moon Base Transportation award to an Arrow-led team. Arrow is prime and mission integrator; the team includes SpaceX Falcon 9 for launch and Quantum Space’s Ranger for orbital transfer of two CAPSTONE-2 spacecraft. Quantum says its expected portion is approximately 25% of total contract value, while subcontract terms were still being finalized. The award therefore adds an identified Falcon 9 mission-service comparator to `rc-338`, but its bundled OTV and integration scope and undisclosed launch allocation do not establish a Falcon 9 vehicle price. Extracted: `extracted_data/r449_quantum_space_falcon9_moonbase_award.csv`.

## R450 — Impulse Space VADR task-order service scope (2026-11-09)

`impulse_space_moonbase_vadr_task_orders_2026` — Impulse Space’s Nov. 7 announcement says NASA awarded it two firm-fixed-price VADR task orders for Moon Base missions scheduled to begin in 2028. One task order uses SpaceX Falcon 9 and may use Mira vehicles for cislunar delivery; the second uses Relativity Terran R, Impulse Helios, and its lander for cislunar payload delivery and a surface-delivery demonstration. The release gives no individual order values. This confirms another Falcon 9 integrated-service award structure relevant to `rc-338`, but supplies no isolated launch price. Extracted: `extracted_data/r450_impulse_space_moonbase_vadr_task_orders.csv`.


## R513 — H3 configuration cost-target relationship (2026-11-10)

`sacj_2026_h3_f6_prelaunch_cost_briefing` — In the June 8, 2026 H3 F6 prelaunch briefing transcript, JAXA H3 project manager Makoto Arita says the H3-22 target is about 20% above H3-30 and H3-24 is “6割くらい高い” (about 60% higher; transcript lines 76–83). The current H3-30 target in the upstream note is $33M at 2024 rates; applying the 1.6 relative-cost factor gives a derived comparator of about $52.8M, not an independently quoted H3-24 price. Spacecost’s `H3 (24L)` row stores an estimated $50M–$75M band and $61.2M center, so the comparator falls inside the band and about 13.7% below its center. The briefing supports calibration of the estimate, while its target-cost basis does not establish a flight-service selling price or require a replacement. Open **rc-379** to review the band and target-to-price distinction. Extracted: `extracted_data/r513_h3_configuration_cost_targets.csv`.


## R544 — Green Launch light-gas-gun roadmap and cost target (2026-11-10)

`greenlaunch_2025_phases_leo_roadmap` — Green Launch’s Phases page says Phase 3 will “Deliver 1 lb to Low Earth Orbit” and “Will be scaled up for larger 100 lb to 1000 lb payloads” (Phases 3, lines 24–27). The delivery sequence says the impulse-launched vehicle’s rocket motor burns for 100 seconds and delivers a cubesat to 300 km Earth orbit (Cubesat Orbital Delivery, lines 60–78). `greenlaunch_2026_nonrocket_launch_cost_target` — the company’s Apr. 14, 2026 blog says Green Launch “targets ~$220/kg ($100/lb)” and describes light-gas guns as requiring an upper stage (sections “Infrastructure vs. Per-Launch Cost Trade-Off” and “The Orbital Velocity Gap,” lines 124–137); it gives no cost model or configuration-specific payload-price pairing. Spacecost main stores 30 kg payload and $300,000 as the price target for “Light-gas gun (orbital),” implying $10,000/kg. The public roadmap and cost target are material comparators, but their relation to the row’s mass, system boundary, and target price is unresolved. Open **rc-409** for reconciliation; no replacement is inferred. Extracted: `extracted_data/r544_green_launch_light_gas_gun_roadmap_cost.csv`.


## R549 — Jielong-3 reported unit launch-cost target (2026-11-10)

`xinhuanet_2021_jielong3_unit_launch_cost` — Xinhua’s March 3, 2021 report attributes to chief designer Jiang Jie the statement that Jielong-3 could reduce unit payload launch cost to “1万美元每公斤” ($10,000/kg), and gives 1.5 t to 500 km sun-synchronous orbit (paragraph 6). Multiplying the two produces a roughly $15M per-flight cost comparator, not a quoted selling price. The upstream 2026 Jielong-3 row stores $14.1M as an estimate and 1.6 t as its LEO figure; its price basis, year, and orbit scope are not established as like-for-like with the 2021 statement. Open **rc-415** to review the estimate and sourcing; no replacement is inferred. Extracted: `extracted_data/r549_xinhuanet_jielong3_cost.csv`.

## R571 — Spacecost fairing fill-ratio transfer (2026-11-10)

`spacecost_fairing_fill_ratio_working_tree_2026`: `spacecost/spacecost/fairings.py` computes usable-envelope/outer-cylinder ratios for ten guide-drawn fairings and takes their median, 0.482 (range 0.27–0.63). `_build` applies that factor to the outer cylinder for Angara A5, H3 (24L), H3 (30), Long March 2D, Long March 5, and Long March 10B because only outer dimensions are listed for those rows. The exported values are 127, 168, 107, 29.7, 126, and 128 m³, each marked `estimate`. Verdict: the code documents how the estimates are calculated, but the calibration sample does not itself establish transferability to these six fairing designs; review usable-envelope evidence or validate the cross-vehicle estimate and its uncertainty. No replacement values inferred. **rc-436**. Extracted: `extracted_data/r571_spacecost_fairing_fill_ratio.csv`.
## R595 — JAXA H3 light-configuration target price

- **jaxa_h3_launch_vehicle**: JAXA’s official English H3 project page states, “Our target price is about 5 billion yen for a light configuration with no solid rocket booster.” This supports the ¥5B target associated with the H3 no-booster configuration in `launch_vehicles.csv`; it does not state a contracted launch-service price. The H3 target is source-supported; no revision candidate was opened. `extracted_data/r595_jaxa_h3_target_price.csv`.
## R611 — Long March 7 price estimate lacks a cited price basis (2026-11-11)

spacecost_lm7_launch_price_code_current_2026: spacecost stores Long March 7 at $59.2M with a $50M–$70M range, price_basis=estimate, and a derived $4,385/kg to LEO. Its note says “price estimated” but names no price source or method. The registered China Daily sources citing CALT and the Long March 7 article support payload and variant provenance recorded under rc-213; they do not supply the stored price basis. Verdict: request the price source/calculation and define year and service scope, or identify the amounts as scenario estimates. Keep current values pending a comparable basis; no replacement inferred. rc-474. Extracted: extracted_data/r611_long_march_7_price_basis.csv.
## R612 — Pallas-1 launch-price estimate has no stated price basis (2026-11-11)

spacecost_pallas1_price_estimate_code_current_2026: the Pallas-1 row stores $28.3M with a $20M–$40M range and price_basis=estimate; its note says “Price estimated” but gives no source or calculation. galactic_energy_pallas1_first_flight_release_2026 (lines 59–62, 84–91) reports 5–7 t LEO capacity, a design reuse life of at least 25 flights, and a phased recovery-validation path toward commercial high-frequency reuse; it states no absolute launch price. beijing_e_town_pallas1_reuse_cost_share_2026 (line 24) quotes company chairman Liu Jianshe that recovery accounts for two-thirds of total cost and 50 recoveries are a target, but gives no absolute price. These sources bound vehicle and cost-structure context, not the estimate or service-price boundary. Verdict: request a documented price basis and reuse/configuration scope, or label as a scenario estimate; no replacement inferred. rc-475. Extracted: extracted_data/r612_pallas1_launch_price_basis.csv.
## R613 — Long March 2C price estimate inherits an unresolved Long March 2D anchor (2026-11-11)

spacecost_lm2c_price_proxy_code_current_2026: the Long March 2C row stores $29.6M with a $25M–$35M range and price_basis=estimate; its note says the estimate is against Long March 2D at $30M, but gives no 2C-specific calculation or range basis. The Long March 2D $30M anchor remains under open rc-315 review. Changguang Satellite’s SSE inquiry reply reports RMB 81.0M–85.9M in customer batch rocket fees for 2020–2022, while Wu (2025, p. 50) reports RMB 112.9M for a 2022 Long March 2D rocket plus monitoring/control service; neither is a like-for-like 2C price. Verdict: document the proxy and range basis or label them as an analogy-based scenario; retain current values pending comparable evidence. No replacement inferred. rc-476. Extracted: extracted_data/r613_lm2c_price_proxy_basis.csv.

## R614 — Epsilon S price estimate and predecessor comparison (2026-11-11)

spacecost_epsilon_s_price_estimate_code_current_2026: the Epsilon S row stores $30.8M [25M,38M], price_basis=estimate and reference_year=2026; its note says the $38M ceiling is the original Epsilon price, but supplies no source or method for the Epsilon S estimate or range. newspace_im_epsilon_s_price_chart_2024 (lines 0–12) plots IHI Epsilon S at about 600 kg and $25M; the chart does not specify contract status, price year, configuration or service scope. faa_ast_2016_compendium_epsilon_price (PDF fact sheet, lines 3677–3739) identifies the predecessor Epsilon and reports an estimated $39M per launch and 700–1,200 kg LEO capacity. The 2016 predecessor estimate is historical and distinct from Epsilon S; it does not validate the present $30.8M center or establish comparable price boundaries. Verdict: request the source and derivation for the Epsilon S point and range, including the derivation, configuration, meaning of the 2026 reference year, and vehicle-cost versus launch-service scope; retain current values pending comparable evidence. No replacement inferred. rc-477. Extracted: extracted_data/r614_epsilon_s_price_basis.csv.

## R615 — Ariane 5 ECA price field and cost boundary (2026-11-11)

spacecost_ariane5_eca_price_estimate_code_current_2026: spacecost stores Ariane 5 ECA at $191M [$165M,$220M], price_basis=estimate, reference_year=2026; the note says the band brackets €150–190M vehicle cost and that two GTO satellites commonly shared a launch, lowering per-customer price. esa_2003_ariane5_service_cost_atv_price (ESA INFO 10-2003, lines 211–225) distinguishes the Ariane 5 ECA qualification configuration from the Ariane 5 ES used for the first ATV and reports a €170M ES launch-service cost versus €129M paid by the Space Station Programme for the ATV launch (2003 economic conditions). These figures are historical, refer to ES/service-price bases, and do not establish the current ECA band or vehicle-production cost. Verdict: clarify whether the 2026 USD field represents vehicle cost or a commercial launch-service/list price, and document the source, configuration, conversion and inflation basis for the band; keep current values pending like-for-like evidence. No replacement inferred. rc-478. Extracted: extracted_data/r615_ariane5_price_scope.csv.

## R616 — Long March 9 price guess needs a scenario basis (2026-11-11)

spacecost_lm9_price_guess_code_current_2026: spacecost stores Long March 9 at $707M [$500M,$1,000M], price_basis=estimate, reference_year=2026. The row note attributes its capability/architecture context to CASC roadmap presentations, calls the price “a guess,” says so explicitly, and explains that the vehicle is included as an announced non-Starship vehicle in the Starship class. The note gives no derivation for the band or point and the vehicle’s first flight is planned for 2033. Verdict: retain this only as an explicitly scenario-level assumption with a documented derivation and sensitivity range; do not present it as a market quote or current commercial price. No replacement inferred. rc-479. Extracted: extracted_data/r616_lm9_price_guess_basis.csv.


## R623 — StarTram Gen-1 projected cost basis (2026-11-11)

- **powell_maise_rather_2010_startram_gen1_cost**: Powell, Maise & Rather’s SPESIF-2010 paper states the Gen-1 cost per kg depends on facility construction and amortization, annual payload throughput, and operating cost/payload per launch, and assumes a 10-year amortization (p. 9). Table 5.3 specifies a 35-ton payload, 30 g and 10 launches/day (p. 8). Table 5.4 gives “Total cost/kg of payload” as $43/kg for 35-ton launches at 10/day, with $19.25B projected construction and $0.52M amortized capital per launch (p. 10). The abstract calls $43/kg projected. Spacecost’s StarTram row stores $40/kg and $1.6M for a 40,000-kg LEO payload, labels the price as a 2026 target, and identifies no study. The study supports a close but not identical proponent-model estimate; it does not establish the row’s exact price year, payload basis, or an observed commercial price. Verdict: cite and scope the scenario estimate; no replacement inferred. **rc-486**. Extracted: `extracted_data/r623_startram_gen1_cost_basis.csv`.


## R624 — Long March 10B price-estimate basis (2026-11-11)

- **spacecost_lm10b_launch_price_code_current_2026**: Spacecost’s pinned Long March 10B row stores a $52.9M point, a $40M–$70M band, and a derived $3,306/kg [$2,500,$4,375], with `price_basis=estimate` and `reference_year=2026`; its only price explanation is “Price estimated.” **xinhuanet_2026_lm10b_reuse_launch_context**: Xinhua reports a 16 t LEO reusable commercial vehicle and says reuse can substantially reduce launch cost (10 Jul 2026, lines 35–38), without an absolute price. Verdict: the public first-flight source does not substantiate the stored price or range; request the calculation and scope, or document these as scenario estimates. No replacement inferred. **rc-487**. Extracted: `extracted_data/r624_long_march_10b_price_basis.csv`.


## R625 — Long March 10 development-price estimate (2026-11-11)

- **spacecost_lm10_launch_price_code_current_2026**: Spacecost’s Long March 10 row stores a $212M point and $150M–$300M band ($3,029/kg [$2,143,$4,286] to LEO), marks the vehicle in development and the price as an estimate, and says only “price estimated.” Its noted CASC disclosures and the registered SCIO payload source support 70 t LEO / 27 t lunar-transfer capability; they do not provide the price or its derivation. The current row also states the three-core vehicle has not flown. Verdict: request the estimate method and cost boundary, or document it as a scenario estimate for the development configuration; no replacement inferred. **rc-488**. Extracted: `extracted_data/r625_long_march_10_price_basis.csv`.


## R637 — Long March 6A price estimate lacks a stated basis (2026-11-11)

- **spacecost_lm6a_price_estimate_code_current_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, `reference/launch_vehicles.csv` stores $45.8M [$35M,$60M], `price_basis=estimate`, and `reference_year=2026`; the note says “Price estimated” without naming a source or method. With the stored 8,000 kg LEO payload, the derived headline rate is $5,725/kg. The geometric center of the endpoints reproduces $45.8M, but does not establish the endpoints.
- **spacenexus_lm6a_price_status_2026**: the profile lists launch price as “Not published” (Launch price field); its FAQ states SAST/CASC “has not published a list price” (How much does a Long March 6A launch cost?). The source gives no alternative price or cost boundary. The registered CASC product page supplies capability context only; it does not substantiate this estimate.
- Verdict: provide a source or calculation for both endpoints and define the dollar year and price boundary; otherwise retain the values only as an explicit scenario with sensitivity. No replacement inferred. **rc-499**. Extracted: `extracted_data/r637_lm6a_price_basis.csv`.


## R638 — Vulcan VC6 price basis and first-configuration schedule (2026-11-11)

- **spacecost_vulcan_vc6_current_record_2026**: at `spacecost@aaed2720ee44610c5cf90fc204db160deb5669bb`, the VC6 row stores $128M [$110M,$150M], `price_basis=estimate`, and `reference_year=2026`. Its note attributes $110M to ULA’s starting price for the smallest configuration and says six GEM 63XL boosters “are not free”; it calls $150M an estimate without giving a calculation. Reuters reports a generic Vulcan starting price of “roughly $110 million” (10 Jan 2024, paragraph 13) and says the vehicle can use up to six solid rocket motors (paragraph 14); it gives neither a VC6-specific price nor a six-booster adder. ULA’s guide defines VC6 as the six-SRB configuration (printed pp. 1–4). Existing rc-321 concerns VC4 and NSSL mission-service prices, not the VC6 vehicle-price basis. Verdict: document a VC6-specific band derivation and 2026 price boundary or label it as an explicit scenario; no replacement inferred. **rc-500**. Extracted: `extracted_data/r638_vc6_price_basis.csv`.
- **spacecost_vulcan_vc6_current_record_2026**: the same row says the first VC6 is manifested for October 2026. ULA’s 10 Nov 2026 blog post says the first Vulcan Leo 1 is planned for 13 Nov (lines 10–11) and identifies V-012 as VC6L with six SRBs and a LEO-optimized Centaur V (line 25); the current mission page gives the same date and variant (lines 45, 60). As of 11 Nov, it remains scheduled, not flown. Verdict: update the stale manifest date and retain scheduled status pending outcome. **rc-501**. Extracted: `extracted_data/r638_vc6_manifest_schedule.csv`.

## R685 — Tianlong-3 launch-price estimate has no derivation (rc-543) (2026-11-12)

- **spacecost_tianlong3_price_code_current_2026**: the Tianlong-3 row stores $33.5 million [$25 million, $45 million], price_basis=estimate, reference_year=2026; its note says “price estimated” without a source or calculation.
- **space_pioneer_tianlong3_product_page_current_2026**: the official TL-3 specification lists “17~22（t）” LEO and “10~17（t）” SSO capacity, but no launch price (payload fields). **carrier_space_tianlong3_price_request_current_2026** lists “Price on request” (Price section), with no amount.
- **Verdict**: neither page supports the stored numeric range or its center. Request a traceable basis and define configuration, service scope, and price year; otherwise state that the band is a scenario estimate. No replacement inferred. Distinct from rc-217, which addressed flight chronology and left the price cells unchanged. Extracted: `extracted_data/r685_tianlong3_price_basis.csv`.
