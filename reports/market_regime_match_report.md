# Market Regime Match Report

Generated: 2026-08-23 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | DISTRIBUTION | 76.328 $ | True | -1.41% | -9.61% | DISTRIBUTION | -1.41% | -9.61% |
| DOGE-USD | DISTRIBUTION | 0.09067 $ | True | -11.53% | -16.09% | DISTRIBUTION | -1.41% | -9.61% |
| SOL-USD | MIXED | 93,19 $ | True | 9.28% | -15.87% | DISTRIBUTION | -1.41% | -9.61% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 5.87% | 17.13% | 41.32% | -6.99% | -16.59% | 16.69% | 28.52% | 51.71% | 67.50% | 21.90% | 43.67% | 92.30% |
| BTC-USD | SAME_BTC_REGIME | 3 | 100.00% | 14.34% | 14.35% | 14.36% | 0.00% | -3.49% | 16.50% | 20.24% | 22.49% | 100.00% | 30.12% | 41.27% | 47.96% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 3.09% | 3.09% | 3.09% | -3.35% | -3.35% | 6.53% | 6.53% | 6.53% | 0.00% | -9.24% | -9.24% | -9.24% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 60.00% | 3.14% | 13.41% | 49.28% | -7.37% | -31.30% | 20.62% | 39.85% | 65.46% | 37.50% | -10.92% | 23.29% | 99.49% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 100.00% | 48.82% | 48.82% | 48.82% | 0.00% | 0.00% | 78.14% | 78.14% | 78.14% | 100.00% | 131.14% | 131.14% | 131.14% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -2.19% | 17.71% | 44.10% | -9.28% | -15.81% | 11.30% | 26.34% | 51.71% | 77.50% | 23.92% | 43.52% | 115.99% |
| SOL-USD | SAME_BTC_REGIME | 3 | 100.00% | 17.49% | 18.19% | 18.61% | 0.00% | -10.65% | 18.89% | 21.44% | 22.97% | 66.67% | 52.42% | 66.94% | 75.64% |
| SOL-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 13 | 53.85% | 0.55% | -4.66% | 30.32% | 46.15% | -9.24% | 70.08% |
| BTC-USD | HISTORICAL_BTC_BULL | 18 | 83.33% | 11.38% | -6.87% | 32.37% | 77.78% | 21.90% | 83.31% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 14.34% | 0.00% | 20.24% | 100.00% | 30.12% | 49.06% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 0.00% | -8.07% | -12.41% | 20.57% | 66.67% | 26.44% | 53.87% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 5 | 60.00% | 3.57% | -4.25% | 37.84% | 0.00% | -16.66% | 37.84% |
| DOGE-USD | HISTORICAL_BTC_BULL | 29 | 65.52% | 3.56% | -6.90% | 39.84% | 48.28% | -7.48% | 68.26% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 48.82% | 0.00% | 78.14% | 100.00% | 131.14% | 140.49% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -16.40% | -16.40% | 34.11% | 0.00% | -22.01% | 34.11% |
| SOL-USD | HISTORICAL_BTC_BEAR | 7 | 57.14% | 28.81% | -5.21% | 58.36% | 57.14% | 28.92% | 105.40% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 80.00% | 8.66% | -8.00% | 27.78% | 60.00% | 23.60% | 150.62% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 17.49% | 0.00% | 21.44% | 66.67% | 52.42% | 77.63% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 20 | 15.00% | -7.13% | -13.14% | 13.50% | 95.00% | 21.98% | 51.28% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 22 | 68.18% | 6.31% | -3.85% | 27.67% | 68.18% | 18.10% | 69.30% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 77.78% | 11.17% | -4.50% | 36.50% | 55.56% | 5.03% | 123.95% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.09% | -3.35% | 6.53% | 0.00% | -9.24% | 12.81% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 25.00% | -6.28% | -11.86% | 17.52% | 87.50% | 26.44% | 58.76% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 10 | 50.00% | -0.08% | -5.41% | 36.91% | 20.00% | -15.52% | 39.38% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 25 | 68.00% | 3.56% | -6.90% | 41.89% | 48.00% | -7.48% | 68.26% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -29.26% | -31.16% | 20.59% | 20.00% | -32.36% | 35.71% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 13 | 61.54% | 4.51% | -8.51% | 30.32% | 53.85% | 13.70% | 100.07% |
| SOL-USD | HISTORICAL_ASSET_BULL | 7 | 85.71% | 14.83% | -2.94% | 82.41% | 71.43% | 70.71% | 226.72% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 20 | 20.00% | -6.97% | -13.14% | 13.94% | 95.00% | 23.04% | 49.18% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LTC-USD | 2023-07-27 | 83.57% | DISTRIBUTION | BULL | SAME_BTC_ONLY | MIXED | 3.98% | -4.37% | 8.18% | 5.03% | -4.37% | 12.82% |
| BTC-USD | 1INCH-USD | 2023-07-27 | 78.15% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 14.34% | 0.00% | 23.99% | 52.42% | 0.00% | 57.23% |
| BTC-USD | ZIL-USD | 2023-07-27 | 77.56% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | BULLISH_30D | 14.36% | 0.00% | 16.50% | 30.12% | 0.00% | 40.90% |
| BTC-USD | BNB-USD | 2026-01-15 | 78.03% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |
| BTC-USD | XLM-USD | 2020-08-14 | 85.62% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | XRP-USD | 2023-07-30 | 84.87% | BULL | BULL | DIFFERENT | BEARISH_30D | -10.51% | -18.88% | 0.00% | -19.43% | -19.43% | 0.00% |
| BTC-USD | MKR-USD | 2020-02-22 | 83.76% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| BTC-USD | ETC-USD | 2020-08-14 | 82.76% | BULL | RECOVERY | DIFFERENT | MIXED | -6.61% | -12.09% | 10.56% | 20.57% | -22.64% | 35.47% |
| BTC-USD | BNB-USD | 2018-11-03 | 82.45% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| BTC-USD | XRP-USD | 2026-01-15 | 82.12% | BEAR | BEAR | DIFFERENT | MIXED | -5.83% | -6.97% | 3.52% | -22.62% | -23.73% | 3.52% |
| DOGE-USD | EGLD-USD | 2023-07-15 | 82.34% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 48.82% | 0.00% | 78.14% | 131.14% | 0.00% | 140.49% |
| DOGE-USD | MANA-USD | 2025-01-15 | 87.90% | BULL | BULL | DIFFERENT | MIXED | -4.31% | -10.11% | 18.69% | -19.03% | -26.84% | 18.69% |
| DOGE-USD | SAND-USD | 2025-01-14 | 87.54% | BULL | BULL | DIFFERENT | MIXED | 3.56% | -8.98% | 23.97% | -21.92% | -21.92% | 23.97% |
| DOGE-USD | DOGE-USD | 2025-01-15 | 87.08% | BULL | BULL | DIFFERENT | BULLISH_30D | 23.48% | -6.52% | 36.30% | -9.92% | -17.06% | 36.30% |
| DOGE-USD | OP-USD | 2026-01-16 | 86.18% | BEAR | BEAR | DIFFERENT | MIXED | 3.57% | -4.25% | 37.84% | -16.66% | -27.25% | 37.84% |
| DOGE-USD | VET-USD | 2025-01-17 | 85.70% | BULL | BULL | DIFFERENT | MIXED | 1.03% | -8.45% | 18.77% | -22.61% | -29.05% | 18.77% |
| DOGE-USD | AVAX-USD | 2025-01-16 | 85.29% | BULL | BULL | DIFFERENT | MIXED | 5.65% | -11.98% | 16.68% | -17.86% | -25.64% | 16.68% |
| DOGE-USD | HBAR-USD | 2020-08-16 | 85.27% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | -12.50% | -12.50% | 13.17% | 177.04% | -12.50% | 191.62% |
| DOGE-USD | FIL-USD | 2022-04-25 | 85.16% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -29.26% | -31.16% | 16.04% | -32.36% | -35.61% | 16.04% |
| DOGE-USD | AVAX-USD | 2025-09-28 | 84.87% | BULL | RECOVERY | DIFFERENT | BEARISH_30D | -32.83% | -32.83% | 1.94% | -37.57% | -42.62% | 1.94% |
| SOL-USD | VET-USD | 2023-07-27 | 71.23% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 17.49% | 0.00% | 18.85% | 81.45% | 0.00% | 98.04% |
| SOL-USD | CRV-USD | 2023-08-03 | 69.44% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.89% | -13.32% | 18.89% | -13.86% | -14.48% | 18.89% |
| SOL-USD | 1INCH-USD | 2023-07-27 | 68.15% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 14.34% | 0.00% | 23.99% | 52.42% | 0.00% | 57.23% |
| SOL-USD | VET-USD | 2020-02-23 | 80.57% | RECOVERY | RECOVERY | DIFFERENT | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | ZIL-USD | 2020-08-16 | 79.67% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 135.96% | 0.00% | 135.96% | 177.93% | 0.00% | 267.71% |
| SOL-USD | EOS-USD | 2018-11-13 | 78.48% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -6.92% | -16.43% | 8.85% | 33.78% | -16.43% | 48.92% |
| SOL-USD | BNB-USD | 2018-11-03 | 78.23% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| SOL-USD | MKR-USD | 2020-02-22 | 76.86% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| SOL-USD | ZEC-USD | 2020-02-21 | 76.64% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -4.23% | -9.12% | 6.45% | 32.15% | -9.12% | 32.15% |
| SOL-USD | BNB-USD | 2020-02-21 | 75.54% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -12.61% | -14.42% | 0.97% | 12.13% | -14.42% | 13.70% |

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

