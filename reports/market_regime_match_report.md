# Market Regime Match Report

Generated: 2026-09-12 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-12 | RECOVERY | 77.219 $ | True | 17.51% | -4.89% | RECOVERY | 17.51% | -4.89% |
| DOGE-USD | 2026-09-12 | BEAR | 0.08434 $ | False | -4.99% | -12.27% | RECOVERY | 17.51% | -4.89% |
| SOL-USD | 2026-09-12 | RECOVERY | 101,55 $ | True | 42.69% | -9.17% | RECOVERY | 17.51% | -4.89% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 82.50% | 35.67% | 52.63% | 88.33% | -5.30% | -34.04% | 39.63% | 63.25% | 118.17% | 70.00% | 17.49% | 54.80% | 136.75% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | -0.18% | 23.67% | 37.97% | -27.58% | -44.10% | 192.45% | 254.21% | 291.26% | 50.00% | 46.62% | 92.09% | 119.38% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -14.87% | 1.33% | 19.27% | -17.80% | -32.09% | 10.90% | 23.21% | 39.33% | 32.50% | -8.96% | 3.73% | 35.18% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 22 | 22.73% | -14.87% | -7.76% | 10.46% | -17.08% | -31.80% | 8.56% | 21.50% | 27.16% | 27.27% | -15.18% | 1.46% | 31.79% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 35.15% | 60.06% | 113.47% | -6.32% | -31.99% | 41.41% | 69.99% | 148.24% | 65.00% | 16.10% | 105.73% | 199.13% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -1.22% | 23.15% | 37.77% | -6.93% | -19.62% | 59.94% | 64.45% | 67.15% | 33.33% | -13.67% | 61.95% | 107.32% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 26 | 84.62% | 35.78% | -5.72% | 58.82% | 69.23% | 18.19% | 86.88% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 78.57% | 29.19% | -3.58% | 81.63% | 71.43% | 16.98% | 147.49% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 26 | 19.23% | -16.52% | -18.58% | 22.07% | 26.92% | -10.49% | 26.92% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 50.00% | -4.50% | -12.72% | 21.40% | 50.00% | 0.23% | 39.34% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 25.00% | -11.30% | -18.83% | 23.84% | 25.00% | -37.43% | 41.17% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 61.54% | 26.61% | -7.50% | 57.37% | 61.54% | 12.12% | 89.79% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 76.92% | 67.32% | -2.53% | 145.34% | 76.92% | 22.69% | 294.55% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.18% | -20.87% | 12.60% | 0.00% | -12.94% | 12.60% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 87.50% | 35.67% | -4.54% | 48.24% | 71.88% | 15.70% | 71.17% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.49% | -7.66% | 89.19% | 60.00% | 18.76% | 179.49% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 91.00% | -16.34% | 125.42% | 100.00% | 162.43% | 162.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -0.18% | -27.58% | 254.21% | 50.00% | 46.62% | 273.09% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 22 | 22.73% | -14.87% | -17.08% | 21.50% | 27.27% | -15.18% | 30.73% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 11 | 36.36% | -12.10% | -25.09% | 24.49% | 45.45% | -2.65% | 37.99% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 10.11% | -3.76% | 49.51% | 66.67% | 21.20% | 99.06% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -27.34% | -28.35% | 4.00% | 0.00% | -10.69% | 4.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 68.97% | 34.53% | -6.49% | 61.35% | 68.97% | 15.99% | 92.05% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 35.78% | -4.85% | 138.78% | 60.00% | 19.29% | 243.80% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 90.17% | -2.53% | 228.60% | 66.67% | 163.27% | 268.50% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -1.22% | -6.93% | 64.45% | 33.33% | -13.67% | 102.21% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 22 | 0 | 22 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | MANA-USD | 2022-10-28 | 85.76% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.58% | -26.10% | 3.31% | -21.11% | -33.73% | 3.31% |
| DOGE-USD | ETH-USD | 2025-02-19 | 82.35% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -7.43% | -15.36% | 6.87% | 43.86% | -15.36% | 47.20% |
| DOGE-USD | DASH-USD | 2019-10-29 | 81.90% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.73% | -30.58% | 9.23% | -45.15% | -64.88% | 9.23% |
| DOGE-USD | EOS-USD | 2019-10-29 | 80.95% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -15.18% | -22.30% | 18.74% | -47.68% | -59.08% | 18.74% |
| DOGE-USD | ENJ-USD | 2022-10-28 | 80.78% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.74% | -12.44% | 14.38% | -10.30% | -25.78% | 14.38% |
| DOGE-USD | NEAR-USD | 2022-10-28 | 80.77% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -17.77% | -18.69% | 7.88% | -18.91% | -28.44% | 7.88% |
| DOGE-USD | FIL-USD | 2022-05-15 | 80.67% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.45% | -16.88% | 3.53% | -21.51% | -21.73% | 3.53% |
| DOGE-USD | YFI-USD | 2022-05-10 | 80.53% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.15% | -23.92% | 0.00% | -30.34% | -32.23% | 0.00% |
| DOGE-USD | THETA-USD | 2026-01-29 | 80.19% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -34.68% | -36.16% | 5.54% | -40.86% | -45.71% | 5.54% |
| DOGE-USD | ALGO-USD | 2026-01-14 | 79.79% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 9.51% | 0.00% | 27.32% | -14.61% | -17.13% | 27.32% |

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

