# Market Regime Match Report

Generated: 2026-08-27 15:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | 2026-08-27      | MIXED                 |       78653.3  | True                 | 7.20%               | -8.53%                   | MIXED              | 7.20%            | -8.53%                |
| DOGE-USD | 2026-08-27      | BEAR                  |           0.09 | False                | -13.19%             | -15.19%                  | MIXED              | 7.20%            | -8.53%                |
| SOL-USD  | 2026-08-27      | RECOVERY              |         100.99 | True                 | 23.26%              | -14.40%                  | MIXED              | 7.20%            | -8.53%                |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 70.00%              | 11.54%           | 19.60%           | 40.46%           | -9.51%             | -19.06%            | 17.64%             | 28.99%             | 49.29%             | 67.50%              | 12.54%           | 32.43%           | 93.87%           |
| BTC-USD  | SAME_BTC_REGIME           |         0 | n/a                 | n/a              | n/a              | n/a              | n/a                | n/a                | n/a                | n/a                | n/a                | n/a                 | n/a              | n/a              | n/a              |
| BTC-USD  | SAME_ASSET_REGIME         |         1 | 0.00%               | -1.72%           | -1.72%           | -1.72%           | -7.24%             | -7.24%             | 44.52%             | 44.52%             | 44.52%             | 100.00%             | 22.36%           | 22.36%           | 22.36%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |         0 | n/a                 | n/a              | n/a              | n/a              | n/a                | n/a                | n/a                | n/a                | n/a                | n/a                 | n/a              | n/a              | n/a              |
| DOGE-USD | ALL_MATCHES               |        40 | 40.00%              | -4.56%           | 4.90%            | 23.91%           | -9.82%             | -30.87%            | 17.61%             | 24.51%             | 65.37%             | 35.00%              | -11.11%          | 12.19%           | 53.31%           |
| DOGE-USD | SAME_BTC_REGIME           |         0 | n/a                 | n/a              | n/a              | n/a              | n/a                | n/a                | n/a                | n/a                | n/a                | n/a                 | n/a              | n/a              | n/a              |
| DOGE-USD | SAME_ASSET_REGIME         |         8 | 50.00%              | -1.79%           | 24.21%           | 39.63%           | -10.23%            | -32.40%            | 17.63%             | 42.59%             | 59.83%             | 25.00%              | -13.53%          | 11.51%           | 79.43%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |         0 | n/a                 | n/a              | n/a              | n/a              | n/a                | n/a                | n/a                | n/a                | n/a                | n/a                 | n/a              | n/a              | n/a              |
| SOL-USD  | ALL_MATCHES               |        40 | 62.50%              | 3.92%            | 19.14%           | 94.36%           | -11.39%            | -21.63%            | 14.68%             | 30.72%             | 99.16%             | 72.50%              | 22.50%           | 57.85%           | 130.70%          |
| SOL-USD  | SAME_BTC_REGIME           |         0 | n/a                 | n/a              | n/a              | n/a              | n/a                | n/a                | n/a                | n/a                | n/a                | n/a                 | n/a              | n/a              | n/a              |
| SOL-USD  | SAME_ASSET_REGIME         |         8 | 37.50%              | -3.27%           | 2.71%            | 6.80%            | -13.65%            | -17.07%            | 10.66%             | 12.63%             | 15.70%             | 100.00%             | 46.21%           | 55.19%           | 57.89%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |         0 | n/a                 | n/a              | n/a              | n/a              | n/a                | n/a                | n/a                | n/a                | n/a                | n/a                 | n/a              | n/a              | n/a              |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |         5 | 60.00%              | 29.53%           | -6.28%             | 67.25%             | 60.00%              | 26.93%           | 114.38%            |
| BTC-USD  | HISTORICAL_BTC_BULL         |        27 | 70.37%              | 11.53%           | -9.35%             | 25.54%             | 77.78%              | 14.56%           | 93.19%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |         7 | 85.71%              | 12.12%           | -13.32%            | 22.40%             | 28.57%              | -1.95%           | 42.82%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         1 | 0.00%               | -1.72%           | -7.24%             | 44.52%             | 100.00%             | 22.36%           | 44.52%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |         3 | 33.33%              | -7.14%           | -16.21%            | 24.27%             | 0.00%               | -16.66%          | 24.27%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |        31 | 45.16%              | -1.17%           | -8.29%             | 24.54%             | 45.16%              | -6.27%           | 48.87%             |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         6 | 16.67%              | -19.59%          | -24.39%            | 20.84%             | 0.00%               | -28.72%          | 20.84%             |
| SOL-USD  | HISTORICAL_BTC_BEAR         |         5 | 40.00%              | -2.00%           | -11.54%            | 21.08%             | 40.00%              | -22.47%          | 44.56%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |        20 | 70.00%              | 9.26%            | -11.97%            | 56.60%             | 70.00%              | 18.43%           | 115.17%            |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         4 | 75.00%              | 11.11%           | -12.23%            | 24.71%             | 50.00%              | 8.79%            | 71.26%             |
| SOL-USD  | HISTORICAL_BTC_RECOVERY     |        11 | 54.55%              | 3.23%            | -10.39%            | 32.55%             | 100.00%             | 54.31%           | 89.25%             |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        25 | 80.00%              | 11.79%           | -9.92%             | 29.84%             | 72.00%              | 8.80%            | 65.84%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         9 | 66.67%              | 14.13%           | -5.26%             | 27.19%             | 55.56%              | 14.99%           | 103.40%            |
| BTC-USD  | HISTORICAL_ASSET_MIXED        |         1 | 0.00%               | -1.72%           | -7.24%             | 44.52%             | 100.00%             | 22.36%           | 44.52%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         5 | 40.00%              | -4.88%           | -17.07%            | 17.27%             | 60.00%              | 22.65%           | 45.32%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |         8 | 50.00%              | -1.79%           | -10.23%            | 42.59%             | 25.00%              | -13.53%          | 64.06%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |        27 | 40.74%              | -4.02%           | -9.79%             | 24.54%             | 37.04%              | -10.37%          | 41.78%             |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         5 | 20.00%              | -24.68%          | -27.27%            | 11.72%             | 40.00%              | -20.52%          | 16.04%             |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        20 | 65.00%              | 5.07%            | -11.29%            | 20.50%             | 55.00%              | 0.36%            | 63.43%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         9 | 77.78%              | 83.57%           | -11.26%            | 182.90%            | 77.78%              | 106.74%          | 182.90%            |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         1 | 100.00%             | 98.37%           | -0.47%             | 98.37%             | 100.00%             | 158.76%          | 174.79%            |
| SOL-USD  | HISTORICAL_ASSET_MIXED        |         2 | 50.00%              | 0.76%            | -8.82%             | 36.50%             | 100.00%             | 13.06%           | 36.59%             |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         8 | 37.50%              | -3.27%           | -13.65%            | 12.63%             | 100.00%             | 46.21%           | 60.27%             |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD  | NONE                    |                     0 |                           1 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   |
| DOGE-USD | SAME_ASSET_REGIME       |                     0 |                           8 |                         0 |                      8 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD  | SAME_ASSET_REGIME       |                     0 |                           8 |                         0 |                      8 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | YFI-USD         | 2022-04-25   | 86.70%       | RECOVERY              | BEAR                            | SAME_ASSET_ONLY    | BEARISH_30D      | -14.50%      | -21.51%        | 13.63%         | -25.07%      | -25.52%        | 13.63%         |
| DOGE-USD | DOT-USD         | 2023-07-30   | 85.81%       | BULL                  | BEAR                            | SAME_ASSET_ONLY    | HIGH_SPIKE_60D   | 21.64%       | -1.59%         | 21.64%         | 49.86%       | -1.59%         | 85.75%         |
| DOGE-USD | EGLD-USD        | 2023-07-20   | 85.31%       | BULL                  | BEAR                            | SAME_ASSET_ONLY    | EXPLOSIVE_60D    | 57.59%       | 0.00%          | 66.83%         | 148.44%      | 0.00%          | 154.29%        |
| DOGE-USD | OP-USD          | 2026-01-16   | 82.68%       | BEAR                  | BEAR                            | SAME_ASSET_ONLY    | MIXED            | 3.57%        | -4.25%         | 37.84%         | -16.66%      | -27.25%        | 37.84%         |
| DOGE-USD | MATIC-USD       | 2022-04-11   | 82.39%       | BEAR                  | BEAR                            | SAME_ASSET_ONLY    | MIXED            | -7.14%       | -16.21%        | 10.70%         | -10.40%      | -17.51%        | 10.70%         |
| DOGE-USD | EOS-USD         | 2022-04-26   | 82.19%       | RECOVERY              | BEAR                            | SAME_ASSET_ONLY    | BULLISH_30D      | 31.93%       | 0.00%          | 56.82%         | -1.27%       | -2.15%         | 56.82%         |
| DOGE-USD | NEAR-USD        | 2022-05-06   | 82.01%       | BEAR                  | BEAR                            | SAME_ASSET_ONLY    | BEARISH_30D      | -13.38%      | -36.06%        | 0.00%          | -46.25%      | -46.25%        | 0.00%          |
| DOGE-USD | KSM-USD         | 2022-04-24   | 81.88%       | RECOVERY              | BEAR                            | SAME_ASSET_ONLY    | BEARISH_30D      | -26.09%      | -30.83%        | 3.57%          | -34.28%      | -38.46%        | 3.57%          |
| SOL-USD  | ZEC-USD         | 2020-02-26   | 74.30%       | RECOVERY              | RECOVERY                        | SAME_ASSET_ONLY    | EXPLOSIVE_60D    | -1.66%       | -4.67%         | 11.66%         | 57.83%       | -4.67%         | 71.76%         |
| SOL-USD  | ETC-USD         | 2020-08-19   | 73.46%       | BULL                  | RECOVERY                        | SAME_ASSET_ONLY    | MIXED            | -4.88%       | -17.07%        | 9.66%          | 22.65%       | -17.07%        | 45.22%         |
| SOL-USD  | WAVES-USD       | 2023-08-04   | 73.27%       | BULL                  | RECOVERY                        | SAME_ASSET_ONLY    | MIXED            | 2.14%        | -12.76%        | 13.61%         | 15.52%       | -12.76%        | 36.03%         |
| SOL-USD  | ETH-USD         | 2020-02-26   | 71.39%       | RECOVERY              | RECOVERY                        | SAME_ASSET_ONLY    | EXPLOSIVE_60D    | -6.28%       | -8.78%         | 1.23%          | 58.04%       | -8.78%         | 58.04%         |
| SOL-USD  | LRC-USD         | 2020-03-02   | 70.99%       | RECOVERY              | RECOVERY                        | SAME_ASSET_ONLY    | EXPLOSIVE_60D    | 4.44%        | -17.07%        | 20.58%         | 50.29%       | -17.07%        | 50.55%         |
| SOL-USD  | QTUM-USD        | 2020-02-26   | 70.71%       | RECOVERY              | RECOVERY                        | SAME_ASSET_ONLY    | MIXED            | -8.20%       | -13.76%        | 0.78%          | 42.12%       | -13.76%        | 43.18%         |
| SOL-USD  | ADA-USD         | 2020-02-26   | 70.38%       | RECOVERY              | RECOVERY                        | SAME_ASSET_ONLY    | EXPLOSIVE_60D    | 12.31%       | -15.33%        | 12.31%         | 54.31%       | -15.33%        | 66.96%         |
| SOL-USD  | BNB-USD         | 2020-02-26   | 70.00%       | RECOVERY              | RECOVERY                        | SAME_ASSET_ONLY    | BEARISH_30D      | -11.46%      | -13.55%        | 0.70%          | 25.56%       | -13.55%        | 25.56%         |

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the preferred and most stringent filter.
- Below 5 full-regime matches, the selector falls back first to SAME_ASSET_REGIME and then to SAME_BTC_REGIME.
- A fallback is always labelled as less stringent; groups are never combined.
- If every group is below threshold, the result is INSUFFICIENT_REGIME_MATCHES.
- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.
- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.

## Regime definitions

- BULL: price above MA200, MA200 rising, positive 90d trend.
- BEAR: price below MA200, MA200 falling, weak 90d trend.
- RECOVERY: improving 90d trend, but not yet a clean bull structure.
- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.
- MIXED: unclear regime.
- UNKNOWN: not enough historical data.

