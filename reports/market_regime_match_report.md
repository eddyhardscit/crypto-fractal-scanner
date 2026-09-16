# Market Regime Match Report

Generated: 2026-09-16 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-16 | RECOVERY | 75.812 $ | True | 20.53% | -3.99% | RECOVERY | 20.53% | -3.99% |
| DOGE-USD | 2026-09-16 | BEAR | 0.08018 $ | False | -3.89% | -11.63% | RECOVERY | 20.53% | -3.99% |
| SOL-USD | 2026-09-16 | RECOVERY | 97,07 $ | True | 39.42% | -7.83% | RECOVERY | 20.53% | -3.99% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 90.00% | 25.55% | 57.00% | 68.64% | -3.31% | -32.86% | 40.94% | 67.60% | 86.62% | 77.50% | 21.60% | 74.11% | 138.30% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 47.51% | 47.51% | 47.51% | -6.93% | -6.93% | 68.95% | 68.95% | 68.95% | 100.00% | 137.57% | 137.57% | 137.57% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -10.25% | 2.91% | 20.41% | -21.22% | -33.34% | 11.67% | 21.16% | 44.99% | 55.00% | 1.14% | 15.74% | 32.40% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 25 | 24.00% | -17.24% | -0.09% | 14.56% | -20.27% | -35.59% | 10.63% | 19.20% | 29.02% | 36.00% | -8.74% | 1.32% | 26.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 24.41% | 64.16% | 97.68% | -4.30% | -33.54% | 33.91% | 78.48% | 125.06% | 67.50% | 19.01% | 84.69% | 173.55% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -1.22% | 3.73% | 6.70% | -16.37% | -43.21% | 22.31% | 27.04% | 29.88% | 33.33% | -13.67% | 23.29% | 45.47% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 28 | 92.86% | 25.55% | -3.10% | 58.45% | 71.43% | 18.28% | 80.33% |
| BTC-USD | HISTORICAL_BTC_BULL | 12 | 83.33% | 34.14% | -9.24% | 88.63% | 91.67% | 84.48% | 158.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 27.59% | -11.61% | -20.94% | 21.04% | 44.83% | -1.60% | 27.08% |
| DOGE-USD | HISTORICAL_BTC_BULL | 7 | 42.86% | -1.97% | -18.57% | 33.69% | 100.00% | 15.70% | 53.45% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 25.00% | -5.51% | -24.36% | 7.21% | 50.00% | 7.44% | 56.54% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 65.38% | 18.80% | -3.73% | 59.54% | 65.38% | 12.56% | 78.99% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 81.82% | 60.36% | -0.41% | 118.08% | 90.91% | 166.43% | 282.86% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 0.00% | -21.84% | -23.58% | 7.08% | 0.00% | -23.20% | 7.08% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 93.55% | 24.65% | -3.03% | 55.41% | 74.19% | 20.17% | 80.87% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 23.83% | -14.53% | 95.33% | 83.33% | 37.13% | 149.59% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 48.87% | -33.92% | 78.05% | 100.00% | 170.45% | 192.55% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 81.54% | 0.00% | 131.38% | 100.00% | 137.49% | 137.49% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 47.51% | -6.93% | 68.95% | 100.00% | 137.57% | 144.47% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 25 | 24.00% | -17.24% | -20.27% | 19.20% | 36.00% | -8.74% | 33.12% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 11 | 36.36% | -3.20% | -24.51% | 23.00% | 90.91% | 12.27% | 55.09% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 2.94% | -16.70% | 39.04% | 100.00% | 12.27% | 39.04% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -18.34% | -19.39% | 3.18% | 0.00% | -21.46% | 3.18% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 62.96% | 24.03% | -4.11% | 62.60% | 62.96% | 8.73% | 78.20% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 53.56% | -2.45% | 122.22% | 100.00% | 69.18% | 195.23% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 58.15% | -10.43% | 135.43% | 75.00% | 185.93% | 260.23% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -1.22% | -16.37% | 27.04% | 33.33% | -13.67% | 77.79% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 25 | 0 | 25 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | ALGO-USD | 2026-01-19 | 85.43% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.05% | -4.94% | 19.19% | -23.29% | -25.87% | 19.19% |
| DOGE-USD | MANA-USD | 2022-11-02 | 85.39% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.04% | -23.69% | 9.52% | -9.67% | -23.69% | 9.52% |
| DOGE-USD | ETH-USD | 2025-02-24 | 85.12% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -0.09% | -14.08% | 8.49% | 30.83% | -14.08% | 49.43% |
| DOGE-USD | NEO-USD | 2019-08-15 | 83.91% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -8.05% | -18.57% | 4.55% | 15.70% | -18.57% | 22.70% |
| DOGE-USD | ENJ-USD | 2022-11-02 | 81.29% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -20.27% | -20.27% | 22.87% | -1.58% | -20.27% | 22.87% |
| DOGE-USD | SOL-USD | 2022-10-31 | 81.26% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -27.46% | -27.46% | 9.72% | -16.03% | -27.46% | 9.72% |
| DOGE-USD | NEAR-USD | 2022-11-02 | 81.14% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -20.02% | -20.94% | 19.20% | -8.74% | -20.94% | 19.20% |
| DOGE-USD | YFI-USD | 2022-05-15 | 81.03% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.14% | -10.14% | 17.05% | -14.71% | -16.21% | 17.05% |
| DOGE-USD | AAVE-USD | 2022-10-31 | 80.96% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.69% | -22.69% | 3.44% | -14.07% | -24.14% | 3.44% |
| DOGE-USD | MKR-USD | 2018-07-22 | 80.82% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -39.79% | -49.29% | 10.63% | -23.59% | -49.54% | 10.63% |

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

