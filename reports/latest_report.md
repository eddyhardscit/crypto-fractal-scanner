<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-07 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +7 | BULLISH | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +8 | BULLISH | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +1 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+7**, spot = **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+8**, spot = **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+1**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+7**
- Confluenza: **POSITIVA FORTE**
- Bias Global: **Rialzista**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 81.347; conferma del doppio minimo sopra 65.402.
- Invalidazioni: Sotto 76.248 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+8**
- Confluenza: **POSITIVA FORTE**
- Bias Global: **Rialzista**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 110,82 / 133,01, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 88,08 / 97,45 / 62,19.

### DOGE

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.08028 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,25 $; upside verso EMA200 +5,36%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-07T05:33:13+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-07T05:05:32+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-07T05:05:32+00:00 | 2026-09-07T05:05:32+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-07T04:45:00+00:00 | 2026-09-07T04:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-09-07T04:00:00+00:00 | 2026-09-07T04:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-09-07T00:00:00+00:00 | 2026-09-07T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 Nohigh Range Only V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Strict3 V1 | TAO | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ZEC | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced Long No Rhv V1 | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | TAO | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | UNI | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,24 | 6,00 | 0,76 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,16 | 6,00 | 1,84 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,03 | 6,00 | 1,97 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 3,14 | 6,00 | 2,86 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 1,36 | 6,00 | 4,64 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 0,50 | 6,00 | 5,50 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | TAO | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | TAO | 60m | LONG | 7,75 | 4,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | TAO | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 + forza BTC 1H | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Mfe V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.816,71 | -1,83% | €8,15 | €3.000,00 | 0,27% | 5 | 60 | 41,67% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 60 | 3170 | PRIME INDICAZIONI | 100 (mancano 40) |

