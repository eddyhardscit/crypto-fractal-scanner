# Paper trading automatico KuCoin

Generato: 2026-08-14T11:04:43+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-14T10:05:49+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-14T10:05:49+00:00 | 2026-08-14T10:05:49+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-14T09:45:00+00:00 | 2026-08-14T09:45:00+00:00 | 6,3 min | 25,0 min | OK |
| 60m | 12 | 2026-08-14T09:00:00+00:00 | 2026-08-14T09:00:00+00:00 | 6,3 min | 45,0 min | OK |
| 240m | 12 | 2026-08-14T04:00:00+00:00 | 2026-08-14T04:00:00+00:00 | 2,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Expanded V1 | SNDK | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | SKHYNIX | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Donchian 1H | DOGE | 60m | SHORT | -7,44 | 5,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Mean Reversion | BTC | 60m | SHORT | -6,00 | 5,00 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | DOGE | 60m | SHORT | -7,44 | 5,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | DOGE | 60m | SHORT | -7,44 | 5,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | SKHYNIX | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | SKHYNIX | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | 60m | SHORT | -7,44 | 6,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | DOGE | 60m | SHORT | -7,44 | 6,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced Long No Rhv V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | EDEN | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,15 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,86 | 6,00 | 1,14 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,62 | 6,00 | 1,38 | STALE_CANDLE | 2,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SNDK | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -3,34 | 6,00 | 2,66 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,26 | 6,00 | 4,74 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 0,99 | 6,00 | 5,01 | STALE_CANDLE | 2,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Side Regime Guard V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 Be V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 Partial V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend Side Regime Guard V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.731,82 | -2,68% | €-16,53 | €3.000,00 | -0,55% | 5 | 40 | 35,00% | 0,78 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 40 | 1295 | PRIME INDICAZIONI | 100 (mancano 60) |

