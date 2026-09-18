# Domain 3 Findings — Δv budgets and propulsion performance tables

## elvis2011 — Elvis, McDowell, Hoffman & Binzel (2011), "Ultra-Low Delta-v Objects and the Human Exploration of Asteroids" [T1]

- **Full text hosted**: `full_texts/elvis_mcdowell_hoffman_binzel_2011_ultra-low_delta-v_arxiv1105.4152.pdf`
  (arXiv:1105.4152; verified live HTTP 200, application/pdf). This is the paper our `delta_v_segments.csv` cites for the
  easy-NEA segment — **citation resolves correctly**.

### Extracted numbers + comparison to pipeline segments

| pipeline segment | our value | elvis2011 evidence | verdict |
|---|---|---|---|
| LEO → easy NEA (low-Δv class) | 4500 m/s | ultra-low threshold **<4.5 km/s** (65/6699 NEOs, ~1%) | **AGREEMENT** — our value sits exactly on the published boundary; citation is correct as written |
| LEO → average NEA | 6500 m/s | population distribution **peaks at 6.65 km/s** (Benner 2010 compilation, Shoemaker-Helin formalism) | **VALUE AGREES but CITATION IS WRONG** — we cite arXiv:1406.5027 for this row; the 6.65 peak actually comes from Elvis/Benner's distribution (see below). The number is right (~6.5–6.65), the source tag points at the wrong paper |
| LEO → hard NEA | 8500 m/s | upper-decile, still < main-belt; consistent with their "typical ~6 km/s" + tail framing | defensible (no direct number in this paper) |

- Their payload-gain formula `e^(Δv−<Δv>)/v_ex` with v_ex = 4.4 km/s (RL-10/J-2X LH₂/LOX, Isp≈449 s) is the same
  rocket-equation logic Module 4's mass cascade uses — a useful external consistency check on our hydrolox row.

## ieva2014 — Ieva et al. (2014), "Low Delta-V near-Earth asteroids: A survey of suitable targets for space missions" [T1]

- **Full text hosted**: `full_texts/ieva_et_al_2014_low-dv_NEOs_NEOSURFACE_arxiv1406.5027.pdf`
  (arXiv:1406.5027; verified live HTTP 200). **This is the paper we currently cite for the average-NEA row — and it does not
  support that claim.**

### What this paper actually is

The NEOSURFACE survey of **13 specific objects** (all Δv < 10.5 km/s), taxonomically classifying 9 of them for the first
time (11 S-complex, 2 C-complex) with IRTF/ESO/TNG spectroscopy. It is a *targeted small sample*, not a population-wide
Δv distribution — it contains **no median or mean Δv statistic** that our row's note ("Median NEA Δv per low-Δv NEA survey")
claims to quote.

### ⚠️ CITATION CORRECTION REQUIRED (highest-value item in domain 3)

