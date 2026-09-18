# Paper trading automatico KuCoin

Generato: 2026-09-18T01:16:35+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-18T01:06:27+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-18T01:06:27+00:00 | 2026-09-18T01:06:27+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-18T00:45:00+00:00 | 2026-09-18T00:45:00+00:00 | 7,0 min | 25,0 min | OK |
| 60m | 12 | 2026-09-18T00:00:00+00:00 | 2026-09-18T00:00:00+00:00 | 7,0 min | 45,0 min | OK |
| 240m | 12 | 2026-09-17T20:00:00+00:00 | 2026-09-17T20:00:00+00:00 | 1,12 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bilanciata V3 · LONG only | HYPE | 60m | LONG | 6,22 | 6,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| FAST NoHigh <7,5 · SHORT only | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Regime Guard | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Regime Guard | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Loss Cap 0,75R | NEAR | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Loss Cap 0,75R | ARB | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — 50% a 0,75R | NEAR | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — 50% a 0,75R | ARB | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Breakeven 0,5R | NEAR | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Breakeven 0,5R | ARB | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | NEAR | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | ARB | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | NEAR | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | ARB | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Expanded V1 | NEAR | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Expanded V1 | ARB | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | NEAR | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | ARB | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — target pieno 3R | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — target pieno 3R | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — target pieno 3R | BR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — target pieno 3R | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — parziale 1R | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | ZEC | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — MFE Trail esistente | ZEC | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — MFE Trail esistente | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — MFE Trail esistente | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — MFE Trail esistente | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — madre | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | ZEC | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 + MFE | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 + MFE | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | ZEC | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC≤3 | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC≤3 | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC≤3 | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard | ZEC | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | BR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | HYPE | 60m | LONG | 6,22 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | ARB | 60m | LONG | 7,75 | 4,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — qualità completa + profit lock | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — qualità completa + profit lock | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — qualità completa + profit lock | BR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Long Only | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Long Only | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long + no HIGH + score <7,5 | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long + no HIGH + score <7,5 | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long + no HIGH + score <7,5 | BR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long Only | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long Only | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — no volatilità HIGH | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — no volatilità HIGH | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — score <7,5 | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — senza PEPE | NEAR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — no HIGH + score <7,5 | HYPE | 60m | LONG | 6,22 | 4,50 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida score 6–7,5 — Cost Aware | HYPE | 60m | LONG | 6,22 | 6,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida score 6–7,5 — senza Trend Up | HYPE | 60m | LONG | 6,22 | 6,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — score 6–7,5 | HYPE | 60m | LONG | 6,22 | 6,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | HYPE | 60m | LONG | 6,22 | 6,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H — LONG senza Range High Vol | ZEC | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H — LONG senza Range High Vol | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H — LONG senza Range High Vol | BR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H — LONG senza Range High Vol | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | ARB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 7,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BR | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ONE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | NEAR | 240m | LONG | 7,25 | 6,00 | 0,00 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ARB | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,67 | 6,00 | 1,33 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -4,14 | 6,00 | 1,86 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | POWER | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 2,57 | 6,00 | 3,43 | STALE_CANDLE | 1,12 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,60 | 6,00 | 4,40 | STALE_CANDLE | 1,12 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,12 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,38 | 6,00 | 5,62 | STALE_CANDLE | 1,12 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 67.0 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | ONE | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H — LONG senza Range High Vol | ONE | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | ONE | 60m | LONG | 8,25 | 5,50 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | ONE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | ONE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered — madre | ONE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — no volatilità HIGH | ONE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — Long Only | ONE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 7,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.788,59 | -2,11% | €-19,97 | €3.000,00 | -0,67% | 6 | 64 | 40,62% | 0,78 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 64 | 3865 | PRIME INDICAZIONI | 100 (mancano 36) |

