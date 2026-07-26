# Market Regime Match Report

Generated: 2026-07-26 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.460 $ | False | -16.69% | -9.82% | BEAR | -16.69% | -9.82% |
| DOGE-USD | BEAR | 0.07349 $ | False | -25.80% | -16.04% | BEAR | -16.69% | -9.82% |
| SOL-USD | BEAR | 75,08 $ | False | -11.47% | -16.65% | BEAR | -16.69% | -9.82% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 65.00% | 9.80% | 24.97% | 44.15% | -7.97% | -27.11% | 15.09% | 29.11% | 54.47% | 57.50% | 11.28% | 41.82% | 62.36% |
| BTC-USD | SAME_BTC_REGIME | 10 | 70.00% | 4.13% | 29.42% | 36.93% | -7.97% | -22.42% | 9.70% | 39.68% | 61.89% | 70.00% | 8.61% | 11.85% | 66.66% |
| BTC-USD | SAME_ASSET_REGIME | 19 | 78.95% | 22.59% | 34.64% | 45.89% | -6.41% | -19.08% | 22.59% | 43.10% | 55.04% | 78.95% | 29.73% | 53.27% | 62.75% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 70.00% | 4.13% | 29.42% | 36.93% | -7.97% | -22.42% | 9.70% | 39.68% | 61.89% | 70.00% | 8.61% | 11.85% | 66.66% |
| DOGE-USD | ALL_MATCHES | 40 | 62.50% | 4.13% | 17.67% | 32.09% | -7.57% | -23.42% | 15.51% | 32.21% | 41.11% | 82.50% | 26.27% | 40.81% | 60.86% |
| DOGE-USD | SAME_BTC_REGIME | 30 | 70.00% | 5.62% | 18.58% | 32.68% | -6.25% | -18.80% | 17.65% | 32.58% | 41.11% | 90.00% | 30.87% | 44.72% | 61.29% |
| DOGE-USD | SAME_ASSET_REGIME | 29 | 65.52% | 4.43% | 19.04% | 32.69% | -6.22% | -17.20% | 19.77% | 32.02% | 39.94% | 89.66% | 31.22% | 45.34% | 62.49% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 28 | 67.86% | 5.62% | 21.21% | 32.70% | -6.21% | -17.38% | 17.65% | 32.21% | 40.11% | 89.29% | 31.80% | 46.27% | 63.70% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 5.22% | 19.20% | 37.74% | -8.27% | -17.86% | 11.78% | 24.54% | 44.69% | 62.50% | 2.91% | 25.71% | 62.83% |
| SOL-USD | SAME_BTC_REGIME | 20 | 75.00% | 7.59% | 19.37% | 36.45% | -8.16% | -19.88% | 16.76% | 24.19% | 48.78% | 75.00% | 2.91% | 32.98% | 89.20% |
| SOL-USD | SAME_ASSET_REGIME | 26 | 69.23% | 6.36% | 20.22% | 40.73% | -8.15% | -18.41% | 13.19% | 25.65% | 55.54% | 69.23% | 2.91% | 47.82% | 63.43% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 73.68% | 5.72% | 17.35% | 29.18% | -7.96% | -20.66% | 14.26% | 21.55% | 35.45% | 73.68% | 2.51% | 21.35% | 63.03% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 10 | 70.00% | 4.13% | -7.97% | 39.68% | 70.00% | 8.61% | 41.90% |
| BTC-USD | HISTORICAL_BTC_BULL | 22 | 68.18% | 17.23% | -6.36% | 31.48% | 63.64% | 29.58% | 54.07% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 42.86% | -2.53% | -15.01% | 11.78% | 14.29% | -15.27% | 14.08% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 70.00% | 5.62% | -6.25% | 32.58% | 90.00% | 30.87% | 60.29% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 75.00% | 14.60% | -6.40% | 39.98% | 75.00% | 24.76% | 51.22% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -20.98% | -23.66% | 13.78% | 50.00% | 7.58% | 33.57% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 75.00% | 7.59% | -8.16% | 24.19% | 75.00% | 2.91% | 59.46% |
| SOL-USD | HISTORICAL_BTC_BULL | 6 | 83.33% | 20.86% | -1.03% | 42.59% | 83.33% | 35.62% | 64.07% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -5.89% | -15.62% | 6.07% | 100.00% | 26.02% | 83.19% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 61.54% | 4.16% | -8.83% | 11.45% | 30.77% | -8.97% | 18.99% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 19 | 78.95% | 22.59% | -6.41% | 43.10% | 78.95% | 29.73% | 56.83% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 54.55% | 10.75% | -8.82% | 25.63% | 45.45% | -1.00% | 37.28% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.22% | -5.61% | 18.22% | 100.00% | 29.43% | 32.77% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 3.45% | -21.88% | 41.66% | 50.00% | 2.47% | 82.23% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 42.86% | -2.53% | -15.01% | 11.78% | 14.29% | -15.27% | 14.08% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 4.43% | -6.22% | 32.02% | 89.66% | 31.22% | 60.33% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 8.87% | -17.54% | 34.30% | 100.00% | 24.07% | 49.59% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -17.99% | -19.88% | 13.78% | 33.33% | -14.29% | 30.13% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 26 | 69.23% | 6.36% | -8.15% | 25.65% | 69.23% | 2.91% | 64.07% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -37.82% | -38.96% | 1.00% | 0.00% | -50.22% | 1.00% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 19.99% | -1.20% | 24.50% | 100.00% | 42.40% | 47.99% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -12.42% | -12.78% | 2.93% | 0.00% | -11.30% | 2.93% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 11 | 81.82% | 4.72% | -8.22% | 23.29% | 54.55% | 3.89% | 23.29% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 91.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | XRP-USD | 2019-10-09 | 90.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | BTC-USD | 2018-10-03 | 87.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.21% | -7.60% | 1.35% | 6.15% | -7.60% | 12.60% |
| BTC-USD | OMG-USD | 2018-10-04 | 86.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.64% | -21.63% | 0.39% | 11.07% | -21.63% | 11.07% |
| BTC-USD | ETH-USD | 2025-12-16 | 86.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -8.55% | 11.67% | -3.23% | -8.55% | 11.67% |
| BTC-USD | BNB-USD | 2018-10-04 | 86.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | BNB-USD | 2025-12-21 | 85.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| BTC-USD | BTC-USD | 2025-12-20 | 85.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.76% | 0.00% | 19.26% | 11.50% | 0.00% | 24.54% |
| BTC-USD | APT-USD | 2024-09-16 | 85.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.47% | -29.47% | 7.73% | -30.92% | -30.92% | 7.73% |
| BTC-USD | NEO-USD | 2018-10-04 | 85.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.18% | -13.66% | 1.68% | 11.97% | -13.66% | 28.15% |
| DOGE-USD | DASH-USD | 2022-03-07 | 90.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | MKR-USD | 2022-09-24 | 89.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.72% | -1.56% | 39.59% | 72.17% | -1.56% | 80.88% |
| DOGE-USD | THETA-USD | 2022-03-11 | 88.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.61% | -6.22% | 26.91% | 19.72% | -6.22% | 43.44% |
| DOGE-USD | OMG-USD | 2022-03-07 | 88.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.54% | -14.76% | 5.54% | 24.58% | -14.76% | 24.58% |
| DOGE-USD | VET-USD | 2022-03-09 | 88.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.43% | -5.37% | 15.47% | 38.55% | -5.37% | 47.28% |
| DOGE-USD | INJ-USD | 2022-03-09 | 88.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.67% | -13.24% | 7.61% | 32.39% | -13.24% | 54.99% |
| DOGE-USD | OP-USD | 2025-12-22 | 88.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | ENJ-USD | 2022-03-12 | 88.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.33% | 0.00% | 41.33% | 40.13% | 0.00% | 60.33% |
| DOGE-USD | QTUM-USD | 2022-03-07 | 88.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -0.80% | -6.74% | 13.36% | 54.57% | -6.74% | 68.52% |
| DOGE-USD | RUNE-USD | 2022-03-08 | 88.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -22.98% | 22.31% | 37.54% | -22.98% | 46.15% |
| SOL-USD | ENJ-USD | 2018-10-04 | 81.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -12.02% | -26.93% | 5.36% | 445.37% | -26.93% | 526.80% |
| SOL-USD | QTUM-USD | 2018-10-04 | 80.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.14% | -19.10% | 3.33% | -0.16% | -19.10% | 10.72% |
| SOL-USD | RUNE-USD | 2025-12-22 | 79.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.64% | -8.40% | 23.46% | 3.30% | -8.40% | 52.16% |
| SOL-USD | BNB-USD | 2025-12-21 | 79.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | SOL-USD | 2025-12-19 | 79.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | NEAR-USD | 2025-12-16 | 78.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.14% | -9.23% | 12.11% | 87.14% | -9.23% | 91.97% |
| SOL-USD | KAVA-USD | 2025-12-21 | 78.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.72% | -7.96% | 14.26% | 2.51% | -7.96% | 24.10% |
| SOL-USD | ZIL-USD | 2018-10-06 | 77.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.19% | -10.59% | 26.39% | -0.95% | -11.40% | 26.39% |
| SOL-USD | LRC-USD | 2018-10-04 | 77.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| SOL-USD | LINK-USD | 2025-12-16 | 77.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.03% | -10.34% | 2.67% | 0.58% | -10.34% | 14.27% |

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

