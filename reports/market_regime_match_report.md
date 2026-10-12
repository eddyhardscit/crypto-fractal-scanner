# Market Regime Match Report

Generated: 2026-10-12 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-12 | BULL | 83.863 $ | True | 29.11% | 3.38% | BULL | 29.11% | 3.38% |
| DOGE-USD | 2026-10-12 | RECOVERY | 0.08754 $ | False | 17.60% | -3.71% | BULL | 29.11% | 3.38% |
| SOL-USD | 2026-10-12 | BULL | 112,60 $ | True | 44.80% | 5.18% | BULL | 29.11% | 3.38% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 45.00% | -2.34% | 7.97% | 22.48% | -15.54% | -30.60% | 10.19% | 20.00% | 38.92% | 37.50% | -4.65% | 18.84% | 49.18% |
| BTC-USD | SAME_BTC_REGIME | 6 | 66.67% | 3.20% | 10.11% | 26.11% | -13.53% | -22.31% | 10.63% | 13.01% | 30.88% | 33.33% | -12.65% | 70.58% | 176.41% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 0.00% | -8.36% | -6.47% | -5.34% | -18.83% | -20.51% | 7.19% | 8.69% | 9.58% | 0.00% | -22.42% | -22.08% | -21.88% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 0.00% | -8.36% | -6.47% | -5.34% | -18.83% | -20.51% | 7.19% | 8.69% | 9.58% | 0.00% | -22.42% | -22.08% | -21.88% |
| DOGE-USD | ALL_MATCHES | 40 | 70.00% | 6.60% | 11.94% | 21.97% | -9.39% | -24.85% | 12.95% | 20.74% | 31.37% | 40.00% | -2.25% | 11.45% | 31.79% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 62.50% | 3.99% | 5.72% | 7.85% | -9.40% | -21.02% | 12.09% | 13.31% | 14.42% | 37.50% | -12.83% | 17.78% | 46.84% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | -16.97% | -5.37% | 1.59% | -28.68% | -47.89% | 12.41% | 14.31% | 15.44% | 0.00% | -22.65% | -22.04% | -21.68% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 6.23% | 6.23% | 6.23% | -4.67% | -4.67% | 16.20% | 16.20% | 16.20% | 0.00% | -23.87% | -23.87% | -23.87% |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 2.76% | 10.61% | 28.62% | -9.95% | -21.43% | 14.24% | 21.98% | 35.70% | 42.50% | -2.25% | 25.11% | 39.71% |
| SOL-USD | SAME_BTC_REGIME | 14 | 71.43% | 3.49% | 9.13% | 31.91% | -10.23% | -19.67% | 12.73% | 15.92% | 34.75% | 42.86% | -11.47% | 34.84% | 101.88% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 50.00% | -1.58% | 8.31% | 20.72% | -12.76% | -19.67% | 7.40% | 16.39% | 27.57% | 25.00% | -16.93% | 0.59% | 23.47% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 33.33% | -4.58% | -1.58% | 0.22% | -16.72% | -20.09% | 4.61% | 7.40% | 9.07% | 0.00% | -21.74% | -16.93% | -14.04% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 59.09% | 0.54% | -12.89% | 23.90% | 50.00% | 2.61% | 41.04% |
| BTC-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 3.20% | -13.53% | 13.01% | 33.33% | -12.65% | 83.33% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 12 | 8.33% | -12.54% | -16.22% | 17.49% | 16.67% | -5.89% | 17.49% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 73.33% | 7.76% | -8.98% | 21.58% | 40.00% | -1.22% | 35.06% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 3.99% | -9.40% | 13.31% | 37.50% | -12.83% | 31.02% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -13.73% | -15.63% | 12.79% | 0.00% | -5.57% | 12.79% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 71.43% | 6.98% | -8.82% | 27.27% | 42.86% | -1.28% | 40.37% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 71.43% | 3.49% | -10.23% | 15.92% | 42.86% | -11.47% | 54.16% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -13.73% | -15.63% | 16.97% | 40.00% | -0.57% | 22.51% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 34 | 50.00% | -0.82% | -15.54% | 22.33% | 44.12% | -0.88% | 39.09% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -8.36% | -18.83% | 8.69% | 0.00% | -22.42% | 26.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -6.98% | -11.55% | 11.18% | 0.00% | -10.33% | 11.18% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 76.47% | 7.24% | -9.29% | 20.87% | 38.24% | -2.25% | 35.06% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -12.15% | -20.93% | 22.61% | 66.67% | 15.36% | 43.88% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -9.36% | -9.36% | 7.51% | 100.00% | 25.03% | 30.88% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -16.97% | -28.68% | 14.31% | 0.00% | -22.65% | 14.31% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 5.55% | -10.18% | 22.51% | 44.83% | -0.57% | 40.37% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | -1.58% | -12.76% | 16.39% | 25.00% | -16.93% | 37.64% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -8.87% | -9.36% | 16.35% | 66.67% | 25.03% | 42.87% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 41.98% | 0.00% | 41.98% | 100.00% | 11.39% | 52.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 100.00% | 0.85% | -10.34% | 14.01% | 0.00% | -23.31% | 14.01% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 6 | 6 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 1 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 3 | 4 | 14 | 14 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-06-26 | 89.67% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| BTC-USD | MKR-USD | 2020-11-18 | 87.59% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| BTC-USD | LRC-USD | 2020-11-17 | 86.64% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| BTC-USD | XLM-USD | 2025-05-25 | 85.87% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| BTC-USD | ETH-USD | 2025-05-25 | 85.05% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| BTC-USD | DOGE-USD | 2024-01-11 | 84.52% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -4.58% | -16.72% | 4.20% | -21.74% | -21.74% | 11.32% |
| DOGE-USD | LINK-USD | 2019-08-20 | 85.41% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| DOGE-USD | LRC-USD | 2020-11-17 | 83.38% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| DOGE-USD | ADA-USD | 2025-05-25 | 82.81% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| DOGE-USD | MKR-USD | 2020-11-18 | 82.79% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| DOGE-USD | XLM-USD | 2025-05-25 | 82.49% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| DOGE-USD | ZEC-USD | 2024-05-25 | 82.45% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| DOGE-USD | HBAR-USD | 2025-05-27 | 82.16% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| DOGE-USD | LINK-USD | 2025-05-30 | 81.69% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -9.44% | 13.20% | -31.77% | -33.69% | 13.20% |
| SOL-USD | MKR-USD | 2020-11-18 | 89.46% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| SOL-USD | ETH-USD | 2025-05-25 | 88.95% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| SOL-USD | ZEC-USD | 2024-05-25 | 88.68% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| SOL-USD | RUNE-USD | 2023-06-26 | 88.61% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| SOL-USD | ADA-USD | 2025-05-25 | 88.15% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| SOL-USD | LINK-USD | 2025-05-25 | 87.90% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.45% | -10.56% | 11.81% | -23.31% | -26.11% | 11.81% |
| SOL-USD | LRC-USD | 2020-11-17 | 87.33% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| SOL-USD | XTZ-USD | 2019-09-19 | 86.83% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| SOL-USD | BNB-USD | 2025-05-30 | 86.64% | BULL | MIXED | SAME_BTC_ONLY | BULLISH_30D | 41.98% | 0.00% | 41.98% | 11.39% | 0.00% | 52.04% |
| SOL-USD | LINK-USD | 2020-11-22 | 86.52% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 6.32% | -9.25% | 14.82% | 38.11% | -9.25% | 54.86% |

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

