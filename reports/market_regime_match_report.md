# Market Regime Match Report

Generated: 2026-10-10 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-10 | BULL | 82.605 $ | True | 29.56% | 2.84% | BULL | 29.56% | 2.84% |
| DOGE-USD | 2026-10-10 | RECOVERY | 0.08635 $ | False | 18.80% | -4.15% | BULL | 29.56% | 2.84% |
| SOL-USD | 2026-10-10 | BULL | 109,96 $ | True | 43.04% | 4.35% | BULL | 29.56% | 2.84% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 47.50% | -1.49% | 10.35% | 23.89% | -10.45% | -20.90% | 13.82% | 24.73% | 43.42% | 52.50% | 1.73% | 29.94% | 89.66% |
| BTC-USD | SAME_BTC_REGIME | 7 | 71.43% | 5.55% | 17.45% | 31.14% | -10.29% | -22.04% | 11.08% | 31.58% | 55.48% | 57.14% | 97.72% | 119.10% | 182.76% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |
| DOGE-USD | ALL_MATCHES | 40 | 65.00% | 5.89% | 14.48% | 29.84% | -10.81% | -20.96% | 12.42% | 26.81% | 42.23% | 50.00% | 0.25% | 20.17% | 52.25% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 62.50% | 3.00% | 7.19% | 19.23% | -10.42% | -21.96% | 11.44% | 15.35% | 25.77% | 62.50% | 20.20% | 99.21% | 149.09% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 100.00% | 3.34% | 4.78% | 5.65% | -7.61% | -9.97% | 14.01% | 15.10% | 15.76% | 0.00% | -23.59% | -23.45% | -23.37% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 3.34% | 4.78% | 5.65% | -7.61% | -9.97% | 14.01% | 15.10% | 15.76% | 0.00% | -23.59% | -23.45% | -23.37% |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 3.10% | 10.51% | 22.18% | -10.32% | -20.93% | 13.62% | 22.35% | 43.10% | 40.00% | -2.67% | 27.65% | 49.18% |
| SOL-USD | SAME_BTC_REGIME | 11 | 72.73% | 5.55% | 8.19% | 21.32% | -10.18% | -20.93% | 11.81% | 15.63% | 23.98% | 54.55% | 25.03% | 67.92% | 103.66% |
| SOL-USD | SAME_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 15 | 66.67% | 1.89% | -10.11% | 24.54% | 66.67% | 5.97% | 55.08% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 5.55% | -10.29% | 31.58% | 57.14% | 97.72% | 208.16% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -23.46% | -29.48% | 3.72% | 0.00% | -14.62% | 3.72% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 17 | 23.53% | -10.01% | -12.77% | 24.51% | 41.18% | -2.56% | 25.37% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 26 | 76.92% | 9.03% | -10.81% | 25.68% | 42.31% | -0.81% | 36.20% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 3.00% | -10.42% | 15.35% | 62.50% | 20.20% | 115.79% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -7.24% | -15.10% | 42.16% | 100.00% | 17.46% | 42.16% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -9.93% | -11.88% | 26.76% | 60.00% | 0.63% | 26.76% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 78.95% | 7.08% | -10.57% | 19.83% | 26.32% | -4.85% | 29.12% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 72.73% | 5.55% | -10.18% | 15.63% | 54.55% | 25.03% | 77.77% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 10 | 30.00% | -9.18% | -11.67% | 26.41% | 50.00% | -0.75% | 29.88% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 48.39% | -1.34% | -10.57% | 24.94% | 58.06% | 3.20% | 38.50% |
| BTC-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -12.15% | -20.93% | 10.18% | 0.00% | -23.11% | 31.41% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -23.46% | -29.48% | 3.72% | 0.00% | -14.62% | 3.72% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 0.64% | -6.85% | 29.77% | 42.86% | -2.56% | 32.80% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 69.70% | 8.13% | -11.05% | 26.76% | 48.48% | -0.13% | 36.30% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 25.00% | -9.70% | -18.01% | 36.81% | 75.00% | 16.41% | 45.71% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -9.36% | -9.36% | 7.51% | 100.00% | 25.03% | 30.88% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 3.34% | -7.61% | 15.10% | 0.00% | -23.59% | 15.10% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 64.52% | 3.75% | -10.57% | 23.59% | 38.71% | -2.12% | 33.35% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -12.15% | -20.93% | 10.18% | 0.00% | -23.11% | 31.41% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -1.52% | -9.30% | 12.99% | 100.00% | 31.57% | 48.87% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 21.32% | -0.24% | 23.98% | 100.00% | 28.74% | 54.90% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 80.00% | 0.85% | -10.34% | 16.20% | 20.00% | -10.83% | 16.20% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 1 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 2 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 1 | 1 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-06-26 | 90.13% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| BTC-USD | MKR-USD | 2020-11-18 | 88.60% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| BTC-USD | LRC-USD | 2020-11-17 | 87.06% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| BTC-USD | ONE-USD | 2023-07-20 | 85.61% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -1.34% | -2.11% | 0.00% | -1.15% | -2.11% | 0.00% |
| BTC-USD | XTZ-USD | 2019-09-19 | 85.38% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| BTC-USD | DASH-USD | 2020-09-28 | 84.58% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.84% | 0.00% | 66.53% | 134.54% | 0.00% | 265.03% |
| BTC-USD | ETH-USD | 2025-05-25 | 84.39% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| DOGE-USD | XTZ-USD | 2019-09-19 | 90.72% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| DOGE-USD | LINK-USD | 2019-08-20 | 86.73% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| DOGE-USD | MKR-USD | 2020-11-18 | 85.26% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| DOGE-USD | LRC-USD | 2020-11-17 | 85.22% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| DOGE-USD | ADA-USD | 2025-05-25 | 84.98% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| DOGE-USD | RUNE-USD | 2023-06-26 | 83.40% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| DOGE-USD | ZEC-USD | 2024-05-25 | 82.51% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| DOGE-USD | LINK-USD | 2025-05-25 | 82.27% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 0.45% | -10.56% | 11.81% | -23.31% | -26.11% | 11.81% |
| SOL-USD | XTZ-USD | 2019-09-19 | 90.17% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| SOL-USD | RUNE-USD | 2023-06-26 | 89.80% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| SOL-USD | MKR-USD | 2020-11-18 | 89.27% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| SOL-USD | LRC-USD | 2020-11-17 | 88.77% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| SOL-USD | ZEC-USD | 2024-05-25 | 88.76% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| SOL-USD | ETH-USD | 2025-05-25 | 88.20% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| SOL-USD | ADA-USD | 2025-05-25 | 88.12% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| SOL-USD | LINK-USD | 2025-05-25 | 87.67% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.45% | -10.56% | 11.81% | -23.31% | -26.11% | 11.81% |
| SOL-USD | HBAR-USD | 2025-05-22 | 86.37% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -5.19% | -9.07% | 8.86% | -14.65% | -28.68% | 8.86% |
| SOL-USD | BNB-USD | 2025-05-25 | 86.09% | BULL | MIXED | SAME_BTC_ONLY | BULLISH_30D | 21.32% | -0.24% | 23.98% | 28.74% | -0.24% | 54.90% |

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

