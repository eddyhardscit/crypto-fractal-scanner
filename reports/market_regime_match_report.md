# Market Regime Match Report

Generated: 2026-08-07 05:16 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.195 $ | False | -20.41% | -10.02% | BEAR | -20.41% | -10.02% |
| DOGE-USD | BEAR | 0.06898 $ | False | -36.52% | -16.61% | BEAR | -20.41% | -10.02% |
| SOL-USD | BEAR | 72,65 $ | False | -22.00% | -17.08% | BEAR | -20.41% | -10.02% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 82.50% | 10.40% | 20.56% | 46.97% | -4.21% | -17.98% | 14.64% | 39.88% | 56.99% | 57.50% | 14.06% | 40.16% | 79.91% |
| BTC-USD | SAME_BTC_REGIME | 16 | 87.50% | 6.51% | 10.41% | 17.49% | -5.25% | -16.13% | 10.78% | 13.67% | 35.86% | 31.25% | -14.31% | 14.43% | 60.84% |
| BTC-USD | SAME_ASSET_REGIME | 22 | 90.91% | 8.72% | 21.17% | 39.50% | -4.18% | -14.13% | 12.78% | 41.86% | 55.83% | 50.00% | 5.88% | 43.42% | 75.67% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 87.50% | 6.51% | 10.41% | 17.49% | -5.25% | -16.13% | 10.78% | 13.67% | 35.86% | 31.25% | -14.31% | 14.43% | 60.84% |
| DOGE-USD | ALL_MATCHES | 40 | 57.50% | 10.80% | 23.21% | 43.22% | -14.48% | -29.37% | 16.28% | 25.32% | 50.07% | 45.00% | -6.11% | 16.24% | 80.63% |
| DOGE-USD | SAME_BTC_REGIME | 23 | 69.57% | 12.42% | 23.28% | 43.93% | -13.75% | -27.60% | 19.73% | 24.22% | 49.44% | 43.48% | -5.90% | 12.06% | 39.30% |
| DOGE-USD | SAME_ASSET_REGIME | 21 | 76.19% | 16.16% | 23.41% | 46.09% | -10.52% | -22.75% | 19.73% | 24.43% | 59.00% | 47.62% | -5.58% | 27.38% | 80.49% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 73.68% | 12.42% | 22.89% | 44.30% | -11.49% | -24.07% | 17.64% | 23.85% | 51.66% | 42.11% | -5.90% | 9.24% | 49.68% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 7.59% | 20.44% | 52.38% | -4.27% | -25.16% | 12.59% | 26.66% | 58.73% | 52.50% | 4.35% | 53.58% | 141.49% |
| SOL-USD | SAME_BTC_REGIME | 16 | 87.50% | 7.50% | 17.67% | 46.08% | -4.27% | -16.78% | 13.33% | 23.20% | 54.10% | 50.00% | 6.29% | 123.97% | 149.40% |
| SOL-USD | SAME_ASSET_REGIME | 23 | 73.91% | 7.22% | 19.35% | 40.41% | -4.80% | -25.56% | 12.55% | 23.99% | 55.40% | 47.83% | -0.20% | 77.65% | 136.46% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 87.50% | 7.50% | 17.67% | 46.08% | -4.27% | -16.78% | 13.33% | 23.20% | 54.10% | 50.00% | 6.29% | 123.97% | 149.40% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 16 | 87.50% | 6.51% | -5.25% | 13.67% | 31.25% | -14.31% | 37.03% |
| BTC-USD | HISTORICAL_BTC_BULL | 15 | 73.33% | 16.43% | -4.65% | 53.61% | 66.67% | 22.49% | 69.27% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 100.00% | 11.52% | 0.00% | 40.55% | 100.00% | 26.79% | 67.27% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 12.72% | -1.80% | 15.10% | 100.00% | 8.35% | 15.10% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 13.44% | -2.60% | 46.96% | 75.00% | 46.17% | 74.60% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 69.57% | 12.42% | -13.75% | 24.22% | 43.48% | -5.90% | 54.01% |
| DOGE-USD | HISTORICAL_BTC_BULL | 14 | 50.00% | 3.43% | -10.81% | 29.09% | 50.00% | -0.62% | 58.63% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -21.24% | -23.02% | 5.25% | 33.33% | -13.39% | 53.01% |
| SOL-USD | HISTORICAL_BTC_BEAR | 16 | 87.50% | 7.50% | -4.27% | 23.20% | 50.00% | 6.29% | 123.97% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 40.00% | -9.01% | -12.06% | 35.69% | 40.00% | -4.39% | 44.48% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 100.00% | 20.80% | 0.00% | 58.01% | 100.00% | 73.90% | 165.00% |
| SOL-USD | HISTORICAL_BTC_MIXED | 2 | 100.00% | 8.54% | -3.33% | 10.41% | 50.00% | 1.19% | 10.49% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 8 | 50.00% | -3.75% | -9.33% | 26.66% | 50.00% | 0.11% | 35.87% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 22 | 90.91% | 8.72% | -4.18% | 41.86% | 50.00% | 5.88% | 60.11% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 80.00% | 13.07% | -4.43% | 48.48% | 70.00% | 18.80% | 60.70% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 63.84% | -4.76% | 106.37% | 100.00% | 36.55% | 106.37% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 11.93% | -1.80% | 20.37% | 57.14% | 6.11% | 36.02% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 21 | 76.19% | 16.16% | -10.52% | 24.43% | 47.62% | -5.58% | 63.02% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 7 | 42.86% | -19.26% | -23.02% | 32.10% | 57.14% | 14.84% | 77.67% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 43.62% | -10.62% | 46.98% | 100.00% | 14.59% | 69.28% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 20.00% | -18.04% | -23.36% | 16.65% | 20.00% | -21.90% | 21.84% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 23 | 73.91% | 7.22% | -4.80% | 23.99% | 47.83% | -0.20% | 92.05% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 25.82% | -5.84% | 64.03% | 50.00% | 139.84% | 274.74% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -2.05% | -10.61% | 43.70% | 50.00% | -2.35% | 53.40% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 5.72% | 0.00% | 13.71% | 100.00% | 14.78% | 16.85% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 10 | 70.00% | 10.80% | -3.33% | 26.99% | 60.00% | 4.35% | 42.16% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2025-12-31 | 90.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.65% | -1.42% | 9.89% | -13.09% | -18.65% | 10.41% |
| BTC-USD | ETH-USD | 2025-12-31 | 88.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.28% | 0.00% | 10.59% | -22.79% | -28.34% | 10.59% |
| BTC-USD | BTC-USD | 2018-10-15 | 88.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.70% | -5.69% | 10.97% | 11.96% | -5.69% | 14.92% |
| BTC-USD | BNB-USD | 2025-12-31 | 87.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| BTC-USD | SOL-USD | 2025-12-29 | 87.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| BTC-USD | BTC-USD | 2026-01-01 | 86.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.55% | -3.05% | 12.55% | -15.53% | -16.60% | 12.55% |
| BTC-USD | ETH-USD | 2018-07-11 | 86.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -14.43% | -14.43% | 7.43% | -53.22% | -58.54% | 7.43% |
| BTC-USD | XTZ-USD | 2025-12-31 | 86.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| BTC-USD | QTUM-USD | 2025-12-31 | 85.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.54% | -6.19% | 5.05% | -23.02% | -25.42% | 13.74% |
| BTC-USD | XTZ-USD | 2018-10-19 | 85.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 4.87% | -11.35% | 13.01% | 76.63% | -11.35% | 102.96% |
| DOGE-USD | OP-USD | 2026-01-01 | 91.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.98% | -7.10% | 49.82% | -15.88% | -18.56% | 49.82% |
| DOGE-USD | VET-USD | 2022-03-24 | 90.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.63% | -3.05% | 23.68% | 9.84% | -3.05% | 50.90% |
| DOGE-USD | LTC-USD | 2018-04-18 | 89.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -31.08% | -35.74% | 0.52% | -31.01% | -38.52% | 0.52% |
| DOGE-USD | HBAR-USD | 2022-03-24 | 89.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 23.41% | -3.18% | 23.41% | 3.08% | -3.18% | 34.66% |
| DOGE-USD | MKR-USD | 2022-10-04 | 89.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.99% | -0.27% | 24.02% | 41.98% | -0.27% | 48.95% |
| DOGE-USD | XTZ-USD | 2025-12-31 | 88.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| DOGE-USD | DASH-USD | 2022-03-17 | 88.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.39% | -22.75% | 0.95% | -6.32% | -22.75% | 9.96% |
| DOGE-USD | ADA-USD | 2022-03-22 | 88.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.42% | -10.22% | 12.42% | -7.62% | -10.22% | 22.52% |
| DOGE-USD | BAT-USD | 2018-10-19 | 88.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.64% | -16.39% | 17.64% | 80.49% | -16.39% | 80.49% |
| DOGE-USD | INJ-USD | 2022-03-24 | 88.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 20.22% | -1.35% | 21.97% | 28.58% | -1.35% | 76.25% |
| SOL-USD | ENJ-USD | 2018-10-14 | 80.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.62% | -25.10% | 11.62% | 465.84% | -25.10% | 542.51% |
| SOL-USD | EOS-USD | 2018-10-29 | 79.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 58.60% | -1.80% | 78.67% | 123.88% | -1.80% | 123.88% |
| SOL-USD | RUNE-USD | 2026-01-01 | 79.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 51.69% | -4.54% | 51.69% | -3.02% | -20.45% | 56.14% |
| SOL-USD | QTUM-USD | 2018-10-19 | 78.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.74% | -15.73% | 15.32% | 25.81% | -15.73% | 31.28% |
| SOL-USD | SOL-USD | 2025-12-29 | 78.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| SOL-USD | NEAR-USD | 2025-12-26 | 78.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 0.47% | -0.75% | 14.11% | 124.27% | -0.75% | 124.27% |
| SOL-USD | BNB-USD | 2025-12-31 | 78.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| SOL-USD | DOT-USD | 2025-12-26 | 77.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.89% | -6.91% | 6.75% | -11.84% | -13.97% | 10.44% |
| SOL-USD | KAVA-USD | 2025-12-31 | 77.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.73% | -3.48% | 25.59% | -18.69% | -20.93% | 27.22% |
| SOL-USD | LINK-USD | 2025-12-31 | 76.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.98% | -2.30% | 15.98% | -10.68% | -17.80% | 19.79% |

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

