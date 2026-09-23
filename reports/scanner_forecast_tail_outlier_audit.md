# Scanner forecast tail / outlier audit

Generato: 2026-09-23 05:31:53 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 98.819,34 $   | n/a                | 143.053,32 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           2 |                         1 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 121,80 $      | n/a                | 200,60 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 0.09332 $     | n/a                | 0.13604 $     | n/a                |

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | INJ-USD         | 2023-08-21   | 2023-11-28 | 114,93%          | UPPER_P90   | True          | 0,62%                   | 0,13%                   | 10,57%                  | 2,49%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-09-18   | 2020-12-26 | 78,30%           | UPPER_P90   | True          | 0,62%                   | 0,13%                   | 10,57%                  | 1,55%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | KSM-USD         | 2023-08-27   | 2023-12-04 | 67,94%           | UPPER_P90   | True          | 0,62%                   | 0,13%                   | 10,57%                  | 1,29%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-13   | 2020-12-21 | 145,91%          | UPPER_P90   | True          | 0,62%                   | 0,13%                   | 10,57%                  | 3,29%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2022-11-10   | 2023-02-17 | -25,81%          | LOWER_P10   | False         | -2,61%                  | -0,13%                  | -0,34%                  | -1,12%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-06-26   | 2018-10-03 | -33,85%          | LOWER_P10   | False         | -2,61%                  | -0,13%                  | -0,34%                  | -1,32%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-13   | 2020-12-21 | -42,64%          | LOWER_P10   | True          | -2,61%                  | -0,13%                  | -0,34%                  | -1,55%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-12-03   | 2020-03-11 | -37,38%          | LOWER_P10   | False         | -2,61%                  | -0,13%                  | -0,34%                  | -1,41%                   |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2020-11-09   | 2021-02-16 | 153,55%          | UPPER_P90   | True          | 0,80%                   | 1,33%                   | 11,51%                  | 3,60%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-04-02   | 2020-07-10 | 75,00%           | UPPER_P90   | False         | 0,80%                   | 1,33%                   | 11,51%                  | 1,59%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-13   | 2020-12-21 | 145,91%          | UPPER_P90   | True          | 0,80%                   | 1,33%                   | 11,51%                  | 3,41%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SOL-USD         | 2020-10-31   | 2021-02-07 | 121,57%          | UPPER_P90   | True          | 0,80%                   | 1,33%                   | 11,51%                  | 2,78%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2022-01-18   | 2022-04-27 | -49,99%          | LOWER_P10   | False         | -1,03%                  | -1,33%                  | -0,71%                  | -1,62%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-13   | 2020-12-21 | -42,64%          | LOWER_P10   | False         | -1,03%                  | -1,33%                  | -0,71%                  | -1,43%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2021-01-26   | 2021-05-05 | -39,91%          | LOWER_P10   | False         | -1,03%                  | -1,33%                  | -0,71%                  | -1,36%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-06-26   | 2018-10-03 | -33,85%          | LOWER_P10   | False         | -1,03%                  | -1,33%                  | -0,71%                  | -1,20%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FIL-USD         | 2020-12-06   | 2021-03-15 | 213,76%          | UPPER_P90   | True          | 0,08%                   | 1,21%                   | 5,19%                   | 5,54%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2020-09-09   | 2020-12-17 | 97,38%           | UPPER_P90   | True          | 0,08%                   | 1,21%                   | 5,19%                   | 2,55%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2023-08-26   | 2023-12-03 | 55,72%           | UPPER_P90   | True          | 0,08%                   | 1,21%                   | 5,19%                   | 1,48%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ICP-USD         | 2023-08-22   | 2023-11-29 | 108,08%          | UPPER_P90   | True          | 0,08%                   | 1,21%                   | 5,19%                   | 2,83%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DASH-USD        | 2019-11-08   | 2020-02-15 | -64,76%          | LOWER_P10   | True          | -0,99%                  | -1,21%                  | -2,50%                  | -1,60%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EOS-USD         | 2019-11-08   | 2020-02-15 | -60,27%          | LOWER_P10   | True          | -0,99%                  | -1,21%                  | -2,50%                  | -1,49%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BCH-USD         | 2019-11-08   | 2020-02-15 | -60,99%          | LOWER_P10   | True          | -0,99%                  | -1,21%                  | -2,50%                  | -1,51%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2019-11-08   | 2020-02-15 | -62,00%          | LOWER_P10   | True          | -0,99%                  | -1,21%                  | -2,50%                  | -1,53%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ONE-USD         | 2019-11-08   | 2020-02-15 | -58,32%          | CENTRAL     | True          | 0,08%                   | -1,21%                  | -2,50%                  | -1,44%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | TRX-USD         | 2019-11-08   | 2020-02-15 | -59,46%          | CENTRAL     | True          | -0,83%                  | -1,21%                  | -2,50%                  | -1,47%                   |
