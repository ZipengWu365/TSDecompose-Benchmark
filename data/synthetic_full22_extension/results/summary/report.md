# Full Benchmark Report

This experiment uses the paper-aligned 6-scenario synthetic benchmark protocol and extends it with a 22-method roster plus an additional 12-metric audit panel.

## Protocol

| field | value |
| --- | --- |
| experiment_name | experiments_20260406_full_benchmark_22methods_detime |
| suite_name | core |
| scenario_count | 6 |
| draws_per_scenario | 50 |
| series_length | 512 |
| dt_fs | 1.0 / 1.0 |
| period_protocol | true-period-given |
| seed_list | [0] |
| paper_alignment_claim | paper-aligned benchmark protocol with an additional 12-metric audit panel |

## Scenarios

| tier | scenario_id | periods | mechanism |
| --- | --- | --- | --- |
| 1 | trend_only_linear | [50] | pure linear trend |
| 1 | trend_plus_single_sine | [50] | quadratic trend plus single seasonal sine |
| 2 | poly_trend_multi_harmonic | [48] | polynomial trend plus multi-harmonic seasonality |
| 2 | logistic_trend_multi_seasonal | [24, 168] | logistic trend plus dual seasonal structure |
| 3 | rw_trend_freq_drifting_cycle | [50] | smooth random-walk trend plus drifting-frequency cycle |
| 3 | piecewise_trend_regime_cycle_with_events | [40, 65] | piecewise trend plus regime cycle plus event perturbations |

## Metrics

| panel | metrics |
| --- | --- |
| paper_5metric | `metric_T_r2`, `metric_T_dtw`, `metric_S_r2`, `metric_S_spectral_corr`, `metric_S_maxlag_corr` |
| audit_12metric | `metric_T_r2`, `metric_T_dtw`, `metric_T_pearson_r`, `metric_T_ccc`, `metric_T_first_diff_pearson`, `metric_T_directional_accuracy`, `metric_S_r2`, `metric_S_spectral_corr`, `metric_S_maxlag_corr`, `metric_S_best_lag_pearson`, `metric_S_spectral_cosine_similarity`, `metric_S_spectral_js_similarity` |
| auxiliary_diagnostics | `metric_S_topk_freq_hit_rate` (stored in raw outputs and coverage diagnostics; not included in the literal 12-metric ranking panel) |

## Method Families

| family | method_count |
| --- | --- |
| classical | 6 |
| neural_decomposition | 8 |
| neural_learned_prior | 1 |
| neural_ma_family | 3 |
| neural_wavelet_frequency | 4 |

## De-Time Backend Selection

| method | status | backend_selected | mean_abs_metric_delta_max | mean_abs_rank_delta | notes |
| --- | --- | --- | --- | --- | --- |
| amd_block | current_only | current |  |  | method policy is current_only |
| autoformer_block | current_only | current |  |  | method policy is current_only |
| ceemdan | failed | current | 0.2302612311126844 | 0.3 | delta=0.230261, rank_delta=0.300000 |
| delelstm_block | current_only | current |  |  | method policy is current_only |
| dlinear_block | current_only | current |  |  | method policy is current_only |
| freqmoe_block | current_only | current |  |  | method policy is current_only |
| inparformer_block | current_only | current |  |  | method policy is current_only |
| leddam_block | current_only | current |  |  | method policy is current_only |
| ma_baseline | current_only | current |  |  | method policy is current_only |
| moving_average_decomposition_block | current_only | current |  |  | method policy is current_only |
| nbeats_interpretable | current_only | current |  |  | method policy is current_only |
| parsimony_block | current_only | current |  |  | method policy is current_only |
| ssa | passed | detime | 0.0 | 0.0 |  |
| st_mtm_block | current_only | current |  |  | method policy is current_only |
| stl | passed | detime | 0.0 | 0.0 |  |
| timekan_block | current_only | current |  |  | method policy is current_only |
| times2d_block | current_only | current |  |  | method policy is current_only |
| vmd | passed | detime | 0.0 | 0.0 |  |
| waveform_block | current_only | current |  |  | method policy is current_only |
| wavelet | passed | detime | 0.0 | 0.0 |  |
| waveletmixer_block | current_only | current |  |  | method policy is current_only |
| xpatch_block | current_only | current |  |  | method policy is current_only |

## Coverage

