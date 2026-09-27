# Market Regime Match Report

Generated: 2026-09-27 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-27 | RECOVERY | 84.377 $ | True | 40.30% | -1.01% | RECOVERY | 40.30% | -1.01% |
| DOGE-USD | 2026-09-27 | RECOVERY | 0.09591 $ | True | 30.87% | -8.16% | RECOVERY | 40.30% | -1.01% |
| SOL-USD | 2026-09-27 | RECOVERY | 120,68 $ | True | 61.02% | -2.67% | RECOVERY | 40.30% | -1.01% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 42.50% | -3.50% | 9.78% | 34.84% | -13.71% | -28.93% | 18.19% | 28.15% | 64.10% | 40.00% | -5.03% | 20.61% | 91.65% |
| BTC-USD | SAME_BTC_REGIME | 7 | 57.14% | 2.84% | 6.62% | 16.84% | -8.74% | -22.04% | 22.25% | 25.72% | 28.54% | 42.86% | -1.86% | 10.28% | 23.32% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 0.00% | -8.93% | -5.56% | -3.54% | -22.96% | -25.94% | 30.88% | 34.34% | 36.42% | 50.00% | 48.08% | 84.74% | 106.74% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -15.67% | -15.67% | -15.67% | -26.69% | -26.69% | 23.95% | 23.95% | 23.95% | 0.00% | -25.25% | -25.25% | -25.25% |
| DOGE-USD | ALL_MATCHES | 40 | 42.50% | -7.33% | 15.44% | 57.47% | -19.13% | -58.39% | 8.58% | 25.95% | 92.06% | 42.50% | -4.21% | 15.48% | 76.24% |
| DOGE-USD | SAME_BTC_REGIME | 5 | 60.00% | 2.84% | 2.95% | 12.49% | -8.74% | -15.49% | 20.73% | 24.01% | 32.17% | 20.00% | -3.53% | -1.86% | 3.59% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 1.28% | 1.28% | 1.28% | -4.43% | -4.43% | 30.62% | 30.62% | 30.62% | 100.00% | 0.91% | 0.91% | 0.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -4.92% | 16.13% | 55.27% | -17.24% | -30.51% | 17.76% | 30.89% | 87.24% | 45.00% | -4.06% | 21.99% | 74.08% |
| SOL-USD | SAME_BTC_REGIME | 9 | 77.78% | 7.98% | 18.85% | 34.06% | -3.55% | -10.78% | 27.49% | 33.18% | 52.03% | 55.56% | 1.61% | 18.94% | 32.28% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 0.00% | -31.03% | -29.95% | -29.31% | -34.92% | -37.49% | 3.75% | 5.62% | 6.74% | 50.00% | -5.97% | -1.37% | 1.39% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 23 | 43.48% | -7.74% | -15.00% | 23.04% | 43.48% | -5.17% | 44.84% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 33.33% | -2.45% | -9.97% | 37.65% | 33.33% | -8.85% | 202.07% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.76% | -19.86% | 38.61% | 0.00% | -2.68% | 38.61% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 57.14% | 2.84% | -8.74% | 25.72% | 42.86% | -1.86% | 28.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 28.57% | -14.22% | -28.42% | 16.61% | 35.71% | -17.54% | 26.22% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 78.89% | -5.22% | 132.08% | 80.00% | 48.30% | 458.70% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 8.83% | -8.55% | 12.80% | 100.00% | 45.29% | 62.15% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 60.00% | 2.84% | -8.74% | 24.01% | 20.00% | -3.53% | 24.01% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 31.58% | -14.09% | -20.79% | 21.85% | 36.84% | -14.25% | 33.31% |
| SOL-USD | HISTORICAL_BTC_BULL | 12 | 41.67% | -8.80% | -19.42% | 39.24% | 50.00% | 4.65% | 110.73% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 9 | 77.78% | 7.98% | -3.55% | 33.18% | 55.56% | 1.61% | 37.60% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 45.45% | -2.45% | -13.21% | 24.39% | 39.39% | -4.88% | 37.65% |
| BTC-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 34.46% | -7.60% | 130.76% | 50.00% | 40.90% | 225.60% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -15.45% | -22.78% | 8.44% | 0.00% | -9.99% | 8.44% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -8.93% | -22.96% | 34.34% | 50.00% | 48.08% | 157.54% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 31.25% | -13.89% | -26.63% | 19.13% | 31.25% | -12.88% | 27.94% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 45.40% | -7.54% | 130.33% | 83.33% | 29.69% | 377.05% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 2.39% | -3.49% | 5.41% | 100.00% | 12.61% | 14.68% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 1.28% | -4.43% | 30.62% | 100.00% | 0.91% | 30.62% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 50.00% | 0.92% | -13.67% | 32.42% | 43.33% | -4.06% | 45.31% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 25.00% | -8.80% | -19.07% | 44.57% | 50.00% | 7.66% | 78.98% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 0.61% | -14.65% | 48.90% | 50.00% | 3.83% | 76.12% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -31.03% | -34.92% | 5.62% | 50.00% | -5.97% | 5.62% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ATOM-USD | 2023-09-03 | 87.59% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| BTC-USD | EGLD-USD | 2023-09-03 | 87.32% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| BTC-USD | ETC-USD | 2023-09-03 | 87.22% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| BTC-USD | XTZ-USD | 2023-09-03 | 87.05% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| BTC-USD | EOS-USD | 2023-09-03 | 86.28% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| BTC-USD | ADA-USD | 2023-09-03 | 85.58% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| BTC-USD | ETH-USD | 2019-03-13 | 85.08% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -15.67% | -26.69% | 23.95% | -25.25% | -31.75% | 23.95% |
| DOGE-USD | DOT-USD | 2023-09-03 | 83.98% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| DOGE-USD | EGLD-USD | 2023-09-03 | 83.35% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| DOGE-USD | KAVA-USD | 2023-09-03 | 82.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | ADA-USD | 2023-09-03 | 82.11% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| DOGE-USD | EOS-USD | 2023-09-03 | 82.06% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | ATOM-USD | 2023-09-03 | 88.75% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| SOL-USD | EGLD-USD | 2023-09-03 | 87.36% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| SOL-USD | WAVES-USD | 2023-09-03 | 86.79% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 13.10% | -1.28% | 33.18% | -0.79% | -8.93% | 33.18% |
| SOL-USD | ETC-USD | 2023-09-03 | 85.88% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| SOL-USD | EOS-USD | 2023-09-03 | 85.66% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | DOT-USD | 2023-09-03 | 85.12% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| SOL-USD | LINK-USD | 2019-03-13 | 84.79% | RECOVERY | BULL | SAME_BTC_ONLY | HIGH_SPIKE_60D | 49.79% | -3.55% | 109.74% | 41.89% | -3.55% | 109.74% |
| SOL-USD | KAVA-USD | 2023-09-03 | 84.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| SOL-USD | XTZ-USD | 2023-09-03 | 84.38% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |

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

