# Market Regime Match Report

Generated: 2026-07-23 07:37 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 65.400 $ | False | -15.58% | -9.90% | BEAR | -15.58% | -9.90% |
| DOGE-USD | BEAR | 0.07226 $ | False | -26.59% | -16.11% | BEAR | -15.58% | -9.90% |
| SOL-USD | BEAR | 77,11 $ | False | -10.57% | -16.91% | BEAR | -15.58% | -9.90% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 10.04% | 23.31% | 29.52% | -11.34% | -28.78% | 13.86% | 27.13% | 33.06% | 57.50% | 11.71% | 43.89% | 78.22% |
| BTC-USD | SAME_BTC_REGIME | 7 | 85.71% | 6.86% | 21.12% | 31.24% | -8.55% | -16.91% | 11.67% | 28.73% | 44.81% | 42.86% | -3.23% | 11.71% | 18.58% |
| BTC-USD | SAME_ASSET_REGIME | 22 | 86.36% | 22.37% | 26.46% | 30.33% | -9.07% | -13.72% | 22.53% | 28.96% | 43.50% | 72.73% | 29.73% | 48.04% | 76.00% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 7 | 85.71% | 6.86% | 21.12% | 31.24% | -8.55% | -16.91% | 11.67% | 28.73% | 44.81% | 42.86% | -3.23% | 11.71% | 18.58% |
| DOGE-USD | ALL_MATCHES | 40 | 47.50% | -0.99% | 12.21% | 27.88% | -14.61% | -35.19% | 13.74% | 21.46% | 33.95% | 75.00% | 19.64% | 38.94% | 57.40% |
| DOGE-USD | SAME_BTC_REGIME | 28 | 50.00% | -0.40% | 12.46% | 28.21% | -14.10% | -35.27% | 13.83% | 20.82% | 35.21% | 82.14% | 21.48% | 42.37% | 57.99% |
| DOGE-USD | SAME_ASSET_REGIME | 29 | 48.28% | -0.80% | 15.02% | 28.05% | -10.05% | -35.23% | 15.47% | 22.48% | 34.58% | 82.76% | 24.58% | 48.98% | 57.70% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 27 | 48.15% | -0.80% | 13.31% | 28.38% | -13.72% | -35.32% | 14.12% | 21.81% | 35.83% | 81.48% | 23.23% | 44.60% | 58.29% |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 3.79% | 15.82% | 30.00% | -8.66% | -22.41% | 10.31% | 22.70% | 44.49% | 70.00% | 5.43% | 28.39% | 66.47% |
| SOL-USD | SAME_BTC_REGIME | 22 | 68.18% | 4.57% | 17.08% | 34.71% | -8.86% | -22.24% | 10.89% | 24.80% | 50.83% | 81.82% | 6.65% | 25.23% | 84.12% |
| SOL-USD | SAME_ASSET_REGIME | 27 | 66.67% | 5.72% | 20.55% | 41.83% | -8.49% | -21.91% | 12.11% | 24.49% | 57.62% | 77.78% | 7.75% | 32.38% | 73.36% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 22 | 68.18% | 4.57% | 17.08% | 34.71% | -8.86% | -22.24% | 10.89% | 24.80% | 50.83% | 81.82% | 6.65% | 25.23% | 84.12% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 7 | 85.71% | 6.86% | -8.55% | 28.73% | 42.86% | -3.23% | 39.20% |
| BTC-USD | HISTORICAL_BTC_BULL | 24 | 58.33% | 13.19% | -10.87% | 27.13% | 66.67% | 31.23% | 58.92% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 9 | 55.56% | 8.85% | -13.46% | 22.26% | 44.44% | -3.08% | 39.13% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 50.00% | -0.40% | -14.10% | 20.82% | 82.14% | 21.48% | 59.69% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 14.01% | -6.83% | 32.09% | 60.00% | 27.74% | 50.85% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 7 | 14.29% | -17.99% | -24.85% | 13.61% | 57.14% | 0.59% | 23.33% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 68.18% | 4.57% | -8.86% | 24.80% | 81.82% | 6.65% | 74.63% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -3.92% | -8.33% | 22.59% | 77.78% | 7.46% | 36.59% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -16.48% | -17.11% | 2.98% | 0.00% | -21.33% | 2.98% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 8 | 75.00% | 6.51% | -7.31% | 18.19% | 37.50% | -6.51% | 41.35% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 22 | 86.36% | 22.37% | -9.07% | 28.96% | 72.73% | 29.73% | 62.17% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 27.27% | -16.23% | -22.79% | 21.67% | 45.45% | -5.18% | 50.90% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -37.22% | -39.28% | 4.09% | 0.00% | -36.70% | 4.09% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | -3.17% | -11.85% | 16.06% | 33.33% | -6.00% | 20.40% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 29 | 48.28% | -0.80% | -10.05% | 22.48% | 82.76% | 24.58% | 59.53% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 11.44% | -12.74% | 36.78% | 75.00% | 15.77% | 58.21% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -17.98% | -19.91% | 13.61% | 42.86% | -8.92% | 16.67% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 66.67% | 5.72% | -8.49% | 24.49% | 77.78% | 7.75% | 67.90% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 16.67% | -9.66% | -15.15% | 14.58% | 66.67% | 3.31% | 20.55% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 19.99% | -1.20% | 24.50% | 100.00% | 42.40% | 47.99% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 83.33% | 6.51% | -7.56% | 14.78% | 33.33% | -5.66% | 32.90% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-09 | 89.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | ETH-USD | 2025-12-16 | 86.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -8.55% | 11.67% | -3.23% | -8.55% | 11.67% |
| BTC-USD | XRP-USD | 2025-12-16 | 86.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.37% | -6.98% | 4.44% | -4.54% | -6.98% | 4.94% |
| BTC-USD | MKR-USD | 2020-01-23 | 86.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.42% | -10.98% | 43.69% | 27.94% | -10.98% | 94.10% |
| BTC-USD | BTC-USD | 2025-12-17 | 85.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.82% | -4.12% | 13.78% | 12.34% | -4.12% | 19.40% |
| BTC-USD | OMG-USD | 2018-10-04 | 85.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.64% | -21.63% | 0.39% | 11.07% | -21.63% | 11.07% |
| BTC-USD | THETA-USD | 2022-03-21 | 85.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.86% | -13.75% | 6.86% | -10.80% | -13.75% | 31.92% |
| BTC-USD | SAND-USD | 2023-06-29 | 89.94% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 24.82% | -6.32% | 24.82% | 49.53% | -6.32% | 49.53% |
| BTC-USD | LRC-USD | 2018-09-29 | 89.93% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.04% | -13.46% | 133.38% | 29.74% | -13.46% | 133.38% |
| BTC-USD | FIL-USD | 2023-06-29 | 89.06% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 23.33% | -4.87% | 23.33% | 43.44% | -4.87% | 56.53% |
| DOGE-USD | OP-USD | 2025-12-17 | 89.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.02% | -6.29% | 23.81% | 19.12% | -6.29% | 58.54% |
| DOGE-USD | VET-USD | 2022-03-09 | 89.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.43% | -5.37% | 15.47% | 38.55% | -5.37% | 47.28% |
| DOGE-USD | MKR-USD | 2022-09-24 | 88.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.72% | -1.56% | 39.59% | 72.17% | -1.56% | 80.88% |
| DOGE-USD | THETA-USD | 2022-03-11 | 88.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.61% | -6.22% | 26.91% | 19.72% | -6.22% | 43.44% |
| DOGE-USD | INJ-USD | 2022-03-04 | 88.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.36% | -35.14% | 0.00% | 0.31% | -36.02% | 0.31% |
| DOGE-USD | DASH-USD | 2022-03-07 | 88.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | XRP-USD | 2019-10-04 | 87.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| DOGE-USD | HBAR-USD | 2022-03-09 | 87.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.03% | -8.48% | 14.12% | 19.55% | -8.48% | 27.29% |
| DOGE-USD | OMG-USD | 2022-03-07 | 87.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.54% | -14.76% | 5.54% | 24.58% | -14.76% | 24.58% |
| DOGE-USD | LTC-USD | 2018-04-08 | 87.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -35.58% | -35.58% | 6.16% | -33.12% | -38.94% | 6.16% |
| SOL-USD | QTUM-USD | 2018-10-04 | 80.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.14% | -19.10% | 3.33% | -0.16% | -19.10% | 10.72% |
| SOL-USD | ENJ-USD | 2018-10-04 | 79.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -12.02% | -26.93% | 5.36% | 445.37% | -26.93% | 526.80% |
| SOL-USD | NEAR-USD | 2025-12-16 | 78.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.14% | -9.23% | 12.11% | 87.14% | -9.23% | 91.97% |
| SOL-USD | BNB-USD | 2025-12-21 | 78.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | LINK-USD | 2025-12-16 | 78.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.03% | -10.34% | 2.67% | 0.58% | -10.34% | 14.27% |
| SOL-USD | RUNE-USD | 2025-12-17 | 78.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.50% | -7.03% | 20.04% | 9.91% | -7.03% | 54.43% |
| SOL-USD | SOL-USD | 2025-12-19 | 77.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | LRC-USD | 2018-10-04 | 77.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| SOL-USD | APT-USD | 2024-09-16 | 77.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.47% | -29.47% | 7.73% | -30.92% | -30.92% | 7.73% |
| SOL-USD | EOS-USD | 2018-10-14 | 77.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 66.62% | -4.37% | 66.62% | 55.08% | -4.37% | 81.36% |

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

