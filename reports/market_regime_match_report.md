# Market Regime Match Report

Generated: 2026-09-24 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-24 | RECOVERY | 84.184 $ | True | 40.27% | -1.90% | RECOVERY | 40.27% | -1.90% |
| DOGE-USD | 2026-09-24 | RECOVERY | 0.09448 $ | True | 24.87% | -9.23% | RECOVERY | 40.27% | -1.90% |
| SOL-USD | 2026-09-24 | RECOVERY | 115,45 $ | True | 60.71% | -4.32% | RECOVERY | 40.27% | -1.90% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 8.51% | 25.00% | 64.90% | -4.44% | -32.79% | 23.46% | 50.91% | 95.32% | 60.00% | 8.32% | 35.61% | 118.00% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 24.99% | 29.42% | 32.08% | -13.94% | -16.12% | 48.48% | 51.63% | 53.52% | 100.00% | 154.75% | 183.20% | 200.26% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -7.20% | 3.45% | 55.15% | -22.77% | -61.13% | 9.04% | 20.78% | 61.16% | 57.50% | 3.52% | 20.34% | 58.38% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | 25.78% | 40.75% | 49.73% | -9.13% | -16.43% | 31.59% | 43.65% | 50.89% | 50.00% | 2.59% | 7.67% | 10.72% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | 0.30% | 22.87% | 68.64% | -14.57% | -35.17% | 14.20% | 51.03% | 80.76% | 45.00% | -0.81% | 23.93% | 141.43% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 2 | 0.00% | -36.54% | -34.86% | -33.85% | -44.39% | -49.38% | 0.00% | 0.00% | 0.00% | 0.00% | -36.06% | -25.62% | -19.35% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 66.67% | 10.99% | -3.65% | 42.51% | 54.17% | 3.64% | 56.21% |
| BTC-USD | HISTORICAL_BTC_BULL | 15 | 66.67% | 5.85% | -9.97% | 50.47% | 66.67% | 10.15% | 159.15% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 14.06% | 0.00% | 92.34% | 100.00% | 10.26% | 92.34% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 17.86% | -13.96% | -25.26% | 12.78% | 50.00% | -1.98% | 31.64% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 66.67% | 23.20% | -6.32% | 88.39% | 77.78% | 16.91% | 88.39% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -2.17% | -25.24% | 8.41% | 66.67% | 0.79% | 42.74% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 45.45% | -4.23% | -18.09% | 36.44% | 36.36% | -5.11% | 54.97% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 58.82% | 5.85% | -3.00% | 52.43% | 58.82% | 9.69% | 103.78% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -11.89% | -21.59% | 0.76% | 0.00% | -28.06% | 0.76% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 70.97% | 7.73% | -1.10% | 44.87% | 58.06% | 7.58% | 53.39% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 78.30% | -10.65% | 148.83% | 80.00% | 111.45% | 280.80% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -19.23% | -25.62% | 3.81% | 0.00% | -10.12% | 3.81% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 24.99% | -13.94% | 51.63% | 100.00% | 154.75% | 185.40% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 27 | 18.52% | -14.25% | -25.24% | 17.77% | 48.15% | -5.35% | 26.51% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 9 | 66.67% | 4.72% | -12.58% | 58.13% | 100.00% | 29.97% | 59.24% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -47.71% | -51.80% | 0.00% | 0.00% | -33.65% | 0.00% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -49.55% | -68.95% | 4.40% | 0.00% | -65.63% | 4.40% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 25.78% | -9.13% | 43.65% | 50.00% | 2.59% | 43.65% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 32 | 50.00% | 0.30% | -14.57% | 41.49% | 40.62% | -2.87% | 52.50% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 7.79% | -5.54% | 64.30% | 100.00% | 9.69% | 78.10% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 17.79% | -12.33% | 65.42% | 66.67% | 56.67% | 151.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -36.54% | -44.39% | 0.00% | 0.00% | -36.06% | 0.00% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

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

