# Market Regime Match Report

Generated: 2026-08-28 08:01 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-08-28 | MIXED | 79.679 $ | True | 8.03% | -8.26% | MIXED | 8.03% | -8.26% |
| DOGE-USD | 2026-08-28 | BEAR | 0.08752 $ | False | -12.82% | -14.95% | MIXED | 8.03% | -8.26% |
| SOL-USD | 2026-08-28 | RECOVERY | 106,34 $ | True | 28.82% | -13.98% | MIXED | 8.03% | -8.26% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 6.41% | 21.37% | 43.49% | -10.88% | -34.10% | 14.37% | 31.80% | 54.77% | 67.50% | 13.91% | 27.48% | 81.19% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -1.72% | -1.72% | -1.72% | -7.24% | -7.24% | 44.52% | 44.52% | 44.52% | 100.00% | 22.36% | 22.36% | 22.36% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -4.56% | 20.50% | 42.28% | -11.97% | -36.82% | 17.69% | 24.96% | 66.06% | 35.00% | -11.10% | 13.36% | 71.11% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 10 | 30.00% | -9.50% | 15.72% | 32.79% | -16.95% | -36.20% | 11.83% | 20.30% | 49.40% | 20.00% | -20.25% | -4.59% | 55.95% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 6.90% | 55.37% | 94.36% | -13.61% | -31.60% | 21.89% | 62.05% | 132.74% | 62.50% | 27.76% | 66.31% | 136.46% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 2 | 100.00% | 3.29% | 3.86% | 4.21% | -14.92% | -16.64% | 17.09% | 18.84% | 19.88% | 100.00% | 32.90% | 41.60% | 46.81% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 6 | 33.33% | -28.92% | -29.56% | 30.70% | 33.33% | -28.01% | 80.87% |
| BTC-USD | HISTORICAL_BTC_BULL | 25 | 72.00% | 4.16% | -10.34% | 18.01% | 76.00% | 14.56% | 62.02% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 7 | 100.00% | 18.89% | -13.32% | 34.87% | 57.14% | 13.26% | 57.26% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 34.12% | -4.40% | 66.49% | 100.00% | 68.08% | 96.48% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 5 | 20.00% | -5.61% | -14.75% | 16.29% | 20.00% | -15.42% | 16.29% |
| DOGE-USD | HISTORICAL_BTC_BULL | 32 | 40.62% | -2.86% | -9.33% | 24.96% | 40.62% | -5.74% | 48.12% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -14.50% | -21.51% | 35.23% | 0.00% | -25.07% | 35.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 9 | 33.33% | -12.67% | -19.42% | 31.22% | 33.33% | -21.82% | 62.62% |
| SOL-USD | HISTORICAL_BTC_BULL | 27 | 77.78% | 9.27% | -12.76% | 70.85% | 70.37% | 29.02% | 131.82% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 10.10% | -16.48% | 12.22% | 0.00% | -1.95% | 36.95% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 69.95% | -1.56% | 86.09% | 100.00% | 113.80% | 144.29% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 72.41% | 6.74% | -11.06% | 31.66% | 58.62% | 3.84% | 65.84% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 14.13% | -5.26% | 23.88% | 80.00% | 76.15% | 174.70% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 23.22% | -19.34% | 32.28% | 100.00% | 22.03% | 35.00% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -1.72% | -7.24% | 44.52% | 100.00% | 22.36% | 44.52% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 2.14% | -12.76% | 11.63% | 100.00% | 15.52% | 40.62% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 10 | 30.00% | -9.50% | -16.95% | 20.30% | 20.00% | -20.25% | 46.69% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 26 | 42.31% | -1.63% | -9.33% | 30.14% | 42.31% | -4.91% | 59.55% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -27.04% | -31.63% | 9.96% | 25.00% | -29.88% | 13.46% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 26 | 65.38% | 3.94% | -14.26% | 31.08% | 53.85% | 8.77% | 66.62% |
| SOL-USD | HISTORICAL_ASSET_BULL | 11 | 72.73% | 83.57% | -12.56% | 156.86% | 72.73% | 63.03% | 163.21% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 98.37% | -0.47% | 98.37% | 100.00% | 158.76% | 174.79% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 3.29% | -14.92% | 18.84% | 100.00% | 32.90% | 46.92% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 10 | 0 | 10 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | FIL-USD | 2022-04-30 | 87.32% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.15% | -36.15% | 0.00% | -37.52% | -40.20% | 0.00% |
| DOGE-USD | MATIC-USD | 2022-04-16 | 84.34% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -5.61% | -12.38% | 16.29% | -14.57% | -20.09% | 16.29% |
| DOGE-USD | YFI-USD | 2022-04-25 | 83.28% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -14.50% | -21.51% | 13.63% | -25.07% | -25.52% | 13.63% |
| DOGE-USD | DOT-USD | 2023-07-30 | 83.15% | BULL | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.64% | -1.59% | 21.64% | 49.86% | -1.59% | 85.75% |
| DOGE-USD | NEAR-USD | 2022-05-06 | 82.80% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -13.38% | -36.06% | 0.00% | -46.25% | -46.25% | 0.00% |
| DOGE-USD | EGLD-USD | 2023-07-25 | 82.80% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 40.51% | 0.00% | 48.58% | 110.79% | 0.00% | 126.47% |
| DOGE-USD | EOS-USD | 2022-04-26 | 82.48% | RECOVERY | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 31.93% | 0.00% | 56.82% | -1.27% | -2.15% | 56.82% |
| DOGE-USD | EOS-USD | 2021-12-22 | 81.99% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.56% | -28.56% | 2.40% | -50.86% | -57.12% | 2.40% |
| DOGE-USD | KSM-USD | 2021-12-25 | 81.37% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.71% | -36.71% | 0.00% | -63.53% | -67.03% | 0.00% |
| DOGE-USD | MANA-USD | 2022-10-13 | 81.27% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -2.01% | -12.01% | 10.03% | -15.42% | -29.42% | 10.03% |

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

