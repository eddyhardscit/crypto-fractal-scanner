# Market Regime Match Report

Generated: 2026-09-25 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-25 | RECOVERY | 84.151 $ | True | 40.39% | -1.59% | RECOVERY | 40.39% | -1.59% |
| DOGE-USD | 2026-09-25 | RECOVERY | 0.09506 $ | True | 27.72% | -8.87% | RECOVERY | 40.39% | -1.59% |
| SOL-USD | 2026-09-25 | RECOVERY | 116,42 $ | True | 65.34% | -3.77% | RECOVERY | 40.39% | -1.59% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 11.38% | 25.56% | 64.90% | -2.44% | -24.19% | 27.00% | 51.23% | 81.18% | 57.50% | 8.32% | 41.52% | 130.55% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 16.13% | 16.13% | 16.13% | -16.67% | -16.67% | 42.17% | 42.17% | 42.17% | 100.00% | 211.64% | 211.64% | 211.64% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -5.50% | 5.21% | 38.62% | -24.49% | -52.69% | 7.40% | 27.42% | 61.16% | 55.00% | 1.15% | 17.79% | 51.27% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | -1.44% | -0.08% | 0.74% | -11.34% | -16.87% | 19.04% | 24.83% | 28.30% | 50.00% | -3.33% | -1.21% | 0.06% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 1.17% | 18.94% | 68.64% | -11.95% | -32.67% | 20.78% | 50.42% | 110.98% | 45.00% | -2.87% | 21.16% | 141.43% |
| SOL-USD | SAME_BTC_REGIME | 2 | 100.00% | 27.53% | 38.66% | 45.34% | -4.07% | -4.48% | 66.00% | 87.87% | 100.99% | 100.00% | 21.75% | 31.82% | 37.86% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 50.00% | -15.95% | -7.33% | -2.17% | -21.28% | -34.77% | 15.31% | 22.96% | 27.56% | 50.00% | -7.13% | -3.11% | -0.70% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 79.17% | 15.36% | -1.54% | 56.64% | 62.50% | 11.93% | 64.01% |
| BTC-USD | HISTORICAL_BTC_BULL | 15 | 66.67% | 5.85% | -3.00% | 46.27% | 53.33% | 8.88% | 88.12% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.76% | -19.86% | 38.61% | 0.00% | -2.68% | 38.61% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 27 | 18.52% | -13.67% | -27.70% | 10.69% | 40.74% | -8.39% | 24.08% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 80.00% | 20.51% | -2.98% | 80.82% | 80.00% | 13.62% | 80.82% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 66.67% | 1.60% | -13.62% | 9.84% | 100.00% | 11.63% | 45.78% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 38.10% | -7.99% | -18.11% | 30.62% | 28.57% | -10.53% | 30.62% |
| SOL-USD | HISTORICAL_BTC_BULL | 16 | 62.50% | 5.84% | -3.61% | 53.28% | 56.25% | 9.45% | 105.67% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.77% | 0.00% | 30.86% | 100.00% | 101.23% | 116.77% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 100.00% | 27.53% | -4.07% | 87.87% | 100.00% | 21.75% | 87.87% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 78.12% | 11.38% | -1.16% | 50.42% | 59.38% | 8.32% | 57.75% |
| BTC-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 34.16% | -11.52% | 139.12% | 50.00% | 49.71% | 191.10% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -18.39% | -23.29% | 7.44% | 0.00% | -7.73% | 7.44% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 42.78% | -3.04% | 69.02% | 100.00% | 125.39% | 125.68% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 16.13% | -16.67% | 42.17% | 100.00% | 211.64% | 211.64% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 28 | 28.57% | -12.55% | -26.50% | 23.33% | 42.86% | -7.12% | 36.63% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 3.87% | -20.13% | 67.94% | 100.00% | 30.97% | 108.67% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 1.60% | -4.41% | 4.40% | 100.00% | 11.63% | 13.59% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -49.55% | -68.95% | 4.40% | 0.00% | -65.63% | 4.40% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -1.44% | -11.34% | 24.83% | 50.00% | -3.33% | 24.83% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 32 | 50.00% | 0.20% | -12.39% | 39.36% | 40.62% | -5.11% | 50.74% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 28.79% | -4.55% | 95.42% | 100.00% | 25.32% | 95.42% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 1.17% | -17.56% | 60.62% | 50.00% | 25.60% | 147.79% |
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

