# Market Regime Match Report

Generated: 2026-07-21 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 65.472 $ | False | -16.27% | -9.73% | BEAR | -16.27% | -9.73% |
| DOGE-USD | BEAR | 0.07277 $ | False | -23.94% | -15.64% | BEAR | -16.27% | -9.73% |
| SOL-USD | BEAR | 78,18 $ | False | -10.02% | -16.70% | BEAR | -16.27% | -9.73% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 5.34% | 22.32% | 27.56% | -11.17% | -29.34% | 12.14% | 23.05% | 32.21% | 60.00% | 7.92% | 34.47% | 78.22% |
| BTC-USD | SAME_BTC_REGIME | 4 | 75.00% | 17.45% | 29.38% | 29.40% | -8.78% | -10.66% | 23.06% | 35.92% | 40.58% | 50.00% | -0.17% | 8.00% | 19.96% |
| BTC-USD | SAME_ASSET_REGIME | 18 | 88.89% | 21.58% | 23.24% | 29.39% | -10.00% | -13.09% | 22.19% | 26.20% | 36.44% | 77.78% | 29.98% | 44.79% | 57.68% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 100.00% | 29.37% | 29.40% | 29.41% | -7.64% | -10.31% | 33.33% | 38.51% | 41.62% | 33.33% | -1.70% | 13.12% | 22.01% |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -12.28% | 9.88% | 26.56% | -20.97% | -37.07% | 11.92% | 23.40% | 31.64% | 67.50% | 8.67% | 41.29% | 72.43% |
| DOGE-USD | SAME_BTC_REGIME | 30 | 33.33% | -13.63% | 9.49% | 19.66% | -22.47% | -37.07% | 1.04% | 21.78% | 29.33% | 70.00% | 7.11% | 42.84% | 65.48% |
| DOGE-USD | SAME_ASSET_REGIME | 32 | 31.25% | -13.63% | 8.91% | 18.64% | -22.47% | -36.57% | 1.38% | 21.66% | 28.95% | 71.88% | 8.67% | 41.29% | 71.42% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 29 | 31.03% | -13.83% | 8.62% | 15.82% | -23.04% | -37.42% | 0.00% | 17.32% | 28.06% | 68.97% | 7.07% | 40.52% | 66.22% |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 0.70% | 12.29% | 17.42% | -9.63% | -23.41% | 9.69% | 19.83% | 27.74% | 57.50% | 2.52% | 22.14% | 44.32% |
| SOL-USD | SAME_BTC_REGIME | 12 | 50.00% | 0.18% | 9.38% | 12.50% | -8.84% | -23.16% | 5.73% | 10.00% | 12.50% | 66.67% | 2.52% | 8.80% | 9.82% |
| SOL-USD | SAME_ASSET_REGIME | 23 | 65.22% | 1.17% | 14.12% | 20.53% | -7.77% | -22.97% | 9.67% | 20.23% | 26.49% | 60.87% | 3.69% | 16.44% | 41.76% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 60.00% | 0.87% | 10.45% | 13.26% | -7.66% | -22.41% | 7.41% | 10.66% | 13.41% | 70.00% | 5.72% | 8.95% | 11.08% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 4 | 75.00% | 17.45% | -8.78% | 35.92% | 50.00% | -0.17% | 67.06% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 65.22% | 9.93% | -11.54% | 23.14% | 65.22% | 25.46% | 53.73% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 13 | 46.15% | -5.27% | -11.49% | 19.23% | 53.85% | 1.53% | 29.68% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 33.33% | -13.63% | -22.47% | 21.78% | 70.00% | 7.11% | 57.36% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 50.00% | 12.63% | -6.01% | 31.53% | 66.67% | 33.05% | 78.26% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 0.00% | -21.59% | -24.05% | 16.43% | 50.00% | 7.36% | 22.20% |
| SOL-USD | HISTORICAL_BTC_BEAR | 12 | 50.00% | 0.18% | -8.84% | 10.00% | 66.67% | 2.52% | 19.92% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 33.33% | -6.67% | -13.82% | 19.76% | 55.56% | 5.32% | 36.59% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -16.48% | -17.11% | 2.98% | 0.00% | -21.33% | 2.98% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 18 | 66.67% | 4.77% | -7.43% | 24.14% | 55.56% | 6.05% | 45.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 18 | 88.89% | 21.58% | -10.00% | 26.20% | 77.78% | 29.98% | 74.78% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 40.00% | -11.28% | -20.62% | 22.15% | 40.00% | -4.58% | 27.06% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -40.58% | -42.28% | 0.00% | 0.00% | -45.29% | 0.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -5.91% | -10.83% | 18.12% | 50.00% | 0.06% | 27.05% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 31.25% | -13.63% | -22.47% | 21.66% | 71.88% | 8.67% | 56.31% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 10.33% | -9.05% | 34.69% | 75.00% | 29.15% | 74.17% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 38.17% | -2.98% | 38.17% | 100.00% | 47.83% | 82.05% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 0.00% | -13.13% | -15.94% | 17.58% | 0.00% | -14.97% | 17.58% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 23 | 65.22% | 1.17% | -7.77% | 20.23% | 60.87% | 3.69% | 34.77% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 0.00% | -10.50% | -16.47% | 12.23% | 50.00% | 2.50% | 24.30% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 12.15% | -0.77% | 25.06% | 100.00% | 36.30% | 41.07% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 11 | 45.45% | -6.67% | -9.34% | 16.45% | 45.45% | -6.89% | 40.64% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-04 | 90.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| BTC-USD | ETH-USD | 2025-12-11 | 85.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -7.64% | 12.79% | -1.70% | -7.64% | 12.79% |
| BTC-USD | MKR-USD | 2020-01-23 | 84.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.42% | -10.98% | 43.69% | 27.94% | -10.98% | 94.10% |
| BTC-USD | BNB-USD | 2025-12-16 | 85.29% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.69% | -9.92% | 0.00% | 1.35% | -9.92% | 4.73% |
| BTC-USD | LRC-USD | 2018-09-29 | 91.57% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.04% | -13.46% | 133.38% | 29.74% | -13.46% | 133.38% |
| BTC-USD | FIL-USD | 2023-06-29 | 88.82% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 23.33% | -4.87% | 23.33% | 43.44% | -4.87% | 56.53% |
| BTC-USD | SAND-USD | 2023-06-24 | 88.52% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 7.39% | -12.66% | 11.30% | 26.71% | -12.66% | 37.05% |
| BTC-USD | APT-USD | 2024-05-27 | 87.04% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -1.32% | -3.95% | 7.11% | -53.95% | -53.95% | 7.11% |
| BTC-USD | OMG-USD | 2018-09-29 | 86.36% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -31.70% | -31.70% | 0.00% | -21.19% | -35.29% | 0.00% |
| BTC-USD | ETC-USD | 2023-06-25 | 85.86% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 9.93% | -8.65% | 9.93% | 17.30% | -8.65% | 28.49% |
| DOGE-USD | DASH-USD | 2022-03-02 | 90.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.14% | -27.85% | 0.00% | -2.98% | -30.72% | 0.00% |
| DOGE-USD | INJ-USD | 2022-03-04 | 88.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.36% | -35.14% | 0.00% | 0.31% | -36.02% | 0.31% |
| DOGE-USD | VET-USD | 2022-03-04 | 88.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.06% | -21.27% | 0.00% | 18.68% | -22.08% | 18.68% |
| DOGE-USD | QTUM-USD | 2022-03-02 | 88.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.26% | -33.72% | 0.00% | 6.79% | -33.72% | 19.77% |
| DOGE-USD | 1INCH-USD | 2022-03-04 | 88.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -14.71% | -20.68% | 8.97% | 26.51% | -20.68% | 26.51% |
| DOGE-USD | ENJ-USD | 2022-03-07 | 88.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.19% | -8.90% | 29.08% | 54.45% | -8.90% | 55.79% |
| DOGE-USD | THETA-USD | 2022-03-06 | 88.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.29% | -5.56% | 27.80% | 40.52% | -5.56% | 44.44% |
| DOGE-USD | OMG-USD | 2022-03-02 | 88.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.92% | -36.72% | 0.00% | -11.78% | -39.47% | 0.00% |
| DOGE-USD | XRP-USD | 2019-09-29 | 87.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| DOGE-USD | CHZ-USD | 2022-03-06 | 87.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 8.62% | -7.36% | 16.30% | 74.78% | -7.36% | 74.78% |
| SOL-USD | RUNE-USD | 2025-12-17 | 79.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.50% | -7.03% | 20.04% | 9.91% | -7.03% | 54.43% |
| SOL-USD | SOL-USD | 2025-12-14 | 78.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.93% | -13.64% | 0.31% | -7.78% | -13.64% | 6.48% |
| SOL-USD | NEAR-USD | 2025-12-11 | 78.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.92% | -11.77% | 8.98% | 21.58% | -11.77% | 23.26% |
| SOL-USD | LINK-USD | 2025-12-11 | 77.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.47% | -7.77% | 5.62% | 3.69% | -7.77% | 17.55% |
| SOL-USD | KAVA-USD | 2025-12-16 | 77.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.67% | -7.55% | 12.67% | 9.02% | -7.55% | 24.66% |
| SOL-USD | BTC-USD | 2025-12-15 | 76.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.99% | -6.47% | 10.99% | 8.73% | -6.47% | 16.48% |
| SOL-USD | AVAX-USD | 2025-12-12 | 76.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.82% | -6.61% | 5.84% | 0.86% | -6.61% | 11.16% |
| SOL-USD | APT-USD | 2024-09-11 | 76.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.26% | -23.26% | 3.72% | -33.02% | -33.49% | 3.72% |
| SOL-USD | OMG-USD | 2025-12-16 | 76.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.84% | -4.58% | 9.67% | 7.75% | -4.58% | 18.81% |
| SOL-USD | DOT-USD | 2025-12-11 | 75.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.31% | -22.31% | 0.00% | -18.37% | -22.31% | 0.00% |

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

