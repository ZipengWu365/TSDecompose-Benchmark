# Real Dataset Hourly 22-Method Report

Latest round: `round_0003`

A real-dataset companion track extending the paper's CO2 and tide case studies to a broader 22-method, hourly-refreshable decomposition registry.

## Registry Snapshot

| dataset_id | status | domain | cadence | primary_period | expected_periods_json | expected_trend |
| --- | --- | --- | --- | --- | --- | --- |
| mauna_loa_co2 | ready_core | carbon_cycle | monthly | 12 | [12] | upward |
| global_ch4 | ready_core | carbon_cycle | monthly | 12 | [12] | upward |
| qbo_30mb | ready_core | atmosphere | monthly | 28 | [24,28,32] | oscillatory |
| arctic_sea_ice_extent | ready_core | cryosphere | monthly | 12 | [12] | downward |
| antarctic_sea_ice_extent | ready_core | cryosphere | monthly | 12 | [12] | regime_shifted |
| global_ndvi | ready_core | biosphere | monthly | 12 | [12] | mixed |
| sunspots_monthly | ready_core | solar | monthly | 132 | [120,132,144] | cyclic |
| nino34_sst_anom | ready_core | ocean_atmosphere | monthly | 48 | [36,48,60] | oscillatory |
| soi_monthly | ready_core | ocean_atmosphere | monthly | 48 | [36,48,60] | oscillatory |
| pdo_index | ready_exploratory | ocean_atmosphere | monthly | 120 | [96,120,144] | oscillatory |
| ao_index | ready_exploratory | atmosphere | monthly | 12 | [12,48] | weakly_seasonal |
| nao_index | ready_exploratory | atmosphere | monthly | 12 | [12,48] | weakly_seasonal |
| global_mean_sea_level | ready_core | ocean | monthly | 12 | [12] | upward |
| sf_tide_hourly | ready_core | ocean | hourly | 12 | [12,24] | stable_harmonic |
| ny_tide_hourly | candidate_api | ocean | hourly | 12 | [12,24] | stable_harmonic |
| honolulu_tide_hourly | candidate_api | ocean | hourly | 12 | [12,24] | stable_harmonic |
| amo_index | candidate_page | ocean_atmosphere | monthly | 120 | [96,120,144] | oscillatory |
| usgs_colorado_streamflow | candidate_api | hydrology | daily | 365 | [365] | seasonal |
| iers_length_of_day | candidate_manual | geodesy | daily | 365 | [365,433] | oscillatory |

## Latest Overall Ranking

| round_id | method | overall_mean_rank | overall_std_rank | setting_count | rank_order |
| --- | --- | --- | --- | --- | --- |
| round_0003 | vmd | 7.464285714285714 | 3.0892552773278816 | 14 | 1.0 |
| round_0003 | stl | 7.571428571428571 | 2.1510425674505207 | 14 | 2.0 |
| round_0003 | ceemdan | 8.607142857142858 | 2.398011233388592 | 14 | 3.0 |
| round_0003 | waveform_block | 9.011904761904765 | 1.7350882212530676 | 14 | 4.0 |
| round_0003 | wavelet | 9.011904761904765 | 1.7350882212530676 | 14 | 4.0 |
| round_0003 | ssa | 9.25 | 3.605403115316181 | 14 | 5.0 |
| round_0003 | waveletmixer_block | 10.202380952380953 | 1.0725370741078255 | 14 | 6.0 |
| round_0003 | freqmoe_block | 10.529761904761903 | 2.4507122510079675 | 14 | 7.0 |
| round_0003 | amd_block | 10.607142857142858 | 3.793047588972488 | 14 | 8.0 |
| round_0003 | st_mtm_block | 10.857142857142858 | 2.4889560703038374 | 14 | 9.0 |
| round_0003 | inparformer_block | 11.625 | 3.807991764966317 | 14 | 10.0 |
| round_0003 | ma_baseline | 11.666666666666668 | 2.273970134135488 | 14 | 11.0 |
| round_0003 | xpatch_block | 11.702380952380953 | 3.236529329408602 | 14 | 12.0 |
| round_0003 | delelstm_block | 12.464285714285714 | 2.420689464747076 | 14 | 13.0 |
| round_0003 | autoformer_block | 12.892857142857142 | 1.3849884180717609 | 14 | 14.0 |

## Latest By-Dataset Ranking

