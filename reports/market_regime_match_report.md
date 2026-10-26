# Market Regime Match Report

Generated: 2026-10-26 06:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-26 | BULL | 79.856 $ | True | 25.03% | 5.37% | BULL | 25.03% | 5.37% |
| DOGE-USD | 2026-10-26 | RECOVERY | 0.07658 $ | False | 8.24% | -2.56% | BULL | 25.03% | 5.37% |
| SOL-USD | 2026-10-26 | BULL | 100,60 $ | True | 36.50% | 8.44% | BULL | 25.03% | 5.37% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 47.50% | -0.31% | 12.70% | 32.68% | -10.54% | -24.45% | 12.43% | 19.01% | 38.96% | 52.50% | 1.80% | 32.68% | 93.57% |
| BTC-USD | SAME_BTC_REGIME | 10 | 40.00% | -7.28% | 4.92% | 46.07% | -18.04% | -28.39% | 5.42% | 15.17% | 46.43% | 30.00% | -27.58% | 85.25% | 161.27% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 100.00% | 16.96% | 21.49% | 24.21% | -12.75% | -14.25% | 17.36% | 22.88% | 26.20% | 100.00% | 116.42% | 133.93% | 144.43% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 11.71% | 14.34% | 15.91% | -13.69% | -14.44% | 16.73% | 17.04% | 17.23% | 100.00% | 133.93% | 142.68% | 147.93% |
| DOGE-USD | ALL_MATCHES | 40 | 47.50% | -0.26% | 13.35% | 45.30% | -8.76% | -22.20% | 13.40% | 28.44% | 54.40% | 35.00% | -12.35% | 15.05% | 62.68% |
| DOGE-USD | SAME_BTC_REGIME | 4 | 50.00% | 3.36% | 82.82% | 217.95% | -18.60% | -38.00% | 10.06% | 86.29% | 219.34% | 50.00% | 26.36% | 108.20% | 193.18% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -46.00% | -46.00% | -46.00% | -46.00% | -46.00% | 1.05% | 1.05% | 1.05% | 0.00% | -38.82% | -38.82% | -38.82% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -46.00% | -46.00% | -46.00% | -46.00% | -46.00% | 1.05% | 1.05% | 1.05% | 0.00% | -38.82% | -38.82% | -38.82% |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | 0.30% | 15.01% | 26.34% | -10.63% | -21.78% | 15.04% | 20.81% | 30.23% | 40.00% | -9.13% | 27.59% | 79.38% |
| SOL-USD | SAME_BTC_REGIME | 12 | 33.33% | -3.59% | 9.09% | 25.34% | -15.08% | -26.28% | 9.39% | 16.41% | 34.08% | 41.67% | -11.15% | 57.65% | 147.93% |
| SOL-USD | SAME_ASSET_REGIME | 6 | 50.00% | 2.65% | 14.34% | 21.49% | -12.28% | -15.08% | 13.13% | 17.04% | 22.88% | 66.67% | 29.77% | 96.83% | 133.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 40.00% | -1.17% | 6.46% | 12.76% | -12.75% | -15.17% | 10.16% | 16.10% | 16.86% | 60.00% | 38.06% | 116.42% | 137.43% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 27 | 48.15% | -0.11% | -8.29% | 19.63% | 59.26% | 8.14% | 47.95% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 40.00% | -7.28% | -18.04% | 15.17% | 30.00% | -27.58% | 95.82% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 29.69% | -6.08% | 63.93% | 100.00% | 27.41% | 86.54% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -11.36% | -19.06% | 2.22% | 0.00% | -7.74% | 2.22% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 34 | 47.06% | -0.26% | -8.11% | 26.97% | 32.35% | -13.12% | 34.82% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 50.00% | 3.36% | -18.60% | 86.29% | 50.00% | 26.36% | 135.74% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -14.97% | -21.38% | 0.00% | 0.00% | -5.83% | 0.00% |
| SOL-USD | HISTORICAL_BTC_BEAR | 27 | 55.56% | 2.87% | -7.98% | 20.82% | 37.04% | -9.99% | 35.95% |
| SOL-USD | HISTORICAL_BTC_BULL | 12 | 33.33% | -3.59% | -15.08% | 16.41% | 41.67% | -11.15% | 60.10% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 28 | 53.57% | 1.58% | -8.08% | 22.77% | 57.14% | 8.25% | 55.15% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 100.00% | 16.96% | -12.75% | 22.88% | 100.00% | 116.42% | 148.74% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 12.50% | -14.57% | -20.05% | 5.10% | 25.00% | -16.61% | 7.52% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 47.22% | -0.26% | -8.26% | 28.79% | 33.33% | -12.83% | 38.78% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 16.88% | -11.18% | 23.24% | 100.00% | 41.24% | 56.60% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -46.00% | -46.00% | 1.05% | 0.00% | -38.82% | 1.05% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 56.67% | 2.88% | -8.14% | 24.30% | 40.00% | -7.03% | 38.68% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 50.00% | 2.65% | -12.28% | 17.04% | 66.67% | 29.77% | 97.65% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -4.77% | -20.78% | 10.85% | 0.00% | -15.00% | 27.11% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -19.72% | -21.73% | 4.68% | 0.00% | -34.79% | 4.68% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group     |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:--------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 3 | 10 | 10 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | NONE | 1 | 1 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 6 | 12 | 5 | 5 | 0_FULL_REGIME | FULL_REGIME_THRESHOLD_MET |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-11 | 90.61% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 308.03% | -3.16% | 308.03% | 249.83% | -3.16% | 350.68% |
| BTC-USD | ADA-USD | 2025-06-09 | 88.76% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -26.77% | -28.22% | 5.07% | -42.84% | -43.41% | 5.07% |
| BTC-USD | LRC-USD | 2020-12-02 | 88.75% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.03% | -19.36% | 12.38% | -8.26% | -21.94% | 34.03% |
| BTC-USD | ETH-USD | 2025-06-09 | 87.51% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -13.52% | -16.72% | 4.09% | -29.69% | -31.08% | 4.09% |
| BTC-USD | MKR-USD | 2020-12-03 | 86.79% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| BTC-USD | LINK-USD | 2025-06-09 | 86.21% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -25.92% | -26.73% | 4.88% | -39.90% | -41.26% | 4.88% |
| BTC-USD | ONE-USD | 2023-08-04 | 86.11% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 0.29% | -0.68% | 1.26% | -43.98% | -45.15% | 1.26% |
| BTC-USD | ALGO-USD | 2025-06-08 | 83.71% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.62% | -24.43% | 5.77% | -30.93% | -33.70% | 5.77% |
| BTC-USD | ETC-USD | 2025-06-09 | 83.38% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -23.03% | -29.97% | 2.28% | -25.48% | -30.26% | 2.28% |
| BTC-USD | ETH-USD | 2020-12-02 | 83.28% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.96% | -12.75% | 17.36% | 116.42% | -12.75% | 116.42% |
| SOL-USD | MKR-USD | 2020-12-03 | 90.25% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| SOL-USD | TRX-USD | 2025-06-09 | 88.01% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -7.85% | -8.13% | 2.35% | -14.03% | -17.89% | 2.35% |
| SOL-USD | DOGE-USD | 2024-01-26 | 87.36% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -1.17% | -11.82% | 8.62% | -26.03% | -26.03% | 8.62% |
| SOL-USD | ETH-USD | 2020-12-02 | 86.47% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.96% | -12.75% | 17.36% | 116.42% | -12.75% | 116.42% |
| SOL-USD | LINK-USD | 2019-08-30 | 86.23% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |

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

