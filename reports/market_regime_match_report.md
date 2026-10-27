# Market Regime Match Report

Generated: 2026-10-27 06:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-27 | BULL | 79.617 $ | True | 24.58% | 5.37% | BULL | 24.58% | 5.37% |
| DOGE-USD | 2026-10-27 | RECOVERY | 0.07724 $ | False | 10.23% | -2.59% | BULL | 24.58% | 5.37% |
| SOL-USD | 2026-10-27 | BULL | 99,68 $ | True | 35.44% | 8.43% | BULL | 24.58% | 5.37% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 45.00% | -1.10% | 15.01% | 34.04% | -10.70% | -24.81% | 12.45% | 20.07% | 36.26% | 52.50% | 1.80% | 33.17% | 93.78% |
| BTC-USD | SAME_BTC_REGIME | 9 | 22.22% | -13.52% | -1.03% | 66.78% | -18.80% | -29.38% | 6.39% | 12.38% | 74.49% | 22.22% | -29.69% | -8.26% | 171.11% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 66.67% | 6.46% | 16.24% | 22.11% | -11.82% | -14.07% | 16.10% | 22.25% | 25.95% | 66.67% | 21.48% | 86.46% | 125.44% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 2.65% | 4.55% | 5.70% | -13.22% | -14.35% | 12.36% | 14.23% | 15.35% | 50.00% | 62.70% | 107.07% | 133.68% |
| DOGE-USD | ALL_MATCHES | 40 | 40.00% | -1.19% | 9.93% | 45.30% | -8.11% | -25.15% | 14.47% | 25.70% | 49.90% | 32.50% | -13.44% | 14.46% | 43.18% |
| DOGE-USD | SAME_BTC_REGIME | 3 | 33.33% | -1.03% | 3.36% | 5.99% | -19.36% | -40.67% | 7.75% | 10.06% | 11.45% | 33.33% | -8.26% | 26.36% | 47.14% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -46.00% | -46.00% | -46.00% | -46.00% | -46.00% | 1.05% | 1.05% | 1.05% | 0.00% | -38.82% | -38.82% | -38.82% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -46.00% | -46.00% | -46.00% | -46.00% | -46.00% | 1.05% | 1.05% | 1.05% | 0.00% | -38.82% | -38.82% | -38.82% |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -0.77% | 15.01% | 28.77% | -9.28% | -21.78% | 15.04% | 25.81% | 38.25% | 42.50% | -10.96% | 30.39% | 79.38% |
| SOL-USD | SAME_BTC_REGIME | 11 | 36.36% | -1.17% | 7.10% | 26.27% | -16.72% | -26.73% | 7.75% | 14.24% | 35.94% | 36.36% | -14.03% | 38.48% | 151.43% |
| SOL-USD | SAME_ASSET_REGIME | 5 | 60.00% | 6.46% | 7.75% | 18.71% | -11.82% | -16.55% | 8.62% | 16.10% | 23.48% | 60.00% | 21.48% | 60.99% | 115.25% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 4 | 50.00% | 2.65% | 6.78% | 7.36% | -13.22% | -16.87% | 8.18% | 10.49% | 13.85% | 50.00% | 23.48% | 83.60% | 124.30% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 29 | 51.72% | 2.87% | -8.24% | 20.85% | 62.07% | 8.36% | 54.12% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 22.22% | -13.52% | -18.80% | 12.38% | 22.22% | -29.69% | 34.03% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | -6.58% | -27.74% | 21.39% | 50.00% | -6.98% | 43.68% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 34 | 41.18% | -0.93% | -7.03% | 26.24% | 32.35% | -14.33% | 36.64% |
| DOGE-USD | HISTORICAL_BTC_BULL | 3 | 33.33% | -1.03% | -19.36% | 10.06% | 33.33% | -8.26% | 49.06% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | -0.97% | -21.53% | 21.39% | 50.00% | 3.68% | 43.68% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -14.97% | -21.38% | 0.00% | 0.00% | -5.83% | 0.00% |
| SOL-USD | HISTORICAL_BTC_BEAR | 28 | 46.43% | -0.26% | -7.37% | 25.81% | 42.86% | -10.96% | 38.78% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 36.36% | -1.17% | -16.72% | 14.24% | 36.36% | -14.03% | 51.42% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 50.00% | 1.18% | -8.76% | 21.31% | 56.25% | 8.25% | 59.77% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 6.46% | -11.82% | 22.25% | 66.67% | 21.48% | 107.59% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -16.16% | -17.76% | 5.25% | 25.00% | -31.07% | 7.99% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 38.89% | -1.72% | -7.79% | 25.70% | 30.56% | -14.33% | 38.78% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 16.88% | -11.18% | 23.24% | 100.00% | 41.24% | 56.60% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -46.00% | -46.00% | 1.05% | 0.00% | -38.82% | 1.05% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 48.39% | -0.01% | -7.61% | 27.74% | 45.16% | -9.99% | 45.52% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 6.46% | -11.82% | 16.10% | 60.00% | 21.48% | 64.10% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -4.77% | -20.78% | 10.85% | 0.00% | -15.00% | 27.11% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -19.72% | -21.73% | 4.68% | 0.00% | -34.79% | 4.68% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 3 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | NONE | 1 | 1 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_ASSET_REGIME | 4 | 5 | 11 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-11 | 89.37% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 308.03% | -3.16% | 308.03% | 249.83% | -3.16% | 350.68% |
| BTC-USD | LRC-USD | 2020-12-02 | 87.55% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.03% | -19.36% | 12.38% | -8.26% | -21.94% | 34.03% |
| BTC-USD | ADA-USD | 2025-06-09 | 87.50% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -26.77% | -28.22% | 5.07% | -42.84% | -43.41% | 5.07% |
| BTC-USD | ETH-USD | 2025-06-09 | 86.49% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -13.52% | -16.72% | 4.09% | -29.69% | -31.08% | 4.09% |
| BTC-USD | MKR-USD | 2020-12-03 | 85.80% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| BTC-USD | LINK-USD | 2025-06-09 | 85.33% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -25.92% | -26.73% | 4.88% | -39.90% | -41.26% | 4.88% |
| BTC-USD | XLM-USD | 2025-06-09 | 83.95% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -18.80% | -18.80% | 6.39% | -32.45% | -32.47% | 6.39% |
| BTC-USD | DOGE-USD | 2024-01-26 | 83.83% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -1.17% | -11.82% | 8.62% | -26.03% | -26.03% | 8.62% |
| BTC-USD | HBAR-USD | 2025-06-11 | 82.98% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -32.68% | -34.03% | 0.00% | -40.91% | -40.91% | 0.00% |
| SOL-USD | MKR-USD | 2020-12-03 | 89.73% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| SOL-USD | DOGE-USD | 2024-01-26 | 88.69% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -1.17% | -11.82% | 8.62% | -26.03% | -26.03% | 8.62% |
| SOL-USD | TRX-USD | 2025-06-09 | 88.68% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -7.85% | -8.13% | 2.35% | -14.03% | -17.89% | 2.35% |
| SOL-USD | ETH-USD | 2021-06-30 | 86.65% | BEAR | BULL | SAME_ASSET_ONLY | BULLISH_30D | 26.02% | -4.52% | 28.41% | 21.48% | -4.52% | 34.12% |
| SOL-USD | LINK-USD | 2019-09-04 | 85.59% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 7.75% | -17.83% | 7.75% | 60.99% | -17.83% | 64.10% |

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

