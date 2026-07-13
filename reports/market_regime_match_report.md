# Market Regime Match Report

Generated: 2026-07-13 06:28 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 62.682 $ | False | -15.39% | -10.18% | BEAR | -15.39% | -10.18% |
| DOGE-USD | BEAR | 0.07214 $ | False | -22.38% | -16.45% | BEAR | -15.39% | -10.18% |
| SOL-USD | BEAR | 76,29 $ | False | -8.90% | -18.22% | BEAR | -15.39% | -10.18% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 8.25% | 19.78% | 39.95% | -4.63% | -24.56% | 15.35% | 26.31% | 53.53% | 65.00% | 21.86% | 44.19% | 67.36% |
| BTC-USD | SAME_BTC_REGIME | 14 | 100.00% | 30.09% | 43.77% | 81.69% | 0.00% | -4.66% | 36.06% | 55.99% | 100.38% | 92.86% | 29.27% | 46.62% | 63.09% |
| BTC-USD | SAME_ASSET_REGIME | 26 | 88.46% | 11.31% | 21.79% | 47.13% | -4.01% | -10.14% | 19.29% | 26.41% | 57.87% | 84.62% | 31.05% | 51.37% | 68.64% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 100.00% | 20.68% | 46.19% | 91.02% | 0.00% | -4.75% | 29.97% | 55.51% | 111.18% | 91.67% | 19.97% | 45.70% | 65.72% |
| DOGE-USD | ALL_MATCHES | 40 | 17.50% | -19.69% | -6.59% | 7.92% | -26.99% | -43.10% | 4.92% | 15.20% | 26.69% | 37.50% | -2.71% | 7.38% | 39.33% |
| DOGE-USD | SAME_BTC_REGIME | 32 | 15.62% | -22.23% | -13.00% | 6.19% | -28.98% | -44.26% | 3.80% | 12.28% | 28.49% | 34.38% | -2.71% | 4.46% | 37.90% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 18.18% | -21.58% | -12.89% | 16.31% | -28.71% | -44.11% | 4.26% | 13.35% | 28.35% | 39.39% | -1.48% | 11.61% | 38.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 30 | 13.33% | -22.23% | -13.92% | 6.57% | -28.98% | -44.45% | 3.27% | 11.69% | 28.93% | 33.33% | -2.92% | 3.35% | 26.83% |
| SOL-USD | ALL_MATCHES | 40 | 35.00% | -2.61% | 3.58% | 28.87% | -12.08% | -25.31% | 7.81% | 15.50% | 44.97% | 52.50% | 6.06% | 27.92% | 54.41% |
| SOL-USD | SAME_BTC_REGIME | 22 | 40.91% | -0.79% | 6.00% | 27.61% | -10.90% | -22.45% | 9.50% | 16.08% | 42.61% | 68.18% | 8.58% | 39.53% | 65.72% |
| SOL-USD | SAME_ASSET_REGIME | 30 | 40.00% | -0.28% | 6.00% | 28.87% | -11.83% | -24.07% | 9.50% | 16.81% | 44.97% | 63.33% | 7.70% | 33.85% | 54.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 38.89% | -0.79% | 2.00% | 20.85% | -11.56% | -20.76% | 9.50% | 11.64% | 27.16% | 72.22% | 8.58% | 31.73% | 57.83% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 100.00% | 30.09% | 0.00% | 55.99% | 92.86% | 29.27% | 81.65% |
| BTC-USD | HISTORICAL_BTC_BULL | 16 | 50.00% | 0.49% | -8.66% | 10.72% | 50.00% | 10.60% | 43.61% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 100.00% | 11.51% | -5.57% | 21.60% | 100.00% | 50.78% | 73.78% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -7.78% | -12.50% | 16.64% | 0.00% | -25.42% | 16.64% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 32 | 15.62% | -22.23% | -28.98% | 12.28% | 34.38% | -2.71% | 25.43% |
| DOGE-USD | HISTORICAL_BTC_BULL | 3 | 0.00% | -6.66% | -14.04% | 15.24% | 33.33% | -9.16% | 15.89% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 21.44% | -1.83% | 24.78% | 100.00% | 76.22% | 136.08% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -9.79% | -13.95% | 12.70% | 33.33% | -15.37% | 27.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 40.91% | -0.79% | -10.90% | 16.08% | 68.18% | 8.58% | 68.69% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 10.00% | -6.31% | -22.26% | 3.09% | 20.00% | -4.03% | 3.09% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 9.86% | -5.76% | 17.45% | 100.00% | 54.98% | 64.19% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 6 | 33.33% | -9.44% | -15.49% | 40.99% | 33.33% | -9.05% | 40.99% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 88.46% | 11.31% | -4.01% | 26.41% | 84.62% | 31.05% | 79.85% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 28.57% | -17.97% | -17.97% | 9.09% | 28.57% | -5.68% | 20.47% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 9.86% | -10.72% | 31.08% | 50.00% | 11.71% | 64.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -7.78% | -11.48% | 32.20% | 20.00% | -25.42% | 32.20% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 18.18% | -21.58% | -28.71% | 13.35% | 39.39% | -1.48% | 28.83% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -3.74% | -10.00% | 13.15% | 50.00% | -11.83% | 16.71% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -25.24% | -38.58% | 7.55% | 0.00% | -3.26% | 7.55% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -8.75% | -14.04% | 12.94% | 0.00% | -9.16% | 12.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -2.56% | -8.55% | 20.44% | 33.33% | -15.37% | 47.15% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 40.00% | -0.28% | -11.83% | 16.81% | 63.33% | 7.70% | 58.94% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 0.00% | -13.12% | -21.16% | 2.39% | 0.00% | -8.98% | 2.39% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -5.30% | -20.18% | 1.03% | 0.00% | -2.08% | 4.45% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -6.02% | -22.79% | 26.08% | 40.00% | -4.13% | 70.92% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-09-19 | 89.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| BTC-USD | ONE-USD | 2020-01-12 | 86.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |
| BTC-USD | KSM-USD | 2022-03-10 | 85.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.02% | -4.93% | 16.96% | 14.38% | -4.93% | 37.01% |
| BTC-USD | LTC-USD | 2020-01-08 | 85.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.23% | -4.36% | 15.86% | 2.87% | -4.36% | 15.86% |
| BTC-USD | BAT-USD | 2019-10-04 | 84.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.15% | -1.02% | 43.98% | 5.38% | -1.02% | 63.91% |
| BTC-USD | XLM-USD | 2019-10-04 | 84.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 49.02% | 0.00% | 53.16% | 5.97% | 0.00% | 80.44% |
| BTC-USD | MKR-USD | 2020-01-13 | 84.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 2.37% | 0.00% | 19.75% | 67.03% | 0.00% | 121.83% |
| BTC-USD | XLM-USD | 2020-01-07 | 84.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| BTC-USD | QTUM-USD | 2020-01-12 | 83.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.33% | 0.00% | 26.00% | 25.57% | 0.00% | 43.16% |
| BTC-USD | EOS-USD | 2020-01-07 | 83.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.83% | 0.00% | 25.64% | 7.27% | 0.00% | 25.64% |
| DOGE-USD | VET-USD | 2022-02-27 | 88.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | DASH-USD | 2022-02-25 | 87.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 87.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | INJ-USD | 2022-02-22 | 86.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -42.93% | -42.93% | 3.20% | -31.40% | -43.70% | 3.20% |
| DOGE-USD | ENJ-USD | 2022-02-25 | 86.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.55% | -33.46% | 5.00% | 1.45% | -33.46% | 5.00% |
| DOGE-USD | DOT-USD | 2022-02-25 | 86.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.93% | -28.64% | 0.66% | -15.09% | -33.21% | 0.66% |
| DOGE-USD | OP-USD | 2025-12-07 | 86.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -12.89% | -25.94% | 0.00% | -0.67% | -25.94% | 25.30% |
| DOGE-USD | ETH-USD | 2022-02-25 | 86.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.11% | -44.85% | 3.20% | -10.14% | -44.85% | 3.20% |
| DOGE-USD | XTZ-USD | 2025-12-06 | 86.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.41% | -12.14% | 4.26% | -2.16% | -12.14% | 4.26% |
| SOL-USD | SOL-USD | 2025-12-04 | 78.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.51% | -10.44% | 9.16% | 6.95% | -10.44% | 10.43% |
| SOL-USD | APT-USD | 2024-09-06 | 77.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | ENJ-USD | 2018-09-19 | 76.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -16.11% | -19.37% | 5.11% | 93.16% | -38.09% | 93.16% |
| SOL-USD | NEAR-USD | 2025-12-06 | 76.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.76% | -13.93% | 10.53% | 16.47% | -13.93% | 18.85% |
| SOL-USD | OMG-USD | 2025-12-06 | 76.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -8.00% | 2.31% | 8.91% | -8.00% | 14.55% |
| SOL-USD | CRV-USD | 2025-12-05 | 75.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.77% | -11.77% | 8.67% | 13.61% | -11.77% | 20.25% |
| SOL-USD | XLM-USD | 2020-01-07 | 75.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| SOL-USD | RUNE-USD | 2025-12-07 | 75.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.46% | -17.52% | 0.00% | 8.26% | -17.52% | 37.02% |
| SOL-USD | BTC-USD | 2025-12-07 | 75.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.07% | -11.90% | 0.00% | 5.62% | -11.90% | 9.72% |
| SOL-USD | LINK-USD | 2025-12-06 | 75.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.84% | -11.36% | 4.69% | 10.45% | -11.36% | 12.98% |

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

