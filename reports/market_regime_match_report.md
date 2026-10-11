# Market Regime Match Report

Generated: 2026-10-11 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-11 | BULL | 82.976 $ | True | 33.32% | 3.12% | BULL | 33.32% | 3.12% |
| DOGE-USD | 2026-10-11 | RECOVERY | 0.08535 $ | False | 18.79% | -3.92% | BULL | 33.32% | 3.12% |
| SOL-USD | 2026-10-11 | BULL | 109,54 $ | True | 46.32% | 4.78% | BULL | 33.32% | 3.12% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 45.00% | -2.05% | 9.35% | 24.03% | -13.79% | -21.07% | 11.93% | 21.98% | 41.50% | 40.00% | -2.34% | 19.63% | 38.71% |
| BTC-USD | SAME_BTC_REGIME | 7 | 57.14% | 0.85% | 8.59% | 23.22% | -10.34% | -22.04% | 10.18% | 12.37% | 27.44% | 28.57% | -10.83% | 48.29% | 160.67% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 0.00% | -8.36% | -6.47% | -5.34% | -18.83% | -20.51% | 7.19% | 8.69% | 9.58% | 0.00% | -22.42% | -22.08% | -21.88% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 0.00% | -8.36% | -6.47% | -5.34% | -18.83% | -20.51% | 7.19% | 8.69% | 9.58% | 0.00% | -22.42% | -22.08% | -21.88% |
| DOGE-USD | ALL_MATCHES | 40 | 72.50% | 6.66% | 13.35% | 26.44% | -10.18% | -21.22% | 12.42% | 20.24% | 42.44% | 45.00% | -1.22% | 17.88% | 39.71% |
| DOGE-USD | SAME_BTC_REGIME | 9 | 66.67% | 5.55% | 10.07% | 17.42% | -10.29% | -21.71% | 11.81% | 15.06% | 22.58% | 55.56% | 15.36% | 97.72% | 133.95% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 100.00% | 3.34% | 4.78% | 5.65% | -7.61% | -9.97% | 14.01% | 15.10% | 15.76% | 0.00% | -23.59% | -23.45% | -23.37% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 3.34% | 4.78% | 5.65% | -7.61% | -9.97% | 14.01% | 15.10% | 15.76% | 0.00% | -23.59% | -23.45% | -23.37% |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 2.76% | 9.91% | 21.37% | -10.56% | -21.00% | 12.98% | 18.02% | 26.90% | 40.00% | -2.67% | 19.50% | 39.16% |
| SOL-USD | SAME_BTC_REGIME | 11 | 72.73% | 5.55% | 8.19% | 21.32% | -10.29% | -20.93% | 14.82% | 17.04% | 23.98% | 54.55% | 25.03% | 67.92% | 103.66% |
| SOL-USD | SAME_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 16 | 75.00% | 7.40% | -10.38% | 23.39% | 56.25% | 5.66% | 38.22% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 57.14% | 0.85% | -10.34% | 12.37% | 28.57% | -10.83% | 66.03% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 17 | 11.76% | -11.35% | -15.58% | 22.51% | 29.41% | -5.57% | 22.51% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 75.86% | 7.39% | -10.11% | 20.59% | 41.38% | -1.28% | 37.20% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 66.67% | 5.55% | -10.29% | 15.06% | 55.56% | 15.36% | 100.64% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | -1.26% | -10.76% | 22.23% | 50.00% | 6.04% | 22.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 77.27% | 3.41% | -11.18% | 17.40% | 27.27% | -4.65% | 22.82% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 72.73% | 5.55% | -10.29% | 17.04% | 54.55% | 25.03% | 77.77% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 7 | 28.57% | -9.93% | -11.88% | 23.94% | 57.14% | 0.63% | 26.06% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 48.39% | -1.34% | -14.81% | 22.16% | 45.16% | -1.15% | 28.84% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -8.36% | -18.83% | 8.69% | 0.00% | -22.42% | 26.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 42.86% | -2.61% | -10.34% | 29.77% | 28.57% | -5.63% | 30.55% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 76.47% | 7.76% | -10.18% | 20.47% | 44.12% | -1.22% | 40.97% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -12.15% | -20.93% | 22.61% | 66.67% | 15.36% | 43.88% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -9.36% | -9.36% | 7.51% | 100.00% | 25.03% | 30.88% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 3.34% | -7.61% | 15.10% | 0.00% | -23.59% | 15.10% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 32 | 68.75% | 3.41% | -11.18% | 19.30% | 40.62% | -1.64% | 32.39% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -12.15% | -20.93% | 10.18% | 0.00% | -23.11% | 31.41% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -8.87% | -9.36% | 16.35% | 66.67% | 25.03% | 42.87% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 21.32% | -0.24% | 23.98% | 100.00% | 28.74% | 54.90% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 100.00% | 0.85% | -10.34% | 14.01% | 0.00% | -23.31% | 14.01% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 2 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 1 | 1 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-06-26 | 90.41% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| BTC-USD | MKR-USD | 2020-11-18 | 88.74% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| BTC-USD | LRC-USD | 2020-11-17 | 87.81% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| BTC-USD | ETH-USD | 2025-05-25 | 85.51% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| BTC-USD | ONE-USD | 2023-07-20 | 84.80% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -1.34% | -2.11% | 0.00% | -1.15% | -2.11% | 0.00% |
| BTC-USD | XLM-USD | 2025-05-25 | 84.77% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| BTC-USD | DOGE-USD | 2024-01-11 | 84.25% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -4.58% | -16.72% | 4.20% | -21.74% | -21.74% | 11.32% |
| DOGE-USD | XTZ-USD | 2019-09-19 | 88.05% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| DOGE-USD | LINK-USD | 2019-08-20 | 86.60% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| DOGE-USD | LRC-USD | 2020-11-17 | 85.74% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| DOGE-USD | MKR-USD | 2020-11-18 | 84.68% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| DOGE-USD | ADA-USD | 2025-05-25 | 84.62% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| DOGE-USD | ZEC-USD | 2024-05-25 | 83.33% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| DOGE-USD | RUNE-USD | 2023-06-26 | 82.71% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| DOGE-USD | XLM-USD | 2025-05-25 | 82.27% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| DOGE-USD | LINK-USD | 2025-05-25 | 82.21% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 0.45% | -10.56% | 11.81% | -23.31% | -26.11% | 11.81% |
| SOL-USD | MKR-USD | 2020-11-18 | 89.81% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| SOL-USD | ZEC-USD | 2024-05-25 | 89.55% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| SOL-USD | RUNE-USD | 2023-06-26 | 89.54% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| SOL-USD | ETH-USD | 2025-05-25 | 89.37% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| SOL-USD | ADA-USD | 2025-05-25 | 88.80% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| SOL-USD | LRC-USD | 2020-11-17 | 88.75% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| SOL-USD | XTZ-USD | 2019-09-19 | 88.68% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| SOL-USD | LINK-USD | 2025-05-25 | 88.66% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.45% | -10.56% | 11.81% | -23.31% | -26.11% | 11.81% |
| SOL-USD | LINK-USD | 2020-11-22 | 86.74% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 6.32% | -9.25% | 14.82% | 38.11% | -9.25% | 54.86% |
| SOL-USD | SNX-USD | 2020-11-17 | 86.52% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -8.87% | -15.78% | 17.87% | -26.68% | -28.58% | 17.87% |

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

