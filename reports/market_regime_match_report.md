# Market Regime Match Report

Generated: 2026-09-22 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-22 | RECOVERY | 85.204 $ | True | 39.69% | -2.53% | RECOVERY | 39.69% | -2.53% |
| DOGE-USD | 2026-09-22 | RECOVERY | 0.09884 $ | True | 30.03% | -10.01% | RECOVERY | 39.69% | -2.53% |
| SOL-USD | 2026-09-22 | RECOVERY | 115,88 $ | True | 70.46% | -5.39% | RECOVERY | 39.69% | -2.53% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 12.86% | 24.16% | 65.80% | -2.37% | -27.51% | 27.52% | 50.42% | 93.60% | 65.00% | 7.67% | 31.10% | 121.18% |
| BTC-USD | SAME_BTC_REGIME | 1 | 0.00% | -14.59% | -14.59% | -14.59% | -15.40% | -15.40% | 25.18% | 25.18% | 25.18% | 0.00% | -30.63% | -30.63% | -30.63% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 33.33% | -14.59% | 0.77% | 9.99% | -16.67% | -25.77% | 25.18% | 33.68% | 38.78% | 33.33% | -17.92% | 96.86% | 165.73% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -14.59% | -14.59% | -14.59% | -15.40% | -15.40% | 25.18% | 25.18% | 25.18% | 0.00% | -30.63% | -30.63% | -30.63% |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -8.65% | 5.95% | 49.73% | -20.21% | -62.08% | 14.92% | 22.48% | 57.85% | 60.00% | 3.10% | 16.75% | 48.72% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 3 | 33.33% | -17.66% | 19.03% | 41.04% | -18.81% | -39.85% | 6.73% | 31.22% | 45.92% | 33.33% | -17.15% | -2.20% | 6.77% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 55.00% | 5.22% | 34.88% | 75.86% | -12.70% | -35.39% | 22.81% | 56.89% | 115.84% | 55.00% | 5.26% | 36.06% | 141.43% |
| SOL-USD | SAME_BTC_REGIME | 1 | 100.00% | 58.51% | 58.51% | 58.51% | -2.78% | -2.78% | 115.14% | 115.14% | 115.14% | 100.00% | 31.94% | 31.94% | 31.94% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 0.00% | -35.88% | -33.87% | -32.66% | -44.33% | -49.37% | 0.09% | 0.14% | 0.17% | 0.00% | -36.88% | -26.84% | -20.82% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 25 | 76.00% | 13.78% | -1.10% | 45.75% | 60.00% | 1.82% | 56.21% |
| BTC-USD | HISTORICAL_BTC_BULL | 13 | 61.54% | 6.68% | -10.65% | 50.37% | 76.92% | 10.15% | 211.64% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 14.06% | 0.00% | 92.34% | 100.00% | 10.26% | 92.34% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -14.59% | -15.40% | 25.18% | 0.00% | -30.63% | 25.18% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 26.67% | -13.42% | -20.42% | 21.01% | 50.00% | -1.37% | 22.83% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -1.90% | -14.26% | 57.66% | 88.89% | 28.59% | 195.62% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 4.17% | -11.25% | 12.06% | 100.00% | 55.90% | 55.90% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 50.00% | 2.07% | -13.81% | 42.20% | 45.83% | -3.05% | 56.21% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 69.23% | 7.79% | -5.54% | 76.16% | 69.23% | 10.15% | 197.82% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -11.93% | -17.96% | 16.61% | 50.00% | -11.17% | 16.61% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 100.00% | 58.51% | -2.78% | 115.14% | 100.00% | 31.94% | 115.14% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 75.86% | 13.78% | -1.04% | 50.37% | 68.97% | 7.75% | 56.21% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 47.12% | -5.93% | 137.84% | 83.33% | 60.57% | 217.75% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -17.13% | -27.45% | 1.89% | 0.00% | -14.77% | 1.89% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -18.84% | -22.70% | 5.96% | 0.00% | -12.90% | 5.96% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -14.59% | -16.67% | 33.68% | 33.33% | -17.92% | 118.41% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 24 | 20.83% | -13.42% | -20.36% | 20.81% | 54.17% | 0.45% | 23.61% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 10 | 60.00% | 13.63% | -17.27% | 59.09% | 80.00% | 25.90% | 161.61% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -3.66% | -13.60% | 21.37% | 100.00% | 26.40% | 40.62% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -49.55% | -68.95% | 4.40% | 0.00% | -65.63% | 4.40% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -17.66% | -18.81% | 31.22% | 33.33% | -17.15% | 31.22% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 55.17% | 4.60% | -13.08% | 50.57% | 48.28% | -0.75% | 56.22% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 34.78% | -5.54% | 115.14% | 100.00% | 31.94% | 115.14% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 2.90% | -13.33% | 60.62% | 75.00% | 31.20% | 147.79% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -35.88% | -44.33% | 0.14% | 0.00% | -36.88% | 0.14% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 1 | 3 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 0 | 2 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

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

