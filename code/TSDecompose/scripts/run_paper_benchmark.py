#!/usr/bin/env python3
"""Run the paper-aligned TSDecompose core benchmark from the source snapshot.

Default run:
  6 scenarios x 50 generated draws = 300 synthetic series.
  Each series is evaluated by the six camera-ready Table 2 method families.

The row count in leaderboard.csv is larger because each generated series is
evaluated by every requested method.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


def load_local_tsdecomp() -> None:
    """Pin imports to this source snapshot, even if tsdecomp is installed."""
    package_dir = SRC / "tsdecomp"
    init_file = package_dir / "__init__.py"
    if not init_file.exists():
        raise FileNotFoundError(f"Cannot find local tsdecomp package at {package_dir}")

    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))

    for name in list(sys.modules):
        if name == "tsdecomp" or name.startswith("tsdecomp."):
            del sys.modules[name]

    spec = importlib.util.spec_from_file_location(
        "tsdecomp",
        init_file,
        submodule_search_locations=[str(package_dir)],
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load local tsdecomp package from {init_file}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["tsdecomp"] = module
    spec.loader.exec_module(module)


load_local_tsdecomp()

from tsdecomp.bench_config import SUITES, resolve_methods  # noqa: E402
from tsdecomp.leaderboard import run_leaderboard  # noqa: E402


PAPER_SUITE = "core"
PAPER_METHODS = "ma_baseline,stl,ssa,emd,vmd,wavelet"
PAPER_SEEDS = "0"
PAPER_N_SAMPLES = 50
PAPER_LENGTH = 512
PAPER_DT = 1.0
PAPER_OUT = ROOT / "artifacts" / "paper_core_benchmark"
SMOKE_OUT = ROOT / "artifacts" / "paper_core_smoke"
SMOKE_METHODS = "stl,wavelet"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "One-command runner for the ICML 2026 TSDecompose paper core "
            "benchmark."
        )
    )
    parser.add_argument(
        "--smoke",
        action="store_true",
        help=(
            "Run a fast integration check: 6 scenarios x 1 draw with STL and "
            "Wavelet."
        ),
    )
    parser.add_argument(
        "--methods",
        default=None,
        help=(
            "Comma-separated method list or preset. Defaults to the "
            "camera-ready six-method Table 2 set for the full paper run, "
            "or 'stl,wavelet' for --smoke."
        ),
    )
    parser.add_argument(
        "--seeds",
        default=PAPER_SEEDS,
        help="Seed list, for example '0', '0,1,2', or '0:5'. Default: 0.",
    )
    parser.add_argument(
        "--n-samples",
        type=int,
        default=None,
        help="Generated draws per scenario. Default: 50, or 1 with --smoke.",
    )
    parser.add_argument(
        "--length",
        type=int,
        default=PAPER_LENGTH,
        help="Series length. Default: 512.",
    )
    parser.add_argument(
        "--dt",
        type=float,
        default=PAPER_DT,
        help="Sampling interval. Default: 1.0.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=(
            "Output directory. Default: artifacts/paper_core_benchmark, or "
            "artifacts/paper_core_smoke with --smoke."
        ),
    )
    parser.add_argument(
        "--plots",
        action="store_true",
        help="Also export diagnostic heatmaps under the output directory.",
    )
    parser.add_argument(
        "--no-aggregate",
        action="store_true",
        help="Skip summary CSV aggregation. Raw leaderboard.csv is still written.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    methods = args.methods
    if methods is None:
        methods = SMOKE_METHODS if args.smoke else PAPER_METHODS

    n_samples = args.n_samples
    if n_samples is None:
        n_samples = 1 if args.smoke else PAPER_N_SAMPLES

    out_dir = args.out
    if out_dir is None:
        out_dir = SMOKE_OUT if args.smoke else PAPER_OUT

    method_list = resolve_methods(methods)
    scenario_count = len(SUITES[PAPER_SUITE])
    generated_series = scenario_count * n_samples
    result_rows = generated_series * len(method_list)

    print("TSDecompose paper core benchmark")
    print(f"  source: {SRC}")
    print(f"  suite: {PAPER_SUITE}")
    print(f"  scenarios: {scenario_count}")
    print(f"  draws per scenario: {n_samples}")
    print(f"  generated series: {generated_series}")
    print(f"  methods: {', '.join(method_list)}")
    print(f"  expected result rows per seed: {result_rows}")
    print(f"  length: {args.length}")
    print(f"  output: {out_dir}")

    df = run_leaderboard(
        suite=PAPER_SUITE,
        methods=methods,
        seeds=args.seeds,
        n_samples=n_samples,
        length=args.length,
        dt=args.dt,
        out_dir=out_dir,
        export_format="leaderboard_csv",
        aggregate=not args.no_aggregate,
        plots=args.plots,
    )

    errors = int((df["status"] == "error").sum()) if not df.empty else 0
    print("")
    print(f"Done. Rows written: {df.shape[0]}")
    print(f"Errored rows: {errors}")
    print(f"Raw leaderboard: {Path(out_dir) / 'leaderboard.csv'}")
    if not args.no_aggregate:
        print(f"Summaries: {Path(out_dir) / 'summary'}")


if __name__ == "__main__":
    main()
