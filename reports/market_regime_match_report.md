# Market Regime Match Report

Generated: 2026-08-24 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | MIXED | 77.028 $ | True | 1.47% | -9.39% | MIXED | 1.47% | -9.39% |
| DOGE-USD | DISTRIBUTION | 0.09210 $ | True | -9.05% | -15.89% | MIXED | 1.47% | -9.39% |
| SOL-USD | RECOVERY | 94,05 $ | True | 12.18% | -15.58% | MIXED | 1.47% | -9.39% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 5.87% | 14.85% | 36.85% | -7.21% | -17.32% | 13.00% | 28.52% | 44.17% | 70.00% | 16.96% | 43.67% | 92.30% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 52.50% | 1.87% | 16.86% | 33.77% | -10.26% | -31.21% | 20.29% | 36.69% | 48.21% | 42.50% | -10.49% | 29.18% | 93.88% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -27.61% | -27.61% | -27.61% | -34.07% | -34.07% | 0.00% | 0.00% | 0.00% | 0.00% | -25.08% | -25.08% | -25.08% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 1.63% | 18.70% | 44.10% | -9.86% | -17.25% | 11.83% | 24.05% | 51.71% | 75.00% | 23.92% | 32.48% | 110.93% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 16 | 25.00% | -5.89% | 1.69% | 24.60% | -11.51% | -16.41% | 5.09% | 18.79% | 48.01% | 93.75% | 24.48% | 31.51% | 37.80% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 11 | 36.36% | -5.83% | -6.97% | 31.98% | 54.55% | 12.70% | 91.53% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 78.26% | 9.48% | -7.00% | 26.15% | 78.26% | 15.86% | 72.89% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 66.67% | 14.34% | 0.00% | 20.24% | 66.67% | 30.12% | 49.06% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -15.07% | -15.75% | 35.71% | 66.67% | 23.44% | 55.17% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 6 | 33.33% | -5.92% | -17.12% | 34.47% | 16.67% | -22.88% | 34.47% |
| DOGE-USD | HISTORICAL_BTC_BULL | 27 | 66.67% | 8.90% | -6.74% | 39.10% | 59.26% | 7.49% | 77.00% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -27.61% | -34.07% | 0.00% | 0.00% | -25.08% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -15.45% | -18.95% | 20.85% | 0.00% | -28.72% | 20.85% |
| SOL-USD | HISTORICAL_BTC_BEAR | 9 | 66.67% | 12.26% | -6.90% | 49.47% | 66.67% | 5.41% | 62.62% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 71.43% | 7.35% | -9.71% | 22.60% | 64.29% | 23.60% | 68.34% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 18.89% | -13.32% | 18.89% | 0.00% | -13.86% | 18.89% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 16 | 25.00% | -7.07% | -12.23% | 14.80% | 93.75% | 26.93% | 56.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 65.38% | 7.69% | -6.27% | 26.53% | 73.08% | 14.42% | 64.53% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 11.17% | -5.70% | 40.01% | 57.14% | 29.10% | 163.32% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -4.88% | -15.75% | 27.81% | 71.43% | 22.65% | 55.17% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 8 | 37.50% | -5.92% | -14.31% | 27.72% | 25.00% | -19.33% | 49.82% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 24 | 62.50% | 4.61% | -8.71% | 42.30% | 54.17% | 4.67% | 71.74% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -27.61% | -34.07% | 0.00% | 0.00% | -25.08% | 0.00% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 7 | 42.86% | -20.28% | -31.16% | 26.14% | 28.57% | -32.36% | 33.51% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 17 | 70.59% | 4.51% | -9.89% | 20.31% | 52.94% | 0.43% | 62.62% |
| SOL-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 14.13% | -2.94% | 80.25% | 85.71% | 106.74% | 221.20% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 16 | 25.00% | -5.89% | -11.51% | 18.79% | 93.75% | 24.48% | 51.28% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2023-07-30 | 86.54% | BULL | BULL | DIFFERENT | BEARISH_30D | -10.51% | -18.88% | 0.00% | -19.43% | -19.43% | 0.00% |
| BTC-USD | BNB-USD | 2018-11-03 | 85.25% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| BTC-USD | THETA-USD | 2018-11-02 | 83.27% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 93.12% | 0.00% | 137.20% | 61.21% | 0.00% | 137.20% |
| BTC-USD | XLM-USD | 2020-08-14 | 82.55% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | EOS-USD | 2023-07-30 | 82.38% | BULL | BEAR | DIFFERENT | MIXED | 5.82% | -7.00% | 6.19% | 6.95% | -7.00% | 29.44% |
| BTC-USD | LTC-USD | 2023-07-28 | 82.33% | BULL | BULL | DIFFERENT | MIXED | 3.33% | -5.70% | 6.67% | -7.34% | -7.34% | 11.25% |
| BTC-USD | LTC-USD | 2018-11-01 | 82.02% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 31.56% | -4.20% | 33.64% | 99.67% | -4.20% | 112.99% |
| BTC-USD | ETC-USD | 2023-07-30 | 81.54% | BULL | BEAR | DIFFERENT | MIXED | 9.48% | -1.99% | 12.30% | 8.74% | -1.99% | 22.62% |
| BTC-USD | ETC-USD | 2020-08-19 | 81.38% | BULL | RECOVERY | DIFFERENT | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| BTC-USD | RUNE-USD | 2026-01-16 | 81.29% | BEAR | BEAR | DIFFERENT | MIXED | -7.25% | -12.51% | 30.32% | -16.10% | -33.60% | 30.32% |
| DOGE-USD | BTC-USD | 2025-10-10 | 81.88% | DISTRIBUTION | DISTRIBUTION | SAME_ASSET_ONLY | BEARISH_30D | -27.61% | -34.07% | 0.00% | -25.08% | -34.07% | 0.00% |
| DOGE-USD | MANA-USD | 2025-01-15 | 87.60% | BULL | BULL | DIFFERENT | MIXED | -4.31% | -10.11% | 18.69% | -19.03% | -26.84% | 18.69% |
| DOGE-USD | VET-USD | 2025-01-17 | 86.57% | BULL | BULL | DIFFERENT | MIXED | 1.03% | -8.45% | 18.77% | -22.61% | -29.05% | 18.77% |
| DOGE-USD | FIL-USD | 2022-04-25 | 86.24% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -29.26% | -31.16% | 16.04% | -32.36% | -35.61% | 16.04% |
| DOGE-USD | OP-USD | 2026-01-16 | 85.45% | BEAR | BEAR | DIFFERENT | MIXED | 3.57% | -4.25% | 37.84% | -16.66% | -27.25% | 37.84% |
| DOGE-USD | AVAX-USD | 2025-01-16 | 85.43% | BULL | BULL | DIFFERENT | MIXED | 5.65% | -11.98% | 16.68% | -17.86% | -25.64% | 16.68% |
| DOGE-USD | IOTA-USD | 2025-01-16 | 85.24% | BULL | BULL | DIFFERENT | MIXED | -0.35% | -6.45% | 21.79% | -22.35% | -30.21% | 21.79% |
| DOGE-USD | SAND-USD | 2025-01-14 | 85.13% | BULL | BULL | DIFFERENT | MIXED | 3.56% | -8.98% | 23.97% | -21.92% | -21.92% | 23.97% |
| DOGE-USD | AVAX-USD | 2025-09-28 | 84.37% | BULL | RECOVERY | DIFFERENT | BEARISH_30D | -32.83% | -32.83% | 1.94% | -37.57% | -42.62% | 1.94% |
| DOGE-USD | QTUM-USD | 2022-04-21 | 84.37% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -36.05% | -36.05% | 0.00% | -38.23% | -40.91% | 0.00% |
| SOL-USD | VET-USD | 2020-02-23 | 80.79% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | ZEC-USD | 2020-02-21 | 74.56% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.23% | -9.12% | 6.45% | 32.15% | -9.12% | 32.15% |
| SOL-USD | MKR-USD | 2020-02-22 | 73.89% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| SOL-USD | ETC-USD | 2020-08-19 | 73.42% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| SOL-USD | ALGO-USD | 2020-02-25 | 73.37% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.75% | -15.75% | 2.83% | 24.41% | -15.75% | 60.35% |
| SOL-USD | BNB-USD | 2020-02-21 | 72.24% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.61% | -14.42% | 0.97% | 12.13% | -14.42% | 13.70% |
| SOL-USD | WAVES-USD | 2023-07-30 | 72.01% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 10.19% | -6.81% | 17.27% | 24.55% | -6.81% | 45.32% |
| SOL-USD | DASH-USD | 2020-02-21 | 71.11% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.85% | -14.87% | 1.15% | 3.43% | -15.78% | 3.43% |
| SOL-USD | QTUM-USD | 2020-02-26 | 70.36% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -8.20% | -13.76% | 0.78% | 42.12% | -13.76% | 43.18% |
| SOL-USD | BAT-USD | 2020-02-21 | 69.11% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 18.68% | -4.23% | 23.34% | 12.07% | -4.23% | 23.75% |

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

