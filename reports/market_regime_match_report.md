# Market Regime Match Report

Generated: 2026-09-09 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-09 | RECOVERY | 79.123 $ | True | 24.48% | -5.56% | RECOVERY | 24.48% | -5.56% |
| DOGE-USD | 2026-09-09 | MIXED | 0.09043 $ | True | 5.18% | -12.77% | RECOVERY | 24.48% | -5.56% |
| SOL-USD | 2026-09-09 | RECOVERY | 104,43 $ | True | 56.28% | -10.14% | RECOVERY | 24.48% | -5.56% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 20.27% | 42.90% | 78.68% | -8.20% | -39.04% | 29.28% | 55.69% | 111.40% | 80.00% | 18.79% | 44.50% | 93.74% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 5 | 60.00% | 3.09% | 36.70% | 40.25% | -14.89% | -36.96% | 36.70% | 45.11% | 207.62% | 80.00% | 8.85% | 25.17% | 63.73% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -8.47% | 9.89% | 32.92% | -17.22% | -33.55% | 14.67% | 25.06% | 41.67% | 37.50% | -7.01% | 11.42% | 43.96% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 17.40% | 58.32% | 113.47% | -9.25% | -42.28% | 36.97% | 71.78% | 149.39% | 62.50% | 19.45% | 96.24% | 207.38% |
| SOL-USD | SAME_BTC_REGIME | 1 | 100.00% | 99.18% | 99.18% | 99.18% | -8.40% | -8.40% | 121.32% | 121.32% | 121.32% | 100.00% | 116.63% | 116.63% | 116.63% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 39.66% | 81.40% | 151.20% | -13.26% | -39.78% | 180.53% | 321.36% | 331.09% | 75.00% | 57.31% | 116.05% | 163.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 71.43% | 29.40% | -17.90% | 63.27% | 71.43% | 44.79% | 106.16% |
| BTC-USD | HISTORICAL_BTC_BULL | 26 | 84.62% | 18.56% | -5.42% | 50.90% | 84.62% | 18.22% | 67.83% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 19 | 21.05% | -19.36% | -23.58% | 20.43% | 15.79% | -13.10% | 21.32% |
| DOGE-USD | HISTORICAL_BTC_BULL | 12 | 66.67% | 7.11% | -8.95% | 42.88% | 66.67% | 10.60% | 86.74% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 8 | 37.50% | -10.82% | -20.15% | 27.82% | 50.00% | -1.15% | 41.17% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 50.00% | 0.63% | -19.30% | 47.26% | 50.00% | 0.39% | 73.78% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 82.35% | 46.20% | -2.19% | 145.34% | 82.35% | 31.36% | 315.96% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -7.27% | -19.74% | 17.02% | 0.00% | -5.17% | 18.93% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 100.00% | 99.18% | -8.40% | 121.32% | 100.00% | 116.63% | 141.68% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 86.21% | 20.77% | -4.97% | 52.49% | 86.21% | 19.19% | 69.58% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.49% | -7.66% | 89.19% | 40.00% | -4.71% | 179.49% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 91.00% | -16.34% | 125.42% | 100.00% | 162.43% | 162.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 3.09% | -14.89% | 45.11% | 80.00% | 8.85% | 103.03% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 19 | 36.84% | -7.43% | -15.36% | 19.09% | 31.58% | -13.69% | 36.99% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 18 | 38.89% | -15.95% | -24.22% | 29.76% | 44.44% | -3.05% | 44.61% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -6.73% | -12.50% | 36.07% | 50.00% | 8.14% | 36.07% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -16.58% | -20.55% | 0.00% | 0.00% | -11.78% | 0.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 63.33% | 15.56% | -7.49% | 61.05% | 63.33% | 16.10% | 81.74% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 50.13% | -17.28% | 150.55% | 50.00% | 68.33% | 240.52% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 40.65% | -19.07% | 96.88% | 50.00% | 76.43% | 124.64% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 39.66% | -13.26% | 321.36% | 75.00% | 57.31% | 321.36% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_ASSET_REGIME | 0 | 5 | 0 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| DOGE-USD | NONE | 0 | 0 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 0 | 4 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING BTC-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | UNI-USD | 2023-04-07 | 88.00% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | -47.87% | -48.23% | 315.96% | -44.33% | -53.90% | 315.96% |
| BTC-USD | LRC-USD | 2020-03-12 | 85.00% | BEAR | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 42.62% | -20.06% | 45.11% | 89.45% | -20.06% | 103.03% |
| BTC-USD | QTUM-USD | 2023-08-09 | 84.64% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.09% | -5.87% | 12.60% | 0.39% | -5.87% | 20.46% |
| BTC-USD | WAVES-USD | 2023-08-14 | 84.26% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 36.70% | 0.00% | 36.70% | 25.17% | 0.00% | 55.93% |
| BTC-USD | DASH-USD | 2020-08-29 | 83.61% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.81% | -14.89% | 7.15% | 8.85% | -14.89% | 45.20% |

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