- Trade del Principale 4H chiusi: **60**; win rate **41,67%**; profit factor **0,88**.
- Expectancy: **€-3,05** per trade; P&L netto: **€-182,77**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.816,71 | €700,63 | €2.101,90 | €196,32 | €0,56 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.553,24 | €3.519,85 | €7.039,69 | €226,86 | €20,87 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.281,23 | €3.436,97 | €6.873,95 | €221,52 | €20,38 |
| TEST | Scanner Top 5 Long 1H | 7 | €11.240,58 | €1.431,12 | €2.862,24 | €226,81 | €281,77 |
| TEST | Main Side Regime Guard V1 | 6 | €11.183,96 | €628,60 | €1.885,81 | €223,51 | €8,47 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.090,92 | €716,47 | €2.149,41 | €167,48 | €21,35 |
| TEST | Combo Adaptive Long Only V1 | 9 | €11.038,39 | €2.472,42 | €4.944,83 | €223,40 | €484,84 |
| TEST | Combo Trend Side Regime Guard V1 | 8 | €11.036,19 | €1.496,97 | €2.993,94 | €170,70 | €235,98 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 5 | €10.744,26 | €2.373,95 | €7.121,85 | €213,34 | €29,44 |
| TEST | Scanner Top15 Long | 9 | €10.705,85 | €2.026,14 | €4.052,27 | €215,77 | €298,19 |
| TEST | Scanner Top20 Long | 9 | €10.705,85 | €2.026,14 | €4.052,27 | €215,77 | €298,19 |
| TEST | Combo Adaptive | 8 | €10.645,54 | €1.392,20 | €2.784,40 | €163,09 | €270,51 |
| TEST | Scanner Top10 Long | 8 | €10.623,32 | €2.420,01 | €4.840,03 | €212,47 | €407,56 |
| TEST | Rapida 1H V2 | 1 | €10.621,79 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.593,78 | €1.338,00 | €4.014,01 | €211,55 | €16,17 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.584,54 | €1.600,08 | €4.800,25 | €211,69 | €187,56 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 7 | €10.557,76 | €1.019,18 | €3.057,55 | €160,55 | €28,16 |
| TEST | Scanner Top 5 + forza BTC 1H | 7 | €10.531,31 | €1.170,86 | €2.341,73 | €211,83 | €266,57 |
| TEST | Combo Scanner | 7 | €10.528,06 | €1.538,63 | €3.077,25 | €211,77 | €246,47 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.516,54 | €1.589,80 | €4.769,41 | €210,33 | €186,36 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €10.315,19 | €1.981,44 | €3.962,88 | €205,93 | €39,63 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €10.309,15 | €1.980,28 | €3.960,56 | €205,81 | €39,60 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.293,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 8 | €10.245,85 | €1.002,78 | €3.008,34 | €204,92 | €20,86 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 6 | €10.238,74 | €1.851,73 | €5.555,19 | €156,02 | €52,05 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.210,22 | €344,54 | €1.033,63 | €101,76 | €9,25 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 9 | €10.198,96 | €1.023,36 | €2.046,73 | €203,96 | €5,38 |
| TEST | Sol Adaptive 4H | 1 | €10.189,10 | €613,63 | €1.227,27 | €50,96 | €-1,35 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 9 | €10.166,48 | €1.157,98 | €2.315,96 | €104,41 | €264,78 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €10.155,20 | €1.531,50 | €4.594,51 | €152,42 | €25,46 |
| TEST | Sol Donchian 4H | 1 | €10.155,15 | €574,98 | €1.149,96 | €50,72 | €11,27 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.093,26 | €985,68 | €1.971,36 | €50,34 | €25,68 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €10.087,82 | €1.310,73 | €3.932,19 | €196,71 | €196,11 |
| TEST | Doge Donchian 1H | 0 | €10.066,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.051,27 | €1.165,90 | €3.497,71 | €50,37 | €-19,54 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.050,43 | €1.946,29 | €3.892,58 | €151,20 | €-2,73 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.048,74 | €598,29 | €1.794,87 | €150,72 | €-2,10 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.042,02 | €667,02 | €1.334,05 | €50,29 | €-14,78 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.014,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.994,27 | €817,27 | €1.634,54 | €50,09 | €-21,94 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.989,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.987,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.987,29 | €1.158,48 | €3.475,45 | €50,05 | €-19,41 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.979,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.963,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 7 | €9.959,49 | €1.520,36 | €3.040,71 | €200,33 | €276,93 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.959,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 7 | €9.948,90 | €1.518,74 | €3.037,48 | €200,11 | €276,64 |
| TEST | Scanner Top5 Btc Guard V1 | 7 | €9.947,39 | €1.075,40 | €2.150,81 | €199,99 | €249,95 |
| TEST | Btc Ema 4H | 1 | €9.941,56 | €887,05 | €1.774,10 | €49,83 | €-23,81 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.937,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 6 | €9.930,97 | €1.021,43 | €3.064,29 | €198,11 | €26,30 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.917,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 7 | €9.910,42 | €1.512,86 | €3.025,73 | €199,34 | €275,57 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.903,76 | €1.275,14 | €3.825,42 | €192,09 | €24,63 |
| TEST | Btc Donchian 1H | 0 | €9.897,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.888,37 | €882,31 | €1.764,61 | €49,57 | €-23,68 |
| TEST | Eth Ema 4H | 1 | €9.887,35 | €690,19 | €1.380,39 | €49,44 | €1,44 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.882,55 | €1.233,36 | €3.700,08 | €197,60 | €2,42 |
| TEST | Master Adaptive Runner25 V1 | 9 | €9.873,79 | €1.584,35 | €3.168,69 | €199,15 | €319,70 |
| TEST | Scanner Top5 Btc Mfe V1 | 7 | €9.872,59 | €1.097,63 | €2.195,25 | €198,58 | €249,90 |
| TEST | Forza relativa 1H V2 | 6 | €9.839,17 | €842,73 | €1.685,47 | €99,49 | €-0,01 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.834,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 6 | €9.794,29 | €1.151,65 | €3.454,96 | €195,89 | €135,29 |
| TEST | Master Adaptive Gb20 V1 | 7 | €9.779,61 | €1.492,84 | €2.985,67 | €196,71 | €271,93 |
| TEST | Eth Adaptive 1H | 0 | €9.771,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.765,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 4 | €9.756,32 | €1.108,11 | €3.324,34 | €194,32 | €35,11 |
| TEST | Eth Bollinger 1H | 0 | €9.731,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.719,02 | €1.004,71 | €3.014,12 | €145,58 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.716,07 | €1.125,12 | €3.375,35 | €48,61 | €-2,74 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 7 | €9.716,06 | €1.050,39 | €2.100,79 | €195,34 | €244,13 |
| TEST | Eth Donchian 1H | 0 | €9.711,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.650,59 | €1.438,51 | €2.877,02 | €190,29 | €136,22 |
| TEST | Global Confluence puro 1H | 0 | €9.647,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.630,67 | €2.419,44 | €7.258,32 | €194,73 | €231,29 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €9.600,71 | €727,34 | €2.182,02 | €97,60 | €44,95 |
| TEST | Bilanciata 1H V1 | 9 | €9.590,69 | €1.147,60 | €3.442,79 | €146,55 | €256,77 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.587,02 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 7 | €9.584,46 | €1.548,47 | €3.096,94 | €191,21 | €46,43 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €9.572,18 | €727,29 | €2.181,88 | €97,41 | €44,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.561,05 | €1.053,15 | €3.159,44 | €191,07 | €8,54 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.476,95 | €979,65 | €2.938,95 | €141,95 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.463,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 7 | €9.412,71 | €1.528,53 | €3.057,07 | €146,56 | €236,86 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.397,98 | €981,82 | €1.963,65 | €144,18 | €210,85 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.371,11 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.353,07 | €1.707,75 | €3.415,51 | €186,48 | €35,32 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 7 | €9.311,76 | €1.160,62 | €2.321,24 | €185,91 | €16,31 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.286,88 | €1.162,48 | €2.324,96 | €151,54 | €241,74 |
| TEST | Combo Trend | 6 | €9.278,35 | €2.003,10 | €4.006,21 | €95,46 | €202,09 |
| TEST | Bilanciata 1H V2 | 5 | €9.262,32 | €1.119,75 | €3.359,24 | €138,17 | €26,93 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 7 | €9.236,63 | €1.499,98 | €2.999,97 | €143,82 | €232,43 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.108,85 | €2.288,34 | €6.865,03 | €184,18 | €218,76 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €9.096,93 | €1.570,62 | €3.141,23 | €136,01 | €19,67 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.073,03 | €1.427,94 | €2.855,87 | €181,48 | €0,15 |
| TEST | Master Adaptive Strict3 V1 | 6 | €9.023,57 | €1.120,46 | €2.240,91 | €180,47 | €19,29 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €9.015,82 | €1.081,14 | €3.243,43 | €134,32 | €44,93 |
| TEST | Forza relativa 1H V1 | 7 | €8.840,11 | €1.785,85 | €3.571,70 | €135,52 | €237,21 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €8.781,38 | €2.035,43 | €4.070,86 | €175,01 | €34,22 |
| TEST | Combo Mean Reversion | 1 | €8.636,37 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.194,49 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.816,71 | €-182,77 | 60 | 60 | 41,67% | 0,88 | €-3,05 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.553,24 | €1.536,83 | 139 | 139 | 45,32% | 1,50 | €11,06 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.281,23 | €1.265,21 | 107 | 107 | 43,93% | 1,59 | €11,82 | 6,75% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.240,58 | €960,56 | 174 | 174 | 47,70% | 1,31 | €5,52 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.183,96 | €1.177,18 | 51 | 51 | 60,78% | 2,53 | €23,08 | 3,82% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.090,92 | €1.070,99 | 192 | 192 | 50,00% | 1,27 | €5,58 | 7,95% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €11.038,39 | €556,50 | 161 | 161 | 48,45% | 1,19 | €3,46 | 7,78% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.036,19 | €802,25 | 152 | 152 | 51,32% | 1,27 | €5,28 | 10,10% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.744,26 | €719,09 | 124 | 124 | 49,19% | 1,28 | €5,80 | 4,50% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.705,85 | €409,97 | 194 | 194 | 47,94% | 1,14 | €2,11 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.705,85 | €409,97 | 194 | 194 | 47,94% | 1,14 | €2,11 | 10,31% |
| TEST | Combo Adaptive | Combo Adaptive | €10.645,54 | €376,88 | 204 | 204 | 46,57% | 1,11 | €1,85 | 8,17% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.623,32 | €218,67 | 176 | 176 | 48,30% | 1,08 | €1,24 | 10,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.621,79 | €622,95 | 74 | 65 | 50,00% | 1,36 | €8,42 | 3,89% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.593,78 | €579,84 | 270 | 270 | 44,44% | 1,13 | €2,15 | 9,28% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.584,54 | €399,98 | 213 | 213 | 49,30% | 1,11 | €1,88 | 9,50% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.557,76 | €531,56 | 132 | 132 | 49,24% | 1,25 | €4,03 | 5,24% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.531,31 | €266,19 | 155 | 155 | 45,16% | 1,09 | €1,72 | 11,27% |
| TEST | Combo Scanner | Combo Scanner | €10.528,06 | €283,55 | 186 | 186 | 44,09% | 1,08 | €1,52 | 11,38% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.516,54 | €333,16 | 257 | 257 | 44,36% | 1,07 | €1,30 | 9,48% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.315,19 | €278,05 | 150 | 150 | 44,00% | 1,09 | €1,85 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.309,15 | €272,04 | 154 | 154 | 44,16% | 1,09 | €1,77 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.293,89 | €293,89 | 19 | 19 | 57,89% | 1,95 | €15,47 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.245,85 | €226,81 | 231 | 231 | 43,29% | 1,05 | €0,98 | 10,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.238,74 | €189,83 | 76 | 76 | 44,74% | 1,10 | €2,50 | 6,05% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.210,22 | €201,95 | 18 | 18 | 38,89% | 1,40 | €11,22 | 3,39% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Ampia 4H | Confluenza trend | €10.198,96 | €194,83 | 55 | 55 | 34,55% | 1,15 | €3,54 | 4,45% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.189,10 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.166,48 | €-96,66 | 159 | 159 | 44,03% | 0,97 | €-0,61 | 11,68% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.155,20 | €132,30 | 51 | 51 | 43,14% | 1,10 | €2,59 | 6,49% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.155,15 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,61% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.093,26 | €68,27 | 3 | 3 | 66,67% | 2,25 | €22,76 | 0,91% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €10.087,82 | €-105,92 | 231 | 231 | 42,86% | 0,98 | €-0,46 | 12,52% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.066,52 | €66,52 | 17 | 17 | 58,82% | 1,16 | €3,91 | 3,08% |
| TEST | Sol Ema 1H | Trend following EMA | €10.051,27 | €73,41 | 23 | 23 | 43,48% | 1,11 | €3,19 | 3,33% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.050,43 | €55,48 | 177 | 177 | 44,63% | 1,02 | €0,31 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.048,74 | €51,91 | 267 | 267 | 39,70% | 1,01 | €0,19 | 6,56% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Ema 4H | Trend following EMA | €10.042,02 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.014,08 | €14,08 | 30 | 30 | 43,33% | 1,10 | €0,47 | 0,33% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,82 | €2,82 | 30 | 30 | 43,33% | 1,10 | €0,09 | 0,07% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.994,27 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Doge Ema 1H | Trend following EMA | €9.989,46 | €-10,54 | 26 | 26 | 57,69% | 0,98 | €-0,41 | 2,77% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.987,54 | €-12,46 | 18 | 18 | 33,33% | 0,30 | €-0,69 | 0,15% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.987,29 | €9,29 | 24 | 24 | 45,83% | 1,01 | €0,39 | 4,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.979,42 | €-20,58 | 15 | 15 | 60,00% | 0,94 | €-1,37 | 1,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.963,04 | €-36,96 | 18 | 18 | 33,33% | 0,63 | €-2,05 | 0,71% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.959,49 | €-316,68 | 103 | 103 | 33,01% | 0,88 | €-3,07 | 8,39% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.959,32 | €-40,68 | 55 | 55 | 49,09% | 0,97 | €-0,74 | 4,27% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.948,90 | €-326,97 | 98 | 98 | 35,71% | 0,87 | €-3,34 | 7,98% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.947,39 | €-301,77 | 143 | 143 | 39,16% | 0,90 | €-2,11 | 7,34% |
| TEST | Btc Ema 4H | Trend following EMA | €9.941,56 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.937,70 | €-62,30 | 18 | 18 | 33,33% | 0,30 | €-3,46 | 0,76% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.930,97 | €-93,49 | 151 | 151 | 44,37% | 0,97 | €-0,62 | 6,64% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.917,05 | €-82,95 | 30 | 30 | 43,33% | 0,52 | €-2,77 | 0,84% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.910,42 | €-364,39 | 100 | 100 | 35,00% | 0,87 | €-3,64 | 7,80% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.903,76 | €-118,51 | 154 | 154 | 47,40% | 0,97 | €-0,77 | 8,44% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.897,46 | €-102,54 | 12 | 12 | 41,67% | 0,70 | €-8,55 | 1,91% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.888,37 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,35 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.882,55 | €-117,93 | 171 | 171 | 45,03% | 0,96 | €-0,69 | 7,10% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.873,79 | €-444,69 | 84 | 84 | 32,14% | 0,82 | €-5,29 | 8,44% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.872,59 | €-375,95 | 147 | 147 | 44,22% | 0,86 | €-2,56 | 12,28% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.839,17 | €-159,53 | 138 | 131 | 40,58% | 0,95 | €-1,16 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.834,05 | €-165,95 | 55 | 55 | 45,45% | 0,88 | €-3,02 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.794,29 | €-338,86 | 122 | 122 | 45,08% | 0,85 | €-2,78 | 9,26% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.779,61 | €-491,56 | 134 | 134 | 44,78% | 0,83 | €-3,67 | 9,02% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.771,60 | €-228,40 | 19 | 19 | 42,11% | 0,63 | €-12,02 | 3,14% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.765,13 | €-234,87 | 17 | 17 | 41,18% | 0,62 | €-13,82 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.756,32 | €-276,80 | 135 | 135 | 40,74% | 0,91 | €-2,05 | 7,99% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.731,13 | €-268,87 | 10 | 10 | 40,00% | 0,38 | €-26,89 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.719,02 | €-279,18 | 199 | 199 | 40,20% | 0,93 | €-1,40 | 10,60% |
| TEST | Eth Ema 1H | Trend following EMA | €9.716,07 | €-279,00 | 27 | 27 | 40,74% | 0,67 | €-10,33 | 4,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.716,06 | €-527,30 | 160 | 160 | 40,00% | 0,85 | €-3,30 | 8,78% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.711,11 | €-288,89 | 18 | 18 | 33,33% | 0,56 | €-16,05 | 3,74% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.650,59 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.647,46 | €-352,54 | 21 | 21 | 33,33% | 0,46 | €-16,79 | 3,93% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.630,67 | €-596,48 | 201 | 201 | 40,80% | 0,85 | €-2,97 | 12,68% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.600,71 | €-442,93 | 186 | 186 | 41,40% | 0,91 | €-2,38 | 15,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.590,69 | €-663,77 | 173 | 173 | 39,88% | 0,79 | €-3,84 | 15,68% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.587,02 | €-411,80 | 84 | 84 | 46,43% | 0,80 | €-4,90 | 6,28% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.584,46 | €-461,55 | 90 | 90 | 26,67% | 0,81 | €-5,13 | 11,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.572,18 | €-470,51 | 145 | 145 | 42,76% | 0,88 | €-3,24 | 15,94% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.561,05 | €-445,48 | 225 | 225 | 42,22% | 0,91 | €-1,98 | 10,92% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.476,95 | €-521,29 | 162 | 162 | 38,27% | 0,84 | €-3,22 | 10,60% |
| TEST | Btc Ema 1H | Trend following EMA | €9.463,59 | €-536,41 | 20 | 20 | 20,00% | 0,33 | €-26,82 | 5,46% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.412,71 | €-822,18 | 142 | 142 | 36,62% | 0,70 | €-5,79 | 14,10% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.397,98 | €-811,71 | 158 | 158 | 39,24% | 0,71 | €-5,14 | 12,31% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.371,11 | €-628,22 | 86 | 86 | 34,88% | 0,73 | €-7,30 | 7,96% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.353,07 | €-679,95 | 97 | 97 | 35,05% | 0,77 | €-7,01 | 10,13% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.311,76 | €-703,63 | 105 | 105 | 38,10% | 0,76 | €-6,70 | 11,79% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.286,88 | €-953,49 | 220 | 220 | 40,91% | 0,76 | €-4,33 | 15,45% |
| TEST | Combo Trend | Combo Trend | €9.278,35 | €-921,05 | 191 | 191 | 39,79% | 0,78 | €-4,82 | 14,08% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.262,32 | €-761,93 | 159 | 145 | 42,14% | 0,78 | €-4,79 | 11,82% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.236,63 | €-993,87 | 122 | 122 | 36,07% | 0,60 | €-8,15 | 14,10% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.108,85 | €-1.105,99 | 155 | 155 | 40,65% | 0,64 | €-7,14 | 12,43% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.096,93 | €-920,75 | 52 | 52 | 26,92% | 0,44 | €-17,71 | 12,23% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.073,03 | €-925,85 | 129 | 129 | 37,98% | 0,72 | €-7,18 | 13,91% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.023,57 | €-994,35 | 78 | 78 | 29,49% | 0,67 | €-12,75 | 13,60% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.015,82 | €-1.027,16 | 195 | 195 | 38,46% | 0,78 | €-5,27 | 17,41% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.840,11 | €-1.394,62 | 149 | 149 | 33,56% | 0,60 | €-9,36 | 19,11% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.781,38 | €-1.250,32 | 107 | 107 | 36,45% | 0,56 | €-11,69 | 16,19% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.636,37 | €-1.362,34 | 60 | 60 | 33,33% | 0,44 | €-22,71 | 16,00% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.194,49 | €-1.805,51 | 110 | 110 | 38,18% | 0,51 | €-16,41 | 19,95% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 7,00700 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,56 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,17410 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €238,74 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €-0,00 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,41290 | 1,40809 | 1,39256 | 0,94900 | 1,45359 | €9,02 | €27,05 | €0,39 | €-0,09 |
| Bilanciata 1H V1 | DASH | LONG | Confluenza trend | 60m | 3,0x | 70,61412 | 70,79000 | 64,59923 | 47,42915 | 82,64391 | €24,96 | €74,87 | €6,38 | €0,19 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,40748 | 2,42700 | 2,29716 | 1,61703 | 2,62812 | €10,93 | €32,80 | €1,50 | €0,27 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2503,97069 | 2501,94000 | 2467,91352 | 1681,83365 | 2576,08505 | €14,30 | €42,91 | €0,62 | €-0,03 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1186,35722 | 1208,44000 | 1129,86589 | 796,83660 | 1299,33988 | €321,10 | €963,30 | €45,87 | €17,93 |
| Bilanciata 1H V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 273,49469 | 273,44000 | 262,68503 | 183,69727 | 295,11399 | €366,94 | €1.100,83 | €43,51 | €-0,22 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 273,44000 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €135,27 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1207,83152 | 1208,44000 | 1150,42638 | 811,26017 | 1322,64180 | €22,21 | €66,63 | €3,17 | €0,03 |
| 1H Balanced Long No Rhv V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,42749 | 2,42700 | 2,32276 | 1,63046 | 2,63693 | €20,90 | €62,71 | €2,71 | €-0,01 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,17410 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €17,15 |
| Bilanciata 1H V2 | DASH | LONG | Confluenza trend V2 | 60m | 3,0x | 69,34387 | 70,79000 | 63,21411 | 46,57596 | 81,60338 | €160,09 | €480,27 | €42,45 | €10,02 |
| Bilanciata 1H V2 | TAO | LONG | Confluenza trend V2 | 60m | 3,0x | 273,49469 | 273,44000 | 262,68503 | 183,69727 | 295,11399 | €390,62 | €1.171,85 | €46,32 | €-0,23 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,17410 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €244,80 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,00700 | 6,87560 | 4,79666 | 7,67309 | €9,58 | €28,74 | €1,07 | €-0,54 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2511,57221 | 2501,94000 | 2475,40557 | 1686,93934 | 2583,90549 | €1.126,95 | €3.380,86 | €48,68 | €-12,97 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,17410 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €20,98 |
| 1H Fast Score 6 75 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 80028,10242 | 79715,87000 | 79131,78767 | 53752,20879 | 81372,57454 | €18,39 | €55,17 | €0,62 | €-0,22 |
| 1H Fast Score 6 75 V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €127,25 | €381,75 | €45,81 | €0,00 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €433,10 | €1.299,29 | €48,12 | €24,18 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,17410 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €20,43 |
| 1H Fast Score 6 75 No Trend Up V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €126,82 | €380,47 | €45,66 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 80317,26024 | 79715,87000 | 79417,70693 | 53946,42646 | 81666,59021 | €24,01 | €72,04 | €0,81 | €-0,54 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €431,80 | €1.295,41 | €47,98 | €24,11 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €455,89 | €1.367,67 | €50,65 | €25,46 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,42700 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €21,35 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,25201 | 0,25201 | 0,22400 | 0,16927 | 0,29402 | €141,43 | €424,29 | €47,15 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €-0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €138,86 | €416,57 | €49,99 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1191,60827 | 1208,44000 | 1147,31771 | 800,36356 | 1258,04412 | €432,44 | €1.297,33 | €48,22 | €18,33 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DASH | LONG | Momentum / breakout | 60m | 3,0x | 69,61392 | 70,79000 | 66,26910 | 46,75735 | 74,63116 | €331,14 | €993,42 | €47,73 | €16,78 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €15,14 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1190,40803 | 1208,44000 | 1149,56911 | 799,55740 | 1251,66642 | €22,62 | €67,87 | €2,33 | €1,03 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| 1H Fast Tp2 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,18396 | 0,17410 | 0,17269 | 0,12356 | 0,20650 | €13,04 | €39,13 | €2,40 | €-2,10 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €186,38 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €-0,00 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1208,68169 | 1208,44000 | 1168,71362 | 811,83120 | 1268,63379 | €37,35 | €112,04 | €3,70 | €-0,02 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €125,88 | €377,63 | €45,32 | €0,00 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €397,18 | €1.191,54 | €44,13 | €22,18 |
| 1H Fast V3 Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €435,59 | €1.306,77 | €44,88 | €22,75 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1190,40803 | 1208,44000 | 1149,56911 | 799,55740 | 1251,66642 | €53,23 | €159,68 | €5,48 | €2,42 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €175,14 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,18396 | 0,17410 | 0,17269 | 0,12356 | 0,20086 | €19,13 | €57,39 | €3,52 | €-3,07 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €430,45 | €1.291,35 | €47,83 | €24,04 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €134,15 | €402,44 | €48,29 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80317,26024 | 79715,87000 | 79417,70693 | 53946,42646 | 81666,59021 | €16,11 | €48,34 | €0,54 | €-0,36 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €31,85 | €95,56 | €3,54 | €1,78 |
| 1H Fast V3 Long Nohigh Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €476,47 | €1.429,42 | €49,09 | €24,88 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €8,54 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €-0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,18396 | 0,17410 | 0,17269 | 0,12356 | 0,20086 | €24,76 | €74,28 | €4,55 | €-3,98 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €444,95 | €1.334,85 | €49,44 | €24,85 |
| 1H Fast V3 No Esports Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 273,49469 | 273,44000 | 265,08718 | 183,69727 | 286,10595 | €17,17 | €51,50 | €1,58 | €-0,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €187,58 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1208,68169 | 1208,44000 | 1168,71362 | 811,83120 | 1268,63379 | €37,59 | €112,76 | €3,73 | €-0,02 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79715,87000 | 79131,78767 | 53752,20879 | 81372,57454 | €77,79 | €233,37 | €2,61 | €-0,91 |
| 1H Fast V3 No Esports Stress Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41948 | 2,42700 | 2,33363 | 1,62509 | 2,54827 | €509,84 | €1.529,52 | €54,28 | €4,75 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €464,69 | €1.394,07 | €51,63 | €25,95 |
| 1H Fast V3 No Esports Stress Guard V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 273,49469 | 273,44000 | 265,08718 | 183,69727 | 286,10595 | €582,59 | €1.747,77 | €53,73 | €-0,35 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1207,83152 | 1208,44000 | 1163,18307 | 811,26017 | 1274,80418 | €447,04 | €1.341,11 | €49,58 | €0,68 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80317,26024 | 79715,87000 | 79417,70693 | 53946,42646 | 81666,59021 | €10,38 | €31,14 | €0,35 | €-0,23 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €463,10 | €1.389,30 | €47,71 | €24,18 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2501,94000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,11 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 86,35400 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €2,45 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 105,25300 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €0,39 |
| Ampia 4H | XRP | LONG | Confluenza trend | 240m | 2,0x | 1,42001 | 1,40809 | 1,35851 | 0,71711 | 1,59222 | €12,52 | €25,04 | €1,08 | €-0,21 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 7,00700 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €1,63 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €219,20 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €-0,00 |
| Forza relativa 1H V1 | DASH | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 82,82933 | €20,72 | €41,45 | €3,66 | €0,86 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €474,73 | €949,47 | €43,71 | €20,19 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 87,57151 | 86,35400 | 85,96029 | 44,22361 | 91,11620 | €88,01 | €176,03 | €3,24 | €-2,45 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,69291 | €13,42 | €26,84 | €0,90 | €-0,59 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TAO | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 297,27592 | €14,32 | €28,64 | €1,13 | €-0,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2486,95729 | 2501,94000 | 2447,16598 | 1255,91343 | 2586,43558 | €1.753,97 | €3.507,94 | €56,13 | €21,13 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 105,92618 | 105,25300 | 104,23136 | 53,49272 | 110,16323 | €20,43 | €40,86 | €0,65 | €-0,26 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2486,95729 | 2501,94000 | 2447,16598 | 1255,91343 | 2586,43558 | €1.712,67 | €3.425,35 | €54,81 | €20,64 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 105,92618 | 105,25300 | 104,23136 | 53,49272 | 110,16323 | €19,95 | €39,90 | €0,64 | €-0,25 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,17410 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €212,27 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 7,07742 | 7,00700 | 6,75804 | 3,57409 | 7,78005 | €71,53 | €143,05 | €6,46 | €-1,42 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €281,93 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1215,33302 | 1208,44000 | 1158,91544 | 613,74317 | 1328,16817 | €13,38 | €26,76 | €1,24 | €-0,15 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2501,94029 | 2501,94000 | 2465,91235 | 1263,47985 | 2573,99617 | €260,98 | €521,97 | €7,52 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €142,88 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €262,32 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 7,14143 | 7,00700 | 6,87560 | 3,60642 | 7,67309 | €15,10 | €30,20 | €1,12 | €-0,57 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 105,69714 | 105,25300 | 104,13756 | 53,37705 | 108,81629 | €21,20 | €42,41 | €0,63 | €-0,18 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €83,79 | €167,58 | €7,98 | €3,12 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 2,42749 | 2,42700 | 2,32276 | 1,22588 | 2,63693 | €18,65 | €37,30 | €1,61 | €-0,01 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €5,58 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €18,65 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €264,76 |
| Scanner Top15 Long | DASH | LONG | Scanner Top15 Long | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 81,60338 | €295,33 | €590,66 | €52,21 | €12,32 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1322,64180 | €84,93 | €169,86 | €8,07 | €0,09 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,12843 | 7,00700 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €-3,00 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 105,69714 | 105,25300 | 104,13756 | 53,37705 | 108,81629 | €23,28 | €46,56 | €0,69 | €-0,20 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €5,58 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €18,65 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €264,76 |
| Scanner Top20 Long | DASH | LONG | Scanner Top20 Long | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 81,60338 | €295,33 | €590,66 | €52,21 | €12,32 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1322,64180 | €84,93 | €169,86 | €8,07 | €0,09 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,12843 | 7,00700 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €-3,00 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 105,69714 | 105,25300 | 104,13756 | 53,37705 | 108,81629 | €23,28 | €46,56 | €0,69 | €-0,20 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €264,05 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €-0,45 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €69,93 | €139,86 | €6,44 | €2,97 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €247,53 |
| Scanner Top5 Btc Mfe V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €-0,42 |
| Scanner Top5 Btc Mfe V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €65,55 | €131,11 | €6,04 | €2,79 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €249,24 |
| Scanner Top5 Btc Guard V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 82,82933 | €15,44 | €30,88 | €2,73 | €0,64 |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1334,12283 | €61,52 | €123,04 | €5,85 | €0,06 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €466,33 | €932,66 | €42,93 | €19,83 |
| Scanner Top5 Btc Btc Le3 V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,88377 | 70,79000 | 63,76753 | 34,78631 | 80,13952 | €14,76 | €29,52 | €2,19 | €0,82 |
| Scanner Top5 Btc Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,69291 | €17,38 | €34,75 | €1,16 | €-0,77 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1190,40803 | 1208,44000 | 1137,90085 | 601,15606 | 1305,92385 | €473,42 | €946,84 | €41,76 | €14,34 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €188,32 | €376,64 | €45,20 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €-0,45 |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €473,04 | €946,07 | €43,55 | €20,11 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €243,44 |
| Scanner Top5 Btc Guard Mfe V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 82,82933 | €15,08 | €30,17 | €2,67 | €0,63 |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1334,12283 | €60,09 | €120,18 | €5,71 | €0,06 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €32,15 | €64,31 | €2,96 | €1,37 |
| Scanner Top5 Btc Guard Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,14143 | 7,00700 | 6,87560 | 3,60642 | 7,72626 | €12,97 | €25,94 | €0,97 | €-0,49 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1190,40803 | 1208,44000 | 1137,90085 | 601,15606 | 1305,92385 | €509,37 | €1.018,74 | €44,94 | €15,43 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €186,87 | €373,73 | €44,85 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1334,12283 | €469,07 | €938,15 | €44,59 | €0,47 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 70,93418 | 70,79000 | 66,36043 | 35,82176 | 80,99644 | €23,68 | €47,37 | €3,05 | €-0,10 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 297,27592 | €562,94 | €1.125,89 | €44,50 | €-0,23 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €16,92 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €-0,53 |
| Scanner Top5 Btc Runner25 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,70466 | €545,89 | €1.091,78 | €50,26 | €23,21 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €16,93 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €-0,53 |
| Scanner Top5 Btc Tp3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,70466 | €546,21 | €1.092,42 | €50,29 | €23,23 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,17410 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €203,69 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 105,92618 | 105,25300 | 104,23136 | 53,49272 | 109,65478 | €19,15 | €38,30 | €0,61 | €-0,24 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 7,07742 | 7,00700 | 6,75804 | 3,57409 | 7,78005 | €68,62 | €137,24 | €6,19 | €-1,37 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €260,44 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €-14,54 |
| Combo Scanner | NEAR | LONG | Combo Scanner | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €21,23 | €42,45 | €1,95 | €0,90 |
| Combo Scanner | DASH | LONG | Combo Scanner | 60m | 2,0x | 70,93418 | 70,79000 | 66,36043 | 35,82176 | 80,99644 | €81,07 | €162,13 | €10,45 | €-0,33 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €8,61 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €261,39 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,64496 | €12,79 | €25,58 | €0,86 | €-0,57 |
| Combo Adaptive | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,41248 | 2,42700 | 2,30417 | 1,21830 | 2,62911 | €89,29 | €178,57 | €8,02 | €1,07 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €11,43 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €228,31 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1191,60827 | 1208,44000 | 1134,66326 | 601,76218 | 1305,49830 | €70,67 | €141,33 | €6,75 | €2,00 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €136,22 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €214,34 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €271,36 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1322,64180 | €82,44 | €164,87 | €7,84 | €0,08 |
| Combo Adaptive Long Only V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 70,98419 | 70,79000 | 65,99178 | 35,84702 | 80,96902 | €44,54 | €89,07 | €6,26 | €-0,24 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2503,97069 | 2501,94000 | 2467,91352 | 1264,50520 | 2576,08505 | €14,64 | €29,28 | €0,42 | €-0,02 |
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,64496 | €15,48 | €30,96 | €1,04 | €-0,68 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18396 | 0,17410 | 0,16947 | 0,09290 | 0,21294 | €25,44 | €50,88 | €4,01 | €-2,73 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €233,80 |
| Combo Adaptive Runner25 V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,34306 | 105,25300 | 103,60820 | 53,19825 | 110,54767 | €199,12 | €398,24 | €6,56 | €-0,34 |
| Combo Adaptive Runner25 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1380,04694 | €24,90 | €49,79 | €2,37 | €0,03 |
| Combo Adaptive Runner25 V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,41748 | 2,42700 | 2,30912 | 1,22083 | 2,74258 | €524,28 | €1.048,57 | €47,00 | €4,13 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,88472 | €17,00 | €34,01 | €1,14 | €-0,75 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €229,42 |
| Combo Adaptive Tp3 V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,34306 | 105,25300 | 103,60820 | 53,19825 | 110,54767 | €195,44 | €390,89 | €6,44 | €-0,33 |
| Combo Adaptive Tp3 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1380,04694 | €24,43 | €48,86 | €2,32 | €0,02 |
| Combo Adaptive Tp3 V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,41748 | 2,42700 | 2,30912 | 1,22083 | 2,74258 | €514,48 | €1.028,95 | €46,12 | €4,05 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,88472 | €16,69 | €33,37 | €1,12 | €-0,74 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80800,35684 | 79715,87000 | 78530,68128 | 40804,18020 | 86474,54655 | €887,05 | €1.774,10 | €49,83 | €-23,81 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80800,35684 | 79715,87000 | 78530,68128 | 40804,18020 | 87155,44873 | €882,31 | €1.764,61 | €49,57 | €-23,68 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80768,04316 | 79715,87000 | 82830,55933 | 120748,22452 | 77055,51340 | €985,68 | €1.971,36 | €50,34 | €25,68 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80800,35684 | 79715,87000 | 78324,34707 | 40804,18020 | 86990,38168 | €817,27 | €1.634,54 | €50,09 | €-21,94 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 105,84416 | 105,25300 | 104,32001 | 71,09200 | 108,89248 | €1.165,90 | €3.497,71 | €50,37 | €-19,54 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 106,43228 | 105,25300 | 102,42020 | 53,74830 | 116,46248 | €667,02 | €1.334,05 | €50,29 | €-14,78 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,23184 | 105,25300 | 99,63427 | 52,63708 | 117,10505 | €574,98 | €1.149,96 | €50,72 | €11,27 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 105,84416 | 105,25300 | 104,32001 | 71,09200 | 108,89248 | €1.158,48 | €3.475,45 | €50,05 | €-19,41 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 105,36907 | 105,25300 | 100,99415 | 53,21138 | 116,30636 | €613,63 | €1.227,27 | €50,96 | €-1,35 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2503,97069 | 2501,94000 | 2467,91352 | 1681,83365 | 2576,08505 | €1.125,12 | €3.375,35 | €48,61 | €-2,74 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2499,33977 | 2501,94000 | 2409,82951 | 1262,16658 | 2723,11538 | €690,19 | €1.380,39 | €49,44 | €1,44 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €236,36 |
| Master Adaptive V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,47 | €44,95 | €5,39 | €0,00 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €609,04 | €1.218,08 | €49,01 | €38,94 |
| Master Adaptive V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €16,19 | €32,38 | €1,48 | €0,26 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 70,79000 | 64,01551 | 34,80651 | 78,74032 | €315,67 | €631,34 | €44,96 | €17,09 |
| Master Adaptive No Alt V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €489,56 | €979,12 | €46,62 | €18,23 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2501,94029 | 2501,94000 | 2465,91235 | 1263,47985 | 2573,99617 | €109,70 | €219,41 | €3,16 | €-0,00 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 70,79000 | 64,01551 | 34,80651 | 78,74032 | €31,26 | €62,52 | €4,45 | €1,69 |
| Master Adaptive Strict3 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €472,80 | €945,61 | €45,03 | €17,60 |
| Master Adaptive Strict3 V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 295,11400 | €12,91 | €25,82 | €1,02 | €-0,01 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €233,24 |
| Master Adaptive Gb20 V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,18 | €44,35 | €5,32 | €0,00 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €601,00 | €1.202,00 | €48,36 | €38,43 |
| Master Adaptive Gb20 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €15,88 | €31,75 | €1,45 | €0,26 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €230,37 |
| Master Adaptive Runner25 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,42700 | 2,12346 | 1,12183 | 2,51541 | €477,69 | €955,38 | €42,14 | €88,40 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1142,68849 | 1208,44000 | 1099,52971 | 577,05769 | 1272,16483 | €18,41 | €36,81 | €1,39 | €2,12 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 86,72534 | 86,35400 | 85,46149 | 43,79630 | 90,51689 | €188,43 | €376,86 | €5,49 | €-1,61 |
| Master Adaptive Runner25 V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 69,97399 | 70,79000 | 65,60770 | 35,33687 | 83,07286 | €18,41 | €36,82 | €2,30 | €0,43 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €25,74 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €239,37 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,92618 | 105,25300 | 104,40084 | 53,49272 | 108,97686 | €23,43 | €46,87 | €0,67 | €-0,30 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,64496 | €12,54 | €25,08 | €0,84 | €-0,55 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €14,29 | €28,58 | €1,36 | €0,53 |
| Combo Adaptive Side Regime Guard V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 295,11399 | €40,44 | €80,89 | €3,20 | €-0,02 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €237,53 |
| Master Adaptive Gb20 Be V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,58 | €45,17 | €5,42 | €0,00 |
| Master Adaptive Gb20 Be V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €612,05 | €1.224,11 | €49,25 | €39,13 |
| Master Adaptive Gb20 Be V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €16,27 | €32,54 | €1,49 | €0,26 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €237,28 |
| Master Adaptive Gb20 Partial V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,56 | €45,12 | €5,41 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €611,40 | €1.222,81 | €49,20 | €39,09 |
| Master Adaptive Gb20 Partial V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €16,25 | €32,50 | €1,49 | €0,26 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €11,13 |
| Master Adaptive Gb20 Loss Cap V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,37648 | 2,42700 | 2,29443 | 1,20012 | 2,59527 | €691,76 | €1.383,52 | €47,77 | €29,41 |
| Master Adaptive Gb20 Loss Cap V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1168,87373 | 1208,44000 | 1128,11099 | 590,28123 | 1277,57438 | €86,94 | €173,88 | €6,06 | €5,89 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €460,83 | €1.382,48 | €51,20 | €25,73 |
| 1H Fast V3 Nohigh Range Only V1 | DASH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 69,61392 | 70,79000 | 66,26910 | 46,75735 | 74,63116 | €16,79 | €50,37 | €2,42 | €0,85 |
| 1H Fast V3 Nohigh Range Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €487,86 | €1.463,59 | €50,26 | €25,48 |
| 1H Fast V3 Nohigh Range Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 273,49469 | 273,44000 | 265,08718 | 183,69727 | 286,10595 | €10,13 | €30,38 | €0,93 | €-0,01 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79715,87000 | 79131,78767 | 53752,20879 | 81372,57454 | €20,36 | €61,08 | €0,68 | €-0,24 |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €38,56 | €115,68 | €4,28 | €2,15 |
| 1H Fast V3 Nohigh Regime Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €502,64 | €1.507,91 | €51,79 | €26,25 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | DASH | LONG | Confluenza trend | 240m | 3,0x | 69,69394 | 70,79000 | 61,33066 | 46,81109 | 86,42048 | €155,22 | €465,66 | €55,88 | €7,32 |
| Main Side Regime Guard V1 | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,38548 | 2,42700 | 2,20016 | 1,60225 | 2,75612 | €21,97 | €65,90 | €5,12 | €1,15 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Main Dynamic Asset Selector V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1190,40803 | 1208,44000 | 1090,98250 | 799,55740 | 1389,25911 | €203,57 | €610,70 | €51,01 | €9,25 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,17410 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €248,32 |
| Combo Trend Side Regime Guard V1 | XRP | LONG | Combo Trend | 60m | 2,0x | 1,41420 | 1,40809 | 1,39158 | 0,71417 | 1,46398 | €20,70 | €41,41 | €0,66 | €-0,18 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,00700 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €-13,04 |
| Combo Trend Side Regime Guard V1 | SOL | LONG | Combo Trend | 60m | 2,0x | 105,69714 | 105,25300 | 103,96427 | 53,37705 | 109,50944 | €16,60 | €33,19 | €0,54 | €-0,14 |
| Combo Trend Side Regime Guard V1 | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,41248 | 2,42700 | 2,29213 | 1,21830 | 2,67725 | €84,20 | €168,39 | €8,40 | €1,01 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,17410 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €231,54 |
| 1H Balanced V3 Long Only V1 | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,00700 | 6,87560 | 4,79666 | 7,67309 | €9,06 | €27,18 | €1,01 | €-0,51 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2511,57221 | 2501,94000 | 2475,40557 | 1686,93934 | 2583,90549 | €1.065,89 | €3.197,67 | €46,05 | €-12,26 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,55 | €385,10 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €179,76 | €359,53 | €43,14 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,85 | €385,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €180,04 | €360,08 | €43,21 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports Stress Guard V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-57,04 | -1,05 | STOP |
| 1H Fast V3 No Esports Long Only V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,97756 | €-0,75 | -1,05 | STOP |
| 1H Fast V3 Long Only V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,97756 | €-0,71 | -1,05 | STOP |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-5,39 | -1,05 | STOP |
| 1H Fast V3 Cap75 V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-1,05 | -1,05 | STOP |
| 1H Fast Score 6 75 V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-51,01 | -1,05 | STOP |
| 1H Fast Score 6 75 No Trend Up V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-50,86 | -1,05 | STOP |
| Scanner Top5 Btc Guard Btc Le3 V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17683 | €-46,90 | -1,02 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17833 | €-46,50 | -1,02 | STOP |
| Scanner Top5 Btc Btc Le3 V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17683 | €-43,81 | -1,02 | STOP |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17833 | €-46,80 | -1,02 | STOP |
| 1H Fast V3 Nohigh V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17944 | €-5,75 | -1,03 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
<!-- PAPER_TRADING_END -->

