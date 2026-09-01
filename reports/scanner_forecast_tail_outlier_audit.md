# Scanner forecast tail / outlier audit

Generato: 2026-09-01 05:32:08 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_BTC_REGIME         |                     2 |                           3 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK   | FALLBACK_TO_SAME_BTC_REGIME   | 82.038,99 $   | 102.614,43 $       | 111.062,22 $  | 124.157,90 $       |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           2 |                         4 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 109,40 $      | n/a                | 208,11 $      | n/a                |
| DOGE    | AVAILABLE                   | SAME_ASSET_REGIME       |                     0 |                           9 |                         1 |                      9 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07934 $     | 0.07870 $          | 0.12350 $     | 0.10399 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2023-08-10   | 2023-11-17 | 85,33%           | UPPER_P90   | True          | 0,08%                   | 0,25%                   | 0,50%                   | 2,01%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XRP-USD         | 2020-08-24   | 2020-12-01 | -64,13%          | LOWER_P10   | True          | -1,69%                  | -0,25%                  | -0,29%                  | -1,82%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2019-11-08   | 2020-02-15 | -43,47%          | LOWER_P10   | False         | -1,69%                  | -0,25%                  | -0,29%                  | -1,29%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETC-USD         | 2021-12-22   | 2022-03-31 | -45,17%          | LOWER_P10   | False         | -1,69%                  | -0,25%                  | -0,29%                  | -1,34%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2026-01-26   | 2026-05-05 | -33,21%          | LOWER_P10   | False         | -1,69%                  | -0,25%                  | -0,29%                  | -1,03%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BNB-USD         | 2018-11-08   | 2019-02-15 | 69,95%           | UPPER_P90   | True          | 0,08%                   | 0,25%                   | 0,50%                   | 1,62%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-08-04   | 2023-11-11 | 45,30%           | UPPER_P90   | False         | 0,08%                   | 0,25%                   | 0,50%                   | 0,98%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2023-08-04   | 2023-11-11 | 43,28%           | UPPER_P90   | False         | 0,08%                   | 0,25%                   | 0,50%                   | 0,93%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2020-03-03   | 2020-06-10 | -32,40%          | LOWER_P10   | False         | -29,77%                 | -4,13%                  | -3,17%                  | -13,61%                  |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2018-11-08   | 2019-02-15 | 69,95%           | UPPER_P90   | False         | 3,68%                   | 12,77%                  | 21,51%                  | 11,98%                   |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-10-18   | 2021-01-25 | 1.143,11%        | UPPER_P90   | True          | 0,37%                   | 0,73%                   | 4,72%                   | 28,14%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-26   | 2020-12-03 | 116,90%          | UPPER_P90   | True          | 0,37%                   | 0,73%                   | 4,72%                   | 1,83%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2020-03-04   | 2020-06-11 | 109,07%          | UPPER_P90   | False         | 0,37%                   | 0,73%                   | 4,72%                   | 1,63%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LINK-USD        | 2019-02-16   | 2019-05-26 | 101,43%          | UPPER_P90   | False         | 0,37%                   | 0,73%                   | 4,72%                   | 1,43%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-24   | 2020-12-01 | -64,13%          | LOWER_P10   | False         | -1,97%                  | -0,73%                  | -0,13%                  | -2,81%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-08   | 2020-02-15 | -61,35%          | LOWER_P10   | False         | -1,97%                  | -0,73%                  | -0,13%                  | -2,74%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2019-11-13   | 2020-02-20 | -37,39%          | LOWER_P10   | False         | -1,97%                  | -0,73%                  | -0,13%                  | -2,13%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -1,97%                  | -0,73%                  | -0,13%                  | -2,09%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | CHZ-USD         | 2020-08-23   | 2020-11-30 | 90,11%           | UPPER_P90   | True          | 0,35%                   | 0,77%                   | 6,31%                   | 2,12%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZEC-USD         | 2026-01-05   | 2026-04-14 | 58,15%           | UPPER_P90   | False         | 0,35%                   | 0,77%                   | 6,31%                   | 1,30%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2021-05-12   | 2021-08-19 | 125,28%          | UPPER_P90   | True          | 0,35%                   | 0,77%                   | 6,31%                   | 3,02%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | FTM-USD         | 2021-05-11   | 2021-08-18 | 199,71%          | UPPER_P90   | True          | 0,35%                   | 0,77%                   | 6,31%                   | 4,93%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | FIL-USD         | 2022-04-30   | 2022-08-07 | -36,15%          | LOWER_P10   | False         | -4,27%                  | -0,77%                  | -1,11%                  | -1,12%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | SOL-USD         | 2021-12-25   | 2022-04-03 | -37,24%          | LOWER_P10   | False         | -4,27%                  | -0,77%                  | -1,11%                  | -1,15%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LRC-USD         | 2021-12-27   | 2022-04-05 | -32,76%          | LOWER_P10   | False         | -4,27%                  | -0,77%                  | -1,11%                  | -1,03%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | KSM-USD         | 2021-12-25   | 2022-04-03 | -36,71%          | LOWER_P10   | False         | -4,27%                  | -0,77%                  | -1,11%                  | -1,13%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | EGLD-USD        | 2023-07-25   | 2023-11-01 | 40,51%           | UPPER_P90   | True          | 0,06%                   | 2,88%                   | 18,62%                  | 5,82%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | KSM-USD         | 2021-12-25   | 2022-04-03 | -36,71%          | LOWER_P10   | False         | -8,35%                  | -2,06%                  | -1,97%                  | -3,83%                   |
