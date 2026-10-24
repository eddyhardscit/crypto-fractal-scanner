# Scanner forecast tail / outlier audit

Generato: 2026-10-24 05:32:57 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_BTC_REGIME         |                     2 |                           3 |                        10 |                     10 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 83.362,74 $   | 74.792,77 $        | 105.805,03 $  | 133.395,34 $       |
| SOL     | AVAILABLE                   | SAME_BTC_REGIME         |                     4 |                           4 |                        11 |                     11 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 104,73 $      | 99,33 $            | 132,01 $      | 147,66 $           |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         4 |                      0 |                  5 | NONE                | INSUFFICIENT_REGIME_MATCHES | 0.08402 $     | n/a                | 0.10959 $     | n/a                |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,04%                   | 0,45%                   | 3,09%                   | 7,52%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,04%                   | 0,45%                   | 3,09%                   | 2,21%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,04%                   | 0,45%                   | 3,09%                   | 2,04%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XLM-USD         | 2020-12-02   | 2021-03-11 | 38,42%           | UPPER_P90   | False         | 0,04%                   | 0,45%                   | 3,09%                   | 0,61%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-09   | 2025-09-16 | -26,77%          | LOWER_P10   | False         | -2,60%                  | -0,45%                  | -0,80%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | QTUM-USD        | 2023-09-23   | 2023-12-31 | -22,07%          | LOWER_P10   | False         | -2,60%                  | -0,45%                  | -0,80%                  | -0,94%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2020-04-28   | 2020-08-05 | -23,47%          | LOWER_P10   | False         | -2,60%                  | -0,45%                  | -0,80%                  | -0,98%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-09   | 2025-09-16 | -25,92%          | LOWER_P10   | False         | -2,60%                  | -0,45%                  | -0,80%                  | -1,04%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,08%                   | 6,24%                   | 52,52%                  | 31,49%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-09   | 2025-09-16 | -26,77%          | LOWER_P10   | False         | -3,47%                  | -6,24%                  | -26,96%                 | -5,71%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,09%                   | 0,37%                   | 2,15%                   | 7,51%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2025-06-06   | 2025-09-13 | -21,68%          | LOWER_P10   | False         | -2,86%                  | -0,37%                  | -1,70%                  | -0,94%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-09   | 2025-09-16 | -25,92%          | LOWER_P10   | True          | -2,86%                  | -0,37%                  | -1,70%                  | -1,05%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2025-06-09   | 2025-09-16 | -13,52%          | LOWER_P10   | False         | -2,86%                  | -0,37%                  | -1,70%                  | -0,73%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2019-12-03   | 2020-03-11 | -22,41%          | LOWER_P10   | False         | -2,86%                  | -0,37%                  | -1,70%                  | -0,96%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,09%                   | 0,37%                   | 2,15%                   | 2,20%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,09%                   | 0,37%                   | 2,15%                   | 2,03%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | True          | 0,09%                   | 0,37%                   | 2,15%                   | 0,75%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,42%                   | 1,61%                   | 27,40%                  | 28,14%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | HBAR-USD        | 2025-06-06   | 2025-09-13 | -21,68%          | LOWER_P10   | False         | -6,92%                  | -0,87%                  | -26,35%                 | -4,83%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-09   | 2025-09-16 | -25,92%          | LOWER_P10   | False         | -7,35%                  | -0,87%                  | -26,35%                 | -5,26%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | True          | 0,42%                   | 1,61%                   | 1,05%                   | 1,79%                    |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,38%                   | 0,43%                   | 1,71%                   | 7,38%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2022-12-12   | 2023-03-21 | -11,67%          | LOWER_P10   | False         | -3,12%                  | -0,43%                  | -0,67%                  | -0,82%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ONE-USD         | 2019-12-03   | 2020-03-11 | -25,69%          | LOWER_P10   | False         | -3,12%                  | -0,43%                  | -0,67%                  | -1,18%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2021-06-29   | 2021-10-06 | -11,45%          | LOWER_P10   | False         | -3,12%                  | -0,43%                  | -0,67%                  | -0,82%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BCH-USD         | 2019-12-03   | 2020-03-11 | -12,65%          | LOWER_P10   | False         | -3,12%                  | -0,43%                  | -0,67%                  | -0,85%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2021-07-16   | 2021-10-23 | 105,52%          | UPPER_P90   | True          | 0,38%                   | 0,43%                   | 1,71%                   | 2,18%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,38%                   | 0,43%                   | 1,71%                   | 2,07%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-03-22   | 2020-06-29 | 46,00%           | UPPER_P90   | False         | 0,38%                   | 0,43%                   | 1,71%                   | 0,66%                    |
