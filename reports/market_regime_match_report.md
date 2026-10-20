# Market Regime Match Report

Generated: 2026-10-20 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-20 | BULL | 81.881 $ | True | 23.87% | 5.21% | BULL | 23.87% | 5.21% |
| DOGE-USD | 2026-10-20 | RECOVERY | 0.07939 $ | False | 8.82% | -2.41% | BULL | 23.87% | 5.21% |
| SOL-USD | 2026-10-20 | BULL | 104,61 $ | True | 34.28% | 8.07% | BULL | 23.87% | 5.21% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 55.00% | 1.65% | 21.37% | 34.16% | -7.98% | -23.08% | 14.75% | 24.78% | 35.38% | 47.50% | -0.92% | 22.96% | 66.00% |
| BTC-USD | SAME_BTC_REGIME | 9 | 44.44% | -1.05% | 2.85% | 63.80% | -15.93% | -29.37% | 7.79% | 11.30% | 65.51% | 33.33% | -20.01% | 112.89% | 149.88% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 27.38% | 27.38% | 27.38% | -3.71% | -3.71% | 29.52% | 29.52% | 29.52% | 100.00% | 112.89% | 112.89% | 112.89% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 27.38% | 27.38% | 27.38% | -3.71% | -3.71% | 29.52% | 29.52% | 29.52% | 100.00% | 112.89% | 112.89% | 112.89% |
| DOGE-USD | ALL_MATCHES | 40 | 80.00% | 11.17% | 21.08% | 30.71% | -6.00% | -26.65% | 17.06% | 23.10% | 46.48% | 35.00% | -7.17% | 13.10% | 58.24% |
| DOGE-USD | SAME_BTC_REGIME | 7 | 71.43% | 2.85% | 33.31% | 110.49% | -15.53% | -25.31% | 11.30% | 33.31% | 110.49% | 71.43% | 38.06% | 89.93% | 173.49% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 27.51% | 27.51% | 27.51% | -0.34% | -0.34% | 30.16% | 30.16% | 30.16% | 100.00% | 35.24% | 35.24% | 35.24% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 4.51% | 19.38% | 33.25% | -8.34% | -29.34% | 11.77% | 22.17% | 46.48% | 35.00% | -7.17% | 18.53% | 58.24% |
| SOL-USD | SAME_BTC_REGIME | 13 | 53.85% | 0.88% | 9.94% | 40.04% | -15.93% | -28.25% | 9.54% | 12.63% | 40.04% | 38.46% | -8.21% | 37.69% | 111.73% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 66.67% | 8.23% | 9.08% | 9.59% | -14.02% | -15.73% | 11.98% | 12.31% | 12.50% | 33.33% | -8.21% | 13.29% | 26.19% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 66.67% | 8.23% | 9.08% | 9.59% | -14.02% | -15.73% | 11.98% | 12.31% | 12.50% | 33.33% | -8.21% | 13.29% | 26.19% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 29 | 62.07% | 11.15% | -5.95% | 26.65% | 55.17% | 3.50% | 41.88% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -1.05% | -15.93% | 11.30% | 33.33% | -20.01% | 112.89% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -14.59% | -14.59% | 14.83% | 0.00% | -14.60% | 14.83% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 32 | 84.38% | 11.22% | -4.18% | 23.10% | 28.12% | -8.73% | 27.13% |
| DOGE-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 2.85% | -15.53% | 33.31% | 71.43% | 38.06% | 112.45% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -26.36% | -26.36% | 4.66% | 0.00% | -30.78% | 4.66% |
| SOL-USD | HISTORICAL_BTC_BEAR | 27 | 70.37% | 7.41% | -4.34% | 23.78% | 33.33% | -7.06% | 31.10% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 53.85% | 0.88% | -15.93% | 12.63% | 38.46% | -8.21% | 49.44% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 58.62% | 2.85% | -7.82% | 23.70% | 55.17% | 3.50% | 33.33% |
| BTC-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 27.38% | -3.71% | 29.52% | 100.00% | 112.89% | 112.89% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 16.44% | -12.32% | 26.10% | 0.00% | -2.47% | 40.58% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 25.00% | -13.16% | -13.16% | 21.89% | 25.00% | -6.34% | 24.82% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 80.56% | 11.17% | -5.30% | 23.10% | 30.56% | -8.73% | 27.89% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -6.00% | -15.53% | 10.16% | 100.00% | 38.06% | 41.33% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 11.48% | -18.06% | 18.51% | 50.00% | 26.01% | 48.73% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 27.51% | -0.34% | 30.16% | 100.00% | 35.24% | 41.88% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 64.52% | 3.49% | -8.15% | 22.06% | 35.48% | -7.29% | 31.10% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 8.23% | -14.02% | 12.31% | 33.33% | -8.21% | 26.99% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 11.48% | -18.06% | 24.61% | 25.00% | -2.47% | 47.30% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 5.79% | -8.14% | 24.05% | 50.00% | 7.62% | 32.83% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 1 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 3 | 3 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-06 | 90.78% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| BTC-USD | LRC-USD | 2020-11-27 | 88.49% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| BTC-USD | MKR-USD | 2020-11-28 | 87.85% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| BTC-USD | ADA-USD | 2025-06-04 | 87.48% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| BTC-USD | ETH-USD | 2025-06-04 | 86.39% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| BTC-USD | ONE-USD | 2023-07-30 | 86.11% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | -1.05% | -2.01% | 0.00% | -37.64% | -37.64% | 0.00% |
| BTC-USD | HBAR-USD | 2025-06-01 | 84.30% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| BTC-USD | LINK-USD | 2025-06-04 | 84.22% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| BTC-USD | ETH-USD | 2020-11-27 | 83.60% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.38% | -3.71% | 29.52% | 112.89% | -3.71% | 112.89% |
| DOGE-USD | LINK-USD | 2019-08-30 | 88.33% | BULL | BULL | SAME_BTC_ONLY | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |
| DOGE-USD | ZEC-USD | 2024-06-04 | 86.32% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| DOGE-USD | LRC-USD | 2020-11-27 | 85.84% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| DOGE-USD | RUNE-USD | 2023-07-06 | 82.85% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| DOGE-USD | MKR-USD | 2020-11-28 | 82.74% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| DOGE-USD | MKR-USD | 2023-05-22 | 81.77% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 44.53% | -0.31% | 44.53% | 37.69% | -0.31% | 49.44% |
| DOGE-USD | ADA-USD | 2025-06-04 | 81.65% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| SOL-USD | MKR-USD | 2020-11-28 | 91.05% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| SOL-USD | LRC-USD | 2020-11-27 | 90.00% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| SOL-USD | ZEC-USD | 2024-06-04 | 89.30% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| SOL-USD | ETH-USD | 2025-06-04 | 89.20% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| SOL-USD | LINK-USD | 2025-06-04 | 88.87% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| SOL-USD | RUNE-USD | 2023-07-06 | 88.79% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| SOL-USD | ADA-USD | 2025-06-04 | 88.48% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| SOL-USD | LINK-USD | 2019-08-25 | 88.29% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| SOL-USD | MKR-USD | 2023-05-22 | 87.98% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 44.53% | -0.31% | 44.53% | 37.69% | -0.31% | 49.44% |
| SOL-USD | HBAR-USD | 2025-06-01 | 87.75% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |

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

