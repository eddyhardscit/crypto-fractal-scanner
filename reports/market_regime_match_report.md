# Market Regime Match Report

Generated: 2026-10-06 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-06 | RECOVERY | 85.668 $ | True | 37.60% | 1.72% | RECOVERY | 37.60% | 1.72% |
| DOGE-USD | 2026-10-06 | RECOVERY | 0.09490 $ | True | 31.24% | -5.19% | RECOVERY | 37.60% | 1.72% |
| SOL-USD | 2026-10-06 | BULL | 120,12 $ | True | 54.42% | 2.46% | RECOVERY | 37.60% | 1.72% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 42.50% | -5.84% | 21.72% | 33.42% | -14.05% | -25.15% | 12.85% | 29.82% | 53.89% | 52.50% | 1.45% | 37.84% | 65.41% |
| BTC-USD | SAME_BTC_REGIME | 16 | 31.25% | -7.10% | 2.97% | 26.44% | -11.62% | -21.24% | 19.64% | 23.98% | 36.65% | 37.50% | -3.22% | 8.59% | 33.41% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 66.67% | 29.09% | 30.96% | 32.08% | -23.02% | -29.79% | 42.36% | 42.36% | 42.37% | 66.67% | 29.72% | 64.39% | 85.19% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 0.75% | 14.92% | 23.42% | -19.34% | -29.05% | 25.07% | 33.72% | 38.91% | 50.00% | -5.98% | 11.87% | 22.58% |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -5.35% | 5.40% | 30.11% | -15.45% | -26.61% | 13.02% | 23.98% | 53.93% | 45.00% | -1.75% | 20.51% | 54.53% |
| DOGE-USD | SAME_BTC_REGIME | 12 | 25.00% | -4.41% | 0.73% | 22.20% | -9.36% | -17.29% | 22.50% | 26.38% | 31.34% | 33.33% | -2.68% | 8.59% | 34.76% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -0.62% | -0.62% | -0.62% | -5.39% | -5.39% | 22.01% | 22.01% | 22.01% | 100.00% | 7.74% | 7.74% | 7.74% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 25.00% | -6.97% | 0.68% | 21.87% | -13.86% | -25.15% | 10.12% | 21.49% | 30.97% | 37.50% | -2.51% | 20.51% | 54.53% |
| SOL-USD | SAME_BTC_REGIME | 12 | 16.67% | -7.85% | -3.18% | 4.46% | -11.48% | -17.75% | 21.26% | 29.34% | 31.34% | 16.67% | -2.68% | -1.25% | 6.13% |
| SOL-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 16 | 56.25% | 5.71% | -14.77% | 42.58% | 68.75% | 14.04% | 73.12% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 42.86% | -6.30% | -19.81% | 39.21% | 57.14% | 54.26% | 229.75% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -50.50% | -51.94% | 0.00% | 0.00% | -36.31% | 0.00% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 16 | 31.25% | -7.10% | -11.62% | 23.98% | 37.50% | -3.22% | 25.58% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 22 | 27.27% | -5.13% | -19.38% | 20.22% | 45.45% | -3.86% | 29.26% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 40.00% | -6.30% | -20.98% | 11.50% | 60.00% | 54.26% | 146.24% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.72% | -8.72% | 52.83% | 100.00% | 14.96% | 52.83% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 12 | 25.00% | -4.41% | -9.36% | 26.38% | 33.33% | -2.68% | 31.04% |
| SOL-USD | HISTORICAL_BTC_BEAR | 16 | 31.25% | -4.52% | -12.89% | 19.97% | 43.75% | -3.35% | 33.71% |
| SOL-USD | HISTORICAL_BTC_BULL | 12 | 25.00% | -8.60% | -15.40% | 14.57% | 50.00% | 4.70% | 77.25% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 16.67% | -7.85% | -11.48% | 29.34% | 16.67% | -2.68% | 29.34% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 41.94% | -5.58% | -13.72% | 24.15% | 51.61% | 0.08% | 36.01% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -6.30% | -14.27% | 100.78% | 33.33% | -0.49% | 242.66% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -24.16% | -25.03% | 64.12% | 66.67% | 54.26% | 89.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 29.09% | -23.02% | 42.36% | 66.67% | 29.72% | 70.71% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 30.30% | -4.17% | -15.44% | 24.51% | 42.42% | -3.24% | 31.38% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 25.00% | -7.51% | -16.47% | 29.48% | 50.00% | 7.24% | 44.40% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -24.26% | -27.87% | 2.88% | 50.00% | 15.85% | 41.62% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -0.62% | -5.39% | 22.01% | 100.00% | 7.74% | 22.01% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 26.67% | -6.97% | -13.86% | 21.31% | 33.33% | -3.61% | 31.27% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 6 | 16.67% | -8.84% | -16.02% | 17.99% | 66.67% | 22.62% | 53.98% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -7.88% | -14.80% | 23.71% | 25.00% | -2.31% | 23.71% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 3 | 16 | 16 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 12 | 12 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 0 | 12 | 12 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | QTUM-USD | 2023-09-03 | 89.10% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 1.33% | -4.79% | 19.28% | -3.46% | -10.06% | 19.28% |
| BTC-USD | THETA-USD | 2023-09-12 | 88.74% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.12% | -9.20% | 30.93% | 6.90% | -13.58% | 30.93% |
| BTC-USD | MANA-USD | 2023-09-08 | 87.11% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -10.01% | -15.01% | 11.74% | -2.99% | -15.41% | 11.74% |
| BTC-USD | XTZ-USD | 2023-09-08 | 87.10% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| BTC-USD | EOS-USD | 2023-09-08 | 86.72% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| BTC-USD | ATOM-USD | 2023-09-08 | 86.70% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| BTC-USD | ETH-USD | 2019-03-23 | 86.58% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -27.58% | -31.48% | 7.76% | -41.69% | -41.69% | 7.76% |
| BTC-USD | EGLD-USD | 2023-09-08 | 86.56% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| BTC-USD | XRP-USD | 2023-09-08 | 86.39% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.08% | -10.99% | 4.28% | -13.14% | -18.82% | 4.28% |
| BTC-USD | SAND-USD | 2023-09-12 | 86.36% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.58% | -9.26% | 21.21% | -1.38% | -17.39% | 21.21% |
| DOGE-USD | NEAR-USD | 2023-09-08 | 86.39% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | EGLD-USD | 2023-09-13 | 85.51% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.42% | -18.33% | 17.47% | -2.12% | -21.63% | 17.47% |
| DOGE-USD | ENJ-USD | 2023-09-03 | 84.02% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.69% | -10.24% | 24.87% | -9.90% | -18.68% | 24.87% |
| DOGE-USD | SAND-USD | 2023-09-12 | 83.97% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.58% | -9.26% | 21.21% | -1.38% | -17.39% | 21.21% |
| DOGE-USD | EOS-USD | 2023-09-08 | 83.74% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| DOGE-USD | DOT-USD | 2023-09-13 | 83.66% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -17.49% | -17.78% | 10.37% | -3.97% | -24.26% | 10.37% |
| DOGE-USD | THETA-USD | 2023-09-12 | 83.60% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.12% | -9.20% | 30.93% | 6.90% | -13.58% | 30.93% |
| DOGE-USD | KAVA-USD | 2023-09-08 | 83.58% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| DOGE-USD | XTZ-USD | 2023-09-08 | 83.08% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| DOGE-USD | LRC-USD | 2023-09-08 | 82.57% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| SOL-USD | ATOM-USD | 2023-09-13 | 89.35% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -17.48% | 4.95% | -5.74% | -21.39% | 4.95% |
| SOL-USD | THETA-USD | 2023-09-12 | 88.45% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.12% | -9.20% | 30.93% | 6.90% | -13.58% | 30.93% |
| SOL-USD | EGLD-USD | 2023-09-13 | 88.40% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.42% | -18.33% | 17.47% | -2.12% | -21.63% | 17.47% |
| SOL-USD | NEO-USD | 2023-09-08 | 87.39% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -8.58% | -13.72% | 11.41% | -6.84% | -20.33% | 11.41% |
| SOL-USD | LRC-USD | 2023-09-08 | 87.21% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| SOL-USD | ENJ-USD | 2023-09-03 | 87.15% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.69% | -10.24% | 24.87% | -9.90% | -18.68% | 24.87% |
| SOL-USD | NEAR-USD | 2023-09-08 | 87.13% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| SOL-USD | ALGO-USD | 2023-09-12 | 86.38% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.72% | -12.72% | 21.31% | -0.88% | -19.77% | 21.31% |
| SOL-USD | WAVES-USD | 2023-09-08 | 86.38% | RECOVERY | RECOVERY | SAME_BTC_ONLY | MIXED | 5.14% | 0.00% | 28.82% | -1.73% | -11.91% | 28.82% |
| SOL-USD | SAND-USD | 2023-09-12 | 86.37% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.58% | -9.26% | 21.21% | -1.38% | -17.39% | 21.21% |

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

