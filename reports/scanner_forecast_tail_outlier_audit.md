# Scanner forecast tail / outlier audit

Generato: 2026-10-16 05:32:57 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           2 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 88.345,19 $   | 87.457,68 $        | 110.180,56 $  | 107.480,38 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           3 |                        13 |                     13 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 116,20 $      | 114,52 $           | 136,94 $      | 130,12 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09378 $     | 0.08727 $          | 0.11012 $     | 0.11417 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2019-04-02   | 2019-07-10 | -27,42%          | LOWER_P10   | False         | -4,75%                  | -0,62%                  | -0,25%                  | -0,91%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2023-09-18   | 2023-12-26 | -25,10%          | LOWER_P10   | False         | -4,75%                  | -0,62%                  | -0,25%                  | -0,85%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -4,75%                  | -0,62%                  | -0,25%                  | -1,03%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-18   | 2026-05-28 | -25,56%          | LOWER_P10   | False         | -4,75%                  | -0,62%                  | -0,25%                  | -0,87%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-03   | 2023-03-12 | 36,42%           | UPPER_P90   | False         | 0,19%                   | 0,62%                   | 4,28%                   | 0,72%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,19%                   | 0,62%                   | 4,28%                   | 2,24%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | False         | 0,19%                   | 0,62%                   | 4,28%                   | 1,16%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-04-21   | 2020-07-29 | 79,49%           | UPPER_P90   | True          | 0,19%                   | 0,62%                   | 4,28%                   | 1,83%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,67%                   | 0,28%                   | 19,70%                  | 10,00%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-22   | 2021-03-01 | -6,75%           | LOWER_P10   | True          | -5,08%                  | -0,85%                  | -8,07%                  | -2,77%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,44%                   | 0,13%                   | 0,88%                   | 2,14%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SNX-USD         | 2020-11-22   | 2021-03-01 | -14,46%          | LOWER_P10   | False         | -2,03%                  | -0,13%                  | -0,50%                  | -0,67%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | False         | -2,03%                  | -0,13%                  | -0,50%                  | -1,07%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2023-09-23   | 2023-12-31 | -11,14%          | LOWER_P10   | False         | -2,03%                  | -0,13%                  | -0,50%                  | -0,59%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DASH-USD        | 2019-11-28   | 2020-03-06 | -28,09%          | LOWER_P10   | False         | -2,03%                  | -0,13%                  | -0,50%                  | -1,02%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,44%                   | 0,13%                   | 0,88%                   | 1,07%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-03   | 2023-03-12 | 36,42%           | UPPER_P90   | False         | 0,44%                   | 0,13%                   | 0,88%                   | 0,63%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-20   | 2021-09-27 | 33,95%           | UPPER_P90   | False         | 0,44%                   | 0,13%                   | 0,88%                   | 0,57%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,20%                   | 0,85%                   | 8,45%                   | 6,90%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2023-05-17   | 2023-08-24 | 24,95%           | UPPER_P90   | True          | 0,20%                   | 0,85%                   | 8,45%                   | 1,03%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-22   | 2021-03-01 | -6,75%           | LOWER_P10   | True          | -2,59%                  | -0,26%                  | -0,99%                  | -1,61%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | SNX-USD         | 2020-11-22   | 2021-03-01 | -14,46%          | LOWER_P10   | True          | -2,59%                  | -0,26%                  | -0,99%                  | -2,25%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ALGO-USD        | 2025-05-29   | 2025-09-05 | -4,76%           | CENTRAL     | True          | -0,80%                  | -0,26%                  | -0,99%                  | -1,45%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -2,93%                  | -0,05%                  | -0,10%                  | -0,69%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-18   | 2026-05-28 | -25,56%          | LOWER_P10   | False         | -2,93%                  | -0,05%                  | -0,10%                  | -0,99%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | True          | -2,93%                  | -0,05%                  | -0,10%                  | -1,10%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | True          | -2,93%                  | -0,05%                  | -0,10%                  | -1,31%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-12-03   | 2023-03-12 | 36,42%           | UPPER_P90   | False         | 0,38%                   | 0,05%                   | 2,61%                   | 0,60%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,38%                   | 0,05%                   | 2,61%                   | 1,04%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BAT-USD         | 2022-12-02   | 2023-03-11 | 34,91%           | UPPER_P90   | False         | 0,38%                   | 0,05%                   | 2,61%                   | 0,56%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,38%                   | 0,05%                   | 2,61%                   | 2,11%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,70%                   | 0,28%                   | 27,82%                  | 11,74%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -3,11%                  | -0,28%                  | -8,07%                  | -3,86%                   |
