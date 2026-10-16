# Market Regime Match Report

Generated: 2026-10-16 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-16 | BULL | 82.104 $ | True | 26.71% | 4.55% | BULL | 26.71% | 4.55% |
| DOGE-USD | 2026-10-16 | RECOVERY | 0.08215 $ | False | 13.36% | -2.77% | BULL | 26.71% | 4.55% |
| SOL-USD | 2026-10-16 | BULL | 105,82 $ | True | 40.23% | 6.96% | BULL | 26.71% | 4.55% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 7.60% | 17.56% | 34.20% | -7.72% | -24.63% | 13.99% | 27.12% | 41.91% | 50.00% | -0.21% | 19.97% | 67.90% |
| BTC-USD | SAME_BTC_REGIME | 9 | 77.78% | 6.52% | 9.67% | 30.91% | -9.50% | -17.42% | 12.63% | 13.61% | 32.77% | 33.33% | -19.22% | 0.10% | 151.01% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 21.09% | 27.52% | 31.38% | -9.17% | -13.05% | 28.19% | 35.97% | 40.64% | 50.00% | 9.08% | 23.23% | 31.72% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 8.23% | 8.23% | 8.23% | -14.02% | -14.02% | 12.63% | 12.63% | 12.63% | 0.00% | -19.22% | -19.22% | -19.22% |
| DOGE-USD | ALL_MATCHES | 40 | 75.00% | 14.16% | 22.00% | 34.05% | -3.34% | -23.00% | 19.36% | 30.02% | 41.26% | 45.00% | -0.98% | 19.61% | 43.67% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 62.50% | 6.24% | 10.25% | 38.97% | -10.87% | -18.29% | 12.52% | 15.40% | 43.52% | 50.00% | 15.17% | 61.36% | 166.60% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | 0.73% | 3.62% | 5.36% | -8.18% | -9.29% | 12.52% | 13.06% | 13.39% | 0.00% | -27.01% | -23.88% | -22.00% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 0.73% | 3.62% | 5.36% | -8.18% | -9.29% | 12.52% | 13.06% | 13.39% | 0.00% | -27.01% | -23.88% | -22.00% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 9.81% | 19.42% | 29.41% | -6.08% | -21.80% | 16.43% | 27.12% | 42.95% | 47.50% | -0.60% | 22.43% | 61.33% |
| SOL-USD | SAME_BTC_REGIME | 13 | 76.92% | 8.23% | 9.94% | 22.97% | -11.05% | -20.53% | 12.63% | 15.51% | 27.98% | 38.46% | -8.21% | 51.74% | 110.96% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 100.00% | 9.94% | 21.94% | 29.15% | -4.32% | -12.08% | 12.63% | 28.19% | 37.53% | 33.33% | -8.21% | 14.59% | 28.26% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 9.08% | 9.51% | 9.77% | -7.01% | -12.62% | 12.31% | 12.47% | 12.57% | 0.00% | -13.72% | -10.96% | -9.31% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 25 | 64.00% | 11.61% | -5.35% | 30.68% | 56.00% | 6.55% | 42.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 77.78% | 6.52% | -9.50% | 13.61% | 33.33% | -19.22% | 27.57% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 0.00% | -9.26% | -18.18% | 12.02% | 40.00% | -0.57% | 13.36% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 31 | 77.42% | 14.31% | -0.02% | 32.14% | 41.94% | -1.28% | 42.70% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 6.24% | -10.87% | 15.40% | 50.00% | 15.17% | 62.03% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 69.23% | 12.78% | -2.18% | 28.81% | 50.00% | 0.49% | 36.92% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 76.92% | 8.23% | -11.05% | 15.51% | 38.46% | -8.21% | 51.74% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 62.07% | 11.15% | -7.63% | 28.53% | 51.72% | 0.10% | 42.42% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 21.09% | -9.17% | 35.97% | 50.00% | 9.08% | 51.74% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -0.40% | -19.60% | 6.71% | 50.00% | 57.69% | 96.76% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -27.42% | -31.31% | 0.00% | 0.00% | -37.46% | 0.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 0.47% | -8.15% | 13.21% | 50.00% | -5.53% | 17.53% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 78.79% | 14.78% | -1.65% | 30.68% | 42.42% | -1.28% | 42.99% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 10.09% | -10.24% | 34.91% | 100.00% | 36.08% | 57.76% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 5.95% | -15.96% | 12.12% | 66.67% | 41.88% | 81.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 0.73% | -8.18% | 13.06% | 0.00% | -27.01% | 13.06% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 70.00% | 12.78% | -2.80% | 28.81% | 50.00% | 0.49% | 41.20% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 100.00% | 9.94% | -4.32% | 28.19% | 33.33% | -8.21% | 39.47% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 60.00% | 5.95% | -15.96% | 15.51% | 60.00% | 41.88% | 75.50% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 8.10% | -8.15% | 12.79% | 0.00% | -26.57% | 12.79% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 2 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 2 | 3 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-01 | 90.49% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| BTC-USD | LRC-USD | 2020-11-22 | 88.45% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| BTC-USD | MKR-USD | 2020-11-23 | 87.81% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| BTC-USD | ADA-USD | 2025-05-30 | 87.35% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| BTC-USD | ETH-USD | 2025-05-30 | 86.65% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| BTC-USD | ONE-USD | 2023-07-25 | 84.86% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -0.10% | -0.87% | 1.16% | 0.10% | -0.87% | 1.16% |
| BTC-USD | LINK-USD | 2025-05-30 | 84.35% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -9.44% | 13.20% | -31.77% | -33.69% | 13.20% |
| BTC-USD | XLM-USD | 2025-05-30 | 84.29% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 14.78% | -1.65% | 14.78% | -21.24% | -24.08% | 14.78% |
| BTC-USD | DOGE-USD | 2024-01-16 | 83.95% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 8.23% | -14.02% | 12.63% | -19.22% | -19.22% | 14.94% |
| DOGE-USD | LINK-USD | 2019-08-25 | 87.95% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| DOGE-USD | LRC-USD | 2020-11-22 | 86.98% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| DOGE-USD | ZEC-USD | 2024-05-30 | 85.66% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| DOGE-USD | ADA-USD | 2025-05-30 | 84.90% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| DOGE-USD | MKR-USD | 2020-11-23 | 83.82% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| DOGE-USD | XLM-USD | 2025-05-30 | 82.03% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 14.78% | -1.65% | 14.78% | -21.24% | -24.08% | 14.78% |
| DOGE-USD | ZEC-USD | 2021-09-08 | 81.97% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | -5.07% | -9.57% | 11.42% | -20.75% | -41.73% | 11.42% |
| DOGE-USD | RUNE-USD | 2023-07-01 | 81.90% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| SOL-USD | MKR-USD | 2020-11-23 | 91.28% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| SOL-USD | ADA-USD | 2025-05-30 | 90.15% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| SOL-USD | ETH-USD | 2025-05-30 | 89.85% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| SOL-USD | ZEC-USD | 2024-05-30 | 89.68% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| SOL-USD | LRC-USD | 2020-11-22 | 89.61% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| SOL-USD | LINK-USD | 2025-05-30 | 89.53% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -9.44% | 13.20% | -31.77% | -33.69% | 13.20% |
| SOL-USD | RUNE-USD | 2023-07-01 | 88.24% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| SOL-USD | SNX-USD | 2020-11-22 | 87.46% | BULL | DISTRIBUTION | SAME_BTC_ONLY | BEARISH_30D | -14.46% | -21.67% | 9.63% | -11.74% | -33.57% | 9.63% |
| SOL-USD | LINK-USD | 2020-11-27 | 86.87% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 15.02% | -11.05% | 15.51% | 75.50% | -11.05% | 75.50% |
| SOL-USD | DOGE-USD | 2024-01-16 | 86.71% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 8.23% | -14.02% | 12.63% | -19.22% | -19.22% | 14.94% |

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

