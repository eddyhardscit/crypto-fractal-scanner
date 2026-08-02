# Market Regime Match Report

Generated: 2026-08-02 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.406 $ | False | -20.56% | -9.85% | BEAR | -20.56% | -9.85% |
| DOGE-USD | BEAR | 0.07014 $ | False | -36.30% | -16.37% | BEAR | -20.56% | -9.85% |
| SOL-USD | BEAR | 73,42 $ | False | -12.68% | -16.79% | BEAR | -20.56% | -9.85% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 8.14% | 25.22% | 51.43% | -3.12% | -19.16% | 14.02% | 40.79% | 64.29% | 55.00% | 6.70% | 45.17% | 78.24% |
| BTC-USD | SAME_BTC_REGIME | 12 | 83.33% | 5.55% | 10.55% | 14.73% | -2.05% | -12.76% | 9.95% | 13.85% | 17.31% | 25.00% | -10.87% | -4.96% | 4.34% |
| BTC-USD | SAME_ASSET_REGIME | 20 | 85.00% | 10.59% | 30.46% | 51.43% | -1.80% | -10.34% | 17.27% | 44.46% | 62.23% | 60.00% | 17.21% | 64.92% | 103.56% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 90.00% | 6.28% | 12.59% | 15.10% | -1.11% | -10.70% | 11.33% | 16.10% | 19.70% | 30.00% | -9.66% | 0.15% | 11.86% |
| DOGE-USD | ALL_MATCHES | 40 | 65.00% | 6.97% | 17.87% | 29.56% | -11.77% | -30.06% | 16.62% | 29.23% | 44.33% | 62.50% | 4.97% | 16.34% | 72.02% |
| DOGE-USD | SAME_BTC_REGIME | 21 | 76.19% | 6.51% | 16.75% | 27.99% | -13.35% | -18.23% | 14.24% | 18.11% | 33.34% | 71.43% | 5.90% | 13.77% | 18.18% |
| DOGE-USD | SAME_ASSET_REGIME | 21 | 80.95% | 7.44% | 16.84% | 29.45% | -11.66% | -16.44% | 14.24% | 22.25% | 33.34% | 71.43% | 5.90% | 30.97% | 70.99% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 17 | 76.47% | 4.83% | 13.34% | 16.79% | -13.62% | -17.16% | 10.38% | 16.77% | 19.77% | 64.71% | 2.89% | 13.77% | 21.82% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 9.58% | 24.57% | 60.68% | -4.48% | -20.41% | 14.16% | 27.51% | 62.58% | 60.00% | 5.70% | 43.76% | 125.14% |
| SOL-USD | SAME_BTC_REGIME | 21 | 85.71% | 11.57% | 17.32% | 41.91% | -2.36% | -11.80% | 14.21% | 24.96% | 48.32% | 61.90% | 4.52% | 32.48% | 88.49% |
| SOL-USD | SAME_ASSET_REGIME | 28 | 75.00% | 9.58% | 19.23% | 44.83% | -2.59% | -21.37% | 14.16% | 25.38% | 51.99% | 64.29% | 7.41% | 54.65% | 100.07% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 90.00% | 11.60% | 19.23% | 42.88% | -1.55% | -11.66% | 15.56% | 25.38% | 50.22% | 65.00% | 5.58% | 43.52% | 92.06% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 12 | 83.33% | 5.55% | -2.05% | 13.85% | 25.00% | -10.87% | 21.58% |
| BTC-USD | HISTORICAL_BTC_BULL | 18 | 72.22% | 20.86% | -4.57% | 48.43% | 66.67% | 17.15% | 60.04% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -2.54% | -2.54% | 68.05% | 100.00% | 98.26% | 134.71% |
| BTC-USD | HISTORICAL_BTC_MIXED | 3 | 100.00% | 12.97% | -2.65% | 22.86% | 33.33% | -5.83% | 31.45% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 50.00% | 5.17% | -3.89% | 68.56% | 75.00% | 19.76% | 123.40% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 21 | 76.19% | 6.51% | -13.35% | 18.11% | 71.43% | 5.90% | 53.75% |
| DOGE-USD | HISTORICAL_BTC_BULL | 12 | 58.33% | 10.11% | -7.88% | 34.88% | 58.33% | 4.39% | 71.04% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 7 | 42.86% | -6.23% | -18.07% | 31.09% | 42.86% | -4.34% | 55.53% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 85.71% | 11.57% | -2.36% | 24.96% | 61.90% | 4.52% | 62.96% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 60.00% | 10.20% | -9.36% | 36.61% | 60.00% | 12.39% | 57.24% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 52.24% | -6.77% | 90.71% | 100.00% | 41.96% | 110.46% |
| SOL-USD | HISTORICAL_BTC_MIXED | 3 | 100.00% | 13.99% | -1.30% | 39.59% | 66.67% | 10.39% | 119.29% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 4 | 0.00% | -16.90% | -25.72% | 3.96% | 25.00% | -13.25% | 135.63% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 85.00% | 10.59% | -1.80% | 44.46% | 60.00% | 17.21% | 90.78% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 55.56% | 1.78% | -15.02% | 35.94% | 55.56% | 10.93% | 58.55% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 25.26% | -0.11% | 35.46% | 100.00% | 42.26% | 50.68% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 68.06% | -1.33% | 96.14% | 100.00% | 45.08% | 100.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 50.00% | 0.55% | -8.41% | 10.81% | 25.00% | -7.64% | 15.52% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 21 | 80.95% | 7.44% | -11.66% | 22.25% | 71.43% | 5.90% | 66.25% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 8.28% | -11.88% | 29.16% | 60.00% | 7.68% | 85.40% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 13.08% | -17.22% | 25.72% | 100.00% | 12.97% | 61.37% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 12 | 41.67% | -4.17% | -12.41% | 30.90% | 41.67% | -8.76% | 31.32% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 75.00% | 9.58% | -2.59% | 25.38% | 64.29% | 7.41% | 86.53% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 47.93% | -4.16% | 71.68% | 100.00% | 162.44% | 314.21% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -13.44% | -14.29% | 14.96% | 33.33% | -13.10% | 21.74% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 110.91% | 0.00% | 118.05% | 100.00% | 42.57% | 118.05% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 6.04% | -10.60% | 24.15% | 33.33% | -3.07% | 39.56% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-26 | 89.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.81% | 0.00% | 12.27% | -8.77% | -8.77% | 12.81% |
| BTC-USD | ETH-USD | 2025-12-26 | 88.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.61% | 0.00% | 17.22% | -12.28% | -12.28% | 17.22% |
| BTC-USD | BTC-USD | 2025-12-27 | 87.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 17.32% | -0.18% | 17.32% | -7.51% | -7.51% | 19.07% |
| BTC-USD | BNB-USD | 2025-12-26 | 86.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| BTC-USD | XTZ-USD | 2018-10-14 | 86.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 9.53% | -14.08% | 9.53% | 77.90% | -14.08% | 96.71% |
| BTC-USD | XRP-USD | 2019-10-14 | 85.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.85% | -7.06% | 41.18% | -33.30% | -41.12% | 41.18% |
| BTC-USD | XTZ-USD | 2025-12-26 | 85.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| BTC-USD | SOL-USD | 2025-12-24 | 85.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| BTC-USD | ETC-USD | 2025-12-26 | 85.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.56% | -5.82% | 2.55% | -10.55% | -11.99% | 15.34% |
| BTC-USD | QTUM-USD | 2025-12-26 | 85.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.97% | -10.32% | 0.75% | -15.48% | -16.50% | 8.73% |
| DOGE-USD | OP-USD | 2025-12-27 | 90.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.75% | -2.92% | 22.25% | 1.62% | -2.92% | 56.55% |
| DOGE-USD | VET-USD | 2022-03-19 | 90.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.00% | -11.66% | 7.24% | 10.13% | -11.66% | 37.50% |
| DOGE-USD | LTC-USD | 2018-04-13 | 89.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.07% | -36.07% | 5.71% | -35.67% | -38.84% | 5.71% |
| DOGE-USD | HBAR-USD | 2022-03-19 | 89.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.48% | -13.35% | 6.89% | 1.24% | -13.35% | 20.52% |
| DOGE-USD | XTZ-USD | 2025-12-26 | 88.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| DOGE-USD | DASH-USD | 2022-03-12 | 88.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.34% | -9.62% | 18.11% | 13.82% | -9.62% | 28.65% |
| DOGE-USD | INJ-USD | 2022-03-19 | 88.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.63% | -13.94% | 4.96% | 30.97% | -13.94% | 53.75% |
| DOGE-USD | ADA-USD | 2022-03-17 | 88.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.92% | -16.28% | 3.63% | -6.81% | -16.28% | 14.25% |
| DOGE-USD | BAT-USD | 2018-10-14 | 88.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.84% | -13.62% | 17.16% | 62.34% | -13.62% | 69.37% |
| DOGE-USD | ENJ-USD | 2022-03-17 | 88.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.44% | -14.62% | 14.24% | 4.04% | -14.62% | 29.60% |
| SOL-USD | RUNE-USD | 2025-12-27 | 79.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.91% | -0.37% | 41.91% | -5.22% | -5.22% | 62.96% |
| SOL-USD | NEAR-USD | 2025-12-26 | 79.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 0.47% | -0.75% | 14.11% | 124.27% | -0.75% | 124.27% |
| SOL-USD | QTUM-USD | 2018-10-14 | 79.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.45% | -14.45% | 6.45% | 24.60% | -14.45% | 33.28% |
| SOL-USD | SOL-USD | 2025-12-24 | 78.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| SOL-USD | EOS-USD | 2018-10-24 | 78.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.66% | 0.00% | 83.90% | 81.05% | 0.00% | 86.15% |
| SOL-USD | KAVA-USD | 2025-12-26 | 78.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.96% | -2.75% | 24.96% | 1.20% | -2.75% | 31.13% |
| SOL-USD | BNB-USD | 2025-12-26 | 77.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| SOL-USD | LINK-USD | 2025-12-26 | 77.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.60% | 0.00% | 10.72% | -4.12% | -4.12% | 23.23% |
| SOL-USD | DOT-USD | 2025-12-21 | 77.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.50% | -6.20% | 7.56% | -4.04% | -6.20% | 11.28% |
| SOL-USD | BTC-USD | 2025-12-27 | 77.06% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 17.32% | -0.18% | 17.32% | -7.51% | -7.51% | 19.07% |

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

