# Market Regime Match Report

Generated: 2026-10-03 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-03 | RECOVERY | 84.612 $ | True | 33.15% | 0.80% | RECOVERY | 33.15% | 0.80% |
| DOGE-USD | 2026-10-03 | RECOVERY | 0.09315 $ | True | 19.83% | -6.12% | RECOVERY | 33.15% | 0.80% |
| SOL-USD | 2026-10-03 | RECOVERY | 119,53 $ | True | 46.80% | 0.77% | RECOVERY | 33.15% | 0.80% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 47.50% | -1.60% | 21.34% | 44.87% | -11.19% | -22.40% | 16.13% | 38.95% | 66.92% | 52.50% | 0.46% | 31.55% | 111.11% |
| BTC-USD | SAME_BTC_REGIME | 11 | 36.36% | -5.13% | 7.20% | 23.80% | -10.99% | -21.95% | 16.06% | 23.89% | 37.98% | 36.36% | -4.63% | 0.46% | 13.64% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | -0.94% | 14.07% | 23.08% | -22.29% | -34.37% | 24.11% | 33.24% | 38.72% | 50.00% | -5.08% | 12.32% | 22.76% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | -0.94% | 14.07% | 23.08% | -22.29% | -34.37% | 24.11% | 33.24% | 38.72% | 50.00% | -5.08% | 12.32% | 22.76% |
| DOGE-USD | ALL_MATCHES | 40 | 35.00% | -5.00% | 5.07% | 43.72% | -14.68% | -28.14% | 12.94% | 30.53% | 96.52% | 47.50% | -2.00% | 21.61% | 63.91% |
| DOGE-USD | SAME_BTC_REGIME | 10 | 30.00% | -5.24% | 4.16% | 25.29% | -11.04% | -22.61% | 18.03% | 28.63% | 36.33% | 40.00% | -4.11% | 6.08% | 16.28% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -0.62% | -0.62% | -0.62% | -5.39% | -5.39% | 22.01% | 22.01% | 22.01% | 100.00% | 7.74% | 7.74% | 7.74% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 40.00% | -3.36% | 10.02% | 39.15% | -13.07% | -26.07% | 18.03% | 29.17% | 81.86% | 45.00% | -1.53% | 31.55% | 107.01% |
| SOL-USD | SAME_BTC_REGIME | 13 | 46.15% | -1.65% | 6.09% | 28.03% | -8.66% | -14.71% | 23.99% | 30.24% | 40.17% | 46.15% | -0.88% | 8.08% | 26.50% |
| SOL-USD | SAME_ASSET_REGIME | 6 | 50.00% | 2.26% | 23.10% | 50.77% | -6.30% | -30.34% | 25.41% | 38.98% | 66.76% | 50.00% | 3.01% | 24.22% | 57.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 17.11% | 23.10% | 26.69% | -3.60% | -6.48% | 35.59% | 38.98% | 41.02% | 50.00% | 13.99% | 21.85% | 26.57% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 50.00% | 0.06% | -11.39% | 37.46% | 54.55% | 2.84% | 40.89% |
| BTC-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 5.29% | -4.69% | 109.40% | 80.00% | 124.16% | 473.81% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 6.03% | -13.82% | 40.79% | 50.00% | 115.88% | 217.02% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 11 | 36.36% | -5.13% | -10.99% | 23.89% | 36.36% | -4.63% | 23.89% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 32.00% | -6.97% | -17.65% | 22.01% | 44.00% | -2.68% | 35.89% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 75.00% | 25.79% | -7.72% | 130.50% | 75.00% | 100.25% | 228.13% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.72% | -8.72% | 52.83% | 100.00% | 14.96% | 52.83% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 10 | 30.00% | -5.24% | -11.04% | 28.63% | 40.00% | -4.11% | 28.63% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 31.58% | -7.24% | -16.04% | 21.67% | 36.84% | -7.04% | 32.74% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 42.86% | -10.44% | -17.08% | 59.32% | 57.14% | 37.07% | 196.46% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 25.20% | -11.23% | 25.20% | 100.00% | 238.16% | 274.03% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 46.15% | -1.65% | -8.66% | 30.24% | 46.15% | -0.88% | 30.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 35 | 45.71% | -1.89% | -11.23% | 36.93% | 48.57% | -1.33% | 39.92% |
| BTC-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 169.31% | 0.00% | 190.06% | 100.00% | 396.97% | 473.81% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 37.69% | -12.18% | 95.00% | 100.00% | 49.37% | 106.60% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -0.94% | -22.29% | 33.24% | 50.00% | -5.08% | 33.24% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 32.35% | -7.21% | -15.74% | 22.98% | 41.18% | -4.11% | 31.10% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 47.00% | 0.00% | 150.35% | 66.67% | 14.96% | 292.23% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 32.89% | -14.30% | 93.49% | 100.00% | 57.96% | 106.96% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -0.62% | -5.39% | 22.01% | 100.00% | 7.74% | 22.01% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 38.71% | -3.69% | -13.30% | 25.03% | 41.94% | -3.24% | 33.64% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -14.55% | -20.80% | 58.42% | 66.67% | 37.07% | 172.86% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 2.26% | -6.30% | 38.98% | 50.00% | 3.01% | 38.98% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 10 | 10 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_ASSET_REGIME | 2 | 6 | 13 | 6 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | EGLD-USD | 2023-09-08 | 88.53% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| BTC-USD | XTZ-USD | 2023-09-08 | 88.25% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| BTC-USD | ATOM-USD | 2023-09-08 | 87.98% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| BTC-USD | MANA-USD | 2023-09-03 | 87.66% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.13% | -12.85% | 14.59% | -4.63% | -13.25% | 14.59% |
| BTC-USD | EOS-USD | 2023-09-08 | 87.45% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| BTC-USD | ETC-USD | 2023-09-08 | 87.30% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |
| BTC-USD | OMG-USD | 2023-09-03 | 85.70% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 9.65% | -2.45% | 37.98% | -4.03% | -10.47% | 37.98% |
| BTC-USD | KAVA-USD | 2023-09-08 | 85.52% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| BTC-USD | NEO-USD | 2023-09-03 | 85.26% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 4.75% | -3.97% | 23.99% | 0.84% | -11.34% | 23.99% |
| BTC-USD | ETH-USD | 2019-03-18 | 85.17% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -30.97% | -37.39% | 5.86% | -39.87% | -41.71% | 5.86% |
| DOGE-USD | EGLD-USD | 2023-09-08 | 87.02% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| DOGE-USD | NEAR-USD | 2023-09-08 | 86.17% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | EOS-USD | 2023-09-08 | 85.33% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| DOGE-USD | DOT-USD | 2023-09-08 | 84.90% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 6.09% | -5.23% | 30.24% | 8.08% | -10.63% | 30.24% |
| DOGE-USD | XTZ-USD | 2023-09-08 | 84.47% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| DOGE-USD | KAVA-USD | 2023-09-08 | 84.19% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| DOGE-USD | LRC-USD | 2023-09-08 | 84.01% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| DOGE-USD | ATOM-USD | 2023-09-08 | 83.36% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| DOGE-USD | ADA-USD | 2023-09-08 | 83.00% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -13.08% | -18.67% | 4.77% | -4.99% | -23.23% | 4.77% |
| DOGE-USD | AVAX-USD | 2023-09-14 | 83.00% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -28.54% | -28.54% | 6.39% | -15.22% | -35.12% | 6.39% |
| SOL-USD | MKR-USD | 2018-12-24 | 87.94% | BEAR | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -29.36% | -36.47% | 0.00% | -7.04% | -36.47% | 0.00% |
| SOL-USD | OP-USD | 2023-09-09 | 87.36% | BEAR | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 72.45% | 0.00% | 91.14% | 85.11% | 0.00% | 91.14% |
| SOL-USD | WAVES-USD | 2023-09-08 | 87.35% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 5.14% | 0.00% | 28.82% | -1.73% | -11.91% | 28.82% |
| SOL-USD | ETC-USD | 2023-09-08 | 86.90% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |
| SOL-USD | HBAR-USD | 2023-09-10 | 86.72% | BEAR | RECOVERY | SAME_ASSET_ONLY | MIXED | -0.62% | -5.39% | 22.01% | 7.74% | -13.94% | 22.01% |
| SOL-USD | ZEC-USD | 2024-05-20 | 85.48% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.14% | -24.21% | 0.00% | -2.90% | -27.89% | 6.57% |

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

