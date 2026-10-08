# Market Regime Match Report

Generated: 2026-10-08 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-08 | BULL | 82.851 $ | True | 29.20% | 2.28% | BULL | 29.20% | 2.28% |
| DOGE-USD | 2026-10-08 | RECOVERY | 0.08774 $ | False | 18.49% | -4.64% | BULL | 29.20% | 2.28% |
| SOL-USD | 2026-10-08 | BULL | 115,51 $ | True | 47.96% | 3.45% | BULL | 29.20% | 2.28% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 47.50% | -1.04% | 20.47% | 27.07% | -10.62% | -21.01% | 18.38% | 29.82% | 56.69% | 52.50% | 1.73% | 30.49% | 58.07% |
| BTC-USD | SAME_BTC_REGIME | 6 | 50.00% | 10.26% | 28.30% | 104.52% | -14.24% | -27.87% | 18.25% | 57.26% | 132.98% | 66.67% | 94.40% | 170.42% | 241.50% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 179.59% | 179.59% | 179.59% | -0.05% | -0.05% | 199.43% | 199.43% | 199.43% | 100.00% | 300.63% | 300.63% | 300.63% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 179.59% | 179.59% | 179.59% | -0.05% | -0.05% | 199.43% | 199.43% | 199.43% | 100.00% | 300.63% | 300.63% | 300.63% |
| DOGE-USD | ALL_MATCHES | 40 | 45.00% | -2.34% | 9.91% | 25.55% | -12.81% | -21.07% | 13.07% | 24.73% | 45.14% | 47.50% | -0.29% | 19.26% | 59.68% |
| DOGE-USD | SAME_BTC_REGIME | 5 | 80.00% | 6.23% | 10.07% | 111.78% | -9.07% | -10.25% | 15.06% | 16.20% | 126.14% | 60.00% | 97.72% | 103.66% | 221.84% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 100.00% | 39.09% | 55.52% | 65.37% | -2.34% | -4.21% | 44.07% | 58.01% | 66.37% | 50.00% | 30.08% | 57.06% | 73.25% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 6.23% | 6.23% | 6.23% | -4.67% | -4.67% | 16.20% | 16.20% | 16.20% | 0.00% | -23.87% | -23.87% | -23.87% |
| SOL-USD | ALL_MATCHES | 40 | 40.00% | -4.76% | 10.28% | 21.62% | -13.24% | -21.30% | 10.92% | 20.77% | 29.60% | 37.50% | -4.22% | 25.23% | 54.53% |
| SOL-USD | SAME_BTC_REGIME | 11 | 27.27% | -5.49% | 2.87% | 21.32% | -14.10% | -25.03% | 7.05% | 17.38% | 23.98% | 45.45% | -2.90% | 78.96% | 155.82% |
| SOL-USD | SAME_ASSET_REGIME | 1 | 100.00% | 13.20% | 13.20% | 13.20% | -18.66% | -18.66% | 13.66% | 13.66% | 13.66% | 100.00% | 24.06% | 24.06% | 24.06% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 61.11% | 5.71% | -10.34% | 37.86% | 61.11% | 11.48% | 46.61% |
| BTC-USD | HISTORICAL_BTC_BULL | 6 | 50.00% | 10.26% | -14.24% | 57.26% | 66.67% | 94.40% | 257.01% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 16 | 31.25% | -8.69% | -12.07% | 25.72% | 37.50% | -2.55% | 27.80% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 21 | 47.62% | -1.65% | -16.86% | 14.28% | 42.86% | -0.45% | 26.53% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 6.23% | -9.07% | 16.20% | 60.00% | 97.72% | 161.23% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -7.24% | -15.10% | 42.16% | 100.00% | 17.46% | 42.16% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 13 | 30.77% | -9.93% | -11.88% | 26.76% | 46.15% | -0.57% | 30.93% |
| SOL-USD | HISTORICAL_BTC_BEAR | 16 | 62.50% | 5.42% | -11.67% | 15.61% | 31.25% | -4.65% | 29.00% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 27.27% | -5.49% | -14.10% | 17.38% | 45.45% | -2.90% | 108.06% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 23.08% | -9.93% | -13.72% | 26.76% | 38.46% | -3.97% | 26.76% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 45.45% | -1.65% | -10.68% | 26.76% | 48.48% | -1.38% | 36.38% |
| BTC-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 179.59% | -0.05% | 199.43% | 100.00% | 300.63% | 300.63% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -24.16% | -25.03% | 25.72% | 66.67% | 19.91% | 51.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 19.55% | -6.85% | 42.12% | 66.67% | 29.36% | 58.57% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 40.62% | -2.83% | -11.82% | 22.04% | 43.75% | -0.51% | 32.27% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 6 | 50.00% | -3.09% | -17.24% | 37.05% | 66.67% | 12.83% | 42.02% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 39.09% | -2.34% | 58.01% | 50.00% | 30.08% | 74.26% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 41.94% | -3.16% | -11.88% | 21.43% | 32.26% | -4.85% | 26.64% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 13.20% | -18.66% | 13.66% | 100.00% | 24.06% | 41.59% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 0.00% | -24.16% | -25.03% | 11.71% | 66.67% | 54.26% | 111.62% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 21.32% | -0.24% | 23.98% | 100.00% | 28.74% | 54.90% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -10.37% | -13.24% | 24.38% | 25.00% | -4.27% | 24.38% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 1 | 6 | 6 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 1 | 2 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 1 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-06-21 | 89.72% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 29.46% | -20.98% | 29.46% | 182.38% | -20.98% | 232.96% |
| BTC-USD | MKR-USD | 2020-11-13 | 86.12% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | -24.16% | -25.03% | 0.38% | 54.26% | -29.92% | 54.26% |
| BTC-USD | DASH-USD | 2020-09-28 | 85.44% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.84% | 0.00% | 66.53% | 134.54% | 0.00% | 265.03% |
| BTC-USD | LRC-USD | 2020-11-12 | 84.92% | BULL | DISTRIBUTION | SAME_BTC_ONLY | BEARISH_30D | -24.36% | -30.70% | 3.71% | -22.56% | -38.83% | 3.71% |
| BTC-USD | RUNE-USD | 2020-09-24 | 84.89% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 179.59% | -0.05% | 199.43% | 300.63% | -0.05% | 300.63% |
| BTC-USD | XLM-USD | 2025-05-20 | 84.66% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -4.32% | -7.50% | 7.05% | -12.65% | -18.68% | 7.95% |
| DOGE-USD | XTZ-USD | 2019-09-19 | 86.08% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| DOGE-USD | MKR-USD | 2020-11-18 | 84.09% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| DOGE-USD | RUNE-USD | 2020-09-24 | 83.09% | BULL | BULL | SAME_BTC_ONLY | EXPLOSIVE_60D | 179.59% | -0.05% | 199.43% | 300.63% | -0.05% | 300.63% |
| DOGE-USD | ADA-USD | 2025-05-25 | 82.01% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| DOGE-USD | HBAR-USD | 2025-05-22 | 81.95% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -5.19% | -9.07% | 8.86% | -14.65% | -28.68% | 8.86% |
| SOL-USD | RUNE-USD | 2023-06-21 | 88.35% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 29.46% | -20.98% | 29.46% | 182.38% | -20.98% | 232.96% |
| SOL-USD | MKR-USD | 2020-11-13 | 87.06% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | -24.16% | -25.03% | 0.38% | 54.26% | -29.92% | 54.26% |
| SOL-USD | ETH-USD | 2025-05-20 | 87.06% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -10.38% | -14.10% | 4.70% | -7.67% | -16.72% | 4.70% |
| SOL-USD | LRC-USD | 2020-11-12 | 86.92% | BULL | DISTRIBUTION | SAME_BTC_ONLY | BEARISH_30D | -24.36% | -30.70% | 3.71% | -22.56% | -38.83% | 3.71% |
| SOL-USD | XLM-USD | 2025-05-20 | 86.89% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -4.32% | -7.50% | 7.05% | -12.65% | -18.68% | 7.95% |
| SOL-USD | XTZ-USD | 2019-09-19 | 86.85% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| SOL-USD | SOL-USD | 2020-11-15 | 86.57% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | -5.49% | -12.76% | 19.70% | 155.82% | -12.76% | 168.98% |
| SOL-USD | BNB-USD | 2025-05-25 | 86.48% | BULL | MIXED | SAME_BTC_ONLY | BULLISH_30D | 21.32% | -0.24% | 23.98% | 28.74% | -0.24% | 54.90% |
| SOL-USD | LINK-USD | 2025-05-20 | 86.44% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.25% | -15.36% | 5.99% | -21.96% | -30.08% | 5.99% |
| SOL-USD | ZEC-USD | 2024-05-20 | 85.97% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.14% | -24.21% | 0.00% | -2.90% | -27.89% | 6.57% |

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

