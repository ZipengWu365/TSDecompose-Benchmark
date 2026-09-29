from __future__ import annotations

from importlib import import_module, machinery, util
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, Iterator
import os
import site
import sys

_MODULE: ModuleType | None = None
_IMPORT_ERROR: Exception | None = None


def _candidate_paths() -> Iterator[Path]:
    pkg_dir = Path(__file__).resolve().parent
    suffixes = tuple(machinery.EXTENSION_SUFFIXES)

    for suffix in suffixes:
        name = f"_tsdecomp_native{suffix}"
        yield pkg_dir / name


def _external_candidate_paths() -> Iterator[Path]:
    suffixes = tuple(machinery.EXTENSION_SUFFIXES)
    site_roots = [Path(path) for path in site.getsitepackages()]
    user_site = site.getusersitepackages()
    if user_site:
        site_roots.append(Path(user_site))

    for suffix in suffixes:
        name = f"_tsdecomp_native{suffix}"
        for root in site_roots:
            yield root / "tsdecomp" / name
            yield root / name


def _load_from_path(path: Path) -> ModuleType:
    spec = util.spec_from_file_location("tsdecomp._tsdecomp_native", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create module spec for native extension at {path}")
    module = util.module_from_spec(spec)
    sys.modules["tsdecomp._tsdecomp_native"] = module
    spec.loader.exec_module(module)
    return module


_MODULE_NAMES = ["tsdecomp._tsdecomp_native"]
if os.environ.get("TSDECOMP_ALLOW_EXTERNAL_NATIVE") == "1":
    _MODULE_NAMES.append("_tsdecomp_native")

for _module_name in _MODULE_NAMES:
    try:
        _MODULE = import_module(_module_name)
        _IMPORT_ERROR = None
        break
    except Exception as exc:  # pragma: no cover - import error depends on env/build
        _IMPORT_ERROR = exc

if _MODULE is None:
    candidates = _candidate_paths()
    if os.environ.get("TSDECOMP_ALLOW_EXTERNAL_NATIVE") == "1":
        candidates = iter([*candidates, *_external_candidate_paths()])

    for _candidate in candidates:
        if not _candidate.exists():
            continue
        try:
            _MODULE = _load_from_path(_candidate)
            _IMPORT_ERROR = None
            break
        except Exception as exc:  # pragma: no cover - import error depends on env/build
            _IMPORT_ERROR = exc
            sys.modules.pop("tsdecomp._tsdecomp_native", None)


def native_extension_available() -> bool:
    return _MODULE is not None


def native_import_error() -> Exception | None:
    return _IMPORT_ERROR


def native_capabilities() -> Dict[str, bool]:
    if _MODULE is None:
        return {}
    if hasattr(_MODULE, "capabilities"):
        data = getattr(_MODULE, "capabilities")()
        if isinstance(data, dict):
            return {str(key): bool(val) for key, val in data.items()}
    return {
        name: hasattr(_MODULE, name)
        for name in (
            "ssa_decompose",
            "dr_ts_reg_decompose",
            "std_decompose",
            "gabor_stft_rfft",
            "gabor_istft_rfft",
            "gabor_cluster_decompose",
        )
    }


def has_native_method(name: str) -> bool:
    return _MODULE is not None and hasattr(_MODULE, name)


def invoke_native(name: str, *args: Any, **kwargs: Any) -> Any:
    if _MODULE is None:
        raise RuntimeError("Native extension is not available.") from _IMPORT_ERROR
    if not hasattr(_MODULE, name):
        raise AttributeError(f"Native extension does not export '{name}'.")
    return getattr(_MODULE, name)(*args, **kwargs)
