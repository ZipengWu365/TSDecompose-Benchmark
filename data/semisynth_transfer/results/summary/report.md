# Semi-Synthetic 22-Method Aligned Report

This experiment aligns the semi-synthetic transfer track to the paper-aligned 22-method synthetic benchmark by reusing the same fixed method defaults, the same metric panels, and the same De-Time gating policy for the classical subset.

## Protocol

| field | value |
| --- | --- |
| experiment_name | experiments_20260406_semisynth_22methods_aligned |
| dataset_count | 6 |
| mechanism_count | 3 |
| background_scales | [0.5, 1.0] |
| windows_per_setting | 8 |
| series_length | 480 |
| dt_fs | 1.0 / 1.0 |
| headline_claim | 22-method semi-synthetic companion track aligned to the paper-aligned 22-method synthetic benchmark |

## Mechanisms

| tier | mechanism | periods |
| --- | --- | --- |
| 1 | single_annual_cycle | [12] |
| 2 | annual_semiannual_multi_harmonic | [12, 6] |
| 3 | drifting_annual_cycle | [12] |

## Metrics

| panel | metrics |
| --- | --- |
| paper_5metric | `metric_T_r2`, `metric_T_dtw`, `metric_S_r2`, `metric_S_spectral_corr`, `metric_S_maxlag_corr` |
| audit_12metric | `metric_T_r2`, `metric_T_dtw`, `metric_T_pearson_r`, `metric_T_ccc`, `metric_T_first_diff_pearson`, `metric_T_directional_accuracy`, `metric_S_r2`, `metric_S_spectral_corr`, `metric_S_maxlag_corr`, `metric_S_best_lag_pearson`, `metric_S_spectral_cosine_similarity`, `metric_S_spectral_js_similarity` |
| semi_transfer_legacy | `trend_r2`, `seasonal_r2`, `spectral_corr`, `maxlag_corr`, `suite_score`, `pure_suite_score`, `transfer_gap` |

## Coverage

| method | display_name | family | dependency_requirements | total_rows | ok_rows | error_rows | coverage_success | detime_rows | current_rows | backends_seen | error_types |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| amd_block | AMD block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| autoformer_block | Autoformer block | neural_ma_family |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| ceemdan | CEEMDAN | classical |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| delelstm_block | DeLELSTM block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| dlinear_block | DLinear block | neural_ma_family |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| freqmoe_block | FreqMoE block | neural_wavelet_frequency |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| inparformer_block | InParformer block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| leddam_block | LEDDAM block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| ma_baseline | MA baseline | classical |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| moving_average_decomposition_block | Moving-average decomposition block | neural_ma_family |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| nbeats_interpretable | N-BEATS interpretable | neural_learned_prior | torch | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| parsimony_block | Parsimony block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| ssa | SSA | classical |  | 288 | 288 | 0 | 1.0 | 288 | 0 | detime |  |
| st_mtm_block | ST-MTM block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| stl | STL | classical |  | 288 | 288 | 0 | 1.0 | 288 | 0 | detime |  |
| timekan_block | TimeKAN block | neural_wavelet_frequency |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| times2d_block | Times2D block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| vmd | VMD | classical |  | 288 | 288 | 0 | 1.0 | 288 | 0 | detime |  |
| waveform_block | WaveForM block | neural_wavelet_frequency | pywt | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| wavelet | Wavelet | classical | pywt | 288 | 288 | 0 | 1.0 | 288 | 0 | detime |  |
| waveletmixer_block | WaveletMixer block | neural_wavelet_frequency | pywt | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |
| xpatch_block | xPatch block | neural_decomposition |  | 288 | 288 | 0 | 1.0 | 0 | 288 | current |  |

## Top Methods

### Paper 5-Metric

