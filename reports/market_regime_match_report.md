# Market Regime Match Report

Generated: 2026-09-05 08:21 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-05 | RECOVERY | 79.667 $ | True | 25.98% | -6.44% | RECOVERY | 25.98% | -6.44% |
| DOGE-USD | 2026-09-05 | BEAR | 0.08575 $ | False | -0.39% | -13.66% | RECOVERY | 25.98% | -6.44% |
| SOL-USD | 2026-09-05 | RECOVERY | 102,31 $ | True | 54.29% | -11.42% | RECOVERY | 25.98% | -6.44% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 82.50% | 13.03% | 35.72% | 62.68% | -11.71% | -28.63% | 21.00% | 46.09% | 82.03% | 80.00% | 18.22% | 39.70% | 93.83% |
| BTC-USD | SAME_BTC_REGIME | 3 | 66.67% | 34.95% | 37.08% | 38.36% | -19.15% | -20.35% | 34.95% | 40.97% | 44.58% | 100.00% | 71.29% | 95.96% | 110.76% |
| BTC-USD | SAME_ASSET_REGIME | 5 | 60.00% | 3.17% | 34.95% | 192.28% | -14.89% | -20.05% | 11.00% | 34.95% | 202.67% | 80.00% | 8.85% | 32.97% | 55.96% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 9.15% | 22.05% | 29.79% | -19.90% | -20.50% | 17.47% | 26.21% | 31.45% | 100.00% | 52.13% | 61.71% | 67.46% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -14.41% | 0.93% | 10.88% | -20.03% | -33.16% | 10.62% | 18.45% | 44.28% | 32.50% | -10.41% | 6.67% | 33.76% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -16.46% | -16.46% | -16.46% | -18.64% | -18.64% | 9.17% | 9.17% | 9.17% | 0.00% | -21.13% | -21.13% | -21.13% |
| DOGE-USD | SAME_ASSET_REGIME | 12 | 25.00% | -11.98% | -3.09% | 1.75% | -17.35% | -34.20% | 8.43% | 12.36% | 16.73% | 16.67% | -21.27% | -6.74% | 5.47% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -16.46% | -16.46% | -16.46% | -18.64% | -18.64% | 9.17% | 9.17% | 9.17% | 0.00% | -21.13% | -21.13% | -21.13% |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 15.91% | 47.65% | 100.44% | -12.84% | -40.33% | 26.02% | 58.47% | 112.75% | 67.50% | 26.34% | 93.21% | 185.43% |
| SOL-USD | SAME_BTC_REGIME | 2 | 50.00% | 41.26% | 70.22% | 87.60% | -13.78% | -18.08% | 60.66% | 90.99% | 109.19% | 100.00% | 74.80% | 95.71% | 108.26% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 21.27% | 38.18% | 40.84% | -9.58% | -19.79% | 38.14% | 40.97% | 43.45% | 100.00% | 45.40% | 65.73% | 79.96% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -16.66% | -16.66% | -16.66% | -19.15% | -19.15% | 0.00% | 0.00% | 0.00% | 100.00% | 32.97% | 32.97% | 32.97% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 7 | 71.43% | 11.75% | -19.30% | 46.94% | 71.43% | 11.36% | 54.56% |
| BTC-USD | HISTORICAL_BTC_BULL | 30 | 86.67% | 13.03% | -10.00% | 44.86% | 80.00% | 17.38% | 76.60% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 66.67% | 34.95% | -19.15% | 40.97% | 100.00% | 71.29% | 99.67% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 13 | 23.08% | -16.19% | -23.58% | 16.82% | 15.38% | -21.40% | 17.76% |
| DOGE-USD | HISTORICAL_BTC_BULL | 20 | 40.00% | -2.96% | -18.19% | 22.16% | 45.00% | -4.33% | 45.81% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 6 | 16.67% | -20.76% | -30.13% | 21.85% | 33.33% | -3.88% | 21.85% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -16.46% | -18.64% | 9.17% | 0.00% | -21.13% | 9.17% |
| SOL-USD | HISTORICAL_BTC_BEAR | 15 | 60.00% | 22.36% | -13.77% | 49.98% | 60.00% | 27.52% | 98.07% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 88.24% | 39.80% | -9.91% | 81.01% | 88.24% | 30.42% | 185.86% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 6 | 16.67% | -19.55% | -21.40% | 31.12% | 16.67% | -15.73% | 31.76% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 41.26% | -13.78% | 90.99% | 100.00% | 74.80% | 117.56% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 86.21% | 13.56% | -10.70% | 45.80% | 82.76% | 18.05% | 66.45% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 12.19% | -14.99% | 50.31% | 66.67% | 100.34% | 172.07% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 3.17% | -14.89% | 34.95% | 80.00% | 8.85% | 71.29% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 12 | 25.00% | -11.98% | -17.35% | 12.36% | 16.67% | -21.27% | 18.14% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 24 | 33.33% | -14.41% | -21.14% | 26.34% | 37.50% | -7.68% | 40.83% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -23.58% | -23.58% | 33.50% | 66.67% | 6.81% | 33.50% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -31.12% | -33.14% | 0.00% | 0.00% | -53.85% | 0.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 60.71% | 13.97% | -11.16% | 53.08% | 60.71% | 19.36% | 84.56% |
| SOL-USD | HISTORICAL_ASSET_BULL | 8 | 75.00% | 62.23% | -16.62% | 205.02% | 75.00% | 94.85% | 205.02% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 21.27% | -9.58% | 40.97% | 100.00% | 45.40% | 78.01% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_ASSET_REGIME | 2 | 5 | 3 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 12 | 1 | 12 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 1 | 4 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING BTC-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | DASH-USD | 2020-08-29 | 85.69% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.81% | -14.89% | 7.15% | 8.85% | -14.89% | 45.20% |
| BTC-USD | UNI-USD | 2023-04-02 | 83.61% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 297.17% | -2.12% | 314.49% | -44.88% | -54.06% | 314.49% |
| BTC-USD | LRC-USD | 2020-03-07 | 83.09% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 34.95% | -20.65% | 34.95% | 71.29% | -20.65% | 71.29% |
| BTC-USD | WAVES-USD | 2023-08-09 | 82.37% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.17% | -14.77% | 11.00% | 8.47% | -14.77% | 32.90% |
| BTC-USD | MKR-USD | 2020-03-08 | 82.19% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -16.66% | -19.15% | 0.00% | 32.97% | -19.26% | 45.21% |
| DOGE-USD | YFI-USD | 2022-05-05 | 84.71% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -11.73% | -26.53% | 0.00% | -32.16% | -32.16% | 0.00% |
| DOGE-USD | INJ-USD | 2022-05-18 | 83.94% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -7.49% | -18.36% | 4.84% | 6.62% | -18.36% | 17.76% |
| DOGE-USD | ETH-USD | 2025-02-14 | 83.26% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -4.30% | -11.95% | 11.18% | 43.43% | -11.95% | 48.71% |
| DOGE-USD | ALGO-USD | 2026-01-09 | 82.31% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 1.88% | -4.85% | 24.89% | -7.35% | -18.72% | 24.89% |
| DOGE-USD | FIL-USD | 2022-05-05 | 82.31% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -26.85% | -35.95% | 0.00% | -41.41% | -41.41% | 0.00% |
| DOGE-USD | THETA-USD | 2026-01-24 | 82.23% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.19% | -16.19% | 15.89% | -36.50% | -40.39% | 15.89% |
| DOGE-USD | MATIC-USD | 2022-04-21 | 81.12% | RECOVERY | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.46% | -18.64% | 9.17% | -21.13% | -24.98% | 9.17% |
| DOGE-USD | KAVA-USD | 2023-08-09 | 80.73% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 2.77% | -11.52% | 11.12% | -4.89% | -11.52% | 19.28% |
| DOGE-USD | MANA-USD | 2022-10-23 | 80.70% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -12.23% | -16.35% | 7.70% | -21.40% | -30.92% | 7.70% |
| DOGE-USD | NEAR-USD | 2022-10-23 | 79.34% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 0.56% | -5.20% | 16.82% | -13.69% | -22.51% | 16.82% |

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

