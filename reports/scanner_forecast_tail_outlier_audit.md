# Scanner forecast tail / outlier audit

Generato: 2026-10-14 05:32:25 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           0 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 85.942,23 $   | 88.733,66 $        | 101.871,32 $  | 114.235,01 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     3 |                           4 |                        13 |                     13 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 116,47 $      | 113,03 $           | 139,73 $      | 145,52 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           2 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09659 $     | 0.09009 $          | 0.11487 $     | 0.12389 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,41%                   | 0,17%                   | 0,79%                   | 2,39%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | False         | 0,41%                   | 0,17%                   | 0,79%                   | 1,09%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-01   | 2023-03-10 | 40,35%           | UPPER_P90   | False         | 0,41%                   | 0,17%                   | 0,79%                   | 0,97%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -0,75%                  | -0,17%                  | -0,16%                  | -0,88%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | False         | -0,75%                  | -0,17%                  | -0,16%                  | -0,86%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | CRV-USD         | 2023-09-17   | 2023-12-25 | -30,57%          | LOWER_P10   | False         | -0,75%                  | -0,17%                  | -0,16%                  | -0,85%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ENJ-USD         | 2022-12-02   | 2023-03-11 | 23,45%           | UPPER_P90   | False         | 0,41%                   | 0,17%                   | 0,79%                   | 0,54%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2023-09-18   | 2023-12-26 | -25,10%          | LOWER_P10   | False         | -0,75%                  | -0,17%                  | -0,16%                  | -0,70%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,67%                   | 0,28%                   | 26,31%                  | 11,40%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-22   | 2021-03-01 | -6,75%           | LOWER_P10   | False         | -3,69%                  | -0,28%                  | -8,38%                  | -3,20%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,28%                   | 0,27%                   | 1,58%                   | 2,19%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-01   | 2023-03-10 | 40,35%           | UPPER_P90   | False         | 0,28%                   | 0,27%                   | 1,58%                   | 0,78%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | False         | 0,28%                   | 0,27%                   | 1,58%                   | 0,90%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BNB-USD         | 2025-05-30   | 2025-09-06 | 41,98%           | UPPER_P90   | False         | 0,28%                   | 0,27%                   | 1,58%                   | 0,82%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -1,45%                  | -0,27%                  | -1,14%                  | -0,65%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | True          | -1,45%                  | -0,27%                  | -1,14%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | True          | -1,45%                  | -0,27%                  | -1,14%                  | -1,02%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | True          | -1,45%                  | -0,27%                  | -1,14%                  | -1,07%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,21%                   | 1,27%                   | 25,94%                  | 7,04%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2025-05-30   | 2025-09-06 | 41,98%           | UPPER_P90   | True          | 0,21%                   | 1,27%                   | 25,94%                  | 2,59%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -1,92%                  | -0,34%                  | -3,23%                  | -2,19%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | SNX-USD         | 2020-11-17   | 2021-02-24 | -8,87%           | LOWER_P10   | False         | -1,92%                  | -0,34%                  | -3,23%                  | -1,65%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-01   | 2023-03-10 | 40,35%           | UPPER_P90   | False         | 0,48%                   | 0,30%                   | 3,72%                   | 0,65%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,48%                   | 0,30%                   | 3,72%                   | 2,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,48%                   | 0,30%                   | 3,72%                   | 0,99%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOT-USD         | 2021-06-20   | 2021-09-27 | 45,51%           | UPPER_P90   | False         | 0,48%                   | 0,30%                   | 3,72%                   | 0,78%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -1,31%                  | -0,30%                  | -0,54%                  | -0,74%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-18   | 2026-05-28 | -25,56%          | LOWER_P10   | True          | -1,31%                  | -0,30%                  | -0,54%                  | -1,04%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | True          | -1,31%                  | -0,30%                  | -0,54%                  | -1,16%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2019-01-03   | 2019-04-12 | -12,60%          | LOWER_P10   | False         | -1,31%                  | -0,30%                  | -0,54%                  | -0,71%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,70%                   | 0,28%                   | 30,87%                  | 11,42%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -7,79%                  | -0,28%                  | -7,05%                  | -4,18%                   |
