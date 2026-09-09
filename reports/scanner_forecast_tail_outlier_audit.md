# Scanner forecast tail / outlier audit

Generato: 2026-09-09 05:31:55 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_ASSET_REGIME       |                     0 |                           5 |                         0 |                      5 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 95.158,40 $   | 81.563,96 $        | 141.373,53 $  | 110.970,49 $       |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           4 |                         1 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 122,60 $      | n/a                | 222,92 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           0 |                         1 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 0.08277 $     | n/a                | 0.12020 $     | n/a                |

- WARNING BTC: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XLM-USD         | 2020-09-03   | 2020-12-11 | 91,00%           | UPPER_P90   | False         | 0,20%                   | 0,50%                   | 6,77%                   | 1,72%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | INJ-USD         | 2023-08-06   | 2023-11-13 | 89,19%           | UPPER_P90   | False         | 0,20%                   | 0,50%                   | 6,77%                   | 1,67%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2023-08-20   | 2023-11-27 | 108,32%          | UPPER_P90   | True          | 0,20%                   | 0,50%                   | 6,77%                   | 2,16%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ADA-USD         | 2020-09-03   | 2020-12-11 | 118,64%          | UPPER_P90   | True          | 0,20%                   | 0,50%                   | 6,77%                   | 2,43%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | True          | -2,06%                  | -0,50%                  | -1,17%                  | -1,84%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XRP-USD         | 2020-09-03   | 2020-12-11 | -41,75%          | LOWER_P10   | False         | -2,06%                  | -0,50%                  | -1,17%                  | -1,68%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -2,06%                  | -0,50%                  | -1,17%                  | -1,54%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ETC-USD         | 2022-01-01   | 2022-04-10 | -41,06%          | LOWER_P10   | False         | -2,06%                  | -0,50%                  | -1,17%                  | -1,67%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | False         | -25,81%                 | -16,81%                 | -0,59%                  | -13,05%                  |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | LRC-USD         | 2020-03-12   | 2020-06-19 | 42,62%           | UPPER_P90   | False         | 3,51%                   | 7,95%                   | 13,64%                  | 9,57%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-31   | 2020-12-08 | 143,04%          | UPPER_P90   | False         | 0,05%                   | 0,04%                   | 11,54%                  | 2,82%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-28   | 2021-02-04 | 221,50%          | UPPER_P90   | True          | 0,05%                   | 0,04%                   | 11,54%                  | 4,83%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-03   | 2020-12-11 | 118,64%          | UPPER_P90   | False         | 0,05%                   | 0,04%                   | 11,54%                  | 2,20%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-11-02   | 2021-02-09 | 197,73%          | UPPER_P90   | True          | 0,05%                   | 0,04%                   | 11,54%                  | 4,23%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-03   | 2020-12-11 | -41,75%          | LOWER_P10   | False         | -2,21%                  | -0,04%                  | -0,58%                  | -1,92%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-18   | 2020-02-25 | -41,16%          | LOWER_P10   | False         | -2,21%                  | -0,04%                  | -0,58%                  | -1,90%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2024-08-28   | 2024-12-05 | -32,47%          | LOWER_P10   | False         | -2,21%                  | -0,04%                  | -0,58%                  | -1,68%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | False         | -2,21%                  | -0,04%                  | -0,58%                  | -2,07%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2026-01-15   | 2026-04-24 | 84,11%           | UPPER_P90   | True          | 0,01%                   | 0,47%                   | 11,08%                  | 2,22%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SNX-USD         | 2023-08-04   | 2023-11-11 | 69,65%           | UPPER_P90   | True          | 0,01%                   | 0,47%                   | 11,08%                  | 1,84%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2023-08-07   | 2023-11-14 | 48,98%           | UPPER_P90   | False         | 0,01%                   | 0,47%                   | 11,08%                  | 1,31%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | CHZ-USD         | 2020-09-02   | 2020-12-10 | 68,67%           | UPPER_P90   | True          | 0,01%                   | 0,47%                   | 11,08%                  | 1,82%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2022-05-10   | 2022-08-17 | -28,78%          | LOWER_P10   | False         | -0,79%                  | -0,47%                  | -1,78%                  | -0,68%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | THETA-USD       | 2026-01-29   | 2026-05-08 | -34,68%          | LOWER_P10   | False         | -0,79%                  | -0,47%                  | -1,78%                  | -0,83%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2021-05-26   | 2021-09-02 | -25,96%          | LOWER_P10   | False         | -0,79%                  | -0,47%                  | -1,78%                  | -0,61%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2022-01-03   | 2022-04-12 | -54,16%          | LOWER_P10   | False         | -0,79%                  | -0,47%                  | -1,78%                  | -1,33%                   |
