# Market Regime Match Report

Generated: 2026-08-16 05:34 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.000 $ | False | -18.13% | -10.21% | BEAR | -18.13% | -10.21% |
| DOGE-USD | BEAR | 0.06964 $ | False | -33.45% | -16.71% | BEAR | -18.13% | -10.21% |
| SOL-USD | BEAR | 75,31 $ | False | -11.70% | -16.89% | BEAR | -18.13% | -10.21% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 7.75% | 17.60% | 31.21% | -3.47% | -16.80% | 16.88% | 29.67% | 48.58% | 57.50% | 11.53% | 62.55% | 107.95% |
| BTC-USD | SAME_BTC_REGIME | 21 | 66.67% | 8.28% | 13.12% | 27.24% | -3.99% | -10.88% | 17.08% | 23.17% | 46.91% | 42.86% | -11.59% | 61.55% | 91.70% |
| BTC-USD | SAME_ASSET_REGIME | 24 | 66.67% | 8.68% | 16.39% | 29.60% | -4.67% | -16.08% | 17.90% | 28.20% | 44.00% | 50.00% | -3.21% | 62.82% | 86.18% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 65.00% | 8.68% | 13.86% | 30.00% | -4.20% | -11.39% | 17.90% | 24.34% | 48.58% | 45.00% | -12.37% | 63.12% | 98.46% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 13.37% | 24.47% | 40.78% | -9.45% | -27.96% | 23.28% | 36.50% | 51.89% | 45.00% | -2.61% | 14.65% | 103.11% |
| DOGE-USD | SAME_BTC_REGIME | 20 | 85.00% | 14.57% | 25.54% | 45.54% | -10.07% | -17.26% | 23.94% | 42.37% | 51.91% | 45.00% | -2.61% | 9.45% | 111.39% |
| DOGE-USD | SAME_ASSET_REGIME | 15 | 80.00% | 14.03% | 24.60% | 30.83% | -9.75% | -20.59% | 23.54% | 32.42% | 40.36% | 46.67% | -2.00% | 5.41% | 17.89% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 13 | 76.92% | 13.28% | 21.57% | 27.01% | -10.17% | -23.41% | 23.01% | 31.81% | 42.10% | 38.46% | -3.21% | 3.04% | 7.11% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 7.03% | 22.77% | 50.77% | -1.59% | -13.30% | 18.61% | 29.33% | 77.92% | 65.00% | 22.92% | 63.37% | 148.71% |
| SOL-USD | SAME_BTC_REGIME | 13 | 92.31% | 4.18% | 21.01% | 72.90% | 0.00% | -7.00% | 22.38% | 48.60% | 93.74% | 53.85% | 27.84% | 82.67% | 140.46% |
| SOL-USD | SAME_ASSET_REGIME | 10 | 80.00% | 4.05% | 15.56% | 37.94% | -1.62% | -15.35% | 20.24% | 30.14% | 63.07% | 40.00% | -9.43% | 76.17% | 174.40% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 9 | 88.89% | 4.18% | 15.59% | 54.87% | 0.00% | -8.32% | 22.38% | 32.41% | 77.55% | 44.44% | -7.07% | 82.67% | 201.45% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 21 | 66.67% | 8.28% | -3.99% | 23.17% | 42.86% | -11.59% | 61.55% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 90.00% | 14.80% | -0.30% | 35.24% | 90.00% | 21.72% | 93.79% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 37.50% | -3.45% | -4.38% | 18.92% | 50.00% | 18.90% | 70.17% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 20 | 85.00% | 14.57% | -10.07% | 42.37% | 45.00% | -2.61% | 49.93% |
| DOGE-USD | HISTORICAL_BTC_BULL | 17 | 41.18% | -3.46% | -5.75% | 31.02% | 41.18% | -10.60% | 41.88% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 24.33% | -8.70% | 28.68% | 66.67% | 5.82% | 52.26% |
| SOL-USD | HISTORICAL_BTC_BEAR | 13 | 92.31% | 4.18% | 0.00% | 48.60% | 53.85% | 27.84% | 107.36% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 8.41% | -7.94% | 29.09% | 42.86% | -1.64% | 34.38% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 20 | 60.00% | 5.40% | -1.50% | 25.68% | 80.00% | 30.68% | 97.76% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 24 | 66.67% | 8.68% | -4.67% | 28.20% | 50.00% | -3.21% | 66.50% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 100.00% | 16.65% | -0.13% | 45.67% | 100.00% | 102.25% | 267.81% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.72% | -0.24% | 9.96% | 0.00% | -6.25% | 16.45% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 44.44% | -3.38% | -4.81% | 16.68% | 55.56% | 0.92% | 61.71% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 15 | 80.00% | 14.03% | -9.75% | 32.42% | 46.67% | -2.00% | 44.47% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 13 | 61.54% | 12.95% | -1.13% | 40.57% | 53.85% | 8.45% | 58.07% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 51.18% | -11.72% | 54.71% | 100.00% | 82.52% | 130.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 50.00% | 1.00% | -10.46% | 26.22% | 20.00% | -19.87% | 36.76% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 10 | 80.00% | 4.05% | -1.62% | 30.14% | 40.00% | -9.43% | 102.26% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 19.55% | -1.19% | 60.53% | 66.67% | 49.82% | 115.54% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 12.63% | -4.47% | 26.76% | 50.00% | 2.44% | 30.51% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 3 | 100.00% | 78.73% | 0.00% | 106.96% | 100.00% | 112.92% | 221.88% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 17 | 58.82% | 4.05% | -1.75% | 20.49% | 76.47% | 20.48% | 58.32% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | BTC-USD | 2018-10-24 | 87.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.76% | -1.69% | 19.80% | 20.26% | -1.69% | 20.26% |
| BTC-USD | NEO-USD | 2018-10-24 | 87.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.24% | -1.02% | 46.91% | 44.33% | -1.02% | 46.91% |
| BTC-USD | XRP-USD | 2026-01-10 | 86.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.44% | -2.44% | 6.41% | -17.87% | -21.60% | 6.41% |
| BTC-USD | SOL-USD | 2026-01-08 | 86.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | ETC-USD | 2018-10-24 | 86.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| BTC-USD | ETH-USD | 2026-01-05 | 85.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.82% | -3.01% | 4.21% | -27.68% | -32.48% | 4.21% |
| BTC-USD | OMG-USD | 2018-10-24 | 85.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.35% | -6.48% | 23.17% | 67.84% | -6.48% | 81.36% |
| BTC-USD | THETA-USD | 2022-04-15 | 84.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -10.88% | 27.86% | -20.52% | -20.52% | 27.86% |
| BTC-USD | XTZ-USD | 2026-01-10 | 84.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | OP-USD | 2026-01-06 | 90.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.03% | -0.09% | 43.84% | -9.51% | -24.09% | 43.84% |
| DOGE-USD | QTUM-USD | 2022-07-30 | 87.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.20% | -30.29% | 1.37% | -32.40% | -35.81% | 1.37% |
| DOGE-USD | ADA-USD | 2022-03-27 | 87.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | NEO-USD | 2022-03-27 | 87.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | CHZ-USD | 2022-03-26 | 86.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.08% | -1.30% | 51.20% | 116.30% | -1.30% | 153.33% |
| DOGE-USD | THETA-USD | 2022-03-26 | 86.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.01% | -10.28% | 22.09% | -4.02% | -10.28% | 37.23% |
| DOGE-USD | FTM-USD | 2022-03-27 | 86.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.54% | -11.30% | 35.15% | 1.61% | -11.30% | 54.20% |
| DOGE-USD | DASH-USD | 2022-03-27 | 86.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LINK-USD | 2022-03-27 | 86.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| DOGE-USD | LTC-USD | 2018-04-27 | 85.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.69% | -26.23% | 1.90% | -21.48% | -29.43% | 1.90% |
| SOL-USD | ENJ-USD | 2018-10-24 | 82.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 190.30% | -13.17% | 193.34% | 417.86% | -13.17% | 644.83% |
| SOL-USD | SOL-USD | 2026-01-08 | 79.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| SOL-USD | RUNE-USD | 2026-01-11 | 79.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | NEAR-USD | 2026-01-05 | 77.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.59% | -7.11% | 17.95% | 56.65% | -7.11% | 107.36% |
| SOL-USD | XTZ-USD | 2018-11-03 | 77.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 21.01% | 0.00% | 22.38% | 147.35% | 0.00% | 179.64% |
| SOL-USD | QTUM-USD | 2018-10-29 | 76.77% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.48% | -3.25% | 32.41% | 82.67% | -3.25% | 86.97% |
| SOL-USD | BTC-USD | 2026-01-10 | 76.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.92% | 0.00% | 11.21% | -14.84% | -17.59% | 11.21% |
| SOL-USD | KAVA-USD | 2026-01-10 | 76.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | 0.00% | 23.31% | -16.11% | -23.42% | 23.31% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | BNB-USD | 2026-01-10 | 79.62% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 3.72% | -0.24% | 9.96% | -6.25% | -7.20% | 16.45% |

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

