# Scanner forecast tail / outlier audit

Generato: 2026-09-03 05:31:53 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           2 |                         3 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 84.069,39 $   | n/a                | 106.304,16 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           2 |                         4 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 112,17 $      | n/a                | 202,06 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         2 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 0.07480 $     | n/a                | 0.11186 $     | n/a                |

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-26   | 2026-05-05 | -33,21%          | LOWER_P10   | True          | -13,63%                 | -0,35%                  | -0,17%                  | -1,05%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ETC-USD         | 2021-12-27   | 2022-04-05 | -36,44%          | LOWER_P10   | True          | -13,63%                 | -0,35%                  | -0,17%                  | -1,13%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-24   | 2020-12-01 | -64,13%          | LOWER_P10   | True          | -13,63%                 | -0,35%                  | -0,17%                  | -1,84%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BNB-USD         | 2019-11-13   | 2020-02-20 | -45,76%          | LOWER_P10   | True          | -13,63%                 | -0,35%                  | -0,17%                  | -1,37%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BNB-USD         | 2018-11-13   | 2019-02-20 | 39,22%           | UPPER_P90   | False         | 0,83%                   | 0,35%                   | 6,23%                   | 0,81%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EGLD-USD        | 2023-08-09   | 2023-11-16 | 39,98%           | UPPER_P90   | False         | 0,83%                   | 0,35%                   | 6,23%                   | 0,83%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2023-08-09   | 2023-11-16 | 63,44%           | UPPER_P90   | True          | 0,83%                   | 0,35%                   | 6,23%                   | 1,43%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2020-08-24   | 2020-12-01 | 40,39%           | UPPER_P90   | False         | 0,83%                   | 0,35%                   | 6,23%                   | 0,84%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-26   | 2020-12-03 | 116,90%          | UPPER_P90   | False         | 0,06%                   | 1,32%                   | 6,41%                   | 2,38%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2020-03-04   | 2020-06-11 | 109,07%          | UPPER_P90   | False         | 0,06%                   | 1,32%                   | 6,41%                   | 2,18%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-23   | 2021-01-30 | 111,80%          | UPPER_P90   | False         | 0,06%                   | 1,32%                   | 6,41%                   | 2,25%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ATOM-USD        | 2020-10-18   | 2021-01-25 | 151,32%          | UPPER_P90   | True          | 0,06%                   | 1,32%                   | 6,41%                   | 3,27%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-13   | 2020-02-20 | -54,50%          | LOWER_P10   | False         | -5,11%                  | -1,32%                  | -0,76%                  | -2,01%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2019-11-13   | 2020-02-20 | -37,39%          | LOWER_P10   | False         | -5,11%                  | -1,32%                  | -0,76%                  | -1,57%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | False         | -5,11%                  | -1,32%                  | -0,76%                  | -2,24%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2024-08-23   | 2024-11-30 | -36,71%          | LOWER_P10   | False         | -5,11%                  | -1,32%                  | -0,76%                  | -1,55%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2026-01-10   | 2026-04-19 | 90,12%           | UPPER_P90   | True          | 0,46%                   | 0,15%                   | 10,21%                  | 2,25%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2021-05-12   | 2021-08-19 | 125,28%          | UPPER_P90   | True          | 0,46%                   | 0,15%                   | 10,21%                  | 3,15%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | OMG-USD         | 2021-05-11   | 2021-08-18 | 63,54%           | UPPER_P90   | True          | 0,46%                   | 0,15%                   | 10,21%                  | 1,57%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2021-05-11   | 2021-08-18 | 199,71%          | UPPER_P90   | True          | 0,46%                   | 0,15%                   | 10,21%                  | 5,06%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SOL-USD         | 2021-12-30   | 2022-04-08 | -31,49%          | LOWER_P10   | False         | -0,49%                  | -0,15%                  | -3,05%                  | -0,87%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2021-12-27   | 2022-04-05 | -32,76%          | LOWER_P10   | False         | -0,49%                  | -0,15%                  | -3,05%                  | -0,90%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2021-12-29   | 2022-04-07 | -35,36%          | LOWER_P10   | False         | -0,49%                  | -0,15%                  | -3,05%                  | -0,97%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KSM-USD         | 2021-12-30   | 2022-04-08 | -35,06%          | LOWER_P10   | False         | -0,49%                  | -0,15%                  | -3,05%                  | -0,96%                   |
