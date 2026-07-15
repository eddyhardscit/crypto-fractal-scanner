# Market Regime Match Report

Generated: 2026-07-15 07:26 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.596 $ | False | -14.07% | -10.08% | BEAR | -14.07% | -10.08% |
| DOGE-USD | BEAR | 0.07409 $ | False | -25.36% | -16.26% | BEAR | -14.07% | -10.08% |
| SOL-USD | BEAR | 77,68 $ | False | -12.71% | -17.83% | BEAR | -14.07% | -10.08% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 65.00% | 7.47% | 16.61% | 31.52% | -8.29% | -25.97% | 11.70% | 19.71% | 44.67% | 65.00% | 22.43% | 40.84% | 72.75% |
| BTC-USD | SAME_BTC_REGIME | 11 | 100.00% | 25.26% | 39.26% | 41.99% | -4.62% | -8.95% | 28.30% | 47.44% | 56.93% | 72.73% | 10.19% | 32.39% | 40.43% |
| BTC-USD | SAME_ASSET_REGIME | 24 | 91.67% | 14.42% | 22.83% | 36.61% | -7.00% | -11.13% | 15.25% | 26.02% | 48.83% | 83.33% | 29.75% | 47.23% | 87.84% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 9 | 100.00% | 25.26% | 39.15% | 46.88% | -4.79% | -9.21% | 28.30% | 43.98% | 54.01% | 77.78% | 10.19% | 26.22% | 57.42% |
| DOGE-USD | ALL_MATCHES | 40 | 20.00% | -16.61% | -7.35% | 7.89% | -26.76% | -44.62% | 3.22% | 13.62% | 25.28% | 42.50% | -1.37% | 22.69% | 40.52% |
| DOGE-USD | SAME_BTC_REGIME | 32 | 15.62% | -18.74% | -11.65% | 6.19% | -28.79% | -44.48% | 1.51% | 11.23% | 25.08% | 40.62% | -1.37% | 14.47% | 25.82% |
| DOGE-USD | SAME_ASSET_REGIME | 34 | 20.59% | -17.15% | -8.35% | 14.94% | -27.62% | -44.46% | 3.22% | 11.69% | 25.38% | 44.12% | -1.03% | 21.89% | 38.60% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 30 | 13.33% | -20.94% | -12.27% | 6.57% | -28.79% | -44.62% | 1.51% | 10.94% | 25.28% | 36.67% | -3.19% | 9.14% | 25.49% |
| SOL-USD | ALL_MATCHES | 40 | 55.00% | 2.23% | 17.58% | 28.87% | -8.17% | -23.82% | 8.31% | 23.00% | 44.97% | 65.00% | 5.68% | 26.74% | 41.54% |
| SOL-USD | SAME_BTC_REGIME | 23 | 60.87% | 2.99% | 14.71% | 26.96% | -7.43% | -17.23% | 8.37% | 20.70% | 41.72% | 65.22% | 5.04% | 14.85% | 38.20% |
| SOL-USD | SAME_ASSET_REGIME | 28 | 64.29% | 5.52% | 13.33% | 29.12% | -7.97% | -18.18% | 10.65% | 21.81% | 46.02% | 71.43% | 7.29% | 26.74% | 42.45% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 63.16% | 2.99% | 10.94% | 21.62% | -7.43% | -14.75% | 8.37% | 17.01% | 33.55% | 68.42% | 5.04% | 13.46% | 37.17% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 11 | 100.00% | 25.26% | -4.62% | 47.44% | 72.73% | 10.19% | 64.59% |
| BTC-USD | HISTORICAL_BTC_BULL | 19 | 57.89% | 4.86% | -8.94% | 13.94% | 73.68% | 26.74% | 57.38% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 11.31% | -6.15% | 12.74% | 100.00% | 56.16% | 145.55% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 25.00% | -12.97% | -13.30% | 12.00% | 25.00% | -18.88% | 31.68% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 32 | 15.62% | -18.74% | -28.79% | 11.23% | 40.62% | -1.37% | 26.04% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 50.00% | 1.45% | -6.16% | 18.88% | 50.00% | 5.16% | 73.12% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -11.61% | -17.84% | 15.09% | 50.00% | 10.81% | 32.11% |
| SOL-USD | HISTORICAL_BTC_BEAR | 23 | 60.87% | 2.99% | -7.43% | 20.70% | 65.22% | 5.04% | 41.42% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -6.02% | -16.92% | 11.57% | 66.67% | 12.43% | 33.76% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 8 | 50.00% | 5.57% | -8.31% | 37.88% | 62.50% | 23.56% | 118.29% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 24 | 91.67% | 14.42% | -7.00% | 26.02% | 83.33% | 29.75% | 66.06% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 22.22% | -16.88% | -20.68% | 11.82% | 55.56% | 2.96% | 32.74% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -10.81% | -11.48% | 13.16% | 14.29% | -27.44% | 13.34% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 20.59% | -17.15% | -27.62% | 11.69% | 44.12% | -1.03% | 35.55% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -24.46% | -25.29% | 13.57% | 0.00% | -33.00% | 13.57% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -15.30% | -28.11% | 0.44% | 50.00% | 0.55% | 20.10% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -3.41% | -15.15% | 21.93% | 50.00% | 29.03% | 61.99% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 64.29% | 5.52% | -7.97% | 21.81% | 71.43% | 7.29% | 51.49% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 0.00% | -13.24% | -24.49% | 2.06% | 50.00% | -0.20% | 5.61% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -4.00% | -9.19% | 0.80% | 0.00% | -0.43% | 5.57% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 17.93% | -0.01% | 31.47% | 57.14% | 13.23% | 54.26% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-09-29 | 88.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| BTC-USD | ONE-USD | 2020-01-12 | 87.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |
| BTC-USD | XLM-USD | 2020-01-12 | 85.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| BTC-USD | TRX-USD | 2020-01-12 | 85.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.85% | 0.00% | 30.82% | 26.22% | 0.00% | 45.23% |
| BTC-USD | KSM-USD | 2022-03-15 | 85.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 28.30% | -10.24% | 28.30% | -2.40% | -10.24% | 29.36% |
| BTC-USD | ZEC-USD | 2020-01-12 | 84.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.12% | -6.11% | 14.56% | 20.62% | -6.11% | 29.97% |
| BTC-USD | ADA-USD | 2020-01-12 | 84.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 66.41% | 0.00% | 66.41% | 132.91% | 0.00% | 160.41% |
| BTC-USD | ETH-USD | 2025-12-06 | 84.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.70% | -8.95% | 8.87% | 4.75% | -8.95% | 11.19% |
| BTC-USD | BAT-USD | 2019-10-04 | 84.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.15% | -1.02% | 43.98% | 5.38% | -1.02% | 63.91% |
| BTC-USD | EOS-USD | 2020-01-12 | 85.40% | BEAR | RECOVERY | SAME_BTC_ONLY | MIXED | 2.83% | -4.62% | 19.52% | -0.79% | -4.62% | 19.52% |
| DOGE-USD | DASH-USD | 2022-02-25 | 89.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | XRP-USD | 2019-09-29 | 88.34% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 88.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | VET-USD | 2022-02-27 | 87.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | INJ-USD | 2022-02-27 | 87.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -37.21% | -41.89% | 0.00% | -21.93% | -42.67% | 0.00% |
| DOGE-USD | ENJ-USD | 2022-03-02 | 87.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.40% | -33.49% | 0.00% | 12.28% | -33.49% | 13.74% |
| DOGE-USD | THETA-USD | 2022-03-01 | 87.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.39% | -17.72% | 11.00% | 25.45% | -17.98% | 25.45% |
| DOGE-USD | 1INCH-USD | 2022-02-27 | 87.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.47% | -36.99% | 0.00% | -5.00% | -36.99% | 0.00% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | CHZ-USD | 2022-03-01 | 87.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -15.78% | -27.66% | 0.00% | 25.86% | -27.66% | 25.86% |
| SOL-USD | XLM-USD | 2020-01-12 | 80.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| SOL-USD | NEAR-USD | 2025-12-06 | 79.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.76% | -13.93% | 10.53% | 16.47% | -13.93% | 18.85% |
| SOL-USD | RUNE-USD | 2025-12-12 | 79.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.99% | -7.87% | 5.19% | 5.91% | -7.87% | 53.05% |
| SOL-USD | SOL-USD | 2025-12-09 | 79.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.32% | -12.34% | 1.82% | -5.43% | -12.34% | 8.09% |
| SOL-USD | XRP-USD | 2020-01-12 | 78.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.93% | 0.00% | 23.95% | 1.80% | 0.00% | 23.95% |
| SOL-USD | LINK-USD | 2025-12-06 | 77.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.84% | -11.36% | 4.69% | 10.45% | -11.36% | 12.98% |
| SOL-USD | AVAX-USD | 2025-12-07 | 77.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.07% | -18.05% | 0.00% | -9.08% | -18.05% | 0.00% |
| SOL-USD | APT-USD | 2024-09-06 | 77.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | OMG-USD | 2025-12-11 | 76.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.97% | -5.71% | 8.37% | 4.15% | -5.71% | 17.41% |
| SOL-USD | BNB-USD | 2020-01-12 | 76.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.95% | 0.00% | 16.57% | 5.45% | 0.00% | 18.76% |

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