| method | family | total_rows | ok_rows | error_rows | coverage_success | backends_seen | error_types |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amd_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |
| autoformer_block | neural_ma_family | 300 | 300 | 0 | 1.0 | current |  |
| ceemdan | classical | 300 | 300 | 0 | 1.0 | current |  |
| delelstm_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |
| dlinear_block | neural_ma_family | 300 | 300 | 0 | 1.0 | current |  |
| freqmoe_block | neural_wavelet_frequency | 300 | 300 | 0 | 1.0 | current |  |
| inparformer_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |
| leddam_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |
| ma_baseline | classical | 300 | 300 | 0 | 1.0 | current |  |
| moving_average_decomposition_block | neural_ma_family | 300 | 300 | 0 | 1.0 | current |  |
| nbeats_interpretable | neural_learned_prior | 300 | 300 | 0 | 1.0 | current |  |
| parsimony_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |
| ssa | classical | 300 | 300 | 0 | 1.0 | detime |  |
| st_mtm_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |
| stl | classical | 300 | 300 | 0 | 1.0 | detime |  |
| timekan_block | neural_wavelet_frequency | 300 | 300 | 0 | 1.0 | current |  |
| times2d_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |
| vmd | classical | 300 | 300 | 0 | 1.0 | detime |  |
| waveform_block | neural_wavelet_frequency | 300 | 300 | 0 | 1.0 | current |  |
| wavelet | classical | 300 | 300 | 0 | 1.0 | detime |  |
| waveletmixer_block | neural_wavelet_frequency | 300 | 300 | 0 | 1.0 | current |  |
| xpatch_block | neural_decomposition | 300 | 300 | 0 | 1.0 | current |  |

## Paper 5-Metric Overall Means

| method | metric_T_r2_mean | metric_T_dtw_mean | metric_S_r2_mean | metric_S_spectral_corr_mean | metric_S_maxlag_corr_mean | coverage_success | row_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amd_block | 0.7274904809989802 | 2.6113763521860847 | 0.1442848388203126 | 0.196940552528148 | 0.2246530789928432 | 1.0 | 300 |
| autoformer_block | 0.7060377118337006 | 2.6462532649550146 | 0.4521116268284184 | 0.905989454648077 | 0.7986117036379898 | 1.0 | 300 |
| ceemdan | 0.6578167872839796 | 3.1095527221248376 | 0.752213716351843 | 0.9025583319934 | 0.8660846543531738 | 1.0 | 300 |
| delelstm_block | -1.591470576993057 | 12.788397456680917 | 0.0338553899030091 | 0.1977800982739836 | 0.2229542822584521 | 1.0 | 300 |
| dlinear_block | 0.7060377118337006 | 2.6462532649550146 | 0.4521116268284184 | 0.905989454648077 | 0.7986117036379898 | 1.0 | 300 |
| freqmoe_block | 0.6965214315719787 | 2.5749302517849504 | 0.6154587815514886 | 0.9190916096298012 | 0.8974242924729325 | 1.0 | 300 |
| inparformer_block | 0.7060377118337006 | 2.6462532649550146 | 0.1447520051719121 | 0.1971248662217653 | 0.224704638446838 | 1.0 | 300 |
| leddam_block | -0.9362691028534768 | 11.251548224862738 | -0.2033296029022165 | -0.1622887202822312 | 0.034352568418867 | 1.0 | 300 |
| ma_baseline | 0.6847688721725587 | 3.74386962637587 | 0.6810977668054502 | 0.8482671467114736 | 0.7888608497857817 | 1.0 | 300 |
| moving_average_decomposition_block | 0.7060377118337006 | 2.6462532649550146 | 0.4521116268284184 | 0.905989454648077 | 0.7986117036379898 | 1.0 | 300 |

## Audit 12-Metric Overall Means

