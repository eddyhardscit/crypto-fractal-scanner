# Market Regime Match Report

Generated: 2026-10-25 06:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-25 | BULL | 80.521 $ | True | 26.36% | 5.38% | BULL | 26.36% | 5.38% |
| DOGE-USD | 2026-10-25 | RECOVERY | 0.07697 $ | False | 9.43% | -2.52% | BULL | 26.36% | 5.38% |
| SOL-USD | 2026-10-25 | BULL | 101,76 $ | True | 37.25% | 8.48% | BULL | 26.36% | 5.38% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 2.88% | 23.52% | 35.98% | -7.95% | -24.81% | 14.30% | 26.08% | 60.88% | 47.50% | -2.82% | 27.07% | 93.14% |
| BTC-USD | SAME_BTC_REGIME | 9 | 33.33% | -13.52% | 0.29% | 66.78% | -19.36% | -29.36% | 5.07% | 12.38% | 74.49% | 22.22% | -29.91% | -8.26% | 171.11% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 16.24% | 21.13% | 24.06% | -9.57% | -13.62% | 22.25% | 25.33% | 27.18% | 100.00% | 86.46% | 118.94% | 138.43% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 6.46% | 6.46% | 6.46% | -14.63% | -14.63% | 16.10% | 16.10% | 16.10% | 100.00% | 151.43% | 151.43% | 151.43% |
| DOGE-USD | ALL_MATCHES | 40 | 50.00% | 1.43% | 23.52% | 45.30% | -9.03% | -21.41% | 13.40% | 26.22% | 50.88% | 35.00% | -9.13% | 26.16% | 62.68% |
| DOGE-USD | SAME_BTC_REGIME | 4 | 50.00% | 3.36% | 82.82% | 217.95% | -18.60% | -38.00% | 10.06% | 86.29% | 219.34% | 50.00% | 26.36% | 108.20% | 193.18% |
| DOGE-USD | SAME_ASSET_REGIME | 3 | 33.33% | -7.64% | 9.94% | 20.48% | -19.66% | -40.73% | 1.05% | 15.61% | 24.34% | 33.33% | -4.06% | 15.59% | 27.38% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -46.00% | -46.00% | -46.00% | -46.00% | -46.00% | 1.05% | 1.05% | 1.05% | 0.00% | -38.82% | -38.82% | -38.82% |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | 0.30% | 11.98% | 27.01% | -10.80% | -28.79% | 13.07% | 19.27% | 30.74% | 40.00% | -10.96% | 27.59% | 93.14% |
| SOL-USD | SAME_BTC_REGIME | 13 | 38.46% | -2.78% | 14.08% | 24.41% | -15.53% | -27.92% | 10.16% | 17.36% | 33.00% | 38.46% | -14.43% | 38.06% | 144.43% |
| SOL-USD | SAME_ASSET_REGIME | 5 | 60.00% | 6.46% | 14.08% | 15.81% | -12.75% | -15.17% | 16.10% | 17.36% | 19.68% | 60.00% | 38.06% | 116.42% | 137.43% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 60.00% | 6.46% | 14.08% | 15.81% | -12.75% | -15.17% | 16.10% | 17.36% | 19.68% | 60.00% | 38.06% | 116.42% | 137.43% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 29 | 68.97% | 6.46% | -5.05% | 25.31% | 51.72% | 8.14% | 47.84% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 33.33% | -13.52% | -19.36% | 12.38% | 22.22% | -29.91% | 34.03% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 29.69% | -6.08% | 63.93% | 100.00% | 27.41% | 86.54% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 34 | 50.00% | 1.43% | -8.26% | 24.76% | 32.35% | -12.35% | 33.09% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 50.00% | 3.36% | -18.60% | 86.29% | 50.00% | 26.36% | 135.74% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |
| DOGE-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -7.64% | -19.66% | 0.00% | 0.00% | -4.06% | 1.58% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 53.85% | 1.16% | -8.14% | 18.72% | 38.46% | -10.96% | 34.49% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 38.46% | -2.78% | -15.53% | 17.36% | 38.46% | -14.43% | 41.33% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 68.75% | 4.68% | -5.79% | 26.11% | 50.00% | 3.10% | 50.48% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 16.24% | -9.57% | 25.33% | 100.00% | 86.46% | 144.32% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 20.00% | -15.62% | -21.04% | 5.77% | 20.00% | -29.69% | 5.77% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 35 | 51.43% | 2.87% | -8.29% | 26.99% | 34.29% | -11.93% | 36.75% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 7.75% | -17.83% | 7.75% | 100.00% | 60.99% | 64.10% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -7.64% | -19.66% | 15.61% | 33.33% | -4.06% | 21.73% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 53.33% | 1.16% | -9.28% | 20.29% | 40.00% | -10.96% | 38.08% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 6.46% | -12.75% | 17.36% | 60.00% | 38.06% | 116.42% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -1.90% | -21.69% | 10.86% | 0.00% | -12.65% | 27.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -13.52% | -16.72% | 17.52% | 33.33% | -29.69% | 23.38% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group     |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:--------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | NONE | 1 | 3 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 5 | 13 | 5 | 5 | 0_FULL_REGIME | FULL_REGIME_THRESHOLD_MET |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-11 | 90.64% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 308.03% | -3.16% | 308.03% | 249.83% | -3.16% | 350.68% |
| BTC-USD | ADA-USD | 2025-06-09 | 88.38% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -26.77% | -28.22% | 5.07% | -42.84% | -43.41% | 5.07% |
| BTC-USD | LRC-USD | 2020-12-02 | 88.19% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.03% | -19.36% | 12.38% | -8.26% | -21.94% | 34.03% |
| BTC-USD | ETH-USD | 2025-06-09 | 86.93% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -13.52% | -16.72% | 4.09% | -29.69% | -31.08% | 4.09% |
| BTC-USD | ONE-USD | 2023-08-04 | 86.86% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 0.29% | -0.68% | 1.26% | -43.98% | -45.15% | 1.26% |
| BTC-USD | MKR-USD | 2020-12-03 | 86.86% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| BTC-USD | LINK-USD | 2025-06-09 | 85.39% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -25.92% | -26.73% | 4.88% | -39.90% | -41.26% | 4.88% |
| BTC-USD | HBAR-USD | 2025-06-06 | 84.55% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -21.68% | -33.92% | 0.00% | -29.91% | -34.48% | 0.00% |
| BTC-USD | ALGO-USD | 2025-06-08 | 83.41% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.62% | -24.43% | 5.77% | -30.93% | -33.70% | 5.77% |
| SOL-USD | MKR-USD | 2020-12-03 | 90.16% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| SOL-USD | LINK-USD | 2019-08-30 | 87.87% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |
| SOL-USD | DOGE-USD | 2024-01-21 | 87.20% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |
| SOL-USD | TRX-USD | 2025-06-04 | 86.92% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -9.18% | -9.18% | 1.79% | -14.47% | -18.83% | 1.79% |
| SOL-USD | ETH-USD | 2020-12-02 | 85.96% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.96% | -12.75% | 17.36% | 116.42% | -12.75% | 116.42% |

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

