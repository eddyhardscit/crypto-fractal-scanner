# Market Regime Match Report

Generated: 2026-09-06 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-06 | RECOVERY | 79.859 $ | True | 26.58% | -6.28% | RECOVERY | 26.58% | -6.28% |
| DOGE-USD | 2026-09-06 | MIXED | 0.09084 $ | True | 5.28% | -13.38% | RECOVERY | 26.58% | -6.28% |
| SOL-USD | 2026-09-06 | RECOVERY | 106,09 $ | True | 58.83% | -11.17% | RECOVERY | 26.58% | -6.28% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 87.50% | 13.97% | 38.32% | 62.68% | -11.01% | -28.63% | 24.92% | 47.44% | 82.03% | 82.50% | 20.21% | 49.44% | 93.83% |
| BTC-USD | SAME_BTC_REGIME | 2 | 100.00% | 37.08% | 38.15% | 38.79% | -16.91% | -19.90% | 40.97% | 43.98% | 45.79% | 100.00% | 95.96% | 108.29% | 115.69% |
| BTC-USD | SAME_ASSET_REGIME | 4 | 75.00% | 19.06% | 100.51% | 218.51% | -14.83% | -18.92% | 22.97% | 104.83% | 230.63% | 75.00% | 8.66% | 24.46% | 52.56% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 34.95% | 34.95% | 34.95% | -20.65% | -20.65% | 34.95% | 34.95% | 34.95% | 100.00% | 71.29% | 71.29% | 71.29% |
| DOGE-USD | ALL_MATCHES | 40 | 35.00% | -11.98% | 2.10% | 33.17% | -18.50% | -32.86% | 11.29% | 25.01% | 47.43% | 35.00% | -10.41% | 12.21% | 44.19% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -16.46% | -16.46% | -16.46% | -18.64% | -18.64% | 9.17% | 9.17% | 9.17% | 0.00% | -21.13% | -21.13% | -21.13% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 15.91% | 43.51% | 100.44% | -12.84% | -42.07% | 26.02% | 56.45% | 112.75% | 67.50% | 26.34% | 86.25% | 153.03% |
| SOL-USD | SAME_BTC_REGIME | 2 | 50.00% | 41.26% | 70.22% | 87.60% | -13.78% | -18.08% | 60.66% | 90.99% | 109.19% | 100.00% | 74.80% | 95.71% | 108.26% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 21.27% | 38.18% | 40.84% | -9.58% | -19.79% | 38.14% | 40.97% | 43.45% | 100.00% | 45.40% | 65.73% | 79.96% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -16.66% | -16.66% | -16.66% | -19.15% | -19.15% | 0.00% | 0.00% | 0.00% | 100.00% | 32.97% | 32.97% | 32.97% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 9 | 77.78% | 24.82% | -18.90% | 56.23% | 77.78% | 32.84% | 71.26% |
| BTC-USD | HISTORICAL_BTC_BULL | 29 | 89.66% | 13.46% | -10.09% | 45.80% | 82.76% | 18.05% | 78.94% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 100.00% | 37.08% | -16.91% | 43.98% | 100.00% | 95.96% | 113.86% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 12 | 25.00% | -14.21% | -20.97% | 18.05% | 16.67% | -19.09% | 18.75% |
| DOGE-USD | HISTORICAL_BTC_BULL | 19 | 47.37% | -1.55% | -11.95% | 33.70% | 52.63% | 6.33% | 48.07% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 8 | 25.00% | -20.76% | -30.13% | 37.60% | 25.00% | -10.01% | 37.60% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -16.46% | -18.64% | 9.17% | 0.00% | -21.13% | 9.17% |
| SOL-USD | HISTORICAL_BTC_BEAR | 16 | 62.50% | 23.70% | -13.65% | 55.19% | 62.50% | 28.43% | 95.60% |
| SOL-USD | HISTORICAL_BTC_BULL | 16 | 87.50% | 38.25% | -10.00% | 75.61% | 87.50% | 27.80% | 179.85% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 6 | 16.67% | -19.55% | -21.40% | 31.12% | 16.67% | -15.73% | 31.76% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 41.26% | -13.78% | 90.99% | 100.00% | 74.80% | 117.56% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 30 | 90.00% | 15.40% | -10.39% | 46.69% | 86.67% | 20.21% | 69.18% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 12.19% | -14.99% | 50.31% | 66.67% | 100.34% | 172.07% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 19.06% | -14.83% | 104.83% | 75.00% | 8.66% | 132.09% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 12 | 41.67% | -5.89% | -14.07% | 18.84% | 33.33% | -10.52% | 29.01% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 24 | 33.33% | -16.86% | -24.08% | 36.87% | 33.33% | -14.76% | 47.17% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -23.58% | -23.58% | 33.50% | 66.67% | 6.81% | 33.50% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -31.12% | -33.14% | 0.00% | 0.00% | -53.85% | 0.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 60.71% | 13.97% | -11.16% | 53.08% | 60.71% | 19.36% | 73.87% |
| SOL-USD | HISTORICAL_ASSET_BULL | 8 | 75.00% | 62.23% | -16.62% | 205.02% | 75.00% | 94.85% | 205.02% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 21.27% | -9.58% | 40.97% | 100.00% | 45.40% | 78.01% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 1 | 4 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
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