- Trade del Principale 4H chiusi: **64**; win rate **40,62%**; profit factor **0,78**.
- Expectancy: **€-5,90** per trade; P&L netto: **€-377,40**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.788,59 | €712,23 | €2.136,68 | €102,80 | €167,29 |
| TEST | Benchmark Donchian breakout 1H | 1 | €12.187,80 | €496,10 | €992,20 | €59,93 | €39,79 |
| TEST | Donchian 1H Gb20 120R V1 | 1 | €11.900,85 | €484,42 | €968,84 | €58,52 | €38,85 |
| TEST | Combo Trend — Side × Regime Guard | 4 | €11.333,46 | €1.888,51 | €3.777,02 | €114,31 | €82,96 |
| TEST | Rapida score 6–7,5 — Cost Aware | 5 | €11.171,61 | €1.651,77 | €4.955,32 | €223,43 | €24,13 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 3 | €11.054,24 | €2.045,47 | €6.136,41 | €164,98 | €-23,89 |
| TEST | MAIN — Side × Regime Guard | 2 | €10.998,94 | €377,83 | €1.133,50 | €68,97 | €-1,28 |
| TEST | Rapida V3 NoHigh — Regime Guard | 5 | €10.702,60 | €1.538,86 | €4.616,57 | €214,05 | €6,23 |
| TEST | Rapida V1 — senza PEPE | 5 | €10.669,39 | €1.525,72 | €4.577,15 | €211,71 | €30,46 |
| TEST | Combo Adaptive — madre | 6 | €10.665,77 | €2.369,66 | €4.739,32 | €213,33 | €-13,20 |
| TEST | Rapida 1H V2 | 0 | €10.617,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 4 | €10.594,69 | €2.236,74 | €4.473,48 | €158,96 | €5,17 |
| TEST | Scanner Top15 Long | 5 | €10.526,93 | €2.352,42 | €4.704,83 | €210,55 | €-16,44 |
| TEST | Scanner Top20 Long | 5 | €10.526,93 | €2.352,42 | €4.704,83 | €210,55 | €-16,44 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €10.524,85 | €1.743,00 | €3.486,01 | €105,59 | €113,50 |
| TEST | Combo Adaptive — Long Only | 4 | €10.448,20 | €2.783,00 | €5.566,01 | €208,98 | €-1,11 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.443,12 | €1.501,55 | €4.504,66 | €208,86 | €6,08 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.376,02 | €1.491,91 | €4.475,72 | €207,52 | €6,04 |
| TEST | Combo Adaptive — parziale 1R | 5 | €10.340,05 | €2.303,37 | €4.606,74 | €205,83 | €-16,02 |
| TEST | Rapida V1 — target pieno 2R | 4 | €10.333,49 | €1.011,89 | €3.035,67 | €154,13 | €29,89 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.264,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.235,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.205,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.203,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.202,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.180,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.175,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €10.121,03 | €1.455,28 | €4.365,84 | €202,42 | €5,89 |
| TEST | Combo Scanner | 4 | €10.106,51 | €2.691,74 | €5.383,48 | €202,17 | €-1,08 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 5 | €10.080,63 | €1.499,37 | €4.498,10 | €201,61 | €21,92 |
| TEST | Forza relativa 1H V2 | 4 | €10.071,79 | €1.689,33 | €3.378,66 | €149,64 | €86,17 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.058,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.020,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.019,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.011,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.011,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.010,33 | €1.504,77 | €4.514,32 | €149,09 | €34,76 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 5 | €10.004,39 | €1.438,47 | €4.315,41 | €200,09 | €5,82 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.002,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.002,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.993,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.988,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.985,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.982,95 | €286,89 | €573,77 | €54,81 | €-1,75 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €9.967,76 | €2.339,63 | €4.679,25 | €194,20 | €5,68 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.966,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €9.960,21 | €2.096,96 | €4.193,92 | €149,44 | €4,05 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.956,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.955,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.951,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.940,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.939,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.934,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.927,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.912,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.897,12 | €2.577,23 | €5.154,47 | €148,81 | €71,40 |
| TEST | Sol Ema 1H | 0 | €9.874,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.868,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 5 | €9.829,56 | €1.462,02 | €4.386,06 | €196,59 | €21,37 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.791,86 | €1.407,91 | €4.223,74 | €195,84 | €5,70 |
| TEST | Eth Ema 4H | 0 | €9.783,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.779,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.775,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.761,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.676,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 5 | €9.652,45 | €1.387,87 | €4.163,60 | €193,05 | €5,62 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.601,91 | €1.556,85 | €4.670,55 | €144,07 | €-0,93 |
| TEST | Combo Trend | 5 | €9.597,60 | €2.499,24 | €4.998,48 | €144,31 | €69,23 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.591,64 | €1.555,18 | €4.665,55 | €143,92 | €-0,93 |
| TEST | Bilanciata 1H V2 | 3 | €9.584,90 | €731,42 | €2.194,25 | €142,89 | €28,34 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 3 | €9.567,75 | €1.109,72 | €2.219,45 | €142,86 | €8,83 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 5 | €9.547,46 | €1.420,45 | €4.261,35 | €190,95 | €20,78 |
| TEST | Combo Adaptive — Trend/Transition | 0 | €9.543,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom15 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom20 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 5 | €9.508,08 | €1.414,59 | €4.243,78 | €190,16 | €20,69 |
| TEST | Bilanciata V3 · LONG only | 4 | €9.470,83 | €1.423,67 | €4.271,02 | €141,05 | €32,88 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 0 | €9.464,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.459,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €9.456,91 | €2.313,96 | €4.627,93 | €141,89 | €48,55 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 4 | €9.451,38 | €2.312,61 | €4.625,22 | €141,81 | €48,52 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 0 | €9.450,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.414,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 4 | €9.397,39 | €2.502,87 | €5.005,75 | €187,98 | €-1,00 |
| TEST | Scanner Bottom 5 Short 1H | 0 | €9.377,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.353,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €9.348,35 | €1.131,22 | €3.393,67 | €186,97 | €-0,68 |
| TEST | Top 5 + BTC — solo MFE | 4 | €9.337,21 | €1.965,80 | €3.931,59 | €140,09 | €3,80 |
| TEST | Bilanciata 1H V1 | 5 | €9.222,28 | €1.327,45 | €3.982,36 | €138,07 | €59,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 2 | €9.218,82 | €889,81 | €1.779,62 | €92,20 | €-0,36 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 2 | €9.209,01 | €888,86 | €1.777,73 | €92,10 | €-0,36 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.178,84 | €2.444,67 | €4.889,34 | €183,61 | €-0,98 |
| TEST | Master Adaptive V1 | 2 | €9.173,39 | €885,42 | €1.770,85 | €91,74 | €-0,35 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.158,43 | €1.273,07 | €2.546,14 | €131,16 | €54,12 |
| TEST | Rapida V3 — score <7,5 | 5 | €9.111,39 | €1.362,05 | €4.086,16 | €182,23 | €19,96 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.052,35 | €873,74 | €1.747,48 | €90,53 | €-0,35 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 5 | €9.038,73 | €2.121,83 | €4.243,65 | €180,78 | €-1,57 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €9.035,10 | €2.406,61 | €4.813,21 | €180,71 | €-0,96 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.014,99 | €664,35 | €1.328,69 | €89,77 | €-15,08 |
| TEST | Master Adaptive Expanded V1 | 2 | €8.984,25 | €867,17 | €1.734,34 | €89,85 | €-0,35 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €8.974,47 | €406,98 | €1.220,95 | €44,66 | €-18,85 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 2 | €8.926,87 | €1.148,89 | €2.297,77 | €89,28 | €-0,46 |
| TEST | Combo Adaptive — target pieno 3R | 5 | €8.869,64 | €2.082,13 | €4.164,27 | €177,40 | €-1,54 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €8.649,11 | €2.159,27 | €4.318,55 | €129,77 | €50,35 |
| TEST | Forza relativa 1H V1 | 5 | €8.557,95 | €1.906,03 | €3.812,05 | €171,17 | €-10,85 |
| TEST | Combo Mean Reversion | 1 | €8.548,94 | €653,10 | €1.306,20 | €43,35 | €18,04 |
| TEST | Master Adaptive Strict3 V1 | 0 | €8.448,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €8.413,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 4 | €8.242,60 | €2.072,64 | €4.145,29 | €123,67 | €50,04 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €8.207,89 | €2.040,88 | €4.081,76 | €123,15 | €46,64 |
| TEST | Benchmark Bollinger mean reversion 1H | 4 | €8.073,47 | €2.632,22 | €5.264,43 | €161,50 | €-4,57 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | Solo Long della Bilanciata 1H; esclude esattamente RANGE_HIGH_VOL. |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | Solo Short con regime esatto TREND_DOWN, BTC trend score ≤ -2 e score minimo 6. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | Madre Rapida 1H V1 originale, invariata. |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | Accetta soltanto score assoluti da 6,0 a meno di 7,5. |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | Mantiene score 6–7,5 ma esclude TREND_UP e TREND_UP_HIGH_VOL. |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | Opera solo nei regimi esatti RANGE e RANGE_LOW_VOL. |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | Richiede target lordo almeno 2 volte i costi round-trip stimati e slippage massimo 2 bps. |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | Esclude volatilità HIGH e score assoluti almeno 7,5. |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | Solo Long, BTC trend score 1–3 e score assoluto sotto 7,5. |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | Stessa madre, ma esclude PEPE. |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | Stessi ingressi della madre con target portato da 1,5R a 2R. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | Madre Rapida 1H V3 Filtered originale, invariata. |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | Mantiene il filtro V3 ed esclude score assoluti almeno 7,5. |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | Mantiene il filtro V3 ed esclude volatilità HIGH. |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | Mantiene il filtro V3 e accetta soltanto segnali Long. |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | Combina Long Only, esclusione HIGH e score sotto 7,5. |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | Mantiene il filtro V3 ed esclude ESPORTS. |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | Replica la variante senza ESPORTS accettando soltanto segnali Long. |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | Aggiunge breakeven a 0,75R, lock 0,25R da 1R e giveback dinamico dopo 1,25R. |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | Esclude regimi e volatilità HIGH, ATR oltre 3% e asset con slippage stimato oltre 2 bps. |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | Combina i filtri di qualità e protegge +0,25R dopo il raggiungimento di +1R, dalla candela successiva. |
| TEST | Ampia 4H | Confluenza trend | Test a 4 ore con stop più ampio, leva inferiore e durata maggiore. |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | Versione originale V1 a 1 ora basata sulla forza o debolezza rispetto a Bitcoin. |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | Versione V2 più selettiva: forza vs BTC, trend USDT, RSI, ADX, regime e massimo due segnali per direzione nella stessa candela. |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 15 e conferma il recupero verso 20. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 20 e conferma il recupero verso 25. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 25 e conferma il recupero verso 30. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 15 e conferma il recupero verso 20. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 20 e conferma il recupero verso 25. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 25 e conferma il recupero verso 30. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 15 e conferma il recupero verso 20. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 20 e conferma il recupero verso 25. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 25 e conferma il recupero verso 30. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 85 e conferma il rientro verso 80. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 80 e conferma il rientro verso 75. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 75 e conferma il rientro verso 70. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 85 e conferma il rientro verso 80. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 80 e conferma il rientro verso 75. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 75 e conferma il rientro verso 70. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 85 e conferma il rientro verso 80. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 80 e conferma il rientro verso 75. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 75 e conferma il rientro verso 70. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | Benchmark puro: breakout o breakdown dei massimi/minimi delle 20 barre precedenti, con filtro ADX. |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | Benchmark puro: ritorno verso la media dopo uscita dalle Bollinger e conferma RSI estrema. |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | Benchmark puro: trend following con prezzo, EMA20, EMA50 e filtro ADX. |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | Opera long solo sulle cinque crypto più forti della classifica live KuCoin, con conferma tecnica. |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | Opera short solo sulle cinque crypto più deboli della classifica live KuCoin, con conferma tecnica. |
| TEST | Scanner Top10 Long | Scanner Top10 Long | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Top15 Long | Scanner Top15 Long | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Top20 Long | Scanner Top20 Long | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | Top 5 live KuCoin con conferma tecnica e forza relativa positiva contro Bitcoin. |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | Stessi ingressi della madre; protegge progressivamente il profitto tramite MFE. |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | Scarta score sotto 7 fuori dai regimi Range. |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | Accetta soltanto contesti con BTC trend score non superiore a 3. |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | Accetta soltanto BTC trend score compreso tra 2 e 3. |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | Combina filtro score/regime e protezione MFE. |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | Combina filtro score/regime e BTC trend score ≤3. |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | Combina Guard, BTC trend score ≤3 e protezione MFE. |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | Chiude il 75% a 2,2R e lascia il 25% verso 3R con profit lock a 2R. |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | Mantiene il 100% della posizione fino al target 3R. |
| TEST | Global Confluence puro 1H | Global Confluence puro | Opera soltanto quando Global Confluence, dati exchange e struttura tecnica sono allineati. |
| TEST | Combo Trend | Combo Trend | Portafoglio sperimentale separato. |
| TEST | Combo Mean Reversion | Combo Mean Reversion | Portafoglio sperimentale separato. |
| TEST | Combo Scanner | Combo Scanner | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive — madre | Combo Adaptive | Madre Combo Adaptive originale, invariata. |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | Variante MFE trailing già esistente; resta come confronto storico separato. |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | Accetta soltanto segnali con score assoluto almeno 7. |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | Opera soltanto nei regimi TREND_UP e TRANSITION. |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | Combina score assoluto almeno 7 con regimi Trend/Transition. |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | Accetta esclusivamente segnali Long. |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | Realizza il 50% della posizione a +1R e lascia correre il residuo. |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | Combina qualità, regime e presa parziale del 50% a +1R. |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | Chiude il 75% a 2R e lascia il 25% verso 3R con profit lock a 1,8R. |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | Mantiene il 100% della posizione fino al target 3R. |
| TEST | Btc Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Btc Ema 4H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Btc Adaptive 1H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Btc Adaptive 4H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Sol Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Sol Ema 4H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Sol Adaptive 1H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Sol Adaptive 4H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Eth Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Eth Ema 4H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Eth Adaptive 1H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Doge Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | Blocca soltanto i Long nei regimi ALT_ROTATION_DOWN, TREND_UP_HIGH_VOL e RANGE_HIGH_VOL; gli Short restano un controllo separato. Richiede target/costi almeno 2x. |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | Stessa entrata GB20; dalla candela successiva porta lo stop a breakeven dopo un MFE di almeno +0,5R. |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | Stessa entrata GB20; realizza il 50% a +0,75R e protegge il residuo a breakeven dalla candela successiva. |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | Stessa entrata e target monetario teorico della GB20; stop iniziale ridotto al 75% della distanza originaria e reward/risk compensato. |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | Replica NoHigh ma accetta esclusivamente RANGE e RANGE_LOW_VOL, con filtro cost-aware. |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | Replica NoHigh; blocca i Long in TREND_UP, TREND_UP_HIGH_VOL e ALT_ROTATION_DOWN, mantenendo gli Short come campione separato. |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | Replica MAIN e blocca soltanto LONG in ALT_ROTATION_UP e SHORT in RANGE; mantiene gli altri segmenti come controllo prospettico e applica un filtro cost-aware. |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | Replica MAIN Side × Regime Guard e usa un ranking adattivo degli asset: storico, recente, regime BTC, alpha residuo, esecuzione, stabilità, liquidità, esplorazione e isteresi. AKE/BANK/LAB sono riferimenti storici, non una whitelist. |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | Replica Combo Trend; blocca LONG in ALT_ROTATION_DOWN e RANGE_HIGH_VOL e SHORT in RANGE. Mantiene LONG in RANGE/TRANSITION/TREND_UP e SHORT in TRANSITION come test prospettico. |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | Challenger forward isolato: copia soltanto i segnali SHORT della variante FAST NoHigh score <7,5. Nessuna promozione automatica. |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | Challenger forward isolato: copia soltanto i segnali LONG della Bilanciata V3. Il regime viene registrato point-in-time, ma non viene usato come filtro finché il campione non è sufficiente. |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.788,59 | €-377,40 | 64 | 64 | 40,62% | 0,78 | €-5,90 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €12.187,80 | €2.148,61 | 173 | 173 | 45,66% | 1,61 | €12,42 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.900,85 | €1.862,58 | 141 | 141 | 44,68% | 1,71 | €13,21 | 6,75% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €11.333,46 | €1.252,77 | 166 | 166 | 51,20% | 1,42 | €7,55 | 10,10% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.171,61 | €1.150,45 | 217 | 217 | 49,31% | 1,27 | €5,30 | 7,95% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €11.054,24 | €1.081,81 | 189 | 189 | 49,21% | 1,29 | €5,72 | 5,29% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.998,94 | €1.000,64 | 63 | 63 | 55,56% | 1,94 | €15,88 | 7,33% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.702,60 | €643,43 | 189 | 188 | 49,21% | 1,22 | €3,40 | 5,24% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.669,39 | €640,78 | 305 | 304 | 43,93% | 1,13 | €2,10 | 9,28% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.665,77 | €681,81 | 234 | 234 | 47,01% | 1,20 | €2,91 | 8,17% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.617,99 | €617,99 | 92 | 82 | 48,91% | 1,28 | €6,72 | 3,89% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.594,69 | €592,20 | 198 | 198 | 44,44% | 1,17 | €2,99 | 8,85% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.526,93 | €546,19 | 224 | 224 | 48,21% | 1,16 | €2,44 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.526,93 | €546,19 | 224 | 224 | 48,21% | 1,16 | €2,44 | 10,31% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.524,85 | €413,44 | 184 | 184 | 44,57% | 1,13 | €2,25 | 11,68% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.448,20 | €452,65 | 194 | 194 | 44,85% | 1,14 | €2,33 | 7,78% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.443,12 | €439,74 | 243 | 243 | 49,38% | 1,11 | €1,81 | 9,50% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.376,02 | €372,67 | 287 | 287 | 44,95% | 1,07 | €1,30 | 9,48% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.340,05 | €358,83 | 192 | 192 | 45,83% | 1,13 | €1,87 | 8,69% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.333,49 | €305,43 | 296 | 296 | 40,20% | 1,06 | €1,03 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.264,13 | €264,13 | 26 | 26 | 38,46% | 1,36 | €10,16 | 3,39% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.235,99 | €235,99 | 23 | 23 | 56,52% | 1,56 | €10,26 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.205,57 | €205,57 | 121 | 121 | 42,15% | 1,08 | €1,70 | 7,07% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.203,50 | €203,50 | 9 | 9 | 77,78% | 2,77 | €22,61 | 0,85% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.202,44 | €202,44 | 20 | 20 | 60,00% | 1,43 | €10,12 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.180,44 | €180,44 | 31 | 31 | 61,29% | 1,28 | €5,82 | 2,77% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.175,88 | €175,88 | 77 | 77 | 44,16% | 1,11 | €2,28 | 6,49% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.121,03 | €113,54 | 214 | 213 | 44,86% | 1,04 | €0,53 | 7,10% |
| TEST | Combo Scanner | Combo Scanner | €10.106,51 | €110,81 | 197 | 197 | 43,65% | 1,03 | €0,56 | 11,38% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.080,63 | €61,41 | 231 | 231 | 42,42% | 1,01 | €0,27 | 10,86% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.071,79 | €-12,36 | 154 | 147 | 41,56% | 1,00 | €-0,08 | 10,88% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.058,95 | €58,95 | 34 | 34 | 47,06% | 1,40 | €1,73 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.020,29 | €20,29 | 7 | 7 | 57,14% | 1,71 | €2,90 | 0,31% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.019,53 | €19,53 | 12 | 12 | 50,00% | 1,39 | €1,63 | 0,36% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.011,79 | €11,79 | 34 | 34 | 47,06% | 1,40 | €0,35 | 0,07% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.011,55 | €11,55 | 19 | 19 | 42,11% | 1,20 | €0,61 | 0,53% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.010,33 | €-21,72 | 232 | 232 | 42,24% | 0,99 | €-0,09 | 14,04% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.004,39 | €1,15 | 277 | 277 | 42,24% | 1,00 | €0,00 | 10,60% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,06 | €4,06 | 7 | 7 | 57,14% | 1,71 | €0,58 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.002,31 | €2,31 | 19 | 19 | 42,11% | 1,20 | €0,12 | 0,11% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.002,17 | €2,17 | 15 | 15 | 40,00% | 1,01 | €0,14 | 1,80% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,71 | €-2,29 | 12 | 12 | 33,33% | 0,62 | €-0,19 | 0,04% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.993,20 | €-6,80 | 5 | 5 | 20,00% | 0,05 | €-1,36 | 0,07% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,19 | €-8,81 | 7 | 7 | 57,14% | 0,68 | €-1,26 | 0,30% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.988,57 | €-11,43 | 12 | 12 | 33,33% | 0,62 | €-0,95 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.985,57 | €-14,43 | 22 | 22 | 36,36% | 0,31 | €-0,66 | 0,17% |
| TEST | Ampia 4H | Confluenza trend | €9.982,95 | €-14,92 | 65 | 65 | 33,85% | 0,99 | €-0,23 | 4,45% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.967,76 | €-35,11 | 205 | 205 | 44,88% | 0,99 | €-0,17 | 10,31% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.966,02 | €-33,98 | 5 | 5 | 20,00% | 0,05 | €-6,80 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.960,21 | €-41,33 | 164 | 164 | 44,51% | 0,99 | €-0,25 | 11,27% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.956,17 | €-43,83 | 34 | 34 | 47,06% | 0,76 | €-1,29 | 0,84% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.955,89 | €-44,11 | 5 | 5 | 20,00% | 0,09 | €-8,82 | 0,45% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.951,01 | €-48,99 | 19 | 19 | 36,84% | 0,53 | €-2,58 | 0,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.940,92 | €-59,08 | 22 | 22 | 31,82% | 0,53 | €-2,69 | 0,73% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.939,78 | €-60,22 | 16 | 16 | 50,00% | 0,85 | €-3,76 | 1,98% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.934,84 | €-65,16 | 14 | 14 | 50,00% | 0,80 | €-4,65 | 2,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.927,87 | €-72,13 | 22 | 22 | 36,36% | 0,31 | €-3,28 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.912,62 | €-87,38 | 29 | 29 | 44,83% | 0,89 | €-3,01 | 4,59% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.897,12 | €-171,18 | 167 | 167 | 41,32% | 0,94 | €-1,03 | 12,31% |
| TEST | Sol Ema 1H | Trend following EMA | €9.874,85 | €-125,15 | 31 | 31 | 38,71% | 0,87 | €-4,04 | 4,45% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.868,16 | €-131,84 | 12 | 12 | 50,00% | 0,70 | €-10,99 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.829,56 | €-189,18 | 194 | 194 | 41,24% | 0,94 | €-0,98 | 10,86% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.791,86 | €-211,31 | 250 | 250 | 43,20% | 0,96 | €-0,85 | 10,92% |
| TEST | Eth Ema 4H | Trend following EMA | €9.783,14 | €-216,86 | 9 | 9 | 22,22% | 0,41 | €-24,10 | 2,32% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.779,96 | €-220,04 | 23 | 23 | 39,13% | 0,66 | €-9,57 | 3,93% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.775,84 | €-224,16 | 20 | 20 | 40,00% | 0,67 | €-11,21 | 3,48% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.761,07 | €-238,93 | 19 | 19 | 47,37% | 0,58 | €-12,58 | 3,13% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.676,47 | €-323,53 | 23 | 23 | 34,78% | 0,61 | €-14,07 | 4,65% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.652,45 | €-350,67 | 280 | 280 | 41,79% | 0,94 | €-1,25 | 12,52% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.601,91 | €-394,35 | 199 | 199 | 45,73% | 0,93 | €-1,98 | 8,44% |
| TEST | Combo Trend | Combo Trend | €9.597,60 | €-468,64 | 201 | 201 | 41,29% | 0,89 | €-2,33 | 14,08% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.591,64 | €-404,62 | 201 | 201 | 43,28% | 0,92 | €-2,01 | 6,64% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.584,90 | €-442,12 | 184 | 170 | 45,11% | 0,88 | €-2,40 | 11,82% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.567,75 | €-439,75 | 109 | 109 | 39,45% | 0,83 | €-4,03 | 8,88% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.547,46 | €-470,76 | 216 | 216 | 43,52% | 0,91 | €-2,18 | 15,94% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.543,88 | €-456,12 | 91 | 91 | 46,15% | 0,79 | €-5,01 | 6,28% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.508,08 | €-510,07 | 254 | 254 | 42,13% | 0,92 | €-2,01 | 15,64% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.470,83 | €-559,49 | 187 | 187 | 42,78% | 0,82 | €-2,99 | 13,79% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.464,68 | €-535,32 | 67 | 67 | 34,33% | 0,71 | €-7,99 | 9,08% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.459,83 | €-540,17 | 26 | 26 | 34,62% | 0,42 | €-20,78 | 5,44% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.456,91 | €-588,86 | 176 | 176 | 41,48% | 0,85 | €-3,35 | 11,91% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.451,38 | €-594,36 | 180 | 180 | 41,67% | 0,85 | €-3,30 | 12,06% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.450,28 | €-549,72 | 68 | 68 | 33,82% | 0,69 | €-8,08 | 9,08% |
| TEST | Eth Ema 1H | Trend following EMA | €9.414,26 | €-585,74 | 34 | 34 | 35,29% | 0,50 | €-17,23 | 5,86% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.397,39 | €-598,61 | 169 | 169 | 36,69% | 0,83 | €-3,54 | 7,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.377,56 | €-622,44 | 95 | 95 | 33,68% | 0,73 | €-6,55 | 10,17% |
| TEST | Btc Ema 1H | Trend following EMA | €9.353,69 | €-646,31 | 28 | 28 | 25,00% | 0,36 | €-23,08 | 6,56% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.348,35 | €-648,94 | 145 | 145 | 43,45% | 0,75 | €-4,48 | 9,26% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.337,21 | €-664,23 | 156 | 156 | 43,59% | 0,79 | €-4,26 | 12,28% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.222,28 | €-834,33 | 214 | 214 | 40,65% | 0,78 | €-3,90 | 15,68% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.218,82 | €-779,76 | 124 | 124 | 31,45% | 0,76 | €-6,29 | 10,08% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.209,01 | €-789,56 | 119 | 119 | 33,61% | 0,76 | €-6,63 | 9,87% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.178,84 | €-817,24 | 186 | 186 | 37,63% | 0,79 | €-4,39 | 8,78% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.173,39 | €-825,19 | 121 | 121 | 33,06% | 0,76 | €-6,82 | 9,87% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.158,43 | €-894,15 | 110 | 110 | 30,91% | 0,72 | €-8,13 | 9,31% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.111,39 | €-906,12 | 272 | 272 | 40,44% | 0,85 | €-3,33 | 19,03% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.052,35 | €-946,25 | 155 | 155 | 41,94% | 0,74 | €-6,10 | 10,69% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.038,73 | €-957,16 | 165 | 165 | 36,36% | 0,69 | €-5,80 | 14,10% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.035,10 | €-961,05 | 241 | 241 | 41,08% | 0,77 | €-3,99 | 15,45% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.014,99 | €-969,13 | 68 | 68 | 30,88% | 0,51 | €-14,25 | 12,43% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €8.984,25 | €-1.014,36 | 99 | 99 | 33,33% | 0,63 | €-10,25 | 10,41% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €8.974,47 | €-1.005,95 | 163 | 163 | 38,65% | 0,76 | €-6,17 | 13,09% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €8.926,87 | €-1.071,29 | 113 | 113 | 25,66% | 0,68 | €-9,48 | 12,05% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.869,64 | €-1.126,32 | 145 | 145 | 35,86% | 0,60 | €-7,77 | 14,10% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €8.649,11 | €-1.398,65 | 137 | 137 | 37,23% | 0,63 | €-10,21 | 16,24% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.557,95 | €-1.428,91 | 185 | 185 | 35,14% | 0,62 | €-7,72 | 19,11% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.548,94 | €-1.468,36 | 85 | 85 | 36,47% | 0,51 | €-17,27 | 16,26% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.448,19 | €-1.551,81 | 88 | 88 | 26,14% | 0,56 | €-17,63 | 15,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €8.413,97 | €-1.586,03 | 126 | 126 | 30,95% | 0,61 | €-12,59 | 16,10% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €8.242,60 | €-1.804,95 | 160 | 160 | 38,12% | 0,59 | €-11,28 | 18,17% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.207,89 | €-1.836,30 | 137 | 137 | 35,77% | 0,50 | €-13,40 | 20,25% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.073,47 | €-1.918,84 | 150 | 150 | 41,33% | 0,56 | €-12,79 | 21,12% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,93739 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,00 |
| Principale 4H | BR | LONG | Confluenza trend | 240m | 3,0x | 0,64695 | 0,66681 | 0,56932 | 0,43453 | 0,80222 | €133,65 | €400,94 | €48,11 | €12,31 |
| Principale 4H | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,86857 | 3,16900 | 3,01621 | 1,92673 | 3,28758 | €219,58 | €658,74 | €0,00 | €68,99 |
| Principale 4H | ARB | LONG | Confluenza trend | 240m | 3,0x | 0,16607 | 0,18299 | 0,14920 | 0,11155 | 0,19981 | €157,86 | €473,57 | €48,11 | €48,24 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1362,57246 | 1462,41000 | 1402,82450 | 915,19450 | 1590,97378 | €171,74 | €515,21 | €0,00 | €37,75 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,67 | €32,02 | €1,66 | €0,00 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1367,76350 | 1462,41000 | 1437,10567 | 918,68115 | 1515,93042 | €279,62 | €838,86 | €0,00 | €58,05 |
| Bilanciata 1H V1 | BR | LONG | Confluenza trend | 60m | 3,0x | 0,66741 | 0,66681 | 0,58732 | 0,44828 | 0,82759 | €127,56 | €382,69 | €45,92 | €-0,35 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €641,80 | €1.925,39 | €46,04 | €0,00 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 83,16563 | 86,73400 | 84,77298 | 55,85958 | 87,00319 | €11,35 | €34,06 | €0,00 | €1,46 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,18303 | 0,18299 | 0,17249 | 0,12293 | 0,20409 | €267,12 | €801,35 | €46,11 | €-0,16 |
| Bilanciata 1H — LONG senza Range High Vol | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1462,70248 | 1462,41000 | 1401,11389 | 982,44850 | 1585,87967 | €370,14 | €1.110,42 | €46,76 | €-0,22 |
| Bilanciata 1H — LONG senza Range High Vol | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,18303 | 0,18299 | 0,17249 | 0,12293 | 0,20409 | €270,80 | €812,41 | €46,75 | €-0,16 |
| Bilanciata 1H — LONG senza Range High Vol | NEAR | LONG | Confluenza trend | 60m | 3,0x | 3,16963 | 3,16900 | 3,02031 | 2,12894 | 3,46828 | €330,76 | €992,29 | €46,75 | €-0,20 |
| Bilanciata 1H — LONG senza Range High Vol | BR | LONG | Confluenza trend | 60m | 3,0x | 0,66694 | 0,66681 | 0,60183 | 0,44796 | 0,79717 | €159,52 | €478,55 | €46,72 | €-0,10 |
| Bilanciata 1H V2 | BR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,66741 | 0,66681 | 0,58732 | 0,44828 | 0,82759 | €132,20 | €396,61 | €47,59 | €-0,36 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 1478,71568 | 1462,41000 | 1409,80814 | 993,20403 | 1616,53079 | €341,14 | €1.023,41 | €47,69 | €-11,29 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,17400 | 0,18299 | 0,16331 | 0,11687 | 0,19540 | €258,08 | €774,23 | €47,61 | €39,98 |
| Bilanciata 1H V3 Filtered | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,66681 | 0,63674 | 0,42768 | 0,78955 | €134,14 | €402,41 | €0,00 | €19,01 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1415,48789 | 997,65136 | 1625,03524 | €347,14 | €1.041,42 | €48,97 | €-16,07 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17637 | 0,18299 | 0,16609 | 0,11846 | 0,19692 | €286,36 | €859,08 | €50,05 | €32,27 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 84,78752 | 58,26799 | 90,67899 | €737,14 | €2.211,41 | €50,06 | €-0,44 |
| Rapida V1 — score 6–7,5 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €427,79 | €1.283,38 | €46,94 | €-19,81 |
| Rapida V1 — score 6–7,5 | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66963 | 0,66681 | 0,60886 | 0,44977 | 0,76080 | €172,61 | €517,83 | €47,00 | €-2,18 |
| Rapida V1 — score 6–7,5 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 3,16063 | 3,16900 | 3,04641 | 2,12289 | 3,33197 | €436,61 | €1.309,84 | €47,34 | €3,47 |
| Rapida V1 — score 6–7,5 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17637 | 0,18299 | 0,16837 | 0,11846 | 0,18835 | €348,17 | €1.044,50 | €47,33 | €39,23 |
| Rapida V1 — score 6–7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €29,41 | €88,23 | €1,55 | €-0,02 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €429,57 | €1.288,70 | €47,13 | €-19,89 |
| Rapida score 6–7,5 — senza Trend Up | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66963 | 0,66681 | 0,60886 | 0,44977 | 0,76080 | €173,33 | €519,98 | €47,19 | €-2,19 |
| Rapida score 6–7,5 — senza Trend Up | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 3,16063 | 3,16900 | 3,04641 | 2,12289 | 3,33197 | €438,42 | €1.315,26 | €47,53 | €3,48 |
| Rapida score 6–7,5 — senza Trend Up | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17637 | 0,18299 | 0,16837 | 0,11846 | 0,18835 | €349,61 | €1.048,82 | €47,53 | €39,40 |
| Rapida score 6–7,5 — senza Trend Up | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €29,53 | €88,59 | €1,56 | €-0,02 |
| Rapida score 6–7,5 — Cost Aware | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €506,37 | €1.519,10 | €55,56 | €-23,45 |
| Rapida score 6–7,5 — Cost Aware | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66963 | 0,66681 | 0,60886 | 0,44977 | 0,76080 | €204,33 | €612,98 | €55,63 | €-2,58 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 3,16063 | 3,16900 | 3,04641 | 2,12289 | 3,33197 | €513,00 | €1.539,00 | €55,62 | €4,07 |
| Rapida score 6–7,5 — Cost Aware | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17637 | 0,18299 | 0,16837 | 0,11846 | 0,18835 | €409,08 | €1.227,24 | €55,61 | €46,10 |
| Rapida score 6–7,5 — Cost Aware | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €19,00 | €57,00 | €1,00 | €-0,01 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €453,98 | €1.361,95 | €49,81 | €-21,02 |
| Rapida V1 — no HIGH + score <7,5 | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66963 | 0,66681 | 0,60886 | 0,44977 | 0,76080 | €182,99 | €548,98 | €49,83 | €-2,32 |
| Rapida V1 — no HIGH + score <7,5 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 3,16063 | 3,16900 | 3,04641 | 2,12289 | 3,33197 | €462,90 | €1.388,71 | €50,19 | €3,68 |
| Rapida V1 — no HIGH + score <7,5 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17637 | 0,18299 | 0,16837 | 0,11846 | 0,18835 | €369,13 | €1.107,40 | €50,18 | €41,60 |
| Rapida V1 — no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €30,35 | €91,06 | €1,60 | €-0,02 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €406,98 | €1.220,95 | €44,66 | €-18,85 |
| Rapida V1 — senza PEPE | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €156,44 | €469,33 | €52,50 | €-0,42 |
| Rapida V1 — senza PEPE | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1462,33241 | 1462,41000 | 1408,47620 | 982,19993 | 1543,11671 | €479,24 | €1.437,71 | €52,95 | €0,08 |
| Rapida V1 — senza PEPE | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €380,61 | €1.141,83 | €52,91 | €29,21 |
| Rapida V1 — senza PEPE | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 84,52690 | 86,73400 | 85,01497 | 56,77390 | 86,76663 | €24,07 | €72,22 | €0,00 | €1,89 |
| Rapida V1 — senza PEPE | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €485,35 | €1.456,06 | €53,35 | €-0,29 |
| Rapida V1 — target pieno 2R | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,81674 | €152,62 | €457,86 | €51,22 | €-0,41 |
| Rapida V1 — target pieno 2R | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1462,33241 | 1462,41000 | 1408,47620 | 982,19993 | 1570,04482 | €465,91 | €1.397,73 | €51,48 | €0,07 |
| Rapida V1 — target pieno 2R | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19496 | €370,02 | €1.110,06 | €51,43 | €28,40 |
| Rapida V1 — target pieno 2R | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 84,52690 | 86,73400 | 85,01497 | 56,77390 | 87,51321 | €23,34 | €70,02 | €0,00 | €1,83 |
| Rapida 1H V3 Filtered — madre | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €152,93 | €458,78 | €51,32 | €-0,41 |
| Rapida 1H V3 Filtered — madre | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €467,66 | €1.402,98 | €51,31 | €-21,66 |
| Rapida 1H V3 Filtered — madre | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €370,21 | €1.110,63 | €51,46 | €28,41 |
| Rapida 1H V3 Filtered — madre | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €472,01 | €1.416,03 | €51,89 | €-0,28 |
| Rapida 1H V3 Filtered — madre | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €29,10 | €87,29 | €1,54 | €-0,02 |
| Rapida V3 — score <7,5 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €407,08 | €1.221,23 | €44,67 | €-18,85 |
| Rapida V3 — score <7,5 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66963 | 0,66681 | 0,60886 | 0,44977 | 0,76080 | €164,60 | €493,79 | €44,82 | €-2,08 |
| Rapida V3 — score <7,5 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16063 | 3,16900 | 3,04641 | 2,12289 | 3,33197 | €418,40 | €1.255,19 | €45,36 | €3,32 |
| Rapida V3 — score <7,5 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17637 | 0,18299 | 0,16837 | 0,11846 | 0,18835 | €333,64 | €1.000,92 | €45,36 | €37,60 |
| Rapida V3 — score <7,5 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €38,34 | €115,02 | €2,03 | €-0,02 |
| Rapida V3 — no volatilità HIGH | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €149,16 | €447,49 | €50,06 | €-0,40 |
| Rapida V3 — no volatilità HIGH | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €456,16 | €1.368,47 | €50,05 | €-21,12 |
| Rapida V3 — no volatilità HIGH | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €361,11 | €1.083,33 | €50,20 | €27,71 |
| Rapida V3 — no volatilità HIGH | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €460,41 | €1.381,23 | €50,61 | €-0,28 |
| Rapida V3 — no volatilità HIGH | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €28,44 | €85,32 | €1,50 | €-0,02 |
| Rapida V3 — Long Only | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €142,26 | €426,79 | €47,74 | €-0,39 |
| Rapida V3 — Long Only | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €435,05 | €1.305,14 | €47,74 | €-20,15 |
| Rapida V3 — Long Only | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €344,40 | €1.033,19 | €47,87 | €26,43 |
| Rapida V3 — Long Only | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €439,10 | €1.317,29 | €48,27 | €-0,26 |
| Rapida V3 — Long Only | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €27,07 | €81,20 | €1,43 | €-0,02 |
| Rapida V3 — Long + no HIGH + score <7,5 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €436,45 | €1.309,35 | €47,98 | €-0,26 |
| Rapida V3 — Long + no HIGH + score <7,5 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66694 | 0,66681 | 0,61630 | 0,44796 | 0,74291 | €210,58 | €631,75 | €47,97 | €-0,13 |
| Rapida V3 — Long + no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €908,15 | €2.724,46 | €47,97 | €-0,54 |
| Rapida V3 — senza ESPORTS | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €144,32 | €432,95 | €48,43 | €-0,39 |
| Rapida V3 — senza ESPORTS | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €441,33 | €1.323,99 | €48,43 | €-20,44 |
| Rapida V3 — senza ESPORTS | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €349,37 | €1.048,11 | €48,56 | €26,81 |
| Rapida V3 — senza ESPORTS | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €445,44 | €1.336,31 | €48,96 | €-0,27 |
| Rapida V3 — senza ESPORTS | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €27,46 | €82,38 | €1,45 | €-0,02 |
| Rapida V3 senza ESPORTS — Long Only | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €147,45 | €442,35 | €49,48 | €-0,40 |
| Rapida V3 senza ESPORTS — Long Only | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €450,91 | €1.352,73 | €49,48 | €-20,88 |
| Rapida V3 senza ESPORTS — Long Only | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €356,95 | €1.070,86 | €49,62 | €27,39 |
| Rapida V3 senza ESPORTS — Long Only | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €455,11 | €1.365,32 | €50,03 | €-0,27 |
| Rapida V3 senza ESPORTS — Long Only | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €28,06 | €84,17 | €1,48 | €-0,02 |
| Rapida V3 senza ESPORTS — MFE Lock | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €153,92 | €461,75 | €51,65 | €-0,42 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €470,68 | €1.412,05 | €51,65 | €-21,80 |
| Rapida V3 senza ESPORTS — MFE Lock | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €372,61 | €1.117,82 | €51,79 | €28,59 |
| Rapida V3 senza ESPORTS — MFE Lock | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €475,06 | €1.425,19 | €52,22 | €-0,28 |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €29,29 | €87,86 | €1,55 | €-0,02 |
| Rapida V3 senza ESPORTS — Stress Guard | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €495,86 | €1.487,59 | €54,41 | €-22,96 |
| Rapida V3 senza ESPORTS — Stress Guard | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €502,97 | €1.508,92 | €55,29 | €-0,30 |
| Rapida V3 senza ESPORTS — Stress Guard | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €1.046,63 | €3.139,90 | €55,28 | €-0,63 |
| Rapida V3 — qualità completa + profit lock | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €436,92 | €1.310,75 | €48,03 | €-0,26 |
| Rapida V3 — qualità completa + profit lock | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66694 | 0,66681 | 0,61630 | 0,44796 | 0,74291 | €210,81 | €632,43 | €48,02 | €-0,13 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €909,12 | €2.727,37 | €48,02 | €-0,55 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,72745 | 0,72745 | 0,78235 | 1,08754 | 0,57376 | €23,11 | €46,21 | €3,49 | €-0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08143 | 0,08182 | 0,08517 | 0,12174 | 0,07096 | €31,75 | €63,49 | €2,92 | €-0,30 |
| Ampia 4H | SOL | SHORT | Confluenza trend | 240m | 2,0x | 97,48250 | 101,43400 | 102,49471 | 145,73634 | 83,44831 | €17,85 | €35,69 | €1,84 | €-1,45 |
| Forza relativa 1H V1 | BR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,84361 | €179,69 | €359,39 | €43,13 | €-0,32 |
| Forza relativa 1H V1 | ZEC | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1478,71568 | 1462,41000 | 1409,80814 | 746,75142 | 1630,31230 | €463,14 | €926,28 | €43,16 | €-10,21 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €872,60 | €1.745,20 | €41,73 | €0,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,29450 | 1,29953 | 1,31506 | 1,93528 | 1,24928 | €21,63 | €43,26 | €0,69 | €-0,17 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €368,96 | €737,93 | €42,46 | €-0,15 |
| Forza relativa 1H V2 | BR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,84361 | €207,58 | €415,16 | €49,82 | €-0,38 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1478,71568 | 1462,41000 | 1409,80814 | 746,75142 | 1630,31230 | €535,87 | €1.071,75 | €49,94 | €-11,82 |
| Forza relativa 1H V2 | NEAR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 3,01160 | 3,16900 | 3,06811 | 1,52086 | 3,31780 | €540,30 | €1.080,59 | €0,00 | €56,48 |
| Forza relativa 1H V2 | ARB | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,17400 | 0,18299 | 0,16331 | 0,08787 | 0,19754 | €405,58 | €811,16 | €49,88 | €41,89 |
| Benchmark Donchian breakout 1H | ARB | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17594 | 0,18299 | 0,16531 | 0,08885 | 0,20250 | €496,10 | €992,20 | €59,93 | €39,79 |
| Donchian 1H Gb20 120R V1 | ARB | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17594 | 0,18299 | 0,16531 | 0,08885 | 0,20250 | €484,42 | €968,84 | €58,52 | €38,85 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,28183 | 1,29953 | 1,23929 | 0,64732 | 1,34563 | €603,45 | €1.206,90 | €40,05 | €16,67 |
| Benchmark Bollinger mean reversion 1H | ZEC | SHORT | Bollinger mean reversion | 60m | 2,0x | 1484,74299 | 1462,41000 | 1542,92731 | 2219,69077 | 1397,46652 | €519,64 | €1.039,27 | €40,73 | €15,63 |
| Benchmark Bollinger mean reversion 1H | ARB | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,17586 | 0,18299 | 0,18383 | 0,26292 | 0,16391 | €449,84 | €899,67 | €40,76 | €-36,45 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 86,71665 | 86,73400 | 88,35252 | 129,64140 | 84,26286 | €1.059,30 | €2.118,59 | €39,97 | €-0,42 |
| Benchmark trend following EMA 1H | BR | LONG | Trend following EMA | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,84361 | €203,60 | €407,20 | €48,86 | €-0,37 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 1478,71568 | 1462,41000 | 1402,15173 | 746,75142 | 1647,15637 | €474,62 | €949,23 | €49,15 | €-10,47 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,92 | €1.849,84 | €49,14 | €0,00 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 83,16563 | 86,73400 | 84,66233 | 41,99864 | 87,85598 | €958,32 | €1.916,65 | €0,00 | €82,24 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 3,16963 | 3,16900 | 3,00372 | 1,60067 | 3,53465 | €15,78 | €31,55 | €1,65 | €-0,01 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1515,93042 | €43,70 | €87,39 | €0,00 | €6,05 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €562,41 | €1.124,81 | €52,99 | €-0,22 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €460,38 | €920,77 | €52,99 | €-0,18 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 90,67899 | €1.170,25 | €2.340,50 | €52,98 | €-0,47 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1515,93042 | €47,66 | €95,32 | €0,00 | €6,60 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €529,15 | €1.058,29 | €49,86 | €-0,21 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €433,16 | €866,32 | €49,85 | €-0,17 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 90,67899 | €1.101,04 | €2.202,09 | €49,85 | €-0,44 |
| Scanner Top10 Long | BR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,66694 | 0,66681 | 0,60183 | 0,33681 | 0,79717 | €228,62 | €457,24 | €44,64 | €-0,09 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1485,33701 | 1462,41000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-17,21 |
| Scanner Top15 Long | BR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,82759 | €218,31 | €436,62 | €52,39 | €-0,39 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.099,00 | €2.198,01 | €52,56 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 84,52690 | 86,73400 | 82,60713 | 42,68609 | 88,36644 | €25,82 | €51,63 | €1,17 | €1,35 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €451,78 | €903,55 | €52,00 | €-0,18 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1485,33701 | 1462,41000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-17,21 |
| Scanner Top20 Long | BR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,82759 | €218,31 | €436,62 | €52,39 | €-0,39 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.099,00 | €2.198,01 | €52,56 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 84,52690 | 86,73400 | 82,60713 | 42,68609 | 88,36644 | €25,82 | €51,63 | €1,17 | €1,35 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €451,78 | €903,55 | €52,00 | €-0,18 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1530,74711 | €35,25 | €70,50 | €0,00 | €4,88 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €528,73 | €1.057,45 | €49,82 | €-0,21 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €432,81 | €865,63 | €49,81 | €-0,17 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €1.100,17 | €2.200,34 | €49,81 | €-0,44 |
| Top 5 + BTC — solo MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1530,74711 | €33,05 | €66,09 | €0,00 | €4,57 |
| Top 5 + BTC — solo MFE | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €495,65 | €991,31 | €46,70 | €-0,20 |
| Top 5 + BTC — solo MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €405,74 | €811,48 | €46,70 | €-0,16 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €1.031,35 | €2.062,71 | €46,69 | €-0,41 |
| Top 5 + BTC — Guard | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €498,90 | €997,79 | €47,01 | €-0,20 |
| Top 5 + BTC — Guard | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €408,40 | €816,79 | €47,00 | €-0,16 |
| Top 5 + BTC — Guard | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1462,70248 | 1462,41000 | 1401,11389 | 738,66475 | 1598,19740 | €558,11 | €1.116,22 | €47,00 | €-0,22 |
| Top 5 + BTC — Guard | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €1.037,47 | €2.074,94 | €46,97 | €-0,41 |
| Top 5 + BTC — BTC≤3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1530,74711 | €341,89 | €683,78 | €0,00 | €47,32 |
| Top 5 + BTC — BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €435,71 | €871,41 | €41,05 | €-0,17 |
| Top 5 + BTC — BTC≤3 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €356,67 | €713,34 | €41,05 | €-0,14 |
| Top 5 + BTC — BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €906,61 | €1.813,23 | €41,05 | €-0,36 |
| Top 5 + BTC — BTC 2–3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1485,33701 | 1462,41000 | 1415,48789 | 750,09519 | 1639,00507 | €477,40 | €954,81 | €44,90 | €-14,74 |
| Top 5 + BTC — BTC 2–3 | BR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,84361 | €186,94 | €373,89 | €44,87 | €-0,34 |
| Top 5 + BTC — Guard + MFE | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €487,29 | €974,59 | €45,91 | €-0,19 |
| Top 5 + BTC — Guard + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €398,90 | €797,80 | €45,91 | €-0,16 |
| Top 5 + BTC — Guard + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1462,70248 | 1462,41000 | 1401,11389 | 738,66475 | 1598,19740 | €545,13 | €1.090,26 | €45,91 | €-0,22 |
| Top 5 + BTC — Guard + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €1.013,35 | €2.026,69 | €45,88 | €-0,41 |
| Top 5 + BTC — Guard + BTC≤3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1530,74711 | €368,96 | €737,91 | €0,00 | €51,06 |
| Top 5 + BTC — Guard + BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €459,13 | €918,25 | €43,26 | €-0,18 |
| Top 5 + BTC — Guard + BTC≤3 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €375,84 | €751,68 | €43,26 | €-0,15 |
| Top 5 + BTC — Guard + BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €955,35 | €1.910,70 | €43,25 | €-0,38 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1530,74711 | €366,47 | €732,95 | €0,00 | €50,72 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €437,55 | €875,10 | €41,23 | €-0,17 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €358,18 | €716,35 | €41,22 | €-0,14 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €910,45 | €1.820,89 | €41,22 | €-0,36 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1590,01389 | €356,23 | €712,46 | €0,00 | €49,30 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,61761 | €501,71 | €1.003,43 | €47,27 | €-0,20 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,21462 | €410,70 | €821,41 | €47,27 | €-0,16 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 92,64282 | €1.043,96 | €2.087,93 | €47,27 | €-0,42 |
| Top 5 + BTC — target pieno 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1462,41000 | 1437,10567 | 690,72057 | 1590,01389 | €356,44 | €712,87 | €0,00 | €49,33 |
| Top 5 + BTC — target pieno 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,61761 | €502,01 | €1.004,02 | €47,30 | €-0,20 |
| Top 5 + BTC — target pieno 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,21462 | €410,94 | €821,89 | €47,30 | €-0,16 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 92,64282 | €1.044,58 | €2.089,15 | €47,29 | €-0,42 |
| Combo Trend | BR | LONG | Combo Trend | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,84361 | €197,44 | €394,87 | €47,38 | €-0,36 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 1478,71568 | 1462,41000 | 1402,15173 | 746,75142 | 1647,15637 | €460,25 | €920,51 | €47,66 | €-10,15 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €896,93 | €1.793,85 | €47,66 | €0,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 83,16563 | 86,73400 | 84,66233 | 41,99864 | 87,85598 | €929,32 | €1.858,64 | €0,00 | €79,75 |
| Combo Trend | NEAR | LONG | Combo Trend | 60m | 2,0x | 3,16963 | 3,16900 | 3,00372 | 1,60067 | 3,53465 | €15,30 | €30,60 | €1,60 | €-0,01 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,28183 | 1,29953 | 1,23929 | 0,64732 | 1,34989 | €653,10 | €1.306,20 | €43,35 | €18,04 |
| Combo Scanner | NEAR | LONG | Combo Scanner | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,49815 | €536,54 | €1.073,08 | €50,55 | €-0,21 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20620 | €439,21 | €878,43 | €50,55 | €-0,18 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 1462,70248 | 1462,41000 | 1401,11389 | 738,66475 | 1598,19740 | €600,23 | €1.200,45 | €50,55 | €-0,24 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 91,07176 | €1.115,76 | €2.231,52 | €50,52 | €-0,45 |
| Combo Adaptive — madre | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29953 | 1,33225 | 1,92042 | 1,18918 | €35,04 | €70,07 | €2,60 | €-0,82 |
| Combo Adaptive — madre | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,82759 | €220,13 | €440,26 | €52,83 | €-0,40 |
| Combo Adaptive — madre | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1478,71568 | 1462,41000 | 1409,80814 | 746,75142 | 1616,53079 | €571,67 | €1.143,34 | €53,28 | €-12,61 |
| Combo Adaptive — madre | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.068,45 | €2.136,89 | €51,09 | €0,00 |
| Combo Adaptive — madre | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 84,52690 | 86,73400 | 82,60713 | 42,68609 | 88,36644 | €15,40 | €30,79 | €0,70 | €0,80 |
| Combo Adaptive — madre | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €458,98 | €917,96 | €52,82 | €-0,18 |
| Combo Adaptive — MFE Trail esistente | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €479,66 | €959,32 | €45,19 | €-0,19 |
| Combo Adaptive — MFE Trail esistente | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 90,67899 | €998,15 | €1.996,30 | €45,19 | €-0,40 |
| Combo Adaptive — MFE Trail esistente | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1462,70248 | 1462,41000 | 1401,11389 | 738,66475 | 1585,87967 | €536,54 | €1.073,07 | €45,18 | €-0,21 |
| Combo Adaptive — MFE Trail esistente | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €392,26 | €784,52 | €45,15 | €-0,16 |
| Combo Adaptive — Quality7 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,82759 | €197,86 | €395,73 | €47,49 | €-0,36 |
| Combo Adaptive — Quality7 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1478,71568 | 1462,41000 | 1409,80814 | 746,75142 | 1616,53079 | €511,68 | €1.023,36 | €47,69 | €-11,28 |
| Combo Adaptive — Quality7 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,17843 | 0,18299 | 0,16780 | 0,09010 | 0,19968 | €400,18 | €800,36 | €47,68 | €20,47 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €554,68 | €1.109,36 | €52,26 | €-0,22 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 90,67899 | €1.154,26 | €2.308,52 | €52,26 | €-0,46 |
| Combo Adaptive — Long Only | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1462,70248 | 1462,41000 | 1401,11389 | 738,66475 | 1585,87967 | €620,45 | €1.240,90 | €52,25 | €-0,25 |
| Combo Adaptive — Long Only | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €453,61 | €907,22 | €52,21 | €-0,18 |
| Combo Adaptive — parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1485,33701 | 1462,41000 | 1415,48789 | 750,09519 | 1625,03524 | €544,86 | €1.089,72 | €51,25 | €-16,82 |
| Combo Adaptive — parziale 1R | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,82759 | €213,50 | €427,01 | €51,24 | €-0,39 |
| Combo Adaptive — parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.079,83 | €2.159,67 | €51,64 | €0,00 |
| Combo Adaptive — parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 83,16563 | 86,73400 | 84,88362 | 41,99864 | 87,00319 | €15,93 | €31,86 | €0,00 | €1,37 |
| Combo Adaptive — parziale 1R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €449,24 | €898,48 | €51,70 | €-0,18 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29953 | 1,33225 | 1,92042 | 1,14149 | €31,43 | €62,85 | €2,33 | €-0,73 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,61761 | €479,83 | €959,66 | €45,21 | €-0,19 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 92,64282 | €998,49 | €1.996,99 | €45,21 | €-0,40 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,21462 | €392,72 | €785,43 | €45,20 | €-0,16 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66694 | 0,66681 | 0,60183 | 0,33681 | 0,86228 | €219,36 | €438,72 | €42,83 | €-0,09 |
| Combo Adaptive — target pieno 3R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29953 | 1,33225 | 1,92042 | 1,14149 | €30,84 | €61,68 | €2,29 | €-0,72 |
| Combo Adaptive — target pieno 3R | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,61761 | €470,85 | €941,70 | €44,36 | €-0,19 |
| Combo Adaptive — target pieno 3R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 86,75135 | 86,73400 | 84,78752 | 43,80943 | 92,64282 | €979,81 | €1.959,63 | €44,36 | €-0,39 |
| Combo Adaptive — target pieno 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,21462 | €385,37 | €770,74 | €44,35 | €-0,15 |
| Combo Adaptive — target pieno 3R | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66694 | 0,66681 | 0,60183 | 0,33681 | 0,86228 | €215,26 | €430,52 | €42,03 | €-0,09 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €398,59 | €797,17 | €45,87 | €-0,16 |
| Master Adaptive V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €486,84 | €973,68 | €45,87 | €-0,19 |
| Master Adaptive Expanded V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €390,37 | €780,74 | €44,93 | €-0,16 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €476,80 | €953,60 | €44,93 | €-0,19 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €393,33 | €786,65 | €45,27 | €-0,16 |
| Master Adaptive Gb20 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €480,41 | €960,83 | €45,27 | €-0,19 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1462,41000 | 1297,25468 | 690,20536 | 1575,20914 | €389,09 | €778,18 | €39,56 | €54,47 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,21462 | €397,94 | €795,87 | €45,80 | €-0,16 |
| Master Adaptive Runner25 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,61761 | €486,04 | €972,09 | €45,80 | €-0,19 |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29953 | 1,33225 | 1,92042 | 1,18918 | €28,88 | €57,77 | €2,14 | €-0,67 |
| Combo Adaptive — Side × Regime Guard | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1367,76350 | 1462,41000 | 1441,62027 | 690,72057 | 1515,93042 | €18,84 | €37,68 | €0,00 | €2,61 |
| Combo Adaptive — Side × Regime Guard | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,82759 | €214,56 | €429,12 | €51,49 | €-0,39 |
| Combo Adaptive — Side × Regime Guard | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,17843 | 0,18299 | 0,16780 | 0,09010 | 0,19968 | €436,03 | €872,06 | €51,95 | €22,31 |
| Combo Adaptive — Side × Regime Guard | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 83,16563 | 86,73400 | 84,88362 | 41,99864 | 87,00319 | €1.044,69 | €2.089,38 | €0,00 | €89,65 |
| Master Adaptive GB20 — Breakeven 0,5R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €400,56 | €801,12 | €46,10 | €-0,16 |
| Master Adaptive GB20 — Breakeven 0,5R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €489,25 | €978,50 | €46,10 | €-0,20 |
| Master Adaptive GB20 — 50% a 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,18303 | 0,18299 | 0,17249 | 0,09243 | 0,20409 | €400,13 | €800,27 | €46,05 | €-0,16 |
| Master Adaptive GB20 — 50% a 0,75R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,16963 | 3,16900 | 3,02031 | 1,60067 | 3,46828 | €488,73 | €977,46 | €46,05 | €-0,20 |
| Master Adaptive GB20 — Loss Cap 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,18303 | 0,18299 | 0,17513 | 0,09243 | 0,20409 | €517,19 | €1.034,39 | €44,64 | €-0,21 |
| Master Adaptive GB20 — Loss Cap 0,75R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,16963 | 3,16900 | 3,05764 | 1,60067 | 3,46828 | €631,69 | €1.263,38 | €44,64 | €-0,25 |
| Rapida V3 NoHigh — Regime Guard | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66681 | 0,59275 | 0,44828 | 0,77941 | €157,74 | €473,22 | €52,94 | €-0,43 |
| Rapida V3 NoHigh — Regime Guard | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €482,38 | €1.447,14 | €52,93 | €-22,34 |
| Rapida V3 NoHigh — Regime Guard | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17843 | 0,18299 | 0,17016 | 0,11984 | 0,19083 | €381,86 | €1.145,59 | €53,08 | €29,31 |
| Rapida V3 NoHigh — Regime Guard | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,16963 | 3,16900 | 3,05349 | 2,12894 | 3,34385 | €486,87 | €1.460,60 | €53,52 | €-0,29 |
| Rapida V3 NoHigh — Regime Guard | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €30,00 | €90,01 | €1,58 | €-0,02 |
| MAIN — Side × Regime Guard | SUI | SHORT | Confluenza trend | 240m | 3,0x | 0,72995 | 0,72995 | 0,77421 | 0,96962 | 0,64144 | €294,19 | €882,58 | €53,51 | €-0,00 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,29295 | 1,29953 | 1,37261 | 1,71747 | 1,13364 | €83,64 | €250,92 | €15,46 | €-1,28 |
| Combo Trend — Side × Regime Guard | BR | LONG | Combo Trend | 60m | 2,0x | 0,66741 | 0,66681 | 0,58732 | 0,33704 | 0,84361 | €232,73 | €465,46 | €55,86 | €-0,42 |
| Combo Trend — Side × Regime Guard | ZEC | LONG | Combo Trend | 60m | 2,0x | 1478,71568 | 1462,41000 | 1402,15173 | 746,75142 | 1647,15637 | €542,53 | €1.085,06 | €56,18 | €-11,96 |
| Combo Trend — Side × Regime Guard | HYPE | LONG | Combo Trend | 60m | 2,0x | 83,16563 | 86,73400 | 84,66233 | 41,99864 | 87,85598 | €1.095,70 | €2.191,40 | €0,00 | €94,03 |
| Combo Trend — Side × Regime Guard | ARB | LONG | Combo Trend | 60m | 2,0x | 0,17637 | 0,18299 | 0,16495 | 0,08906 | 0,20148 | €17,55 | €35,09 | €2,27 | €1,32 |
| FAST NoHigh <7,5 · SHORT only | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1462,41000 | 1431,00992 | 997,65136 | 1566,82765 | €442,67 | €1.328,02 | €48,57 | €-20,50 |
| FAST NoHigh <7,5 · SHORT only | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66963 | 0,66681 | 0,60886 | 0,44977 | 0,76080 | €178,44 | €535,31 | €48,59 | €-2,26 |
| FAST NoHigh <7,5 · SHORT only | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 3,16063 | 3,16900 | 3,04641 | 2,12289 | 3,33197 | €451,37 | €1.354,12 | €48,94 | €3,59 |
| FAST NoHigh <7,5 · SHORT only | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17637 | 0,18299 | 0,16837 | 0,11846 | 0,18835 | €359,94 | €1.079,81 | €48,93 | €40,56 |
| FAST NoHigh <7,5 · SHORT only | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 86,75135 | 86,73400 | 85,22393 | 58,26799 | 89,04247 | €29,60 | €88,80 | €1,56 | €-0,02 |
| Bilanciata V3 · LONG only | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,66681 | 0,63674 | 0,42768 | 0,78955 | €126,91 | €380,72 | €0,00 | €17,98 |
| Bilanciata V3 · LONG only | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1462,41000 | 1415,48789 | 997,65136 | 1625,03524 | €328,43 | €985,30 | €46,33 | €-15,21 |
| Bilanciata V3 · LONG only | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17637 | 0,18299 | 0,16609 | 0,11846 | 0,19692 | €270,93 | €812,78 | €47,35 | €30,53 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 86,75135 | 86,73400 | 84,78752 | 58,26799 | 90,67899 | €697,41 | €2.092,23 | €47,36 | €-0,42 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bilanciata V3 · LONG only | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08561 | €35,05 | 0,76 | STOP |
| Combo Trend — Side × Regime Guard | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,07046 | €17,52 | 0,31 | STOP |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08388 | €25,62 | 0,49 | STOP |
| Combo Adaptive — target pieno 3R | ZEC | LONG | 2026-09-18T00:30:00+00:00 | 1444,93022 | €1,42 | 1,10 | STOP |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | LONG | 2026-09-18T00:30:00+00:00 | 1444,93022 | €1,44 | 1,10 | STOP |
| Combo Adaptive — parziale 1R | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08388 | €25,46 | 0,49 | STOP |
| Combo Adaptive — Quality7 | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08388 | €23,51 | 0,49 | STOP |
| Combo Adaptive — madre | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08388 | €26,27 | 0,49 | STOP |
| Top 5 + BTC — BTC 2–3 | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08561 | €33,96 | 0,76 | STOP |
| Scanner Top20 Long | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08561 | €39,66 | 0,76 | STOP |
| Scanner Top15 Long | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,08561 | €39,66 | 0,76 | STOP |
| Donchian 1H Gb20 120R V1 | NEAR | LONG | 2026-09-18T00:30:00+00:00 | 3,07065 | €33,64 | 0,57 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🧪 Validazione congiunta Research + Paper

