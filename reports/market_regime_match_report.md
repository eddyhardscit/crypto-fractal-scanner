# Market Regime Match Report

Generated: 2026-07-11 07:21 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.142 $ | False | -9.30% | -10.24% | BEAR | -9.30% | -10.24% |
| DOGE-USD | BEAR | 0.07431 $ | False | -18.15% | -16.60% | BEAR | -9.30% | -10.24% |
| SOL-USD | BEAR | 77,93 $ | False | -4.38% | -18.58% | BEAR | -9.30% | -10.24% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 7.63% | 19.85% | 38.29% | -4.42% | -24.56% | 12.73% | 27.89% | 40.08% | 67.50% | 22.54% | 43.73% | 57.64% |
| BTC-USD | SAME_BTC_REGIME | 13 | 100.00% | 25.70% | 39.37% | 48.27% | 0.00% | -3.45% | 37.70% | 53.16% | 61.45% | 92.31% | 32.98% | 42.97% | 47.46% |
| BTC-USD | SAME_ASSET_REGIME | 26 | 88.46% | 11.06% | 21.79% | 37.45% | -2.98% | -10.88% | 18.35% | 32.07% | 45.89% | 88.46% | 33.21% | 49.59% | 58.33% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 100.00% | 22.02% | 37.45% | 49.02% | 0.00% | -3.57% | 34.23% | 45.89% | 62.58% | 90.91% | 14.38% | 41.68% | 46.00% |
| DOGE-USD | ALL_MATCHES | 40 | 17.50% | -20.25% | -8.23% | 10.73% | -28.67% | -42.94% | 5.31% | 14.11% | 26.69% | 37.50% | -2.71% | 6.57% | 25.79% |
| DOGE-USD | SAME_BTC_REGIME | 32 | 12.50% | -23.14% | -16.69% | 0.98% | -30.89% | -42.96% | 3.80% | 9.30% | 28.38% | 34.38% | -2.71% | 2.66% | 14.49% |
| DOGE-USD | SAME_ASSET_REGIME | 34 | 17.65% | -21.65% | -11.03% | 15.06% | -28.94% | -42.95% | 4.92% | 15.62% | 28.12% | 38.24% | -1.76% | 9.20% | 33.26% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 30 | 13.33% | -22.70% | -16.60% | 2.09% | -30.03% | -43.15% | 3.80% | 11.05% | 28.93% | 33.33% | -2.92% | 1.50% | 15.78% |
| SOL-USD | ALL_MATCHES | 40 | 35.00% | -1.70% | 6.82% | 29.40% | -12.39% | -30.88% | 6.66% | 15.45% | 39.02% | 57.50% | 6.73% | 28.98% | 51.09% |
| SOL-USD | SAME_BTC_REGIME | 24 | 45.83% | -0.22% | 14.94% | 42.27% | -8.81% | -22.62% | 10.48% | 25.62% | 51.84% | 75.00% | 10.12% | 31.25% | 50.61% |
| SOL-USD | SAME_ASSET_REGIME | 31 | 41.94% | -0.39% | 8.97% | 35.32% | -10.44% | -23.64% | 9.84% | 18.31% | 44.45% | 67.74% | 8.91% | 31.58% | 50.78% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 21 | 47.62% | 0.00% | 14.56% | 45.24% | -8.00% | -19.37% | 10.51% | 25.47% | 55.01% | 76.19% | 11.32% | 30.91% | 42.97% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 13 | 100.00% | 25.70% | 0.00% | 53.16% | 92.31% | 32.98% | 78.05% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 42.86% | -7.09% | -10.83% | 9.66% | 42.86% | -4.13% | 42.87% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 8 | 100.00% | 9.66% | -5.04% | 20.20% | 100.00% | 46.43% | 77.46% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 40.00% | -7.78% | -12.28% | 16.64% | 20.00% | -24.31% | 32.20% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 32 | 12.50% | -23.14% | -30.89% | 9.30% | 34.38% | -2.71% | 22.67% |
| DOGE-USD | HISTORICAL_BTC_BULL | 2 | 0.00% | -7.70% | -15.78% | 9.71% | 50.00% | -4.03% | 13.92% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 21.44% | -1.83% | 24.78% | 100.00% | 76.22% | 136.08% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 25.00% | -6.70% | -13.68% | 16.66% | 25.00% | -10.28% | 22.35% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 45.83% | -0.22% | -8.81% | 25.62% | 75.00% | 10.12% | 45.66% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 0.00% | -7.40% | -25.96% | 2.26% | 10.00% | -4.91% | 2.26% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 75.00% | 5.03% | -9.15% | 11.55% | 100.00% | 42.24% | 68.81% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -16.77% | -29.03% | 11.14% | 0.00% | -35.08% | 11.14% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 88.46% | 11.06% | -2.98% | 32.07% | 88.46% | 33.21% | 76.98% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 16.67% | -18.39% | -20.49% | 8.15% | 16.67% | -7.51% | 8.15% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 4.40% | -3.37% | 24.00% | 66.67% | 21.58% | 57.57% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 5.95% | -11.70% | 32.20% | 20.00% | -24.31% | 32.20% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 17.65% | -21.65% | -28.94% | 15.62% | 38.24% | -1.76% | 25.07% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -6.66% | -17.52% | 5.68% | 66.67% | 1.10% | 12.81% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -25.24% | -38.58% | 7.55% | 0.00% | -3.26% | 7.55% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -8.75% | -14.04% | 12.94% | 0.00% | -9.16% | 12.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -9.79% | -21.74% | 17.47% | 0.00% | -15.37% | 17.47% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 41.94% | -0.39% | -10.44% | 18.31% | 67.74% | 8.91% | 49.90% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 0.00% | -18.82% | -28.28% | 0.42% | 33.33% | -5.68% | 0.42% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -6.61% | -31.16% | 1.10% | 0.00% | -3.73% | 1.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 20.00% | -6.02% | -30.84% | 4.03% | 20.00% | -4.13% | 4.03% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-09-19 | 89.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| BTC-USD | KSM-USD | 2022-03-10 | 86.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.02% | -4.93% | 16.96% | 14.38% | -4.93% | 37.01% |
| BTC-USD | XLM-USD | 2020-01-07 | 85.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| BTC-USD | ONE-USD | 2020-01-07 | 84.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.92% | 0.00% | 14.92% | -3.06% | -3.06% | 19.26% |
| BTC-USD | TRX-USD | 2020-01-07 | 84.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.02% | 0.00% | 33.95% | 32.98% | 0.00% | 48.70% |
| BTC-USD | EOS-USD | 2020-01-07 | 84.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.83% | 0.00% | 25.64% | 7.27% | 0.00% | 25.64% |
| BTC-USD | XLM-USD | 2019-10-04 | 84.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 49.02% | 0.00% | 53.16% | 5.97% | 0.00% | 80.44% |
| BTC-USD | ZEC-USD | 2020-01-07 | 84.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.42% | 0.00% | 34.23% | 46.00% | 0.00% | 56.81% |
| BTC-USD | MKR-USD | 2021-07-21 | 83.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.66% | -0.21% | 38.63% | 12.58% | -6.23% | 38.63% |
| BTC-USD | LTC-USD | 2020-01-06 | 83.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.04% | -3.57% | 20.47% | 9.84% | -3.57% | 20.47% |
| DOGE-USD | DASH-USD | 2022-02-20 | 88.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.45% | -33.95% | 2.32% | -19.38% | -36.58% | 2.32% |
| DOGE-USD | XTZ-USD | 2025-12-06 | 87.11% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.41% | -12.14% | 4.26% | -2.16% | -12.14% | 4.26% |
| DOGE-USD | VET-USD | 2022-02-27 | 87.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 86.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | CHZ-USD | 2022-02-24 | 86.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -19.17% | -28.71% | 5.97% | 11.61% | -28.71% | 22.22% |
| DOGE-USD | 1INCH-USD | 2022-02-22 | 86.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -31.62% | -42.19% | 0.00% | -20.09% | -42.19% | 0.00% |
| DOGE-USD | ENJ-USD | 2022-02-25 | 86.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.55% | -33.46% | 5.00% | 1.45% | -33.46% | 5.00% |
| DOGE-USD | XLM-USD | 2019-09-29 | 86.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.92% | -5.54% | 39.92% | 24.54% | -5.54% | 74.65% |
| DOGE-USD | ETH-USD | 2022-02-25 | 86.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.11% | -44.85% | 3.20% | -10.14% | -44.85% | 3.20% |
| SOL-USD | TRX-USD | 2018-09-19 | 78.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 55.01% | 0.00% | 55.01% | 32.25% | 0.00% | 58.38% |
| SOL-USD | QTUM-USD | 2018-09-19 | 78.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.21% | -3.68% | 15.25% | -0.51% | -17.60% | 15.25% |
| SOL-USD | XLM-USD | 2020-01-07 | 77.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| SOL-USD | SOL-USD | 2025-12-04 | 77.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.51% | -10.44% | 9.16% | 6.95% | -10.44% | 10.43% |
| SOL-USD | LRC-USD | 2018-09-19 | 77.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| SOL-USD | NEAR-USD | 2025-12-01 | 76.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.36% | -9.61% | 16.07% | 21.89% | -9.61% | 24.08% |
| SOL-USD | ENJ-USD | 2018-09-19 | 76.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -16.11% | -19.37% | 5.11% | 93.16% | -38.09% | 93.16% |
| SOL-USD | APT-USD | 2024-09-06 | 76.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | OMG-USD | 2025-12-06 | 75.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -8.00% | 2.31% | 8.91% | -8.00% | 14.55% |
| SOL-USD | RUNE-USD | 2025-12-07 | 75.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.46% | -17.52% | 0.00% | 8.26% | -17.52% | 37.02% |

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

