# Market Regime Match Report

Generated: 2026-10-18 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-18 | BULL | 81.642 $ | True | 25.16% | 4.97% | BULL | 25.16% | 4.97% |
| DOGE-USD | 2026-10-18 | RECOVERY | 0.07915 $ | False | 9.72% | -2.50% | BULL | 25.16% | 4.97% |
| SOL-USD | 2026-10-18 | BULL | 103,44 $ | True | 32.97% | 7.62% | BULL | 25.16% | 4.97% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 6.96% | 19.14% | 32.19% | -8.15% | -24.07% | 13.12% | 26.51% | 34.61% | 47.50% | -1.95% | 20.58% | 60.31% |
| BTC-USD | SAME_BTC_REGIME | 8 | 75.00% | 7.37% | 10.95% | 73.18% | -9.00% | -18.14% | 11.48% | 13.90% | 73.18% | 25.00% | -19.54% | 26.62% | 157.17% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 21.09% | 27.52% | 31.38% | -9.17% | -13.05% | 28.19% | 35.97% | 40.64% | 50.00% | 9.08% | 23.23% | 31.72% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 8.23% | 8.23% | 8.23% | -14.02% | -14.02% | 12.63% | 12.63% | 12.63% | 0.00% | -19.22% | -19.22% | -19.22% |
| DOGE-USD | ALL_MATCHES | 40 | 75.00% | 11.17% | 19.44% | 29.65% | -4.25% | -22.69% | 15.56% | 24.15% | 45.78% | 42.50% | -7.17% | 17.92% | 65.47% |
| DOGE-USD | SAME_BTC_REGIME | 5 | 60.00% | 2.85% | 8.74% | 129.16% | -8.50% | -17.36% | 11.30% | 17.27% | 132.58% | 80.00% | 41.88% | 126.27% | 197.10% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 60.00% | 6.24% | 13.91% | 29.41% | -8.22% | -44.08% | 12.31% | 20.06% | 31.96% | 35.00% | -8.97% | 15.09% | 52.54% |
| SOL-USD | SAME_BTC_REGIME | 14 | 71.43% | 7.37% | 9.87% | 21.90% | -8.97% | -20.02% | 12.31% | 14.48% | 26.64% | 35.71% | -9.97% | 40.11% | 99.40% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 9.08% | 15.94% | 26.75% | -9.17% | -15.52% | 12.31% | 20.41% | 34.42% | 50.00% | 13.29% | 35.44% | 36.60% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 66.67% | 8.23% | 9.08% | 9.59% | -14.02% | -15.73% | 11.98% | 12.31% | 12.50% | 33.33% | -8.21% | 13.29% | 26.19% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 29 | 62.07% | 9.64% | -6.95% | 28.53% | 51.72% | 3.50% | 44.59% |
| BTC-USD | HISTORICAL_BTC_BULL | 8 | 75.00% | 7.37% | -9.00% | 13.90% | 25.00% | -19.54% | 50.64% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -7.79% | -10.59% | 10.60% | 66.67% | 1.35% | 16.78% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 35 | 77.14% | 11.57% | -4.01% | 24.48% | 37.14% | -7.89% | 32.54% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 2.85% | -8.50% | 17.27% | 80.00% | 41.88% | 169.44% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 53.85% | 3.30% | -7.31% | 22.32% | 34.62% | -8.51% | 27.79% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 71.43% | 7.37% | -8.97% | 14.48% | 35.71% | -9.97% | 41.83% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 62.07% | 9.64% | -7.67% | 26.65% | 51.72% | 3.50% | 42.99% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 21.09% | -9.17% | 35.97% | 50.00% | 9.08% | 51.74% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 5.95% | -15.96% | 19.58% | 33.33% | -3.38% | 82.21% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -27.42% | -31.31% | 0.00% | 0.00% | -37.46% | 0.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -7.37% | -9.50% | 12.02% | 40.00% | -12.41% | 13.61% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 37 | 75.68% | 11.19% | -4.13% | 23.82% | 37.84% | -7.89% | 32.79% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 10.09% | -10.24% | 34.91% | 100.00% | 36.08% | 57.76% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 8.74% | -4.86% | 17.27% | 100.00% | 41.88% | 42.76% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 58.62% | 5.27% | -7.67% | 22.84% | 34.48% | -9.73% | 28.04% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 9.08% | -9.17% | 20.41% | 50.00% | 13.29% | 45.29% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -0.40% | -18.82% | 11.54% | 50.00% | 18.71% | 62.03% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 6.52% | -9.50% | 11.96% | 0.00% | -26.27% | 11.96% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 0 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 3 | 4 | 14 | 14 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-06 | 87.56% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| BTC-USD | LRC-USD | 2020-11-22 | 85.97% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| BTC-USD | XLM-USD | 2025-05-30 | 85.71% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 14.78% | -1.65% | 14.78% | -21.24% | -24.08% | 14.78% |
| BTC-USD | MKR-USD | 2020-11-23 | 85.36% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| BTC-USD | ETH-USD | 2025-05-30 | 84.73% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| BTC-USD | ADA-USD | 2025-05-30 | 84.63% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| BTC-USD | HBAR-USD | 2025-06-01 | 84.57% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| BTC-USD | DOGE-USD | 2024-01-16 | 83.69% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 8.23% | -14.02% | 12.63% | -19.22% | -19.22% | 14.94% |
| DOGE-USD | LINK-USD | 2019-08-25 | 85.61% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| DOGE-USD | ZEC-USD | 2024-05-30 | 83.32% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| DOGE-USD | MKR-USD | 2020-11-28 | 82.71% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| DOGE-USD | RUNE-USD | 2023-07-06 | 82.53% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| DOGE-USD | HBAR-USD | 2025-06-01 | 82.45% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| SOL-USD | MKR-USD | 2020-11-23 | 89.26% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| SOL-USD | DOGE-USD | 2024-01-16 | 88.22% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 8.23% | -14.02% | 12.63% | -19.22% | -19.22% | 14.94% |
| SOL-USD | ZEC-USD | 2024-05-30 | 88.08% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| SOL-USD | LINK-USD | 2019-08-25 | 88.04% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| SOL-USD | TRX-USD | 2025-05-30 | 87.97% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 9.94% | 0.00% | 11.98% | -8.21% | -10.70% | 11.98% |
| SOL-USD | ETH-USD | 2025-05-30 | 87.69% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| SOL-USD | MKR-USD | 2023-05-17 | 87.55% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.95% | -1.75% | 30.65% | 51.74% | -1.75% | 51.74% |
| SOL-USD | SNX-USD | 2020-11-22 | 87.53% | BULL | DISTRIBUTION | SAME_BTC_ONLY | BEARISH_30D | -14.46% | -21.67% | 9.63% | -11.74% | -33.57% | 9.63% |
| SOL-USD | ADA-USD | 2025-05-30 | 87.47% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| SOL-USD | HBAR-USD | 2025-06-01 | 87.20% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |

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

