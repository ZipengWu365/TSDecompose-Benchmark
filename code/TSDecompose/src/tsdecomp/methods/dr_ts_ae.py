import numpy as np
from typing import Any, Dict

from ..core import DecompResult
from ..registry import MethodRegistry

try:
    from synthetic_ts_bench.dr_ts_ae import dr_ts_ae_decompose
    _HAS_DR_TS_AE = True
except ImportError as exc:  # pragma: no cover - optional dependency path
    dr_ts_ae_decompose = None
    _HAS_DR_TS_AE = False
    _IMPORT_ERROR = exc


@MethodRegistry.register("DR_TS_AE")
def dr_ts_ae_wrapper(
    y: np.ndarray,
    params: Dict[str, Any],
) -> DecompResult:
    if not _HAS_DR_TS_AE:
        raise ImportError(
            "synthetic_ts_bench is required for DR_TS_AE decomposition."
        ) from _IMPORT_ERROR

    cfg = dict(params or {})
    meta = {}
    if "primary_period" in cfg:
        meta["primary_period"] = cfg["primary_period"]

    res = dr_ts_ae_decompose(
        np.asarray(y, dtype=float).ravel(),
        config=cfg,
        fs=float(cfg.get("fs", 1.0)),
        meta=meta or None,
    )
    meta_out = dict(getattr(res, "extra", {}) or {})
    meta_out.setdefault("method", "DR_TS_AE")
    return DecompResult(
        trend=np.asarray(res.trend, dtype=float),
        season=np.asarray(res.season, dtype=float),
        residual=np.asarray(res.residual, dtype=float),
        meta=meta_out,
    )
