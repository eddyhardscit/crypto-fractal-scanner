# Scanner forecast tail / outlier audit

Generato: 2026-10-20 05:32:59 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           1 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 83.236,06 $   | 81.018,41 $        | 109.849,68 $  | 134.118,57 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     3 |                           3 |                        13 |                     13 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 109,33 $      | 105,53 $           | 139,39 $      | 146,49 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08825 $     | 0.08165 $          | 0.10377 $     | 0.16711 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,15%                   | 0,68%                   | 3,46%                   | 5,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | False         | 0,15%                   | 0,68%                   | 3,46%                   | 1,33%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | False         | 0,15%                   | 0,68%                   | 3,46%                   | 1,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-04-26   | 2020-08-03 | 78,11%           | UPPER_P90   | True          | 0,15%                   | 0,68%                   | 3,46%                   | 1,69%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -1,62%                  | -0,68%                  | -2,16%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MANA-USD        | 2023-09-18   | 2023-12-26 | -22,50%          | LOWER_P10   | False         | -1,62%                  | -0,68%                  | -2,16%                  | -0,89%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -1,62%                  | -0,68%                  | -2,16%                  | -1,07%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2023-09-23   | 2023-12-31 | -20,26%          | LOWER_P10   | False         | -1,62%                  | -0,68%                  | -2,16%                  | -0,83%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,03%                   | 0,99%                   | 53,58%                  | 23,94%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -9,43%                  | -0,97%                  | -18,21%                 | -5,95%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-28   | 2020-03-06 | -33,50%          | LOWER_P10   | False         | -8,08%                  | -1,03%                  | -1,25%                  | -1,16%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -8,08%                  | -1,03%                  | -1,25%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -8,08%                  | -1,03%                  | -1,25%                  | -1,05%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | True          | -8,08%                  | -1,03%                  | -1,25%                  | -1,27%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,37%                   | 1,03%                   | 4,84%                   | 5,07%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,37%                   | 1,03%                   | 4,84%                   | 1,34%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,37%                   | 1,03%                   | 4,84%                   | 2,12%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 0,37%                   | 1,03%                   | 4,84%                   | 0,84%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 1,34%                   | 1,83%                   | 19,17%                  | 16,15%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 1,34%                   | 1,83%                   | 19,17%                  | 2,41%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -10,92%                 | -0,99%                  | -2,24%                  | -3,77%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -10,92%                 | -0,99%                  | -2,24%                  | -3,75%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | True          | -7,09%                  | -0,02%                  | -1,54%                  | -1,15%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | True          | -7,09%                  | -0,02%                  | -1,54%                  | -1,37%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2021-09-13   | 2021-12-21 | -26,36%          | LOWER_P10   | False         | -7,09%                  | -0,02%                  | -1,54%                  | -1,08%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-28   | 2020-03-06 | -33,50%          | LOWER_P10   | True          | -7,09%                  | -0,02%                  | -1,54%                  | -1,26%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 1,31%                   | 0,02%                   | 2,87%                   | 4,97%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 1,31%                   | 0,02%                   | 2,87%                   | 1,24%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 1,31%                   | 0,02%                   | 2,87%                   | 2,02%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 1,31%                   | 0,02%                   | 2,87%                   | 0,74%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 2,33%                   | 0,99%                   | 77,19%                  | 29,09%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -12,76%                 | -9,62%                  | -16,49%                 | -10,70%                  |
