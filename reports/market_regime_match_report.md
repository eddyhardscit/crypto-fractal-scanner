# Market Regime Match Report

Generated: 2026-08-11 05:21 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.976 $ | False | -19.40% | -10.12% | BEAR | -19.40% | -10.12% |
| DOGE-USD | BEAR | 0.07000 $ | False | -38.04% | -16.72% | BEAR | -19.40% | -10.12% |
| SOL-USD | BEAR | 75,98 $ | False | -16.83% | -17.06% | BEAR | -19.40% | -10.12% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 9.15% | 16.51% | 35.05% | -3.04% | -21.62% | 15.87% | 35.60% | 57.28% | 57.50% | 13.11% | 56.37% | 102.63% |
| BTC-USD | SAME_BTC_REGIME | 17 | 88.24% | 9.08% | 10.41% | 21.20% | -4.42% | -14.77% | 12.45% | 15.90% | 26.01% | 41.18% | -13.16% | 24.79% | 86.54% |
| BTC-USD | SAME_ASSET_REGIME | 21 | 85.71% | 9.08% | 15.64% | 27.93% | -4.42% | -17.83% | 14.99% | 28.52% | 39.85% | 47.62% | -13.16% | 45.05% | 76.63% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 87.50% | 9.03% | 11.71% | 21.72% | -5.03% | -15.28% | 12.73% | 16.77% | 27.54% | 43.75% | -14.35% | 29.85% | 89.02% |
| DOGE-USD | ALL_MATCHES | 40 | 72.50% | 15.50% | 36.15% | 47.55% | -8.48% | -31.93% | 22.24% | 43.08% | 64.24% | 52.50% | 1.97% | 16.02% | 82.47% |
| DOGE-USD | SAME_BTC_REGIME | 21 | 90.48% | 23.14% | 41.46% | 53.58% | -8.37% | -16.39% | 23.68% | 44.13% | 64.24% | 57.14% | 3.08% | 8.64% | 28.58% |
| DOGE-USD | SAME_ASSET_REGIME | 17 | 88.24% | 22.63% | 31.89% | 57.85% | -7.10% | -21.57% | 23.41% | 31.89% | 72.64% | 52.94% | 0.86% | 8.64% | 49.34% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 87.50% | 21.42% | 28.53% | 47.78% | -7.73% | -22.86% | 22.75% | 28.53% | 57.03% | 50.00% | 0.11% | 5.93% | 19.21% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 11.48% | 21.00% | 58.48% | -4.56% | -17.94% | 17.23% | 29.84% | 70.85% | 55.00% | 4.29% | 59.90% | 104.15% |
| SOL-USD | SAME_BTC_REGIME | 14 | 100.00% | 18.33% | 27.08% | 49.62% | -2.58% | -14.51% | 28.38% | 45.29% | 65.14% | 57.14% | 37.49% | 67.31% | 137.43% |
| SOL-USD | SAME_ASSET_REGIME | 14 | 85.71% | 15.36% | 20.83% | 29.51% | -2.58% | -22.05% | 24.18% | 30.07% | 52.22% | 50.00% | 25.73% | 81.58% | 138.73% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 100.00% | 16.07% | 24.96% | 29.72% | -2.05% | -7.89% | 29.47% | 40.25% | 53.03% | 54.55% | 55.80% | 74.90% | 158.51% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 17 | 88.24% | 9.08% | -4.42% | 15.90% | 41.18% | -13.16% | 35.16% |
| BTC-USD | HISTORICAL_BTC_BULL | 11 | 72.73% | 14.00% | -1.22% | 58.04% | 72.73% | 55.25% | 141.90% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 11.10% | 0.00% | 34.10% | 100.00% | 19.41% | 38.76% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 9 | 66.67% | 5.22% | -4.58% | 27.16% | 55.56% | 2.26% | 64.01% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 21 | 90.48% | 23.14% | -8.37% | 44.13% | 57.14% | 3.08% | 62.44% |
| DOGE-USD | HISTORICAL_BTC_BULL | 15 | 53.33% | 8.30% | -9.41% | 49.61% | 46.67% | -14.77% | 81.07% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 11.10% | 0.00% | 36.94% | 100.00% | 19.41% | 36.94% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -21.24% | -21.24% | 7.30% | 33.33% | -7.71% | 89.52% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 100.00% | 18.33% | -2.58% | 45.29% | 57.14% | 37.49% | 104.25% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -2.70% | -13.16% | 10.45% | 33.33% | -6.36% | 16.92% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 15.09% | 0.00% | 23.49% | 100.00% | 92.57% | 95.28% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 104.48% | -3.96% | 120.09% | 100.00% | 307.28% | 352.55% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 15 | 60.00% | 0.71% | -4.54% | 18.59% | 60.00% | 6.32% | 54.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 21 | 85.71% | 9.08% | -4.42% | 28.52% | 47.62% | -13.16% | 45.05% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 85.71% | 11.20% | -0.49% | 58.04% | 85.71% | 74.76% | 198.54% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 10.41% | 0.00% | 66.00% | 66.67% | 8.80% | 68.47% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 55.56% | 2.92% | -4.58% | 24.82% | 55.56% | 2.26% | 64.01% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 17 | 88.24% | 22.63% | -7.10% | 31.89% | 52.94% | 0.86% | 64.24% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 9.70% | -5.90% | 46.27% | 75.00% | 16.61% | 96.16% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 36.77% | -11.51% | 42.76% | 100.00% | 9.69% | 61.11% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 3 | 100.00% | 16.41% | -9.41% | 42.38% | 33.33% | -31.97% | 42.38% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -1.50% | -12.62% | 20.06% | 30.00% | -17.60% | 64.60% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 14 | 85.71% | 15.36% | -2.58% | 30.07% | 50.00% | 25.73% | 104.25% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 10.75% | -9.90% | 39.35% | 75.00% | 58.65% | 169.92% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 10.45% | 0.00% | 63.57% | 33.33% | -0.73% | 66.80% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -4.97% | -6.37% | 5.09% | 0.00% | -3.20% | 5.09% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 17 | 64.71% | 2.92% | -4.58% | 24.82% | 64.71% | 6.32% | 47.21% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2026-01-05 | 88.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.98% | 0.00% | 8.98% | -15.55% | -19.71% | 8.98% |
| BTC-USD | BTC-USD | 2018-10-19 | 88.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -5.63% | 14.99% | 13.45% | -5.63% | 14.99% |
| BTC-USD | ETH-USD | 2025-12-31 | 87.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.28% | 0.00% | 10.59% | -22.79% | -28.34% | 10.59% |
| BTC-USD | SOL-USD | 2026-01-03 | 87.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| BTC-USD | 1INCH-USD | 2024-07-06 | 86.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 19.12% | -11.35% | 19.92% | 101.40% | -11.35% | 137.19% |
| BTC-USD | NEO-USD | 2018-10-19 | 86.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.31% | -8.94% | 35.16% | 24.79% | -8.94% | 35.16% |
| BTC-USD | XTZ-USD | 2026-01-05 | 86.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.21% | 0.00% | 15.85% | -31.20% | -34.31% | 15.85% |
| BTC-USD | 1INCH-USD | 2026-01-02 | 86.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.40% | -2.51% | 11.14% | -26.00% | -27.22% | 11.14% |
| BTC-USD | OMG-USD | 2018-10-19 | 85.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.73% | -17.83% | 7.53% | 45.05% | -17.83% | 45.05% |
| BTC-USD | ETC-USD | 2018-10-19 | 85.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.17% | -12.72% | 12.45% | 12.77% | -12.72% | 13.63% |
| DOGE-USD | VET-USD | 2022-03-24 | 90.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.63% | -3.05% | 23.68% | 9.84% | -3.05% | 50.90% |
| DOGE-USD | OP-USD | 2026-01-01 | 90.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.98% | -7.10% | 49.82% | -15.88% | -18.56% | 49.82% |
| DOGE-USD | ADA-USD | 2022-03-22 | 89.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.42% | -10.22% | 12.42% | -7.62% | -10.22% | 22.52% |
| DOGE-USD | DASH-USD | 2022-03-22 | 89.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.27% | -10.11% | 17.74% | -0.65% | -10.11% | 27.95% |
| DOGE-USD | BAT-USD | 2018-10-19 | 88.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.64% | -16.39% | 17.64% | 80.49% | -16.39% | 80.49% |
| DOGE-USD | NEO-USD | 2022-03-22 | 88.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 31.89% | -6.02% | 31.89% | 3.42% | -6.02% | 39.93% |
| DOGE-USD | LTC-USD | 2018-04-22 | 88.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.45% | -34.83% | 0.00% | -25.29% | -37.65% | 0.00% |
| DOGE-USD | XTZ-USD | 2026-01-05 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.21% | 0.00% | 15.85% | -31.20% | -34.31% | 15.85% |
| DOGE-USD | INJ-USD | 2022-03-24 | 87.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 20.22% | -1.35% | 21.97% | 28.58% | -1.35% | 76.25% |
| DOGE-USD | QTUM-USD | 2022-07-25 | 87.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -21.47% | -29.34% | 7.38% | -34.87% | -34.93% | 7.38% |
| SOL-USD | ENJ-USD | 2018-10-19 | 82.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 130.26% | -26.20% | 130.26% | 394.56% | -26.20% | 533.03% |
| SOL-USD | EOS-USD | 2018-11-03 | 81.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 29.01% | -3.10% | 50.33% | 88.25% | -3.10% | 105.67% |
| SOL-USD | RUNE-USD | 2026-01-06 | 80.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.91% | 0.00% | 53.03% | -4.33% | -22.03% | 53.03% |
| SOL-USD | SOL-USD | 2026-01-03 | 79.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| SOL-USD | NEAR-USD | 2025-12-31 | 79.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.61% | -7.58% | 16.66% | 55.80% | -7.58% | 106.31% |
| SOL-USD | QTUM-USD | 2018-10-24 | 78.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 13.12% | -5.39% | 29.47% | 61.55% | -5.39% | 61.55% |
| SOL-USD | XTZ-USD | 2025-03-11 | 78.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 29.72% | -7.89% | 29.72% | 59.35% | -7.89% | 99.97% |
| SOL-USD | XTZ-USD | 2018-10-29 | 77.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 12.52% | -2.05% | 24.86% | 158.51% | -2.05% | 185.30% |
| SOL-USD | KAVA-USD | 2026-01-05 | 77.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.58% | 0.00% | 30.18% | -12.71% | -19.16% | 30.18% |
| SOL-USD | BTC-USD | 2026-01-05 | 76.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.26% | -0.44% | 10.73% | -13.16% | -17.95% | 10.73% |

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

