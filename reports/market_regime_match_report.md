# Market Regime Match Report

Generated: 2026-07-08 08:40 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       61875    | False                | -13.78%             | -10.26%                  | BEAR               | -13.78%          | -10.26%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -23.24%             | -16.76%                  | BEAR               | -13.78%          | -10.26%               |
| SOL-USD  | BEAR                  |          76.86 | False                | -7.73%              | -18.95%                  | BEAR               | -13.78%          | -10.26%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 65.00%              | 3.53%            | 22.56%           | 43.75%           | -4.91%             | -32.77%            | 16.43%             | 31.33%             | 50.89%             | 72.50%              | 21.61%           | 43.91%           | 64.01%           |
| BTC-USD  | SAME_BTC_REGIME           |        18 | 83.33%              | 25.67%           | 42.67%           | 49.49%           | -2.14%             | -16.48%            | 32.50%             | 49.75%             | 62.70%             | 88.89%              | 31.63%           | 50.73%           | 93.85%           |
| BTC-USD  | SAME_ASSET_REGIME         |        30 | 70.00%              | 4.72%            | 23.63%           | 40.45%           | -4.91%             | -18.88%            | 16.43%             | 30.30%             | 48.73%             | 83.33%              | 25.20%           | 43.13%           | 62.17%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        15 | 80.00%              | 22.02%           | 35.48%           | 51.45%           | -4.08%             | -16.88%            | 31.04%             | 43.93%             | 59.86%             | 86.67%              | 25.86%           | 38.45%           | 50.45%           |
| DOGE-USD | ALL_MATCHES               |        40 | 20.00%              | -19.94%          | -1.66%           | 19.52%           | -26.99%            | -43.86%            | 4.32%              | 13.96%             | 27.40%             | 47.50%              | -2.92%           | 12.90%           | 32.92%           |
| DOGE-USD | SAME_BTC_REGIME           |        32 | 15.62%              | -26.01%          | -4.52%           | 17.60%           | -30.10%            | -44.65%            | 3.41%              | 11.20%             | 27.81%             | 50.00%              | -0.98%           | 10.75%           | 29.71%           |
| DOGE-USD | SAME_ASSET_REGIME         |        35 | 20.00%              | -23.40%          | -2.05%           | 20.18%           | -28.51%            | -44.36%            | 4.26%              | 14.07%             | 27.84%             | 51.43%              | 0.20%            | 15.19%           | 34.47%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        31 | 16.13%              | -26.97%          | -4.49%           | 19.38%           | -29.24%            | -44.75%            | 3.48%              | 12.09%             | 28.19%             | 48.39%              | -2.16%           | 11.25%           | 30.28%           |
| SOL-USD  | ALL_MATCHES               |        40 | 47.50%              | -1.54%           | 10.05%           | 43.75%           | -9.97%             | -29.10%            | 8.30%              | 21.29%             | 55.77%             | 55.00%              | 1.16%            | 32.61%           | 54.79%           |
| SOL-USD  | SAME_BTC_REGIME           |        26 | 61.54%              | 3.63%            | 14.64%           | 44.41%           | -6.09%             | -20.32%            | 15.66%             | 27.98%             | 58.80%             | 65.38%              | 4.95%            | 29.66%           | 53.21%           |
| SOL-USD  | SAME_ASSET_REGIME         |        30 | 56.67%              | 0.78%            | 10.69%           | 46.22%           | -7.30%             | -23.12%            | 12.73%             | 22.87%             | 55.77%             | 63.33%              | 5.83%            | 33.33%           | 54.79%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        22 | 63.64%              | 3.63%            | 13.95%           | 43.65%           | -6.09%             | -17.28%            | 15.66%             | 25.02%             | 54.31%             | 63.64%              | 4.95%            | 19.95%           | 45.07%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        18 | 83.33%              | 25.67%           | -2.14%             | 49.75%             | 88.89%              | 31.63%           | 77.34%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |         9 | 44.44%              | -0.83%           | -4.35%             | 13.54%             | 44.44%              | -5.37%           | 62.47%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |         8 | 62.50%              | 2.78%            | -4.88%             | 17.62%             | 100.00%             | 20.18%           | 74.58%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         5 | 40.00%              | -3.60%           | -10.08%            | 16.48%             | 20.00%              | -23.70%          | 32.20%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        32 | 15.62%              | -26.01%          | -30.10%            | 11.20%             | 50.00%              | -0.98%           | 24.12%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         3 | 66.67%              | 15.56%           | -3.55%             | 21.78%             | 33.33%              | -8.83%           | 45.73%             |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION |         2 | 50.00%              | 8.67%            | -5.24%             | 16.31%             | 100.00%             | 77.65%           | 128.13%            |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         3 | 0.00%               | -11.71%          | -11.71%            | 6.53%              | 0.00%               | -34.20%          | 6.53%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        26 | 61.54%              | 3.63%            | -6.09%             | 27.98%             | 65.38%              | 4.95%            | 53.71%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |        11 | 18.18%              | -8.96%           | -27.41%            | 5.35%              | 18.18%              | -5.68%           | 5.35%              |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         3 | 33.33%              | -2.54%           | -7.18%             | 89.21%             | 100.00%             | 33.69%           | 127.37%            |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        30 | 70.00%              | 4.72%            | -4.91%             | 30.30%             | 83.33%              | 25.20%           | 74.43%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -11.76%          | -11.76%            | 13.48%             | 0.00%               | -24.75%          | 13.48%             |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         2 | 100.00%             | 25.64%           | -1.68%             | 39.97%             | 100.00%             | 81.53%           | 116.04%            |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         5 | 60.00%              | 2.98%            | -8.55%             | 32.20%             | 40.00%              | -20.22%          | 76.83%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        35 | 20.00%              | -23.40%          | -28.51%            | 14.07%             | 51.43%              | 0.20%            | 37.49%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         2 | 50.00%              | -4.75%           | -21.32%            | 12.19%             | 50.00%              | -7.05%           | 14.20%             |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION |         1 | 0.00%               | -18.56%          | -18.58%            | 0.00%              | 0.00%               | -8.83%           | 0.00%              |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         2 | 0.00%               | -6.05%           | -7.15%             | 7.22%              | 0.00%               | -24.95%          | 7.22%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        30 | 56.67%              | 0.78%            | -7.30%             | 22.87%             | 63.33%              | 5.83%            | 61.45%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -18.82%          | -28.28%            | 3.76%              | 33.33%              | -5.68%           | 3.76%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         3 | 0.00%               | -10.79%          | -27.41%            | 0.55%              | 0.00%               | -12.07%          | 0.55%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         4 | 50.00%              | 5.95%            | -17.25%            | 37.36%             | 50.00%              | 26.06%           | 93.44%             |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-14   | 87.88%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 55.58%       | -16.08%        | 55.79%         | 30.28%       | -16.08%        | 133.75%        |
| BTC-USD  | KSM-USD         | 2022-03-05   | 86.85%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -8.02%       | -9.39%         | 13.41%         | 19.28%       | -9.39%         | 31.79%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 85.20%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | BAT-USD         | 2019-09-29   | 84.30%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 31.04%       | -4.08%         | 31.04%         | 25.86%       | -4.08%         | 61.96%         |
| BTC-USD  | OMG-USD         | 2020-01-07   | 84.25%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 79.99%       | 0.00%          | 79.99%         | 195.80%      | 0.00%          | 253.59%        |
| BTC-USD  | ENJ-USD         | 2022-03-02   | 84.10%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.40%      | -33.49%        | 0.00%          | 12.28%       | -33.49%        | 13.74%         |
| BTC-USD  | QTUM-USD        | 2020-01-07   | 83.98%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 16.10%       | 0.00%          | 28.06%         | 33.45%       | 0.00%          | 45.51%         |
| BTC-USD  | XLM-USD         | 2020-01-07   | 83.70%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| BTC-USD  | ZIL-USD         | 2018-09-16   | 83.62%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 7.24%        | -17.41%        | 18.30%         | -9.96%       | -19.41%        | 18.30%         |
| BTC-USD  | EOS-USD         | 2022-03-07   | 83.62%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 3.13%        | -5.47%         | 10.35%         | 43.45%       | -5.47%         | 43.45%         |
| DOGE-USD | VET-USD         | 2022-02-22   | 87.74%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | DASH-USD        | 2022-02-20   | 87.66%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 86.69%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XLM-USD         | 2019-09-29   | 86.53%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.19%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | 1INCH-USD       | 2022-02-22   | 85.97%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.62%      | -42.19%        | 0.00%          | -20.09%      | -42.19%        | 0.00%          |
| DOGE-USD | THETA-USD       | 2022-02-24   | 85.60%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 1.59%        | -8.56%         | 23.35%         | 14.81%       | -8.85%         | 24.03%         |
| DOGE-USD | XTZ-USD         | 2025-12-06   | 85.51%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.41%      | -12.14%        | 4.26%          | -2.16%       | -12.14%        | 4.26%          |
| DOGE-USD | CHZ-USD         | 2022-02-19   | 85.17%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -9.76%       | -23.41%        | 13.85%         | 6.31%        | -23.41%        | 13.85%         |
| DOGE-USD | OP-USD          | 2025-12-02   | 85.11%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -4.42%       | -15.36%        | 14.28%         | 35.71%       | -15.36%        | 43.20%         |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 78.52%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | LRC-USD         | 2018-09-19   | 77.84%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| SOL-USD  | TRX-USD         | 2018-09-19   | 77.09%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 55.01%       | 0.00%          | 55.01%         | 32.25%       | 0.00%          | 58.38%         |
| SOL-USD  | XLM-USD         | 2020-01-07   | 76.82%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| SOL-USD  | OMG-USD         | 2025-12-01   | 76.72%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -5.35%       | -7.41%         | 2.96%          | 13.31%       | -7.41%         | 15.03%         |
| SOL-USD  | CRV-USD         | 2025-11-30   | 76.70%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.12%      | -14.42%        | 5.41%          | 5.96%        | -14.42%        | 5.96%          |
| SOL-USD  | ZIL-USD         | 2018-09-16   | 76.38%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 7.24%        | -17.41%        | 18.30%         | -9.96%       | -19.41%        | 18.30%         |
| SOL-USD  | FIL-USD         | 2018-10-03   | 76.32%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.67%        | -10.34%        | 5.32%          | -5.02%       | -10.34%        | 15.14%         |
| SOL-USD  | SOL-USD         | 2025-12-04   | 76.06%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -7.51%       | -10.44%        | 9.16%          | 6.95%        | -10.44%        | 10.43%         |
| SOL-USD  | ENJ-USD         | 2018-09-14   | 75.60%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -21.31%      | -23.24%        | 4.73%          | -12.17%      | -41.06%        | 4.73%          |

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

