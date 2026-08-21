# Market Regime Match Report

Generated: 2026-08-21 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | DISTRIBUTION | 75.133 $ | True | -2.04% | -9.92% | DISTRIBUTION | -2.04% | -9.92% |
| DOGE-USD | BEAR | 0.08238 $ | False | -19.92% | -16.43% | DISTRIBUTION | -2.04% | -9.92% |
| SOL-USD | MIXED | 89,55 $ | True | 4.65% | -16.34% | DISTRIBUTION | -2.04% | -9.92% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 2.70% | 13.00% | 38.19% | -7.22% | -16.59% | 17.14% | 27.70% | 51.68% | 60.00% | 17.04% | 48.22% | 145.84% |
| BTC-USD | SAME_BTC_REGIME | 1 | 100.00% | 30.61% | 30.61% | 30.61% | -14.39% | -14.39% | 37.23% | 37.23% | 37.23% | 100.00% | 66.62% | 66.62% | 66.62% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | -14.77% | -5.84% | -0.48% | -18.59% | -30.78% | 19.63% | 26.18% | 30.11% | 0.00% | -25.57% | -17.40% | -12.51% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 1.88% | 17.67% | 48.56% | -12.04% | -33.08% | 17.97% | 34.37% | 51.07% | 32.50% | -11.43% | 18.09% | 114.31% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -32.40% | -32.40% | -32.40% | -36.26% | -36.26% | 0.00% | 0.00% | 0.00% | 0.00% | -27.09% | -27.09% | -27.09% |
| DOGE-USD | SAME_ASSET_REGIME | 12 | 66.67% | 23.37% | 38.37% | 49.34% | -8.63% | -27.89% | 34.74% | 48.71% | 64.10% | 41.67% | -7.05% | 51.37% | 82.07% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 47.50% | -0.88% | 15.71% | 68.73% | -8.26% | -14.44% | 11.77% | 24.78% | 70.41% | 75.00% | 29.19% | 58.98% | 187.89% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 55.56% | 1.84% | -3.61% | 30.84% | 44.44% | -10.51% | 53.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 15 | 80.00% | 8.41% | -12.16% | 23.74% | 80.00% | 23.22% | 115.39% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 0.00% | -10.93% | -12.48% | 23.59% | 50.00% | 9.44% | 45.87% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 14 | 71.43% | 9.93% | -12.82% | 38.13% | 28.57% | -11.83% | 45.03% |
| DOGE-USD | HISTORICAL_BTC_BULL | 24 | 50.00% | -1.64% | -10.97% | 21.46% | 37.50% | -11.43% | 44.31% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -32.40% | -36.26% | 0.00% | 0.00% | -27.09% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -4.88% | 65.73% | 0.00% | -4.17% | 65.73% |
| SOL-USD | HISTORICAL_BTC_BEAR | 9 | 55.56% | 3.09% | -4.66% | 49.47% | 44.44% | -9.24% | 112.24% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 14.83% | -2.99% | 65.24% | 71.43% | 30.01% | 248.94% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 24 | 37.50% | -2.84% | -9.82% | 17.14% | 87.50% | 30.22% | 58.76% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 60.00% | 4.05% | -4.10% | 28.19% | 55.00% | 13.11% | 64.08% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 77.78% | 9.47% | -12.20% | 26.02% | 66.67% | 29.10% | 191.62% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.77% | -18.59% | 26.18% | 0.00% | -25.57% | 27.75% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 33.33% | -6.61% | -11.63% | 15.31% | 77.78% | 23.44% | 69.53% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 12 | 66.67% | 23.37% | -8.63% | 48.71% | 41.67% | -7.05% | 73.07% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 20 | 55.00% | 1.41% | -8.71% | 23.91% | 35.00% | -10.25% | 29.87% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 6.99% | -17.49% | 31.76% | 0.00% | -3.55% | 31.76% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -10.00% | -20.85% | 9.07% | 14.29% | -27.09% | 11.37% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 13 | 53.85% | 0.30% | -8.51% | 25.50% | 53.85% | 14.57% | 114.84% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 16.59% | -2.96% | 83.43% | 83.33% | 126.54% | 280.55% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.09% | -3.35% | 6.53% | 0.00% | -9.24% | 12.81% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 20 | 30.00% | -5.89% | -9.66% | 12.27% | 90.00% | 26.18% | 51.61% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | DOT-USD | 2024-07-14 | 79.24% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 30.61% | -14.39% | 37.23% | 66.62% | -14.39% | 144.58% |
| BTC-USD | BNB-USD | 2026-01-15 | 82.46% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |
| BTC-USD | MANA-USD | 2018-07-21 | 80.11% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | BEARISH_30D | -32.64% | -33.83% | 32.73% | -41.90% | -44.09% | 32.73% |
| BTC-USD | XLM-USD | 2020-08-14 | 88.96% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | XRP-USD | 2023-07-25 | 86.20% | BULL | BULL | DIFFERENT | MIXED | 0.55% | -4.77% | 17.39% | 0.89% | -4.77% | 17.39% |
| BTC-USD | LTC-USD | 2023-07-25 | 85.77% | BULL | RECOVERY | DIFFERENT | MIXED | 2.30% | -4.97% | 7.49% | 4.09% | -4.97% | 12.10% |
| BTC-USD | THETA-USD | 2022-04-20 | 85.01% | RECOVERY | BEAR | DIFFERENT | BEARISH_30D | -16.53% | -16.53% | 23.44% | -18.80% | -23.27% | 23.44% |
| BTC-USD | ETC-USD | 2020-08-14 | 84.60% | BULL | RECOVERY | DIFFERENT | MIXED | -6.61% | -12.09% | 10.56% | 20.57% | -22.64% | 35.47% |
| BTC-USD | LTC-USD | 2018-10-29 | 83.67% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 66.94% | -3.86% | 66.94% | 170.23% | -3.86% | 170.23% |
| BTC-USD | NEO-USD | 2018-10-29 | 83.50% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 30.74% | -2.98% | 44.00% | 85.04% | -2.98% | 91.46% |
| DOGE-USD | SNX-USD | 2025-10-12 | 87.71% | DISTRIBUTION | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -32.40% | -36.26% | 0.00% | -27.09% | -36.26% | 0.00% |
| DOGE-USD | OP-USD | 2026-01-11 | 89.34% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | KSM-USD | 2022-04-19 | 85.34% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.63% | -28.63% | 6.88% | -34.98% | -36.50% | 6.88% |
| DOGE-USD | OMG-USD | 2025-10-07 | 84.90% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -31.06% | -32.57% | 0.00% | -31.91% | -34.94% | 0.00% |
| DOGE-USD | SOL-USD | 2022-04-19 | 84.40% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.29% | -21.29% | 15.33% | -19.78% | -24.60% | 15.33% |
| DOGE-USD | FTM-USD | 2022-04-01 | 83.69% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 35.00% | -16.51% | 35.47% | -9.93% | -16.51% | 45.15% |
| DOGE-USD | EGLD-USD | 2023-07-10 | 83.67% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 79.03% | -3.32% | 97.30% | 150.60% | -3.32% | 166.35% |
| DOGE-USD | ATOM-USD | 2022-04-01 | 83.66% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 31.00% | -13.26% | 31.00% | 44.09% | -13.26% | 44.68% |
| DOGE-USD | VET-USD | 2022-04-03 | 83.44% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 48.46% | -2.52% | 48.46% | 16.58% | -2.52% | 51.72% |
| DOGE-USD | DOT-USD | 2023-07-25 | 83.35% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 15.73% | -2.44% | 20.65% | 73.20% | -2.44% | 95.07% |
| SOL-USD | EOS-USD | 2018-11-13 | 82.18% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -6.92% | -16.43% | 8.85% | 33.78% | -16.43% | 48.92% |
| SOL-USD | ONE-USD | 2020-02-21 | 78.94% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -22.17% | -28.41% | 0.73% | -4.55% | -28.41% | 0.73% |
| SOL-USD | BNB-USD | 2020-02-21 | 78.52% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -12.61% | -14.42% | 0.97% | 12.13% | -14.42% | 13.70% |
| SOL-USD | VET-USD | 2020-02-18 | 78.27% | RECOVERY | RECOVERY | DIFFERENT | EXPLOSIVE_60D | 82.11% | 0.00% | 98.84% | 258.30% | 0.00% | 308.84% |
| SOL-USD | ATOM-USD | 2020-02-21 | 77.96% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -5.94% | -13.19% | 11.96% | 29.45% | -13.19% | 55.17% |
| SOL-USD | ZIL-USD | 2020-08-11 | 77.78% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 101.63% | -2.99% | 101.63% | 237.58% | -2.99% | 312.16% |
| SOL-USD | EOS-USD | 2020-02-21 | 77.54% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -13.99% | -14.92% | 2.21% | 9.56% | -14.92% | 9.56% |
| SOL-USD | MKR-USD | 2020-02-22 | 77.39% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| SOL-USD | QTUM-USD | 2020-02-21 | 76.81% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -7.01% | -11.63% | 4.96% | 30.99% | -11.63% | 33.54% |
| SOL-USD | ALGO-USD | 2020-02-20 | 76.64% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -9.13% | -10.10% | 8.93% | 36.82% | -10.92% | 69.53% |

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

