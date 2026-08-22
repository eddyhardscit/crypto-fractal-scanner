# Market Regime Match Report

Generated: 2026-08-22 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | DISTRIBUTION | 77.239 $ | True | -0.00% | -9.79% | DISTRIBUTION | -0.00% | -9.79% |
| DOGE-USD | DISTRIBUTION | 0.09061 $ | True | -12.39% | -16.28% | DISTRIBUTION | -0.00% | -9.79% |
| SOL-USD | MIXED | 93,70 $ | True | 9.43% | -16.13% | DISTRIBUTION | -0.00% | -9.79% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 3.62% | 12.40% | 38.19% | -7.22% | -16.00% | 17.60% | 26.50% | 52.35% | 65.00% | 21.90% | 43.67% | 145.84% |
| BTC-USD | SAME_BTC_REGIME | 1 | 100.00% | 4.15% | 4.15% | 4.15% | -4.23% | -4.23% | 8.33% | 8.33% | 8.33% | 100.00% | 7.69% | 7.69% | 7.69% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 3.09% | 3.09% | 3.09% | -3.35% | -3.35% | 6.53% | 6.53% | 6.53% | 0.00% | -9.24% | -9.24% | -9.24% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 1.88% | 9.43% | 32.37% | -8.71% | -32.98% | 18.73% | 34.66% | 49.58% | 30.00% | -13.33% | 4.92% | 76.94% |
| DOGE-USD | SAME_BTC_REGIME | 2 | 50.00% | 8.21% | 28.51% | 40.70% | -18.13% | -32.63% | 39.07% | 58.60% | 70.32% | 50.00% | 52.02% | 91.58% | 115.32% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -1.14% | 15.49% | 44.10% | -9.35% | -14.59% | 11.30% | 24.78% | 51.71% | 77.50% | 23.84% | 37.75% | 115.99% |
| SOL-USD | SAME_BTC_REGIME | 3 | 100.00% | 17.49% | 18.19% | 18.61% | 0.00% | -10.65% | 18.89% | 21.44% | 22.97% | 66.67% | 52.42% | 66.94% | 75.64% |
| SOL-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 15 | 53.33% | 2.09% | -3.35% | 29.12% | 46.67% | -9.24% | 61.19% |
| BTC-USD | HISTORICAL_BTC_BULL | 17 | 82.35% | 9.47% | -10.11% | 26.02% | 82.35% | 29.10% | 123.95% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 4.15% | -4.23% | 8.33% | 100.00% | 7.69% | 12.98% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 0.00% | -9.13% | -13.19% | 23.54% | 57.14% | 23.44% | 52.57% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 6 | 66.67% | 2.85% | -8.35% | 37.02% | 16.67% | -15.44% | 39.68% |
| DOGE-USD | HISTORICAL_BTC_BULL | 29 | 55.17% | 1.95% | -8.98% | 23.89% | 34.48% | -14.42% | 36.30% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 8.21% | -18.13% | 58.60% | 50.00% | 52.02% | 105.36% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -1.77% | -6.57% | 53.51% | 0.00% | -8.94% | 53.51% |
| SOL-USD | HISTORICAL_BTC_BEAR | 8 | 50.00% | 0.06% | -6.59% | 53.91% | 37.50% | -17.40% | 69.74% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 85.71% | 14.83% | -2.94% | 82.41% | 71.43% | 30.01% | 226.72% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 17.49% | 0.00% | 21.44% | 66.67% | 52.42% | 77.63% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 22 | 22.73% | -6.97% | -10.79% | 13.11% | 95.45% | 23.84% | 50.34% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 55.00% | 3.13% | -5.06% | 24.71% | 55.00% | 7.77% | 55.96% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 81.82% | 9.47% | -4.77% | 31.26% | 72.73% | 29.10% | 157.79% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.09% | -3.35% | 6.53% | 0.00% | -9.24% | 12.81% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 25.00% | -6.28% | -12.64% | 20.03% | 87.50% | 30.22% | 77.13% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 10 | 50.00% | 1.06% | -5.73% | 39.68% | 30.00% | -11.66% | 60.47% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 24 | 58.33% | 1.88% | -8.14% | 24.85% | 29.17% | -13.35% | 29.87% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | -6.35% | -21.13% | 18.04% | 33.33% | -19.17% | 39.90% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 14 | 57.14% | 0.43% | -9.02% | 25.12% | 50.00% | -0.08% | 87.84% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 100.00% | 16.59% | -1.49% | 109.19% | 83.33% | 124.32% | 247.22% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 20 | 20.00% | -6.97% | -11.56% | 12.93% | 95.00% | 23.84% | 50.10% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LTC-USD | 2023-07-26 | 84.93% | DISTRIBUTION | BULL | SAME_BTC_ONLY | MIXED | 4.15% | -4.23% | 8.33% | 7.69% | -4.23% | 12.98% |
| BTC-USD | BNB-USD | 2026-01-15 | 80.59% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |
| BTC-USD | XLM-USD | 2020-08-14 | 88.54% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | MKR-USD | 2020-02-22 | 84.67% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| BTC-USD | ETC-USD | 2020-08-14 | 84.65% | BULL | RECOVERY | DIFFERENT | MIXED | -6.61% | -12.09% | 10.56% | 20.57% | -22.64% | 35.47% |
| BTC-USD | XRP-USD | 2023-07-25 | 83.61% | BULL | BULL | DIFFERENT | MIXED | 0.55% | -4.77% | 17.39% | 0.89% | -4.77% | 17.39% |
| BTC-USD | DOGE-USD | 2020-08-14 | 83.28% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 36.50% | -12.20% | 36.50% | 158.34% | -12.20% | 202.68% |
| BTC-USD | THETA-USD | 2022-04-20 | 83.14% | RECOVERY | BEAR | DIFFERENT | BEARISH_30D | -16.53% | -16.53% | 23.44% | -18.80% | -23.27% | 23.44% |
| BTC-USD | XRP-USD | 2026-01-15 | 83.05% | BEAR | BEAR | DIFFERENT | MIXED | -5.83% | -6.97% | 3.52% | -22.62% | -23.73% | 3.52% |
| BTC-USD | LTC-USD | 2018-10-30 | 82.73% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 70.34% | 0.00% | 73.65% | 180.30% | 0.00% | 181.10% |
| DOGE-USD | SNX-USD | 2025-10-12 | 84.80% | DISTRIBUTION | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -32.40% | -36.26% | 0.00% | -27.09% | -36.26% | 0.00% |
| DOGE-USD | EGLD-USD | 2023-07-15 | 83.68% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 48.82% | 0.00% | 78.14% | 131.14% | 0.00% | 140.49% |
| DOGE-USD | SAND-USD | 2025-01-14 | 88.90% | BULL | BULL | DIFFERENT | MIXED | 3.56% | -8.98% | 23.97% | -21.92% | -21.92% | 23.97% |
| DOGE-USD | DOGE-USD | 2025-01-15 | 87.86% | BULL | BULL | DIFFERENT | BULLISH_30D | 23.48% | -6.52% | 36.30% | -9.92% | -17.06% | 36.30% |
| DOGE-USD | OP-USD | 2026-01-11 | 87.41% | BEAR | BEAR | DIFFERENT | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | MANA-USD | 2025-01-15 | 86.11% | BULL | BULL | DIFFERENT | MIXED | -4.31% | -10.11% | 18.69% | -19.03% | -26.84% | 18.69% |
| DOGE-USD | HBAR-USD | 2020-08-16 | 86.01% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | -12.50% | -12.50% | 13.17% | 177.04% | -12.50% | 191.62% |
| DOGE-USD | ALGO-USD | 2025-01-14 | 85.86% | BULL | BULL | DIFFERENT | MIXED | 4.60% | -6.82% | 18.34% | -25.30% | -25.30% | 18.34% |
| DOGE-USD | KSM-USD | 2022-04-19 | 85.00% | BEAR | BEAR | DIFFERENT | BEARISH_30D | -28.63% | -28.63% | 6.88% | -34.98% | -36.50% | 6.88% |
| DOGE-USD | VET-USD | 2025-01-17 | 84.97% | BULL | BULL | DIFFERENT | MIXED | 1.03% | -8.45% | 18.77% | -22.61% | -29.05% | 18.77% |
| SOL-USD | VET-USD | 2023-07-27 | 70.65% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 17.49% | 0.00% | 18.85% | 81.45% | 0.00% | 98.04% |
| SOL-USD | 1INCH-USD | 2023-07-27 | 69.14% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 14.34% | 0.00% | 23.99% | 52.42% | 0.00% | 57.23% |
| SOL-USD | CRV-USD | 2023-08-03 | 69.09% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.89% | -13.32% | 18.89% | -13.86% | -14.48% | 18.89% |
| SOL-USD | EOS-USD | 2018-11-13 | 81.37% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -6.92% | -16.43% | 8.85% | 33.78% | -16.43% | 48.92% |
| SOL-USD | MKR-USD | 2020-02-22 | 79.23% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| SOL-USD | ZIL-USD | 2020-08-16 | 77.61% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 135.96% | 0.00% | 135.96% | 177.93% | 0.00% | 267.71% |
| SOL-USD | VET-USD | 2020-02-23 | 77.30% | RECOVERY | RECOVERY | DIFFERENT | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | BNB-USD | 2020-02-21 | 77.11% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -12.61% | -14.42% | 0.97% | 12.13% | -14.42% | 13.70% |
| SOL-USD | ZEC-USD | 2020-02-21 | 76.97% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -4.23% | -9.12% | 6.45% | 32.15% | -9.12% | 32.15% |
| SOL-USD | BNB-USD | 2018-11-03 | 76.40% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |

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

