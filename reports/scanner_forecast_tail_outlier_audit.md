# Scanner forecast tail / outlier audit

Generato: 2026-10-15 05:32:57 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           0 |                         6 |                      6 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 84.647,98 $   | 86.046,41 $        | 105.608,34 $  | 123.561,49 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                        13 |                     13 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 112,85 $      | 108,30 $           | 138,62 $      | 139,61 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           3 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09110 $     | 0.08478 $          | 0.10697 $     | 0.11658 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-02   | 2023-03-11 | 43,72%           | UPPER_P90   | False         | 0,05%                   | 1,44%                   | 5,85%                   | 1,01%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,05%                   | 1,44%                   | 5,85%                   | 2,33%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | False         | 0,05%                   | 1,44%                   | 5,85%                   | 1,26%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-04-21   | 2020-07-29 | 79,49%           | UPPER_P90   | True          | 0,05%                   | 1,44%                   | 5,85%                   | 1,92%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -1,51%                  | -1,44%                  | -1,48%                  | -0,93%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-18   | 2026-05-28 | -25,56%          | LOWER_P10   | False         | -1,51%                  | -1,44%                  | -1,48%                  | -0,77%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | False         | -1,51%                  | -1,44%                  | -1,48%                  | -0,92%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2019-04-02   | 2019-07-10 | -27,42%          | LOWER_P10   | False         | -1,51%                  | -1,44%                  | -1,48%                  | -0,82%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,67%                   | 0,28%                   | 44,14%                  | 15,40%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-22   | 2021-03-01 | -6,75%           | LOWER_P10   | False         | -5,75%                  | -0,28%                  | -8,58%                  | -5,04%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-02   | 2023-03-11 | 43,72%           | UPPER_P90   | False         | 0,15%                   | 0,74%                   | 5,51%                   | 0,80%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,15%                   | 0,74%                   | 5,51%                   | 1,05%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,15%                   | 0,74%                   | 5,51%                   | 2,13%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BNB-USD         | 2025-05-30   | 2025-09-06 | 41,98%           | UPPER_P90   | False         | 0,15%                   | 0,74%                   | 5,51%                   | 0,76%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2019-01-03   | 2019-04-12 | -12,60%          | LOWER_P10   | False         | -2,83%                  | -0,74%                  | -0,71%                  | -0,64%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | True          | -2,83%                  | -0,74%                  | -0,71%                  | -1,09%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SNX-USD         | 2020-11-22   | 2021-03-01 | -14,46%          | LOWER_P10   | False         | -2,83%                  | -0,74%                  | -0,71%                  | -0,69%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -2,83%                  | -0,74%                  | -0,71%                  | -0,71%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,77%                   | 0,34%                   | 22,10%                  | 6,95%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2025-05-30   | 2025-09-06 | 41,98%           | UPPER_P90   | True          | 0,77%                   | 0,34%                   | 22,10%                  | 2,50%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | SNX-USD         | 2020-11-22   | 2021-03-01 | -14,46%          | LOWER_P10   | True          | -6,98%                  | -0,28%                  | -2,70%                  | -2,21%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | True          | -6,98%                  | -0,28%                  | -2,70%                  | -2,28%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-02   | 2023-03-11 | 43,72%           | UPPER_P90   | False         | 0,10%                   | 0,05%                   | 2,50%                   | 0,76%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,10%                   | 0,05%                   | 2,50%                   | 1,01%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BAT-USD         | 2022-12-02   | 2023-03-11 | 34,91%           | UPPER_P90   | False         | 0,10%                   | 0,05%                   | 2,50%                   | 0,53%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,10%                   | 0,05%                   | 2,50%                   | 2,08%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -1,45%                  | -0,05%                  | -0,10%                  | -0,72%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-18   | 2026-05-28 | -25,56%          | LOWER_P10   | True          | -1,45%                  | -0,05%                  | -0,10%                  | -1,02%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | True          | -1,45%                  | -0,05%                  | -0,10%                  | -1,13%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | QTUM-USD        | 2023-09-13   | 2023-12-21 | -7,79%           | LOWER_P10   | False         | -1,45%                  | -0,05%                  | -0,10%                  | -0,56%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,70%                   | 0,28%                   | 30,87%                  | 11,56%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -3,11%                  | -0,28%                  | -7,05%                  | -4,04%                   |
