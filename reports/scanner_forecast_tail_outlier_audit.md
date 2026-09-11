# Scanner forecast tail / outlier audit

Generato: 2026-09-11 05:31:57 UTC

Audit diagnostico dei percorsi a 30 giorni. I casi in coda o outlier non vengono rimossi dal cono: l'impatto leave-one-out mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media.

## Disponibilità coorti

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           4 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 106.889,48 $  | n/a                | 147.877,13 $  | n/a                |
| SOL     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           4 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 127,44 $      | n/a                | 203,20 $      | n/a                |
| DOGE    | AVAILABLE                   | SAME_ASSET_REGIME       |                     1 |                          20 |                         1 |                     20 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07212 $     | 0.07316 $          | 0.12147 $     | 0.10279 $          |

- WARNING DOGE: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

## BTC

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-03   | 2020-12-11 | -41,75%          | LOWER_P10   | False         | -6,74%                  | -0,89%                  | -0,90%                  | -2,11%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | UNI-USD         | 2023-04-07   | 2023-07-15 | -47,87%          | LOWER_P10   | False         | -6,74%                  | -0,89%                  | -0,90%                  | -2,26%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ETC-USD         | 2022-01-01   | 2022-04-10 | -41,06%          | LOWER_P10   | False         | -6,74%                  | -0,89%                  | -0,90%                  | -2,09%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | LRC-USD         | 2019-11-18   | 2020-02-25 | -31,73%          | LOWER_P10   | False         | -6,74%                  | -0,89%                  | -0,90%                  | -1,85%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | DOGE-USD        | 2020-09-03   | 2020-12-11 | 220,23%          | UPPER_P90   | True          | 1,15%                   | 0,89%                   | 2,35%                   | 4,61%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-03   | 2020-12-11 | 118,64%          | UPPER_P90   | False         | 1,15%                   | 0,89%                   | 2,35%                   | 2,01%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | VET-USD         | 2020-03-14   | 2020-06-21 | 103,01%          | UPPER_P90   | False         | 1,15%                   | 0,89%                   | 2,35%                   | 1,60%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | NEAR-USD        | 2023-08-14   | 2023-11-21 | 100,04%          | UPPER_P90   | False         | 1,15%                   | 0,89%                   | 2,35%                   | 1,53%                    |

## SOL

| cohort   | cohort_status   | selected_regime_group   | fallback_level   | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:---------|:----------------|:------------------------|:-----------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ADA-USD         | 2020-09-03   | 2020-12-11 | 118,64%          | UPPER_P90   | False         | 0,27%                   | 6,58%                   | 11,26%                  | 2,24%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | ENJ-USD         | 2020-10-28   | 2021-02-04 | 221,50%          | UPPER_P90   | True          | 0,27%                   | 6,58%                   | 11,26%                  | 4,87%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | BAT-USD         | 2020-10-28   | 2021-02-04 | 112,89%          | UPPER_P90   | False         | 0,27%                   | 6,58%                   | 11,26%                  | 2,09%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | FTM-USD         | 2020-11-02   | 2021-02-09 | 197,73%          | UPPER_P90   | True          | 0,27%                   | 6,58%                   | 11,26%                  | 4,27%                    |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | XRP-USD         | 2020-09-03   | 2020-12-11 | -41,75%          | LOWER_P10   | False         | -3,20%                  | -6,58%                  | -0,99%                  | -1,88%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | MANA-USD        | 2019-11-18   | 2020-02-25 | -41,16%          | LOWER_P10   | False         | -3,20%                  | -6,58%                  | -0,99%                  | -1,86%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | WAVES-USD       | 2019-11-18   | 2020-02-25 | -32,00%          | LOWER_P10   | False         | -3,20%                  | -6,58%                  | -0,99%                  | -1,63%                   |
| RAW      | AVAILABLE       | ALL_MATCHES             | NONE             | TRX-USD         | 2021-01-11   | 2021-04-20 | -32,65%          | LOWER_P10   | False         | -3,20%                  | -6,58%                  | -0,99%                  | -1,64%                   |

## DOGE

| cohort          | cohort_status   | selected_regime_group   | fallback_level        | similar_asset   | start_date   | end_date   | return_30d_pct   | tail_side   | iqr_outlier   | p10_impact_pct_points   | p50_impact_pct_points   | p90_impact_pct_points   | mean_impact_pct_points   |
|:----------------|:----------------|:------------------------|:----------------------|:----------------|:-------------|:-----------|:-----------------|:------------|:--------------|:------------------------|:------------------------|:------------------------|:-------------------------|
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | QTUM-USD        | 2020-09-03   | 2020-12-11 | 46,63%           | UPPER_P90   | False         | 0,17%                   | 0,48%                   | 20,21%                  | 1,32%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | DOT-USD         | 2023-08-14   | 2023-11-21 | 71,01%           | UPPER_P90   | True          | 0,17%                   | 0,48%                   | 20,21%                  | 1,95%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ICP-USD         | 2023-08-07   | 2023-11-14 | 48,98%           | UPPER_P90   | False         | 0,17%                   | 0,48%                   | 20,21%                  | 1,38%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZEC-USD         | 2026-01-15   | 2026-04-24 | 84,11%           | UPPER_P90   | True          | 0,17%                   | 0,48%                   | 20,21%                  | 2,28%                    |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | NEO-USD         | 2019-08-10   | 2019-11-17 | -35,14%          | LOWER_P10   | False         | -0,17%                  | -0,48%                  | -0,21%                  | -0,78%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | THETA-USD       | 2026-01-29   | 2026-05-08 | -34,68%          | LOWER_P10   | False         | -0,17%                  | -0,48%                  | -0,21%                  | -0,76%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | DASH-USD        | 2022-01-01   | 2022-04-10 | -34,38%          | LOWER_P10   | False         | -0,17%                  | -0,48%                  | -0,21%                  | -0,76%                   |
| RAW             | AVAILABLE       | ALL_MATCHES             | NONE                  | ZEC-USD         | 2021-05-21   | 2021-08-28 | -30,46%          | LOWER_P10   | False         | -0,17%                  | -0,48%                  | -0,21%                  | -0,66%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | THETA-USD       | 2026-01-29   | 2026-05-08 | -34,68%          | LOWER_P10   | False         | -4,59%                  | -0,76%                  | -2,95%                  | -1,60%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | DASH-USD        | 2022-01-01   | 2022-04-10 | -34,38%          | LOWER_P10   | False         | -4,59%                  | -0,76%                  | -2,95%                  | -1,59%                   |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | DOT-USD         | 2023-08-14   | 2023-11-21 | 71,01%           | UPPER_P90   | True          | 0,56%                   | 0,76%                   | 3,17%                   | 3,96%                    |
| REGIME_ADJUSTED | AVAILABLE       | SAME_ASSET_REGIME       | 1_SAME_ASSET_FALLBACK | ICP-USD         | 2023-08-07   | 2023-11-14 | 48,98%           | UPPER_P90   | False         | 0,56%                   | 0,76%                   | 3,17%                   | 2,80%                    |
