# Real Proxy 22-Method Track

This directory contains a real-data companion track for public time series.

Real data do not provide exact ground-truth trend and seasonal components, so these rows use proxy and stability metrics rather than exact component-recovery scores.

Included files:

- `data/raw/*.csv`: canonicalized small real-series CSV files;
- `configs/*.csv` and `configs/*.json`: dataset and method registries;
- `results/summary/*`: rankings, coverage, discovery notes, and proxy metrics.
