# Market Regime Match Report

Generated: 2026-07-22 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 66.220 $ | False | -15.39% | -9.73% | BEAR | -15.39% | -9.73% |
| DOGE-USD | BEAR | 0.07317 $ | False | -24.72% | -15.72% | BEAR | -15.39% | -9.73% |
| SOL-USD | BEAR | 77,84 $ | False | -9.67% | -16.69% | BEAR | -15.39% | -9.73% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 9.39% | 23.31% | 29.38% | -10.52% | -23.79% | 16.52% | 25.39% | 30.60% | 60.00% | 14.13% | 41.71% | 80.46% |
| BTC-USD | SAME_BTC_REGIME | 5 | 60.00% | 6.81% | 29.37% | 29.40% | -9.92% | -10.60% | 11.67% | 33.33% | 39.55% | 40.00% | -1.77% | 1.35% | 17.30% |
| BTC-USD | SAME_ASSET_REGIME | 21 | 80.95% | 22.48% | 27.01% | 29.42% | -9.96% | -13.46% | 22.59% | 29.45% | 33.33% | 76.19% | 30.21% | 48.98% | 81.89% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 4 | 75.00% | 18.09% | 29.38% | 29.40% | -9.29% | -10.70% | 22.50% | 35.92% | 40.58% | 25.00% | -2.50% | 5.66% | 19.03% |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -7.77% | 9.88% | 25.38% | -20.48% | -37.18% | 14.24% | 21.66% | 30.01% | 72.50% | 7.31% | 39.04% | 72.43% |
| DOGE-USD | SAME_BTC_REGIME | 30 | 40.00% | -8.65% | 9.55% | 19.66% | -21.29% | -37.18% | 11.25% | 21.78% | 29.33% | 76.67% | 7.31% | 40.03% | 65.48% |
| DOGE-USD | SAME_ASSET_REGIME | 32 | 40.62% | -4.85% | 10.25% | 24.64% | -19.59% | -36.67% | 14.24% | 23.40% | 29.76% | 78.12% | 10.48% | 41.29% | 71.42% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 29 | 37.93% | -8.77% | 9.78% | 20.28% | -21.90% | -37.52% | 8.97% | 23.26% | 29.58% | 75.86% | 7.14% | 40.52% | 66.22% |
| SOL-USD | ALL_MATCHES | 40 | 47.50% | -0.93% | 8.84% | 17.75% | -9.63% | -25.09% | 8.85% | 16.65% | 27.33% | 55.00% | 1.11% | 12.39% | 30.27% |
| SOL-USD | SAME_BTC_REGIME | 15 | 46.67% | -0.47% | 8.73% | 16.17% | -9.92% | -25.40% | 5.84% | 9.71% | 17.09% | 66.67% | 3.69% | 9.47% | 17.38% |
| SOL-USD | SAME_ASSET_REGIME | 23 | 56.52% | 0.82% | 10.76% | 17.79% | -7.77% | -22.18% | 8.30% | 16.35% | 26.11% | 56.52% | 0.86% | 10.49% | 28.11% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 13 | 53.85% | 0.82% | 8.84% | 17.34% | -7.77% | -22.18% | 7.73% | 9.76% | 18.57% | 69.23% | 7.75% | 9.91% | 19.48% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 5 | 60.00% | 6.81% | -9.92% | 33.33% | 40.00% | -1.77% | 58.05% |
| BTC-USD | HISTORICAL_BTC_BULL | 22 | 68.18% | 22.30% | -10.00% | 26.54% | 72.73% | 34.39% | 61.78% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 13 | 46.15% | -3.96% | -12.93% | 19.23% | 46.15% | -4.05% | 29.68% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 40.00% | -8.65% | -21.29% | 21.78% | 76.67% | 7.31% | 54.63% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 14.72% | -6.83% | 29.83% | 80.00% | 32.77% | 80.30% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 0.00% | -23.97% | -27.41% | 18.96% | 40.00% | -5.22% | 19.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 15 | 46.67% | -0.47% | -9.92% | 9.71% | 66.67% | 3.69% | 21.04% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 22.22% | -6.67% | -13.82% | 16.09% | 44.44% | -0.32% | 34.24% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -16.48% | -17.11% | 2.98% | 0.00% | -21.33% | 2.98% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 15 | 66.67% | 5.16% | -7.41% | 24.34% | 53.33% | 0.80% | 36.72% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 21 | 80.95% | 22.48% | -9.96% | 29.45% | 76.19% | 30.21% | 78.53% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 33.33% | -16.23% | -22.79% | 16.23% | 44.44% | -9.67% | 40.34% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 44.44% | -3.96% | -11.34% | 18.56% | 33.33% | -4.18% | 29.65% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 40.62% | -4.85% | -19.59% | 23.40% | 78.12% | 10.48% | 56.31% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 8.87% | -20.28% | 22.81% | 100.00% | 19.94% | 64.95% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 5 | 0.00% | -13.13% | -24.85% | 18.96% | 20.00% | -14.97% | 18.96% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 23 | 56.52% | 0.82% | -7.77% | 16.35% | 56.52% | 0.86% | 25.97% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 20.00% | -8.48% | -14.33% | 19.76% | 60.00% | 5.32% | 34.24% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 11 | 45.45% | -6.67% | -9.34% | 16.45% | 45.45% | -6.89% | 36.72% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-04 | 89.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| BTC-USD | MKR-USD | 2020-01-23 | 86.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.42% | -10.98% | 43.69% | 27.94% | -10.98% | 94.10% |
| BTC-USD | ETH-USD | 2025-12-16 | 85.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -8.55% | 11.67% | -3.23% | -8.55% | 11.67% |
| BTC-USD | WAVES-USD | 2025-12-16 | 84.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.09% | -10.03% | 0.00% | -8.67% | -15.86% | 0.00% |
| BTC-USD | BNB-USD | 2025-12-16 | 85.38% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.69% | -9.92% | 0.00% | 1.35% | -9.92% | 4.73% |
| BTC-USD | LRC-USD | 2018-09-29 | 91.36% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.04% | -13.46% | 133.38% | 29.74% | -13.46% | 133.38% |
| BTC-USD | FIL-USD | 2023-06-29 | 89.17% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 23.33% | -4.87% | 23.33% | 43.44% | -4.87% | 56.53% |
| BTC-USD | SAND-USD | 2023-06-29 | 88.99% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 24.82% | -6.32% | 24.82% | 49.53% | -6.32% | 49.53% |
| BTC-USD | APT-USD | 2024-05-27 | 87.65% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -1.32% | -3.95% | 7.11% | -53.95% | -53.95% | 7.11% |
| BTC-USD | MATIC-USD | 2023-06-30 | 86.46% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 30.44% | -9.96% | 30.44% | 45.24% | -9.96% | 63.53% |
| DOGE-USD | DASH-USD | 2022-03-02 | 89.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.14% | -27.85% | 0.00% | -2.98% | -30.72% | 0.00% |
| DOGE-USD | INJ-USD | 2022-03-04 | 89.06% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.36% | -35.14% | 0.00% | 0.31% | -36.02% | 0.31% |
| DOGE-USD | OP-USD | 2025-12-17 | 89.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.02% | -6.29% | 23.81% | 19.12% | -6.29% | 58.54% |
| DOGE-USD | 1INCH-USD | 2022-03-04 | 88.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -14.71% | -20.68% | 8.97% | 26.51% | -20.68% | 26.51% |
| DOGE-USD | ENJ-USD | 2022-03-07 | 88.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.19% | -8.90% | 29.08% | 54.45% | -8.90% | 55.79% |
| DOGE-USD | VET-USD | 2022-03-09 | 88.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.43% | -5.37% | 15.47% | 38.55% | -5.37% | 47.28% |
| DOGE-USD | THETA-USD | 2022-03-06 | 88.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.29% | -5.56% | 27.80% | 40.52% | -5.56% | 44.44% |
| DOGE-USD | LTC-USD | 2022-03-02 | 87.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.06% | -28.09% | 0.00% | 3.95% | -28.09% | 5.39% |
| DOGE-USD | OMG-USD | 2022-03-07 | 87.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.54% | -14.76% | 5.54% | 24.58% | -14.76% | 24.58% |
| DOGE-USD | XRP-USD | 2019-09-29 | 87.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| SOL-USD | RUNE-USD | 2025-12-17 | 79.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.50% | -7.03% | 20.04% | 9.91% | -7.03% | 54.43% |
| SOL-USD | QTUM-USD | 2018-10-04 | 79.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.14% | -19.10% | 3.33% | -0.16% | -19.10% | 10.72% |
| SOL-USD | SOL-USD | 2025-12-14 | 78.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.93% | -13.64% | 0.31% | -7.78% | -13.64% | 6.48% |
| SOL-USD | NEAR-USD | 2025-12-11 | 77.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.92% | -11.77% | 8.98% | 21.58% | -11.77% | 23.26% |
| SOL-USD | BTC-USD | 2025-12-16 | 76.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.62% | -7.51% | 9.76% | 7.95% | -7.51% | 15.19% |
| SOL-USD | APT-USD | 2024-09-16 | 76.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.47% | -29.47% | 7.73% | -30.92% | -30.92% | 7.73% |
| SOL-USD | LINK-USD | 2025-12-11 | 76.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.47% | -7.77% | 5.62% | 3.69% | -7.77% | 17.55% |
| SOL-USD | EOS-USD | 2018-10-14 | 76.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 66.62% | -4.37% | 66.62% | 55.08% | -4.37% | 81.36% |
| SOL-USD | KAVA-USD | 2025-12-16 | 76.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.67% | -7.55% | 12.67% | 9.02% | -7.55% | 24.66% |
| SOL-USD | DOT-USD | 2025-12-11 | 76.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.31% | -22.31% | 0.00% | -18.37% | -22.31% | 0.00% |

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

