# Scanner forecast tail / outlier audit

Generato: 2026-09-24 05:31:53 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 91.351,82 $   | n/a                | 138.820,39 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 115,80 $      | n/a                | 194,70 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 0.08767 $     | n/a                | 0.14658 $     | n/a                |

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | INJ-USD         | 2023-08-21   | 2023-11-28 | 114,93%          | UPPER_P90   | True          | 0,45%                   | 0,79%                   | 4,41%                   | 2,55%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-09-18   | 2020-12-26 | 78,30%           | UPPER_P90   | True          | 0,45%                   | 0,79%                   | 4,41%                   | 1,61%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KSM-USD         | 2023-08-27   | 2023-12-04 | 67,94%           | UPPER_P90   | False         | 0,45%                   | 0,79%                   | 4,41%                   | 1,35%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-13   | 2020-12-21 | 145,91%          | UPPER_P90   | True          | 0,45%                   | 0,79%                   | 4,41%                   | 3,35%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2022-11-10   | 2023-02-17 | -25,81%          | LOWER_P10   | False         | -1,82%                  | -0,79%                  | -0,34%                  | -1,06%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-12-03   | 2020-03-11 | -37,38%          | LOWER_P10   | False         | -1,82%                  | -0,79%                  | -0,34%                  | -1,35%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-06-26   | 2018-10-03 | -33,85%          | LOWER_P10   | False         | -1,82%                  | -0,79%                  | -0,34%                  | -1,26%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-13   | 2020-12-21 | -42,64%          | LOWER_P10   | False         | -1,82%                  | -0,79%                  | -0,34%                  | -1,49%                   |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-04-02   | 2020-07-10 | 75,00%           | UPPER_P90   | False         | 0,07%                   | 0,77%                   | 11,51%                  | 1,57%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2020-11-09   | 2021-02-16 | 153,55%          | UPPER_P90   | True          | 0,07%                   | 0,77%                   | 11,51%                  | 3,58%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SNX-USD         | 2019-02-01   | 2019-05-11 | 275,40%          | UPPER_P90   | True          | 0,07%                   | 0,77%                   | 11,51%                  | 6,71%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SOL-USD         | 2020-10-31   | 2021-02-07 | 121,57%          | UPPER_P90   | True          | 0,07%                   | 0,77%                   | 11,51%                  | 2,76%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2022-01-18   | 2022-04-27 | -49,99%          | LOWER_P10   | False         | -5,50%                  | -0,77%                  | -0,71%                  | -1,64%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-06-26   | 2018-10-03 | -33,85%          | LOWER_P10   | False         | -5,50%                  | -0,77%                  | -0,71%                  | -1,22%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-13   | 2020-12-21 | -42,64%          | LOWER_P10   | False         | -5,50%                  | -0,77%                  | -0,71%                  | -1,45%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2021-01-26   | 2021-05-05 | -39,91%          | LOWER_P10   | False         | -5,50%                  | -0,77%                  | -0,71%                  | -1,38%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-09-09   | 2020-12-17 | 97,38%           | UPPER_P90   | True          | 0,19%                   | 0,78%                   | 23,12%                  | 2,54%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2020-12-06   | 2021-03-15 | 213,76%          | UPPER_P90   | True          | 0,19%                   | 0,78%                   | 23,12%                  | 5,52%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2023-08-22   | 2023-11-29 | 108,08%          | UPPER_P90   | True          | 0,19%                   | 0,78%                   | 23,12%                  | 2,81%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2023-08-26   | 2023-12-03 | 55,72%           | UPPER_P90   | True          | 0,19%                   | 0,78%                   | 23,12%                  | 1,47%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEAR-USD        | 2023-08-29   | 2023-12-06 | 55,08%           | CENTRAL     | True          | 0,19%                   | 0,78%                   | 22,99%                  | 1,45%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DASH-USD        | 2019-11-08   | 2020-02-15 | -64,76%          | LOWER_P10   | True          | -7,22%                  | -0,78%                  | -0,06%                  | -1,62%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BCH-USD         | 2019-11-08   | 2020-02-15 | -60,99%          | LOWER_P10   | True          | -7,22%                  | -0,78%                  | -0,06%                  | -1,52%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EOS-USD         | 2019-11-08   | 2020-02-15 | -60,27%          | LOWER_P10   | True          | -7,22%                  | -0,78%                  | -0,06%                  | -1,51%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2019-11-08   | 2020-02-15 | -62,00%          | LOWER_P10   | True          | -7,22%                  | -0,78%                  | -0,06%                  | -1,55%                   |
