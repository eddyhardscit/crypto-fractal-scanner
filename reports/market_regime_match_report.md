# Market Regime Match Report

Generated: 2026-09-01 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-01 | RECOVERY | 78.947 $ | True | 23.33% | -7.37% | RECOVERY | 23.33% | -7.37% |
| DOGE-USD | 2026-09-01 | BEAR | 0.08338 $ | False | -8.73% | -14.08% | RECOVERY | 23.33% | -7.37% |
| SOL-USD | 2026-09-01 | RECOVERY | 103,93 $ | True | 45.13% | -12.65% | RECOVERY | 23.33% | -7.37% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 3.92% | 20.28% | 40.68% | -12.62% | -33.25% | 14.78% | 25.56% | 54.79% | 70.00% | 13.16% | 41.02% | 114.89% |
| BTC-USD | SAME_BTC_REGIME | 5 | 80.00% | 29.98% | 38.24% | 57.27% | -3.49% | -27.01% | 41.86% | 73.81% | 91.04% | 80.00% | 50.29% | 81.97% | 101.07% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 100.00% | 4.44% | 17.21% | 24.87% | -12.76% | -16.21% | 20.58% | 61.55% | 86.13% | 100.00% | 34.79% | 42.54% | 47.19% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 17.21% | 23.59% | 27.42% | -10.28% | -15.71% | 61.55% | 82.04% | 94.33% | 100.00% | 42.54% | 46.41% | 48.74% |
| DOGE-USD | ALL_MATCHES | 40 | 35.00% | -4.84% | 21.03% | 48.12% | -11.66% | -36.20% | 20.00% | 43.03% | 73.50% | 42.50% | -4.18% | 25.71% | 70.54% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -20.03% | -20.03% | -20.03% | -23.75% | -23.75% | 9.37% | 9.37% | 9.37% | 0.00% | -29.37% | -29.37% | -29.37% |
| DOGE-USD | SAME_ASSET_REGIME | 9 | 22.22% | -5.61% | -0.19% | 24.72% | -11.95% | -36.26% | 16.29% | 18.77% | 35.48% | 44.44% | -14.57% | 40.32% | 56.99% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 5.27% | 41.41% | 100.24% | -13.20% | -35.03% | 26.55% | 58.75% | 113.79% | 65.00% | 22.84% | 86.93% | 133.42% |
| SOL-USD | SAME_BTC_REGIME | 4 | 75.00% | 37.08% | 56.68% | 88.12% | -16.91% | -29.74% | 40.97% | 66.66% | 102.06% | 75.00% | 95.96% | 125.96% | 135.57% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 100.00% | 19.06% | 27.01% | 31.77% | -17.71% | -20.06% | 22.97% | 28.96% | 32.55% | 100.00% | 39.88% | 55.58% | 65.01% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 34.95% | 34.95% | 34.95% | -20.65% | -20.65% | 34.95% | 34.95% | 34.95% | 100.00% | 71.29% | 71.29% | 71.29% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 4 | 0.00% | -20.80% | -26.15% | 11.03% | 50.00% | -6.70% | 24.93% |
| BTC-USD | HISTORICAL_BTC_BULL | 30 | 73.33% | 3.92% | -12.62% | 24.94% | 70.00% | 11.04% | 61.87% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 18.48% | -2.96% | 24.83% | 100.00% | 151.30% | 193.70% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 80.00% | 29.98% | -3.49% | 73.81% | 80.00% | 50.29% | 112.35% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 6 | 16.67% | -8.49% | -13.57% | 18.18% | 33.33% | -21.36% | 27.75% |
| DOGE-USD | HISTORICAL_BTC_BULL | 31 | 41.94% | -2.82% | -7.75% | 46.37% | 48.39% | -3.77% | 64.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -25.91% | -33.22% | 8.86% | 0.00% | -12.46% | 8.86% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -20.03% | -23.75% | 9.37% | 0.00% | -29.37% | 9.37% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 57.14% | 1.89% | -13.13% | 72.82% | 50.00% | 1.38% | 76.66% |
| SOL-USD | HISTORICAL_BTC_BULL | 21 | 76.19% | 8.57% | -12.63% | 51.65% | 76.19% | 29.02% | 112.47% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -26.14% | -26.76% | 21.34% | 0.00% | -32.16% | 21.34% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 37.08% | -16.91% | 66.66% | 75.00% | 95.96% | 132.64% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 28 | 75.00% | 4.35% | -12.11% | 29.73% | 67.86% | 10.80% | 52.31% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 33.33% | -5.45% | -12.59% | 18.65% | 66.67% | 38.36% | 128.84% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.48% | -2.96% | 24.83% | 100.00% | 151.30% | 193.70% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -20.22% | -25.68% | 4.94% | 50.00% | 5.98% | 33.05% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 100.00% | 4.44% | -12.76% | 61.55% | 100.00% | 34.79% | 76.54% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 9 | 22.22% | -5.61% | -11.95% | 18.77% | 44.44% | -14.57% | 40.32% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 27 | 37.04% | -4.07% | -8.92% | 43.41% | 40.74% | -3.99% | 48.19% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 86.14% | 0.00% | 115.24% | 100.00% | 62.20% | 131.12% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -14.05% | -19.59% | 8.58% | 0.00% | -17.36% | 12.86% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 26 | 65.38% | 3.31% | -13.09% | 46.67% | 57.69% | 5.80% | 68.48% |
| SOL-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 51.83% | -14.99% | 126.09% | 75.00% | 65.21% | 149.38% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 105.25% | -12.68% | 119.61% | 100.00% | 130.65% | 217.10% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 14.90% | -17.32% | 68.80% | 50.00% | 54.36% | 99.79% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 19.06% | -17.71% | 28.96% | 100.00% | 39.88% | 61.69% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 3 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 9 | 1 | 9 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 1 | 2 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | BNB-USD | 2018-11-08 | 85.39% | RECOVERY | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 69.95% | -1.56% | 73.81% | 113.80% | -1.56% | 113.80% |
| BTC-USD | THETA-USD | 2018-11-12 | 82.82% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.98% | -3.49% | 102.52% | 34.79% | -3.49% | 102.52% |
| BTC-USD | LTC-USD | 2018-11-09 | 82.10% | RECOVERY | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 38.24% | 0.00% | 41.86% | 81.97% | 0.00% | 112.35% |
| BTC-USD | MKR-USD | 2020-03-03 | 81.38% | RECOVERY | MIXED | SAME_BTC_ONLY | BEARISH_30D | -32.40% | -33.64% | 0.00% | -10.55% | -33.73% | 0.00% |
| BTC-USD | LRC-USD | 2020-03-02 | 79.57% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 4.44% | -17.07% | 20.58% | 50.29% | -17.07% | 50.55% |
| DOGE-USD | YFI-USD | 2022-04-30 | 86.50% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -24.38% | -25.90% | 0.85% | -28.14% | -30.98% | 0.85% |
| DOGE-USD | FIL-USD | 2022-04-30 | 84.51% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.15% | -36.15% | 0.00% | -37.52% | -40.20% | 0.00% |
| DOGE-USD | EGLD-USD | 2023-07-25 | 84.13% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 40.51% | 0.00% | 48.58% | 110.79% | 0.00% | 126.47% |
| DOGE-USD | ETH-USD | 2025-02-09 | 83.16% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -0.19% | -4.46% | 11.24% | 40.32% | -11.90% | 40.32% |
| DOGE-USD | THETA-USD | 2026-01-19 | 82.68% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -11.37% | -11.37% | 18.77% | -37.22% | -37.22% | 18.77% |
| DOGE-USD | MATIC-USD | 2022-04-16 | 82.57% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -5.61% | -12.38% | 16.29% | -14.57% | -20.09% | 16.29% |
| DOGE-USD | DOT-USD | 2023-08-04 | 82.48% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 20.77% | -11.95% | 32.21% | 43.54% | -11.95% | 66.19% |
| DOGE-USD | INJ-USD | 2022-05-13 | 82.02% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -1.50% | -9.36% | 16.40% | 23.27% | -9.36% | 30.74% |
| DOGE-USD | KSM-USD | 2021-12-25 | 80.71% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.71% | -36.71% | 0.00% | -63.53% | -67.03% | 0.00% |

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

