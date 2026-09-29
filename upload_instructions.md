# Hugging Face Upload Instructions

This bundle is prepared for a Hugging Face dataset repository.

Recommended repository id:

```text
Zipeng365/TSDecompose-Benchmark
```

Dry-run checks:

```powershell
hf auth whoami
Get-ChildItem -Recurse -File . | Measure-Object Length -Sum
```

Create the dataset repository when ready:

```powershell
hf repo create Zipeng365/TSDecompose-Benchmark --repo-type dataset --private --exist-ok
```

Upload the prepared bundle:

```powershell
hf upload Zipeng365/TSDecompose-Benchmark . --repo-type dataset --commit-message "Add ICML 2026 TSDecompose benchmark release"
```

After upload, check:

```powershell
hf download Zipeng365/TSDecompose-Benchmark README.md --repo-type dataset --local-dir .hf_upload_check
```

Do not upload the old full website or large `_downloads` source archives into this repository unless a separate LFS/storage policy is chosen.