</details>
<!-- COMPACT_SECTION_END:decision -->

<!-- COMPACT_SECTION_START:module_accuracy -->
<details>
<summary><strong>🧪 Accuratezza moduli e raccolta dati</strong></summary>

<!-- MODULE_ACCURACY_START -->
# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [module_accuracy_report.md](module_accuracy_report.md)

Questo report salva ogni giorno i segnali dei moduli e controlla ogni giorno quali orizzonti sono maturati.

La calibrazione ora controlla questi orizzonti:

- **1g / 2g / 3g** = feedback rapidissimo
- **5g / 7g / 10g** = feedback settimanale
- **14g / 21g** = feedback swing
- **30g / 45g / 60g** = feedback più serio

Moduli controllati:

- Global Confluence = benchmark dell'aggregato finale
- **Famiglia statistica Scanner + Market Regime = modulo calibrabile reale**
- Scanner grezzo = diagnostico, già incluso nella famiglia statistica
- Market Regime grezzo = diagnostico, già incluso nella famiglia statistica
- Struttura tecnica
- Classic technical confirmation
- Microstruttura exchange, OI/funding/taker flow/order book
- Frattale SOL/BTC, solo per SOL

Regola anti-doppio-conteggio: **Scanner e Market Regime continuano a essere misurati separatamente solo per diagnosi, ma non devono ricevere due modifiche di peso autonome**. La calibrazione dei pesi deve agire sulla Famiglia statistica.

Nota: i controlli vengono aggiornati **ogni giorno**, ma i pesi del Global non devono cambiare automaticamente sotto 30 controlli. Prima si osserva, poi si calibra.

Segnali totali salvati: **177**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-07 | BTC | 79.828,11 | +7 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-07 | DOGE | 0.09027 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-07 | SOL | 105,55 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-06 | BTC | 79.879,48 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-06 | DOGE | 0.09088 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-06 | SOL | 105,95 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-05 | BTC | 79.660,00 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-05 | DOGE | 0.08560 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-05 | SOL | 102,27 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-04 | BTC | 80.963,98 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-04 | DOGE | 0.08695 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-04 | SOL | 103,67 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59 | 58 | 57 | 56 | 54 | 52 | 49 | 45 | 38 | 31 | 16 | 1 |
| SOL | 59 | 58 | 57 | 56 | 54 | 52 | 49 | 45 | 38 | 31 | 16 | 1 |
| DOGE | 59 | 58 | 57 | 56 | 54 | 52 | 49 | 45 | 38 | 31 | 16 | 1 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 60g | 2026-09-08 | domani |
| SOL | 2026-07-10 | 60g | 2026-09-08 | domani |
| DOGE | 2026-07-10 | 60g | 2026-09-08 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 55 | 50,91% | +0,45% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 2g | 54 | 53,70% | +0,79% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 3g | 53 | 49,06% | +1,02% | +0,89% | PRIMA CALIBRAZIONE |
| BTC | 5g | 51 | 47,06% | +1,99% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 7g | 49 | 55,10% | +2,73% | +2,51% | PRIMA CALIBRAZIONE |
| BTC | 10g | 46 | 60,87% | +3,80% | +3,60% | PRIMA CALIBRAZIONE |
| BTC | 14g | 42 | 66,67% | +6,07% | +5,98% | PRIMA CALIBRAZIONE |
| BTC | 21g | 36 | 61,11% | +10,21% | +10,03% | PRIMA CALIBRAZIONE |
| BTC | 30g | 29 | 89,66% | +13,35% | +11,87% | FEEDBACK RAPIDO |
| BTC | 45g | 14 | 85,71% | +22,52% | +16,15% | FEEDBACK RAPIDO |
| BTC | 60g | 1 | 100,00% | +26,24% | +26,24% | FEEDBACK RAPIDO |
| SOL | 1g | 51 | 54,90% | +0,70% | +0,58% | PRIMA CALIBRAZIONE |
| SOL | 2g | 50 | 54,00% | +1,42% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 3g | 49 | 59,18% | +2,19% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | 47 | 61,70% | +3,60% | +3,49% | PRIMA CALIBRAZIONE |
| SOL | 7g | 45 | 66,67% | +5,02% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 10g | 42 | 71,43% | +7,21% | +7,39% | PRIMA CALIBRAZIONE |
| SOL | 14g | 38 | 78,95% | +10,88% | +11,83% | PRIMA CALIBRAZIONE |
| SOL | 21g | 31 | 74,19% | +16,13% | +14,98% | PRIMA CALIBRAZIONE |
| SOL | 30g | 24 | 58,33% | +18,43% | +10,19% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 1 | 100,00% | +35,29% | +35,29% | FEEDBACK RAPIDO |
| DOGE | 1g | 54 | 44,44% | +0,53% | +0,13% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 53 | 47,17% | +1,07% | +0,41% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 52 | 42,31% | +1,48% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 50 | 52,00% | +2,26% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 48 | 62,50% | +2,63% | +3,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 46 | 56,52% | +2,84% | +3,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 43 | 69,77% | +5,33% | +7,49% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 36 | 77,78% | +8,88% | +7,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 29 | 72,41% | +11,27% | +3,57% | FEEDBACK RAPIDO |
| DOGE | 45g | 16 | 0,00% | +19,77% | -19,77% | FEEDBACK RAPIDO |
| DOGE | 60g | 1 | 0,00% | +23,91% | -23,91% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 55 | 50,91% | +0,45% | +0,43% | -0,00% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 58 | 53,45% | +0,42% | +0,42% | -0,02% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 58 | 53,45% | +0,42% | +0,42% | -0,02% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 53 | 39,62% | +0,55% | +0,16% | +0,09% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 54 | 53,70% | +0,79% | +0,70% | +0,20% | +1,49% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 57 | 56,14% | +0,88% | +0,88% | +0,30% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 57 | 56,14% | +0,88% | +0,88% | +0,30% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 52 | 46,15% | +1,07% | +0,27% | +0,48% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,27% | +1,27% | +0,55% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 53 | 49,06% | +1,02% | +0,89% | -0,94% | +2,69% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 56 | 57,14% | +1,31% | +1,31% | -0,93% | +2,91% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 56 | 57,14% | +1,31% | +1,31% | -0,93% | +2,91% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 51 | 39,22% | +1,64% | -0,02% | -0,74% | +3,20% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,72% | +0,72% | -0,94% | +2,21% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 51 | 47,06% | +1,99% | +1,74% | -1,55% | +4,21% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 54 | 53,70% | +2,24% | +2,24% | -1,52% | +4,52% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 54 | 53,70% | +2,24% | +2,24% | -1,52% | +4,52% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 49 | 44,90% | +2,58% | -0,88% | -1,32% | +4,90% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 22 | 50,00% | +4,06% | -1,22% | -1,06% | +6,26% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 49 | 55,10% | +2,73% | +2,51% | -1,76% | +5,40% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 52 | 61,54% | +3,05% | +3,05% | -1,74% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 52 | 61,54% | +3,05% | +3,05% | -1,74% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 47 | 42,55% | +3,61% | -1,82% | -1,52% | +6,19% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 20 | 45,00% | +5,94% | -3,27% | -1,13% | +8,88% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 46 | 60,87% | +3,80% | +3,60% | -1,99% | +6,54% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 49 | 65,31% | +3,96% | +3,96% | -1,99% | +6,79% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 49 | 65,31% | +3,96% | +3,96% | -1,99% | +6,79% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 44 | 45,45% | +4,55% | -1,50% | -1,74% | +7,43% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 17 | 52,94% | +7,60% | -4,82% | -1,13% | +10,52% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 42 | 66,67% | +6,07% | +5,98% | -1,97% | +9,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 45 | 66,67% | +6,11% | +6,11% | -1,99% | +9,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 45 | 66,67% | +6,11% | +6,11% | -1,99% | +9,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 40 | 62,50% | +7,03% | +0,98% | -1,68% | +10,43% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 13 | 53,85% | +9,92% | -5,20% | -0,30% | +13,51% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +1,23% | +1,23% | -1,55% | +6,04% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 36 | 61,11% | +10,21% | +10,03% | -2,64% | +13,81% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 38 | 68,42% | +9,62% | +9,62% | -2,69% | +13,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 38 | 68,42% | +9,62% | +9,62% | -2,69% | +13,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,91% | +10,91% | -2,48% | +14,50% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 33 | 33,33% | +10,84% | -1,59% | -2,43% | +14,49% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 8 | 0,00% | +19,34% | -19,34% | -0,83% | +22,19% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 29 | 89,66% | +13,35% | +11,87% | -2,94% | +17,21% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 31 | 83,87% | +13,01% | +13,01% | -2,98% | +16,95% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 31 | 83,87% | +13,01% | +13,01% | -2,98% | +16,95% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 27 | 85,19% | +14,24% | +14,24% | -2,76% | +18,42% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 26 | 38,46% | +13,07% | -4,29% | -2,70% | +17,36% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 14 | 85,71% | +22,52% | +16,15% | -3,23% | +26,32% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 16 | 100,00% | +22,58% | +22,58% | -3,28% | +26,36% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 16 | 100,00% | +22,58% | +22,58% | -3,28% | +26,36% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 12 | 100,00% | +23,08% | +23,08% | -2,88% | +26,74% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 13 | 30,77% | +22,83% | -9,06% | -2,94% | +26,83% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 1 | 0,00% | +26,24% | -26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 54 | 44,44% | +0,53% | +0,13% | -0,13% | +1,54% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 57 | 57,89% | +0,41% | +0,44% | -0,27% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 57 | 57,89% | +0,41% | +0,44% | -0,27% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 51 | 52,94% | +0,32% | +0,49% | -0,38% | +1,25% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 32 | 40,62% | +0,24% | -0,51% | -0,42% | +0,95% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 53 | 47,17% | +1,07% | +0,41% | +0,26% | +2,39% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 56 | 53,57% | +0,85% | +0,70% | +0,05% | +2,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 56 | 53,57% | +0,85% | +0,70% | +0,05% | +2,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 50 | 58,00% | +0,46% | +0,83% | -0,32% | +1,66% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 52 | 42,31% | +1,48% | +0,87% | -1,59% | +4,38% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 55 | 52,73% | +1,25% | +1,12% | -1,76% | +3,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 55 | 52,73% | +1,25% | +1,12% | -1,76% | +3,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 49 | 46,94% | +0,38% | +0,73% | -2,05% | +2,99% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 50 | 52,00% | +2,26% | +2,13% | -2,53% | +6,52% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 53 | 50,94% | +2,08% | +2,12% | -2,63% | +6,21% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 53 | 50,94% | +2,08% | +2,12% | -2,63% | +6,21% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 47 | 57,45% | +0,95% | +0,68% | -3,11% | +5,09% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 48 | 62,50% | +2,63% | +3,74% | -3,04% | +8,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +2,66% | +3,06% | -3,12% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +2,66% | +3,06% | -3,12% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 45 | 57,78% | +1,19% | +1,22% | -3,72% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 46 | 56,52% | +2,84% | +3,96% | -3,54% | +9,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 48 | 56,25% | +2,73% | +3,70% | -3,60% | +9,34% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 48 | 56,25% | +2,73% | +3,70% | -3,60% | +9,34% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 42 | 61,90% | +0,61% | +1,52% | -4,31% | +6,82% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,00% | -0,43% | -2,75% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 43 | 69,77% | +5,33% | +7,49% | -3,60% | +13,80% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 45 | 73,33% | +5,00% | +7,08% | -3,64% | +13,23% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 45 | 73,33% | +5,00% | +7,08% | -3,64% | +13,23% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 38 | 65,79% | +1,62% | +1,16% | -4,34% | +8,83% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 30 | 50,00% | +3,47% | -3,89% | -4,22% | +11,44% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 36 | 77,78% | +8,88% | +7,78% | -3,89% | +18,78% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 38 | 86,84% | +8,94% | +12,06% | -3,92% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 38 | 86,84% | +8,94% | +12,06% | -3,92% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 36 | 88,89% | +9,51% | +12,66% | -3,93% | +19,72% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 33 | 63,64% | +7,02% | -3,84% | -4,34% | +15,23% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 25 | 60,00% | +5,34% | -5,34% | -4,25% | +13,53% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 29 | 72,41% | +11,27% | +3,57% | -4,67% | +23,21% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 31 | 87,10% | +11,94% | +10,47% | -4,66% | +24,30% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 31 | 87,10% | +11,94% | +10,47% | -4,66% | +24,30% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 29 | 93,10% | +10,84% | +13,12% | -4,72% | +23,41% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 21 | 52,38% | +8,46% | -8,46% | -5,03% | +18,17% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +31,57% | +10,47% | -1,27% | +41,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 15 | 0,00% | +20,08% | -20,08% | -6,17% | +37,48% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +30,79% | +30,79% | -1,52% | +44,86% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 51 | 54,90% | +0,70% | +0,58% | -0,01% | +1,62% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 53 | 56,60% | +0,40% | +0,39% | -0,24% | +1,29% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 56 | 55,36% | +0,44% | +0,31% | -0,21% | +1,32% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 55 | 50,91% | +0,40% | +0,37% | -0,28% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 39 | 51,28% | +0,61% | +0,57% | -0,20% | +1,55% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 50 | 54,00% | +1,42% | +1,28% | +0,47% | +2,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 52 | 50,00% | +1,03% | +0,57% | +0,07% | +1,87% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 55 | 49,09% | +0,99% | +0,52% | +0,06% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 54 | 46,30% | +0,93% | +0,36% | +0,03% | +2,03% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 38 | 55,26% | +1,08% | +1,05% | +0,15% | +2,08% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 49 | 59,18% | +2,19% | +2,01% | -1,31% | +4,41% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 51 | 50,98% | +1,67% | +1,09% | -1,62% | +3,89% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 54 | 50,00% | +1,59% | +1,01% | -1,60% | +3,86% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 53 | 50,94% | +1,45% | +0,21% | -1,67% | +3,59% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 37 | 56,76% | +1,42% | +1,27% | -1,63% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 47 | 61,70% | +3,60% | +3,49% | -2,00% | +6,92% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 49 | 55,10% | +2,89% | +1,78% | -2,32% | +6,20% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 52 | 53,85% | +2,76% | +1,63% | -2,30% | +6,07% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 51 | 49,02% | +2,77% | -0,36% | -2,46% | +5,96% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 35 | 60,00% | +2,07% | +1,91% | -2,42% | +5,15% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 45 | 66,67% | +5,02% | +5,14% | -2,34% | +8,92% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 47 | 61,70% | +4,18% | +2,83% | -2,68% | +8,13% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 50 | 62,00% | +3,92% | +2,67% | -2,68% | +7,88% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 49 | 42,86% | +3,88% | -1,24% | -2,86% | +7,81% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 33 | 54,55% | +2,25% | +2,30% | -2,89% | +6,15% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 42 | 71,43% | +7,21% | +7,39% | -2,38% | +11,59% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 44 | 65,91% | +6,27% | +5,23% | -2,81% | +10,42% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 47 | 63,83% | +5,85% | +4,91% | -2,85% | +10,01% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 46 | 50,00% | +5,23% | -2,08% | -3,06% | +9,57% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 30 | 63,33% | +2,44% | +2,56% | -3,06% | +7,12% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 38 | 78,95% | +10,88% | +11,83% | -2,52% | +16,52% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 40 | 80,00% | +10,23% | +9,21% | -2,90% | +15,14% | PRIMA CALIBRAZIONE |

