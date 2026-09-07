# Market Regime Match Report

Generated: 2026-09-07 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-07 | RECOVERY | 79.818 $ | True | 29.48% | -6.03% | RECOVERY | 29.48% | -6.03% |
| DOGE-USD | 2026-09-07 | MIXED | 0.09020 $ | True | 6.38% | -13.18% | RECOVERY | 29.48% | -6.03% |
| SOL-USD | 2026-09-07 | RECOVERY | 105,54 $ | True | 62.46% | -10.83% | RECOVERY | 29.48% | -6.03% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 85.00% | 18.09% | 38.07% | 71.21% | -10.00% | -36.52% | 24.81% | 53.09% | 87.93% | 80.00% | 20.60% | 44.50% | 93.83% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | 142.18% | 219.68% | 266.18% | -8.51% | -13.62% | 160.82% | 237.65% | 283.75% | 50.00% | -18.01% | -4.58% | 3.48% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -15.20% | 1.00% | 10.88% | -24.26% | -33.16% | 10.62% | 18.05% | 35.52% | 30.00% | -8.03% | 6.67% | 33.27% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 19.90% | 47.65% | 103.57% | -12.84% | -42.28% | 26.02% | 58.22% | 127.78% | 65.00% | 26.34% | 79.29% | 153.03% |
| SOL-USD | SAME_BTC_REGIME | 2 | 50.00% | 41.26% | 70.22% | 87.60% | -13.78% | -18.08% | 60.66% | 90.99% | 109.19% | 100.00% | 74.80% | 95.71% | 108.26% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 39.66% | 81.40% | 151.20% | -12.81% | -19.79% | 40.90% | 118.23% | 249.84% | 100.00% | 61.21% | 116.05% | 163.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -16.66% | -16.66% | -16.66% | -19.15% | -19.15% | 0.00% | 0.00% | 0.00% | 100.00% | 32.97% | 32.97% | 32.97% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 11 | 81.82% | 25.26% | -11.06% | 71.04% | 81.82% | 32.86% | 97.85% |
| BTC-USD | HISTORICAL_BTC_BULL | 29 | 86.21% | 13.76% | -9.12% | 45.80% | 79.31% | 18.05% | 82.45% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 14 | 28.57% | -11.98% | -17.35% | 20.50% | 14.29% | -15.24% | 20.73% |
| DOGE-USD | HISTORICAL_BTC_BULL | 14 | 42.86% | -2.92% | -18.78% | 11.16% | 50.00% | 0.96% | 48.39% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 11 | 18.18% | -22.03% | -30.53% | 23.72% | 27.27% | -7.28% | 23.72% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 64.71% | 22.36% | -13.77% | 54.85% | 58.82% | 29.33% | 93.12% |
| SOL-USD | HISTORICAL_BTC_BULL | 16 | 87.50% | 43.00% | -8.88% | 75.61% | 87.50% | 27.80% | 179.85% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 0.00% | -18.80% | -21.80% | 18.94% | 0.00% | -12.77% | 21.48% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 41.26% | -13.78% | 90.99% | 100.00% | 74.80% | 117.56% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 90.32% | 20.77% | -8.74% | 49.31% | 87.10% | 22.02% | 72.74% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 10.93% | -15.83% | 39.28% | 57.14% | 85.18% | 166.29% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 142.18% | -8.51% | 237.65% | 50.00% | -18.01% | 247.17% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 14 | 28.57% | -6.43% | -16.12% | 15.78% | 14.29% | -13.80% | 18.90% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 22 | 31.82% | -19.34% | -27.18% | 20.48% | 36.36% | -7.63% | 44.18% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -23.58% | -23.58% | 33.50% | 66.67% | 6.81% | 33.50% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -31.12% | -33.14% | 0.00% | 0.00% | -53.85% | 0.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 14.38% | -11.06% | 54.85% | 62.07% | 22.02% | 81.70% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 62.23% | -16.62% | 159.65% | 66.67% | 63.47% | 183.86% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -9.69% | -21.80% | 11.27% | 0.00% | -9.57% | 11.27% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 39.66% | -12.81% | 118.23% | 100.00% | 61.21% | 161.67% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 0 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 1 | 4 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

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