I due campioni vengono letti insieme ma **non sommati**: il paper è normalmente un sottoinsieme dei segnali Research. La soglia usa gli **eventi di mercato indipendenti**.
Research è HYPOTHESIS_SCREENING_ONLY: PF e numerosità non superano un gate di causalità/parità/integrità non PASS.

Requisiti per la revisione live: almeno **30 eventi indipendenti per lato**, PF almeno **1,10**, expectancy positiva e max drawdown paper non superiore a **15,00%**.

| Profilo | Conto paper di riferimento | Research eventi | Paper eventi | PF Research | PF Paper | Exp. Research | Exp. Paper | DD Paper | Accordo | Stato |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 859/30 | 33/30 | 0,87 | 2,04 | -0,06R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 805/30 | 20/30 | 0,83 | 1,90 | -0,08R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 385/30 | 22/30 | 0,96 | 1,74 | -0,02R | €12,35 | 1,72% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 392/30 | 22/30 | 0,91 | 1,57 | -0,05R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 722/30 | 31/30 | 0,93 | 0,62 | -0,03R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 672/30 | 11/30 | 0,91 | 0,00 | -0,04R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 244/30 | 8/30 | 0,90 | 1,02 | -0,05R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 544/30 | 17/30 | 0,83 | 4,50 | -0,09R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 772/30 | 24/30 | 0,83 | 0,64 | -0,09R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 719/30 | 7/30 | 0,75 | 0,02 | -0,13R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 722/30 | 30/30 | 0,95 | 1,02 | -0,02R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 1217/30 | 55/30 | 0,87 | 1,12 | -0,06R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 310/30 | 15/30 | 0,78 | 0,99 | -0,12R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 1065/30 | 44/30 | 0,82 | 1,20 | -0,09R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 1069/30 | 37/30 | 0,82 | 0,76 | -0,09R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 998/30 | 23/30 | 0,78 | 1,12 | -0,11R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 451/30 | 64/30 | 0,81 | 0,78 | -0,12R | €-5,90 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 26/30 | 0,00 | 1,36 | 0,00R | €10,16 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 63/30 | 0,00 | 1,94 | 0,00R | €15,88 | 7,33% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 40/30 | 22/30 | 0,36 | 0,53 | -0,36R | €-2,69 | 0,73% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 57/30 | 34/30 | 0,82 | 0,76 | -0,09R | €-1,29 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 1206/30 | 214/30 | 0,89 | 0,78 | -0,06R | €-3,90 | 15,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 145/30 | 0,00 | 0,75 | 0,00R | €-4,48 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 15/30 | 0,00 | 1,01 | 0,00R | €0,14 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 417/30 | 170/30 | 1,05 | 0,88 | 0,03R | €-2,40 | 11,82% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 784/30 | 232/30 | 0,93 | 0,99 | -0,04R | €-0,09 | 14,04% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 705/30 | 187/30 | 0,89 | 0,82 | -0,06R | €-2,99 | 13,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 380/30 | 163/30 | 0,86 | 0,76 | -0,07R | €-6,17 | 13,09% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 802/30 | 194/30 | 0,93 | 0,94 | -0,04R | €-0,98 | 10,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 869/30 | 231/30 | 0,94 | 1,01 | -0,03R | €0,27 | 10,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1373/30 | 304/30 | 0,86 | 1,13 | -0,07R | €2,10 | 9,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 217/30 | 0,00 | 1,27 | 0,00R | €5,30 | 7,95% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 216/30 | 0,00 | 0,91 | 0,00R | €-2,18 | 15,94% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 77/30 | 0,00 | 1,11 | 0,00R | €2,28 | 6,49% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 788/30 | 254/30 | 0,92 | 0,92 | -0,04R | €-2,01 | 15,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 1327/30 | 296/30 | 0,83 | 1,06 | -0,09R | €1,03 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 107/30 | 82/30 | 1,00 | 1,28 | -0,00R | €6,72 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 1270/30 | 287/30 | 0,86 | 1,07 | -0,07R | €1,30 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 966/30 | 272/30 | 0,89 | 0,85 | -0,06R | €-3,33 | 19,03% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 436/30 | 199/30 | 1,02 | 0,93 | 0,01R | €-1,98 | 8,44% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 443/30 | 201/30 | 0,96 | 0,92 | -0,02R | €-2,01 | 6,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 818/30 | 280/30 | 0,95 | 0,94 | -0,03R | €-1,25 | 12,52% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 121/30 | 0,00 | 1,08 | 0,00R | €1,70 | 7,07% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 188/30 | 0,00 | 1,22 | 0,00R | €3,40 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 906/30 | 213/30 | 0,87 | 1,04 | -0,07R | €0,53 | 7,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 277/30 | 0,00 | 1,00 | 0,00R | €0,00 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 243/30 | 0,00 | 1,11 | 0,00R | €1,81 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 189/30 | 0,00 | 1,29 | 0,00R | €5,72 | 5,29% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 1223/30 | 250/30 | 0,84 | 0,96 | -0,08R | €-0,85 | 10,92% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 421/30 | 65/30 | 0,83 | 0,99 | -0,11R | €-0,23 | 4,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 410/30 | 150/30 | 1,07 | 0,56 | 0,03R | €-12,79 | 21,12% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 20/30 | 14/30 | 0,65 | 0,80 | -0,18R | €-4,65 | 2,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 4/30 | 4/30 | 0,76 | 0,77 | -0,19R | €-8,79 | 1,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 12/30 | 9/30 | 2,57 | 2,77 | 0,45R | €22,61 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 4/30 | 4/30 | 2,81 | 2,86 | 0,50R | €25,47 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 23/30 | 16/30 | 0,40 | 0,85 | -0,42R | €-3,76 | 1,98% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 9/30 | 7/30 | 0,32 | 0,41 | -0,65R | €-27,30 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 34/30 | 28/30 | 0,52 | 0,36 | -0,32R | €-23,08 | 6,56% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 6/30 | 5/30 | 0,45 | 0,58 | -0,49R | €-17,17 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 1005/30 | 234/30 | 0,94 | 1,20 | -0,03R | €2,91 | 8,17% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 641/30 | 194/30 | 0,96 | 1,14 | -0,02R | €2,33 | 7,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 1127/30 | 241/30 | 0,95 | 0,77 | -0,02R | €-3,99 | 15,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 946/30 | 192/30 | 0,91 | 1,13 | -0,05R | €1,87 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 102/30 | 58/30 | 1,37 | 0,95 | 0,16R | €-1,12 | 4,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 102/30 | 58/30 | 1,33 | 0,86 | 0,14R | €-3,27 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 352/30 | 109/30 | 0,89 | 0,83 | -0,06R | €-4,03 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 286/30 | 91/30 | 1,00 | 0,79 | 0,00R | €-5,01 | 6,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 165/30 | 0,74 | 0,69 | -0,20R | €-5,80 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 184/30 | 0,00 | 1,13 | 0,00R | €2,25 | 11,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 145/30 | 0,74 | 0,60 | -0,20R | €-7,77 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 160/30 | 85/30 | 1,00 | 0,51 | -0,00R | €-17,27 | 16,26% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 642/30 | 197/30 | 1,00 | 1,03 | 0,00R | €0,56 | 11,38% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 833/30 | 201/30 | 0,93 | 0,89 | -0,04R | €-2,33 | 14,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 166/30 | 0,00 | 1,42 | 0,00R | €7,55 | 10,10% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 22/30 | 19/30 | 1,03 | 0,58 | 0,01R | €-12,58 | 3,13% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 26/30 | 20/30 | 0,80 | 1,43 | -0,13R | €10,12 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 44/30 | 31/30 | 0,63 | 1,28 | -0,23R | €5,82 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 438/30 | 173/30 | 0,89 | 1,61 | -0,07R | €12,42 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 368/30 | 141/30 | 0,89 | 1,71 | -0,06R | €13,21 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 846/30 | 167/30 | 0,89 | 0,94 | -0,06R | €-1,03 | 12,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 35/30 | 26/30 | 0,51 | 0,42 | -0,36R | €-20,78 | 5,44% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 21/30 | 12/30 | 2,42 | 0,70 | 0,45R | €-10,99 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 31/30 | 23/30 | 0,63 | 0,61 | -0,26R | €-14,07 | 4,65% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 48/30 | 34/30 | 0,40 | 0,50 | -0,42R | €-17,23 | 5,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 8/30 | 9/30 | 0,39 | 0,41 | -0,40R | €-24,10 | 2,32% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 21/30 | 23/30 | 1,00 | 0,66 | -0,00R | €-9,57 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 435/30 | 99/30 | 1,04 | 0,63 | 0,03R | €-10,25 | 10,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 124/30 | 0,00 | 0,76 | 0,00R | €-6,29 | 10,08% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 113/30 | 0,00 | 0,68 | 0,00R | €-9,48 | 12,05% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 119/30 | 0,00 | 0,76 | 0,00R | €-6,63 | 9,87% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 825/30 | 155/30 | 1,25 | 0,74 | 0,08R | €-6,10 | 10,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 356/30 | 126/30 | 1,03 | 0,61 | 0,02R | €-12,59 | 16,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 401/30 | 110/30 | 1,05 | 0,72 | 0,03R | €-8,13 | 9,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 253/30 | 88/30 | 0,91 | 0,56 | -0,06R | €-17,63 | 15,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 417/30 | 121/30 | 1,03 | 0,76 | 0,02R | €-6,82 | 9,87% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 1001/30 | 185/30 | 0,87 | 0,62 | -0,08R | €-7,72 | 19,11% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 397/30 | 147/30 | 1,03 | 1,00 | 0,02R | €-0,08 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 341/30 | 76/30 | 0,59 | 0,76 | -0,23R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 341/30 | 76/30 | 0,59 | 0,76 | -0,23R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 341/30 | 76/30 | 0,59 | 0,76 | -0,23R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 362/30 | 95/30 | 0,69 | 0,73 | -0,17R | €-6,55 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 411/30 | 67/30 | 0,79 | 0,71 | -0,09R | €-7,99 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 369/30 | 68/30 | 0,73 | 0,69 | -0,12R | €-8,08 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 650/30 | 205/30 | 0,94 | 0,99 | -0,03R | €-0,17 | 10,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 652/30 | 224/30 | 0,94 | 1,16 | -0,03R | €2,44 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 652/30 | 224/30 | 0,94 | 1,16 | -0,03R | €2,44 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 615/30 | 164/30 | 1,00 | 0,99 | 0,00R | €-0,25 | 11,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 220/30 | 68/30 | 0,67 | 0,51 | -0,21R | €-14,25 | 12,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 470/30 | 137/30 | 0,81 | 0,50 | -0,11R | €-13,40 | 20,25% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 508/30 | 160/30 | 0,96 | 0,59 | -0,02R | €-11,28 | 18,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 421/30 | 137/30 | 0,86 | 0,63 | -0,08R | €-10,21 | 16,24% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 638/30 | 186/30 | 1,04 | 0,79 | 0,02R | €-4,39 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 520/30 | 169/30 | 1,00 | 0,83 | -0,00R | €-3,54 | 7,34% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 707/30 | 156/30 | 0,98 | 0,79 | -0,01R | €-4,26 | 12,28% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 562/30 | 180/30 | 0,96 | 0,85 | -0,02R | €-3,30 | 12,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 533/30 | 176/30 | 0,97 | 0,85 | -0,02R | €-3,35 | 11,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 674/30 | 198/30 | 1,02 | 1,17 | 0,01R | €2,99 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 43/30 | 29/30 | 0,79 | 0,89 | -0,14R | €-3,01 | 4,59% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 11/30 | 10/30 | 1,54 | 1,64 | 0,26R | €13,87 | 1,37% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 31/30 | 20/30 | 0,82 | 0,67 | -0,10R | €-11,21 | 3,48% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 6/30 | 5/30 | 2,48 | 0,88 | 0,51R | €-3,80 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 34/30 | 23/30 | 0,98 | 1,56 | -0,01R | €10,26 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 10/30 | 9/30 | 0,73 | 1,15 | -0,20R | €4,46 | 2,25% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 44/30 | 31/30 | 0,80 | 0,87 | -0,14R | €-4,04 | 4,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 12/30 | 11/30 | 0,64 | 1,02 | -0,25R | €0,50 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08182**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 31.5 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 76575.9 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, bearish_confirmation, stop_within_limit**
- High **0.0818**; close **0.08177**; wick alta **7.9%**; volume **x0.94**

