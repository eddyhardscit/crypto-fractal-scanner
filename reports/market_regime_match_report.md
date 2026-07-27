# Market Regime Match Report

Generated: 2026-07-27 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 65.304 $ | False | -14.43% | -9.81% | BEAR | -14.43% | -9.81% |
| DOGE-USD | BEAR | 0.07289 $ | False | -26.67% | -16.08% | BEAR | -14.43% | -9.81% |
| SOL-USD | BEAR | 76,32 $ | False | -9.10% | -16.61% | BEAR | -14.43% | -9.81% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 10.38% | 33.48% | 44.97% | -6.62% | -24.90% | 14.81% | 38.74% | 54.47% | 62.50% | 9.43% | 41.82% | 66.03% |
| BTC-USD | SAME_BTC_REGIME | 17 | 82.35% | 3.95% | 19.22% | 34.51% | -4.18% | -19.06% | 11.48% | 22.12% | 48.54% | 64.71% | 5.54% | 10.02% | 29.98% |
| BTC-USD | SAME_ASSET_REGIME | 22 | 86.36% | 10.38% | 34.97% | 49.03% | -4.18% | -17.97% | 14.81% | 43.78% | 51.41% | 72.73% | 9.73% | 53.34% | 65.44% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 15 | 86.67% | 3.95% | 16.42% | 34.77% | -4.18% | -18.44% | 11.48% | 20.88% | 49.57% | 66.67% | 5.54% | 10.55% | 38.99% |
| DOGE-USD | ALL_MATCHES | 40 | 62.50% | 5.37% | 16.33% | 29.64% | -6.78% | -21.40% | 20.47% | 32.13% | 41.11% | 75.00% | 21.48% | 37.71% | 58.18% |
| DOGE-USD | SAME_BTC_REGIME | 27 | 74.07% | 7.02% | 23.38% | 32.28% | -6.22% | -17.62% | 22.31% | 32.77% | 41.18% | 85.19% | 23.23% | 37.87% | 55.58% |
| DOGE-USD | SAME_ASSET_REGIME | 28 | 71.43% | 6.92% | 19.61% | 32.22% | -6.21% | -17.42% | 21.47% | 31.70% | 40.11% | 85.71% | 26.16% | 40.65% | 61.62% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 25 | 72.00% | 7.02% | 19.04% | 32.41% | -6.20% | -18.01% | 21.82% | 32.02% | 40.63% | 84.00% | 23.23% | 38.20% | 56.09% |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 5.22% | 14.95% | 35.47% | -8.29% | -18.20% | 11.47% | 24.19% | 37.97% | 70.00% | 5.12% | 25.71% | 77.39% |
| SOL-USD | SAME_BTC_REGIME | 22 | 86.36% | 9.49% | 25.90% | 35.16% | -5.63% | -13.75% | 16.48% | 27.34% | 45.77% | 86.36% | 7.48% | 51.53% | 86.21% |
| SOL-USD | SAME_ASSET_REGIME | 28 | 64.29% | 5.81% | 11.01% | 29.95% | -8.18% | -18.63% | 11.47% | 19.47% | 30.45% | 71.43% | 4.00% | 25.71% | 77.51% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 84.21% | 9.45% | 16.28% | 29.18% | -5.72% | -14.14% | 14.26% | 21.48% | 37.16% | 84.21% | 4.70% | 41.30% | 79.74% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 17 | 82.35% | 3.95% | -4.18% | 22.12% | 64.71% | 5.54% | 28.15% |
| BTC-USD | HISTORICAL_BTC_BULL | 18 | 66.67% | 19.81% | -6.62% | 43.78% | 66.67% | 34.67% | 62.92% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 50.00% | -0.38% | -13.25% | 9.86% | 25.00% | -13.29% | 11.82% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 27 | 74.07% | 7.02% | -6.22% | 32.77% | 85.19% | 23.23% | 59.11% |
| DOGE-USD | HISTORICAL_BTC_BULL | 7 | 57.14% | 7.72% | -5.98% | 32.09% | 57.14% | 7.71% | 60.42% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -17.99% | -20.57% | 13.78% | 50.00% | 7.82% | 33.57% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 86.36% | 9.49% | -5.63% | 27.34% | 86.36% | 7.48% | 71.04% |
| SOL-USD | HISTORICAL_BTC_BULL | 6 | 50.00% | 0.99% | -6.15% | 29.06% | 66.67% | 5.93% | 35.62% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -5.89% | -15.62% | 6.07% | 100.00% | 26.02% | 83.19% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 10 | 30.00% | -6.61% | -15.77% | 5.11% | 30.00% | -12.10% | 20.02% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 22 | 86.36% | 10.38% | -4.18% | 43.78% | 72.73% | 9.73% | 55.18% |
| BTC-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 18.22% | -7.40% | 42.56% | 62.50% | 16.74% | 59.61% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.22% | -5.61% | 18.22% | 100.00% | 29.43% | 32.77% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 3 | 66.67% | 33.93% | -4.48% | 45.34% | 66.67% | 9.42% | 72.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -3.90% | -16.17% | 6.14% | 16.67% | -13.29% | 11.43% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 28 | 71.43% | 6.92% | -6.21% | 31.70% | 85.71% | 26.16% | 60.21% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 14.56% | -6.27% | 42.27% | 75.00% | 17.02% | 76.21% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 8 | 25.00% | -12.55% | -18.75% | 20.39% | 37.50% | -8.68% | 29.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 64.29% | 5.81% | -8.18% | 19.47% | 71.43% | 4.00% | 54.79% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -19.37% | -24.60% | 2.76% | 50.00% | -23.81% | 2.76% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 30.90% | -1.74% | 30.90% | 100.00% | 35.13% | 47.19% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 3 | 66.67% | 33.93% | -4.48% | 45.34% | 66.67% | 9.42% | 72.39% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 83.33% | 4.44% | -8.29% | 29.06% | 66.67% | 7.66% | 35.62% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 91.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | XRP-USD | 2019-10-09 | 89.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | ONE-USD | 2020-01-27 | 88.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| BTC-USD | BTC-USD | 2018-10-04 | 87.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.08% | -7.81% | 1.12% | 6.01% | -7.81% | 12.34% |
| BTC-USD | XRP-USD | 2025-12-21 | 86.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | -0.53% | 11.68% | 0.43% | -1.24% | 12.21% |
| BTC-USD | APT-USD | 2024-09-16 | 86.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.47% | -29.47% | 7.73% | -30.92% | -30.92% | 7.73% |
| BTC-USD | BNB-USD | 2025-12-21 | 86.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| BTC-USD | ETH-USD | 2025-12-21 | 86.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.36% | 0.00% | 19.65% | -0.57% | -0.79% | 19.65% |
| BTC-USD | BNB-USD | 2018-10-04 | 85.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | BTC-USD | 2025-12-21 | 85.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.62% | 0.00% | 17.94% | 10.02% | 0.00% | 23.16% |
| DOGE-USD | DASH-USD | 2022-03-07 | 89.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | OP-USD | 2025-12-22 | 89.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | MKR-USD | 2022-09-24 | 89.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.72% | -1.56% | 39.59% | 72.17% | -1.56% | 80.88% |
| DOGE-USD | VET-USD | 2022-03-14 | 88.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.68% | -8.95% | 11.10% | 9.39% | -8.95% | 41.71% |
| DOGE-USD | RUNE-USD | 2022-03-08 | 88.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -22.98% | 22.31% | 37.54% | -22.98% | 46.15% |
| DOGE-USD | LTC-USD | 2018-04-12 | 88.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.99% | -34.14% | 7.89% | -34.63% | -37.58% | 7.89% |
| DOGE-USD | INJ-USD | 2022-03-09 | 88.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.67% | -13.24% | 7.61% | 32.39% | -13.24% | 54.99% |
| DOGE-USD | OMG-USD | 2022-03-07 | 88.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.54% | -14.76% | 5.54% | 24.58% | -14.76% | 24.58% |
| DOGE-USD | XRP-USD | 2019-10-04 | 88.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| DOGE-USD | AVAX-USD | 2022-03-13 | 88.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 37.69% | -6.20% | 44.34% | 31.22% | -6.20% | 71.22% |
| SOL-USD | RUNE-USD | 2025-12-22 | 80.06% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.64% | -8.40% | 23.46% | 3.30% | -8.40% | 52.16% |
| SOL-USD | SOL-USD | 2025-12-19 | 79.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | ENJ-USD | 2018-10-04 | 78.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -12.02% | -26.93% | 5.36% | 445.37% | -26.93% | 526.80% |
| SOL-USD | BNB-USD | 2025-12-21 | 78.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | ZIL-USD | 2018-10-06 | 77.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.19% | -10.59% | 26.39% | -0.95% | -11.40% | 26.39% |
| SOL-USD | KAVA-USD | 2025-12-21 | 77.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.72% | -7.96% | 14.26% | 2.51% | -7.96% | 24.10% |
| SOL-USD | NEAR-USD | 2025-12-16 | 77.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.14% | -9.23% | 12.11% | 87.14% | -9.23% | 91.97% |
| SOL-USD | EOS-USD | 2018-10-19 | 76.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.40% | -7.62% | 75.20% | 77.34% | -7.62% | 77.34% |
| SOL-USD | BTC-USD | 2025-12-21 | 76.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.62% | 0.00% | 17.94% | 10.02% | 0.00% | 23.16% |
| SOL-USD | DOT-USD | 2025-12-16 | 76.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.88% | -14.40% | 0.00% | -8.57% | -14.40% | 1.55% |

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

