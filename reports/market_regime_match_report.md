# Market Regime Match Report

Generated: 2026-07-30 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.885 $ | False | -18.27% | -9.80% | BEAR | -18.27% | -9.80% |
| DOGE-USD | BEAR | 0.06963 $ | False | -35.77% | -16.18% | BEAR | -18.27% | -9.80% |
| SOL-USD | BEAR | 73,43 $ | False | -12.31% | -16.60% | BEAR | -18.27% | -9.80% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 7.47% | 30.20% | 49.37% | -5.10% | -32.21% | 17.33% | 40.79% | 62.95% | 62.50% | 9.15% | 42.05% | 67.38% |
| BTC-USD | SAME_BTC_REGIME | 11 | 72.73% | 4.95% | 13.11% | 17.59% | -4.18% | -13.03% | 11.48% | 18.62% | 22.12% | 45.45% | -0.57% | 5.57% | 6.88% |
| BTC-USD | SAME_ASSET_REGIME | 21 | 80.95% | 11.36% | 35.08% | 49.54% | -0.53% | -13.61% | 18.04% | 41.18% | 54.41% | 76.19% | 16.42% | 43.28% | 96.88% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 80.00% | 7.17% | 13.98% | 17.76% | -3.11% | -9.31% | 11.58% | 19.13% | 24.03% | 50.00% | -0.07% | 6.10% | 7.13% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 6.96% | 15.20% | 28.22% | -10.32% | -28.99% | 15.08% | 26.33% | 39.28% | 70.00% | 11.61% | 19.34% | 83.34% |
| DOGE-USD | SAME_BTC_REGIME | 23 | 82.61% | 8.81% | 16.81% | 27.85% | -9.62% | -16.19% | 14.47% | 27.45% | 40.68% | 82.61% | 13.26% | 17.73% | 34.69% |
| DOGE-USD | SAME_ASSET_REGIME | 25 | 80.00% | 8.81% | 17.92% | 27.97% | -9.62% | -17.75% | 14.24% | 21.82% | 36.78% | 84.00% | 14.25% | 37.11% | 87.74% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 80.00% | 8.24% | 14.78% | 20.04% | -9.63% | -16.46% | 13.87% | 18.34% | 33.92% | 80.00% | 11.58% | 17.31% | 46.04% |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 6.32% | 26.44% | 50.16% | -6.72% | -21.51% | 12.25% | 36.36% | 62.38% | 65.00% | 4.61% | 36.68% | 109.92% |
| SOL-USD | SAME_BTC_REGIME | 19 | 84.21% | 11.36% | 22.50% | 35.53% | -1.77% | -10.89% | 14.95% | 27.93% | 37.58% | 63.16% | 2.44% | 8.02% | 43.57% |
| SOL-USD | SAME_ASSET_REGIME | 28 | 64.29% | 6.32% | 20.87% | 48.15% | -3.46% | -22.23% | 11.63% | 27.80% | 64.93% | 64.29% | 4.61% | 32.76% | 85.62% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 15 | 86.67% | 9.39% | 18.81% | 35.13% | -1.77% | -10.34% | 12.72% | 24.23% | 39.67% | 60.00% | 1.20% | 5.66% | 54.82% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 11 | 72.73% | 4.95% | -4.18% | 18.62% | 45.45% | -0.57% | 21.57% |
| BTC-USD | HISTORICAL_BTC_BULL | 21 | 66.67% | 18.39% | -5.26% | 44.46% | 61.90% | 24.11% | 64.13% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -2.54% | -2.54% | 18.04% | 100.00% | 98.26% | 98.26% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 66.67% | 5.36% | -12.84% | 42.64% | 83.33% | 19.28% | 91.16% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 82.61% | 8.81% | -9.62% | 27.45% | 82.61% | 13.26% | 63.30% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 4.94% | -5.43% | 30.02% | 62.50% | 9.74% | 52.97% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.74% | -20.84% | 2.91% | 100.00% | 14.25% | 20.66% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 8 | 37.50% | -11.07% | -18.24% | 21.13% | 37.50% | -4.77% | 68.44% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 84.21% | 11.36% | -1.77% | 27.93% | 63.16% | 2.44% | 36.41% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 55.56% | 5.61% | -7.24% | 60.53% | 66.67% | 6.12% | 60.53% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -6.44% | -13.55% | 8.68% | 100.00% | 41.35% | 87.69% |
| SOL-USD | HISTORICAL_BTC_MIXED | 2 | 100.00% | 53.09% | -6.11% | 60.09% | 100.00% | 131.55% | 193.17% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 9 | 22.22% | -11.19% | -20.14% | 4.69% | 55.56% | 18.07% | 111.01% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 21 | 80.95% | 11.36% | -0.53% | 41.18% | 76.19% | 16.42% | 64.53% |
| BTC-USD | HISTORICAL_ASSET_BULL | 12 | 50.00% | -9.04% | -22.11% | 24.61% | 41.67% | -27.73% | 53.63% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 49.35% | 0.00% | 64.13% | 100.00% | 46.87% | 64.13% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 2.32% | -24.12% | 40.64% | 50.00% | -1.86% | 81.21% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 50.00% | 0.64% | -9.98% | 33.38% | 50.00% | -1.15% | 39.45% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 25 | 80.00% | 8.81% | -9.62% | 21.82% | 84.00% | 14.25% | 69.70% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 7 | 57.14% | 7.72% | -6.55% | 29.49% | 57.14% | 4.86% | 56.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 8 | 37.50% | -9.28% | -17.31% | 30.95% | 37.50% | -7.52% | 32.77% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 64.29% | 6.32% | -3.46% | 27.80% | 64.29% | 4.61% | 66.55% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 2.34% | -8.74% | 29.92% | 75.00% | 4.36% | 128.48% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 8.73% | -8.02% | 23.46% | 50.00% | 11.01% | 35.68% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 39.02% | -2.24% | 49.77% | 100.00% | 25.53% | 90.33% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 50.00% | 7.03% | -10.93% | 26.73% | 50.00% | -2.40% | 67.60% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ONE-USD | 2020-01-27 | 88.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| BTC-USD | XRP-USD | 2019-10-14 | 88.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.85% | -7.06% | 41.18% | -33.30% | -41.12% | 41.18% |
| BTC-USD | XRP-USD | 2025-12-21 | 88.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | -0.53% | 11.68% | 0.43% | -1.24% | 12.21% |
| BTC-USD | ETH-USD | 2025-12-21 | 88.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.36% | 0.00% | 19.65% | -0.57% | -0.79% | 19.65% |
| BTC-USD | BTC-USD | 2018-10-07 | 87.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.00% | -8.27% | 0.61% | 6.88% | -8.27% | 11.78% |
| BTC-USD | XTZ-USD | 2025-12-26 | 86.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| BTC-USD | BTC-USD | 2025-12-24 | 86.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 17.59% | 0.00% | 17.59% | 6.62% | 0.00% | 22.80% |
| BTC-USD | QTUM-USD | 2020-01-27 | 85.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.22% | -8.83% | 22.12% | 9.44% | -8.83% | 22.12% |
| BTC-USD | BNB-USD | 2025-12-26 | 85.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| BTC-USD | LTC-USD | 2020-01-25 | 85.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.86% | -13.61% | 0.00% | -14.05% | -14.21% | 0.00% |
| DOGE-USD | OP-USD | 2025-12-22 | 90.11% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | DASH-USD | 2022-03-12 | 89.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.34% | -9.62% | 18.11% | 13.82% | -9.62% | 28.65% |
| DOGE-USD | THETA-USD | 2022-03-16 | 89.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.32% | -16.14% | 13.49% | -6.06% | -16.14% | 28.27% |
| DOGE-USD | VET-USD | 2022-03-14 | 89.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.68% | -8.95% | 11.10% | 9.39% | -8.95% | 41.71% |
| DOGE-USD | LTC-USD | 2018-04-10 | 88.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.26% | -37.33% | 2.67% | -34.49% | -40.60% | 2.67% |
| DOGE-USD | ENJ-USD | 2022-03-17 | 88.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.44% | -14.62% | 14.24% | 4.04% | -14.62% | 29.60% |
| DOGE-USD | OMG-USD | 2022-03-12 | 88.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.56% | -9.26% | 12.35% | 16.89% | -9.26% | 32.62% |
| DOGE-USD | FIL-USD | 2022-03-16 | 88.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.69% | -12.34% | 5.53% | 8.99% | -12.34% | 69.70% |
| DOGE-USD | NEO-USD | 2022-03-12 | 88.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.70% | -11.00% | 15.70% | 15.06% | -11.00% | 32.52% |
| DOGE-USD | XTZ-USD | 2025-12-26 | 88.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| SOL-USD | NEAR-USD | 2025-12-21 | 81.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.29% | 0.00% | 23.51% | 104.94% | 0.00% | 139.37% |
| SOL-USD | RUNE-USD | 2025-12-27 | 80.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.91% | -0.37% | 41.91% | -5.22% | -5.22% | 62.96% |
| SOL-USD | LINK-USD | 2025-12-21 | 78.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.89% | 0.00% | 11.78% | 4.70% | 0.00% | 24.41% |
| SOL-USD | BNB-USD | 2025-12-26 | 78.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| SOL-USD | SOL-USD | 2025-12-24 | 78.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| SOL-USD | KAVA-USD | 2025-12-26 | 78.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.96% | -2.75% | 24.96% | 1.20% | -2.75% | 31.13% |
| SOL-USD | DOT-USD | 2025-12-21 | 77.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.50% | -6.20% | 7.56% | -4.04% | -6.20% | 11.28% |
| SOL-USD | EOS-USD | 2018-10-19 | 77.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.40% | -7.62% | 75.20% | 77.34% | -7.62% | 77.34% |
| SOL-USD | ONE-USD | 2020-01-27 | 77.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| SOL-USD | BTC-USD | 2025-12-24 | 76.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 17.59% | 0.00% | 17.59% | 6.62% | 0.00% | 22.80% |

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

