# Scanner forecast tail / outlier audit

Generato: 2026-09-10 05:31:55 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           4 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 107.687,94 $  | n/a                | 148.571,98 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           4 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 131,54 $      | n/a                | 208,12 $      | n/a                |
| DOGE    | AVAILABLE                   | SAME_ASSET_REGIME       |                     1 |                          18 |                         1 |                     18 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07613 $     | 0.07952 $          | 0.12620 $     | 0.11030 $          |

- WARNING DOGE: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | True          | -28,08%                 | -0,56%                  | -0,18%                  | -2,12%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-03   | 2020-12-11 | -41,75%          | LOWER_P10   | False         | -28,08%                 | -0,56%                  | -0,18%                  | -1,97%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ETC-USD         | 2022-01-01   | 2022-04-10 | -41,06%          | LOWER_P10   | False         | -28,08%                 | -0,56%                  | -0,18%                  | -1,95%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2020-08-29   | 2020-12-06 | -34,05%          | LOWER_P10   | False         | -28,08%                 | -0,56%                  | -0,18%                  | -1,77%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-09-03   | 2020-12-11 | 91,00%           | UPPER_P90   | False         | 0,23%                   | 0,56%                   | 9,52%                   | 1,44%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-03   | 2020-12-11 | 118,64%          | UPPER_P90   | True          | 0,23%                   | 0,56%                   | 9,52%                   | 2,14%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2023-08-20   | 2023-11-27 | 108,32%          | UPPER_P90   | False         | 0,23%                   | 0,56%                   | 9,52%                   | 1,88%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEAR-USD        | 2023-08-14   | 2023-11-21 | 100,04%          | UPPER_P90   | False         | 0,23%                   | 0,56%                   | 9,52%                   | 1,67%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-28   | 2021-02-04 | 221,50%          | UPPER_P90   | True          | 0,27%                   | 7,57%                   | 10,60%                  | 4,84%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-03   | 2020-12-11 | 118,64%          | UPPER_P90   | False         | 0,27%                   | 7,57%                   | 10,60%                  | 2,20%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BAT-USD         | 2020-10-28   | 2021-02-04 | 112,89%          | UPPER_P90   | False         | 0,27%                   | 7,57%                   | 10,60%                  | 2,06%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-11-02   | 2021-02-09 | 197,73%          | UPPER_P90   | True          | 0,27%                   | 7,57%                   | 10,60%                  | 4,23%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-03   | 2020-12-11 | -41,75%          | LOWER_P10   | False         | -4,05%                  | -7,57%                  | -0,99%                  | -1,91%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2019-11-18   | 2020-02-25 | -32,00%          | LOWER_P10   | False         | -4,05%                  | -7,57%                  | -0,99%                  | -1,66%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-18   | 2020-02-25 | -41,16%          | LOWER_P10   | False         | -4,05%                  | -7,57%                  | -0,99%                  | -1,89%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | False         | -4,05%                  | -7,57%                  | -0,99%                  | -2,07%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZEC-USD         | 2026-01-15   | 2026-04-24 | 84,11%           | UPPER_P90   | True          | 0,25%                   | 0,67%                   | 12,63%                  | 2,20%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | DOT-USD         | 2023-08-14   | 2023-11-21 | 71,01%           | UPPER_P90   | True          | 0,25%                   | 0,67%                   | 12,63%                  | 1,87%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ICP-USD         | 2023-08-07   | 2023-11-14 | 48,98%           | UPPER_P90   | True          | 0,25%                   | 0,67%                   | 12,63%                  | 1,30%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | SNX-USD         | 2023-08-04   | 2023-11-11 | 69,65%           | UPPER_P90   | True          | 0,25%                   | 0,67%                   | 12,63%                  | 1,83%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | NEO-USD         | 2019-08-10   | 2019-11-17 | -35,14%          | LOWER_P10   | False         | -0,54%                  | -0,67%                  | -0,24%                  | -0,86%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | THETA-USD       | 2026-01-29   | 2026-05-08 | -34,68%          | LOWER_P10   | False         | -0,54%                  | -0,67%                  | -0,24%                  | -0,84%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | QTUM-USD        | 2019-08-10   | 2019-11-17 | -28,78%          | LOWER_P10   | False         | -0,54%                  | -0,67%                  | -0,24%                  | -0,69%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | FIL-USD         | 2022-05-10   | 2022-08-17 | -28,78%          | LOWER_P10   | False         | -0,54%                  | -0,67%                  | -0,24%                  | -0,69%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | DOT-USD         | 2023-08-14   | 2023-11-21 | 71,01%           | UPPER_P90   | True          | 0,50%                   | 0,03%                   | 9,01%                   | 4,22%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | ICP-USD         | 2023-08-07   | 2023-11-14 | 48,98%           | UPPER_P90   | True          | 0,50%                   | 0,03%                   | 9,01%                   | 2,92%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | FIL-USD         | 2022-05-10   | 2022-08-17 | -28,78%          | LOWER_P10   | False         | -2,46%                  | -0,03%                  | -2,95%                  | -1,65%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | THETA-USD       | 2026-01-29   | 2026-05-08 | -34,68%          | LOWER_P10   | False         | -2,46%                  | -0,03%                  | -2,95%                  | -2,00%                   |
