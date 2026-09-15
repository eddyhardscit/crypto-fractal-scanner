# Market Regime Match Report

Generated: 2026-09-15 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-15 | RECOVERY | 77.439 $ | True | 20.21% | -4.22% | RECOVERY | 20.21% | -4.22% |
| DOGE-USD | 2026-09-15 | BEAR | 0.08285 $ | False | -3.43% | -11.80% | RECOVERY | 20.21% | -4.22% |
| SOL-USD | 2026-09-15 | RECOVERY | 100,90 $ | True | 40.27% | -8.17% | RECOVERY | 20.21% | -4.22% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 87.50% | 24.46% | 57.03% | 70.73% | -4.10% | -33.88% | 37.23% | 65.45% | 99.54% | 75.00% | 15.70% | 52.59% | 138.30% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 92.44% | 114.91% | 128.39% | -3.47% | -6.24% | 107.58% | 126.89% | 138.48% | 100.00% | 145.10% | 148.86% | 151.12% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -8.40% | 2.97% | 62.13% | -19.04% | -33.08% | 10.92% | 23.28% | 63.98% | 50.00% | -0.32% | 15.25% | 32.40% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 23 | 21.74% | -16.58% | -3.88% | 13.25% | -18.57% | -32.57% | 9.23% | 16.43% | 31.07% | 26.09% | -13.26% | -0.32% | 19.84% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 25.55% | 61.27% | 81.48% | -3.35% | -33.87% | 37.23% | 69.45% | 125.06% | 65.00% | 18.98% | 105.28% | 199.13% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -1.22% | 23.15% | 37.77% | -6.93% | -41.33% | 22.31% | 45.63% | 59.62% | 33.33% | -13.67% | 61.95% | 107.32% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 27 | 92.59% | 24.26% | -3.88% | 56.29% | 70.37% | 10.93% | 76.83% |
| BTC-USD | HISTORICAL_BTC_BULL | 13 | 76.92% | 43.15% | -6.83% | 98.68% | 84.62% | 18.76% | 152.63% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 21.43% | -16.52% | -20.06% | 19.43% | 32.14% | -10.57% | 19.43% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 8.90% | -13.54% | 64.10% | 100.00% | 33.07% | 187.52% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 50.00% | 1.03% | -20.57% | 13.24% | 75.00% | 10.99% | 56.54% |
| SOL-USD | HISTORICAL_BTC_BEAR | 28 | 71.43% | 24.72% | -3.13% | 62.02% | 60.71% | 12.32% | 80.33% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 80.00% | 65.65% | -2.90% | 163.28% | 90.00% | 181.73% | 319.74% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -18.29% | -27.18% | 9.56% | 0.00% | -18.67% | 9.56% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 90.62% | 24.19% | -3.81% | 59.56% | 71.88% | 9.59% | 73.67% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 0.90% | -18.61% | 98.68% | 80.00% | 18.76% | 171.02% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 48.87% | -33.92% | 78.05% | 100.00% | 170.45% | 192.55% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 92.44% | -3.47% | 126.89% | 100.00% | 145.10% | 150.59% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 23 | 21.74% | -16.58% | -18.57% | 16.43% | 26.09% | -13.26% | 22.79% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 13 | 46.15% | -0.68% | -22.44% | 25.28% | 84.62% | 11.74% | 64.01% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 2.94% | -16.70% | 39.04% | 100.00% | 12.27% | 39.04% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -18.34% | -19.39% | 3.18% | 0.00% | -21.46% | 3.18% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 72.41% | 24.79% | -3.23% | 64.03% | 62.07% | 16.39% | 81.97% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 39.35% | -9.40% | 106.53% | 100.00% | 79.53% | 225.31% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 69.52% | -10.43% | 187.88% | 75.00% | 212.30% | 272.65% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -1.22% | -6.93% | 45.63% | 33.33% | -13.67% | 83.39% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 23 | 0 | 23 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | ETH-USD | 2025-02-24 | 84.51% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -0.09% | -14.08% | 8.49% | 30.83% | -14.08% | 49.43% |
| DOGE-USD | ALGO-USD | 2026-01-19 | 83.36% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.05% | -4.94% | 19.19% | -23.29% | -25.87% | 19.19% |
| DOGE-USD | MANA-USD | 2022-10-28 | 82.52% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.58% | -26.10% | 3.31% | -21.11% | -33.73% | 3.31% |
| DOGE-USD | NEO-USD | 2019-08-15 | 81.35% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -8.05% | -18.57% | 4.55% | 15.70% | -18.57% | 22.70% |
| DOGE-USD | NEAR-USD | 2022-10-28 | 81.24% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -17.77% | -18.69% | 7.88% | -18.91% | -28.44% | 7.88% |
| DOGE-USD | MKR-USD | 2018-07-22 | 81.00% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -39.79% | -49.29% | 10.63% | -23.59% | -49.54% | 10.63% |
| DOGE-USD | YFI-USD | 2022-05-15 | 80.95% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.14% | -10.14% | 17.05% | -14.71% | -16.21% | 17.05% |
| DOGE-USD | MATIC-USD | 2022-05-01 | 80.84% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -8.76% | -17.13% | 11.21% | -9.73% | -23.58% | 11.21% |
| DOGE-USD | AAVE-USD | 2022-10-31 | 80.54% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.69% | -22.69% | 3.44% | -14.07% | -24.14% | 3.44% |
| DOGE-USD | CHZ-USD | 2024-07-13 | 80.23% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 2.16% | -27.07% | 6.78% | 15.87% | -27.07% | 77.87% |

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

