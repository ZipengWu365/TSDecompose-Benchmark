# FFgj Claim Audit

## Supported

- `drift` remains a strong seasonal stressor: the mean seasonal diagnostics under `drifting_annual_cycle` stay below the easier annual mechanisms in the aligned semi-synthetic track.

## Softened

- `STL fails under drift` is too strong. In the aligned semi-synthetic track, STL under drift has seasonal_r2 `0.405` and suite_score `0.373`, which supports `degrades under drift but remains competitive`.
- `CEEMDAN` must be described as dropping in transfer: the semi-vs-synthetic paper-rank delta is `2.0`.

## Not Supported By Transfer

- `wavelet remains weak on seasonal transfer` is not supported by the aligned track: wavelet reaches seasonal_r2 `0.669`, suite_score `0.635`, and legacy rank `4`.
- `SSA remains one of the more stable methods in transfer` is not supported by the aligned track: SSA falls to legacy rank `22` with trend_r2 `-46.228`.
- `VMD drift strength cleanly transfers` is not supported on trend recovery: VMD under drift reaches trend_r2 `-7.487` in the aligned semi-synthetic track.
