# Market Regime Match Report

Generated: 2026-10-23 05:33 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-23 | BULL | 81.511 $ | True | 26.74% | 5.37% | BULL | 26.74% | 5.37% |
| DOGE-USD | 2026-10-23 | RECOVERY | 0.07959 $ | False | 11.04% | -2.47% | BULL | 26.74% | 5.37% |
| SOL-USD | 2026-10-23 | BULL | 104,09 $ | True | 39.85% | 8.40% | BULL | 26.74% | 5.37% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 6.94% | 24.93% | 31.17% | -9.42% | -25.62% | 12.37% | 25.34% | 35.67% | 50.00% | 0.26% | 32.37% | 92.51% |
| BTC-USD | SAME_BTC_REGIME | 10 | 50.00% | -7.82% | 2.36% | 55.52% | -18.87% | -30.07% | 4.84% | 10.42% | 55.52% | 30.00% | -22.05% | 46.48% | 138.07% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 32.38% | 35.40% | 37.21% | -9.95% | -10.02% | 33.77% | 36.09% | 37.49% | 100.00% | 39.13% | 50.81% | 57.82% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 38.42% | 38.42% | 38.42% | -9.85% | -9.85% | 38.42% | 38.42% | 38.42% | 100.00% | 62.50% | 62.50% | 62.50% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 8.49% | 25.97% | 44.47% | -7.37% | -37.77% | 15.50% | 26.32% | 77.17% | 37.50% | -8.91% | 29.02% | 57.46% |
| DOGE-USD | SAME_BTC_REGIME | 4 | 50.00% | 8.04% | 93.57% | 222.25% | -14.50% | -28.41% | 16.12% | 93.57% | 222.25% | 75.00% | 45.82% | 102.65% | 190.96% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 27.51% | 27.51% | 27.51% | -0.34% | -0.34% | 30.16% | 30.16% | 30.16% | 100.00% | 35.24% | 35.24% | 35.24% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 3.52% | 16.08% | 39.78% | -10.50% | -34.27% | 13.08% | 21.45% | 45.07% | 37.50% | -9.81% | 24.22% | 57.46% |
| SOL-USD | SAME_BTC_REGIME | 14 | 50.00% | -0.95% | 20.08% | 42.95% | -15.73% | -29.54% | 8.97% | 21.87% | 48.34% | 35.71% | -14.45% | 37.97% | 104.46% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -6.00% | 4.04% | 10.06% | -9.31% | -14.28% | 10.16% | 15.70% | 19.02% | 33.33% | -14.43% | 11.81% | 27.56% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 33.33% | -6.00% | 4.04% | 10.06% | -9.31% | -14.28% | 10.16% | 15.70% | 19.02% | 33.33% | -14.43% | 11.81% | 27.56% |

## Breakdown by historical BTC regime

| target   | group               |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:--------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 30 | 73.33% | 9.60% | -7.28% | 25.42% | 56.67% | 7.91% | 35.28% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 50.00% | -7.82% | -18.87% | 10.42% | 30.00% | -22.05% | 54.01% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 36 | 69.44% | 8.49% | -6.75% | 26.32% | 33.33% | -10.96% | 30.54% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 50.00% | 8.04% | -14.50% | 93.57% | 75.00% | 45.82% | 129.26% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 73.08% | 6.68% | -7.33% | 20.25% | 38.46% | -9.07% | 27.17% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 50.00% | -0.95% | -15.73% | 21.87% | 35.71% | -14.45% | 49.84% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 34 | 67.65% | 6.94% | -8.51% | 23.72% | 50.00% | -0.37% | 35.28% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 32.38% | -9.95% | 36.09% | 100.00% | 39.13% | 54.16% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 0.88% | -22.65% | 7.79% | 0.00% | -1.57% | 28.55% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -15.93% | -15.93% | 20.39% | 33.33% | -2.38% | 26.24% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 37 | 67.57% | 8.36% | -7.13% | 25.46% | 32.43% | -11.93% | 29.28% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -6.00% | -15.53% | 10.16% | 100.00% | 38.06% | 41.33% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 22.09% | -13.47% | 22.09% | 100.00% | 53.59% | 55.45% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 27.51% | -0.34% | 30.16% | 100.00% | 35.24% | 41.88% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 67.74% | 3.67% | -10.27% | 19.70% | 38.71% | -9.63% | 28.42% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -6.00% | -9.31% | 15.70% | 33.33% | -14.43% | 31.28% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 11.48% | -18.06% | 29.06% | 25.00% | -9.30% | 51.34% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 5.79% | -8.14% | 24.05% | 50.00% | 7.62% | 32.83% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 10 | 10 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | NONE | 0 | 1 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_BTC_REGIME | 3 | 3 | 14 | 14 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-06 | 87.55% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| BTC-USD | LRC-USD | 2020-11-27 | 86.37% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| BTC-USD | ADA-USD | 2025-06-04 | 86.12% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| BTC-USD | HBAR-USD | 2025-06-06 | 85.65% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -21.68% | -33.92% | 0.00% | -29.91% | -34.48% | 0.00% |
| BTC-USD | ETH-USD | 2025-06-04 | 85.40% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| BTC-USD | XLM-USD | 2025-06-04 | 85.39% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -18.36% | -19.58% | 3.25% | -24.08% | -31.94% | 3.25% |
| BTC-USD | MKR-USD | 2020-11-28 | 85.24% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| BTC-USD | LINK-USD | 2025-06-04 | 83.98% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| BTC-USD | XLM-USD | 2020-12-02 | 83.73% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.42% | -9.85% | 38.42% | 62.50% | -9.85% | 62.50% |
| BTC-USD | ONE-USD | 2023-08-04 | 83.57% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 0.29% | -0.68% | 1.26% | -43.98% | -45.15% | 1.26% |
| SOL-USD | ZEC-USD | 2024-06-04 | 89.15% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| SOL-USD | MKR-USD | 2020-11-28 | 89.03% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| SOL-USD | MKR-USD | 2023-05-22 | 88.98% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 44.53% | -0.31% | 44.53% | 37.69% | -0.31% | 49.44% |
| SOL-USD | DOGE-USD | 2024-01-21 | 88.68% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |
| SOL-USD | TRX-USD | 2025-06-04 | 88.56% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -9.18% | -9.18% | 1.79% | -14.47% | -18.83% | 1.79% |
| SOL-USD | ETH-USD | 2025-06-04 | 87.90% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| SOL-USD | LINK-USD | 2019-08-30 | 87.78% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |
| SOL-USD | LRC-USD | 2020-11-27 | 87.50% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| SOL-USD | SNX-USD | 2020-11-27 | 87.47% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -2.78% | -24.03% | 6.30% | -17.04% | -35.57% | 6.30% |
| SOL-USD | ADA-USD | 2025-06-04 | 87.16% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |

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

