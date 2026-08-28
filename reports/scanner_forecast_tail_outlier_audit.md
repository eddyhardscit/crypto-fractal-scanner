# Scanner forecast tail / outlier audit

Generato: 2026-08-28 08:01:22 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 84.787,03 $   | n/a                | 114.328,93 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 113,68 $      | n/a                | 206,69 $      | n/a                |
| DOGE    | AVAILABLE                   | SAME_ASSET_REGIME       |                     0 |                          10 |                         0 |                     10 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.08353 $     | 0.07921 $          | 0.12452 $     | 0.11622 $          |

- WARNING DOGE: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-11-08   | 2020-02-15 | -43,47%          | LOWER_P10   | True          | -14,12%                 | -0,33%                  | -0,20%                  | -1,36%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ETC-USD         | 2021-12-22   | 2022-03-31 | -45,17%          | LOWER_P10   | True          | -14,12%                 | -0,33%                  | -0,20%                  | -1,40%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2019-11-08   | 2020-02-15 | -45,65%          | LOWER_P10   | True          | -14,12%                 | -0,33%                  | -0,20%                  | -1,41%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BNB-USD         | 2019-11-08   | 2020-02-15 | -61,13%          | LOWER_P10   | True          | -14,12%                 | -0,33%                  | -0,20%                  | -1,81%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BNB-USD         | 2018-11-08   | 2019-02-15 | 69,95%           | UPPER_P90   | True          | 1,31%                   | 0,33%                   | 2,80%                   | 1,55%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2023-08-05   | 2023-11-12 | 98,61%           | UPPER_P90   | True          | 1,31%                   | 0,33%                   | 2,80%                   | 2,29%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EGLD-USD        | 2023-08-04   | 2023-11-11 | 45,30%           | UPPER_P90   | False         | 1,31%                   | 0,33%                   | 2,80%                   | 0,92%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ALGO-USD        | 2023-08-03   | 2023-11-10 | 57,16%           | UPPER_P90   | True          | 1,31%                   | 0,33%                   | 2,80%                   | 1,22%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-10-18   | 2021-01-25 | 1.143,11%        | UPPER_P90   | True          | 0,28%                   | 2,37%                   | 5,69%                   | 27,95%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-08   | 2020-02-15 | -61,35%          | LOWER_P10   | False         | -7,85%                  | -2,37%                  | -0,44%                  | -2,93%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-26   | 2026-05-05 | -33,21%          | LOWER_P10   | False         | -7,85%                  | -2,37%                  | -0,44%                  | -2,21%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-19   | 2020-11-26 | -44,71%          | LOWER_P10   | False         | -7,85%                  | -2,37%                  | -0,44%                  | -2,51%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2019-11-08   | 2020-02-15 | -49,74%          | LOWER_P10   | False         | -7,85%                  | -2,37%                  | -0,44%                  | -2,64%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-21   | 2020-11-28 | 235,51%          | UPPER_P90   | True          | 0,28%                   | 2,37%                   | 5,69%                   | 4,68%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2020-02-28   | 2020-06-06 | 98,37%           | UPPER_P90   | False         | 0,28%                   | 2,37%                   | 5,69%                   | 1,16%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ATOM-USD        | 2020-10-13   | 2021-01-20 | 156,87%          | UPPER_P90   | True          | 0,28%                   | 2,37%                   | 5,69%                   | 2,66%                    |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2021-05-07   | 2021-08-14 | 193,95%          | UPPER_P90   | True          | 0,06%                   | 0,53%                   | 8,63%                   | 4,81%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZEC-USD         | 2026-01-05   | 2026-04-14 | 58,15%           | UPPER_P90   | False         | 0,06%                   | 0,53%                   | 8,63%                   | 1,33%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | EGLD-USD        | 2021-05-06   | 2021-08-13 | 92,46%           | UPPER_P90   | True          | 0,06%                   | 0,53%                   | 8,63%                   | 2,21%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | CHZ-USD         | 2020-08-23   | 2020-11-30 | 90,11%           | UPPER_P90   | True          | 0,06%                   | 0,53%                   | 8,63%                   | 2,15%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | SOL-USD         | 2021-12-25   | 2022-04-03 | -37,24%          | LOWER_P10   | False         | -1,73%                  | -0,53%                  | -1,76%                  | -1,11%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LRC-USD         | 2021-12-22   | 2022-03-31 | -41,29%          | LOWER_P10   | False         | -1,73%                  | -0,53%                  | -1,76%                  | -1,22%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | KSM-USD         | 2021-12-25   | 2022-04-03 | -36,71%          | LOWER_P10   | False         | -1,73%                  | -0,53%                  | -1,76%                  | -1,10%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | VET-USD         | 2021-12-24   | 2022-04-02 | -38,30%          | LOWER_P10   | False         | -1,73%                  | -0,53%                  | -1,76%                  | -1,14%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | EGLD-USD        | 2023-07-25   | 2023-11-01 | 40,51%           | UPPER_P90   | False         | 0,06%                   | 3,89%                   | 9,09%                   | 4,98%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | KSM-USD         | 2021-12-25   | 2022-04-03 | -36,71%          | LOWER_P10   | False         | -6,13%                  | -3,89%                  | -0,86%                  | -3,60%                   |
