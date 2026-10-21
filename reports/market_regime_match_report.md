# Market Regime Match Report

Generated: 2026-10-21 05:33 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-21 | BULL | 82.812 $ | True | 27.32% | 5.32% | BULL | 27.32% | 5.32% |
| DOGE-USD | 2026-10-21 | RECOVERY | 0.08169 $ | False | 18.16% | -2.39% | BULL | 27.32% | 5.32% |
| SOL-USD | 2026-10-21 | BULL | 105,97 $ | True | 39.69% | 8.26% | BULL | 27.32% | 5.32% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 2.03% | 22.17% | 35.20% | -9.18% | -25.34% | 11.81% | 22.86% | 35.38% | 45.00% | -1.97% | 27.42% | 101.39% |
| BTC-USD | SAME_BTC_REGIME | 11 | 54.55% | 0.88% | 18.08% | 27.38% | -15.93% | -29.30% | 7.79% | 21.66% | 29.52% | 36.36% | -14.43% | 83.24% | 126.27% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 20.73% | 24.06% | 26.05% | -6.51% | -8.75% | 25.38% | 27.45% | 28.69% | 50.00% | 49.23% | 81.06% | 100.16% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 20.73% | 24.06% | 26.05% | -6.51% | -8.75% | 25.38% | 27.45% | 28.69% | 50.00% | 49.23% | 81.06% | 100.16% |
| DOGE-USD | ALL_MATCHES | 40 | 82.50% | 10.87% | 21.36% | 25.66% | -6.00% | -23.39% | 15.31% | 23.02% | 31.08% | 30.00% | -7.56% | 7.69% | 39.61% |
| DOGE-USD | SAME_BTC_REGIME | 5 | 60.00% | 0.88% | 2.85% | 14.39% | -18.16% | -26.64% | 10.16% | 11.30% | 17.77% | 60.00% | 38.06% | 53.59% | 97.19% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 27.51% | 27.51% | 27.51% | -0.34% | -0.34% | 30.16% | 30.16% | 30.16% | 100.00% | 35.24% | 35.24% | 35.24% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 6.48% | 19.44% | 29.21% | -8.34% | -34.58% | 13.14% | 23.10% | 46.48% | 37.50% | -8.17% | 23.36% | 101.39% |
| SOL-USD | SAME_BTC_REGIME | 14 | 50.00% | -0.95% | 20.08% | 39.38% | -14.70% | -27.72% | 8.96% | 21.87% | 40.03% | 42.86% | -8.00% | 49.61% | 122.25% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 50.00% | 2.45% | 17.41% | 23.39% | -9.24% | -14.11% | 14.81% | 23.30% | 27.03% | 50.00% | 10.18% | 54.31% | 89.46% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 4 | 50.00% | 2.45% | 17.41% | 23.39% | -9.24% | -14.11% | 14.81% | 23.30% | 27.03% | 50.00% | 10.18% | 54.31% | 89.46% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 27 | 62.96% | 10.54% | -5.95% | 24.73% | 51.85% | 2.08% | 37.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 11 | 54.55% | 0.88% | -15.93% | 21.66% | 36.36% | -14.43% | 84.17% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -14.59% | -14.59% | 14.83% | 0.00% | -14.60% | 14.83% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 34 | 88.24% | 11.22% | -4.18% | 25.05% | 26.47% | -8.05% | 27.90% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 0.88% | -18.16% | 11.30% | 60.00% | 38.06% | 55.45% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -26.36% | -26.36% | 4.66% | 0.00% | -30.78% | 4.66% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 80.77% | 9.58% | -4.50% | 24.46% | 34.62% | -8.17% | 27.33% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 50.00% | -0.95% | -14.70% | 21.87% | 42.86% | -8.00% | 53.95% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 27 | 59.26% | 2.34% | -8.40% | 22.01% | 51.85% | 2.08% | 33.45% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 20.73% | -6.51% | 27.45% | 50.00% | 49.23% | 89.98% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 22.09% | -13.47% | 27.14% | 33.33% | -1.57% | 50.02% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 25.00% | -13.16% | -13.16% | 21.89% | 25.00% | -6.34% | 24.82% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 83.33% | 10.87% | -5.30% | 23.02% | 25.00% | -8.95% | 27.58% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -6.00% | -15.53% | 10.16% | 100.00% | 38.06% | 41.33% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 11.48% | -18.06% | 18.51% | 50.00% | 26.01% | 48.73% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 27.51% | -0.34% | 30.16% | 100.00% | 35.24% | 41.88% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 74.19% | 7.41% | -5.95% | 23.78% | 35.48% | -8.51% | 28.42% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 2.45% | -9.24% | 23.30% | 50.00% | 10.18% | 57.51% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 0.88% | -22.65% | 14.94% | 33.33% | -1.57% | 42.00% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 5.79% | -8.14% | 24.05% | 50.00% | 7.62% | 32.83% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 4 | 4 | 14 | 14 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-06 | 90.62% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| BTC-USD | LRC-USD | 2020-11-27 | 89.01% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| BTC-USD | ADA-USD | 2025-06-04 | 88.51% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| BTC-USD | MKR-USD | 2020-11-28 | 87.75% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| BTC-USD | ETH-USD | 2025-06-04 | 87.64% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| BTC-USD | ONE-USD | 2023-07-30 | 85.51% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | -1.05% | -2.01% | 0.00% | -37.64% | -37.64% | 0.00% |
| BTC-USD | LINK-USD | 2025-06-04 | 85.47% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| BTC-USD | ZEC-USD | 2024-06-04 | 84.40% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| BTC-USD | DOGE-USD | 2024-01-21 | 84.07% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |
| BTC-USD | ETH-USD | 2020-11-27 | 83.99% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.38% | -3.71% | 29.52% | 112.89% | -3.71% | 112.89% |
| DOGE-USD | LINK-USD | 2019-08-30 | 88.40% | BULL | BULL | SAME_BTC_ONLY | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |
| DOGE-USD | ZEC-USD | 2024-06-04 | 87.22% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| DOGE-USD | LRC-USD | 2020-11-27 | 86.06% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| DOGE-USD | ADA-USD | 2025-06-04 | 82.04% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| DOGE-USD | MKR-USD | 2020-11-28 | 81.73% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| SOL-USD | MKR-USD | 2020-11-28 | 91.11% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| SOL-USD | ZEC-USD | 2024-06-04 | 90.53% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| SOL-USD | ETH-USD | 2025-06-04 | 90.26% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| SOL-USD | LRC-USD | 2020-11-27 | 89.99% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| SOL-USD | LINK-USD | 2025-06-04 | 89.62% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| SOL-USD | ADA-USD | 2025-06-04 | 89.47% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| SOL-USD | MKR-USD | 2023-05-22 | 88.52% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 44.53% | -0.31% | 44.53% | 37.69% | -0.31% | 49.44% |
| SOL-USD | RUNE-USD | 2023-07-06 | 88.38% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| SOL-USD | TRX-USD | 2025-06-04 | 87.79% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -9.18% | -9.18% | 1.79% | -14.47% | -18.83% | 1.79% |
| SOL-USD | DOGE-USD | 2024-01-21 | 87.68% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |

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

