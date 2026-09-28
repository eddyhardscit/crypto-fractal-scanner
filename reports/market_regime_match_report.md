# Market Regime Match Report

Generated: 2026-09-28 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-28 | RECOVERY | 83.028 $ | True | 41.79% | -0.74% | RECOVERY | 41.79% | -0.74% |
| DOGE-USD | 2026-09-28 | RECOVERY | 0.09336 $ | True | 29.68% | -7.83% | RECOVERY | 41.79% | -0.74% |
| SOL-USD | 2026-09-28 | RECOVERY | 119,07 $ | True | 61.95% | -2.11% | RECOVERY | 41.79% | -0.74% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 45.00% | -2.32% | 11.82% | 34.02% | -12.39% | -29.79% | 18.19% | 32.01% | 58.09% | 45.00% | -3.10% | 25.88% | 94.35% |
| BTC-USD | SAME_BTC_REGIME | 7 | 57.14% | 2.84% | 6.62% | 16.84% | -8.74% | -14.20% | 20.73% | 24.87% | 28.54% | 42.86% | -1.86% | 10.28% | 23.32% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -2.19% | -2.19% | -2.19% | -19.23% | -19.23% | 37.81% | 37.81% | 37.81% | 100.00% | 121.40% | 121.40% | 121.40% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 42.50% | -9.72% | 12.63% | 42.57% | -18.09% | -34.88% | 10.38% | 26.56% | 86.79% | 42.50% | -4.06% | 19.16% | 76.16% |
| DOGE-USD | SAME_BTC_REGIME | 9 | 77.78% | 5.27% | 12.28% | 27.15% | -3.44% | -12.04% | 24.01% | 37.60% | 49.58% | 44.44% | -1.68% | 7.23% | 21.88% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 4.21% | 4.21% | 4.21% | -2.11% | -2.11% | 26.25% | 26.25% | 26.25% | 100.00% | 1.91% | 1.91% | 1.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | 0.61% | 15.97% | 61.36% | -11.32% | -29.09% | 21.15% | 34.29% | 87.64% | 50.00% | 0.41% | 30.82% | 75.64% |
| SOL-USD | SAME_BTC_REGIME | 10 | 80.00% | 10.13% | 17.41% | 33.15% | -3.13% | -9.76% | 28.81% | 36.50% | 44.24% | 50.00% | 0.41% | 16.01% | 30.26% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -24.53% | -10.16% | -1.54% | -31.71% | -34.27% | 7.49% | 16.87% | 22.50% | 66.67% | 1.91% | 2.57% | 2.96% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 26 | 46.15% | -6.15% | -14.61% | 25.45% | 46.15% | -5.03% | 54.68% |
| BTC-USD | HISTORICAL_BTC_BULL | 6 | 33.33% | -2.32% | -11.50% | 37.77% | 50.00% | 56.28% | 232.93% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.76% | -19.86% | 38.61% | 0.00% | -2.68% | 38.61% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 57.14% | 2.84% | -8.74% | 24.87% | 42.86% | -1.86% | 27.89% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 24.00% | -14.34% | -27.97% | 17.14% | 32.00% | -17.40% | 24.39% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 34.42% | -6.88% | 125.06% | 80.00% | 37.07% | 132.08% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 0.04% | -4.42% | 4.39% | 100.00% | 9.57% | 13.58% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 9 | 77.78% | 5.27% | -3.44% | 37.60% | 44.44% | -1.68% | 37.60% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 42.11% | -10.94% | -16.54% | 34.06% | 47.37% | -12.86% | 56.21% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 36.36% | -8.02% | -17.79% | 23.06% | 54.55% | 17.65% | 123.24% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 10 | 80.00% | 10.13% | -3.13% | 36.50% | 50.00% | 0.41% | 38.58% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 36 | 44.44% | -2.85% | -12.39% | 26.22% | 41.67% | -4.20% | 40.57% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 95.49% | -4.49% | 142.18% | 100.00% | 276.27% | 381.00% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -15.45% | -22.78% | 8.44% | 0.00% | -9.99% | 8.44% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -2.19% | -19.23% | 37.81% | 100.00% | 121.40% | 202.07% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 35.29% | -11.16% | -19.21% | 23.57% | 35.29% | -10.22% | 31.66% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 100.00% | 78.89% | -5.22% | 128.57% | 66.67% | 22.96% | 295.39% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -7.25% | -12.61% | 5.91% | 100.00% | 23.32% | 43.04% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 4.21% | -2.11% | 26.25% | 100.00% | 1.91% | 26.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 54.84% | 3.89% | -10.94% | 38.25% | 45.16% | -1.68% | 58.51% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -8.80% | -19.07% | 17.13% | 50.00% | 21.07% | 51.54% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 1.06% | -13.66% | 48.90% | 75.00% | 27.36% | 81.43% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -24.53% | -31.71% | 16.87% | 66.67% | 1.91% | 16.87% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 1 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 3 | 10 | 10 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ATOM-USD | 2023-09-03 | 88.49% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| BTC-USD | EGLD-USD | 2023-09-03 | 88.10% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| BTC-USD | XTZ-USD | 2023-09-03 | 87.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| BTC-USD | ETC-USD | 2023-09-03 | 87.16% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| BTC-USD | EOS-USD | 2023-09-03 | 86.87% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| BTC-USD | XRP-USD | 2023-09-03 | 86.10% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.26% | -11.04% | 4.21% | -15.19% | -18.87% | 4.21% |
| BTC-USD | ADA-USD | 2023-09-03 | 85.41% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| DOGE-USD | EGLD-USD | 2023-09-03 | 84.65% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| DOGE-USD | NEAR-USD | 2023-09-03 | 84.50% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| DOGE-USD | DOT-USD | 2023-09-03 | 84.48% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| DOGE-USD | KAVA-USD | 2023-09-03 | 83.80% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | EOS-USD | 2023-09-03 | 83.45% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| DOGE-USD | ADA-USD | 2023-09-03 | 82.85% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| DOGE-USD | XTZ-USD | 2023-09-03 | 82.62% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| DOGE-USD | LRC-USD | 2023-09-03 | 81.89% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 12.28% | -3.44% | 38.90% | -1.68% | -7.92% | 38.90% |
| DOGE-USD | ATOM-USD | 2023-09-03 | 81.49% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| SOL-USD | ATOM-USD | 2023-09-03 | 88.78% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| SOL-USD | EGLD-USD | 2023-09-03 | 87.86% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| SOL-USD | WAVES-USD | 2023-09-03 | 87.27% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 13.10% | -1.28% | 33.18% | -0.79% | -8.93% | 33.18% |
| SOL-USD | ETC-USD | 2023-09-03 | 86.46% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| SOL-USD | EOS-USD | 2023-09-03 | 86.31% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | NEAR-USD | 2023-09-03 | 85.64% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| SOL-USD | DOT-USD | 2023-09-03 | 85.28% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| SOL-USD | KAVA-USD | 2023-09-03 | 85.19% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| SOL-USD | XTZ-USD | 2023-09-03 | 85.11% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| SOL-USD | LRC-USD | 2023-09-03 | 84.93% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 12.28% | -3.44% | 38.90% | -1.68% | -7.92% | 38.90% |

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

