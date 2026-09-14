# Market Regime Match Report

Generated: 2026-09-14 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-14 | RECOVERY | 77.493 $ | True | 18.13% | -4.43% | RECOVERY | 18.13% | -4.43% |
| DOGE-USD | 2026-09-14 | BEAR | 0.08402 $ | False | -3.55% | -11.94% | RECOVERY | 18.13% | -4.43% |
| SOL-USD | 2026-09-14 | RECOVERY | 101,00 $ | True | 37.58% | -8.49% | RECOVERY | 18.13% | -4.43% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 85.00% | 36.97% | 55.12% | 67.55% | -4.54% | -33.88% | 40.49% | 65.26% | 106.35% | 72.50% | 19.47% | 58.55% | 136.80% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 47.51% | 47.51% | 47.51% | -6.93% | -6.93% | 68.95% | 68.95% | 68.95% | 100.00% | 137.57% | 137.57% | 137.57% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 25.00% | -12.84% | 0.21% | 15.76% | -18.52% | -32.06% | 12.36% | 24.68% | 44.99% | 42.50% | -6.20% | 12.12% | 32.40% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -31.54% | -31.54% | -31.54% | -34.03% | -34.03% | 7.07% | 7.07% | 7.07% | 0.00% | -69.31% | -69.31% | -69.31% |
| DOGE-USD | SAME_ASSET_REGIME | 23 | 17.39% | -13.59% | -7.86% | 1.95% | -17.24% | -29.88% | 9.23% | 17.90% | 30.63% | 30.43% | -10.47% | 3.26% | 15.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 31.40% | 61.27% | 90.83% | -4.00% | -34.08% | 36.89% | 72.72% | 134.47% | 60.00% | 22.13% | 116.90% | 199.13% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -1.22% | 23.15% | 37.77% | -6.93% | -41.33% | 22.31% | 45.63% | 59.62% | 33.33% | -13.67% | 61.95% | 107.32% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 25 | 88.00% | 33.08% | -4.10% | 61.35% | 68.00% | 16.21% | 81.97% |
| BTC-USD | HISTORICAL_BTC_BULL | 15 | 80.00% | 37.82% | -4.97% | 73.86% | 80.00% | 22.69% | 104.97% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 12.00% | -17.24% | -18.69% | 20.13% | 24.00% | -10.47% | 20.13% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 55.56% | 7.16% | -11.00% | 63.91% | 88.89% | 32.24% | 179.39% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 40.00% | -0.09% | -22.30% | 18.74% | 60.00% | 6.12% | 49.43% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -31.54% | -34.03% | 7.07% | 0.00% | -69.31% | 7.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 25 | 68.00% | 24.79% | -3.88% | 59.42% | 56.00% | 8.25% | 81.97% |
| SOL-USD | HISTORICAL_BTC_BULL | 12 | 83.33% | 69.13% | 0.00% | 174.21% | 83.33% | 159.58% | 302.94% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 0.00% | -28.41% | -29.31% | 6.52% | 0.00% | -24.40% | 6.52% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 87.88% | 36.85% | -3.88% | 58.96% | 72.73% | 16.21% | 79.60% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 0.90% | -10.45% | 131.17% | 60.00% | 18.76% | 171.02% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 48.87% | -33.92% | 78.05% | 100.00% | 170.45% | 192.55% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 47.51% | -6.93% | 68.95% | 100.00% | 137.57% | 144.47% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 23 | 17.39% | -13.59% | -17.24% | 17.90% | 30.43% | -10.47% | 24.21% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 13 | 38.46% | -6.30% | -24.59% | 27.97% | 69.23% | 6.12% | 64.01% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 10.63% | 0.00% | 42.88% | 100.00% | 33.89% | 42.88% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 0.00% | -25.90% | -27.91% | 5.13% | 0.00% | -21.46% | 5.13% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 68.97% | 26.30% | -3.88% | 64.03% | 58.62% | 16.39% | 99.27% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 70.44% | -9.31% | 141.09% | 75.00% | 141.17% | 244.41% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 69.52% | -10.43% | 187.88% | 75.00% | 212.30% | 272.65% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -1.22% | -6.93% | 45.63% | 33.33% | -13.67% | 83.39% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 23 | 1 | 23 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | MANA-USD | 2022-10-28 | 84.59% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.58% | -26.10% | 3.31% | -21.11% | -33.73% | 3.31% |
| DOGE-USD | NEAR-USD | 2022-10-28 | 82.05% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -17.77% | -18.69% | 7.88% | -18.91% | -28.44% | 7.88% |
| DOGE-USD | FIL-USD | 2022-05-15 | 81.84% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.45% | -16.88% | 3.53% | -21.51% | -21.73% | 3.53% |
| DOGE-USD | ETH-USD | 2025-02-24 | 81.80% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -0.09% | -14.08% | 8.49% | 30.83% | -14.08% | 49.43% |
| DOGE-USD | DASH-USD | 2019-10-29 | 81.24% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.73% | -30.58% | 9.23% | -45.15% | -64.88% | 9.23% |
| DOGE-USD | MATIC-USD | 2022-05-01 | 80.92% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -8.76% | -17.13% | 11.21% | -9.73% | -23.58% | 11.21% |
| DOGE-USD | ENJ-USD | 2022-10-28 | 80.43% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.74% | -12.44% | 14.38% | -10.30% | -25.78% | 14.38% |
| DOGE-USD | YFI-USD | 2025-02-08 | 80.41% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -11.00% | -11.00% | 5.38% | 5.57% | -17.54% | 5.57% |
| DOGE-USD | MKR-USD | 2018-07-22 | 80.22% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -39.79% | -49.29% | 10.63% | -23.59% | -49.54% | 10.63% |
| DOGE-USD | CRV-USD | 2022-10-27 | 79.79% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.58% | -18.47% | 13.52% | -10.67% | -24.70% | 13.52% |

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

