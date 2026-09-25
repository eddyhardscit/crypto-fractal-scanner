# Scanner forecast tail / outlier audit

Generato: 2026-09-25 05:31:52 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 93.723,69 $   | n/a                | 138.766,61 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         2 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 117,79 $      | n/a                | 196,33 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 0.08983 $     | n/a                | 0.13177 $     | n/a                |

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | INJ-USD         | 2023-08-21   | 2023-11-28 | 114,93%          | UPPER_P90   | True          | 0,17%                   | 2,08%                   | 17,76%                  | 2,41%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-09-18   | 2020-12-26 | 78,30%           | UPPER_P90   | True          | 0,17%                   | 2,08%                   | 17,76%                  | 1,47%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KSM-USD         | 2023-08-27   | 2023-12-04 | 67,94%           | UPPER_P90   | True          | 0,17%                   | 2,08%                   | 17,76%                  | 1,21%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SNX-USD         | 2019-02-01   | 2019-05-11 | 275,40%          | UPPER_P90   | True          | 0,17%                   | 2,08%                   | 17,76%                  | 6,53%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2022-11-10   | 2023-02-17 | -25,81%          | LOWER_P10   | False         | -3,50%                  | -2,08%                  | -0,34%                  | -1,20%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-12-03   | 2020-03-11 | -37,38%          | LOWER_P10   | False         | -3,50%                  | -2,08%                  | -0,34%                  | -1,49%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BCH-USD         | 2023-04-21   | 2023-07-29 | -21,34%          | LOWER_P10   | False         | -3,50%                  | -2,08%                  | -0,34%                  | -1,08%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | CRV-USD         | 2022-11-11   | 2023-02-18 | -23,26%          | LOWER_P10   | False         | -3,50%                  | -2,08%                  | -0,34%                  | -1,13%                   |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-04-02   | 2020-07-10 | 75,00%           | UPPER_P90   | True          | 0,20%                   | 0,11%                   | 10,99%                  | 1,52%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2020-11-09   | 2021-02-16 | 153,55%          | UPPER_P90   | True          | 0,20%                   | 0,11%                   | 10,99%                  | 3,53%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SNX-USD         | 2019-02-01   | 2019-05-11 | 275,40%          | UPPER_P90   | True          | 0,20%                   | 0,11%                   | 10,99%                  | 6,66%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SOL-USD         | 2020-10-31   | 2021-02-07 | 121,57%          | UPPER_P90   | True          | 0,20%                   | 0,11%                   | 10,99%                  | 2,71%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -1,08%                  | -0,11%                  | -0,71%                  | -1,38%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-07-01   | 2018-10-08 | -34,80%          | LOWER_P10   | False         | -1,08%                  | -0,11%                  | -0,71%                  | -1,30%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2024-05-10   | 2024-08-17 | -33,18%          | LOWER_P10   | False         | -1,08%                  | -0,11%                  | -0,71%                  | -1,26%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2022-11-15   | 2023-02-22 | -26,39%          | LOWER_P10   | False         | -1,08%                  | -0,11%                  | -0,71%                  | -1,08%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2020-12-06   | 2021-03-15 | 213,76%          | UPPER_P90   | True          | 0,03%                   | 0,05%                   | 10,25%                  | 5,45%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-09-09   | 2020-12-17 | 97,38%           | UPPER_P90   | True          | 0,03%                   | 0,05%                   | 10,25%                  | 2,46%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEAR-USD        | 2023-08-29   | 2023-12-06 | 55,08%           | UPPER_P90   | True          | 0,03%                   | 0,05%                   | 10,25%                  | 1,38%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2023-08-22   | 2023-11-29 | 108,08%          | UPPER_P90   | True          | 0,03%                   | 0,05%                   | 10,25%                  | 2,74%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DASH-USD        | 2019-11-08   | 2020-02-15 | -64,76%          | LOWER_P10   | True          | -0,70%                  | -0,05%                  | -1,83%                  | -1,69%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BCH-USD         | 2019-11-08   | 2020-02-15 | -60,99%          | LOWER_P10   | True          | -0,70%                  | -0,05%                  | -1,83%                  | -1,60%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EOS-USD         | 2019-11-08   | 2020-02-15 | -60,27%          | LOWER_P10   | True          | -0,70%                  | -0,05%                  | -1,83%                  | -1,58%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KAVA-USD        | 2022-01-16   | 2022-04-25 | -49,55%          | LOWER_P10   | True          | -0,70%                  | -0,05%                  | -1,83%                  | -1,30%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BTC-USD         | 2019-11-08   | 2020-02-15 | -49,29%          | CENTRAL     | True          | -0,65%                  | -0,05%                  | -1,83%                  | -1,30%                   |
