# Market Regime Match Report

Generated: 2026-09-02 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-02 | RECOVERY | 77.667 $ | True | 21.73% | -7.16% | RECOVERY | 21.73% | -7.16% |
| DOGE-USD | 2026-09-02 | BEAR | 0.08188 $ | False | -7.35% | -13.93% | RECOVERY | 21.73% | -7.16% |
| SOL-USD | 2026-09-02 | RECOVERY | 100,24 $ | True | 45.87% | -12.35% | RECOVERY | 21.73% | -7.16% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 7.19% | 20.28% | 39.29% | -12.92% | -33.71% | 15.48% | 26.12% | 52.57% | 67.50% | 11.04% | 36.38% | 90.22% |
| BTC-USD | SAME_BTC_REGIME | 4 | 75.00% | 33.98% | 38.29% | 38.85% | -8.33% | -27.50% | 43.89% | 60.87% | 85.86% | 75.00% | 60.81% | 95.28% | 110.49% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 16.58% | 23.28% | 27.30% | -9.13% | -13.64% | 56.76% | 79.64% | 93.37% | 100.00% | 21.63% | 28.21% | 32.15% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 29.98% | 29.98% | 29.98% | -3.49% | -3.49% | 102.52% | 102.52% | 102.52% | 100.00% | 34.79% | 34.79% | 34.79% |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -7.54% | 2.27% | 42.82% | -10.59% | -29.86% | 17.43% | 33.17% | 58.40% | 32.50% | -8.75% | 21.50% | 84.06% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -16.46% | -16.46% | -16.46% | -18.64% | -18.64% | 9.17% | 9.17% | 9.17% | 0.00% | -21.13% | -21.13% | -21.13% |
| DOGE-USD | SAME_ASSET_REGIME | 13 | 15.38% | -9.86% | -1.50% | 26.38% | -14.09% | -28.03% | 9.17% | 16.98% | 41.55% | 23.08% | -23.01% | -10.39% | 36.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -16.46% | -16.46% | -16.46% | -18.64% | -18.64% | 9.17% | 9.17% | 9.17% | 0.00% | -21.13% | -21.13% | -21.13% |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 6.71% | 41.41% | 102.20% | -12.59% | -38.27% | 25.74% | 52.07% | 113.79% | 67.50% | 23.69% | 74.76% | 133.42% |
| SOL-USD | SAME_BTC_REGIME | 3 | 100.00% | 39.22% | 74.14% | 95.10% | -13.17% | -19.16% | 46.99% | 86.33% | 109.93% | 100.00% | 120.62% | 131.30% | 137.70% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 100.00% | 19.06% | 27.01% | 31.77% | -17.71% | -20.06% | 22.97% | 28.96% | 32.55% | 100.00% | 39.88% | 55.58% | 65.01% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 34.95% | 34.95% | 34.95% | -20.65% | -20.65% | 34.95% | 34.95% | 34.95% | 100.00% | 71.29% | 71.29% | 71.29% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 5 | 20.00% | -24.87% | -33.21% | 27.42% | 40.00% | -22.48% | 29.58% |
| BTC-USD | HISTORICAL_BTC_BULL | 30 | 80.00% | 7.19% | -12.62% | 22.72% | 70.00% | 10.73% | 51.59% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 18.48% | -2.96% | 24.83% | 100.00% | 151.30% | 193.70% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 33.98% | -8.33% | 60.87% | 75.00% | 60.81% | 115.06% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 11 | 18.18% | -9.86% | -14.09% | 17.88% | 18.18% | -28.14% | 24.76% |
| DOGE-USD | HISTORICAL_BTC_BULL | 26 | 34.62% | -3.87% | -8.30% | 41.13% | 42.31% | -3.88% | 43.99% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -25.91% | -33.22% | 8.86% | 0.00% | -12.46% | 8.86% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -16.46% | -18.64% | 9.17% | 0.00% | -21.13% | 9.17% |
| SOL-USD | HISTORICAL_BTC_BEAR | 15 | 53.33% | 0.86% | -12.94% | 43.25% | 60.00% | 5.36% | 69.65% |
| SOL-USD | HISTORICAL_BTC_BULL | 20 | 80.00% | 9.75% | -10.83% | 61.29% | 75.00% | 31.38% | 120.23% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -27.96% | -32.00% | 18.27% | 0.00% | -31.96% | 18.27% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 39.22% | -13.17% | 86.33% | 100.00% | 120.62% | 137.23% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 28 | 75.00% | 7.19% | -13.19% | 30.76% | 64.29% | 10.73% | 54.93% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 10.93% | -12.56% | 21.74% | 71.43% | 28.07% | 119.17% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.48% | -2.96% | 24.83% | 100.00% | 151.30% | 193.70% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -20.22% | -25.68% | 4.94% | 50.00% | 5.98% | 33.05% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 16.58% | -9.13% | 79.64% | 100.00% | 21.63% | 85.12% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 13 | 15.38% | -9.86% | -14.09% | 16.98% | 23.08% | -23.01% | 30.74% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 25 | 32.00% | -5.12% | -8.92% | 36.57% | 36.00% | -3.99% | 43.45% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 125.28% | 0.00% | 128.29% | 100.00% | 81.09% | 149.46% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -8.06% | -15.42% | 6.21% | 0.00% | -5.35% | 14.02% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 62.07% | 2.91% | -12.19% | 46.99% | 62.07% | 11.31% | 68.64% |
| SOL-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 16.29% | -12.56% | 139.71% | 71.43% | 85.18% | 155.24% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 105.25% | -12.68% | 119.61% | 100.00% | 130.65% | 217.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 19.06% | -17.71% | 28.96% | 100.00% | 39.88% | 61.69% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 1 | 2 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 13 | 1 | 13 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 1 | 2 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | FIL-USD | 2022-05-05 | 85.28% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -26.85% | -35.95% | 0.00% | -41.41% | -41.41% | 0.00% |
| DOGE-USD | YFI-USD | 2022-04-30 | 84.49% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -24.38% | -25.90% | 0.85% | -28.14% | -30.98% | 0.85% |
| DOGE-USD | QTUM-USD | 2022-05-01 | 82.69% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -25.68% | -28.31% | 2.87% | -32.52% | -33.72% | 2.87% |
| DOGE-USD | MATIC-USD | 2022-04-21 | 82.26% | RECOVERY | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.46% | -18.64% | 9.17% | -21.13% | -24.98% | 9.17% |
| DOGE-USD | THETA-USD | 2026-01-19 | 82.20% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -11.37% | -11.37% | 18.77% | -37.22% | -37.22% | 18.77% |
| DOGE-USD | ETH-USD | 2025-02-09 | 82.12% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -0.19% | -4.46% | 11.24% | 40.32% | -11.90% | 40.32% |
| DOGE-USD | EGLD-USD | 2023-07-25 | 82.04% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 40.51% | 0.00% | 48.58% | 110.79% | 0.00% | 126.47% |
| DOGE-USD | INJ-USD | 2022-05-13 | 81.80% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -1.50% | -9.36% | 16.40% | 23.27% | -9.36% | 30.74% |
| DOGE-USD | EOS-USD | 2022-05-01 | 81.34% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 33.02% | -5.84% | 47.24% | -10.39% | -10.39% | 47.24% |
| DOGE-USD | MANA-USD | 2022-10-18 | 81.05% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -3.09% | -6.46% | 16.98% | -14.29% | -24.97% | 16.98% |

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

