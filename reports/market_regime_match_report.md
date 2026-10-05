# Market Regime Match Report

Generated: 2026-10-05 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-05 | RECOVERY | 85.483 $ | True | 35.05% | 1.40% | RECOVERY | 35.05% | 1.40% |
| DOGE-USD | 2026-10-05 | RECOVERY | 0.09504 $ | True | 28.11% | -5.51% | RECOVERY | 35.05% | 1.40% |
| SOL-USD | 2026-10-05 | RECOVERY | 120,09 $ | True | 48.91% | 1.90% | RECOVERY | 35.05% | 1.40% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 47.50% | -1.49% | 24.55% | 39.15% | -12.76% | -23.09% | 16.61% | 37.50% | 65.51% | 55.00% | 2.82% | 41.53% | 100.12% |
| BTC-USD | SAME_BTC_REGIME | 15 | 33.33% | -5.13% | 7.19% | 26.97% | -10.99% | -19.18% | 16.06% | 21.90% | 37.98% | 33.33% | -4.63% | 6.86% | 23.56% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 100.00% | 29.09% | 30.96% | 32.08% | -7.20% | -19.85% | 42.36% | 42.36% | 42.37% | 100.00% | 29.72% | 64.39% | 85.19% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 21.07% | 25.08% | 27.48% | -3.60% | -6.48% | 28.13% | 35.25% | 39.52% | 100.00% | 22.01% | 25.87% | 28.18% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -6.53% | 5.82% | 36.83% | -15.45% | -26.61% | 12.06% | 24.06% | 65.51% | 42.50% | -3.11% | 23.24% | 65.45% |
| DOGE-USD | SAME_BTC_REGIME | 11 | 27.27% | -3.69% | -0.16% | 23.80% | -9.26% | -15.18% | 20.00% | 24.33% | 31.38% | 27.27% | -3.24% | -0.65% | 13.64% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -0.62% | -0.62% | -0.62% | -5.39% | -5.39% | 22.01% | 22.01% | 22.01% | 100.00% | 7.74% | 7.74% | 7.74% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 30.00% | -7.18% | 6.93% | 30.11% | -13.76% | -25.14% | 14.22% | 25.85% | 45.30% | 40.00% | -3.07% | 24.26% | 59.10% |
| SOL-USD | SAME_BTC_REGIME | 13 | 23.08% | -5.58% | -1.65% | 20.07% | -9.26% | -14.89% | 21.31% | 28.82% | 31.29% | 30.77% | -1.73% | 0.08% | 12.29% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 25.00% | -7.88% | 0.82% | 3.41% | -14.80% | -32.79% | 11.01% | 23.71% | 26.78% | 25.00% | -2.31% | 0.64% | 4.90% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 5.14% | 5.14% | 5.14% | 0.00% | 0.00% | 28.82% | 28.82% | 28.82% | 0.00% | -1.73% | -1.73% | -1.73% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 19 | 57.89% | 1.89% | -11.64% | 42.80% | 68.42% | 12.83% | 82.51% |
| BTC-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 5.29% | -14.27% | 48.97% | 80.00% | 124.16% | 232.96% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -50.50% | -51.94% | 0.00% | 0.00% | -36.31% | 0.00% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 15 | 33.33% | -5.13% | -10.99% | 21.90% | 33.33% | -4.63% | 21.90% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 24 | 29.17% | -7.11% | -18.97% | 20.83% | 41.67% | -4.94% | 37.65% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 50.00% | -9.79% | -23.01% | 13.52% | 75.00% | 100.25% | 167.92% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.72% | -8.72% | 52.83% | 100.00% | 14.96% | 52.83% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 11 | 27.27% | -3.69% | -9.26% | 24.33% | 27.27% | -3.24% | 24.33% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 29.41% | -7.24% | -15.46% | 22.01% | 41.18% | -7.04% | 43.24% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 40.00% | -10.81% | -15.40% | 18.97% | 50.00% | 15.03% | 123.24% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 23.08% | -5.58% | -9.26% | 28.82% | 30.77% | -1.73% | 28.82% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 42.42% | -2.94% | -12.83% | 29.46% | 48.48% | -1.33% | 36.06% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 81.51% | -7.14% | 145.42% | 50.00% | 198.24% | 358.24% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 32.89% | -14.30% | 93.49% | 100.00% | 57.96% | 106.96% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 100.00% | 29.09% | -7.20% | 42.36% | 100.00% | 29.72% | 70.71% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 35 | 31.43% | -6.10% | -15.46% | 22.50% | 37.14% | -3.46% | 30.15% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -8.72% | -8.72% | 52.83% | 100.00% | 14.96% | 52.83% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -24.16% | -25.03% | 64.12% | 66.67% | 54.26% | 89.39% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -0.62% | -5.39% | 22.01% | 100.00% | 7.74% | 22.01% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 32 | 28.12% | -7.18% | -13.76% | 26.01% | 37.50% | -5.86% | 34.35% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -5.93% | -13.21% | 44.53% | 75.00% | 43.60% | 113.91% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -7.88% | -14.80% | 23.71% | 25.00% | -2.31% | 23.71% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 3 | 15 | 15 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 1 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | QTUM-USD | 2023-09-03 | 89.65% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 1.33% | -4.79% | 19.28% | -3.46% | -10.06% | 19.28% |
| BTC-USD | XTZ-USD | 2023-09-08 | 88.24% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| BTC-USD | MANA-USD | 2023-09-03 | 87.81% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.13% | -12.85% | 14.59% | -4.63% | -13.25% | 14.59% |
| BTC-USD | EGLD-USD | 2023-09-08 | 87.73% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| BTC-USD | ATOM-USD | 2023-09-08 | 87.59% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| BTC-USD | EOS-USD | 2023-09-08 | 87.34% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| BTC-USD | ETC-USD | 2023-09-08 | 86.66% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |
| BTC-USD | XRP-USD | 2023-09-08 | 86.50% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.08% | -10.99% | 4.28% | -13.14% | -18.82% | 4.28% |
| BTC-USD | BTC-USD | 2023-09-03 | 86.16% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 13.05% | 0.00% | 13.88% | 14.31% | -4.21% | 14.31% |
| BTC-USD | KAVA-USD | 2023-09-08 | 85.96% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| DOGE-USD | NEAR-USD | 2023-09-08 | 86.97% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | EOS-USD | 2023-09-08 | 84.44% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| DOGE-USD | KAVA-USD | 2023-09-08 | 84.38% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| DOGE-USD | EGLD-USD | 2023-09-08 | 84.10% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| DOGE-USD | XTZ-USD | 2023-09-08 | 83.99% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| DOGE-USD | DOT-USD | 2023-09-13 | 83.83% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -17.49% | -17.78% | 10.37% | -3.97% | -24.26% | 10.37% |
| DOGE-USD | LRC-USD | 2023-09-08 | 83.33% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| DOGE-USD | ENJ-USD | 2023-09-03 | 83.17% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.69% | -10.24% | 24.87% | -9.90% | -18.68% | 24.87% |
| DOGE-USD | SAND-USD | 2023-09-12 | 83.03% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.58% | -9.26% | 21.21% | -1.38% | -17.39% | 21.21% |
| DOGE-USD | QTUM-USD | 2023-09-03 | 82.58% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 1.33% | -4.79% | 19.28% | -3.46% | -10.06% | 19.28% |
| SOL-USD | ATOM-USD | 2023-09-13 | 89.38% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -17.48% | 4.95% | -5.74% | -21.39% | 4.95% |
| SOL-USD | ENJ-USD | 2023-09-03 | 87.97% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.69% | -10.24% | 24.87% | -9.90% | -18.68% | 24.87% |
| SOL-USD | EGLD-USD | 2023-09-08 | 87.32% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| SOL-USD | LRC-USD | 2023-09-08 | 87.29% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| SOL-USD | NEAR-USD | 2023-09-08 | 87.28% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| SOL-USD | WAVES-USD | 2023-09-08 | 87.16% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 5.14% | 0.00% | 28.82% | -1.73% | -11.91% | 28.82% |
| SOL-USD | NEO-USD | 2023-09-08 | 87.06% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -8.58% | -13.72% | 11.41% | -6.84% | -20.33% | 11.41% |
| SOL-USD | THETA-USD | 2023-09-12 | 86.54% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.12% | -9.20% | 30.93% | 6.90% | -13.58% | 30.93% |
| SOL-USD | KAVA-USD | 2023-09-08 | 86.23% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| SOL-USD | ALGO-USD | 2023-09-12 | 86.17% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.72% | -12.72% | 21.31% | -0.88% | -19.77% | 21.31% |

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