| method | overall_mean_rank | overall_std_rank | setting_count | rank_order |
| --- | --- | --- | --- | --- |
| stl | 6.985416666666667 | 3.599951001408708 | 288 | 1.0 |
| amd_block | 8.172222222222222 | 3.735999545703596 | 288 | 2.0 |
| ma_baseline | 8.489583333333334 | 5.142881399962151 | 288 | 3.0 |
| times2d_block | 8.595833333333333 | 2.7967595734167525 | 288 | 4.0 |
| autoformer_block | 9.111805555555556 | 2.346529694391044 | 288 | 5.0 |
| dlinear_block | 9.111805555555556 | 2.346529694391044 | 288 | 5.0 |
| moving_average_decomposition_block | 9.111805555555556 | 2.346529694391044 | 288 | 5.0 |
| ceemdan | 9.12152777777778 | 3.863826039656928 | 288 | 6.0 |

### Audit 12-Metric

| method | overall_mean_rank | overall_std_rank | setting_count | rank_order |
| --- | --- | --- | --- | --- |
| stl | 6.706452546296296 | 3.1410210818104267 | 288 | 1.0 |
| amd_block | 7.521267361111111 | 2.9045104738009093 | 288 | 2.0 |
| times2d_block | 7.574797453703703 | 2.7959623298339067 | 288 | 3.0 |
| st_mtm_block | 8.88816550925926 | 3.6043869446288825 | 288 | 4.0 |
| ceemdan | 9.166377314814817 | 3.729079262492143 | 288 | 5.0 |
| waveform_block | 9.753616898148149 | 3.69134737958948 | 288 | 6.0 |
| wavelet | 9.753616898148149 | 3.69134737958948 | 288 | 6.0 |
| timekan_block | 9.79296875 | 2.279786170402802 | 288 | 7.0 |

### Legacy Transfer Summary

| method | trend_r2 | seasonal_r2 | spectral_corr | maxlag_corr | suite_score | pure_suite_score | transfer_gap | legacy_rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stl | 0.5917646867309988 | 0.6094860238087247 | 0.8877583442431365 | 0.8576004266920986 | 0.7322220360993081 | 0.9348560943641604 | -0.2026340582648521 | 1 |
| amd_block | 0.6019793140919784 | 0.4146566846495754 | 0.6850578487622954 | 0.6732440298676681 | 0.64056512670348 | 0.5291524316369823 | 0.1114126950664977 | 2 |
| waveform_block | 0.3450634382941816 | 0.6687218685310619 | 0.9455414014217948 | 0.9034871805217368 | 0.6347888646329737 | -0.3119977513175105 | 0.9467866159504842 | 3 |
| wavelet | 0.3450634382941816 | 0.6687218685310619 | 0.9455414014217948 | 0.9034871805217368 | 0.6347888646329737 | -0.3119977513175105 | 0.9467866159504842 | 4 |
| times2d_block | 0.4493059644016218 | 0.3717861862247353 | 0.8139137678807056 | 0.7600482785353486 | 0.6181434938048245 | 0.9206584861239776 | -0.3025149923191532 | 5 |
| timekan_block | 0.4493059644016218 | 0.3286766179221844 | 0.7632182334043284 | 0.7164115133967102 | 0.5945604189010705 | 0.903505660013453 | -0.3089452411123823 | 6 |
| st_mtm_block | 0.4493059644016218 | 0.3843035237458225 | 0.6920137999909912 | 0.6668359825567408 | 0.5643654278377439 | 0.584934684533819 | -0.0205692566960751 | 7 |
| autoformer_block | 0.1880083416222151 | 0.6617075525339767 | 0.9450000111159644 | 0.9023458829783552 | 0.5558406443346874 | 0.8919207120026792 | -0.3360800676679917 | 8 |
| dlinear_block | 0.1880083416222151 | 0.6617075525339767 | 0.9450000111159644 | 0.9023458829783552 | 0.5558406443346874 | 0.8919207120026792 | -0.3360800676679917 | 9 |
| moving_average_decomposition_block | 0.1880083416222151 | 0.6617075525339767 | 0.9450000111159644 | 0.9023458829783552 | 0.5558406443346874 | 0.8919207120026792 | -0.3360800676679917 | 10 |

