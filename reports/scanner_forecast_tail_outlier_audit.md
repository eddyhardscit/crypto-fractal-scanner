# Scanner forecast tail / outlier audit

Generato: 2026-10-19 05:32:58 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 83.990,66 $   | 81.752,90 $        | 109.220,34 $  | 126.999,80 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     3 |                           4 |                        13 |                     13 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 108,97 $      | 106,55 $           | 142,59 $      | 147,91 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           0 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08832 $     | 0.08172 $          | 0.10726 $     | 0.16724 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,09%                   | 0,68%                   | 1,50%                   | 5,07%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,09%                   | 0,68%                   | 1,50%                   | 1,34%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,09%                   | 0,68%                   | 1,50%                   | 1,08%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-20   | 2021-09-27 | 33,95%           | UPPER_P90   | False         | 0,09%                   | 0,68%                   | 1,50%                   | 0,57%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -0,62%                  | -0,68%                  | -0,20%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -0,62%                  | -0,68%                  | -0,20%                  | -1,05%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MANA-USD        | 2023-09-18   | 2023-12-26 | -22,50%          | LOWER_P10   | False         | -0,62%                  | -0,68%                  | -0,20%                  | -0,88%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-22   | 2023-12-30 | -17,48%          | LOWER_P10   | False         | -0,62%                  | -0,68%                  | -0,20%                  | -0,75%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,03%                   | 0,99%                   | 47,28%                  | 24,11%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -9,43%                  | -0,97%                  | -19,47%                 | -5,77%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,03%                   | 0,32%                   | 5,09%                   | 5,15%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,03%                   | 0,32%                   | 5,09%                   | 1,42%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,03%                   | 0,32%                   | 5,09%                   | 1,15%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 0,03%                   | 0,32%                   | 5,09%                   | 0,92%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-28   | 2020-03-06 | -33,50%          | LOWER_P10   | False         | -3,99%                  | -0,32%                  | -1,06%                  | -1,08%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -3,99%                  | -0,32%                  | -1,06%                  | -0,98%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | False         | -3,99%                  | -0,32%                  | -1,06%                  | -1,19%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2019-11-28   | 2020-03-06 | -42,86%          | LOWER_P10   | True          | -3,99%                  | -0,32%                  | -1,06%                  | -1,32%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 1,34%                   | 1,96%                   | 19,17%                  | 16,22%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 1,34%                   | 1,96%                   | 19,17%                  | 2,48%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -10,85%                 | -0,99%                  | -2,24%                  | -3,70%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -10,85%                 | -0,99%                  | -2,24%                  | -3,67%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,30%                   | 0,02%                   | 4,88%                   | 4,93%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,30%                   | 0,02%                   | 4,88%                   | 1,20%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,30%                   | 0,02%                   | 4,88%                   | 1,98%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 0,30%                   | 0,02%                   | 4,88%                   | 0,70%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | True          | -0,42%                  | -0,02%                  | -1,06%                  | -1,41%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2019-11-27   | 2020-03-05 | -24,36%          | LOWER_P10   | False         | -0,42%                  | -0,02%                  | -1,06%                  | -1,07%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-30   | 2019-12-07 | -6,00%           | LOWER_P10   | False         | -0,42%                  | -0,02%                  | -1,06%                  | -0,60%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | FIL-USD         | 2021-06-24   | 2021-10-01 | -9,94%           | LOWER_P10   | False         | -0,42%                  | -0,02%                  | -1,06%                  | -0,70%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,30%                   | 0,99%                   | 77,19%                  | 28,46%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-30   | 2019-12-07 | -6,00%           | LOWER_P10   | False         | -3,14%                  | -9,62%                  | -16,49%                 | -7,45%                   |
