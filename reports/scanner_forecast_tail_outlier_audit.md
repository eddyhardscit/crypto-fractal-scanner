# Scanner forecast tail / outlier audit

Generato: 2026-10-10 05:32:31 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           1 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.371,05 $   | 87.193,11 $        | 102.342,44 $  | 108.330,37 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           1 |                        11 |                     11 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 113,37 $      | 116,07 $           | 134,35 $      | 133,40 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                         8 |                      8 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09144 $     | 0.08894 $          | 0.11211 $     | 0.10295 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-27   | 2023-03-06 | 25,63%           | UPPER_P90   | False         | 0,02%                   | 0,15%                   | 1,69%                   | 0,61%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,02%                   | 0,15%                   | 1,69%                   | 1,00%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,02%                   | 0,15%                   | 1,69%                   | 0,89%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DASH-USD        | 2020-09-28   | 2021-01-05 | 24,84%           | UPPER_P90   | False         | 0,02%                   | 0,15%                   | 1,69%                   | 0,59%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XLM-USD         | 2020-05-21   | 2020-08-28 | -23,46%          | LOWER_P10   | False         | -0,05%                  | -0,15%                  | -0,10%                  | -0,65%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2023-09-13   | 2023-12-21 | -19,53%          | LOWER_P10   | False         | -0,05%                  | -0,15%                  | -0,10%                  | -0,55%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-13   | 2023-12-21 | -15,42%          | LOWER_P10   | False         | -0,05%                  | -0,15%                  | -0,10%                  | -0,44%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EOS-USD         | 2023-09-13   | 2023-12-21 | -14,00%          | LOWER_P10   | False         | -0,05%                  | -0,15%                  | -0,10%                  | -0,40%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 1,08%                   | 2,35%                   | 13,69%                  | 5,14%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | False         | -5,42%                  | -2,26%                  | -1,58%                  | -3,65%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,14%                   | 0,65%                   | 0,77%                   | 1,05%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,14%                   | 0,65%                   | 0,77%                   | 0,94%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,14%                   | 0,65%                   | 0,77%                   | 0,83%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-29   | 2019-04-07 | -27,90%          | LOWER_P10   | False         | -0,36%                  | -0,65%                  | -0,38%                  | -0,82%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-27   | 2023-03-06 | 25,63%           | UPPER_P90   | False         | 0,14%                   | 0,65%                   | 0,77%                   | 0,55%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2023-09-18   | 2023-12-26 | -20,59%          | LOWER_P10   | False         | -0,36%                  | -0,65%                  | -0,38%                  | -0,63%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-13   | 2023-12-21 | -15,42%          | LOWER_P10   | False         | -0,36%                  | -0,65%                  | -0,38%                  | -0,50%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2023-09-13   | 2023-12-21 | -19,53%          | LOWER_P10   | False         | -0,36%                  | -0,65%                  | -0,38%                  | -0,61%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,28%                   | 2,35%                   | 10,13%                  | 3,47%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2025-05-25   | 2025-09-01 | 21,32%           | UPPER_P90   | False         | 0,28%                   | 2,35%                   | 8,20%                   | 1,54%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | False         | -3,75%                  | -0,34%                  | -1,93%                  | -1,80%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ZEC-USD         | 2024-05-25   | 2024-09-01 | -9,36%           | LOWER_P10   | False         | -3,47%                  | -0,34%                  | -1,93%                  | -1,52%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -1,29%                  | -0,34%                  | -0,85%                  | -0,57%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2026-02-13   | 2026-05-23 | -22,03%          | LOWER_P10   | False         | -1,29%                  | -0,34%                  | -0,85%                  | -0,74%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EOS-USD         | 2023-09-13   | 2023-12-21 | -14,00%          | LOWER_P10   | False         | -1,29%                  | -0,34%                  | -0,85%                  | -0,53%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-18   | 2020-02-25 | -35,92%          | LOWER_P10   | True          | -1,29%                  | -0,34%                  | -0,85%                  | -1,09%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | True          | 0,03%                   | 0,34%                   | 1,29%                   | 0,98%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,03%                   | 0,34%                   | 1,29%                   | 0,87%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2025-03-21   | 2025-06-28 | 55,41%           | UPPER_P90   | True          | 0,03%                   | 0,34%                   | 1,29%                   | 1,25%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOT-USD         | 2021-06-15   | 2021-09-22 | 37,45%           | UPPER_P90   | False         | 0,03%                   | 0,34%                   | 1,29%                   | 0,79%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 0,32%                   | 2,55%                   | 11,46%                  | 5,34%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -2,64%                  | -2,55%                  | -3,05%                  | -2,66%                   |
