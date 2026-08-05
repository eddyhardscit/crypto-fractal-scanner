# Market Regime Match Report

Generated: 2026-08-05 05:15 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.258 $ | False | -19.69% | -9.93% | BEAR | -19.69% | -9.93% |
| DOGE-USD | BEAR | 0.06992 $ | False | -35.13% | -16.51% | BEAR | -19.69% | -9.93% |
| SOL-USD | BEAR | 73,91 $ | False | -16.41% | -16.97% | BEAR | -19.69% | -9.93% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 9.97% | 20.39% | 41.22% | -4.78% | -20.52% | 14.34% | 31.72% | 52.72% | 50.00% | 4.07% | 37.04% | 81.05% |
| BTC-USD | SAME_BTC_REGIME | 18 | 88.89% | 9.57% | 10.31% | 15.97% | -4.02% | -16.08% | 11.08% | 16.54% | 46.67% | 33.33% | -11.06% | 13.24% | 44.83% |
| BTC-USD | SAME_ASSET_REGIME | 22 | 90.91% | 9.63% | 13.39% | 39.07% | -3.41% | -14.40% | 12.06% | 34.54% | 50.40% | 45.45% | -4.48% | 36.56% | 76.99% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 88.89% | 9.57% | 10.31% | 15.97% | -4.02% | -16.08% | 11.08% | 16.54% | 46.67% | 33.33% | -11.06% | 13.24% | 44.83% |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 4.72% | 17.08% | 30.12% | -13.85% | -28.37% | 12.20% | 23.00% | 31.53% | 50.00% | 0.31% | 18.71% | 82.99% |
| DOGE-USD | SAME_BTC_REGIME | 26 | 61.54% | 6.69% | 16.60% | 25.62% | -13.85% | -24.29% | 9.47% | 21.62% | 29.78% | 50.00% | 0.31% | 13.88% | 52.16% |
| DOGE-USD | SAME_ASSET_REGIME | 24 | 66.67% | 7.34% | 16.77% | 27.59% | -13.69% | -18.20% | 9.47% | 20.36% | 30.54% | 54.17% | 1.43% | 33.72% | 89.54% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 22 | 63.64% | 6.69% | 15.12% | 17.72% | -13.85% | -18.22% | 8.09% | 17.65% | 23.85% | 50.00% | 0.31% | 12.02% | 60.30% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 8.72% | 23.11% | 51.67% | -3.67% | -25.16% | 12.12% | 26.42% | 59.08% | 55.00% | 5.47% | 51.12% | 127.77% |
| SOL-USD | SAME_BTC_REGIME | 17 | 76.47% | 7.22% | 12.74% | 35.88% | -3.86% | -24.56% | 10.72% | 22.40% | 49.67% | 47.06% | -0.20% | 32.48% | 138.27% |
| SOL-USD | SAME_ASSET_REGIME | 27 | 74.07% | 7.60% | 21.32% | 44.78% | -3.86% | -25.33% | 11.62% | 26.24% | 53.54% | 51.85% | 2.39% | 55.46% | 107.36% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 81.25% | 7.41% | 15.24% | 38.51% | -3.67% | -19.65% | 11.17% | 23.20% | 50.01% | 43.75% | -1.61% | 44.62% | 141.78% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 88.89% | 9.57% | -4.02% | 16.54% | 33.33% | -11.06% | 33.43% |
| BTC-USD | HISTORICAL_BTC_BULL | 13 | 69.23% | 16.96% | -5.08% | 50.41% | 61.54% | 28.24% | 69.91% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 3.24% | -10.73% | 14.18% | 100.00% | 109.39% | 115.00% |
| BTC-USD | HISTORICAL_BTC_MIXED | 6 | 83.33% | 15.94% | -2.63% | 25.96% | 66.67% | 21.48% | 46.11% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 20.57% | -15.48% | 80.74% | 50.00% | 8.10% | 80.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 26 | 61.54% | 6.69% | -13.85% | 21.62% | 50.00% | 0.31% | 56.29% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 50.00% | 3.43% | -10.21% | 29.38% | 50.00% | -0.62% | 58.41% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 25.00% | -14.40% | -19.80% | 19.71% | 50.00% | 1.68% | 46.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 76.47% | 7.22% | -3.86% | 22.40% | 47.06% | -0.20% | 56.14% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -10.37% | -12.90% | 56.32% | 44.44% | -7.92% | 69.91% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 28.98% | 0.00% | 76.01% | 100.00% | 96.08% | 233.92% |
| SOL-USD | HISTORICAL_BTC_MIXED | 9 | 100.00% | 12.97% | -2.60% | 25.03% | 77.78% | 8.35% | 38.00% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -26.16% | -27.30% | 1.90% | 0.00% | -29.07% | 1.90% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 22 | 90.91% | 9.63% | -3.41% | 34.54% | 45.45% | -4.48% | 49.87% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 66.67% | 15.05% | -6.13% | 35.54% | 55.56% | 12.03% | 35.54% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 63.84% | -4.76% | 106.37% | 100.00% | 36.55% | 106.37% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 25.21% | -2.65% | 30.40% | 100.00% | 47.58% | 47.58% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 12.72% | -4.75% | 20.17% | 42.86% | -0.32% | 28.92% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 24 | 66.67% | 7.34% | -13.69% | 20.36% | 54.17% | 1.43% | 59.76% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | -0.60% | -13.36% | 30.92% | 50.00% | 4.85% | 68.75% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 35.55% | -7.36% | 43.09% | 100.00% | 16.24% | 72.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 20.00% | -12.87% | -22.92% | 18.66% | 30.00% | -11.64% | 27.85% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 74.07% | 7.60% | -3.86% | 26.24% | 51.85% | 2.39% | 78.03% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 42.91% | -12.23% | 70.27% | 100.00% | 166.06% | 324.13% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -15.08% | -16.46% | 15.30% | 33.33% | -15.06% | 19.19% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 8 | 87.50% | 12.85% | -2.92% | 25.34% | 62.50% | 5.47% | 44.00% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ETH-USD | 2025-12-26 | 88.77% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.61% | 0.00% | 17.22% | -12.28% | -12.28% | 17.22% |
| BTC-USD | BTC-USD | 2018-10-13 | 88.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.61% | -5.60% | 9.61% | 11.89% | -5.60% | 15.04% |
| BTC-USD | XRP-USD | 2025-12-26 | 87.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.81% | 0.00% | 12.27% | -8.77% | -8.77% | 12.81% |
| BTC-USD | OMG-USD | 2018-10-14 | 87.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.30% | -19.94% | 4.30% | 30.65% | -19.94% | 30.65% |
| BTC-USD | BNB-USD | 2025-12-31 | 87.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| BTC-USD | XTZ-USD | 2025-12-31 | 87.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| BTC-USD | SOL-USD | 2025-12-29 | 87.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| BTC-USD | BTC-USD | 2025-12-30 | 87.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.74% | -0.52% | 14.49% | -11.08% | -14.42% | 15.49% |
| BTC-USD | XTZ-USD | 2018-10-14 | 87.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 9.53% | -14.08% | 9.53% | 77.90% | -14.08% | 96.71% |
| BTC-USD | NEO-USD | 2018-10-14 | 86.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 21.47% | -9.47% | 21.47% | 21.84% | -9.47% | 34.36% |
| DOGE-USD | OP-USD | 2025-12-27 | 90.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.75% | -2.92% | 22.25% | 1.62% | -2.92% | 56.55% |
| DOGE-USD | VET-USD | 2022-03-19 | 90.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.00% | -11.66% | 7.24% | 10.13% | -11.66% | 37.50% |
| DOGE-USD | DASH-USD | 2022-03-17 | 89.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.39% | -22.75% | 0.95% | -6.32% | -22.75% | 9.96% |
| DOGE-USD | ETC-USD | 2022-03-17 | 89.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 56.33% | -15.35% | 59.00% | 109.41% | -15.35% | 165.75% |
| DOGE-USD | LTC-USD | 2018-04-16 | 89.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -35.55% | -39.52% | 0.00% | -32.31% | -42.14% | 0.00% |
| DOGE-USD | NEO-USD | 2022-03-17 | 89.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.51% | -16.44% | 8.94% | 2.89% | -16.44% | 24.41% |
| DOGE-USD | XTZ-USD | 2025-12-31 | 89.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| DOGE-USD | MKR-USD | 2022-10-04 | 89.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.99% | -0.27% | 24.02% | 41.98% | -0.27% | 48.95% |
| DOGE-USD | ADA-USD | 2022-03-17 | 89.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.92% | -16.28% | 3.63% | -6.81% | -16.28% | 14.25% |
| DOGE-USD | BAT-USD | 2018-10-14 | 88.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.84% | -13.62% | 17.16% | 62.34% | -13.62% | 69.37% |
| SOL-USD | ENJ-USD | 2018-10-14 | 84.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.62% | -25.10% | 11.62% | 465.84% | -25.10% | 542.51% |
| SOL-USD | NEAR-USD | 2025-12-26 | 80.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 0.47% | -0.75% | 14.11% | 124.27% | -0.75% | 124.27% |
| SOL-USD | RUNE-USD | 2026-01-01 | 80.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 51.69% | -4.54% | 51.69% | -3.02% | -20.45% | 56.14% |
| SOL-USD | QTUM-USD | 2018-10-14 | 79.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.45% | -14.45% | 6.45% | 24.60% | -14.45% | 33.28% |
| SOL-USD | BNB-USD | 2025-12-31 | 79.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| SOL-USD | SOL-USD | 2025-12-29 | 78.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| SOL-USD | KAVA-USD | 2025-12-31 | 78.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.73% | -3.48% | 25.59% | -18.69% | -20.93% | 27.22% |
| SOL-USD | EOS-USD | 2018-10-24 | 77.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.66% | 0.00% | 83.90% | 81.05% | 0.00% | 86.15% |
| SOL-USD | LINK-USD | 2025-12-26 | 76.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.60% | 0.00% | 10.72% | -4.12% | -4.12% | 23.23% |
| SOL-USD | BTC-USD | 2025-12-30 | 76.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.74% | -0.52% | 14.49% | -11.08% | -14.42% | 15.49% |

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

