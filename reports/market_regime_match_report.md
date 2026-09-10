# Market Regime Match Report

Generated: 2026-09-10 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-10 | RECOVERY | 78.457 $ | True | 23.47% | -5.34% | RECOVERY | 23.47% | -5.34% |
| DOGE-USD | 2026-09-10 | BEAR | 0.08593 $ | False | -0.04% | -12.60% | RECOVERY | 23.47% | -5.34% |
| SOL-USD | 2026-09-10 | RECOVERY | 102,02 $ | True | 52.84% | -9.83% | RECOVERY | 23.47% | -5.34% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 87.50% | 37.26% | 56.23% | 89.37% | -2.93% | -36.52% | 41.33% | 72.24% | 111.40% | 77.50% | 23.52% | 58.30% | 132.80% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 4 | 75.00% | 19.89% | 38.18% | 40.84% | -12.97% | -39.78% | 40.90% | 112.82% | 234.70% | 75.00% | 12.78% | 41.24% | 70.16% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -11.41% | 5.46% | 46.86% | -16.34% | -33.55% | 10.18% | 26.05% | 46.86% | 35.00% | -9.23% | 10.11% | 43.96% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 18 | 33.33% | -7.46% | 7.27% | 28.36% | -14.26% | -32.20% | 8.43% | 23.40% | 42.11% | 33.33% | -12.83% | 5.75% | 41.93% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 28.93% | 55.25% | 103.99% | -9.65% | -37.41% | 38.43% | 69.99% | 148.24% | 60.00% | 16.10% | 86.08% | 201.68% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 39.66% | 81.40% | 151.20% | -13.26% | -39.78% | 180.53% | 321.36% | 331.09% | 75.00% | 57.31% | 116.05% | 163.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 88.89% | 37.15% | -6.11% | 66.93% | 77.78% | 29.29% | 102.35% |
| BTC-USD | HISTORICAL_BTC_BULL | 22 | 86.36% | 37.26% | 0.00% | 80.31% | 77.27% | 23.52% | 84.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 20 | 15.00% | -13.39% | -21.14% | 16.97% | 20.00% | -12.49% | 18.21% |
| DOGE-USD | HISTORICAL_BTC_BULL | 15 | 60.00% | 4.11% | -14.27% | 43.74% | 60.00% | 8.47% | 79.20% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 25.00% | -15.43% | -23.46% | 29.01% | 25.00% | -12.36% | 41.17% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 58.33% | 14.09% | -14.32% | 46.64% | 54.17% | 10.35% | 74.95% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 78.57% | 69.13% | -3.58% | 167.10% | 78.57% | 93.80% | 314.75% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -17.13% | -29.26% | 8.45% | 0.00% | -12.35% | 8.45% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 30 | 93.33% | 38.01% | -1.76% | 63.95% | 83.33% | 23.52% | 81.66% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.49% | -7.66% | 89.19% | 40.00% | -4.71% | 179.49% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 91.00% | -16.34% | 125.42% | 100.00% | 162.43% | 162.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 19.89% | -12.97% | 112.82% | 75.00% | 12.78% | 156.26% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 18 | 33.33% | -7.46% | -14.26% | 23.40% | 33.33% | -12.83% | 38.08% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 17 | 35.29% | -17.32% | -26.32% | 27.97% | 41.18% | -2.67% | 48.00% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 10.11% | -1.42% | 40.85% | 100.00% | 21.20% | 40.85% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -22.68% | -24.67% | 4.00% | 0.00% | -11.03% | 4.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 21.36% | -6.59% | 57.10% | 62.07% | 15.99% | 79.60% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -16.13% | -19.11% | 82.75% | 33.33% | -13.63% | 215.61% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 40.24% | -19.07% | 137.65% | 50.00% | 76.43% | 185.36% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 39.66% | -13.26% | 321.36% | 75.00% | 57.31% | 321.36% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 18 | 1 | 18 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | YFI-USD | 2022-05-10 | 82.77% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.15% | -23.92% | 0.00% | -30.34% | -32.23% | 0.00% |
| DOGE-USD | FIL-USD | 2022-05-10 | 82.74% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.78% | -31.42% | 0.00% | -36.98% | -38.04% | 0.00% |
| DOGE-USD | ETH-USD | 2025-02-19 | 82.74% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -7.43% | -15.36% | 6.87% | 43.86% | -15.36% | 47.20% |
| DOGE-USD | MANA-USD | 2022-10-23 | 82.32% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -12.23% | -16.35% | 7.70% | -21.40% | -30.92% | 7.70% |
| DOGE-USD | MATIC-USD | 2022-04-26 | 80.98% | RECOVERY | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.77% | -13.97% | 15.45% | -13.91% | -20.67% | 15.45% |
| DOGE-USD | NEAR-USD | 2022-10-23 | 80.43% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 0.56% | -5.20% | 16.82% | -13.69% | -22.51% | 16.82% |
| DOGE-USD | CHZ-USD | 2024-07-08 | 80.43% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.74% | -34.03% | 0.00% | 34.22% | -34.03% | 60.89% |
| DOGE-USD | THETA-USD | 2026-01-29 | 80.25% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -34.68% | -36.16% | 5.54% | -40.86% | -45.71% | 5.54% |
| DOGE-USD | KAVA-USD | 2023-08-14 | 80.20% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 19.52% | 0.00% | 25.59% | 3.12% | 0.00% | 34.81% |
| DOGE-USD | ALGO-USD | 2026-01-14 | 80.09% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 9.51% | 0.00% | 27.32% | -14.61% | -17.13% | 27.32% |

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

