from typing import Dict

import numpy as np
from scipy.signal import welch

def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    R-squared score.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    if y_true.shape != y_pred.shape or y_true.size == 0:
        return float("nan")
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    if ss_tot <= 1e-12:
        return float("nan")
    return float(1 - (ss_res / ss_tot))

def dtw_distance(s1: np.ndarray, s2: np.ndarray) -> float:
    """
    Squared-cost Dynamic Time Warping distance with O(NM) dynamic programming.
    """
    x = np.asarray(s1, dtype=float).reshape(-1)
    y = np.asarray(s2, dtype=float).reshape(-1)
    n, m = x.size, y.size
    if n == 0 or m == 0:
        return float("nan")
    prev = np.full(m + 1, np.inf, dtype=float)
    curr = np.full(m + 1, np.inf, dtype=float)
    prev[0] = 0.0
    for i in range(1, n + 1):
        curr[0] = np.inf
        xi = x[i - 1]
        for j in range(1, m + 1):
            cost = (xi - y[j - 1]) ** 2
            curr[j] = cost + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev
    return float(np.sqrt(prev[m]))

def spectral_correlation(s1: np.ndarray, s2: np.ndarray, fs: float = 1.0) -> float:
    """
    Pearson correlation of normalized power spectral densities.
    """
    s1 = np.asarray(s1, dtype=float)
    s2 = np.asarray(s2, dtype=float)
    if s1.shape != s2.shape or s1.size < 2:
        return float("nan")
    f1, Pxx1 = welch(s1, fs=fs)
    f2, Pxx2 = welch(s2, fs=fs)
    if len(Pxx1) != len(Pxx2):
        min_len = min(len(Pxx1), len(Pxx2))
        Pxx1 = Pxx1[:min_len]
        Pxx2 = Pxx2[:min_len]
    Pxx1 = Pxx1 / (np.sum(Pxx1) + 1e-12)
    Pxx2 = Pxx2 / (np.sum(Pxx2) + 1e-12)
    corr = np.corrcoef(Pxx1, Pxx2)[0, 1]
    return float(corr) if np.isfinite(corr) else float("nan")

def _safe_corr(x: np.ndarray, y: np.ndarray) -> float:
    x_c = x - np.mean(x)
    y_c = y - np.mean(y)
    vx = np.mean(x_c**2)
    vy = np.mean(y_c**2)
    if vx <= 1e-12 or vy <= 1e-12:
        return float("nan")
    return float(np.mean(x_c * y_c) / np.sqrt(vx * vy))

def max_lag_correlation(s1: np.ndarray, s2: np.ndarray, max_lag: int = 10) -> float:
    """
    Maximum Pearson correlation over lags in [-max_lag, max_lag].
    """
    x = np.asarray(s1, dtype=float).reshape(-1)
    y = np.asarray(s2, dtype=float).reshape(-1)
    if x.shape != y.shape or x.size < 3:
        return float("nan")
    best = -np.inf
    for lag in range(-max_lag, max_lag + 1):
        if lag == 0:
            xc, yc = x, y
        elif lag > 0:
            xc, yc = x[lag:], y[:-lag]
        else:
            k = -lag
            xc, yc = x[:-k], y[k:]
        if xc.size < 3:
            continue
        val = _safe_corr(xc, yc)
        if np.isfinite(val) and val > best:
            best = val
    return float(best if best != -np.inf else np.nan)

def compute_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    fs: float = 1.0
) -> Dict[str, float]:
    return {
        "r2": r2_score(y_true, y_pred),
        "dtw": dtw_distance(y_true, y_pred),
        "spec_corr": spectral_correlation(y_true, y_pred, fs),
        "max_lag_corr": max_lag_correlation(y_true, y_pred)
    }
