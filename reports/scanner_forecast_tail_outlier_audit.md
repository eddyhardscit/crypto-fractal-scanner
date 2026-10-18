# Scanner forecast tail / outlier audit

Generato: 2026-10-18 05:32:55 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           2 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 87.321,03 $   | 87.661,06 $        | 107.922,78 $  | 141.384,19 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     3 |                           4 |                        14 |                     14 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 109,89 $      | 111,07 $           | 133,86 $      | 126,09 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           0 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08799 $     | 0.08141 $          | 0.10262 $     | 0.18138 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,50%                   | 0,44%                   | 2,67%                   | 5,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | False         | 0,50%                   | 0,44%                   | 2,67%                   | 1,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,50%                   | 0,44%                   | 2,67%                   | 1,33%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-20   | 2021-09-27 | 33,95%           | UPPER_P90   | False         | 0,50%                   | 0,44%                   | 2,67%                   | 0,56%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2019-04-02   | 2019-07-10 | -27,42%          | LOWER_P10   | False         | -0,50%                  | -0,44%                  | -0,20%                  | -1,01%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2023-09-18   | 2023-12-26 | -23,18%          | LOWER_P10   | False         | -0,50%                  | -0,44%                  | -0,20%                  | -0,91%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | CRV-USD         | 2023-09-22   | 2023-12-30 | -22,99%          | LOWER_P10   | False         | -0,50%                  | -0,44%                  | -0,20%                  | -0,90%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MANA-USD        | 2023-09-18   | 2023-12-26 | -22,50%          | LOWER_P10   | False         | -0,50%                  | -0,44%                  | -0,20%                  | -0,89%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,37%                   | 0,85%                   | 61,46%                  | 25,55%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-22   | 2021-03-01 | -6,75%           | LOWER_P10   | False         | -6,51%                  | -0,85%                  | -19,47%                 | -5,34%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-28   | 2020-03-06 | -33,50%          | LOWER_P10   | True          | -7,41%                  | -0,28%                  | -0,50%                  | -1,11%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2019-11-28   | 2020-03-06 | -42,86%          | LOWER_P10   | True          | -7,41%                  | -0,28%                  | -0,50%                  | -1,35%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | True          | -7,41%                  | -0,28%                  | -0,50%                  | -1,22%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DASH-USD        | 2019-11-28   | 2020-03-06 | -28,09%          | LOWER_P10   | False         | -7,41%                  | -0,28%                  | -0,50%                  | -0,97%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,50%                   | 0,28%                   | 3,67%                   | 5,12%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,50%                   | 0,28%                   | 3,67%                   | 1,13%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,50%                   | 0,28%                   | 3,67%                   | 1,39%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-20   | 2021-09-27 | 33,95%           | UPPER_P90   | False         | 0,50%                   | 0,28%                   | 3,67%                   | 0,62%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,70%                   | 0,85%                   | 8,09%                   | 14,65%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2023-05-17   | 2023-08-24 | 24,95%           | UPPER_P90   | False         | 0,70%                   | 0,85%                   | 8,09%                   | 0,46%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -5,65%                  | -0,85%                  | -1,02%                  | -2,52%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | SNX-USD         | 2020-11-22   | 2021-03-01 | -14,46%          | LOWER_P10   | False         | -5,65%                  | -0,85%                  | -1,02%                  | -2,57%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -5,91%                  | -0,02%                  | -0,48%                  | -0,73%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | True          | -5,91%                  | -0,02%                  | -0,48%                  | -1,35%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2019-11-26   | 2020-03-04 | -23,09%          | LOWER_P10   | False         | -5,91%                  | -0,02%                  | -0,48%                  | -0,97%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-28   | 2020-03-06 | -33,50%          | LOWER_P10   | True          | -5,91%                  | -0,02%                  | -0,48%                  | -1,24%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,38%                   | 0,02%                   | 0,69%                   | 4,99%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,38%                   | 0,02%                   | 0,69%                   | 1,26%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-06   | 2021-10-13 | 53,62%           | UPPER_P90   | True          | 0,38%                   | 0,02%                   | 0,69%                   | 1,00%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-20   | 2021-09-27 | 33,95%           | UPPER_P90   | False         | 0,38%                   | 0,02%                   | 0,69%                   | 0,49%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 1,07%                   | 2,94%                   | 122,19%                 | 42,15%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-25   | 2019-12-02 | -13,76%          | LOWER_P10   | False         | -8,20%                  | -2,94%                  | -20,07%                 | -13,65%                  |
