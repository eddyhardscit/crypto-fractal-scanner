# Market Regime Match Report

Generated: 2026-08-18 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.178 $ | False | -17.18% | -10.22% | BEAR | -17.18% | -10.22% |
| DOGE-USD | BEAR | 0.06976 $ | False | -32.69% | -16.74% | BEAR | -17.18% | -10.22% |
| SOL-USD | BEAR | 75,70 $ | False | -12.05% | -16.85% | BEAR | -17.18% | -10.22% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 4.07% | 13.69% | 35.16% | -4.16% | -16.66% | 17.82% | 29.67% | 54.44% | 55.00% | 12.51% | 62.82% | 119.58% |
| BTC-USD | SAME_BTC_REGIME | 26 | 53.85% | 3.84% | 12.16% | 32.87% | -4.58% | -14.95% | 17.82% | 27.11% | 47.28% | 46.15% | -9.02% | 70.37% | 131.72% |
| BTC-USD | SAME_ASSET_REGIME | 27 | 55.56% | 4.18% | 12.82% | 32.44% | -5.26% | -15.02% | 17.99% | 26.36% | 46.63% | 51.85% | 13.51% | 69.97% | 128.69% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 24 | 54.17% | 4.07% | 12.67% | 33.72% | -4.58% | -13.02% | 17.82% | 25.61% | 48.59% | 50.00% | 4.65% | 76.24% | 137.80% |
| DOGE-USD | ALL_MATCHES | 40 | 72.50% | 14.02% | 28.91% | 45.15% | -8.15% | -19.70% | 24.22% | 37.00% | 50.30% | 50.00% | -0.16% | 20.49% | 103.09% |
| DOGE-USD | SAME_BTC_REGIME | 15 | 73.33% | 9.84% | 30.77% | 54.72% | -9.97% | -22.57% | 23.01% | 37.08% | 54.72% | 46.67% | -3.21% | 6.32% | 99.73% |
| DOGE-USD | SAME_ASSET_REGIME | 16 | 81.25% | 24.60% | 34.06% | 44.33% | -8.93% | -19.86% | 32.42% | 39.07% | 46.30% | 62.50% | 3.83% | 11.91% | 74.29% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 72.73% | 9.84% | 26.21% | 34.01% | -9.75% | -26.92% | 23.01% | 34.58% | 39.02% | 45.45% | -3.21% | 4.02% | 7.64% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 6.93% | 22.47% | 67.54% | -2.81% | -10.42% | 21.33% | 30.37% | 94.20% | 70.00% | 21.68% | 58.48% | 157.46% |
| SOL-USD | SAME_BTC_REGIME | 13 | 76.92% | 4.18% | 34.36% | 88.13% | -3.35% | -9.29% | 22.14% | 48.60% | 92.04% | 46.15% | -2.78% | 82.67% | 134.53% |
| SOL-USD | SAME_ASSET_REGIME | 11 | 72.73% | 4.18% | 17.98% | 93.69% | -4.48% | -9.63% | 22.14% | 40.50% | 93.69% | 45.45% | -7.07% | 113.56% | 157.07% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 9 | 77.78% | 4.18% | 20.47% | 128.84% | -3.25% | -7.36% | 22.14% | 48.60% | 129.05% | 44.44% | -7.07% | 82.67% | 205.52% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 26 | 53.85% | 3.84% | -4.58% | 27.11% | 46.15% | -9.02% | 83.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 100.00% | 8.78% | -3.41% | 33.46% | 85.71% | 13.51% | 85.01% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 50.00% | 0.09% | -2.67% | 18.96% | 50.00% | 18.60% | 61.52% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 15 | 73.33% | 9.84% | -9.97% | 37.08% | 46.67% | -3.21% | 49.65% |
| DOGE-USD | HISTORICAL_BTC_BULL | 20 | 75.00% | 15.95% | -5.64% | 39.89% | 55.00% | 2.60% | 55.92% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -32.40% | -36.26% | 0.00% | 0.00% | -27.09% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 19.46% | -8.93% | 26.50% | 50.00% | -0.95% | 46.83% |
| SOL-USD | HISTORICAL_BTC_BEAR | 13 | 76.92% | 4.18% | -3.35% | 48.60% | 46.15% | -2.78% | 98.06% |
| SOL-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 17.17% | -5.52% | 29.69% | 60.00% | 6.51% | 39.06% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 22 | 63.64% | 5.34% | -1.56% | 25.59% | 86.36% | 30.68% | 68.90% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 27 | 55.56% | 4.18% | -5.26% | 26.36% | 51.85% | 13.51% | 108.15% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 100.00% | 8.41% | -3.41% | 30.28% | 80.00% | 11.51% | 102.58% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.46% | -17.03% | 27.03% | 0.00% | -24.07% | 28.66% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 2.71% | -1.33% | 20.49% | 60.00% | 38.53% | 66.99% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 16 | 81.25% | 24.60% | -8.93% | 39.07% | 62.50% | 3.83% | 56.43% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 11 | 72.73% | 15.25% | -1.37% | 39.10% | 54.55% | 0.57% | 49.97% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 23.86% | -7.19% | 44.78% | 100.00% | 29.43% | 104.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 50.00% | -1.55% | -13.37% | 18.20% | 10.00% | -19.53% | 20.05% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 11 | 72.73% | 4.18% | -4.48% | 40.50% | 45.45% | -7.07% | 132.65% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 25.76% | -5.86% | 60.14% | 75.00% | 29.28% | 126.19% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 12.32% | -5.64% | 26.76% | 50.00% | 1.87% | 30.51% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 20 | 65.00% | 5.34% | -1.56% | 27.31% | 85.00% | 28.91% | 67.63% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2026-01-10 | 88.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.44% | -2.44% | 6.41% | -17.87% | -21.60% | 6.41% |
| BTC-USD | BTC-USD | 2018-10-26 | 87.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.83% | -3.45% | 17.65% | 41.24% | -3.45% | 41.24% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | NEO-USD | 2018-10-29 | 85.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 30.74% | -2.98% | 44.00% | 85.04% | -2.98% | 91.46% |
| BTC-USD | ETH-USD | 2026-01-10 | 85.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| BTC-USD | THETA-USD | 2022-04-15 | 84.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -10.88% | 27.86% | -20.52% | -20.52% | 27.86% |
| BTC-USD | SOL-USD | 2026-01-08 | 84.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | LTC-USD | 2018-10-26 | 84.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.00% | -4.25% | 50.56% | 146.90% | -4.25% | 146.90% |
| BTC-USD | QTUM-USD | 2026-01-10 | 84.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.32% | -2.69% | 17.99% | -18.21% | -22.94% | 17.99% |
| BTC-USD | ETC-USD | 2018-10-24 | 84.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| DOGE-USD | OP-USD | 2026-01-11 | 89.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | THETA-USD | 2022-03-31 | 85.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 34.01% | -12.38% | 34.01% | -13.72% | -13.72% | 34.01% |
| DOGE-USD | ADA-USD | 2022-03-27 | 85.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | NEO-USD | 2022-03-27 | 85.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | XTZ-USD | 2026-01-10 | 85.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | ETH-USD | 2018-07-21 | 85.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -46.43% | -47.25% | 6.37% | -43.24% | -58.95% | 6.37% |
| DOGE-USD | LTC-USD | 2018-04-29 | 85.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.91% | -26.92% | 0.00% | -20.47% | -30.09% | 0.00% |
| DOGE-USD | CHZ-USD | 2022-03-31 | 85.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 49.44% | -3.88% | 49.44% | 83.06% | -3.88% | 146.71% |
| DOGE-USD | DASH-USD | 2022-03-27 | 84.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LINK-USD | 2022-03-27 | 84.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| SOL-USD | ENJ-USD | 2018-10-29 | 80.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 269.45% | -9.43% | 270.52% | 449.81% | -9.43% | 676.95% |
| SOL-USD | NEAR-USD | 2026-01-10 | 78.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 20.47% | -4.92% | 22.14% | 68.39% | -4.92% | 112.24% |
| SOL-USD | SOL-USD | 2026-01-13 | 77.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.00% | -4.48% | 12.01% | -16.68% | -28.45% | 12.01% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | RUNE-USD | 2026-01-11 | 76.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | QTUM-USD | 2018-10-29 | 75.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.48% | -3.25% | 32.41% | 82.67% | -3.25% | 86.97% |
| SOL-USD | BTC-USD | 2026-01-12 | 75.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.55% | -0.76% | 7.58% | -15.86% | -20.28% | 7.58% |
| SOL-USD | ETH-USD | 2026-01-10 | 75.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| SOL-USD | BNB-USD | 2018-10-29 | 74.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 93.69% | -1.14% | 93.69% | 144.45% | -1.14% | 153.07% |
| SOL-USD | BNB-USD | 2026-01-15 | 79.13% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |

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