## Old vs New Semi-Synthetic Delta

| method | old_legacy_rank | legacy_rank | legacy_rank_delta_new_minus_old | suite_score_old | suite_score_new | suite_score_delta_new_minus_old |
| --- | --- | --- | --- | --- | --- | --- |
| stl | 5 | 1 | -4 | -3.8599256267196953 | 0.7322220360993081 | 4.592147662819004 |
| wavelet | 6 | 4 | -2 | -4.736082287280521 | 0.6347888646329737 | 5.370871151913494 |
| ma_baseline | 1 | 11 | 10 | -2.8483193173365784 | 0.5447590374849766 | 3.393078354821555 |
| ceemdan | 7 | 14 | 7 | -4.745963232861623 | 0.2421634218869134 | 4.988126654748537 |
| vmd | 8 | 18 | 10 | -5.191380807551536 | -0.9585644598484072 | 4.232816347703129 |
| ssa | 2 | 22 | 20 | -3.4865185476305545 | -22.923564698096094 | -19.43704615046554 |

## Semi vs Synthetic 300 Delta

| method | semi_rank | synthetic_rank | rank_delta_semi_minus_synth | metric_T_r2_delta_semi_minus_synth | metric_S_spectral_corr_delta_semi_minus_synth | metric_S_maxlag_corr_delta_semi_minus_synth |
| --- | --- | --- | --- | --- | --- | --- |
| stl | 1.0 | 1.0 | 0.0 | -0.1338530116641941 | -0.0245774880468091 | -0.0076706068394367 |
| amd_block | 2.0 | 13.0 | -11.0 | -0.1255111669070017 | 0.4881172962341473 | 0.4485909508748248 |
| ma_baseline | 3.0 | 8.0 | -5.0 | -0.2740849193265473 | -0.1631031060865009 | -0.1163566461628708 |
| times2d_block | 4.0 | 5.0 | -1.0 | -0.2443913995790761 | -0.1022777266178012 | -0.1338488184890812 |
| autoformer_block | 5.0 | 7.0 | -2.0 | -0.5180293702114854 | 0.0390105564678875 | 0.1037341793403651 |
| dlinear_block | 5.0 | 7.0 | -2.0 | -0.5180293702114854 | 0.0390105564678875 | 0.1037341793403651 |
| moving_average_decomposition_block | 5.0 | 7.0 | -2.0 | -0.5180293702114854 | 0.0390105564678875 | 0.1037341793403651 |
| ceemdan | 6.0 | 4.0 | 2.0 | -1.10733924107924 | 0.0527223674894715 | 0.0463332413021285 |
| inparformer_block | 7.0 | 14.0 | -7.0 | -0.5180293702114854 | 0.4863447997849348 | 0.4470615130594693 |
| waveform_block | 8.0 | 15.0 | -7.0 | 0.8256413390958743 | 0.5390324779399767 | 0.5193756490089592 |
| wavelet | 8.0 | 15.0 | -7.0 | 0.8256413390958743 | 0.5390324779399767 | 0.5193756490089592 |
| st_mtm_block | 9.0 | 10.0 | -1.0 | -0.2443913995790761 | 0.2746219852159466 | 0.4330153067819444 |

## Reviewer Audit

See [ffgj_claim_audit.md](ffgj_claim_audit.md) for the FFgj-specific claim audit.

## Notes

- The aligned semi-synthetic track keeps the 22-method fixed defaults identical to the paper-aligned synthetic 300 benchmark.
- The benchmark protocol is semi-synthetic rather than paper-identical: the data source is real-background plus injected seasonal mechanism, while the metric panel and method defaults remain aligned.
- The old rebuttal semi-synthetic results remain historical evidence; the new aligned track is the comparison-grade companion experiment.
