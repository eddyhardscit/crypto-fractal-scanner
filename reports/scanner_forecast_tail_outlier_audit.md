# Scanner forecast tail / outlier audit

Generato: 2026-09-29 05:31:57 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.312,25 $   | 86.661,15 $        | 112.715,59 $  | 96.387,34 $        |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           3 |                        11 |                     11 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 115,55 $      | 127,21 $           | 185,25 $      | 153,30 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08312 $     | 0.09854 $          | 0.15157 $     | 0.12269 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | INJ-USD         | 2023-08-26   | 2023-12-03 | 112,10%          | UPPER_P90   | True          | 0,28%                   | 0,13%                   | 4,64%                   | 2,67%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-14   | 2020-12-22 | 78,89%           | UPPER_P90   | True          | 0,28%                   | 0,13%                   | 4,64%                   | 1,82%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2023-08-26   | 2023-12-03 | 54,44%           | UPPER_P90   | False         | 0,28%                   | 0,13%                   | 4,64%                   | 1,19%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SNX-USD         | 2019-02-06   | 2019-05-16 | 143,22%          | UPPER_P90   | True          | 0,28%                   | 0,13%                   | 4,64%                   | 3,47%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2022-11-15   | 2023-02-22 | -26,39%          | LOWER_P10   | False         | -0,94%                  | -0,13%                  | -2,11%                  | -0,88%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -0,94%                  | -0,13%                  | -2,11%                  | -1,18%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOGE-USD        | 2024-01-01   | 2024-04-09 | -19,52%          | LOWER_P10   | False         | -0,94%                  | -0,13%                  | -2,11%                  | -0,70%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ENJ-USD         | 2022-11-17   | 2023-02-24 | -21,74%          | LOWER_P10   | False         | -0,94%                  | -0,13%                  | -2,11%                  | -0,76%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ETC-USD         | 2023-09-03   | 2023-12-11 | 30,13%           | UPPER_P90   | True          | 0,79%                   | 1,16%                   | 7,15%                   | 3,60%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -3,06%                  | -1,16%                  | -2,05%                  | -2,30%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,26%                   | 0,18%                   | 19,23%                  | 1,32%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2020-11-14   | 2021-02-21 | 121,56%          | UPPER_P90   | True          | 0,26%                   | 0,18%                   | 19,23%                  | 2,89%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | OP-USD          | 2023-09-04   | 2023-12-12 | 70,44%           | UPPER_P90   | True          | 0,26%                   | 0,18%                   | 19,23%                  | 1,58%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SNX-USD         | 2019-02-06   | 2019-05-16 | 143,22%          | UPPER_P90   | True          | 0,26%                   | 0,18%                   | 19,23%                  | 3,45%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-19   | 2019-03-28 | -28,88%          | LOWER_P10   | False         | -1,30%                  | -0,18%                  | -0,35%                  | -0,97%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2022-11-14   | 2023-02-21 | -24,36%          | LOWER_P10   | False         | -1,30%                  | -0,18%                  | -0,35%                  | -0,85%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2024-05-15   | 2024-08-22 | -24,53%          | LOWER_P10   | False         | -1,30%                  | -0,18%                  | -0,35%                  | -0,86%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-11-07   | 2021-02-14 | -29,90%          | LOWER_P10   | False         | -1,30%                  | -0,18%                  | -0,35%                  | -0,99%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,43%                   | 1,62%                   | 15,33%                  | 5,02%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ETC-USD         | 2023-09-03   | 2023-12-11 | 30,13%           | UPPER_P90   | False         | 0,43%                   | 1,62%                   | 12,30%                  | 2,00%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ATOM-USD        | 2023-09-08   | 2023-12-16 | -15,48%          | LOWER_P10   | False         | -8,14%                  | -0,45%                  | -3,02%                  | -2,56%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -7,71%                  | -0,45%                  | -3,02%                  | -2,13%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | FIL-USD         | 2020-12-11   | 2021-03-20 | 87,82%           | UPPER_P90   | True          | 0,02%                   | 0,11%                   | 17,66%                  | 2,11%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-14   | 2020-12-22 | 78,89%           | UPPER_P90   | True          | 0,02%                   | 0,11%                   | 17,66%                  | 1,88%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2023-08-27   | 2023-12-04 | 179,92%          | UPPER_P90   | True          | 0,02%                   | 0,11%                   | 17,66%                  | 4,47%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | INJ-USD         | 2023-08-26   | 2023-12-03 | 112,10%          | UPPER_P90   | True          | 0,02%                   | 0,11%                   | 17,66%                  | 2,73%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | CENTRAL     | True          | 0,02%                   | 0,11%                   | 13,95%                  | 1,40%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -1,00%                  | -0,11%                  | -1,85%                  | -1,12%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-08-06   | 2018-11-13 | -51,13%          | LOWER_P10   | False         | -1,00%                  | -0,11%                  | -1,85%                  | -1,46%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2022-11-15   | 2023-02-22 | -26,39%          | LOWER_P10   | False         | -1,00%                  | -0,11%                  | -1,85%                  | -0,82%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DASH-USD        | 2019-11-13   | 2020-02-20 | -32,46%          | LOWER_P10   | False         | -1,00%                  | -0,11%                  | -1,85%                  | -0,98%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,90%                   | 2,52%                   | 16,39%                  | 6,98%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -5,68%                  | -2,52%                  | -4,15%                  | -3,24%                   |
