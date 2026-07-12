# Market Regime Match Report

Generated: 2026-07-12 07:39 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.827 $ | False | -14.33% | -10.21% | BEAR | -14.33% | -10.21% |
| DOGE-USD | BEAR | 0.07282 $ | False | -22.62% | -16.55% | BEAR | -14.33% | -10.21% |
| SOL-USD | BEAR | 76,45 $ | False | -11.78% | -18.42% | BEAR | -14.33% | -10.21% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 8.43% | 19.78% | 39.95% | -4.74% | -24.56% | 14.06% | 26.06% | 53.53% | 67.50% | 25.26% | 48.57% | 67.36% |
| BTC-USD | SAME_BTC_REGIME | 15 | 100.00% | 25.26% | 42.31% | 77.02% | 0.00% | -4.87% | 33.95% | 55.04% | 94.98% | 93.33% | 25.57% | 45.40% | 61.77% |
| BTC-USD | SAME_ASSET_REGIME | 27 | 85.19% | 11.11% | 21.57% | 46.75% | -4.27% | -11.83% | 19.75% | 26.13% | 56.92% | 85.19% | 32.98% | 52.58% | 68.32% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 13 | 100.00% | 22.02% | 45.24% | 86.36% | 0.00% | -4.90% | 26.00% | 53.16% | 105.78% | 92.31% | 14.38% | 42.97% | 64.40% |
| DOGE-USD | ALL_MATCHES | 40 | 17.50% | -19.69% | -6.59% | 7.92% | -26.99% | -43.10% | 5.08% | 15.20% | 26.69% | 35.00% | -3.47% | 4.46% | 37.22% |
| DOGE-USD | SAME_BTC_REGIME | 32 | 15.62% | -22.60% | -13.00% | 6.19% | -28.98% | -44.26% | 4.55% | 12.28% | 28.49% | 31.25% | -3.47% | 2.13% | 25.12% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 18.18% | -21.97% | -12.89% | 16.31% | -28.71% | -44.11% | 4.84% | 13.35% | 28.35% | 36.36% | -2.16% | 5.97% | 34.68% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 30 | 13.33% | -22.60% | -13.92% | 6.57% | -28.98% | -44.45% | 3.80% | 11.69% | 28.93% | 30.00% | -6.08% | 1.50% | 22.51% |
| SOL-USD | ALL_MATCHES | 40 | 37.50% | -2.61% | 3.58% | 28.87% | -12.02% | -25.31% | 7.81% | 15.50% | 44.97% | 52.50% | 6.73% | 27.92% | 54.41% |
| SOL-USD | SAME_BTC_REGIME | 22 | 45.45% | -0.76% | 6.00% | 27.61% | -10.21% | -22.45% | 9.50% | 16.08% | 42.61% | 68.18% | 9.68% | 39.53% | 65.72% |
| SOL-USD | SAME_ASSET_REGIME | 30 | 43.33% | -0.28% | 6.00% | 28.87% | -11.65% | -24.07% | 9.50% | 16.81% | 44.97% | 63.33% | 8.58% | 33.85% | 54.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 44.44% | -0.76% | 2.26% | 20.85% | -10.90% | -20.76% | 9.50% | 11.64% | 27.16% | 72.22% | 9.68% | 31.73% | 57.83% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 15 | 100.00% | 25.26% | 0.00% | 55.04% | 93.33% | 25.57% | 81.25% |
| BTC-USD | HISTORICAL_BTC_BULL | 16 | 50.00% | 0.49% | -8.66% | 10.72% | 50.00% | 10.60% | 47.34% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 100.00% | 11.31% | -6.15% | 15.36% | 100.00% | 54.98% | 93.27% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -7.80% | -12.28% | 14.85% | 20.00% | -20.22% | 32.20% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 32 | 15.62% | -22.60% | -28.98% | 12.28% | 31.25% | -3.47% | 25.33% |
| DOGE-USD | HISTORICAL_BTC_BULL | 3 | 0.00% | -6.66% | -14.04% | 15.24% | 33.33% | -9.16% | 15.89% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 21.44% | -1.83% | 24.78% | 100.00% | 76.22% | 136.08% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -9.79% | -13.95% | 12.70% | 33.33% | -15.37% | 27.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 45.45% | -0.76% | -10.21% | 16.08% | 68.18% | 9.68% | 68.69% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 10.00% | -6.31% | -22.26% | 3.09% | 20.00% | -4.03% | 3.09% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 9.86% | -5.76% | 17.45% | 100.00% | 54.98% | 64.19% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 6 | 33.33% | -9.44% | -15.49% | 40.99% | 33.33% | -9.05% | 40.99% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 27 | 85.19% | 11.11% | -4.27% | 26.13% | 85.19% | 32.98% | 79.25% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 28.57% | -18.82% | -23.01% | 9.09% | 28.57% | -5.68% | 20.47% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 9.86% | -10.72% | 31.08% | 50.00% | 11.71% | 64.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 50.00% | 3.62% | -5.74% | 38.38% | 25.00% | -23.83% | 41.88% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 18.18% | -21.97% | -28.71% | 13.35% | 36.36% | -2.16% | 25.45% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -3.74% | -10.00% | 13.15% | 50.00% | -11.83% | 16.71% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -25.24% | -38.58% | 7.55% | 0.00% | -3.26% | 7.55% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -8.75% | -14.04% | 12.94% | 0.00% | -9.16% | 12.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -2.56% | -8.55% | 20.44% | 33.33% | -15.37% | 47.15% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 43.33% | -0.28% | -11.65% | 16.81% | 63.33% | 8.58% | 58.94% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 0.00% | -13.12% | -21.16% | 2.39% | 0.00% | -8.98% | 2.39% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -5.30% | -20.18% | 1.03% | 0.00% | -2.08% | 4.45% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -6.02% | -22.79% | 26.08% | 40.00% | -4.13% | 70.92% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-09-19 | 89.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| BTC-USD | XRP-USD | 2019-09-29 | 86.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| BTC-USD | ONE-USD | 2020-01-12 | 85.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |
| BTC-USD | KSM-USD | 2022-03-10 | 85.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.02% | -4.93% | 16.96% | 14.38% | -4.93% | 37.01% |
| BTC-USD | BAT-USD | 2019-10-04 | 84.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.15% | -1.02% | 43.98% | 5.38% | -1.02% | 63.91% |
| BTC-USD | XLM-USD | 2019-10-04 | 84.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 49.02% | 0.00% | 53.16% | 5.97% | 0.00% | 80.44% |
| BTC-USD | MKR-USD | 2020-01-13 | 84.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 2.37% | 0.00% | 19.75% | 67.03% | 0.00% | 121.83% |
| BTC-USD | XLM-USD | 2020-01-07 | 84.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| BTC-USD | QTUM-USD | 2020-01-12 | 83.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.33% | 0.00% | 26.00% | 25.57% | 0.00% | 43.16% |
| BTC-USD | EOS-USD | 2020-01-07 | 83.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.83% | 0.00% | 25.64% | 7.27% | 0.00% | 25.64% |
| DOGE-USD | VET-USD | 2022-02-27 | 88.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | DASH-USD | 2022-02-25 | 87.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 87.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | INJ-USD | 2022-02-22 | 86.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -42.93% | -42.93% | 3.20% | -31.40% | -43.70% | 3.20% |
| DOGE-USD | OP-USD | 2025-12-07 | 86.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -12.89% | -25.94% | 0.00% | -0.67% | -25.94% | 25.30% |
| DOGE-USD | ENJ-USD | 2022-02-25 | 86.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.55% | -33.46% | 5.00% | 1.45% | -33.46% | 5.00% |
| DOGE-USD | DOT-USD | 2022-02-25 | 86.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.93% | -28.64% | 0.66% | -15.09% | -33.21% | 0.66% |
| DOGE-USD | XTZ-USD | 2025-12-06 | 86.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.41% | -12.14% | 4.26% | -2.16% | -12.14% | 4.26% |
| DOGE-USD | ETH-USD | 2022-02-25 | 86.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.11% | -44.85% | 3.20% | -10.14% | -44.85% | 3.20% |
| SOL-USD | SOL-USD | 2025-12-04 | 78.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.51% | -10.44% | 9.16% | 6.95% | -10.44% | 10.43% |
| SOL-USD | APT-USD | 2024-09-06 | 77.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | ENJ-USD | 2018-09-19 | 76.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -16.11% | -19.37% | 5.11% | 93.16% | -38.09% | 93.16% |
| SOL-USD | NEAR-USD | 2025-12-06 | 76.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.76% | -13.93% | 10.53% | 16.47% | -13.93% | 18.85% |
| SOL-USD | OMG-USD | 2025-12-06 | 76.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -8.00% | 2.31% | 8.91% | -8.00% | 14.55% |
| SOL-USD | CRV-USD | 2025-12-05 | 75.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.77% | -11.77% | 8.67% | 13.61% | -11.77% | 20.25% |
| SOL-USD | RUNE-USD | 2025-12-07 | 75.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.46% | -17.52% | 0.00% | 8.26% | -17.52% | 37.02% |
| SOL-USD | XLM-USD | 2020-01-07 | 75.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| SOL-USD | LINK-USD | 2025-12-06 | 75.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.84% | -11.36% | 4.69% | 10.45% | -11.36% | 12.98% |
| SOL-USD | BTC-USD | 2025-12-06 | 75.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.91% | -9.39% | 2.85% | 11.35% | -9.39% | 12.84% |

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

