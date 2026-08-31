# Scanner forecast tail / outlier audit

Generato: 2026-08-31 05:32:03 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           2 |                         3 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 81.493,09 $   | n/a                | 112.013,52 $  | n/a                |
| SOL     | AVAILABLE                   | SAME_BTC_REGIME         |                     1 |                           2 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK   | FALLBACK_TO_SAME_BTC_REGIME   | 107,27 $      | 174,49 $           | 207,27 $      | 225,31 $           |
| DOGE    | AVAILABLE                   | SAME_ASSET_REGIME       |                     1 |                          11 |                         2 |                     11 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07906 $     | 0.07177 $          | 0.11789 $     | 0.10932 $          |

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-11-08   | 2020-02-15 | -43,47%          | LOWER_P10   | True          | -14,12%                 | -0,05%                  | -0,19%                  | -1,34%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ETC-USD         | 2021-12-22   | 2022-03-31 | -45,17%          | LOWER_P10   | True          | -14,12%                 | -0,05%                  | -0,19%                  | -1,38%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2019-11-08   | 2020-02-15 | -45,65%          | LOWER_P10   | True          | -14,12%                 | -0,05%                  | -0,19%                  | -1,40%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BNB-USD         | 2019-11-08   | 2020-02-15 | -61,13%          | LOWER_P10   | True          | -14,12%                 | -0,05%                  | -0,19%                  | -1,79%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2023-08-05   | 2023-11-12 | 98,61%           | UPPER_P90   | True          | 1,31%                   | 0,05%                   | 0,30%                   | 2,30%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BNB-USD         | 2018-11-08   | 2019-02-15 | 69,95%           | UPPER_P90   | True          | 1,31%                   | 0,05%                   | 0,30%                   | 1,57%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EGLD-USD        | 2023-08-04   | 2023-11-11 | 45,30%           | UPPER_P90   | False         | 1,31%                   | 0,05%                   | 0,30%                   | 0,93%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ALGO-USD        | 2023-08-03   | 2023-11-10 | 57,16%           | UPPER_P90   | True          | 1,31%                   | 0,05%                   | 0,30%                   | 1,24%                    |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | FTM-USD         | 2020-10-18   | 2021-01-25 | 1.143,11%        | UPPER_P90   | True          | 0,08%                   | 0,05%                   | 12,31%                  | 28,00%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZIL-USD         | 2020-08-21   | 2020-11-28 | 235,51%          | UPPER_P90   | True          | 0,08%                   | 0,05%                   | 12,31%                  | 4,73%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-03-03   | 2020-06-10 | 133,50%          | UPPER_P90   | True          | 0,08%                   | 0,05%                   | 12,31%                  | 2,11%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2020-10-13   | 2021-01-20 | 156,87%          | UPPER_P90   | True          | 0,08%                   | 0,05%                   | 12,31%                  | 2,71%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XRP-USD         | 2020-08-24   | 2020-12-01 | -64,13%          | LOWER_P10   | False         | -1,69%                  | -0,05%                  | -3,51%                  | -2,96%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MANA-USD        | 2019-11-08   | 2020-02-15 | -61,35%          | LOWER_P10   | False         | -1,69%                  | -0,05%                  | -3,51%                  | -2,89%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2026-01-26   | 2026-05-05 | -33,21%          | LOWER_P10   | False         | -1,69%                  | -0,05%                  | -3,51%                  | -2,16%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | WAVES-USD       | 2019-11-08   | 2020-02-15 | -49,74%          | LOWER_P10   | False         | -1,69%                  | -0,05%                  | -3,51%                  | -2,59%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2020-03-03   | 2020-06-10 | -32,40%          | LOWER_P10   | False         | -41,76%                 | -14,21%                 | -3,51%                  | -21,79%                  |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2020-03-03   | 2020-06-10 | 133,50%          | UPPER_P90   | False         | 3,68%                   | 32,76%                  | 29,61%                  | 19,68%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2021-05-07   | 2021-08-14 | 193,95%          | UPPER_P90   | True          | 0,76%                   | 0,51%                   | 8,63%                   | 4,79%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | CHZ-USD         | 2020-08-23   | 2020-11-30 | 90,11%           | UPPER_P90   | True          | 0,76%                   | 0,51%                   | 8,63%                   | 2,13%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZEC-USD         | 2026-01-05   | 2026-04-14 | 58,15%           | UPPER_P90   | False         | 0,76%                   | 0,51%                   | 8,63%                   | 1,31%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | EGLD-USD        | 2021-05-06   | 2021-08-13 | 92,46%           | UPPER_P90   | True          | 0,76%                   | 0,51%                   | 8,63%                   | 2,19%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | FIL-USD         | 2022-04-30   | 2022-08-07 | -36,15%          | LOWER_P10   | False         | -1,65%                  | -0,51%                  | -1,76%                  | -1,11%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | SOL-USD         | 2021-12-25   | 2022-04-03 | -37,24%          | LOWER_P10   | False         | -1,65%                  | -0,51%                  | -1,76%                  | -1,14%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | KSM-USD         | 2021-12-25   | 2022-04-03 | -36,71%          | LOWER_P10   | False         | -1,65%                  | -0,51%                  | -1,76%                  | -1,12%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LRC-USD         | 2021-12-22   | 2022-03-31 | -41,29%          | LOWER_P10   | False         | -1,65%                  | -0,51%                  | -1,76%                  | -1,24%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | EGLD-USD        | 2023-07-25   | 2023-11-01 | 40,51%           | UPPER_P90   | False         | 0,06%                   | 5,50%                   | 10,04%                  | 4,70%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | EOS-USD         | 2022-04-26   | 2022-08-03 | 31,93%           | UPPER_P90   | False         | 0,06%                   | 5,50%                   | 9,18%                   | 3,84%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | KSM-USD         | 2021-12-25   | 2022-04-03 | -36,71%          | LOWER_P10   | False         | -6,83%                  | -3,89%                  | -0,86%                  | -3,02%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | FIL-USD         | 2022-04-30   | 2022-08-07 | -36,15%          | LOWER_P10   | False         | -6,77%                  | -3,89%                  | -0,86%                  | -2,97%                   |
