# Market Regime Match Report

Generated: 2026-10-24 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-24 | BULL | 80.661 $ | True | 23.45% | 5.39% | BULL | 23.45% | 5.39% |
| DOGE-USD | 2026-10-24 | RECOVERY | 0.07829 $ | False | 6.81% | -2.48% | BULL | 23.45% | 5.39% |
| SOL-USD | 2026-10-24 | BULL | 102,17 $ | True | 33.38% | 8.47% | BULL | 23.45% | 5.39% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 3.35% | 22.42% | 31.17% | -9.95% | -24.81% | 14.30% | 25.34% | 35.67% | 47.50% | -2.38% | 31.78% | 92.51% |
| BTC-USD | SAME_BTC_REGIME | 10 | 40.00% | -7.28% | 4.92% | 65.38% | -18.04% | -28.79% | 4.97% | 15.17% | 65.38% | 30.00% | -26.88% | 44.81% | 161.27% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 100.00% | 26.34% | 32.38% | 36.00% | -10.04% | -13.71% | 29.13% | 33.77% | 36.56% | 100.00% | 62.50% | 106.96% | 133.64% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 22.44% | 30.43% | 35.22% | -12.24% | -14.15% | 27.26% | 32.84% | 36.18% | 100.00% | 106.96% | 129.20% | 142.54% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 7.32% | 22.39% | 39.98% | -8.14% | -19.73% | 15.94% | 26.22% | 63.57% | 40.00% | -6.50% | 31.93% | 79.38% |
| DOGE-USD | SAME_BTC_REGIME | 4 | 75.00% | 7.10% | 82.82% | 217.95% | -16.23% | -18.90% | 14.24% | 89.08% | 220.45% | 75.00% | 106.21% | 176.03% | 220.31% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 27.51% | 27.51% | 27.51% | -0.34% | -0.34% | 30.16% | 30.16% | 30.16% | 100.00% | 35.24% | 35.24% | 35.24% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 57.50% | 2.50% | 10.76% | 29.21% | -10.50% | -34.25% | 13.78% | 20.81% | 31.60% | 45.00% | -5.55% | 27.59% | 86.61% |
| SOL-USD | SAME_BTC_REGIME | 11 | 36.36% | -2.78% | 10.27% | 44.53% | -15.53% | -26.73% | 10.16% | 18.67% | 44.53% | 36.36% | -14.43% | 37.87% | 151.43% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 50.00% | 0.23% | 8.37% | 11.79% | -11.97% | -15.26% | 13.13% | 17.38% | 19.69% | 50.00% | 11.81% | 66.40% | 117.42% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 4 | 50.00% | 0.23% | 8.37% | 11.79% | -11.97% | -15.26% | 13.13% | 17.38% | 19.69% | 50.00% | 11.81% | 66.40% | 117.42% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 30 | 70.00% | 6.94% | -8.64% | 25.42% | 53.33% | 8.25% | 42.46% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 40.00% | -7.28% | -18.04% | 15.17% | 30.00% | -26.88% | 55.38% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 35 | 65.71% | 6.89% | -7.61% | 23.15% | 34.29% | -9.99% | 32.07% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 75.00% | 7.10% | -16.23% | 89.08% | 75.00% | 106.21% | 223.46% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |
| SOL-USD | HISTORICAL_BTC_BEAR | 28 | 64.29% | 2.88% | -7.95% | 19.15% | 46.43% | -1.95% | 31.27% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 36.36% | -2.78% | -15.53% | 18.67% | 36.36% | -14.43% | 45.39% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 63.64% | 2.90% | -8.99% | 20.85% | 45.45% | -2.83% | 42.66% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 100.00% | 26.34% | -10.04% | 33.77% | 100.00% | 62.50% | 121.78% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -13.52% | -16.72% | 17.52% | 33.33% | -29.69% | 23.38% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 66.67% | 7.62% | -7.79% | 26.22% | 36.11% | -8.54% | 35.97% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 7.10% | -16.23% | 14.01% | 100.00% | 106.21% | 151.82% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 27.51% | -0.34% | 30.16% | 100.00% | 35.24% | 41.88% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 64.52% | 2.90% | -8.29% | 20.82% | 48.39% | -1.08% | 37.67% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 0.23% | -11.97% | 17.38% | 50.00% | 11.81% | 76.26% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -1.90% | -21.69% | 10.86% | 0.00% | -12.65% | 27.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -13.52% | -16.72% | 17.52% | 33.33% | -29.69% | 23.38% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 3 | 10 | 10 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | NONE | 0 | 1 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_BTC_REGIME | 4 | 4 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-11 | 89.73% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 308.03% | -3.16% | 308.03% | 249.83% | -3.16% | 350.68% |
| BTC-USD | ADA-USD | 2025-06-09 | 87.14% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -26.77% | -28.22% | 5.07% | -42.84% | -43.41% | 5.07% |
| BTC-USD | ONE-USD | 2023-08-04 | 86.28% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 0.29% | -0.68% | 1.26% | -43.98% | -45.15% | 1.26% |
| BTC-USD | MKR-USD | 2020-12-03 | 86.18% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| BTC-USD | ETH-USD | 2025-06-09 | 85.91% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -13.52% | -16.72% | 4.09% | -29.69% | -31.08% | 4.09% |
| BTC-USD | HBAR-USD | 2025-06-06 | 85.60% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -21.68% | -33.92% | 0.00% | -29.91% | -34.48% | 0.00% |
| BTC-USD | LRC-USD | 2020-12-02 | 85.42% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.03% | -19.36% | 12.38% | -8.26% | -21.94% | 34.03% |
| BTC-USD | LINK-USD | 2025-06-09 | 84.48% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -25.92% | -26.73% | 4.88% | -39.90% | -41.26% | 4.88% |
| BTC-USD | XLM-USD | 2025-06-04 | 84.08% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -18.36% | -19.58% | 3.25% | -24.08% | -31.94% | 3.25% |
| BTC-USD | XLM-USD | 2020-12-02 | 83.74% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.42% | -9.85% | 38.42% | 62.50% | -9.85% | 62.50% |
| SOL-USD | MKR-USD | 2020-12-03 | 89.22% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| SOL-USD | DOGE-USD | 2024-01-21 | 88.92% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |
| SOL-USD | RUNE-USD | 2023-07-11 | 88.79% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 308.03% | -3.16% | 308.03% | 249.83% | -3.16% | 350.68% |
| SOL-USD | LRC-USD | 2020-12-02 | 88.35% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.03% | -19.36% | 12.38% | -8.26% | -21.94% | 34.03% |
| SOL-USD | LINK-USD | 2019-08-30 | 88.30% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |
| SOL-USD | TRX-USD | 2025-06-04 | 87.68% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -9.18% | -9.18% | 1.79% | -14.47% | -18.83% | 1.79% |
| SOL-USD | HBAR-USD | 2025-06-06 | 87.45% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -21.68% | -33.92% | 0.00% | -29.91% | -34.48% | 0.00% |
| SOL-USD | LINK-USD | 2025-06-09 | 87.28% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -25.92% | -26.73% | 4.88% | -39.90% | -41.26% | 4.88% |
| SOL-USD | MKR-USD | 2023-05-22 | 87.27% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 44.53% | -0.31% | 44.53% | 37.69% | -0.31% | 49.44% |
| SOL-USD | ETH-USD | 2025-06-09 | 87.22% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -13.52% | -16.72% | 4.09% | -29.69% | -31.08% | 4.09% |

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