| method | metric_T_r2_mean | metric_T_dtw_mean | metric_T_pearson_r_mean | metric_T_ccc_mean | metric_T_first_diff_pearson_mean | metric_T_directional_accuracy_mean | metric_S_r2_mean | metric_S_spectral_corr_mean | metric_S_maxlag_corr_mean | metric_S_best_lag_pearson_mean | metric_S_spectral_cosine_similarity_mean | metric_S_spectral_js_similarity_mean | coverage_success | row_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| amd_block | 0.7274904809989802 | 2.6113763521860847 | 0.9411841680791596 | 0.8946930886820151 | 0.3463249899567091 | 0.7306066536203523 | 0.1442848388203126 | 0.196940552528148 | 0.2246530789928432 | 0.2351280197336298 | 0.2150496501165736 | 0.2300197713359312 | 1.0 | 300 |
| autoformer_block | 0.7060377118337006 | 2.6462532649550146 | 0.9307344951652644 | 0.8875981604603232 | 0.2642415805690847 | 0.696921069797782 | 0.4521116268284184 | 0.905989454648077 | 0.7986117036379898 | 0.8026281569452465 | 0.976560225039356 | 0.8108375457239894 | 1.0 | 300 |
| ceemdan | 0.6578167872839796 | 3.1095527221248376 | 0.9123895733543712 | 0.85999119762386 | 0.5664785886274973 | 0.8016503587736464 | 0.752213716351843 | 0.9025583319934 | 0.8660846543531738 | 0.8756795324803649 | 0.9109446947577576 | 0.8869916936693941 | 1.0 | 300 |
| delelstm_block | -1.591470576993057 | 12.788397456680917 | 0.6252463976444814 | 0.5468654602542021 | 0.0356829362595106 | 0.5232876712328768 | 0.0338553899030091 | 0.1977800982739836 | 0.2229542822584521 | 0.2349268753955885 | 0.2150337671682623 | 0.2301915257373063 | 1.0 | 300 |
| dlinear_block | 0.7060377118337006 | 2.6462532649550146 | 0.9307344951652644 | 0.8875981604603232 | 0.2642415805690847 | 0.696921069797782 | 0.4521116268284184 | 0.905989454648077 | 0.7986117036379898 | 0.8026281569452465 | 0.976560225039356 | 0.8108375457239894 | 1.0 | 300 |
| freqmoe_block | 0.6965214315719787 | 2.5749302517849504 | 0.928708851795916 | 0.8927757871414688 | 0.2019236916863964 | 0.6440052185257664 | 0.6154587815514886 | 0.9190916096298012 | 0.8974242924729325 | 0.9042492199736842 | 0.9631265227708422 | 0.9057927636050498 | 1.0 | 300 |
| inparformer_block | 0.7060377118337006 | 2.6462532649550146 | 0.9307344951652644 | 0.8875981604603232 | 0.2642415805690847 | 0.696921069797782 | 0.1447520051719121 | 0.1971248662217653 | 0.224704638446838 | 0.235219815475121 | 0.2150568766625822 | 0.2300874930356285 | 1.0 | 300 |
| leddam_block | -0.9362691028534768 | 11.251548224862738 | 0.6527959284772961 | 0.5838428716423929 | 0.028535030077391 | 0.5179452054794521 | -0.2033296029022165 | -0.1622887202822312 | 0.034352568418867 | 0.035934604329463 | 0.0168418789025069 | 0.0170314990476996 | 1.0 | 300 |
| ma_baseline | 0.6847688721725587 | 3.74386962637587 | 0.9130561903460296 | 0.865435612828151 | 0.1825368341800967 | 0.6285257664709719 | 0.6810977668054502 | 0.8482671467114736 | 0.7888608497857817 | 0.8114482560960236 | 0.8298382591384343 | 0.8242555522069939 | 1.0 | 300 |
| moving_average_decomposition_block | 0.7060377118337006 | 2.6462532649550146 | 0.9307344951652644 | 0.8875981604603232 | 0.2642415805690847 | 0.696921069797782 | 0.4521116268284184 | 0.905989454648077 | 0.7986117036379898 | 0.8026281569452465 | 0.976560225039356 | 0.8108375457239894 | 1.0 | 300 |

## Top 5 By Paper 5-Metric Ranking

| rank_order | method | overall_mean_rank | overall_std_rank |
| --- | --- | --- | --- |
| 1.0 | stl | 5.563666666666666 | 3.2378995042394494 |
| 2.0 | freqmoe_block | 7.244666666666667 | 1.7137467672216815 |
| 3.0 | vmd | 7.338666666666667 | 4.711350936590757 |
| 4.0 | ceemdan | 7.773333333333333 | 3.461825579570233 |
| 5.0 | times2d_block | 7.959333333333334 | 1.9070752499360415 |

## Top 5 By Audit 12-Metric Ranking

| rank_order | method | overall_mean_rank | overall_std_rank |
| --- | --- | --- | --- |
| 1.0 | stl | 5.244666666666667 | 2.93897524844332 |
| 2.0 | ceemdan | 7.443138888888889 | 3.0992365204402947 |
| 3.0 | vmd | 7.705916666666667 | 4.631125955194508 |
| 4.0 | freqmoe_block | 8.20336111111111 | 1.8021406531740567 |
| 5.0 | times2d_block | 8.420694444444445 | 1.947709382980104 |

## Notes

- The benchmark generation protocol is paper-aligned: 6 scenarios, 50 draws, length 512, dt=1.0, true-period-given.
- The 22-method roster is an extension over the paper's original method family list and should be described as such.
- The 12-metric audit panel is an extension over the paper's original 5-metric panel.
- `metric_S_topk_freq_hit_rate` is emitted as an auxiliary raw diagnostic, but excluded from the audit_12 ranking panel to keep the panel literally 12 metrics wide.
