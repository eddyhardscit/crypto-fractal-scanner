# Scanner forecast tail / outlier audit

Generato: 2026-09-26 05:31:54 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           2 |                         3 |                      0 |                  5 | NONE                | INSUFFICIENT_REGIME_MATCHES | 82.488,67 $   | n/a                | 119.591,26 $  | n/a                |
| SOL     | AVAILABLE                   | SAME_BTC_REGIME         |                     0 |                           1 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 110,91 $      | 126,74 $           | 186,94 $      | 170,88 $           |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         2 |                      0 |                  5 | NONE                | INSUFFICIENT_REGIME_MATCHES | 0.09179 $     | n/a                | 0.13509 $     | n/a                |

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SNX-USD         | 2019-02-01   | 2019-05-11 | 275,40%          | UPPER_P90   | True          | 0,65%                   | 0,48%                   | 6,10%                   | 6,75%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | INJ-USD         | 2023-08-26   | 2023-12-03 | 112,10%          | UPPER_P90   | True          | 0,65%                   | 0,48%                   | 6,10%                   | 2,57%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2023-08-26   | 2023-12-03 | 54,44%           | UPPER_P90   | False         | 0,65%                   | 0,48%                   | 6,10%                   | 1,09%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KSM-USD         | 2023-08-27   | 2023-12-04 | 67,94%           | UPPER_P90   | False         | 0,65%                   | 0,48%                   | 6,10%                   | 1,43%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | CRV-USD         | 2022-11-11   | 2023-02-18 | -23,26%          | LOWER_P10   | False         | -1,32%                  | -0,48%                  | -1,33%                  | -0,90%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -1,32%                  | -0,48%                  | -1,33%                  | -1,28%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | CRV-USD         | 2023-09-02   | 2023-12-10 | -27,54%          | LOWER_P10   | False         | -1,32%                  | -0,48%                  | -1,33%                  | -1,01%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2022-11-10   | 2023-02-17 | -25,81%          | LOWER_P10   | False         | -1,32%                  | -0,48%                  | -1,33%                  | -0,97%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2020-11-14   | 2021-02-21 | 121,56%          | UPPER_P90   | True          | 0,68%                   | 0,14%                   | 4,42%                   | 2,98%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | OP-USD          | 2023-09-04   | 2023-12-12 | 70,44%           | UPPER_P90   | True          | 0,68%                   | 0,14%                   | 4,42%                   | 1,67%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SOL-USD         | 2020-11-05   | 2021-02-12 | 56,90%           | UPPER_P90   | True          | 0,68%                   | 0,14%                   | 4,42%                   | 1,32%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-04-07   | 2020-07-15 | 135,41%          | UPPER_P90   | True          | 0,68%                   | 0,14%                   | 4,42%                   | 3,33%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-08-29   | 2023-12-06 | 55,08%           | CENTRAL     | True          | 0,68%                   | 0,14%                   | 4,05%                   | 1,28%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2024-05-10   | 2024-08-17 | -33,18%          | LOWER_P10   | False         | -2,31%                  | -0,14%                  | -0,18%                  | -0,99%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -2,31%                  | -0,14%                  | -0,18%                  | -1,11%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOGE-USD        | 2018-07-01   | 2018-10-08 | -34,80%          | LOWER_P10   | False         | -2,31%                  | -0,14%                  | -0,18%                  | -1,03%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XRP-USD         | 2021-01-31   | 2021-05-10 | -33,76%          | LOWER_P10   | False         | -2,31%                  | -0,14%                  | -0,18%                  | -1,00%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-03-13   | 2019-06-20 | 49,79%           | UPPER_P90   | False         | 0,90%                   | 3,69%                   | 19,26%                  | 8,85%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -7,64%                  | -12,43%                 | -1,97%                  | -6,38%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEAR-USD        | 2023-08-29   | 2023-12-06 | 55,08%           | UPPER_P90   | True          | 0,31%                   | 0,35%                   | 4,63%                   | 1,32%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2020-12-11   | 2021-03-20 | 87,82%           | UPPER_P90   | True          | 0,31%                   | 0,35%                   | 4,63%                   | 2,16%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-09-14   | 2020-12-22 | 78,89%           | UPPER_P90   | True          | 0,31%                   | 0,35%                   | 4,63%                   | 1,93%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2023-08-27   | 2023-12-04 | 179,92%          | UPPER_P90   | True          | 0,31%                   | 0,35%                   | 4,63%                   | 4,53%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DASH-USD        | 2019-11-13   | 2020-02-20 | -32,46%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -0,92%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -1,06%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ONE-USD         | 2019-11-13   | 2020-02-20 | -49,38%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -1,35%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2019-11-13   | 2020-02-20 | -45,99%          | LOWER_P10   | False         | -2,77%                  | -0,35%                  | -1,83%                  | -1,27%                   |
