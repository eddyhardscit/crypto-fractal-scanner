# Scanner forecast tail / outlier audit

Generato: 2026-10-27 06:32:58 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | AVAILABLE                   | SAME_BTC_REGIME         |                     2 |                           3 |                         9 |                      9 |                  5 | 2_SAME_BTC_FALLBACK   | FALLBACK_TO_SAME_BTC_REGIME   | 78.739,57 $   | 68.853,77 $        | 106.720,86 $  | 132.781,49 $       |
| SOL     | AVAILABLE                   | SAME_ASSET_REGIME       |                     4 |                           5 |                        11 |                      5 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 98,91 $       | 106,12 $           | 128,36 $      | 118,33 $           |
| DOGE    | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     1 |                           1 |                         3 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 0.07632 $     | n/a                | 0.11223 $     | n/a                |

- WARNING BTC: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

- WARNING SOL: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort          | cohort_status   | selected_regime_group   | fallback_level      | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:--------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,38%                   | 0,07%                   | 5,69%                   | 7,57%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | AVAX-USD        | 2021-07-16   | 2021-10-23 | 105,52%          | UPPER_P90   | True          | 0,38%                   | 0,07%                   | 5,69%                   | 2,38%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,38%                   | 0,07%                   | 5,69%                   | 2,27%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | EGLD-USD        | 2021-07-05   | 2021-10-12 | 34,87%           | UPPER_P90   | False         | 0,38%                   | 0,07%                   | 5,69%                   | 0,57%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | ADA-USD         | 2025-06-09   | 2025-09-16 | -26,77%          | LOWER_P10   | False         | -3,01%                  | -0,07%                  | -0,09%                  | -1,01%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | LINK-USD        | 2025-06-09   | 2025-09-16 | -25,92%          | LOWER_P10   | False         | -3,01%                  | -0,07%                  | -0,09%                  | -0,99%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | VET-USD         | 2020-05-03   | 2020-08-10 | -40,11%          | LOWER_P10   | False         | -3,01%                  | -0,07%                  | -0,09%                  | -1,35%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                | HBAR-USD        | 2025-06-11   | 2025-09-18 | -32,68%          | LOWER_P10   | False         | -3,01%                  | -0,07%                  | -0,09%                  | -1,16%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,59%                   | 2,64%                   | 65,56%                  | 35,80%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_BTC_REGIME         | 2_SAME_BTC_FALLBACK | HBAR-USD        | 2025-06-11   | 2025-09-18 | -32,68%          | LOWER_P10   | False         | -1,78%                  | -6,17%                  | -30,16%                 | -6,79%                   |

## SOL

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | RUNE-USD        | 2023-07-11   | 2023-10-18 | 308,03%          | UPPER_P90   | True          | 0,30%                   | 0,26%                   | 2,36%                   | 7,50%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | AVAX-USD        | 2021-07-16   | 2021-10-23 | 105,52%          | UPPER_P90   | True          | 0,30%                   | 0,26%                   | 2,36%                   | 2,31%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,30%                   | 0,26%                   | 2,36%                   | 2,19%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | MKR-USD         | 2019-01-18   | 2019-04-27 | 45,14%           | UPPER_P90   | True          | 0,30%                   | 0,26%                   | 2,36%                   | 0,76%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | BCH-USD         | 2019-12-03   | 2020-03-11 | -12,65%          | LOWER_P10   | False         | -0,95%                  | -0,26%                  | -1,82%                  | -0,72%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ETH-USD         | 2025-06-09   | 2025-09-16 | -13,52%          | LOWER_P10   | False         | -0,95%                  | -0,26%                  | -1,82%                  | -0,74%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | LINK-USD        | 2025-06-09   | 2025-09-16 | -25,92%          | LOWER_P10   | False         | -0,95%                  | -0,26%                  | -1,82%                  | -1,06%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ADA-USD         | 2025-06-09   | 2025-09-16 | -26,77%          | LOWER_P10   | False         | -0,95%                  | -0,26%                  | -1,82%                  | -1,08%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | ETH-USD         | 2021-06-30   | 2021-10-07 | 26,02%           | UPPER_P90   | True          | 0,67%                   | 3,82%                   | 11,35%                  | 4,94%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | TRX-USD         | 2025-06-09   | 2025-09-16 | -7,85%           | LOWER_P10   | False         | -6,30%                  | -0,64%                  | -1,83%                  | -3,52%                   |

## DOGE

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XTZ-USD         | 2019-10-04   | 2020-01-11 | 101,06%          | UPPER_P90   | True          | 0,18%                   | 0,16%                   | 14,71%                  | 2,41%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2020-03-27   | 2020-07-04 | 46,77%           | UPPER_P90   | True          | 0,18%                   | 0,16%                   | 14,71%                  | 1,02%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | AVAX-USD        | 2021-07-16   | 2021-10-23 | 105,52%          | UPPER_P90   | True          | 0,18%                   | 0,16%                   | 14,71%                  | 2,53%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XLM-USD         | 2020-03-27   | 2020-07-04 | 54,80%           | UPPER_P90   | True          | 0,18%                   | 0,16%                   | 14,71%                  | 1,23%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MKR-USD         | 2019-01-18   | 2019-04-27 | 45,14%           | CENTRAL     | True          | 0,18%                   | 0,16%                   | 14,38%                  | 0,98%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ZEC-USD         | 2021-09-18   | 2021-12-26 | -46,00%          | LOWER_P10   | True          | -0,59%                  | -0,16%                  | -0,16%                  | -1,36%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2018-07-31   | 2018-11-07 | -42,15%          | LOWER_P10   | True          | -0,59%                  | -0,16%                  | -0,16%                  | -1,26%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | EOS-USD         | 2025-03-01   | 2025-06-08 | -28,88%          | LOWER_P10   | True          | -0,59%                  | -0,16%                  | -0,16%                  | -0,92%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2019-04-12   | 2019-07-20 | -14,97%          | LOWER_P10   | False         | -0,59%                  | -0,16%                  | -0,16%                  | -0,56%                   |
