# Market Regime Match Report

Generated: 2026-09-13 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-13 | RECOVERY | 77.274 $ | True | 16.57% | -4.66% | RECOVERY | 16.57% | -4.66% |
| DOGE-USD | 2026-09-13 | BEAR | 0.08481 $ | False | -3.74% | -12.08% | RECOVERY | 16.57% | -4.66% |
| SOL-USD | 2026-09-13 | RECOVERY | 101,86 $ | True | 37.69% | -8.81% | RECOVERY | 16.57% | -4.66% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 85.00% | 36.97% | 57.03% | 71.50% | -4.81% | -33.88% | 40.49% | 69.13% | 108.26% | 72.50% | 19.47% | 65.68% | 136.80% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 47.51% | 47.51% | 47.51% | -6.93% | -6.93% | 68.95% | 68.95% | 68.95% | 100.00% | 137.57% | 137.57% | 137.57% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 25.00% | -14.87% | -1.36% | 48.16% | -18.58% | -32.15% | 12.36% | 25.39% | 48.36% | 35.00% | -8.57% | 7.07% | 44.50% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -31.54% | -31.54% | -31.54% | -34.03% | -34.03% | 7.07% | 7.07% | 7.07% | 0.00% | -69.31% | -69.31% | -69.31% |
| DOGE-USD | SAME_ASSET_REGIME | 20 | 15.00% | -15.82% | -10.24% | 2.06% | -17.80% | -30.83% | 9.93% | 15.47% | 26.34% | 25.00% | -16.09% | -1.25% | 44.50% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 33.19% | 67.90% | 119.22% | -5.29% | -33.87% | 46.65% | 72.84% | 179.77% | 67.50% | 18.89% | 132.32% | 199.13% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -1.22% | 23.15% | 37.77% | -6.93% | -19.62% | 59.94% | 64.45% | 67.15% | 33.33% | -13.67% | 61.95% | 107.32% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 26 | 88.46% | 35.08% | -4.94% | 63.36% | 69.23% | 18.19% | 94.47% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 78.57% | 37.34% | -3.58% | 75.96% | 78.57% | 20.72% | 106.11% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 13.04% | -16.45% | -18.69% | 21.71% | 21.74% | -10.67% | 23.36% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 60.00% | 6.80% | -11.08% | 59.59% | 70.00% | 18.13% | 100.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 6 | 16.67% | -18.12% | -26.27% | 16.83% | 33.33% | -46.33% | 29.41% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -31.54% | -34.03% | 7.07% | 0.00% | -69.31% | 7.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 62.50% | 16.05% | -6.37% | 59.90% | 62.50% | 12.12% | 98.80% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 85.71% | 69.13% | -1.10% | 174.31% | 85.71% | 148.45% | 291.62% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -18.29% | -27.18% | 9.56% | 0.00% | -18.67% | 9.56% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 87.88% | 36.85% | -4.10% | 61.35% | 72.73% | 16.21% | 81.97% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 0.90% | -10.45% | 131.17% | 60.00% | 18.76% | 171.02% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 48.87% | -33.92% | 78.05% | 100.00% | 170.45% | 192.55% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 47.51% | -6.93% | 68.95% | 100.00% | 137.57% | 144.47% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 20 | 15.00% | -15.82% | -17.80% | 15.47% | 25.00% | -16.09% | 20.48% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 14 | 42.86% | -7.73% | -20.94% | 46.04% | 57.14% | 1.14% | 59.08% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -10.17% | -15.94% | 34.33% | 50.00% | 9.46% | 34.50% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -28.72% | -30.97% | 9.30% | 0.00% | -12.71% | 9.30% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 67.86% | 26.15% | -5.84% | 63.09% | 67.86% | 15.60% | 98.80% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 112.37% | -1.27% | 191.58% | 75.00% | 132.76% | 283.98% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 80.00% | 90.17% | -2.53% | 228.48% | 80.00% | 170.45% | 282.85% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -1.22% | -6.93% | 64.45% | 33.33% | -13.67% | 102.21% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 20 | 1 | 20 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | MANA-USD | 2022-10-28 | 85.64% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.58% | -26.10% | 3.31% | -21.11% | -33.73% | 3.31% |
| DOGE-USD | DASH-USD | 2019-10-29 | 82.87% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.73% | -30.58% | 9.23% | -45.15% | -64.88% | 9.23% |
| DOGE-USD | FIL-USD | 2022-05-15 | 82.68% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.45% | -16.88% | 3.53% | -21.51% | -21.73% | 3.53% |
| DOGE-USD | EOS-USD | 2019-10-29 | 81.80% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -15.18% | -22.30% | 18.74% | -47.68% | -59.08% | 18.74% |
| DOGE-USD | NEAR-USD | 2022-10-28 | 81.31% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -17.77% | -18.69% | 7.88% | -18.91% | -28.44% | 7.88% |
| DOGE-USD | YFI-USD | 2025-02-08 | 81.03% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -11.00% | -11.00% | 5.38% | 5.57% | -17.54% | 5.57% |
| DOGE-USD | ENJ-USD | 2022-10-28 | 80.91% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.74% | -12.44% | 14.38% | -10.30% | -25.78% | 14.38% |
| DOGE-USD | ETH-USD | 2025-02-19 | 80.29% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -7.43% | -15.36% | 6.87% | 43.86% | -15.36% | 47.20% |
| DOGE-USD | QTUM-USD | 2022-05-11 | 79.94% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -18.16% | -20.89% | 0.00% | -27.54% | -30.31% | 0.00% |
| DOGE-USD | CRV-USD | 2022-10-27 | 79.77% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.58% | -18.47% | 13.52% | -10.67% | -24.70% | 13.52% |

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

