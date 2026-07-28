# Market Regime Match Report

Generated: 2026-07-28 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.392 $ | False | -16.36% | -9.80% | BEAR | -16.36% | -9.80% |
| DOGE-USD | BEAR | 0.06996 $ | False | -32.74% | -16.09% | BEAR | -16.36% | -9.80% |
| SOL-USD | BEAR | 73,28 $ | False | -11.76% | -16.58% | BEAR | -16.36% | -9.80% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 7.47% | 33.94% | 44.97% | -6.56% | -32.12% | 13.48% | 38.85% | 54.47% | 55.00% | 6.12% | 41.82% | 66.03% |
| BTC-USD | SAME_BTC_REGIME | 16 | 68.75% | 6.67% | 22.90% | 34.64% | -4.95% | -15.04% | 13.48% | 28.91% | 49.05% | 50.00% | -0.07% | 8.42% | 33.22% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 78.26% | 11.36% | 35.19% | 48.53% | -4.18% | -14.04% | 19.65% | 43.32% | 51.21% | 65.22% | 8.09% | 42.82% | 65.06% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 14 | 71.43% | 6.67% | 17.37% | 34.90% | -4.95% | -12.10% | 13.48% | 25.32% | 50.08% | 50.00% | -0.07% | 7.74% | 42.73% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 6.65% | 19.61% | 32.09% | -9.10% | -21.40% | 17.52% | 32.20% | 41.63% | 65.00% | 9.67% | 33.17% | 68.19% |
| DOGE-USD | SAME_BTC_REGIME | 23 | 78.26% | 6.81% | 23.60% | 32.54% | -8.31% | -18.26% | 19.82% | 32.55% | 41.28% | 73.91% | 9.96% | 30.87% | 39.61% |
| DOGE-USD | SAME_ASSET_REGIME | 26 | 76.92% | 6.92% | 26.96% | 35.18% | -7.54% | -17.46% | 20.47% | 31.91% | 42.84% | 76.92% | 21.36% | 39.48% | 76.78% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 21 | 76.19% | 6.81% | 19.04% | 32.67% | -8.31% | -18.79% | 16.79% | 31.59% | 41.33% | 71.43% | 9.39% | 31.22% | 40.13% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 7.64% | 19.37% | 46.86% | -4.18% | -18.20% | 16.70% | 31.03% | 55.50% | 77.50% | 8.68% | 36.76% | 105.22% |
| SOL-USD | SAME_BTC_REGIME | 21 | 90.48% | 9.53% | 18.94% | 33.93% | -3.74% | -10.59% | 19.46% | 23.51% | 36.50% | 80.95% | 4.70% | 25.61% | 77.90% |
| SOL-USD | SAME_ASSET_REGIME | 29 | 68.97% | 9.39% | 14.29% | 39.07% | -4.18% | -18.42% | 14.26% | 23.46% | 58.57% | 75.86% | 5.54% | 29.89% | 83.31% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 88.89% | 9.45% | 13.67% | 19.45% | -3.79% | -11.64% | 15.14% | 21.37% | 24.37% | 77.78% | 2.91% | 11.08% | 77.51% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 16 | 68.75% | 6.67% | -4.95% | 28.91% | 50.00% | -0.07% | 28.91% |
| BTC-USD | HISTORICAL_BTC_BULL | 20 | 60.00% | 19.81% | -7.40% | 42.75% | 60.00% | 32.71% | 60.68% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -2.53% | -15.01% | 4.77% | 33.33% | -16.17% | 11.33% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 78.26% | 6.81% | -8.31% | 32.55% | 73.91% | 9.96% | 59.11% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 66.67% | 7.72% | -6.83% | 37.34% | 55.56% | 7.71% | 78.82% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 8 | 37.50% | -14.15% | -19.83% | 20.16% | 50.00% | 8.74% | 43.14% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 90.48% | 9.53% | -3.74% | 23.51% | 80.95% | 4.70% | 47.19% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 85.71% | 5.61% | -2.06% | 51.15% | 100.00% | 24.11% | 82.85% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -5.89% | -15.62% | 6.07% | 100.00% | 26.02% | 83.19% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 10 | 20.00% | -9.57% | -17.86% | 5.11% | 50.00% | 1.42% | 90.20% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 78.26% | 11.36% | -4.18% | 43.32% | 65.22% | 8.09% | 55.62% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 40.00% | -15.35% | -21.20% | 33.82% | 40.00% | -23.29% | 46.73% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.22% | -5.61% | 18.22% | 100.00% | 29.43% | 32.77% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 3 | 66.67% | 33.93% | -4.48% | 45.34% | 66.67% | 9.42% | 72.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 0.00% | -5.27% | -17.34% | 1.99% | 0.00% | -21.02% | 1.99% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 26 | 76.92% | 6.92% | -7.54% | 31.91% | 76.92% | 21.36% | 64.58% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 12.21% | -5.98% | 37.34% | 60.00% | 9.96% | 75.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 9 | 33.33% | -8.09% | -19.76% | 14.07% | 33.33% | -6.60% | 18.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 68.97% | 9.39% | -4.18% | 23.46% | 75.86% | 5.54% | 77.34% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 2.34% | -8.74% | 29.92% | 75.00% | 4.36% | 128.48% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 30.90% | -1.74% | 30.90% | 100.00% | 35.13% | 47.19% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 39.02% | -2.24% | 49.77% | 100.00% | 25.53% | 90.33% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 3.82% | -4.18% | 35.28% | 75.00% | 16.69% | 58.92% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 90.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | ONE-USD | 2020-01-27 | 88.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| BTC-USD | XRP-USD | 2019-10-09 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | XRP-USD | 2025-12-21 | 87.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | -0.53% | 11.68% | 0.43% | -1.24% | 12.21% |
| BTC-USD | BTC-USD | 2018-10-05 | 87.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.35% | -7.15% | 1.84% | 6.70% | -7.15% | 13.14% |
| BTC-USD | ETH-USD | 2025-12-21 | 86.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.36% | 0.00% | 19.65% | -0.57% | -0.79% | 19.65% |
| BTC-USD | BTC-USD | 2025-12-22 | 85.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.83% | -1.97% | 15.28% | 8.09% | -1.97% | 20.38% |
| BTC-USD | BNB-USD | 2025-12-21 | 85.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| BTC-USD | BNB-USD | 2018-10-04 | 85.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | QTUM-USD | 2020-01-27 | 85.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.22% | -8.83% | 22.12% | 9.44% | -8.83% | 22.12% |
| DOGE-USD | OP-USD | 2025-12-22 | 89.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | VET-USD | 2022-03-14 | 89.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.68% | -8.95% | 11.10% | 9.39% | -8.95% | 41.71% |
| DOGE-USD | DASH-USD | 2022-03-07 | 89.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | LTC-USD | 2018-04-13 | 88.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.07% | -36.07% | 5.71% | -35.67% | -38.84% | 5.71% |
| DOGE-USD | RUNE-USD | 2022-03-08 | 88.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -22.98% | 22.31% | 37.54% | -22.98% | 46.15% |
| DOGE-USD | INJ-USD | 2022-03-09 | 88.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.67% | -13.24% | 7.61% | 32.39% | -13.24% | 54.99% |
| DOGE-USD | HBAR-USD | 2022-03-14 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.78% | -18.79% | 1.28% | -7.73% | -18.79% | 12.96% |
| DOGE-USD | AVAX-USD | 2022-03-13 | 88.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 37.69% | -6.20% | 44.34% | 31.22% | -6.20% | 71.22% |
| DOGE-USD | THETA-USD | 2022-03-16 | 88.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.32% | -16.14% | 13.49% | -6.06% | -16.14% | 28.27% |
| DOGE-USD | OMG-USD | 2022-03-12 | 87.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.56% | -9.26% | 12.35% | 16.89% | -9.26% | 32.62% |
| SOL-USD | RUNE-USD | 2025-12-22 | 79.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.64% | -8.40% | 23.46% | 3.30% | -8.40% | 52.16% |
| SOL-USD | SOL-USD | 2025-12-19 | 78.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | NEAR-USD | 2025-12-21 | 78.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.29% | 0.00% | 23.51% | 104.94% | 0.00% | 139.37% |
| SOL-USD | BNB-USD | 2025-12-21 | 78.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | EOS-USD | 2018-10-19 | 77.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.40% | -7.62% | 75.20% | 77.34% | -7.62% | 77.34% |
| SOL-USD | KAVA-USD | 2025-12-21 | 77.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.72% | -7.96% | 14.26% | 2.51% | -7.96% | 24.10% |
| SOL-USD | LINK-USD | 2025-12-21 | 77.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.89% | 0.00% | 11.78% | 4.70% | 0.00% | 24.41% |
| SOL-USD | DOT-USD | 2025-12-16 | 77.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.88% | -14.40% | 0.00% | -8.57% | -14.40% | 1.55% |
| SOL-USD | BTC-USD | 2025-12-22 | 76.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.83% | -1.97% | 15.28% | 8.09% | -1.97% | 20.38% |
| SOL-USD | ZIL-USD | 2018-10-06 | 76.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.19% | -10.59% | 26.39% | -0.95% | -11.40% | 26.39% |

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

