# Market Regime Match Report

Generated: 2026-09-26 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-26 | RECOVERY | 83.923 $ | True | 40.97% | -1.30% | RECOVERY | 40.97% | -1.30% |
| DOGE-USD | 2026-09-26 | RECOVERY | 0.09745 $ | True | 33.32% | -8.50% | RECOVERY | 40.97% | -1.30% |
| SOL-USD | 2026-09-26 | RECOVERY | 120,40 $ | True | 68.83% | -3.22% | RECOVERY | 40.97% | -1.30% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 47.50% | -1.71% | 18.78% | 42.50% | -13.71% | -28.15% | 20.34% | 39.93% | 65.81% | 45.00% | -5.03% | 20.61% | 92.43% |
| BTC-USD | SAME_BTC_REGIME | 3 | 66.67% | 7.98% | 19.05% | 25.70% | -4.53% | -22.26% | 27.49% | 28.81% | 29.60% | 66.67% | 18.94% | 24.41% | 27.69% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 0.00% | -8.93% | -5.56% | -3.54% | -22.96% | -25.94% | 30.88% | 34.34% | 36.42% | 50.00% | 48.08% | 84.74% | 106.74% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -15.67% | -15.67% | -15.67% | -26.69% | -26.69% | 23.95% | 23.95% | 23.95% | 0.00% | -25.25% | -25.25% | -25.25% |
| DOGE-USD | ALL_MATCHES | 40 | 40.00% | -5.80% | 10.47% | 38.62% | -20.13% | -35.62% | 10.04% | 25.95% | 86.39% | 47.50% | -4.59% | 16.78% | 51.08% |
| DOGE-USD | SAME_BTC_REGIME | 2 | 50.00% | 3.85% | 11.35% | 15.85% | -9.47% | -17.04% | 26.15% | 31.88% | 35.31% | 50.00% | -2.84% | 2.19% | 5.21% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | -1.44% | -0.08% | 0.74% | -11.34% | -16.87% | 19.04% | 24.83% | 28.30% | 50.00% | -3.33% | -1.21% | 0.06% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 42.50% | -7.88% | 10.75% | 55.27% | -17.95% | -33.30% | 16.17% | 33.54% | 87.24% | 40.00% | -8.91% | 27.14% | 74.08% |
| SOL-USD | SAME_BTC_REGIME | 5 | 60.00% | 5.27% | 30.13% | 41.93% | -4.59% | -14.86% | 22.25% | 30.13% | 77.90% | 60.00% | 1.61% | 29.88% | 37.09% |
| SOL-USD | SAME_ASSET_REGIME | 1 | 0.00% | -33.18% | -33.18% | -33.18% | -38.14% | -38.14% | 0.00% | 0.00% | 0.00% | 0.00% | -15.17% | -15.17% | -15.17% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 50.00% | -1.04% | -14.61% | 52.35% | 50.00% | 1.44% | 66.27% |
| BTC-USD | HISTORICAL_BTC_BULL | 11 | 45.45% | -2.19% | -2.45% | 37.73% | 36.36% | -8.02% | 50.47% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -4.99% | -19.52% | 42.58% | 0.00% | -10.71% | 42.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 66.67% | 7.98% | -4.53% | 28.81% | 66.67% | 18.94% | 40.00% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 31.03% | -7.99% | -23.46% | 20.11% | 44.83% | -5.35% | 30.62% |
| DOGE-USD | HISTORICAL_BTC_BULL | 7 | 57.14% | 1.06% | -6.88% | 106.72% | 42.86% | -5.85% | 110.24% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 9.74% | -8.26% | 12.97% | 100.00% | 45.68% | 62.33% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 3.85% | -9.47% | 31.88% | 50.00% | -2.84% | 31.88% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 38.10% | -10.94% | -18.70% | 38.52% | 33.33% | -10.53% | 47.91% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 42.86% | -8.80% | -19.42% | 29.73% | 42.86% | -9.05% | 83.47% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 5 | 60.00% | 5.27% | -4.59% | 30.13% | 60.00% | 1.61% | 46.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 34 | 52.94% | 1.77% | -12.07% | 42.58% | 47.06% | -3.78% | 50.52% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -9.97% | -9.97% | 80.26% | 33.33% | -12.03% | 80.26% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -15.45% | -22.78% | 8.44% | 0.00% | -9.99% | 8.44% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -8.93% | -22.96% | 34.34% | 50.00% | 48.08% | 157.54% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 31 | 32.26% | -10.94% | -23.46% | 21.21% | 41.94% | -5.85% | 37.55% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 8.32% | -13.76% | 106.96% | 66.67% | 15.77% | 112.23% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 4.22% | -2.90% | 6.05% | 100.00% | 13.39% | 15.38% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -1.44% | -11.34% | 24.83% | 50.00% | -3.33% | 24.83% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 48.39% | -1.11% | -13.21% | 35.20% | 38.71% | -8.36% | 49.59% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 25.00% | -8.80% | -19.07% | 44.57% | 50.00% | 7.66% | 78.98% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 25.00% | -15.80% | -24.19% | 48.90% | 50.00% | 9.22% | 63.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -33.18% | -38.14% | 0.00% | 0.00% | -15.17% | 0.00% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | NONE | 1 | 2 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 2 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_BTC_REGIME | 0 | 1 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| SOL-USD | ATOM-USD | 2023-09-03 | 87.89% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| SOL-USD | EGLD-USD | 2023-09-03 | 86.09% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| SOL-USD | LINK-USD | 2019-03-13 | 85.60% | RECOVERY | BULL | SAME_BTC_ONLY | HIGH_SPIKE_60D | 49.79% | -3.55% | 109.74% | 41.89% | -3.55% | 109.74% |
| SOL-USD | EOS-USD | 2023-09-03 | 84.19% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | ETC-USD | 2023-09-03 | 84.08% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |

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

