# Market Regime Match Report

Generated: 2026-10-19 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-19 | BULL | 82.623 $ | True | 24.24% | 5.11% | BULL | 24.24% | 5.11% |
| DOGE-USD | 2026-10-19 | RECOVERY | 0.07945 $ | False | 8.42% | -2.44% | BULL | 24.24% | 5.11% |
| SOL-USD | 2026-10-19 | BULL | 105,62 $ | True | 35.22% | 7.85% | BULL | 24.24% | 5.11% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 55.00% | 1.65% | 19.48% | 32.19% | -8.45% | -23.08% | 14.32% | 25.41% | 35.60% | 47.50% | -0.92% | 23.95% | 56.98% |
| BTC-USD | SAME_BTC_REGIME | 9 | 44.44% | -1.05% | 2.85% | 53.71% | -15.93% | -29.37% | 7.79% | 11.30% | 53.71% | 22.22% | -21.24% | -1.57% | 149.88% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 33.95% | 33.95% | 33.95% | -4.32% | -4.32% | 43.75% | 43.75% | 43.75% | 100.00% | 37.38% | 37.38% | 37.38% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 77.50% | 11.17% | 21.48% | 35.01% | -5.33% | -22.65% | 15.31% | 25.08% | 46.48% | 32.50% | -7.17% | 15.20% | 58.24% |
| DOGE-USD | SAME_BTC_REGIME | 7 | 71.43% | 2.85% | 33.31% | 110.49% | -13.47% | -19.95% | 11.30% | 33.31% | 110.49% | 71.43% | 38.06% | 89.93% | 173.49% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 57.50% | 3.17% | 15.04% | 35.01% | -9.02% | -31.21% | 11.24% | 22.17% | 46.48% | 37.50% | -7.75% | 20.99% | 54.20% |
| SOL-USD | SAME_BTC_REGIME | 13 | 53.85% | 0.88% | 9.94% | 40.04% | -15.93% | -27.97% | 9.63% | 12.63% | 40.04% | 38.46% | -8.21% | 37.69% | 111.73% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 9.08% | 15.94% | 26.75% | -9.17% | -15.52% | 12.31% | 20.41% | 34.42% | 50.00% | 13.29% | 35.44% | 36.60% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 66.67% | 8.23% | 9.08% | 9.59% | -14.02% | -15.73% | 11.98% | 12.31% | 12.50% | 33.33% | -8.21% | 13.29% | 26.19% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 30 | 60.00% | 9.72% | -7.98% | 26.60% | 56.67% | 7.00% | 44.19% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -1.05% | -15.93% | 11.30% | 22.22% | -21.24% | 28.55% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -10.38% | -10.38% | 19.13% | 0.00% | -8.02% | 19.13% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 33 | 78.79% | 11.19% | -4.01% | 25.06% | 24.24% | -9.63% | 29.28% |
| DOGE-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 2.85% | -13.47% | 33.31% | 71.43% | 38.06% | 112.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 27 | 59.26% | 4.26% | -5.95% | 23.74% | 37.04% | -7.29% | 32.40% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 53.85% | 0.88% | -15.93% | 12.63% | 38.46% | -8.21% | 49.44% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 57.58% | 2.85% | -8.40% | 25.06% | 54.55% | 6.55% | 42.99% |
| BTC-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 33.95% | -4.32% | 43.75% | 100.00% | 37.38% | 64.00% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 16.44% | -12.32% | 26.10% | 0.00% | -2.47% | 40.58% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -13.16% | -13.16% | 12.74% | 0.00% | -14.02% | 12.74% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 77.78% | 11.17% | -4.36% | 25.08% | 27.78% | -8.87% | 30.46% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 13.97% | -9.93% | 35.35% | 100.00% | 37.72% | 58.33% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 11.48% | -18.06% | 18.51% | 50.00% | 26.01% | 48.73% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 58.06% | 3.49% | -8.15% | 23.74% | 38.71% | -7.29% | 37.89% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 9.08% | -9.17% | 20.41% | 50.00% | 13.29% | 45.29% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 0.88% | -21.67% | 15.86% | 33.33% | -1.57% | 42.00% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -29.39% | -36.19% | 4.27% | 0.00% | -23.14% | 4.27% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 1 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 0 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 3 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-06 | 89.85% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| BTC-USD | MKR-USD | 2020-11-28 | 86.87% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| BTC-USD | ADA-USD | 2025-06-04 | 86.42% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| BTC-USD | ONE-USD | 2023-07-30 | 85.67% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | -1.05% | -2.01% | 0.00% | -37.64% | -37.64% | 0.00% |
| BTC-USD | ETH-USD | 2025-06-04 | 85.57% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| BTC-USD | LRC-USD | 2020-11-27 | 85.45% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| BTC-USD | HBAR-USD | 2025-06-01 | 84.91% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| BTC-USD | XLM-USD | 2025-05-30 | 84.33% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 14.78% | -1.65% | 14.78% | -21.24% | -24.08% | 14.78% |
| BTC-USD | LINK-USD | 2025-06-04 | 83.44% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| DOGE-USD | LINK-USD | 2019-08-30 | 86.12% | BULL | BULL | SAME_BTC_ONLY | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |
| DOGE-USD | ZEC-USD | 2024-06-04 | 84.25% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| DOGE-USD | RUNE-USD | 2023-07-06 | 83.66% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| DOGE-USD | MKR-USD | 2020-11-28 | 83.61% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| DOGE-USD | LRC-USD | 2020-11-27 | 83.14% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| DOGE-USD | MKR-USD | 2023-05-22 | 82.01% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 44.53% | -0.31% | 44.53% | 37.69% | -0.31% | 49.44% |
| DOGE-USD | HBAR-USD | 2025-06-01 | 81.72% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| SOL-USD | MKR-USD | 2020-11-28 | 89.99% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| SOL-USD | LINK-USD | 2019-08-25 | 88.65% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| SOL-USD | LRC-USD | 2020-11-27 | 88.57% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| SOL-USD | ETH-USD | 2025-06-04 | 88.49% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| SOL-USD | RUNE-USD | 2023-07-06 | 88.41% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| SOL-USD | DOGE-USD | 2024-01-16 | 88.29% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 8.23% | -14.02% | 12.63% | -19.22% | -19.22% | 14.94% |
| SOL-USD | HBAR-USD | 2025-06-01 | 88.19% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| SOL-USD | LINK-USD | 2025-06-04 | 88.11% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| SOL-USD | ADA-USD | 2025-06-04 | 87.37% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| SOL-USD | TRX-USD | 2025-05-30 | 87.37% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 9.94% | 0.00% | 11.98% | -8.21% | -10.70% | 11.98% |

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

