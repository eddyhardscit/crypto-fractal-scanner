# Scanner forecast tail / outlier audit

Generato: 2026-10-23 05:33:01 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_BTC_REGIME         |                     1 |                           2 |                        10 |                     10 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 87.166,05 $   | 75.137,50 $        | 106.919,15 $  | 126.764,13 $       |
| SOL     | AVAILABLE                   | SAME_BTC_REGIME         |                     3 |                           3 |                        14 |                     14 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 107,75 $      | 103,10 $           | 145,50 $      | 148,79 $           |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         4 |                      0 |                  5 | NONE                | INSUFFICIENT_REGIME_MATCHES | 0.08635 $     | n/a                | 0.11498 $     | n/a                |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,14%                   | 0,47%                   | 1,98%                   | 5,04%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,14%                   | 0,47%                   | 1,98%                   | 2,26%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,14%                   | 0,47%                   | 1,98%                   | 2,08%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XLM-USD         | 2020-12-02   | 2021-03-11 | 38,42%           | UPPER_P90   | False         | 0,14%                   | 0,47%                   | 1,98%                   | 0,65%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -1,57%                  | -0,47%                  | -0,80%                  | -1,09%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2020-04-28   | 2020-08-05 | -23,47%          | LOWER_P10   | False         | -1,57%                  | -0,47%                  | -0,80%                  | -0,94%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2025-06-06   | 2025-09-13 | -21,68%          | LOWER_P10   | False         | -1,57%                  | -0,47%                  | -0,80%                  | -0,89%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -1,57%                  | -0,47%                  | -0,80%                  | -1,09%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,03%                   | 8,11%                   | 45,55%                  | 21,75%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -6,13%                  | -8,11%                  | -17,10%                 | -4,82%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | XLM-USD         | 2020-12-02   | 2021-03-11 | 38,42%           | CENTRAL     | True          | 0,03%                   | 8,11%                   | 11,35%                  | 2,75%                    |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,07%                   | 0,15%                   | 9,93%                   | 2,19%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,07%                   | 0,15%                   | 9,93%                   | 2,02%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 0,07%                   | 0,15%                   | 9,93%                   | 0,74%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,07%                   | 0,15%                   | 9,93%                   | 7,50%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2019-12-03   | 2020-03-11 | -22,41%          | LOWER_P10   | False         | -4,68%                  | -0,15%                  | -0,53%                  | -0,97%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -4,68%                  | -0,15%                  | -0,53%                  | -1,15%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2020-04-28   | 2020-08-05 | -23,47%          | LOWER_P10   | False         | -4,68%                  | -0,15%                  | -0,53%                  | -1,00%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -4,68%                  | -0,15%                  | -0,53%                  | -1,16%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,76%                   | 1,83%                   | 7,12%                   | 21,95%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 0,76%                   | 1,83%                   | 7,12%                   | 1,68%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -6,49%                  | -1,83%                  | -0,53%                  | -4,00%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -6,49%                  | -1,83%                  | -0,53%                  | -4,02%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,90%                   | 0,13%                   | 2,55%                   | 7,39%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,90%                   | 0,13%                   | 2,55%                   | 2,09%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,90%                   | 0,13%                   | 2,55%                   | 1,91%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-03-22   | 2020-06-29 | 46,00%           | UPPER_P90   | False         | 0,90%                   | 0,13%                   | 2,55%                   | 0,67%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ONE-USD         | 2019-12-03   | 2020-03-11 | -25,69%          | LOWER_P10   | False         | -1,69%                  | -0,13%                  | -0,17%                  | -1,16%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEO-USD         | 2019-12-03   | 2020-03-11 | -22,41%          | LOWER_P10   | False         | -1,69%                  | -0,13%                  | -0,17%                  | -1,08%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-07-26   | 2018-11-02 | -40,47%          | LOWER_P10   | False         | -1,69%                  | -0,13%                  | -0,17%                  | -1,54%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2025-06-06   | 2025-09-13 | -21,68%          | LOWER_P10   | False         | -1,69%                  | -0,13%                  | -0,17%                  | -1,06%                   |
