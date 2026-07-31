# Market Regime Match Report

Generated: 2026-07-31 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.330 $ | False | -18.19% | -9.81% | BEAR | -18.19% | -9.81% |
| DOGE-USD | BEAR | 0.07005 $ | False | -35.41% | -16.24% | BEAR | -18.19% | -9.81% |
| SOL-USD | BEAR | 74,00 $ | False | -12.15% | -16.66% | BEAR | -18.19% | -9.81% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 6.74% | 21.70% | 50.98% | -3.36% | -26.20% | 17.12% | 40.79% | 65.47% | 65.00% | 10.48% | 43.65% | 82.89% |
| BTC-USD | SAME_BTC_REGIME | 12 | 83.33% | 8.07% | 15.48% | 18.97% | -3.11% | -11.86% | 12.20% | 20.27% | 24.70% | 41.67% | -0.45% | 3.16% | 8.95% |
| BTC-USD | SAME_ASSET_REGIME | 24 | 79.17% | 8.07% | 23.33% | 49.80% | -2.24% | -13.70% | 15.12% | 40.79% | 58.70% | 66.67% | 12.93% | 47.92% | 97.85% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 90.00% | 8.07% | 13.98% | 17.53% | -1.28% | -9.17% | 12.20% | 19.12% | 24.03% | 40.00% | -0.45% | 2.14% | 5.01% |
| DOGE-USD | ALL_MATCHES | 40 | 62.50% | 6.96% | 18.27% | 29.01% | -10.32% | -28.99% | 14.35% | 24.45% | 39.53% | 75.00% | 12.30% | 18.72% | 83.34% |
| DOGE-USD | SAME_BTC_REGIME | 24 | 79.17% | 10.78% | 18.27% | 29.86% | -9.41% | -15.68% | 15.08% | 24.96% | 42.23% | 87.50% | 12.92% | 16.43% | 31.72% |
| DOGE-USD | SAME_ASSET_REGIME | 26 | 76.92% | 10.26% | 17.63% | 27.75% | -9.59% | -15.74% | 14.35% | 22.25% | 36.21% | 84.62% | 14.66% | 32.62% | 86.88% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 80.00% | 10.26% | 15.96% | 20.04% | -9.59% | -14.77% | 13.87% | 18.34% | 33.92% | 85.00% | 13.80% | 17.31% | 46.04% |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 6.12% | 20.87% | 42.46% | -6.91% | -21.51% | 11.63% | 26.44% | 60.68% | 57.50% | 2.57% | 31.20% | 78.57% |
| SOL-USD | SAME_BTC_REGIME | 24 | 83.33% | 8.07% | 18.01% | 33.02% | -3.46% | -11.68% | 12.87% | 23.87% | 36.44% | 58.33% | 1.82% | 8.50% | 64.18% |
| SOL-USD | SAME_ASSET_REGIME | 31 | 70.97% | 6.34% | 18.69% | 41.91% | -4.18% | -21.16% | 11.78% | 24.40% | 60.53% | 61.29% | 4.52% | 35.62% | 77.34% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 89.47% | 6.75% | 15.82% | 28.35% | -2.75% | -10.89% | 12.72% | 22.79% | 37.44% | 57.89% | 1.20% | 6.93% | 76.77% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 12 | 83.33% | 8.07% | -3.11% | 20.27% | 41.67% | -0.45% | 22.87% |
| BTC-USD | HISTORICAL_BTC_BULL | 17 | 82.35% | 19.20% | -2.44% | 60.53% | 70.59% | 25.43% | 64.13% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -2.54% | -2.54% | 68.05% | 100.00% | 98.26% | 134.71% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 50.00% | 2.39% | -12.84% | 19.10% | 75.00% | 17.45% | 51.47% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 24 | 79.17% | 10.78% | -9.41% | 24.96% | 87.50% | 12.92% | 62.41% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 50.00% | -2.55% | -9.26% | 29.83% | 62.50% | 8.43% | 52.42% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.74% | -20.84% | 2.91% | 100.00% | 14.25% | 20.66% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 7 | 28.57% | -11.30% | -21.22% | 16.16% | 42.86% | -6.60% | 70.88% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 83.33% | 8.07% | -3.46% | 23.87% | 58.33% | 1.82% | 36.36% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 57.14% | 23.40% | -2.44% | 49.87% | 57.14% | 23.57% | 75.12% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -6.44% | -13.55% | 8.68% | 100.00% | 41.35% | 87.69% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 62.06% | -7.74% | 62.06% | 100.00% | 221.46% | 221.46% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 7 | 14.29% | -14.15% | -24.73% | 4.66% | 42.86% | -10.89% | 69.39% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 24 | 79.17% | 8.07% | -2.24% | 40.79% | 66.67% | 12.93% | 65.82% |
| BTC-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 3.83% | -11.66% | 31.54% | 50.00% | -11.69% | 41.96% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 49.35% | 0.00% | 64.13% | 100.00% | 46.87% | 64.13% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 110.91% | 0.00% | 118.05% | 100.00% | 42.57% | 118.05% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 1.27% | -8.05% | 29.83% | 66.67% | 10.19% | 37.66% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 26 | 76.92% | 10.26% | -9.59% | 22.25% | 84.62% | 14.66% | 68.77% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 40.00% | -10.84% | -21.32% | 33.07% | 80.00% | 9.96% | 75.34% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.83% | -24.71% | 17.21% | 100.00% | 7.76% | 37.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 8 | 37.50% | -9.28% | -17.31% | 31.58% | 37.50% | -7.52% | 33.39% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 70.97% | 6.34% | -4.18% | 24.40% | 61.29% | 4.52% | 70.15% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -36.80% | -40.77% | 1.46% | 0.00% | -46.57% | 1.46% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 8.73% | -8.02% | 23.46% | 50.00% | 11.01% | 35.68% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 33.93% | 0.00% | 36.50% | 100.00% | 9.42% | 36.50% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -0.90% | -11.38% | 14.95% | 40.00% | -7.25% | 16.31% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-14 | 88.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.85% | -7.06% | 41.18% | -33.30% | -41.12% | 41.18% |
| BTC-USD | ONE-USD | 2020-01-27 | 88.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| BTC-USD | ETH-USD | 2025-12-21 | 87.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.36% | 0.00% | 19.65% | -0.57% | -0.79% | 19.65% |
| BTC-USD | XTZ-USD | 2025-12-26 | 86.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| BTC-USD | BNB-USD | 2025-12-26 | 86.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| BTC-USD | BTC-USD | 2025-12-25 | 86.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 17.34% | 0.00% | 17.52% | -0.34% | -0.34% | 22.72% |
| BTC-USD | XRP-USD | 2025-12-21 | 86.11% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | -0.53% | 11.68% | 0.43% | -1.24% | 12.21% |
| BTC-USD | LTC-USD | 2020-01-26 | 85.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.63% | -12.16% | 1.37% | -13.20% | -13.20% | 1.37% |
| BTC-USD | QTUM-USD | 2020-01-27 | 85.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.22% | -8.83% | 22.12% | 9.44% | -8.83% | 22.12% |
| BTC-USD | SOL-USD | 2025-12-24 | 85.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| DOGE-USD | DASH-USD | 2022-03-12 | 89.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.34% | -9.62% | 18.11% | 13.82% | -9.62% | 28.65% |
| DOGE-USD | OP-USD | 2025-12-27 | 89.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.75% | -2.92% | 22.25% | 1.62% | -2.92% | 56.55% |
| DOGE-USD | XTZ-USD | 2025-12-26 | 89.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| DOGE-USD | THETA-USD | 2022-03-16 | 89.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.32% | -16.14% | 13.49% | -6.06% | -16.14% | 28.27% |
| DOGE-USD | LTC-USD | 2018-04-11 | 89.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -33.91% | -37.12% | 3.02% | -39.38% | -40.40% | 3.02% |
| DOGE-USD | VET-USD | 2022-03-14 | 89.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.68% | -8.95% | 11.10% | 9.39% | -8.95% | 41.71% |
| DOGE-USD | ENJ-USD | 2022-03-17 | 88.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.44% | -14.62% | 14.24% | 4.04% | -14.62% | 29.60% |
| DOGE-USD | OMG-USD | 2022-03-12 | 88.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.56% | -9.26% | 12.35% | 16.89% | -9.26% | 32.62% |
| DOGE-USD | BAT-USD | 2022-03-12 | 88.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 26.67% | 0.00% | 33.34% | 15.73% | 0.00% | 37.73% |
| DOGE-USD | NEO-USD | 2022-03-12 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.70% | -11.00% | 15.70% | 15.06% | -11.00% | 32.52% |
| SOL-USD | RUNE-USD | 2025-12-27 | 80.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.91% | -0.37% | 41.91% | -5.22% | -5.22% | 62.96% |
| SOL-USD | NEAR-USD | 2025-12-21 | 79.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.29% | 0.00% | 23.51% | 104.94% | 0.00% | 139.37% |
| SOL-USD | BNB-USD | 2025-12-26 | 79.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| SOL-USD | KAVA-USD | 2025-12-26 | 79.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.96% | -2.75% | 24.96% | 1.20% | -2.75% | 31.13% |
| SOL-USD | SOL-USD | 2025-12-24 | 78.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| SOL-USD | XRP-USD | 2020-01-27 | 77.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.30% | -10.39% | 1.55% | -17.78% | -18.75% | 1.55% |
| SOL-USD | BNB-USD | 2020-01-27 | 77.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.82% | -10.77% | 5.88% | -8.08% | -10.77% | 5.88% |
| SOL-USD | BTC-USD | 2025-12-25 | 76.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 17.34% | 0.00% | 17.52% | -0.34% | -0.34% | 22.72% |
| SOL-USD | LINK-USD | 2025-12-21 | 76.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.89% | 0.00% | 11.78% | 4.70% | 0.00% | 24.41% |
| SOL-USD | EOS-USD | 2018-10-19 | 76.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.40% | -7.62% | 75.20% | 77.34% | -7.62% | 77.34% |

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

