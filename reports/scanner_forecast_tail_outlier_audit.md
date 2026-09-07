# Scanner forecast tail / outlier audit

Generato: 2026-09-07 05:31:52 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           2 |                         0 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 94.260,37 $   | n/a                | 136.653,94 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           4 |                         2 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 126,54 $      | n/a                | 214,85 $      | n/a                |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           0 |                         1 |                      0 |                  5 | NONE             | INSUFFICIENT_REGIME_MATCHES | 0.07649 $     | n/a                | 0.10002 $     | n/a                |

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | True          | -15,37%                 | -1,67%                  | -0,70%                  | -2,38%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ETC-USD         | 2021-12-27   | 2022-04-05 | -36,44%          | LOWER_P10   | False         | -15,37%                 | -1,67%                  | -0,70%                  | -1,69%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -15,37%                 | -1,67%                  | -0,70%                  | -1,68%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2020-08-29   | 2020-12-06 | -34,05%          | LOWER_P10   | False         | -15,37%                 | -1,67%                  | -0,70%                  | -1,63%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2023-08-14   | 2023-11-21 | 77,51%           | UPPER_P90   | False         | 0,23%                   | 1,67%                   | 7,03%                   | 1,23%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2023-08-20   | 2023-11-27 | 108,32%          | UPPER_P90   | True          | 0,23%                   | 1,67%                   | 7,03%                   | 2,02%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2020-08-29   | 2020-12-06 | 192,80%          | UPPER_P90   | True          | 0,23%                   | 1,67%                   | 7,03%                   | 4,19%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 0,23%                   | 1,67%                   | 7,03%                   | 6,86%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-31   | 2020-12-08 | 143,04%          | UPPER_P90   | False         | 0,30%                   | 2,46%                   | 27,33%                  | 2,88%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-28   | 2021-02-04 | 221,50%          | UPPER_P90   | True          | 0,30%                   | 2,46%                   | 27,33%                  | 4,90%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LINK-USD        | 2019-02-21   | 2019-05-31 | 237,43%          | UPPER_P90   | True          | 0,30%                   | 2,46%                   | 27,33%                  | 5,30%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-11-02   | 2021-02-09 | 197,73%          | UPPER_P90   | True          | 0,30%                   | 2,46%                   | 27,33%                  | 4,29%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -0,67%                  | -2,46%                  | -4,39%                  | -1,71%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | False         | -0,67%                  | -2,46%                  | -4,39%                  | -2,41%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-13   | 2020-02-20 | -54,50%          | LOWER_P10   | False         | -0,67%                  | -2,46%                  | -4,39%                  | -2,18%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BTC-USD         | 2017-09-11   | 2017-12-19 | -35,45%          | LOWER_P10   | False         | -0,67%                  | -2,46%                  | -4,39%                  | -1,69%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2026-01-15   | 2026-04-24 | 84,11%           | UPPER_P90   | True          | 0,06%                   | 0,98%                   | 1,10%                   | 2,37%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | HBAR-USD        | 2021-05-13   | 2021-08-20 | 60,48%           | UPPER_P90   | True          | 0,06%                   | 0,98%                   | 1,10%                   | 1,76%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | OMG-USD         | 2021-05-16   | 2021-08-23 | 41,60%           | UPPER_P90   | True          | 0,06%                   | 0,98%                   | 1,10%                   | 1,28%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2022-01-03   | 2022-04-12 | -54,16%          | LOWER_P10   | False         | -0,19%                  | -0,98%                  | -1,07%                  | -1,18%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XTZ-USD         | 2019-08-15   | 2019-11-22 | 20,48%           | UPPER_P90   | False         | 0,06%                   | 0,98%                   | 1,10%                   | 0,74%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2021-05-21   | 2021-08-28 | -29,89%          | LOWER_P10   | False         | -0,19%                  | -0,98%                  | -1,07%                  | -0,56%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DASH-USD        | 2021-12-27   | 2022-04-05 | -31,12%          | LOWER_P10   | False         | -0,19%                  | -0,98%                  | -1,07%                  | -0,59%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEO-USD         | 2021-05-16   | 2021-08-23 | -29,39%          | LOWER_P10   | False         | -0,19%                  | -0,98%                  | -1,07%                  | -0,54%                   |