| round_id | dataset_id | method | overall_mean_rank | overall_std_rank | setting_count | rank_order |
| --- | --- | --- | --- | --- | --- | --- |
| round_0003 | antarctic_sea_ice_extent | stl | 5.833333333333333 |  | 1 | 1.0 |
| round_0003 | antarctic_sea_ice_extent | vmd | 6.666666666666667 |  | 1 | 2.0 |
| round_0003 | antarctic_sea_ice_extent | amd_block | 7.5 |  | 1 | 3.0 |
| round_0003 | antarctic_sea_ice_extent | ceemdan | 8.0 |  | 1 | 4.0 |
| round_0003 | antarctic_sea_ice_extent | ma_baseline | 9.0 |  | 1 | 5.0 |
| round_0003 | antarctic_sea_ice_extent | waveletmixer_block | 9.166666666666666 |  | 1 | 6.0 |
| round_0003 | antarctic_sea_ice_extent | inparformer_block | 9.416666666666666 |  | 1 | 7.0 |
| round_0003 | antarctic_sea_ice_extent | freqmoe_block | 9.666666666666666 |  | 1 | 8.0 |
| round_0003 | antarctic_sea_ice_extent | ssa | 9.666666666666666 |  | 1 | 8.0 |
| round_0003 | antarctic_sea_ice_extent | delelstm_block | 9.833333333333334 |  | 1 | 9.0 |
| round_0003 | antarctic_sea_ice_extent | waveform_block | 9.833333333333334 |  | 1 | 9.0 |
| round_0003 | antarctic_sea_ice_extent | wavelet | 9.833333333333334 |  | 1 | 9.0 |
| round_0003 | antarctic_sea_ice_extent | st_mtm_block | 10.25 |  | 1 | 10.0 |
| round_0003 | antarctic_sea_ice_extent | times2d_block | 11.916666666666666 |  | 1 | 11.0 |
| round_0003 | antarctic_sea_ice_extent | autoformer_block | 13.75 |  | 1 | 12.0 |
| round_0003 | antarctic_sea_ice_extent | dlinear_block | 13.75 |  | 1 | 12.0 |
| round_0003 | antarctic_sea_ice_extent | moving_average_decomposition_block | 13.75 |  | 1 | 12.0 |
| round_0003 | antarctic_sea_ice_extent | xpatch_block | 15.5 |  | 1 | 13.0 |
| round_0003 | antarctic_sea_ice_extent | nbeats_interpretable | 16.0 |  | 1 | 14.0 |
| round_0003 | antarctic_sea_ice_extent | timekan_block | 16.75 |  | 1 | 15.0 |

## Coverage

| method | display_name | family | total_rows | ok_rows | error_rows | coverage_success | backends_seen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amd_block | AMD block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |
| autoformer_block | Autoformer block | neural_ma_family | 14 | 14 | 0 | 1.0 | current |
| ceemdan | CEEMDAN | classical | 14 | 14 | 0 | 1.0 | current |
| delelstm_block | DeLELSTM block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |
| dlinear_block | DLinear block | neural_ma_family | 14 | 14 | 0 | 1.0 | current |
| freqmoe_block | FreqMoE block | neural_wavelet_frequency | 14 | 14 | 0 | 1.0 | current |
| inparformer_block | InParformer block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |
| leddam_block | LEDDAM block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |
| ma_baseline | MA baseline | classical | 14 | 14 | 0 | 1.0 | current |
| moving_average_decomposition_block | Moving-average decomposition block | neural_ma_family | 14 | 14 | 0 | 1.0 | current |
| nbeats_interpretable | N-BEATS interpretable | neural_learned_prior | 14 | 14 | 0 | 1.0 | current |
| parsimony_block | Parsimony block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |
| ssa | SSA | classical | 14 | 14 | 0 | 1.0 | detime |
| st_mtm_block | ST-MTM block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |
| stl | STL | classical | 14 | 14 | 0 | 1.0 | detime |
| timekan_block | TimeKAN block | neural_wavelet_frequency | 14 | 14 | 0 | 1.0 | current |
| times2d_block | Times2D block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |
| vmd | VMD | classical | 14 | 14 | 0 | 1.0 | detime |
| waveform_block | WaveForM block | neural_wavelet_frequency | 14 | 14 | 0 | 1.0 | current |
| wavelet | Wavelet | classical | 14 | 14 | 0 | 1.0 | detime |
| waveletmixer_block | WaveletMixer block | neural_wavelet_frequency | 14 | 14 | 0 | 1.0 | current |
| xpatch_block | xPatch block | neural_decomposition | 14 | 14 | 0 | 1.0 | current |

## Notes

- These rankings are proxy-diagnostic rankings on real data, not ground-truth recovery rankings.
- The method defaults are identical to the paper-aligned 22-method synthetic benchmark.
- De-Time reuse follows the validated backend choices from the synthetic benchmark rather than a new real-data parity gate.
