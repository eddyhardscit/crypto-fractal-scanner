# Market Regime Match Report

Generated: 2026-07-29 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.922 $ | False | -16.23% | -9.79% | BEAR | -16.23% | -9.79% |
| DOGE-USD | BEAR | 0.07061 $ | False | -33.70% | -16.13% | BEAR | -16.23% | -9.79% |
| SOL-USD | BEAR | 73,47 $ | False | -11.51% | -16.59% | BEAR | -16.23% | -9.79% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 13.10% | 35.13% | 49.37% | -4.49% | -32.12% | 18.83% | 41.43% | 62.95% | 62.50% | 9.43% | 42.05% | 67.22% |
| BTC-USD | SAME_BTC_REGIME | 14 | 85.71% | 10.38% | 18.13% | 34.89% | -4.25% | -13.63% | 13.61% | 32.90% | 48.49% | 57.14% | 2.99% | 9.43% | 43.04% |
| BTC-USD | SAME_ASSET_REGIME | 21 | 90.48% | 14.84% | 35.65% | 49.54% | -2.71% | -14.37% | 19.65% | 42.19% | 51.62% | 71.43% | 10.45% | 43.28% | 65.83% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 91.67% | 10.38% | 15.95% | 33.69% | -4.25% | -8.79% | 13.61% | 26.88% | 50.58% | 58.33% | 2.99% | 9.69% | 52.35% |
| DOGE-USD | ALL_MATCHES | 40 | 65.00% | 4.54% | 12.49% | 28.22% | -12.71% | -21.40% | 14.17% | 24.03% | 33.74% | 60.00% | 8.85% | 20.62% | 72.14% |
| DOGE-USD | SAME_BTC_REGIME | 22 | 81.82% | 7.13% | 15.11% | 28.00% | -10.31% | -18.52% | 14.97% | 22.19% | 33.32% | 77.27% | 11.89% | 18.70% | 36.52% |
| DOGE-USD | SAME_ASSET_REGIME | 26 | 76.92% | 7.13% | 17.37% | 30.43% | -10.31% | -19.81% | 14.17% | 22.19% | 33.05% | 76.92% | 14.66% | 35.64% | 76.78% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 80.00% | 7.13% | 13.93% | 27.20% | -10.31% | -19.20% | 14.17% | 19.04% | 32.15% | 75.00% | 11.60% | 17.78% | 37.15% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 9.45% | 25.28% | 46.86% | -4.33% | -20.60% | 14.98% | 36.36% | 55.50% | 72.50% | 5.41% | 36.76% | 105.22% |
| SOL-USD | SAME_BTC_REGIME | 23 | 91.30% | 9.53% | 19.49% | 40.31% | -3.06% | -10.69% | 15.01% | 27.20% | 40.82% | 73.91% | 2.71% | 23.32% | 77.78% |
| SOL-USD | SAME_ASSET_REGIME | 30 | 73.33% | 9.42% | 17.91% | 42.46% | -3.45% | -20.60% | 13.49% | 23.75% | 56.49% | 70.00% | 4.61% | 28.82% | 80.60% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 89.47% | 9.45% | 14.56% | 24.41% | -3.06% | -10.47% | 14.26% | 19.57% | 37.44% | 68.42% | 2.51% | 14.56% | 77.45% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 85.71% | 10.38% | -4.25% | 32.90% | 57.14% | 2.99% | 32.90% |
| BTC-USD | HISTORICAL_BTC_BULL | 22 | 68.18% | 19.31% | -3.60% | 43.89% | 63.64% | 30.11% | 62.95% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -11.19% | -20.14% | 3.93% | 66.67% | 16.42% | 19.52% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 22 | 81.82% | 7.13% | -10.31% | 22.19% | 77.27% | 11.89% | 55.83% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 4.54% | -11.06% | 30.02% | 37.50% | -12.89% | 52.97% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.74% | -20.84% | 2.91% | 100.00% | 14.25% | 20.66% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 9 | 33.33% | -10.84% | -18.65% | 19.23% | 33.33% | -6.60% | 65.99% |
| SOL-USD | HISTORICAL_BTC_BEAR | 23 | 91.30% | 9.53% | -3.06% | 27.20% | 73.91% | 2.71% | 41.84% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 23.40% | -2.31% | 51.15% | 85.71% | 23.57% | 82.85% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 9 | 22.22% | -10.22% | -20.14% | 4.69% | 55.56% | 18.07% | 111.01% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 21 | 90.48% | 14.84% | -2.71% | 42.19% | 71.43% | 10.45% | 59.40% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 45.45% | -19.69% | -26.89% | 28.98% | 45.45% | -26.19% | 54.07% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 49.35% | 0.00% | 64.13% | 100.00% | 46.87% | 64.13% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 3 | 66.67% | 33.93% | -4.48% | 45.34% | 66.67% | 9.42% | 72.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 50.00% | -1.17% | -12.13% | 33.38% | 50.00% | -6.07% | 39.45% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 26 | 76.92% | 7.13% | -10.31% | 22.19% | 76.92% | 14.66% | 68.77% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.72% | -6.55% | 33.07% | 40.00% | -5.85% | 75.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 9 | 33.33% | -7.26% | -17.65% | 18.25% | 22.22% | -8.44% | 18.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 73.33% | 9.42% | -3.45% | 23.75% | 70.00% | 4.61% | 62.89% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 2.34% | -8.74% | 29.92% | 75.00% | 4.36% | 128.48% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 30.90% | -1.74% | 30.90% | 100.00% | 35.13% | 47.19% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 39.02% | -2.24% | 49.77% | 100.00% | 25.53% | 90.33% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 14.95% | -10.48% | 30.87% | 66.67% | 2.44% | 65.72% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 89.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | ONE-USD | 2020-01-27 | 89.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| BTC-USD | XRP-USD | 2025-12-21 | 88.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | -0.53% | 11.68% | 0.43% | -1.24% | 12.21% |
| BTC-USD | ETH-USD | 2025-12-21 | 87.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.36% | 0.00% | 19.65% | -0.57% | -0.79% | 19.65% |
| BTC-USD | BTC-USD | 2018-10-06 | 87.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | -4.32% | 4.94% | 10.45% | -4.32% | 16.59% |
| BTC-USD | XRP-USD | 2019-10-14 | 87.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.85% | -7.06% | 41.18% | -33.30% | -41.12% | 41.18% |
| BTC-USD | BNB-USD | 2018-10-04 | 86.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | XTZ-USD | 2025-12-26 | 85.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| BTC-USD | BTC-USD | 2025-12-23 | 85.89% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.84% | -1.75% | 15.54% | 8.08% | -1.75% | 20.65% |
| BTC-USD | QTUM-USD | 2020-01-27 | 85.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.22% | -8.83% | 22.12% | 9.44% | -8.83% | 22.12% |
| DOGE-USD | OP-USD | 2025-12-22 | 90.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | VET-USD | 2022-03-14 | 89.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.68% | -8.95% | 11.10% | 9.39% | -8.95% | 41.71% |
| DOGE-USD | THETA-USD | 2022-03-16 | 89.11% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.32% | -16.14% | 13.49% | -6.06% | -16.14% | 28.27% |
| DOGE-USD | LTC-USD | 2018-04-14 | 88.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.24% | -35.07% | 7.37% | -31.89% | -37.88% | 7.37% |
| DOGE-USD | HBAR-USD | 2022-03-14 | 88.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.78% | -18.79% | 1.28% | -7.73% | -18.79% | 12.96% |
| DOGE-USD | ENJ-USD | 2022-03-17 | 88.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.44% | -14.62% | 14.24% | 4.04% | -14.62% | 29.60% |
| DOGE-USD | FIL-USD | 2022-03-16 | 88.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.69% | -12.34% | 5.53% | 8.99% | -12.34% | 69.70% |
| DOGE-USD | DASH-USD | 2022-03-12 | 88.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.34% | -9.62% | 18.11% | 13.82% | -9.62% | 28.65% |
| DOGE-USD | INJ-USD | 2022-03-14 | 87.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.78% | -13.07% | 7.82% | 19.15% | -13.07% | 55.30% |
| DOGE-USD | RUNE-USD | 2022-03-08 | 87.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -22.98% | 22.31% | 37.54% | -22.98% | 46.15% |
| SOL-USD | NEAR-USD | 2025-12-21 | 80.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.29% | 0.00% | 23.51% | 104.94% | 0.00% | 139.37% |
| SOL-USD | RUNE-USD | 2025-12-27 | 78.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.91% | -0.37% | 41.91% | -5.22% | -5.22% | 62.96% |
| SOL-USD | LINK-USD | 2025-12-21 | 78.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.89% | 0.00% | 11.78% | 4.70% | 0.00% | 24.41% |
| SOL-USD | BNB-USD | 2025-12-26 | 78.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| SOL-USD | EOS-USD | 2018-10-19 | 77.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.40% | -7.62% | 75.20% | 77.34% | -7.62% | 77.34% |
| SOL-USD | SOL-USD | 2025-12-24 | 77.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| SOL-USD | ONE-USD | 2020-01-27 | 77.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| SOL-USD | BTC-USD | 2025-12-23 | 76.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.84% | -1.75% | 15.54% | 8.08% | -1.75% | 20.65% |
| SOL-USD | DOT-USD | 2025-12-21 | 76.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.50% | -6.20% | 7.56% | -4.04% | -6.20% | 11.28% |
| SOL-USD | KAVA-USD | 2025-12-21 | 76.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.72% | -7.96% | 14.26% | 2.51% | -7.96% | 24.10% |

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

