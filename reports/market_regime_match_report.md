# Market Regime Match Report

Generated: 2026-09-23 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-23 | RECOVERY | 86.751 $ | True | 45.26% | -2.19% | RECOVERY | 45.26% | -2.19% |
| DOGE-USD | 2026-09-23 | RECOVERY | 0.10210 $ | True | 36.52% | -9.59% | RECOVERY | 45.26% | -2.19% |
| SOL-USD | 2026-09-23 | RECOVERY | 118,95 $ | True | 76.03% | -4.82% | RECOVERY | 45.26% | -2.19% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 75.00% | 13.91% | 26.98% | 64.90% | -1.59% | -28.19% | 27.00% | 50.68% | 95.32% | 65.00% | 9.28% | 32.28% | 118.00% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 16.13% | 16.13% | 16.13% | -16.67% | -16.67% | 42.17% | 42.17% | 42.17% | 100.00% | 211.64% | 211.64% | 211.64% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -8.60% | 3.32% | 33.24% | -20.36% | -62.08% | 11.31% | 26.39% | 58.27% | 60.00% | 3.10% | 18.77% | 63.06% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | 19.03% | 37.37% | 48.38% | -9.41% | -16.93% | 31.22% | 43.47% | 50.82% | 50.00% | -2.20% | 5.28% | 9.76% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 2.40% | 25.96% | 68.64% | -12.70% | -34.86% | 18.46% | 53.28% | 86.83% | 47.50% | -0.46% | 29.65% | 141.43% |
| SOL-USD | SAME_BTC_REGIME | 1 | 100.00% | 48.11% | 48.11% | 48.11% | -6.40% | -6.40% | 82.91% | 82.91% | 82.91% | 100.00% | 41.79% | 41.79% | 41.79% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 50.00% | 4.10% | 26.10% | 39.31% | -28.52% | -46.21% | 41.45% | 62.18% | 74.62% | 50.00% | -7.58% | 17.10% | 31.92% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 48.11% | 48.11% | 48.11% | -6.40% | -6.40% | 82.91% | 82.91% | 82.91% | 100.00% | 41.79% | 41.79% | 41.79% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 25 | 72.00% | 13.78% | -1.45% | 45.75% | 56.00% | 1.26% | 56.21% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 78.57% | 11.41% | -2.37% | 50.52% | 78.57% | 11.02% | 182.87% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 14.06% | 0.00% | 92.34% | 100.00% | 10.26% | 92.34% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 17.24% | -14.25% | -21.73% | 21.83% | 51.72% | 0.60% | 30.70% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 23.72% | -7.87% | 67.94% | 87.50% | 32.42% | 210.96% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -2.17% | -25.24% | 6.80% | 66.67% | 0.79% | 31.70% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 40.00% | -8.84% | -19.67% | 32.26% | 35.00% | -6.13% | 52.50% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 70.59% | 7.79% | -2.25% | 55.83% | 64.71% | 10.15% | 157.53% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -9.40% | -18.64% | 0.68% | 0.00% | -27.51% | 0.68% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 100.00% | 48.11% | -6.40% | 82.91% | 100.00% | 41.79% | 82.91% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 75.00% | 11.54% | -1.17% | 50.42% | 62.50% | 7.67% | 53.58% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 78.30% | -10.65% | 148.83% | 80.00% | 111.45% | 280.80% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -17.13% | -27.45% | 1.89% | 0.00% | -14.77% | 1.89% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 26.20% | -15.55% | 47.22% | 100.00% | 96.56% | 96.56% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 16.13% | -16.67% | 42.17% | 100.00% | 211.64% | 211.64% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 25 | 16.00% | -12.29% | -20.47% | 21.83% | 52.00% | 0.60% | 24.95% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 10 | 60.00% | 13.63% | -17.27% | 59.21% | 90.00% | 26.58% | 161.61% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -29.45% | -32.80% | 16.93% | 50.00% | 7.47% | 36.18% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -49.55% | -68.95% | 4.40% | 0.00% | -65.63% | 4.40% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 19.03% | -9.41% | 43.47% | 50.00% | -2.20% | 43.47% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 50.00% | 0.30% | -14.50% | 36.86% | 40.00% | -3.10% | 51.09% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 21.28% | -8.10% | 94.33% | 100.00% | 54.32% | 205.19% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 5.44% | -14.01% | 60.62% | 50.00% | 20.95% | 147.79% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 4.10% | -28.52% | 62.18% | 50.00% | -7.58% | 62.18% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 1 | 2 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

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

