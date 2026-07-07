# Technical Structure Report

Generated: 2026-07-07 21:58 UTC

This report adds classic technical-analysis structure to the scanner.

Included modules:

- MA20 / MA50 / MA200 trend structure
- Higher high / higher low versus lower high / lower low
- Double bottom, triple bottom, double top, triple top
- Adam and Eve bottom / top candidates
- RSI divergence and hidden RSI divergence
- MACD momentum
- OBV / CMF volume confirmation
- Simple Wyckoff phase candidate
- Technical confluence score

## Summary

| Asset   |       Price |   Score | Verdict        | Trend         | Momentum           | Structure           | Divergence             | Wyckoff                |     Support |   Resistance |
|:--------|------------:|--------:|:---------------|:--------------|:-------------------|:--------------------|:-----------------------|:-----------------------|------------:|-------------:|
| BTC     | 63366       |      -1 | NEUTRALE_MISTO | BEARISH_TREND | MOMENTUM_IMPROVING | LH_LL_DOWNSTRUCTURE | BULLISH_RSI_DIVERGENCE | ACCUMULATION_CANDIDATE | 57748       |  65544       |
| SOL     |    80.76    |      -3 | DEBOLE         | MIXED_TREND   | MOMENTUM_MIXED     | LH_LL_DOWNSTRUCTURE | NONE                   | RANGE_OR_UNKNOWN       |    64.42    |     87.79    |
| DOGE    |     0.07395 |      -5 | DEBOLE         | BEARISH_TREND | MOMENTUM_IMPROVING | LH_LL_DOWNSTRUCTURE | NONE                   | ACCUMULATION_CANDIDATE |     0.06961 |      0.09169 |

## Pattern snapshot

| Asset   | Double bottom   | Triple bottom   | Adam/Eve bottom     | Double top   | Triple top   | Adam/Eve top     |   Pattern score |
|:--------|:----------------|:----------------|:--------------------|:-------------|:-------------|:-----------------|----------------:|
| BTC     | POSSIBILE       | POSSIBILE       | ADAM_AND_EVE_BOTTOM | CONFERMATO   | CONFERMATO   | EVE_AND_ADAM_TOP |              -4 |
| SOL     | CONFERMATO      | POSSIBILE       | ADAM_AND_EVE_BOTTOM | CONFERMATO   | CONFERMATO   | ADAM_AND_EVE_TOP |              -2 |
| DOGE    | ASSENTE         | POSSIBILE       | ADAM_AND_EVE_BOTTOM | CONFERMATO   | CONFERMATO   | ADAM_AND_EVE_TOP |              -4 |

## Indicator snapshot

| Asset   |   RSI 14 |   MACD hist |        MA20 |        MA50 |       MA200 | MA50 slope 20d   | MA200 slope 60d   | Return 30d   | Return 90d   |
|:--------|---------:|------------:|------------:|------------:|------------:|:-----------------|:------------------|:-------------|:-------------|
| BTC     |    50.62 |   718.438   | 61873       | 66213       | 74483       | -9.22%           | -10.10%           | 0.44%        | -11.71%      |
| SOL     |    61.25 |     1.24589 |    74.51    |    75.16    |    92.92    | -6.59%           | -18.74%           | 20.91%       | -3.05%       |
| DOGE    |    34.24 |     0.00072 |     0.07714 |     0.08703 |     0.10244 | -12.71%          | -16.51%           | -14.30%      | -20.08%      |

## Asset details

### BTC

- Price: **63,366**
- Technical score: **-1 / 12**
- Verdict: **NEUTRALE_MISTO**
- Trend: **BEARISH_TREND** (-3)
- Momentum: **MOMENTUM_IMPROVING** (3)
- Volume: **ACCUMULATION_VOLUME** (2)
- Structure: **LH_LL_DOWNSTRUCTURE** (-2)
  - Last lows 5.808e+04->5.775e+04; last highs 6.725e+04->6.554e+04
- Divergence: **BULLISH_RSI_DIVERGENCE** (2)
- Wyckoff candidate: **ACCUMULATION_CANDIDATE** (1)
  - Below MA200, near lower 120d range, RSI 50.6
- Nearest support: **57,748**
- Nearest resistance: **65,544**

Classic patterns:

- Double bottom: **POSSIBILE**
  - Two similar lows near 57,748 between 2026-06-05 and 2026-07-01
- Triple bottom: **POSSIBILE**
  - Three similar lows near 57,748 from 2026-06-05 to 2026-07-01
- Adam/Eve bottom: **ADAM_AND_EVE_BOTTOM**
  - ADAM_AND_EVE_BOTTOM near 62,201 from 2026-03-29 to 2026-06-18
- Double top: **CONFERMATO**
  - Two similar highs near 79,488 between 2026-04-27 and 2026-05-26
- Triple top: **CONFERMATO**
  - Three similar highs near 79,468 from 2026-04-17 to 2026-05-26
- Adam/Eve top: **EVE_AND_ADAM_TOP**
  - EVE_AND_ADAM_TOP near 82,792 from 2026-04-22 to 2026-05-06

### SOL

- Price: **80.76**
- Technical score: **-3 / 12**
- Verdict: **DEBOLE**
- Trend: **MIXED_TREND** (-1)
- Momentum: **MOMENTUM_MIXED** (0)
- Volume: **ACCUMULATION_VOLUME** (2)
- Structure: **LH_LL_DOWNSTRUCTURE** (-2)
  - Last lows 67.92->64.42; last highs 75.94->74.89
- Divergence: **NONE** (0)
- Wyckoff candidate: **RANGE_OR_UNKNOWN** (0)
  - Position in 120d range: 53.75%
- Nearest support: **64.42**
- Nearest resistance: **87.79**

Classic patterns:

- Double bottom: **CONFERMATO**
  - Two similar lows near 60.41 between 2026-06-06 and 2026-06-25
- Triple bottom: **POSSIBILE**
  - Three similar lows near 81.41 from 2026-04-12 to 2026-05-23
- Adam/Eve bottom: **ADAM_AND_EVE_BOTTOM**
  - ADAM_AND_EVE_BOTTOM near 60.41 from 2026-06-06 to 2026-06-25
- Double top: **CONFERMATO**
  - Two similar highs near 88.05 between 2026-04-27 and 2026-05-21
- Triple top: **CONFERMATO**
  - Three similar highs near 89.26 from 2026-04-22 to 2026-05-21
- Adam/Eve top: **ADAM_AND_EVE_TOP**
  - ADAM_AND_EVE_TOP near 89.26 from 2026-04-22 to 2026-05-21

### DOGE

- Price: **0.07395**
- Technical score: **-5 / 12**
- Verdict: **DEBOLE**
- Trend: **BEARISH_TREND** (-3)
- Momentum: **MOMENTUM_IMPROVING** (2)
- Volume: **ACCUMULATION_VOLUME** (1)
- Structure: **LH_LL_DOWNSTRUCTURE** (-2)
  - Last lows 0.07809->0.06961; last highs 0.1183->0.09169
- Divergence: **NONE** (0)
- Wyckoff candidate: **ACCUMULATION_CANDIDATE** (1)
  - Below MA200, near lower 120d range, RSI 34.2
- Nearest support: **0.06961**
- Nearest resistance: **0.09169**

Classic patterns:

- Double bottom: **ASSENTE**
- Triple bottom: **POSSIBILE**
  - Three similar lows near 0.09274 from 2026-04-19 to 2026-05-28
- Adam/Eve bottom: **ADAM_AND_EVE_BOTTOM**
  - ADAM_AND_EVE_BOTTOM near 0.09274 from 2026-04-19 to 2026-05-23
- Double top: **CONFERMATO**
  - Two similar highs near 0.09584 between 2026-04-07 and 2026-06-12
- Triple top: **CONFERMATO**
  - Three similar highs near 0.10200 from 2026-03-25 to 2026-04-17
- Adam/Eve top: **ADAM_AND_EVE_TOP**
  - ADAM_AND_EVE_TOP near 0.09772 from 2026-03-25 to 2026-04-07

## How to read the score

- +7 to +12: strong technical bullish confluence.
- +3 to +6: constructive, but still needs confirmation.
- -2 to +2: mixed / neutral.
- -6 to -3: weak technical structure.
- -12 to -7: strong technical bearish confluence.

Important: this is not a prediction by itself. It is a technical confluence filter to combine with the fractal scanner, market regime, futures and RSI reports.

