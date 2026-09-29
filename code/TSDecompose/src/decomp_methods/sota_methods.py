"""Legacy SOTA-method wrappers used by synthetic_ts_bench.

The original synthetic benchmark imported these helpers from a top-level
``decomp_methods`` package. The Hugging Face source snapshot keeps that import
path as a shim and delegates to the bundled ``tsdecomp`` implementations.
"""

from __future__ import annotations

from typing import Any, Dict, Tuple

import numpy as np

from tsdecomp.core import DecompResult
from tsdecomp.methods.ceemdan import ceemdan_decompose
from tsdecomp.methods.stl import mstl_decompose, robuststl_decompose
from tsdecomp.methods.vmd import vmd_decompose


def _params(fs: float, config: Dict[str, Any], meta: Dict[str, Any]) -> Dict[str, Any]:
    params = dict(config or {})
    params.setdefault("fs", fs)
    for key in ("period", "periods", "primary_period"):
        if key in meta and key not in params:
            params[key] = meta[key]
    if "primary_period" not in params and "period" in params:
        params["primary_period"] = params["period"]
    return params


def _as_legacy_tuple(result: DecompResult) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    extra = dict(result.meta or {})
    if result.components:
        extra.setdefault("components", result.components)
    return (
        np.asarray(result.trend, dtype=float),
        np.asarray(result.season, dtype=float),
        np.asarray(result.residual, dtype=float),
        extra,
    )


def decompose_mstl_components(
    y: np.ndarray,
    fs: float,
    config: Dict[str, Any],
    meta: Dict[str, Any],
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    params = _params(fs, config, meta)
    if "periods" not in params and "period" in params:
        params["periods"] = [params["period"]]
    return _as_legacy_tuple(mstl_decompose(np.asarray(y, dtype=float), params))


def decompose_robuststl_components(
    y: np.ndarray,
    fs: float,
    config: Dict[str, Any],
    meta: Dict[str, Any],
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    params = _params(fs, config, meta)
    return _as_legacy_tuple(robuststl_decompose(np.asarray(y, dtype=float), params))


def decompose_ceemdan_components(
    y: np.ndarray,
    fs: float,
    config: Dict[str, Any],
    meta: Dict[str, Any],
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    params = _params(fs, config, meta)
    return _as_legacy_tuple(ceemdan_decompose(np.asarray(y, dtype=float), params))


def decompose_vmd_components(
    y: np.ndarray,
    fs: float,
    config: Dict[str, Any],
    meta: Dict[str, Any],
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    params = _params(fs, config, meta)
    return _as_legacy_tuple(vmd_decompose(np.asarray(y, dtype=float), params))
