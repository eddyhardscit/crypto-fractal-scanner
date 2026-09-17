# Market Regime Match Report

Generated: 2026-09-17 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-17 | RECOVERY | 76.403 $ | True | 20.24% | -3.78% | RECOVERY | 20.24% | -3.78% |
| DOGE-USD | 2026-09-17 | BEAR | 0.08094 $ | False | -3.10% | -11.50% | RECOVERY | 20.24% | -3.78% |
| SOL-USD | 2026-09-17 | RECOVERY | 99,61 $ | True | 42.87% | -7.50% | RECOVERY | 20.24% | -3.78% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 87.50% | 24.46% | 52.09% | 68.28% | -2.42% | -24.85% | 35.12% | 61.89% | 84.47% | 72.50% | 19.80% | 71.02% | 121.69% |
| BTC-USD | SAME_BTC_REGIME | 1 | 0.00% | -2.79% | -2.79% | -2.79% | -11.42% | -11.42% | 3.01% | 3.01% | 3.01% | 100.00% | 18.02% | 18.02% | 18.02% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 66.67% | 17.16% | 39.46% | 52.83% | -0.73% | -9.28% | 36.05% | 76.25% | 100.36% | 66.67% | 18.02% | 71.51% | 103.60% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -2.79% | -2.79% | -2.79% | -11.42% | -11.42% | 3.01% | 3.01% | 3.01% | 100.00% | 18.02% | 18.02% | 18.02% |
| DOGE-USD | ALL_MATCHES | 40 | 25.00% | -16.48% | 0.66% | 16.06% | -21.88% | -38.16% | 10.18% | 19.34% | 43.72% | 52.50% | 1.14% | 16.86% | 36.16% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 25 | 12.00% | -20.27% | -10.93% | 1.79% | -21.51% | -43.16% | 9.72% | 19.14% | 20.53% | 32.00% | -9.67% | 1.32% | 24.78% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 21.19% | 64.67% | 101.97% | -6.19% | -37.62% | 33.43% | 77.41% | 131.24% | 67.50% | 23.63% | 82.09% | 169.93% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -7.13% | 0.78% | 5.52% | -16.37% | -43.21% | 12.61% | 22.19% | 27.94% | 33.33% | -9.80% | 25.23% | 46.24% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 30 | 90.00% | 24.46% | -1.43% | 52.81% | 63.33% | 12.25% | 72.78% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 88.89% | 61.75% | -10.45% | 104.86% | 100.00% | 121.32% | 171.02% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -2.79% | -11.42% | 3.01% | 100.00% | 18.02% | 18.02% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 24.00% | -17.24% | -22.44% | 19.20% | 44.00% | -1.60% | 21.04% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 40.00% | -6.93% | -17.46% | 38.28% | 90.00% | 13.00% | 58.73% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 0.00% | -37.64% | -37.65% | 8.49% | 20.00% | -41.50% | 41.31% |
| SOL-USD | HISTORICAL_BTC_BEAR | 28 | 64.29% | 18.80% | -4.30% | 61.89% | 64.29% | 19.01% | 80.33% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 80.00% | 63.89% | -4.10% | 124.07% | 90.00% | 157.57% | 305.50% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -15.44% | -22.81% | 9.45% | 0.00% | -18.27% | 9.45% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 90.62% | 24.46% | -1.43% | 53.78% | 71.88% | 18.98% | 79.65% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 76.94% | -18.61% | 104.86% | 80.00% | 144.94% | 236.59% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 17.16% | -0.73% | 76.25% | 66.67% | 18.02% | 80.52% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 25 | 12.00% | -20.27% | -21.51% | 19.14% | 32.00% | -9.67% | 21.04% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 10 | 40.00% | -4.67% | -23.51% | 23.74% | 100.00% | 16.30% | 59.55% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 6.79% | -11.60% | 33.67% | 100.00% | 20.67% | 36.79% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -18.34% | -19.39% | 27.76% | 33.33% | -8.51% | 31.44% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 24.03% | -4.11% | 64.03% | 65.52% | 21.63% | 81.97% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 60.36% | -4.48% | 130.06% | 100.00% | 82.86% | 210.74% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 67.43% | 0.00% | 166.45% | 66.67% | 201.42% | 282.86% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -7.13% | -16.37% | 22.19% | 33.33% | -9.80% | 72.94% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 1 | 3 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 25 | 0 | 25 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | MANA-USD | 2022-11-02 | 86.86% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.04% | -23.69% | 9.52% | -9.67% | -23.69% | 9.52% |
| DOGE-USD | NEO-USD | 2019-08-15 | 84.11% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -8.05% | -18.57% | 4.55% | 15.70% | -18.57% | 22.70% |
| DOGE-USD | ETH-USD | 2025-02-24 | 83.65% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -0.09% | -14.08% | 8.49% | 30.83% | -14.08% | 49.43% |
| DOGE-USD | ALGO-USD | 2026-01-19 | 83.60% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.05% | -4.94% | 19.19% | -23.29% | -25.87% | 19.19% |
| DOGE-USD | DASH-USD | 2019-11-03 | 83.48% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -43.40% | -43.40% | 4.87% | -41.50% | -66.28% | 4.87% |
| DOGE-USD | NEAR-USD | 2022-11-02 | 83.11% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -20.02% | -20.94% | 19.20% | -8.74% | -20.94% | 19.20% |
| DOGE-USD | SOL-USD | 2022-10-31 | 82.04% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -27.46% | -27.46% | 9.72% | -16.03% | -27.46% | 9.72% |
| DOGE-USD | ENJ-USD | 2022-11-02 | 81.78% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -20.27% | -20.27% | 22.87% | -1.58% | -20.27% | 22.87% |
| DOGE-USD | MANA-USD | 2025-02-09 | 81.41% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.06% | -21.51% | 5.31% | 1.32% | -27.09% | 5.31% |
| DOGE-USD | AAVE-USD | 2022-10-31 | 81.02% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.69% | -22.69% | 3.44% | -14.07% | -24.14% | 3.44% |

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

