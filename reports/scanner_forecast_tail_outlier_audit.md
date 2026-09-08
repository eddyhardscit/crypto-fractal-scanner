# Scanner forecast tail / outlier audit

Generato: 2026-09-08 05:31:56 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_ASSET_REGIME       |                     0 |                           5 |                         0 |                      5 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 94.263,72 $   | 81.210,60 $        | 134.877,23 $  | 110.489,74 $       |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           3 |                         1 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 125,62 $      | n/a                | 240,03 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           0 |                         1 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 0.08070 $     | n/a                | 0.10939 $     | n/a                |

- WARNING BTC: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XLM-USD         | 2020-09-03   | 2020-12-11 | 91,00%           | UPPER_P90   | False         | 0,23%                   | 0,11%                   | 7,03%                   | 1,77%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | INJ-USD         | 2023-08-06   | 2023-11-13 | 89,19%           | UPPER_P90   | False         | 0,23%                   | 0,11%                   | 7,03%                   | 1,72%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ADA-USD         | 2023-08-14   | 2023-11-21 | 77,51%           | UPPER_P90   | False         | 0,23%                   | 0,11%                   | 7,03%                   | 1,42%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2023-08-20   | 2023-11-27 | 108,32%          | UPPER_P90   | True          | 0,23%                   | 0,11%                   | 7,03%                   | 2,21%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | True          | -4,28%                  | -0,11%                  | -0,70%                  | -1,79%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -4,28%                  | -0,11%                  | -0,70%                  | -1,49%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | True          | -4,28%                  | -0,11%                  | -0,70%                  | -2,19%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | WAVES-USD       | 2020-08-29   | 2020-12-06 | -34,05%          | LOWER_P10   | False         | -4,28%                  | -0,11%                  | -0,70%                  | -1,44%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | False         | -25,81%                 | -16,81%                 | -0,59%                  | -13,05%                  |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | LRC-USD         | 2020-03-12   | 2020-06-19 | 42,62%           | UPPER_P90   | False         | 3,51%                   | 7,95%                   | 13,64%                  | 9,57%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-31   | 2020-12-08 | 143,04%          | UPPER_P90   | False         | 0,05%                   | 4,18%                   | 11,23%                  | 2,71%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-28   | 2021-02-04 | 221,50%          | UPPER_P90   | True          | 0,05%                   | 4,18%                   | 11,23%                  | 4,72%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LINK-USD        | 2019-02-21   | 2019-05-31 | 237,43%          | UPPER_P90   | True          | 0,05%                   | 4,18%                   | 11,23%                  | 5,13%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-11-02   | 2021-02-09 | 197,73%          | UPPER_P90   | True          | 0,05%                   | 4,18%                   | 11,23%                  | 4,11%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -1,51%                  | -4,18%                  | -1,18%                  | -1,89%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | False         | -1,51%                  | -4,18%                  | -1,18%                  | -2,59%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2024-08-28   | 2024-12-05 | -32,47%          | LOWER_P10   | False         | -1,51%                  | -4,18%                  | -1,18%                  | -1,79%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-18   | 2020-02-25 | -41,16%          | LOWER_P10   | False         | -1,51%                  | -4,18%                  | -1,18%                  | -2,02%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2026-01-15   | 2026-04-24 | 84,11%           | UPPER_P90   | True          | 0,22%                   | 1,40%                   | 7,50%                   | 2,32%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | OMG-USD         | 2021-05-16   | 2021-08-23 | 41,60%           | UPPER_P90   | False         | 0,22%                   | 1,40%                   | 7,50%                   | 1,23%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SAND-USD        | 2023-08-03   | 2023-11-10 | 31,66%           | UPPER_P90   | False         | 0,22%                   | 1,40%                   | 7,50%                   | 0,98%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-08-25   | 2020-12-02 | 31,14%           | UPPER_P90   | False         | 0,22%                   | 1,40%                   | 7,50%                   | 0,96%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2022-05-10   | 2022-08-17 | -28,78%          | LOWER_P10   | False         | -0,71%                  | -1,40%                  | -1,07%                  | -0,57%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEO-USD         | 2019-08-05   | 2019-11-12 | -28,61%          | LOWER_P10   | False         | -0,71%                  | -1,40%                  | -1,07%                  | -0,57%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2022-01-03   | 2022-04-12 | -54,16%          | LOWER_P10   | False         | -0,71%                  | -1,40%                  | -1,07%                  | -1,22%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SOL-USD         | 2022-01-04   | 2022-04-13 | -53,72%          | LOWER_P10   | False         | -0,71%                  | -1,40%                  | -1,07%                  | -1,21%                   |
