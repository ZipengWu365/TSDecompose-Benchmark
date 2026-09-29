import argparse
import sys
import json
from pathlib import Path
import numpy as np
import pandas as pd
from typing import List, Dict, Any

from .core import DecompositionConfig
from .registry import decompose, MethodRegistry
from .io import read_series, save_result
from .viz import plot_components, plot_error
from .metrics import compute_metrics
from .metrics import compute_metrics
from .leaderboard import run_leaderboard, validate_runbook, merge_results
from .bench_config import resolve_methods

def cmd_merge_results(args):
    merge_results(
        input_dirs=args.inputs,
        out_dir=args.out,
        aggregate=args.aggregate,
        plots=args.plots
    )
    print(f"Done. Merged results saved to {args.out}")

def parse_params(param_list: List[str]) -> Dict[str, Any]:
    """
    Parse list of 'key=value' strings into a dict.
    Supports basic types (int, float, bool, json-list).
    """
    params = {}
    if not param_list:
        return params

    for item in param_list:
        if "=" not in item:
            continue
        key, val = item.split("=", 1)

        # Try JSON first (for lists/dicts)
        try:
            val_parsed = json.loads(val)
            params[key] = val_parsed
            continue
        except json.JSONDecodeError:
            pass

        # Try int/float/bool
        if val.lower() == "true":
            params[key] = True
        elif val.lower() == "false":
            params[key] = False
        else:
            try:
                if "." in val:
                    params[key] = float(val)
                else:
                    params[key] = int(val)
            except ValueError:
                params[key] = val
    return params

def cmd_run(args):
    series = read_series(args.series, args.col)
    params = parse_params(args.param)

    cfg = DecompositionConfig(
        method=args.method,
        params=params
    )

    print(f"Running {args.method} on {args.series}...")
    res = decompose(series, cfg)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    name = Path(args.series).stem
    save_result(res, out_dir, name)

    if args.plot:
        plot_components(res, series, save_path=out_dir / f"{name}_plot.png")
        plot_error(res, series, save_path=out_dir / f"{name}_error.png")

    print(f"Done. Results saved to {out_dir}")

def cmd_batch(args):
    import glob
    files = sorted(glob.glob(args.glob))
    if not files:
        print(f"No files found for glob: {args.glob}")
        return

    params = parse_params(args.param)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Found {len(files)} files. Processing...")

    for fpath in files:
        try:
            series = read_series(fpath)
            cfg = DecompositionConfig(method=args.method, params=params)
            res = decompose(series, cfg)
            name = Path(fpath).stem
            save_result(res, out_dir, name)
            if args.plot:
                plot_components(res, series, save_path=out_dir / f"{name}_plot.png")
        except Exception as e:
            print(f"Error processing {fpath}: {e}")

def cmd_eval(args):
    truth_dir = Path(args.truth_dir)
    pred_dir = Path(args.pred_dir)

    metrics_list = args.metrics.split(",")
    results = []

    pred_files = sorted(list(pred_dir.glob("*_components.csv")))

    for p_file in pred_files:
        name = p_file.stem.replace("_components", "")
        # Try to find matching truth file
        # Assuming truth file has same stem or similar convention
        # This is a heuristic matching
        t_file = truth_dir / f"{name}.csv"
        if not t_file.exists():
            # Try without extension or other patterns if needed
            continue

        try:
            y_pred_df = pd.read_csv(p_file)
            # Reconstruct signal from components or read residual?
            # Usually we compare components if ground truth has components.
            # Or we compare reconstruction to original if we just want R2 of fit.
            # But 'eval' usually implies we have ground truth components (trend, season).

            y_true_df = pd.read_csv(t_file)

            # Compare trend, season if available
            row = {"file": name}

            if "trend" in y_true_df.columns and "trend" in y_pred_df.columns:
                m = compute_metrics(y_true_df["trend"].values, y_pred_df["trend"].values)
                for k, v in m.items():
                    if k in metrics_list:
                        row[f"trend_{k}"] = v

            if "season" in y_true_df.columns and "season" in y_pred_df.columns:
                m = compute_metrics(y_true_df["season"].values, y_pred_df["season"].values)
                for k, v in m.items():
                    if k in metrics_list:
                        row[f"season_{k}"] = v

            results.append(row)

        except Exception as e:
            print(f"Error evaluating {name}: {e}")

    if results:
        df_res = pd.DataFrame(results)
        print(df_res)
        if args.out_csv:
            df_res.to_csv(args.out_csv, index=False)
    else:
        print("No matching files found or evaluation failed.")