### Gestione

- TP1 0,07107: chiude 25% e porta lo stop residuo al pareggio costi.
- TP2 0,06961: chiude 25% e porta lo stop residuo a TP1.
- TP3 0,06400: chiude 25% e porta lo stop residuo a TP2.
- TP4 0,06000: chiude l’ultimo 25%.
- Stop iniziale dinamico: almeno 0,08060, sopra il massimo della rejection con buffer 0,2%, mai oltre 0,08120.
- Politica conservativa: se stop e target sono toccati nella stessa candela, prevale lo stop.

## 🔬 Research All Signals

CAUSALITY= AFFECTED (storico) / CLEAN solo per LEGACY_RESEARCH_CAUSAL_V3
SEMANTIC_PARITY= REQUIRES_REVIEW · EVIDENCE_TIER=RESEARCH
PROMOTION_ELIGIBLE=NO · HYPOTHESIS_SCREENING_ONLY
⚠ Historical Research result — invalid for promotion evidence
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=539; LEGACY_RESEARCH_EVIDENCE_V3=19587; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **90,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +2.55%, 82% oltre +1%.
- BTC trend score: **-1,00**; ADX: **26,70**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **2,55%**; dispersione: **21,34%**

- Aperti in questo ciclo: **103**
- Chiusi in questo ciclo: **99**
- Posizioni research aperte: **1157**
- Trade research chiusi: **50581**
- Eventi di mercato indipendenti chiusi: **6700**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **138021**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 17 | 859 | 859 | 37,02% | 0,87 | -0,06R | €-549,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 17 | 805 | 805 | 36,52% | 0,83 | -0,08R | €-681,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 8 | 385 | 385 | 48,05% | 0,96 | -0,02R | €-71,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 8 | 392 | 392 | 37,24% | 0,91 | -0,05R | €-180,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 11 | 722 | 722 | 37,81% | 0,93 | -0,03R | €-233,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 11 | 672 | 672 | 37,95% | 0,91 | -0,04R | €-295,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 244 | 244 | 39,34% | 0,90 | -0,05R | €-116,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 11 | 544 | 544 | 36,40% | 0,83 | -0,09R | €-471,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 15 | 772 | 772 | 35,49% | 0,83 | -0,09R | €-689,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 15 | 719 | 719 | 34,49% | 0,75 | -0,13R | €-932,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 11 | 722 | 722 | 38,09% | 0,95 | -0,02R | €-174,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 18 | 1217 | 1217 | 40,67% | 0,87 | -0,06R | €-704,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 4 | 310 | 310 | 40,32% | 0,78 | -0,12R | €-379,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 19 | 1065 | 1065 | 35,40% | 0,82 | -0,09R | €-965,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 19 | 1069 | 1069 | 35,36% | 0,82 | -0,09R | €-966,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 19 | 998 | 998 | 34,77% | 0,78 | -0,11R | €-1140,94 |
| MAIN | 27 | 451 | 451 | 30,60% | 0,81 | -0,12R | €-518,80 |
| RSI_EXTREME_LONG_15M | 0 | 40 | 40 | 37,50% | 0,36 | -0,36R | €-145,44 |
| RSI_EXTREME_SHORT_15M | 0 | 57 | 57 | 42,11% | 0,82 | -0,09R | €-52,44 |
| Bilanciata 1H V1 | 31 | 1206 | 1206 | 37,56% | 0,89 | -0,06R | €-754,85 |
| Bilanciata 1H V2 | 14 | 478 | 417 | 41,84% | 1,05 | 0,03R | €132,31 |
| Bilanciata 1H V3 Filtered | 21 | 784 | 784 | 38,65% | 0,93 | -0,04R | €-279,67 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 21 | 705 | 705 | 38,58% | 0,89 | -0,06R | €-425,01 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 3 | 380 | 380 | 37,63% | 0,86 | -0,07R | €-262,99 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 19 | 802 | 802 | 38,78% | 0,93 | -0,04R | €-295,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 19 | 869 | 869 | 39,13% | 0,94 | -0,03R | €-261,15 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 25 | 1373 | 1373 | 37,58% | 0,86 | -0,07R | €-1023,41 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 15 | 788 | 788 | 39,34% | 0,92 | -0,04R | €-328,38 |
| SHADOW_1H_FAST_TP2_V1 | 25 | 1327 | 1327 | 35,49% | 0,83 | -0,09R | €-1134,45 |
| Rapida 1H V2 | 0 | 122 | 107 | 45,90% | 1,00 | -0,00R | €-0,44 |
| Rapida 1H V3 Filtered | 19 | 1270 | 1270 | 37,72% | 0,86 | -0,07R | €-940,04 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 17 | 966 | 966 | 39,13% | 0,89 | -0,06R | €-534,09 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 8 | 436 | 436 | 48,85% | 1,02 | 0,01R | €35,43 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 8 | 443 | 443 | 39,50% | 0,96 | -0,02R | €-81,79 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 11 | 818 | 818 | 39,73% | 0,95 | -0,03R | €-220,28 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 15 | 906 | 906 | 37,53% | 0,87 | -0,07R | €-609,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 19 | 1223 | 1223 | 37,37% | 0,84 | -0,08R | €-1022,00 |
| SHADOW_4H_WIDE | 37 | 421 | 421 | 25,18% | 0,83 | -0,11R | €-467,96 |
| SHADOW_BOLLINGER_MR_1H | 6 | 410 | 410 | 48,78% | 1,07 | 0,03R | €131,46 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 20 | 20 | 50,00% | 0,65 | -0,18R | €-35,17 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 4 | 4 | 25,00% | 0,76 | -0,19R | €-7,44 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 12 | 12 | 75,00% | 2,57 | 0,45R | €53,43 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 4 | 4 | 75,00% | 2,81 | 0,50R | €19,94 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 23 | 23 | 34,78% | 0,40 | -0,42R | €-95,85 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 9 | 9 | 11,11% | 0,32 | -0,65R | €-58,49 |
| SHADOW_BTC_EMA_1H | 0 | 34 | 34 | 38,24% | 0,52 | -0,32R | €-109,09 |
| SHADOW_BTC_EMA_4H | 0 | 6 | 6 | 16,67% | 0,45 | -0,49R | €-29,19 |
| SHADOW_COMBO_ADAPTIVE | 26 | 1005 | 1005 | 40,10% | 0,94 | -0,03R | €-342,36 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 15 | 641 | 641 | 40,87% | 0,96 | -0,02R | €-120,25 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 25 | 1127 | 1127 | 40,64% | 0,95 | -0,02R | €-261,28 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 26 | 946 | 946 | 41,86% | 0,91 | -0,05R | €-456,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 102 | 102 | 49,02% | 1,37 | 0,16R | €159,66 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 102 | 102 | 44,12% | 1,33 | 0,14R | €140,93 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 14 | 352 | 352 | 39,20% | 0,89 | -0,06R | €-214,96 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 1 | 286 | 286 | 40,91% | 1,00 | 0,00R | €2,92 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 160 | 160 | 46,25% | 1,00 | -0,00R | €-1,64 |
| SHADOW_COMBO_SCANNER | 16 | 642 | 642 | 38,79% | 1,00 | 0,00R | €9,14 |
| SHADOW_COMBO_TREND | 26 | 833 | 833 | 36,73% | 0,93 | -0,04R | €-321,55 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 22 | 22 | 54,55% | 1,03 | 0,01R | €2,87 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 26 | 26 | 42,31% | 0,80 | -0,13R | €-33,11 |
| SHADOW_DOGE_EMA_1H | 0 | 44 | 44 | 36,36% | 0,63 | -0,23R | €-100,13 |
| SHADOW_DONCHIAN_1H | 9 | 438 | 438 | 36,07% | 0,89 | -0,07R | €-296,82 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 9 | 368 | 368 | 38,04% | 0,89 | -0,06R | €-231,73 |
| SHADOW_EMA_TREND_1H | 26 | 846 | 846 | 35,93% | 0,89 | -0,06R | €-520,15 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 35 | 35 | 34,29% | 0,51 | -0,36R | €-124,30 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 21 | 21 | 66,67% | 2,42 | 0,45R | €94,65 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 31 | 31 | 35,48% | 0,63 | -0,26R | €-79,28 |
| SHADOW_ETH_EMA_1H | 0 | 48 | 48 | 33,33% | 0,40 | -0,42R | €-203,72 |
| SHADOW_ETH_EMA_4H | 0 | 8 | 8 | 37,50% | 0,39 | -0,40R | €-31,92 |
| SHADOW_GLOBAL_PURE | 0 | 21 | 21 | 47,62% | 1,00 | -0,00R | €-0,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 14 | 435 | 435 | 34,48% | 1,04 | 0,03R | €111,50 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 11 | 825 | 825 | 65,82% | 1,25 | 0,08R | €673,66 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 9 | 356 | 356 | 33,71% | 1,03 | 0,02R | €67,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 13 | 401 | 401 | 33,92% | 1,05 | 0,03R | €121,32 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 253 | 253 | 31,23% | 0,91 | -0,06R | €-148,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | 13 | 417 | 417 | 34,29% | 1,03 | 0,02R | €81,62 |
| Forza relativa 1H V1 | 31 | 1001 | 1001 | 34,07% | 0,87 | -0,08R | €-753,13 |
| Forza relativa 1H V2 | 21 | 427 | 397 | 38,41% | 1,03 | 0,02R | €74,51 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 13 | 341 | 341 | 31,67% | 0,59 | -0,23R | €-793,51 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 13 | 341 | 341 | 31,67% | 0,59 | -0,23R | €-793,51 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 13 | 341 | 341 | 31,67% | 0,59 | -0,23R | €-793,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 12 | 362 | 362 | 32,32% | 0,69 | -0,17R | €-614,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 12 | 411 | 411 | 54,26% | 0,79 | -0,09R | €-380,43 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 12 | 369 | 369 | 53,39% | 0,73 | -0,12R | €-443,21 |
| SHADOW_SCANNER_TOP10_LONG | 16 | 650 | 650 | 39,54% | 0,94 | -0,03R | €-200,31 |
| SHADOW_SCANNER_TOP15_LONG | 16 | 652 | 652 | 39,57% | 0,94 | -0,03R | €-196,79 |
| SHADOW_SCANNER_TOP20_LONG | 16 | 652 | 652 | 39,57% | 0,94 | -0,03R | €-196,79 |
| SHADOW_SCANNER_TOP5_BTC | 16 | 615 | 615 | 38,21% | 1,00 | 0,00R | €6,42 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 5 | 220 | 220 | 31,82% | 0,67 | -0,21R | €-453,10 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 15 | 470 | 470 | 34,68% | 0,81 | -0,11R | €-506,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 14 | 508 | 508 | 42,13% | 0,96 | -0,02R | €-96,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 14 | 421 | 421 | 36,10% | 0,86 | -0,08R | €-328,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 15 | 638 | 638 | 43,42% | 1,04 | 0,02R | €119,69 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 15 | 520 | 520 | 39,04% | 1,00 | -0,00R | €-14,14 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 16 | 707 | 707 | 42,29% | 0,98 | -0,01R | €-76,56 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 16 | 562 | 562 | 37,54% | 0,96 | -0,02R | €-137,33 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 16 | 533 | 533 | 37,34% | 0,97 | -0,02R | €-88,74 |
| SHADOW_SCANNER_TOP5_LONG | 16 | 674 | 674 | 39,47% | 1,02 | 0,01R | €54,04 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 43 | 43 | 39,53% | 0,79 | -0,14R | €-60,01 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 11 | 11 | 54,55% | 1,54 | 0,26R | €28,27 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 31 | 31 | 48,39% | 0,82 | -0,10R | €-30,88 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 6 | 6 | 66,67% | 2,48 | 0,51R | €30,82 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 34 | 34 | 47,06% | 0,98 | -0,01R | €-3,42 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 10 | 10 | 30,00% | 0,73 | -0,20R | €-20,19 |
| SHADOW_SOL_EMA_1H | 0 | 44 | 44 | 36,36% | 0,80 | -0,14R | €-59,46 |
| SHADOW_SOL_EMA_4H | 0 | 12 | 12 | 33,33% | 0,64 | -0,25R | €-30,53 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 3 | 128 | 128 | 32,03% | 0,65 | -0,19R | €-244,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 7 | 226 | 226 | 43,36% | 1,04 | 0,02R | €40,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 4 | 208 | 208 | 41,35% | 0,98 | -0,01R | €-18,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 1 | 49 | 49 | 26,53% | 0,30 | -0,45R | €-220,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 7 | 7 | 71,43% | 2,09 | 0,32R | €22,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 68 | 68 | 36,76% | 1,38 | 0,16R | €105,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 60 | 60 | 26,67% | 0,55 | -0,26R | €-153,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 68 | 68 | 20,59% | 0,43 | -0,31R | €-208,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 3 | 118 | 118 | 31,36% | 0,57 | -0,25R | €-297,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 7 | 206 | 206 | 41,75% | 1,02 | 0,01R | €18,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 4 | 199 | 199 | 40,70% | 0,86 | -0,07R | €-136,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 1 | 47 | 47 | 25,53% | 0,28 | -0,47R | €-219,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 5,17 | 0,70R | €42,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 67 | 67 | 37,31% | 1,37 | 0,15R | €99,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 56 | 56 | 25,00% | 0,52 | -0,27R | €-151,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 64 | 64 | 23,44% | 0,45 | -0,30R | €-189,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 17 | 17 | 41,18% | 0,64 | -0,22R | €-37,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 5 | 125 | 125 | 48,00% | 1,03 | 0,02R | €20,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 2 | 113 | 113 | 46,02% | 0,83 | -0,09R | €-105,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 42 | 42 | 64,29% | 2,20 | 0,39R | €163,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 52 | 52 | 42,31% | 0,69 | -0,16R | €-85,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 31,25% | 0,65 | -0,21R | €-33,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 5 | 128 | 128 | 38,28% | 0,89 | -0,06R | €-77,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 2 | 118 | 118 | 41,53% | 0,91 | -0,05R | €-53,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 42 | 42 | 38,10% | 1,86 | 0,26R | €109,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 52 | 52 | 26,92% | 0,64 | -0,17R | €-87,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,81 | -0,08R | €-45,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 8 | 264 | 264 | 39,39% | 0,86 | -0,08R | €-199,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 2 | 153 | 153 | 40,52% | 0,95 | -0,03R | €-39,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 72 | 72 | 30,56% | 0,72 | -0,14R | €-101,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 54 | 54 | 31,48% | 0,76 | -0,11R | €-57,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 8 | 242 | 242 | 38,43% | 0,86 | -0,08R | €-184,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 2 | 140 | 140 | 42,14% | 0,91 | -0,05R | €-63,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,59 | -0,24R | €-73,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 57 | 57 | 42,11% | 1,81 | 0,26R | €145,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 38 | 38 | 31,58% | 0,61 | -0,21R | €-81,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 66 | 66 | 31,82% | 0,62 | -0,19R | €-124,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 240 | 240 | 39,17% | 0,90 | -0,05R | €-116,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 3 | 58 | 58 | 37,93% | 0,62 | -0,24R | €-137,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 6 | 151 | 151 | 36,42% | 0,78 | -0,13R | €-193,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 210 | 210 | 40,48% | 0,97 | -0,02R | €-34,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 50 | 50 | 36,00% | 1,35 | 0,14R | €69,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 57 | 57 | 26,32% | 0,62 | -0,20R | €-116,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 3 | 99 | 99 | 33,33% | 0,60 | -0,24R | €-241,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 6 | 166 | 166 | 36,75% | 0,81 | -0,10R | €-173,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 5 | 261 | 261 | 40,23% | 0,96 | -0,02R | €-46,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 68 | 68 | 33,82% | 1,20 | 0,08R | €53,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 89 | 89 | 25,84% | 0,61 | -0,20R | €-180,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 3 | 93 | 93 | 31,18% | 0,53 | -0,30R | €-281,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 6 | 149 | 149 | 34,90% | 0,78 | -0,13R | €-196,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 5 | 247 | 247 | 39,68% | 0,87 | -0,06R | €-154,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 67 | 67 | 34,33% | 1,14 | 0,05R | €36,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 83 | 83 | 26,51% | 0,52 | -0,25R | €-209,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,81 | -0,08R | €-45,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 8 | 265 | 265 | 39,62% | 0,87 | -0,07R | €-179,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 2 | 153 | 153 | 41,83% | 1,03 | 0,01R | €19,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 72 | 72 | 30,56% | 0,72 | -0,14R | €-101,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 3 | 196 | 196 | 37,24% | 0,63 | -0,19R | €-373,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 8 | 321 | 321 | 41,43% | 0,94 | -0,03R | €-92,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 4 | 290 | 290 | 41,72% | 0,99 | -0,00R | €-12,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 67 | 67 | 38,81% | 0,48 | -0,29R | €-193,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 8 | 8 | 50,00% | 0,84 | -0,08R | €-6,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 89 | 89 | 47,19% | 1,55 | 0,17R | €151,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 92 | 92 | 38,04% | 0,78 | -0,09R | €-85,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,59 | -0,12R | €-5,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 102 | 102 | 38,24% | 0,71 | -0,14R | €-147,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 1 | 64 | 64 | 43,75% | 0,82 | -0,11R | €-67,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 3 | 73 | 73 | 36,99% | 0,77 | -0,14R | €-99,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 109 | 109 | 44,04% | 0,82 | -0,09R | €-99,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 15 | 15 | 60,00% | 1,97 | 0,42R | €63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 15 | 15 | 33,33% | 0,56 | -0,20R | €-30,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 33 | 33 | 21,21% | 0,31 | -0,50R | €-164,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 3 | 166 | 166 | 28,92% | 0,56 | -0,25R | €-418,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 9 | 280 | 280 | 39,29% | 0,88 | -0,06R | €-179,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 4 | 253 | 253 | 39,53% | 0,94 | -0,03R | €-79,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 88 | 88 | 25,00% | 0,57 | -0,23R | €-200,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 3 | 166 | 166 | 28,92% | 0,56 | -0,25R | €-418,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 9 | 282 | 282 | 39,36% | 0,88 | -0,06R | €-169,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 4 | 254 | 254 | 39,37% | 0,93 | -0,04R | €-89,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 88 | 88 | 25,00% | 0,57 | -0,23R | €-200,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 3 | 156 | 156 | 28,21% | 0,53 | -0,28R | €-438,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 9 | 256 | 256 | 38,67% | 0,88 | -0,07R | €-166,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 4 | 241 | 241 | 38,59% | 0,81 | -0,09R | €-220,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 61 | 61 | 31,15% | 0,49 | -0,29R | €-179,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 79 | 79 | 37,97% | 1,45 | 0,17R | €133,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 82 | 82 | 25,61% | 0,47 | -0,29R | €-234,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 7 | 42 | 42 | 28,57% | 0,77 | -0,14R | €-57,07 |
| MAIN | ALT_ROTATION_UP | 7 | 117 | 117 | 30,77% | 0,63 | -0,24R | €-281,61 |
| MAIN | RANGE | 4 | 105 | 105 | 29,52% | 0,82 | -0,11R | €-114,02 |
| MAIN | RANGE_HIGH_VOL | 3 | 26 | 26 | 23,08% | 0,72 | -0,16R | €-40,78 |
| MAIN | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,01 | 0,41R | €20,46 |
| MAIN | TRANSITION | 2 | 43 | 43 | 30,23% | 0,83 | -0,10R | €-42,41 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,96 | 0,48R | €19,39 |
| MAIN | TREND_UP | 2 | 48 | 48 | 29,17% | 0,93 | -0,04R | €-19,03 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,48R | €-14,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 25 | 25 | 32,00% | 0,13 | -0,59R | €-146,37 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 100,00% | ∞ | 1,09R | €32,57 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 25 | 25 | 44,00% | 0,92 | -0,04R | €-9,44 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 12 | 12 | 41,67% | 0,85 | -0,08R | €-10,11 |
| RSI_EXTREME_SHORT_15M | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,32R | €13,24 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 7 | 157 | 157 | 30,57% | 0,57 | -0,27R | €-431,26 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 11 | 295 | 295 | 42,37% | 0,97 | -0,02R | €-52,08 |
| Bilanciata 1H V1 | RANGE | 9 | 289 | 289 | 41,87% | 1,00 | -0,00R | €-0,32 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 74 | 74 | 31,08% | 0,53 | -0,30R | €-219,07 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-2,77 |
| Bilanciata 1H V1 | TRANSITION | 0 | 117 | 117 | 37,61% | 1,08 | 0,04R | €48,40 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 89 | 89 | 31,46% | 0,75 | -0,13R | €-113,61 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 50,00% | 1,44 | 0,24R | €14,27 |
| Bilanciata 1H V1 | TREND_UP | 0 | 128 | 128 | 32,03% | 0,91 | -0,05R | €-59,38 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 8 | 167 | 142 | 47,90% | 1,27 | 0,14R | €230,73 |
| Bilanciata 1H V2 | RANGE | 6 | 214 | 191 | 38,32% | 0,83 | -0,09R | €-201,04 |
| Bilanciata 1H V2 | TRANSITION | 0 | 97 | 84 | 39,18% | 1,21 | 0,11R | €102,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 4 | 116 | 116 | 28,45% | 0,50 | -0,33R | €-377,44 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 7 | 188 | 188 | 43,09% | 1,05 | 0,03R | €51,49 |
| Bilanciata 1H V3 Filtered | RANGE | 6 | 194 | 194 | 44,33% | 1,09 | 0,05R | €88,01 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 2 | 37 | 37 | 27,03% | 0,41 | -0,37R | €-138,27 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 64 | 64 | 37,50% | 1,15 | 0,07R | €44,08 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,10 | 0,06R | €4,35 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 75 | 75 | 34,67% | 1,13 | 0,06R | €47,35 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 105 | 105 | 26,67% | 0,41 | -0,39R | €-410,81 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 7 | 186 | 186 | 43,55% | 1,07 | 0,04R | €72,49 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 6 | 172 | 172 | 43,60% | 0,97 | -0,02R | €-28,15 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 35 | 35 | 28,57% | 0,45 | -0,34R | €-117,44 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 56 | 56 | 37,50% | 1,16 | 0,07R | €38,40 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,10 | 0,06R | €4,35 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 31,48% | 0,95 | -0,02R | €-13,49 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 22,58% | 0,49 | -0,26R | €-80,47 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 2 | 128 | 128 | 39,06% | 0,83 | -0,09R | €-110,65 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 82 | 82 | 43,90% | 1,05 | 0,03R | €20,62 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,18 | -0,71R | €-135,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 45,95% | 1,50 | 0,20R | €74,56 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 63 | 63 | 33,33% | 0,87 | -0,06R | €-35,07 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 86 | 86 | 40,70% | 0,97 | -0,01R | €-12,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 6 | 176 | 176 | 40,91% | 0,91 | -0,04R | €-79,10 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 7 | 272 | 272 | 41,18% | 0,99 | -0,00R | €-11,81 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 78 | 78 | 39,74% | 1,13 | 0,05R | €41,79 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 97 | 97 | 29,90% | 0,75 | -0,12R | €-114,38 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 104 | 104 | 37,50% | 0,83 | -0,09R | €-94,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 6 | 177 | 177 | 41,24% | 0,93 | -0,04R | €-65,20 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 7 | 302 | 302 | 43,05% | 1,09 | 0,04R | €133,38 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 80 | 80 | 41,25% | 1,23 | 0,09R | €71,48 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 113 | 113 | 29,20% | 0,68 | -0,17R | €-186,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 5 | 203 | 203 | 30,54% | 0,62 | -0,22R | €-450,22 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 10 | 346 | 346 | 40,17% | 0,86 | -0,08R | €-268,67 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 6 | 342 | 342 | 41,52% | 1,00 | 0,00R | €6,92 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 1 | 75 | 75 | 38,67% | 0,66 | -0,19R | €-143,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 54,55% | 1,45 | 0,17R | €18,77 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 109 | 109 | 42,20% | 1,33 | 0,13R | €141,25 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 104 | 104 | 29,81% | 0,64 | -0,19R | €-202,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,66 | -0,15R | €-7,59 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 128 | 128 | 28,91% | 0,70 | -0,16R | €-204,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 50 | 50 | 46,00% | 1,46 | 0,17R | €87,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 3 | 119 | 119 | 32,77% | 0,61 | -0,23R | €-274,27 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 7 | 204 | 204 | 41,67% | 0,96 | -0,02R | €-39,85 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 3 | 190 | 190 | 45,79% | 1,24 | 0,11R | €210,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 1 | 40 | 40 | 35,00% | 0,41 | -0,36R | €-143,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 100,00% | ∞ | 0,89R | €62,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 61 | 61 | 42,62% | 1,60 | 0,20R | €120,86 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,34 | -0,47R | €-28,15 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 75 | 75 | 28,00% | 0,62 | -0,21R | €-159,54 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 203 | 203 | 28,57% | 0,61 | -0,23R | €-469,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 10 | 342 | 342 | 40,06% | 0,90 | -0,05R | €-173,20 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 6 | 318 | 318 | 40,25% | 0,99 | -0,01R | €-16,95 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 77 | 77 | 32,47% | 0,53 | -0,26R | €-203,44 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 50,00% | 1,49 | 0,20R | €20,16 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 104 | 104 | 39,42% | 1,35 | 0,14R | €146,34 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 98 | 98 | 29,59% | 0,67 | -0,18R | €-179,94 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,21 | -0,35R | €-17,65 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 118 | 118 | 22,88% | 0,51 | -0,27R | €-318,56 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 38 | 34 | 47,37% | 0,96 | -0,02R | €-8,67 |
| Rapida 1H V2 | RANGE | 0 | 73 | 62 | 42,47% | 0,95 | -0,03R | €-19,03 |
| Rapida 1H V2 | TRANSITION | 0 | 11 | 11 | 63,64% | 1,79 | 0,25R | €27,27 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 195 | 195 | 30,26% | 0,56 | -0,26R | €-504,90 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 9 | 313 | 313 | 41,53% | 0,93 | -0,03R | €-108,23 |
| Rapida 1H V3 Filtered | RANGE | 4 | 306 | 306 | 40,52% | 0,97 | -0,02R | €-47,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 70 | 70 | 38,57% | 0,60 | -0,23R | €-158,07 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 94 | 94 | 40,43% | 1,27 | 0,11R | €104,32 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 126 | 126 | 36,51% | 0,94 | -0,03R | €-37,80 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 61 | 61 | 36,07% | 0,87 | -0,07R | €-42,57 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 3 | 150 | 150 | 33,33% | 0,62 | -0,22R | €-324,13 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 7 | 245 | 245 | 44,49% | 1,04 | 0,02R | €43,56 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 4 | 240 | 240 | 42,08% | 1,05 | 0,02R | €56,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 1 | 55 | 55 | 32,73% | 0,41 | -0,38R | €-206,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 87,50% | 6,12 | 0,65R | €51,94 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 71 | 71 | 40,85% | 1,26 | 0,11R | €75,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 66 | 66 | 27,27% | 0,61 | -0,22R | €-144,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,45 | -0,30R | €-18,15 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 86 | 86 | 29,07% | 0,64 | -0,20R | €-171,36 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,29 | -0,52R | €-125,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 5 | 136 | 136 | 49,26% | 1,00 | -0,00R | €-0,04 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 131 | 131 | 47,33% | 1,04 | 0,02R | €27,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 43 | 43 | 65,12% | 2,22 | 0,36R | €154,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 63 | 63 | 47,62% | 0,91 | -0,05R | €-28,47 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 23 | 23 | 21,74% | 0,28 | -0,52R | €-120,49 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 5 | 138 | 138 | 39,13% | 0,89 | -0,06R | €-80,53 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 135 | 135 | 44,44% | 1,13 | 0,07R | €89,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 43 | 43 | 44,19% | 1,85 | 0,26R | €109,67 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 65 | 65 | 32,31% | 0,78 | -0,11R | €-69,36 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 66 | 66 | 25,76% | 0,48 | -0,27R | €-180,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 8 | 297 | 297 | 41,08% | 0,91 | -0,05R | €-138,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 177 | 177 | 42,94% | 1,06 | 0,03R | €48,89 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 36,36% | 0,66 | -0,20R | €-64,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 62 | 62 | 46,77% | 1,73 | 0,25R | €153,48 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 0,81 | -0,10R | €-49,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 47,80 | 0,48R | €14,34 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 85 | 85 | 34,12% | 0,83 | -0,09R | €-72,37 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 43,59% | 1,23 | 0,10R | €40,01 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 3 | 122 | 122 | 33,61% | 0,60 | -0,24R | €-294,86 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 6 | 182 | 182 | 38,46% | 0,85 | -0,09R | €-157,60 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 5 | 315 | 315 | 41,90% | 1,03 | 0,01R | €46,93 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 74 | 74 | 39,19% | 1,32 | 0,12R | €87,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 112 | 112 | 32,14% | 0,76 | -0,13R | €-142,98 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 194 | 194 | 30,41% | 0,56 | -0,25R | €-493,47 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 9 | 312 | 312 | 41,03% | 0,91 | -0,05R | €-149,35 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 304 | 304 | 40,46% | 0,96 | -0,02R | €-62,60 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 69 | 69 | 39,13% | 0,61 | -0,21R | €-147,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 89 | 89 | 40,45% | 1,31 | 0,12R | €107,09 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 109 | 109 | 31,19% | 0,73 | -0,15R | €-160,54 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 41 | 41 | 41,46% | 1,16 | 0,07R | €29,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 9 | 40 | 40 | 27,50% | 1,02 | 0,01R | €5,72 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 8 | 100 | 100 | 33,00% | 0,85 | -0,10R | €-97,49 |
| SHADOW_4H_WIDE | RANGE | 6 | 97 | 97 | 19,59% | 0,71 | -0,19R | €-186,66 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 3 | 20 | 20 | 15,00% | 0,63 | -0,25R | €-49,32 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 44 | 44 | 20,45% | 0,59 | -0,28R | €-121,03 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,37 | 0,19R | €7,47 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 46 | 46 | 28,26% | 1,22 | 0,13R | €57,78 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 2 | 20 | 20 | 25,00% | 0,80 | -0,13R | €-25,04 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 2 | 55 | 55 | 43,64% | 0,80 | -0,11R | €-60,18 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 4 | 132 | 132 | 50,76% | 1,18 | 0,07R | €98,49 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 102 | 102 | 49,02% | 0,97 | -0,02R | €-16,51 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 16 | 16 | 50,00% | 1,36 | 0,15R | €23,95 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 0,70 | -0,21R | €-6,33 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 19 | 19 | 52,63% | 1,52 | 0,23R | €44,43 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 45 | 45 | 42,22% | 0,85 | -0,07R | €-33,39 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 45,00% | 1,00 | 0,00R | €0,09 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 50,00% | 0,93 | -0,03R | €-2,49 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 50,00% | 0,45 | -0,31R | €-24,46 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,32 | 0,69R | €13,75 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,14 | 0,07R | €3,26 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,17 | -0,47R | €-9,40 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 2,22 | 0,45R | €13,43 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,65R | €6,51 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,45 | -0,38R | €-30,72 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,41 | -0,38R | €-34,16 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 25,00% | 0,85 | -0,12R | €-4,85 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,38 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,27 | -0,64R | €-51,33 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,27 | -0,48R | €-24,20 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 10 | 10 | 60,00% | 1,24 | 0,11R | €10,80 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,66 | -0,18R | €-3,69 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,10 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,31 | 0,68R | €13,64 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 8 | 136 | 136 | 33,09% | 0,70 | -0,18R | €-250,79 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 10 | 244 | 244 | 42,62% | 1,00 | -0,00R | €-1,57 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 241 | 241 | 44,81% | 0,94 | -0,03R | €-73,87 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 58 | 58 | 34,48% | 0,53 | -0,26R | €-153,32 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,95 | -0,03R | €-3,06 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 92 | 92 | 42,39% | 1,23 | 0,11R | €98,46 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 76 | 76 | 35,53% | 0,95 | -0,02R | €-18,40 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,61 | 0,91R | €36,57 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 106 | 106 | 37,74% | 1,09 | 0,04R | €41,55 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 47 | 47 | 31,91% | 0,81 | -0,11R | €-50,70 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 10 | 234 | 234 | 41,88% | 0,95 | -0,03R | €-73,02 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 3 | 133 | 133 | 46,62% | 0,98 | -0,01R | €-14,79 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 23 | 23 | 30,43% | 0,38 | -0,37R | €-86,15 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 53 | 53 | 47,17% | 1,65 | 0,22R | €114,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 45 | 45 | 37,78% | 1,22 | 0,10R | €44,99 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,16 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 65 | 65 | 32,31% | 0,68 | -0,15R | €-98,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 7 | 164 | 164 | 35,98% | 0,74 | -0,13R | €-207,92 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 10 | 287 | 287 | 38,68% | 0,91 | -0,04R | €-123,16 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 6 | 255 | 255 | 42,35% | 1,08 | 0,04R | €91,71 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 66 | 66 | 34,85% | 0,49 | -0,26R | €-171,59 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,51 | -0,30R | €-35,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 84 | 84 | 45,24% | 1,22 | 0,09R | €71,97 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 100 | 100 | 38,00% | 0,96 | -0,02R | €-16,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 3,69 | 0,68R | €27,30 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 109 | 109 | 50,46% | 1,27 | 0,11R | €121,70 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 8 | 136 | 136 | 33,09% | 0,71 | -0,18R | €-242,19 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 10 | 242 | 242 | 42,98% | 0,95 | -0,03R | €-67,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 229 | 229 | 47,16% | 1,00 | -0,00R | €-3,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 56 | 56 | 37,50% | 0,63 | -0,20R | €-113,63 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,75 | -0,16R | €-15,75 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 75 | 75 | 46,67% | 1,21 | 0,09R | €70,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 76 | 76 | 39,47% | 0,96 | -0,02R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,07 | 0,78R | €31,07 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 85 | 85 | 38,82% | 0,78 | -0,10R | €-87,22 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,97 | -0,01R | €-6,60 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 38 | 38 | 52,63% | 1,53 | 0,20R | €77,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 57,89% | 2,69 | 0,47R | €88,74 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,88 | -0,06R | €-26,38 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 38 | 38 | 42,11% | 1,37 | 0,14R | €54,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 52,63% | 3,13 | 0,59R | €112,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 4 | 43 | 43 | 37,21% | 0,74 | -0,14R | €-59,10 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 6 | 108 | 108 | 40,74% | 0,79 | -0,13R | €-138,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 76 | 76 | 36,84% | 0,79 | -0,13R | €-96,03 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 2 | 15 | 15 | 46,67% | 1,19 | 0,08R | €11,47 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 39 | 39 | 41,03% | 0,90 | -0,05R | €-19,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 26 | 26 | 38,46% | 1,17 | 0,06R | €15,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 110 | 110 | 41,82% | 1,06 | 0,03R | €30,23 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 125 | 125 | 36,80% | 0,78 | -0,11R | €-133,30 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 51 | 51 | 49,02% | 1,43 | 0,21R | €105,99 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 40,00% | 2,13 | 0,62R | €61,68 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 0 | 17 | 17 | 17,65% | 0,68 | -0,24R | €-40,76 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 40,00% | 2,13 | 0,62R | €61,68 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 0 | 17 | 17 | 17,65% | 0,68 | -0,24R | €-40,76 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 33 | 33 | 36,36% | 0,65 | -0,17R | €-57,65 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 21 | 21 | 47,62% | 1,21 | 0,11R | €23,55 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 53 | 53 | 45,28% | 0,87 | -0,07R | €-37,33 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 10 | 10 | 20,00% | 0,44 | -0,38R | €-38,09 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 8 | 8 | 62,50% | 2,67 | 0,46R | €36,75 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 17 | 17 | 58,82% | 1,72 | 0,23R | €38,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 50 | 50 | 26,00% | 0,48 | -0,36R | €-178,40 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 10 | 195 | 195 | 41,03% | 1,02 | 0,01R | €18,46 |
| SHADOW_COMBO_SCANNER | RANGE | 4 | 145 | 145 | 44,14% | 1,08 | 0,04R | €61,11 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 25 | 25 | 40,00% | 0,56 | -0,24R | €-60,42 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 72 | 72 | 43,06% | 1,49 | 0,22R | €160,17 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 45 | 45 | 31,11% | 0,82 | -0,10R | €-45,10 |
| SHADOW_COMBO_SCANNER | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 72 | 72 | 31,94% | 1,09 | 0,04R | €31,62 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 7 | 106 | 106 | 29,25% | 0,55 | -0,30R | €-312,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 9 | 216 | 216 | 41,67% | 0,98 | -0,01R | €-24,39 |
| SHADOW_COMBO_TREND | RANGE | 6 | 201 | 201 | 38,81% | 1,06 | 0,03R | €61,92 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 2 | 43 | 43 | 39,53% | 0,99 | -0,01R | €-2,80 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 76 | 76 | 36,84% | 1,15 | 0,08R | €60,00 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 68 | 68 | 30,88% | 0,76 | -0,13R | €-86,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 1,61 | 0,21R | €6,21 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 82 | 82 | 31,71% | 1,04 | 0,02R | €15,16 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,62 | -0,21R | €-12,31 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 6 | 6 | 66,67% | 3,84 | 0,56R | €33,45 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 9 | 9 | 55,56% | 0,84 | -0,08R | €-7,12 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,15 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 25,00% | 0,33 | -0,56R | €-44,78 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,14 | -0,73R | €-36,57 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 55,56% | 1,07 | 0,03R | €3,05 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,92 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,75 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,08 | -0,74R | €-81,45 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 18,18% | 0,41 | -0,51R | €-56,27 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 13 | 13 | 46,15% | 1,23 | 0,12R | €15,53 |
| SHADOW_DOGE_EMA_1H | RANGE_HIGH_VOL | 0 | 4 | 4 | 100,00% | ∞ | 0,81R | €32,50 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 72 | 72 | 29,17% | 0,55 | -0,31R | €-225,72 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 2 | 117 | 117 | 32,48% | 0,64 | -0,26R | €-304,17 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 108 | 108 | 41,67% | 1,14 | 0,08R | €86,09 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 16 | 16 | 50,00% | 1,82 | 0,38R | €60,21 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 33 | 33 | 39,39% | 1,29 | 0,15R | €48,35 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 22 | 22 | 27,27% | 0,43 | -0,41R | €-89,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 43 | 43 | 30,23% | 1,15 | 0,07R | €32,24 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 54,17% | 1,90 | 0,44R | €104,71 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 62 | 62 | 29,03% | 0,46 | -0,38R | €-234,20 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 2 | 109 | 109 | 33,94% | 0,67 | -0,23R | €-253,75 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 88 | 88 | 44,32% | 1,16 | 0,08R | €71,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,52 | 0,57R | €80,48 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 26 | 26 | 46,15% | 1,68 | 0,30R | €77,62 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 20 | 20 | 30,00% | 0,46 | -0,40R | €-79,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 29 | 29 | 27,59% | 1,04 | 0,02R | €5,27 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 61,11% | 2,36 | 0,56R | €99,93 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 7 | 113 | 113 | 28,32% | 0,50 | -0,34R | €-379,95 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 9 | 221 | 221 | 41,63% | 0,97 | -0,02R | €-40,14 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 194 | 194 | 37,63% | 1,01 | 0,00R | €8,92 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 2 | 45 | 45 | 40,00% | 1,12 | 0,06R | €28,53 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 72 | 72 | 34,72% | 1,04 | 0,02R | €17,55 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,51 | -0,34R | €-10,34 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 89 | 89 | 29,21% | 0,86 | -0,08R | €-68,04 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 40,62% | 1,21 | 0,12R | €38,66 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 27,27% | 0,48 | -0,41R | €-45,03 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 10 | 10 | 30,00% | 0,38 | -0,48R | €-48,41 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,00 | -0,71R | €-21,28 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 3 | 3 | 66,67% | 2,41 | 0,52R | €15,63 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 70,00% | 4,04 | 0,66R | €65,54 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 66,67% | 1,30 | 0,11R | €3,44 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,39 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,21 | -0,60R | €-18,01 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,64 | -0,20R | €-3,91 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 22,22% | 0,30 | -0,59R | €-53,47 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,77 | -0,15R | €-13,41 |
| SHADOW_ETH_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,20 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,67 | 0,37R | €7,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,39 | -0,46R | €-13,71 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,91 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 19 | 19 | 42,11% | 0,56 | -0,25R | €-48,22 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,25 | -0,55R | €-49,78 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,43 | -0,49R | €-24,67 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,81 | -0,13R | €-6,46 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 0,64 | -0,19R | €-7,65 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,04R | €-10,39 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,35R | €3,51 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 10 | 10 | 40,00% | 0,80 | -0,13R | €-13,34 |
| SHADOW_GLOBAL_PURE | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,59R | €15,85 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 30 | 30 | 40,00% | 1,35 | 0,20R | €60,80 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 7 | 85 | 85 | 35,29% | 0,97 | -0,02R | €-16,69 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 4 | 144 | 144 | 29,86% | 0,85 | -0,10R | €-149,95 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 46 | 46 | 47,83% | 1,97 | 0,46R | €212,56 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 50 | 50 | 38,00% | 1,29 | 0,17R | €82,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 1 | 71 | 71 | 29,58% | 0,85 | -0,11R | €-74,81 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 49 | 49 | 59,18% | 1,01 | 0,01R | €2,65 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 6 | 183 | 183 | 66,67% | 1,27 | 0,09R | €160,96 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 268 | 268 | 66,04% | 1,26 | 0,08R | €221,24 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 100 | 100 | 73,00% | 1,75 | 0,18R | €181,85 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 78 | 78 | 64,10% | 1,36 | 0,12R | €94,03 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 132 | 132 | 60,61% | 0,99 | -0,00R | €-5,71 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 39,29% | 1,40 | 0,22R | €61,61 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 6 | 146 | 146 | 30,82% | 0,89 | -0,08R | €-110,85 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 46 | 46 | 45,65% | 1,79 | 0,40R | €182,06 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 45 | 45 | 40,00% | 1,37 | 0,21R | €96,58 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 1 | 82 | 82 | 25,61% | 0,69 | -0,23R | €-188,38 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 25 | 25 | 48,00% | 1,99 | 0,49R | €123,26 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 7 | 89 | 89 | 32,58% | 0,87 | -0,10R | €-88,60 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 129 | 129 | 31,01% | 0,97 | -0,02R | €-21,82 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 41 | 41 | 43,90% | 1,70 | 0,36R | €145,68 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 40,48% | 1,42 | 0,24R | €100,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 67 | 67 | 25,37% | 0,71 | -0,21R | €-142,89 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,73 | -0,19R | €-35,51 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 4 | 100 | 100 | 31,00% | 0,86 | -0,10R | €-101,93 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 36 | 36 | 47,22% | 2,12 | 0,49R | €176,16 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 59 | 59 | 27,12% | 0,75 | -0,18R | €-106,89 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 39,29% | 1,32 | 0,18R | €51,75 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 7 | 87 | 87 | 35,63% | 0,99 | -0,01R | €-9,22 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 4 | 135 | 135 | 31,85% | 0,94 | -0,04R | €-53,96 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 45 | 45 | 44,44% | 1,71 | 0,36R | €162,62 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 43 | 43 | 39,53% | 1,35 | 0,20R | €86,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 1 | 70 | 70 | 25,71% | 0,70 | -0,22R | €-153,22 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 7 | 132 | 132 | 31,82% | 0,61 | -0,24R | €-318,56 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 10 | 242 | 242 | 39,26% | 0,93 | -0,04R | €-102,17 |
| Forza relativa 1H V1 | RANGE | 9 | 253 | 253 | 33,99% | 0,81 | -0,11R | €-269,82 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 49 | 49 | 28,57% | 0,52 | -0,30R | €-148,31 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 11 | 11 | 27,27% | 0,72 | -0,18R | €-19,83 |
| Forza relativa 1H V1 | TRANSITION | 1 | 91 | 91 | 39,56% | 1,38 | 0,18R | €168,06 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 78 | 78 | 29,49% | 0,95 | -0,02R | €-19,05 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 1 | 3 | 3 | 100,00% | ∞ | 1,66R | €49,91 |
| Forza relativa 1H V1 | TREND_UP | 0 | 108 | 108 | 27,78% | 0,92 | -0,04R | €-43,00 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 34 | 34 | 26,47% | 0,77 | -0,15R | €-50,36 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 5 | 62 | 60 | 43,55% | 0,84 | -0,08R | €-50,02 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 7 | 102 | 93 | 43,14% | 1,13 | 0,08R | €82,56 |
| Forza relativa 1H V2 | RANGE | 7 | 113 | 107 | 31,86% | 0,73 | -0,16R | €-183,75 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 8 | 7 | 25,00% | 0,66 | -0,18R | €-14,36 |
| Forza relativa 1H V2 | TRANSITION | 0 | 49 | 44 | 40,82% | 1,54 | 0,25R | €122,15 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 36 | 35 | 27,78% | 0,89 | -0,05R | €-17,72 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 40,00% | 0,92 | -0,05R | €-2,35 |
| Forza relativa 1H V2 | TREND_UP | 0 | 42 | 38 | 47,62% | 1,81 | 0,36R | €152,91 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 6 | 94 | 94 | 23,40% | 0,34 | -0,48R | €-449,04 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 4 | 103 | 103 | 37,86% | 0,71 | -0,14R | €-139,33 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 6 | 94 | 94 | 23,40% | 0,34 | -0,48R | €-449,04 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 4 | 103 | 103 | 37,86% | 0,71 | -0,14R | €-139,33 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 6 | 94 | 94 | 23,40% | 0,34 | -0,48R | €-449,04 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 4 | 103 | 103 | 37,86% | 0,71 | -0,14R | €-139,33 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 6 | 81 | 81 | 24,69% | 0,42 | -0,41R | €-331,93 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 19 | 19 | 47,37% | 1,74 | 0,29R | €54,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 116 | 116 | 37,93% | 0,88 | -0,06R | €-68,89 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 30 | 30 | 46,67% | 1,14 | 0,06R | €17,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 42 | 42 | 38,10% | 1,01 | 0,01R | €2,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 6 | 100 | 100 | 45,00% | 0,51 | -0,27R | €-267,53 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,32 | 0,15R | €20,41 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 3 | 132 | 132 | 62,88% | 0,99 | -0,00R | €-4,42 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 35 | 35 | 62,86% | 1,17 | 0,07R | €23,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 33 | 33 | 57,58% | 1,30 | 0,13R | €44,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 68 | 68 | 52,94% | 0,63 | -0,16R | €-108,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,62 | -0,21R | €-8,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 6 | 81 | 81 | 40,74% | 0,39 | -0,35R | €-285,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 52,94% | 1,61 | 0,23R | €38,54 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 3 | 120 | 120 | 64,17% | 0,92 | -0,03R | €-33,92 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 34 | 34 | 58,82% | 0,96 | -0,02R | €-6,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 32 | 32 | 59,38% | 1,50 | 0,21R | €67,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 57 | 57 | 50,88% | 0,60 | -0,18R | €-103,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,37 | -0,35R | €-14,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,49 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 10 | 249 | 249 | 40,56% | 0,88 | -0,07R | €-175,15 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 10 | 253 | 253 | 41,11% | 0,89 | -0,07R | €-164,45 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 10 | 253 | 253 | 41,11% | 0,89 | -0,07R | €-164,45 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 46 | 46 | 28,26% | 0,55 | -0,29R | €-134,71 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 10 | 193 | 193 | 40,93% | 1,01 | 0,00R | €9,10 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 4 | 134 | 134 | 44,03% | 1,10 | 0,05R | €70,86 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 22 | 22 | 31,82% | 0,48 | -0,32R | €-71,39 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 67 | 67 | 41,79% | 1,48 | 0,22R | €145,48 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 71 | 71 | 30,99% | 1,03 | 0,02R | €10,91 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 11,11% | 0,18 | -0,67R | €-119,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 3 | 84 | 84 | 32,14% | 0,56 | -0,32R | €-265,32 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 1 | 12 | 12 | 41,67% | 0,44 | -0,35R | €-41,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,27 | -0,58R | €-23,05 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 30 | 30 | 53,33% | 2,17 | 0,40R | €120,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 58 | 58 | 29,31% | 0,86 | -0,07R | €-42,83 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 40 | 40 | 27,50% | 0,53 | -0,30R | €-120,90 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 8 | 106 | 106 | 32,08% | 0,62 | -0,26R | €-277,20 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 5 | 130 | 130 | 43,08% | 1,01 | 0,00R | €5,12 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,52 | -0,29R | €-60,69 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 2,10 | 0,38R | €193,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 52 | 52 | 23,08% | 0,59 | -0,24R | €-122,50 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 37 | 37 | 32,43% | 0,69 | -0,14R | €-50,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 7 | 106 | 106 | 36,79% | 0,73 | -0,14R | €-151,29 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 5 | 156 | 156 | 43,59% | 1,08 | 0,04R | €58,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 1,28 | 0,11R | €54,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 53 | 53 | 50,94% | 1,34 | 0,14R | €72,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 57,14% | 1,17 | 0,07R | €5,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 30 | 30 | 33,33% | 0,62 | -0,22R | €-67,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 7 | 85 | 85 | 34,12% | 0,71 | -0,19R | €-162,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 5 | 134 | 134 | 44,03% | 1,04 | 0,02R | €24,81 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 25 | 25 | 32,00% | 0,44 | -0,35R | €-88,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 46 | 46 | 39,13% | 1,52 | 0,21R | €97,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 26,83% | 0,78 | -0,12R | €-47,64 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,42 | -0,37R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 45 | 45 | 37,78% | 0,83 | -0,08R | €-35,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 9 | 199 | 199 | 41,71% | 0,99 | -0,00R | €-9,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 4 | 157 | 157 | 43,95% | 1,10 | 0,05R | €71,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 57 | 57 | 43,86% | 1,25 | 0,09R | €51,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 60 | 60 | 50,00% | 1,33 | 0,13R | €78,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 36 | 36 | 33,33% | 0,67 | -0,20R | €-71,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 9 | 162 | 162 | 43,83% | 1,15 | 0,08R | €133,34 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 4 | 133 | 133 | 44,36% | 1,05 | 0,03R | €37,33 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 25 | 25 | 32,00% | 0,44 | -0,35R | €-88,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 51 | 51 | 39,22% | 1,34 | 0,15R | €73,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 46 | 46 | 26,09% | 0,80 | -0,10R | €-48,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 56 | 56 | 35,71% | 0,70 | -0,14R | €-78,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 10 | 230 | 230 | 40,00% | 0,87 | -0,06R | €-145,80 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 4 | 148 | 148 | 44,59% | 1,11 | 0,05R | €73,98 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,45 | -0,26R | €-78,43 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 65 | 65 | 44,62% | 1,28 | 0,10R | €67,21 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 58 | 58 | 44,83% | 1,01 | 0,00R | €1,84 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 73 | 73 | 49,32% | 1,28 | 0,11R | €78,63 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 39 | 39 | 33,33% | 0,67 | -0,21R | €-80,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 10 | 194 | 194 | 40,72% | 1,01 | 0,01R | €16,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 125 | 125 | 42,40% | 1,04 | 0,02R | €25,66 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,52 | -0,29R | €-61,69 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 55 | 55 | 40,00% | 1,41 | 0,18R | €99,29 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 43 | 43 | 30,23% | 0,87 | -0,07R | €-31,88 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,08 | 0,55R | €10,95 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 54 | 54 | 24,07% | 0,68 | -0,17R | €-91,68 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 37 | 37 | 32,43% | 0,69 | -0,20R | €-72,22 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 9 | 185 | 185 | 40,00% | 1,00 | 0,00R | €3,08 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 119 | 119 | 42,02% | 1,06 | 0,03R | €41,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 30,00% | 0,31 | -0,44R | €-88,35 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 49 | 49 | 38,78% | 1,59 | 0,24R | €116,44 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,93 | -0,04R | €-14,25 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,23 | 0,12R | €2,31 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 53 | 53 | 26,42% | 0,73 | -0,13R | €-70,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 53 | 53 | 32,08% | 0,69 | -0,18R | €-97,82 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 10 | 202 | 202 | 40,59% | 0,92 | -0,05R | €-90,96 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 141 | 141 | 44,68% | 1,06 | 0,03R | €42,81 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 27 | 27 | 25,93% | 0,49 | -0,34R | €-92,68 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 70 | 70 | 41,43% | 1,43 | 0,18R | €124,25 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 92 | 92 | 38,04% | 1,14 | 0,07R | €59,88 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,10 | -0,84R | €-75,50 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 58,33% | 1,98 | 0,44R | €53,24 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 11 | 11 | 54,55% | 1,00 | -0,00R | €-0,06 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,82 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,86 | -0,10R | €-3,05 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 3,31 | 0,60R | €23,94 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 71,43% | 1,78 | 0,24R | €17,02 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,42 | -0,40R | €-44,47 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,53 | -0,33R | €-26,28 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 11,45 | 0,62R | €12,47 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,28 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,97 | -0,01R | €-0,27 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 28,57% | 0,26 | -0,59R | €-41,10 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 44,44% | 1,33 | 0,16R | €14,69 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 10 | 10 | 70,00% | 2,18 | 0,40R | €39,82 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,62 | 0,84R | €16,82 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,60 | -0,28R | €-8,29 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,08 | -0,85R | €-76,70 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 58,33% | 1,98 | 0,44R | €53,30 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 11 | 11 | 36,36% | 0,78 | -0,16R | €-17,14 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,82 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,29 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 0,91 | -0,05R | €-1,98 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,84 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-09-18T01:09:00+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **355**
- Scenari virtuali ancora attivi: **13240**
- Gruppi in attesa dell'uscita originale: **259**
- Gruppi con originale chiuso ma Shadow ancora attive: **96**
- Confronti completati: **659303**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ATR10_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR15_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR15_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR20_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR20_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR30_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A020 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A030 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A040 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A060 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A075 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A125 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R020_BALANCED_LONG | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R040 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R075 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| CH_MBV3_GB20_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-09-18T01:11:45+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **659303**
- Valutazioni prodotte: **29854**
- Candidature al Blocco 5: **15**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 41 | 3,520 | 4,831 | 2,865 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB30_R050 | 41 | 3,496 | 4,818 | 2,778 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB20_R075 | 41 | 3,451 | 4,831 | 2,743 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB30_R075 | 41 | 3,429 | 4,818 | 2,683 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB40_R050 | 41 | 3,392 | 4,678 | 2,694 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB40_R075 | 41 | 3,328 | 4,678 | 2,680 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB50_R050 | 41 | 3,280 | 4,538 | 2,626 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB50_R075 | 41 | 3,219 | 4,538 | 2,439 | 85,4% | 87,5 | EARLY_SIGNAL |
| ATR15_R050 | 41 | 2,910 | 4,115 | 2,282 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB30_R100 | 41 | 3,324 | 4,818 | 2,482 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R075 | 41 | 3,293 | 4,587 | 2,616 | 85,4% | 87,5 | EARLY_SIGNAL |
| ATR10_R050 | 41 | 3,269 | 4,641 | 2,577 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB40_R100 | 41 | 3,221 | 4,678 | 2,481 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R060 | 41 | 3,169 | 4,437 | 2,482 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R050 | 41 | 3,159 | 4,337 | 2,558 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB50_R100 | 41 | 3,117 | 4,538 | 2,303 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R040 | 41 | 3,071 | 4,238 | 2,505 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R035 | 41 | 3,027 | 4,188 | 2,449 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB20_R100 | 41 | 3,340 | 4,831 | 2,630 | 85,4% | 87,5 | EARLY_SIGNAL |
| ATR15_R100 | 41 | 2,788 | 4,115 | 2,074 | 85,4% | 87,5 | EARLY_SIGNAL |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.

