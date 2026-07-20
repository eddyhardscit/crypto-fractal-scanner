# Market Regime Match Report

Generated: 2026-07-20 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.150 $ | False | -15.95% | -9.76% | BEAR | -15.95% | -9.76% |
| DOGE-USD | BEAR | 0.07174 $ | False | -24.54% | -15.64% | BEAR | -15.95% | -9.76% |
| SOL-USD | BEAR | 75,92 $ | False | -11.70% | -16.80% | BEAR | -15.95% | -9.76% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 6.46% | 17.31% | 26.50% | -11.43% | -31.88% | 13.01% | 22.39% | 32.21% | 55.00% | 1.83% | 27.49% | 51.72% |
| BTC-USD | SAME_BTC_REGIME | 3 | 100.00% | 17.36% | 23.37% | 26.97% | -7.64% | -11.12% | 26.83% | 30.08% | 32.03% | 0.00% | -1.77% | -1.74% | -1.72% |
| BTC-USD | SAME_ASSET_REGIME | 19 | 84.21% | 14.72% | 21.68% | 27.02% | -8.65% | -12.82% | 15.79% | 25.00% | 37.26% | 68.42% | 26.71% | 37.67% | 66.14% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 100.00% | 17.36% | 23.37% | 26.97% | -7.64% | -11.12% | 26.83% | 30.08% | 32.03% | 0.00% | -1.77% | -1.74% | -1.72% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -13.34% | 6.29% | 21.91% | -22.47% | -40.44% | 8.73% | 17.35% | 29.15% | 65.00% | 8.39% | 34.56% | 55.48% |
| DOGE-USD | SAME_BTC_REGIME | 30 | 30.00% | -14.27% | 7.84% | 21.91% | -25.63% | -40.44% | 0.00% | 16.61% | 29.39% | 70.00% | 8.39% | 37.89% | 55.48% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 33.33% | -13.83% | 8.62% | 20.17% | -23.04% | -39.54% | 2.09% | 16.72% | 28.82% | 69.70% | 9.63% | 39.94% | 62.68% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 28 | 28.57% | -15.93% | 6.29% | 13.76% | -25.63% | -40.84% | 0.00% | 16.40% | 28.18% | 67.86% | 6.97% | 32.89% | 57.53% |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | 0.06% | 11.66% | 17.42% | -10.16% | -23.41% | 9.35% | 17.39% | 27.95% | 60.00% | 2.52% | 18.50% | 37.90% |
| SOL-USD | SAME_BTC_REGIME | 13 | 46.15% | -0.47% | 10.28% | 12.39% | -10.49% | -23.07% | 5.62% | 10.28% | 12.66% | 69.23% | 1.35% | 6.53% | 9.73% |
| SOL-USD | SAME_ASSET_REGIME | 23 | 65.22% | 1.17% | 12.08% | 17.69% | -10.07% | -22.97% | 8.98% | 18.32% | 26.11% | 65.22% | 3.69% | 10.60% | 28.11% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 54.55% | 0.82% | 10.78% | 12.67% | -10.49% | -22.31% | 5.84% | 11.44% | 12.67% | 72.73% | 3.69% | 7.78% | 9.91% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 3 | 100.00% | 17.36% | -7.64% | 30.08% | 0.00% | -1.77% | 42.44% |
| BTC-USD | HISTORICAL_BTC_BULL | 24 | 62.50% | 9.10% | -11.53% | 22.05% | 62.50% | 20.86% | 51.48% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 13 | 46.15% | -6.55% | -11.34% | 21.45% | 53.85% | 1.00% | 26.94% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 30.00% | -14.27% | -25.63% | 16.61% | 70.00% | 8.39% | 50.04% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 2.30% | -10.51% | 22.98% | 60.00% | 32.77% | 44.20% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 0.00% | -18.14% | -23.06% | 16.38% | 40.00% | -5.22% | 19.94% |
| SOL-USD | HISTORICAL_BTC_BEAR | 13 | 46.15% | -0.47% | -10.49% | 10.28% | 69.23% | 1.35% | 19.29% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 33.33% | -6.67% | -11.54% | 11.50% | 55.56% | 5.32% | 24.73% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -16.48% | -17.11% | 2.98% | 0.00% | -21.33% | 2.98% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 17 | 64.71% | 4.38% | -7.45% | 25.06% | 58.82% | 11.29% | 74.37% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 19 | 84.21% | 14.72% | -8.65% | 25.00% | 68.42% | 26.71% | 63.22% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 40.00% | -11.28% | -20.62% | 22.15% | 40.00% | -4.58% | 27.06% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -37.64% | -38.49% | 4.08% | 0.00% | -41.73% | 4.08% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 44.44% | -6.55% | -10.62% | 18.56% | 55.56% | 1.00% | 19.23% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 33.33% | -13.83% | -23.04% | 16.72% | 69.70% | 9.63% | 46.69% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -23.86% | -27.55% | 8.37% | 50.00% | -1.55% | 16.96% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 12.46% | -17.87% | 28.63% | 100.00% | 36.02% | 68.19% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 0.00% | -13.13% | -15.94% | 17.58% | 0.00% | -14.97% | 17.58% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 23 | 65.22% | 1.17% | -10.07% | 18.32% | 65.22% | 3.69% | 26.01% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 0.00% | -10.50% | -16.47% | 12.23% | 50.00% | 2.50% | 24.30% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 4.99% | -4.53% | 20.78% | 100.00% | 34.99% | 85.23% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -8.01% | -10.44% | 15.36% | 40.00% | -4.62% | 44.19% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-04 | 90.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| BTC-USD | ETH-USD | 2025-12-11 | 85.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -7.64% | 12.79% | -1.70% | -7.64% | 12.79% |
| BTC-USD | KSM-USD | 2022-03-20 | 84.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 17.36% | -11.99% | 26.83% | -16.23% | -16.23% | 26.83% |
| BTC-USD | LRC-USD | 2018-09-29 | 90.91% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.04% | -13.46% | 133.38% | 29.74% | -13.46% | 133.38% |
| BTC-USD | SAND-USD | 2023-06-24 | 89.08% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 7.39% | -12.66% | 11.30% | 26.71% | -12.66% | 37.05% |
| BTC-USD | FIL-USD | 2023-06-24 | 88.41% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 10.53% | -8.25% | 11.57% | 26.74% | -8.25% | 50.97% |
| BTC-USD | EOS-USD | 2023-06-25 | 87.29% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 11.50% | -8.92% | 11.50% | 17.48% | -8.92% | 24.73% |
| BTC-USD | DOT-USD | 2023-06-25 | 86.65% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 14.72% | -11.52% | 14.72% | 32.77% | -11.52% | 38.41% |
| BTC-USD | OMG-USD | 2018-09-29 | 86.08% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -31.70% | -31.70% | 0.00% | -21.19% | -35.29% | 0.00% |
| BTC-USD | XTZ-USD | 2023-06-25 | 86.02% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 15.79% | -7.92% | 15.79% | 24.24% | -7.92% | 36.93% |
| DOGE-USD | DASH-USD | 2022-03-02 | 90.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.14% | -27.85% | 0.00% | -2.98% | -30.72% | 0.00% |
| DOGE-USD | VET-USD | 2022-03-04 | 89.06% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.06% | -21.27% | 0.00% | 18.68% | -22.08% | 18.68% |
| DOGE-USD | QTUM-USD | 2022-03-02 | 88.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.26% | -33.72% | 0.00% | 6.79% | -33.72% | 19.77% |
| DOGE-USD | THETA-USD | 2022-03-06 | 88.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.29% | -5.56% | 27.80% | 40.52% | -5.56% | 44.44% |
| DOGE-USD | 1INCH-USD | 2022-03-04 | 88.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -14.71% | -20.68% | 8.97% | 26.51% | -20.68% | 26.51% |
| DOGE-USD | INJ-USD | 2022-03-04 | 88.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.36% | -35.14% | 0.00% | 0.31% | -36.02% | 0.31% |
| DOGE-USD | ENJ-USD | 2022-03-07 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.19% | -8.90% | 29.08% | 54.45% | -8.90% | 55.79% |
| DOGE-USD | OP-USD | 2025-12-12 | 88.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -13.30% | 14.55% | 9.63% | -13.30% | 46.69% |
| DOGE-USD | OMG-USD | 2022-03-02 | 88.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.92% | -36.72% | 0.00% | -11.78% | -39.47% | 0.00% |
| DOGE-USD | XRP-USD | 2019-09-29 | 87.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| SOL-USD | RUNE-USD | 2025-12-17 | 79.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.50% | -7.03% | 20.04% | 9.91% | -7.03% | 54.43% |
| SOL-USD | NEAR-USD | 2025-12-11 | 79.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.92% | -11.77% | 8.98% | 21.58% | -11.77% | 23.26% |
| SOL-USD | LINK-USD | 2025-12-11 | 79.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.47% | -7.77% | 5.62% | 3.69% | -7.77% | 17.55% |
| SOL-USD | SOL-USD | 2025-12-14 | 78.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.93% | -13.64% | 0.31% | -7.78% | -13.64% | 6.48% |
| SOL-USD | APT-USD | 2024-09-11 | 77.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.26% | -23.26% | 3.72% | -33.02% | -33.49% | 3.72% |
| SOL-USD | DOT-USD | 2025-12-11 | 77.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.31% | -22.31% | 0.00% | -18.37% | -22.31% | 0.00% |
| SOL-USD | BTC-USD | 2025-12-14 | 76.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.28% | -6.99% | 10.28% | 6.45% | -6.99% | 15.83% |
| SOL-USD | AVAX-USD | 2025-12-12 | 76.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.82% | -6.61% | 5.84% | 0.86% | -6.61% | 11.16% |
| SOL-USD | KAVA-USD | 2025-12-16 | 75.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.67% | -7.55% | 12.67% | 9.02% | -7.55% | 24.66% |
| SOL-USD | FIL-USD | 2018-10-13 | 75.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.28% | -10.49% | 12.60% | 6.53% | -10.49% | 14.95% |

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