def cmd_validate(args):
    validate_runbook(
        suite=args.suite,
        methods=resolve_methods(args.methods),
        length=args.length,
        dt=args.dt,
    )
    print("Validation passed.")


def cmd_run_leaderboard(args):
    run_leaderboard(
        suite=args.suite,
        methods=args.methods,
        seeds=args.seeds,
        n_samples=args.n_samples,
        length=args.length,
        dt=args.dt,
        out_dir=args.out,
        export_format=args.export,
        aggregate=args.aggregate,
        plots=args.plots,
    )
    print(f"Done. Artifacts saved to {args.out}")

def main():
    parser = argparse.ArgumentParser(description="tsdecomp CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # RUN
    p_run = subparsers.add_parser("run", help="Run decomposition on a single file")
    p_run.add_argument("--method", required=True, help="Decomposition method name")
    p_run.add_argument("--series", required=True, help="Path to input series (csv/parquet)")
    p_run.add_argument("--col", help="Column name if CSV has multiple columns")
    p_run.add_argument("--param", action="append", help="Method params as key=value")
    p_run.add_argument("--out_dir", required=True, help="Output directory")
    p_run.add_argument("--plot", action="store_true", help="Generate plots")
    p_run.set_defaults(func=cmd_run)

    # BATCH
    p_batch = subparsers.add_parser("batch", help="Run decomposition on a batch of files")
    p_batch.add_argument("--method", required=True)
    p_batch.add_argument("--glob", required=True, help="Glob pattern for input files")
    p_batch.add_argument("--param", action="append")
    p_batch.add_argument("--out_dir", required=True)
    p_batch.add_argument("--plot", action="store_true")
    p_batch.set_defaults(func=cmd_batch)

    # EVAL
    p_eval = subparsers.add_parser("eval", help="Evaluate decomposition results")
    p_eval.add_argument("--truth_dir", required=True)
    p_eval.add_argument("--pred_dir", required=True)
    p_eval.add_argument("--metrics", default="r2,dtw", help="Comma-separated metrics")
    p_eval.add_argument("--out_csv", help="Output CSV for metrics")
    p_eval.set_defaults(func=cmd_eval)

    # VALIDATE
    p_validate = subparsers.add_parser("validate", help="Validate benchmark config")
    p_validate.add_argument("--suite", default="core", help="Benchmark suite")
    p_validate.add_argument("--methods", default="core", help="Method list or preset")
    p_validate.add_argument("--length", type=int, default=512)
    p_validate.add_argument("--dt", type=float, default=1.0)
    p_validate.set_defaults(func=cmd_validate)

    # RUN LEADERBOARD
    p_leader = subparsers.add_parser("run_leaderboard", help="Run official leaderboard")
    p_leader.add_argument("--suite", default="core", help="Benchmark suite")
    p_leader.add_argument("--methods", default="core", help="Method list or preset")
    p_leader.add_argument("--seeds", default="0", help="Seed list (e.g., 0,1,2 or 0:5)")
    p_leader.add_argument("--n_samples", type=int, default=50, help="Samples per scenario")
    p_leader.add_argument("--length", type=int, default=512)
    p_leader.add_argument("--dt", type=float, default=1.0)
    p_leader.add_argument("--out", default="artifacts/tscomp_v1_core", help="Output directory")
    p_leader.add_argument("--export", default="leaderboard_csv", help="Export format")
    p_leader.add_argument("--aggregate", action="store_true", help="Aggregate summaries")
    p_leader.add_argument("--plots", action="store_true", help="Generate plots")
    p_leader.set_defaults(func=cmd_run_leaderboard)

    # MERGE RESULTS
    p_merge = subparsers.add_parser("merge_results", help="Merge multiple benchmark results")
    p_merge.add_argument("--inputs", nargs="+", required=True, help="Input directories")
    p_merge.add_argument("--out", required=True, help="Output directory")
    p_merge.add_argument("--aggregate", action="store_true", default=True, help="Aggregate summaries")
    p_merge.add_argument("--plots", action="store_true", default=True, help="Generate plots")
    p_merge.set_defaults(func=cmd_merge_results)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