🏆 CHALLENGER CANDIDATE
Aggiornamento aggregazione UTC: 2026-09-18T01:16:17+00:00
Mother canonica simulata: stessi ingressi, osservazioni ed execution del challenger.
PnL al netto delle fee modellate, funding escluso da entrambi; FX congelato all'ingresso.
Osservazioni MARK discrete: nessuna certificazione del percorso intrabar tra quotazioni.
Ranking promozionale: INSUFFICIENT_CERTIFIED_DATA

Rapida 1H V1 — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Rapida 1H V1 — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 90 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Master Adaptive Consensus — breakeven dopo +0,2R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 38 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 154 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 0 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

AUTO_PROMOTION=DISABLED · nessun ordine · revisione umana obbligatoria.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-18T01:08:28+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **46**
- Simulazioni bloccate attive: **100**
- Simulazioni completate nel ciclo: **14**
- Liquidazioni virtuali evitate totali: **2**
- Valore cumulato del filtro: **776.59 R**
- Profitto virtuale mancato: **1901.88 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 153 | 0 | 14183.96 |
| DOWN_20 | 153 | 0 | 28367.92 |
| DOWN_30 | 153 | 0 | 42551.89 |
| DOWN_40 | 153 | 79 | 51872.46 |
| UP_10 | 13 | 0 | 485.92 |
| UP_20 | 13 | 0 | 971.84 |
| UP_30 | 13 | 0 | 1457.77 |
| UP_40 | 13 | 2 | 1868.12 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-09-18T01:06:14+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **16**
- Nuovi candidati nel ciclo: **0**
- Evidenze rifiutate nel ciclo: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Regola di mutazione