## Come leggerlo

- **CALIBRABILE** = modulo reale sul quale, con dati maturi, si può valutare una modifica di peso.
- **DIAGNOSTICO** = resta misurato, ma è già incluso in una famiglia e il suo peso separato deve restare 0.
- **BENCHMARK** = risultato complessivo del Global; serve per confrontare l'aggregato, non è un peso interno.
- **Controlli** = segnali non neutrali già verificati su quell'orizzonte.
- **Accuratezza direzione** = quante volte un segnale positivo ha avuto return positivo o un segnale negativo ha avuto return negativo.
- **Return medio** = rendimento reale medio dell'asset su quell'orizzonte.
- **Return corretto direzione** = return visto dal lato del modulo: se il modulo era ribassista, un calo conta positivo.
- **Drawdown medio** = peggior discesa media durante l'orizzonte.
- **Max gain medio** = massimo rialzo medio durante l'orizzonte.

Regole operative:

- Sotto **30 controlli**: solo osservazione, nessuna modifica ai pesi.
- Da **30 controlli**: possibile calibrazione leggera.
- Da **60 controlli**: lettura più utile.
- Da **100+ controlli**: possibile revisione più seria dei pesi.

Questo report non cambia ancora automaticamente i pesi del Global Confluence. Produce però i metadati `calibratable` e `calibration_role`, così il report di calibrazione può escludere Scanner e Market dalle proposte di peso separate.

Nota tecnica: le colonne data sono forzate come testo, quindi non deve più apparire l'errore `Invalid value 'YYYY-MM-DD' for dtype 'float64'`.
<!-- MODULE_ACCURACY_END -->

</details>
<!-- COMPACT_SECTION_END:module_accuracy -->

<!-- COMPACT_SECTION_START:global_weight_calibration -->
<details>
<summary><strong>⚖️ Calibrazione pesi Global Confluence</strong></summary>

<!-- GLOBAL_WEIGHT_CALIBRATION_START -->
# Calibrazione pesi Global Confluence

Generato: 2026-09-07 05:32 UTC

Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)

Questo blocco controlla se, col tempo, i moduli reali del Global Confluence meritano più peso, meno peso o peso invariato.

Correzione anti-doppio-conteggio: **la Famiglia statistica Scanner + Market Regime è il modulo calibrabile**. Scanner grezzo e Market Regime grezzo restano visibili solo come diagnostica e non ricevono proposte di peso separate.

Regola principale:

- sotto **30 controlli**: osservazione, nessuna modifica pesi
- da **30 controlli**: prima calibrazione leggera
- da **60 controlli**: lettura utile
- da **100+ controlli**: possibile proposta prudente di modifica pesi

Il file continua a produrre solo raccomandazioni: **non modifica automaticamente** `global_confluence_report.py`.

## Sintesi per asset

| Asset | Segnali salvati | Stato | Controlli max | Righe 30+ | Righe 60+ | Righe 100+ | Miglior modulo calibrabile | Orizzonte | Accuratezza | Return corretto direzione | Lettura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59 | PRIMA CALIBRAZIONE | 58 | 17 | 0 | 0 | Famiglia statistica | 1g | 53,45% | +0,42% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 59 | PRIMA CALIBRAZIONE | 55 | 23 | 0 | 0 | Tecnico | 1g | 50,91% | +0,37% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 59 | PRIMA CALIBRAZIONE | 57 | 25 | 0 | 0 | Famiglia statistica | 1g | 57,89% | +0,44% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 58 | 53,45% | +0,42% | +0,42% | -0,02% | +0,95% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 53 | 39,62% | +0,16% | +0,55% | +0,09% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 57 | 56,14% | +0,88% | +0,88% | +0,30% | +1,57% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,27% | +1,27% | +0,55% | +1,72% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 52 | 46,15% | +0,27% | +1,07% | +0,48% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 56 | 57,14% | +1,31% | +1,31% | -0,93% | +2,91% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +0,72% | +0,72% | -0,94% | +2,21% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 51 | 39,22% | -0,02% | +1,64% | -0,74% | +3,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 22 | 50,00% | -1,22% | +4,06% | -1,06% | +6,26% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 54 | 53,70% | +2,24% | +2,24% | -1,52% | +4,52% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 49 | 44,90% | -0,88% | +2,58% | -1,32% | +4,90% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 20 | 45,00% | -3,27% | +5,94% | -1,13% | +8,88% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 52 | 61,54% | +3,05% | +3,05% | -1,74% | +5,70% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 47 | 42,55% | -1,82% | +3,61% | -1,52% | +6,19% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 17 | 52,94% | -4,82% | +7,60% | -1,13% | +10,52% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 49 | 65,31% | +3,96% | +3,96% | -1,99% | +6,79% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 44 | 45,45% | -1,50% | +4,55% | -1,74% | +7,43% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 13 | 53,85% | -5,20% | +9,92% | -0,30% | +13,51% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 45 | 66,67% | +6,11% | +6,11% | -1,99% | +9,45% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +1,23% | +1,23% | -1,55% | +6,04% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 40 | 62,50% | +0,98% | +7,03% | -1,68% | +10,43% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 8 | 0,00% | -19,34% | +19,34% | -0,83% | +22,19% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 38 | 68,42% | +9,62% | +9,62% | -2,69% | +13,22% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 33 | 33,33% | -1,59% | +10,84% | -2,43% | +14,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 31 | 83,87% | +13,01% | +13,01% | -2,98% | +16,95% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 26 | 38,46% | -4,29% | +13,07% | -2,70% | +17,36% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 16 | 100,00% | +22,58% | +22,58% | -3,28% | +26,36% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 13 | 30,77% | -9,06% | +22,83% | -2,94% | +26,83% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 1 | 0,00% | -26,24% | +26,24% | -2,32% | +30,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 32 | 40,62% | -0,51% | +0,24% | -0,42% | +0,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 57 | 57,89% | +0,44% | +0,41% | -0,27% | +1,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 51 | 52,94% | +0,49% | +0,32% | -0,38% | +1,25% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 56 | 53,57% | +0,70% | +0,85% | +0,05% | +2,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 50 | 58,00% | +0,83% | +0,46% | -0,32% | +1,66% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 55 | 52,73% | +1,12% | +1,25% | -1,76% | +3,97% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 49 | 46,94% | +0,73% | +0,38% | -2,05% | +2,99% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 53 | 50,94% | +2,12% | +2,08% | -2,63% | +6,21% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 47 | 57,45% | +0,68% | +0,95% | -3,11% | +5,09% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 51 | 56,86% | +3,06% | +2,66% | -3,12% | +7,96% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 45 | 57,78% | +1,22% | +1,19% | -3,72% | +6,40% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 48 | 56,25% | +3,70% | +2,73% | -3,60% | +9,34% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 7 | 57,14% | -0,43% | +0,00% | -2,75% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 42 | 61,90% | +1,52% | +0,61% | -4,31% | +6,82% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 30 | 50,00% | -3,89% | +3,47% | -4,22% | +11,44% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 45 | 73,33% | +7,08% | +5,00% | -3,64% | +13,23% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 7 | 57,14% | +2,04% | +7,65% | -2,99% | +15,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 38 | 65,79% | +1,16% | +1,62% | -4,34% | +8,83% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 25 | 60,00% | -5,34% | +5,34% | -4,25% | +13,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 38 | 86,84% | +12,06% | +8,94% | -3,92% | +18,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 33 | 63,64% | -3,84% | +7,02% | -4,34% | +15,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 21 | 52,38% | -8,46% | +8,46% | -5,03% | +18,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 31 | 87,10% | +10,47% | +11,94% | -4,66% | +24,30% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 3 | 66,67% | +10,47% | +31,57% | -1,27% | +41,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 15 | 0,00% | -20,08% | +20,08% | -6,17% | +37,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 16 | 0,00% | -19,77% | +19,77% | -6,29% | +37,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +30,79% | +30,79% | -1,52% | +44,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 16 | 0,00% | -19,77% | +19,77% | -6,29% | +37,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 1 | 0,00% | -23,91% | +23,91% | -6,69% | +37,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 1 | 0,00% | -23,91% | +23,91% | -6,69% | +37,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 1 | 0,00% | -23,91% | +23,91% | -6,69% | +37,24% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 39 | 51,28% | +0,57% | +0,61% | -0,20% | +1,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 53 | 56,60% | +0,39% | +0,40% | -0,24% | +1,29% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 55 | 50,91% | +0,37% | +0,40% | -0,28% | +1,24% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 38 | 55,26% | +1,05% | +1,08% | +0,15% | +2,08% | PESO OK | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 52 | 50,00% | +0,57% | +1,03% | +0,07% | +1,87% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 54 | 46,30% | +0,36% | +0,93% | +0,03% | +2,03% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 37 | 56,76% | +1,27% | +1,42% | -1,63% | +3,57% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 51 | 50,98% | +1,09% | +1,67% | -1,62% | +3,89% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 53 | 50,94% | +0,21% | +1,45% | -1,67% | +3,59% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 35 | 60,00% | +1,91% | +2,07% | -2,42% | +5,15% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 49 | 55,10% | +1,78% | +2,89% | -2,32% | +6,20% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 51 | 49,02% | -0,36% | +2,77% | -2,46% | +5,96% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 33 | 54,55% | +2,30% | +2,25% | -2,89% | +6,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 47 | 61,70% | +2,83% | +4,18% | -2,68% | +8,13% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 49 | 42,86% | -1,24% | +3,88% | -2,86% | +7,81% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 30 | 63,33% | +2,56% | +2,44% | -3,06% | +7,12% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 44 | 65,91% | +5,23% | +6,27% | -2,81% | +10,42% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 46 | 50,00% | -2,08% | +5,23% | -3,06% | +9,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 26 | 50,00% | +1,72% | +3,64% | -3,23% | +8,17% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 40 | 80,00% | +9,21% | +10,23% | -2,90% | +15,14% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 42 | 38,10% | -4,93% | +7,76% | -3,25% | +12,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 34 | 85,29% | +17,72% | +16,08% | -4,28% | +21,44% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 36 | 33,33% | -14,01% | +12,87% | -4,63% | +18,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 27 | 88,89% | +23,02% | +23,41% | -5,16% | +29,61% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 31 | 12,90% | -21,05% | +20,44% | -5,38% | +26,28% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 8 | 0,00% | -35,68% | +35,68% | -7,09% | +44,63% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 12 | 33,33% | -7,79% | +31,67% | -7,99% | +39,17% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 16 | 25,00% | -20,49% | +32,79% | -7,71% | +39,99% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 1 | 0,00% | -35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 55 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 58 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 171 | 55,56% | +0,87% |
| BTC | BREVE | Microstruttura exchange | 13 | 46,15% | +0,55% |
| BTC | BREVE | Tecnico | 156 | 41,67% | +0,14% |
| BTC | SETTIMANALE | Classic technical | 59 | 49,15% | -2,95% |
| BTC | SETTIMANALE | Famiglia statistica | 155 | 60,00% | +3,05% |
| BTC | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | +0,53% |
| BTC | SETTIMANALE | Tecnico | 140 | 44,29% | -1,39% |
| BTC | SWING | Classic technical | 21 | 33,33% | -10,59% |
| BTC | SWING | Famiglia statistica | 83 | 67,47% | +7,72% |
| BTC | SWING | Microstruttura exchange | 3 | 66,67% | +1,23% |
| BTC | SWING | Tecnico | 73 | 49,32% | -0,18% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 48 | 89,58% | +16,47% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 40 | 35,00% | -6,39% |
| DOGE | BREVE | Classic technical | 94 | 39,36% | -1,27% |
| DOGE | BREVE | Famiglia statistica | 168 | 54,76% | +0,75% |
| DOGE | BREVE | Microstruttura exchange | 25 | 52,00% | +2,46% |
| DOGE | BREVE | Tecnico | 150 | 52,67% | +0,68% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 152 | 54,61% | +2,93% |
| DOGE | SETTIMANALE | Microstruttura exchange | 23 | 47,83% | +0,43% |
| DOGE | SETTIMANALE | Tecnico | 134 | 58,96% | +1,12% |
| DOGE | SWING | Classic technical | 55 | 54,55% | -4,55% |
| DOGE | SWING | Famiglia statistica | 83 | 79,52% | +9,36% |
| DOGE | SWING | Microstruttura exchange | 11 | 63,64% | +0,95% |
| DOGE | SWING | Tecnico | 71 | 64,79% | -1,16% |
| DOGE | MEDIO | Classic technical | 37 | 29,73% | -13,59% |
| DOGE | MEDIO | Famiglia statistica | 48 | 56,25% | -0,33% |
| DOGE | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,55% |
| DOGE | MEDIO | Tecnico | 47 | 25,53% | -14,64% |
| SOL | BREVE | Classic technical | 114 | 54,39% | +0,96% |
| SOL | BREVE | Famiglia statistica | 156 | 52,56% | +0,68% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 162 | 49,38% | +0,31% |
| SOL | SETTIMANALE | Classic technical | 98 | 59,18% | +2,24% |
| SOL | SETTIMANALE | Famiglia statistica | 140 | 60,71% | +3,22% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 146 | 47,26% | -1,19% |
| SOL | SWING | Classic technical | 47 | 44,68% | -4,05% |
| SOL | SWING | Famiglia statistica | 74 | 82,43% | +13,12% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 5 | 60,00% | +13,52% |
| SOL | SWING | Tecnico | 78 | 35,90% | -9,12% |
| SOL | MEDIO | Classic technical | 29 | 6,90% | -29,06% |
| SOL | MEDIO | Famiglia statistica | 40 | 70,00% | +12,32% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 2 | 100,00% | +20,54% |
| SOL | MEDIO | Tecnico | 48 | 18,75% | -19,69% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 6 | in attesa di controlli maturati |
| SOL | MEDIO | 2 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 4 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

È iniziata la prima calibrazione, ma sono ammesse solo valutazioni leggere e manuali.
<!-- GLOBAL_WEIGHT_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:global_weight_calibration -->

<!-- COMPACT_SECTION_START:risk_calibration -->
<details>
<summary><strong>🛡️ Calibrazione rischio spot / leva</strong></summary>

<!-- RISK_CALIBRATION_START -->
# Calibrazione rischio spot / leva

Report completo: [risk_calibration_report.md](risk_calibration_report.md)

Questo blocco controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         59 |              31 |          28 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         59 |              31 |          28 | OSSERVAZIONE 30+ | 3,23%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         59 |              31 |          28 | OSSERVAZIONE 30+ | 6,45%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [global_confluence_report.md](global_confluence_report.md)

Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.

Moduli letti:

- Famiglia statistica Scanner + Market Regime, conteggiata una sola volta
- Scanner path / cono previsionale
- Struttura tecnica classica precedente
- Classic technical confirmation, filtro tecnico completo
- Frattale BTC 2022 vs SOL 2026, solo per SOL
- Fractal path tracker, solo per SOL
- RSI top-cycle, soprattutto per SOL
- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL
- Exchange microstructure: OI, funding, taker flow, order book e liquidazioni campionate
- Futures / liquidazioni precedente, mantenuto come diagnostica
- Cambiamento giornaliero

Nota statistica: **Scanner e Market Regime non vengono più sommati come due prove indipendenti**. Lo Scanner è il punteggio principale; il Market Regime può aggiungere al massimo 1 punto di conferma con almeno 10 match. La famiglia statistica è limitata a ±4.

Nota importante: **Lifecycle EMA200 viene letto e mostrato, ma vale sempre 0 punti nel Global Confluence**. Serve come contesto, non come conferma operativa.

Nota Classic technical: **pesa massimo ±1** perché è un filtro di conferma e in parte si sovrappone alla struttura tecnica già esistente.

Nota exchange: **candidato massimo ±1, peso iniziale 0** e più conferme indipendenti. Order book, funding o una singola liquidazione non bastano da soli.

## Sintesi operativa

| Asset | Punteggio | Confluenza | Bias | Affidabilità | Azione coerente | Conferme | Invalidazioni |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +7 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | Prima resistenza sopra 81.347; conferma del doppio minimo sopra 65.402. | Sotto 76.248 il quadro tecnico peggiora. |
| SOL | +8 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 110,82 / 133,01, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 88,08 / 97,45 / 62,19. |
| DOGE | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.08028 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +7 |
| SOL | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +8 |
| DOGE | -2 | 0 | -2 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +1 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+7**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**

BTC ha una confluenza positiva forte. Resta comunque necessario evitare leva eccessiva: la conferma deve arrivare da prezzo e resistenze, non solo dallo score.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 85,00%, return centrale 30g +18,09%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 56. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 7/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 4/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 81.347; conferma del doppio minimo sopra 65.402.

Invalidazioni: Sotto 76.248 il quadro tecnico peggiora.

