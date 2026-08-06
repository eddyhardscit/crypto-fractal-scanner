# Market Regime Match Report

Generated: 2026-08-06 05:15 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.848 $ | False | -19.11% | -9.96% | BEAR | -19.11% | -9.96% |
| DOGE-USD | BEAR | 0.06998 $ | False | -36.07% | -16.56% | BEAR | -19.11% | -9.96% |
| SOL-USD | BEAR | 74,13 $ | False | -19.36% | -17.03% | BEAR | -19.11% | -9.96% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 9.59% | 19.25% | 40.79% | -4.71% | -20.52% | 12.66% | 39.88% | 56.99% | 55.00% | 10.44% | 35.65% | 81.05% |
| BTC-USD | SAME_BTC_REGIME | 18 | 88.89% | 8.52% | 10.25% | 15.12% | -4.87% | -16.08% | 10.14% | 13.06% | 46.67% | 33.33% | -12.05% | 13.39% | 44.83% |
| BTC-USD | SAME_ASSET_REGIME | 25 | 88.00% | 9.53% | 20.26% | 37.41% | -4.65% | -17.73% | 11.77% | 42.84% | 54.34% | 48.00% | -0.20% | 34.16% | 73.56% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 88.89% | 8.52% | 10.25% | 15.12% | -4.87% | -16.08% | 10.14% | 13.06% | 46.67% | 33.33% | -12.05% | 13.39% | 44.83% |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 6.69% | 22.92% | 43.22% | -13.85% | -27.49% | 14.49% | 25.02% | 50.07% | 47.50% | -1.42% | 28.28% | 93.08% |
| DOGE-USD | SAME_BTC_REGIME | 23 | 60.87% | 6.86% | 17.33% | 42.89% | -13.94% | -25.21% | 11.77% | 23.04% | 47.17% | 43.48% | -2.22% | 14.59% | 58.27% |
| DOGE-USD | SAME_ASSET_REGIME | 22 | 68.18% | 10.83% | 22.01% | 45.42% | -12.64% | -18.22% | 12.09% | 23.87% | 54.77% | 50.00% | 1.14% | 39.22% | 91.72% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 63.16% | 6.86% | 16.50% | 27.13% | -13.75% | -19.13% | 8.94% | 18.77% | 29.18% | 42.11% | -2.22% | 20.55% | 71.75% |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 7.52% | 13.04% | 52.38% | -3.92% | -25.16% | 12.12% | 22.50% | 54.39% | 52.50% | 2.50% | 46.72% | 127.77% |
| SOL-USD | SAME_BTC_REGIME | 15 | 80.00% | 7.22% | 14.19% | 40.11% | -3.99% | -22.04% | 13.46% | 19.19% | 41.25% | 46.67% | -0.20% | 84.46% | 145.28% |
| SOL-USD | SAME_ASSET_REGIME | 24 | 70.83% | 6.97% | 14.49% | 27.11% | -4.27% | -25.50% | 12.12% | 18.44% | 36.08% | 50.00% | 1.09% | 46.72% | 124.15% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 15 | 80.00% | 7.22% | 14.19% | 40.11% | -3.99% | -22.04% | 13.46% | 19.19% | 41.25% | 46.67% | -0.20% | 84.46% | 145.28% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 88.89% | 8.52% | -4.87% | 13.06% | 33.33% | -12.05% | 33.43% |
| BTC-USD | HISTORICAL_BTC_BULL | 13 | 69.23% | 15.05% | -4.65% | 52.32% | 69.23% | 27.38% | 69.91% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 11.75% | -5.36% | 42.07% | 100.00% | 71.78% | 99.09% |
| BTC-USD | HISTORICAL_BTC_MIXED | 3 | 100.00% | 12.72% | -1.80% | 20.68% | 100.00% | 8.35% | 28.39% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 50.00% | -0.35% | -10.20% | 45.59% | 50.00% | 10.79% | 68.43% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 60.87% | 6.86% | -13.94% | 23.04% | 43.48% | -2.22% | 51.79% |
| DOGE-USD | HISTORICAL_BTC_BULL | 13 | 61.54% | 13.48% | -8.39% | 36.19% | 61.54% | 14.84% | 63.02% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 0.00% | -19.52% | -21.25% | 13.88% | 25.00% | -7.71% | 36.24% |
| SOL-USD | HISTORICAL_BTC_BEAR | 15 | 80.00% | 7.22% | -3.99% | 19.19% | 46.67% | -0.20% | 90.01% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 30.00% | -10.79% | -13.78% | 18.75% | 30.00% | -11.49% | 30.87% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 28.98% | 0.00% | 76.01% | 100.00% | 96.08% | 233.92% |
| SOL-USD | HISTORICAL_BTC_MIXED | 6 | 100.00% | 9.20% | -1.96% | 14.72% | 83.33% | 3.86% | 14.72% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 6 | 50.00% | -2.79% | -9.33% | 25.92% | 50.00% | 11.00% | 95.78% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 25 | 88.00% | 9.53% | -4.65% | 42.84% | 48.00% | -0.20% | 51.37% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 14.50% | -5.08% | 43.93% | 71.43% | 16.16% | 90.82% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 63.84% | -4.76% | 106.37% | 100.00% | 36.55% | 106.37% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 8.74% | -2.60% | 20.21% | 57.14% | 5.12% | 28.92% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 22 | 68.18% | 10.83% | -12.64% | 23.87% | 50.00% | 1.14% | 60.70% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 22.75% | -4.25% | 36.19% | 80.00% | 20.27% | 95.53% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 43.62% | -10.62% | 46.98% | 100.00% | 14.59% | 69.28% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 11 | 18.18% | -16.07% | -21.24% | 16.75% | 18.18% | -21.46% | 21.02% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 24 | 70.83% | 6.97% | -4.27% | 18.44% | 50.00% | 1.09% | 64.11% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 7.63% | -0.48% | 53.39% | 66.67% | 120.52% | 243.02% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -2.05% | -10.61% | 43.70% | 50.00% | -2.35% | 53.40% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 9 | 66.67% | 8.74% | -3.24% | 15.10% | 55.56% | 2.60% | 16.25% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-31 | 88.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.65% | -1.42% | 9.89% | -13.09% | -18.65% | 10.41% |
| BTC-USD | BTC-USD | 2018-10-14 | 88.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.85% | -4.94% | 11.85% | 12.53% | -4.94% | 15.84% |
| BTC-USD | ETH-USD | 2025-12-31 | 87.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.28% | 0.00% | 10.59% | -22.79% | -28.34% | 10.59% |
| BTC-USD | SOL-USD | 2025-12-29 | 87.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| BTC-USD | BNB-USD | 2025-12-31 | 87.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| BTC-USD | XTZ-USD | 2025-12-31 | 87.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| BTC-USD | BTC-USD | 2025-12-31 | 86.89% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.40% | -1.41% | 13.46% | -12.09% | -15.19% | 14.45% |
| BTC-USD | ETH-USD | 2018-07-11 | 86.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -14.43% | -14.43% | 7.43% | -53.22% | -58.54% | 7.43% |
| BTC-USD | NEO-USD | 2018-10-14 | 86.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 21.47% | -9.47% | 21.47% | 21.84% | -9.47% | 34.36% |
| BTC-USD | XTZ-USD | 2018-10-14 | 86.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 9.53% | -14.08% | 9.53% | 77.90% | -14.08% | 96.71% |
| DOGE-USD | OP-USD | 2026-01-01 | 90.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.98% | -7.10% | 49.82% | -15.88% | -18.56% | 49.82% |
| DOGE-USD | VET-USD | 2022-03-19 | 89.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.00% | -11.66% | 7.24% | 10.13% | -11.66% | 37.50% |
| DOGE-USD | LTC-USD | 2018-04-17 | 89.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.86% | -37.42% | 0.00% | -28.88% | -40.13% | 0.00% |
| DOGE-USD | DASH-USD | 2022-03-17 | 89.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.39% | -22.75% | 0.95% | -6.32% | -22.75% | 9.96% |
| DOGE-USD | MKR-USD | 2022-10-04 | 89.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.99% | -0.27% | 24.02% | 41.98% | -0.27% | 48.95% |
| DOGE-USD | XTZ-USD | 2025-12-31 | 89.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| DOGE-USD | ETC-USD | 2022-03-17 | 89.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 56.33% | -15.35% | 59.00% | 109.41% | -15.35% | 165.75% |
| DOGE-USD | HBAR-USD | 2022-03-24 | 88.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 23.41% | -3.18% | 23.41% | 3.08% | -3.18% | 34.66% |
| DOGE-USD | NEO-USD | 2022-03-17 | 88.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.51% | -16.44% | 8.94% | 2.89% | -16.44% | 24.41% |
| DOGE-USD | INJ-USD | 2022-03-19 | 88.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.63% | -13.94% | 4.96% | 30.97% | -13.94% | 53.75% |
| SOL-USD | ENJ-USD | 2018-10-14 | 81.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.62% | -25.10% | 11.62% | 465.84% | -25.10% | 542.51% |
| SOL-USD | RUNE-USD | 2026-01-01 | 80.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 51.69% | -4.54% | 51.69% | -3.02% | -20.45% | 56.14% |
| SOL-USD | SOL-USD | 2025-12-29 | 79.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| SOL-USD | NEAR-USD | 2025-12-26 | 79.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 0.47% | -0.75% | 14.11% | 124.27% | -0.75% | 124.27% |
| SOL-USD | EOS-USD | 2018-10-29 | 79.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 58.60% | -1.80% | 78.67% | 123.88% | -1.80% | 123.88% |
| SOL-USD | BNB-USD | 2025-12-31 | 78.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| SOL-USD | KAVA-USD | 2025-12-31 | 77.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.73% | -3.48% | 25.59% | -18.69% | -20.93% | 27.22% |
| SOL-USD | QTUM-USD | 2018-10-19 | 77.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.74% | -15.73% | 15.32% | 25.81% | -15.73% | 31.28% |
| SOL-USD | DOT-USD | 2025-12-26 | 76.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.89% | -6.91% | 6.75% | -11.84% | -13.97% | 10.44% |
| SOL-USD | BTC-USD | 2025-12-31 | 76.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.40% | -1.41% | 13.46% | -12.09% | -15.19% | 14.45% |

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

