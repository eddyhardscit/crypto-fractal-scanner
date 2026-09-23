# Paper trading automatico KuCoin

Generato: 2026-09-23T05:33:20+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-17T17:30:04+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-17T17:30:04+00:00 | 2026-09-17T17:30:04+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-17T17:00:00+00:00 | 2026-09-17T17:00:00+00:00 | 15,3 min | 25,0 min | OK |
| 60m | 12 | 2026-09-17T16:00:00+00:00 | 2026-09-17T16:00:00+00:00 | 30,3 min | 45,0 min | OK |
| 240m | 12 | 2026-09-17T12:00:00+00:00 | 2026-09-17T12:00:00+00:00 | 1,50 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Balanced V3 Long Only V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced V3 Long Only V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 Short Only V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 Short Only V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend Side Regime Guard V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | BR | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | ARB | 60m | LONG | 8,25 | 7,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | BR | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | NEAR | 60m | LONG | 7,25 | 4,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | BR | 60m | LONG | 7,75 | 4,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | BR | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | NEAR | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ARB | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BR | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,87 | 6,00 | 0,13 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | POWER | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,54 | 6,00 | 2,46 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 2,85 | 6,00 | 3,15 | STALE_CANDLE | 1,50 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,50 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,11 | 6,00 | 4,89 | STALE_CANDLE | 1,50 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | ARB | 60m | LONG | 8,25 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ARB | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ARB | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | ARB | 60m | LONG | 8,25 | 4,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | ARB | 60m | LONG | 8,25 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.723,97 | -2,76% | €-84,59 | €3.000,00 | -2,82% | 6 | 64 | 40,62% | 0,78 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 64 | 3853 | PRIME INDICAZIONI | 100 (mancano 36) |

