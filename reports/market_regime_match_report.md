# Market Regime Match Report

Generated: 2026-08-03 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 62.760 $ | False | -22.44% | -9.90% | BEAR | -22.44% | -9.90% |
| DOGE-USD | BEAR | 0.06985 $ | False | -39.19% | -16.46% | BEAR | -22.44% | -9.90% |
| SOL-USD | BEAR | 72,93 $ | False | -15.51% | -16.88% | BEAR | -22.44% | -9.90% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 77.50% | 9.76% | 26.13% | 51.43% | -3.42% | -26.26% | 14.75% | 43.14% | 62.23% | 52.50% | 7.73% | 45.17% | 69.75% |
| BTC-USD | SAME_BTC_REGIME | 13 | 92.31% | 5.81% | 9.85% | 17.32% | -2.06% | -13.33% | 9.53% | 17.22% | 39.76% | 23.08% | -12.28% | -8.77% | 25.43% |
| BTC-USD | SAME_ASSET_REGIME | 20 | 95.00% | 10.76% | 31.42% | 51.43% | -2.00% | -11.06% | 17.74% | 46.46% | 62.23% | 60.00% | 30.27% | 52.19% | 81.05% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 90.91% | 5.81% | 9.76% | 13.61% | -3.24% | -14.08% | 9.53% | 14.75% | 18.25% | 27.27% | -11.53% | -2.12% | 30.65% |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 3.44% | 17.87% | 37.36% | -13.69% | -27.68% | 12.32% | 29.23% | 44.45% | 52.50% | 1.16% | 14.09% | 72.08% |
| DOGE-USD | SAME_BTC_REGIME | 20 | 65.00% | 5.23% | 16.77% | 31.82% | -13.69% | -22.95% | 9.47% | 20.36% | 44.45% | 60.00% | 2.25% | 12.75% | 34.11% |
| DOGE-USD | SAME_ASSET_REGIME | 21 | 66.67% | 6.51% | 16.84% | 45.81% | -13.62% | -22.75% | 8.94% | 22.25% | 55.31% | 57.14% | 1.62% | 45.22% | 81.89% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 62.50% | 3.44% | 9.90% | 16.79% | -13.85% | -20.49% | 7.31% | 12.07% | 20.99% | 50.00% | -0.49% | 6.96% | 46.66% |
| SOL-USD | ALL_MATCHES | 40 | 80.00% | 12.30% | 25.06% | 65.84% | -2.55% | -20.45% | 14.76% | 29.14% | 84.88% | 57.50% | 6.49% | 44.66% | 125.14% |
| SOL-USD | SAME_BTC_REGIME | 19 | 94.74% | 11.57% | 21.61% | 43.86% | -1.76% | -15.55% | 14.11% | 23.52% | 52.13% | 52.63% | 1.20% | 54.55% | 126.01% |
| SOL-USD | SAME_ASSET_REGIME | 27 | 85.19% | 11.57% | 22.44% | 45.81% | -2.12% | -22.00% | 14.11% | 25.92% | 55.93% | 55.56% | 2.39% | 54.55% | 103.53% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 94.74% | 11.57% | 21.61% | 43.86% | -1.76% | -15.55% | 14.11% | 23.52% | 52.13% | 52.63% | 1.20% | 54.55% | 126.01% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 13 | 92.31% | 5.81% | -2.06% | 17.22% | 23.08% | -12.28% | 30.65% |
| BTC-USD | HISTORICAL_BTC_BULL | 18 | 66.67% | 21.42% | -4.57% | 48.43% | 66.67% | 27.54% | 60.04% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 57.08% | -5.36% | 92.08% | 100.00% | 75.98% | 117.29% |
| BTC-USD | HISTORICAL_BTC_MIXED | 3 | 66.67% | 12.97% | -2.65% | 22.86% | 33.33% | -5.83% | 31.45% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 6.05% | -3.62% | 68.56% | 75.00% | 20.60% | 123.40% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 20 | 65.00% | 5.23% | -13.69% | 20.36% | 60.00% | 2.25% | 57.80% |
| DOGE-USD | HISTORICAL_BTC_BULL | 11 | 54.55% | 11.95% | -8.39% | 33.10% | 54.55% | 1.09% | 59.36% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 9 | 33.33% | -7.78% | -18.07% | 29.43% | 33.33% | -12.52% | 35.30% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 94.74% | 11.57% | -1.76% | 23.52% | 52.63% | 1.20% | 74.55% |
| SOL-USD | HISTORICAL_BTC_BULL | 12 | 58.33% | 10.20% | -9.48% | 31.39% | 58.33% | 12.39% | 57.94% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 109.98% | 0.00% | 116.54% | 100.00% | 189.82% | 308.32% |
| SOL-USD | HISTORICAL_BTC_MIXED | 5 | 100.00% | 13.99% | -2.12% | 25.03% | 80.00% | 10.39% | 38.00% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -26.62% | -28.64% | 0.00% | 0.00% | -27.24% | 0.00% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 95.00% | 10.76% | -2.00% | 46.46% | 60.00% | 30.27% | 80.32% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 55.56% | 1.78% | -15.02% | 35.94% | 55.56% | 10.93% | 58.55% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 25.26% | -0.11% | 35.46% | 100.00% | 42.26% | 50.68% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 68.06% | -1.33% | 96.14% | 100.00% | 45.08% | 100.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 50.00% | -0.41% | -9.48% | 10.81% | 12.50% | -13.74% | 15.52% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 21 | 66.67% | 6.51% | -13.62% | 22.25% | 57.14% | 1.62% | 69.37% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 40.00% | -7.78% | -12.40% | 29.16% | 40.00% | -12.52% | 38.51% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 13.08% | -17.22% | 25.72% | 100.00% | 12.97% | 61.37% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 12 | 41.67% | -4.17% | -17.76% | 30.90% | 41.67% | -8.76% | 37.37% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 85.19% | 11.57% | -2.12% | 25.92% | 55.56% | 2.39% | 74.55% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 2.18% | -8.23% | 53.65% | 66.67% | 4.77% | 216.82% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 4.68% | -11.18% | 29.14% | 50.00% | 2.47% | 39.09% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 110.91% | 0.00% | 118.05% | 100.00% | 42.57% | 118.05% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 80.00% | 18.22% | -4.75% | 27.09% | 60.00% | 33.09% | 50.93% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-26 | 90.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.81% | 0.00% | 12.27% | -8.77% | -8.77% | 12.81% |
| BTC-USD | ETH-USD | 2025-12-26 | 89.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.61% | 0.00% | 17.22% | -12.28% | -12.28% | 17.22% |
| BTC-USD | BTC-USD | 2025-12-28 | 87.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.25% | 0.00% | 18.25% | -11.53% | -11.53% | 19.28% |
| BTC-USD | XTZ-USD | 2018-10-14 | 86.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 9.53% | -14.08% | 9.53% | 77.90% | -14.08% | 96.71% |
| BTC-USD | OMG-USD | 2018-10-14 | 86.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.30% | -19.94% | 4.30% | 30.65% | -19.94% | 30.65% |
| BTC-USD | BNB-USD | 2025-12-26 | 86.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| BTC-USD | XTZ-USD | 2025-12-31 | 85.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| BTC-USD | QTUM-USD | 2025-12-26 | 85.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.97% | -10.32% | 0.75% | -15.48% | -16.50% | 8.73% |
| BTC-USD | XRP-USD | 2019-10-19 | 85.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.85% | 0.00% | 45.14% | -24.13% | -39.47% | 45.14% |
| BTC-USD | ETC-USD | 2025-12-26 | 85.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.56% | -5.82% | 2.55% | -10.55% | -11.99% | 15.34% |
| DOGE-USD | OP-USD | 2025-12-27 | 91.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.75% | -2.92% | 22.25% | 1.62% | -2.92% | 56.55% |
| DOGE-USD | VET-USD | 2022-03-19 | 90.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.00% | -11.66% | 7.24% | 10.13% | -11.66% | 37.50% |
| DOGE-USD | LTC-USD | 2018-04-14 | 89.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.24% | -35.07% | 7.37% | -31.89% | -37.88% | 7.37% |
| DOGE-USD | HBAR-USD | 2022-03-19 | 89.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.48% | -13.35% | 6.89% | 1.24% | -13.35% | 20.52% |
| DOGE-USD | BAT-USD | 2018-10-14 | 88.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.84% | -13.62% | 17.16% | 62.34% | -13.62% | 69.37% |
| DOGE-USD | XTZ-USD | 2025-12-26 | 88.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| DOGE-USD | ADA-USD | 2022-03-17 | 88.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.92% | -16.28% | 3.63% | -6.81% | -16.28% | 14.25% |
| DOGE-USD | FIL-USD | 2022-03-21 | 88.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 7.81% | -7.71% | 9.99% | 5.90% | -7.71% | 78.68% |
| DOGE-USD | INJ-USD | 2022-03-19 | 88.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.63% | -13.94% | 4.96% | 30.97% | -13.94% | 53.75% |
| DOGE-USD | THETA-USD | 2022-03-21 | 88.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.86% | -13.75% | 6.86% | -10.80% | -13.75% | 31.92% |
| SOL-USD | ENJ-USD | 2018-10-14 | 81.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.62% | -25.10% | 11.62% | 465.84% | -25.10% | 542.51% |
| SOL-USD | NEAR-USD | 2025-12-26 | 80.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 0.47% | -0.75% | 14.11% | 124.27% | -0.75% | 124.27% |
| SOL-USD | QTUM-USD | 2018-10-14 | 79.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.45% | -14.45% | 6.45% | 24.60% | -14.45% | 33.28% |
| SOL-USD | RUNE-USD | 2025-12-27 | 78.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.91% | -0.37% | 41.91% | -5.22% | -5.22% | 62.96% |
| SOL-USD | LINK-USD | 2025-12-26 | 78.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.60% | 0.00% | 10.72% | -4.12% | -4.12% | 23.23% |
| SOL-USD | EOS-USD | 2018-10-24 | 78.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.66% | 0.00% | 83.90% | 81.05% | 0.00% | 86.15% |
| SOL-USD | BNB-USD | 2025-12-31 | 78.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| SOL-USD | SOL-USD | 2025-12-29 | 77.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| SOL-USD | BTC-USD | 2025-12-28 | 77.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.25% | 0.00% | 18.25% | -11.53% | -11.53% | 19.28% |
| SOL-USD | KAVA-USD | 2025-12-26 | 76.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.96% | -2.75% | 24.96% | 1.20% | -2.75% | 31.13% |

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

