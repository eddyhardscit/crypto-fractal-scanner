# Market Regime Match Report

Generated: 2026-08-09 05:15 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.728 $ | False | -20.79% | -10.08% | BEAR | -20.79% | -10.08% |
| DOGE-USD | BEAR | 0.06997 $ | False | -37.15% | -16.69% | BEAR | -20.79% | -10.08% |
| SOL-USD | BEAR | 75,95 $ | False | -22.02% | -17.09% | BEAR | -20.79% | -10.08% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 85.00% | 11.66% | 16.10% | 25.20% | -1.69% | -15.72% | 18.09% | 35.60% | 51.41% | 60.00% | 17.79% | 56.64% | 77.93% |
| BTC-USD | SAME_BTC_REGIME | 17 | 94.12% | 9.21% | 15.64% | 18.23% | -3.46% | -13.36% | 15.04% | 17.64% | 26.01% | 35.29% | -10.68% | 24.79% | 78.17% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 95.65% | 14.08% | 16.81% | 23.50% | -1.76% | -11.35% | 16.09% | 33.21% | 42.27% | 52.17% | 10.06% | 47.68% | 74.72% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 17 | 94.12% | 9.21% | 15.64% | 18.23% | -3.46% | -13.36% | 15.04% | 17.64% | 26.01% | 35.29% | -10.68% | 24.79% | 78.17% |
| DOGE-USD | ALL_MATCHES | 40 | 70.00% | 15.34% | 34.28% | 54.15% | -9.85% | -29.83% | 22.03% | 38.74% | 64.95% | 47.50% | -1.32% | 21.40% | 82.47% |
| DOGE-USD | SAME_BTC_REGIME | 23 | 91.30% | 21.57% | 41.72% | 58.15% | -8.37% | -16.36% | 23.68% | 46.98% | 69.93% | 56.52% | 3.42% | 16.92% | 72.79% |
| DOGE-USD | SAME_ASSET_REGIME | 20 | 95.00% | 22.10% | 43.01% | 59.78% | -6.56% | -11.98% | 23.85% | 53.12% | 72.75% | 60.00% | 4.22% | 27.68% | 82.47% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 94.44% | 20.89% | 29.77% | 55.29% | -7.39% | -12.96% | 23.55% | 30.02% | 66.38% | 55.56% | 3.25% | 16.66% | 53.53% |
| SOL-USD | ALL_MATCHES | 40 | 80.00% | 12.10% | 21.52% | 59.02% | -3.61% | -15.94% | 18.03% | 35.43% | 85.21% | 55.00% | 12.57% | 62.11% | 158.66% |
| SOL-USD | SAME_BTC_REGIME | 19 | 100.00% | 15.64% | 24.87% | 58.24% | -2.30% | -16.15% | 24.86% | 50.41% | 72.00% | 57.89% | 25.81% | 96.56% | 158.81% |
| SOL-USD | SAME_ASSET_REGIME | 20 | 90.00% | 14.17% | 22.80% | 42.97% | -2.24% | -18.67% | 20.03% | 49.10% | 79.90% | 55.00% | 20.82% | 107.60% | 158.66% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 100.00% | 15.12% | 22.80% | 49.53% | -2.24% | -16.78% | 22.13% | 49.10% | 67.59% | 56.25% | 35.43% | 127.78% | 159.27% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 17 | 94.12% | 9.21% | -3.46% | 17.64% | 35.29% | -10.68% | 39.96% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 70.00% | 11.29% | -0.86% | 49.58% | 70.00% | 37.68% | 78.16% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 7 | 100.00% | 14.66% | 0.00% | 37.29% | 100.00% | 34.16% | 48.10% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 66.67% | 13.44% | -4.08% | 26.70% | 66.67% | 46.17% | 74.24% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 91.30% | 21.57% | -8.37% | 46.98% | 56.52% | 3.42% | 67.80% |
| DOGE-USD | HISTORICAL_BTC_BULL | 14 | 42.86% | -2.48% | -18.42% | 29.09% | 28.57% | -22.95% | 29.09% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 11.10% | 0.00% | 36.94% | 100.00% | 19.41% | 36.94% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -22.31% | -27.36% | 0.00% | 50.00% | 61.06% | 119.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 100.00% | 15.64% | -2.30% | 50.41% | 57.89% | 25.81% | 115.09% |
| SOL-USD | HISTORICAL_BTC_BULL | 5 | 40.00% | -6.28% | -8.34% | 22.81% | 40.00% | -6.36% | 35.74% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 4.13% | 0.00% | 55.80% | 100.00% | 15.82% | 65.94% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 104.48% | -3.96% | 120.09% | 100.00% | 307.28% | 352.55% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 58.33% | 1.05% | -4.46% | 25.40% | 41.67% | -0.43% | 51.41% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 95.65% | 14.08% | -1.76% | 33.21% | 52.17% | 10.06% | 51.90% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 85.71% | 11.20% | -0.49% | 47.23% | 85.71% | 19.41% | 179.06% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 40.15% | -2.38% | 86.65% | 100.00% | 35.59% | 90.23% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 3.93% | -1.63% | 11.57% | 100.00% | 3.48% | 11.57% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 42.86% | -0.51% | -4.58% | 25.07% | 42.86% | -0.85% | 59.90% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 20 | 95.00% | 22.10% | -6.56% | 53.12% | 60.00% | 4.22% | 72.58% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 6 | 33.33% | -21.97% | -25.04% | 24.69% | 50.00% | 2.32% | 35.32% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 8.09% | -25.85% | 33.24% | 50.00% | -8.23% | 42.98% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 28.93% | -8.73% | 51.06% | 50.00% | -13.78% | 51.06% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -2.48% | -17.07% | 20.32% | 20.00% | -26.13% | 20.32% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 20 | 90.00% | 14.17% | -2.24% | 49.10% | 55.00% | 20.82% | 110.70% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 21.27% | -11.21% | 55.93% | 66.67% | 19.19% | 215.36% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 10.69% | -4.20% | 43.70% | 50.00% | 4.81% | 53.40% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 4 | 50.00% | 0.13% | -3.01% | 12.11% | 50.00% | 1.71% | 12.89% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 9 | 77.78% | 11.93% | -3.96% | 31.31% | 55.56% | 47.21% | 71.56% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-31 | 90.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.65% | -1.42% | 9.89% | -13.09% | -18.65% | 10.41% |
| BTC-USD | ETH-USD | 2025-12-31 | 90.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.28% | 0.00% | 10.59% | -22.79% | -28.34% | 10.59% |
| BTC-USD | OMG-USD | 2018-10-19 | 88.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.73% | -17.83% | 7.53% | 45.05% | -17.83% | 45.05% |
| BTC-USD | BTC-USD | 2018-10-17 | 88.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.04% | -5.59% | 15.04% | 10.06% | -5.59% | 15.04% |
| BTC-USD | NEO-USD | 2018-10-19 | 87.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.31% | -8.94% | 35.16% | 24.79% | -8.94% | 35.16% |
| BTC-USD | XTZ-USD | 2018-10-19 | 87.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 4.87% | -11.35% | 13.01% | 76.63% | -11.35% | 102.96% |
| BTC-USD | SOL-USD | 2026-01-03 | 86.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| BTC-USD | QTUM-USD | 2025-12-31 | 86.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.54% | -6.19% | 5.05% | -23.02% | -25.42% | 13.74% |
| BTC-USD | BTC-USD | 2026-01-03 | 86.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.74% | 0.00% | 16.09% | -10.17% | -13.97% | 16.09% |
| BTC-USD | XTZ-USD | 2026-01-05 | 86.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.21% | 0.00% | 15.85% | -31.20% | -34.31% | 15.85% |
| DOGE-USD | OP-USD | 2026-01-01 | 91.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.98% | -7.10% | 49.82% | -15.88% | -18.56% | 49.82% |
| DOGE-USD | VET-USD | 2022-03-24 | 90.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.63% | -3.05% | 23.68% | 9.84% | -3.05% | 50.90% |
| DOGE-USD | ADA-USD | 2022-03-22 | 90.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.42% | -10.22% | 12.42% | -7.62% | -10.22% | 22.52% |
| DOGE-USD | BAT-USD | 2018-10-19 | 89.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.64% | -16.39% | 17.64% | 80.49% | -16.39% | 80.49% |
| DOGE-USD | NEO-USD | 2022-03-22 | 89.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 31.89% | -6.02% | 31.89% | 3.42% | -6.02% | 39.93% |
| DOGE-USD | DASH-USD | 2022-03-22 | 89.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.27% | -10.11% | 17.74% | -0.65% | -10.11% | 27.95% |
| DOGE-USD | QTUM-USD | 2022-07-25 | 88.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -21.47% | -29.34% | 7.38% | -34.87% | -34.93% | 7.38% |
| DOGE-USD | THETA-USD | 2022-03-26 | 88.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.01% | -10.28% | 22.09% | -4.02% | -10.28% | 37.23% |
| DOGE-USD | HBAR-USD | 2022-03-24 | 88.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 23.41% | -3.18% | 23.41% | 3.08% | -3.18% | 34.66% |
| DOGE-USD | FIL-USD | 2022-03-26 | 88.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 53.58% | -4.32% | 85.24% | 8.64% | -4.32% | 85.24% |
| SOL-USD | ENJ-USD | 2018-10-19 | 84.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 130.26% | -26.20% | 130.26% | 394.56% | -26.20% | 533.03% |
| SOL-USD | NEAR-USD | 2025-12-31 | 81.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.61% | -7.58% | 16.66% | 55.80% | -7.58% | 106.31% |
| SOL-USD | EOS-USD | 2018-10-29 | 80.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 58.60% | -1.80% | 78.67% | 123.88% | -1.80% | 123.88% |
| SOL-USD | QTUM-USD | 2018-10-19 | 80.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.74% | -15.73% | 15.32% | 25.81% | -15.73% | 31.28% |
| SOL-USD | RUNE-USD | 2026-01-06 | 79.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.91% | 0.00% | 53.03% | -4.33% | -22.03% | 53.03% |
| SOL-USD | SOL-USD | 2026-01-03 | 78.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| SOL-USD | LINK-USD | 2025-12-31 | 78.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.98% | -2.30% | 15.98% | -10.68% | -17.80% | 19.79% |
| SOL-USD | DOT-USD | 2025-12-31 | 77.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.56% | -10.35% | 5.52% | -25.10% | -27.46% | 6.36% |
| SOL-USD | KAVA-USD | 2026-01-05 | 77.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.58% | 0.00% | 30.18% | -12.71% | -19.16% | 30.18% |
| SOL-USD | XTZ-USD | 2018-10-29 | 76.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 12.52% | -2.05% | 24.86% | 158.51% | -2.05% | 185.30% |

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

