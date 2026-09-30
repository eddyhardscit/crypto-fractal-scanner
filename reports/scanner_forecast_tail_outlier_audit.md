# Scanner forecast tail / outlier audit

Generato: 2026-09-30 05:31:55 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 83.168,97 $   | 90.003,44 $        | 110.755,10 $  | 113.504,55 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           4 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 113,74 $      | 129,70 $           | 155,39 $      | 162,21 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08976 $     | 0.09863 $          | 0.13200 $     | 0.12081 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SNX-USD         | 2019-02-06   | 2019-05-16 | 143,22%          | UPPER_P90   | True          | 0,43%                   | 1,67%                   | 2,21%                   | 3,44%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | INJ-USD         | 2023-08-26   | 2023-12-03 | 112,10%          | UPPER_P90   | True          | 0,43%                   | 1,67%                   | 2,21%                   | 2,65%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-01   | 2023-12-09 | 33,29%           | UPPER_P90   | False         | 0,43%                   | 1,67%                   | 2,21%                   | 0,62%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,43%                   | 1,67%                   | 2,21%                   | 1,32%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2022-11-15   | 2023-02-22 | -26,39%          | LOWER_P10   | False         | -0,98%                  | -1,67%                  | -0,05%                  | -0,91%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOGE-USD        | 2024-01-01   | 2024-04-09 | -19,52%          | LOWER_P10   | False         | -0,98%                  | -1,67%                  | -0,05%                  | -0,73%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ENJ-USD         | 2022-11-17   | 2023-02-24 | -21,74%          | LOWER_P10   | False         | -0,98%                  | -1,67%                  | -0,05%                  | -0,79%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | QTUM-USD        | 2020-05-11   | 2020-08-18 | -22,53%          | LOWER_P10   | False         | -0,98%                  | -1,67%                  | -0,05%                  | -0,81%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,79%                   | 1,36%                   | 18,86%                  | 6,03%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -2,39%                  | -0,83%                  | -3,02%                  | -2,90%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-01   | 2023-12-09 | 33,29%           | UPPER_P90   | False         | 0,28%                   | 1,46%                   | 2,06%                   | 0,81%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,28%                   | 1,46%                   | 2,06%                   | 1,50%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | OP-USD          | 2023-09-09   | 2023-12-17 | 72,45%           | UPPER_P90   | True          | 0,28%                   | 1,46%                   | 2,06%                   | 1,81%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SOL-USD         | 2020-11-10   | 2021-02-17 | 72,75%           | UPPER_P90   | True          | 0,28%                   | 1,46%                   | 2,06%                   | 1,82%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2024-05-15   | 2024-08-22 | -24,53%          | LOWER_P10   | False         | -1,31%                  | -1,46%                  | -0,32%                  | -0,68%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-11-07   | 2021-02-14 | -29,90%          | LOWER_P10   | False         | -1,31%                  | -1,46%                  | -0,32%                  | -0,81%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-19   | 2019-03-28 | -28,88%          | LOWER_P10   | False         | -1,31%                  | -1,46%                  | -0,32%                  | -0,79%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SNX-USD         | 2020-11-07   | 2021-02-14 | -25,61%          | LOWER_P10   | False         | -1,31%                  | -1,46%                  | -0,32%                  | -0,70%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,43%                   | 2,07%                   | 17,97%                  | 6,14%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ATOM-USD        | 2023-09-08   | 2023-12-16 | -15,48%          | LOWER_P10   | False         | -7,20%                  | -1,70%                  | -3,02%                  | -3,33%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,26%                   | 1,15%                   | 5,22%                   | 1,46%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | FIL-USD         | 2020-12-16   | 2021-03-25 | 47,00%           | UPPER_P90   | True          | 0,26%                   | 1,15%                   | 5,22%                   | 1,12%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2023-08-27   | 2023-12-04 | 179,92%          | UPPER_P90   | True          | 0,26%                   | 1,15%                   | 5,22%                   | 4,52%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-06   | 2023-12-14 | 43,36%           | UPPER_P90   | False         | 0,26%                   | 1,15%                   | 5,22%                   | 1,02%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-08-06   | 2018-11-13 | -51,13%          | LOWER_P10   | False         | -1,30%                  | -1,15%                  | -0,28%                  | -1,40%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-03   | 2026-05-13 | -26,22%          | LOWER_P10   | False         | -1,30%                  | -1,15%                  | -0,28%                  | -0,76%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2022-11-14   | 2023-02-21 | -24,36%          | LOWER_P10   | False         | -1,30%                  | -1,15%                  | -0,28%                  | -0,71%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2026-02-04   | 2026-05-14 | -24,99%          | LOWER_P10   | False         | -1,30%                  | -1,15%                  | -0,28%                  | -0,73%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,90%                   | 1,16%                   | 21,89%                  | 8,41%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | True          | -6,14%                  | -0,41%                  | -5,24%                  | -3,51%                   |
