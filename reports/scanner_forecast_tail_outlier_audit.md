# Scanner forecast tail / outlier audit

Generato: 2026-10-13 05:32:20 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           3 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK   | FALLBACK_TO_SAME_BTC_REGIME   | 85.015,50 $   | 88.276,27 $        | 108.515,77 $  | 107.892,82 $       |
| SOL     | AVAILABLE        | SAME_ASSET_REGIME       |                     3 |                           5 |                        15 |                      5 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 114,63 $      | 109,75 $           | 140,47 $      | 129,36 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           3 |                         6 |                      6 |                  5 | 2_SAME_BTC_FALLBACK   | FALLBACK_TO_SAME_BTC_REGIME   | 0.09577 $     | 0.08836 $          | 0.11446 $     | 0.12786 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-30   | 2023-03-09 | 37,25%           | UPPER_P90   | False         | 0,04%                   | 1,07%                   | 6,52%                   | 0,91%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | False         | 0,04%                   | 1,07%                   | 6,52%                   | 0,99%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | False         | 0,04%                   | 1,07%                   | 6,52%                   | 1,10%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,04%                   | 1,07%                   | 6,52%                   | 0,89%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -0,19%                  | -1,07%                  | -0,76%                  | -0,86%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | CRV-USD         | 2023-09-17   | 2023-12-25 | -30,57%          | LOWER_P10   | False         | -0,19%                  | -1,07%                  | -0,76%                  | -0,83%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | False         | -0,19%                  | -1,07%                  | -0,76%                  | -0,85%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EOS-USD         | 2023-09-18   | 2023-12-26 | -21,01%          | LOWER_P10   | False         | -0,19%                  | -1,07%                  | -0,76%                  | -0,59%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-26   | 2023-10-03 | 40,60%           | UPPER_P90   | True          | 1,49%                   | 1,42%                   | 19,21%                  | 7,73%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-17   | 2021-02-24 | -12,15%          | LOWER_P10   | True          | -9,77%                  | -3,04%                  | -2,90%                  | -5,45%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | EGLD-USD        | 2023-09-18   | 2023-12-26 | -31,33%          | LOWER_P10   | False         | -5,10%                  | -0,38%                  | -0,83%                  | -0,98%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | THETA-USD       | 2023-09-17   | 2023-12-25 | -31,86%          | LOWER_P10   | False         | -5,10%                  | -0,38%                  | -0,83%                  | -0,99%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | False         | -5,10%                  | -0,38%                  | -0,83%                  | -0,94%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | NEO-USD         | 2019-11-23   | 2020-03-01 | -40,18%          | LOWER_P10   | True          | -5,10%                  | -0,38%                  | -0,83%                  | -1,21%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,93%                   | 0,38%                   | 1,27%                   | 2,27%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | BTC-USD         | 2022-11-30   | 2023-03-09 | 37,25%           | UPPER_P90   | False         | 0,93%                   | 0,38%                   | 1,27%                   | 0,78%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | False         | 0,93%                   | 0,38%                   | 1,27%                   | 0,98%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | BNB-USD         | 2025-05-30   | 2025-09-06 | 41,98%           | UPPER_P90   | False         | 0,93%                   | 0,38%                   | 1,27%                   | 0,90%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | ETH-USD         | 2021-06-15   | 2021-09-22 | 28,99%           | UPPER_P90   | True          | 1,08%                   | 3,00%                   | 15,36%                  | 6,46%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -8,27%                  | -1,98%                  | -2,36%                  | -4,63%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-30   | 2023-03-09 | 37,25%           | UPPER_P90   | False         | 0,77%                   | 0,35%                   | 4,97%                   | 0,66%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-01   | 2021-10-08 | 44,92%           | UPPER_P90   | False         | 0,77%                   | 0,35%                   | 4,97%                   | 0,86%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOT-USD         | 2021-06-20   | 2021-09-27 | 45,51%           | UPPER_P90   | False         | 0,77%                   | 0,35%                   | 4,97%                   | 0,87%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,77%                   | 0,35%                   | 4,97%                   | 2,15%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-23   | 2020-03-01 | -29,90%          | LOWER_P10   | True          | -2,99%                  | -0,35%                  | -0,23%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ONE-USD         | 2019-11-23   | 2020-03-01 | -36,26%          | LOWER_P10   | True          | -2,99%                  | -0,35%                  | -0,23%                  | -1,22%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEO-USD         | 2019-11-23   | 2020-03-01 | -40,18%          | LOWER_P10   | True          | -2,99%                  | -0,35%                  | -0,23%                  | -1,32%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2019-11-26   | 2020-03-04 | -23,09%          | LOWER_P10   | False         | -2,99%                  | -0,35%                  | -0,23%                  | -0,89%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-01   | 2023-10-08 | 95,43%           | UPPER_P90   | True          | 0,86%                   | 1,62%                   | 44,68%                  | 16,14%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LINK-USD        | 2019-08-20   | 2019-11-27 | -15,37%          | LOWER_P10   | False         | -8,10%                  | -1,62%                  | -8,89%                  | -6,02%                   |
