# Market Regime Match Report

Generated: 2026-08-10 05:16 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.946 $ | False | -19.27% | -10.10% | BEAR | -19.27% | -10.10% |
| DOGE-USD | BEAR | 0.06971 $ | False | -36.64% | -16.72% | BEAR | -19.27% | -10.10% |
| SOL-USD | BEAR | 76,55 $ | False | -18.77% | -17.09% | BEAR | -19.27% | -10.10% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 82.50% | 10.75% | 19.10% | 40.22% | -1.97% | -15.72% | 17.19% | 37.70% | 56.34% | 57.50% | 16.09% | 61.57% | 102.18% |
| BTC-USD | SAME_BTC_REGIME | 20 | 90.00% | 8.56% | 16.14% | 19.64% | -4.95% | -13.51% | 14.05% | 19.53% | 35.64% | 45.00% | -6.91% | 52.95% | 102.18% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 91.30% | 10.40% | 19.10% | 31.45% | -3.53% | -13.10% | 16.75% | 33.72% | 49.66% | 56.52% | 12.77% | 63.13% | 97.22% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 89.47% | 7.90% | 16.64% | 20.16% | -5.56% | -13.83% | 15.08% | 19.66% | 36.12% | 47.37% | -13.09% | 60.84% | 102.95% |
| DOGE-USD | ALL_MATCHES | 40 | 72.50% | 18.93% | 41.30% | 54.15% | -9.09% | -29.88% | 23.55% | 45.55% | 64.95% | 52.50% | 1.97% | 19.06% | 82.47% |
| DOGE-USD | SAME_BTC_REGIME | 24 | 91.67% | 23.28% | 41.59% | 57.58% | -7.73% | -16.35% | 24.38% | 50.17% | 69.22% | 58.33% | 3.25% | 11.10% | 64.92% |
| DOGE-USD | SAME_ASSET_REGIME | 21 | 90.48% | 23.14% | 41.98% | 59.29% | -6.02% | -16.39% | 24.34% | 51.20% | 71.36% | 57.14% | 3.08% | 18.94% | 80.49% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 89.47% | 22.63% | 34.99% | 54.72% | -7.10% | -18.98% | 23.68% | 40.85% | 65.67% | 52.63% | 0.86% | 9.24% | 38.96% |
| SOL-USD | ALL_MATCHES | 40 | 80.00% | 12.10% | 21.52% | 59.02% | -3.51% | -15.66% | 18.03% | 30.47% | 85.21% | 52.50% | 7.85% | 59.45% | 158.66% |
| SOL-USD | SAME_BTC_REGIME | 18 | 100.00% | 15.81% | 26.67% | 58.29% | -2.50% | -15.03% | 26.08% | 43.39% | 72.83% | 55.56% | 22.50% | 66.76% | 158.96% |
| SOL-USD | SAME_ASSET_REGIME | 19 | 89.47% | 14.61% | 24.69% | 44.71% | -2.30% | -17.83% | 20.66% | 39.00% | 81.12% | 52.63% | 15.82% | 80.77% | 158.81% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 15 | 100.00% | 15.64% | 24.69% | 47.05% | -2.30% | -13.58% | 24.86% | 39.00% | 68.41% | 53.33% | 25.81% | 91.61% | 159.42% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 20 | 90.00% | 8.56% | -4.95% | 19.53% | 45.00% | -6.91% | 53.91% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 70.00% | 12.60% | -0.51% | 55.20% | 70.00% | 41.72% | 147.38% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 14.66% | 0.00% | 44.16% | 100.00% | 30.43% | 45.98% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 2.62% | -3.44% | 9.51% | 0.00% | -0.06% | 9.51% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 66.67% | 13.44% | -2.01% | 26.70% | 66.67% | 48.67% | 74.24% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 24 | 91.67% | 23.28% | -7.73% | 50.17% | 58.33% | 3.25% | 66.02% |
| DOGE-USD | HISTORICAL_BTC_BULL | 13 | 46.15% | -0.45% | -12.34% | 42.72% | 38.46% | -16.07% | 63.02% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 11.10% | 0.00% | 36.94% | 100.00% | 19.41% | 36.94% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -22.31% | -27.36% | 0.00% | 50.00% | 61.06% | 119.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 18 | 100.00% | 15.81% | -2.50% | 43.39% | 55.56% | 22.50% | 104.72% |
| SOL-USD | HISTORICAL_BTC_BULL | 6 | 33.33% | -4.27% | -12.77% | 6.36% | 33.33% | -7.53% | 13.65% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 22.68% | 0.00% | 73.37% | 100.00% | 59.00% | 84.06% |
| SOL-USD | HISTORICAL_BTC_MIXED | 2 | 100.00% | 53.55% | -3.70% | 92.45% | 50.00% | 153.61% | 266.79% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 66.67% | 3.55% | -3.98% | 27.45% | 50.00% | 7.36% | 51.41% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 91.30% | 10.40% | -3.53% | 33.72% | 56.52% | 12.77% | 74.60% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 11.20% | -0.49% | 51.82% | 80.00% | 74.76% | 283.35% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 10.41% | 0.00% | 66.41% | 66.67% | 7.83% | 68.90% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 55.56% | 2.62% | -3.57% | 25.33% | 44.44% | -0.06% | 64.01% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 21 | 90.48% | 23.14% | -6.02% | 51.20% | 57.14% | 3.08% | 71.36% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 40.00% | -23.38% | -28.70% | 36.94% | 60.00% | 5.92% | 42.72% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 36.77% | -11.51% | 42.76% | 100.00% | 9.69% | 61.11% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 28.93% | -8.73% | 51.06% | 50.00% | -13.78% | 51.06% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -1.50% | -12.62% | 20.32% | 30.00% | -22.34% | 64.60% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 19 | 89.47% | 14.61% | -2.30% | 39.00% | 52.63% | 15.82% | 104.24% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 42.06% | -7.25% | 70.25% | 100.00% | 157.49% | 290.44% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 37.13% | -2.38% | 82.38% | 50.00% | 17.91% | 84.01% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 3 | 33.33% | -3.67% | -4.39% | 9.71% | 33.33% | -0.05% | 11.28% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 14 | 71.43% | 4.65% | -4.25% | 28.04% | 50.00% | 0.43% | 59.81% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ETH-USD | 2025-12-31 | 88.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.28% | 0.00% | 10.59% | -22.79% | -28.34% | 10.59% |
| BTC-USD | BTC-USD | 2018-10-18 | 88.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.85% | -5.56% | 15.08% | 10.70% | -5.56% | 15.08% |
| BTC-USD | XRP-USD | 2025-12-31 | 88.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.65% | -1.42% | 9.89% | -13.09% | -18.65% | 10.41% |
| BTC-USD | OMG-USD | 2018-10-19 | 87.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.73% | -17.83% | 7.53% | 45.05% | -17.83% | 45.05% |
| BTC-USD | NEO-USD | 2018-10-19 | 87.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.31% | -8.94% | 35.16% | 24.79% | -8.94% | 35.16% |
| BTC-USD | SOL-USD | 2026-01-03 | 87.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| BTC-USD | XTZ-USD | 2026-01-05 | 86.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.21% | 0.00% | 15.85% | -31.20% | -34.31% | 15.85% |
| BTC-USD | 1INCH-USD | 2024-07-06 | 86.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 19.12% | -11.35% | 19.92% | 101.40% | -11.35% | 137.19% |
| BTC-USD | XTZ-USD | 2018-10-19 | 86.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 4.87% | -11.35% | 13.01% | 76.63% | -11.35% | 102.96% |
| BTC-USD | 1INCH-USD | 2026-01-02 | 86.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.40% | -2.51% | 11.14% | -26.00% | -27.22% | 11.14% |
| DOGE-USD | OP-USD | 2026-01-01 | 91.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.98% | -7.10% | 49.82% | -15.88% | -18.56% | 49.82% |
| DOGE-USD | VET-USD | 2022-03-24 | 90.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.63% | -3.05% | 23.68% | 9.84% | -3.05% | 50.90% |
| DOGE-USD | ADA-USD | 2022-03-22 | 90.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.42% | -10.22% | 12.42% | -7.62% | -10.22% | 22.52% |
| DOGE-USD | BAT-USD | 2018-10-19 | 89.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.64% | -16.39% | 17.64% | 80.49% | -16.39% | 80.49% |
| DOGE-USD | DASH-USD | 2022-03-22 | 89.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.27% | -10.11% | 17.74% | -0.65% | -10.11% | 27.95% |
| DOGE-USD | NEO-USD | 2022-03-22 | 89.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 31.89% | -6.02% | 31.89% | 3.42% | -6.02% | 39.93% |
| DOGE-USD | LTC-USD | 2018-04-21 | 89.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.05% | -35.78% | 0.00% | -25.10% | -38.57% | 0.00% |
| DOGE-USD | XTZ-USD | 2026-01-05 | 88.56% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.21% | 0.00% | 15.85% | -31.20% | -34.31% | 15.85% |
| DOGE-USD | QTUM-USD | 2022-07-25 | 88.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -21.47% | -29.34% | 7.38% | -34.87% | -34.93% | 7.38% |
| DOGE-USD | FIL-USD | 2022-03-26 | 88.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 53.58% | -4.32% | 85.24% | 8.64% | -4.32% | 85.24% |
| SOL-USD | ENJ-USD | 2018-10-19 | 85.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 130.26% | -26.20% | 130.26% | 394.56% | -26.20% | 533.03% |
| SOL-USD | RUNE-USD | 2026-01-06 | 80.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.91% | 0.00% | 53.03% | -4.33% | -22.03% | 53.03% |
| SOL-USD | EOS-USD | 2018-10-29 | 80.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 58.60% | -1.80% | 78.67% | 123.88% | -1.80% | 123.88% |
| SOL-USD | NEAR-USD | 2025-12-31 | 80.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.61% | -7.58% | 16.66% | 55.80% | -7.58% | 106.31% |
| SOL-USD | QTUM-USD | 2018-10-19 | 79.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.74% | -15.73% | 15.32% | 25.81% | -15.73% | 31.28% |
| SOL-USD | SOL-USD | 2026-01-03 | 79.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| SOL-USD | KAVA-USD | 2026-01-05 | 78.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.58% | 0.00% | 30.18% | -12.71% | -19.16% | 30.18% |
| SOL-USD | XTZ-USD | 2018-10-29 | 77.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 12.52% | -2.05% | 24.86% | 158.51% | -2.05% | 185.30% |
| SOL-USD | XTZ-USD | 2025-03-11 | 77.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 29.72% | -7.89% | 29.72% | 59.35% | -7.89% | 99.97% |
| SOL-USD | BTC-USD | 2026-01-04 | 76.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.43% | -0.84% | 10.28% | -14.69% | -18.28% | 10.28% |

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

