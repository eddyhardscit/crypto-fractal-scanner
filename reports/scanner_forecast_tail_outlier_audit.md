# Scanner forecast tail / outlier audit

Generato: 2026-10-08 05:32:25 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           1 |                         6 |                      6 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.993,54 $   | 91.350,16 $        | 105.280,22 $  | 169.448,50 $       |
| SOL     | AVAILABLE        | SAME_BTC_REGIME         |                     0 |                           1 |                        11 |                     11 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 110,02 $      | 109,17 $           | 140,48 $      | 140,14 $           |
| DOGE    | AVAILABLE        | SAME_BTC_REGIME         |                     1 |                           2 |                         5 |                      5 |                  5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08568 $     | 0.09321 $          | 0.11016 $     | 0.18582 $          |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING DOGE: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-24   | 2021-01-01 | 179,59%          | UPPER_P90   | True          | 0,14%                   | 0,61%                   | 1,46%                   | 4,42%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-21   | 2023-09-28 | 29,46%           | UPPER_P90   | False         | 0,14%                   | 0,61%                   | 1,46%                   | 0,57%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,14%                   | 0,61%                   | 1,46%                   | 0,76%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-08   | 2023-12-16 | 38,69%           | UPPER_P90   | False         | 0,14%                   | 0,61%                   | 1,46%                   | 0,81%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ETH-USD         | 2019-03-23   | 2019-06-30 | -27,58%          | LOWER_P10   | False         | -0,34%                  | -0,61%                  | -0,26%                  | -0,89%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-11-12   | 2021-02-19 | -24,36%          | LOWER_P10   | False         | -0,34%                  | -0,61%                  | -0,26%                  | -0,81%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2020-11-13   | 2021-02-20 | -24,16%          | LOWER_P10   | False         | -0,34%                  | -0,61%                  | -0,26%                  | -0,80%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2023-09-13   | 2023-12-21 | -15,42%          | LOWER_P10   | False         | -0,34%                  | -0,61%                  | -0,26%                  | -0,58%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2020-09-24   | 2021-01-01 | 179,59%          | UPPER_P90   | True          | 0,02%                   | 14,58%                  | 76,91%                  | 29,88%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-12   | 2021-02-19 | -24,36%          | LOWER_P10   | False         | -8,04%                  | -14,58%                 | -15,01%                 | -10,91%                  |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,21%                   | 0,44%                   | 1,72%                   | 0,95%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-06-21   | 2023-09-28 | 29,46%           | UPPER_P90   | False         | 0,21%                   | 0,44%                   | 1,72%                   | 0,76%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BTC-USD         | 2022-11-25   | 2023-03-04 | 24,32%           | UPPER_P90   | False         | 0,21%                   | 0,44%                   | 1,72%                   | 0,63%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-08   | 2023-12-16 | 38,69%           | UPPER_P90   | False         | 0,21%                   | 0,44%                   | 1,72%                   | 1,00%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2018-12-29   | 2019-04-07 | -27,90%          | LOWER_P10   | False         | -0,44%                  | -0,44%                  | -0,30%                  | -0,71%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LRC-USD         | 2020-11-12   | 2021-02-19 | -24,36%          | LOWER_P10   | False         | -0,44%                  | -0,44%                  | -0,30%                  | -0,62%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | MKR-USD         | 2020-11-13   | 2021-02-20 | -24,16%          | LOWER_P10   | False         | -0,44%                  | -0,44%                  | -0,30%                  | -0,61%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOT-USD         | 2023-09-13   | 2023-12-21 | -17,49%          | LOWER_P10   | False         | -0,44%                  | -0,44%                  | -0,30%                  | -0,44%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-06-21   | 2023-09-28 | 29,46%           | UPPER_P90   | True          | 0,02%                   | 2,45%                   | 10,13%                  | 3,30%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | BNB-USD         | 2025-05-25   | 2025-09-01 | 21,32%           | UPPER_P90   | False         | 0,02%                   | 2,45%                   | 9,31%                   | 2,49%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | LRC-USD         | 2020-11-12   | 2021-02-19 | -24,36%          | LOWER_P10   | False         | -8,12%                  | -0,15%                  | -0,81%                  | -2,08%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | MKR-USD         | 2020-11-13   | 2021-02-20 | -24,16%          | LOWER_P10   | False         | -8,10%                  | -0,15%                  | -0,81%                  | -2,06%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | KSM-USD         | 2023-09-11   | 2023-12-19 | 36,63%           | UPPER_P90   | False         | 0,17%                   | 0,15%                   | 7,74%                   | 0,81%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2020-09-24   | 2021-01-01 | 179,59%          | UPPER_P90   | True          | 0,17%                   | 0,15%                   | 7,74%                   | 4,47%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | NEAR-USD        | 2023-09-08   | 2023-12-16 | 38,69%           | UPPER_P90   | True          | 0,17%                   | 0,15%                   | 7,74%                   | 0,86%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2020-03-07   | 2020-06-14 | 71,94%           | UPPER_P90   | True          | 0,17%                   | 0,15%                   | 7,74%                   | 1,71%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ENJ-USD         | 2023-09-13   | 2023-12-21 | -17,13%          | LOWER_P10   | False         | -1,18%                  | -0,15%                  | -1,23%                  | -0,57%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | DOT-USD         | 2023-09-13   | 2023-12-21 | -17,49%          | LOWER_P10   | False         | -1,18%                  | -0,15%                  | -1,23%                  | -0,58%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | BCH-USD         | 2019-11-18   | 2020-02-25 | -35,92%          | LOWER_P10   | False         | -1,18%                  | -0,15%                  | -1,23%                  | -1,05%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2019-11-23   | 2020-03-01 | -41,48%          | LOWER_P10   | True          | -1,18%                  | -0,15%                  | -1,23%                  | -1,20%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2020-09-24   | 2021-01-01 | 179,59%          | UPPER_P90   | True          | 1,07%                   | 0,34%                   | 102,86%                 | 35,08%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | HBAR-USD        | 2025-05-22   | 2025-08-29 | -5,19%           | LOWER_P10   | True          | -6,65%                  | -1,92%                  | -16,95%                 | -11,11%                  |
