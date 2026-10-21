# Scanner forecast tail / outlier audit

Generato: 2026-10-21 05:33:01 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     2 |                           2 |                        11 |                     11 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 84.490,39 $   | 83.541,28 $        | 111.959,46 $  | 105.490,43 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     4 |                           4 |                        14 |                     14 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 112,83 $      | 104,96 $           | 136,92 $      | 147,71 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09057 $     | 0.08241 $          | 0.10265 $     | 0.09345 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,10%                   | 0,31%                   | 4,50%                   | 5,07%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,10%                   | 0,31%                   | 4,50%                   | 2,12%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | False         | 0,10%                   | 0,31%                   | 4,50%                   | 1,34%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-04-26   | 2020-08-03 | 78,11%           | UPPER_P90   | False         | 0,10%                   | 0,31%                   | 4,50%                   | 1,70%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -1,88%                  | -0,31%                  | -3,20%                  | -1,05%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -1,88%                  | -0,31%                  | -3,20%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2020-04-28   | 2020-08-05 | -23,47%          | LOWER_P10   | False         | -1,88%                  | -0,31%                  | -3,20%                  | -0,90%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ALGO-USD        | 2025-06-03   | 2025-09-10 | -26,51%          | LOWER_P10   | False         | -1,88%                  | -0,31%                  | -3,20%                  | -0,98%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,03%                   | 0,97%                   | 4,77%                   | 19,36%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -2,48%                  | -0,99%                  | -18,21%                 | -4,51%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -2,51%                  | -0,99%                  | -18,21%                 | -4,55%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ETH-USD         | 2020-11-27   | 2021-03-06 | 27,38%           | UPPER_P90   | False         | 0,03%                   | 0,97%                   | -13,44%                 | 1,15%                    |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 0,58%                   | 0,94%                   | 1,80%                   | 5,06%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -4,65%                  | -0,94%                  | -1,70%                  | -1,07%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -4,65%                  | -0,94%                  | -1,70%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-28   | 2020-03-06 | -33,50%          | LOWER_P10   | False         | -4,65%                  | -0,94%                  | -1,70%                  | -1,17%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-28   | 2020-03-06 | -37,91%          | LOWER_P10   | True          | -4,65%                  | -0,94%                  | -1,70%                  | -1,28%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,58%                   | 0,94%                   | 1,80%                   | 2,11%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,58%                   | 0,94%                   | 1,80%                   | 1,33%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 0,58%                   | 0,94%                   | 1,80%                   | 0,83%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-06   | 2023-10-13 | 209,44%          | UPPER_P90   | True          | 1,34%                   | 1,83%                   | 13,06%                  | 14,92%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2023-05-22   | 2023-08-29 | 44,53%           | UPPER_P90   | False         | 1,34%                   | 1,83%                   | 13,06%                  | 2,23%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2025-06-04   | 2025-09-11 | -29,65%          | LOWER_P10   | False         | -9,79%                  | -1,83%                  | -1,71%                  | -3,48%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | False         | -9,79%                  | -1,83%                  | -1,71%                  | -3,45%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | True          | -5,05%                  | -0,28%                  | -0,21%                  | -1,04%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2019-11-29   | 2020-03-07 | -18,39%          | LOWER_P10   | False         | -5,05%                  | -0,28%                  | -0,21%                  | -0,76%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2021-09-13   | 2021-12-21 | -26,36%          | LOWER_P10   | False         | -5,05%                  | -0,28%                  | -0,21%                  | -0,96%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-28   | 2020-03-06 | -33,50%          | LOWER_P10   | True          | -5,05%                  | -0,28%                  | -0,21%                  | -1,15%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-11   | 2021-10-18 | 94,33%           | UPPER_P90   | True          | 0,69%                   | 0,28%                   | 0,76%                   | 2,13%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-09-29   | 2020-01-06 | 64,01%           | UPPER_P90   | True          | 0,69%                   | 0,28%                   | 0,76%                   | 1,35%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2021-06-25   | 2021-10-02 | 27,51%           | UPPER_P90   | False         | 0,69%                   | 0,28%                   | 0,76%                   | 0,42%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2022-12-07   | 2023-03-16 | 39,31%           | UPPER_P90   | False         | 0,69%                   | 0,28%                   | 0,76%                   | 0,72%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ADA-USD         | 2025-06-04   | 2025-09-11 | -29,30%          | LOWER_P10   | True          | -16,04%                 | -0,99%                  | -1,92%                  | -6,85%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ZEC-USD         | 2024-06-04   | 2024-09-11 | 22,09%           | UPPER_P90   | True          | 2,33%                   | 3,44%                   | 12,13%                  | 6,00%                    |
