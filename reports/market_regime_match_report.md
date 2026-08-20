# Market Regime Match Report

Generated: 2026-08-20 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | DISTRIBUTION | 69.565 $ | True | -7.83% | -10.07% | DISTRIBUTION | -7.83% | -10.07% |
| DOGE-USD | BEAR | 0.07459 $ | False | -27.07% | -16.58% | DISTRIBUTION | -7.83% | -10.07% |
| SOL-USD | MIXED | 84,87 $ | True | 0.69% | -16.57% | DISTRIBUTION | -7.83% | -10.07% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 2.17% | 13.97% | 38.32% | -4.49% | -14.63% | 17.74% | 33.09% | 66.23% | 55.00% | 4.26% | 55.01% | 145.86% |
| BTC-USD | SAME_BTC_REGIME | 1 | 100.00% | 30.61% | 30.61% | 30.61% | -14.39% | -14.39% | 37.23% | 37.23% | 37.23% | 100.00% | 66.62% | 66.62% | 66.62% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | -14.77% | -5.84% | -0.48% | -18.59% | -30.78% | 19.63% | 26.18% | 30.11% | 0.00% | -25.57% | -17.40% | -12.51% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 10.59% | 31.49% | 45.15% | -12.11% | -29.02% | 18.87% | 34.37% | 48.11% | 37.50% | -8.70% | 10.55% | 84.98% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -32.40% | -32.40% | -32.40% | -36.26% | -36.26% | 0.00% | 0.00% | 0.00% | 0.00% | -27.09% | -27.09% | -27.09% |
| DOGE-USD | SAME_ASSET_REGIME | 15 | 86.67% | 32.95% | 34.60% | 63.05% | -12.71% | -23.78% | 33.03% | 41.09% | 63.05% | 53.33% | 0.11% | 26.50% | 123.58% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | -0.01% | 18.77% | 83.27% | -5.57% | -13.21% | 11.99% | 27.31% | 94.20% | 72.50% | 23.95% | 44.90% | 165.12% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 21 | 61.90% | 3.09% | -2.98% | 44.00% | 42.86% | -9.24% | 91.46% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 70.00% | 3.71% | -12.12% | 19.55% | 80.00% | 17.04% | 107.02% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 25.00% | -10.93% | -11.71% | 23.49% | 50.00% | -0.15% | 67.63% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 16 | 81.25% | 20.76% | -12.98% | 34.37% | 31.25% | -6.60% | 43.81% |
| DOGE-USD | HISTORICAL_BTC_BULL | 20 | 60.00% | 4.08% | -8.41% | 31.78% | 40.00% | -10.63% | 38.69% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -32.40% | -36.26% | 0.00% | 0.00% | -27.09% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 66.67% | 33.03% | -9.15% | 52.37% | 66.67% | 5.82% | 56.56% |
| SOL-USD | HISTORICAL_BTC_BEAR | 11 | 63.64% | 5.46% | -4.48% | 65.88% | 54.55% | 21.54% | 105.15% |
| SOL-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 8.53% | -5.62% | 46.93% | 62.50% | 14.41% | 107.94% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 21 | 38.10% | -1.75% | -6.62% | 23.31% | 85.71% | 25.36% | 50.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 24 | 62.50% | 3.50% | -3.21% | 28.19% | 50.00% | -0.37% | 100.78% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 4.48% | -10.62% | 39.08% | 66.67% | 11.21% | 159.77% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.77% | -18.59% | 26.18% | 0.00% | -25.57% | 27.75% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -6.61% | -10.39% | 15.84% | 71.43% | 20.57% | 68.26% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 15 | 86.67% | 32.95% | -12.71% | 41.09% | 53.33% | 0.11% | 44.92% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 14 | 71.43% | 4.08% | -6.67% | 29.71% | 35.71% | -8.70% | 35.50% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 68.42% | 0.00% | 71.72% | 100.00% | 45.88% | 71.72% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 30.00% | -6.57% | -17.27% | 13.85% | 10.00% | -23.94% | 18.30% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 10 | 50.00% | 1.06% | -7.11% | 28.65% | 40.00% | -10.51% | 142.86% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 26.36% | -4.31% | 87.80% | 83.33% | 50.36% | 260.95% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 3.09% | -3.35% | 16.16% | 66.67% | 8.24% | 22.90% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 21 | 38.10% | -1.75% | -5.52% | 23.31% | 85.71% | 24.46% | 50.46% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | DOT-USD | 2024-07-14 | 81.17% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 30.61% | -14.39% | 37.23% | 66.62% | -14.39% | 144.58% |
| BTC-USD | BNB-USD | 2026-01-15 | 83.81% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |
| BTC-USD | MANA-USD | 2018-07-21 | 82.52% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | BEARISH_30D | -32.64% | -33.83% | 32.73% | -41.90% | -44.09% | 32.73% |
| BTC-USD | XLM-USD | 2020-08-14 | 87.27% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | NEO-USD | 2018-10-29 | 86.89% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 30.74% | -2.98% | 44.00% | 85.04% | -2.98% | 91.46% |
| BTC-USD | XRP-USD | 2023-07-25 | 86.53% | BULL | BULL | DIFFERENT | MIXED | 0.55% | -4.77% | 17.39% | 0.89% | -4.77% | 17.39% |
| BTC-USD | LTC-USD | 2023-07-24 | 86.10% | BULL | BEAR | DIFFERENT | MIXED | 0.72% | -3.61% | 9.03% | 6.33% | -3.61% | 13.70% |
| BTC-USD | THETA-USD | 2022-04-20 | 85.58% | RECOVERY | BEAR | DIFFERENT | BEARISH_30D | -16.53% | -16.53% | 23.44% | -18.80% | -23.27% | 23.44% |
| BTC-USD | XRP-USD | 2026-01-10 | 85.57% | BEAR | BEAR | DIFFERENT | MIXED | -2.44% | -2.44% | 6.41% | -17.87% | -21.60% | 6.41% |
| BTC-USD | BTC-USD | 2018-10-28 | 85.51% | BEAR | BEAR | DIFFERENT | BULLISH_30D | 12.86% | -1.73% | 19.76% | 45.60% | -1.73% | 45.60% |
| DOGE-USD | SNX-USD | 2025-10-12 | 88.37% | DISTRIBUTION | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -32.40% | -36.26% | 0.00% | -27.09% | -36.26% | 0.00% |
| DOGE-USD | OP-USD | 2026-01-11 | 90.60% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | FTM-USD | 2022-04-01 | 84.91% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 35.00% | -16.51% | 35.47% | -9.93% | -16.51% | 45.15% |
| DOGE-USD | THETA-USD | 2022-03-31 | 84.86% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 34.01% | -12.38% | 34.01% | -13.72% | -13.72% | 34.01% |
| DOGE-USD | CHZ-USD | 2022-03-31 | 84.68% | BEAR | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 49.44% | -3.88% | 49.44% | 83.06% | -3.88% | 146.71% |
| DOGE-USD | VET-USD | 2022-03-29 | 84.64% | RECOVERY | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 33.03% | -9.15% | 33.03% | 5.82% | -9.15% | 41.40% |
| DOGE-USD | ADA-USD | 2022-04-01 | 84.39% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 12.08% | -12.71% | 12.08% | 0.11% | -12.71% | 19.13% |
| DOGE-USD | ATOM-USD | 2022-04-01 | 84.18% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 31.00% | -13.26% | 31.00% | 44.09% | -13.26% | 44.68% |
| DOGE-USD | KSM-USD | 2022-04-19 | 83.97% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.63% | -28.63% | 6.88% | -34.98% | -36.50% | 6.88% |
| DOGE-USD | EGLD-USD | 2023-07-10 | 83.74% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 79.03% | -3.32% | 97.30% | 150.60% | -3.32% | 166.35% |
| SOL-USD | ENJ-USD | 2018-10-29 | 80.94% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 269.45% | -9.43% | 270.52% | 449.81% | -9.43% | 676.95% |
| SOL-USD | ZIL-USD | 2020-08-11 | 80.58% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 101.63% | -2.99% | 101.63% | 237.58% | -2.99% | 312.16% |
| SOL-USD | DASH-USD | 2020-02-16 | 80.38% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.44% | -4.98% | 8.64% | -2.17% | -9.55% | 8.64% |
| SOL-USD | ALGO-USD | 2020-02-20 | 80.33% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -9.13% | -10.10% | 8.93% | 36.82% | -10.92% | 69.53% |
| SOL-USD | EOS-USD | 2018-11-13 | 79.87% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -6.92% | -16.43% | 8.85% | 33.78% | -16.43% | 48.92% |
| SOL-USD | VET-USD | 2020-02-18 | 79.72% | RECOVERY | RECOVERY | DIFFERENT | EXPLOSIVE_60D | 82.11% | 0.00% | 98.84% | 258.30% | 0.00% | 308.84% |
| SOL-USD | ONE-USD | 2020-02-16 | 78.23% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -22.88% | -22.88% | 8.51% | -2.49% | -22.88% | 8.51% |
| SOL-USD | BCH-USD | 2020-02-16 | 77.91% | RECOVERY | RECOVERY | DIFFERENT | MIXED | 1.12% | -1.45% | 11.58% | 2.15% | -5.27% | 11.58% |
| SOL-USD | BNB-USD | 2020-02-16 | 77.89% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -2.28% | -3.01% | 9.23% | 16.78% | -7.41% | 16.78% |
| SOL-USD | ATOM-USD | 2020-02-21 | 77.66% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -5.94% | -13.19% | 11.96% | 29.45% | -13.19% | 55.17% |

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