### SOL

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+8**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**

SOL ha una confluenza molto interessante, ma resta più rischiosa di BTC. Le conferme tecniche e frattali devono comunque reggere prima di usare leva.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 65,00%, return centrale 30g +19,90%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 0,00%, return p50 -16,66%.
- Scanner path: **0** — Controlli disponibili 56. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 7/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +68,14%, aderenza live +71,92%, errore live +14,04%, gap corrente +10,76%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 53, ma percorso ancorato non aderente: gap +10,76%, errore live +14,04%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,25 $, upside EMA200 +5,36%, gap EMA50/EMA200 -5,72%, hit EMA200 12w +86,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow -0.25, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — SOL: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 110,82 / 133,01, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 88,08 / 97,45 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 30,00%, return centrale 30g -15,20%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 56. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 12/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 8/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow -0.25, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — DOGE: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.08028 il rischio ribassista aumenta.


## Come leggere il punteggio

- +7 o più: confluenza positiva forte.
- Da +3 a +6: confluenza moderatamente positiva.
- Da 0 a +2: confluenza parziale o mista.
- Da -1 a -3: confluenza debole o fragile.
- -4 o meno: confluenza negativa.

Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0.
Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero.

Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze resta nel report, ma pesa **0** nel Global perché EMA50/EMA200 e target EMA200 sono contesto, non conferme dirette di prezzo.

Nota Classic technical: il modulo è utile per capire se il setup è confermato davvero, ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente.

Nota exchange: il modulo salva OI, funding, taker flow, order book e liquidazioni campionate. Il candidato è limitato a ±1; il peso Global resta 0 finché il gate storico a 7 giorni non matura.
<!-- GLOBAL_CONFLUENCE_END -->

</details>
<!-- COMPACT_SECTION_END:global_confluence -->

<!-- COMPACT_SECTION_START:btc_macro_cycle -->
<details>
<summary><strong>🌀 Bitcoin Macro Cycle — Power Law e Spiral</strong></summary>

<!-- BTC_MACRO_CYCLE_START -->
# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 79.828 $ | prezzo corrente |
| Power Law centrale | 124.812 $ | deviazione -36,04% |
| Banda p10-p90 | 77.541 $ / 315.057 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 12,67% | posizione storica nel corridoio |
| Esponente β | 5,8049 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3165 cambiando finestra |
| Ultimo halving | 2024-04-19 | 871 giorni fa |
| Fase ciclo | 59,62% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-07 (4373 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0680) × giorni^5.8049
- Prezzo centrale oggi: **124.812 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 12,67%
- Scarto dal centro: **-36,04%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8049 | 91,93% |
| 2015 | 5,8872 | 91,48% |
| 2016 | 5,5713 | 87,73% |
| 2017 | 4,8434 | 82,91% |
| 2018 | 4,5707 | 78,42% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 80 | 27,50% | 53,06% | 20,63% |
| 180g | 80 | 41,25% | 60,12% | 47,43% |
| 365g | 80 | 57,50% | 72,70% | 78,86% |
| 730g | 80 | 58,75% | 72,61% | 109,35% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-01-23 | +1,33% | +1,54% | +19,04% | +66,39% |
| 2016-07-09 → 2020-05-11 | 2018-10-23 | -32,58% | -44,78% | -17,93% | +16,04% |
| 2020-05-11 → 2024-04-19 | 2022-09-16 | -2,55% | -12,18% | +23,28% | +34,37% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 16.502204813829845 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -2 | 0 | 5.376915981669561 | 0 |

## Tracker live Power Law

| Orizzonte | Controlli | Vittorie vs naive | Errore modello | Errore naive | Stato |
| --- | --- | --- | --- | --- | --- |
| 90g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 180g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 365g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |

Il modulo resta a peso 0 anche con un buon backtest. Prima si osserva la verifica live, poi si decide se usarlo soltanto per il rischio macro di lungo periodo. Le fotografie live della Power Law vengono salvate una sola volta per mese, così non si contano come indipendenti previsioni giornaliere quasi identiche.

## File prodotti

- `reports/btc_power_law_metrics.csv`
- `reports/btc_power_law_backtest.csv`
- `reports/btc_cycle_phase_metrics.csv`
- `reports/btc_macro_cycle_history.csv`
- `reports/btc_macro_cycle_tracker_metrics.csv`
<!-- BTC_MACRO_CYCLE_END -->

</details>
<!-- COMPACT_SECTION_END:btc_macro_cycle -->

<!-- COMPACT_SECTION_START:relative_strength_btc -->
<details>
<summary><strong>₿ Forza relativa SOL/BTC e DOGE/BTC</strong></summary>

<!-- RELATIVE_STRENGTH_BTC_START -->
# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00132230 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +16,50% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000113 | -2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +5,38% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+4)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +0,86%; 30g +16,50%; 90g +24,86%; 180g +7,77%
- **Daily:** RSI 62.68; MA50 0.00121049; MA200 0.00118189
- **Weekly:** MA30 0.00118778; RSI 58.00
- **Livelli:** supporto 0.00127500; resistenza 0.00134900; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +6,98%; 30g +5,38%; 90g -17,32%; 180g -16,37%
- **Daily:** RSI 56.25; MA50 0.00000110; MA200 0.00000127
- **Weekly:** MA30 0.00000126; RSI 40.98
- **Livelli:** supporto 0.00000112; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 207 | 52,17% | +1,95% | -1,06% |
| SOL | 30g | 204 | 47,06% | +4,50% | +0,44% |
| SOL | 90g | 199 | 52,76% | +9,91% | +3,03% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 32 | 59,38% | +0,23% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 32 | 56,25% | +0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 28 | 50,00% | +0,75% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 21 | 33,33% | -0,14% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 15 | 0,00% | -12,64% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 46 | 67,39% | -0,10% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 45 | 57,78% | +0,04% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 41 | 60,98% | +0,23% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 35 | 68,57% | +0,20% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 29 | 68,97% | +0,57% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
<!-- RELATIVE_STRENGTH_BTC_END -->

</details>
<!-- COMPACT_SECTION_END:relative_strength_btc -->

<!-- COMPACT_SECTION_START:btc_sol_fractal -->
<details>
<summary><strong>🧬 Frattale mirato BTC 2022 / SOL 2026</strong></summary>

<!-- BTC_SOL_FRACTAL_START -->

---

# Frattale mirato: BTC 2022 vs SOL 2026

Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)

Ultima candela SOL usata: **7 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 105,54 $ | 2026-09-07T05:30:22Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 105,61 $ | 2026-09-07T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | 0,07000 $ | +0,07% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=105.54000091552734
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-07T05:30:22Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=105.61000061035156
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-07T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-07T05:32:09Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=107.798227
ANCHOR_AGE_HOURS=0.029943951944444443
CURRENT_VS_ANCHOR_GAP_USD=0.06999969482421875
CURRENT_VS_ANCHOR_GAP_PCT=0.0663252740354281
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +68,14%
- **Somiglianza strutturale:** +68,14%
- **Aderenza prezzo live:** +71,92%
- **Errore medio live:** +14,04%
- **Gap prezzo corrente:** +10,76%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 93 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-22
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Fase negativa / rischio discesa.** Zona bassa **94,76 $** intorno al **21 settembre 2026**; zona alta **105,54 $** intorno al **7 settembre 2026**; fine step circa **94,76 $** entro il **21 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=14.040655698981599
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=10.761855474865921
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 7 settembre 2026 | 67 | +71,92% | +14,04% | +10,76% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 7 settembre 2026 | 94 | +76,52% | +11,74% | +10,76% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +71,92% | Errore medio live +14,04%. |
| Gap corrente | +10,76% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 110,82 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 133,01 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 88,08 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 544,32 $ |
| Massimo percorso base | 544,32 $ (21 aprile 2029) |

## Grafici

### Grafico frattale sovrapposto

Scala normalizzata base 100; valori non USD.

![Frattale BTC 2022 vs SOL 2026](btc_2022_vs_sol_2026_fractal_chart.png)

### Grafico proiezione condizionale

Serie e proiezioni ancorate all'input computazionale; riferimento pubblico separato e solo display.

![Proiezione SOL BTC 2022](btc_2022_vs_sol_2026_projection_chart.png)

### Grafico ciclo base

Scenario analogico in USD; non previsione live e non segnale di trading.

![Ciclo base SOL BTC 2025](btc_2022_vs_sol_2026_cycle_base_chart.png)

### Grafico struttura vs aderenza

![Tracking frattale BTC SOL](btc_2022_vs_sol_2026_tracking_chart.png)

## Livelli chiave

| Livello | Prezzo / soglia | Lettura |
| --- | --- | --- |
| Rientro gap | entro ±12% | Condizione necessaria per tornare operativo. |
| Prima conferma | 110,82 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 133,01 $ | Scenario più credibile. |
| Invalidazione soft | 88,08 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 14 settembre 2026 | -2,24% | 103,17 $ | 101,00 $ | 105,54 $ |
| 14 giorni | 21 settembre 2026 | -10,21% | 94,76 $ | 94,76 $ | 105,54 $ |
| 30 giorni | 7 ottobre 2026 | +13,66% | 119,96 $ | 88,08 $ | 123,63 $ |
| 60 giorni | 6 novembre 2026 | +14,07% | 120,39 $ | 88,08 $ | 133,01 $ |
| 90 giorni | 6 dicembre 2026 | +12,55% | 118,79 $ | 88,08 $ | 133,01 $ |
| 120 giorni | 5 gennaio 2027 | +23,66% | 130,51 $ | 88,08 $ | 133,01 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 7 settembre 2026 -> 21 settembre 2026 | -10,21% | 94,76 $ (21 settembre 2026) | 105,54 $ (7 settembre 2026) | 94,76 $ | Fase negativa / rischio discesa. |
| Step 2 - primo mese | 22 settembre 2026 -> 7 ottobre 2026 | +13,66% | 88,08 $ (23 settembre 2026) | 123,63 $ (6 ottobre 2026) | 119,96 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 8 ottobre 2026 -> 6 novembre 2026 | +14,07% | 118,42 $ (10 ottobre 2026) | 133,01 $ (28 ottobre 2026) | 120,39 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 7 novembre 2026 -> 6 dicembre 2026 | +12,55% | 116,73 $ (4 dicembre 2026) | 128,86 $ (18 novembre 2026) | 118,79 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali. Motivo del verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

<!-- BTC_SOL_FRACTAL_END -->

</details>
<!-- COMPACT_SECTION_END:btc_sol_fractal -->

<!-- COMPACT_SECTION_START:rsi_top_cycle -->
<details>
<summary><strong>📈 RSI top-cycle SOL</strong></summary>

<!-- RSI_TOP_CYCLE_START -->

---

# RSI top-cycle warning - SOL

Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)

Filtro prudente: usa almeno 3 picchi RSI, separa vicinanza matematica e rischio reale, e non proietta la top-line oltre 12 mesi.

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 105,54 $ |  |
| Weekly RSI | 59,90 / linea grezza 52,24 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 47,52 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 544,32 $ | Avanzamento +19,39% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 47,5, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
- Confluenza prezzo + RSI: **BASSO**

Questo non è un segnale di entrata. RSI bassi o trendline non affidabili restano neutrali e non penalizzano il Global Confluence.

## Grafici RSI

![SOL weekly RSI top-line](rsi_top_cycle_SOL_weekly.png)

![SOL monthly RSI top-line](rsi_top_cycle_SOL_monthly.png)

<!-- RSI_TOP_CYCLE_END -->

</details>
<!-- COMPACT_SECTION_END:rsi_top_cycle -->

<!-- COMPACT_SECTION_START:sol_onchain -->
<details>
<summary><strong>⛓️ Metriche on-chain SOL</strong></summary>

<!-- SOL_ONCHAIN_METRICS_START -->

---

# SOL on-chain metrics

Report separato completo: **[sol_onchain_metrics_report.md](sol_onchain_metrics_report.md)**

| Voce | Valore |
| --- | --- |
| Score on-chain | 3 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Prezzo SOL | 105,54 $ |
| TVL Solana | 5,92 mld $ |
| TVL 7g | +0,23% |
| DEX volume 24h | 1,96 mld $ |
| Fees 24h | 10,48 mln $ |
| Stablecoin su Solana | 16,67 mld $ |
| Stake ratio | 69,36% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE**

Questo blocco non sostituisce il frattale SOL/BTC: serve come filtro per capire se il movimento è sostenuto anche da attività on-chain.

<!-- SOL_ONCHAIN_METRICS_END -->

</details>
<!-- COMPACT_SECTION_END:sol_onchain -->

<!-- COMPACT_SECTION_START:major_alt_lifecycle -->
<details>
<summary><strong>🔄 Lifecycle squeeze / EMA200 SOL</strong></summary>

<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->

---

# Major alt lifecycle squeeze - SOL

Report separato completo: **[major_alt_lifecycle_squeeze_report.md](major_alt_lifecycle_squeeze_report.md)**

| Voce                      | Valore                       |
|:--------------------------|:-----------------------------|
| Lifecycle squeeze score | 2 |
| Bias | CONTESTO DA OSSERVARE |
| Azione coerente | SOLO OSSERVAZIONE |
| Peso suggerito Global | 0 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-08-31 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 105,54 $ |
| EMA200 weekly target | 111,25 $ |
| Upside verso EMA200 | +5,36% |
| Distanza prezzo da EMA200 | -5,09% |
| Gap EMA50/EMA200 | -5,72% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 59,92 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +86,67% |
| Max gain mediano 12w | +24,21% |
| Drawdown mediano 12w | -37,81% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-07 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-07 05:30:23 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante in miglioramento rispetto a ieri.
- SOL: cambiamento importante in miglioramento rispetto a ieri.
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +85.00% | -2.50 punti |
| SOL | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +65.00% | 0.00 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIBASSISTA | +30.00% | -5.00 punti |

<!-- DAILY_CHANGE_END -->

</details>
<!-- COMPACT_SECTION_END:daily_change -->

<!-- COMPACT_SECTION_START:bounce_after_drawdown -->
<details>
<summary><strong>↕️ Sequenze rimbalzo / dump</strong></summary>

<!-- BOUNCE_AFTER_DRAWDOWN_START -->

---

# Sequenze pratiche: rimbalzo / dump

Report separato completo: [bounce_after_drawdown_report.md](bounce_after_drawdown_report.md)

Questa sezione risponde subito a due domande:

- **Se scende, è una zona di rimbalzo?**
- **Se sale forte, è una zona da prendere profitto?**

| Asset | Scende a | Target rimbalzo | % casi rimbalzo | Movimento reale | Lettura discesa | Sale a | Target dump | % casi dump | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 75.827 $ | 87.800 $ | +80,00% | +15,79% | buona zona storica di rimbalzo | 87.800 $ | 75.827 $ | +2,86% | -13,64% | spike storicamente più resistente |
| SOL | 100,26 $ | 116,09 $ | +61,29% | +15,79% | rimbalzo possibile | 116,09 $ | 100,26 $ | +16,67% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08569 $ | 0,09922 $ | +34,29% | +15,79% | rimbalzo poco frequente | 0,09922 $ | 0,08569 $ | +66,67% | -13,64% | spike spesso scaricato |

## Spiegazione ultra semplice

`% casi rimbalzo` e `% casi dump` non sono percentuali assolute.

Sono percentuali **condizionate**:

- prima deve succedere la prima cosa;
- solo dopo si controlla se succede la seconda.

Esempio rimbalzo:

- prezzo iniziale 100 $
- scende a -5% = 95 $
- poi target +10% = 110 $
- da 95 $ a 110 $ il movimento reale è circa +15,79%

Quindi `poi +10%` non vuol dire +10% dal minimo. Vuol dire +10% dal prezzo iniziale.

Esempio dump:

- prezzo iniziale 100 $
- sale a +10% = 110 $
- poi target -5% = 95 $
- da 110 $ a 95 $ il movimento reale è circa -13,64%

Quindi `dump -5%` non vuol dire -5% dallo spike. Vuol dire che torna fino a 5% sotto il prezzo iniziale.

Nel report principale vedi solo la sintesi. Nel report separato ci sono anche soglie intermedie: -8%, +5%, +15%, ecc.

## Traduzione veloce

