# Market Regime Match Report

Generated: 2026-09-25 23:49 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-25 | RECOVERY | 84.065 $ | True | 40.25% | -1.48% | RECOVERY | 40.25% | -1.48% |
| DOGE-USD | 2026-09-25 | RECOVERY | 0.09899 $ | True | 33.00% | -8.83% | RECOVERY | 40.25% | -1.48% |
| SOL-USD | 2026-09-25 | RECOVERY | 122,13 $ | True | 73.45% | -3.56% | RECOVERY | 40.25% | -1.48% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 55.00% | 4.16% | 21.85% | 56.37% | -8.73% | -28.06% | 23.02% | 50.42% | 91.76% | 50.00% | 2.04% | 28.36% | 112.44% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -2.19% | -2.19% | -2.19% | -19.23% | -19.23% | 37.81% | 37.81% | 37.81% | 100.00% | 121.40% | 121.40% | 121.40% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 40.00% | -5.80% | 15.41% | 38.62% | -22.64% | -40.40% | 10.03% | 32.34% | 61.16% | 50.00% | -1.84% | 20.79% | 76.24% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | -1.44% | -0.08% | 0.74% | -11.34% | -16.87% | 19.04% | 24.83% | 28.30% | 50.00% | -3.33% | -1.21% | 0.06% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 47.50% | -4.42% | 17.79% | 68.19% | -17.40% | -33.30% | 19.15% | 43.99% | 90.52% | 45.00% | -2.87% | 25.79% | 75.64% |
| SOL-USD | SAME_BTC_REGIME | 2 | 100.00% | 27.53% | 38.66% | 45.34% | -4.07% | -4.48% | 66.00% | 87.87% | 100.99% | 100.00% | 21.75% | 31.82% | 37.86% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 50.00% | -15.95% | -7.33% | -2.17% | -21.28% | -34.77% | 15.31% | 22.96% | 27.56% | 50.00% | -7.13% | -3.11% | -0.70% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 63.64% | 14.17% | -9.21% | 55.48% | 54.55% | 7.15% | 67.02% |
| BTC-USD | HISTORICAL_BTC_BULL | 16 | 50.00% | 0.20% | -3.61% | 40.95% | 50.00% | 1.71% | 60.02% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -4.99% | -19.52% | 42.58% | 0.00% | -10.71% | 42.58% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 25.00% | -13.68% | -27.29% | 12.85% | 39.29% | -7.98% | 31.17% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 70.00% | 22.77% | -5.57% | 80.82% | 70.00% | 14.32% | 80.82% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 8.43% | -9.01% | 12.55% | 100.00% | 44.80% | 61.88% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 41.67% | -7.86% | -17.56% | 32.60% | 37.50% | -7.40% | 44.21% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 50.00% | -2.07% | -19.42% | 50.52% | 50.00% | 4.65% | 83.47% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 100.00% | 27.53% | -4.07% | 87.87% | 100.00% | 21.75% | 87.87% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 60.61% | 6.68% | -4.22% | 50.37% | 51.52% | 6.55% | 62.32% |
| BTC-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 34.16% | -11.52% | 139.12% | 50.00% | 49.71% | 191.10% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -18.39% | -23.29% | 7.44% | 0.00% | -7.73% | 7.44% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -2.19% | -19.23% | 37.81% | 100.00% | 121.40% | 202.07% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 28 | 32.14% | -13.68% | -26.50% | 17.44% | 39.29% | -7.12% | 49.68% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 8.32% | -15.95% | 67.94% | 87.50% | 24.65% | 107.84% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -10.73% | -21.77% | 10.70% | 50.00% | -5.09% | 13.39% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -1.44% | -11.34% | 24.83% | 50.00% | -3.33% | 24.83% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 48.39% | -1.11% | -17.02% | 40.20% | 41.94% | -4.88% | 50.91% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -8.02% | -21.06% | 66.30% | 66.67% | 41.89% | 89.23% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 1.17% | -17.56% | 60.62% | 50.00% | 23.34% | 147.79% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -15.95% | -21.28% | 22.96% | 50.00% | -7.13% | 22.96% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 0 | 2 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

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

