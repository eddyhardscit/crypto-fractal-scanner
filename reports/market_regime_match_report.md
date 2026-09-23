# Market Regime Match Report

Generated: 2026-09-23 10:18 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-23 | RECOVERY | 85.837 $ | True | 43.73% | -2.07% | RECOVERY | 43.73% | -2.07% |
| DOGE-USD | 2026-09-23 | RECOVERY | 0.09968 $ | True | 33.29% | -9.55% | RECOVERY | 43.73% | -2.07% |
| SOL-USD | 2026-09-23 | RECOVERY | 117,38 $ | True | 73.71% | -4.63% | RECOVERY | 43.73% | -2.07% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 11.54% | 22.56% | 64.90% | -3.04% | -32.79% | 25.04% | 50.68% | 95.32% | 62.50% | 9.28% | 32.28% | 118.00% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 16.13% | 16.13% | 16.13% | -16.67% | -16.67% | 42.17% | 42.17% | 42.17% | 100.00% | 211.64% | 211.64% | 211.64% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -5.98% | 6.54% | 55.15% | -23.61% | -61.13% | 9.04% | 24.41% | 62.45% | 55.00% | 2.34% | 21.11% | 58.38% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | 25.78% | 40.75% | 49.73% | -9.13% | -16.43% | 31.59% | 43.65% | 50.89% | 50.00% | 2.59% | 7.67% | 10.72% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 1.77% | 25.96% | 68.64% | -14.57% | -35.17% | 16.56% | 53.28% | 86.83% | 45.00% | -0.81% | 29.65% | 141.43% |
| SOL-USD | SAME_BTC_REGIME | 1 | 100.00% | 48.11% | 48.11% | 48.11% | -6.40% | -6.40% | 82.91% | 82.91% | 82.91% | 100.00% | 41.79% | 41.79% | 41.79% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -33.18% | 7.46% | 31.85% | -38.14% | -48.13% | 0.00% | 41.45% | 66.33% | 33.33% | -15.17% | 13.31% | 30.40% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 48.11% | 48.11% | 48.11% | -6.40% | -6.40% | 82.91% | 82.91% | 82.91% | 100.00% | 41.79% | 41.79% | 41.79% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 25 | 68.00% | 13.78% | -5.77% | 39.37% | 56.00% | 5.63% | 56.22% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 71.43% | 6.26% | -2.37% | 50.52% | 71.43% | 10.24% | 171.91% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 14.06% | 0.00% | 92.34% | 100.00% | 10.26% | 92.34% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 20.69% | -13.67% | -26.87% | 12.71% | 44.83% | -5.41% | 34.46% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 66.67% | 23.20% | -6.91% | 88.39% | 77.78% | 16.91% | 88.39% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 6.55% | -19.43% | 11.84% | 100.00% | 39.38% | 60.36% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 47.62% | -7.99% | -18.11% | 38.52% | 33.33% | -5.35% | 56.21% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 58.82% | 5.85% | -3.00% | 52.43% | 58.82% | 9.69% | 103.78% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -11.89% | -21.59% | 0.76% | 0.00% | -28.06% | 0.76% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 100.00% | 48.11% | -6.40% | 82.91% | 100.00% | 41.79% | 82.91% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 72.73% | 9.30% | -1.45% | 50.37% | 60.61% | 7.75% | 56.21% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 78.30% | -10.65% | 148.83% | 80.00% | 111.45% | 280.80% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -17.13% | -27.45% | 1.89% | 0.00% | -14.77% | 1.89% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 16.13% | -16.67% | 42.17% | 100.00% | 211.64% | 211.64% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 27 | 18.52% | -14.25% | -26.87% | 15.36% | 40.74% | -5.85% | 26.51% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 10 | 70.00% | 8.36% | -13.46% | 59.21% | 100.00% | 26.58% | 59.48% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -49.55% | -68.95% | 4.40% | 0.00% | -65.63% | 4.40% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 25.78% | -9.13% | 43.65% | 50.00% | 2.59% | 43.65% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 51.61% | 1.06% | -15.93% | 44.45% | 38.71% | -4.88% | 53.73% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 7.79% | -5.54% | 64.30% | 100.00% | 9.69% | 78.10% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 17.79% | -12.33% | 65.42% | 66.67% | 56.67% | 151.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -33.18% | -38.14% | 41.45% | 33.33% | -15.17% | 41.45% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 1 | 3 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

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

