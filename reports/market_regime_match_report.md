# Market Regime Match Report

Generated: 2026-08-25 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | MIXED | 80.568 $ | True | 8.51% | -9.09% | MIXED | 8.51% | -9.09% |
| DOGE-USD | DISTRIBUTION | 0.09289 $ | True | -7.49% | -15.60% | MIXED | 8.51% | -9.09% |
| SOL-USD | RECOVERY | 102,48 $ | True | 24.49% | -15.17% | MIXED | 8.51% | -9.09% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 7.69% | 16.45% | 42.70% | -7.34% | -19.02% | 16.59% | 27.61% | 52.63% | 65.00% | 13.77% | 40.80% | 73.07% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 1.55% | 18.91% | 42.31% | -9.87% | -31.21% | 21.55% | 42.02% | 66.32% | 50.00% | -2.59% | 30.92% | 93.88% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 55.00% | 3.87% | 17.36% | 58.17% | -11.39% | -21.71% | 13.17% | 24.07% | 58.17% | 75.00% | 23.26% | 42.84% | 110.93% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 10 | 30.00% | -5.58% | 6.58% | 39.85% | -12.55% | -17.37% | 4.64% | 15.37% | 46.61% | 100.00% | 28.85% | 54.06% | 78.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 8 | 37.50% | -3.77% | -8.94% | 39.55% | 62.50% | 26.27% | 108.72% |
| BTC-USD | HISTORICAL_BTC_BULL | 26 | 76.92% | 10.68% | -7.01% | 24.83% | 73.08% | 15.21% | 64.74% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 66.67% | 16.22% | -13.32% | 22.40% | 0.00% | -13.86% | 22.40% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -15.07% | -15.75% | 35.71% | 66.67% | 23.44% | 55.17% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 5 | 40.00% | -4.70% | -16.21% | 37.84% | 20.00% | -16.66% | 37.84% |
| DOGE-USD | HISTORICAL_BTC_BULL | 30 | 63.33% | 4.19% | -7.21% | 43.25% | 63.33% | 9.93% | 81.38% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -14.50% | -21.51% | 22.44% | 0.00% | -32.36% | 22.44% |
| SOL-USD | HISTORICAL_BTC_BEAR | 6 | 66.67% | 10.35% | -9.55% | 56.97% | 66.67% | 16.28% | 90.71% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 58.82% | 6.74% | -11.52% | 23.19% | 70.59% | 14.56% | 68.47% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 80.00% | 12.12% | -13.32% | 18.89% | 40.00% | -1.95% | 65.84% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 33.33% | -5.25% | -11.40% | 20.47% | 100.00% | 28.85% | 66.20% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 73.08% | 11.44% | -7.09% | 26.67% | 69.23% | 12.84% | 63.85% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 57.14% | 3.67% | -7.26% | 35.24% | 57.14% | 29.10% | 103.37% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -4.88% | -15.75% | 35.71% | 57.14% | 22.65% | 50.49% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 6 | 50.00% | -0.57% | -8.33% | 34.47% | 33.33% | -13.53% | 73.77% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 28 | 60.71% | 2.39% | -9.07% | 44.03% | 60.71% | 9.93% | 71.74% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -24.77% | -31.40% | 14.96% | 16.67% | -33.81% | 23.30% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 19 | 73.68% | 10.10% | -10.70% | 20.70% | 57.89% | 0.43% | 64.23% |
| SOL-USD | HISTORICAL_ASSET_BULL | 8 | 50.00% | 1.53% | -15.07% | 52.47% | 75.00% | 81.61% | 197.95% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -10.88% | -21.55% | 1.18% | 100.00% | 23.88% | 40.23% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 0.76% | -8.82% | 36.50% | 100.00% | 13.06% | 36.59% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 10 | 30.00% | -5.58% | -12.55% | 15.37% | 100.00% | 28.85% | 59.77% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2023-07-30 | 86.96% | BULL | BULL | DIFFERENT | BEARISH_30D | -10.51% | -18.88% | 0.00% | -19.43% | -19.43% | 0.00% |
| BTC-USD | BNB-USD | 2018-11-03 | 85.94% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| BTC-USD | ETC-USD | 2020-08-19 | 82.97% | BULL | RECOVERY | DIFFERENT | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| BTC-USD | ETC-USD | 2023-07-30 | 82.93% | BULL | BEAR | DIFFERENT | MIXED | 9.48% | -1.99% | 12.30% | 8.74% | -1.99% | 22.62% |
| BTC-USD | THETA-USD | 2018-11-02 | 82.23% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 93.12% | 0.00% | 137.20% | 61.21% | 0.00% | 137.20% |
| BTC-USD | LTC-USD | 2018-11-02 | 82.18% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 23.73% | -7.03% | 29.69% | 97.31% | -7.03% | 106.68% |
| BTC-USD | EOS-USD | 2023-07-30 | 81.89% | BULL | BEAR | DIFFERENT | MIXED | 5.82% | -7.00% | 6.19% | 6.95% | -7.00% | 29.44% |
| BTC-USD | XLM-USD | 2020-08-19 | 81.61% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | -12.24% | -24.52% | 23.19% | 56.48% | -24.52% | 103.40% |
| BTC-USD | THETA-USD | 2023-07-29 | 81.53% | BULL | BEAR | DIFFERENT | EXPLOSIVE_60D | 39.97% | 0.00% | 40.40% | 52.99% | 0.00% | 78.81% |
| BTC-USD | XTZ-USD | 2023-07-30 | 81.18% | BULL | BEAR | DIFFERENT | MIXED | 5.91% | -7.43% | 11.68% | 12.98% | -7.43% | 33.82% |
| DOGE-USD | FIL-USD | 2022-04-25 | 86.69% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -29.26% | -31.16% | 16.04% | -32.36% | -35.61% | 16.04% |
| DOGE-USD | MANA-USD | 2025-01-15 | 86.50% | BULL | BULL | DIFFERENT | MIXED | -4.31% | -10.11% | 18.69% | -19.03% | -26.84% | 18.69% |
| DOGE-USD | VET-USD | 2025-01-17 | 85.96% | BULL | BULL | DIFFERENT | MIXED | 1.03% | -8.45% | 18.77% | -22.61% | -29.05% | 18.77% |
| DOGE-USD | SAND-USD | 2025-01-19 | 84.79% | BULL | BULL | DIFFERENT | MIXED | 2.06% | -9.85% | 22.79% | -20.44% | -22.67% | 22.79% |
| DOGE-USD | YFI-USD | 2022-04-25 | 84.48% | RECOVERY | BEAR | DIFFERENT | BEARISH_30D | -14.50% | -21.51% | 13.63% | -25.07% | -25.52% | 13.63% |
| DOGE-USD | KAVA-USD | 2023-07-30 | 84.47% | BULL | RECOVERY | DIFFERENT | MIXED | 8.90% | -6.74% | 11.72% | 7.44% | -6.74% | 25.72% |
| DOGE-USD | EGLD-USD | 2023-07-20 | 84.19% | BULL | BEAR | DIFFERENT | EXPLOSIVE_60D | 57.59% | 0.00% | 66.83% | 148.44% | 0.00% | 154.29% |
| DOGE-USD | DOT-USD | 2023-07-30 | 84.15% | BULL | BEAR | DIFFERENT | HIGH_SPIKE_60D | 21.64% | -1.59% | 21.64% | 49.86% | -1.59% | 85.75% |
| DOGE-USD | QTUM-USD | 2022-04-21 | 83.98% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -36.05% | -36.05% | 0.00% | -38.23% | -40.91% | 0.00% |
| DOGE-USD | ALGO-USD | 2025-01-19 | 83.92% | BULL | BULL | DIFFERENT | MIXED | -5.72% | -13.55% | 9.80% | -24.18% | -30.69% | 9.80% |
| SOL-USD | VET-USD | 2020-02-23 | 79.66% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | ETC-USD | 2020-08-19 | 73.81% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| SOL-USD | WAVES-USD | 2023-07-30 | 72.44% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 10.19% | -6.81% | 17.27% | 24.55% | -6.81% | 45.32% |
| SOL-USD | ALGO-USD | 2020-02-25 | 71.85% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.75% | -15.75% | 2.83% | 24.41% | -15.75% | 60.35% |
| SOL-USD | QTUM-USD | 2020-02-26 | 71.75% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -8.20% | -13.76% | 0.78% | 42.12% | -13.76% | 43.18% |
| SOL-USD | ZEC-USD | 2020-02-21 | 71.17% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.23% | -9.12% | 6.45% | 32.15% | -9.12% | 32.15% |
| SOL-USD | ETH-USD | 2020-02-26 | 69.59% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | -6.28% | -8.78% | 1.23% | 58.04% | -8.78% | 58.04% |
| SOL-USD | BNB-USD | 2020-02-26 | 68.80% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -11.46% | -13.55% | 0.70% | 25.56% | -13.55% | 25.56% |
| SOL-USD | LRC-USD | 2020-02-26 | 68.72% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 39.66% | -11.55% | 47.16% | 69.37% | -11.55% | 83.74% |
| SOL-USD | NEO-USD | 2020-02-26 | 67.69% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -18.30% | -20.05% | 0.00% | 1.84% | -20.05% | 9.18% |

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

