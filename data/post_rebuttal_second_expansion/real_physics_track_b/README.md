# Real Physics Track B

This folder contains the mechanism-aware real-data recovery checks added during the rebuttal stage.

## Files

- `track_b_raw.csv`: method-level raw metrics, method configuration JSON, status fields, and any error fields.
- `track_b_summary.csv`: compact method-level summary metrics.

## Scope

- Datasets: `co2`, `tides`
- Methods: `stl`, `mstl`, `robuststl`, `ssa`, `ceemdan`, `vmd`, `wavelet`, `ma_baseline`
- Rows: 16 method-dataset combinations

## Metrics

The CO2 checks include trend and seasonal recovery metrics such as `trend_r2`, `seasonal_r2`, quadratic trend-fit diagnostics, and seasonal-amplitude diagnostics.

The tides checks include target-frequency and harmonic-separation diagnostics such as `target_frequency_coverage`, `m2_s2_separation_success`, and `main_peak_frequency_error`.

These metrics use mechanism-informed approximate structure. They are stronger than purely proxy checks, but they are still real-data companion evidence rather than the controlled synthetic ground truth used by the primary benchmark.
