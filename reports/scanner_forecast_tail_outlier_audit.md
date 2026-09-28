# Scanner forecast tail / outlier audit

Generato: 2026-09-28 05:31:55 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         7 |                      7 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.102,29 $   | 85.382,23 $        | 111.275,66 $  | 97.008,56 $        |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           3 |                        10 |                     10 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 119,79 $      | 131,13 $           | 192,13 $      | 158,54 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08429 $     | 0.09828 $          | 0.13310 $     | 0.11871 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | INJ-USD         | 2023-08-26   | 2023-12-03 | 112,10%          | UPPER_P90   | True          | 0,14%                   | 0,13%                   | 3,26%                   | 2,77%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-14   | 2020-12-22 | 78,89%           | UPPER_P90   | True          | 0,14%                   | 0,13%                   | 3,26%                   | 1,92%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2023-08-26   | 2023-12-03 | 54,44%           | UPPER_P90   | True          | 0,14%                   | 0,13%                   | 3,26%                   | 1,29%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LTC-USD         | 2018-12-06   | 2019-03-15 | 40,60%           | UPPER_P90   | False         | 0,14%                   | 0,13%                   | 3,26%                   | 0,94%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2022-11-15   | 2023-02-22 | -26,39%          | LOWER_P10   | False         | -1,50%                  | -0,13%                  | -0,73%                  | -0,78%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -1,50%                  | -0,13%                  | -0,73%                  | -1,08%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | CRV-USD         | 2023-09-02   | 2023-12-10 | -27,54%          | LOWER_P10   | False         | -1,50%                  | -0,13%                  | -0,73%                  | -0,81%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOGE-USD        | 2018-07-01   | 2018-10-08 | -34,80%          | LOWER_P10   | False         | -1,50%                  | -0,13%                  | -0,73%                  | -0,99%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ETC-USD         | 2023-09-03   | 2023-12-11 | 30,13%           | UPPER_P90   | True          | 0,79%                   | 2,47%                   | 10,22%                  | 4,31%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -3,73%                  | -1,22%                  | -2,21%                  | -2,57%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2020-11-14   | 2021-02-21 | 121,56%          | UPPER_P90   | True          | 0,26%                   | 2,34%                   | 3,77%                   | 2,82%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | OP-USD          | 2023-09-04   | 2023-12-12 | 70,44%           | UPPER_P90   | True          | 0,26%                   | 2,34%                   | 3,77%                   | 1,51%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | SNX-USD         | 2019-02-06   | 2019-05-16 | 143,22%          | UPPER_P90   | True          | 0,26%                   | 2,34%                   | 3,77%                   | 3,37%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-04-07   | 2020-07-15 | 135,41%          | UPPER_P90   | True          | 0,26%                   | 2,34%                   | 3,77%                   | 3,17%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2022-11-14   | 2023-02-21 | -24,36%          | LOWER_P10   | False         | -2,38%                  | -2,34%                  | -1,01%                  | -0,92%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-19   | 2019-03-28 | -28,88%          | LOWER_P10   | False         | -2,38%                  | -2,34%                  | -1,01%                  | -1,04%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2022-11-15   | 2023-02-22 | -26,39%          | LOWER_P10   | False         | -2,38%                  | -2,34%                  | -1,01%                  | -0,98%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2024-05-15   | 2024-08-22 | -24,53%          | LOWER_P10   | False         | -2,38%                  | -2,34%                  | -1,01%                  | -0,93%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,90%                   | 2,15%                   | 12,04%                  | 5,18%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -4,95%                  | -2,15%                  | -3,02%                  | -2,77%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-14   | 2020-12-22 | 78,89%           | UPPER_P90   | True          | 0,61%                   | 1,22%                   | 6,92%                   | 1,93%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | FIL-USD         | 2020-12-11   | 2021-03-20 | 87,82%           | UPPER_P90   | True          | 0,61%                   | 1,22%                   | 6,92%                   | 2,16%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,61%                   | 1,22%                   | 6,92%                   | 1,45%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2023-08-27   | 2023-12-04 | 179,92%          | UPPER_P90   | True          | 0,61%                   | 1,22%                   | 6,92%                   | 4,52%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-21   | 2022-04-30 | -38,08%          | LOWER_P10   | False         | -0,74%                  | -1,22%                  | -1,98%                  | -1,07%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DASH-USD        | 2019-11-13   | 2020-02-20 | -32,46%          | LOWER_P10   | False         | -0,74%                  | -1,22%                  | -1,98%                  | -0,93%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-08-06   | 2018-11-13 | -51,13%          | LOWER_P10   | False         | -0,74%                  | -1,22%                  | -1,98%                  | -1,41%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-13   | 2020-02-20 | -41,11%          | LOWER_P10   | False         | -0,74%                  | -1,22%                  | -1,98%                  | -1,15%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-03   | 2023-12-11 | 60,35%           | UPPER_P90   | True          | 0,90%                   | 1,16%                   | 12,90%                  | 6,19%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-03   | 2023-12-11 | -11,15%          | LOWER_P10   | False         | -5,27%                  | -1,36%                  | -4,15%                  | -2,74%                   |
