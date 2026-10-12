# Scanner forecast tail / outlier audit

Generato: 2026-10-12 05:32:24 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                         6 |                      6 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.897,22 $   | 86.547,74 $        | 102.714,69 $  | 105.761,59 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     3 |                           4 |                        14 |                     14 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 115,71 $      | 116,53 $           | 144,83 $      | 148,53 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           2 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09332 $     | 0.09104 $          | 0.10677 $     | 0.09441 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-29   | 2023-03-08 | 28,58%           | UPPER_P90   | False         | 0,52%                   | 0,15%                   | 5,76%                   | 0,77%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,52%                   | 0,15%                   | 5,76%                   | 1,08%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,52%                   | 0,15%                   | 5,76%                   | 1,19%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,52%                   | 0,15%                   | 5,76%                   | 0,98%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -2,20%                  | -0,15%                  | -0,68%                  | -0,78%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | CRV-USD         | 2023-09-17   | 2023-12-25 | -30,57%          | LOWER_P10   | False         | -2,20%                  | -0,15%                  | -0,68%                  | -0,74%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-29   | 2019-04-07 | -27,90%          | LOWER_P10   | False         | -2,20%                  | -0,15%                  | -0,68%                  | -0,67%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | False         | -2,20%                  | -0,15%                  | -0,68%                  | -0,76%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,76%                   | 2,35%                   | 16,92%                  | 6,72%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | False         | -5,95%                  | -2,35%                  | -2,90%                  | -3,83%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,24%                   | 0,31%                   | 5,47%                   | 1,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,24%                   | 0,31%                   | 5,47%                   | 0,95%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-15   | 2021-09-22 | 28,99%           | UPPER_P90   | False         | 0,24%                   | 0,31%                   | 5,47%                   | 0,65%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BNB-USD         | 2025-05-30   | 2025-09-06 | 41,98%           | UPPER_P90   | True          | 0,24%                   | 0,31%                   | 5,47%                   | 0,98%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2023-09-18   | 2023-12-26 | -20,59%          | LOWER_P10   | False         | -2,96%                  | -0,31%                  | -0,04%                  | -0,62%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | False         | -2,96%                  | -0,31%                  | -0,04%                  | -0,90%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -2,96%                  | -0,31%                  | -0,04%                  | -0,91%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2023-09-13   | 2023-12-21 | -19,53%          | LOWER_P10   | False         | -2,96%                  | -0,31%                  | -0,04%                  | -0,60%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,05%                   | 2,07%                   | 20,59%                  | 2,63%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2025-05-30   | 2025-09-06 | 41,98%           | UPPER_P90   | True          | 0,05%                   | 2,07%                   | 20,59%                  | 2,73%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ZEC-USD         | 2024-05-25   | 2024-09-01 | -9,36%           | LOWER_P10   | False         | -1,20%                  | -2,07%                  | -2,90%                  | -1,22%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | False         | -1,20%                  | -2,07%                  | -2,90%                  | -1,43%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-13   | 2026-05-23 | -22,03%          | LOWER_P10   | False         | -4,46%                  | -0,37%                  | -0,16%                  | -0,66%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | True          | -4,46%                  | -0,37%                  | -0,16%                  | -0,89%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2019-11-23   | 2020-03-01 | -40,18%          | LOWER_P10   | True          | -4,46%                  | -0,37%                  | -0,16%                  | -1,12%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | True          | -4,46%                  | -0,37%                  | -0,16%                  | -0,86%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,12%                   | 0,37%                   | 0,79%                   | 1,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-29   | 2023-03-08 | 28,58%           | UPPER_P90   | False         | 0,12%                   | 0,37%                   | 0,79%                   | 0,64%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-15   | 2021-09-22 | 28,99%           | UPPER_P90   | False         | 0,12%                   | 0,37%                   | 0,79%                   | 0,65%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ENJ-USD         | 2022-12-02   | 2023-03-11 | 23,45%           | UPPER_P90   | False         | 0,12%                   | 0,37%                   | 0,79%                   | 0,51%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -2,64%                  | -1,27%                  | -0,54%                  | -2,10%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | XLM-USD         | 2025-05-25   | 2025-09-01 | 11,63%           | UPPER_P90   | False         | 0,32%                   | 1,27%                   | 2,02%                   | 1,76%                    |