- Trade del Principale 4H chiusi: **40**; win rate **35,00%**; profit factor **0,78**.
- Expectancy: **€-7,08** per trade; P&L netto: **€-283,07**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.731,82 | €1.286,74 | €3.860,23 | €194,28 | €14,79 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.678,56 | €4.649,93 | €9.299,86 | €160,67 | €50,21 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 4 | €10.527,70 | €2.028,02 | €6.084,05 | €104,55 | €74,28 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €10.506,14 | €3.438,21 | €10.314,63 | €104,97 | €72,21 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.427,14 | €4.540,45 | €9.080,90 | €156,89 | €49,03 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 4 | €10.420,33 | €3.399,91 | €10.199,73 | €103,61 | €80,56 |
| TEST | Main Side Regime Guard V1 | 5 | €10.411,79 | €2.118,53 | €6.355,60 | €155,48 | €44,72 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 2 | €10.382,24 | €1.685,04 | €5.055,13 | €0,00 | €72,04 |
| TEST | 1H Fast Nohigh Cap75 V1 | 6 | €10.340,80 | €3.503,92 | €10.511,76 | €152,60 | €97,70 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.329,69 | €2.006,67 | €6.020,01 | €152,93 | €73,90 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.308,28 | €3.044,20 | €9.132,59 | €157,27 | €52,82 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €10.226,81 | €3.346,80 | €10.040,39 | €102,18 | €70,29 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.178,68 | €3.367,42 | €10.102,25 | €101,24 | €120,78 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.178,25 | €5.432,18 | €10.864,35 | €149,28 | €75,58 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.168,22 | €2.738,64 | €5.477,28 | €203,37 | €57,25 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €10.130,84 | €139,31 | €417,94 | €50,15 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €10.106,20 | €3.294,62 | €9.883,86 | €151,79 | €68,22 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 6 | €10.083,47 | €3.416,73 | €10.250,18 | €148,81 | €95,27 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.063,01 | €3.574,44 | €7.148,87 | €151,50 | €6,90 |
| TEST | Btc Donchian 1H | 1 | €10.058,10 | €1.301,67 | €3.905,01 | €0,00 | €60,81 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.039,42 | €2.004,50 | €6.013,51 | €150,99 | €97,92 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €10.013,79 | €1.152,72 | €3.458,17 | €0,00 | €53,85 |
| TEST | Doge Ema 1H | 1 | €10.011,70 | €1.155,63 | €3.466,88 | €49,92 | €28,47 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 8 | €10.007,56 | €3.973,75 | €7.947,50 | €99,11 | €173,42 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.002,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 4 | €10.000,95 | €3.303,34 | €9.910,01 | €149,55 | €62,40 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 6 | €9.994,09 | €1.980,18 | €5.940,53 | €151,21 | €0,40 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.989,13 | €1.413,45 | €2.826,90 | €49,75 | €38,45 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.971,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €9.958,96 | €2.980,95 | €8.942,84 | €49,80 | €77,10 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €9.944,63 | €1.295,48 | €3.886,44 | €49,75 | €-2,33 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.930,87 | €1.406,00 | €2.812,00 | €49,49 | €32,33 |
| TEST | Btc Ema 1H | 1 | €9.926,82 | €1.141,05 | €3.423,15 | €0,00 | €67,15 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.901,43 | €2.071,84 | €4.143,68 | €100,29 | €158,82 |
| TEST | Ampia 4H | 5 | €9.886,46 | €1.961,33 | €3.922,65 | €148,09 | €12,12 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.870,59 | €4.759,21 | €9.518,42 | €197,93 | €-23,41 |
| TEST | Bilanciata 1H V2 | 5 | €9.857,34 | €2.605,16 | €7.815,47 | €146,25 | €41,79 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €9.836,81 | €2.673,82 | €5.347,63 | €195,68 | €68,12 |
| TEST | Combo Adaptive Runner25 V1 | 8 | €9.836,12 | €3.904,34 | €7.808,68 | €97,46 | €170,41 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €9.826,20 | €2.725,63 | €8.176,89 | €146,67 | €158,22 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.817,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.813,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €9.811,17 | €1.238,27 | €3.714,81 | €147,46 | €109,70 |
| TEST | Combo Adaptive Long Only V1 | 6 | €9.785,70 | €2.646,36 | €5.292,73 | €194,66 | €66,67 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.781,27 | €2.046,69 | €4.093,39 | €99,07 | €156,89 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €9.775,94 | €1.230,80 | €2.461,59 | €48,59 | €131,66 |
| TEST | Rapida 1H V2 | 1 | €9.772,66 | €1.461,59 | €4.384,76 | €49,11 | €6,97 |
| TEST | Scanner Bottom10 Short | 6 | €9.771,84 | €4.868,27 | €9.736,53 | €97,72 | €67,61 |
| TEST | Scanner Bottom15 Short | 6 | €9.771,84 | €4.868,27 | €9.736,53 | €97,72 | €67,61 |
| TEST | Scanner Bottom20 Short | 6 | €9.771,84 | €4.868,27 | €9.736,53 | €97,72 | €67,61 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €9.761,99 | €2.707,82 | €8.123,46 | €145,71 | €157,19 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.757,74 | €206,68 | €413,36 | €0,00 | €120,61 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.753,95 | €1.231,32 | €3.693,95 | €195,08 | €107,46 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.749,98 | €2.879,32 | €8.637,97 | €148,75 | €49,96 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.731,55 | €2.036,29 | €4.072,58 | €98,57 | €156,09 |
| TEST | Combo Mean Reversion | 1 | €9.728,99 | €1.946,42 | €3.892,84 | €46,71 | €-0,78 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.716,12 | €3.221,09 | €9.663,28 | €144,29 | €144,99 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €9.706,12 | €4.839,94 | €9.679,89 | €96,59 | €67,79 |
| TEST | Global Confluence puro 1H | 1 | €9.700,99 | €1.512,09 | €3.024,18 | €48,39 | €24,84 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.697,12 | €2.449,27 | €4.898,54 | €193,94 | €39,73 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.696,17 | €1.935,76 | €3.871,51 | €0,00 | €42,91 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.691,35 | €4.832,58 | €9.665,16 | €96,44 | €67,69 |
| TEST | Forza relativa 1H V2 | 5 | €9.683,34 | €3.368,25 | €6.736,51 | €145,60 | €54,15 |
| TEST | Sol Adaptive 1H | 0 | €9.674,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 8 | €9.652,37 | €3.831,40 | €7.662,80 | €95,64 | €167,23 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.635,01 | €204,08 | €408,16 | €0,00 | €119,09 |
| TEST | Eth Ema 1H | 0 | €9.622,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.616,78 | €4.795,39 | €9.590,79 | €95,70 | €67,17 |
| TEST | Combo Adaptive Partial 1R V1 | 8 | €9.609,71 | €3.815,77 | €7.631,55 | €95,17 | €166,53 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €9.608,95 | €1.780,13 | €5.340,40 | €143,47 | €71,63 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.574,78 | €2.655,14 | €5.310,27 | €191,50 | €41,11 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.560,90 | €3.213,74 | €9.641,23 | €142,79 | €121,62 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.553,79 | €1.999,09 | €3.998,19 | €96,77 | €153,24 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.515,69 | €4.064,03 | €8.128,06 | €191,14 | €-21,79 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.505,57 | €4.059,71 | €8.119,42 | €190,93 | €-21,77 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.505,50 | €1.356,82 | €4.070,45 | €142,73 | €54,04 |
| TEST | Combo Trend | 9 | €9.475,09 | €2.667,77 | €5.335,55 | €189,50 | €98,10 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €9.470,38 | €2.574,21 | €5.148,43 | €188,39 | €65,58 |
| TEST | Master Adaptive V1 | 5 | €9.468,81 | €4.044,01 | €8.088,01 | €190,19 | €-21,68 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €9.464,84 | €2.572,71 | €5.145,42 | €188,28 | €65,54 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.450,36 | €3.456,78 | €6.913,56 | €139,67 | €109,65 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.449,17 | €2.982,76 | €5.965,52 | €188,53 | €73,73 |
| TEST | Forza relativa 1H V1 | 6 | €9.411,34 | €2.803,25 | €5.606,50 | €188,15 | €3,87 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €9.400,06 | €2.555,10 | €5.110,20 | €186,99 | €65,09 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.365,36 | €2.164,98 | €4.329,96 | €184,17 | €214,11 |
| TEST | Scanner Top10 Long | 5 | €9.365,21 | €2.525,43 | €5.050,87 | €187,30 | €52,72 |
| TEST | Scanner Top15 Long | 5 | €9.365,21 | €2.525,43 | €5.050,87 | €187,30 | €52,72 |
| TEST | Scanner Top20 Long | 5 | €9.365,21 | €2.525,43 | €5.050,87 | €187,30 | €52,72 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.343,00 | €3.990,28 | €7.980,55 | €187,67 | €-21,39 |
| TEST | Combo Scanner | 5 | €9.281,18 | €2.742,78 | €5.485,56 | €185,62 | €67,34 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.220,59 | €2.506,32 | €5.012,63 | €183,42 | €63,85 |
| TEST | 1H Fast V3 Long Only V1 | 4 | €9.148,76 | €1.694,88 | €5.084,64 | €136,60 | €68,20 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.101,40 | €192,15 | €384,31 | €46,12 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 6 | €8.948,28 | €3.586,88 | €7.173,75 | €131,96 | €75,03 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.731,82 | €-283,07 | 40 | 40 | 35,00% | 0,78 | €-7,08 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.678,56 | €632,45 | 59 | 59 | 47,46% | 1,44 | €10,72 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.527,70 | €453,69 | 55 | 55 | 50,91% | 1,42 | €8,25 | 3,00% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.506,14 | €436,77 | 103 | 103 | 43,69% | 1,20 | €4,24 | 3,21% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.427,14 | €382,12 | 27 | 27 | 44,44% | 1,67 | €14,15 | 3,63% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.420,33 | €340,71 | 29 | 29 | 48,28% | 1,57 | €11,75 | 3,55% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.411,79 | €367,24 | 20 | 20 | 50,00% | 1,85 | €18,36 | 2,40% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.382,24 | €309,95 | 29 | 29 | 51,72% | 1,42 | €10,69 | 2,31% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.340,80 | €244,16 | 91 | 91 | 41,76% | 1,12 | €2,68 | 6,15% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.329,69 | €256,02 | 37 | 37 | 51,35% | 1,36 | €6,92 | 4,32% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.308,28 | €257,89 | 82 | 82 | 39,02% | 1,16 | €3,15 | 4,31% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.226,81 | €159,28 | 61 | 61 | 47,54% | 1,11 | €2,61 | 3,56% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.178,68 | €58,92 | 94 | 94 | 42,55% | 1,03 | €0,63 | 3,64% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.178,25 | €103,88 | 50 | 50 | 46,00% | 1,11 | €2,08 | 5,79% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.168,22 | €113,82 | 67 | 67 | 43,28% | 1,07 | €1,70 | 7,66% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.130,84 | €131,11 | 28 | 28 | 39,29% | 1,25 | €4,68 | 2,27% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.106,20 | €40,71 | 92 | 92 | 41,30% | 1,02 | €0,44 | 5,76% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.083,47 | €-10,76 | 55 | 55 | 38,18% | 0,99 | €-0,20 | 6,15% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.063,01 | €57,88 | 42 | 42 | 50,00% | 1,07 | €1,38 | 2,94% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.058,10 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.039,42 | €-58,14 | 107 | 107 | 35,51% | 0,97 | €-0,54 | 3,95% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,79 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 1,13% |
| TEST | Doge Ema 1H | Trend following EMA | €10.011,70 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Combo Adaptive | Combo Adaptive | €10.007,56 | €-163,51 | 57 | 57 | 36,84% | 0,85 | €-2,87 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.002,03 | €2,03 | 6 | 6 | 50,00% | 1,02 | €0,34 | 1,50% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.000,95 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,36% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.994,09 | €-3,47 | 92 | 92 | 42,39% | 1,00 | €-0,04 | 6,27% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,76 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Btc Ema 4H | Trend following EMA | €9.989,13 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.971,04 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.958,96 | €-117,76 | 30 | 30 | 43,33% | 0,84 | €-3,93 | 3,94% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,80 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.944,63 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 1,63% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.930,87 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Btc Ema 1H | Trend following EMA | €9.926,82 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,72% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.901,43 | €-255,26 | 34 | 34 | 38,24% | 0,76 | €-7,51 | 6,54% |
| TEST | Ampia 4H | Confluenza trend | €9.886,46 | €-125,24 | 34 | 34 | 23,53% | 0,86 | €-3,68 | 4,36% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.870,59 | €-98,48 | 23 | 23 | 43,48% | 0,79 | €-4,28 | 2,18% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.857,34 | €-181,81 | 59 | 55 | 44,07% | 0,87 | €-3,08 | 5,62% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.836,81 | €-228,54 | 55 | 55 | 34,55% | 0,84 | €-4,16 | 8,46% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.836,12 | €-332,00 | 64 | 64 | 32,81% | 0,74 | €-5,19 | 6,25% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.826,20 | €-330,30 | 77 | 77 | 48,05% | 0,78 | €-4,29 | 6,78% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.817,19 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,06% |
| TEST | Sol Ema 1H | Trend following EMA | €9.813,68 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 2,63% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.811,17 | €-296,11 | 60 | 60 | 40,00% | 0,82 | €-4,94 | 4,70% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.785,70 | €-278,21 | 35 | 35 | 31,43% | 0,67 | €-7,95 | 4,45% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.781,27 | €-373,52 | 39 | 39 | 33,33% | 0,69 | €-9,58 | 6,13% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.775,94 | €-354,13 | 35 | 35 | 28,57% | 0,57 | €-10,12 | 4,71% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.772,66 | €-233,44 | 28 | 25 | 35,71% | 0,71 | €-8,34 | 3,89% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.771,84 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.771,84 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.771,84 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.761,99 | €-393,48 | 121 | 121 | 38,02% | 0,85 | €-3,25 | 6,75% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.757,74 | €-362,51 | 15 | 15 | 33,33% | 0,35 | €-24,17 | 3,11% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.753,95 | €-351,10 | 65 | 65 | 44,62% | 0,81 | €-5,40 | 4,93% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.749,98 | €-297,68 | 38 | 38 | 34,21% | 0,60 | €-7,83 | 4,03% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.731,55 | €-422,45 | 49 | 49 | 38,78% | 0,69 | €-8,62 | 5,80% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.728,99 | €-267,90 | 28 | 28 | 35,71% | 0,72 | €-9,57 | 4,71% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.716,12 | €-427,91 | 82 | 82 | 40,24% | 0,79 | €-5,22 | 5,62% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.706,12 | €-358,39 | 36 | 36 | 33,33% | 0,58 | €-9,96 | 5,27% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.700,99 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.697,12 | €-339,61 | 40 | 40 | 30,00% | 0,74 | €-8,49 | 4,45% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.696,17 | €-344,88 | 66 | 66 | 42,42% | 0,80 | €-5,23 | 6,53% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.691,35 | €-373,06 | 37 | 37 | 32,43% | 0,53 | €-10,08 | 5,27% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.683,34 | €-365,97 | 68 | 65 | 38,24% | 0,83 | €-5,38 | 8,11% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.674,16 | €-325,84 | 9 | 9 | 22,22% | 0,17 | €-36,20 | 3,94% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.652,37 | €-512,62 | 45 | 45 | 31,11% | 0,50 | €-11,39 | 6,25% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.635,01 | €-483,73 | 15 | 15 | 20,00% | 0,16 | €-32,25 | 4,33% |
| TEST | Eth Ema 1H | Trend following EMA | €9.622,18 | €-377,82 | 10 | 10 | 20,00% | 0,12 | €-37,78 | 3,78% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.616,78 | €-447,14 | 64 | 64 | 32,81% | 0,68 | €-6,99 | 6,41% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.609,71 | €-554,55 | 58 | 58 | 34,48% | 0,55 | €-9,56 | 6,07% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.608,95 | €-459,44 | 52 | 52 | 34,62% | 0,68 | €-8,84 | 8,14% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.574,78 | €-463,04 | 36 | 36 | 25,00% | 0,65 | €-12,86 | 6,03% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.560,90 | €-558,04 | 95 | 95 | 37,89% | 0,74 | €-5,87 | 6,72% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.553,79 | €-597,40 | 56 | 56 | 37,50% | 0,62 | €-10,67 | 7,59% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.515,69 | €-456,42 | 39 | 39 | 20,51% | 0,59 | €-11,70 | 6,68% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.505,57 | €-466,57 | 34 | 34 | 26,47% | 0,57 | €-13,72 | 6,27% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.505,50 | €-545,83 | 39 | 39 | 30,77% | 0,54 | €-14,00 | 7,00% |
| TEST | Combo Trend | Combo Trend | €9.475,09 | €-622,46 | 88 | 88 | 31,82% | 0,74 | €-7,07 | 9,82% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.470,38 | €-592,54 | 40 | 40 | 27,50% | 0,53 | €-14,81 | 9,16% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.468,81 | €-503,45 | 36 | 36 | 25,00% | 0,60 | €-13,98 | 6,08% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.464,84 | €-598,04 | 44 | 44 | 29,55% | 0,53 | €-13,59 | 9,46% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.450,36 | €-657,74 | 58 | 58 | 27,59% | 0,54 | €-11,34 | 7,38% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.449,17 | €-620,05 | 33 | 33 | 21,21% | 0,51 | €-18,79 | 6,64% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.411,34 | €-589,79 | 78 | 78 | 28,21% | 0,67 | €-7,56 | 8,31% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.400,06 | €-662,39 | 36 | 36 | 27,78% | 0,42 | €-18,40 | 8,92% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.365,36 | €-845,83 | 39 | 39 | 23,08% | 0,50 | €-21,69 | 9,06% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.365,21 | €-684,88 | 39 | 39 | 33,33% | 0,42 | €-17,56 | 9,13% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.365,21 | €-684,88 | 39 | 39 | 33,33% | 0,42 | €-17,56 | 9,13% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.365,21 | €-684,88 | 39 | 39 | 33,33% | 0,42 | €-17,56 | 9,13% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.343,00 | €-629,62 | 71 | 71 | 47,89% | 0,57 | €-8,87 | 7,33% |
| TEST | Combo Scanner | Combo Scanner | €9.281,18 | €-784,58 | 64 | 64 | 32,81% | 0,58 | €-12,26 | 10,13% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.220,59 | €-840,67 | 48 | 48 | 29,17% | 0,33 | €-17,51 | 9,50% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.148,76 | €-916,35 | 72 | 72 | 27,78% | 0,56 | €-12,73 | 10,12% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.101,40 | €-898,33 | 31 | 31 | 16,13% | 0,32 | €-28,98 | 10,58% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.948,28 | €-1.124,73 | 71 | 71 | 29,58% | 0,37 | €-15,84 | 11,05% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00378 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €14,13 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | CYS | LONG | Confluenza trend | 240m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,91631 | €134,84 | €404,53 | €48,54 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 62813,56000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €0,66 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,91631 | €134,24 | €402,71 | €48,32 | €0,00 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,04289 | 1,04289 | 1,03001 | 1,38531 | 0,79260 | €139,17 | €417,52 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,06956 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €0,37 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 1,00378 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €0,03 |
| 1H Balanced Long No Rhv V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,86025 | €131,62 | €394,86 | €0,00 | €0,00 |
| 1H Balanced Long No Rhv V1 | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| 1H Balanced Long No Rhv V1 | APR | LONG | Confluenza trend | 60m | 3,0x | 0,49291 | 0,49291 | 0,43376 | 0,33107 | 0,61121 | €131,87 | €395,61 | €47,47 | €0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00937 | €130,81 | €392,43 | €47,09 | €54,06 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1181,69000 | 1155,07338 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,73 | €-0,02 |
| 1H Balanced Short Trend Down Strict V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,03900 | 1,03900 | 1,03001 | 1,38014 | 0,78964 | €138,10 | €414,31 | €0,00 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63436,91008 | 62813,56000 | 64350,40159 | 84265,36222 | 61609,92707 | €1.150,82 | €3.452,45 | €49,72 | €33,92 |
| 1H Balanced Short Trend Down Strict V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,06956 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €28,48 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 63596,27820 | 62813,56000 | 64512,06461 | 84477,05621 | 61764,70539 | €1.127,13 | €3.381,38 | €48,69 | €41,62 |
| Bilanciata 1H V2 | CYS | LONG | Confluenza trend V2 | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,86025 | €136,27 | €408,82 | €0,00 | €0,00 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 1,00378 | 1,01986 | 1,33548 | 0,97642 | €37,09 | €111,28 | €1,60 | €0,18 |
| Bilanciata 1H V2 | BEAT | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,96465 | 0,96465 | 1,08040 | 1,28137 | 0,73313 | €124,99 | €374,96 | €45,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63106,84706 | 84757,27849 | 61969,58760 | €1.129,53 | €3.388,60 | €0,00 | €52,77 |
| Bilanciata 1H V3 Filtered | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,91879 | €140,87 | €422,61 | €50,71 | €0,00 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06956 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €0,05 |
| 1H Fast Score 6 75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.575,50 | €4.726,51 | €0,00 | €73,61 |
| 1H Fast Score 6 75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €145,36 | €436,08 | €0,00 | €0,00 |
| 1H Fast Score 6 75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €142,15 | €426,45 | €51,17 | €-0,00 |
| 1H Fast Score 6 75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €32,86 | €98,57 | €1,97 | €1,38 |
| 1H Fast Score 6 75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.542,34 | €4.627,02 | €51,82 | €-2,78 |
| 1H Fast Score 6 75 No Trend Up V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.533,61 | €4.600,84 | €0,00 | €71,65 |
| 1H Fast Score 6 75 No Trend Up V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €141,49 | €424,48 | €0,00 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €138,37 | €415,11 | €49,81 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €31,98 | €95,95 | €1,92 | €1,35 |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.501,33 | €4.504,00 | €50,44 | €-2,70 |
| 1H Fast Score 6 75 Range Only V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.542,02 | €4.626,07 | €0,00 | €72,04 |
| 1H Fast Score 6 75 Range Only V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,48830 | 1,48830 | 1,48830 | 0,99964 | 1,75619 | €143,02 | €429,06 | €0,00 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.591,68 | €4.775,04 | €0,00 | €74,36 |
| 1H Fast Score 6 75 Cost Aware V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €145,92 | €437,77 | €0,00 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95974 | 0,95974 | 1,07491 | 1,27485 | 0,78699 | €145,66 | €436,97 | €52,44 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03776 | 0,03777 | 0,04229 | 0,05016 | 0,03097 | €144,75 | €434,26 | €52,11 | €-0,09 |
| 1H Fast Nohigh Cap75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.585,67 | €4.757,02 | €0,00 | €74,08 |
| 1H Fast Nohigh Cap75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €200,91 | €602,72 | €51,68 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,06956 | 0,07069 | 0,09286 | 0,06873 | €1.537,89 | €4.613,67 | €51,67 | €22,84 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €143,81 | €431,44 | €47,91 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1161,28635 | 1181,69000 | 1161,28781 | 779,99733 | 1196,37370 | €15,47 | €46,40 | €0,00 | €0,82 |
| 1H Fast Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €20,17 | €60,51 | €1,35 | €-0,04 |
| 1H Fast Long Btc 1 3 Cap75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €139,31 | €417,94 | €50,15 | €0,00 |
| 1H Fast No Pepe V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.518,20 | €4.554,59 | €0,00 | €70,93 |
| 1H Fast No Pepe V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,51880 | 1,51880 | 1,51880 | 1,02013 | 1,79219 | €136,73 | €410,18 | €0,00 | €0,00 |
| 1H Fast No Pepe V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.503,80 | €4.511,41 | €50,53 | €7,17 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1161,28635 | 1181,69000 | 1161,28781 | 779,99733 | 1196,37370 | €34,85 | €104,55 | €0,00 | €1,84 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00782 | 0,00860 | 0,00688 | 0,00525 | 0,00923 | €137,46 | €412,39 | €49,49 | €40,90 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €36,38 | €109,13 | €1,22 | €-0,07 |
| 1H Fast Tp2 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62377,95391 | €1.482,17 | €4.446,51 | €0,00 | €69,25 |
| 1H Fast Tp2 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64299 | 1,64299 | 1,47977 | 1,10354 | 1,96941 | €161,09 | €483,28 | €48,01 | €0,00 |
| 1H Fast Tp2 V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98286 | €55,98 | €167,93 | €1,88 | €0,27 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,68886 | €146,30 | €438,91 | €48,73 | €-0,00 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00803 | 0,00860 | 0,00706 | 0,00539 | 0,00995 | €133,72 | €401,16 | €48,14 | €28,42 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03778 | 0,03777 | 0,04232 | 0,05019 | 0,02871 | €9,36 | €28,07 | €3,37 | €0,01 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1182,39901 | 1181,69000 | 1161,14575 | 794,17800 | 1224,90555 | €15,88 | €47,65 | €0,86 | €-0,03 |
| Rapida 1H V2 | XRP | SHORT | Momentum / breakout V2 | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.461,59 | €4.384,76 | €49,11 | €6,97 |
| Rapida 1H V3 Filtered | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.474,48 | €4.423,44 | €0,00 | €68,89 |
| Rapida 1H V3 Filtered | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €177,34 | €532,02 | €45,61 | €0,00 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €135,20 | €405,61 | €48,67 | €55,87 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €776,07 | €2.328,22 | €46,56 | €32,69 |
| Rapida 1H V3 Filtered | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €144,72 | €434,17 | €4,86 | €-0,26 |
| 1H Fast V3 Cap75 V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.501,29 | €4.503,87 | €0,00 | €70,14 |
| 1H Fast V3 Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €139,51 | €418,54 | €50,22 | €0,00 |
| 1H Fast V3 Cap75 V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €152,00 | €456,00 | €50,63 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €17,79 | €53,38 | €1,07 | €0,75 |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.484,03 | €4.452,08 | €49,86 | €-2,67 |
| 1H Fast V3 Nohigh V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.489,03 | €4.467,09 | €0,00 | €69,57 |
| 1H Fast V3 Nohigh V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €187,10 | €561,31 | €48,13 | €0,00 |
| 1H Fast V3 Nohigh V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06991 | 0,06956 | 0,07069 | 0,09286 | 0,06873 | €1.375,16 | €4.125,47 | €46,21 | €20,42 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €131,98 | €395,95 | €47,51 | €54,54 |
| 1H Fast V3 Nohigh V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €11,94 | €35,81 | €0,72 | €0,50 |
| 1H Fast V3 Nohigh V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €25,88 | €77,64 | €1,73 | €-0,05 |
| 1H Fast V3 Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,46019 | 1,46056 | 0,98076 | 1,72303 | €127,65 | €382,94 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €757,07 | €2.271,20 | €45,42 | €31,89 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00782 | 0,00860 | 0,00688 | 0,00525 | 0,00923 | €126,18 | €378,54 | €45,42 | €37,54 |
| 1H Fast V3 Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €683,99 | €2.051,96 | €45,76 | €-1,23 |
| 1H Fast V3 Long Nohigh Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €135,24 | €405,73 | €48,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,15 | €405,45 | €48,65 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00725 | 0,00860 | 0,00758 | 0,00487 | 0,00855 | €135,47 | €406,41 | €0,00 | €75,78 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €806,60 | €2.419,81 | €48,39 | €33,97 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €25,80 | €77,41 | €1,73 | €-0,05 |
| 1H Fast V3 No Esports V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.444,46 | €4.333,39 | €0,00 | €67,48 |
| 1H Fast V3 No Esports V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €173,73 | €521,19 | €44,69 | €0,00 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €132,88 | €398,64 | €47,84 | €54,91 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €42,36 | €127,08 | €2,54 | €1,78 |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.420,31 | €4.260,93 | €47,72 | €-2,56 |
| 1H Fast V3 No Esports Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,46019 | 1,46056 | 0,98076 | 1,72303 | €134,07 | €402,21 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €795,15 | €2.385,44 | €47,70 | €33,49 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00782 | 0,00860 | 0,00688 | 0,00525 | 0,00923 | €132,53 | €397,58 | €47,71 | €39,43 |
| 1H Fast V3 No Esports Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €718,39 | €2.155,18 | €48,06 | €-1,29 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.484,18 | €4.452,53 | €0,00 | €69,34 |
| 1H Fast V3 No Esports Mfe Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €178,51 | €535,52 | €45,91 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €136,09 | €408,28 | €48,99 | €56,24 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €781,18 | €2.343,53 | €46,86 | €32,90 |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €145,68 | €437,03 | €4,89 | €-0,26 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.498,86 | €4.496,57 | €0,00 | €70,03 |
| 1H Fast V3 No Esports Stress Guard V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.482,09 | €4.446,28 | €49,80 | €7,07 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €136,31 | €408,93 | €49,07 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,37 | €406,10 | €48,73 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00725 | 0,00860 | 0,00638 | 0,00487 | 0,00855 | €131,77 | €395,30 | €47,44 | €73,71 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €802,37 | €2.407,11 | €48,13 | €33,80 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €25,50 | €76,51 | €1,71 | €-0,05 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00378 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €11,01 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 62813,56000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €1,12 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | CYS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,62778 | 1,62778 | 1,43244 | 0,82203 | 2,05751 | €195,68 | €391,36 | €46,96 | €0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €169,57 | €339,13 | €40,70 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €14,04 | €28,09 | €3,37 | €3,87 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €200,27 | €400,55 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €-0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €196,65 | €393,29 | €47,20 | €54,18 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €1,08 | €-0,03 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 62813,56000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.676,44 | €3.352,88 | €53,65 | €52,21 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06956 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-2,00 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 62813,56000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.636,97 | €3.273,94 | €52,38 | €50,99 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06956 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-1,96 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 57,25563 | 56,62100 | 56,86676 | 85,59716 | 56,22502 | €1.935,76 | €3.871,51 | €0,00 | €42,91 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 64070,44335 | 62813,56000 | 63182,46843 | 95785,31281 | 61815,16374 | €1.516,95 | €3.033,89 | €0,00 | €59,52 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,06956 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,38 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €180,04 | €360,09 | €43,21 | €49,60 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1181,69000 | 1144,24012 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,71 | €0,15 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €0,00 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | APR | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €209,11 | €418,21 | €50,19 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €207,87 | €415,75 | €49,89 | €57,27 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1711,72778 | €13,45 | €26,90 | €0,77 | €-0,02 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.717,08 | €3.434,17 | €0,00 | €67,37 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €199,49 | €398,98 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €-0,00 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €0,04 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,76 | €25,52 | €0,46 | €-0,24 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | APR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €191,43 | €382,85 | €45,94 | €52,74 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €-0,02 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €0,00 | €67,81 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,04 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,24 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | APR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €191,43 | €382,85 | €45,94 | €52,74 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €-0,02 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €0,00 | €67,81 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,04 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,24 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | APR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €191,43 | €382,85 | €45,94 | €52,74 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €-0,02 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €0,00 | €67,81 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,04 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,24 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €192,28 | €384,55 | €46,15 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00934 | €202,99 | €405,99 | €48,72 | €66,35 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €18,79 | €37,58 | €0,00 | €1,79 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,84 | €-0,02 |
| Scanner Top5 Btc Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €180,23 | €360,46 | €43,26 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00934 | €190,28 | €380,55 | €45,67 | €62,20 |
| Scanner Top5 Btc Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €17,61 | €35,23 | €0,00 | €1,68 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,79 | €-0,02 |
| Scanner Top5 Btc Guard V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €200,65 | €401,31 | €48,16 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €201,05 | €402,10 | €0,00 | €74,97 |
| Scanner Top5 Btc Guard V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €861,11 | €1.722,22 | €0,00 | €81,98 |
| Scanner Top5 Btc Guard V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €2,48 | €-0,06 |
| Scanner Top5 Btc Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €183,74 | €367,48 | €44,10 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00934 | €193,98 | €387,96 | €46,56 | €63,41 |
| Scanner Top5 Btc Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €17,96 | €35,91 | €0,00 | €1,71 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,80 | €-0,02 |
| Scanner Top5 Btc Guard Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €195,99 | €391,97 | €47,04 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €196,38 | €392,75 | €0,00 | €73,23 |
| Scanner Top5 Btc Guard Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €841,08 | €1.682,17 | €0,00 | €80,07 |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €2,42 | €-0,06 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €203,12 | €406,24 | €48,75 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €203,52 | €407,04 | €0,00 | €75,90 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €871,69 | €1.743,38 | €0,00 | €82,98 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €2,51 | €-0,07 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €199,63 | €399,27 | €47,91 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €200,03 | €400,06 | €0,00 | €74,59 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €856,73 | €1.713,46 | €0,00 | €81,56 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €2,46 | €-0,06 |
| Scanner Top5 Btc Runner25 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,01 | €370,01 | €44,40 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,01005 | €195,32 | €390,64 | €46,88 | €63,84 |
| Scanner Top5 Btc Runner25 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1674,36149 | €18,08 | €36,16 | €0,00 | €1,72 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,81 | €-0,02 |
| Scanner Top5 Btc Tp3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,11 | €370,23 | €44,43 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,01005 | €195,43 | €390,86 | €46,90 | €63,88 |
| Scanner Top5 Btc Tp3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1674,36149 | €18,09 | €36,18 | €0,00 | €1,72 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,81 | €-0,02 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,06956 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €24,84 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63807,23600 | 62813,56000 | 64828,15178 | 95391,81782 | 61561,22129 | €1.485,14 | €2.970,29 | €47,52 | €46,26 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €179,75 | €359,50 | €43,14 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,06956 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,48 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €185,96 | €371,91 | €44,63 | €51,23 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1181,69000 | 1144,24012 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,71 | €0,15 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1618,90076 | 1617,93000 | 1567,33019 | 817,54488 | 1732,35601 | €12,85 | €25,70 | €0,82 | €-0,02 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62826,12271 | 62813,56000 | 62072,20924 | 31727,19197 | 64032,38427 | €1.946,42 | €3.892,84 | €46,71 | €-0,78 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,06956 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €16,03 |
| Combo Scanner | APR | LONG | Combo Scanner | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €186,01 | €372,01 | €44,64 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €186,31 | €372,62 | €44,71 | €51,33 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1721,01048 | €20,29 | €40,58 | €1,16 | €-0,02 |
| Combo Adaptive | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.768,38 | €3.536,76 | €0,00 | €55,08 |
| Combo Adaptive | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €-0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,51 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €195,39 | €390,77 | €0,00 | €114,02 |
| Combo Adaptive | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1631,04636 | €36,25 | €72,50 | €0,00 | €3,45 |
| Combo Adaptive | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,72 | €0,36 |
| Combo Adaptive Mfe Trail | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive Mfe Trail | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.608,91 | €3.217,82 | €0,00 | €50,11 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €-0,00 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07030 | 0,06956 | 0,07021 | 0,10509 | 0,06827 | €23,31 | €46,62 | €0,00 | €0,49 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00803 | 0,00860 | 0,00706 | 0,00405 | 0,00995 | €172,57 | €345,13 | €41,42 | €24,45 |
| Combo Adaptive Mfe Trail | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1711,72778 | €17,51 | €35,02 | €1,00 | €-0,02 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €206,24 | €412,47 | €0,00 | €120,35 |
| Combo Adaptive Quality7 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1181,69000 | 1147,33658 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €48,59 | €11,31 |
| Combo Adaptive Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,00918 | 56,62100 | 56,18825 | 28,78964 | 58,65105 | €1.719,32 | €3.438,64 | €49,52 | €-23,41 |
| Combo Adaptive Regime V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,96465 | 0,96465 | 1,08040 | 1,44215 | 0,73313 | €206,23 | €412,46 | €49,50 | €-0,00 |
| Combo Adaptive Regime V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €-0,00 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €204,08 | €408,16 | €0,00 | €119,09 |
| Combo Adaptive Long Only V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | APR | LONG | Combo Adaptive | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €199,74 | €399,48 | €47,94 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00916 | €198,58 | €397,17 | €47,66 | €64,91 |
| Combo Adaptive Long Only V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1631,04636 | €18,74 | €37,47 | €0,00 | €1,78 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,80 | €-0,02 |
| Combo Adaptive Partial 1R V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive Partial 1R V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.698,08 | €3.396,15 | €0,00 | €52,89 |
| Combo Adaptive Partial 1R V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €-0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,49 |
| Combo Adaptive Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €187,62 | €375,24 | €0,00 | €109,49 |
| Combo Adaptive Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1631,04636 | €34,81 | €69,62 | €0,00 | €3,31 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,69 | €0,34 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €206,68 | €413,36 | €0,00 | €120,61 |
| Combo Adaptive Runner25 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive Runner25 V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61050,76340 | €1.736,70 | €3.473,39 | €0,00 | €54,09 |
| Combo Adaptive Runner25 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €-0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,51 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00905 | €192,08 | €384,15 | €0,00 | €112,09 |
| Combo Adaptive Runner25 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1674,36149 | €35,39 | €70,77 | €0,00 | €3,37 |
| Combo Adaptive Runner25 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,70 | €0,35 |
| Combo Adaptive Tp3 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive Tp3 V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61050,76340 | €1.704,25 | €3.408,50 | €0,00 | €53,08 |
| Combo Adaptive Tp3 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €-0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,50 |
| Combo Adaptive Tp3 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00905 | €188,49 | €376,98 | €0,00 | €110,00 |
| Combo Adaptive Tp3 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1674,36149 | €34,73 | €69,45 | €0,00 | €3,31 |
| Combo Adaptive Tp3 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,69 | €0,34 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64070,44335 | 62813,56000 | 63108,68675 | 85106,90558 | 62225,21458 | €1.141,05 | €3.423,15 | €0,00 | €67,15 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 62813,56000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €38,45 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62173,77076 | €1.301,67 | €3.905,01 | €0,00 | €60,81 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 62813,56000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €32,33 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 61969,58760 | €1.152,72 | €3.458,17 | €0,00 | €53,85 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,06956 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €28,47 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06952 | 0,06956 | 0,07041 | 0,09234 | 0,06774 | €1.295,48 | €3.886,44 | €49,75 | €-2,33 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.570,92 | €3.141,85 | €45,24 | €-25,77 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,13 | €396,27 | €47,55 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €42,93 | €85,86 | €2,41 | €4,09 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,48 | €398,96 | €47,88 | €0,00 |
| Master Adaptive No Alt V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €24,83 | €49,66 | €1,39 | €2,36 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00782 | 0,00860 | 0,00688 | 0,00395 | 0,00970 | €195,44 | €390,89 | €46,91 | €38,77 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €-0,02 |
| Master Adaptive Strict3 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €190,97 | €381,94 | €45,83 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00665 | 0,00860 | 0,00586 | 0,00336 | 0,00825 | €193,63 | €387,26 | €46,47 | €113,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €823,31 | €1.646,62 | €46,18 | €78,38 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €22,73 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €202,38 | €404,77 | €48,57 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00782 | 0,00860 | 0,00688 | 0,00395 | 0,00970 | €200,40 | €400,79 | €48,09 | €39,75 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1711,72778 | €15,69 | €31,37 | €0,90 | €-0,02 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.550,05 | €3.100,10 | €44,64 | €-25,43 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €195,50 | €391,00 | €46,92 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €42,36 | €84,71 | €2,38 | €4,03 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,31376 | 1,15611 | 0,66345 | 1,78672 | €188,92 | €377,85 | €45,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,62100 | 55,05283 | 28,20787 | 58,27020 | €24,55 | €49,10 | €0,71 | €0,67 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1972,45969 | €1.573,63 | €3.147,26 | €45,32 | €-25,81 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00685 | 0,00860 | 0,00603 | 0,00346 | 0,00931 | €192,44 | €384,89 | €46,19 | €98,28 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1181,69000 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,59 |
| Combo Adaptive Side Regime Guard V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.842,32 | €3.684,64 | €0,00 | €57,38 |
| Combo Adaptive Side Regime Guard V1 | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,06956 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €16,43 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €1,77 |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.578,70 | €3.157,40 | €45,47 | €-25,90 |
| Master Adaptive Gb20 Be V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive Gb20 Be V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,12 | €398,23 | €47,79 | €0,00 |
| Master Adaptive Gb20 Be V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €43,14 | €86,28 | €2,42 | €4,11 |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.577,02 | €3.154,05 | €45,42 | €-25,87 |
| Master Adaptive Gb20 Partial V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive Gb20 Partial V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,90 | €397,81 | €47,74 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €43,09 | €86,19 | €2,42 | €4,10 |
| Master Adaptive Gb20 Loss Cap V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,46019 | 1,46019 | 1,28497 | 0,73740 | 1,92745 | €192,15 | €384,31 | €46,12 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.566,03 | €4.698,09 | €0,00 | €73,16 |
| 1H Fast V3 Nohigh Range Only V1 | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €143,18 | €429,53 | €51,54 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,48830 | 1,48830 | 1,48830 | 0,99964 | 1,75619 | €141,11 | €423,32 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.549,60 | €4.648,80 | €52,07 | €7,39 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.581,87 | €4.745,62 | €0,00 | €73,90 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €144,63 | €433,88 | €52,07 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,82358 | €144,27 | €432,81 | €51,94 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93367 | 0,93367 | 1,04571 | 1,24023 | 0,76561 | €135,90 | €407,70 | €48,92 | €-0,00 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00378 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €14,83 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 62813,56000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €29,89 |
| Main Side Regime Guard V1 | BEAT | SHORT | Confluenza trend | 240m | 3,0x | 1,03900 | 1,03900 | 1,03900 | 1,38014 | 0,78964 | €144,10 | €432,31 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend Side Regime Guard V1 | BEAT | SHORT | Combo Trend | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €209,53 | €419,07 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,06956 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €4,78 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00378 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €2,11 |
| Combo Trend Side Regime Guard V1 | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.546,22 | €4.638,65 | €0,00 | €72,24 |
| 1H Fast Nohigh Cap75 Short Only V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €195,91 | €587,73 | €50,39 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,06956 | 0,07069 | 0,09286 | 0,06873 | €1.499,62 | €4.498,86 | €50,39 | €22,27 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €140,23 | €420,70 | €46,71 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1161,28635 | 1181,69000 | 1161,28781 | 779,99733 | 1196,37370 | €15,08 | €45,24 | €0,00 | €0,79 |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €19,67 | €59,00 | €1,32 | €-0,04 |
| 1H Balanced V3 Long Only V1 | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63106,84706 | 84757,27849 | 61969,58760 | €1.068,36 | €3.205,08 | €0,00 | €49,91 |
| 1H Balanced V3 Long Only V1 | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,91879 | €133,24 | €399,72 | €47,97 | €0,00 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06956 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €0,05 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.730,40 | €3.460,80 | €0,00 | €67,89 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,04 | €402,07 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €0,04 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,86 | €25,72 | €0,46 | €-0,24 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.733,03 | €3.466,07 | €0,00 | €67,99 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,34 | €402,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €0,04 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,88 | €25,76 | €0,47 | €-0,24 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Strict3 V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-50,61 | -1,10 | STOP |
| Master Adaptive No Alt V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-52,93 | -1,10 | STOP |
| Master Adaptive Expanded V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-53,61 | -1,10 | STOP |
| Donchian 1H Gb20 120R V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-33,86 | -0,65 | STOP_GAP_STRESS |
| Benchmark Donchian breakout 1H | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-34,68 | -0,65 | STOP_GAP_STRESS |
| Combo Adaptive Quality7 V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-54,67 | -1,10 | STOP |
| Combo Adaptive Quality7 V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-32,04 | -0,65 | STOP_GAP_STRESS |
| Combo Adaptive Quality7 Regime V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-62,42 | -1,29 | STOP_GAP_STRESS |
| Combo Adaptive Quality7 Regime V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-54,11 | -1,10 | STOP |
| Combo Adaptive Quality7 Regime Partial 1R V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-54,80 | -1,10 | STOP |
| Combo Adaptive Quality7 Regime Partial 1R V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-63,21 | -1,29 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-56,53 | -1,18 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
