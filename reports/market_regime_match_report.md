# Market Regime Match Report

Generated: 2026-09-11 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-11 | RECOVERY | 77.059 $ | True | 19.62% | -5.12% | RECOVERY | 19.62% | -5.12% |
| DOGE-USD | 2026-09-11 | BEAR | 0.08393 $ | False | -4.48% | -12.43% | RECOVERY | 19.62% | -5.12% |
| SOL-USD | 2026-09-11 | RECOVERY | 99,61 $ | True | 44.63% | -9.52% | RECOVERY | 19.62% | -5.12% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 85.00% | 38.71% | 64.92% | 91.90% | -4.24% | -24.34% | 41.33% | 78.10% | 126.12% | 77.50% | 28.32% | 62.27% | 137.12% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 4 | 75.00% | 19.89% | 39.40% | 44.27% | -6.40% | -35.84% | 52.82% | 130.70% | 241.85% | 75.00% | 12.78% | 53.27% | 103.85% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -14.08% | 5.46% | 44.73% | -17.86% | -33.55% | 12.49% | 23.21% | 46.86% | 35.00% | -9.23% | 7.51% | 44.50% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 20 | 30.00% | -12.84% | 9.77% | 22.47% | -14.96% | -34.24% | 7.89% | 23.21% | 40.15% | 30.00% | -15.18% | 10.89% | 44.50% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 27.94% | 48.44% | 103.99% | -6.52% | -36.00% | 38.43% | 69.13% | 139.43% | 60.00% | 16.10% | 85.69% | 201.68% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 42.10% | 85.07% | 152.67% | -6.70% | -18.03% | 64.45% | 136.11% | 256.99% | 75.00% | 81.37% | 152.14% | 178.36% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 20 | 80.00% | 38.34% | -6.54% | 69.49% | 75.00% | 29.17% | 106.97% |
| BTC-USD | HISTORICAL_BTC_BULL | 20 | 90.00% | 40.49% | 0.00% | 91.90% | 80.00% | 28.26% | 149.21% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 16.00% | -17.68% | -23.92% | 20.13% | 24.00% | -13.01% | 21.01% |
| DOGE-USD | HISTORICAL_BTC_BULL | 11 | 63.64% | 4.11% | -11.17% | 43.74% | 54.55% | 3.12% | 68.37% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -7.43% | -15.36% | 23.02% | 66.67% | 4.84% | 43.18% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 58.33% | 14.09% | -9.65% | 51.41% | 54.17% | 10.35% | 75.89% |
| SOL-USD | HISTORICAL_BTC_BULL | 15 | 73.33% | 43.15% | -4.85% | 142.06% | 73.33% | 22.69% | 302.84% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -9.69% | -21.80% | 11.27% | 0.00% | -9.57% | 11.27% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 30 | 86.67% | 38.71% | -3.38% | 63.95% | 80.00% | 28.32% | 84.74% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 89.19% | -2.19% | 138.78% | 60.00% | 137.07% | 404.50% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 91.00% | -16.34% | 125.42% | 100.00% | 162.43% | 162.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 19.89% | -6.40% | 130.70% | 75.00% | 12.78% | 187.34% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 20 | 30.00% | -12.84% | -14.96% | 23.21% | 30.00% | -15.18% | 41.17% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 12 | 33.33% | -14.71% | -25.09% | 22.75% | 41.67% | -3.05% | 32.98% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -6.85% | -16.66% | 45.18% | 75.00% | 13.02% | 69.96% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -27.34% | -28.35% | 4.00% | 0.00% | -10.69% | 4.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 21.36% | -6.15% | 59.42% | 62.07% | 15.99% | 83.02% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 40.00% | -25.63% | -25.63% | 96.27% | 40.00% | -13.63% | 96.27% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 40.24% | -10.90% | 133.58% | 50.00% | 122.29% | 193.43% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 42.10% | -6.70% | 136.11% | 75.00% | 81.37% | 192.75% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 20 | 1 | 20 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | MANA-USD | 2022-10-28 | 84.05% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.58% | -26.10% | 3.31% | -21.11% | -33.73% | 3.31% |
| DOGE-USD | ETH-USD | 2025-02-19 | 83.62% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -7.43% | -15.36% | 6.87% | 43.86% | -15.36% | 47.20% |
| DOGE-USD | YFI-USD | 2022-05-10 | 82.95% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.15% | -23.92% | 0.00% | -30.34% | -32.23% | 0.00% |
| DOGE-USD | ALGO-USD | 2026-01-14 | 81.50% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 9.51% | 0.00% | 27.32% | -14.61% | -17.13% | 27.32% |
| DOGE-USD | THETA-USD | 2026-01-29 | 81.32% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -34.68% | -36.16% | 5.54% | -40.86% | -45.71% | 5.54% |
| DOGE-USD | CHZ-USD | 2024-07-08 | 80.11% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.74% | -34.03% | 0.00% | 34.22% | -34.03% | 60.89% |
| DOGE-USD | ENJ-USD | 2022-10-28 | 80.11% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.74% | -12.44% | 14.38% | -10.30% | -25.78% | 14.38% |
| DOGE-USD | KAVA-USD | 2023-08-14 | 79.99% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 19.52% | 0.00% | 25.59% | 3.12% | 0.00% | 34.81% |
| DOGE-USD | INJ-USD | 2022-05-23 | 79.94% | BEAR | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 10.57% | -4.67% | 22.42% | 50.26% | -4.67% | 50.26% |
| DOGE-USD | DOT-USD | 2023-08-14 | 79.37% | BULL | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 71.01% | 0.00% | 71.01% | 41.10% | 0.00% | 88.75% |

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

