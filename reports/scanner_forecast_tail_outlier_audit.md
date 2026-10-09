# Scanner forecast tail / outlier audit

Generato: 2026-10-09 05:32:24 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           0 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.762,94 $   | 90.747,57 $        | 103.333,68 $  | 110.721,40 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           1 |                        11 |                     11 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 111,36 $      | 111,43 $           | 134,15 $      | 134,05 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09039 $     | 0.09010 $          | 0.11670 $     | 0.10438 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,14%                   | 0,51%                   | 0,40%                   | 0,94%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EOS-USD         | 2023-09-13   | 2023-12-21 | -14,00%          | LOWER_P10   | False         | -0,91%                  | -0,51%                  | -0,02%                  | -0,46%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-13   | 2023-12-21 | -15,42%          | LOWER_P10   | False         | -0,91%                  | -0,51%                  | -0,02%                  | -0,50%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2023-09-13   | 2023-12-21 | -13,73%          | LOWER_P10   | False         | -0,91%                  | -0,51%                  | -0,02%                  | -0,46%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2023-09-13   | 2023-12-21 | -13,76%          | LOWER_P10   | False         | -0,91%                  | -0,51%                  | -0,02%                  | -0,46%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,14%                   | 0,51%                   | 0,40%                   | 0,84%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | 1INCH-USD       | 2023-09-10   | 2023-12-18 | 26,81%           | UPPER_P90   | False         | 0,14%                   | 0,51%                   | 0,40%                   | 0,58%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-26   | 2023-03-05 | 25,55%           | UPPER_P90   | False         | 0,14%                   | 0,51%                   | 0,40%                   | 0,55%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,69%                   | 2,26%                   | 13,89%                  | 6,16%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ONE-USD         | 2023-07-20   | 2024-04-24 | -1,34%           | LOWER_P10   | False         | -5,49%                  | -7,38%                  | -1,58%                  | -4,32%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,03%                   | 0,06%                   | 1,51%                   | 0,97%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-26   | 2023-03-05 | 25,55%           | UPPER_P90   | False         | 0,03%                   | 0,06%                   | 1,51%                   | 0,58%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,03%                   | 0,06%                   | 1,51%                   | 0,87%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LTC-USD         | 2018-12-22   | 2019-03-31 | 22,26%           | UPPER_P90   | False         | 0,03%                   | 0,06%                   | 1,51%                   | 0,50%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-29   | 2019-04-07 | -27,90%          | LOWER_P10   | False         | -1,17%                  | -0,06%                  | -0,09%                  | -0,79%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-13   | 2023-12-21 | -15,42%          | LOWER_P10   | False         | -1,17%                  | -0,06%                  | -0,09%                  | -0,47%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2023-09-18   | 2023-12-26 | -20,59%          | LOWER_P10   | False         | -1,17%                  | -0,06%                  | -0,09%                  | -0,60%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EOS-USD         | 2023-09-13   | 2023-12-21 | -14,00%          | LOWER_P10   | False         | -1,17%                  | -0,06%                  | -0,09%                  | -0,43%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,28%                   | 0,20%                   | 10,13%                  | 3,57%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2025-05-25   | 2025-09-01 | 21,32%           | UPPER_P90   | False         | 0,28%                   | 0,20%                   | 8,20%                   | 1,64%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | False         | -3,75%                  | -2,35%                  | -1,93%                  | -1,71%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ZEC-USD         | 2024-05-25   | 2024-09-01 | -9,36%           | LOWER_P10   | False         | -3,47%                  | -2,35%                  | -1,93%                  | -1,43%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,01%                   | 0,34%                   | 8,94%                   | 0,89%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | False         | 0,01%                   | 0,34%                   | 8,94%                   | 1,00%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2025-03-21   | 2025-06-28 | 55,41%           | UPPER_P90   | True          | 0,01%                   | 0,34%                   | 8,94%                   | 1,27%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOT-USD         | 2021-06-15   | 2021-09-22 | 37,45%           | UPPER_P90   | False         | 0,01%                   | 0,34%                   | 8,94%                   | 0,81%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-13   | 2026-05-23 | -22,03%          | LOWER_P10   | False         | -1,10%                  | -0,34%                  | -0,08%                  | -0,71%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-13   | 2023-12-21 | -15,42%          | LOWER_P10   | False         | -1,10%                  | -0,34%                  | -0,08%                  | -0,55%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-13   | 2023-12-21 | -15,92%          | LOWER_P10   | False         | -1,10%                  | -0,34%                  | -0,08%                  | -0,56%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-18   | 2020-02-25 | -35,92%          | LOWER_P10   | False         | -1,10%                  | -0,34%                  | -0,08%                  | -1,07%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 1,02%                   | 2,55%                   | 14,13%                  | 5,76%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -6,89%                  | -0,34%                  | -3,05%                  | -3,57%                   |
