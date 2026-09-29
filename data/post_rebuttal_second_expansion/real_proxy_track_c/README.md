# Real Proxy Track C

This folder contains the broad real-data proxy and stability panel added during the rebuttal stage.

## Files

- `track_c_raw.csv`: method-level proxy metrics, method configuration JSON, status fields, and any error fields.
- `track_c_summary.csv`: compact method-level proxy summary.

## Scope

- Datasets: `ch4`, `gpcc_precip`, `ndvi`, `qbo`, `sea_ice_arctic`, `sunspots`
- Methods: `ceemdan`, `mstl`, `ssa`, `stl`, `vmd`, `wavelet`
- Rows: 36 method-dataset combinations
- Expected bands: `annual`, `annual_semiannual`, `qbo`, `solar`

## Metrics

The panel uses proxy diagnostics because exact real-world trend, seasonal, and residual components are unavailable. The columns cover:

- band plausibility and peak-hit checks;
- resampling stability for trend and seasonality;
- spectral and max-lag seasonal agreement under resampling;
- temporal spectrum overlap and drift diagnostics.

These results should be interpreted as plausibility and robustness evidence on real observational series, not as exact component-recovery labels.
