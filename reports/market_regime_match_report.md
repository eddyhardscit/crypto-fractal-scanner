# Market Regime Match Report

Generated: 2026-08-04 05:16 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.846 $ | False | -21.62% | -9.91% | BEAR | -21.62% | -9.91% |
| DOGE-USD | BEAR | 0.07019 $ | False | -37.58% | -16.51% | BEAR | -21.62% | -9.91% |
| SOL-USD | BEAR | 73,72 $ | False | -17.35% | -16.94% | BEAR | -21.62% | -9.91% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 12.19% | 25.22% | 60.77% | -4.17% | -20.56% | 16.27% | 40.46% | 68.36% | 57.50% | 20.09% | 47.78% | 81.05% |
| BTC-USD | SAME_BTC_REGIME | 13 | 92.31% | 9.53% | 11.22% | 19.90% | -4.80% | -13.33% | 11.77% | 17.22% | 40.41% | 38.46% | -8.77% | 21.84% | 68.45% |
| BTC-USD | SAME_ASSET_REGIME | 20 | 95.00% | 10.53% | 29.21% | 60.77% | -2.84% | -11.06% | 15.70% | 46.46% | 68.36% | 60.00% | 25.87% | 52.19% | 81.05% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 13 | 92.31% | 9.53% | 11.22% | 19.90% | -4.80% | -13.33% | 11.77% | 17.22% | 40.41% | 38.46% | -8.77% | 21.84% | 68.45% |
| DOGE-USD | ALL_MATCHES | 40 | 57.50% | 6.69% | 17.83% | 31.21% | -13.69% | -27.68% | 13.01% | 25.15% | 37.43% | 52.50% | 1.16% | 16.98% | 82.99% |
| DOGE-USD | SAME_BTC_REGIME | 24 | 66.67% | 7.34% | 16.77% | 26.57% | -13.69% | -21.39% | 10.42% | 22.35% | 30.27% | 54.17% | 1.43% | 14.04% | 56.23% |
| DOGE-USD | SAME_ASSET_REGIME | 24 | 70.83% | 8.73% | 17.08% | 40.90% | -13.49% | -17.69% | 10.42% | 22.70% | 48.02% | 58.33% | 2.25% | 42.79% | 89.54% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 21 | 66.67% | 6.86% | 16.16% | 17.82% | -13.75% | -18.23% | 8.94% | 17.82% | 24.02% | 52.38% | 1.24% | 12.65% | 62.34% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 7.50% | 23.11% | 65.84% | -4.46% | -25.16% | 11.17% | 25.91% | 84.88% | 52.50% | 3.58% | 44.66% | 125.14% |
| SOL-USD | SAME_BTC_REGIME | 20 | 80.00% | 7.02% | 15.89% | 51.67% | -4.20% | -24.42% | 11.17% | 19.32% | 53.26% | 50.00% | 4.42% | 43.52% | 125.14% |
| SOL-USD | SAME_ASSET_REGIME | 28 | 75.00% | 7.02% | 15.47% | 51.67% | -4.46% | -25.27% | 11.17% | 19.32% | 56.39% | 50.00% | 1.09% | 37.28% | 99.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 84.21% | 7.60% | 18.17% | 51.67% | -3.86% | -20.92% | 11.62% | 21.41% | 54.82% | 47.37% | -0.20% | 54.55% | 126.01% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 13 | 92.31% | 9.53% | -4.80% | 17.22% | 38.46% | -8.77% | 34.36% |
| BTC-USD | HISTORICAL_BTC_BULL | 17 | 70.59% | 22.75% | -5.08% | 52.32% | 64.71% | 38.53% | 66.60% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 57.08% | -5.36% | 92.08% | 100.00% | 75.98% | 117.29% |
| BTC-USD | HISTORICAL_BTC_MIXED | 6 | 83.33% | 15.94% | -2.63% | 25.96% | 66.67% | 21.48% | 46.11% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | -5.52% | -13.10% | 84.21% | 50.00% | 4.77% | 84.21% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 24 | 66.67% | 7.34% | -13.69% | 22.35% | 54.17% | 1.43% | 55.76% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 60.00% | 14.93% | -7.88% | 34.93% | 60.00% | 6.54% | 62.80% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -8.73% | -20.19% | 15.92% | 33.33% | -6.52% | 26.30% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 80.00% | 7.02% | -4.20% | 19.32% | 50.00% | 4.42% | 63.64% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 50.00% | -4.09% | -10.57% | 28.30% | 50.00% | -1.57% | 40.85% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 109.05% | 0.00% | 115.02% | 100.00% | 51.71% | 244.90% |
| SOL-USD | HISTORICAL_BTC_MIXED | 5 | 100.00% | 12.97% | -2.12% | 17.12% | 60.00% | 2.39% | 17.12% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -26.16% | -27.30% | 1.90% | 0.00% | -29.07% | 1.90% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 95.00% | 10.53% | -2.84% | 46.46% | 60.00% | 25.87% | 80.32% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 60.00% | 10.90% | -12.59% | 48.12% | 50.00% | 0.43% | 58.83% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 25.26% | -0.11% | 35.46% | 100.00% | 42.26% | 50.68% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 68.06% | -1.33% | 96.14% | 100.00% | 45.08% | 100.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 12.72% | -4.75% | 20.17% | 42.86% | -0.32% | 28.92% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 24 | 70.83% | 8.73% | -13.49% | 22.70% | 58.33% | 2.25% | 67.03% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 40.00% | -7.78% | -12.40% | 29.16% | 40.00% | -8.70% | 38.51% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 27.99% | -9.73% | 28.55% | 100.00% | 18.18% | 69.38% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 30.00% | -7.96% | -19.04% | 21.84% | 40.00% | -7.19% | 27.85% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 75.00% | 7.02% | -4.46% | 19.32% | 50.00% | 1.09% | 63.64% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 2.18% | -8.23% | 49.67% | 100.00% | 12.01% | 231.19% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -15.08% | -16.46% | 14.58% | 33.33% | -15.06% | 21.36% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 110.91% | 0.00% | 118.05% | 100.00% | 42.57% | 118.05% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 80.00% | 12.97% | -3.24% | 25.03% | 40.00% | -0.23% | 50.93% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-26 | 89.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.81% | 0.00% | 12.27% | -8.77% | -8.77% | 12.81% |
| BTC-USD | ETH-USD | 2025-12-26 | 89.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.61% | 0.00% | 17.22% | -12.28% | -12.28% | 17.22% |
| BTC-USD | BTC-USD | 2018-10-12 | 88.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.02% | -8.83% | 5.02% | 9.63% | -8.83% | 11.10% |
| BTC-USD | OMG-USD | 2018-10-14 | 87.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.30% | -19.94% | 4.30% | 30.65% | -19.94% | 30.65% |
| BTC-USD | XTZ-USD | 2018-10-14 | 87.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 9.53% | -14.08% | 9.53% | 77.90% | -14.08% | 96.71% |
| BTC-USD | XRP-USD | 2019-10-19 | 87.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.85% | 0.00% | 45.14% | -24.13% | -39.47% | 45.14% |
| BTC-USD | BTC-USD | 2025-12-29 | 87.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.22% | -1.65% | 13.19% | -15.39% | -15.39% | 14.18% |
| BTC-USD | XTZ-USD | 2025-12-31 | 86.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| BTC-USD | SOL-USD | 2025-12-29 | 86.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| BTC-USD | NEO-USD | 2018-10-14 | 86.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 21.47% | -9.47% | 21.47% | 21.84% | -9.47% | 34.36% |
| DOGE-USD | OP-USD | 2025-12-27 | 91.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.75% | -2.92% | 22.25% | 1.62% | -2.92% | 56.55% |
| DOGE-USD | VET-USD | 2022-03-19 | 90.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.00% | -11.66% | 7.24% | 10.13% | -11.66% | 37.50% |
| DOGE-USD | LTC-USD | 2018-04-15 | 89.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.89% | -34.50% | 8.31% | -26.34% | -37.34% | 8.31% |
| DOGE-USD | DASH-USD | 2022-03-17 | 89.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.39% | -22.75% | 0.95% | -6.32% | -22.75% | 9.96% |
| DOGE-USD | ETC-USD | 2022-03-17 | 89.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 56.33% | -15.35% | 59.00% | 109.41% | -15.35% | 165.75% |
| DOGE-USD | ADA-USD | 2022-03-17 | 89.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.92% | -16.28% | 3.63% | -6.81% | -16.28% | 14.25% |
| DOGE-USD | BAT-USD | 2018-10-14 | 89.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.84% | -13.62% | 17.16% | 62.34% | -13.62% | 69.37% |
| DOGE-USD | NEO-USD | 2022-03-17 | 89.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.51% | -16.44% | 8.94% | 2.89% | -16.44% | 24.41% |
| DOGE-USD | HBAR-USD | 2022-03-19 | 88.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.48% | -13.35% | 6.89% | 1.24% | -13.35% | 20.52% |
| DOGE-USD | THETA-USD | 2022-03-21 | 88.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.86% | -13.75% | 6.86% | -10.80% | -13.75% | 31.92% |
| SOL-USD | ENJ-USD | 2018-10-14 | 83.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.62% | -25.10% | 11.62% | 465.84% | -25.10% | 542.51% |
| SOL-USD | NEAR-USD | 2025-12-26 | 82.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 0.47% | -0.75% | 14.11% | 124.27% | -0.75% | 124.27% |
| SOL-USD | QTUM-USD | 2018-10-14 | 80.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.45% | -14.45% | 6.45% | 24.60% | -14.45% | 33.28% |
| SOL-USD | RUNE-USD | 2026-01-01 | 79.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 51.69% | -4.54% | 51.69% | -3.02% | -20.45% | 56.14% |
| SOL-USD | LINK-USD | 2025-12-26 | 78.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.60% | 0.00% | 10.72% | -4.12% | -4.12% | 23.23% |
| SOL-USD | BNB-USD | 2025-12-31 | 78.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| SOL-USD | EOS-USD | 2018-10-24 | 78.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.66% | 0.00% | 83.90% | 81.05% | 0.00% | 86.15% |
| SOL-USD | SOL-USD | 2025-12-29 | 78.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| SOL-USD | DOT-USD | 2025-12-26 | 77.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.89% | -6.91% | 6.75% | -11.84% | -13.97% | 10.44% |
| SOL-USD | KAVA-USD | 2025-12-31 | 77.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.73% | -3.48% | 25.59% | -18.69% | -20.93% | 27.22% |

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

