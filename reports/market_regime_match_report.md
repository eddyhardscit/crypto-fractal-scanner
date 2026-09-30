# Market Regime Match Report

Generated: 2026-09-30 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-30 | RECOVERY | 83.353 $ | True | 35.57% | -0.13% | RECOVERY | 35.57% | -0.13% |
| DOGE-USD | 2026-09-30 | RECOVERY | 0.09370 $ | True | 26.48% | -7.11% | RECOVERY | 35.57% | -0.13% |
| SOL-USD | 2026-09-30 | RECOVERY | 119,12 $ | True | 47.71% | -0.93% | RECOVERY | 35.57% | -0.13% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 50.00% | -0.22% | 14.04% | 32.87% | -10.76% | -28.49% | 20.43% | 36.49% | 54.66% | 55.00% | 3.39% | 30.82% | 85.11% |
| BTC-USD | SAME_BTC_REGIME | 9 | 66.67% | 7.98% | 11.83% | 36.17% | -4.53% | -12.62% | 27.49% | 36.05% | 48.85% | 55.56% | 1.61% | 18.94% | 30.63% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -2.19% | -2.19% | -2.19% | -19.23% | -19.23% | 37.81% | 37.81% | 37.81% | 100.00% | 121.40% | 121.40% | 121.40% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 40.00% | -4.21% | 8.58% | 40.87% | -15.90% | -30.46% | 14.10% | 26.58% | 67.67% | 42.50% | -5.31% | 19.71% | 77.90% |
| DOGE-USD | SAME_BTC_REGIME | 7 | 71.43% | 5.27% | 7.04% | 28.93% | -4.59% | -12.82% | 24.01% | 28.86% | 55.07% | 57.14% | 1.61% | 13.51% | 24.82% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 4.21% | 4.21% | 4.21% | -2.11% | -2.11% | 26.25% | 26.25% | 26.25% | 100.00% | 1.91% | 1.91% | 1.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 37.50% | -4.52% | 12.49% | 30.45% | -12.31% | -28.96% | 14.35% | 27.22% | 70.82% | 45.00% | -1.06% | 23.20% | 87.24% |
| SOL-USD | SAME_BTC_REGIME | 9 | 66.67% | 8.88% | 13.10% | 36.17% | -3.97% | -19.54% | 30.13% | 38.90% | 73.75% | 33.33% | -0.79% | 0.84% | 30.63% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 50.00% | -10.16% | 21.27% | 51.98% | -16.91% | -33.95% | 16.87% | 42.47% | 71.67% | 75.00% | 2.57% | 23.70% | 60.54% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 23 | 56.52% | 4.73% | -11.14% | 36.93% | 60.87% | 11.02% | 68.39% |
| BTC-USD | HISTORICAL_BTC_BULL | 5 | 0.00% | -2.45% | -19.23% | 18.72% | 40.00% | -8.85% | 52.86% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -13.14% | -16.41% | 36.15% | 33.33% | -6.40% | 160.01% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 9 | 66.67% | 7.98% | -4.53% | 36.05% | 55.56% | 1.61% | 37.98% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 32.00% | -14.09% | -22.38% | 22.14% | 36.00% | -11.17% | 31.41% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 33.33% | -2.40% | -11.97% | 54.40% | 50.00% | 2.74% | 99.22% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 6.03% | -13.82% | 40.79% | 50.00% | 115.88% | 217.02% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 7 | 71.43% | 5.27% | -4.59% | 28.86% | 57.14% | 1.61% | 31.89% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 31.58% | -6.21% | -17.06% | 24.54% | 42.11% | -2.76% | 33.65% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 18.18% | -11.19% | -20.80% | 15.34% | 54.55% | 12.20% | 89.00% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 25.20% | -11.23% | 25.20% | 100.00% | 238.16% | 274.03% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 9 | 66.67% | 8.88% | -3.97% | 38.90% | 33.33% | -0.79% | 46.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 35 | 51.43% | 1.45% | -10.47% | 33.01% | 51.43% | 1.61% | 46.23% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 11.83% | -3.76% | 91.97% | 66.67% | 11.84% | 91.97% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -14.55% | -20.80% | 6.42% | 100.00% | 37.07% | 52.86% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -2.19% | -19.23% | 37.81% | 100.00% | 121.40% | 202.07% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 35 | 37.14% | -5.36% | -16.41% | 25.74% | 40.00% | -6.05% | 39.76% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 34.42% | -4.46% | 87.79% | 33.33% | -17.68% | 87.79% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -14.55% | -20.80% | 6.42% | 100.00% | 37.07% | 52.86% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 4.21% | -2.11% | 26.25% | 100.00% | 1.91% | 26.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 35.71% | -3.00% | -11.58% | 26.43% | 35.71% | -3.15% | 38.21% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | -1.15% | -13.37% | 55.34% | 50.00% | 62.42% | 127.14% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 6 | 33.33% | -15.11% | -24.63% | 14.11% | 66.67% | 14.93% | 51.09% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 50.00% | -10.16% | -16.91% | 42.47% | 75.00% | 2.57% | 42.47% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 1 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 4 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ATOM-USD | 2023-09-03 | 88.67% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| BTC-USD | EGLD-USD | 2023-09-03 | 87.81% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| BTC-USD | XRP-USD | 2023-09-03 | 87.62% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.26% | -11.04% | 4.21% | -15.19% | -18.87% | 4.21% |
| BTC-USD | XTZ-USD | 2023-09-03 | 87.20% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| BTC-USD | OMG-USD | 2023-09-03 | 86.79% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 9.65% | -2.45% | 37.98% | -4.03% | -10.47% | 37.98% |
| BTC-USD | ETC-USD | 2023-09-03 | 86.69% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| BTC-USD | EOS-USD | 2023-09-03 | 86.50% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| BTC-USD | THETA-USD | 2020-06-14 | 86.24% | RECOVERY | BULL | SAME_BTC_ONLY | BULLISH_30D | 11.83% | -3.22% | 36.05% | 11.84% | -3.22% | 36.05% |
| BTC-USD | NEAR-USD | 2023-09-03 | 85.51% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| DOGE-USD | NEAR-USD | 2023-09-03 | 86.44% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| DOGE-USD | KAVA-USD | 2023-09-03 | 84.39% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | DOT-USD | 2023-09-08 | 84.31% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 6.09% | -5.23% | 30.24% | 8.08% | -10.63% | 30.24% |
| DOGE-USD | EGLD-USD | 2023-09-03 | 83.41% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| DOGE-USD | EOS-USD | 2023-09-03 | 83.28% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| DOGE-USD | XTZ-USD | 2023-09-03 | 82.80% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| DOGE-USD | ATOM-USD | 2023-09-03 | 82.56% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| SOL-USD | ATOM-USD | 2023-09-08 | 88.99% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| SOL-USD | WAVES-USD | 2023-09-03 | 87.18% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 13.10% | -1.28% | 33.18% | -0.79% | -8.93% | 33.18% |
| SOL-USD | EGLD-USD | 2023-09-03 | 86.65% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| SOL-USD | NEO-USD | 2023-09-03 | 86.51% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 4.75% | -3.97% | 23.99% | 0.84% | -11.34% | 23.99% |
| SOL-USD | NEAR-USD | 2023-09-03 | 86.45% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| SOL-USD | LINK-USD | 2019-03-18 | 86.39% | RECOVERY | BULL | SAME_BTC_ONLY | MIXED | 8.88% | 0.00% | 69.12% | -0.21% | -4.59% | 69.12% |
| SOL-USD | LRC-USD | 2023-09-03 | 85.89% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 12.28% | -3.44% | 38.90% | -1.68% | -7.92% | 38.90% |
| SOL-USD | EOS-USD | 2023-09-03 | 85.26% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | ETC-USD | 2023-09-03 | 84.90% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |

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

