# Market Regime Match Report

Generated: 2026-09-08 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-08 | RECOVERY | 78.780 $ | True | 28.20% | -5.79% | RECOVERY | 28.20% | -5.79% |
| DOGE-USD | 2026-09-08 | MIXED | 0.09000 $ | True | 8.49% | -12.97% | RECOVERY | 28.20% | -5.79% |
| SOL-USD | 2026-09-08 | RECOVERY | 103,29 $ | True | 63.53% | -10.48% | RECOVERY | 28.20% | -5.79% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 82.50% | 19.65% | 40.50% | 71.21% | -9.84% | -36.52% | 26.22% | 56.43% | 91.25% | 82.50% | 23.54% | 42.29% | 93.74% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 5 | 60.00% | 3.09% | 36.70% | 40.25% | -14.89% | -36.96% | 36.70% | 45.11% | 207.62% | 80.00% | 8.85% | 25.17% | 63.73% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -10.33% | 4.51% | 21.55% | -18.23% | -32.73% | 11.15% | 21.45% | 31.93% | 32.50% | -7.01% | 9.10% | 33.27% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 21.62% | 54.75% | 132.39% | -11.71% | -42.28% | 29.65% | 74.27% | 188.57% | 62.50% | 27.25% | 107.54% | 165.77% |
| SOL-USD | SAME_BTC_REGIME | 1 | 100.00% | 99.18% | 99.18% | 99.18% | -8.40% | -8.40% | 121.32% | 121.32% | 121.32% | 100.00% | 116.63% | 116.63% | 116.63% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 100.00% | 42.62% | 120.18% | 166.71% | -6.46% | -17.34% | 45.11% | 191.34% | 279.08% | 100.00% | 89.45% | 142.65% | 174.57% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 12 | 75.00% | 25.62% | -19.10% | 68.74% | 75.00% | 37.35% | 104.73% |
| BTC-USD | HISTORICAL_BTC_BULL | 28 | 85.71% | 16.96% | -8.20% | 47.72% | 85.71% | 18.79% | 64.31% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 16 | 25.00% | -11.98% | -17.35% | 21.31% | 12.50% | -14.61% | 21.31% |
| DOGE-USD | HISTORICAL_BTC_BULL | 14 | 42.86% | -2.92% | -17.21% | 11.16% | 50.00% | 2.52% | 47.85% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 9 | 33.33% | -19.19% | -25.63% | 31.66% | 44.44% | -0.47% | 34.44% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 52.94% | 6.14% | -20.06% | 45.11% | 47.06% | -15.32% | 75.73% |
| SOL-USD | HISTORICAL_BTC_BULL | 18 | 88.89% | 43.00% | -5.16% | 135.44% | 88.89% | 39.54% | 206.14% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 0.00% | -14.99% | -21.11% | 17.77% | 0.00% | -11.17% | 18.40% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 100.00% | 99.18% | -8.40% | 121.32% | 100.00% | 116.63% | 141.68% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 89.66% | 19.76% | -8.74% | 52.49% | 89.66% | 25.06% | 69.58% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.49% | -14.15% | 62.60% | 40.00% | -4.71% | 177.84% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 91.00% | -16.34% | 125.42% | 100.00% | 162.43% | 162.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 3.09% | -14.89% | 45.11% | 80.00% | 8.85% | 103.03% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 16 | 31.25% | -6.43% | -15.46% | 16.25% | 18.75% | -13.80% | 19.80% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 21 | 33.33% | -15.86% | -24.94% | 21.82% | 42.86% | -2.67% | 47.42% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -1.55% | -11.79% | 39.39% | 50.00% | 10.54% | 39.39% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -16.58% | -20.55% | 0.00% | 0.00% | -11.78% | 0.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 62.07% | 14.38% | -11.27% | 54.70% | 58.62% | 6.16% | 81.70% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 124.92% | -9.44% | 206.14% | 66.67% | 120.96% | 250.11% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 40.65% | -19.07% | 96.88% | 50.00% | 76.43% | 124.64% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 100.00% | 42.62% | -6.46% | 191.34% | 100.00% | 89.45% | 220.30% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_ASSET_REGIME | 0 | 5 | 0 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| DOGE-USD | NONE | 0 | 0 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 0 | 3 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING BTC-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | UNI-USD | 2023-04-07 | 86.02% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | -47.87% | -48.23% | 315.96% | -44.33% | -53.90% | 315.96% |
| BTC-USD | DASH-USD | 2020-08-29 | 84.79% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.81% | -14.89% | 7.15% | 8.85% | -14.89% | 45.20% |
| BTC-USD | QTUM-USD | 2023-08-09 | 83.99% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.09% | -5.87% | 12.60% | 0.39% | -5.87% | 20.46% |
| BTC-USD | WAVES-USD | 2023-08-14 | 83.94% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 36.70% | 0.00% | 36.70% | 25.17% | 0.00% | 55.93% |
| BTC-USD | LRC-USD | 2020-03-12 | 83.50% | BEAR | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 42.62% | -20.06% | 45.11% | 89.45% | -20.06% | 103.03% |

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

