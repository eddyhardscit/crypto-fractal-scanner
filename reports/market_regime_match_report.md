# Market Regime Match Report

Generated: 2026-08-08 05:18 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.960 $ | False | -20.91% | -10.06% | BEAR | -20.91% | -10.06% |
| DOGE-USD | BEAR | 0.07009 $ | False | -37.66% | -16.66% | BEAR | -20.91% | -10.06% |
| SOL-USD | BEAR | 74,58 $ | False | -22.72% | -17.11% | BEAR | -20.91% | -10.06% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 87.50% | 13.31% | 19.40% | 36.48% | -2.03% | -14.75% | 19.66% | 38.88% | 52.72% | 60.00% | 17.79% | 56.64% | 86.39% |
| BTC-USD | SAME_BTC_REGIME | 17 | 94.12% | 9.66% | 15.64% | 20.09% | -3.24% | -12.58% | 11.77% | 15.98% | 26.01% | 29.41% | -15.89% | 12.19% | 57.68% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 95.65% | 13.50% | 17.55% | 31.45% | -1.76% | -11.35% | 15.63% | 33.21% | 45.79% | 52.17% | 12.19% | 47.68% | 74.72% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 93.75% | 8.72% | 14.04% | 17.55% | -3.47% | -12.89% | 11.75% | 15.72% | 19.66% | 31.25% | -14.49% | 15.34% | 60.84% |
| DOGE-USD | ALL_MATCHES | 40 | 62.50% | 13.25% | 24.56% | 44.33% | -10.20% | -29.83% | 19.62% | 28.98% | 53.39% | 47.50% | -1.32% | 22.05% | 100.66% |
| DOGE-USD | SAME_BTC_REGIME | 22 | 81.82% | 19.02% | 29.77% | 44.03% | -9.35% | -27.82% | 23.04% | 30.02% | 49.63% | 50.00% | 1.22% | 14.74% | 76.64% |
| DOGE-USD | SAME_ASSET_REGIME | 19 | 89.47% | 20.22% | 27.65% | 47.59% | -7.10% | -18.98% | 23.41% | 28.16% | 67.46% | 52.63% | 3.08% | 27.98% | 84.46% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 17 | 88.24% | 17.82% | 23.14% | 35.92% | -7.69% | -21.57% | 22.09% | 24.34% | 39.06% | 47.06% | -0.65% | 9.84% | 57.38% |
| SOL-USD | ALL_MATCHES | 40 | 77.50% | 11.90% | 24.29% | 59.02% | -3.97% | -15.94% | 18.03% | 32.64% | 85.21% | 60.00% | 15.30% | 64.21% | 159.36% |
| SOL-USD | SAME_BTC_REGIME | 17 | 100.00% | 14.61% | 22.73% | 54.45% | -3.99% | -16.57% | 19.40% | 30.20% | 65.37% | 52.94% | 19.19% | 123.88% | 159.58% |
| SOL-USD | SAME_ASSET_REGIME | 21 | 90.48% | 12.62% | 28.98% | 51.69% | -3.99% | -17.83% | 19.40% | 40.02% | 78.67% | 57.14% | 25.81% | 102.18% | 159.29% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 15 | 100.00% | 14.61% | 31.60% | 55.83% | -3.99% | -16.99% | 19.40% | 40.94% | 69.81% | 53.33% | 25.81% | 131.69% | 159.73% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 17 | 94.12% | 9.66% | -3.24% | 15.98% | 29.41% | -15.89% | 35.16% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 70.00% | 18.38% | -4.43% | 55.32% | 70.00% | 63.13% | 91.59% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 9 | 100.00% | 14.66% | 0.00% | 37.63% | 100.00% | 34.16% | 51.37% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 13.44% | -2.60% | 46.96% | 75.00% | 46.17% | 74.60% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 22 | 81.82% | 19.02% | -9.35% | 30.02% | 50.00% | 1.22% | 69.28% |
| DOGE-USD | HISTORICAL_BTC_BULL | 16 | 43.75% | -2.77% | -15.39% | 30.05% | 43.75% | -9.34% | 56.26% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -22.31% | -27.36% | 0.00% | 50.00% | 61.06% | 119.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 100.00% | 14.61% | -3.99% | 30.20% | 52.94% | 19.19% | 123.88% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 42.86% | -4.55% | -8.34% | 31.40% | 57.14% | 1.06% | 41.57% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 100.00% | 12.62% | 0.00% | 40.02% | 100.00% | 51.71% | 96.08% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 104.48% | -3.96% | 120.09% | 100.00% | 307.28% | 352.55% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 10 | 50.00% | 1.03% | -4.58% | 26.07% | 50.00% | 7.36% | 54.63% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 95.65% | 13.50% | -1.76% | 33.21% | 52.17% | 12.19% | 51.90% |
| BTC-USD | HISTORICAL_ASSET_BULL | 8 | 87.50% | 13.56% | -3.52% | 57.85% | 87.50% | 47.09% | 108.29% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 40.15% | -2.38% | 86.65% | 100.00% | 35.59% | 90.23% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 3.33% | -0.44% | 26.24% | 42.86% | -0.85% | 53.25% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 19 | 89.47% | 20.22% | -7.10% | 28.16% | 52.63% | 3.08% | 69.64% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 8 | 50.00% | -8.18% | -20.75% | 30.05% | 50.00% | 4.70% | 84.56% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 43.62% | -10.62% | 46.98% | 100.00% | 14.59% | 69.28% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 11 | 18.18% | -16.07% | -21.24% | 19.22% | 27.27% | -21.46% | 37.56% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 21 | 90.48% | 12.62% | -3.99% | 40.02% | 57.14% | 25.81% | 106.31% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 8.36% | -12.02% | 41.61% | 75.00% | 10.12% | 140.27% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 10.69% | -4.20% | 43.70% | 50.00% | 4.81% | 53.40% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 3 | 33.33% | -3.67% | -4.39% | 9.71% | 33.33% | -0.05% | 11.28% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 8 | 75.00% | 15.81% | -3.60% | 30.37% | 75.00% | 29.66% | 67.42% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-31 | 91.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.65% | -1.42% | 9.89% | -13.09% | -18.65% | 10.41% |
| BTC-USD | ETH-USD | 2025-12-31 | 90.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.28% | 0.00% | 10.59% | -22.79% | -28.34% | 10.59% |
| BTC-USD | BTC-USD | 2018-10-16 | 88.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.73% | -5.18% | 11.73% | 12.19% | -5.18% | 15.55% |
| BTC-USD | OMG-USD | 2018-10-19 | 87.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.73% | -17.83% | 7.53% | 45.05% | -17.83% | 45.05% |
| BTC-USD | QTUM-USD | 2025-12-31 | 86.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.54% | -6.19% | 5.05% | -23.02% | -25.42% | 13.74% |
| BTC-USD | BNB-USD | 2025-12-31 | 86.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| BTC-USD | XTZ-USD | 2018-10-19 | 86.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 4.87% | -11.35% | 13.01% | 76.63% | -11.35% | 102.96% |
| BTC-USD | BTC-USD | 2026-01-02 | 86.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.87% | -3.15% | 12.44% | -15.89% | -16.68% | 12.44% |
| BTC-USD | ETC-USD | 2025-12-31 | 85.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.50% | -3.70% | 15.63% | -15.92% | -19.74% | 17.93% |
| BTC-USD | NEO-USD | 2018-10-19 | 85.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.31% | -8.94% | 35.16% | 24.79% | -8.94% | 35.16% |
| DOGE-USD | OP-USD | 2026-01-01 | 91.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.98% | -7.10% | 49.82% | -15.88% | -18.56% | 49.82% |
| DOGE-USD | VET-USD | 2022-03-24 | 90.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.63% | -3.05% | 23.68% | 9.84% | -3.05% | 50.90% |
| DOGE-USD | LTC-USD | 2018-04-19 | 89.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.12% | -36.07% | 0.00% | -31.88% | -38.84% | 0.00% |
| DOGE-USD | HBAR-USD | 2022-03-24 | 89.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 23.41% | -3.18% | 23.41% | 3.08% | -3.18% | 34.66% |
| DOGE-USD | BAT-USD | 2018-10-19 | 89.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.64% | -16.39% | 17.64% | 80.49% | -16.39% | 80.49% |
| DOGE-USD | MKR-USD | 2022-10-04 | 89.11% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.99% | -0.27% | 24.02% | 41.98% | -0.27% | 48.95% |
| DOGE-USD | ADA-USD | 2022-03-22 | 89.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.42% | -10.22% | 12.42% | -7.62% | -10.22% | 22.52% |
| DOGE-USD | XTZ-USD | 2025-12-31 | 88.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| DOGE-USD | NEO-USD | 2022-03-22 | 88.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 31.89% | -6.02% | 31.89% | 3.42% | -6.02% | 39.93% |
| DOGE-USD | FIL-USD | 2022-03-26 | 88.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 53.58% | -4.32% | 85.24% | 8.64% | -4.32% | 85.24% |
| SOL-USD | ENJ-USD | 2018-10-19 | 82.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 130.26% | -26.20% | 130.26% | 394.56% | -26.20% | 533.03% |
| SOL-USD | EOS-USD | 2018-10-29 | 80.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 58.60% | -1.80% | 78.67% | 123.88% | -1.80% | 123.88% |
| SOL-USD | NEAR-USD | 2025-12-31 | 80.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.61% | -7.58% | 16.66% | 55.80% | -7.58% | 106.31% |
| SOL-USD | QTUM-USD | 2018-10-19 | 79.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.74% | -15.73% | 15.32% | 25.81% | -15.73% | 31.28% |
| SOL-USD | RUNE-USD | 2026-01-01 | 78.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 51.69% | -4.54% | 51.69% | -3.02% | -20.45% | 56.14% |
| SOL-USD | LINK-USD | 2025-12-31 | 78.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.98% | -2.30% | 15.98% | -10.68% | -17.80% | 19.79% |
| SOL-USD | SOL-USD | 2026-01-03 | 77.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| SOL-USD | KAVA-USD | 2025-12-31 | 75.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.73% | -3.48% | 25.59% | -18.69% | -20.93% | 27.22% |
| SOL-USD | DOT-USD | 2025-12-31 | 75.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.56% | -10.35% | 5.52% | -25.10% | -27.46% | 6.36% |
| SOL-USD | BTC-USD | 2026-01-02 | 75.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.87% | -3.15% | 12.44% | -15.89% | -16.68% | 12.44% |

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

