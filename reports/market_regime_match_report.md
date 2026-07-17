# Market Regime Match Report

Generated: 2026-07-17 00:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.741 $ | False | -15.94% | -9.87% | BEAR | -15.94% | -9.87% |
| DOGE-USD | BEAR | 0.07229 $ | False | -23.90% | -15.91% | BEAR | -15.94% | -9.87% |
| SOL-USD | BEAR | 75,28 $ | False | -12.80% | -17.28% | BEAR | -15.94% | -9.87% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 3.78% | 14.99% | 26.62% | -8.93% | -27.71% | 11.16% | 19.92% | 31.20% | 62.50% | 9.19% | 32.46% | 46.50% |
| BTC-USD | SAME_BTC_REGIME | 8 | 100.00% | 22.55% | 31.72% | 43.63% | -2.31% | -8.32% | 26.78% | 35.84% | 53.52% | 62.50% | 7.36% | 22.02% | 29.92% |
| BTC-USD | SAME_ASSET_REGIME | 20 | 90.00% | 14.42% | 25.55% | 31.81% | -8.09% | -12.97% | 16.23% | 28.68% | 51.78% | 80.00% | 26.46% | 39.55% | 55.29% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 7 | 100.00% | 25.26% | 35.15% | 44.17% | 0.00% | -8.59% | 28.30% | 40.87% | 54.40% | 71.43% | 10.19% | 23.42% | 31.15% |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -16.78% | 3.16% | 18.73% | -24.45% | -41.93% | 2.22% | 16.13% | 26.85% | 55.00% | 2.45% | 24.52% | 35.79% |
| DOGE-USD | SAME_BTC_REGIME | 33 | 21.21% | -18.05% | -8.77% | 6.69% | -27.58% | -42.18% | 1.05% | 14.45% | 25.39% | 51.52% | 0.39% | 12.28% | 25.78% |
| DOGE-USD | SAME_ASSET_REGIME | 36 | 27.78% | -17.12% | 4.17% | 19.79% | -25.14% | -42.07% | 2.22% | 15.42% | 29.22% | 55.56% | 2.45% | 23.00% | 34.42% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 31 | 19.35% | -19.37% | -9.58% | 6.72% | -27.58% | -42.25% | 1.05% | 12.72% | 25.42% | 48.39% | -0.80% | 9.91% | 25.45% |
| SOL-USD | ALL_MATCHES | 40 | 42.50% | -3.09% | 10.08% | 20.29% | -11.85% | -27.92% | 7.90% | 17.56% | 35.63% | 57.50% | 3.05% | 24.56% | 37.02% |
| SOL-USD | SAME_BTC_REGIME | 17 | 47.06% | -1.32% | 4.73% | 21.31% | -11.36% | -20.55% | 6.41% | 10.53% | 32.21% | 58.82% | 1.80% | 8.83% | 23.87% |
| SOL-USD | SAME_ASSET_REGIME | 24 | 54.17% | 1.11% | 10.84% | 30.48% | -8.39% | -22.00% | 8.87% | 20.68% | 48.17% | 66.67% | 5.48% | 26.74% | 38.04% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 15 | 53.33% | 0.76% | 5.35% | 27.00% | -11.36% | -18.65% | 6.41% | 12.28% | 36.34% | 66.67% | 4.15% | 9.64% | 27.56% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 8 | 100.00% | 22.55% | -2.31% | 35.84% | 62.50% | 7.36% | 53.27% |
| BTC-USD | HISTORICAL_BTC_BULL | 21 | 52.38% | 0.90% | -11.52% | 11.57% | 71.43% | 24.24% | 50.97% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 11 | 36.36% | -7.80% | -10.29% | 14.95% | 45.45% | -10.32% | 71.01% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 33 | 21.21% | -18.05% | -27.58% | 14.45% | 51.52% | 0.39% | 25.86% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 75.00% | 11.09% | -6.16% | 21.06% | 75.00% | 42.50% | 99.06% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -18.14% | -23.06% | 44.23% | 66.67% | 29.01% | 50.99% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 47.06% | -1.32% | -11.36% | 10.53% | 58.82% | 1.80% | 23.95% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 20.00% | -11.50% | -21.36% | 10.86% | 50.00% | 0.82% | 15.56% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 53.85% | 4.38% | -8.08% | 25.06% | 61.54% | 23.83% | 99.95% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 90.00% | 14.42% | -8.09% | 28.68% | 80.00% | 26.46% | 61.04% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 18.18% | -16.88% | -20.68% | 4.01% | 54.55% | 1.96% | 24.15% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -2.17% | -8.30% | 7.94% | 100.00% | 33.68% | 99.95% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 37.50% | -8.92% | -10.89% | 14.80% | 25.00% | -23.47% | 14.83% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 27.78% | -17.12% | -25.14% | 15.42% | 55.56% | 2.45% | 38.40% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -15.30% | -28.11% | 0.44% | 50.00% | 0.55% | 20.10% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -7.58% | -15.80% | 21.43% | 50.00% | 28.11% | 61.50% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 24 | 54.17% | 1.11% | -8.39% | 20.68% | 66.67% | 5.48% | 50.01% |
| SOL-USD | HISTORICAL_ASSET_BULL | 8 | 0.00% | -13.24% | -22.35% | 4.68% | 37.50% | -0.84% | 9.65% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -4.00% | -9.19% | 0.80% | 0.00% | -0.43% | 5.57% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 4.99% | -4.53% | 20.78% | 100.00% | 34.99% | 85.23% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 4.38% | -2.69% | 23.27% | 40.00% | -19.51% | 46.63% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-09-29 | 87.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| BTC-USD | XLM-USD | 2020-01-12 | 85.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| BTC-USD | LTC-USD | 2020-01-12 | 85.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.19% | 0.00% | 21.14% | 4.53% | 0.00% | 21.14% |
| BTC-USD | ZEC-USD | 2020-01-12 | 85.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.12% | -6.11% | 14.56% | 20.62% | -6.11% | 29.97% |
| BTC-USD | XLM-USD | 2019-10-09 | 85.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 47.44% | 0.00% | 59.63% | -34.58% | -37.78% | 59.63% |
| BTC-USD | KSM-USD | 2022-03-15 | 84.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 28.30% | -10.24% | 28.30% | -2.40% | -10.24% | 29.36% |
| BTC-USD | TRX-USD | 2020-01-12 | 84.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.85% | 0.00% | 30.82% | 26.22% | 0.00% | 45.23% |
| BTC-USD | EOS-USD | 2020-01-12 | 85.14% | BEAR | RECOVERY | SAME_BTC_ONLY | MIXED | 2.83% | -4.62% | 19.52% | -0.79% | -4.62% | 19.52% |
| BTC-USD | LRC-USD | 2018-09-24 | 91.05% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 30.68% | -8.53% | 146.68% | 36.85% | -8.53% | 146.68% |
| BTC-USD | FIL-USD | 2023-06-24 | 89.06% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 10.53% | -8.25% | 11.57% | 26.74% | -8.25% | 50.97% |
| DOGE-USD | DASH-USD | 2022-02-25 | 89.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | XRP-USD | 2019-09-29 | 88.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| DOGE-USD | ENJ-USD | 2022-03-02 | 87.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.40% | -33.49% | 0.00% | 12.28% | -33.49% | 13.74% |
| DOGE-USD | VET-USD | 2022-03-04 | 87.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.06% | -21.27% | 0.00% | 18.68% | -22.08% | 18.68% |
| DOGE-USD | INJ-USD | 2022-02-27 | 87.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -37.21% | -41.89% | 0.00% | -21.93% | -42.67% | 0.00% |
| DOGE-USD | 1INCH-USD | 2022-02-27 | 87.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.47% | -36.99% | 0.00% | -5.00% | -36.99% | 0.00% |
| DOGE-USD | OP-USD | 2025-12-12 | 87.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -13.30% | 14.55% | 9.63% | -13.30% | 46.69% |
| DOGE-USD | OMG-USD | 2022-03-02 | 87.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.92% | -36.72% | 0.00% | -11.78% | -39.47% | 0.00% |
| DOGE-USD | THETA-USD | 2022-03-01 | 87.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.39% | -17.72% | 11.00% | 25.45% | -17.98% | 25.45% |
| DOGE-USD | ETH-USD | 2022-03-02 | 87.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.01% | -44.48% | 0.00% | -0.80% | -44.48% | 0.00% |
| SOL-USD | RUNE-USD | 2025-12-12 | 79.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.99% | -7.87% | 5.19% | 5.91% | -7.87% | 53.05% |
| SOL-USD | SOL-USD | 2025-12-09 | 79.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.32% | -12.34% | 1.82% | -5.43% | -12.34% | 8.09% |
| SOL-USD | XLM-USD | 2020-01-12 | 79.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| SOL-USD | NEAR-USD | 2025-12-06 | 77.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.76% | -13.93% | 10.53% | 16.47% | -13.93% | 18.85% |
| SOL-USD | BTC-USD | 2025-12-11 | 76.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.73% | -6.48% | 9.36% | 8.83% | -6.48% | 16.47% |
| SOL-USD | APT-USD | 2024-09-11 | 76.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.26% | -23.26% | 3.72% | -33.02% | -33.49% | 3.72% |
| SOL-USD | LINK-USD | 2025-12-06 | 76.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.84% | -11.36% | 4.69% | 10.45% | -11.36% | 12.98% |
| SOL-USD | XRP-USD | 2020-01-12 | 76.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.93% | 0.00% | 23.95% | 1.80% | 0.00% | 23.95% |
| SOL-USD | OMG-USD | 2025-12-11 | 76.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.97% | -5.71% | 8.37% | 4.15% | -5.71% | 17.41% |
| SOL-USD | DOT-USD | 2025-12-06 | 76.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -19.05% | -19.05% | 14.02% | -5.32% | -19.05% | 14.02% |

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

