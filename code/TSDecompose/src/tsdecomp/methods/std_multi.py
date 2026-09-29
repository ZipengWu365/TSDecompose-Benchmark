import numpy as np
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass
from ..core import DecompResult
from ..registry import MethodRegistry

@dataclass
class STDBasisCache:
    """
    Cache for STD bases.
    """
    bases: Dict[str, np.ndarray] # key -> basis matrix (L, K) or similar

    def fit(self, X_windows: np.ndarray):
        # Placeholder: fit bases from windows
        pass

    def project(self, window: np.ndarray) -> np.ndarray:
        # Placeholder: project window onto basis
        return window

    def save(self, path: str):
        np.savez(path, **self.bases)

    @staticmethod
    def load(path: str) -> "STDBasisCache":
        data = np.load(path)
        return STDBasisCache(bases={k: data[k] for k in data.files})

@MethodRegistry.register("STD_MULTI")
def std_multi_decompose(
    y: np.ndarray,
    params: Dict[str, Any],
) -> DecompResult:
    """
    Experimental placeholder for user-provided STD decomposition.

    The previous implementation silently fell back to SSA or returned a mock
    decomposition, which makes benchmark participation invalid. Fail closed so
    callers cannot mistake this for a supported baseline.
    """
    cfg = dict(params or {})
    raise NotImplementedError(
        "STD_MULTI is an experimental placeholder and is excluded from confirmatory "
        "benchmarking until a real implementation is provided. "
        f"Received params={cfg!r}"
    )

@MethodRegistry.register("STD_FULL_ABLATION")
def std_full_ablation_decompose(
    y: np.ndarray,
    params: Dict[str, Any],
) -> DecompResult:
    return std_multi_decompose(y, {**params, "mode": "STD_FULL_ABLATION"})
