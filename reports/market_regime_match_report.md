# Market Regime Match Report

Generated: 2026-07-25 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.091 $ | False | -18.52% | -9.79% | BEAR | -18.52% | -9.79% |
| DOGE-USD | BEAR | 0.06958 $ | False | -29.98% | -15.99% | BEAR | -18.52% | -9.79% |
| SOL-USD | BEAR | 74,20 $ | False | -14.71% | -16.64% | BEAR | -18.52% | -9.79% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 65.00% | 15.63% | 23.70% | 40.31% | -8.42% | -24.90% | 17.50% | 28.55% | 53.59% | 57.50% | 11.59% | 45.47% | 59.06% |
| BTC-USD | SAME_BTC_REGIME | 9 | 77.78% | 16.66% | 35.30% | 56.25% | -6.98% | -16.93% | 18.60% | 51.62% | 90.68% | 55.56% | 11.07% | 57.00% | 170.38% |
| BTC-USD | SAME_ASSET_REGIME | 18 | 88.89% | 23.14% | 33.65% | 44.70% | -6.69% | -11.76% | 23.14% | 39.47% | 58.57% | 72.22% | 36.83% | 49.39% | 86.73% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 9 | 77.78% | 16.66% | 35.30% | 56.25% | -6.98% | -16.93% | 18.60% | 51.62% | 90.68% | 55.56% | 11.07% | 57.00% | 170.38% |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 1.28% | 12.46% | 27.88% | -11.73% | -29.10% | 14.80% | 22.36% | 32.82% | 80.00% | 26.27% | 42.38% | 57.40% |
| DOGE-USD | SAME_BTC_REGIME | 31 | 61.29% | 3.44% | 15.22% | 29.37% | -8.31% | -22.98% | 15.54% | 25.36% | 33.33% | 87.10% | 28.36% | 45.97% | 60.08% |
| DOGE-USD | SAME_ASSET_REGIME | 32 | 59.38% | 2.73% | 15.88% | 29.21% | -7.83% | -22.96% | 16.81% | 24.58% | 33.27% | 87.50% | 29.44% | 49.00% | 59.78% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 30 | 60.00% | 2.73% | 15.33% | 29.70% | -7.83% | -23.57% | 15.92% | 26.14% | 33.95% | 86.67% | 29.44% | 47.52% | 61.29% |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 5.22% | 20.99% | 44.69% | -8.66% | -19.35% | 9.99% | 26.66% | 47.28% | 70.00% | 4.55% | 20.62% | 66.47% |
| SOL-USD | SAME_BTC_REGIME | 22 | 68.18% | 4.57% | 25.90% | 45.65% | -8.86% | -21.38% | 13.19% | 27.34% | 51.14% | 81.82% | 4.55% | 48.30% | 105.69% |
| SOL-USD | SAME_ASSET_REGIME | 26 | 65.38% | 4.57% | 25.90% | 48.04% | -8.92% | -20.37% | 11.25% | 27.34% | 59.12% | 76.92% | 4.55% | 48.30% | 75.66% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 21 | 66.67% | 3.42% | 20.64% | 35.30% | -9.23% | -21.63% | 12.11% | 26.39% | 51.62% | 80.95% | 3.56% | 27.94% | 87.14% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 9 | 77.78% | 16.66% | -6.98% | 51.62% | 55.56% | 11.07% | 153.58% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 65.22% | 18.22% | -7.67% | 29.18% | 69.57% | 30.21% | 56.06% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 50.00% | -0.26% | -11.20% | 14.65% | 25.00% | -9.32% | 16.30% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 31 | 61.29% | 3.44% | -8.31% | 25.36% | 87.10% | 28.36% | 60.25% |
| DOGE-USD | HISTORICAL_BTC_BULL | 3 | 66.67% | 7.79% | -10.05% | 21.80% | 66.67% | 27.74% | 45.50% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -20.98% | -23.66% | 13.78% | 50.00% | 7.58% | 33.57% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 68.18% | 4.57% | -8.86% | 27.34% | 81.82% | 4.55% | 89.32% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 6.90% | -8.33% | 33.74% | 85.71% | 15.36% | 52.17% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 11 | 63.64% | 4.16% | -8.83% | 17.06% | 36.36% | -8.97% | 24.61% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 18 | 88.89% | 23.14% | -6.69% | 39.47% | 72.22% | 36.83% | 57.69% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 36.36% | -3.90% | -17.11% | 25.63% | 54.55% | 5.32% | 50.90% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 29.19% | -6.62% | 44.46% | 100.00% | 35.07% | 48.10% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -37.22% | -39.28% | 4.09% | 0.00% | -36.70% | 4.09% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 50.00% | -0.26% | -11.20% | 14.65% | 25.00% | -9.32% | 16.30% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 59.38% | 2.73% | -7.83% | 24.58% | 87.50% | 29.44% | 60.21% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 4.00% | -20.28% | 15.50% | 100.00% | 24.07% | 45.66% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 5 | 20.00% | -17.99% | -19.91% | 13.28% | 20.00% | -19.65% | 13.94% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 26 | 65.38% | 4.57% | -8.92% | 27.34% | 76.92% | 4.55% | 77.15% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -3.92% | -10.22% | 13.20% | 66.67% | 1.29% | 21.59% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 19.99% | -1.20% | 24.50% | 100.00% | 42.40% | 47.99% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -12.42% | -12.78% | 2.93% | 0.00% | -11.30% | 2.93% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 9 | 88.89% | 6.78% | -8.22% | 27.47% | 55.56% | 6.05% | 30.23% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 91.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | XRP-USD | 2019-10-09 | 90.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | BTC-USD | 2018-10-02 | 87.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.13% | -15.76% | 0.00% | -2.07% | -15.76% | 2.66% |
| BTC-USD | ETH-USD | 2025-12-16 | 86.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -8.55% | 11.67% | -3.23% | -8.55% | 11.67% |
| BTC-USD | OMG-USD | 2018-10-04 | 86.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.64% | -21.63% | 0.39% | 11.07% | -21.63% | 11.07% |
| BTC-USD | XRP-USD | 2025-12-16 | 85.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.37% | -6.98% | 4.44% | -4.54% | -6.98% | 4.94% |
| BTC-USD | BTC-USD | 2025-12-19 | 85.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.66% | -0.55% | 18.60% | 12.10% | -0.55% | 23.85% |
| BTC-USD | BNB-USD | 2018-10-04 | 85.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | THETA-USD | 2018-10-03 | 85.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 74.78% | -1.48% | 74.78% | 237.54% | -1.48% | 314.58% |
| BTC-USD | SAND-USD | 2023-06-29 | 89.35% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 24.82% | -6.32% | 24.82% | 49.53% | -6.32% | 49.53% |
| DOGE-USD | DASH-USD | 2022-03-07 | 90.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | OP-USD | 2025-12-17 | 89.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.02% | -6.29% | 23.81% | 19.12% | -6.29% | 58.54% |
| DOGE-USD | VET-USD | 2022-03-09 | 89.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.43% | -5.37% | 15.47% | 38.55% | -5.37% | 47.28% |
| DOGE-USD | THETA-USD | 2022-03-11 | 88.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.61% | -6.22% | 26.91% | 19.72% | -6.22% | 43.44% |
| DOGE-USD | MKR-USD | 2022-09-24 | 88.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.72% | -1.56% | 39.59% | 72.17% | -1.56% | 80.88% |
| DOGE-USD | OMG-USD | 2022-03-07 | 88.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.54% | -14.76% | 5.54% | 24.58% | -14.76% | 24.58% |
| DOGE-USD | QTUM-USD | 2022-03-07 | 88.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -0.80% | -6.74% | 13.36% | 54.57% | -6.74% | 68.52% |
| DOGE-USD | INJ-USD | 2022-03-09 | 88.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.67% | -13.24% | 7.61% | 32.39% | -13.24% | 54.99% |
| DOGE-USD | ENJ-USD | 2022-03-12 | 88.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.33% | 0.00% | 41.33% | 40.13% | 0.00% | 60.33% |
| DOGE-USD | LTC-USD | 2022-03-05 | 88.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.42% | -10.22% | 22.27% | 28.36% | -10.22% | 31.59% |
| SOL-USD | ENJ-USD | 2018-10-04 | 81.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -12.02% | -26.93% | 5.36% | 445.37% | -26.93% | 526.80% |
| SOL-USD | QTUM-USD | 2018-10-04 | 80.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.14% | -19.10% | 3.33% | -0.16% | -19.10% | 10.72% |
| SOL-USD | NEAR-USD | 2025-12-16 | 80.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.14% | -9.23% | 12.11% | 87.14% | -9.23% | 91.97% |
| SOL-USD | RUNE-USD | 2025-12-22 | 79.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.64% | -8.40% | 23.46% | 3.30% | -8.40% | 52.16% |
| SOL-USD | BNB-USD | 2025-12-21 | 78.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | LINK-USD | 2025-12-16 | 78.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.03% | -10.34% | 2.67% | 0.58% | -10.34% | 14.27% |
| SOL-USD | SOL-USD | 2025-12-19 | 78.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | LRC-USD | 2018-10-04 | 78.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| SOL-USD | APT-USD | 2024-09-16 | 77.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.47% | -29.47% | 7.73% | -30.92% | -30.92% | 7.73% |
| SOL-USD | ZIL-USD | 2018-10-06 | 77.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.19% | -10.59% | 26.39% | -0.95% | -11.40% | 26.39% |

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

