# Market Regime Match Report

Generated: 2026-09-04 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-04 | RECOVERY | 80.956 $ | True | 33.00% | -6.75% | RECOVERY | 33.00% | -6.75% |
| DOGE-USD | 2026-09-04 | RECOVERY | 0.08695 $ | False | 6.23% | -13.76% | RECOVERY | 33.00% | -6.75% |
| SOL-USD | 2026-09-04 | RECOVERY | 103,67 $ | True | 66.70% | -11.82% | RECOVERY | 33.00% | -6.75% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 82.50% | 12.86% | 31.22% | 68.00% | -12.44% | -28.51% | 21.09% | 43.27% | 104.37% | 80.00% | 11.34% | 42.45% | 116.01% |
| BTC-USD | SAME_BTC_REGIME | 5 | 100.00% | 34.95% | 39.22% | 81.13% | -6.66% | -17.66% | 46.99% | 102.52% | 116.41% | 100.00% | 71.29% | 120.62% | 133.43% |
| BTC-USD | SAME_ASSET_REGIME | 5 | 80.00% | 29.98% | 34.95% | 192.28% | -14.77% | -18.35% | 34.95% | 102.52% | 229.70% | 80.00% | 8.85% | 34.79% | 56.69% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 32.46% | 33.71% | 34.45% | -12.07% | -18.94% | 68.74% | 85.63% | 95.77% | 100.00% | 53.04% | 62.16% | 67.64% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -8.81% | 1.79% | 24.69% | -15.14% | -31.85% | 11.29% | 27.60% | 45.12% | 32.50% | -10.41% | 9.07% | 44.19% |
| DOGE-USD | SAME_BTC_REGIME | 2 | 0.00% | -25.91% | -21.18% | -18.35% | -27.18% | -34.00% | 4.59% | 6.88% | 8.26% | 0.00% | -37.99% | -29.56% | -24.50% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 13.97% | 54.50% | 95.84% | -11.45% | -38.27% | 30.77% | 62.10% | 126.49% | 70.00% | 29.88% | 80.39% | 186.10% |
| SOL-USD | SAME_BTC_REGIME | 5 | 80.00% | 39.22% | 67.31% | 92.37% | -13.17% | -20.05% | 46.99% | 98.59% | 114.83% | 100.00% | 120.62% | 141.97% | 233.11% |
| SOL-USD | SAME_ASSET_REGIME | 5 | 80.00% | 5.84% | 34.95% | 192.28% | -14.77% | -20.05% | 34.95% | 39.59% | 204.53% | 80.00% | 32.97% | 57.82% | 65.90% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 9.15% | 22.05% | 29.79% | -19.90% | -20.50% | 17.47% | 26.21% | 31.45% | 100.00% | 52.13% | 61.71% | 67.46% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 4 | 50.00% | -6.56% | -29.44% | 26.79% | 50.00% | -5.56% | 31.23% |
| BTC-USD | HISTORICAL_BTC_BULL | 31 | 83.87% | 12.21% | -11.27% | 35.63% | 80.65% | 10.68% | 68.31% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 100.00% | 34.95% | -6.66% | 102.52% | 100.00% | 71.29% | 128.04% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 11 | 9.09% | -11.73% | -22.77% | 10.88% | 18.18% | -32.52% | 16.43% |
| DOGE-USD | HISTORICAL_BTC_BULL | 25 | 44.00% | -1.61% | -8.92% | 36.34% | 44.00% | -3.99% | 47.42% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -21.02% | -29.71% | 11.71% | 0.00% | -7.24% | 11.71% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -25.91% | -27.18% | 6.88% | 0.00% | -37.99% | 6.88% |
| SOL-USD | HISTORICAL_BTC_BEAR | 10 | 50.00% | 10.52% | -16.85% | 51.43% | 60.00% | 26.83% | 68.87% |
| SOL-USD | HISTORICAL_BTC_BULL | 18 | 94.44% | 39.89% | -9.81% | 98.33% | 88.89% | 34.55% | 175.12% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 7 | 14.29% | -22.39% | -24.88% | 28.26% | 14.29% | -22.09% | 28.26% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 5 | 80.00% | 39.22% | -13.17% | 98.59% | 100.00% | 120.62% | 146.42% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 28 | 82.14% | 12.23% | -11.76% | 29.21% | 82.14% | 11.04% | 48.88% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 12.19% | -14.99% | 50.31% | 66.67% | 100.34% | 172.07% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 109.07% | -6.61% | 125.67% | 100.00% | 141.97% | 146.42% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 80.00% | 29.98% | -14.77% | 102.52% | 80.00% | 8.85% | 102.52% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 16 | 12.50% | -13.96% | -20.71% | 11.13% | 18.75% | -32.34% | 17.17% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 23 | 39.13% | -2.82% | -8.92% | 36.46% | 39.13% | -3.99% | 43.41% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 125.28% | 0.00% | 128.29% | 100.00% | 81.09% | 149.46% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 60.71% | 11.06% | -10.65% | 52.14% | 64.29% | 22.32% | 75.76% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 62.60% | -14.15% | 133.93% | 80.00% | 85.18% | 166.95% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 88.19% | -3.30% | 118.90% | 100.00% | 217.92% | 257.00% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 80.00% | 5.84% | -14.77% | 39.59% | 80.00% | 32.97% | 71.29% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_ASSET_REGIME | 2 | 5 | 5 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| DOGE-USD | NONE | 0 | 0 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_ASSET_REGIME | 2 | 5 | 5 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | THETA-USD | 2018-11-12 | 85.43% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.98% | -3.49% | 102.52% | 34.79% | -3.49% | 102.52% |
| BTC-USD | WAVES-USD | 2023-08-09 | 83.14% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.17% | -14.77% | 11.00% | 8.47% | -14.77% | 32.90% |
| BTC-USD | UNI-USD | 2023-04-02 | 82.93% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 297.17% | -2.12% | 314.49% | -44.88% | -54.06% | 314.49% |
| BTC-USD | LRC-USD | 2020-03-07 | 82.21% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 34.95% | -20.65% | 34.95% | 71.29% | -20.65% | 71.29% |
| BTC-USD | DASH-USD | 2020-08-29 | 82.09% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.81% | -14.89% | 7.15% | 8.85% | -14.89% | 45.20% |
| SOL-USD | WAVES-USD | 2023-08-09 | 82.45% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.17% | -14.77% | 11.00% | 8.47% | -14.77% | 32.90% |
| SOL-USD | LRC-USD | 2020-03-07 | 81.91% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 34.95% | -20.65% | 34.95% | 71.29% | -20.65% | 71.29% |
| SOL-USD | XRP-USD | 2024-08-23 | 79.77% | DISTRIBUTION | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 5.84% | 0.00% | 39.59% | 57.82% | 0.00% | 69.67% |
| SOL-USD | MKR-USD | 2020-03-08 | 79.74% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -16.66% | -19.15% | 0.00% | 32.97% | -19.26% | 45.21% |
| SOL-USD | UNI-USD | 2023-04-02 | 79.60% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 297.17% | -2.12% | 314.49% | -44.88% | -54.06% | 314.49% |

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

