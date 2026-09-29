# Market Regime Match Report

Generated: 2026-09-29 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-29 | RECOVERY | 83.243 $ | True | 38.73% | -0.45% | RECOVERY | 38.73% | -0.45% |
| DOGE-USD | 2026-09-29 | RECOVERY | 0.09344 $ | True | 29.46% | -7.49% | RECOVERY | 38.73% | -0.45% |
| SOL-USD | 2026-09-29 | RECOVERY | 117,81 $ | True | 52.24% | -1.54% | RECOVERY | 38.73% | -0.45% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 42.50% | -2.32% | 16.24% | 35.41% | -11.30% | -28.89% | 17.98% | 37.85% | 70.32% | 50.00% | -0.66% | 31.68% | 99.55% |
| BTC-USD | SAME_BTC_REGIME | 8 | 62.50% | 4.11% | 8.40% | 15.79% | -4.56% | -13.41% | 23.13% | 28.15% | 32.49% | 37.50% | -3.78% | 5.94% | 22.22% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -2.19% | -2.19% | -2.19% | -19.23% | -19.23% | 37.81% | 37.81% | 37.81% | 100.00% | 121.40% | 121.40% | 121.40% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 40.00% | -11.04% | 12.71% | 62.21% | -18.79% | -32.99% | 10.38% | 30.02% | 95.58% | 37.50% | -10.22% | 15.94% | 78.87% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 75.00% | 5.46% | 13.93% | 31.30% | -3.13% | -12.90% | 25.75% | 37.93% | 54.92% | 37.50% | -1.77% | 10.16% | 23.35% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 4.21% | 4.21% | 4.21% | -2.11% | -2.11% | 26.25% | 26.25% | 26.25% | 100.00% | 1.91% | 1.91% | 1.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -1.92% | 15.28% | 57.24% | -11.15% | -29.18% | 20.46% | 30.89% | 86.27% | 42.50% | -1.51% | 20.88% | 78.69% |
| SOL-USD | SAME_BTC_REGIME | 11 | 72.73% | 7.98% | 12.69% | 30.13% | -3.44% | -18.93% | 27.49% | 36.04% | 69.12% | 36.36% | -0.79% | 9.89% | 29.88% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -24.53% | -10.16% | -1.54% | -31.71% | -34.27% | 7.49% | 16.87% | 22.50% | 66.67% | 1.91% | 2.57% | 2.96% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 45.83% | -6.55% | -14.61% | 38.00% | 54.17% | 11.91% | 69.08% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 14.29% | -2.45% | -17.79% | 28.27% | 57.14% | 37.07% | 222.65% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -13.14% | -16.41% | 45.99% | 0.00% | -6.40% | 45.99% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 62.50% | 4.11% | -4.56% | 28.15% | 37.50% | -3.78% | 34.65% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 26 | 23.08% | -14.86% | -22.63% | 19.44% | 26.92% | -15.57% | 25.78% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 18.61% | -6.05% | 110.03% | 83.33% | 30.01% | 130.35% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 8 | 75.00% | 5.46% | -3.13% | 37.93% | 37.50% | -1.77% | 37.93% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 30.00% | -9.34% | -18.92% | 24.86% | 35.00% | -9.34% | 26.51% |
| SOL-USD | HISTORICAL_BTC_BULL | 8 | 37.50% | -2.40% | -20.14% | 38.87% | 62.50% | 27.36% | 138.29% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 25.20% | -11.23% | 25.20% | 100.00% | 238.16% | 274.03% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 11 | 72.73% | 7.98% | -3.44% | 36.04% | 36.36% | -0.79% | 42.68% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 35 | 42.86% | -2.45% | -11.04% | 28.81% | 45.71% | -3.53% | 46.23% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 78.89% | -5.22% | 136.47% | 66.67% | 93.83% | 303.30% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -14.55% | -20.80% | 6.42% | 100.00% | 37.07% | 52.86% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -2.19% | -19.23% | 37.81% | 100.00% | 121.40% | 202.07% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 30.30% | -13.98% | -20.79% | 24.01% | 27.27% | -12.86% | 33.54% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 100.00% | 78.89% | -4.62% | 132.08% | 80.00% | 22.96% | 147.89% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -14.55% | -20.80% | 6.42% | 100.00% | 37.07% | 52.86% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 4.21% | -2.11% | 26.25% | 100.00% | 1.91% | 26.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 33 | 45.45% | -1.74% | -11.08% | 33.18% | 39.39% | -2.76% | 46.46% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 8.88% | 0.00% | 69.12% | 0.00% | -0.21% | 69.12% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -14.55% | -20.80% | 11.55% | 66.67% | 17.65% | 49.32% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -24.53% | -31.71% | 16.87% | 66.67% | 1.91% | 16.87% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 1 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 3 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ATOM-USD | 2023-09-03 | 88.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| BTC-USD | EGLD-USD | 2023-09-03 | 88.56% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| BTC-USD | XTZ-USD | 2023-09-03 | 87.96% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| BTC-USD | XRP-USD | 2023-09-03 | 87.49% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.26% | -11.04% | 4.21% | -15.19% | -18.87% | 4.21% |
| BTC-USD | EOS-USD | 2023-09-03 | 87.15% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| BTC-USD | ETC-USD | 2023-09-03 | 87.01% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| BTC-USD | OMG-USD | 2023-09-03 | 86.10% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 9.65% | -2.45% | 37.98% | -4.03% | -10.47% | 37.98% |
| BTC-USD | KAVA-USD | 2023-09-03 | 85.37% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | NEAR-USD | 2023-09-03 | 85.93% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| DOGE-USD | EGLD-USD | 2023-09-03 | 84.71% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| DOGE-USD | DOT-USD | 2023-09-03 | 84.68% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| DOGE-USD | KAVA-USD | 2023-09-03 | 84.50% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | EOS-USD | 2023-09-03 | 83.95% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| DOGE-USD | XTZ-USD | 2023-09-03 | 83.30% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| DOGE-USD | ADA-USD | 2023-09-03 | 82.67% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| DOGE-USD | LRC-USD | 2023-09-03 | 82.18% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 12.28% | -3.44% | 38.90% | -1.68% | -7.92% | 38.90% |
| SOL-USD | ATOM-USD | 2023-09-08 | 88.54% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| SOL-USD | EGLD-USD | 2023-09-03 | 87.80% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| SOL-USD | WAVES-USD | 2023-09-03 | 87.44% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 13.10% | -1.28% | 33.18% | -0.79% | -8.93% | 33.18% |
| SOL-USD | EOS-USD | 2023-09-03 | 86.31% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | NEAR-USD | 2023-09-03 | 86.29% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| SOL-USD | NEO-USD | 2023-09-03 | 86.21% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 4.75% | -3.97% | 23.99% | 0.84% | -11.34% | 23.99% |
| SOL-USD | ETC-USD | 2023-09-03 | 85.91% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| SOL-USD | LRC-USD | 2023-09-03 | 85.67% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 12.28% | -3.44% | 38.90% | -1.68% | -7.92% | 38.90% |
| SOL-USD | KAVA-USD | 2023-09-03 | 85.52% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| SOL-USD | XTZ-USD | 2023-09-03 | 85.39% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |

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

