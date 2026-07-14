# Market Regime Match Report

Generated: 2026-07-14 09:33 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 62.583 $ | False | -16.38% | -10.14% | BEAR | -16.38% | -10.14% |
| DOGE-USD | BEAR | 0.07209 $ | False | -24.08% | -16.36% | BEAR | -16.38% | -10.14% |
| SOL-USD | BEAR | 75,06 $ | False | -11.78% | -18.03% | BEAR | -16.38% | -10.14% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 11.27% | 25.77% | 39.63% | -4.71% | -27.71% | 13.10% | 28.93% | 53.53% | 67.50% | 24.79% | 40.84% | 75.20% |
| BTC-USD | SAME_BTC_REGIME | 14 | 100.00% | 28.52% | 41.34% | 61.20% | 0.00% | -6.69% | 37.78% | 52.59% | 63.57% | 78.57% | 17.88% | 38.12% | 105.17% |
| BTC-USD | SAME_ASSET_REGIME | 27 | 88.89% | 19.04% | 28.52% | 44.80% | -3.75% | -9.23% | 25.26% | 37.78% | 58.46% | 81.48% | 29.11% | 49.89% | 90.06% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 100.00% | 28.52% | 43.75% | 64.67% | 0.00% | -7.23% | 37.78% | 51.47% | 65.09% | 83.33% | 17.88% | 37.25% | 123.48% |
| DOGE-USD | ALL_MATCHES | 40 | 22.50% | -16.61% | -5.00% | 18.27% | -25.86% | -42.15% | 3.22% | 15.20% | 25.51% | 42.50% | -1.37% | 23.00% | 52.26% |
| DOGE-USD | SAME_BTC_REGIME | 28 | 14.29% | -21.56% | -12.68% | 4.05% | -28.98% | -42.67% | 2.36% | 11.23% | 24.01% | 35.71% | -2.37% | 7.55% | 29.89% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 24.24% | -17.03% | -6.39% | 18.42% | -27.58% | -41.03% | 2.52% | 13.35% | 26.09% | 45.45% | -0.80% | 25.45% | 49.11% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 26 | 11.54% | -21.56% | -12.92% | 0.08% | -28.98% | -43.19% | 1.51% | 10.18% | 19.94% | 34.62% | -3.17% | 5.47% | 25.65% |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -1.48% | 10.43% | 28.87% | -9.99% | -27.92% | 7.83% | 20.18% | 44.97% | 62.50% | 5.80% | 19.18% | 51.57% |
| SOL-USD | SAME_BTC_REGIME | 21 | 57.14% | 1.66% | 11.95% | 28.74% | -8.00% | -18.05% | 10.53% | 19.75% | 44.45% | 66.67% | 5.91% | 16.47% | 40.43% |
| SOL-USD | SAME_ASSET_REGIME | 28 | 53.57% | 1.21% | 10.43% | 29.12% | -8.08% | -20.41% | 9.99% | 20.18% | 46.02% | 67.86% | 7.41% | 27.92% | 51.63% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 17 | 58.82% | 1.66% | 9.93% | 21.97% | -8.00% | -15.58% | 10.53% | 17.46% | 32.15% | 70.59% | 5.91% | 16.47% | 43.75% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 100.00% | 28.52% | 0.00% | 52.59% | 78.57% | 17.88% | 69.51% |
| BTC-USD | HISTORICAL_BTC_BULL | 17 | 52.94% | 3.72% | -5.49% | 12.93% | 70.59% | 24.95% | 60.26% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 11.51% | -5.57% | 17.44% | 100.00% | 50.78% | 121.71% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -17.48% | -19.35% | 9.53% | 16.67% | -29.02% | 9.53% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 14.29% | -21.56% | -28.98% | 11.23% | 35.71% | -2.37% | 25.43% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 50.00% | 1.45% | -6.16% | 18.52% | 62.50% | 17.27% | 66.75% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 24.17% | -2.40% | 26.46% | 100.00% | 18.78% | 73.78% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -13.42% | -21.74% | 12.70% | 33.33% | -15.37% | 27.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 57.14% | 1.66% | -8.00% | 19.75% | 66.67% | 5.91% | 53.05% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 30.00% | -11.50% | -22.26% | 6.65% | 60.00% | 7.19% | 18.48% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 9 | 33.33% | -8.08% | -8.53% | 23.27% | 55.56% | 3.37% | 108.83% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 27 | 88.89% | 19.04% | -3.75% | 37.78% | 81.48% | 29.11% | 72.86% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 14.29% | -16.88% | -20.68% | 6.20% | 57.14% | 2.96% | 26.79% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -11.46% | -13.30% | 16.34% | 16.67% | -29.02% | 16.34% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 24.24% | -17.03% | -27.58% | 13.35% | 45.45% | -0.80% | 36.99% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 0.00% | -6.66% | -17.52% | 9.60% | 33.33% | -24.75% | 15.89% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -21.30% | -31.01% | 5.81% | 0.00% | -13.19% | 5.81% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -3.41% | -15.15% | 21.93% | 50.00% | 29.03% | 61.99% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 53.57% | 1.21% | -8.08% | 20.18% | 67.86% | 7.41% | 55.29% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 0.00% | -13.36% | -27.82% | 1.63% | 60.00% | 1.96% | 12.43% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -4.00% | -9.19% | 0.80% | 0.00% | -0.43% | 5.57% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 5.96% | -11.40% | 27.56% | 50.00% | 4.55% | 62.59% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-09-29 | 88.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| BTC-USD | ONE-USD | 2020-01-12 | 87.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |
| BTC-USD | KSM-USD | 2022-03-15 | 85.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 28.30% | -10.24% | 28.30% | -2.40% | -10.24% | 29.36% |
| BTC-USD | BAT-USD | 2019-10-04 | 85.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.15% | -1.02% | 43.98% | 5.38% | -1.02% | 63.91% |
| BTC-USD | QTUM-USD | 2020-01-12 | 84.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.33% | 0.00% | 26.00% | 25.57% | 0.00% | 43.16% |
| BTC-USD | OMG-USD | 2020-01-12 | 84.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 113.85% | 0.00% | 116.59% | 166.39% | 0.00% | 244.36% |
| BTC-USD | TRX-USD | 2020-01-12 | 84.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.85% | 0.00% | 30.82% | 26.22% | 0.00% | 45.23% |
| BTC-USD | ADA-USD | 2020-01-12 | 84.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 66.41% | 0.00% | 66.41% | 132.91% | 0.00% | 160.41% |
| BTC-USD | SOL-USD | 2022-03-15 | 84.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.04% | -4.00% | 31.59% | 7.07% | -4.00% | 36.23% |
| BTC-USD | XLM-USD | 2020-01-12 | 84.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| DOGE-USD | DASH-USD | 2022-02-25 | 89.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | VET-USD | 2022-02-27 | 88.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 88.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | 1INCH-USD | 2022-02-27 | 87.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.47% | -36.99% | 0.00% | -5.00% | -36.99% | 0.00% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | THETA-USD | 2022-03-01 | 87.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.39% | -17.72% | 11.00% | 25.45% | -17.98% | 25.45% |
| DOGE-USD | ENJ-USD | 2022-03-02 | 87.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.40% | -33.49% | 0.00% | 12.28% | -33.49% | 13.74% |
| DOGE-USD | XLM-USD | 2019-10-04 | 87.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 49.02% | 0.00% | 53.16% | 5.97% | 0.00% | 80.44% |
| DOGE-USD | INJ-USD | 2022-02-27 | 87.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -37.21% | -41.89% | 0.00% | -21.93% | -42.67% | 0.00% |
| DOGE-USD | OP-USD | 2025-12-07 | 86.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -12.89% | -25.94% | 0.00% | -0.67% | -25.94% | 25.30% |
| SOL-USD | NEAR-USD | 2025-12-06 | 79.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.76% | -13.93% | 10.53% | 16.47% | -13.93% | 18.85% |
| SOL-USD | XLM-USD | 2020-01-12 | 78.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| SOL-USD | RUNE-USD | 2025-12-12 | 78.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.99% | -7.87% | 5.19% | 5.91% | -7.87% | 53.05% |
| SOL-USD | SOL-USD | 2025-12-09 | 78.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.32% | -12.34% | 1.82% | -5.43% | -12.34% | 8.09% |
| SOL-USD | APT-USD | 2024-09-06 | 78.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | LINK-USD | 2025-12-06 | 78.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.84% | -11.36% | 4.69% | 10.45% | -11.36% | 12.98% |
| SOL-USD | XRP-USD | 2020-01-12 | 76.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.93% | 0.00% | 23.95% | 1.80% | 0.00% | 23.95% |
| SOL-USD | DOT-USD | 2025-12-06 | 76.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -19.05% | -19.05% | 14.02% | -5.32% | -19.05% | 14.02% |
| SOL-USD | BAT-USD | 2020-01-12 | 76.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 28.74% | 0.00% | 44.45% | 36.82% | 0.00% | 62.02% |
| SOL-USD | ONE-USD | 2020-01-12 | 76.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |

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

