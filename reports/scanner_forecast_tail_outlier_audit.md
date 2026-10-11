# Scanner forecast tail / outlier audit

Generato: 2026-10-11 05:32:20 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.272,95 $   | 83.681,17 $        | 102.916,66 $  | 102.239,83 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           1 |                        11 |                     11 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 112,57 $      | 115,62 $           | 132,95 $      | 132,90 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09103 $     | 0.09009 $          | 0.10791 $     | 0.10022 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-28   | 2023-03-07 | 26,21%           | UPPER_P90   | False         | 0,41%                   | 0,14%                   | 1,83%                   | 0,65%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,41%                   | 0,14%                   | 1,83%                   | 1,01%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,41%                   | 0,14%                   | 1,83%                   | 1,13%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,41%                   | 0,14%                   | 1,83%                   | 0,91%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2023-09-13   | 2023-12-21 | -19,53%          | LOWER_P10   | False         | -1,55%                  | -0,14%                  | -0,24%                  | -0,53%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2019-03-28   | 2019-07-05 | -22,68%          | LOWER_P10   | False         | -1,55%                  | -0,14%                  | -0,24%                  | -0,61%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-29   | 2019-04-07 | -27,90%          | LOWER_P10   | False         | -1,55%                  | -0,14%                  | -0,24%                  | -0,74%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZIL-USD         | 2023-09-15   | 2023-12-23 | -20,40%          | LOWER_P10   | False         | -1,55%                  | -0,14%                  | -0,24%                  | -0,55%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,76%                   | 1,09%                   | 14,63%                  | 5,80%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | False         | -4,65%                  | -2,35%                  | -2,90%                  | -2,99%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-28   | 2023-03-07 | 26,21%           | UPPER_P90   | False         | 0,17%                   | 0,31%                   | 5,97%                   | 0,59%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,17%                   | 0,31%                   | 5,97%                   | 0,96%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,17%                   | 0,31%                   | 5,97%                   | 1,07%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2022-11-27   | 2023-03-06 | 21,80%           | UPPER_P90   | False         | 0,17%                   | 0,31%                   | 5,97%                   | 0,48%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2023-09-18   | 2023-12-26 | -20,59%          | LOWER_P10   | False         | -1,07%                  | -0,31%                  | -0,05%                  | -0,61%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-13   | 2023-12-21 | -15,42%          | LOWER_P10   | False         | -1,07%                  | -0,31%                  | -0,05%                  | -0,47%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -1,07%                  | -0,31%                  | -0,05%                  | -0,89%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2023-09-13   | 2023-12-21 | -19,53%          | LOWER_P10   | False         | -1,07%                  | -0,31%                  | -0,05%                  | -0,58%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,28%                   | 2,35%                   | 10,13%                  | 3,51%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2025-05-25   | 2025-09-01 | 21,32%           | UPPER_P90   | False         | 0,28%                   | 2,35%                   | 8,20%                   | 1,58%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ZEC-USD         | 2024-05-25   | 2024-09-01 | -9,36%           | LOWER_P10   | False         | -0,16%                  | -0,34%                  | -1,93%                  | -1,49%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | False         | -0,43%                  | -0,34%                  | -1,93%                  | -1,77%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,11%                   | 0,43%                   | 3,75%                   | 0,99%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-15   | 2021-09-22 | 28,99%           | UPPER_P90   | False         | 0,11%                   | 0,43%                   | 3,75%                   | 0,58%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,11%                   | 0,43%                   | 3,75%                   | 0,88%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | QTUM-USD        | 2022-12-02   | 2023-03-11 | 28,44%           | UPPER_P90   | False         | 0,11%                   | 0,43%                   | 3,75%                   | 0,57%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-18   | 2020-02-25 | -35,92%          | LOWER_P10   | True          | -0,47%                  | -0,43%                  | -0,22%                  | -1,08%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-13   | 2026-05-23 | -22,03%          | LOWER_P10   | False         | -0,47%                  | -0,43%                  | -0,22%                  | -0,72%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -0,47%                  | -0,43%                  | -0,22%                  | -0,55%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2023-09-13   | 2023-12-21 | -13,73%          | LOWER_P10   | False         | -0,47%                  | -0,43%                  | -0,22%                  | -0,51%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,32%                   | 2,55%                   | 6,88%                   | 4,55%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -2,60%                  | -0,34%                  | -2,90%                  | -2,44%                   |
