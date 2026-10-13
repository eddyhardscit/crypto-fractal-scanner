# Market Regime Match Report

Generated: 2026-10-13 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-13 | BULL | 83.631 $ | True | 29.24% | 3.67% | BULL | 29.24% | 3.67% |
| DOGE-USD | 2026-10-13 | RECOVERY | 0.08469 $ | False | 14.38% | -3.48% | BULL | 29.24% | 3.67% |
| SOL-USD | 2026-10-13 | BULL | 108,21 $ | True | 40.05% | 5.62% | BULL | 29.24% | 3.67% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 55.00% | 1.66% | 11.31% | 29.76% | -10.18% | -22.53% | 13.51% | 22.46% | 40.04% | 45.00% | -0.88% | 23.00% | 49.18% |
| BTC-USD | SAME_BTC_REGIME | 5 | 80.00% | 5.55% | 11.63% | 29.01% | -10.18% | -22.59% | 13.11% | 13.66% | 34.33% | 40.00% | -11.19% | 97.72% | 192.15% |
| BTC-USD | SAME_ASSET_REGIME | 3 | 66.67% | 5.37% | 17.18% | 24.27% | -8.79% | -18.50% | 19.73% | 27.38% | 31.97% | 66.67% | 6.79% | 22.76% | 32.34% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |
| DOGE-USD | ALL_MATCHES | 40 | 80.00% | 13.08% | 21.22% | 35.15% | -6.37% | -25.24% | 19.93% | 31.41% | 43.07% | 52.50% | 1.14% | 18.75% | 49.11% |
| DOGE-USD | SAME_BTC_REGIME | 6 | 66.67% | 4.34% | 6.38% | 50.98% | -14.07% | -22.23% | 10.04% | 13.49% | 59.19% | 50.00% | 5.45% | 93.71% | 197.79% |
| DOGE-USD | SAME_ASSET_REGIME | 3 | 66.67% | 6.52% | 16.37% | 22.28% | -6.80% | -43.51% | 13.61% | 37.43% | 51.72% | 33.33% | -21.43% | 15.97% | 38.42% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 6.52% | 6.52% | 6.52% | -6.80% | -6.80% | 13.61% | 13.61% | 13.61% | 0.00% | -33.27% | -33.27% | -33.27% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 5.94% | 16.30% | 29.82% | -8.81% | -24.09% | 15.80% | 25.27% | 41.74% | 42.50% | -4.96% | 17.78% | 39.71% |
| SOL-USD | SAME_BTC_REGIME | 15 | 66.67% | 2.72% | 6.42% | 29.84% | -9.44% | -19.42% | 13.11% | 14.24% | 32.34% | 40.00% | -10.83% | 20.20% | 73.88% |
| SOL-USD | SAME_ASSET_REGIME | 5 | 60.00% | 1.42% | 5.37% | 19.54% | -8.79% | -19.42% | 5.09% | 19.73% | 28.91% | 60.00% | 6.79% | 15.36% | 29.38% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 33.33% | -4.58% | -1.58% | 0.22% | -16.72% | -20.31% | 4.61% | 4.85% | 4.99% | 33.33% | -12.12% | 1.62% | 9.87% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 25 | 64.00% | 5.37% | -9.73% | 24.60% | 52.00% | 0.65% | 42.82% |
| BTC-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 5.55% | -10.18% | 13.66% | 40.00% | -11.19% | 100.64% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 9 | 11.11% | -10.66% | -15.63% | 19.40% | 22.22% | -2.56% | 19.40% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 33 | 81.82% | 13.61% | -5.18% | 33.60% | 51.52% | 0.65% | 42.87% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 4.34% | -14.07% | 13.49% | 50.00% | 5.45% | 96.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 70.83% | 8.76% | -7.70% | 29.79% | 41.67% | -3.37% | 42.52% |
| SOL-USD | HISTORICAL_BTC_BULL | 15 | 66.67% | 2.72% | -9.44% | 14.24% | 40.00% | -10.83% | 41.46% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 36 | 55.56% | 1.66% | -10.58% | 22.46% | 44.44% | -0.88% | 41.38% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 5.37% | -8.79% | 27.38% | 66.67% | 6.79% | 49.97% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -2.61% | -6.73% | 16.86% | 0.00% | -2.56% | 16.86% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 84.38% | 13.91% | -5.27% | 31.41% | 50.00% | 0.06% | 42.83% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 5.37% | -8.79% | 27.38% | 100.00% | 15.36% | 49.97% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -0.40% | -19.60% | 6.71% | 50.00% | 57.69% | 96.76% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 6.52% | -6.80% | 37.43% | 33.33% | -21.43% | 52.87% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 77.78% | 9.33% | -7.77% | 27.90% | 40.74% | -5.46% | 42.62% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 1.42% | -8.79% | 19.73% | 60.00% | 6.79% | 43.59% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 25.00% | -7.81% | -12.57% | 15.58% | 50.00% | 10.29% | 36.88% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 41.98% | 0.00% | 41.98% | 100.00% | 11.39% | 52.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 0.85% | -10.34% | 11.45% | 0.00% | -21.43% | 11.45% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 3 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 1 | 3 | 6 | 6 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_ASSET_REGIME | 3 | 5 | 15 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-06-26 | 88.13% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| BTC-USD | MKR-USD | 2020-11-18 | 85.76% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| BTC-USD | XLM-USD | 2025-05-25 | 85.68% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| BTC-USD | LRC-USD | 2020-11-17 | 85.41% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| BTC-USD | HBAR-USD | 2025-05-27 | 84.03% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| DOGE-USD | MKR-USD | 2020-11-23 | 84.20% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| DOGE-USD | LINK-USD | 2019-08-20 | 83.64% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| DOGE-USD | ADA-USD | 2025-05-30 | 83.23% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| DOGE-USD | HBAR-USD | 2025-05-27 | 82.96% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| DOGE-USD | RUNE-USD | 2023-07-01 | 81.80% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| DOGE-USD | LRC-USD | 2020-11-22 | 81.55% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| SOL-USD | ETH-USD | 2021-06-15 | 86.89% | BEAR | BULL | SAME_ASSET_ONLY | BULLISH_30D | 28.99% | -8.79% | 35.03% | 38.72% | -8.79% | 56.34% |
| SOL-USD | TRX-USD | 2025-05-25 | 86.50% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 1.42% | -6.58% | 4.61% | -12.12% | -13.20% | 4.61% |
| SOL-USD | LINK-USD | 2019-08-20 | 86.34% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| SOL-USD | DOGE-USD | 2024-01-11 | 86.13% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -4.58% | -16.72% | 4.20% | -21.74% | -21.74% | 11.32% |
| SOL-USD | TRX-USD | 2021-06-20 | 85.67% | BEAR | BULL | SAME_ASSET_ONLY | MIXED | 5.37% | -3.41% | 19.73% | 6.79% | -3.41% | 43.59% |

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

