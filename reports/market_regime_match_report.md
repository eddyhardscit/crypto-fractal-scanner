# Market Regime Match Report

Generated: 2026-07-14 07:22 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 62.239 $ | False | -16.10% | -10.18% | BEAR | -16.10% | -10.18% |
| DOGE-USD | BEAR | 0.07185 $ | False | -22.75% | -16.45% | BEAR | -16.10% | -10.18% |
| SOL-USD | BEAR | 74,86 $ | False | -10.64% | -18.22% | BEAR | -16.10% | -10.18% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 8.05% | 22.15% | 49.06% | -5.53% | -34.15% | 13.10% | 26.06% | 53.53% | 67.50% | 25.26% | 50.98% | 72.68% |
| BTC-USD | SAME_BTC_REGIME | 14 | 100.00% | 33.95% | 49.32% | 86.91% | 0.00% | -6.69% | 44.21% | 55.99% | 101.53% | 85.71% | 31.19% | 61.02% | 113.20% |
| BTC-USD | SAME_ASSET_REGIME | 26 | 88.46% | 15.37% | 27.54% | 57.72% | -4.53% | -10.88% | 19.54% | 27.79% | 59.78% | 80.77% | 35.13% | 53.08% | 95.02% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 100.00% | 28.52% | 53.37% | 92.76% | 0.00% | -7.23% | 36.14% | 56.47% | 111.57% | 83.33% | 17.88% | 48.99% | 126.33% |
| DOGE-USD | ALL_MATCHES | 40 | 17.50% | -19.00% | -6.59% | 6.57% | -26.95% | -43.10% | 5.40% | 13.62% | 25.53% | 37.50% | -2.71% | 11.78% | 37.22% |
| DOGE-USD | SAME_BTC_REGIME | 31 | 12.90% | -22.91% | -12.96% | 2.98% | -29.01% | -44.40% | 2.52% | 11.46% | 25.42% | 32.26% | -3.26% | 4.97% | 25.45% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 18.18% | -21.33% | -10.41% | 6.69% | -28.71% | -44.11% | 4.26% | 11.92% | 26.25% | 39.39% | -1.48% | 12.28% | 36.28% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 29 | 10.34% | -22.91% | -13.04% | -3.80% | -29.01% | -44.42% | 2.36% | 11.00% | 26.11% | 31.03% | -4.86% | 3.96% | 22.83% |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -0.86% | 12.98% | 28.87% | -9.94% | -24.90% | 7.81% | 20.21% | 44.97% | 65.00% | 6.53% | 27.92% | 51.57% |
| SOL-USD | SAME_BTC_REGIME | 23 | 56.52% | 1.66% | 14.02% | 26.58% | -8.00% | -18.28% | 9.84% | 21.85% | 41.36% | 73.91% | 8.91% | 37.69% | 63.94% |
| SOL-USD | SAME_ASSET_REGIME | 27 | 55.56% | 1.66% | 14.71% | 29.25% | -8.08% | -18.84% | 9.84% | 20.67% | 46.55% | 74.07% | 8.91% | 36.83% | 51.66% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 55.56% | 1.21% | 9.25% | 20.85% | -8.99% | -15.56% | 9.26% | 17.24% | 30.10% | 77.78% | 8.03% | 31.73% | 56.19% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 100.00% | 33.95% | 0.00% | 55.99% | 85.71% | 31.19% | 118.07% |
| BTC-USD | HISTORICAL_BTC_BULL | 16 | 56.25% | 3.80% | -7.64% | 14.51% | 62.50% | 27.03% | 49.09% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 100.00% | 11.31% | -6.15% | 15.36% | 100.00% | 54.98% | 93.27% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 0.00% | -12.14% | -13.81% | 6.78% | 16.67% | -29.02% | 8.03% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 31 | 12.90% | -22.91% | -29.01% | 11.46% | 32.26% | -3.26% | 25.36% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 40.00% | -0.83% | -8.57% | 17.54% | 60.00% | 1.10% | 43.03% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 24.17% | -2.40% | 26.46% | 100.00% | 18.78% | 73.78% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -9.79% | -13.95% | 12.70% | 33.33% | -15.37% | 27.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 23 | 56.52% | 1.66% | -8.00% | 21.85% | 73.91% | 8.91% | 63.65% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 20.00% | -11.50% | -22.26% | 3.09% | 50.00% | -0.20% | 13.65% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 17.86% | 0.00% | 21.60% | 100.00% | 50.78% | 64.83% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 6 | 33.33% | -1.02% | -10.52% | 40.99% | 50.00% | -2.21% | 42.21% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 88.46% | 15.37% | -4.53% | 27.79% | 80.77% | 35.13% | 82.47% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 28.57% | -23.01% | -23.01% | 9.09% | 42.86% | -4.51% | 26.79% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 49.41% | -3.98% | 52.30% | 100.00% | 67.20% | 106.78% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 16.67% | -12.14% | -13.30% | 6.78% | 33.33% | -29.02% | 8.03% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 18.18% | -21.33% | -28.71% | 11.92% | 39.39% | -1.48% | 28.83% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -3.74% | -10.00% | 13.15% | 50.00% | -11.83% | 16.71% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -25.24% | -38.58% | 7.55% | 0.00% | -3.26% | 7.55% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -8.75% | -14.04% | 12.94% | 0.00% | -9.16% | 12.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -2.56% | -8.55% | 20.44% | 33.33% | -15.37% | 47.15% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 55.56% | 1.66% | -8.08% | 20.67% | 74.07% | 8.91% | 63.42% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 0.00% | -13.24% | -24.49% | 1.58% | 50.00% | -0.20% | 10.15% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -4.00% | -9.19% | 0.80% | 0.00% | -0.43% | 5.57% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 5.03% | -13.26% | 28.27% | 50.00% | 4.55% | 62.59% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-09-19 | 89.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| BTC-USD | XRP-USD | 2019-09-29 | 87.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| BTC-USD | ONE-USD | 2020-01-12 | 87.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |
| BTC-USD | BAT-USD | 2019-10-04 | 85.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.15% | -1.02% | 43.98% | 5.38% | -1.02% | 63.91% |
| BTC-USD | LTC-USD | 2020-01-09 | 85.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.10% | -4.48% | 15.70% | 2.65% | -4.48% | 15.70% |
| BTC-USD | QTUM-USD | 2020-01-12 | 84.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.33% | 0.00% | 26.00% | 25.57% | 0.00% | 43.16% |
| BTC-USD | OMG-USD | 2020-01-12 | 84.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 113.85% | 0.00% | 116.59% | 166.39% | 0.00% | 244.36% |
| BTC-USD | ADA-USD | 2020-01-12 | 84.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 66.41% | 0.00% | 66.41% | 132.91% | 0.00% | 160.41% |
| BTC-USD | XLM-USD | 2019-10-04 | 84.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 49.02% | 0.00% | 53.16% | 5.97% | 0.00% | 80.44% |
| BTC-USD | KSM-USD | 2022-03-15 | 84.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 28.30% | -10.24% | 28.30% | -2.40% | -10.24% | 29.36% |
| DOGE-USD | VET-USD | 2022-02-27 | 88.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | DASH-USD | 2022-02-25 | 88.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 87.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | 1INCH-USD | 2022-02-27 | 87.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.47% | -36.99% | 0.00% | -5.00% | -36.99% | 0.00% |
| DOGE-USD | THETA-USD | 2022-03-01 | 86.89% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.39% | -17.72% | 11.00% | 25.45% | -17.98% | 25.45% |
| DOGE-USD | OP-USD | 2025-12-07 | 86.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -12.89% | -25.94% | 0.00% | -0.67% | -25.94% | 25.30% |
| DOGE-USD | SOL-USD | 2022-03-05 | 86.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.55% | -8.30% | 37.70% | 39.29% | -8.30% | 46.05% |
| DOGE-USD | INJ-USD | 2022-02-27 | 86.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -37.21% | -41.89% | 0.00% | -21.93% | -42.67% | 0.00% |
| DOGE-USD | ENJ-USD | 2022-03-02 | 86.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.40% | -33.49% | 0.00% | 12.28% | -33.49% | 13.74% |
| SOL-USD | APT-USD | 2024-09-06 | 78.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | SOL-USD | 2025-12-09 | 77.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.32% | -12.34% | 1.82% | -5.43% | -12.34% | 8.09% |
| SOL-USD | NEAR-USD | 2025-12-06 | 77.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.76% | -13.93% | 10.53% | 16.47% | -13.93% | 18.85% |
| SOL-USD | XLM-USD | 2020-01-12 | 77.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| SOL-USD | CRV-USD | 2025-12-05 | 76.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.77% | -11.77% | 8.67% | 13.61% | -11.77% | 20.25% |
| SOL-USD | RUNE-USD | 2025-12-12 | 76.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.99% | -7.87% | 5.19% | 5.91% | -7.87% | 53.05% |
| SOL-USD | LINK-USD | 2025-12-06 | 76.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.84% | -11.36% | 4.69% | 10.45% | -11.36% | 12.98% |
| SOL-USD | OMG-USD | 2025-12-06 | 76.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -8.00% | 2.31% | 8.91% | -8.00% | 14.55% |
| SOL-USD | BAT-USD | 2020-01-12 | 76.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 28.74% | 0.00% | 44.45% | 36.82% | 0.00% | 62.02% |
| SOL-USD | ONE-USD | 2020-01-12 | 76.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |

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