- **BTC: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 20 poi sono rimbalzati fino a +10,00%. Percentuale: +80,00% (20/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **BTC: su 40 casi simili, 35 prima sono saliti a +10,00%. Tra quei 35, 1 poi sono scaricati a -5,00%. Percentuale: +2,86% (1/35). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 19 poi sono rimbalzati fino a +10,00%. Percentuale: +61,29% (19/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **SOL: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 5 poi sono scaricati a -5,00%. Percentuale: +16,67% (5/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +34,29% (12/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 14 poi sono scaricati a -5,00%. Percentuale: +66,67% (14/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike spesso scaricato.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-07 05:31:52 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-07 | 2026-09-07T05:30:22Z | 2026-09-07 05:30:23 |
| SOL | 2026-09-07 | 2026-09-07T05:30:22Z | 2026-09-07 05:30:23 |
| DOGE | 2026-09-07 | 2026-09-07T05:30:22Z | 2026-09-07 05:30:23 |

La data di generazione del report non sostituisce la data degli input: se gli snapshot locali sono più vecchi, i valori restano riferiti agli snapshot indicati in tabella.

Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto quando sono disponibili dati successivi

Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g      | P90 30g      |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:-------------|:-------------|
| BTC | 2026-09-07 | 79.818 $ | SALITA | 85,00% | 54.305,64 $ | 85.913,62 $ | 94.260,37 $ | 110.205,29 $ | 136.653,94 $ |
| SOL | 2026-09-07 | 105,54 $ | SALITA | 65,00% | 70,96 $ | 85,30 $ | 126,54 $ | 155,83 $ | 214,85 $ |
| DOGE | 2026-09-07 | 0.09020 $ | DISCESA | 30,00% | 0.06419 $ | 0.06865 $ | 0.07649 $ | 0.09110 $ | 0.10002 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 94.260,37 $ | n/a | 136.653,94 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 1 | 4 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 126,54 $ | n/a | 214,85 $ | n/a |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 0 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.07649 $ | n/a | 0.10002 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-08**; verificato fino al **2026-09-07**; stato **COMPLETO 30/30g**.
- Reale **79.836,79 $**; p50 previsto **73.607,26 $**; scarto **8,46%**.
- Errore medio assoluto **7,97%**; massimo **14,56%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-08**; verificato fino al **2026-09-07**; stato **COMPLETO 30/30g**.
- Reale **105,63 $**; p50 previsto **83,46 $**; scarto **26,57%**.
- Errore medio assoluto **16,71%**; massimo **40,96%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-08**; verificato fino al **2026-09-07**; stato **COMPLETO 30/30g**.
- Reale **0.09032 $**; p50 previsto **0.07938 $**; scarto **13,79%**.
- Errore medio assoluto **12,48%**; massimo **37,77%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 56 | 92,86% | 64,29% | 2,13% | 0,66% |
| BTC | 3g | 52 | 90,38% | 69,23% | 3,36% | 1,14% |
| BTC | 7g | 44 | 90,91% | 72,73% | 5,43% | 2,51% |
| BTC | 14g | 37 | 97,30% | 64,86% | 6,56% | 3,96% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 56 | 78,57% | 57,14% | 2,93% | 1,18% |
| SOL | 3g | 52 | 88,46% | 71,15% | 4,17% | 2,04% |
| SOL | 7g | 44 | 86,36% | 68,18% | 5,92% | 4,22% |
| SOL | 14g | 37 | 81,08% | 64,86% | 8,61% | 7,61% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 56 | 85,71% | 57,14% | 3,39% | 0,90% |
| DOGE | 3g | 52 | 88,46% | 67,31% | 4,80% | 2,26% |
| DOGE | 7g | 44 | 72,73% | 70,45% | 9,35% | 6,71% |
| DOGE | 14g | 37 | 81,08% | 51,35% | 11,12% | 10,02% |
| DOGE | 30g | 23 | 91,30% | 34,78% | 17,34% | 17,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |

### Confronto fuori campione: grezzo vs shadow

| Asset   | Orizzonte   |   Controlli OOS | MAE grezzo   | MAE shadow   | Miglioramento   | Shadow vince   | Copertura larga grezza   | Copertura larga shadow   |
|:--------|:------------|----------------:|:-------------|:-------------|:----------------|:---------------|:-------------------------|:-------------------------|
| BTC | 1g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 1g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 1g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |

## Come leggerlo

- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.
- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.
- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.
- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.
- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.

Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. Sotto 5 controlli resta solo osservazione.
<!-- SCANNER_FORECAST_TRACKER_END -->

<!-- FORECAST_30D_HISTORY_START -->

---

# Storico previsioni 30 giorni

Report separato completo: [forecast_30d_history.md](forecast_30d_history.md)

Righe salvate nello storico: **165**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-07 | BTC | 79.818 $ | SALITA | 85,00% | 94.260 $ | 71.836 $ | 99.621 $ | 2026-10-07 |
| 2026-09-07 | DOGE | 0,09000 $ | DISCESA | 30,00% | 0,08000 $ | 0,07000 $ | 0,10000 $ | 2026-10-07 |
| 2026-09-07 | SOL | 105,54 $ | SALITA | 65,00% | 126,54 $ | 91,99 $ | 133,00 $ | 2026-10-07 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +85,00%       | Casi positivi 85.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **-0,66%**
- Return mediano 14g: **+6,92%**
- Return mediano 30g: **+21,64%**
- Drawdown mediano: **-8,26%**
- Max gain mediano: **+26,53%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+4,18%**
- Spike p75 prima del minimo: **+1,92%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-9,52%**
- Casi con almeno +5% prima del minimo: **+14,71%**
- Casi con almeno +10% prima del minimo: **+2,94%**
- Casi con almeno +15% prima del minimo: **+2,94%**
- Discesa quasi immediata: **+67,65%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25     | P50     | P75     | P90     |
|:-------|:--------|:--------|:--------|:--------|
| +7,55% | +12,82% | +21,64% | +39,40% | +75,41% |

### Grafico pulito: bande + mediana

![Extreme clean BTC](extreme_cases_BTC_positive_clean_bands.png)

### Grafico asset per asset

![Extreme asset medians BTC](extreme_cases_BTC_positive_asset_medians.png)

### Spike massimo prima della discesa

La sigla `g7` sopra una barra significa che il massimo rialzo è avvenuto al giorno 7.

![Extreme spike before dump BTC](extreme_cases_BTC_positive_spike_before_dump.png)

### Spike iniziale contro minimo successivo

![Extreme spike vs low BTC](extreme_cases_BTC_positive_spike_vs_low.png)

### Casi ordinati per risultato finale

![Extreme ranked BTC](extreme_cases_BTC_positive_ranked_returns.png)

### Casi con spike maggiore prima del dump

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                      |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------------|
| UNI-USD         | 2023-07-10 | +83,40%      | +100,00%                 |             10 | -2,12%       |              14 | -51,06%          | +297,17%     | ECCEZIONE POSITIVA            |
| XLM-USD         | 2020-12-06 | +86,68%      | +8,98%                   |             10 | -27,99%      |              17 | -33,92%          | +10,93%      | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2020-12-06 | +85,43%      | +5,49%                   |             10 | -14,15%      |              17 | -18,61%          | +62,60%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2023-11-08 | +86,59%      | +5,31%                   |              2 | -15,83%      |              13 | -20,08%          | +13,46%      | RIALZO MODESTO PRIMA DEL DUMP |
| BTC-USD         | 2019-04-18 | +83,35%      | +5,17%                   |              5 | -1,66%       |               7 | -6,49%           | +37,23%      | ECCEZIONE POSITIVA            |
| AVAX-USD        | 2021-09-03 | +84,12%      | +4,94%                   |              2 | -19,30%      |               5 | -23,10%          | +49,67%      | RIALZO MODESTO PRIMA DEL DUMP |
| 1INCH-USD       | 2023-11-18 | +88,24%      | +4,43%                   |              1 | -7,24%       |               3 | -11,18%          | +2,85%       | ECCEZIONE POSITIVA            |
| LTC-USD         | 2019-02-22 | +84,25%      | +3,77%                   |              1 | -10,29%      |               2 | -13,55%          | +20,92%      | RIALZO MODESTO PRIMA DEL DUMP |
| DASH-USD        | 2019-04-16 | +82,68%      | +2,21%                   |              2 | -11,06%      |              13 | -12,99%          | +22,36%      | ECCEZIONE POSITIVA            |
| ZEC-USD         | 2019-04-16 | +84,50%      | +1,02%                   |              2 | -18,90%      |              23 | -19,72%          | +7,69%       | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2023-11-18 | +86,19%      | +0,95%                   |              1 | -10,75%      |               3 | -11,60%          | +2,26%       | DISCESA QUASI IMMEDIATA       |
| MANA-USD        | 2023-11-16 | +84,03%      | +0,00%                   |              3 | -12,25%      |               5 | -12,26%          | +16,43%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-20 | +88,88%      | +0,00%                   |              0 | -10,09%      |               1 | -10,09%          | +12,61%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-02-25 | +86,85%      | +0,00%                   |              0 | -3,26%       |               1 | -3,26%           | +70,51%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2019-02-24 | +86,56%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +25,99%      | DISCESA QUASI IMMEDIATA       |
| MATIC-USD       | 2023-11-21 | +86,41%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,56%      | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-20 | +86,07%      | +0,00%                   |              0 | -12,15%      |               1 | -12,15%          | +39,80%      | DISCESA QUASI IMMEDIATA       |
| FIL-USD         | 2023-11-20 | +86,02%      | +0,00%                   |              0 | -9,91%       |               1 | -9,91%           | +13,56%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-21 | +85,59%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +55,32%      | DISCESA QUASI IMMEDIATA       |
| SAND-USD        | 2023-11-20 | +85,45%      | +0,00%                   |              0 | -10,70%      |               1 | -10,70%          | +25,39%      | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
<!-- EXTREME_CASES_PATH_END -->

</details>
<!-- COMPACT_SECTION_END:extreme_cases -->

<!-- COMPACT_SECTION_START:scanner_full_detail -->
<details>
<summary><strong>📚 Scanner statistico completo — percentili, mappe e 40 casi storici</strong></summary>

# Come leggere questo report

Leggilo sempre in questo ordine:

1. **Direzione più probabile**: ti dice se storicamente era più facile salita, discesa o incertezza.
2. **Casi positivi / negativi**: ti dice la percentuale storica di salita o discesa dopo 30 giorni.
3. **Return 30d**: ti dice dove potrebbe stare il prezzo fra 30 giorni.
4. **Drawdown 30d**: ti dice quanto potrebbe scendere durante quei 30 giorni.
5. **Max gain 30d**: ti dice quanto potrebbe salire durante quei 30 giorni.
6. **Scanner autocalibrato**: dopo abbastanza dati, confronta previsione e realtà e corregge la lettura.

La frase più importante è questa:

> **Return = prezzo finale dopo 30 giorni. Drawdown = discesa durante il mese. Max gain = rialzo durante il mese.**

---

# Scheda veloce: cosa sono i percentili

I **percentili** sono solo un modo per trasformare i 40 casi storici simili in scenari semplici.

## Traduzione semplice

- **Percentile 10%** = molto male / scenario brutto.
- **Percentile 25%** = male / scenario negativo.
- **Percentile 50%** = normale / scenario centrale. È il più importante.
- **Percentile 75%** = bene / scenario buono.
- **Percentile 90%** = molto bene / scenario molto forte.

## Cosa guardare davvero

- Per capire la situazione normale: guarda sempre il **Percentile 50%**.
- Per capire il rischio con leva: guarda **Drawdown 25%** e **Drawdown 10%**.
- Per capire un possibile take profit: guarda **Max gain 50%** e **Max gain 75%**.

## I tre tipi di percentili

- **Percentili Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.
- **Percentili Drawdown 30d** = quanto potrebbe scendere durante i 30 giorni.
- **Percentili Max gain 30d** = quanto potrebbe salire durante i 30 giorni.

## Esempio semplice

Se SOL oggi vale 82 $ e il report dice:

- **Return 50% → 81 $**: fra 30 giorni lo scenario normale è circa 81 $.
- **Drawdown 50% → 77 $**: durante il mese può scendere normalmente verso 77 $.
- **Max gain 50% → 92 $**: durante il mese può fare uno spike normale verso 92 $.

Quindi può salire e scendere durante il mese, ma il **return** guarda solo dove finisce dopo 30 giorni.

---

# Lettura velocissima

Questa è la parte da leggere per prima. Ti dice subito se lo scenario è più da salita, discesa o incertezza.

## Bitcoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **85,00%**
- Casi negativi / discesa storica: **15,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **79.817,81 $**
- Return normale fra 30 giorni: **94.260,37 $** (18,09%)
- Drawdown normale durante il mese: **71.835,56 $** (-10,00%)
- Drawdown brutto da rispettare: **67.742,88 $** (-15,13%)
- Max gain normale durante il mese: **99.621,23 $** (24,81%)
- Max gain buono / take profit ottimistico: **122.189,72 $** (53,09%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **65,00%**
- Casi negativi / discesa storica: **35,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **105,54 $**
- Return normale fra 30 giorni: **126,54 $** (19,90%)
- Drawdown normale durante il mese: **91,99 $** (-12,84%)
- Drawdown brutto da rispettare: **81,26 $** (-23,01%)
- Max gain normale durante il mese: **133,00 $** (26,02%)
- Max gain buono / take profit ottimistico: **166,99 $** (58,22%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **30,00%**
- Casi negativi / discesa storica: **70,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,08 $** (-15,20%)
- Drawdown normale durante il mese: **0,07 $** (-24,26%)
- Drawdown brutto da rispettare: **0,06 $** (-30,75%)
- Max gain normale durante il mese: **0,10 $** (10,62%)
- Max gain buono / take profit ottimistico: **0,11 $** (18,05%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 79.817,81 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **85,00%**
- Probabilità storica di discesa: **15,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **54.305,64 $** (-31,96%)
- Se va male: **85.913,62 $** (7,64%)
- Scenario normale: **94.260,37 $** (18,09%)
- Se va bene: **110.205,29 $** (38,07%)
- Se va molto bene: **136.653,94 $** (71,21%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **71.835,56 $** (-10,00%)
- Discesa brutta: **67.742,88 $** (-15,13%)
- Discesa molto brutta: **50.668,29 $** (-36,52%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **99.621,23 $** (24,81%)
- Rialzo buono: **122.189,72 $** (53,09%)
- Rialzo molto forte: **150.001,51 $** (87,93%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **71.835,56 $** e uno spike normale intorno a **99.621,23 $**.

La chiusura a 30 giorni era più spesso positiva: salita 85,00%, discesa 15,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 105,54 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **65,00%**
- Probabilità storica di discesa: **35,00%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **70,96 $** (-32,77%)
- Se va male: **85,30 $** (-19,17%)
- Scenario normale: **126,54 $** (19,90%)
- Se va bene: **155,83 $** (47,65%)
- Se va molto bene: **214,85 $** (103,57%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **91,99 $** (-12,84%)
- Discesa brutta: **81,26 $** (-23,01%)
- Discesa molto brutta: **60,92 $** (-42,28%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **133,00 $** (26,02%)
- Rialzo buono: **166,99 $** (58,22%)
- Rialzo molto forte: **240,40 $** (127,78%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **91,99 $** e uno spike normale intorno a **133,00 $**.

La chiusura a 30 giorni era più spesso positiva: salita 65,00%, discesa 35,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,09 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **30,00%**
- Probabilità storica di discesa: **70,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,06 $** (-28,84%)
- Se va male: **0,07 $** (-23,90%)
- Scenario normale: **0,08 $** (-15,20%)
- Se va bene: **0,09 $** (1,00%)
- Se va molto bene: **0,10 $** (10,88%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-24,26%)
- Discesa brutta: **0,06 $** (-30,75%)
- Discesa molto brutta: **0,06 $** (-33,16%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (10,62%)
- Rialzo buono: **0,11 $** (18,05%)
- Rialzo molto forte: **0,12 $** (35,52%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 30,00%, discesa 70,00%. Quindi la lettura principale è prudente/debole.

---

# Come leggere correttamente i 30 giorni

Ogni report giornaliero è una previsione statistica sui **prossimi 30 giorni**.

Ci sono tre dati diversi:

1. **Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.
2. **Drawdown 30d** = quanto potrebbe scendere durante quei 30 giorni.
3. **Max gain 30d** = quanto potrebbe salire al massimo durante quei 30 giorni.

Il prezzo può salire durante il mese e poi chiudere sotto, oppure scendere prima e poi recuperare. Per chi usa leva, il drawdown è spesso più importante del prezzo finale.

# Controllo accuratezza dello scanner

Questa sezione controlla se lo scanner sta funzionando davvero. Ogni giorno viene salvata una previsione. Dopo 30 giorni, lo scanner confronta quella previsione con quello che è successo realmente.

## Come leggerla

- **Previsioni già controllate** = quante vecchie previsioni hanno già compiuto 30 giorni.
- **Direzione corretta** = quante volte lo scanner ha indovinato salita o discesa finale a 30 giorni.
- **Errore medio scenario centrale** = quanto era distante il prezzo reale dal prezzo centrale previsto.
- **Zona rischio toccata** = quante volte il prezzo è sceso fino alla zona di rischio prevista.
- **Zona rialzo toccata** = quante volte il prezzo è salito fino alla zona rialzo prevista.

## Riassunto accuratezza

### Bitcoin

- Previsioni già controllate: **30**
- Direzione corretta: **86,96%**
- Errore medio dello scenario centrale: **7,19%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **3,33%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **30**
- Direzione corretta: **92,59%**
- Errore medio dello scenario centrale: **15,19%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **33,33%**
- Prezzo finale dentro lo scenario 10%-90%: **93,33%**

### Solana

- Previsioni già controllate: **30**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,32%**
- Zona rischio toccata: **6,67%**
- Zona rialzo media toccata: **36,67%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

Spiegazione semplice: se col tempo la direzione corretta è bassa o l'errore medio è alto, lo scanner va preso con più cautela. Se invece molte previsioni finiscono dentro i livelli previsti, allora lo scanner sta diventando più affidabile.

---

# Scanner autocalibrato

Questa è una sezione separata dalla previsione storica grezza. La previsione grezza resta quella basata sui pattern storici. Qui invece lo scanner guarda i propri errori passati e prova a correggere leggermente la lettura.

## Come funziona

Lo scanner confronta le sue vecchie previsioni con la realtà dopo 30 giorni.

- Se in passato è stato troppo ottimista, abbassa la stima.
- Se in passato è stato troppo pessimista, alza la stima.
- Se ha sottostimato il drawdown, rende la zona rischio più prudente.
- Se ha sovrastimato gli spike, riduce la zona rialzo calibrata.

La calibrazione non modifica il codice. Crea solo una seconda lettura: **scanner grezzo** contro **scanner corretto dai suoi errori reali**.

Regola: servono almeno **30 previsioni controllate per asset** prima di applicare la calibrazione. Prima di allora mostra solo dati insufficienti.

## Bitcoin

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **86,96%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **18,09%** → **94.260,37 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **20,10%** → **95.863,04 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-10,00%** → **71.835,56 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **-5,28%** → **75.605,61 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **24,81%** → **99.621,23 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **21,99%** → **97.366,44 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **19,90%** → **126,54 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **28,70%** → **135,83 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-12,84%** → **91,99 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-9,85%** → **95,15 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **26,02%** → **133,00 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **30,03%** → **137,24 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **92,59%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **DISCESA**
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-15,20%** → **0,08 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **-0,02%** → **0,09 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-24,26%** → **0,07 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-8,92%** → **0,08 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **10,62%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **13,14%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 79.817,81 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **85,00%**
- Casi negativi dopo 30 giorni: **15,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,89%**
- Rendimento medio dopo 30 giorni: **29,54%**
- Rendimento centrale dopo 30 giorni: **18,09%**
- Discesa media durante i 30 giorni: **-12,63%**
- Massimo rialzo medio durante i 30 giorni: **45,19%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **103.394,66 $**
- Scenario centrale a 30 giorni: **94.260,37 $**
- Zona di rischio media: **69.737,88 $**
- Zona di rialzo media: **115.890,90 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -31,96% → **54.305,64 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 7,64% → **85.913,62 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 18,09% → **94.260,37 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 38,07% → **110.205,29 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 71,21% → **136.653,94 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -36,52% → **50.668,29 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,13% → **67.742,88 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,00% → **71.835,56 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **79.817,81 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **79.817,81 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 7,08% → **85.472,53 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 15,57% → **92.245,42 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 24,81% → **99.621,23 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 53,09% → **122.189,72 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 87,93% → **150.001,51 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| THETA-USD       | 2023-08-13   | 2023-11-20 |        88.88 |        12.61 |         -10.09 |          20.8  |
| 1INCH-USD       | 2023-08-11   | 2023-11-18 |        88.24 |         2.85 |          -7.24 |          17.19 |
| BNB-USD         | 2018-11-18   | 2019-02-25 |        86.85 |        70.51 |          -3.26 |          75.63 |
| XLM-USD         | 2020-08-29   | 2020-12-06 |        86.68 |        10.93 |         -27.99 |          10.93 |
| INJ-USD         | 2023-08-01   | 2023-11-08 |        86.59 |        13.46 |         -15.83 |          13.46 |
| THETA-USD       | 2018-11-17   | 2019-02-24 |        86.56 |        25.99 |           0    |         109.84 |
| MATIC-USD       | 2023-08-14   | 2023-11-21 |        86.41 |        11.56 |           0    |          25.86 |
| ZIL-USD         | 2023-08-11   | 2023-11-18 |        86.19 |         2.26 |         -10.75 |          12.73 |
| ALGO-USD        | 2023-08-13   | 2023-11-20 |        86.07 |        39.8  |         -12.15 |          52.49 |
| XRP-USD         | 2020-08-29   | 2020-12-06 |        86.06 |       -63.42 |         -65.83 |           0    |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 105,54 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **65,00%**
- Casi negativi dopo 30 giorni: **35,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,53%**
- Rendimento medio dopo 30 giorni: **30,58%**
- Rendimento centrale dopo 30 giorni: **19,90%**
- Discesa media durante i 30 giorni: **-17,63%**
- Massimo rialzo medio durante i 30 giorni: **54,72%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **137,82 $**
- Scenario centrale a 30 giorni: **126,54 $**
- Zona di rischio media: **86,94 $**
- Zona di rialzo media: **163,29 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -32,77% → **70,96 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -19,17% → **85,30 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 19,90% → **126,54 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 47,65% → **155,83 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 103,57% → **214,85 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -42,28% → **60,92 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -23,01% → **81,26 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,84% → **91,99 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,29% → **99,96 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,36% → **104,11 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,52% → **106,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,42% → **116,54 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 26,02% → **133,00 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 58,22% → **166,99 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 127,78% → **240,40 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZIL-USD         | 2020-08-31   | 2020-12-08 |        87.88 |       143.04 |          -5.35 |         185.86 |
| VET-USD         | 2020-03-09   | 2020-06-16 |        87.5  |        99.18 |          -8.4  |         121.32 |
| VET-USD         | 2023-08-11   | 2023-11-18 |        86.87 |        52.02 |          -7.84 |          52.02 |
| BNB-USD         | 2018-11-18   | 2019-02-25 |        86    |        70.51 |          -3.26 |          75.63 |
| RUNE-USD        | 2026-01-31   | 2026-05-10 |        85.94 |       -36.07 |         -47.56 |           2.93 |
| HBAR-USD        | 2020-10-25   | 2021-02-01 |        85.71 |        46.2  |           0    |          73.81 |
| THETA-USD       | 2023-08-13   | 2023-11-20 |        85.5  |        12.61 |         -10.09 |          20.8  |
| 1INCH-USD       | 2023-08-11   | 2023-11-18 |        84.49 |         2.85 |          -7.24 |          17.19 |
| NEO-USD         | 2023-08-09   | 2023-11-16 |        84.4  |        14.38 |         -11.27 |          14.38 |
| XRP-USD         | 2020-08-29   | 2020-12-06 |        84.39 |       -63.42 |         -65.83 |           0    |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,09 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **30,00%**
- Casi negativi dopo 30 giorni: **70,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,86%**
- Rendimento medio dopo 30 giorni: **-8,24%**
- Rendimento centrale dopo 30 giorni: **-15,20%**
- Discesa media durante i 30 giorni: **-21,47%**
- Massimo rialzo medio durante i 30 giorni: **17,01%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -28,84% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -23,90% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -15,20% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 1,00% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 10,88% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,16% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -30,75% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -24,26% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -11,48% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -4,69% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,90% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 10,62% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 18,05% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 35,52% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| MANA-USD        | 2025-01-30   | 2025-05-09 |        84.71 |       -20.93 |         -26.57 |           8.86 |
| QTUM-USD        | 2021-05-16   | 2021-08-23 |        84.14 |       -22.03 |         -32.66 |          16.48 |
| MANA-USD        | 2022-10-23   | 2023-01-30 |        83.28 |       -12.23 |         -16.35 |           7.7  |
| FIL-USD         | 2022-05-10   | 2022-08-17 |        83.26 |       -28.78 |         -31.42 |           0    |
| INJ-USD         | 2022-05-18   | 2022-08-25 |        83.2  |        -7.49 |         -18.36 |           4.84 |
| NEO-USD         | 2019-08-05   | 2019-11-12 |        82.92 |       -28.61 |         -29.67 |           8.66 |
| YFI-USD         | 2022-05-05   | 2022-08-12 |        82.64 |       -11.73 |         -26.53 |           0    |
| QTUM-USD        | 2020-08-29   | 2020-12-06 |        82.52 |        -1.55 |         -21.59 |           6.25 |
| ETH-USD         | 2025-02-14   | 2025-05-24 |        82.39 |        -4.3  |         -11.95 |          11.18 |
| BTC-USD         | 2025-02-01   | 2025-05-11 |        82.18 |         5.91 |          -2.43 |           7.27 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-07 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-07 | RECOVERY | 79.818 $ | True | 29.48% | -6.03% | RECOVERY | 29.48% | -6.03% |
| DOGE-USD | 2026-09-07 | MIXED | 0.09020 $ | True | 6.38% | -13.18% | RECOVERY | 29.48% | -6.03% |
| SOL-USD | 2026-09-07 | RECOVERY | 105,54 $ | True | 62.46% | -10.83% | RECOVERY | 29.48% | -6.03% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 85.00% | 18.09% | 38.07% | 71.21% | -10.00% | -36.52% | 24.81% | 53.09% | 87.93% | 80.00% | 20.60% | 44.50% | 93.83% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | 142.18% | 219.68% | 266.18% | -8.51% | -13.62% | 160.82% | 237.65% | 283.75% | 50.00% | -18.01% | -4.58% | 3.48% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -15.20% | 1.00% | 10.88% | -24.26% | -33.16% | 10.62% | 18.05% | 35.52% | 30.00% | -8.03% | 6.67% | 33.27% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 19.90% | 47.65% | 103.57% | -12.84% | -42.28% | 26.02% | 58.22% | 127.78% | 65.00% | 26.34% | 79.29% | 153.03% |
| SOL-USD | SAME_BTC_REGIME | 2 | 50.00% | 41.26% | 70.22% | 87.60% | -13.78% | -18.08% | 60.66% | 90.99% | 109.19% | 100.00% | 74.80% | 95.71% | 108.26% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 39.66% | 81.40% | 151.20% | -12.81% | -19.79% | 40.90% | 118.23% | 249.84% | 100.00% | 61.21% | 116.05% | 163.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -16.66% | -16.66% | -16.66% | -19.15% | -19.15% | 0.00% | 0.00% | 0.00% | 100.00% | 32.97% | 32.97% | 32.97% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 11 | 81.82% | 25.26% | -11.06% | 71.04% | 81.82% | 32.86% | 97.85% |
| BTC-USD | HISTORICAL_BTC_BULL | 29 | 86.21% | 13.76% | -9.12% | 45.80% | 79.31% | 18.05% | 82.45% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 14 | 28.57% | -11.98% | -17.35% | 20.50% | 14.29% | -15.24% | 20.73% |
| DOGE-USD | HISTORICAL_BTC_BULL | 14 | 42.86% | -2.92% | -18.78% | 11.16% | 50.00% | 0.96% | 48.39% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 11 | 18.18% | -22.03% | -30.53% | 23.72% | 27.27% | -7.28% | 23.72% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 64.71% | 22.36% | -13.77% | 54.85% | 58.82% | 29.33% | 93.12% |
| SOL-USD | HISTORICAL_BTC_BULL | 16 | 87.50% | 43.00% | -8.88% | 75.61% | 87.50% | 27.80% | 179.85% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 0.00% | -18.80% | -21.80% | 18.94% | 0.00% | -12.77% | 21.48% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 41.26% | -13.78% | 90.99% | 100.00% | 74.80% | 117.56% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 90.32% | 20.77% | -8.74% | 49.31% | 87.10% | 22.02% | 72.74% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 10.93% | -15.83% | 39.28% | 57.14% | 85.18% | 166.29% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 142.18% | -8.51% | 237.65% | 50.00% | -18.01% | 247.17% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 14 | 28.57% | -6.43% | -16.12% | 15.78% | 14.29% | -13.80% | 18.90% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 22 | 31.82% | -19.34% | -27.18% | 20.48% | 36.36% | -7.63% | 44.18% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -23.58% | -23.58% | 33.50% | 66.67% | 6.81% | 33.50% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -31.12% | -33.14% | 0.00% | 0.00% | -53.85% | 0.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 14.38% | -11.06% | 54.85% | 62.07% | 22.02% | 81.70% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 62.23% | -16.62% | 159.65% | 66.67% | 63.47% | 183.86% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -9.69% | -21.80% | 11.27% | 0.00% | -9.57% | 11.27% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 39.66% | -12.81% | 118.23% | 100.00% | 61.21% | 161.67% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 0 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 1 | 4 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

_No data._

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the preferred and most stringent filter.
- Below 5 full-regime matches, the selector falls back first to SAME_ASSET_REGIME and then to SAME_BTC_REGIME.
- A fallback is always labelled as less stringent; groups are never combined.
- If every group is below threshold, the result is INSUFFICIENT_REGIME_MATCHES.
- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.
- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.

## Regime definitions

- BULL: price above MA200, MA200 rising, positive 90d trend.
- BEAR: price below MA200, MA200 falling, weak 90d trend.
- RECOVERY: improving 90d trend, but not yet a clean bull structure.
- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.
- MIXED: unclear regime.
- UNKNOWN: not enough historical data.
<!-- MARKET_REGIME_MATCH_END -->

</details>
<!-- COMPACT_SECTION_END:market_regime -->

<!-- COMPACT_SECTION_START:classic_technical -->
<details>
<summary><strong>📐 Conferma tecnica classica</strong></summary>

<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->
# Classic technical confirmation report

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [classic_technical_confirmation_report.md](classic_technical_confirmation_report.md)

Questo modulo controlla se il setup è confermato secondo analisi tecnica classica. Non sostituisce lo scanner frattale: serve come filtro di conferma.

Cosa controlla:

- trend daily e weekly
- stage analysis stile Weinstein
- struttura massimi/minimi
- breakout o breakdown con volume
- RSI e MACD
- OBV, CMF e volume relativo
- candele principali
- Wyckoff semplificato
- volatilità tecnica locale tramite ATR e distanza dai livelli

## Sintesi

| Asset | Prezzo | Score | Verdetto | Stage | Struttura | Wyckoff | Volatilità locale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.818 $ | +4 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | SIGN OF STRENGTH POSSIBILE | MEDIO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 105,54 $ | +7 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09020 $ | +8 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | SOLO TRADING VELOCE / NO LEVA AGGRESSIVA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | 0 | -1 | +2 | 0 | 0 | +2 | +4 |
| SOL | +1 | +2 | 0 | +2 | 0 | 0 | +2 | +7 |
| DOGE | +1 | +2 | +3 | +2 | 0 | 0 | 0 | +8 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 81.347 $ | 82.262 $ | 61.276 $ | 3,04% | 23,05% | 26,54% |
| SOL | 97,45 $ | 110,04 $ | 110,04 $ | 70,69 $ | 5,00% | 43,45% | 58,16% |
| DOGE | 0.08189 $ | 0.09169 $ | 0.09998 $ | 0.06797 $ | 5,04% | 29,73% | 4,67% |

## Lettura dettagliata

### BTC

- Prezzo: **79.818 $**
- Score classico: **+4 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **MEDIO** — ATR14 3,04%; distanza supporto 0,80%; distanza resistenza 1,89%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-1** — RSI sano 66.9; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.24; volume ratio 0.61
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 66.87 |
| MACD histogram | -172.17019 |
| CMF20 | 0.238 |
| Volume ratio 20 | 0.61 |
| MA20 | 77.228 $ |
| MA50 | 69.396 $ |
| MA100 | 66.466 $ |
| MA200 | 69.751 $ |
| Pendenza MA50 20g | +9,00% |
| Pendenza MA200 60g | -6,19% |
| Bollinger width | 19,79% |
| Bollinger position | 0.67 |

### SOL

- Prezzo: **105,54 $**
- Score classico: **+7 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,00%; distanza supporto 8,40%; distanza resistenza 4,16%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 67.5; RSI in miglioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.21; volume ratio 0.83
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 67.49 |
| MACD histogram | -0.30132 |
| CMF20 | 0.214 |
| Volume ratio 20 | 0.83 |
| MA20 | 98,47 $ |
| MA50 | 84,38 $ |
| MA100 | 78,92 $ |
| MA200 | 82,43 $ |
| Pendenza MA50 20g | +10,81% |
| Pendenza MA200 60g | -11,06% |
| Bollinger width | 29,74% |
| Bollinger position | 0.73 |

### DOGE

- Prezzo: **0.09020 $**
- Score classico: **+8 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SOLO TRADING VELOCE / NO LEVA AGGRESSIVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,04%; distanza supporto 10,29%; distanza resistenza 1,52%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+3** — RSI sano 63.2; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.07; volume ratio 0.93
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 63.23 |
| MACD histogram | 0.00002 |
| CMF20 | 0.068 |
| Volume ratio 20 | 0.93 |
| MA20 | 0.08532 $ |
| MA50 | 0.07641 $ |
| MA100 | 0.07853 $ |
| MA200 | 0.08843 $ |
| Pendenza MA50 20g | +6,36% |
| Pendenza MA200 60g | -13,43% |
| Bollinger width | 25,79% |
| Bollinger position | 0.71 |

## Come leggere lo score

- **+8 a +12**: conferma tecnica rialzista forte.
- **+5 a +7**: setup costruttivo, ma può mancare ancora una rottura pulita.
- **+2 a +4**: setup anticipato, interessante ma non confermato.
- **-1 a +1**: neutrale / misto.
- **-4 a -2**: debole / non confermato.
- **-8 o meno**: conferma tecnica ribassista.

Nota: questo modulo deve pesare poco nel Global finché non viene verificato dalla calibrazione. La funzione principale è evitare di confondere un contesto interessante con una conferma vera.
<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->

</details>
<!-- COMPACT_SECTION_END:classic_technical -->

<!-- COMPACT_SECTION_START:classic_visual -->
<details>
<summary><strong>🖼️ Grafici e pattern Classic Visual</strong></summary>

<!-- CLASSIC_TECHNICAL_VISUAL_START -->
# Classic technical visual report

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [classic_technical_visual_report.md](classic_technical_visual_report.md)

Questo report crea grafici visivi dei pattern tecnici principali. Serve per vedere il grafico e il ciclo di vita dei pattern; non aggiunge automaticamente punteggio al Global.

Regola anti-pattern-zombie: dopo il breakout un pattern passa da ATTIVO a CONFERMATO RECENTE, poi a MATURO. Quando raggiunge il target o viene invalidato vale 0 e non resta confermato per sempre.

Pattern controllati:

- doppio minimo
- doppio massimo
- testa e spalle
- testa e spalle inverso
- triangolo / compressione
- candela giornaliera principale
- pivot high / pivot low
- supporto, resistenza, breakout e breakdown 60 giorni
- data breakout, età, target teorico, progresso e invalidazione
- livelli Fibonacci 23,6 / 38,2 / 50 / 61,8 / 78,6 letti dal Technical Structure

## Sintesi visiva

| Asset | Prezzo | Pattern principale | Stato | Famiglia | Breakout | Target | Progresso | Distanza neckline | Fibonacci | Stato prezzo | Supporto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.818 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 38,22% | Fib 23,6% NON ATTIVO (0) @ 75.778 $ | NEL RANGE | 76.248 $ |
| SOL | 105,54 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 49,29% | Fib 23,6% TENUTO (+1) @ 98,33 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.09020 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 32,70% | Fib 23,6% TESTATO (0) @ 0.08924 $ | NEL RANGE | 0.08930 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **29 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **38,22%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 75.778 $** — Swing UP 2026-07-01 57.748 -> 2026-08-28 81.347; livello più vicino 23.6% a 75.778; stato NON ATTIVO; confluenza: supporto tecnico.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76.248 $**
- Resistenza: **81.347 $**
- Breakout 60g: **82.262 $**
- Breakdown 60g: **61.276 $**
- RSI14: **66.81**
- ATR14: **3,04%**
- Volume ratio 20g: **0.61**
- Rendimento 30g: **+23,02%**
- Rendimento 90g: **+26,51%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 82.792 $ | n/a | n/a | 90.626 $ | n/a | 3,73% | 81.136 $ | Due minimi simili a 74.959 $ e 76.248 $. Neckline circa 82.792 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 32.703 $ | n/a | 38,22% | 58.903 $ | Due massimi simili a 82.792 $ e 81.347 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 10 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **29 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **49,29%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (+1) @ 98,33 $** — Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato TENUTO; confluenza: supporto tecnico.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **110,04 $**
- Breakout 60g: **110,04 $**
- Breakdown 60g: **70,69 $**
- RSI14: **67.39**
- ATR14: **5,00%**
- Volume ratio 20g: **0.83**
- Rendimento 30g: **+43,31%**
- Rendimento 90g: **+58,01%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 49,29% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 29 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 19g | 85,65 $ | 366,02% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 366,02%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 19g | 84,05 $ | 503,62% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 503,62%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **27 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **32,70%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 0.08924 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-09-02 0.08028; livello più vicino 23.6% a 0.08924; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08930 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **63.09**
- ATR14: **5,05%**
- Volume ratio 20g: **0.93**
- Rendimento 30g: **+29,55%**
- Rendimento 90g: **+4,53%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 32,70% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 27 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 18g | 0.08952 $ | 106,64% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (18 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 106,64%; prezzo sopra neckline. |

## Stati del ciclo di vita

- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; score 0.
- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; score prudente ±1.
- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; score ±2.
- **MATURO**: breakout più vecchio di 14 giorni e ancora valido; score ridotto ±1.
- **TARGET RAGGIUNTO**: movimento teorico già completato; score 0.
- **INVALIDATO**: due chiusure consecutive oltre la soglia opposta; score 0.

## Come leggerlo

- Il grafico in alto mostra prezzo, MA20, MA50, MA200, supporti, resistenze, neckline, target, invalidazione e livelli Fibonacci.
- Il pannello centrale mostra RSI14.
- Il pannello basso mostra volume e media volume 20 giorni.
- Un pattern CANDIDATO non è un segnale operativo: il progresso target resta n/a e viene mostrata soltanto la distanza dalla neckline.
- TARGET RAGGIUNTO e INVALIDATO restano visibili per memoria storica, ma valgono 0.
- Il pattern principale usa come fonte autorevole il lifecycle di technical_structure_metrics.csv; il detector visuale resta di supporto grafico.
- Fibonacci non crea un segnale autonomo: pesa al massimo ±1 nel Technical Structure solo con una confluenza indipendente.

Nota: questi pattern sono riconosciuti con regole algoritmiche semplici. Sono utili per visualizzare il grafico, ma vanno sempre controllati a occhio.
<!-- CLASSIC_TECHNICAL_VISUAL_END -->

</details>
<!-- COMPACT_SECTION_END:classic_visual -->

<!-- COMPACT_SECTION_START:fractal_path -->
<details>
<summary><strong>🛤️ Tracking percorso frattale SOL/BTC</strong></summary>

<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-07**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-22**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **105,54 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+68,14%**
- Aderenza live principale: **+71,92%**
- Errore medio live principale: **14,04%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **93**
- Osservazioni inclusive dal bottom: **94**
- Osservazioni da inizio programma/scanner: **67**
- Errore assoluto medio dal bottom: **11,74%**
- Errore assoluto medio da inizio programma: **14,04%**
- Gap firmato medio ultimi 7 giorni: **+6,88%**
- Errore assoluto medio ultimi 7 giorni: **6,88%**
- Gap ultimo giorno: **+10,76%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+10,76%**
- Gap firmato medio 7g: **+6,88%**
- Errore assoluto medio 7g: **6,88%**
- Variazione recente gap: **+4,38%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 103,19 $ | 96,26 $ | +7,20% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 105,54 $ | 95,29 $ | +10,76% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-14 | 93,15 $ | 103,17 $ | 101,00 $ / 105,54 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-21 | 85,55 $ | 94,76 $ | 94,76 $ / 105,54 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-28 | 96,02 $ | 106,36 $ | 88,08 $ / 107,97 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-05 | 107,57 $ | 119,15 $ | 88,08 $ / 122,94 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-12 | 111,67 $ | 123,69 $ | 88,08 $ / 123,69 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-19 | 111,00 $ | 122,95 $ | 88,08 $ / 124,26 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-26 | 118,72 $ | 131,50 $ | 88,08 $ / 131,92 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-02 | 113,54 $ | 125,76 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-09 | 111,96 $ | 124,01 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-16 | 114,26 $ | 126,56 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-23 | 108,81 $ | 120,52 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-30 | 107,93 $ | 119,55 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-07 | 103,74 $ | 114,90 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-14 | 107,22 $ | 118,76 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-21 | 103,78 $ | 114,95 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-28 | 98,97 $ | 109,62 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-04 | 118,28 $ | 131,01 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-11 | 118,52 $ | 131,27 $ | 88,08 $ / 133,93 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 53 | 33,96% | 11,31% | 12,91% |
| 14g | 46 | 23,91% | 18,75% | 11,67% |
| 21g | 39 | 15,38% | 27,25% | 13,41% |
| 28g | 34 | 32,35% | 25,45% | 12,89% |
| 35g | 27 | 48,15% | 16,52% | 11,95% |
| 42g | 20 | 100,00% | 7,54% | 10,94% |
| 49g | 13 | 100,00% | 6,52% | 10,58% |
| 56g | 6 | 100,00% | 8,03% | 7,46% |
| 63g | 0 | n/a | n/a | n/a |
| 70g | 0 | n/a | n/a | n/a |
| 77g | 0 | n/a | n/a | n/a |
| 84g | 0 | n/a | n/a | n/a |
| 91g | 0 | n/a | n/a | n/a |
| 98g | 0 | n/a | n/a | n/a |
| 105g | 0 | n/a | n/a | n/a |
| 112g | 0 | n/a | n/a | n/a |
| 119g | 0 | n/a | n/a | n/a |
| 126g | 0 | n/a | n/a | n/a |

## Regola di lettura

- La somiglianza strutturale descrive la forma.
- Il gap ancorato descrive la distanza reale dal percorso.
- Lo scenario riancorato non dimostra che il frattale sia valido.
- Prima di pesare il modulo servono milestone maturate e un errore ancorato accettabile.
<!-- FRACTAL_PATH_TRACKER_END -->

<!-- SOL_BTC_FRACTAL_HISTORY_START -->

---

# Storico frattale SOL/BTC

Per vedere la tabella giorno per giorno devi aprire/cliccare questo file:

**[sol_btc_fractal_history.md](sol_btc_fractal_history.md)**

Ultima lettura salvata: **2026-09-07** — SOL 105,54 $, gap +10,76%, somiglianza +68,14%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.707 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0051% | -1,97% | 1,26 | +0,37% | 0 $ | 0 $ |
| SOL | 105,30 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0079% | -0,56% | 0,80 | +4,43% | 0 $ | 0 $ |
| DOGE | 0.08993 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0092% | -5,60% | 0,78 | +5,30% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0106% | 159,44 mln $ | 0,04 | -0,30% |
| BTC | Bitget | OK | +0,0061% | 2,62 mld $ | 2,91 | -66,58% |
| BTC | Kucoin | OK | +0,0036% | 1,22 mld $ | 0,39 | +2,61% |
| SOL | Kraken | OK | -0,0085% | 29,79 mln $ | 0,02 | +4,44% |
| SOL | Bitget | OK | +0,0057% | 473,13 mln $ | 0,12 | -15,50% |
| SOL | Kucoin | OK | +0,0013% | 210,91 mln $ | 0,27 | +5,09% |
| DOGE | Kraken | OK | +0,0027% | 4,66 mln $ | 0,14 | -15,06% |
| DOGE | Bitget | OK | +0,0100% | 113,05 mln $ | 0,00 | -25,09% |
| DOGE | Kucoin | OK | +0,0097% | 85,80 mln $ | 0,16 | -17,98% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +66,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **-0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 1.
- Flusso taker/order book: **-0,25**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto; nessuna conferma exchange netta. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **-0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 8, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **-0,25**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +85,00% | +18,09% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +85,00% | +18,09% |
| SOL | +65,00% | +19,90% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +65,00% | +19,90% |
| DOGE | +30,00% | -15,20% | 3 | +66,67% | RACCOLTA DATI | 0,00 | +30,00% | -15,20% |

## Dati salvati

- `exchange_market_data_snapshot.json`: fotografia derivata Kraken + Bitget + KuCoin, con OKX e Coinbase ausiliari.
- `exchange_market_data_intraday.csv`: memoria operativa mobile degli ultimi 180 giorni, ripristinata da due copie ridondanti su GitHub Releases.
- `exchange_intraday_YYYY-MM.csv.gz`: archivio mensile permanente dei dati intraday, creato dopo la chiusura del mese.
- `exchange_microstructure_metrics.csv`: score e conferme correnti lette dal Global.
- `exchange_microstructure_history.csv`: prima fotografia giornaliera congelata, usata per valutare le previsioni.
- `exchange_signal_tracker_metrics.csv`: accuratezza a 1/3/7/14/30 giorni.
- `exchange_prediction_overlay.csv`: confronto scanner grezzo vs overlay calibrato.

## Regole di prudenza

- Un muro dell'order book può essere cancellato: non è un supporto garantito.
- Funding, OI e flusso misurano pressione/affollamento, non direzione certa.
- OI in aumento conta soltanto insieme alla direzione del prezzo e al taker flow.
- La componente liquidazioni resta neutrale finché non esiste un feed pubblico completo e verificato.
- Prima dei 30 controlli a 7g il modulo non pesa nel Global; prima dei 30 controlli a 30g l'overlay non altera le previsioni.

Salute fonti: **OK** — coppie exchange/asset disponibili: 9/9. Kraken OK; Bitget OK; KuCoin OK.
Fonti ausiliarie non pesate: OKX OK; Coinbase PARZIALE. Copertura ausiliaria: 3/6.
Storage persistente: **OK** — ultimo asset: exchange_state_A.tar.gz.
<!-- EXCHANGE_MICROSTRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_microstructure -->

<!-- COMPACT_SECTION_START:exchange_signal_tracker -->
<details>
<summary><strong>🧠 Accuratezza segnali exchange</strong></summary>

<!-- EXCHANGE_SIGNAL_TRACKER_START -->
# Accuratezza dati exchange e microstruttura

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-07 | BTC | 79.707,00 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,26 | -1,97% | +0,37% |
| 2026-09-07 | DOGE | 0.08993 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,78 | -5,60% | +5,30% |
| 2026-09-07 | SOL | 105,30 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,80 | -0,56% | +4,43% |
| 2026-09-06 | BTC | 79.834,20 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 2,30 | +0,27% | +2,73% |
| 2026-09-06 | DOGE | 0.09052 | V2.1.3 | OK | 1 | 0 | 2,75 | MEDIA | 1,44 | +5,09% | +0,28% |
| 2026-09-06 | SOL | 105,78 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 5,08 | +0,13% | +3,11% |
| 2026-09-05 | BTC | 79.615,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,54 | -2,92% | +2,65% |
| 2026-09-05 | DOGE | 0.08557 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,42 | -2,90% | -0,60% |
| 2026-09-05 | SOL | 102,19 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,99 | -2,32% | -0,84% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 4 | +50,00% | +0,59% | -2,21% | +2,43% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | +66,67% | +0,53% | -2,29% | +3,66% | FEEDBACK RAPIDO |
| BTC | 14g | 2 | +50,00% | +0,85% | -2,33% | +5,63% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 3 | +66,67% | +10,89% | -4,64% | +16,94% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 9 | +44,44% | +0,77% | -0,33% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | 8 | +37,50% | +1,43% | -3,31% | +6,31% | FEEDBACK RAPIDO |
| DOGE | 7g | 8 | +50,00% | -0,83% | -4,47% | +8,09% | FEEDBACK RAPIDO |
| DOGE | 14g | 7 | +42,86% | +0,79% | -5,33% | +14,98% | FEEDBACK RAPIDO |
| DOGE | 30g | 3 | +66,67% | +10,36% | -1,38% | +41,64% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
<!-- EXCHANGE_SIGNAL_TRACKER_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_signal_tracker -->

<!-- COMPACT_SECTION_START:liquidations -->
<details>
<summary><strong>💥 Futures e liquidazioni</strong></summary>

<!-- LIQUIDATION_SUMMARY_START -->

---

# Sintesi semplice futures / liquidazioni

Report separato completo: [liquidation_report.md](liquidation_report.md)

**BTC** — BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.818 $ | +0.0053% | -5.52% | 1.16 | Misto | 1/5 |
| SOL | 105,54 $ | -0.0019% | -31.09% | 2.40 | Misto | 1/5 |
| DOGE | 0.09020 $ | +0.0100% | -14.70% | 5.12 | Rischio sotto | 2/5 |

## Come usarla insieme al frattale

- Frattale ribassista + futures con rischio sotto = prudenza alta.
- Frattale rialzista + futures con rischio sopra = segnale più interessante.
- Frattale e futures opposti = situazione sporca, meglio non forzare.
- Per posizioni a leva, il futures report serve soprattutto a capire se può arrivare una pulizia violenta prima dei 30 giorni.

<!-- LIQUIDATION_SUMMARY_END -->

</details>
<!-- COMPACT_SECTION_END:liquidations -->

<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_START -->
# Divergenze RSI multi-timeframe — diagnostica

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D    | Weekly                    | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-----------------------------------------------------|:-----------|:--------------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish invalidata                            | INVALIDATA | Conferma rialzista        | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Momentum in indebolimento, divergenza non confermata | CONTESTO   | Hidden bearish invalidata | INVALIDATA | La precedente hidden bearish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.                        |      0 |
| DOGE    | Conferma ribassista                                  | CONTESTO   | Hidden bearish            | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish invalidata                            | INVALIDATA | 79.830 $ / 66,85  | n/a                                                                 | +2,67%              | -14,09           |      0 |
| BTC     | 1W   | Conferma rialzista                                   | CONTESTO   | 79.830 $ / 58,57  | n/a                                                                 | +25,75%             | 19,73            |      0 |
| SOL     | 1D   | Momentum in indebolimento, divergenza non confermata | CONTESTO   | 105,58 $ / 67,43  | n/a                                                                 | +10,62%             | -16,88           |      0 |
| SOL     | 1W   | Hidden bearish invalidata                            | INVALIDATA | 105,58 $ / 59,92  | n/a                                                                 | +43,75%             | 21,56            |      0 |
| DOGE    | 1D   | Conferma ribassista                                  | CONTESTO   | 0.09031 $ / 63,22 | n/a                                                                 | -3,33%              | -21,50           |      0 |
| DOGE    | 1W   | Hidden bearish                                       | CONFERMATA | 0.09031 $ / 48,64 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Momentum in indebolimento, divergenza non confermata / CONTESTO**: Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish invalidata / INVALIDATA**: La precedente hidden bearish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.

### DOGE

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **9**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          30 |           1 | +100,00%      | +22,35%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           2 | +50,00%       | -8,18%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |

## Regole di prudenza

- Una divergenza **in formazione** può scomparire prima che il pivot sia confermato.
- Una divergenza weekly può anticipare il prezzo di diverse settimane.
- Prezzo in calo e RSI in calo non è bullish divergence: è conferma ribassista.
- Le divergenze restano dentro la famiglia tecnica e non vengono sommate come prova indipendente.
- Nessuna statistica di questo modulo autorizza automaticamente il trading reale.
<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_END -->

<!-- COMPACT_SECTION_START:technical_structure -->
<details>
<summary><strong>🧱 Struttura tecnica completa e Fibonacci</strong></summary>

<!-- TECHNICAL_STRUCTURE_START -->
# Report struttura tecnica

Generato: 2026-09-07 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [technical_structure_report.md](technical_structure_report.md)

Questo report aggiunge al tuo scanner una lettura classica di analisi tecnica.

Moduli inclusi:

- Struttura trend con MA20 / MA50 / MA200
- Massimi e minimi crescenti oppure decrescenti
- Doppio minimo, triplo minimo, doppio massimo, triplo massimo
- Pattern Adam and Eve Bottom / Top
- Ciclo di vita pattern: candidato, attivo, confermato recente, maturo, target raggiunto, invalidato
- Data breakout, età, target teorico, progresso e recupero della neckline
- Divergenze RSI e divergenze RSI nascoste
- Momentum MACD
- Conferma volume con OBV / CMF
- Candidato fase Wyckoff
- Fibonacci automatico su swing pivot, con lifecycle e confluenza
- Punteggio tecnico di confluenza

Regola anti-pattern-zombie: un pattern vecchio non resta indefinitamente confermato. Dopo il target vale 0; se viene recuperata stabilmente la neckline viene invalidato; se resta valido ma invecchia passa a MATURO con peso ridotto.

## Sintesi

| Asset   | Prezzo   |   Punteggio | Verdetto          | Trend           | Momentum                  | Struttura                                          |   Pattern score | Fibonacci      | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------|:----------------|:--------------------------|:---------------------------------------------------|----------------:|:---------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 79.818 $ | 7 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / NON ATTIVO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 76.248 | 81.347 |
| SOL | 105,54 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | +1 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 97,45 | 110,04 |
| DOGE | 0.09020 $ | 12 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.08028 | 0.09998 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 66.81 | -173.382 | 77.227 | 69.395 | 69.751 | 8,84% | -6,03% | 22,98% | 29,48% |
| SOL | 67.39 | -0.3077 | 98,46 | 84,37 | 82,43 | 10,75% | -10,83% | 38,92% | 62,46% |
| DOGE | 63.09 | 1e-05 | 0.08531 | 0.07641 | 0.08843 | 6,45% | -13,18% | 28,14% | 6,38% |

## Dettaglio asset

### BTC

- Prezzo: **79.818 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 6.249e+04 -> 7.625e+04. Ultimi massimi: 6.54e+04 -> 8.135e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-08-28 81.347; livello più vicino 23.6% a 75.778; stato NON ATTIVO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **76.248**
- Resistenza più vicina: **81.347**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.227 tra 2026-08-03 e 2026-08-14. Neckline stimata: 65.402. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577; progresso corrente: 454,03%. Relazione prezzo/neckline: sopra neckline.
  - neckline 65.402; target 68.577; breakout 2026-08-19 (19g); progresso 454,03%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 274,11%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (19g); progresso 274,11%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 58.076 dal 2026-06-25 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.744; progresso corrente: 146,11%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 75.744; breakout 2026-08-19 (19g); progresso 146,11%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 38,22%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 38,22%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 48 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 38,22%; prezzo sopra neckline.

### SOL

- Prezzo: **105,54 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 74.2 -> 97.45. Ultimi massimi: 77.62 -> 110.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato TENUTO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **97,45**
- Resistenza più vicina: **110,04**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 503,62%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (19g); progresso 503,62%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 333,85%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (19g); progresso 333,85%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 136,76%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (19g); progresso 136,76%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 49,29%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 49,29%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-22 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 63,84%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09020 $**
- Punteggio tecnico: **12 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06895 -> 0.08028. Ultimi massimi: 0.07286 -> 0.09998.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-09-02 0.08028; livello più vicino 23.6% a 0.08924; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.08028**
- Resistenza più vicina: **0.09998**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 297,51%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (19g); progresso 297,51%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06895 dal 2026-07-08 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07866; progresso corrente: 337,85%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07866; breakout 2026-08-19 (19g); progresso 337,85%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (19 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 297,51%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (19g); progresso 297,51%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 32,70%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 32,70%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 32,70%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-08-28 | 75.778 | 72.332 | 69.547 | 66.763 | 62.798 | 23.6% / 75.778 | NON ATTIVO | supporto tecnico | 0 |
| SOL | UP 2026-06-06 -> 2026-08-27 | 98,33 | 91,08 | 85,23 | 79,37 | 71,03 | 23.6% / 98,33 | TENUTO | supporto tecnico | +1 |
| DOGE | DOWN 2026-05-14 -> 2026-09-02 | 0.08924 | 0.09479 | 0.09927 | 0.10375 | 0.11013 | 23.6% / 0.08924 | TESTATO | nessuna confluenza indipendente | 0 |

## Stati del ciclo di vita

- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; punteggio 0.
- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; peso prudente ±1.
- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; peso massimo prudente ±2.
- **MATURO**: breakout più vecchio di 14 giorni e ancora valido; peso ridotto ±1.
- **TARGET RAGGIUNTO**: movimento teorico già sviluppato; punteggio 0.
- **INVALIDATO**: recupero stabile della neckline contro il pattern; punteggio 0.

Per evitare doppio conteggio, nel punteggio entra soltanto il miglior pattern rialzista e il miglior pattern ribassista. Doppio, triplo e Adam/Eve che descrivono la stessa struttura non vengono più sommati tutti insieme.

## Come leggere il punteggio

- Da +7 a +12: forte confluenza tecnica rialzista.
- Da +3 a +6: struttura costruttiva, ma serve ancora conferma.
- Da -2 a +2: situazione mista / neutrale.
- Da -6 a -3: struttura tecnica debole.
- Da -12 a -7: forte confluenza tecnica ribassista.

Nota importante: questo report non è una previsione da solo. È un filtro tecnico da leggere insieme a scanner frattale, market regime, futures e RSI.
<!-- TECHNICAL_STRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:technical_structure -->

<!-- COMPACT_SECTION_START:calibration_readable -->
<details>
<summary><strong>🎯 Stato leggibile accuratezza / calibrazione</strong></summary>

<!-- CALIBRATION_READABLE_START -->

---

# Stato leggibile accuratezza / calibrazione

Report dettagliati:
- [accuracy_report.md](accuracy_report.md)
- [calibration_report.md](calibration_report.md)

## Riassunto semplice

- **BTC**: 30/30 previsioni controllate su 65 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 65 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 65 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 65 | 30 | 30/30 [██████████] | 35 | ATTIVA | 2026-09-08 / tra 1 giorno |
| SOL | 65 | 30 | 30/30 [██████████] | 35 | ATTIVA | 2026-09-08 / tra 1 giorno |
| DOGE | 65 | 30 | 30/30 [██████████] | 35 | ATTIVA | 2026-09-08 / tra 1 giorno |

## Traduzione

- **0/30** significa: lo scanner sta ancora raccogliendo dati.
- **30/30** significa: la calibrazione comincia ad attivarsi.
- **60+** significa: la calibrazione diventa più solida.
- L'email non c'entra con la calibrazione: conta solo che il workflow giri e salvi il diario delle previsioni.

<!-- CALIBRATION_READABLE_END -->

</details>
<!-- COMPACT_SECTION_END:calibration_readable -->

<!-- COMPACT_SECTION_START:data_quality -->
<details>
<summary><strong>✅ Controllo qualità e coerenza dati</strong></summary>

<!-- DATA_QUALITY_COHERENCE_START -->
# Data quality / coherence check

Generato: 2026-09-07 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 2 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 79.818 $          | 79.818 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09020 $         | 0.09020 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 79.818 $          | 79.818 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09020 $         | 0.09020 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 79.818 $          | 79.818 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09020 $         | 0.09020 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 79.818 $          | 79.818 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09020 $         | 0.09020 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 79.818 $          | 79.818 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09020 $         | 0.09020 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 79.818 $          | 79.707 $        | -0,1388%     |
| Exchange Microstructure | SOL     | price             | WARN    | 105,54 $          | 105,30 $        | -0,2293%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.09020 $         | 0.08993 $       | -0,2993%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 105,54 $          | 105,54 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 105,54 $          | 105,54 $        | +0,0000%     |

## Integrità Technical / Classic Visual

- Fibonacci strutturato: **OK**
- Candidati senza falso progresso target: **OK**
- Classic Visual allineato al lifecycle Technical: **OK**

## Controllo codifica UTF-8

Nessun indicatore comune di mojibake trovato.

## File strutturati

- Snapshot condiviso completo: **OK**
- Scanner summary: **OK**
- Price coherence sync: **OK**
- Dati exchange / microstruttura: **OK**

Il workflow può continuare, ma gli avvisi sopra vanno verificati.
<!-- DATA_QUALITY_COHERENCE_END -->

</details>
<!-- COMPACT_SECTION_END:data_quality -->

<!-- SOL_SPOT_ADAPTIVE_START -->
# SOL Spot Adaptive Range — paper trading separato

Generato: 2026-09-08T04:30:35+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €45.138,06 | €27.858,61 | 167.274366 | 103.3000 | +12.85% | €4.505,48 | €124,89 | 6.48% | 64 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 97.1660 · L1 100.0696 · media 103.6991 · U1 107.3285 · U2 110.2321.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
