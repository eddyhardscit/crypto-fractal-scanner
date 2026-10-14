# Market Regime Match Report

Generated: 2026-10-14 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-14 | BULL | 83.524 $ | True | 30.94% | 3.98% | BULL | 30.94% | 3.98% |
| DOGE-USD | 2026-10-14 | RECOVERY | 0.08480 $ | False | 17.22% | -3.22% | BULL | 30.94% | 3.98% |
| SOL-USD | 2026-10-14 | BULL | 107,38 $ | True | 42.66% | 6.08% | BULL | 30.94% | 3.98% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 52.50% | 2.89% | 12.12% | 21.97% | -9.86% | -23.64% | 13.48% | 21.96% | 34.34% | 47.50% | -0.55% | 19.36% | 50.30% |
| BTC-USD | SAME_BTC_REGIME | 8 | 75.00% | 6.24% | 10.16% | 36.77% | -8.15% | -18.14% | 11.71% | 13.62% | 40.99% | 37.50% | -7.82% | 30.03% | 166.60% |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 85.00% | 13.91% | 25.02% | 35.46% | -4.50% | -16.68% | 20.71% | 33.95% | 43.54% | 60.00% | 4.42% | 35.34% | 65.41% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 75.00% | 6.24% | 12.79% | 46.10% | -9.49% | -18.29% | 13.36% | 20.62% | 52.89% | 62.50% | 38.33% | 68.76% | 166.60% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | -0.63% | 2.94% | 5.09% | -8.70% | -10.21% | 12.81% | 13.21% | 13.45% | 50.00% | -15.96% | -7.30% | -2.11% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 6.52% | 6.52% | 6.52% | -6.80% | -6.80% | 13.61% | 13.61% | 13.61% | 0.00% | -33.27% | -33.27% | -33.27% |
| SOL-USD | ALL_MATCHES | 40 | 75.00% | 8.47% | 19.42% | 30.13% | -7.21% | -21.53% | 17.41% | 29.06% | 42.07% | 50.00% | 0.06% | 20.85% | 42.55% |
| SOL-USD | SAME_BTC_REGIME | 13 | 69.23% | 5.27% | 8.74% | 35.52% | -9.50% | -20.31% | 13.11% | 17.27% | 37.16% | 38.46% | -11.19% | 15.36% | 104.23% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 50.00% | -1.58% | 8.31% | 20.72% | -12.76% | -19.86% | 4.85% | 12.57% | 26.05% | 50.00% | 1.62% | 21.20% | 31.71% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 33.33% | -4.58% | -1.58% | 0.22% | -16.72% | -20.31% | 4.61% | 4.85% | 4.99% | 33.33% | -12.12% | 1.62% | 9.87% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 58.33% | 7.35% | -9.50% | 24.98% | 50.00% | 0.06% | 41.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 8 | 75.00% | 6.24% | -8.15% | 13.62% | 37.50% | -7.82% | 50.64% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 0.00% | -9.54% | -18.18% | 12.69% | 42.86% | -0.57% | 16.42% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 89.66% | 14.31% | -2.49% | 35.03% | 55.17% | 3.42% | 46.53% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 75.00% | 6.24% | -9.49% | 20.62% | 62.50% | 38.33% | 68.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 25.98% | -6.31% | 42.79% | 100.00% | 78.98% | 144.43% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -7.79% | -10.59% | 12.02% | 100.00% | 1.35% | 12.02% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 76.92% | 11.38% | -5.09% | 32.87% | 53.85% | 2.07% | 42.85% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 69.23% | 5.27% | -9.50% | 17.27% | 38.46% | -11.19% | 42.76% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 54.55% | 3.07% | -9.54% | 22.51% | 48.48% | -0.52% | 41.71% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -0.40% | -19.60% | 6.71% | 50.00% | 57.69% | 96.76% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -4.66% | -9.50% | 12.02% | 40.00% | -12.41% | 13.61% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 90.91% | 15.44% | -3.12% | 40.91% | 57.58% | 3.50% | 51.03% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 7.61% | -12.48% | 28.37% | 100.00% | 36.76% | 52.02% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 5.95% | -15.96% | 12.12% | 66.67% | 41.88% | 81.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -0.63% | -8.70% | 13.21% | 50.00% | -15.96% | 13.21% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 79.31% | 11.15% | -5.52% | 30.68% | 51.72% | 0.65% | 42.87% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | -1.58% | -12.76% | 12.57% | 50.00% | 1.62% | 32.42% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -0.40% | -15.87% | 17.42% | 50.00% | 18.71% | 62.03% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 41.98% | 0.00% | 41.98% | 100.00% | 11.39% | 52.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 8.10% | -8.15% | 12.79% | 0.00% | -26.57% | 12.79% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 0 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 1 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 3 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-01 | 89.20% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| BTC-USD | MKR-USD | 2020-11-23 | 86.50% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| BTC-USD | ADA-USD | 2025-05-30 | 85.63% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| BTC-USD | ONE-USD | 2023-07-25 | 85.41% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -0.10% | -0.87% | 1.16% | 0.10% | -0.87% | 1.16% |
| BTC-USD | ETH-USD | 2025-05-30 | 84.62% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| BTC-USD | LRC-USD | 2020-11-22 | 84.45% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| BTC-USD | XLM-USD | 2025-05-25 | 84.07% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| BTC-USD | HBAR-USD | 2025-05-27 | 83.97% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| DOGE-USD | LINK-USD | 2019-08-25 | 85.60% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| DOGE-USD | MKR-USD | 2020-11-23 | 85.60% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| DOGE-USD | ADA-USD | 2025-05-30 | 84.66% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| DOGE-USD | LRC-USD | 2020-11-22 | 83.82% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| DOGE-USD | RUNE-USD | 2023-07-01 | 83.51% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| DOGE-USD | ZEC-USD | 2024-05-30 | 82.52% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| DOGE-USD | HBAR-USD | 2025-05-27 | 82.11% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| DOGE-USD | MKR-USD | 2023-05-17 | 81.78% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.95% | -1.75% | 30.65% | 51.74% | -1.75% | 51.74% |
| SOL-USD | MKR-USD | 2020-11-23 | 89.76% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| SOL-USD | RUNE-USD | 2023-07-01 | 88.38% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| SOL-USD | ADA-USD | 2025-05-30 | 88.20% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| SOL-USD | LRC-USD | 2020-11-22 | 88.14% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| SOL-USD | ETH-USD | 2025-05-30 | 87.89% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| SOL-USD | LINK-USD | 2025-05-30 | 87.73% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -9.44% | 13.20% | -31.77% | -33.69% | 13.20% |
| SOL-USD | HBAR-USD | 2025-05-27 | 87.30% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| SOL-USD | LINK-USD | 2019-08-20 | 86.86% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| SOL-USD | ZEC-USD | 2024-05-30 | 86.76% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| SOL-USD | BNB-USD | 2025-05-30 | 86.68% | BULL | MIXED | SAME_BTC_ONLY | BULLISH_30D | 41.98% | 0.00% | 41.98% | 11.39% | 0.00% | 52.04% |

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

