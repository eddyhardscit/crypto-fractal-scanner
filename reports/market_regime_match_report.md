# Market Regime Match Report

Generated: 2026-08-31 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-08-31 | RECOVERY | 77.995 $ | True | 16.93% | -7.67% | RECOVERY | 16.93% | -7.67% |
| DOGE-USD | 2026-08-31 | BEAR | 0.08286 $ | False | -10.50% | -14.22% | RECOVERY | 16.93% | -7.67% |
| SOL-USD | 2026-08-31 | RECOVERY | 102,67 $ | True | 38.48% | -13.14% | RECOVERY | 16.93% | -7.67% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 4.49% | 21.09% | 43.62% | -12.49% | -34.10% | 13.83% | 27.51% | 54.77% | 62.50% | 12.81% | 31.55% | 92.39% |
| BTC-USD | SAME_BTC_REGIME | 3 | 100.00% | 43.43% | 56.69% | 64.65% | -1.56% | -13.97% | 44.84% | 59.32% | 68.02% | 100.00% | 90.52% | 102.16% | 109.14% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 3.29% | 3.86% | 4.21% | -14.92% | -16.64% | 17.09% | 18.84% | 19.88% | 100.00% | 32.90% | 41.60% | 46.81% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 4.44% | 4.44% | 4.44% | -17.07% | -17.07% | 20.58% | 20.58% | 20.58% | 100.00% | 50.29% | 50.29% | 50.29% |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -4.58% | 21.03% | 42.28% | -11.99% | -36.07% | 20.61% | 31.69% | 66.06% | 37.50% | -7.86% | 21.68% | 71.11% |
| DOGE-USD | SAME_BTC_REGIME | 2 | 50.00% | 5.95% | 18.94% | 26.73% | -11.87% | -21.37% | 33.10% | 44.96% | 52.08% | 0.00% | -15.32% | -8.29% | -4.08% |
| DOGE-USD | SAME_ASSET_REGIME | 11 | 36.36% | -13.38% | 14.20% | 31.93% | -25.90% | -36.15% | 2.40% | 24.25% | 48.58% | 18.18% | -28.14% | -7.23% | 43.54% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 31.93% | 31.93% | 31.93% | 0.00% | 0.00% | 56.82% | 56.82% | 56.82% | 0.00% | -1.27% | -1.27% | -1.27% |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 4.49% | 47.36% | 101.88% | -13.61% | -33.25% | 21.81% | 53.27% | 150.32% | 67.50% | 29.06% | 85.56% | 166.61% |
| SOL-USD | SAME_BTC_REGIME | 5 | 80.00% | 69.95% | 98.37% | 119.45% | -2.96% | -27.01% | 73.81% | 98.37% | 131.57% | 80.00% | 113.80% | 158.76% | 248.68% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 100.00% | 3.29% | 3.86% | 4.21% | -14.92% | -16.64% | 17.09% | 18.84% | 19.88% | 100.00% | 32.90% | 41.60% | 46.81% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 4.44% | 4.44% | 4.44% | -17.07% | -17.07% | 20.58% | 20.58% | 20.58% | 100.00% | 50.29% | 50.29% | 50.29% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 5 | 20.00% | -43.47% | -43.47% | 26.12% | 20.00% | -33.56% | 26.12% |
| BTC-USD | HISTORICAL_BTC_BULL | 26 | 65.38% | 2.77% | -11.33% | 17.81% | 65.38% | 12.10% | 57.58% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 6 | 100.00% | 21.89% | -13.99% | 36.47% | 66.67% | 15.76% | 61.55% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 43.43% | -1.56% | 59.32% | 100.00% | 90.52% | 115.30% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 6 | 33.33% | -9.50% | -20.33% | 14.84% | 16.67% | -21.36% | 15.42% |
| DOGE-USD | HISTORICAL_BTC_BULL | 32 | 37.50% | -2.88% | -9.33% | 31.69% | 43.75% | -4.48% | 65.50% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 5.95% | -11.87% | 44.96% | 0.00% | -15.32% | 44.96% |
| SOL-USD | HISTORICAL_BTC_BEAR | 11 | 36.36% | -12.67% | -19.42% | 30.95% | 36.36% | -10.81% | 58.55% |
| SOL-USD | HISTORICAL_BTC_BULL | 24 | 79.17% | 8.92% | -13.38% | 53.27% | 79.17% | 29.96% | 117.85% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 5 | 80.00% | 69.95% | -2.96% | 98.37% | 80.00% | 113.80% | 174.79% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 67.74% | 4.53% | -11.06% | 28.89% | 54.84% | 3.28% | 57.26% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 16.29% | -12.41% | 23.30% | 80.00% | 76.15% | 143.52% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 38.08% | -33.05% | 38.08% | 100.00% | 18.27% | 38.08% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -8.04% | -17.72% | 6.58% | 100.00% | 22.51% | 44.07% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 3.29% | -14.92% | 18.84% | 100.00% | 32.90% | 46.92% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 11 | 36.36% | -13.38% | -25.90% | 24.25% | 18.18% | -28.14% | 36.56% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 27 | 40.74% | -1.56% | -7.75% | 43.58% | 48.15% | -4.15% | 77.38% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -14.05% | -19.59% | 8.58% | 0.00% | -17.36% | 12.86% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 26 | 65.38% | 3.94% | -13.13% | 42.10% | 57.69% | 8.77% | 66.62% |
| SOL-USD | HISTORICAL_ASSET_BULL | 9 | 77.78% | 87.36% | -17.42% | 182.90% | 88.89% | 130.34% | 235.51% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 98.37% | -0.47% | 98.37% | 100.00% | 158.76% | 174.79% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -20.22% | -25.68% | 4.94% | 50.00% | 5.98% | 33.05% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 3.29% | -14.92% | 18.84% | 100.00% | 32.90% | 46.92% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 1 | 2 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 11 | 2 | 11 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | SAME_BTC_REGIME | 1 | 2 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | FIL-USD | 2022-04-30 | 87.30% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.15% | -36.15% | 0.00% | -37.52% | -40.20% | 0.00% |
| DOGE-USD | MATIC-USD | 2022-04-16 | 84.66% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -5.61% | -12.38% | 16.29% | -14.57% | -20.09% | 16.29% |
| DOGE-USD | YFI-USD | 2022-04-30 | 84.61% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -24.38% | -25.90% | 0.85% | -28.14% | -30.98% | 0.85% |
| DOGE-USD | EGLD-USD | 2023-07-25 | 83.71% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 40.51% | 0.00% | 48.58% | 110.79% | 0.00% | 126.47% |
| DOGE-USD | NEAR-USD | 2022-05-06 | 81.98% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -13.38% | -36.06% | 0.00% | -46.25% | -46.25% | 0.00% |
| DOGE-USD | KSM-USD | 2021-12-25 | 81.80% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.71% | -36.71% | 0.00% | -63.53% | -67.03% | 0.00% |
| DOGE-USD | DOT-USD | 2023-08-04 | 81.59% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 20.77% | -11.95% | 32.21% | 43.54% | -11.95% | 66.19% |
| DOGE-USD | EOS-USD | 2021-12-22 | 81.44% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.56% | -28.56% | 2.40% | -50.86% | -57.12% | 2.40% |
| DOGE-USD | NEAR-USD | 2022-10-13 | 81.21% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 7.62% | -8.46% | 10.47% | -13.19% | -25.18% | 12.80% |
| DOGE-USD | EOS-USD | 2022-04-26 | 80.90% | RECOVERY | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 31.93% | 0.00% | 56.82% | -1.27% | -2.15% | 56.82% |
| SOL-USD | VET-USD | 2020-02-28 | 82.13% | RECOVERY | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 98.37% | -0.47% | 98.37% | 158.76% | -0.47% | 174.79% |
| SOL-USD | LRC-USD | 2020-03-02 | 78.48% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 4.44% | -17.07% | 20.58% | 50.29% | -17.07% | 50.55% |
| SOL-USD | BNB-USD | 2018-11-08 | 78.29% | RECOVERY | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 69.95% | -1.56% | 73.81% | 113.80% | -1.56% | 113.80% |
| SOL-USD | MKR-USD | 2020-03-03 | 75.65% | RECOVERY | MIXED | SAME_BTC_ONLY | BEARISH_30D | -32.40% | -33.64% | 0.00% | -10.55% | -33.73% | 0.00% |
| SOL-USD | RUNE-USD | 2020-03-03 | 75.39% | RECOVERY | BULL | SAME_BTC_ONLY | EXPLOSIVE_60D | 133.50% | -2.96% | 153.70% | 308.62% | -2.96% | 308.62% |

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

