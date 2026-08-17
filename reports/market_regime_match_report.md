# Market Regime Match Report

Generated: 2026-08-17 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.429 $ | False | -17.36% | -10.22% | BEAR | -17.36% | -10.22% |
| DOGE-USD | BEAR | 0.07010 $ | False | -31.90% | -16.72% | BEAR | -17.36% | -10.22% |
| SOL-USD | BEAR | 75,42 $ | False | -10.46% | -16.87% | BEAR | -17.36% | -10.22% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 6.19% | 17.60% | 31.21% | -2.49% | -18.22% | 20.38% | 31.45% | 47.99% | 57.50% | 13.74% | 57.78% | 134.82% |
| BTC-USD | SAME_BTC_REGIME | 22 | 54.55% | 4.00% | 9.91% | 26.25% | -4.45% | -15.46% | 17.54% | 23.00% | 45.49% | 40.91% | -12.36% | 43.23% | 126.23% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 56.52% | 5.70% | 10.69% | 29.94% | -5.64% | -15.65% | 17.99% | 22.83% | 44.97% | 47.83% | -12.16% | 55.48% | 120.35% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 55.00% | 4.99% | 10.49% | 29.25% | -4.45% | -11.39% | 17.54% | 22.67% | 47.99% | 45.00% | -12.36% | 50.21% | 134.82% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 14.31% | 28.91% | 40.78% | -8.40% | -30.32% | 26.07% | 39.56% | 51.89% | 47.50% | -2.05% | 17.10% | 103.11% |
| DOGE-USD | SAME_BTC_REGIME | 18 | 77.78% | 13.66% | 26.87% | 44.13% | -9.86% | -28.41% | 25.42% | 40.19% | 53.31% | 44.44% | -4.55% | 6.98% | 112.48% |
| DOGE-USD | SAME_ASSET_REGIME | 17 | 76.47% | 24.33% | 34.01% | 38.54% | -9.15% | -28.68% | 31.81% | 39.23% | 46.79% | 58.82% | 3.04% | 7.64% | 85.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 66.67% | 11.56% | 25.54% | 33.36% | -10.38% | -30.02% | 20.61% | 34.29% | 42.97% | 41.67% | -6.36% | 3.53% | 7.38% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 4.64% | 20.13% | 34.97% | -3.00% | -13.30% | 18.61% | 28.67% | 57.27% | 65.00% | 21.07% | 56.22% | 157.46% |
| SOL-USD | SAME_BTC_REGIME | 12 | 75.00% | 3.31% | 7.00% | 19.97% | -3.75% | -12.54% | 13.96% | 25.59% | 46.98% | 33.33% | -8.15% | 37.98% | 81.24% |
| SOL-USD | SAME_ASSET_REGIME | 10 | 80.00% | 3.86% | 14.18% | 37.46% | -4.08% | -9.98% | 20.12% | 30.14% | 63.07% | 40.00% | -9.43% | 79.10% | 183.15% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 9 | 77.78% | 3.53% | 15.48% | 54.44% | -3.25% | -8.11% | 22.14% | 32.41% | 77.55% | 33.33% | -11.79% | 68.39% | 149.71% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 54.55% | 4.00% | -4.45% | 23.00% | 40.91% | -12.36% | 45.16% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 100.00% | 16.65% | -0.47% | 41.45% | 100.00% | 42.95% | 102.58% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 13.51% | -16.05% | 34.61% | 50.00% | 24.41% | 115.13% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 71.43% | 2.71% | -0.89% | 23.07% | 57.14% | 38.53% | 81.27% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 18 | 77.78% | 13.66% | -9.86% | 40.19% | 44.44% | -4.55% | 47.66% |
| DOGE-USD | HISTORICAL_BTC_BULL | 19 | 52.63% | 13.45% | -5.75% | 39.90% | 47.37% | -0.89% | 50.61% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 24.33% | -8.70% | 28.68% | 66.67% | 5.82% | 52.26% |
| SOL-USD | HISTORICAL_BTC_BEAR | 12 | 75.00% | 3.31% | -3.75% | 25.59% | 33.33% | -8.15% | 58.19% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 10.20% | -7.94% | 31.45% | 57.14% | 6.51% | 60.16% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 21 | 66.67% | 5.57% | -1.66% | 25.79% | 85.71% | 36.82% | 104.38% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 56.52% | 5.70% | -5.64% | 22.83% | 47.83% | -12.16% | 64.13% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 85.71% | 16.65% | -0.47% | 43.56% | 85.71% | 54.46% | 185.19% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.46% | -17.03% | 27.03% | 0.00% | -24.07% | 28.66% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 85.71% | 5.11% | -0.89% | 23.07% | 71.43% | 38.53% | 67.21% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 17 | 76.47% | 24.33% | -9.15% | 39.23% | 58.82% | 3.04% | 54.20% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 13 | 61.54% | 13.45% | -1.13% | 36.32% | 46.15% | -0.89% | 41.88% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 58.23% | -7.19% | 58.23% | 100.00% | 150.14% | 154.68% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 9 | 55.56% | 2.44% | -9.97% | 27.82% | 22.22% | -18.28% | 41.87% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 10 | 80.00% | 3.86% | -4.08% | 30.14% | 40.00% | -9.43% | 105.92% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 13.69% | -3.24% | 32.03% | 66.67% | 48.19% | 112.82% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 60.00% | 3.09% | -7.94% | 25.79% | 40.00% | -1.64% | 29.69% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 61.01% | -1.30% | 108.24% | 100.00% | 165.76% | 274.22% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 17 | 58.82% | 2.71% | -1.75% | 20.52% | 82.35% | 27.84% | 58.32% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | BTC-USD | 2018-10-25 | 87.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.30% | -2.54% | 18.77% | 39.91% | -2.54% | 39.91% |
| BTC-USD | XRP-USD | 2026-01-10 | 87.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.44% | -2.44% | 6.41% | -17.87% | -21.60% | 6.41% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | NEO-USD | 2018-10-24 | 86.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.24% | -1.02% | 46.91% | 44.33% | -1.02% | 46.91% |
| BTC-USD | SOL-USD | 2026-01-08 | 86.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | ETC-USD | 2018-10-24 | 85.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| BTC-USD | THETA-USD | 2022-04-15 | 84.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -10.88% | 27.86% | -20.52% | -20.52% | 27.86% |
| BTC-USD | ETH-USD | 2026-01-10 | 84.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| BTC-USD | LTC-USD | 2018-10-25 | 84.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.38% | 0.00% | 57.75% | 132.10% | 0.00% | 132.10% |
| BTC-USD | XTZ-USD | 2026-01-10 | 83.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | OP-USD | 2026-01-06 | 89.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.03% | -0.09% | 43.84% | -9.51% | -24.09% | 43.84% |
| DOGE-USD | ADA-USD | 2022-03-27 | 86.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | NEO-USD | 2022-03-27 | 86.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | QTUM-USD | 2022-07-30 | 86.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.20% | -30.29% | 1.37% | -32.40% | -35.81% | 1.37% |
| DOGE-USD | FTM-USD | 2022-03-27 | 85.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.54% | -11.30% | 35.15% | 1.61% | -11.30% | 54.20% |
| DOGE-USD | CHZ-USD | 2022-03-26 | 85.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.08% | -1.30% | 51.20% | 116.30% | -1.30% | 153.33% |
| DOGE-USD | LINK-USD | 2022-03-27 | 85.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| DOGE-USD | DASH-USD | 2022-03-27 | 85.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LTC-USD | 2018-04-28 | 85.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.22% | -27.61% | 0.00% | -21.87% | -30.75% | 0.00% |
| DOGE-USD | THETA-USD | 2022-03-31 | 85.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 34.01% | -12.38% | 34.01% | -13.72% | -13.72% | 34.01% |
| SOL-USD | ENJ-USD | 2018-10-24 | 80.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 190.30% | -13.17% | 193.34% | 417.86% | -13.17% | 644.83% |
| SOL-USD | RUNE-USD | 2026-01-11 | 77.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | SOL-USD | 2026-01-08 | 77.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | NEAR-USD | 2026-01-10 | 76.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 20.47% | -4.92% | 22.14% | 68.39% | -4.92% | 112.24% |
| SOL-USD | QTUM-USD | 2018-10-29 | 76.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.48% | -3.25% | 32.41% | 82.67% | -3.25% | 86.97% |
| SOL-USD | BTC-USD | 2026-01-11 | 75.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.09% | -0.13% | 8.26% | -16.25% | -19.78% | 8.26% |
| SOL-USD | ETH-USD | 2026-01-10 | 75.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| SOL-USD | KAVA-USD | 2026-01-10 | 75.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | 0.00% | 23.31% | -16.11% | -23.42% | 23.31% |
| SOL-USD | BNB-USD | 2026-01-15 | 79.47% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |

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

