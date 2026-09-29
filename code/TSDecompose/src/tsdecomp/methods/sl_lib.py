import numpy as np
from typing import Any, Dict

from ..core import DecompResult
from ..registry import MethodRegistry

try:
    from synthetic_ts_bench.sl_lib import sl_lib_decompose
    _HAS_SL_LIB = True
except ImportError as exc:  # pragma: no cover - optional dependency path
    sl_lib_decompose = None
    _HAS_SL_LIB = False
    _IMPORT_ERROR = exc


@MethodRegistry.register("SL_LIB")
def sl_lib_wrapper(
    y: np.ndarray,
    params: Dict[str, Any],
) -> DecompResult:
    if not _HAS_SL_LIB:
        raise ImportError(
            "synthetic_ts_bench is required for SL_LIB decomposition."
        ) from _IMPORT_ERROR

    cfg = dict(params or {})
    res = sl_lib_decompose(
        np.asarray(y, dtype=float).ravel(),
        config=cfg,
        fs=float(cfg.get("fs", 1.0)),
        meta=None,
    )
    meta_out = dict(getattr(res, "extra", {}) or {})
    meta_out.setdefault("method", "SL_LIB")
    return DecompResult(
        trend=np.asarray(res.trend, dtype=float),
        season=np.asarray(res.season, dtype=float),
        residual=np.asarray(res.residual, dtype=float),
        meta=meta_out,
    )
