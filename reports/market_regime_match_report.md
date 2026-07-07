# Market Regime Match Report

Generated: 2026-07-07 22:45 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       63558.8  | False                | -10.64%             | -10.25%                  | BEAR               | -10.64%          | -10.25%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -19.60%             | -16.80%                  | BEAR               | -10.64%          | -10.25%               |
| SOL-USD  | BEAR                  |          80.91 | False                | -2.02%              | -19.06%                  | BEAR               | -10.64%          | -10.25%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 62.50%              | 2.91%            | 15.20%           | 35.12%           | -5.48%             | -32.77%            | 14.64%             | 24.17%             | 41.50%             | 75.00%              | 21.61%           | 42.50%           | 65.33%           |
| BTC-USD  | SAME_BTC_REGIME           |        16 | 81.25%              | 10.58%           | 35.92%           | 49.58%           | -5.51%             | -12.74%            | 27.23%             | 43.88%             | 60.43%             | 93.75%              | 28.07%           | 45.72%           | 68.93%           |
| BTC-USD  | SAME_ASSET_REGIME         |        29 | 68.97%              | 3.13%            | 16.92%           | 35.65%           | -5.47%             | -11.28%            | 14.92%             | 26.46%             | 43.09%             | 89.66%              | 25.86%           | 42.18%           | 63.26%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        14 | 78.57%              | 10.58%           | 33.70%           | 50.88%           | -5.51%             | -14.08%            | 25.92%             | 39.36%             | 57.26%             | 92.86%              | 25.20%           | 40.80%           | 58.13%           |
| DOGE-USD | ALL_MATCHES               |        40 | 17.50%              | -18.49%          | -2.56%           | 19.52%           | -25.74%            | -43.86%            | 4.19%              | 14.78%             | 28.57%             | 42.50%              | -8.51%           | 7.03%            | 30.52%           |
| DOGE-USD | SAME_BTC_REGIME           |        31 | 16.13%              | -25.05%          | -4.49%           | 19.38%           | -31.06%            | -44.75%            | 3.99%              | 14.07%             | 39.92%             | 45.16%              | -8.19%           | 7.36%            | 24.54%           |
| DOGE-USD | SAME_ASSET_REGIME         |        33 | 18.18%              | -22.41%          | -2.70%           | 20.45%           | -29.00%            | -44.55%            | 4.39%              | 16.72%             | 37.40%             | 45.45%              | -8.19%           | 12.26%           | 32.14%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        30 | 16.67%              | -25.19%          | -4.45%           | 19.77%           | -30.15%            | -45.03%            | 4.19%              | 14.17%             | 41.04%             | 43.33%              | -8.19%           | 6.61%            | 25.12%           |
| SOL-USD  | ALL_MATCHES               |        40 | 47.50%              | -2.37%           | 6.51%            | 22.87%           | -11.64%            | -28.34%            | 7.58%              | 16.63%             | 36.78%             | 55.00%              | 1.01%            | 23.11%           | 53.59%           |
| SOL-USD  | SAME_BTC_REGIME           |        27 | 59.26%              | 0.92%            | 12.39%           | 31.42%           | -9.15%             | -20.82%            | 14.92%             | 21.79%             | 51.08%             | 62.96%              | 1.70%            | 21.11%           | 57.30%           |
| SOL-USD  | SAME_ASSET_REGIME         |        33 | 51.52%              | 0.32%            | 6.36%            | 20.71%           | -10.34%            | -23.53%            | 7.94%              | 16.21%             | 33.17%             | 60.61%              | 1.70%            | 21.89%           | 45.63%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        24 | 58.33%              | 0.80%            | 8.18%            | 27.16%           | -9.38%             | -18.67%            | 13.21%             | 18.71%             | 44.23%             | 62.50%              | 1.46%            | 16.60%           | 40.80%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        16 | 81.25%              | 10.58%           | -5.51%             | 43.88%             | 93.75%              | 28.07%           | 75.20%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |        10 | 50.00%              | 1.36%            | -4.03%             | 14.15%             | 60.00%              | 37.08%           | 72.19%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |         8 | 62.50%              | 2.78%            | -4.88%             | 17.62%             | 100.00%             | 20.18%           | 74.58%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         6 | 33.33%              | -3.13%           | -7.79%             | 16.45%             | 16.67%              | -19.23%          | 27.77%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        31 | 16.13%              | -25.05%          | -31.06%            | 14.07%             | 45.16%              | -8.19%           | 20.37%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         5 | 40.00%              | -2.17%           | -3.57%             | 16.94%             | 60.00%              | 5.41%            | 75.21%             |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         4 | 0.00%               | -10.74%          | -17.30%            | 5.84%              | 0.00%               | -22.14%          | 5.84%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        27 | 59.26%              | 0.92%            | -9.15%             | 21.79%             | 62.96%              | 1.70%            | 31.87%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |        10 | 30.00%              | -12.10%          | -25.03%            | 7.38%              | 30.00%              | -7.40%           | 48.52%             |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         2 | 0.00%               | -3.94%           | -10.11%            | 3.67%              | 100.00%             | 23.28%           | 67.33%             |
| SOL-USD  | HISTORICAL_BTC_RECOVERY     |         1 | 0.00%               | -28.55%          | -39.97%            | 4.33%              | 0.00%               | -19.55%          | 4.33%              |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        29 | 68.97%              | 3.13%            | -5.47%             | 26.46%             | 89.66%              | 25.86%           | 73.78%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         4 | 25.00%              | -6.29%           | -7.12%             | 17.69%             | 25.00%              | -15.06%          | 59.52%             |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         1 | 100.00%             | 4.40%            | -3.37%             | 8.82%              | 100.00%             | 21.58%           | 33.10%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 50.00%              | 0.16%            | -7.03%             | 29.52%             | 33.33%              | -13.42%          | 65.51%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        33 | 18.18%              | -22.41%          | -29.00%            | 16.72%             | 45.45%              | -8.19%           | 24.39%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         3 | 33.33%              | -12.18%          | -17.30%            | 8.26%              | 66.67%              | 5.41%            | 15.40%             |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION |         1 | 0.00%               | -18.56%          | -18.58%            | 0.00%              | 0.00%               | -8.83%           | 0.00%              |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         3 | 0.00%               | -9.77%           | -11.71%            | 6.53%              | 0.00%               | -17.46%          | 6.53%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        33 | 51.52%              | 0.32%            | -10.34%            | 16.21%             | 60.61%              | 1.70%            | 39.66%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         2 | 0.00%               | -26.36%          | -34.90%            | 5.01%              | 0.00%               | -20.69%          | 5.01%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         2 | 0.00%               | -14.87%          | -26.93%            | 0.00%              | 0.00%               | -15.73%          | 0.00%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         3 | 66.67%              | 13.78%           | -3.65%             | 45.90%             | 66.67%              | 52.55%           | 109.36%            |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-14   | 88.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 55.58%       | -16.08%        | 55.79%         | 30.28%       | -16.08%        | 133.75%        |
| BTC-USD  | KSM-USD         | 2022-03-05   | 87.65%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -8.02%       | -9.39%         | 13.41%         | 19.28%       | -9.39%         | 31.79%         |
| BTC-USD  | XLM-USD         | 2020-01-02   | 84.41%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 34.59%       | -2.89%         | 57.88%         | 64.43%       | -2.89%         | 72.91%         |
| BTC-USD  | SOL-USD         | 2022-03-05   | 83.96%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 6.55%        | -8.30%         | 37.70%         | 39.29%       | -8.30%         | 46.05%         |
| BTC-USD  | ENJ-USD         | 2022-03-02   | 83.95%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.40%      | -33.49%        | 0.00%          | 12.28%       | -33.49%        | 13.74%         |
| BTC-USD  | EOS-USD         | 2022-03-07   | 83.91%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 3.13%        | -5.47%         | 10.35%         | 43.45%       | -5.47%         | 43.45%         |
| BTC-USD  | XLM-USD         | 2019-09-29   | 83.67%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| BTC-USD  | BAT-USD         | 2019-09-29   | 83.65%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 31.04%       | -4.08%         | 31.04%         | 25.86%       | -4.08%         | 61.96%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 83.55%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | TRX-USD         | 2020-01-02   | 83.44%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.61%       | -1.90%         | 31.40%         | 41.30%       | -1.90%         | 45.88%         |
| DOGE-USD | VET-USD         | 2022-02-22   | 87.39%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | DASH-USD        | 2022-02-20   | 87.07%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.76%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | XLM-USD         | 2019-09-29   | 86.60%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 86.59%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XTZ-USD         | 2025-12-01   | 85.81%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.70%       | -6.44%         | 11.03%         | 6.70%        | -6.44%         | 11.03%         |
| DOGE-USD | ADA-USD         | 2022-02-20   | 85.47%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -18.34%      | -19.98%        | 12.55%         | -8.20%       | -26.69%        | 12.55%         |
| DOGE-USD | CHZ-USD         | 2022-02-19   | 85.23%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -9.76%       | -23.41%        | 13.85%         | 6.31%        | -23.41%        | 13.85%         |
| DOGE-USD | BAT-USD         | 2018-09-19   | 85.13%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -1.76%       | -6.08%         | 10.32%         | 15.56%       | -17.86%        | 15.56%         |
| DOGE-USD | DOT-USD         | 2022-02-20   | 85.05%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.96%      | -32.96%        | 0.00%          | -21.71%      | -39.75%        | 0.00%          |
| SOL-USD  | ZIL-USD         | 2018-09-16   | 77.78%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 7.24%        | -17.41%        | 18.30%         | -9.96%       | -19.41%        | 18.30%         |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 77.62%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | TRX-USD         | 2018-09-14   | 77.44%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 22.15%       | -11.82%        | 35.54%         | 20.33%       | -11.82%        | 39.66%         |
| SOL-USD  | APT-USD         | 2024-09-01   | 76.98%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.92%        | -11.47%        | 6.42%          | -34.40%      | -34.40%        | 6.42%          |
| SOL-USD  | LRC-USD         | 2018-09-14   | 76.86%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 55.58%       | -16.08%        | 55.79%         | 30.28%       | -16.08%        | 133.75%        |
| SOL-USD  | ENJ-USD         | 2018-09-14   | 76.84%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -21.31%      | -23.24%        | 4.73%          | -12.17%      | -41.06%        | 4.73%          |
| SOL-USD  | SOL-USD         | 2025-11-29   | 76.64%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 4.93%        | -3.28%         | 17.89%         | 8.31%        | -3.28%         | 17.89%         |
| SOL-USD  | OMG-USD         | 2025-12-01   | 76.29%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -5.35%       | -7.41%         | 2.96%          | 13.31%       | -7.41%         | 15.03%         |
| SOL-USD  | LINK-USD        | 2025-11-26   | 75.85%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -5.48%       | -8.61%         | 7.94%          | 1.70%        | -8.61%         | 7.94%          |
| SOL-USD  | CRV-USD         | 2025-11-30   | 75.71%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.12%      | -14.42%        | 5.41%          | 5.96%        | -14.42%        | 5.96%          |

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

