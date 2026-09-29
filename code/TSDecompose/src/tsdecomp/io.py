import pandas as pd
import numpy as np
from typing import Union, Dict, Any
from pathlib import Path
from .core import DecompResult

def read_series(path: Union[str, Path], col: str = None) -> np.ndarray:
    """
    Read time series from CSV or Parquet.
    """
    path = Path(path)
    if path.suffix == ".csv":
        df = pd.read_csv(path)
    elif path.suffix == ".parquet":
        df = pd.read_parquet(path)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")

    if col:
        return df[col].values
    else:
        # Try to find a numeric column or use the first one
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            return df[numeric_cols[0]].values
        else:
            return df.iloc[:, 0].values

def save_result(result: DecompResult, out_dir: Union[str, Path], name: str):
    """
    Save decomposition result to CSV/Parquet and metadata to JSON.
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save components
    data = {
        "trend": result.trend,
        "season": result.season,
        "residual": result.residual
    }
    for k, v in result.components.items():
        data[k] = v

    df = pd.DataFrame(data)
    df.to_csv(out_dir / f"{name}_components.csv", index=False)

    # Save meta
    import json
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.floating):
                return float(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return super(NumpyEncoder, self).default(obj)

    with open(out_dir / f"{name}_meta.json", "w") as f:
        json.dump(result.meta, f, indent=2, cls=NumpyEncoder)
