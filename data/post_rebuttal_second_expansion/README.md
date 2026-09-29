# Post-Rebuttal Second Expansion

This directory contains the post-rebuttal second expansion of the real-data evidence for the ICML 2026 TSDecompose benchmark release.

The paper-aligned artifact remains:

- `data/paper_tables/`
- `data/synthetic_full22_extension/`
- `data/real_proxy22/`
- `data/semisynth_transfer/`

This directory is a later companion evidence bundle. It should be read as additional post-rebuttal support, not as a replacement for the paper-aligned benchmark tables.

## Contents

```text
real_physics_track_b/
  Mechanism-aware real-data recovery checks on CO2 and tides.

real_proxy_track_c/
  Broader proxy and stability checks on six real observational time series.

figures/
  Small summary figure generated from the rebuttal-stage real-data panel.
```

## Interpretation

The controlled synthetic benchmark remains the main exact component-recovery evidence because it provides known trend, seasonal, and residual components. Real time series usually do not expose exact decomposed ground truth, so the post-rebuttal expansion separates two evidence types:

- mechanism-aware real-data checks where the physical structure is relatively clear;
- proxy and stability checks where exact components are unavailable.

These files document that second evidence layer. They are intended for transparency and follow-up analysis rather than for redefining the main paper leaderboard.