Ogni candidato è una copia indipendente del genitore e cambia un solo parametro scalare. Il file principale paper_trading_config.json non viene riscritto.

## Candidati attivi

| Candidato | Genitore | Parametro | Vecchio | Nuovo | Scenario |
| --- | --- | --- | ---: | ---: | --- |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | SHADOW_1H_FAST_V3_CAP75_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | SHADOW_1H_FAST_V3 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | SHADOW_1H_FAST_V3 | reward_risk | 1.5 | 2.5 | TP_R250 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | SHADOW_1H_FAST_V3_NOHIGH_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | SHADOW_1H_FAST_V3_CAP75_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | SHADOW_1H_FAST_V3_NOHIGH_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-09-18T01:16:24+00:00

> Paper-only. Confronto sulle stesse entrate tramite `experiment_group_id`. Nessuna promozione, sostituzione, pensione o modifica live automatica.

## Stato

- Candidati valutati: **16**
- Pronti per revisione promozione: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Confronto

| Candidato | Genitore | Stato | Coppie | Δ medio R | CI basso | PF cand. | PF gen. | DD cand. | DD gen. | Score |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | SHADOW_1H_FAST_V3 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | SHADOW_1H_FAST_V3_CAP75_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | SHADOW_1H_FAST_V3_NOHIGH_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | SHADOW_1H_FAST_V3_CAP75_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | SHADOW_1H_FAST_V3 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | SHADOW_1H_FAST_V3_NOHIGH_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |

## Gate di sicurezza

- Solo trade chiusi dopo la creazione della candidata.
- Solo coppie con lo stesso evento d’ingresso.
- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.
- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.
- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.

# Blocco 7 — Governance promozioni Paper

Generato: 2026-09-18T01:16:24+00:00

> Nessuna promozione automatica. Approvazione umana e comando di esecuzione separato sono obbligatori.

## Stato

- Piani totali: **0**
- In attesa di approvazione: **0**
- Approvati ma non eseguiti: **0**
- Promozioni Paper attive: **0**
- Promozioni automatiche: **0**
- Rollback automatici: **0**

## Piani

| Piano | Candidata | Genitore | Stato | Review hash |
| --- | --- | --- | --- | --- |
| — | — | — | Nessun piano | — |

## Sicurezza

- Il piano è legato all’hash esatto della valutazione Block 6.
- Approvazione e esecuzione sono due azioni manuali distinte.
- Prima della promozione candidata e genitore devono essere senza posizioni aperte.
- Il genitore diventa `EX_MASTER` ma resta attivo in Paper.
- Ogni transazione ha backup e rollback esplicito.

# Blocco 8 — Sorveglianza post-promozione

Generato: 2026-09-18T01:16:24+00:00

> Paper-only. Il nuovo MASTER viene confrontato con l’EX_MASTER sugli stessi eventi successivi alla promozione. Nessun rollback automatico.

