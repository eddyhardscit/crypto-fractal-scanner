# Market Regime Match Report

Generated: 2026-08-19 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.306 $ | False | -17.09% | -10.19% | BEAR | -17.09% | -10.19% |
| DOGE-USD | BEAR | 0.07000 $ | False | -33.66% | -16.71% | BEAR | -17.09% | -10.19% |
| SOL-USD | BEAR | 76,92 $ | False | -11.82% | -16.78% | BEAR | -17.09% | -10.19% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 3.21% | 13.97% | 38.86% | -4.25% | -14.58% | 18.05% | 26.45% | 62.37% | 57.50% | 9.76% | 58.04% | 119.34% |
| BTC-USD | SAME_BTC_REGIME | 24 | 58.33% | 3.95% | 13.97% | 51.53% | -3.61% | -13.00% | 18.05% | 27.07% | 55.12% | 50.00% | 7.42% | 76.24% | 136.08% |
| BTC-USD | SAME_ASSET_REGIME | 24 | 58.33% | 6.46% | 13.97% | 50.45% | -4.25% | -14.25% | 19.93% | 24.94% | 54.43% | 54.17% | 17.30% | 76.24% | 136.08% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 60.00% | 6.46% | 13.97% | 62.37% | -2.91% | -11.13% | 18.05% | 24.94% | 62.37% | 55.00% | 30.91% | 89.88% | 145.42% |
| DOGE-USD | ALL_MATCHES | 40 | 70.00% | 14.92% | 33.28% | 49.81% | -8.68% | -20.80% | 26.44% | 37.65% | 57.06% | 35.00% | -7.60% | 6.28% | 84.98% |
| DOGE-USD | SAME_BTC_REGIME | 15 | 73.33% | 13.28% | 34.51% | 51.66% | -12.71% | -19.08% | 25.93% | 37.24% | 62.69% | 26.67% | -9.93% | -1.06% | 52.89% |
| DOGE-USD | SAME_ASSET_REGIME | 15 | 80.00% | 33.03% | 42.22% | 64.52% | -11.40% | -19.08% | 34.01% | 46.30% | 71.88% | 46.67% | -2.22% | 6.73% | 123.58% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 75.00% | 19.30% | 38.61% | 52.76% | -11.89% | -20.36% | 30.48% | 41.63% | 69.32% | 33.33% | -8.13% | 1.99% | 75.52% |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 3.63% | 20.74% | 67.54% | -3.41% | -10.42% | 16.24% | 30.37% | 94.20% | 62.50% | 12.51% | 48.37% | 145.71% |
| SOL-USD | SAME_BTC_REGIME | 15 | 66.67% | 3.09% | 27.42% | 82.58% | -3.47% | -9.15% | 18.10% | 47.45% | 90.39% | 40.00% | -7.07% | 75.53% | 124.62% |
| SOL-USD | SAME_ASSET_REGIME | 14 | 64.29% | 3.49% | 14.18% | 71.72% | -4.70% | -9.57% | 15.27% | 30.22% | 80.16% | 35.71% | -9.43% | 79.10% | 153.29% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 63.64% | 2.83% | 17.98% | 93.69% | -3.47% | -8.51% | 18.10% | 40.50% | 93.69% | 36.36% | -11.79% | 75.53% | 144.45% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 58.33% | 3.95% | -3.61% | 27.07% | 50.00% | 7.42% | 99.81% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 85.71% | 8.41% | -4.77% | 25.27% | 71.43% | 6.00% | 61.42% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 37.50% | -5.44% | -5.92% | 23.49% | 62.50% | 19.50% | 67.63% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 15 | 73.33% | 13.28% | -12.71% | 37.24% | 26.67% | -9.93% | 45.13% |
| DOGE-USD | HISTORICAL_BTC_BULL | 20 | 70.00% | 15.95% | -6.38% | 38.37% | 40.00% | -4.19% | 46.16% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -32.40% | -36.26% | 0.00% | 0.00% | -27.09% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 23.81% | -8.62% | 42.70% | 50.00% | -0.95% | 48.98% |
| SOL-USD | HISTORICAL_BTC_BEAR | 15 | 66.67% | 3.09% | -3.47% | 47.45% | 40.00% | -7.07% | 92.51% |
| SOL-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 8.53% | -6.83% | 29.44% | 50.00% | 2.78% | 29.44% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 19 | 57.89% | 2.71% | -1.75% | 24.71% | 84.21% | 25.36% | 68.26% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 24 | 58.33% | 6.46% | -4.25% | 24.94% | 54.17% | 17.30% | 125.80% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 85.71% | 8.41% | -4.77% | 38.29% | 71.43% | 6.00% | 83.39% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.46% | -17.03% | 27.03% | 0.00% | -24.07% | 28.66% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -5.44% | -5.92% | 13.58% | 66.67% | 19.50% | 61.52% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 15 | 80.00% | 33.03% | -11.40% | 46.30% | 46.67% | -2.22% | 58.34% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 12 | 75.00% | 15.95% | -0.31% | 38.37% | 33.33% | -4.19% | 45.27% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 23.86% | -5.61% | 51.52% | 100.00% | 29.43% | 63.46% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -4.93% | -15.36% | 14.35% | 0.00% | -23.94% | 17.95% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 14 | 64.29% | 3.49% | -4.70% | 30.22% | 35.71% | -9.43% | 105.92% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 34.36% | -8.74% | 73.97% | 66.67% | 21.54% | 188.18% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 60.00% | 3.09% | -7.94% | 25.79% | 60.00% | 6.51% | 29.69% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 17 | 58.82% | 2.71% | -1.75% | 26.85% | 82.35% | 21.82% | 66.99% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2026-01-10 | 88.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.44% | -2.44% | 6.41% | -17.87% | -21.60% | 6.41% |
| BTC-USD | NEO-USD | 2018-10-29 | 87.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 30.74% | -2.98% | 44.00% | 85.04% | -2.98% | 91.46% |
| BTC-USD | BTC-USD | 2018-10-27 | 86.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.48% | -1.86% | 19.59% | 42.11% | -1.86% | 43.56% |
| BTC-USD | ETH-USD | 2026-01-10 | 85.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| BTC-USD | OMG-USD | 2018-10-29 | 85.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.39% | -5.26% | 24.78% | 116.54% | -5.26% | 128.71% |
| BTC-USD | LTC-USD | 2018-10-27 | 84.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 58.89% | -1.51% | 58.89% | 154.14% | -1.51% | 154.14% |
| BTC-USD | SOL-USD | 2026-01-13 | 84.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.00% | -4.48% | 12.01% | -16.68% | -28.45% | 12.01% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 84.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | XTZ-USD | 2018-10-29 | 84.06% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 12.52% | -2.05% | 24.86% | 158.51% | -2.05% | 185.30% |
| BTC-USD | ETC-USD | 2018-10-29 | 83.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 13.49% | -2.84% | 25.18% | 54.96% | -2.84% | 54.96% |
| DOGE-USD | OP-USD | 2026-01-11 | 90.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | THETA-USD | 2022-03-31 | 86.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 34.01% | -12.38% | 34.01% | -13.72% | -13.72% | 34.01% |
| DOGE-USD | CHZ-USD | 2022-03-31 | 85.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 49.44% | -3.88% | 49.44% | 83.06% | -3.88% | 146.71% |
| DOGE-USD | ADA-USD | 2022-04-01 | 84.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.08% | -12.71% | 12.08% | 0.11% | -12.71% | 19.13% |
| DOGE-USD | ETH-USD | 2018-07-21 | 84.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -46.43% | -47.25% | 6.37% | -43.24% | -58.95% | 6.37% |
| DOGE-USD | FTM-USD | 2022-04-01 | 84.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 35.00% | -16.51% | 35.47% | -9.93% | -16.51% | 45.15% |
| DOGE-USD | XTZ-USD | 2026-01-10 | 83.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | LTC-USD | 2018-04-30 | 83.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -15.67% | -20.79% | 0.00% | -15.15% | -24.22% | 0.00% |
| DOGE-USD | BAT-USD | 2018-10-29 | 83.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 72.12% | 0.00% | 72.12% | 187.29% | 0.00% | 204.25% |
| DOGE-USD | FIL-USD | 2022-03-31 | 83.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 53.13% | -11.40% | 71.53% | -2.22% | -11.40% | 71.53% |
| SOL-USD | ENJ-USD | 2018-10-29 | 82.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 269.45% | -9.43% | 270.52% | 449.81% | -9.43% | 676.95% |
| SOL-USD | NEAR-USD | 2026-01-10 | 79.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 20.47% | -4.92% | 22.14% | 68.39% | -4.92% | 112.24% |
| SOL-USD | SOL-USD | 2026-01-13 | 77.06% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.00% | -4.48% | 12.01% | -16.68% | -28.45% | 12.01% |
| SOL-USD | LINK-USD | 2026-01-10 | 75.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | QTUM-USD | 2018-10-29 | 74.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.48% | -3.25% | 32.41% | 82.67% | -3.25% | 86.97% |
| SOL-USD | RUNE-USD | 2026-01-11 | 74.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | KAVA-USD | 2026-01-15 | 74.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.24% | -8.51% | 10.64% | -22.67% | -31.29% | 10.64% |
| SOL-USD | BTC-USD | 2026-01-13 | 74.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.47% | -3.47% | 5.03% | -19.14% | -22.17% | 5.03% |
| SOL-USD | BNB-USD | 2018-10-29 | 74.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 93.69% | -1.14% | 93.69% | 144.45% | -1.14% | 153.07% |
| SOL-USD | ETH-USD | 2026-01-10 | 73.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |

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

