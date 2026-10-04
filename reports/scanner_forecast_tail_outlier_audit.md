# Scanner forecast tail / outlier audit

Generato: 2026-10-04 14:39:39 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           1 |                        13 |                     13 |                  5 | 2_SAME_BTC_FALLBACK   | FALLBACK_TO_SAME_BTC_REGIME   | 85.792,18 $   | 83.722,73 $        | 118.458,49 $  | 108.988,18 $       |
| SOL     | AVAILABLE        | SAME_ASSET_REGIME       |                     2 |                           6 |                        12 |                      6 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 113,48 $      | 124,19 $           | 165,52 $      | 183,11 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK   | FALLBACK_TO_SAME_BTC_REGIME   | 0.08890 $     | 0.09075 $          | 0.13783 $     | 0.11864 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-19   | 2020-12-27 | 169,31%          | UPPER_P90   | True          | 0,05%                   | 0,55%                   | 1,59%                   | 4,09%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | INJ-USD         | 2023-08-31   | 2023-12-08 | 89,93%           | UPPER_P90   | True          | 0,05%                   | 0,55%                   | 1,59%                   | 2,05%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-06   | 2023-12-14 | 43,36%           | UPPER_P90   | False         | 0,05%                   | 0,55%                   | 1,59%                   | 0,86%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BNB-USD         | 2018-12-13   | 2019-03-22 | 58,48%           | UPPER_P90   | False         | 0,05%                   | 0,55%                   | 1,59%                   | 1,24%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ATOM-USD        | 2020-05-16   | 2020-08-23 | -50,50%          | LOWER_P10   | False         | -0,40%                  | -0,55%                  | -0,47%                  | -1,55%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2020-11-13   | 2021-02-20 | -24,16%          | LOWER_P10   | False         | -0,40%                  | -0,55%                  | -0,47%                  | -0,87%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | CRV-USD         | 2023-09-07   | 2023-12-15 | -16,04%          | LOWER_P10   | False         | -0,40%                  | -0,55%                  | -0,47%                  | -0,67%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2022-11-20   | 2023-02-27 | -16,01%          | LOWER_P10   | False         | -0,40%                  | -0,55%                  | -0,47%                  | -0,67%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ETC-USD         | 2023-09-08   | 2023-12-16 | 29,09%           | UPPER_P90   | False         | 0,49%                   | 0,69%                   | 5,65%                   | 2,07%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-08   | 2023-12-16 | 38,69%           | UPPER_P90   | True          | 0,49%                   | 0,69%                   | 5,65%                   | 2,87%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | EGLD-USD        | 2023-09-08   | 2023-12-16 | -12,39%          | LOWER_P10   | False         | -3,99%                  | -1,49%                  | -0,53%                  | -1,39%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ATOM-USD        | 2023-09-08   | 2023-12-16 | -15,48%          | LOWER_P10   | False         | -3,99%                  | -1,49%                  | -0,53%                  | -1,64%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | KSM-USD         | 2023-09-06   | 2023-12-14 | 43,36%           | UPPER_P90   | False         | 0,43%                   | 0,68%                   | 5,52%                   | 1,04%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | SOL-USD         | 2020-11-10   | 2021-02-17 | 72,75%           | UPPER_P90   | True          | 0,43%                   | 0,68%                   | 5,52%                   | 1,79%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | NEAR-USD        | 2023-09-08   | 2023-12-16 | 38,69%           | UPPER_P90   | False         | 0,43%                   | 0,68%                   | 5,52%                   | 0,92%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | OP-USD          | 2023-09-09   | 2023-12-17 | 72,45%           | UPPER_P90   | True          | 0,43%                   | 0,68%                   | 5,52%                   | 1,78%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | HBAR-USD        | 2022-11-19   | 2023-02-26 | -20,31%          | LOWER_P10   | False         | -1,13%                  | -0,68%                  | -0,27%                  | -0,59%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | MKR-USD         | 2018-12-24   | 2019-04-02 | -29,36%          | LOWER_P10   | False         | -1,13%                  | -0,68%                  | -0,27%                  | -0,83%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | MKR-USD         | 2020-11-13   | 2021-02-20 | -24,16%          | LOWER_P10   | False         | -1,13%                  | -0,68%                  | -0,27%                  | -0,69%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LRC-USD         | 2020-11-12   | 2021-02-19 | -24,36%          | LOWER_P10   | False         | -1,13%                  | -0,68%                  | -0,27%                  | -0,70%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | OP-USD          | 2023-09-09   | 2023-12-17 | 72,45%           | UPPER_P90   | False         | 1,42%                   | 2,88%                   | 31,26%                  | 12,44%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | MKR-USD         | 2018-12-24   | 2019-04-02 | -29,36%          | LOWER_P10   | False         | -12,92%                 | -2,88%                  | -4,34%                  | -7,92%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-19   | 2020-12-27 | 169,31%          | UPPER_P90   | True          | 0,01%                   | 1,97%                   | 3,20%                   | 4,08%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ICP-USD         | 2023-09-01   | 2023-12-09 | 145,87%          | UPPER_P90   | True          | 0,01%                   | 1,97%                   | 3,20%                   | 3,48%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | INJ-USD         | 2023-08-31   | 2023-12-08 | 89,93%           | UPPER_P90   | True          | 0,01%                   | 1,97%                   | 3,20%                   | 2,05%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2025-03-16   | 2025-06-23 | 49,87%           | UPPER_P90   | False         | 0,01%                   | 1,97%                   | 3,20%                   | 1,02%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2020-11-13   | 2021-02-20 | -24,16%          | LOWER_P10   | False         | -2,77%                  | -1,97%                  | -0,29%                  | -0,88%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2022-11-19   | 2023-02-26 | -20,45%          | LOWER_P10   | False         | -2,77%                  | -1,97%                  | -0,29%                  | -0,78%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ZEC-USD         | 2026-02-09   | 2026-05-19 | -20,54%          | LOWER_P10   | False         | -2,77%                  | -1,97%                  | -0,29%                  | -0,79%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KAVA-USD        | 2022-01-26   | 2022-05-05 | -36,35%          | LOWER_P10   | False         | -2,77%                  | -1,97%                  | -0,29%                  | -1,19%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | NEAR-USD        | 2023-09-08   | 2023-12-16 | 38,69%           | UPPER_P90   | True          | 0,31%                   | 2,21%                   | 15,37%                  | 4,58%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | ATOM-USD        | 2023-09-08   | 2023-12-16 | -15,48%          | LOWER_P10   | False         | -2,29%                  | -0,69%                  | -1,49%                  | -2,19%                   |
