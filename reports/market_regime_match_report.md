# Market Regime Match Report

Generated: 2026-07-18 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.889 $ | False | -13.50% | -9.83% | BEAR | -13.50% | -9.83% |
| DOGE-USD | BEAR | 0.07237 $ | False | -22.25% | -15.83% | BEAR | -13.50% | -9.83% |
| SOL-USD | BEAR | 74,93 $ | False | -10.34% | -17.11% | BEAR | -13.50% | -9.83% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 3.00% | 11.58% | 26.72% | -8.93% | -29.35% | 11.16% | 19.30% | 33.46% | 55.00% | 2.46% | 32.99% | 48.78% |
| BTC-USD | SAME_BTC_REGIME | 6 | 100.00% | 17.45% | 38.84% | 44.72% | 0.00% | -6.13% | 26.92% | 46.51% | 55.27% | 33.33% | -1.25% | 4.02% | 22.09% |
| BTC-USD | SAME_ASSET_REGIME | 19 | 89.47% | 10.53% | 24.23% | 32.94% | -8.08% | -11.93% | 15.79% | 25.93% | 52.65% | 73.68% | 26.74% | 44.28% | 59.75% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 100.00% | 29.37% | 41.99% | 45.26% | 0.00% | -4.58% | 33.33% | 50.91% | 56.14% | 40.00% | -1.70% | 5.62% | 25.38% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -14.61% | 2.55% | 18.77% | -23.99% | -40.41% | 2.22% | 16.45% | 37.74% | 57.50% | 3.00% | 24.62% | 40.00% |
| DOGE-USD | SAME_BTC_REGIME | 31 | 22.58% | -16.19% | -0.30% | 21.54% | -27.66% | -41.89% | 0.00% | 14.71% | 32.19% | 58.06% | 2.52% | 15.48% | 39.29% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 27.27% | -16.19% | 2.30% | 18.32% | -27.10% | -41.56% | 1.91% | 15.11% | 31.31% | 60.61% | 5.97% | 25.86% | 39.81% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 29 | 20.69% | -20.06% | -0.32% | 12.13% | -27.66% | -41.96% | 0.00% | 14.55% | 28.68% | 55.17% | 0.93% | 10.77% | 32.17% |
| SOL-USD | ALL_MATCHES | 40 | 47.50% | -0.89% | 10.45% | 19.40% | -10.37% | -27.49% | 7.84% | 15.62% | 35.63% | 60.00% | 2.82% | 26.74% | 39.78% |
| SOL-USD | SAME_BTC_REGIME | 16 | 50.00% | 0.18% | 6.96% | 21.21% | -8.53% | -21.15% | 5.73% | 12.69% | 34.29% | 62.50% | 1.33% | 7.61% | 28.61% |
| SOL-USD | SAME_ASSET_REGIME | 24 | 58.33% | 1.96% | 10.84% | 27.31% | -8.16% | -23.22% | 8.67% | 20.68% | 48.18% | 70.83% | 5.03% | 27.51% | 47.15% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 14 | 57.14% | 0.87% | 8.94% | 25.52% | -7.82% | -17.44% | 7.10% | 13.58% | 38.43% | 71.43% | 2.75% | 11.02% | 31.42% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 6 | 100.00% | 17.45% | 0.00% | 46.51% | 33.33% | -1.25% | 59.23% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 56.52% | 2.05% | -11.54% | 11.53% | 65.22% | 24.24% | 52.74% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 11 | 36.36% | -8.08% | -8.53% | 20.34% | 45.45% | -2.44% | 71.01% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 31 | 22.58% | -16.19% | -27.66% | 14.71% | 58.06% | 2.52% | 35.52% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 1.12% | -4.42% | 19.33% | 40.00% | -20.41% | 44.20% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 50.00% | -7.42% | -17.74% | 47.20% | 75.00% | 16.25% | 47.20% |
| SOL-USD | HISTORICAL_BTC_BEAR | 16 | 50.00% | 0.18% | -8.53% | 12.69% | 62.50% | 1.33% | 23.43% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 36.36% | -9.88% | -15.76% | 9.62% | 54.55% | 1.96% | 25.37% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 53.85% | 4.38% | -8.08% | 25.06% | 61.54% | 23.83% | 99.95% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 19 | 89.47% | 10.53% | -8.08% | 25.93% | 73.68% | 26.74% | 66.84% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 27.27% | -16.88% | -20.68% | 6.28% | 45.45% | -5.26% | 25.00% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -21.38% | -25.29% | 5.95% | 50.00% | -5.81% | 74.96% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 37.50% | -12.34% | -13.84% | 19.30% | 25.00% | -3.83% | 19.30% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 27.27% | -16.19% | -27.10% | 15.11% | 60.61% | 5.97% | 44.44% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -11.42% | -12.91% | 8.02% | 0.00% | -23.03% | 8.02% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -13.25% | -23.44% | 19.38% | 66.67% | 24.21% | 54.33% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 1.12% | -12.43% | 27.05% | 33.33% | -17.22% | 27.05% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 24 | 58.33% | 1.96% | -8.16% | 20.68% | 70.83% | 5.03% | 51.49% |
| SOL-USD | HISTORICAL_ASSET_BULL | 7 | 14.29% | -12.52% | -18.60% | 4.67% | 42.86% | -0.32% | 9.57% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -4.00% | -9.19% | 0.80% | 0.00% | -0.43% | 5.57% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 4.99% | -4.53% | 20.78% | 100.00% | 34.99% | 85.23% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | -3.56% | -7.11% | 20.76% | 33.33% | -10.93% | 39.22% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-04 | 87.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| BTC-USD | LTC-USD | 2020-01-13 | 85.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.15% | 0.00% | 20.51% | 5.62% | 0.00% | 20.51% |
| BTC-USD | XLM-USD | 2019-10-09 | 85.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 47.44% | 0.00% | 59.63% | -34.58% | -37.78% | 59.63% |
| BTC-USD | XLM-USD | 2020-01-12 | 84.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| BTC-USD | ETH-USD | 2025-12-11 | 84.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -7.64% | 12.79% | -1.70% | -7.64% | 12.79% |
| BTC-USD | EOS-USD | 2020-01-12 | 84.52% | BEAR | RECOVERY | SAME_BTC_ONLY | MIXED | 2.83% | -4.62% | 19.52% | -0.79% | -4.62% | 19.52% |
| BTC-USD | LRC-USD | 2018-09-24 | 90.61% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 30.68% | -8.53% | 146.68% | 36.85% | -8.53% | 146.68% |
| BTC-USD | FIL-USD | 2023-06-24 | 89.47% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 10.53% | -8.25% | 11.57% | 26.74% | -8.25% | 50.97% |
| BTC-USD | SAND-USD | 2023-06-24 | 89.19% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 7.39% | -12.66% | 11.30% | 26.71% | -12.66% | 37.05% |
| BTC-USD | EOS-USD | 2023-06-25 | 86.80% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 11.50% | -8.92% | 11.50% | 17.48% | -8.92% | 24.73% |
| DOGE-USD | VET-USD | 2022-03-04 | 88.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.06% | -21.27% | 0.00% | 18.68% | -22.08% | 18.68% |
| DOGE-USD | XRP-USD | 2019-09-29 | 88.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| DOGE-USD | DASH-USD | 2022-02-25 | 88.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | OP-USD | 2025-12-12 | 88.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -13.30% | 14.55% | 9.63% | -13.30% | 46.69% |
| DOGE-USD | OMG-USD | 2022-03-02 | 88.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.92% | -36.72% | 0.00% | -11.78% | -39.47% | 0.00% |
| DOGE-USD | INJ-USD | 2022-02-27 | 87.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -37.21% | -41.89% | 0.00% | -21.93% | -42.67% | 0.00% |
| DOGE-USD | QTUM-USD | 2022-03-02 | 87.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.26% | -33.72% | 0.00% | 6.79% | -33.72% | 19.77% |
| DOGE-USD | ENJ-USD | 2022-03-02 | 87.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.40% | -33.49% | 0.00% | 12.28% | -33.49% | 13.74% |
| DOGE-USD | DOT-USD | 2022-03-02 | 87.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -21.34% | -27.10% | 0.00% | 0.39% | -31.78% | 0.39% |
| DOGE-USD | 1INCH-USD | 2022-02-27 | 87.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.47% | -36.99% | 0.00% | -5.00% | -36.99% | 0.00% |
| SOL-USD | RUNE-USD | 2025-12-12 | 78.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.99% | -7.87% | 5.19% | 5.91% | -7.87% | 53.05% |
| SOL-USD | SOL-USD | 2025-12-09 | 78.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.32% | -12.34% | 1.82% | -5.43% | -12.34% | 8.09% |
| SOL-USD | APT-USD | 2024-09-11 | 77.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.26% | -23.26% | 3.72% | -33.02% | -33.49% | 3.72% |
| SOL-USD | LINK-USD | 2025-12-11 | 77.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.47% | -7.77% | 5.62% | 3.69% | -7.77% | 17.55% |
| SOL-USD | BTC-USD | 2025-12-12 | 77.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.42% | -4.01% | 12.25% | 12.73% | -4.01% | 19.54% |
| SOL-USD | NEAR-USD | 2025-12-11 | 76.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.92% | -11.77% | 8.98% | 21.58% | -11.77% | 23.26% |
| SOL-USD | DOT-USD | 2025-12-06 | 76.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -19.05% | -19.05% | 14.02% | -5.32% | -19.05% | 14.02% |
| SOL-USD | XLM-USD | 2020-01-12 | 76.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| SOL-USD | CRV-USD | 2025-12-10 | 76.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.04% | -12.48% | 1.18% | 0.44% | -12.48% | 19.29% |
| SOL-USD | OMG-USD | 2025-12-11 | 76.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.97% | -5.71% | 8.37% | 4.15% | -5.71% | 17.41% |

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