## Stato

- Promozioni attive monitorate: **0**
- Rollback raccomandati: **0**
- Critici: **0**
- Rollback automatici: **0**

## Confronto MASTER / EX_MASTER

| Famiglia | MASTER | EX_MASTER | Stato | Coppie | Δ medio R | CI alto | PF M | PF EX | DD ratio | Liq M/EX | Score |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| — | — | — | Nessuna promozione attiva | 0 | 0 | 0 | 0 | 0 | 0 | 0/0 | 0 |

## Sicurezza

- Solo trade chiusi dopo l’esecuzione della promozione.
- Solo coppie con lo stesso `experiment_group_id`, asset e lato.
- Solo dati `FULL_FROM_ENTRY` con risk model `block4_5_v1`.
- `ROLLBACK_RECOMMENDED` non esegue nulla: richiede il comando umano del Blocco 7.
- MASTER, EX_MASTER, stato promozione e live non vengono modificati.

# Blocco 9 — Hall of Fame e memoria genetica

Generato: 2026-09-18T01:16:24+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **142**
- Hall of Fame: **20**
- Memorie genetiche: **4**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 23.9 | E | 166 | 1.50 | 0.246 | 23.36 |
| 2 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | BASELINE | 21.6 | E | 189 | 1.20 | 0.093 | 10.66 |
| 3 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 21.3 | E | 188 | 1.30 | 0.136 | 14.92 |
| 4 | SHADOW_DONCHIAN_1H | BASELINE | 21.1 | E | 173 | 1.28 | 0.168 | 20.49 |
| 5 | SHADOW_COMBO_ADAPTIVE | BASELINE | 20.6 | E | 234 | 1.25 | 0.123 | 23.82 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 20.5 | E | 217 | 1.22 | 0.109 | 25.45 |
| 7 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | BASELINE | 20.3 | E | 141 | 1.30 | 0.177 | 20.49 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 19.2 | E | 243 | 1.11 | 0.056 | 30.08 |
| 9 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 18.7 | E | 184 | 1.11 | 0.059 | 25.62 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 18.6 | E | 213 | 1.09 | 0.045 | 14.78 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| FAMILY | momentum_breakout_v3_filtered | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |
| FAMILY | momentum_breakout_v3_filtered | reward_risk INCREASE | 2.5 | INSUFFICIENT | 47.5 | 4 | 0 | NO |
| GLOBAL | GLOBAL | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |
| GLOBAL | GLOBAL | reward_risk INCREASE | 2.5 | INSUFFICIENT | 47.5 | 4 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-09-18T01:16:24+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BULL_TREND**
- Righe di performance: **1126**
- Strategie preferite nel regime corrente: **14**
- Strategie da evitare nel regime corrente: **11**
- Memorie contestuali: **538**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.621 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.668 | 0.00 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | shadow-1h-fast-score-6-75-range-only-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.454 | 0.00 |
| 4 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 75.5 | 3 | 2.66 | 0.572 | 1.04 |
| 5 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.8 | 12 | 4.37 | 0.378 | 1.07 |
| 6 | SHADOW_SOL_ADAPTIVE_1H | shadow-sol-adaptive-1h | INSUFFICIENT | 73.2 | 9 | 2.30 | 0.480 | 1.17 |
| 7 | SHADOW_SOL_DONCHIAN_1H | shadow-sol-donchian-1h | INSUFFICIENT | 73.1 | 6 | 3.16 | 0.473 | 1.20 |
| 8 | SHADOW_SOL_EMA_1H | shadow-sol-ema-1h | INSUFFICIENT | 71.8 | 9 | 2.30 | 0.480 | 2.14 |
| 9 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | INSUFFICIENT | 70.7 | 2 | 21.93 | 0.694 | 0.07 |
| 10 | SHADOW_EMA_TREND_1H | shadow-ema-trend-1h | COMPATIBLE | 66.5 | 60 | 1.63 | 0.284 | 9.45 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-09-18T01:16:25+00:00

> Modalità LOCKED_REVIEW_ONLY. Il blocco prepara piani immutabili, ma non può modificare il bot reale o inviare ordini.

## Stato

- Promozioni Paper esaminate: **0**
- Pronte per revisione live: **0**
- Evidenza pronta ma adattatore bloccato: **0**
- Approvate in attesa di esecuzione esplicita: **0**
- Adattatore live configurato: **NO**
- Esecuzione live automatica: **NO**
- Ordini inviati: **0**

## Target iniziale

- Profilo: **SOL_SPOT_100_EUR**
- Solo SOL/USDT Spot
- Capitale massimo 100 €
- Una sola posizione
- Ingressi 10–20 €
- Nessun reinvestimento automatico

## Piani

| Piano | Candidata | Stato | Dominio | Validation | Post | Score | SOL trade | Regime | Crash |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| — | Nessuna promozione Paper eseguita | WAITING | — | 0 | 0 | 0 | 0 | — | — |

## Sicurezza

- Non vengono modificati `sol_spot_live_guarded.py`, `sol_spot_live_config.json`, `sol-live.service` o `sol-live.timer`.
- Un rilascio potrà cambiare un solo parametro e un solo dominio tra ENTRY, EXIT o RISK.
- Approvazione ed esecuzione sono due atti umani distinti.
- Prima dell’esecuzione saranno obbligatori backup transazionale, versione precedente e piano di rollback.
- L’adattatore reale resta bloccato finché non viene verificato separatamente sul codice live corrente.

# Blocco 12 — Evolution Control Tower

Generato: 2026-09-18T01:08:28+00:00

> Ultimo livello di osservabilità della pipeline. Non ripara, non riavvia, non modifica strategie o posizioni e non invia ordini.

## Stato generale

- Salute: **DEGRADED**
- Pipeline completa: **SI**
- Live bloccato: **SI**
- Persistenza completa: **SI**
- Catena audit valida: **SI**
- Recovery readiness: **READY**
- Controlli: **34**
- Warning: **1**
- Critici: **0**

## Controlli non superati

| Categoria | Controllo | Stato | Severità | Dettaglio |
| --- | --- | --- | --- | --- |
| SYSTEMD | sol_live_timer | WARN | WARN | Osservazione read-only: nessun servizio viene riavviato o modificato. |

## Sicurezza

- Riparazioni automatiche: **0**
- Riavvii automatici: **0**
- Mutazioni/promozioni/rollback/rilasci automatici: **0**
- Modifiche live: **NO**
- Ordini reali: **0**
