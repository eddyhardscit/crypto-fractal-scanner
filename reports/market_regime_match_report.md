# Market Regime Match Report

Generated: 2026-08-26 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | MIXED | 78.978 $ | True | 7.54% | -8.85% | MIXED | 7.54% | -8.85% |
| DOGE-USD | BEAR | 0.08660 $ | False | -12.75% | -15.37% | MIXED | 7.54% | -8.85% |
| SOL-USD | RECOVERY | 96,77 $ | True | 18.19% | -14.84% | MIXED | 7.54% | -8.85% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 10.94% | 19.00% | 40.41% | -8.67% | -19.06% | 17.05% | 27.57% | 44.80% | 67.50% | 14.78% | 49.95% | 73.07% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -1.72% | -1.72% | -1.72% | -7.24% | -7.24% | 44.52% | 44.52% | 44.52% | 100.00% | 22.36% | 22.36% | 22.36% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 50.00% | -0.05% | 16.67% | 42.31% | -9.98% | -27.62% | 18.73% | 38.86% | 66.32% | 45.00% | -9.36% | 29.63% | 85.33% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 7 | 42.86% | -4.70% | 12.60% | 36.02% | -12.41% | -25.24% | 21.64% | 31.10% | 49.44% | 28.57% | -16.66% | 19.73% | 89.29% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 57.50% | 3.32% | 19.14% | 79.03% | -11.53% | -21.71% | 16.18% | 30.72% | 99.79% | 77.50% | 24.48% | 60.87% | 149.80% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 10 | 30.00% | -5.58% | 7.23% | 39.85% | -12.55% | -17.37% | 6.25% | 15.87% | 46.61% | 100.00% | 33.84% | 57.99% | 78.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 7 | 42.86% | -0.61% | -11.08% | 48.78% | 57.14% | 39.85% | 106.26% |
| BTC-USD | HISTORICAL_BTC_BULL | 25 | 76.00% | 11.53% | -7.02% | 23.88% | 76.00% | 14.99% | 83.06% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 6 | 83.33% | 14.17% | -12.97% | 24.16% | 33.33% | -4.34% | 42.99% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -8.73% | -11.49% | 34.10% | 100.00% | 23.38% | 56.39% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 5 | 40.00% | -4.70% | -12.41% | 37.84% | 20.00% | -13.88% | 37.84% |
| DOGE-USD | HISTORICAL_BTC_BULL | 29 | 62.07% | 2.72% | -8.45% | 42.40% | 58.62% | 7.44% | 66.30% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 0.00% | -25.39% | -29.05% | 15.44% | 0.00% | -33.32% | 15.44% |
| SOL-USD | HISTORICAL_BTC_BEAR | 4 | 50.00% | -0.81% | -10.14% | 22.34% | 50.00% | -11.02% | 49.07% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 64.71% | 6.74% | -14.54% | 23.88% | 70.59% | 22.65% | 103.40% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 75.00% | 11.11% | -12.23% | 24.71% | 50.00% | 8.79% | 71.26% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 15 | 46.67% | -1.66% | -11.26% | 46.86% | 100.00% | 57.83% | 110.27% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 24 | 83.33% | 11.66% | -8.67% | 27.01% | 70.83% | 13.12% | 69.08% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 55.56% | 14.13% | -5.26% | 27.19% | 55.56% | 14.99% | 103.40% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -1.72% | -7.24% | 44.52% | 100.00% | 22.36% | 44.52% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -8.13% | -16.41% | 15.66% | 66.67% | 23.53% | 56.59% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 7 | 42.86% | -4.70% | -12.41% | 31.10% | 28.57% | -16.66% | 61.80% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 29 | 55.17% | 1.03% | -9.79% | 42.40% | 51.72% | 1.09% | 65.27% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -26.97% | -29.21% | 12.80% | 25.00% | -26.44% | 18.46% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 18 | 72.22% | 8.42% | -11.53% | 20.89% | 55.56% | 0.36% | 65.04% |
| SOL-USD | HISTORICAL_ASSET_BULL | 9 | 66.67% | 14.13% | -11.26% | 235.51% | 88.89% | 133.98% | 235.51% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -10.88% | -21.55% | 1.18% | 100.00% | 23.88% | 40.23% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 0.76% | -8.82% | 36.50% | 100.00% | 13.06% | 36.59% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 10 | 30.00% | -5.58% | -12.55% | 15.87% | 100.00% | 33.84% | 68.91% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | MKR-USD | 2020-02-27 | 78.12% | RECOVERY | MIXED | SAME_ASSET_ONLY | MIXED | -1.72% | -7.24% | 44.52% | 22.36% | -7.36% | 44.52% |
| BTC-USD | XRP-USD | 2023-07-30 | 86.23% | BULL | BULL | DIFFERENT | BEARISH_30D | -10.51% | -18.88% | 0.00% | -19.43% | -19.43% | 0.00% |
| BTC-USD | BNB-USD | 2018-11-03 | 85.39% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| BTC-USD | ETC-USD | 2020-08-19 | 84.53% | BULL | RECOVERY | DIFFERENT | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| BTC-USD | ETC-USD | 2023-07-30 | 84.10% | BULL | BEAR | DIFFERENT | MIXED | 9.48% | -1.99% | 12.30% | 8.74% | -1.99% | 22.62% |
| BTC-USD | DOGE-USD | 2020-08-19 | 83.22% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 38.28% | -5.26% | 47.29% | 157.94% | -5.26% | 226.62% |
| BTC-USD | XLM-USD | 2020-08-19 | 82.79% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | -12.24% | -24.52% | 23.19% | 56.48% | -24.52% | 103.40% |
| BTC-USD | LTC-USD | 2018-11-03 | 82.65% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 21.72% | -11.08% | 24.04% | 70.15% | -11.08% | 97.69% |
| BTC-USD | CRV-USD | 2023-08-03 | 81.02% | DISTRIBUTION | BEAR | DIFFERENT | BULLISH_30D | 18.89% | -13.32% | 18.89% | -13.86% | -14.48% | 18.89% |
| BTC-USD | XTZ-USD | 2023-07-30 | 80.97% | BULL | BEAR | DIFFERENT | MIXED | 5.91% | -7.43% | 11.68% | 12.98% | -7.43% | 33.82% |
| DOGE-USD | YFI-USD | 2022-04-25 | 86.24% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -14.50% | -21.51% | 13.63% | -25.07% | -25.52% | 13.63% |
| DOGE-USD | DOT-USD | 2023-07-30 | 85.61% | BULL | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.64% | -1.59% | 21.64% | 49.86% | -1.59% | 85.75% |
| DOGE-USD | EGLD-USD | 2023-07-20 | 85.53% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 57.59% | 0.00% | 66.83% | 148.44% | 0.00% | 154.29% |
| DOGE-USD | MATIC-USD | 2022-04-11 | 83.61% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -7.14% | -16.21% | 10.70% | -10.40% | -17.51% | 10.70% |
| DOGE-USD | OP-USD | 2026-01-16 | 83.40% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.57% | -4.25% | 37.84% | -16.66% | -27.25% | 37.84% |
| DOGE-USD | KSM-USD | 2022-04-24 | 81.94% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -26.09% | -30.83% | 3.57% | -34.28% | -38.46% | 3.57% |
| DOGE-USD | AVAX-USD | 2022-04-12 | 81.87% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -4.70% | -12.41% | 24.35% | -29.09% | -29.09% | 24.35% |
| DOGE-USD | SAND-USD | 2025-01-19 | 86.88% | BULL | BULL | DIFFERENT | MIXED | 2.06% | -9.85% | 22.79% | -20.44% | -22.67% | 22.79% |
| DOGE-USD | FIL-USD | 2022-04-25 | 86.16% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -29.26% | -31.16% | 16.04% | -32.36% | -35.61% | 16.04% |
| DOGE-USD | ALGO-USD | 2025-01-19 | 85.71% | BULL | BULL | DIFFERENT | MIXED | -5.72% | -13.55% | 9.80% | -24.18% | -30.69% | 9.80% |
| SOL-USD | VET-USD | 2020-02-23 | 78.38% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | ETC-USD | 2020-08-19 | 74.45% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| SOL-USD | ZEC-USD | 2020-02-26 | 73.41% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | -1.66% | -4.67% | 11.66% | 57.83% | -4.67% | 71.76% |
| SOL-USD | QTUM-USD | 2020-02-26 | 72.83% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -8.20% | -13.76% | 0.78% | 42.12% | -13.76% | 43.18% |
| SOL-USD | ETH-USD | 2020-02-26 | 71.98% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | -6.28% | -8.78% | 1.23% | 58.04% | -8.78% | 58.04% |
| SOL-USD | BNB-USD | 2020-02-26 | 71.36% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -11.46% | -13.55% | 0.70% | 25.56% | -13.55% | 25.56% |
| SOL-USD | WAVES-USD | 2023-07-30 | 71.33% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 10.19% | -6.81% | 17.27% | 24.55% | -6.81% | 45.32% |
| SOL-USD | LRC-USD | 2020-02-26 | 70.22% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 39.66% | -11.55% | 47.16% | 69.37% | -11.55% | 83.74% |
| SOL-USD | ALGO-USD | 2020-02-25 | 69.79% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.75% | -15.75% | 2.83% | 24.41% | -15.75% | 60.35% |
| SOL-USD | NEO-USD | 2020-02-26 | 69.66% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -18.30% | -20.05% | 0.00% | 1.84% | -20.05% | 9.18% |

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the cleanest filter, but it needs enough matches to matter.
- If SAME_BTC_AND_ASSET_REGIME has fewer than 5 matches, treat it as useful context, not a strong statistic.
- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.
- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.

## Regime definitions

- BULL: price above MA200, MA200 rising, positive 90d trend.
- BEAR: price below MA200, MA200 falling, weak 90d trend.
- RECOVERY: improving 90d trend, but not yet a clean bull structure.
- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.
- MIXED: unclear regime.
- UNKNOWN: not enough historical data.

