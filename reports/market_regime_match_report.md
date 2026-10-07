# Market Regime Match Report

Generated: 2026-10-07 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-07 | RECOVERY | 84.181 $ | True | 33.21% | 1.99% | RECOVERY | 33.21% | 1.99% |
| DOGE-USD | 2026-10-07 | RECOVERY | 0.09024 $ | True | 23.86% | -4.94% | RECOVERY | 33.21% | 1.99% |
| SOL-USD | 2026-10-07 | BULL | 118,59 $ | True | 51.95% | 2.94% | RECOVERY | 33.21% | 1.99% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 37.50% | -7.03% | 10.98% | 27.07% | -13.90% | -25.15% | 12.27% | 25.87% | 48.33% | 47.50% | -1.75% | 26.36% | 54.15% |
| BTC-USD | SAME_BTC_REGIME | 17 | 29.41% | -8.58% | 1.33% | 14.55% | -12.26% | -17.82% | 17.47% | 24.51% | 35.71% | 29.41% | -3.46% | 6.90% | 34.44% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | -4.01% | 7.77% | 14.84% | -19.17% | -29.02% | 25.33% | 34.11% | 39.38% | 50.00% | -4.51% | 14.07% | 25.22% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | -4.01% | 7.77% | 14.84% | -19.17% | -29.02% | 25.33% | 34.11% | 39.38% | 50.00% | -4.51% | 14.07% | 25.22% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -7.18% | 8.29% | 26.44% | -17.57% | -26.61% | 9.95% | 22.40% | 29.60% | 45.00% | -1.75% | 25.11% | 59.79% |
| DOGE-USD | SAME_BTC_REGIME | 14 | 28.57% | -8.53% | 4.98% | 14.61% | -11.06% | -18.16% | 19.34% | 25.25% | 29.67% | 42.86% | -1.12% | 10.59% | 31.27% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 27.50% | -7.18% | 5.90% | 21.80% | -13.91% | -24.29% | 10.12% | 21.23% | 30.97% | 35.00% | -3.61% | 25.11% | 54.53% |
| SOL-USD | SAME_BTC_REGIME | 15 | 20.00% | -8.58% | -3.61% | 16.21% | -12.72% | -17.66% | 18.20% | 28.15% | 38.29% | 26.67% | -3.24% | 3.01% | 26.66% |
| SOL-USD | SAME_ASSET_REGIME | 1 | 100.00% | 13.20% | 13.20% | 13.20% | -18.66% | -18.66% | 13.66% | 13.66% | 13.66% | 100.00% | 24.06% | 24.06% | 24.06% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 17 | 47.06% | -0.09% | -11.77% | 27.35% | 64.71% | 10.13% | 43.24% |
| BTC-USD | HISTORICAL_BTC_BULL | 5 | 40.00% | -10.39% | -20.98% | 29.46% | 60.00% | 54.26% | 232.96% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -50.50% | -51.94% | 0.00% | 0.00% | -36.31% | 0.00% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 17 | 29.41% | -8.58% | -12.26% | 24.51% | 29.41% | -3.46% | 25.37% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 21 | 23.81% | -7.24% | -20.11% | 14.28% | 38.10% | -6.25% | 27.45% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 4.58% | -20.98% | 29.46% | 80.00% | 146.24% | 232.96% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 14 | 28.57% | -8.53% | -11.06% | 25.25% | 42.86% | -1.12% | 26.41% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 35.71% | -2.68% | -13.61% | 12.71% | 35.71% | -5.55% | 33.88% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 27.27% | -6.82% | -15.36% | 14.54% | 45.45% | -2.90% | 100.57% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 15 | 20.00% | -8.58% | -12.72% | 28.15% | 26.67% | -3.24% | 28.15% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 36.36% | -6.97% | -13.72% | 25.00% | 45.45% | -2.12% | 30.93% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 84.60% | -9.93% | 149.66% | 50.00% | 143.77% | 227.27% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -24.16% | -25.03% | 25.72% | 66.67% | 19.91% | 51.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -4.01% | -19.17% | 34.11% | 50.00% | -4.51% | 34.11% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 29.41% | -6.61% | -16.22% | 23.69% | 44.12% | -1.75% | 30.06% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 2.39% | -19.41% | 66.13% | 50.00% | 9.98% | 106.35% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -24.26% | -27.87% | 2.88% | 50.00% | 15.85% | 41.62% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 25.81% | -7.12% | -13.72% | 21.26% | 29.03% | -4.85% | 28.73% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 13.20% | -18.66% | 13.66% | 100.00% | 24.06% | 41.59% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 0.00% | -24.16% | -25.03% | 11.71% | 66.67% | 54.26% | 111.62% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 21.32% | -0.24% | 23.98% | 100.00% | 28.74% | 54.90% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -10.37% | -13.24% | 24.38% | 25.00% | -4.27% | 24.38% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 17 | 17 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 0 | 14 | 14 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 1 | 15 | 15 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | THETA-USD | 2023-09-12 | 89.38% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.12% | -9.20% | 30.93% | 6.90% | -13.58% | 30.93% |
| BTC-USD | QTUM-USD | 2023-09-03 | 88.43% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 1.33% | -4.79% | 19.28% | -3.46% | -10.06% | 19.28% |
| BTC-USD | MANA-USD | 2023-09-08 | 87.44% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -10.01% | -15.01% | 11.74% | -2.99% | -15.41% | 11.74% |
| BTC-USD | NEO-USD | 2023-09-08 | 87.00% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -8.58% | -13.72% | 11.41% | -6.84% | -20.33% | 11.41% |
| BTC-USD | XTZ-USD | 2023-09-13 | 86.95% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.21% | -5.88% | 25.37% | 17.66% | -5.88% | 25.37% |
| BTC-USD | EGLD-USD | 2023-09-13 | 86.50% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.42% | -18.33% | 17.47% | -2.12% | -21.63% | 17.47% |
| BTC-USD | CHZ-USD | 2023-09-12 | 86.37% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.87% | -9.45% | 24.51% | 37.11% | -9.45% | 41.09% |
| BTC-USD | SAND-USD | 2023-09-12 | 86.30% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.58% | -9.26% | 21.21% | -1.38% | -17.39% | 21.21% |
| BTC-USD | ATOM-USD | 2023-09-13 | 86.18% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -17.48% | 4.95% | -5.74% | -21.39% | 4.95% |
| BTC-USD | EOS-USD | 2023-09-13 | 86.18% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -14.00% | -16.82% | 7.24% | -6.21% | -19.75% | 7.24% |
| DOGE-USD | EGLD-USD | 2023-09-13 | 86.24% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.42% | -18.33% | 17.47% | -2.12% | -21.63% | 17.47% |
| DOGE-USD | NEAR-USD | 2023-09-08 | 84.94% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | THETA-USD | 2023-09-12 | 84.58% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.12% | -9.20% | 30.93% | 6.90% | -13.58% | 30.93% |
| DOGE-USD | EOS-USD | 2023-09-13 | 84.35% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -14.00% | -16.82% | 7.24% | -6.21% | -19.75% | 7.24% |
| DOGE-USD | SAND-USD | 2023-09-12 | 83.86% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.58% | -9.26% | 21.21% | -1.38% | -17.39% | 21.21% |
| DOGE-USD | XTZ-USD | 2023-09-13 | 83.39% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.21% | -5.88% | 25.37% | 17.66% | -5.88% | 25.37% |
| DOGE-USD | DOT-USD | 2023-09-13 | 83.36% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -17.49% | -17.78% | 10.37% | -3.97% | -24.26% | 10.37% |
| DOGE-USD | LRC-USD | 2023-09-13 | 82.90% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -9.93% | -11.88% | 26.76% | 0.63% | -15.97% | 26.76% |
| DOGE-USD | CHZ-USD | 2023-09-12 | 82.90% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.87% | -9.45% | 24.51% | 37.11% | -9.45% | 41.09% |
| DOGE-USD | ENJ-USD | 2023-09-03 | 82.72% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.69% | -10.24% | 24.87% | -9.90% | -18.68% | 24.87% |
| SOL-USD | ATOM-USD | 2023-09-13 | 89.89% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -17.48% | 4.95% | -5.74% | -21.39% | 4.95% |
| SOL-USD | EGLD-USD | 2023-09-13 | 89.56% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.42% | -18.33% | 17.47% | -2.12% | -21.63% | 17.47% |
| SOL-USD | THETA-USD | 2023-09-12 | 88.99% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.12% | -9.20% | 30.93% | 6.90% | -13.58% | 30.93% |
| SOL-USD | NEO-USD | 2023-09-08 | 87.56% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -8.58% | -13.72% | 11.41% | -6.84% | -20.33% | 11.41% |
| SOL-USD | NEAR-USD | 2023-09-08 | 86.93% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| SOL-USD | ENJ-USD | 2023-09-08 | 86.90% | RECOVERY | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -12.30% | -15.03% | 18.20% | -5.63% | -23.02% | 18.20% |
| SOL-USD | WAVES-USD | 2023-09-13 | 86.86% | RECOVERY | RECOVERY | SAME_BTC_ONLY | MIXED | -8.44% | -11.45% | 14.07% | -8.37% | -22.00% | 14.07% |
| SOL-USD | EOS-USD | 2023-09-13 | 86.83% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -14.00% | -16.82% | 7.24% | -6.21% | -19.75% | 7.24% |
| SOL-USD | LRC-USD | 2023-09-08 | 86.65% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| SOL-USD | DOT-USD | 2023-09-13 | 86.42% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -17.49% | -17.78% | 10.37% | -3.97% | -24.26% | 10.37% |

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

