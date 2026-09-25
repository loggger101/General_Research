# Domain 9 — In-space delivery mass fractions & EDL survival (R54)

**Scope.** `spacecost/delivery.py` prices every in-space destination from a small set of structural constants. Most are derived from the reference tables, but three are *typed* because no table carries them: the tug/lander dry-mass fractions and — most load-bearing — **`MARS_LANDED_MASS_FRACTION = 0.30`**, the fraction of Mars-entry mass that survives as useful surface payload. The code comment labels it explicitly *"Measured, not assumed"* from MSL + Perseverance, yet no source was registered in General_Research for those two measurements. That is this round's domain-9 gap (criterion #1). This constant sets the **published mars_surface delivered price** — every kilogram of material landed on Mars is priced off it.

**Anchor 1 — JPL/NASA AIAA SciTech 2022, Edquist et al. (NTRS 20210024709)** [T2 hosted]. Table 3 gives the entry-interface mass of both sky-crane missions in one row: *MSL BET = 3153 kg; Mars-2020 TPS design cases = 3436/3436 kg; Mars-2020 BET = 3369 kg* (word-coordinate extracted from p14 of the hosted PDF). Caption verbatim: “Table 3.”.

**Anchor 2 — NASA AIAA SciTech 2022, Mars 2020 EDL flight-mech simulation (NTRS 20210024480)** [T2 hosted]. p1 states verbatim: *“At 1026 kg, Perseverance is the largest, most sophisticated rover ever delivered to another planet.”* — the landed (numerator) mass for Mars-2020.

**Anchor 3 — JPL MSL fact sheet** [T3 live]. The Curiosity rover line reads *“899 kg in Earth gravity”* (page shows 1,982 lbs / 899 kg) — the landed mass for MSL. Pulled + parsed live this round.

**The audit (all deltas computed in code).**
- MSL landed fraction = 899/3153 = **28.51%**
- Perseverance BET landed fraction = 1026/3369 = **30.45%** (TPS design case /3436 = 29.86%)
- Institutional measured band = **[28.51%, 30.45%]**
- Our `MARS_LANDED_MASS_FRACTION` = 0.30 (30%) → **IN BAND — AGREE**: it sits at the optimistic edge, +5.22% above MSL and -1.49% below the best-case Mars value. The code's own rationale (*takes the better of the two and is generous to Mars*) is exactly what the institutional data shows — 0.30 ≈ Perseverance BET.

**Note-level discrepancy (revision candidate, constant unaffected).** delivery.py's *supporting* comment numbers are slightly off JPL's actuals: it cites MSL entry **3257 kg** where Edquist's BET is 3153 kg (**+3.30% high**), and Perseverance rover **1025 kg** vs the institutional 1026 kg (-0.097, negligible). The rounded inputs shift the *quoted* per-mission percentages (the note's 27.6%/29.8%) but not the chosen constant, which lands at ~30% either way. Recorded as a citation-precision revision candidate for spacecost; no value change.

**Scope boundary — what this does NOT anchor.** The other two typed constants in delivery.py are *engineering estimates by design*, not measurements: `TUG_DRY_MASS_FRAC = 0.10` (mid-range for a cryogenic upper stage, Centaur V ~0.08 / DCSS ~0.11) and `LANDER_DRY_MASS_FRAC = 0.20` (cites Apollo LM descent-stage dry/prop ≈ 0.21). delivery.py itself documents these as non-derivable modelling dials with no table row behind them, so there is no institutional *measured* value to register for them this round — an honest gap, not a missed anchor. **(R56 update: `TUG_DRY_MASS_FRAC = 0.10` is now anchored — SP-4029 p294 'Ground Ignition Weights' carries per-mission S-IVB dry weights for all eleven flights; see the d3 Round 56 block.) `MARS_LANDED_MASS_FRACTION` was the one constant claimed *measured*, and it now has three registered sources.

**What this closes.** The reachability-and-delivery value chain's softest *claimed-measured* number — the Mars landed-mass fraction that prices every kilogram delivered to the Martian surface — is now backed by two hosted public-domain NASA EDL papers + a live JPL fact sheet, with our constant verified inside their measured band. Criterion #1 domain-9 work; all three sources pulled and analyzed this round (criterion #2).

## R56 deepening — as-flown EDL TPS thicknesses + parachute numbers pulled (criterion #2, no new source IDs)

Re-scan of the two hosted Mars EDL papers for data beyond R54's entry-mass Table 3. Both carry exactly one more pricing-relevant fact each; both are recorded verbatim below and neither changes a registered number:

- **Edquist p3 (TPS material thicknesses, as-flown MSL = Mars 2020):** "MSL material thicknesses for PICA on the heatshield (1.25 inches), SLA-561V on the backshell (0.5 inches), and Acusil-II on the parachute cone (variable thicknesses) were unchanged for the Mars 2020 vehicle" — i.e. the heatshield/TPS mass that delivery.py's `edl` leg prices at $50k/kg per kg of TPS is a *thin* ablative layer over a rigid aeroshell (PICA forebody + SLA-561V backshell), which supports treating the row as material+manufacturing cost rather than structural.
- **Flight-mech p2 (as-flown parachute phase, Mars 2020):** "Parachute Deploy E+4:01 Peak inflation load: 34.2 kips Updated parachute load predication approach was accurate Deceleration: 5.3 Earth g’s Altitude: 12.2 km Mach at Peak Inflation: 1.76 Dynamic Pressure: 504 Pa Velocity: 433 m/s" — peak-inflation load/deceleration context for the separately-carried parachute mass in delivery.py's edl leg; no per-unit price exists anywhere reachable, so nothing is pinned here.

No registry change: both sources were registered and hosted in R54 (registry stays at 123 after item (b) of this round).
