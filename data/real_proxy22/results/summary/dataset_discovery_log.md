# Dataset Discovery Log

This file tracks daily discovery work for real datasets with known physical mechanisms, known dominant periods, or known long-run trends.

## Update Template

- Date:
- Newly added candidate datasets:
- Newly promoted ready datasets:
- Duplicate datasets skipped:
- Sources reviewed:
- Key mechanism / period / trend notes:
- Parser or access blockers:
- Next high-value targets:

## Current Focus

- Prioritize official or primary-source datasets over mirrors.
- Prefer datasets with clear physical interpretation and documented expected periodicity or long-run trend.
- Update `configs/real_dataset_registry.csv` before proposing new decomposition runs.

## Update 2026-04-06

- Date: 2026-04-06
- Newly added candidate datasets: `solar_flux_f107`, `total_solar_irradiance`, `nh_snow_cover_extent`, `eurasia_snow_cover_extent`, `north_america_snow_cover_extent`, `upper_colorado_basin_precip`, `upper_colorado_basin_temp`, `mjo_rmm_amplitude`
- Newly promoted ready datasets: none
- Duplicate datasets skipped: none
- Sources reviewed: NOAA PSL Solar Flux monthly page, NOAA NCEI Total Solar Irradiance CDR catalog, Rutgers Global Snow Lab monthly download table, NOAA PSL Upper Colorado basin monthly pages, NOAA CPC MJO index page, NOAA PSL MJO format page
- Key mechanism / period / trend notes: F10.7 and TSI add solar-cycle signals beyond sunspots; Rutgers snow adds strong annual cryosphere forcing; Upper Colorado basin temperature and precipitation add basin-scale annual hydroclimate signals; MJO adds intraseasonal oscillation with 30-60 day structure
- Parser or access blockers: TSI is exposed as monthly NetCDF files in a THREDDS catalog rather than a single flat CSV; MJO direct data file path is not yet pinned down from the public pages; PSL CSV click-through is browser-fragile in tooling but endpoint patterns are clear
- Next high-value targets: promote one snow-cover series to ready with a parser, add direct NOAA API ingestion for `ny_tide_hourly` and `honolulu_tide_hourly`, wire up `upper_colorado_basin_precip`, test `solar_flux_f107`, and resolve a direct daily MJO file

## Update 2026-04-07

- Date: 2026-04-07
- Newly added candidate datasets: `iod_dmi_hadisst`
- Newly promoted ready datasets: none
- Duplicate datasets skipped: none
- Sources reviewed: NOAA PSL AMO monthly page and direct `amon.us.long.data` endpoint, NOAA PSL DMI monthly page and direct `dmi.had.long.csv` endpoint, Bureau of Meteorology MJO page and direct `rmm.74toRealtime.txt` endpoint, USGS NWIS daily-values JSON endpoint for station `09163500`, NOAA NCEI TSI THREDDS catalog dataset page
- Key mechanism / period / trend notes: AMO adds multidecadal North Atlantic variability; DMI adds physically interpretable Indian Ocean SST-gradient oscillations at interannual scales; BOM RMM adds a daily 30-60 day tropical intraseasonal oscillation; Colorado streamflow remains a clear snowmelt-forced annual hydrograph; TSI still looks useful for solar-cycle structure but the official NCEI distribution is cataloged as NetCDF files rather than a single flat time-series asset
- Parser or access blockers: local shell network access is blocked in this environment and `py.exe` has no installed Python runtime, so `scripts/refresh_candidate_downloads.py` and the downstream `candidate_downloads.csv` refresh could not be executed on 2026-04-07; TSI still needs either catalog-walking download support or a parser that stitches the monthly NetCDF assets
- Next high-value targets: add a parser and promotion path for one of `nh_snow_cover_extent` or `amo_index`, parameterize direct NOAA CO-OPS downloads for `ny_tide_hourly` and `honolulu_tide_hourly`, and add catalog-walking support for `total_solar_irradiance`

## Update 2026-04-08

- Date: 2026-04-08
- Newly added candidate datasets: `central_england_temperature`, `england_wales_precipitation`
- Newly promoted ready datasets: `solar_flux_f107`, `nh_snow_cover_extent`, `upper_colorado_basin_precip`, `upper_colorado_basin_temp`
- Duplicate datasets skipped: Great Lakes monthly water-level collection pages and additional IERS metadata pages were reviewed but not added because they were collection-level or yearly-file access patterns rather than clean new benchmark rows
- Sources reviewed: Met Office HadCET monthly download page and direct `meantemp_monthly_totals.txt` endpoint, Met Office HadUKP monthly download page and direct `HadEWP_monthly_totals.txt` endpoint, IERS EOP 14 C04 product/version metadata pages, NOAA CO-OPS Great Lakes monthly water-level ERDDAP page
- Key mechanism / period / trend notes: HadCET adds a very long monthly land-temperature series with a clear annual cycle and persistent long-run warming trend; HadUKP England and Wales precipitation adds a long official hydroclimate series with annual seasonality and lower-frequency variability; Rutgers NH snow remains a strong annual cryosphere benchmark with climate-sensitive decline; solar flux F10.7 adds an official solar-cycle series complementary to sunspots; Upper Colorado basin temperature and precipitation are now parser-ready official PSL basin-average hydroclimate series
- Parser or access blockers: `py.exe` is present but there is still no installed local Python runtime, and outbound shell HTTP requests remain blocked, so `refresh_candidate_downloads.py` could not be executed end-to-end; `candidate_downloads.csv` was refreshed manually from the updated registry plus cached artifacts; `amo_index`, `mjo_rmm_amplitude`, `usgs_colorado_streamflow`, and the new Met Office candidates still need a connected runtime to fetch fresh source artifacts locally
- Next high-value targets: add parser support for `amo_index` and `usgs_colorado_streamflow`, parameterize direct NOAA CO-OPS pulls for `ny_tide_hourly` and `honolulu_tide_hourly`, and add catalog-walking download support for `total_solar_irradiance`
