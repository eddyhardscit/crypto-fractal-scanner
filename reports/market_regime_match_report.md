# Market Regime Match Report

Generated: 2026-09-03 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-03 | RECOVERY | 77.186 $ | True | 26.69% | -6.97% | RECOVERY | 26.69% | -6.97% |
| DOGE-USD | 2026-09-03 | RECOVERY | 0.08221 $ | False | 1.04% | -13.87% | RECOVERY | 26.69% | -6.97% |
| SOL-USD | 2026-09-03 | RECOVERY | 99,93 $ | True | 57.40% | -12.09% | RECOVERY | 26.69% | -6.97% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 77.50% | 8.92% | 18.74% | 37.73% | -12.59% | -33.32% | 16.03% | 27.75% | 49.06% | 67.50% | 9.58% | 36.38% | 88.21% |
| BTC-USD | SAME_BTC_REGIME | 3 | 100.00% | 29.98% | 34.60% | 37.37% | -7.00% | -11.94% | 46.99% | 74.76% | 91.42% | 100.00% | 71.86% | 96.24% | 110.87% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 16.58% | 23.28% | 27.30% | -9.13% | -13.64% | 56.76% | 79.64% | 93.37% | 100.00% | 21.63% | 28.21% | 32.15% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 29.98% | 29.98% | 29.98% | -3.49% | -3.49% | 102.52% | 102.52% | 102.52% | 100.00% | 34.79% | 34.79% | 34.79% |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -9.01% | 1.80% | 36.07% | -11.98% | -31.85% | 15.74% | 31.64% | 50.84% | 30.00% | -10.99% | 13.54% | 54.07% |
| DOGE-USD | SAME_BTC_REGIME | 2 | 0.00% | -25.91% | -21.18% | -18.35% | -27.18% | -34.00% | 4.59% | 6.88% | 8.26% | 0.00% | -37.99% | -29.56% | -24.50% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -8.06% | -8.06% | -8.06% | -15.42% | -15.42% | 6.21% | 6.21% | 6.21% | 0.00% | -5.35% | -5.35% | -5.35% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 12.24% | 48.73% | 102.20% | -11.45% | -38.27% | 24.66% | 66.96% | 126.49% | 72.50% | 26.67% | 93.72% | 147.77% |
| SOL-USD | SAME_BTC_REGIME | 4 | 100.00% | 53.26% | 77.75% | 96.54% | -9.89% | -18.41% | 72.79% | 105.36% | 117.54% | 100.00% | 131.30% | 179.95% | 248.30% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 100.00% | 19.06% | 27.01% | 31.77% | -17.71% | -20.06% | 22.97% | 28.96% | 32.55% | 100.00% | 39.88% | 55.58% | 65.01% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 34.95% | 34.95% | 34.95% | -20.65% | -20.65% | 34.95% | 34.95% | 34.95% | 100.00% | 71.29% | 71.29% | 71.29% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 4 | 25.00% | -29.04% | -33.79% | 35.78% | 25.00% | -23.36% | 35.78% |
| BTC-USD | HISTORICAL_BTC_BULL | 33 | 81.82% | 8.57% | -12.25% | 24.01% | 69.70% | 8.47% | 47.53% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 29.98% | -7.00% | 74.76% | 100.00% | 71.86% | 115.28% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 12 | 16.67% | -10.62% | -18.43% | 17.43% | 16.67% | -30.33% | 21.77% |
| DOGE-USD | HISTORICAL_BTC_BULL | 25 | 36.00% | -3.67% | -8.86% | 36.34% | 40.00% | -3.99% | 42.65% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -22.55% | -29.68% | 11.81% | 0.00% | -1.73% | 11.81% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -25.91% | -27.18% | 6.88% | 0.00% | -37.99% | 6.88% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 50.00% | -1.09% | -12.57% | 48.57% | 64.29% | 14.21% | 69.28% |
| SOL-USD | HISTORICAL_BTC_BULL | 18 | 94.44% | 25.97% | -9.92% | 83.31% | 88.89% | 34.55% | 158.70% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 0.00% | -27.96% | -32.42% | 12.15% | 0.00% | -31.96% | 12.15% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 4 | 100.00% | 53.26% | -9.89% | 105.36% | 100.00% | 131.30% | 183.28% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 30 | 76.67% | 8.00% | -12.44% | 28.40% | 63.33% | 5.88% | 47.05% |
| BTC-USD | HISTORICAL_ASSET_BULL | 8 | 75.00% | 12.19% | -12.59% | 21.02% | 75.00% | 56.63% | 146.33% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 16.58% | -9.13% | 79.64% | 100.00% | 21.63% | 85.12% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 15 | 6.67% | -16.46% | -22.77% | 13.82% | 13.33% | -32.52% | 17.88% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 23 | 39.13% | -3.67% | -8.86% | 36.46% | 39.13% | -3.77% | 43.05% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 125.28% | 0.00% | 128.29% | 100.00% | 81.09% | 149.46% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -8.06% | -15.42% | 6.21% | 0.00% | -5.35% | 14.02% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 62.07% | 6.00% | -10.03% | 46.99% | 65.52% | 16.71% | 68.64% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 68.48% | -12.89% | 158.70% | 83.33% | 103.76% | 175.12% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 101.43% | -6.61% | 113.55% | 100.00% | 141.97% | 267.26% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 19.06% | -17.71% | 28.96% | 100.00% | 39.88% | 61.69% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 1 | 2 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 1 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 1 | 2 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

_No data._

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the preferred and most stringent filter.
- Below 5 full-regime matches, the selector falls back first to SAME_ASSET_REGIME and then to SAME_BTC_REGIME.
- A fallback is always labelled as less stringent; groups are never combined.
- If every group is below threshold, the result is INSUFFICIENT_REGIME_MATCHES.
- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.
- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.

## Regime definitions

- BULL: price above MA200, MA200 rising, positive 90d trend.
- BEAR: price below MA200, MA200 falling, weak 90d trend.
- RECOVERY: improving 90d trend, but not yet a clean bull structure.
- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.
- MIXED: unclear regime.
- UNKNOWN: not enough historical data.

