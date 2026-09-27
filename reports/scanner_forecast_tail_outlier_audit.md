# Scanner forecast tail / outlier audit

Generato: 2026-09-27 05:31:53 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           2 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.425,31 $   | 86.769,82 $        | 113.771,42 $  | 98.585,09 $        |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           2 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 114,74 $      | 130,31 $           | 187,37 $      | 161,79 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08888 $     | 0.09863 $          | 0.15102 $     | 0.10789 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2022-11-15   | 2023-02-22 | -26,39%          | LOWER_P10   | False         | -5,55%                  | -1,05%                  | -0,38%                  | -0,76%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -5,55%                  | -1,05%                  | -0,38%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | CRV-USD         | 2023-09-02   | 2023-12-10 | -27,54%          | LOWER_P10   | False         | -5,55%                  | -1,05%                  | -0,38%                  | -0,79%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOGE-USD        | 2018-07-01   | 2018-10-08 | -34,80%          | LOWER_P10   | False         | -5,55%                  | -1,05%                  | -0,38%                  | -0,98%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | INJ-USD         | 2023-08-26   | 2023-12-03 | 112,10%          | UPPER_P90   | True          | 0,31%                   | 1,05%                   | 1,31%                   | 2,79%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-14   | 2020-12-22 | 78,89%           | UPPER_P90   | True          | 0,31%                   | 1,05%                   | 1,31%                   | 1,94%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2023-08-26   | 2023-12-03 | 54,44%           | UPPER_P90   | True          | 0,31%                   | 1,05%                   | 1,31%                   | 1,31%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LTC-USD         | 2018-12-05   | 2019-03-14 | 38,24%           | UPPER_P90   | False         | 0,31%                   | 1,05%                   | 1,31%                   | 0,89%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ETC-USD         | 2023-09-03   | 2023-12-11 | 30,13%           | UPPER_P90   | True          | 0,45%                   | 2,47%                   | 10,22%                  | 4,61%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ETH-USD         | 2019-03-13   | 2019-06-20 | -15,67%          | LOWER_P10   | False         | -6,33%                  | -1,22%                  | -2,21%                  | -3,02%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2020-11-14   | 2021-02-21 | 121,56%          | UPPER_P90   | True          | 0,25%                   | 2,82%                   | 4,42%                   | 2,94%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | OP-USD          | 2023-09-04   | 2023-12-12 | 70,44%           | UPPER_P90   | True          | 0,25%                   | 2,82%                   | 4,42%                   | 1,63%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SOL-USD         | 2020-11-05   | 2021-02-12 | 56,90%           | UPPER_P90   | False         | 0,25%                   | 2,82%                   | 4,42%                   | 1,28%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-04-07   | 2020-07-15 | 135,41%          | UPPER_P90   | True          | 0,25%                   | 2,82%                   | 4,42%                   | 3,30%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-19   | 2019-03-28 | -28,88%          | LOWER_P10   | False         | -1,88%                  | -2,82%                  | -0,18%                  | -0,92%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2024-05-10   | 2024-08-17 | -33,18%          | LOWER_P10   | False         | -1,88%                  | -2,82%                  | -0,18%                  | -1,03%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -1,88%                  | -2,82%                  | -0,18%                  | -1,15%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XRP-USD         | 2021-01-31   | 2021-05-10 | -33,76%          | LOWER_P10   | False         | -1,88%                  | -2,82%                  | -0,18%                  | -1,04%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-03-13   | 2019-06-20 | 49,79%           | UPPER_P90   | True          | 0,90%                   | 1,36%                   | 11,83%                  | 4,63%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -5,35%                  | -2,56%                  | -1,97%                  | -2,99%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | FIL-USD         | 2020-12-11   | 2021-03-20 | 87,82%           | UPPER_P90   | True          | 0,21%                   | 1,17%                   | 19,81%                  | 2,19%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-14   | 2020-12-22 | 78,89%           | UPPER_P90   | True          | 0,21%                   | 1,17%                   | 19,81%                  | 1,97%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOGE-USD        | 2020-09-18   | 2020-12-26 | 86,54%           | UPPER_P90   | True          | 0,21%                   | 1,17%                   | 19,81%                  | 2,16%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2023-08-27   | 2023-12-04 | 179,92%          | UPPER_P90   | True          | 0,21%                   | 1,17%                   | 19,81%                  | 4,56%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-13   | 2020-02-20 | -49,38%          | LOWER_P10   | False         | -2,63%                  | -1,17%                  | -2,38%                  | -1,32%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2019-11-13   | 2020-02-20 | -45,99%          | LOWER_P10   | False         | -2,63%                  | -1,17%                  | -2,38%                  | -1,24%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-08-06   | 2018-11-13 | -51,13%          | LOWER_P10   | False         | -2,63%                  | -1,17%                  | -2,38%                  | -1,37%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EOS-USD         | 2019-11-13   | 2020-02-20 | -43,18%          | LOWER_P10   | False         | -2,63%                  | -1,17%                  | -2,38%                  | -1,16%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | DOT-USD         | 2023-09-03   | 2023-12-11 | 18,85%           | UPPER_P90   | True          | 0,90%                   | 2,47%                   | 9,58%                   | 4,14%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | True          | -6,91%                  | -0,06%                  | -1,59%                  | -3,36%                   |
