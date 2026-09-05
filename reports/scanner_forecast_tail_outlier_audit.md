# Scanner forecast tail / outlier audit

Generato: 2026-09-05 08:21:38 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_ASSET_REGIME       |                     2 |                           5 |                         3 |                      5 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 90.050,09 $   | 82.195,01 $        | 129.603,90 $  | 232.854,20 $       |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           4 |                         2 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 118,59 $      | n/a                | 205,07 $      | n/a                |
| DOGE    | AVAILABLE                   | SAME_ASSET_REGIME       |                     1 |                          12 |                         1 |                     12 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07340 $     | 0.07548 $          | 0.09508 $     | 0.08725 $          |

- WARNING BTC: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | DOGE-USD        | 2020-08-29   | 2020-12-06 | 192,80%          | UPPER_P90   | True          | 0,82%                   | 0,43%                   | 10,42%                  | 4,27%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ADA-USD         | 2023-08-09   | 2023-11-16 | 63,44%           | UPPER_P90   | False         | 0,82%                   | 0,43%                   | 10,42%                  | 0,95%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 0,82%                   | 0,43%                   | 10,42%                  | 6,94%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2023-08-15   | 2023-11-22 | 118,51%          | UPPER_P90   | True          | 0,82%                   | 0,43%                   | 10,42%                  | 2,36%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | True          | -3,90%                  | -0,43%                  | -0,08%                  | -2,30%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ETC-USD         | 2021-12-27   | 2022-04-05 | -36,44%          | LOWER_P10   | False         | -3,90%                  | -0,43%                  | -0,08%                  | -1,61%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LRC-USD         | 2019-11-13   | 2020-02-20 | -24,87%          | LOWER_P10   | False         | -3,90%                  | -0,43%                  | -0,08%                  | -1,32%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -3,90%                  | -0,43%                  | -0,08%                  | -1,60%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | UNI-USD         | 2023-04-02   | 2023-07-10 | 297,17%          | UPPER_P90   | True          | 0,39%                   | 7,99%                   | 166,87%                 | 59,00%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | MKR-USD         | 2020-03-08   | 2020-06-15 | -16,66%          | LOWER_P10   | False         | -7,11%                  | -15,89%                 | -26,22%                 | -19,46%                  |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZIL-USD         | 2020-08-31   | 2020-12-08 | 143,04%          | UPPER_P90   | False         | 0,41%                   | 1,53%                   | 12,87%                  | 2,93%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-23   | 2021-01-30 | 111,80%          | UPPER_P90   | False         | 0,41%                   | 1,53%                   | 12,87%                  | 2,13%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LINK-USD        | 2019-02-21   | 2019-05-31 | 237,43%          | UPPER_P90   | True          | 0,41%                   | 1,53%                   | 12,87%                  | 5,35%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-10-28   | 2021-02-04 | 228,32%          | UPPER_P90   | True          | 0,41%                   | 1,53%                   | 12,87%                  | 5,12%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-08-29   | 2020-12-06 | -63,42%          | LOWER_P10   | False         | -2,20%                  | -1,53%                  | -1,26%                  | -2,36%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | RUNE-USD        | 2026-01-31   | 2026-05-10 | -36,07%          | LOWER_P10   | False         | -2,20%                  | -1,53%                  | -1,26%                  | -1,66%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-13   | 2020-02-20 | -54,50%          | LOWER_P10   | False         | -2,20%                  | -1,53%                  | -1,26%                  | -2,14%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BTC-USD         | 2017-09-09   | 2017-12-17 | -39,97%          | LOWER_P10   | False         | -2,20%                  | -1,53%                  | -1,26%                  | -1,76%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XTZ-USD         | 2019-08-15   | 2019-11-22 | 20,48%           | UPPER_P90   | False         | 0,12%                   | 0,67%                   | 5,54%                   | 0,73%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | CHZ-USD         | 2020-08-28   | 2020-12-05 | 48,77%           | UPPER_P90   | True          | 0,12%                   | 0,67%                   | 5,54%                   | 1,46%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZEC-USD         | 2026-01-10   | 2026-04-19 | 90,12%           | UPPER_P90   | True          | 0,12%                   | 0,67%                   | 5,54%                   | 2,52%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | HBAR-USD        | 2021-05-13   | 2021-08-20 | 60,48%           | UPPER_P90   | True          | 0,12%                   | 0,67%                   | 5,54%                   | 1,76%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | SOL-USD         | 2021-12-30   | 2022-04-08 | -31,49%          | LOWER_P10   | False         | -1,14%                  | -0,67%                  | -1,07%                  | -0,60%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LRC-USD         | 2022-01-01   | 2022-04-10 | -40,48%          | LOWER_P10   | False         | -1,14%                  | -0,67%                  | -1,07%                  | -0,83%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | DASH-USD        | 2021-12-27   | 2022-04-05 | -31,12%          | LOWER_P10   | False         | -1,14%                  | -0,67%                  | -1,07%                  | -0,59%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | KSM-USD         | 2021-12-30   | 2022-04-08 | -35,06%          | LOWER_P10   | False         | -1,14%                  | -0,67%                  | -1,07%                  | -0,69%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | FIL-USD         | 2022-05-05   | 2022-08-12 | -26,85%          | LOWER_P10   | False         | -2,35%                  | -0,25%                  | -0,13%                  | -1,31%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | KSM-USD         | 2021-12-30   | 2022-04-08 | -35,06%          | LOWER_P10   | False         | -2,35%                  | -0,25%                  | -0,13%                  | -2,06%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | KAVA-USD        | 2023-08-09   | 2023-11-16 | 2,77%            | UPPER_P90   | False         | 0,26%                   | 0,25%                   | 1,19%                   | 1,38%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | ALGO-USD        | 2026-01-09   | 2026-04-18 | 1,88%            | UPPER_P90   | False         | 0,26%                   | 0,25%                   | 1,19%                   | 1,30%                    |