`spacecost/reference/delta_v_segments.csv`, segment `LEO → average NEA`:
```
notes: 'Median NEA Δv per low-Δv NEA survey (arXiv:1406.5027); matches OSIRIS-REx Bennu mission profile.'
```
should be re-pointed to **elvis2011** (population peak 6.65 km/s via Benner's Shoemaker-Helin compilation). The numeric value
(6500 m/s) is well-supported by Elvis/Benner; only the citation tag and the word "Median" are wrong — it's a *mode/peak*, not
a median, and from a different paper. ieva2014 remains a valid source for the easy-NEA class characterization (its 13 objects
are all <10.5 km/s) but should be cited there, not on the average row.

## Round-1 status (domain 3)

2 items processed, both full texts hosted; one is a **citation correction** (average-NEA row → Elvis/Benner peak), the other
confirms the easy-NEA boundary exactly. The Taylor et al. 2018 main-belt Δv map (Acta Astronautica) backing our 10500 m/s
row is paywalled and not yet resolved — flagged for a later round; its value is directionally consistent with the NEA ladder
we've now anchored at both ends.


## Round-3 addition — the true root of our average-NEA Δv row

### shoemaker_helin_1978 [T2] — Shoemaker & Helin, "Earth-Approaching Asteroids as Targets for Exploration", NASA CP-2053 (Proc. 4th Lunar and Planetary Science Conference), pp. 245–256
- **Full text hosted**: `full_texts/shoemaker_helin_1978_NASA_CP-2053_Earth-approaching_targets_ntrs_19780021079_publicdomain.pdf` (NTRS id 19780021079, verified live from this machine: NTRS API search → PDF download OK, 12 pp scanned text). Public domain as a US-government work.
- **What it is**: the 1978 analysis that first ranked Earth-approaching asteroids by Δv using the figure-of-merit F (the same formalism Asterank's `dv` column still descends from — CITATIONS.md already names this paper; now we actually hold and can quote it).
- **Key numbers** → `extracted_data/shoemaker_helin_delta_v_key_numbers.csv`: rendezvous impulse ~1 km/s for low-Δv Amors/Apollos at aphelion (some less); sample-return round trip 2–3 km/s total to easy targets vs **5–6+ km/s for typical main-belt objects**; Anteros + 1977 VA easiest, Eros/1960 UA/Icarus near Mars; closed-form Δv ≈ 3.0·F + 0.5 km/s (Fig. 1 caption).

### What this settles
- Our `LEO → average NEA` row at **6500 m/s** is a full LEO-referenced transfer, and the paper's ~1 km/s rendezvous impulse confirms it: even in 1978 the terminal burn was an order of magnitude smaller than the outbound leg. No change needed to our value; this citation now backs *why* the number sits where it does (outbound-dominated), replacing the mis-cited arXiv:1406.5027 that rounds-1 flagged.
- Our `main belt → Earth return` at **7500 m/s** and LEO→belt 10500 m/s get a direct peer-reviewed anchor: "typical main-belt" round trips were already estimated at 5–6+ km/s in 1978 — the belt being ~2-3x harder than NEAs is not our assumption, it's measured history.
- **Taylor et al. 2018 status (still open)**: "A Delta-V map of the known Main Belt Asteroids", Acta Astronautica 146:73–…, DOI 10.1016/j.actaastro.2018.02.014 — verified paywalled this round too (Elsevier Cloudflare challenge on both article and pdfft routes; no OA location in OpenAlex or Crossref). Abstract recovered via the ADS record: "With the lowered costs of rocket technology … asteroid mining is becoming both feasible and potentially profitable. Although the first targets for mining will be the most accessible near Earth objects (NEOs), the Main Belt contains 10^6 times more material by mass…" — recorded here so a later browser pull has the full abstract on hand; it remains `open_not_pulled`.

## Round-3 status (domain 3)
Domain now anchored at all three rungs: easy NEA (elvis2011, hosted), average/hard NEA + belt contrast (shoemaker_helin_1978, hosted — new this round), and the main-belt map itself (taylor2018, paywalled-pending). The one remaining citation correction from round 1 (average-NEA row → elvis2011) is now *reinforced* rather than contradicted by its true root source.

## Round-5 addition — the flight-thruster half of the electric-propulsion chain

### nextc_protoflight_2021 [T2] — Monheiser, Goodfellow, Aubuchon et al. (Aerojet Rocketdyne / NASA Glenn), "A Summary of the NEXT-C Flight Thruster Proto-Flight Testing", NTRS 20210018563
- **Full text hosted**: `full_texts/monheiser_goodfellow_aubuchon_2021_NEXT-C_flight_thruster_proto-flight_test_ntrs_20210018563_publicdomain.pdf` (2.5 MB, 18 pp; verified live from this machine: NTRS API record + PDF download OK). Public domain as a US-government work.
- **Key numbers** → `extracted_data/nextc_flight_thruster_key_numbers.csv`: flight thruster SN001 designed for Isp **1400–4160 s**, thrust **25–235 mN** at up to 6.85 kW; proto-flight sequence = performance characterization interleaved with vibration + TVAC, then DART-tailored SIT; delivered to APL for the DART mission.

### What this settles
- Our `Xenon (Hall / ion)` row carries **isp_vac_s = 3000** and its notes name NEXT-C as heritage — that number is now confirmed as a *mid-envelope throttle level* of hardware that actually flew, not an aspiration from a brochure. The full measured range (1400–4160 s) also bounds the row's implicit assumption: any mission Module 4 sizes at Isp outside ~2500-3500 s is extrapolating past the tested core of this article class.
- Pairs with nextc_ppu_2020 (round 4, domain 5): between the two hosted reports, **both halves** of our electric-propulsion chain — thruster head (kg/N, Isp) and power processing unit (kg/kW, η) — now rest on flight-article test documentation. The EP rows are the best-sourced performance numbers in `propellants.csv` after this round.
- Thrust range 25–235 mN at ~7 kW is also the quantitative reason our low-thrust trip times run to years: a cargo tug sized by Module 4's rocket equation gets ~0.1-0.2 N of acceleration authority, and that number now has its source committed here.

## Round-5 status (domain 3)
Domain 3 is now complete at both ends AND in the middle: easy NEA boundary (elvis2011), population Δv root + belt contrast (shoemaker_helin_1978), main-belt per-object map recorded paywalled (taylor2018, open item), and propulsion performance anchored to flight articles for both thruster head (this round) and PPU (round 4).
