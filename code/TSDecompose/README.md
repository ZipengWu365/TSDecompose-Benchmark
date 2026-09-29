# TSDecompose Source Snapshot

This folder contains the source snapshot shipped with the benchmark release.

It is intentionally included as repository source code rather than as a PyPI-style package release. The import name remains `tsdecomp` for compatibility with the benchmark scripts.

## Layout

```text
src/tsdecomp/
  Unified decomposition API, method registry, CLI, metrics, and leaderboard runner.

src/synthetic_ts_bench/
  Synthetic scenario generator and component-recovery utilities.

scripts/run_paper_benchmark.py
  One-command runner for the paper-aligned core benchmark.

requirements.txt
  Runtime dependencies for local execution.
```

## One-Command Paper Benchmark

Install dependencies from this folder, then run the paper core benchmark:

```bash
pip install -r requirements.txt
export PYTHONPATH="$PWD/src"
python scripts/run_paper_benchmark.py
```

The script pins imports to this source snapshot, so it is safe to use even if a
different `tsdecomp` package is installed elsewhere on the same machine.

Windows PowerShell:

```powershell
pip install -r requirements.txt
$env:PYTHONPATH = "$PWD\src"
python scripts/run_paper_benchmark.py
```

The default command runs the paper-aligned core synthetic benchmark:

- 6 scenarios;
- 50 deterministic generated draws per scenario;
- 300 generated synthetic series total;
- the camera-ready six-family Table 2 roster (`ma_baseline`, `stl`, `ssa`, `emd`, `vmd`, `wavelet`).

The raw result table is written to:

```text
artifacts/paper_core_benchmark/leaderboard.csv
```

In the dataset release, this same paper-core raw output is stored as
`data/paper_tables/paper_core_50draw_leaderboard.csv` after stable row sorting.
The manuscript Table 2 values are derived from
`data/paper_tables/paper_core_50draw_by_tier.csv` using the tier-balanced rule:
stationary columns average Tier 1 and Tier 2 means with equal weight, while
non-stationary columns use Tier 3 means. The by-tier file records
metric-specific valid-row counts because seasonal metrics are undefined for the
trend-only scenario.

Aggregated summaries are written under:

```text
artifacts/paper_core_benchmark/summary/
```

For a quick dependency and integration check:

```bash
python scripts/run_paper_benchmark.py --smoke
```

This smoke run keeps the same 6 paper scenarios but uses 1 draw per scenario
and the smaller `stl,wavelet` method subset.

## Optional Direct CLI

```bash
python -m tsdecomp validate --suite core --methods ma_baseline,stl,ssa,emd,vmd,wavelet
```

Windows PowerShell:

```powershell
python -m tsdecomp validate --suite core --methods ma_baseline,stl,ssa,emd,vmd,wavelet
```

Use the script entrypoint above for reproduction. The direct module CLI is
shown only for clean environments where no other editable `tsdecomp` install can
shadow this source tree.

The native extension binary from the development machine is not included. The release uses the pure-Python fallback path by default. To test a separately built native extension, set `TSDECOMP_ALLOW_EXTERNAL_NATIVE=1` before importing `tsdecomp`.
