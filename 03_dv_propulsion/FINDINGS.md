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

