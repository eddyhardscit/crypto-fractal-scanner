# Market Regime Match Report

Generated: 2026-10-15 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-15 | BULL | 80.995 $ | True | 26.75% | 4.28% | BULL | 26.75% | 4.28% |
| DOGE-USD | 2026-10-15 | RECOVERY | 0.07980 $ | False | 10.05% | -2.99% | BULL | 26.75% | 4.28% |
| SOL-USD | 2026-10-15 | BULL | 102,21 $ | True | 36.26% | 6.53% | BULL | 26.75% | 4.28% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 52.50% | 4.51% | 14.67% | 30.39% | -10.04% | -27.35% | 13.48% | 24.98% | 41.91% | 50.00% | -0.21% | 20.58% | 67.90% |
| BTC-USD | SAME_BTC_REGIME | 6 | 66.67% | 6.24% | 8.89% | 52.55% | -10.84% | -19.60% | 8.64% | 12.79% | 59.19% | 50.00% | -2.18% | 89.89% | 197.79% |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 77.50% | 14.16% | 22.00% | 34.05% | -3.15% | -16.84% | 19.89% | 30.66% | 44.33% | 52.50% | 1.43% | 26.67% | 60.43% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 62.50% | 6.24% | 12.79% | 46.10% | -10.87% | -18.29% | 12.52% | 20.62% | 52.89% | 62.50% | 38.33% | 68.76% | 166.60% |
| DOGE-USD | SAME_ASSET_REGIME | 3 | 33.33% | -5.07% | 0.73% | 4.20% | -9.57% | -10.39% | 12.02% | 12.81% | 13.29% | 33.33% | -20.75% | -9.70% | -3.07% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 0.73% | 3.62% | 5.36% | -8.18% | -9.29% | 12.52% | 13.06% | 13.39% | 0.00% | -27.01% | -23.88% | -22.00% |
| SOL-USD | ALL_MATCHES | 40 | 77.50% | 10.41% | 19.42% | 35.62% | -5.44% | -21.22% | 17.41% | 28.62% | 42.95% | 57.50% | 2.50% | 18.89% | 61.33% |
| SOL-USD | SAME_BTC_REGIME | 13 | 76.92% | 5.95% | 9.67% | 36.59% | -9.50% | -21.58% | 13.11% | 15.51% | 37.04% | 46.15% | -4.45% | 41.88% | 110.96% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 50.00% | -6.98% | -2.78% | -0.26% | -13.89% | -19.75% | 4.85% | 4.97% | 5.04% | 50.00% | 1.62% | 8.49% | 12.61% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | -6.98% | -2.78% | -0.26% | -13.89% | -19.75% | 4.85% | 4.97% | 5.04% | 50.00% | 1.62% | 8.49% | 12.61% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 27 | 59.26% | 7.72% | -7.63% | 28.72% | 51.85% | 0.65% | 42.90% |
| BTC-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 6.24% | -10.84% | 12.79% | 50.00% | -2.18% | 96.76% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -23.26% | -27.07% | 0.00% | 0.00% | -15.30% | 0.00% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 0.00% | -9.26% | -18.18% | 12.02% | 40.00% | -0.57% | 13.36% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 82.76% | 14.31% | -0.41% | 30.68% | 44.83% | -0.68% | 42.82% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 6.24% | -10.87% | 20.62% | 62.50% | 38.33% | 68.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 25.98% | -6.31% | 42.79% | 100.00% | 78.98% | 144.43% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -7.79% | -10.59% | 12.02% | 100.00% | 1.35% | 12.02% |
| SOL-USD | HISTORICAL_BTC_BEAR | 25 | 80.00% | 13.61% | -0.93% | 33.60% | 60.00% | 3.50% | 42.82% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 76.92% | 5.95% | -9.50% | 15.51% | 46.15% | -4.45% | 52.04% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -7.79% | -10.59% | 12.02% | 100.00% | 1.35% | 12.02% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 30 | 56.67% | 7.35% | -8.60% | 27.93% | 53.33% | 0.37% | 42.95% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -0.40% | -19.60% | 6.71% | 50.00% | 57.69% | 96.76% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -25.34% | -29.19% | 0.00% | 0.00% | -26.38% | 0.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 0.75% | -8.15% | 13.21% | 50.00% | -5.53% | 17.58% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 84.38% | 15.60% | -1.35% | 31.41% | 50.00% | 0.49% | 46.84% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 10.09% | -10.24% | 34.91% | 100.00% | 36.08% | 57.76% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 5.95% | -15.96% | 12.12% | 66.67% | 41.88% | 81.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -5.07% | -9.57% | 12.81% | 33.33% | -20.75% | 12.81% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 82.76% | 13.61% | -2.49% | 33.60% | 58.62% | 3.50% | 42.87% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | -6.98% | -13.89% | 4.97% | 50.00% | 1.62% | 19.49% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 60.00% | 5.95% | -15.96% | 15.51% | 60.00% | 41.88% | 75.50% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 41.98% | 0.00% | 41.98% | 100.00% | 11.39% | 52.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 6.52% | -9.50% | 12.81% | 33.33% | -19.86% | 12.81% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 0 | 6 | 6 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 2 | 3 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 2 | 2 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-01 | 90.33% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| BTC-USD | LRC-USD | 2020-11-22 | 87.74% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| BTC-USD | MKR-USD | 2020-11-23 | 87.59% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| BTC-USD | ADA-USD | 2025-05-30 | 86.67% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| BTC-USD | ONE-USD | 2023-07-25 | 85.64% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -0.10% | -0.87% | 1.16% | 0.10% | -0.87% | 1.16% |
| BTC-USD | ETH-USD | 2025-05-30 | 85.51% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| DOGE-USD | LINK-USD | 2019-08-25 | 87.91% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| DOGE-USD | LRC-USD | 2020-11-22 | 86.68% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| DOGE-USD | ADA-USD | 2025-05-30 | 84.99% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| DOGE-USD | ZEC-USD | 2024-05-30 | 84.98% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| DOGE-USD | MKR-USD | 2020-11-23 | 84.69% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| DOGE-USD | RUNE-USD | 2023-07-01 | 82.87% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| DOGE-USD | ZEC-USD | 2021-09-08 | 81.79% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | -5.07% | -9.57% | 11.42% | -20.75% | -41.73% | 11.42% |
| DOGE-USD | MKR-USD | 2023-05-17 | 81.57% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.95% | -1.75% | 30.65% | 51.74% | -1.75% | 51.74% |
| SOL-USD | MKR-USD | 2020-11-23 | 90.92% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| SOL-USD | LRC-USD | 2020-11-22 | 89.59% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| SOL-USD | ADA-USD | 2025-05-30 | 89.29% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| SOL-USD | ZEC-USD | 2024-05-30 | 88.89% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| SOL-USD | ETH-USD | 2025-05-30 | 88.75% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| SOL-USD | LINK-USD | 2025-05-30 | 88.66% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -9.44% | 13.20% | -31.77% | -33.69% | 13.20% |
| SOL-USD | RUNE-USD | 2023-07-01 | 88.60% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| SOL-USD | HBAR-USD | 2025-05-27 | 86.87% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| SOL-USD | SNX-USD | 2020-11-22 | 86.61% | BULL | DISTRIBUTION | SAME_BTC_ONLY | BEARISH_30D | -14.46% | -21.67% | 9.63% | -11.74% | -33.57% | 9.63% |
| SOL-USD | LINK-USD | 2019-08-20 | 86.42% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |

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