- Trade del Principale 4H chiusi: **64**; win rate **40,62%**; profit factor **0,78**.
- Expectancy: **€-5,90** per trade; P&L netto: **€-377,40**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.723,97 | €712,23 | €2.136,68 | €194,09 | €102,67 |
| TEST | Benchmark Donchian breakout 1H | 2 | €12.001,47 | €1.978,78 | €3.957,56 | €119,87 | €35,47 |
| TEST | Donchian 1H Gb20 120R V1 | 2 | €11.718,91 | €1.932,19 | €3.864,39 | €117,05 | €34,63 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €11.170,76 | €1.851,39 | €3.702,77 | €110,65 | €221,28 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 3 | €11.111,19 | €1.519,40 | €4.558,19 | €111,13 | €41,67 |
| TEST | Main Side Regime Guard V1 | 2 | €10.997,72 | €377,83 | €1.133,50 | €68,97 | €-2,49 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 4 | €10.878,29 | €2.474,36 | €7.423,07 | €163,23 | €34,08 |
| TEST | Rapida 1H V2 | 0 | €10.617,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 1 | €10.599,64 | €43,70 | €87,39 | €0,00 | €7,49 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.584,83 | €1.614,98 | €4.844,93 | €159,37 | €39,53 |
| TEST | Combo Adaptive | 5 | €10.565,78 | €1.413,33 | €2.826,66 | €55,43 | €120,56 |
| TEST | 1H Fast No Pepe V1 | 4 | €10.498,96 | €1.270,67 | €3.812,02 | €209,78 | €-42,29 |
| TEST | Scanner Top15 Long | 4 | €10.483,87 | €1.904,73 | €3.809,46 | €209,68 | €-0,76 |
| TEST | Scanner Top20 Long | 4 | €10.483,87 | €1.904,73 | €3.809,46 | €209,68 | €-0,76 |
| TEST | Combo Adaptive Long Only V1 | 0 | €10.452,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.328,16 | €1.575,31 | €4.725,92 | €155,46 | €38,61 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.298,42 | €1.377,32 | €2.754,64 | €53,64 | €112,75 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.264,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.261,81 | €1.565,18 | €4.695,55 | €154,46 | €38,36 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €10.247,80 | €1.856,83 | €3.713,66 | €102,49 | €114,26 |
| TEST | 1H Fast Tp2 V1 | 4 | €10.242,39 | €1.239,27 | €3.717,81 | €204,52 | €-41,16 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.235,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.205,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.203,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.202,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.180,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.175,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 0 | €10.110,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.054,87 | €50,00 | €750,00 | €16,81 | €-6,04 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.019,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 1 | €10.016,21 | €50,00 | €750,00 | €16,81 | €-6,04 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.010,97 | €10,00 | €150,00 | €3,36 | €-1,21 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €10.009,40 | €1.520,29 | €4.560,86 | €150,17 | €37,67 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €10.007,47 | €50,00 | €750,00 | €16,81 | €-6,04 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 1 | €10.003,24 | €10,00 | €150,00 | €3,36 | €-1,21 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.002,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €10.001,49 | €10,00 | €150,00 | €3,36 | €-1,21 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.993,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €9.992,97 | €89,18 | €445,89 | €10,00 | €-3,59 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.988,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.985,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.982,65 | €286,89 | €573,77 | €54,81 | €-2,05 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 1 | €9.973,01 | €47,66 | €95,32 | €0,00 | €8,17 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.966,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €9.964,67 | €35,25 | €70,50 | €0,00 | €6,05 |
| TEST | Forza relativa 1H V2 | 3 | €9.963,40 | €1.253,06 | €2.506,12 | €99,64 | €100,89 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €9.961,68 | €1.513,13 | €4.539,38 | €149,77 | €-1,93 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.957,95 | €88,87 | €444,33 | €9,96 | €-3,58 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.955,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €9.952,79 | €88,82 | €444,10 | €9,96 | €-3,58 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.940,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.939,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.934,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.927,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.912,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 5 | €9.894,26 | €1.509,13 | €4.527,38 | €148,93 | €36,99 |
| TEST | Sol Ema 1H | 0 | €9.874,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.868,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.793,92 | €1.174,50 | €3.523,50 | €97,95 | €47,75 |
| TEST | Eth Ema 4H | 0 | €9.783,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.779,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.775,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 4 | €9.772,40 | €1.619,63 | €3.239,26 | €96,80 | €193,58 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.761,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.713,57 | €1.475,44 | €4.426,32 | €146,04 | €-1,88 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.684,07 | €1.477,07 | €4.431,20 | €145,77 | €36,20 |
| TEST | Eth Donchian 1H | 0 | €9.676,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.605,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.595,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.546,20 | €1.456,04 | €4.368,12 | €143,69 | €35,69 |
| TEST | Combo Adaptive Regime V1 | 0 | €9.543,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 1 | €9.540,84 | €199,57 | €399,13 | €47,90 | €-38,14 |
| TEST | Scanner Bottom15 Short | 1 | €9.540,84 | €199,57 | €399,13 | €47,90 | €-38,14 |
| TEST | Scanner Bottom20 Short | 1 | €9.540,84 | €199,57 | €399,13 | €47,90 | €-38,14 |
| TEST | Bilanciata 1H V2 | 2 | €9.518,32 | €439,62 | €1.318,87 | €95,19 | €-0,26 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.496,47 | €1.234,41 | €2.468,82 | €94,97 | €78,28 |
| TEST | Combo Trend | 4 | €9.476,65 | €1.570,61 | €3.141,23 | €93,87 | €187,72 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 1 | €9.474,72 | €198,18 | €396,37 | €47,56 | €-37,87 |
| TEST | Scanner Top5 Btc Tp3 V1 | 1 | €9.471,84 | €356,44 | €712,87 | €0,00 | €61,12 |
| TEST | Scanner Top5 Btc Runner25 V1 | 1 | €9.466,30 | €356,23 | €712,46 | €0,00 | €61,09 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 1 | €9.460,31 | €197,88 | €395,77 | €47,49 | €-37,81 |
| TEST | Eth Adaptive 1H | 0 | €9.459,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 3 | €9.425,94 | €1.288,95 | €3.866,84 | €94,28 | €35,35 |
| TEST | Eth Ema 1H | 0 | €9.414,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 0 | €9.401,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 1 | €9.387,51 | €196,36 | €392,72 | €47,13 | €-37,52 |
| TEST | 1H Fast Score 6 75 V1 | 3 | €9.387,06 | €1.283,63 | €3.850,89 | €93,89 | €35,20 |
| TEST | Btc Ema 1H | 0 | €9.353,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 0 | €9.351,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 1 | €9.341,39 | €33,05 | €66,09 | €0,00 | €5,67 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.266,08 | €1.111,20 | €3.333,60 | €92,67 | €45,17 |
| TEST | Master Adaptive Gb20 Be V1 | 1 | €9.207,83 | €435,60 | €871,21 | €44,29 | €75,41 |
| TEST | Master Adaptive Gb20 Partial V1 | 1 | €9.198,03 | €435,14 | €870,28 | €44,25 | €75,33 |
| TEST | Bilanciata 1H V1 | 4 | €9.183,29 | €1.066,41 | €3.199,23 | €137,77 | €71,45 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 0 | €9.182,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.172,73 | €389,09 | €778,18 | €39,56 | €67,35 |
| TEST | Master Adaptive V1 | 1 | €9.162,46 | €433,46 | €866,91 | €44,08 | €75,03 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.043,82 | €117,83 | €235,66 | €7,15 | €1,20 |
| TEST | Master Adaptive Gb20 V1 | 1 | €9.041,56 | €427,66 | €855,33 | €43,49 | €74,03 |
| TEST | Combo Adaptive Mfe Trail | 1 | €9.040,47 | €31,44 | €62,87 | €0,00 | €5,39 |
| TEST | Master Adaptive Expanded V1 | 0 | €8.985,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €8.977,51 | €1.631,05 | €3.262,10 | €179,56 | €-0,65 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.930,52 | €2.039,57 | €6.118,70 | €134,00 | €32,85 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 0 | €8.928,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 3 | €8.928,44 | €1.679,96 | €5.039,89 | €133,97 | €-1,01 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €8.874,63 | €115,65 | €231,30 | €7,01 | €1,17 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €8.664,18 | €368,96 | €737,91 | €0,00 | €63,27 |
| TEST | Forza relativa 1H V1 | 6 | €8.624,96 | €1.478,48 | €2.956,96 | €172,50 | €-32,80 |
| TEST | Combo Mean Reversion | 1 | €8.555,31 | €653,10 | €1.306,20 | €43,35 | €24,41 |
| TEST | Master Adaptive Strict3 V1 | 0 | €8.448,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €8.413,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €8.257,45 | €366,47 | €732,95 | €0,00 | €62,85 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 1 | €8.221,92 | €341,89 | €683,78 | €0,00 | €58,63 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €8.144,60 | €1.123,08 | €2.246,17 | €80,78 | €22,35 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 | Momentum / breakout | Versione originale V1 a 1 ora che cerca momentum e breakout. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | Versione V3 derivata dalla V1: mantiene la logica momentum originale ma esclude i segnali con score assoluto da 5,0 a meno di 6,0, fascia risultata negativa nel confronto Paper vs Shadow. |
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
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | Benchmark puro: ritorno verso la media dopo uscita dalle Bollinger e conferma RSI estrema. |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | Benchmark puro: trend following con prezzo, EMA20, EMA50 e filtro ADX. |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | Opera long solo sulle cinque crypto più forti della classifica live KuCoin, con conferma tecnica. |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | Opera short solo sulle cinque crypto più deboli della classifica live KuCoin, con conferma tecnica. |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | Top 5 live KuCoin con conferma tecnica e forza relativa positiva contro Bitcoin. |
| TEST | Global Confluence puro 1H | Global Confluence puro | Opera soltanto quando Global Confluence, dati exchange e struttura tecnica sono allineati. |
| TEST | Combo Trend | Combo Trend | Portafoglio sperimentale separato. |
| TEST | Combo Mean Reversion | Combo Mean Reversion | Portafoglio sperimentale separato. |
| TEST | Combo Scanner | Combo Scanner | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | Portafoglio sperimentale separato. |
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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.723,97 | €-377,40 | 64 | 64 | 40,62% | 0,78 | €-5,90 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €12.001,47 | €1.968,38 | 171 | 171 | 45,03% | 1,56 | €11,51 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.718,91 | €1.686,60 | 139 | 139 | 43,88% | 1,64 | €12,13 | 6,75% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.170,76 | €1.070,58 | 163 | 163 | 50,31% | 1,35 | €6,57 | 10,10% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.111,19 | €1.152,82 | 216 | 216 | 49,54% | 1,27 | €5,34 | 7,95% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.997,72 | €1.000,64 | 63 | 63 | 55,56% | 1,94 | €15,88 | 7,33% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.878,29 | €927,10 | 186 | 186 | 48,92% | 1,25 | €4,98 | 5,29% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.617,99 | €617,99 | 92 | 82 | 48,91% | 1,28 | €6,72 | 3,89% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.599,64 | €592,20 | 198 | 198 | 44,44% | 1,17 | €2,99 | 8,85% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.584,83 | €624,83 | 185 | 185 | 49,19% | 1,22 | €3,38 | 5,24% |
| TEST | Combo Adaptive | Combo Adaptive | €10.565,78 | €655,55 | 233 | 233 | 46,78% | 1,19 | €2,81 | 8,17% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.498,96 | €620,41 | 301 | 301 | 44,19% | 1,13 | €2,06 | 9,28% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.483,87 | €486,92 | 222 | 222 | 47,75% | 1,14 | €2,19 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.483,87 | €486,92 | 222 | 222 | 47,75% | 1,14 | €2,19 | 10,31% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.452,65 | €452,65 | 194 | 194 | 44,85% | 1,14 | €2,33 | 7,78% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.328,16 | €367,23 | 240 | 240 | 49,17% | 1,09 | €1,53 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.298,42 | €387,82 | 183 | 183 | 44,26% | 1,13 | €2,12 | 11,68% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.264,13 | €264,13 | 26 | 26 | 38,46% | 1,36 | €10,16 | 3,39% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.261,81 | €300,63 | 284 | 284 | 44,72% | 1,06 | €1,06 | 9,48% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.247,80 | €333,37 | 191 | 191 | 45,55% | 1,12 | €1,75 | 8,69% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.242,39 | €325,01 | 293 | 293 | 40,27% | 1,07 | €1,11 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.235,99 | €235,99 | 23 | 23 | 56,52% | 1,56 | €10,26 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.205,57 | €205,57 | 121 | 121 | 42,15% | 1,08 | €1,70 | 7,07% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.203,50 | €203,50 | 9 | 9 | 77,78% | 2,77 | €22,61 | 0,85% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.202,44 | €202,44 | 20 | 20 | 60,00% | 1,43 | €10,12 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.180,44 | €180,44 | 31 | 31 | 61,29% | 1,28 | €5,82 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.175,88 | €175,88 | 77 | 77 | 44,16% | 1,11 | €2,28 | 6,49% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | Combo Scanner | Combo Scanner | €10.110,81 | €110,81 | 197 | 197 | 43,65% | 1,03 | €0,56 | 11,38% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.054,87 | €61,36 | 33 | 33 | 48,48% | 1,43 | €1,86 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.019,53 | €19,53 | 12 | 12 | 50,00% | 1,39 | €1,63 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.016,21 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.010,97 | €12,27 | 33 | 33 | 48,48% | 1,43 | €0,37 | 0,07% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €10.009,40 | €47,47 | 211 | 211 | 45,02% | 1,02 | €0,22 | 7,10% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.007,47 | €13,96 | 18 | 18 | 44,44% | 1,25 | €0,78 | 0,53% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,24 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.002,17 | €2,17 | 15 | 15 | 40,00% | 1,01 | €0,14 | 1,80% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,49 | €2,79 | 18 | 18 | 44,44% | 1,25 | €0,16 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,71 | €-2,29 | 12 | 12 | 33,33% | 0,62 | €-0,19 | 0,04% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.993,20 | €-6,80 | 5 | 5 | 20,00% | 0,05 | €-1,36 | 0,07% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.992,97 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.988,57 | €-11,43 | 12 | 12 | 33,33% | 0,62 | €-0,95 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.985,57 | €-14,43 | 22 | 22 | 36,36% | 0,31 | €-0,66 | 0,17% |
| TEST | Ampia 4H | Confluenza trend | €9.982,65 | €-14,92 | 65 | 65 | 33,85% | 0,99 | €-0,23 | 4,45% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.973,01 | €-35,11 | 205 | 205 | 44,88% | 0,99 | €-0,17 | 10,31% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.966,02 | €-33,98 | 5 | 5 | 20,00% | 0,05 | €-6,80 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.964,67 | €-41,33 | 164 | 164 | 44,51% | 0,99 | €-0,25 | 11,27% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.963,40 | €-29,08 | 153 | 146 | 41,18% | 0,99 | €-0,19 | 10,88% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.961,68 | €38,77 | 227 | 227 | 42,29% | 1,01 | €0,17 | 10,86% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.957,95 | €-38,20 | 33 | 33 | 48,48% | 0,78 | €-1,16 | 0,84% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.955,89 | €-44,11 | 5 | 5 | 20,00% | 0,09 | €-8,82 | 0,45% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,79 | €-43,37 | 18 | 18 | 38,89% | 0,56 | €-2,41 | 0,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.940,92 | €-59,08 | 22 | 22 | 31,82% | 0,53 | €-2,69 | 0,73% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.939,78 | €-60,22 | 16 | 16 | 50,00% | 0,85 | €-3,76 | 1,98% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.934,84 | €-65,16 | 14 | 14 | 50,00% | 0,80 | €-4,65 | 2,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.927,87 | €-72,13 | 22 | 22 | 36,36% | 0,31 | €-3,28 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.912,62 | €-87,38 | 29 | 29 | 44,83% | 0,89 | €-3,01 | 4,59% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.894,26 | €-68,31 | 274 | 274 | 41,97% | 0,99 | €-0,25 | 10,60% |
| TEST | Sol Ema 1H | Trend following EMA | €9.874,85 | €-125,15 | 31 | 31 | 38,71% | 0,87 | €-4,04 | 4,45% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.868,16 | €-131,84 | 12 | 12 | 50,00% | 0,70 | €-10,99 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.793,92 | €-156,51 | 230 | 230 | 41,74% | 0,96 | €-0,68 | 14,04% |
| TEST | Eth Ema 4H | Trend following EMA | €9.783,14 | €-216,86 | 9 | 9 | 22,22% | 0,41 | €-24,10 | 2,32% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.779,96 | €-220,04 | 23 | 23 | 39,13% | 0,66 | €-9,57 | 3,93% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.775,84 | €-224,16 | 20 | 20 | 40,00% | 0,67 | €-11,21 | 3,48% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.772,40 | €-315,23 | 165 | 165 | 40,61% | 0,89 | €-1,91 | 12,31% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.761,07 | €-238,93 | 19 | 19 | 47,37% | 0,58 | €-12,58 | 3,13% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.713,57 | €-211,27 | 190 | 190 | 41,05% | 0,93 | €-1,11 | 10,86% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.684,07 | €-279,30 | 247 | 247 | 42,91% | 0,94 | €-1,13 | 10,92% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.676,47 | €-323,53 | 23 | 23 | 34,78% | 0,61 | €-14,07 | 4,65% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.605,65 | €-394,35 | 199 | 199 | 45,73% | 0,93 | €-1,98 | 8,44% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.595,38 | €-404,62 | 201 | 201 | 43,28% | 0,92 | €-2,01 | 6,64% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.546,20 | €-417,69 | 277 | 277 | 41,52% | 0,92 | €-1,51 | 12,52% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.543,88 | €-456,12 | 91 | 91 | 46,15% | 0,79 | €-5,01 | 6,28% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.540,84 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.540,84 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.540,84 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.518,32 | €-480,63 | 182 | 168 | 44,51% | 0,87 | €-2,64 | 11,82% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.496,47 | €-463,26 | 108 | 108 | 38,89% | 0,83 | €-4,29 | 8,88% |
| TEST | Combo Trend | Combo Trend | €9.476,65 | €-608,34 | 199 | 199 | 40,70% | 0,86 | €-3,06 | 14,08% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.474,72 | €-487,17 | 66 | 66 | 34,85% | 0,72 | €-7,38 | 9,08% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.471,84 | €-588,86 | 176 | 176 | 41,48% | 0,85 | €-3,35 | 11,91% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.466,30 | €-594,36 | 180 | 180 | 41,67% | 0,85 | €-3,30 | 12,06% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.460,31 | €-501,64 | 67 | 67 | 34,33% | 0,71 | €-7,49 | 9,08% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.459,83 | €-540,17 | 26 | 26 | 34,62% | 0,42 | €-20,78 | 5,44% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.425,94 | €-538,75 | 214 | 214 | 43,46% | 0,90 | €-2,52 | 15,94% |
| TEST | Eth Ema 1H | Trend following EMA | €9.414,26 | €-585,74 | 34 | 34 | 35,29% | 0,50 | €-17,23 | 5,86% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.401,39 | €-598,61 | 169 | 169 | 36,69% | 0,83 | €-3,54 | 7,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.387,51 | €-574,73 | 94 | 94 | 34,04% | 0,75 | €-6,11 | 10,17% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.387,06 | €-577,77 | 252 | 252 | 42,06% | 0,91 | €-2,29 | 15,64% |
| TEST | Btc Ema 1H | Trend following EMA | €9.353,69 | €-646,31 | 28 | 28 | 25,00% | 0,36 | €-23,08 | 6,56% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.351,06 | €-648,94 | 145 | 145 | 43,45% | 0,75 | €-4,48 | 9,26% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.341,39 | €-664,23 | 156 | 156 | 43,59% | 0,79 | €-4,26 | 12,28% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.266,08 | €-687,02 | 185 | 185 | 42,16% | 0,78 | €-3,71 | 13,79% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.207,83 | €-779,76 | 124 | 124 | 31,45% | 0,76 | €-6,29 | 10,08% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.198,03 | €-789,56 | 119 | 119 | 33,61% | 0,76 | €-6,63 | 9,87% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.183,29 | €-886,24 | 212 | 212 | 40,09% | 0,77 | €-4,18 | 15,68% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.182,76 | €-817,24 | 186 | 186 | 37,63% | 0,79 | €-4,39 | 8,78% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.172,73 | €-894,15 | 110 | 110 | 30,91% | 0,72 | €-8,13 | 9,31% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.162,46 | €-825,19 | 121 | 121 | 33,06% | 0,76 | €-6,82 | 9,87% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.043,82 | €-957,27 | 163 | 163 | 36,20% | 0,69 | €-5,87 | 14,10% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.041,56 | €-946,25 | 155 | 155 | 41,94% | 0,74 | €-6,10 | 10,69% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.040,47 | €-964,89 | 240 | 240 | 40,83% | 0,77 | €-4,02 | 15,45% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €8.985,64 | €-1.014,36 | 99 | 99 | 33,33% | 0,63 | €-10,25 | 10,40% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.977,51 | €-1.019,89 | 66 | 66 | 28,79% | 0,49 | €-15,45 | 12,43% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.930,52 | €-1.034,19 | 269 | 269 | 40,15% | 0,83 | €-3,84 | 19,03% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €8.928,71 | €-1.071,29 | 113 | 113 | 25,66% | 0,68 | €-9,48 | 12,03% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €8.928,44 | €-1.067,53 | 161 | 161 | 38,51% | 0,74 | €-6,63 | 12,78% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.874,63 | €-1.126,43 | 143 | 143 | 35,66% | 0,60 | €-7,88 | 14,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.664,18 | €-1.398,65 | 137 | 137 | 37,23% | 0,63 | €-10,21 | 16,24% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.624,96 | €-1.340,59 | 180 | 180 | 34,44% | 0,63 | €-7,45 | 19,11% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.555,31 | €-1.468,36 | 85 | 85 | 36,47% | 0,51 | €-17,27 | 16,19% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.448,19 | €-1.551,81 | 88 | 88 | 26,14% | 0,56 | €-17,63 | 15,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €8.413,97 | €-1.586,03 | 126 | 126 | 30,95% | 0,61 | €-12,59 | 16,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.257,45 | €-1.804,95 | 160 | 160 | 38,12% | 0,59 | €-11,28 | 18,17% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.221,92 | €-1.836,30 | 137 | 137 | 35,77% | 0,50 | €-13,40 | 20,25% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.144,60 | €-1.876,44 | 149 | 149 | 41,61% | 0,56 | €-12,59 | 20,43% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,93739 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,00 |
| Principale 4H | BR | LONG | Confluenza trend | 240m | 3,0x | 0,64695 | 0,66728 | 0,56932 | 0,43453 | 0,80222 | €133,65 | €400,94 | €48,11 | €12,60 |
| Principale 4H | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,86857 | 2,98600 | 2,65907 | 1,92673 | 3,28758 | €219,58 | €658,74 | €48,11 | €26,97 |
| Principale 4H | ARB | LONG | Confluenza trend | 240m | 3,0x | 0,16607 | 0,17192 | 0,14920 | 0,11155 | 0,19981 | €157,86 | €473,57 | €48,11 | €16,67 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1362,57246 | 1485,04000 | 1248,37180 | 915,19450 | 1590,97378 | €171,74 | €515,21 | €43,18 | €46,31 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,67 | €32,02 | €1,66 | €0,12 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1367,76350 | 1485,04000 | 1417,55549 | 918,68115 | 1515,93042 | €279,62 | €838,86 | €0,00 | €71,93 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,17195 | 0,17192 | 0,16308 | 0,11550 | 0,18970 | €296,63 | €889,88 | €45,93 | €-0,18 |
| Bilanciata 1H V1 | BR | LONG | Confluenza trend | 60m | 3,0x | 0,66741 | 0,66728 | 0,58732 | 0,44828 | 0,82759 | €127,56 | €382,69 | €45,92 | €-0,08 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,98660 | 2,98600 | 2,86052 | 2,00600 | 3,23875 | €362,60 | €1.087,80 | €45,92 | €-0,22 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,17195 | 0,17192 | 0,16308 | 0,11550 | 0,18970 | €307,42 | €922,26 | €47,60 | €-0,18 |
| Bilanciata 1H V2 | BR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,66741 | 0,66728 | 0,58732 | 0,44828 | 0,82759 | €132,20 | €396,61 | €47,59 | €-0,08 |
| Bilanciata 1H V3 Filtered | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,66728 | 0,63674 | 0,42768 | 0,78955 | €134,14 | €402,41 | €0,00 | €19,30 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16668 | 0,11196 | 0,18419 | €306,48 | €919,44 | €0,00 | €28,89 |
| Bilanciata 1H V3 Filtered | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,86052 | 2,00600 | 3,23875 | €386,74 | €1.160,23 | €48,98 | €-0,23 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1415,48789 | 997,65136 | 1625,03524 | €347,14 | €1.041,42 | €48,97 | €-0,21 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €379,23 | €1.137,68 | €0,00 | €35,74 |
| 1H Fast Score 6 75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €476,61 | €1.429,83 | €46,95 | €-0,29 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €427,79 | €1.283,38 | €46,94 | €-0,26 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €380,80 | €1.142,39 | €0,00 | €35,89 |
| 1H Fast Score 6 75 No Trend Up V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €478,58 | €1.435,75 | €47,14 | €-0,29 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €429,57 | €1.288,70 | €47,13 | €-0,26 |
| 1H Fast Score 6 75 Cost Aware V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €448,88 | €1.346,64 | €0,00 | €42,31 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €564,15 | €1.692,45 | €55,57 | €-0,34 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €506,37 | €1.519,10 | €55,56 | €-0,30 |
| 1H Fast Nohigh Cap75 V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09985 | €137,41 | €412,22 | €49,47 | €-39,39 |
| 1H Fast Nohigh Cap75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €403,64 | €1.210,92 | €0,00 | €38,04 |
| 1H Fast Nohigh Cap75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €505,79 | €1.517,36 | €49,82 | €-0,30 |
| 1H Fast Nohigh Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €453,98 | €1.361,95 | €49,81 | €-0,27 |
| 1H Fast Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €12,31 | €36,94 | €0,67 | €-0,01 |
| 1H Fast Long Btc 1 3 Cap75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €453,42 | €1.360,27 | €44,66 | €-0,27 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €406,98 | €1.220,95 | €44,66 | €-0,24 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €819,56 | €2.458,67 | €44,65 | €-0,49 |
| 1H Fast No Pepe V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09985 | €145,18 | €435,55 | €52,27 | €-41,62 |
| 1H Fast No Pepe V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17195 | 0,17192 | 0,16505 | 0,11550 | 0,18231 | €436,04 | €1.308,12 | €52,51 | €-0,26 |
| 1H Fast No Pepe V1 | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €156,44 | €469,33 | €52,50 | €-0,09 |
| 1H Fast No Pepe V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €533,01 | €1.599,02 | €52,50 | €-0,32 |
| 1H Fast Tp2 V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09254 | €141,28 | €423,85 | €50,86 | €-40,50 |
| 1H Fast Tp2 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17195 | 0,17192 | 0,16505 | 0,11550 | 0,18576 | €425,39 | €1.276,16 | €51,23 | €-0,26 |
| 1H Fast Tp2 V1 | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,81674 | €152,62 | €457,86 | €51,22 | €-0,09 |
| 1H Fast Tp2 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,18272 | €519,98 | €1.559,94 | €51,22 | €-0,31 |
| Rapida 1H V3 Filtered | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €414,35 | €1.243,04 | €0,00 | €39,05 |
| Rapida 1H V3 Filtered | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €152,93 | €458,78 | €51,32 | €-0,09 |
| Rapida 1H V3 Filtered | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €521,03 | €1.563,08 | €51,32 | €-0,31 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €467,66 | €1.402,98 | €51,31 | €-0,28 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €9,23 | €27,68 | €0,50 | €-0,01 |
| 1H Fast V3 Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €359,21 | €1.077,64 | €0,00 | €33,86 |
| 1H Fast V3 Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €453,53 | €1.360,59 | €44,67 | €-0,27 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €407,08 | €1.221,23 | €44,67 | €-0,24 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €819,75 | €2.459,24 | €44,66 | €-0,49 |
| 1H Fast V3 Nohigh V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €406,76 | €1.220,27 | €0,00 | €38,34 |
| 1H Fast V3 Nohigh V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €149,16 | €447,49 | €50,06 | €-0,09 |
| 1H Fast V3 Nohigh V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €508,21 | €1.524,63 | €50,06 | €-0,30 |
| 1H Fast V3 Nohigh V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €456,16 | €1.368,47 | €50,05 | €-0,27 |
| 1H Fast V3 Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €385,45 | €1.156,36 | €0,00 | €36,33 |
| 1H Fast V3 Long Only V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €142,26 | €426,79 | €47,74 | €-0,09 |
| 1H Fast V3 Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €484,69 | €1.454,08 | €47,74 | €-0,29 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €435,05 | €1.305,14 | €47,74 | €-0,26 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €8,59 | €25,76 | €0,47 | €-0,01 |
| 1H Fast V3 No Esports V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €391,02 | €1.173,06 | €0,00 | €36,85 |
| 1H Fast V3 No Esports V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €144,32 | €432,95 | €48,43 | €-0,09 |
| 1H Fast V3 No Esports V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €491,69 | €1.475,08 | €48,43 | €-0,29 |
| 1H Fast V3 No Esports V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €441,33 | €1.323,99 | €48,43 | €-0,26 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €8,71 | €26,13 | €0,47 | €-0,01 |
| 1H Fast V3 No Esports Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €399,51 | €1.198,52 | €0,00 | €37,65 |
| 1H Fast V3 No Esports Long Only V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €147,45 | €442,35 | €49,48 | €-0,09 |
| 1H Fast V3 No Esports Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €502,36 | €1.507,09 | €49,48 | €-0,30 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €450,91 | €1.352,73 | €49,48 | €-0,27 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €8,90 | €26,70 | €0,48 | €-0,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €417,03 | €1.251,08 | €0,00 | €39,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €153,92 | €461,75 | €51,65 | €-0,09 |
| 1H Fast V3 No Esports Mfe Lock V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €524,39 | €1.573,18 | €51,65 | €-0,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €470,68 | €1.412,05 | €51,65 | €-0,28 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €9,29 | €27,86 | €0,51 | €-0,01 |
| 1H Fast V3 No Esports Stress Guard V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16731 | 0,17192 | 0,16731 | 0,11238 | 0,17779 | €427,51 | €1.282,54 | €0,00 | €35,31 |
| 1H Fast V3 No Esports Stress Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €552,45 | €1.657,34 | €54,42 | €-0,33 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €495,86 | €1.487,59 | €54,41 | €-0,30 |
| 1H Fast V3 No Esports Stress Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €998,53 | €2.995,60 | €54,40 | €-0,60 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,72745 | 0,72745 | 0,78235 | 1,08754 | 0,57376 | €23,11 | €46,21 | €3,49 | €-0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08143 | 0,08205 | 0,08517 | 0,12174 | 0,07096 | €31,75 | €63,49 | €2,92 | €-0,48 |
| Ampia 4H | SOL | SHORT | Confluenza trend | 240m | 2,0x | 97,48250 | 101,77000 | 102,49471 | 145,73634 | 83,44831 | €17,85 | €35,69 | €1,84 | €-1,57 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,72256 | 0,72256 | 0,74546 | 1,08022 | 0,67216 | €672,88 | €1.345,76 | €42,66 | €-0,00 |
| Forza relativa 1H V1 | POWER | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,08962 | €173,42 | €346,84 | €41,62 | €-33,14 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 81,62032 | 82,70900 | 79,97846 | 41,21826 | 85,23242 | €21,85 | €43,70 | €0,88 | €0,58 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,19148 | €417,85 | €835,70 | €43,13 | €-0,17 |
| Forza relativa 1H V1 | BR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €179,69 | €359,39 | €43,13 | €-0,07 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,26397 | €12,79 | €25,58 | €1,08 | €-0,01 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1362,57246 | 1485,04000 | 1425,82614 | 688,09909 | 1494,00974 | €562,79 | €1.125,57 | €0,00 | €101,17 |
| Forza relativa 1H V2 | ARB | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,19148 | €482,69 | €965,39 | €49,82 | €-0,19 |
| Forza relativa 1H V2 | BR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €207,58 | €415,16 | €49,82 | €-0,08 |
| Scalp RSI Short 85 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €3,36 | €-1,21 |
| Scalp RSI Short 80 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €3,36 | €-1,21 |
| Scalp RSI Short 75 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €3,36 | €-1,21 |
| Scalp RSI Short 85 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €16,81 | €-6,04 |
| Scalp RSI Short 80 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €16,81 | €-6,04 |
| Scalp RSI Short 75 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €16,81 | €-6,04 |
| Scalp RSI Short 85 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €89,18 | €445,89 | €10,00 | €-3,59 |
| Scalp RSI Short 80 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €88,82 | €444,10 | €9,96 | €-3,58 |
| Scalp RSI Short 75 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €88,87 | €444,33 | €9,96 | €-3,58 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 81,62032 | 82,70900 | 79,79603 | 41,21826 | 86,18106 | €1.339,05 | €2.678,11 | €59,86 | €35,72 |
| Benchmark Donchian breakout 1H | NEAR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2,98660 | 2,98600 | 2,84651 | 1,50823 | 3,33681 | €639,73 | €1.279,45 | €60,01 | €-0,26 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 81,62032 | 82,70900 | 79,79603 | 41,21826 | 86,18106 | €1.307,53 | €2.615,06 | €58,45 | €34,88 |
| Donchian 1H Gb20 120R V1 | NEAR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2,98660 | 2,98600 | 2,84651 | 1,50823 | 3,33681 | €624,67 | €1.249,33 | €58,60 | €-0,25 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,28183 | 1,30578 | 1,23929 | 0,64732 | 1,34563 | €603,45 | €1.206,90 | €40,05 | €22,55 |
| Benchmark Bollinger mean reversion 1H | ZEC | SHORT | Bollinger mean reversion | 60m | 2,0x | 1484,74299 | 1485,04000 | 1542,92731 | 2219,69077 | 1397,46652 | €519,64 | €1.039,27 | €40,73 | €-0,21 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 1349,03975 | 1485,04000 | 1423,61482 | 681,26508 | 1499,54369 | €472,42 | €944,85 | €0,00 | €95,25 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,79556 | 2,98600 | 2,90562 | 1,41176 | 3,07204 | €532,88 | €1.065,76 | €0,00 | €72,60 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,16668 | 0,17192 | 0,15696 | 0,08418 | 0,18808 | €410,73 | €821,46 | €47,94 | €25,81 |
| Benchmark trend following EMA 1H | BR | LONG | Trend following EMA | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €203,60 | €407,20 | €48,86 | €-0,08 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1515,93042 | €43,70 | €87,39 | €0,00 | €7,49 |
| Scanner Bottom 5 Short 1H | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €196,36 | €392,72 | €47,13 | €-37,52 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1515,93042 | €47,66 | €95,32 | €0,00 | €8,17 |
| Scanner Bottom10 Short | POWER | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-38,14 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-0,22 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,23875 | €621,00 | €1.242,00 | €52,43 | €-0,25 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,18970 | €507,91 | €1.015,82 | €52,43 | €-0,20 |
| Scanner Top15 Long | BR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €218,31 | €436,62 | €52,39 | €-0,09 |
| Scanner Bottom15 Short | POWER | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-38,14 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-0,22 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,23875 | €621,00 | €1.242,00 | €52,43 | €-0,25 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,18970 | €507,91 | €1.015,82 | €52,43 | €-0,20 |
| Scanner Top20 Long | BR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €218,31 | €436,62 | €52,39 | €-0,09 |
| Scanner Bottom20 Short | POWER | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-38,14 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €35,25 | €70,50 | €0,00 | €6,05 |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €33,05 | €66,09 | €0,00 | €5,67 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €341,89 | €683,78 | €0,00 | €58,63 |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1639,00507 | €477,40 | €954,81 | €44,90 | €-0,19 |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,26397 | €531,77 | €1.063,54 | €44,90 | €-0,21 |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,19148 | €434,93 | €869,86 | €44,89 | €-0,17 |
| Scanner Top5 Btc Btc 2 3 V1 | BR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €186,94 | €373,89 | €44,87 | €-0,07 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €368,96 | €737,91 | €0,00 | €63,27 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €366,47 | €732,95 | €0,00 | €62,85 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1590,01389 | €356,23 | €712,46 | €0,00 | €61,09 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1590,01389 | €356,44 | €712,87 | €0,00 | €61,12 |
| Combo Trend | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,79556 | 2,98600 | 2,90562 | 1,41176 | 3,07204 | €516,79 | €1.033,59 | €0,00 | €70,41 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 1349,03975 | 1485,04000 | 1423,61482 | 681,26508 | 1499,54369 | €458,08 | €916,17 | €0,00 | €92,36 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,16668 | 0,17192 | 0,15696 | 0,08418 | 0,18808 | €398,30 | €796,60 | €46,48 | €25,03 |
| Combo Trend | BR | LONG | Combo Trend | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €197,44 | €394,87 | €47,38 | €-0,08 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,28183 | 1,30578 | 1,23929 | 0,64732 | 1,34989 | €653,10 | €1.306,20 | €43,35 | €24,41 |
| Combo Adaptive | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,18918 | €35,04 | €70,07 | €2,60 | €-1,16 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1485,04000 | 1425,55871 | 690,20536 | 1505,72053 | €14,74 | €29,48 | €0,00 | €2,55 |
| Combo Adaptive | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,98600 | 2,91914 | 1,41176 | 3,02177 | €645,80 | €1.291,60 | €0,00 | €87,99 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,17192 | 0,16668 | 0,08418 | 0,18419 | €497,62 | €995,25 | €0,00 | €31,27 |
| Combo Adaptive | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €220,13 | €440,26 | €52,83 | €-0,09 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1367,76350 | 1485,04000 | 1441,84940 | 690,72057 | 1515,93042 | €31,44 | €62,87 | €0,00 | €5,39 |
| Combo Adaptive Quality7 V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,98600 | 2,91914 | 1,41176 | 3,02177 | €576,49 | €1.152,98 | €0,00 | €78,54 |
| Combo Adaptive Quality7 V1 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €197,86 | €395,73 | €47,49 | €-0,08 |
| Combo Adaptive Quality7 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,18970 | €460,06 | €920,11 | €47,49 | €-0,18 |
| Combo Adaptive Partial 1R V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,98600 | 2,91914 | 1,41176 | 3,02177 | €620,33 | €1.240,66 | €0,00 | €84,52 |
| Combo Adaptive Partial 1R V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,17192 | 0,16668 | 0,08418 | 0,18419 | €478,13 | €956,27 | €0,00 | €30,04 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1625,03524 | €544,86 | €1.089,72 | €51,25 | €-0,22 |
| Combo Adaptive Partial 1R V1 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €213,50 | €427,01 | €51,24 | €-0,09 |
| Combo Adaptive Runner25 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €73,50 | €146,99 | €4,81 | €-0,00 |
| Combo Adaptive Runner25 V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,14149 | €31,43 | €62,85 | €2,33 | €-1,04 |
| Combo Adaptive Runner25 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1485,04000 | 1425,55871 | 690,20536 | 1575,20916 | €12,91 | €25,81 | €0,00 | €2,23 |
| Combo Adaptive Tp3 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €72,15 | €144,29 | €4,72 | €-0,00 |
| Combo Adaptive Tp3 V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,14149 | €30,84 | €61,68 | €2,29 | €-1,02 |
| Combo Adaptive Tp3 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1485,04000 | 1425,55871 | 690,20536 | 1575,20916 | €12,67 | €25,33 | €0,00 | €2,19 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €433,46 | €866,91 | €44,08 | €75,03 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €427,66 | €855,33 | €43,49 | €74,03 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1575,20914 | €389,09 | €778,18 | €39,56 | €67,35 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,18918 | €28,88 | €57,77 | €2,14 | €-0,95 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1367,76350 | 1485,04000 | 1422,00867 | 690,72057 | 1515,93042 | €18,84 | €37,68 | €0,00 | €3,23 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,80756 | 2,98600 | 2,91919 | 1,41782 | 3,03459 | €630,04 | €1.260,08 | €0,00 | €80,09 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,17192 | 0,16668 | 0,08418 | 0,18419 | €485,00 | €970,00 | €0,00 | €30,47 |
| Combo Adaptive Side Regime Guard V1 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €214,56 | €429,12 | €51,49 | €-0,09 |
| Master Adaptive Gb20 Be V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €435,60 | €871,21 | €44,29 | €75,41 |
| Master Adaptive Gb20 Partial V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €435,14 | €870,28 | €44,25 | €75,33 |
| 1H Fast V3 Nohigh Regime Guard V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €426,97 | €1.280,91 | €0,00 | €40,24 |
| 1H Fast V3 Nohigh Regime Guard V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €157,74 | €473,22 | €52,94 | €-0,09 |
| 1H Fast V3 Nohigh Regime Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €537,43 | €1.612,28 | €52,94 | €-0,32 |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €482,38 | €1.447,14 | €52,93 | €-0,29 |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €10,46 | €31,38 | €0,57 | €-0,01 |
| Main Side Regime Guard V1 | SUI | SHORT | Confluenza trend | 240m | 3,0x | 0,72995 | 0,72995 | 0,77421 | 0,96962 | 0,64144 | €294,19 | €882,58 | €53,51 | €-0,00 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,29295 | 1,30578 | 1,37261 | 1,71747 | 1,13364 | €83,64 | €250,92 | €15,46 | €-2,49 |
| Combo Trend Side Regime Guard V1 | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,79556 | 2,98600 | 2,90562 | 1,41176 | 3,07204 | €609,18 | €1.218,36 | €0,00 | €83,00 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 1349,03975 | 1485,04000 | 1423,61482 | 681,26508 | 1499,54369 | €539,97 | €1.079,95 | €0,00 | €108,87 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,16668 | 0,17192 | 0,15696 | 0,08418 | 0,18808 | €469,50 | €939,00 | €54,79 | €29,50 |
| Combo Trend Side Regime Guard V1 | BR | LONG | Combo Trend | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €232,73 | €465,46 | €55,86 | €-0,09 |
| 1H Fast Nohigh Cap75 Short Only V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09985 | €133,98 | €401,95 | €48,23 | €-38,41 |
| 1H Fast Nohigh Cap75 Short Only V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €393,59 | €1.180,76 | €0,00 | €37,10 |
| 1H Fast Nohigh Cap75 Short Only V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €493,19 | €1.479,57 | €48,58 | €-0,30 |
| 1H Fast Nohigh Cap75 Short Only V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €442,67 | €1.328,02 | €48,57 | €-0,27 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €12,01 | €36,02 | €0,65 | €-0,01 |
| 1H Balanced V3 Long Only V1 | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,66728 | 0,63674 | 0,42768 | 0,78955 | €126,91 | €380,72 | €0,00 | €18,26 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16668 | 0,11196 | 0,18419 | €289,96 | €869,88 | €0,00 | €27,33 |
| 1H Balanced V3 Long Only V1 | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,86052 | 2,00600 | 3,23875 | €365,90 | €1.097,70 | €46,34 | €-0,22 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1415,48789 | 997,65136 | 1625,03524 | €328,43 | €985,30 | €46,33 | €-0,20 |
| Scanner Bottom5 Short Profit Lock V1 | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €197,88 | €395,77 | €47,49 | €-37,81 |
| Scanner Bottom5 Short Mfe Trail V1 | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €198,18 | €396,37 | €47,56 | €-37,87 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Quality7 V1 | ARB | LONG | 2026-09-17T18:30:00+00:00 | 0,17692 | €25,47 | 0,54 | STOP |
| 1H Fast Tp2 V1 | ARB | LONG | 2026-09-17T18:30:00+00:00 | 0,17745 | €39,23 | 0,77 | STOP |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | 2026-09-17T18:00:00+00:00 | 3,03399 | €100,05 | 1,96 | TARGET |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €100,45 | 1,97 | TARGET |
| Combo Adaptive Partial 1R V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €99,02 | 1,97 | TARGET |
| Combo Adaptive | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €103,06 | 1,97 | TARGET |
| 1H Fast No Pepe V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18227 | €76,87 | 1,46 | TARGET |
| 1H Balanced V3 Long Only V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €90,08 | 1,97 | TARGET |
| Bilanciata 1H V3 Filtered | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €95,21 | 1,97 | TARGET |
| 1H Fast V3 No Esports V1 | ARB | LONG | 2026-09-17T17:45:00+00:00 | 0,17686 | €70,18 | 1,46 | TARGET |
| 1H Fast V3 No Esports Stress Guard V1 | ARB | LONG | 2026-09-17T17:45:00+00:00 | 0,17775 | €78,44 | 1,47 | TARGET |
| 1H Fast V3 No Esports Mfe Lock V1 | ARB | LONG | 2026-09-17T17:45:00+00:00 | 0,17686 | €74,84 | 1,46 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
