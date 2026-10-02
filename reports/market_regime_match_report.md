# Market Regime Match Report

Generated: 2026-10-02 14:07 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-02 | RECOVERY | 86.839 $ | True | 37.65% | 0.59% | RECOVERY | 37.65% | 0.59% |
| DOGE-USD | 2026-10-02 | RECOVERY | 0.09707 $ | True | 25.11% | -6.44% | RECOVERY | 37.65% | 0.59% |
| SOL-USD | 2026-10-02 | RECOVERY | 122,43 $ | True | 49.95% | 0.37% | RECOVERY | 37.65% | 0.59% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 52.50% | 2.84% | 17.75% | 45.06% | -11.09% | -22.40% | 18.10% | 38.95% | 92.57% | 57.50% | 3.39% | 34.50% | 88.14% |
| BTC-USD | SAME_BTC_REGIME | 12 | 50.00% | 0.86% | 14.82% | 28.56% | -9.57% | -21.27% | 21.90% | 36.53% | 41.93% | 50.00% | -1.98% | 12.29% | 28.11% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | -0.94% | 14.07% | 23.08% | -22.29% | -34.37% | 24.11% | 33.24% | 38.72% | 50.00% | -5.08% | 12.32% | 22.76% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | -0.94% | 14.07% | 23.08% | -22.29% | -34.37% | 24.11% | 33.24% | 38.72% | 50.00% | -5.08% | 12.32% | 22.76% |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -4.21% | 7.17% | 48.34% | -14.75% | -35.17% | 12.66% | 25.46% | 96.52% | 45.00% | -2.80% | 17.33% | 107.93% |
| DOGE-USD | SAME_BTC_REGIME | 9 | 33.33% | -7.45% | 6.09% | 31.11% | -12.83% | -23.27% | 16.06% | 23.80% | 42.65% | 44.44% | -4.99% | 8.08% | 17.64% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 100.00% | 253.00% | 377.40% | 452.04% | -1.05% | -1.90% | 466.78% | 687.04% | 819.20% | 100.00% | 491.31% | 736.01% | 882.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 35.00% | -6.09% | 6.79% | 30.51% | -12.23% | -28.18% | 15.04% | 26.91% | 71.32% | 45.00% | -1.51% | 16.51% | 84.23% |
| SOL-USD | SAME_BTC_REGIME | 12 | 66.67% | 5.62% | 15.16% | 28.56% | -6.21% | -14.95% | 26.40% | 39.77% | 66.44% | 50.00% | -0.07% | 9.47% | 28.11% |
| SOL-USD | SAME_ASSET_REGIME | 6 | 50.00% | 2.26% | 23.10% | 50.77% | -6.30% | -33.31% | 25.41% | 38.98% | 66.76% | 66.67% | 5.48% | 24.22% | 57.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 17.11% | 23.10% | 26.69% | -3.60% | -6.48% | 35.59% | 38.98% | 41.02% | 50.00% | 13.99% | 21.85% | 26.57% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 20 | 55.00% | 2.84% | -9.83% | 36.41% | 60.00% | 5.86% | 48.04% |
| BTC-USD | HISTORICAL_BTC_BULL | 6 | 50.00% | 1.70% | -8.69% | 94.30% | 66.67% | 80.62% | 412.00% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 6.03% | -13.82% | 40.79% | 50.00% | 115.88% | 217.02% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 12 | 50.00% | 0.86% | -9.57% | 36.53% | 50.00% | -1.98% | 36.53% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 24 | 29.17% | -11.05% | -22.39% | 17.75% | 37.50% | -4.49% | 29.99% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 24.33% | -0.87% | 170.21% | 66.67% | 54.54% | 386.64% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 25.20% | -11.23% | 25.20% | 100.00% | 238.16% | 274.03% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 9 | 33.33% | -7.45% | -12.83% | 23.80% | 44.44% | -4.99% | 23.80% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 21.05% | -6.21% | -16.04% | 22.72% | 36.84% | -6.05% | 27.83% |
| SOL-USD | HISTORICAL_BTC_BULL | 8 | 12.50% | -12.87% | -23.77% | 8.32% | 50.00% | 1.25% | 76.26% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 25.20% | -11.23% | 25.20% | 100.00% | 238.16% | 274.03% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 66.67% | 5.62% | -6.21% | 39.77% | 50.00% | -0.07% | 39.77% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 51.52% | 1.45% | -11.14% | 37.98% | 54.55% | 0.84% | 45.99% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 11.83% | -3.22% | 113.06% | 66.67% | 11.84% | 254.93% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 37.69% | -12.18% | 95.00% | 100.00% | 49.37% | 106.60% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -0.94% | -22.29% | 33.24% | 50.00% | -5.08% | 33.24% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 30.56% | -8.36% | -15.71% | 20.89% | 41.67% | -3.96% | 30.63% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 108.16% | 0.00% | 170.21% | 50.00% | 189.64% | 383.02% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 253.00% | -1.05% | 687.04% | 100.00% | 491.31% | 1194.24% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 32.14% | -6.09% | -12.23% | 24.29% | 35.71% | -6.01% | 29.60% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | -1.15% | -13.37% | 55.34% | 50.00% | 62.42% | 127.14% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 25.00% | -15.11% | -24.88% | 32.42% | 75.00% | 24.63% | 112.86% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 2.26% | -6.30% | 38.98% | 66.67% | 5.48% | 38.98% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 12 | 12 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_ASSET_REGIME | 2 | 6 | 12 | 6 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | EGLD-USD | 2023-09-08 | 88.02% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| BTC-USD | MANA-USD | 2023-09-03 | 87.75% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.13% | -12.85% | 14.59% | -4.63% | -13.25% | 14.59% |
| BTC-USD | ATOM-USD | 2023-09-08 | 87.54% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| BTC-USD | XTZ-USD | 2023-09-08 | 87.46% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| BTC-USD | ETC-USD | 2023-09-08 | 87.30% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |
| BTC-USD | EOS-USD | 2023-09-08 | 86.77% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| BTC-USD | OMG-USD | 2023-09-03 | 86.54% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 9.65% | -2.45% | 37.98% | -4.03% | -10.47% | 37.98% |
| BTC-USD | ETH-USD | 2019-03-18 | 86.28% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -30.97% | -37.39% | 5.86% | -39.87% | -41.71% | 5.86% |
| BTC-USD | XRP-USD | 2023-09-03 | 86.15% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.26% | -11.04% | 4.21% | -15.19% | -18.87% | 4.21% |
| BTC-USD | NEO-USD | 2023-09-03 | 85.54% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 4.75% | -3.97% | 23.99% | 0.84% | -11.34% | 23.99% |
| DOGE-USD | EGLD-USD | 2023-09-08 | 86.94% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| DOGE-USD | DOT-USD | 2023-09-08 | 85.28% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 6.09% | -5.23% | 30.24% | 8.08% | -10.63% | 30.24% |
| DOGE-USD | NEAR-USD | 2023-09-03 | 84.95% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| DOGE-USD | EOS-USD | 2023-09-08 | 84.57% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| DOGE-USD | AVAX-USD | 2023-09-14 | 83.83% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -28.54% | -28.54% | 6.39% | -15.22% | -35.12% | 6.39% |
| DOGE-USD | XTZ-USD | 2023-09-08 | 83.66% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| DOGE-USD | ADA-USD | 2023-09-08 | 83.65% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -13.08% | -18.67% | 4.77% | -4.99% | -23.23% | 4.77% |
| DOGE-USD | ATOM-USD | 2023-09-08 | 83.50% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| DOGE-USD | KAVA-USD | 2023-09-08 | 83.39% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| SOL-USD | OP-USD | 2023-09-09 | 87.48% | BEAR | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 72.45% | 0.00% | 91.14% | 85.11% | 0.00% | 91.14% |
| SOL-USD | ZEC-USD | 2024-05-15 | 87.23% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -24.53% | -34.91% | 3.85% | -9.70% | -38.07% | 3.85% |
| SOL-USD | WAVES-USD | 2023-09-08 | 86.88% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 5.14% | 0.00% | 28.82% | -1.73% | -11.91% | 28.82% |
| SOL-USD | MKR-USD | 2018-12-19 | 86.54% | BEAR | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -28.88% | -31.71% | 7.49% | 3.23% | -31.71% | 7.49% |
| SOL-USD | ETC-USD | 2023-09-08 | 86.28% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |
| SOL-USD | HBAR-USD | 2023-09-10 | 85.99% | BEAR | RECOVERY | SAME_ASSET_ONLY | MIXED | -0.62% | -5.39% | 22.01% | 7.74% | -13.94% | 22.01% |

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

