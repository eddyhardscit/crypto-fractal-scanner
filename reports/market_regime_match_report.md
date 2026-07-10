# Market Regime Match Report

Generated: 2026-07-10 13:27 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       64125.8  | False                | -12.22%             | -10.27%                  | BEAR               | -12.22%          | -10.27%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -20.54%             | -16.68%                  | BEAR               | -12.22%          | -10.27%               |
| SOL-USD  | BEAR                  |          78.85 | False                | -7.18%              | -18.73%                  | BEAR               | -12.22%          | -10.27%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 77.50%              | 9.01%            | 22.56%           | 43.75%           | -3.17%             | -28.94%            | 18.35%             | 34.02%             | 62.62%             | 75.00%              | 30.82%           | 51.81%           | 65.33%           |
| BTC-USD  | SAME_BTC_REGIME           |        17 | 100.00%             | 25.70%           | 43.58%           | 67.02%           | 0.00%              | -4.32%             | 37.70%             | 62.58%             | 70.49%             | 94.12%              | 42.97%           | 52.55%           | 89.02%           |
| BTC-USD  | SAME_ASSET_REGIME         |        29 | 86.21%              | 14.92%           | 24.17%           | 47.87%           | -1.26%             | -9.42%             | 21.60%             | 34.23%             | 62.89%             | 89.66%              | 40.39%           | 53.88%           | 76.40%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        15 | 100.00%             | 22.02%           | 37.45%           | 71.35%           | 0.00%              | -4.53%             | 34.23%             | 55.26%             | 73.66%             | 93.33%              | 40.39%           | 49.94%           | 106.30%          |
| DOGE-USD | ALL_MATCHES               |        40 | 15.00%              | -22.37%          | -7.70%           | 7.45%            | -28.67%            | -44.76%            | 4.32%              | 12.65%             | 24.59%             | 42.50%              | -6.79%           | 11.78%           | 25.66%           |
| DOGE-USD | SAME_BTC_REGIME           |        32 | 9.38%               | -26.01%          | -15.02%          | -2.03%           | -30.74%            | -44.84%            | 3.41%              | 10.47%             | 24.28%             | 40.62%              | -6.79%           | 10.58%           | 23.65%           |
| DOGE-USD | SAME_ASSET_REGIME         |        35 | 14.29%              | -23.93%          | -7.40%           | 4.57%            | -29.00%            | -44.81%            | 4.26%              | 11.74%             | 25.63%             | 42.86%              | -5.40%           | 13.54%           | 31.24%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        31 | 9.68%               | -26.97%          | -13.48%          | -1.76%           | -30.51%            | -44.85%            | 3.48%              | 10.62%             | 24.39%             | 38.71%              | -8.19%           | 10.93%           | 24.54%           |
| SOL-USD  | ALL_MATCHES               |        40 | 37.50%              | -2.05%           | 9.05%            | 43.75%           | -12.77%            | -30.98%            | 7.79%              | 22.56%             | 55.77%             | 55.00%              | 5.83%            | 32.43%           | 52.68%           |
| SOL-USD  | SAME_BTC_REGIME           |        25 | 52.00%              | 0.89%            | 16.09%           | 44.58%           | -8.00%             | -22.16%            | 11.93%             | 29.71%             | 59.55%             | 76.00%              | 8.91%            | 32.98%           | 53.35%           |
| SOL-USD  | SAME_ASSET_REGIME         |        27 | 44.44%              | -0.45%           | 13.80%           | 49.15%           | -9.99%             | -23.47%            | 10.51%             | 23.53%             | 58.04%             | 66.67%              | 8.26%            | 33.34%           | 52.02%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        20 | 50.00%              | 0.22%            | 12.80%           | 46.22%           | -8.81%             | -19.84%            | 11.22%             | 27.59%             | 55.77%             | 75.00%              | 8.58%            | 32.43%           | 46.16%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        17 | 100.00%             | 25.70%           | 0.00%              | 62.58%             | 94.12%              | 42.97%           | 78.05%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |         9 | 44.44%              | -2.75%           | -8.75%             | 9.98%              | 44.44%              | -3.75%           | 83.14%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |        10 | 80.00%              | 4.33%            | -4.56%             | 17.31%             | 100.00%             | 25.15%           | 71.54%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         4 | 50.00%              | -8.18%           | -24.68%            | 12.51%             | 0.00%               | -29.87%          | 12.51%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        32 | 9.38%               | -26.01%          | -30.74%            | 10.47%             | 40.62%              | -6.79%           | 22.67%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         3 | 33.33%              | -8.75%           | -14.04%            | 14.60%             | 33.33%              | -9.16%           | 15.40%             |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION |         3 | 66.67%              | 18.71%           | -2.40%             | 23.10%             | 100.00%             | 21.64%           | 115.31%            |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         2 | 0.00%               | -18.86%          | -18.86%            | 3.86%              | 0.00%               | -38.05%          | 3.86%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        25 | 52.00%              | 0.89%            | -8.00%             | 29.71%             | 76.00%              | 8.91%            | 58.38%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |        10 | 0.00%               | -14.80%          | -28.59%            | 1.40%              | 0.00%               | -8.45%           | 1.40%              |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         3 | 66.67%              | 17.86%           | -5.48%             | 97.60%             | 100.00%             | 50.78%           | 127.37%            |
| SOL-USD  | HISTORICAL_BTC_RECOVERY     |         2 | 0.00%               | -16.77%          | -29.03%            | 11.14%             | 0.00%               | -35.08%          | 11.14%             |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        29 | 86.21%              | 14.92%           | -1.26%             | 34.23%             | 89.66%              | 40.39%           | 78.05%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         4 | 25.00%              | -15.12%          | -20.59%            | 8.51%              | 25.00%              | -12.33%          | 47.44%             |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         2 | 100.00%             | 21.29%           | -3.17%             | 30.83%             | 100.00%             | 34.70%           | 69.81%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         5 | 60.00%              | 5.95%            | -11.70%            | 32.20%             | 20.00%              | -24.31%          | 32.20%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        35 | 14.29%              | -23.93%          | -29.00%            | 11.74%             | 42.86%              | -5.40%           | 26.61%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         3 | 33.33%              | -12.18%          | -17.30%            | 8.26%              | 66.67%              | 5.41%            | 15.40%             |
| DOGE-USD | HISTORICAL_ASSET_MIXED        |         1 | 0.00%               | -8.75%           | -14.04%            | 12.94%             | 0.00%               | -9.16%           | 12.94%             |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         1 | 0.00%               | -11.71%          | -11.71%            | 5.15%              | 0.00%               | -34.20%          | 5.15%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        27 | 44.44%              | -0.45%           | -9.99%             | 23.53%             | 66.67%              | 8.26%            | 61.61%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         4 | 0.00%               | -19.12%          | -29.62%            | 0.21%              | 25.00%              | -6.73%           | 0.21%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         3 | 0.00%               | -10.79%          | -27.41%            | 0.55%              | 0.00%               | -12.07%          | 0.55%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 50.00%              | 3.47%            | -17.29%            | 28.80%             | 50.00%              | 10.69%           | 67.73%             |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-19   | 88.94%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| BTC-USD  | KSM-USD         | 2022-03-10   | 86.41%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 11.02%       | -4.93%         | 16.96%         | 14.38%       | -4.93%         | 37.01%         |
| BTC-USD  | XLM-USD         | 2020-01-07   | 85.76%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 85.70%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | TRX-USD         | 2020-01-07   | 85.35%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 22.02%       | 0.00%          | 33.95%         | 32.98%       | 0.00%          | 48.70%         |
| BTC-USD  | EOS-USD         | 2020-01-07   | 84.94%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 7.83%        | 0.00%          | 25.64%         | 7.27%        | 0.00%          | 25.64%         |
| BTC-USD  | MKR-USD         | 2021-07-21   | 84.90%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 29.66%       | -0.21%         | 38.63%         | 12.58%       | -6.23%         | 38.63%         |
| BTC-USD  | ADA-USD         | 2020-01-07   | 84.41%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 58.37%       | 0.00%          | 64.15%         | 140.87%      | 0.00%          | 179.32%        |
| BTC-USD  | OMG-USD         | 2020-01-07   | 84.32%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 79.99%       | 0.00%          | 79.99%         | 195.80%      | 0.00%          | 253.59%        |
| BTC-USD  | SOL-USD         | 2022-03-10   | 84.14%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 25.70%       | 0.00%          | 37.70%         | 40.39%       | 0.00%          | 51.21%         |
| DOGE-USD | DASH-USD        | 2022-02-20   | 88.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | XTZ-USD         | 2025-12-06   | 87.29%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.41%      | -12.14%        | 4.26%          | -2.16%       | -12.14%        | 4.26%          |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 87.26%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XLM-USD         | 2019-09-29   | 87.21%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | CHZ-USD         | 2022-02-24   | 86.76%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -19.17%      | -28.71%        | 5.97%          | 11.61%       | -28.71%        | 22.22%         |
| DOGE-USD | VET-USD         | 2022-02-22   | 86.54%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | 1INCH-USD       | 2022-02-22   | 86.45%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.62%      | -42.19%        | 0.00%          | -20.09%      | -42.19%        | 0.00%          |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.43%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | THETA-USD       | 2022-02-24   | 86.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 1.59%        | -8.56%         | 23.35%         | 14.81%       | -8.85%         | 24.03%         |
| DOGE-USD | ENJ-USD         | 2022-02-25   | 86.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -16.55%      | -33.46%        | 5.00%          | 1.45%        | -33.46%        | 5.00%          |
| SOL-USD  | TRX-USD         | 2018-09-19   | 79.80%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 55.01%       | 0.00%          | 55.01%         | 32.25%       | 0.00%          | 58.38%         |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 79.73%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | XLM-USD         | 2020-01-07   | 79.40%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| SOL-USD  | LRC-USD         | 2018-09-19   | 78.03%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| SOL-USD  | ENJ-USD         | 2018-09-19   | 77.84%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | -16.11%      | -19.37%        | 5.11%          | 93.16%       | -38.09%        | 93.16%         |
| SOL-USD  | NEAR-USD        | 2025-12-01   | 77.39%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 6.36%        | -9.61%         | 16.07%         | 21.89%       | -9.61%         | 24.08%         |
| SOL-USD  | SOL-USD         | 2025-12-04   | 77.31%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -7.51%       | -10.44%        | 9.16%          | 6.95%        | -10.44%        | 10.43%         |
| SOL-USD  | XRP-USD         | 2020-01-07   | 77.29%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 9.73%        | 0.00%          | 25.47%         | 5.71%        | 0.00%          | 25.47%         |
| SOL-USD  | APT-USD         | 2024-09-01   | 76.91%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.92%        | -11.47%        | 6.42%          | -34.40%      | -34.40%        | 6.42%          |
| SOL-USD  | ONE-USD         | 2020-04-16   | 75.69%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.89%        | -24.91%        | 11.93%         | -10.01%      | -24.91%        | 11.93%         |

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the cleanest filter, but it needs enough matches to matter.
- If SAME_BTC_AND_ASSET_REGIME has fewer than 5 matches, treat it as useful context, not a strong statistic.
- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.
- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.

## Regime definitions

- BULL: price above MA200, MA200 rising, positive 90d trend.
- BEAR: price below MA200, MA200 falling, weak 90d trend.
- RECOVERY: improving 90d trend, but not yet a clean bull structure.
- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.
- MIXED: unclear regime.
- UNKNOWN: not enough historical data.

