# Scanner forecast tail / outlier audit

Generato: 2026-09-25 23:49:54 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 87.565,11 $   | n/a                | 131.453,08 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         2 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 116,73 $      | n/a                | 205,41 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 0.09324 $     | n/a                | 0.13722 $     | n/a                |

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SNX-USD         | 2019-02-01   | 2019-05-11 | 275,40%          | UPPER_P90   | True          | 0,55%                   | 1,68%                   | 1,80%                   | 6,62%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | INJ-USD         | 2023-08-21   | 2023-11-28 | 114,93%          | UPPER_P90   | True          | 0,55%                   | 1,68%                   | 1,80%                   | 2,51%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KSM-USD         | 2023-08-27   | 2023-12-04 | 67,94%           | UPPER_P90   | False         | 0,55%                   | 1,68%                   | 1,80%                   | 1,30%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-09-18   | 2020-12-26 | 78,30%           | UPPER_P90   | True          | 0,55%                   | 1,68%                   | 1,80%                   | 1,57%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | CRV-USD         | 2022-11-11   | 2023-02-18 | -23,26%          | LOWER_P10   | False         | -0,89%                  | -1,68%                  | -1,29%                  | -1,04%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2022-11-10   | 2023-02-17 | -25,81%          | LOWER_P10   | False         | -0,89%                  | -1,68%                  | -1,29%                  | -1,10%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BCH-USD         | 2023-04-21   | 2023-07-29 | -21,34%          | LOWER_P10   | False         | -0,89%                  | -1,68%                  | -1,29%                  | -0,99%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-12-03   | 2020-03-11 | -37,38%          | LOWER_P10   | False         | -0,89%                  | -1,68%                  | -1,29%                  | -1,40%                   |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2020-11-14   | 2021-02-21 | 121,56%          | UPPER_P90   | True          | 0,68%                   | 3,32%                   | 10,53%                  | 2,82%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-04-02   | 2020-07-10 | 75,00%           | UPPER_P90   | True          | 0,68%                   | 3,32%                   | 10,53%                  | 1,63%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | OP-USD          | 2023-09-04   | 2023-12-12 | 70,44%           | UPPER_P90   | False         | 0,68%                   | 3,32%                   | 10,53%                  | 1,51%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SNX-USD         | 2019-02-01   | 2019-05-11 | 275,40%          | UPPER_P90   | True          | 0,68%                   | 3,32%                   | 10,53%                  | 6,77%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2024-05-10   | 2024-08-17 | -33,18%          | LOWER_P10   | False         | -2,31%                  | -3,32%                  | -0,25%                  | -1,15%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-07-01   | 2018-10-08 | -34,80%          | LOWER_P10   | False         | -2,31%                  | -3,32%                  | -0,25%                  | -1,19%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -2,31%                  | -3,32%                  | -0,25%                  | -1,27%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2021-01-31   | 2021-05-10 | -33,76%          | LOWER_P10   | False         | -2,31%                  | -3,32%                  | -0,25%                  | -1,16%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEAR-USD        | 2023-08-29   | 2023-12-06 | 55,08%           | UPPER_P90   | False         | 0,31%                   | 0,35%                   | 9,19%                   | 1,28%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2020-12-06   | 2021-03-15 | 213,76%          | UPPER_P90   | True          | 0,31%                   | 0,35%                   | 9,19%                   | 5,35%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2023-08-22   | 2023-11-29 | 108,08%          | UPPER_P90   | True          | 0,31%                   | 0,35%                   | 9,19%                   | 2,64%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-09-09   | 2020-12-17 | 97,38%           | UPPER_P90   | True          | 0,31%                   | 0,35%                   | 9,19%                   | 2,36%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DASH-USD        | 2019-11-13   | 2020-02-20 | -32,46%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -0,97%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MKR-USD         | 2018-08-01   | 2018-11-08 | -48,45%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -1,38%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -1,11%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BCH-USD         | 2019-11-08   | 2020-02-15 | -60,99%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -1,70%                   |
