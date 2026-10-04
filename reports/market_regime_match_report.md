# Market Regime Match Report

Generated: 2026-10-04 14:39 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-04 | RECOVERY | 85.128 $ | True | 33.02% | 1.19% | RECOVERY | 33.02% | 1.19% |
| DOGE-USD | 2026-10-04 | RECOVERY | 0.09358 $ | True | 22.19% | -5.83% | RECOVERY | 33.02% | 1.19% |
| SOL-USD | 2026-10-04 | RECOVERY | 121,45 $ | True | 48.26% | 1.52% | RECOVERY | 33.02% | 1.19% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 52.50% | 0.78% | 21.78% | 39.15% | -10.65% | -22.65% | 17.67% | 38.95% | 65.51% | 52.50% | 0.46% | 32.29% | 86.69% |
| BTC-USD | SAME_BTC_REGIME | 13 | 46.15% | -1.65% | 9.65% | 28.03% | -8.66% | -14.72% | 20.00% | 31.38% | 41.49% | 38.46% | -3.46% | 0.84% | 26.50% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 29.09% | 29.09% | 29.09% | -7.20% | -7.20% | 42.37% | 42.37% | 42.37% | 100.00% | 29.72% | 29.72% | 29.72% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 29.09% | 29.09% | 29.09% | -7.20% | -7.20% | 42.37% | 42.37% | 42.37% | 100.00% | 29.72% | 29.72% | 29.72% |
| DOGE-USD | ALL_MATCHES | 40 | 35.00% | -5.00% | 21.78% | 47.29% | -15.10% | -26.37% | 16.49% | 32.51% | 96.52% | 47.50% | -2.00% | 29.77% | 101.64% |
| DOGE-USD | SAME_BTC_REGIME | 9 | 33.33% | -3.03% | 6.09% | 26.78% | -9.25% | -16.54% | 20.00% | 30.24% | 41.27% | 44.44% | -2.99% | 8.08% | 18.92% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -0.62% | -0.62% | -0.62% | -5.39% | -5.39% | 22.01% | 22.01% | 22.01% | 100.00% | 7.74% | 7.74% | 7.74% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 35.00% | -6.56% | 12.68% | 36.28% | -13.27% | -25.14% | 14.78% | 28.98% | 65.51% | 45.00% | -1.53% | 34.72% | 86.86% |
| SOL-USD | SAME_BTC_REGIME | 12 | 33.33% | -3.36% | 9.80% | 28.56% | -9.74% | -15.04% | 22.55% | 29.46% | 41.27% | 33.33% | -2.49% | 3.47% | 28.11% |
| SOL-USD | SAME_ASSET_REGIME | 6 | 50.00% | 2.26% | 23.10% | 50.77% | -6.30% | -30.34% | 25.41% | 38.98% | 66.76% | 50.00% | 3.01% | 24.22% | 57.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 17.11% | 23.10% | 26.69% | -3.60% | -6.48% | 35.59% | 38.98% | 41.02% | 50.00% | 13.99% | 21.85% | 26.57% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 21 | 57.14% | 1.45% | -10.30% | 41.87% | 57.14% | 2.97% | 43.24% |
| BTC-USD | HISTORICAL_BTC_BULL | 4 | 50.00% | -0.51% | -13.48% | 84.24% | 75.00% | 89.21% | 288.36% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | -12.65% | -31.59% | 18.90% | 50.00% | 100.93% | 205.53% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 13 | 46.15% | -1.65% | -8.66% | 31.38% | 38.46% | -3.46% | 31.38% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 28.00% | -7.24% | -17.65% | 26.28% | 40.00% | -6.05% | 35.89% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 29.46% | -15.44% | 110.64% | 80.00% | 146.24% | 232.96% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.72% | -8.72% | 52.83% | 100.00% | 14.96% | 52.83% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 9 | 33.33% | -3.03% | -9.25% | 30.24% | 44.44% | -2.99% | 30.24% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 31.58% | -7.24% | -15.46% | 29.18% | 47.37% | -1.33% | 54.54% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -10.38% | -15.44% | 22.56% | 55.56% | 32.95% | 146.24% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 33.33% | -3.36% | -9.74% | 29.46% | 33.33% | -2.49% | 29.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 35 | 51.43% | 0.23% | -10.99% | 33.64% | 48.57% | -1.33% | 39.92% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 81.51% | -7.14% | 145.42% | 50.00% | 198.24% | 358.24% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 32.89% | -14.30% | 93.49% | 100.00% | 57.96% | 106.96% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 29.09% | -7.20% | 42.37% | 100.00% | 29.72% | 42.37% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 32.35% | -7.11% | -15.45% | 28.66% | 41.18% | -3.11% | 34.84% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 47.00% | 0.00% | 150.35% | 66.67% | 14.96% | 292.23% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 32.89% | -14.30% | 93.49% | 100.00% | 57.96% | 106.96% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -0.62% | -5.39% | 22.01% | 100.00% | 7.74% | 22.01% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 30.00% | -7.35% | -13.76% | 24.60% | 40.00% | -4.49% | 42.92% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -5.93% | -13.21% | 44.53% | 75.00% | 43.60% | 113.91% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 2.26% | -6.30% | 38.98% | 50.00% | 3.01% | 38.98% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 1 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_ASSET_REGIME | 2 | 6 | 12 | 6 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | EGLD-USD | 2023-09-08 | 88.85% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| BTC-USD | XTZ-USD | 2023-09-08 | 88.73% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| BTC-USD | QTUM-USD | 2023-09-03 | 88.70% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 1.33% | -4.79% | 19.28% | -3.46% | -10.06% | 19.28% |
| BTC-USD | ATOM-USD | 2023-09-08 | 87.97% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| BTC-USD | EOS-USD | 2023-09-08 | 87.88% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| BTC-USD | MANA-USD | 2023-09-03 | 87.71% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.13% | -12.85% | 14.59% | -4.63% | -13.25% | 14.59% |
| BTC-USD | ETC-USD | 2023-09-08 | 87.12% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |
| BTC-USD | XRP-USD | 2023-09-08 | 86.37% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.08% | -10.99% | 4.28% | -13.14% | -18.82% | 4.28% |
| BTC-USD | KAVA-USD | 2023-09-08 | 86.15% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| BTC-USD | NEAR-USD | 2023-09-08 | 85.60% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | NEAR-USD | 2023-09-08 | 86.97% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | EGLD-USD | 2023-09-08 | 86.24% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| DOGE-USD | EOS-USD | 2023-09-08 | 85.40% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| DOGE-USD | XTZ-USD | 2023-09-08 | 84.70% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| DOGE-USD | KAVA-USD | 2023-09-08 | 84.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| DOGE-USD | DOT-USD | 2023-09-08 | 84.45% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 6.09% | -5.23% | 30.24% | 8.08% | -10.63% | 30.24% |
| DOGE-USD | LRC-USD | 2023-09-08 | 83.91% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| DOGE-USD | ATOM-USD | 2023-09-08 | 82.88% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| DOGE-USD | MANA-USD | 2023-09-08 | 82.44% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -10.01% | -15.01% | 11.74% | -2.99% | -15.41% | 11.74% |
| SOL-USD | MKR-USD | 2018-12-24 | 88.63% | BEAR | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -29.36% | -36.47% | 0.00% | -7.04% | -36.47% | 0.00% |
| SOL-USD | HBAR-USD | 2023-09-10 | 87.86% | BEAR | RECOVERY | SAME_ASSET_ONLY | MIXED | -0.62% | -5.39% | 22.01% | 7.74% | -13.94% | 22.01% |
| SOL-USD | WAVES-USD | 2023-09-08 | 87.33% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 5.14% | 0.00% | 28.82% | -1.73% | -11.91% | 28.82% |
| SOL-USD | ZEC-USD | 2024-05-20 | 86.79% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.14% | -24.21% | 0.00% | -2.90% | -27.89% | 6.57% |
| SOL-USD | OP-USD | 2023-09-09 | 86.76% | BEAR | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 72.45% | 0.00% | 91.14% | 85.11% | 0.00% | 91.14% |
| SOL-USD | ETC-USD | 2023-09-08 | 86.20% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |

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

