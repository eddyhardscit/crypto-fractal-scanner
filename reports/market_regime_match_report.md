# Market Regime Match Report

Generated: 2026-08-01 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.065 $ | False | -19.71% | -9.83% | BEAR | -19.71% | -9.83% |
| DOGE-USD | BEAR | 0.07009 $ | False | -35.26% | -16.29% | BEAR | -19.71% | -9.83% |
| SOL-USD | BEAR | 73,12 $ | False | -12.86% | -16.72% | BEAR | -19.71% | -9.83% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 75.00% | 6.31% | 23.54% | 51.43% | -2.60% | -28.37% | 14.79% | 40.35% | 64.29% | 57.50% | 6.70% | 43.76% | 70.10% |
| BTC-USD | SAME_BTC_REGIME | 11 | 90.91% | 5.81% | 14.23% | 18.63% | -2.03% | -10.87% | 12.27% | 17.93% | 24.99% | 27.27% | -10.09% | -1.08% | 4.52% |
| BTC-USD | SAME_ASSET_REGIME | 21 | 85.71% | 6.75% | 35.65% | 50.41% | -2.03% | -11.31% | 17.22% | 41.18% | 60.53% | 61.90% | 16.42% | 49.70% | 98.26% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 8 | 100.00% | 6.28% | 13.92% | 15.99% | -0.09% | -8.20% | 12.50% | 17.58% | 25.40% | 25.00% | -9.43% | -2.98% | 3.25% |
| DOGE-USD | ALL_MATCHES | 40 | 62.50% | 6.13% | 17.11% | 31.21% | -11.77% | -30.06% | 15.08% | 28.70% | 44.33% | 65.00% | 8.94% | 17.21% | 72.02% |
| DOGE-USD | SAME_BTC_REGIME | 22 | 72.73% | 9.00% | 16.49% | 27.86% | -11.33% | -22.55% | 15.08% | 18.81% | 32.86% | 72.73% | 11.36% | 15.56% | 29.69% |
| DOGE-USD | SAME_ASSET_REGIME | 22 | 72.73% | 9.00% | 16.49% | 28.62% | -11.33% | -20.38% | 14.35% | 18.81% | 33.28% | 72.73% | 13.80% | 27.45% | 70.12% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 72.22% | 6.13% | 14.19% | 16.78% | -12.50% | -18.37% | 13.87% | 17.06% | 20.00% | 66.67% | 7.09% | 15.56% | 40.38% |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 5.70% | 20.87% | 52.55% | -6.97% | -21.92% | 10.03% | 25.92% | 64.24% | 55.00% | 1.95% | 33.33% | 81.92% |
| SOL-USD | SAME_BTC_REGIME | 19 | 84.21% | 6.75% | 16.46% | 28.35% | -1.77% | -12.33% | 12.72% | 22.79% | 37.44% | 57.89% | 1.20% | 22.82% | 77.52% |
| SOL-USD | SAME_ASSET_REGIME | 30 | 70.00% | 6.60% | 19.68% | 42.88% | -2.59% | -21.92% | 11.72% | 24.68% | 62.87% | 60.00% | 3.61% | 38.68% | 81.92% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 88.89% | 7.17% | 17.55% | 30.04% | -1.07% | -12.28% | 12.87% | 23.15% | 37.99% | 61.11% | 1.95% | 23.71% | 77.96% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 11 | 90.91% | 5.81% | -2.03% | 17.93% | 27.27% | -10.09% | 22.69% |
| BTC-USD | HISTORICAL_BTC_BULL | 16 | 81.25% | 20.69% | -3.05% | 52.94% | 68.75% | 21.48% | 65.82% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -2.54% | -2.54% | 68.05% | 100.00% | 98.26% | 134.71% |
| BTC-USD | HISTORICAL_BTC_MIXED | 2 | 100.00% | 19.09% | -1.50% | 26.63% | 50.00% | 20.88% | 39.51% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 50.00% | 2.11% | -10.74% | 19.10% | 62.50% | 13.28% | 51.47% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 22 | 72.73% | 9.00% | -11.33% | 18.81% | 72.73% | 11.36% | 51.21% |
| DOGE-USD | HISTORICAL_BTC_BULL | 11 | 63.64% | 8.28% | -7.26% | 43.96% | 63.64% | 7.68% | 53.55% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.74% | -20.84% | 2.91% | 100.00% | 14.25% | 20.66% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 33.33% | -8.54% | -21.38% | 28.08% | 33.33% | -9.47% | 65.65% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 84.21% | 6.75% | -1.77% | 22.79% | 57.89% | 1.20% | 34.80% |
| SOL-USD | HISTORICAL_BTC_BULL | 12 | 50.00% | -1.92% | -9.36% | 31.39% | 50.00% | 2.23% | 46.89% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 52.24% | -6.77% | 90.71% | 100.00% | 41.96% | 110.46% |
| SOL-USD | HISTORICAL_BTC_MIXED | 2 | 100.00% | 37.51% | -4.05% | 50.37% | 50.00% | 107.82% | 169.93% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -14.15% | -24.73% | 4.63% | 40.00% | -10.89% | 111.01% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 21 | 85.71% | 6.75% | -2.03% | 41.18% | 61.90% | 16.42% | 77.49% |
| BTC-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 3.83% | -7.56% | 32.94% | 50.00% | -10.62% | 42.54% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 3 | 66.67% | 25.21% | -2.65% | 74.23% | 66.67% | 42.57% | 82.82% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 62.50% | 4.11% | -6.96% | 26.60% | 50.00% | 1.52% | 34.58% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 22 | 72.73% | 9.00% | -11.33% | 18.81% | 72.73% | 13.80% | 55.85% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 13.10% | -8.53% | 34.85% | 66.67% | 12.13% | 74.26% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 13.08% | -17.22% | 25.72% | 100.00% | 12.97% | 61.37% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -6.75% | -16.15% | 33.37% | 40.00% | -9.89% | 33.98% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 70.00% | 6.60% | -2.59% | 24.68% | 60.00% | 3.61% | 80.35% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | -17.31% | -24.50% | 4.61% | 50.00% | -20.90% | 4.61% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 5.50% | -7.15% | 21.87% | 50.00% | 3.45% | 32.04% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 110.91% | 0.00% | 118.05% | 100.00% | 42.57% | 118.05% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -0.90% | -10.48% | 15.31% | 20.00% | -5.83% | 16.16% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-26 | 87.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.81% | 0.00% | 12.27% | -8.77% | -8.77% | 12.81% |
| BTC-USD | ETH-USD | 2025-12-26 | 87.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.61% | 0.00% | 17.22% | -12.28% | -12.28% | 17.22% |
| BTC-USD | XRP-USD | 2019-10-14 | 87.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.85% | -7.06% | 41.18% | -33.30% | -41.12% | 41.18% |
| BTC-USD | BNB-USD | 2025-12-26 | 86.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| BTC-USD | BTC-USD | 2025-12-26 | 86.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.63% | 0.00% | 18.63% | -4.87% | -4.87% | 22.07% |
| BTC-USD | XTZ-USD | 2025-12-26 | 86.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| BTC-USD | SOL-USD | 2025-12-24 | 85.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| BTC-USD | LTC-USD | 2020-01-27 | 85.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.82% | -10.87% | 2.86% | -10.09% | -11.93% | 2.86% |
| BTC-USD | ETH-USD | 2018-07-06 | 86.60% | BEAR | RECOVERY | SAME_BTC_ONLY | MIXED | 5.29% | -2.06% | 9.31% | -54.67% | -55.49% | 9.31% |
| BTC-USD | EOS-USD | 2020-01-27 | 85.72% | BEAR | RECOVERY | SAME_BTC_ONLY | MIXED | -1.64% | -13.03% | 1.65% | -11.18% | -15.14% | 1.94% |
| DOGE-USD | OP-USD | 2025-12-27 | 90.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.75% | -2.92% | 22.25% | 1.62% | -2.92% | 56.55% |
| DOGE-USD | LTC-USD | 2018-04-12 | 89.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.99% | -34.14% | 7.89% | -34.63% | -37.58% | 7.89% |
| DOGE-USD | VET-USD | 2022-03-19 | 89.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.00% | -11.66% | 7.24% | 10.13% | -11.66% | 37.50% |
| DOGE-USD | DASH-USD | 2022-03-12 | 89.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.34% | -9.62% | 18.11% | 13.82% | -9.62% | 28.65% |
| DOGE-USD | XTZ-USD | 2025-12-26 | 89.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| DOGE-USD | ENJ-USD | 2022-03-17 | 88.77% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.44% | -14.62% | 14.24% | 4.04% | -14.62% | 29.60% |
| DOGE-USD | HBAR-USD | 2022-03-19 | 88.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.48% | -13.35% | 6.89% | 1.24% | -13.35% | 20.52% |
| DOGE-USD | THETA-USD | 2022-03-16 | 88.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.32% | -16.14% | 13.49% | -6.06% | -16.14% | 28.27% |
| DOGE-USD | INJ-USD | 2022-03-19 | 88.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.63% | -13.94% | 4.96% | 30.97% | -13.94% | 53.75% |
| DOGE-USD | ADA-USD | 2022-03-17 | 88.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.92% | -16.28% | 3.63% | -6.81% | -16.28% | 14.25% |
| SOL-USD | RUNE-USD | 2025-12-27 | 80.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.91% | -0.37% | 41.91% | -5.22% | -5.22% | 62.96% |
| SOL-USD | SOL-USD | 2025-12-24 | 79.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| SOL-USD | BNB-USD | 2025-12-26 | 78.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| SOL-USD | NEAR-USD | 2025-12-21 | 78.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.29% | 0.00% | 23.51% | 104.94% | 0.00% | 139.37% |
| SOL-USD | KAVA-USD | 2025-12-26 | 78.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.96% | -2.75% | 24.96% | 1.20% | -2.75% | 31.13% |
| SOL-USD | QTUM-USD | 2018-10-14 | 78.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.45% | -14.45% | 6.45% | 24.60% | -14.45% | 33.28% |
| SOL-USD | EOS-USD | 2018-10-24 | 77.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.66% | 0.00% | 83.90% | 81.05% | 0.00% | 86.15% |
| SOL-USD | BTC-USD | 2025-12-26 | 77.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.63% | 0.00% | 18.63% | -4.87% | -4.87% | 22.07% |
| SOL-USD | LINK-USD | 2025-12-26 | 76.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.60% | 0.00% | 10.72% | -4.12% | -4.12% | 23.23% |
| SOL-USD | DOT-USD | 2025-12-21 | 76.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.50% | -6.20% | 7.56% | -4.04% | -6.20% | 11.28% |

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

