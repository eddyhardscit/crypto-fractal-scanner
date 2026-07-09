# Market Regime Match Report

Generated: 2026-07-09 01:47 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       62012    | False                | -15.03%             | -10.12%                  | BEAR               | -15.03%          | -10.12%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -22.92%             | -16.49%                  | BEAR               | -15.03%          | -10.12%               |
| SOL-USD  | BEAR                  |          77.53 | False                | -8.60%              | -18.65%                  | BEAR               | -15.03%          | -10.12%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 65.00%              | 3.39%            | 19.54%           | 43.75%           | -5.48%             | -32.27%            | 15.65%             | 28.81%             | 56.47%             | 72.50%              | 23.09%           | 43.91%           | 64.01%           |
| BTC-USD  | SAME_BTC_REGIME           |        17 | 82.35%              | 22.02%           | 43.58%           | 56.70%           | -4.08%             | -16.61%            | 31.04%             | 55.79%             | 63.45%             | 88.24%              | 32.98%           | 52.55%           | 100.41%          |
| BTC-USD  | SAME_ASSET_REGIME         |        31 | 70.97%              | 3.93%            | 23.09%           | 45.24%           | -5.47%             | -17.41%            | 16.38%             | 29.55%             | 55.79%             | 83.87%              | 28.65%           | 44.37%           | 62.96%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        15 | 80.00%              | 22.02%           | 42.58%           | 57.26%           | -4.08%             | -16.88%            | 31.04%             | 51.87%             | 63.52%             | 86.67%              | 30.28%           | 44.37%           | 106.07%          |
| DOGE-USD | ALL_MATCHES               |        40 | 17.50%              | -18.45%          | -3.90%           | 19.52%           | -26.99%            | -43.86%            | 4.57%              | 12.87%             | 27.40%             | 45.00%              | -5.94%           | 8.58%            | 30.52%           |
| DOGE-USD | SAME_BTC_REGIME           |        33 | 15.15%              | -23.40%          | -4.55%           | 15.83%           | -29.24%            | -44.55%            | 4.39%              | 12.55%             | 27.43%             | 48.48%              | -2.16%           | 10.24%           | 29.14%           |
| DOGE-USD | SAME_ASSET_REGIME         |        34 | 17.65%              | -22.37%          | -4.45%           | 20.31%           | -28.76%            | -44.46%            | 4.57%              | 13.52%             | 27.93%             | 47.06%              | -2.92%           | 11.76%           | 31.91%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        32 | 15.62%              | -22.37%          | -4.52%           | 17.60%           | -29.12%            | -44.65%            | 4.57%              | 12.87%             | 27.81%             | 46.88%              | -2.92%           | 10.75%           | 29.71%           |
| SOL-USD  | ALL_MATCHES               |        40 | 45.00%              | -2.05%           | 7.86%            | 43.75%           | -10.95%            | -29.10%            | 7.58%              | 16.73%             | 55.77%             | 52.50%              | 0.42%            | 32.61%           | 54.79%           |
| SOL-USD  | SAME_BTC_REGIME           |        25 | 60.00%              | 0.89%            | 13.78%           | 44.58%           | -8.61%             | -20.91%            | 14.92%             | 25.47%             | 59.55%             | 64.00%              | 4.19%            | 32.25%           | 53.35%           |
| SOL-USD  | SAME_ASSET_REGIME         |        30 | 53.33%              | 0.50%            | 9.11%            | 46.22%           | -9.11%             | -23.27%            | 8.91%              | 17.78%             | 55.77%             | 60.00%              | 4.95%            | 33.33%           | 54.79%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        21 | 61.90%              | 0.89%            | 11.01%           | 45.24%           | -8.61%             | -17.41%            | 14.92%             | 23.67%             | 55.01%             | 61.90%              | 4.19%            | 21.89%           | 45.30%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        17 | 82.35%              | 22.02%           | -4.08%             | 55.79%             | 88.24%              | 32.98%           | 77.51%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |         9 | 44.44%              | -0.83%           | -4.35%             | 13.54%             | 44.44%              | -5.37%           | 62.47%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |         9 | 66.67%              | 3.65%            | -5.75%             | 16.92%             | 100.00%             | 21.58%           | 73.78%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         5 | 40.00%              | -2.65%           | -5.50%             | 16.48%             | 20.00%              | -20.22%          | 32.20%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        33 | 15.15%              | -23.40%          | -29.24%            | 12.55%             | 48.48%              | -2.16%           | 24.03%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         4 | 50.00%              | 1.69%            | -10.42%            | 19.02%             | 50.00%              | -1.71%           | 30.99%             |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         3 | 0.00%               | -11.71%          | -11.71%            | 6.53%              | 0.00%               | -34.20%          | 6.53%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        25 | 60.00%              | 0.89%            | -8.61%             | 25.47%             | 64.00%              | 4.19%            | 58.38%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |        12 | 16.67%              | -9.88%           | -26.93%            | 5.62%              | 16.67%              | -5.05%           | 5.62%              |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         3 | 33.33%              | -2.54%           | -7.18%             | 89.21%             | 100.00%             | 33.69%           | 127.37%            |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        31 | 70.97%              | 3.93%            | -5.47%             | 29.55%             | 83.87%              | 28.65%           | 75.04%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -11.76%          | -11.76%            | 13.48%             | 0.00%               | -24.75%          | 13.48%             |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         1 | 100.00%             | 4.40%            | -3.37%             | 8.82%              | 100.00%             | 21.58%           | 33.10%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         5 | 60.00%              | 2.98%            | -5.50%             | 32.20%             | 40.00%              | -12.07%          | 76.83%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        34 | 17.65%              | -22.37%          | -28.76%            | 13.52%             | 47.06%              | -2.92%           | 24.30%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         3 | 33.33%              | -12.18%          | -17.30%            | 8.26%              | 66.67%              | 5.41%            | 15.40%             |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION |         1 | 0.00%               | -18.56%          | -18.58%            | 0.00%              | 0.00%               | -8.83%           | 0.00%              |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         2 | 0.00%               | -6.05%           | -7.15%             | 7.22%              | 0.00%               | -24.95%          | 7.22%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        30 | 53.33%              | 0.50%            | -9.11%             | 17.78%             | 60.00%              | 4.95%            | 61.45%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -18.82%          | -28.28%            | 3.76%              | 33.33%              | -5.68%           | 3.76%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         3 | 0.00%               | -10.79%          | -27.41%            | 0.55%              | 0.00%               | -12.07%          | 0.55%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         4 | 50.00%              | 5.95%            | -17.25%            | 37.36%             | 50.00%              | 26.06%           | 93.44%             |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-14   | 87.89%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 55.58%       | -16.08%        | 55.79%         | 30.28%       | -16.08%        | 133.75%        |
| BTC-USD  | KSM-USD         | 2022-03-05   | 86.82%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -8.02%       | -9.39%         | 13.41%         | 19.28%       | -9.39%         | 31.79%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 85.20%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | LTC-USD         | 2020-01-04   | 84.72%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -0.80%       | -6.74%         | 16.51%         | 2.51%        | -6.74%         | 16.51%         |
| BTC-USD  | BAT-USD         | 2019-09-29   | 84.32%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 31.04%       | -4.08%         | 31.04%         | 25.86%       | -4.08%         | 61.96%         |
| BTC-USD  | OMG-USD         | 2020-01-07   | 84.25%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 79.99%       | 0.00%          | 79.99%         | 195.80%      | 0.00%          | 253.59%        |
| BTC-USD  | ENJ-USD         | 2022-03-02   | 84.09%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.40%      | -33.49%        | 0.00%          | 12.28%       | -33.49%        | 13.74%         |
| BTC-USD  | ADA-USD         | 2020-01-07   | 83.98%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 58.37%       | 0.00%          | 64.15%         | 140.87%      | 0.00%          | 179.32%        |
| BTC-USD  | QTUM-USD        | 2020-01-07   | 83.98%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 16.10%       | 0.00%          | 28.06%         | 33.45%       | 0.00%          | 45.51%         |
| BTC-USD  | XLM-USD         | 2020-01-07   | 83.71%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| DOGE-USD | VET-USD         | 2022-02-22   | 87.78%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | DASH-USD        | 2022-02-20   | 87.73%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 86.74%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XLM-USD         | 2019-09-29   | 86.63%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.26%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | 1INCH-USD       | 2022-02-22   | 86.02%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.62%      | -42.19%        | 0.00%          | -20.09%      | -42.19%        | 0.00%          |
| DOGE-USD | THETA-USD       | 2022-02-24   | 85.62%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 1.59%        | -8.56%         | 23.35%         | 14.81%       | -8.85%         | 24.03%         |
| DOGE-USD | XTZ-USD         | 2025-12-06   | 85.60%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.41%      | -12.14%        | 4.26%          | -2.16%       | -12.14%        | 4.26%          |
| DOGE-USD | CHZ-USD         | 2022-02-19   | 85.17%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -9.76%       | -23.41%        | 13.85%         | 6.31%        | -23.41%        | 13.85%         |
| DOGE-USD | OP-USD          | 2025-12-02   | 85.13%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -4.42%       | -15.36%        | 14.28%         | 35.71%       | -15.36%        | 43.20%         |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 78.48%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | LRC-USD         | 2018-09-19   | 77.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| SOL-USD  | APT-USD         | 2024-09-01   | 77.43%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.92%        | -11.47%        | 6.42%          | -34.40%      | -34.40%        | 6.42%          |
| SOL-USD  | TRX-USD         | 2018-09-19   | 77.12%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 55.01%       | 0.00%          | 55.01%         | 32.25%       | 0.00%          | 58.38%         |
| SOL-USD  | XLM-USD         | 2020-01-07   | 76.79%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| SOL-USD  | OMG-USD         | 2025-12-01   | 76.68%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -5.35%       | -7.41%         | 2.96%          | 13.31%       | -7.41%         | 15.03%         |
| SOL-USD  | CRV-USD         | 2025-11-30   | 76.65%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.12%      | -14.42%        | 5.41%          | 5.96%        | -14.42%        | 5.96%          |
| SOL-USD  | ZIL-USD         | 2018-09-16   | 76.41%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 7.24%        | -17.41%        | 18.30%         | -9.96%       | -19.41%        | 18.30%         |
| SOL-USD  | FIL-USD         | 2018-10-03   | 76.28%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.67%        | -10.34%        | 5.32%          | -5.02%       | -10.34%        | 15.14%         |
| SOL-USD  | SOL-USD         | 2025-12-04   | 76.03%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -7.51%       | -10.44%        | 9.16%          | 6.95%        | -10.44%        | 10.43%         |

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

