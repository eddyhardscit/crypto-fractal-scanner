# Market Regime Match Report

Generated: 2026-08-14 10:52 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 62.760 $ | False | -19.64% | -10.35% | BEAR | -19.64% | -10.35% |
| DOGE-USD | BEAR | 0.06933 $ | False | -36.56% | -16.94% | BEAR | -19.64% | -10.35% |
| SOL-USD | BEAR | 75,37 $ | False | -12.81% | -17.16% | BEAR | -19.64% | -10.35% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 8.71% | 19.43% | 48.78% | -4.01% | -16.60% | 20.05% | 36.79% | 73.02% | 60.00% | 16.53% | 65.84% | 112.25% |
| BTC-USD | SAME_BTC_REGIME | 22 | 72.73% | 8.71% | 17.03% | 49.50% | -3.50% | -10.45% | 19.43% | 37.48% | 70.74% | 45.45% | -8.92% | 66.53% | 105.81% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 73.91% | 8.98% | 18.10% | 45.07% | -4.24% | -15.65% | 18.73% | 28.54% | 62.61% | 52.17% | 5.16% | 67.23% | 104.60% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 73.68% | 8.98% | 16.71% | 56.82% | -3.99% | -7.44% | 18.73% | 25.51% | 71.10% | 47.37% | -11.59% | 70.57% | 117.47% |
| DOGE-USD | ALL_MATCHES | 40 | 70.00% | 13.37% | 28.91% | 42.79% | -9.45% | -27.84% | 23.28% | 40.90% | 58.08% | 50.00% | -0.19% | 16.02% | 86.97% |
| DOGE-USD | SAME_BTC_REGIME | 20 | 85.00% | 15.57% | 30.17% | 54.05% | -10.07% | -17.54% | 26.08% | 43.91% | 60.93% | 50.00% | -0.19% | 10.21% | 111.39% |
| DOGE-USD | SAME_ASSET_REGIME | 16 | 81.25% | 14.57% | 25.54% | 35.56% | -9.45% | -20.60% | 23.93% | 33.56% | 47.52% | 50.00% | -0.19% | 6.28% | 16.69% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 14 | 78.57% | 13.66% | 24.05% | 34.92% | -9.96% | -23.99% | 23.28% | 34.32% | 48.99% | 42.86% | -2.61% | 4.50% | 8.34% |
| SOL-USD | ALL_MATCHES | 40 | 75.00% | 5.21% | 22.11% | 79.39% | -4.02% | -10.61% | 16.16% | 34.25% | 104.89% | 57.50% | 13.74% | 61.82% | 185.86% |
| SOL-USD | SAME_BTC_REGIME | 14 | 85.71% | 4.12% | 19.65% | 69.98% | -2.20% | -7.03% | 20.24% | 43.82% | 90.92% | 50.00% | 10.80% | 62.36% | 137.02% |
| SOL-USD | SAME_ASSET_REGIME | 12 | 75.00% | 3.86% | 13.74% | 20.46% | -4.82% | -12.56% | 18.02% | 24.85% | 46.69% | 41.67% | -9.43% | 57.87% | 138.77% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 80.00% | 3.86% | 14.97% | 37.94% | -4.82% | -7.71% | 20.24% | 27.93% | 63.07% | 40.00% | -9.43% | 60.32% | 174.40% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 72.73% | 8.71% | -3.50% | 37.48% | 45.45% | -8.92% | 89.45% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 90.00% | 14.80% | -0.30% | 35.24% | 90.00% | 21.72% | 93.79% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 42.86% | -3.52% | -4.81% | 22.81% | 57.14% | 48.71% | 78.63% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 20 | 85.00% | 15.57% | -10.07% | 43.91% | 50.00% | -0.19% | 54.93% |
| DOGE-USD | HISTORICAL_BTC_BULL | 16 | 43.75% | -1.95% | -8.62% | 31.14% | 43.75% | -15.15% | 46.56% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 11.10% | 0.00% | 36.94% | 100.00% | 19.41% | 36.94% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 24.33% | -8.70% | 28.68% | 66.67% | 5.82% | 52.26% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 85.71% | 4.12% | -2.20% | 43.82% | 50.00% | 10.80% | 103.55% |
| SOL-USD | HISTORICAL_BTC_BULL | 8 | 87.50% | 8.39% | -2.96% | 92.25% | 50.00% | 4.67% | 237.88% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 18 | 61.11% | 3.91% | -4.35% | 24.53% | 66.67% | 18.49% | 64.82% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 73.91% | 8.98% | -4.24% | 28.54% | 52.17% | 5.16% | 90.77% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 100.00% | 17.51% | -0.07% | 64.82% | 100.00% | 82.44% | 226.50% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.72% | -0.24% | 9.96% | 0.00% | -6.25% | 16.45% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 44.44% | -3.52% | -6.59% | 25.65% | 55.56% | 0.92% | 61.71% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 16 | 81.25% | 14.57% | -9.45% | 33.56% | 50.00% | -0.19% | 47.38% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 11 | 63.64% | 11.10% | -5.30% | 41.65% | 72.73% | 14.56% | 74.19% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 51.18% | -11.72% | 54.71% | 100.00% | 82.52% | 130.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 11 | 54.55% | 2.44% | -10.96% | 24.62% | 18.18% | -21.46% | 31.65% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 12 | 75.00% | 3.86% | -4.82% | 24.85% | 41.67% | -9.43% | 73.00% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 100.00% | 55.48% | -0.75% | 195.28% | 75.00% | 134.76% | 1021.74% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -2.44% | -4.99% | 7.89% | 0.00% | -3.94% | 12.75% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 4 | 75.00% | 57.68% | -1.30% | 105.67% | 75.00% | 84.05% | 167.40% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 18 | 72.22% | 4.58% | -4.29% | 21.01% | 66.67% | 18.49% | 64.82% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | NEO-USD | 2018-10-24 | 88.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.24% | -1.02% | 46.91% | 44.33% | -1.02% | 46.91% |
| BTC-USD | XRP-USD | 2026-01-05 | 87.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.98% | 0.00% | 8.98% | -15.55% | -19.71% | 8.98% |
| BTC-USD | OMG-USD | 2018-10-24 | 87.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.35% | -6.48% | 23.17% | 67.84% | -6.48% | 81.36% |
| BTC-USD | ETH-USD | 2026-01-05 | 86.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.82% | -3.01% | 4.21% | -27.68% | -32.48% | 4.21% |
| BTC-USD | BTC-USD | 2018-10-22 | 86.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.79% | -1.41% | 20.14% | 19.10% | -1.41% | 20.14% |
| BTC-USD | ETC-USD | 2018-10-24 | 86.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | SOL-USD | 2026-01-08 | 85.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | XTZ-USD | 2018-10-24 | 85.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 7.22% | -3.99% | 22.40% | 159.29% | -3.99% | 179.67% |
| BTC-USD | XTZ-USD | 2026-01-10 | 85.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | OP-USD | 2026-01-06 | 91.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.03% | -0.09% | 43.84% | -9.51% | -24.09% | 43.84% |
| DOGE-USD | ADA-USD | 2022-03-27 | 87.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | CHZ-USD | 2022-03-26 | 87.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.08% | -1.30% | 51.20% | 116.30% | -1.30% | 153.33% |
| DOGE-USD | NEO-USD | 2022-03-27 | 87.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | THETA-USD | 2022-03-26 | 87.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.01% | -10.28% | 22.09% | -4.02% | -10.28% | 37.23% |
| DOGE-USD | QTUM-USD | 2022-07-30 | 87.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.20% | -30.29% | 1.37% | -32.40% | -35.81% | 1.37% |
| DOGE-USD | FTM-USD | 2022-03-27 | 86.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.54% | -11.30% | 35.15% | 1.61% | -11.30% | 54.20% |
| DOGE-USD | DASH-USD | 2022-03-27 | 86.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LINK-USD | 2022-03-27 | 86.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| DOGE-USD | OMG-USD | 2022-03-27 | 86.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.11% | -12.12% | 23.54% | -4.37% | -12.12% | 28.43% |
| SOL-USD | ENJ-USD | 2018-10-24 | 85.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 190.30% | -13.17% | 193.34% | 417.86% | -13.17% | 644.83% |
| SOL-USD | SOL-USD | 2026-01-08 | 79.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| SOL-USD | RUNE-USD | 2026-01-11 | 79.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | NEAR-USD | 2026-01-05 | 79.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.59% | -7.11% | 17.95% | 56.65% | -7.11% | 107.36% |
| SOL-USD | KAVA-USD | 2026-01-10 | 78.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | 0.00% | 23.31% | -16.11% | -23.42% | 23.31% |
| SOL-USD | XTZ-USD | 2018-11-03 | 78.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 21.01% | 0.00% | 22.38% | 147.35% | 0.00% | 179.64% |
| SOL-USD | QTUM-USD | 2018-10-24 | 77.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 13.12% | -5.39% | 29.47% | 61.55% | -5.39% | 61.55% |
| SOL-USD | BTC-USD | 2026-01-08 | 77.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.39% | -4.24% | 6.50% | -14.94% | -21.08% | 6.50% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | ETH-USD | 2026-01-10 | 75.89% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |

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

