# Scanner forecast tail / outlier audit

Generato: 2026-09-04 05:31:55 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_ASSET_REGIME       |                     2 |                           5 |                         5 |                      5 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 91.365,78 $   | 105.225,41 $       | 136.007,54 $  | 236.620,96 $       |
| SOL     | AVAILABLE                   | SAME_ASSET_REGIME       |                     2 |                           5 |                         5 |                      5 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 118,15 $      | 109,72 $           | 203,03 $      | 303,01 $           |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           0 |                         2 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 0.07929 $     | n/a                | 0.10842 $     | n/a                |

- WARNING BTC: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 1,21%                   | 0,60%                   | 5,24%                   | 6,92%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | DOGE-USD        | 2020-08-29   | 2020-12-06 | 192,80%          | UPPER_P90   | True          | 1,21%                   | 0,60%                   | 5,24%                   | 4,24%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2023-08-15   | 2023-11-22 | 118,51%          | UPPER_P90   | True          | 1,21%                   | 0,60%                   | 5,24%                   | 2,34%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | VET-USD         | 2020-03-04   | 2020-06-11 | 109,07%          | UPPER_P90   | True          | 1,21%                   | 0,60%                   | 5,24%                   | 2,09%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LRC-USD         | 2019-11-13   | 2020-02-20 | -24,87%          | LOWER_P10   | False         | -4,87%                  | -0,60%                  | -4,56%                  | -1,34%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ETC-USD         | 2021-12-27   | 2022-04-05 | -36,44%          | LOWER_P10   | False         | -4,87%                  | -0,60%                  | -4,56%                  | -1,64%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | RUNE-USD        | 2026-01-26   | 2026-05-05 | -33,21%          | LOWER_P10   | False         | -4,87%                  | -0,60%                  | -4,56%                  | -1,55%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | True          | -4,87%                  | -0,60%                  | -4,56%                  | -2,33%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 1,60%                   | 13,40%                  | 158,83%                 | 56,67%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | DASH-USD        | 2020-08-29   | 2020-12-06 | -12,81%          | LOWER_P10   | False         | -17,63%                 | -2,49%                  | -26,22%                 | -20,82%                  |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZIL-USD         | 2020-08-26   | 2020-12-03 | 116,90%          | UPPER_P90   | False         | 0,06%                   | 0,41%                   | 9,23%                   | 2,29%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | VET-USD         | 2020-03-04   | 2020-06-11 | 109,07%          | UPPER_P90   | False         | 0,06%                   | 0,41%                   | 9,23%                   | 2,09%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ENJ-USD         | 2020-10-23   | 2021-01-30 | 111,80%          | UPPER_P90   | False         | 0,06%                   | 0,41%                   | 9,23%                   | 2,16%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 0,06%                   | 0,41%                   | 9,23%                   | 6,92%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | False         | -5,11%                  | -0,41%                  | -1,47%                  | -2,33%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | MANA-USD        | 2019-11-13   | 2020-02-20 | -54,50%          | LOWER_P10   | False         | -5,11%                  | -0,41%                  | -1,47%                  | -2,10%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | WAVES-USD       | 2019-11-13   | 2020-02-20 | -37,39%          | LOWER_P10   | False         | -5,11%                  | -0,41%                  | -1,47%                  | -1,66%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XLM-USD         | 2024-08-23   | 2024-11-30 | -36,71%          | LOWER_P10   | False         | -5,11%                  | -0,41%                  | -1,47%                  | -1,65%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 1,98%                   | 1,33%                   | 166,07%                 | 58,07%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | MKR-USD         | 2020-03-08   | 2020-06-15 | -16,66%          | LOWER_P10   | False         | -12,70%                 | -14,56%                 | -26,22%                 | -20,39%                  |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2026-01-10   | 2026-04-19 | 90,12%           | UPPER_P90   | True          | 0,46%                   | 0,04%                   | 6,84%                   | 2,37%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | CHZ-USD         | 2020-08-28   | 2020-12-05 | 48,77%           | UPPER_P90   | True          | 0,46%                   | 0,04%                   | 6,84%                   | 1,31%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2021-05-12   | 2021-08-19 | 125,28%          | UPPER_P90   | True          | 0,46%                   | 0,04%                   | 6,84%                   | 3,27%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EOS-USD         | 2025-01-05   | 2025-04-14 | 30,30%           | UPPER_P90   | False         | 0,46%                   | 0,04%                   | 6,84%                   | 0,84%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2021-12-29   | 2022-04-07 | -35,36%          | LOWER_P10   | False         | -0,49%                  | -0,04%                  | -0,62%                  | -0,85%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KSM-USD         | 2021-12-30   | 2022-04-08 | -35,06%          | LOWER_P10   | False         | -0,49%                  | -0,04%                  | -0,62%                  | -0,84%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2021-12-27   | 2022-04-05 | -32,76%          | LOWER_P10   | False         | -0,49%                  | -0,04%                  | -0,62%                  | -0,78%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SOL-USD         | 2021-12-30   | 2022-04-08 | -31,49%          | LOWER_P10   | False         | -0,49%                  | -0,04%                  | -0,62%                  | -0,75%                   |
