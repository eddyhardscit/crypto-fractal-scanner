# Market Regime Match Report

Generated: 2026-07-10 01:12 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       63022.2  | False                | -13.73%             | -10.12%                  | BEAR               | -13.73%          | -10.12%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -21.74%             | -16.44%                  | BEAR               | -13.73%          | -10.12%               |
| SOL-USD  | BEAR                  |          78.11 | False                | -8.05%              | -18.52%                  | BEAR               | -13.73%          | -10.12%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 72.50%              | 6.89%            | 22.56%           | 43.75%           | -3.94%             | -32.41%            | 16.94%             | 32.64%             | 62.62%             | 72.50%              | 21.61%           | 45.40%           | 63.22%           |
| BTC-USD  | SAME_BTC_REGIME           |        18 | 100.00%             | 23.86%           | 40.45%           | 64.86%           | 0.00%              | -6.02%             | 34.09%             | 58.92%             | 68.90%             | 94.44%              | 41.68%           | 53.55%           | 93.67%           |
| BTC-USD  | SAME_ASSET_REGIME         |        30 | 80.00%              | 12.97%           | 25.32%           | 46.56%           | -2.89%             | -9.92%             | 19.88%             | 34.16%             | 62.73%             | 86.67%              | 30.82%           | 45.61%           | 69.24%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        16 | 100.00%             | 23.86%           | 34.59%           | 69.18%           | 0.00%              | -4.50%             | 34.09%             | 51.61%             | 72.07%             | 93.75%              | 36.92%           | 47.97%           | 97.66%           |
| DOGE-USD | ALL_MATCHES               |        40 | 12.50%              | -20.25%          | -4.52%           | 2.99%            | -28.61%            | -43.86%            | 4.88%              | 11.33%             | 23.46%             | 42.50%              | -6.79%           | 10.58%           | 21.93%           |
| DOGE-USD | SAME_BTC_REGIME           |        31 | 6.45%               | -26.97%          | -13.48%          | -2.33%           | -30.96%            | -44.75%            | 4.26%              | 10.33%             | 23.35%             | 41.94%              | -5.40%           | 9.13%            | 15.56%           |
| DOGE-USD | SAME_ASSET_REGIME         |        34 | 11.76%              | -24.71%          | -5.98%           | 0.71%            | -29.12%            | -44.46%            | 4.57%              | 10.78%             | 24.08%             | 44.12%              | -4.54%           | 12.10%           | 23.67%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        30 | 6.67%               | -27.25%          | -11.95%          | -2.27%           | -30.74%            | -44.76%            | 4.32%              | 10.33%             | 23.46%             | 40.00%              | -6.79%           | 9.20%            | 16.46%           |
| SOL-USD  | ALL_MATCHES               |        40 | 42.50%              | -1.54%           | 11.03%           | 43.75%           | -10.39%            | -30.98%            | 7.79%              | 22.56%             | 55.77%             | 52.50%              | 0.81%            | 24.48%           | 52.68%           |
| SOL-USD  | SAME_BTC_REGIME           |        24 | 62.50%              | 3.64%            | 19.32%           | 44.75%           | -5.08%             | -18.60%            | 15.09%             | 32.20%             | 60.31%             | 66.67%              | 10.13%           | 34.93%           | 53.48%           |
| SOL-USD  | SAME_ASSET_REGIME         |        28 | 50.00%              | 0.14%            | 15.66%           | 48.17%           | -7.71%             | -20.49%            | 11.22%             | 22.56%             | 57.28%             | 60.71%              | 6.46%            | 32.61%           | 51.71%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        19 | 63.16%              | 0.92%            | 21.98%           | 47.20%           | -6.43%             | -17.32%            | 14.92%             | 32.57%             | 56.53%             | 63.16%              | 6.95%            | 27.07%           | 47.02%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        18 | 100.00%             | 23.86%           | 0.00%              | 58.92%             | 94.44%              | 41.68%           | 77.34%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |         8 | 37.50%              | -11.59%          | -12.33%            | 9.57%              | 37.50%              | -14.20%          | 53.66%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |         9 | 66.67%              | 3.65%            | -5.75%             | 16.92%             | 100.00%             | 21.58%           | 73.78%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         5 | 40.00%              | -3.60%           | -11.70%            | 16.38%             | 0.00%               | -24.31%          | 16.38%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        31 | 6.45%               | -26.97%          | -30.96%            | 10.33%             | 41.94%              | -5.40%           | 18.89%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         3 | 33.33%              | -8.75%           | -14.04%            | 14.60%             | 33.33%              | -9.16%           | 15.40%             |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION |         3 | 66.67%              | 18.71%           | -2.40%             | 23.10%             | 100.00%             | 21.64%           | 115.31%            |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         3 | 0.00%               | -11.71%          | -11.71%            | 6.53%              | 0.00%               | -34.20%          | 6.53%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        24 | 62.50%              | 3.64%            | -5.08%             | 32.20%             | 66.67%              | 10.13%           | 60.27%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |         9 | 0.00%               | -10.79%          | -28.90%            | 1.50%              | 0.00%               | -7.77%           | 1.50%              |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         5 | 40.00%              | -2.54%           | -7.18%             | 21.60%             | 100.00%             | 33.69%           | 80.74%             |
| SOL-USD  | HISTORICAL_BTC_RECOVERY     |         2 | 0.00%               | -16.77%          | -29.03%            | 11.14%             | 0.00%               | -35.08%          | 11.14%             |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        30 | 80.00%              | 12.97%           | -2.89%             | 34.16%             | 86.67%              | 30.82%           | 71.82%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -11.76%          | -12.91%            | 8.72%              | 0.00%               | -23.03%          | 8.72%              |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         1 | 100.00%             | 4.40%            | -3.37%             | 8.82%              | 100.00%             | 21.58%           | 33.10%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 66.67%              | 4.46%            | -10.12%            | 30.00%             | 33.33%              | -22.26%          | 65.67%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        34 | 11.76%              | -24.71%          | -29.12%            | 10.78%             | 44.12%              | -4.54%           | 24.30%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         3 | 33.33%              | -12.18%          | -17.30%            | 8.26%              | 66.67%              | 5.41%            | 15.40%             |
| DOGE-USD | HISTORICAL_ASSET_MIXED        |         1 | 0.00%               | -8.75%           | -14.04%            | 12.94%             | 0.00%               | -9.16%           | 12.94%             |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         2 | 0.00%               | -6.05%           | -7.15%             | 7.22%              | 0.00%               | -24.95%          | 7.22%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        28 | 50.00%              | 0.14%            | -7.71%             | 22.56%             | 60.71%              | 6.46%            | 60.00%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         4 | 0.00%               | -19.12%          | -29.62%            | 0.21%              | 25.00%              | -6.73%           | 0.21%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         2 | 0.00%               | -8.70%           | -29.28%            | 0.83%              | 0.00%               | -7.90%           | 0.83%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 50.00%              | 3.47%            | -17.29%            | 28.80%             | 50.00%              | 10.69%           | 67.73%             |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-19   | 87.73%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| BTC-USD  | KSM-USD         | 2022-03-10   | 86.21%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 11.02%       | -4.93%         | 16.96%         | 14.38%       | -4.93%         | 37.01%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 85.71%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | LTC-USD         | 2020-01-05   | 84.89%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 4.68%        | -3.92%         | 20.03%         | 8.79%        | -3.92%         | 20.03%         |
| BTC-USD  | XLM-USD         | 2020-01-07   | 84.84%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| BTC-USD  | MKR-USD         | 2021-07-21   | 84.83%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 29.66%       | -0.21%         | 38.63%         | 12.58%       | -6.23%         | 38.63%         |
| BTC-USD  | TRX-USD         | 2020-01-07   | 84.53%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 22.02%       | 0.00%          | 33.95%         | 32.98%       | 0.00%          | 48.70%         |
| BTC-USD  | OMG-USD         | 2020-01-07   | 84.49%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 79.99%       | 0.00%          | 79.99%         | 195.80%      | 0.00%          | 253.59%        |
| BTC-USD  | ADA-USD         | 2020-01-07   | 84.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 58.37%       | 0.00%          | 64.15%         | 140.87%      | 0.00%          | 179.32%        |
| BTC-USD  | QTUM-USD        | 2020-01-07   | 84.21%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 16.10%       | 0.00%          | 28.06%         | 33.45%       | 0.00%          | 45.51%         |
| DOGE-USD | DASH-USD        | 2022-02-20   | 88.64%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | VET-USD         | 2022-02-22   | 87.39%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 87.31%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XLM-USD         | 2019-09-29   | 87.24%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | 1INCH-USD       | 2022-02-22   | 86.51%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.62%      | -42.19%        | 0.00%          | -20.09%      | -42.19%        | 0.00%          |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.49%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | CHZ-USD         | 2022-02-24   | 86.13%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -19.17%      | -28.71%        | 5.97%          | 11.61%       | -28.71%        | 22.22%         |
| DOGE-USD | THETA-USD       | 2022-02-24   | 86.09%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 1.59%        | -8.56%         | 23.35%         | 14.81%       | -8.85%         | 24.03%         |
| DOGE-USD | XTZ-USD         | 2025-12-06   | 85.94%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.41%      | -12.14%        | 4.26%          | -2.16%       | -12.14%        | 4.26%          |
| DOGE-USD | ENJ-USD         | 2022-02-25   | 85.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -16.55%      | -33.46%        | 5.00%          | 1.45%        | -33.46%        | 5.00%          |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 79.49%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | TRX-USD         | 2018-09-19   | 79.01%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 55.01%       | 0.00%          | 55.01%         | 32.25%       | 0.00%          | 58.38%         |
| SOL-USD  | LRC-USD         | 2018-09-19   | 78.38%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| SOL-USD  | XLM-USD         | 2020-01-07   | 78.14%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| SOL-USD  | APT-USD         | 2024-09-01   | 77.71%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.92%        | -11.47%        | 6.42%          | -34.40%      | -34.40%        | 6.42%          |
| SOL-USD  | NEAR-USD        | 2025-12-01   | 77.66%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 6.36%        | -9.61%         | 16.07%         | 21.89%       | -9.61%         | 24.08%         |
| SOL-USD  | ENJ-USD         | 2018-09-19   | 77.20%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | -16.11%      | -19.37%        | 5.11%          | 93.16%       | -38.09%        | 93.16%         |
| SOL-USD  | SOL-USD         | 2025-12-04   | 76.82%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -7.51%       | -10.44%        | 9.16%          | 6.95%        | -10.44%        | 10.43%         |
| SOL-USD  | XRP-USD         | 2020-01-07   | 76.28%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 9.73%        | 0.00%          | 25.47%         | 5.71%        | 0.00%          | 25.47%         |
| SOL-USD  | LINK-USD        | 2025-12-01   | 75.73%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -0.45%       | -6.43%         | 10.51%         | 15.46%       | -6.43%         | 15.46%         |

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

