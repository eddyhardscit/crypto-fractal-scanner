# Scanner forecast tail / outlier audit

Generato: 2026-09-06 05:31:52 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           4 |                         2 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 91.015,80 $   | n/a                | 129.916,02 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           4 |                         2 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 122,97 $      | n/a                | 212,65 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           0 |                         1 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 0.07996 $     | n/a                | 0.12098 $     | n/a                |

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | True          | -12,45%                 | -0,41%                  | -0,08%                  | -2,36%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ETC-USD         | 2021-12-27   | 2022-04-05 | -36,44%          | LOWER_P10   | False         | -12,45%                 | -0,41%                  | -0,08%                  | -1,67%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-11-13   | 2020-02-20 | -24,87%          | LOWER_P10   | False         | -12,45%                 | -0,41%                  | -0,08%                  | -1,37%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -12,45%                 | -0,41%                  | -0,08%                  | -1,66%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2020-08-29   | 2020-12-06 | 192,80%          | UPPER_P90   | True          | 1,21%                   | 0,41%                   | 10,42%                  | 4,21%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2023-08-09   | 2023-11-16 | 63,44%           | UPPER_P90   | False         | 1,21%                   | 0,41%                   | 10,42%                  | 0,90%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 1,21%                   | 0,41%                   | 10,42%                  | 6,89%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2023-08-15   | 2023-11-22 | 118,51%          | UPPER_P90   | True          | 1,21%                   | 0,41%                   | 10,42%                  | 2,31%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-31   | 2020-12-08 | 143,04%          | UPPER_P90   | True          | 0,13%                   | 1,53%                   | 24,20%                  | 2,96%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-23   | 2021-01-30 | 111,80%          | UPPER_P90   | False         | 0,13%                   | 1,53%                   | 24,20%                  | 2,16%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LINK-USD        | 2019-02-21   | 2019-05-31 | 237,43%          | UPPER_P90   | True          | 0,13%                   | 1,53%                   | 24,20%                  | 5,38%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-10-28   | 2021-02-04 | 228,32%          | UPPER_P90   | True          | 0,13%                   | 1,53%                   | 24,20%                  | 5,15%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | False         | -5,18%                  | -1,53%                  | -1,26%                  | -2,33%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-13   | 2020-02-20 | -54,50%          | LOWER_P10   | False         | -5,18%                  | -1,53%                  | -1,26%                  | -2,10%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2019-11-13   | 2020-02-20 | -37,39%          | LOWER_P10   | False         | -5,18%                  | -1,53%                  | -1,26%                  | -1,66%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BTC-USD         | 2017-09-10   | 2017-12-18 | -41,46%          | LOWER_P10   | False         | -5,18%                  | -1,53%                  | -1,26%                  | -1,77%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | CHZ-USD         | 2020-08-28   | 2020-12-05 | 48,77%           | UPPER_P90   | True          | 0,13%                   | 0,25%                   | 10,34%                  | 1,38%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2026-01-10   | 2026-04-19 | 90,12%           | UPPER_P90   | True          | 0,13%                   | 0,25%                   | 10,34%                  | 2,44%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2021-05-13   | 2021-08-20 | 60,48%           | UPPER_P90   | True          | 0,13%                   | 0,25%                   | 10,34%                  | 1,68%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | OMG-USD         | 2021-05-16   | 2021-08-23 | 41,60%           | UPPER_P90   | True          | 0,13%                   | 0,25%                   | 10,34%                  | 1,19%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2021-05-21   | 2021-08-28 | -29,89%          | LOWER_P10   | False         | -1,38%                  | -0,25%                  | -0,94%                  | -0,64%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | SOL-USD         | 2021-12-30   | 2022-04-08 | -31,49%          | LOWER_P10   | False         | -1,38%                  | -0,25%                  | -0,94%                  | -0,68%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DASH-USD        | 2021-12-27   | 2022-04-05 | -31,12%          | LOWER_P10   | False         | -1,38%                  | -0,25%                  | -0,94%                  | -0,67%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2022-01-01   | 2022-04-10 | -40,48%          | LOWER_P10   | False         | -1,38%                  | -0,25%                  | -0,94%                  | -0,91%                   |
