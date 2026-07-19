# Market Regime Match Report

Generated: 2026-07-19 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.723 $ | False | -14.68% | -9.80% | BEAR | -14.68% | -9.80% |
| DOGE-USD | BEAR | 0.07242 $ | False | -23.94% | -15.74% | BEAR | -14.68% | -9.80% |
| SOL-USD | BEAR | 76,00 $ | False | -10.89% | -16.96% | BEAR | -14.68% | -9.80% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 4.95% | 14.99% | 29.50% | -8.93% | -31.88% | 12.18% | 21.59% | 33.46% | 55.00% | 2.41% | 34.47% | 81.81% |
| BTC-USD | SAME_BTC_REGIME | 3 | 100.00% | 29.37% | 38.41% | 43.83% | 0.00% | -6.11% | 33.33% | 46.48% | 54.37% | 0.00% | -1.77% | -1.74% | -1.72% |
| BTC-USD | SAME_ASSET_REGIME | 18 | 83.33% | 11.01% | 22.10% | 29.77% | -8.29% | -13.59% | 15.25% | 22.10% | 41.22% | 66.67% | 26.72% | 44.80% | 64.20% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 100.00% | 29.37% | 38.41% | 43.83% | 0.00% | -6.11% | 33.33% | 46.48% | 54.37% | 0.00% | -1.77% | -1.74% | -1.72% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -14.07% | 2.55% | 21.91% | -22.48% | -40.44% | 7.23% | 17.50% | 32.74% | 65.00% | 6.38% | 27.14% | 41.25% |
| DOGE-USD | SAME_BTC_REGIME | 30 | 26.67% | -15.99% | 4.07% | 25.31% | -27.38% | -40.44% | 0.00% | 16.47% | 32.74% | 70.00% | 6.97% | 26.35% | 48.49% |
| DOGE-USD | SAME_ASSET_REGIME | 31 | 29.03% | -16.19% | 3.91% | 21.54% | -25.04% | -40.24% | 0.67% | 16.02% | 29.08% | 70.97% | 7.14% | 29.70% | 40.52% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 28 | 25.00% | -16.67% | 1.16% | 22.66% | -27.38% | -40.84% | 0.00% | 15.56% | 30.01% | 67.86% | 6.38% | 26.02% | 44.70% |
| SOL-USD | ALL_MATCHES | 40 | 47.50% | -0.93% | 11.50% | 17.42% | -11.01% | -27.63% | 8.15% | 19.83% | 27.37% | 57.50% | 1.11% | 16.11% | 37.90% |
| SOL-USD | SAME_BTC_REGIME | 13 | 46.15% | -0.47% | 5.97% | 12.29% | -10.49% | -23.07% | 5.62% | 8.98% | 13.46% | 69.23% | 1.35% | 6.53% | 13.41% |
| SOL-USD | SAME_ASSET_REGIME | 21 | 61.90% | 0.92% | 12.54% | 18.50% | -10.24% | -23.26% | 8.37% | 20.04% | 27.29% | 61.90% | 0.86% | 11.29% | 29.74% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 54.55% | 0.82% | 8.63% | 12.54% | -10.49% | -22.31% | 5.84% | 10.79% | 13.68% | 72.73% | 3.69% | 8.22% | 14.29% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 3 | 100.00% | 29.37% | 0.00% | 46.48% | 0.00% | -1.77% | 58.84% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 56.52% | 7.39% | -11.54% | 15.25% | 60.87% | 24.24% | 52.74% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 14 | 50.00% | 0.51% | -8.32% | 20.89% | 57.14% | 2.28% | 83.19% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 26.67% | -15.99% | -27.38% | 16.47% | 70.00% | 6.97% | 46.45% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 1.12% | -10.51% | 15.94% | 40.00% | -14.97% | 38.41% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -18.14% | -23.06% | 19.23% | 60.00% | 3.49% | 29.01% |
| SOL-USD | HISTORICAL_BTC_BEAR | 13 | 46.15% | -0.47% | -10.49% | 8.98% | 69.23% | 1.35% | 19.29% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 30.00% | -7.58% | -14.08% | 17.55% | 50.00% | 0.82% | 29.92% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 17 | 58.82% | 1.17% | -8.06% | 23.27% | 52.94% | 0.80% | 74.37% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 18 | 83.33% | 11.01% | -8.29% | 22.10% | 66.67% | 26.72% | 66.21% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 30.00% | -11.28% | -20.70% | 10.34% | 40.00% | -4.58% | 27.06% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 3 | 0.00% | -34.71% | -34.71% | 6.69% | 33.33% | -38.16% | 52.69% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 55.56% | 4.38% | -5.24% | 19.23% | 55.56% | 1.70% | 26.94% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 31 | 29.03% | -16.19% | -25.04% | 16.02% | 70.97% | 7.14% | 45.09% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -23.86% | -27.55% | 8.37% | 50.00% | -1.55% | 16.96% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 12.46% | -17.87% | 28.63% | 100.00% | 36.02% | 68.19% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -3.70% | -12.43% | 19.23% | 20.00% | -14.97% | 19.23% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 21 | 61.90% | 0.92% | -10.24% | 20.04% | 61.90% | 0.86% | 27.29% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 16.67% | -10.50% | -16.47% | 8.28% | 50.00% | 0.82% | 9.99% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 4.99% | -4.53% | 20.78% | 100.00% | 34.99% | 85.23% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -8.01% | -13.69% | 20.76% | 40.00% | -4.62% | 52.51% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-04 | 88.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| BTC-USD | ETH-USD | 2025-12-11 | 85.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -7.64% | 12.79% | -1.70% | -7.64% | 12.79% |
| BTC-USD | XLM-USD | 2019-10-09 | 84.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 47.44% | 0.00% | 59.63% | -34.58% | -37.78% | 59.63% |
| BTC-USD | LRC-USD | 2018-09-24 | 89.93% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 30.68% | -8.53% | 146.68% | 36.85% | -8.53% | 146.68% |
| BTC-USD | SAND-USD | 2023-06-24 | 89.79% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 7.39% | -12.66% | 11.30% | 26.71% | -12.66% | 37.05% |
| BTC-USD | FIL-USD | 2023-06-24 | 89.30% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 10.53% | -8.25% | 11.57% | 26.74% | -8.25% | 50.97% |
| BTC-USD | EOS-USD | 2023-06-25 | 87.37% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 11.50% | -8.92% | 11.50% | 17.48% | -8.92% | 24.73% |
| BTC-USD | DOT-USD | 2023-06-25 | 87.15% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 14.72% | -11.52% | 14.72% | 32.77% | -11.52% | 38.41% |
| BTC-USD | XTZ-USD | 2023-06-25 | 86.36% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 15.79% | -7.92% | 15.79% | 24.24% | -7.92% | 36.93% |
| BTC-USD | AVAX-USD | 2023-06-26 | 86.29% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 26.43% | -5.19% | 29.83% | 136.51% | -5.19% | 143.09% |
| DOGE-USD | VET-USD | 2022-03-04 | 89.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.06% | -21.27% | 0.00% | 18.68% | -22.08% | 18.68% |
| DOGE-USD | DASH-USD | 2022-03-02 | 89.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.14% | -27.85% | 0.00% | -2.98% | -30.72% | 0.00% |
| DOGE-USD | OP-USD | 2025-12-12 | 88.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -13.30% | 14.55% | 9.63% | -13.30% | 46.69% |
| DOGE-USD | XRP-USD | 2019-09-29 | 88.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| DOGE-USD | QTUM-USD | 2022-03-02 | 88.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.26% | -33.72% | 0.00% | 6.79% | -33.72% | 19.77% |
| DOGE-USD | THETA-USD | 2022-03-06 | 88.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.29% | -5.56% | 27.80% | 40.52% | -5.56% | 44.44% |
| DOGE-USD | INJ-USD | 2022-03-04 | 87.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.36% | -35.14% | 0.00% | 0.31% | -36.02% | 0.31% |
| DOGE-USD | OMG-USD | 2022-03-02 | 87.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.92% | -36.72% | 0.00% | -11.78% | -39.47% | 0.00% |
| DOGE-USD | 1INCH-USD | 2022-03-04 | 87.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -14.71% | -20.68% | 8.97% | 26.51% | -20.68% | 26.51% |
| DOGE-USD | ENJ-USD | 2022-03-07 | 87.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.19% | -8.90% | 29.08% | 54.45% | -8.90% | 55.79% |
| SOL-USD | LINK-USD | 2025-12-11 | 78.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.47% | -7.77% | 5.62% | 3.69% | -7.77% | 17.55% |
| SOL-USD | SOL-USD | 2025-12-14 | 78.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.93% | -13.64% | 0.31% | -7.78% | -13.64% | 6.48% |
| SOL-USD | NEAR-USD | 2025-12-11 | 78.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.92% | -11.77% | 8.98% | 21.58% | -11.77% | 23.26% |
| SOL-USD | RUNE-USD | 2025-12-17 | 78.06% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.50% | -7.03% | 20.04% | 9.91% | -7.03% | 54.43% |
| SOL-USD | APT-USD | 2024-09-11 | 77.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.26% | -23.26% | 3.72% | -33.02% | -33.49% | 3.72% |
| SOL-USD | CRV-USD | 2025-12-10 | 77.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.04% | -12.48% | 1.18% | 0.44% | -12.48% | 19.29% |
| SOL-USD | BTC-USD | 2025-12-13 | 77.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.54% | -2.79% | 13.68% | 14.29% | -2.79% | 21.07% |
| SOL-USD | OMG-USD | 2025-12-11 | 76.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.97% | -5.71% | 8.37% | 4.15% | -5.71% | 17.41% |
| SOL-USD | FIL-USD | 2018-10-13 | 76.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.28% | -10.49% | 12.60% | 6.53% | -10.49% | 14.95% |
| SOL-USD | DOT-USD | 2025-12-11 | 75.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.31% | -22.31% | 0.00% | -18.37% | -22.31% | 0.00% |

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

