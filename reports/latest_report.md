<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-17 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+1**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+2**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910.
- Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,19 / 90,54, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 69,65 / 70,69 / 62,19.

### DOGE

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07286 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,29 $; upside verso EMA200 +47,60%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-17T05:32:55+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-17T05:05:27+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-17T05:05:27+00:00 | 2026-08-17T05:05:27+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-17T04:45:00+00:00 | 2026-08-17T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-17T04:00:00+00:00 | 2026-08-17T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-17T00:00:00+00:00 | 2026-08-17T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Gb20 Loss Cap V1 | BTC | 60m | LONG | 2,25 | 0,00 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Partial V1 | BTC | 60m | LONG | 2,25 | 0,00 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Be V1 | BTC | 60m | LONG | 2,25 | 0,00 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | BTC | 60m | LONG | 2,25 | 0,00 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | BTC | 60m | LONG | 2,25 | 0,00 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | BTC | 60m | LONG | 2,25 | 0,00 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | BTC | 60m | LONG | 2,25 | 0,00 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | HYPE | 60m | LONG | 6,29 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | HYPE | 60m | LONG | 6,29 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | HYPE | 60m | LONG | 6,29 | 4,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | 60m | LONG | 6,29 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | HYPE | 60m | LONG | 6,29 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | HYPE | 60m | LONG | 6,29 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 6,64 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | H | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HEMI | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | CYS | 240m | SHORT | -5,50 | 6,00 | 0,50 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 3,85 | 6,00 | 2,15 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,16 | 6,00 | 2,84 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -2,08 | 6,00 | 3,92 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -2,08 | 6,00 | 3,92 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -1,66 | 6,00 | 4,34 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | BEAT | 60m | SHORT | -8,50 | 5,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | BEAT | 60m | SHORT | -8,50 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | BEAT | 60m | SHORT | -8,50 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | BEAT | 60m | SHORT | -8,50 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Mfe Lock V1 | BEAT | 60m | SHORT | -8,50 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | BEAT | 60m | SHORT | -8,50 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Donchian 1H Gb20 120R V1 | BEAT | 60m | SHORT | -8,50 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | CYS | 60m | SHORT | -7,00 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.639,58 | -3,60% | €-108,77 | €3.000,00 | -3,63% | 6 | 41 | 34,15% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 41 | 1442 | PRIME INDICAZIONI | 100 (mancano 59) |

- Trade del Principale 4H chiusi: **41**; win rate **34,15%**; profit factor **0,72**.
- Expectancy: **€-9,22** per trade; P&L netto: **€-378,20**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.639,58 | €1.293,51 | €3.880,53 | €193,20 | €17,14 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 4 | €10.607,36 | €3.435,12 | €10.305,36 | €157,77 | €13,41 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.587,42 | €5.489,59 | €10.979,18 | €213,00 | €-67,25 |
| TEST | 1H Fast Score 6 75 V1 | 6 | €10.488,36 | €644,95 | €1.934,86 | €155,61 | €68,54 |
| TEST | Main Side Regime Guard V1 | 6 | €10.476,19 | €2.167,54 | €6.502,61 | €210,37 | €4,01 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.338,15 | €5.360,34 | €10.720,69 | €207,98 | €-65,67 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 1 | €10.337,01 | €1.540,99 | €4.622,96 | €51,78 | €-15,65 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 3 | €10.334,84 | €1.828,04 | €5.484,13 | €154,44 | €41,87 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 8 | €10.294,35 | €1.321,52 | €3.964,56 | €155,61 | €47,14 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 7 | €10.261,79 | €694,07 | €2.082,22 | €102,40 | €46,08 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.256,68 | €3.684,62 | €7.369,25 | €206,35 | €-19,15 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.250,00 | €3.323,07 | €9.969,22 | €153,68 | €-9,77 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 6 | €10.209,50 | €627,81 | €1.883,42 | €151,48 | €66,72 |
| TEST | 1H Fast V3 Cap75 V1 | 7 | €10.190,95 | €635,81 | €1.907,42 | €152,44 | €46,48 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €10.029,52 | €1.384,76 | €4.154,29 | €0,00 | €61,71 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 7 | €10.006,43 | €676,80 | €2.030,40 | €99,85 | €44,94 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.002,06 | €4.595,00 | €9.190,00 | €200,28 | €-15,80 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 5 | €9.993,14 | €4.351,33 | €13.053,98 | €200,79 | €-67,61 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.986,26 | €1.305,90 | €3.917,70 | €50,15 | €-40,71 |
| TEST | Doge Ema 1H | 1 | €9.982,18 | €1.155,63 | €3.466,88 | €49,92 | €-3,17 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 8 | €9.970,44 | €1.884,13 | €3.768,26 | €197,81 | €25,70 |
| TEST | Scanner Bottom15 Short | 8 | €9.970,44 | €1.884,13 | €3.768,26 | €197,81 | €25,70 |
| TEST | Scanner Bottom20 Short | 8 | €9.970,44 | €1.884,13 | €3.768,26 | €197,81 | €25,70 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €9.961,49 | €3.797,60 | €7.595,20 | €149,28 | €-6,69 |
| TEST | Btc Ema 4H | 1 | €9.960,58 | €1.413,45 | €2.826,90 | €49,75 | €8,53 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.949,44 | €1.259,31 | €2.518,63 | €49,91 | €-31,14 |
| TEST | Sol Donchian 4H | 1 | €9.949,37 | €1.374,20 | €2.748,40 | €49,92 | €-33,98 |
| TEST | Bilanciata 1H V3 Filtered | 8 | €9.945,49 | €1.989,23 | €5.967,70 | €198,57 | €15,42 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 6 | €9.920,92 | €1.657,67 | €3.315,33 | €149,67 | €102,90 |
| TEST | Doge Donchian 1H | 1 | €9.910,83 | €1.295,48 | €3.886,44 | €49,75 | €-38,11 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 8 | €9.902,86 | €1.892,31 | €3.784,61 | €196,94 | €24,75 |
| TEST | Btc Donchian 4H | 1 | €9.902,56 | €1.406,00 | €2.812,00 | €49,49 | €2,51 |
| TEST | Sol Donchian 1H | 1 | €9.900,68 | €1.293,08 | €3.879,24 | €49,65 | €-27,74 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 8 | €9.887,79 | €1.889,43 | €3.778,85 | €196,64 | €24,71 |
| TEST | Btc Ema 1H | 1 | €9.865,21 | €1.146,03 | €3.438,09 | €49,51 | €-35,67 |
| TEST | 1H Fast Tp2 V1 | 9 | €9.860,21 | €1.256,69 | €3.770,08 | €192,11 | €23,58 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €9.823,23 | €2.916,49 | €8.749,46 | €97,99 | €20,91 |
| TEST | Combo Mean Reversion | 3 | €9.822,98 | €5.821,37 | €11.642,74 | €0,00 | €140,30 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 8 | €9.811,70 | €1.874,89 | €3.749,77 | €195,13 | €24,52 |
| TEST | Sol Ema 4H | 1 | €9.810,65 | €1.355,04 | €2.710,08 | €49,23 | €-33,50 |
| TEST | Rapida 1H V2 | 1 | €9.809,41 | €1.454,10 | €4.362,29 | €0,00 | €40,48 |
| TEST | Combo Adaptive | 7 | €9.798,23 | €2.162,72 | €4.325,45 | €144,35 | €26,96 |
| TEST | Bilanciata 1H V1 | 10 | €9.788,03 | €687,26 | €2.061,77 | €195,76 | €64,34 |
| TEST | Benchmark Bollinger mean reversion 1H | 4 | €9.784,12 | €6.842,91 | €13.685,83 | €94,55 | €94,69 |
| TEST | Sol Ema 1H | 1 | €9.776,88 | €1.135,84 | €3.407,53 | €49,07 | €-35,48 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 9 | €9.774,73 | €1.871,51 | €5.614,54 | €107,99 | €35,38 |
| TEST | Eth Donchian 1H | 0 | €9.762,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.744,20 | €4.625,03 | €9.250,06 | €147,62 | €60,63 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.721,76 | €1.555,69 | €4.667,08 | €94,96 | €59,30 |
| TEST | Forza relativa 1H V2 | 5 | €9.721,76 | €3.369,30 | €6.738,59 | €193,92 | €26,02 |
| TEST | Rapida 1H V3 Filtered | 9 | €9.710,85 | €1.859,28 | €5.577,85 | €107,28 | €35,14 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.675,24 | €1.512,09 | €3.024,18 | €48,39 | €-2,76 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 4 | €9.658,66 | €1.367,72 | €2.735,44 | €145,82 | €30,96 |
| TEST | Combo Adaptive Long Only V1 | 4 | €9.640,30 | €3.169,93 | €6.339,86 | €98,42 | €-11,34 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 6 | €9.640,13 | €2.637,80 | €7.913,40 | €143,22 | €27,69 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 5 | €9.625,02 | €3.104,26 | €9.312,78 | €96,80 | €25,57 |
| TEST | Sol Adaptive 1H | 0 | €9.621,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €9.605,51 | €3.379,40 | €6.758,80 | €146,98 | €0,59 |
| TEST | 1H Fast V3 Nohigh V1 | 7 | €9.600,04 | €1.865,28 | €5.595,84 | €189,61 | €22,71 |
| TEST | Combo Adaptive Runner25 V1 | 8 | €9.582,90 | €1.600,78 | €3.201,56 | €140,78 | €24,87 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.548,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 4 | €9.537,17 | €1.350,52 | €2.701,03 | €143,99 | €30,57 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.535,52 | €2.291,91 | €4.583,81 | €190,23 | €24,13 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 6 | €9.521,74 | €3.419,67 | €10.259,02 | €190,97 | €27,36 |
| TEST | Combo Trend | 9 | €9.521,22 | €2.555,08 | €5.110,15 | €190,47 | €24,89 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.518,64 | €2.892,17 | €5.784,34 | €191,41 | €-38,27 |
| TEST | 1H Fast V3 No Esports V1 | 9 | €9.500,93 | €1.251,85 | €3.755,56 | €147,16 | €35,25 |
| TEST | Master Adaptive No Alt V1 | 7 | €9.418,81 | €4.614,15 | €9.228,29 | €143,23 | €-11,51 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €9.408,70 | €2.076,75 | €4.153,49 | €138,61 | €25,89 |
| TEST | 1H Balanced V3 Long Only V1 | 8 | €9.406,84 | €1.881,50 | €5.644,49 | €187,82 | €14,59 |
| TEST | Combo Adaptive Tp3 V1 | 8 | €9.403,88 | €1.570,88 | €3.141,75 | €138,15 | €24,41 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.403,12 | €2.857,07 | €5.714,15 | €189,09 | €-37,80 |
| TEST | Master Adaptive Expanded V1 | 8 | €9.393,41 | €4.076,41 | €8.152,81 | €188,49 | €-38,37 |
| TEST | Master Adaptive Gb20 Be V1 | 6 | €9.356,21 | €5.147,95 | €10.295,89 | €185,07 | €66,27 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.355,32 | €2.842,55 | €5.685,10 | €188,13 | €-37,61 |
| TEST | Master Adaptive Gb20 Partial V1 | 6 | €9.346,26 | €5.142,47 | €10.284,95 | €184,88 | €66,20 |
| TEST | Master Adaptive V1 | 6 | €9.310,11 | €5.122,58 | €10.245,16 | €184,16 | €65,95 |
| TEST | Forza relativa 1H V1 | 7 | €9.297,36 | €2.872,26 | €5.744,52 | €185,95 | €22,02 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €9.283,78 | €3.252,19 | €6.504,38 | €141,63 | €0,57 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €9.278,35 | €3.250,28 | €6.500,57 | €141,54 | €0,57 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.267,64 | €1.815,27 | €5.445,81 | €185,74 | €-18,93 |
| TEST | Scanner Top10 Long | 5 | €9.213,23 | €4.018,03 | €8.036,07 | €184,49 | €-14,55 |
| TEST | Scanner Top15 Long | 5 | €9.213,23 | €4.018,03 | €8.036,07 | €184,49 | €-14,55 |
| TEST | Scanner Top20 Long | 5 | €9.213,23 | €4.018,03 | €8.036,07 | €184,49 | €-14,55 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.212,74 | €4.183,19 | €8.366,38 | €181,68 | €-4,39 |
| TEST | Benchmark trend following EMA 1H | 10 | €9.188,06 | €3.803,82 | €7.607,65 | €183,15 | €-18,43 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.186,41 | €5.054,52 | €10.109,04 | €181,71 | €65,07 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.184,43 | €2.790,63 | €5.581,25 | €184,69 | €-36,92 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 5 | €9.179,02 | €3.229,36 | €6.458,71 | €140,45 | €0,56 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.164,07 | €2.955,59 | €8.866,78 | €92,17 | €24,35 |
| TEST | Combo Scanner | 5 | €9.109,83 | €4.368,98 | €8.737,97 | €182,54 | €-14,53 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 3 | €9.097,53 | €5.447,73 | €10.895,46 | €117,67 | €75,60 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.003,77 | €3.167,70 | €6.335,40 | €137,77 | €0,55 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.895,46 | €3.297,63 | €6.595,26 | €178,31 | €-5,63 |
| TEST | Combo Adaptive Mfe Trail | 5 | €8.817,23 | €3.239,33 | €6.478,66 | €132,86 | €-0,84 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.639,58 | €-378,20 | 41 | 41 | 34,15% | 0,72 | €-9,22 | 6,36% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.607,36 | €602,09 | 68 | 68 | 51,47% | 1,42 | €8,85 | 3,35% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.587,42 | €659,79 | 61 | 61 | 47,54% | 1,46 | €10,82 | 3,63% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.488,36 | €357,44 | 118 | 117 | 44,07% | 1,13 | €3,03 | 4,89% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.476,19 | €470,38 | 21 | 21 | 52,38% | 2,09 | €22,40 | 2,40% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.338,15 | €408,82 | 29 | 29 | 44,83% | 1,71 | €14,10 | 3,63% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.337,01 | €355,43 | 33 | 33 | 48,48% | 1,52 | €10,77 | 3,55% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.334,84 | €296,26 | 31 | 31 | 51,61% | 1,36 | €9,56 | 2,31% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.294,35 | €245,07 | 113 | 113 | 42,48% | 1,12 | €2,17 | 3,64% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.261,79 | €219,82 | 108 | 108 | 43,52% | 1,09 | €2,04 | 6,52% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.256,68 | €279,20 | 44 | 44 | 52,27% | 1,35 | €6,35 | 2,94% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.250,00 | €268,51 | 53 | 53 | 47,17% | 1,24 | €5,07 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.209,50 | €82,06 | 76 | 75 | 47,37% | 1,04 | €1,08 | 5,23% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.190,95 | €149,56 | 108 | 108 | 42,59% | 1,06 | €1,38 | 6,72% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.029,52 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.006,43 | €-34,49 | 72 | 72 | 41,67% | 0,98 | €-0,48 | 6,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.002,06 | €23,45 | 72 | 72 | 43,06% | 1,01 | €0,33 | 8,85% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.993,14 | €65,90 | 8 | 8 | 37,50% | 1,47 | €8,24 | 1,59% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.986,26 | €29,32 | 6 | 6 | 66,67% | 1,27 | €4,89 | 1,49% |
| TEST | Doge Ema 1H | Trend following EMA | €9.982,18 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.970,44 | €-48,67 | 52 | 52 | 34,62% | 0,95 | €-0,94 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.970,44 | €-48,67 | 52 | 52 | 34,62% | 0,95 | €-0,94 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.970,44 | €-48,67 | 52 | 52 | 34,62% | 0,95 | €-0,94 | 5,27% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.961,49 | €-29,86 | 55 | 55 | 43,64% | 0,97 | €-0,54 | 6,65% |
| TEST | Btc Ema 4H | Trend following EMA | €9.960,58 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.949,44 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.949,37 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.945,49 | €-66,36 | 91 | 91 | 37,36% | 0,97 | €-0,73 | 7,10% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Ampia 4H | Confluenza trend | €9.920,92 | €-182,43 | 36 | 36 | 22,22% | 0,81 | €-5,07 | 4,45% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.910,83 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 2,06% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.902,86 | €-115,34 | 43 | 43 | 34,88% | 0,87 | €-2,68 | 5,27% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.902,56 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.900,68 | €-69,14 | 7 | 7 | 42,86% | 0,63 | €-9,88 | 2,51% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.887,79 | €-130,37 | 44 | 44 | 34,09% | 0,84 | €-2,96 | 5,27% |
| TEST | Btc Ema 1H | Trend following EMA | €9.865,21 | €-98,30 | 8 | 8 | 37,50% | 0,63 | €-12,29 | 1,72% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.860,21 | €-215,71 | 127 | 127 | 35,43% | 0,92 | €-1,70 | 3,95% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.823,23 | €-192,20 | 36 | 36 | 44,44% | 0,79 | €-5,34 | 4,50% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.822,98 | €-308,68 | 30 | 30 | 36,67% | 0,70 | €-10,29 | 5,09% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.811,70 | €-206,32 | 71 | 71 | 33,80% | 0,85 | €-2,91 | 6,41% |
| TEST | Sol Ema 4H | Trend following EMA | €9.810,65 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,93% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.809,41 | €-228,46 | 30 | 27 | 36,67% | 0,72 | €-7,62 | 3,89% |
| TEST | Combo Adaptive | Combo Adaptive | €9.798,23 | €-225,58 | 72 | 72 | 36,11% | 0,83 | €-3,13 | 5,40% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.788,03 | €-275,20 | 102 | 102 | 40,20% | 0,86 | €-2,70 | 8,81% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.784,12 | €-301,34 | 69 | 69 | 43,48% | 0,83 | €-4,37 | 6,53% |
| TEST | Sol Ema 1H | Trend following EMA | €9.776,88 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 3,07% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.774,73 | €-264,17 | 92 | 92 | 45,65% | 0,85 | €-2,87 | 7,17% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.762,69 | €-237,31 | 7 | 7 | 14,29% | 0,28 | €-33,90 | 2,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.744,20 | €-309,48 | 30 | 30 | 36,67% | 0,60 | €-10,32 | 3,91% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.721,76 | €-332,08 | 66 | 60 | 42,42% | 0,79 | €-5,03 | 6,62% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.721,76 | €-299,45 | 72 | 69 | 38,89% | 0,87 | €-4,16 | 8,11% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.710,85 | €-327,80 | 136 | 136 | 37,50% | 0,89 | €-2,41 | 7,14% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.675,24 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.658,66 | €-373,59 | 21 | 21 | 33,33% | 0,51 | €-17,79 | 4,21% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.640,30 | €-344,55 | 44 | 44 | 34,09% | 0,71 | €-7,83 | 5,16% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.640,13 | €-382,69 | 67 | 67 | 40,30% | 0,80 | €-5,71 | 5,23% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.625,02 | €-396,84 | 62 | 62 | 35,48% | 0,75 | €-6,40 | 8,59% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.621,05 | €-378,95 | 10 | 10 | 20,00% | 0,15 | €-37,89 | 4,47% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.605,51 | €-391,03 | 62 | 62 | 33,87% | 0,77 | €-6,31 | 9,76% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.600,04 | €-419,19 | 98 | 98 | 41,84% | 0,83 | €-4,28 | 6,10% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.582,90 | €-439,52 | 76 | 76 | 31,58% | 0,72 | €-5,78 | 6,85% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Eth Ema 1H | Trend following EMA | €9.548,70 | €-451,30 | 11 | 11 | 18,18% | 0,11 | €-41,03 | 4,51% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.537,17 | €-494,67 | 21 | 21 | 23,81% | 0,36 | €-23,56 | 5,41% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.535,52 | €-485,91 | 40 | 40 | 27,50% | 0,54 | €-12,15 | 7,10% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.521,74 | €-562,35 | 73 | 73 | 43,84% | 0,75 | €-7,70 | 6,85% |
| TEST | Combo Trend | Combo Trend | €9.521,22 | €-501,24 | 100 | 100 | 33,00% | 0,81 | €-5,01 | 9,82% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.518,64 | €-439,52 | 43 | 43 | 34,88% | 0,70 | €-10,22 | 7,18% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.500,93 | €-589,70 | 110 | 110 | 37,27% | 0,76 | €-5,36 | 7,03% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.418,81 | €-563,89 | 45 | 45 | 28,89% | 0,66 | €-12,53 | 6,80% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.408,70 | €-614,15 | 73 | 73 | 34,25% | 0,59 | €-8,41 | 6,20% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.406,84 | €-604,36 | 47 | 47 | 31,91% | 0,44 | €-12,86 | 6,83% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.403,88 | €-618,12 | 57 | 57 | 29,82% | 0,52 | €-10,84 | 6,85% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.403,12 | €-555,54 | 48 | 48 | 31,25% | 0,65 | €-11,57 | 6,77% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.393,41 | €-563,14 | 46 | 46 | 30,43% | 0,65 | €-12,24 | 6,33% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.356,21 | €-703,63 | 43 | 43 | 20,93% | 0,49 | €-16,36 | 8,39% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.355,32 | €-603,55 | 58 | 58 | 36,21% | 0,66 | €-10,41 | 6,45% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.346,26 | €-713,51 | 38 | 38 | 26,32% | 0,46 | €-18,78 | 7,98% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.310,11 | €-749,44 | 40 | 40 | 25,00% | 0,50 | €-18,74 | 7,80% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.297,36 | €-721,88 | 83 | 83 | 28,92% | 0,64 | €-8,70 | 9,65% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.283,78 | €-712,89 | 47 | 47 | 27,66% | 0,53 | €-15,17 | 10,10% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.278,35 | €-718,32 | 51 | 51 | 29,41% | 0,53 | €-14,08 | 10,40% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.267,64 | €-713,46 | 45 | 45 | 31,11% | 0,54 | €-15,85 | 9,05% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.213,23 | €-768,11 | 44 | 44 | 34,09% | 0,47 | €-17,46 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.213,23 | €-768,11 | 44 | 44 | 34,09% | 0,47 | €-17,46 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.213,23 | €-768,11 | 44 | 44 | 34,09% | 0,47 | €-17,46 | 10,31% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.212,74 | €-781,07 | 40 | 40 | 22,50% | 0,50 | €-19,53 | 8,14% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.188,06 | €-789,59 | 68 | 68 | 26,47% | 0,54 | €-11,61 | 8,92% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.186,41 | €-872,34 | 75 | 75 | 46,67% | 0,49 | €-11,63 | 9,02% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.184,43 | €-775,19 | 65 | 65 | 35,38% | 0,60 | €-11,93 | 8,22% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.179,02 | €-817,66 | 43 | 43 | 27,91% | 0,42 | €-19,02 | 10,22% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.164,07 | €-856,75 | 82 | 82 | 29,27% | 0,62 | €-10,45 | 10,56% |
| TEST | Combo Scanner | Combo Scanner | €9.109,83 | €-873,51 | 67 | 67 | 32,84% | 0,57 | €-13,04 | 10,79% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.097,53 | €-971,54 | 32 | 32 | 15,62% | 0,30 | €-30,36 | 11,09% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.003,77 | €-992,98 | 55 | 55 | 29,09% | 0,34 | €-18,05 | 10,78% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.895,46 | €-1.094,57 | 45 | 45 | 24,44% | 0,48 | €-24,32 | 11,51% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.817,23 | €-1.177,44 | 85 | 85 | 30,59% | 0,42 | €-13,85 | 11,85% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00217 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €17,54 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63487,50000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €-0,09 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06958 | 0,07020 | 0,07069 | 0,09242 | 0,06735 | €11,27 | €33,82 | €0,54 | €-0,30 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,07020 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €-0,31 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 1,00217 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €0,13 |
| Bilanciata 1H V1 | TUT | SHORT | Confluenza trend | 60m | 3,0x | 0,03281 | 0,03281 | 0,03675 | 0,04359 | 0,02494 | €125,03 | €375,08 | €45,01 | €-0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 487,26746 | 491,71000 | 494,28412 | 647,25361 | 473,23416 | €24,62 | €73,85 | €1,06 | €-0,67 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63004,39660 | 63487,50000 | 63911,65991 | 83690,84015 | 61189,86998 | €18,78 | €56,35 | €0,81 | €-0,43 |
| Bilanciata 1H V1 | ACE | SHORT | Confluenza trend | 60m | 3,0x | 0,14042 | 0,14042 | 0,15727 | 0,18652 | 0,10672 | €129,09 | €387,27 | €46,47 | €-0,00 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,67910 | 0,85472 | 1,01371 | 0,57999 | €135,05 | €405,16 | €48,62 | €44,62 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 0,36815 | 0,34829 | 0,41233 | 0,48902 | 0,27979 | €135,05 | €405,14 | €48,62 | €21,85 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1889,17209 | 1901,13000 | 1916,37617 | 2509,45026 | 1834,76393 | €43,74 | €131,21 | €1,89 | €-0,83 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 58,85077 | 58,83900 | 58,00332 | 39,52810 | 60,54567 | €30,15 | €90,44 | €1,30 | €-0,02 |
| 1H Balanced Long No Rhv V1 | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1182,39901 | 1155,07338 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | SNDK | LONG | Confluenza trend | 60m | 3,0x | 1632,05865 | 1632,05865 | 1586,54905 | 1096,19939 | 1723,07784 | €570,53 | €1.711,58 | €47,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01002 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €-18,93 |
| 1H Balanced Short Trend Down Strict V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,07020 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €-3,17 |
| 1H Balanced Short Trend Down Strict V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 74,71805 | 75,49600 | 75,79399 | 99,25048 | 72,56617 | €1.131,56 | €3.394,68 | €48,88 | €-35,34 |
| 1H Balanced Short Trend Down Strict V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 62929,63156 | 63487,50000 | 63835,81825 | 83591,52725 | 61117,25817 | €34,60 | €103,79 | €1,49 | €-0,92 |
| 1H Balanced Short Trend Down Strict V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 0,99419 | 1,00217 | 1,00851 | 1,32062 | 0,96556 | €1.170,75 | €3.512,25 | €50,58 | €-28,18 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 1,00217 | 1,00538 | 1,33548 | 0,97642 | €37,09 | €111,28 | €0,00 | €0,36 |
| Bilanciata 1H V2 | ACE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,11641 | €136,55 | €409,66 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01002 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €-2,18 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 58,29796 | 58,83900 | 58,52114 | 39,15679 | 59,97694 | €1.118,28 | €3.354,85 | €0,00 | €31,14 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,67910 | 0,82506 | 0,97853 | 0,55986 | €127,95 | €383,85 | €46,06 | €29,99 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07020 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,35 |
| Bilanciata 1H V3 Filtered | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €457,69 | €1.373,07 | €49,01 | €0,00 |
| Bilanciata 1H V3 Filtered | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €127,78 | €383,34 | €46,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 1,00217 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €-0,47 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 62892,88891 | 63487,50000 | 63798,54651 | 83542,72076 | 61081,57371 | €40,14 | €120,43 | €1,73 | €-1,14 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,36815 | 0,34829 | 0,41233 | 0,48902 | 0,27979 | €134,23 | €402,68 | €48,32 | €21,72 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,06542 | 39,57042 | 60,61050 | €1.138,79 | €3.416,38 | €49,20 | €-4,34 |
| 1H Fast Score 6 75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €32,86 | €98,57 | €0,00 | €0,00 |
| 1H Fast Score 6 75 V1 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €144,97 | €434,90 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €146,27 | €438,81 | €52,66 | €-0,00 |
| 1H Fast Score 6 75 V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,77873 | 0,67910 | 0,76350 | 1,03442 | 0,63856 | €144,96 | €434,87 | €0,00 | €55,64 |
| 1H Fast Score 6 75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,35940 | 0,34829 | 0,40201 | 0,47741 | 0,29550 | €139,31 | €417,92 | €49,54 | €12,92 |
| 1H Fast Score 6 75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,85077 | 58,83900 | 58,19164 | 39,52810 | 59,83946 | €36,60 | €109,79 | €1,23 | €-0,02 |
| 1H Fast Score 6 75 No Trend Up V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €31,98 | €95,95 | €0,00 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €141,11 | €423,34 | €50,80 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €142,38 | €427,15 | €51,26 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,77873 | 0,67910 | 0,76350 | 1,03442 | 0,63856 | €141,10 | €423,30 | €0,00 | €54,16 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,35940 | 0,34829 | 0,40201 | 0,47741 | 0,29550 | €135,60 | €406,81 | €48,22 | €12,58 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,85077 | 58,83900 | 58,19164 | 39,52810 | 59,83946 | €35,62 | €106,87 | €1,20 | €-0,02 |
| 1H Fast Score 6 75 Range Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,36742 | 0,34829 | 0,40862 | 0,48806 | 0,30561 | €153,02 | €459,07 | €51,48 | €23,90 |
| 1H Fast Score 6 75 Range Only V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,67910 | 0,82506 | 0,97853 | 0,60406 | €143,00 | €428,99 | €51,48 | €33,52 |
| 1H Fast Score 6 75 Range Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 59,03881 | 58,83900 | 58,37757 | 39,65440 | 60,03066 | €1.532,02 | €4.596,07 | €51,48 | €-15,55 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99774 | 1,00217 | 1,00892 | 1,32533 | 0,98098 | €1.572,34 | €4.717,02 | €52,83 | €-20,94 |
| 1H Fast Score 6 75 Cost Aware V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €147,46 | €442,37 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,74855 | 0,67910 | 0,83838 | 0,99432 | 0,61381 | €144,91 | €434,74 | €52,17 | €40,33 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €1.570,41 | €4.711,24 | €52,77 | €-5,98 |
| 1H Fast Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €20,17 | €60,51 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €140,04 | €420,12 | €50,41 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €138,95 | €416,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,15 | €75,44 | €0,84 | €0,46 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01002 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €-0,69 |
| 1H Fast Nohigh Cap75 V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,76314 | 0,67910 | 0,75343 | 1,01371 | 0,62578 | €140,65 | €421,95 | €0,00 | €46,47 |
| 1H Fast Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €39,47 | €118,41 | €1,33 | €-0,15 |
| 1H Fast No Pepe V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €771,03 | €2.313,08 | €50,17 | €0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €142,21 | €426,63 | €51,20 | €-0,00 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1191,94474 | 1191,94474 | 1171,66933 | 800,58955 | 1222,35785 | €47,86 | €143,59 | €2,44 | €0,00 |
| 1H Fast No Pepe V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06539 | 0,06539 | 0,05878 | 0,04392 | 0,07530 | €166,06 | €498,19 | €50,35 | €0,00 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €30,07 | €90,22 | €1,01 | €0,55 |
| 1H Fast No Pepe V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,76835 | 0,67910 | 0,76767 | 1,02062 | 0,63004 | €133,17 | €399,52 | €0,00 | €46,41 |
| 1H Fast No Pepe V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99419 | 1,00217 | 1,00533 | 1,32062 | 0,97749 | €13,10 | €39,31 | €0,44 | €-0,32 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,29796 | 58,83900 | 58,59340 | 39,15679 | 59,27736 | €18,01 | €54,02 | €0,00 | €0,50 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03778 | 0,03778 | 0,03531 | 0,05019 | 0,02871 | €9,36 | €28,07 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1182,39901 | 1182,39901 | 1161,14575 | 794,17800 | 1224,90555 | €15,88 | €47,65 | €0,86 | €0,00 |
| 1H Fast Tp2 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,91916 | 1632,91916 | 1597,68836 | 1096,77737 | 1703,38077 | €753,45 | €2.260,36 | €48,77 | €0,00 |
| 1H Fast Tp2 V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,08248 | €168,46 | €505,38 | €48,56 | €0,00 |
| 1H Fast Tp2 V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,10258 | €139,64 | €418,91 | €50,27 | €-0,00 |
| 1H Fast Tp2 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 62929,63156 | 63487,50000 | 63634,44343 | 83591,52725 | 61520,00781 | €21,81 | €65,43 | €0,73 | €-0,58 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,37290 | 0,34829 | 0,41764 | 0,49533 | 0,28340 | €118,31 | €354,93 | €42,59 | €23,42 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1931,97597 | €9,62 | €28,86 | €0,32 | €0,18 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,29796 | 58,83900 | 58,59340 | 39,15679 | 59,60383 | €20,17 | €60,50 | €0,00 | €0,56 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 58,29796 | 58,83900 | 58,59340 | 39,15679 | 59,27736 | €1.454,10 | €4.362,29 | €0,00 | €40,48 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €776,07 | €2.328,22 | €0,00 | €0,00 |
| Rapida 1H V3 Filtered | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €752,55 | €2.257,65 | €48,96 | €0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €136,31 | €408,92 | €49,07 | €-0,00 |
| Rapida 1H V3 Filtered | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,48 | €49,45 | €4,75 | €0,00 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,31 | €75,93 | €0,85 | €0,46 |
| Rapida 1H V3 Filtered | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99419 | 1,00217 | 1,00533 | 1,32062 | 0,97749 | €15,63 | €46,89 | €0,53 | €-0,38 |
| Rapida 1H V3 Filtered | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,67910 | 0,75343 | 1,01371 | 0,62578 | €110,76 | €332,29 | €0,00 | €36,59 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01002 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €-1,39 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 59,03881 | 58,83900 | 58,37757 | 39,65440 | 60,03066 | €14,35 | €43,06 | €0,48 | €-0,15 |
| 1H Fast V3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €17,79 | €53,38 | €0,00 | €0,00 |
| 1H Fast V3 Cap75 V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03283 | 0,03283 | 0,03677 | 0,04361 | 0,02692 | €139,04 | €417,11 | €50,05 | €-0,00 |
| 1H Fast V3 Cap75 V1 | APR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €136,16 | €408,49 | €49,02 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €142,42 | €427,26 | €51,27 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €53,48 | €160,43 | €1,80 | €0,97 |
| 1H Fast V3 Cap75 V1 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,67910 | 0,75343 | 1,01371 | 0,62578 | €138,02 | €414,05 | €0,00 | €45,60 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 59,03881 | 58,83900 | 58,37757 | 39,65440 | 60,03066 | €8,89 | €26,68 | €0,30 | €-0,09 |
| 1H Fast V3 Nohigh V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €11,94 | €35,81 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,88 | €77,64 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €135,40 | €406,20 | €48,74 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.284,05 | €3.852,15 | €43,14 | €23,41 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01002 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €-25,29 |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,36968 | 0,34829 | 0,41111 | 0,49106 | 0,30753 | €142,81 | €428,42 | €48,02 | €24,79 |
| 1H Fast V3 Nohigh V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €50,08 | €150,25 | €1,68 | €-0,19 |
| 1H Fast V3 Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €757,07 | €2.271,20 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €683,99 | €2.051,96 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €135,06 | €405,19 | €45,82 | €0,00 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.343,18 | €4.029,53 | €45,13 | €24,48 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €36,30 | €108,90 | €1,22 | €-0,14 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €806,60 | €2.419,81 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,80 | €77,41 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €144,03 | €432,09 | €48,86 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.430,90 | €4.292,71 | €48,08 | €26,08 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,01002 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €1,73 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €33,83 | €101,48 | €1,14 | €-0,13 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €42,36 | €127,08 | €0,00 | €0,00 |
| 1H Fast V3 No Esports V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €736,66 | €2.209,98 | €47,93 | €0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €133,42 | €400,27 | €48,03 | €-0,00 |
| 1H Fast V3 No Esports V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €163,10 | €489,29 | €47,02 | €0,00 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,33 | €75,98 | €0,85 | €0,46 |
| 1H Fast V3 No Esports V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99419 | 1,00217 | 1,00533 | 1,32062 | 0,97749 | €15,56 | €46,67 | €0,52 | €-0,37 |
| 1H Fast V3 No Esports V1 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,67910 | 0,75343 | 1,01371 | 0,62578 | €110,59 | €331,77 | €0,00 | €36,54 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01002 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €-1,22 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 59,03881 | 58,83900 | 58,37757 | 39,65440 | 60,03066 | €14,44 | €43,32 | €0,49 | €-0,15 |
| 1H Fast V3 No Esports Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €795,15 | €2.385,44 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €718,39 | €2.155,18 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €141,86 | €425,58 | €48,12 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.410,74 | €4.232,21 | €47,40 | €25,72 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €38,12 | €114,37 | €1,28 | €-0,15 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €781,18 | €2.343,53 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €757,50 | €2.272,50 | €49,29 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €137,20 | €411,61 | €49,39 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,59 | €49,77 | €4,78 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,48 | €76,43 | €0,86 | €0,46 |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99419 | 1,00217 | 1,00533 | 1,32062 | 0,97749 | €15,73 | €47,20 | €0,53 | €-0,38 |
| 1H Fast V3 No Esports Mfe Lock V1 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,67910 | 0,75343 | 1,01371 | 0,62578 | €111,49 | €334,48 | €0,00 | €36,83 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01002 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €-1,40 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 59,03881 | 58,83900 | 58,37757 | 39,65440 | 60,03066 | €14,45 | €43,35 | €0,49 | €-0,15 |
| 1H Fast V3 No Esports Stress Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.453,04 | €4.359,11 | €48,82 | €26,49 |
| 1H Fast V3 No Esports Stress Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €1.463,45 | €4.390,35 | €49,17 | €-5,57 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1142,02581 | 782,71250 | 1200,28321 | €802,37 | €2.407,11 | €48,13 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1582,80136 | 1087,36168 | 1673,04985 | €25,50 | €76,51 | €1,71 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 9,38563 | 9,38563 | 9,22869 | 6,30401 | 9,62103 | €949,50 | €2.848,50 | €47,63 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.413,33 | €4.239,98 | €47,49 | €25,76 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,01002 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €1,72 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €33,51 | €100,52 | €1,13 | €-0,13 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00217 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €13,66 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 63487,50000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €-0,16 |
| Ampia 4H | BEAT | SHORT | Confluenza trend | 240m | 2,0x | 0,44779 | 0,34829 | 0,44779 | 0,66945 | 0,29733 | €202,71 | €405,42 | €0,00 | €90,09 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,07020 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-0,68 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €-0,00 |
| Forza relativa 1H V1 | SKHYNIX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €79,48 | €158,95 | €3,52 | €0,00 |
| Forza relativa 1H V1 | TUT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,03281 | 0,03281 | 0,03675 | 0,04906 | 0,02415 | €186,76 | €373,52 | €44,82 | €-0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,27445 | €166,87 | €333,74 | €40,05 | €22,02 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 58,85077 | 58,83900 | 58,00332 | 29,71964 | 60,71516 | €15,19 | €30,38 | €0,44 | €-0,01 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €1,08 | €0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02493 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,27445 | €197,18 | €394,37 | €47,32 | €26,02 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07020 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-32,74 |
| Benchmark Donchian breakout 1H | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €858,65 | €1.717,31 | €52,93 | €0,00 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,49600 | 75,91354 | 111,70349 | 71,72933 | €1.657,45 | €3.314,90 | €53,04 | €-34,51 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07020 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-31,97 |
| Donchian 1H Gb20 120R V1 | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €838,44 | €1.676,87 | €51,68 | €0,00 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,49600 | 75,91354 | 111,70349 | 71,72933 | €1.618,43 | €3.236,85 | €51,79 | €-33,70 |
| Benchmark Bollinger mean reversion 1H | SNDK | SHORT | Bollinger mean reversion | 60m | 2,0x | 1630,10135 | 1630,10135 | 1667,98054 | 2437,00152 | 1573,28257 | €1.043,30 | €2.086,60 | €48,49 | €-0,00 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 74,39088 | 75,49600 | 75,22660 | 37,56739 | 75,72991 | €1.939,28 | €3.878,55 | €0,00 | €57,62 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 0,99354 | 1,00217 | 0,99765 | 0,50174 | 1,01142 | €1.940,88 | €3.881,75 | €0,00 | €33,73 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 58,89022 | 58,83900 | 59,59690 | 88,04088 | 57,83020 | €1.919,46 | €3.838,92 | €46,07 | €3,34 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07020 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €-0,04 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,71 | €0,00 |
| Benchmark trend following EMA 1H | SNDK | LONG | Trend following EMA | 60m | 2,0x | 1632,05865 | 1632,05865 | 1581,49243 | 824,18962 | 1743,30434 | €724,64 | €1.449,29 | €44,90 | €0,00 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 62898,88771 | 63487,50000 | 63905,26991 | 94033,83712 | 60684,84686 | €27,47 | €54,94 | €0,88 | €-0,51 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 1,00217 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €-0,16 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 57,44244 | 58,83900 | 58,53616 | 29,00843 | 59,46442 | €13,41 | €26,81 | €0,00 | €0,65 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 74,94501 | 75,49600 | 76,14413 | 112,04279 | 72,30694 | €1.248,89 | €2.497,78 | €39,96 | €-18,36 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €13,45 | €26,90 | €0,77 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.146,19 | €2.292,38 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €-4,26 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 59,03881 | 58,83900 | 58,18865 | 29,81460 | 60,73912 | €1.703,71 | €3.407,43 | €49,07 | €-11,53 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €-0,00 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00217 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €0,16 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €200,12 | €400,25 | €48,03 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,49600 | 75,79399 | 111,70349 | 72,56617 | €21,64 | €43,28 | €0,62 | €-0,45 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,07020 | 0,07049 | 0,10388 | 0,06749 | €69,53 | €139,06 | €2,00 | €-1,42 |
| Scanner Bottom 5 Short 1H | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €204,10 | €408,20 | €48,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €203,89 | €407,78 | €48,93 | €26,91 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63487,50000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,05 | €90,11 | €1,30 | €-0,67 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top10 Long | SNDK | LONG | Scanner Top10 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €-3,93 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 59,03881 | 58,83900 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €-10,63 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 1,00217 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,16 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 75,16396 | 75,49600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,15 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06949 | 0,07020 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-1,21 |
| Scanner Bottom10 Short | ACE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €207,19 | €414,39 | €49,73 | €27,34 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 63018,79372 | 63487,50000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,44 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top15 Long | SNDK | LONG | Scanner Top15 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €-3,93 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 59,03881 | 58,83900 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €-10,63 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 1,00217 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,16 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 75,16396 | 75,49600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,15 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06949 | 0,07020 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-1,21 |
| Scanner Bottom15 Short | ACE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €207,19 | €414,39 | €49,73 | €27,34 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 63018,79372 | 63487,50000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,44 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top20 Long | SNDK | LONG | Scanner Top20 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €-3,93 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 59,03881 | 58,83900 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €-10,63 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 1,00217 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,16 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 75,16396 | 75,49600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,15 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06949 | 0,07020 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-1,21 |
| Scanner Bottom20 Short | ACE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €207,19 | €414,39 | €49,73 | €27,34 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 63018,79372 | 63487,50000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,44 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,84 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €22,01 | €44,02 | €1,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €200,15 | €400,30 | €48,04 | €-30,37 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,83900 | 57,45847 | 29,44047 | 60,14484 | €1.668,18 | €3.336,37 | €48,04 | €30,96 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,79 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €20,63 | €41,26 | €1,12 | €0,00 |
| Scanner Top5 Btc Mfe V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €187,61 | €375,22 | €45,03 | €-28,47 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,83900 | 57,45847 | 29,44047 | 60,14484 | €1.563,68 | €3.127,36 | €45,03 | €29,02 |
| Scanner Top5 Btc Guard V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €2,48 | €0,00 |
| Scanner Top5 Btc Guard V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €890,44 | €1.780,87 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €-4,11 |
| Scanner Top5 Btc Guard V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €196,57 | €393,15 | €47,18 | €-29,83 |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 58,83900 | 58,06542 | 29,75146 | 60,78017 | €1.519,74 | €3.039,48 | €43,77 | €-3,86 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,80 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €21,03 | €42,07 | €1,14 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €191,26 | €382,53 | €45,90 | €-29,03 |
| Scanner Top5 Btc Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,83900 | 57,45847 | 29,44047 | 60,14484 | €1.594,12 | €3.188,23 | €45,91 | €29,59 |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €2,42 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €869,73 | €1.739,45 | €47,32 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €-4,02 |
| Scanner Top5 Btc Guard Mfe V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €192,00 | €384,00 | €46,08 | €-29,14 |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 58,83900 | 58,06542 | 29,75146 | 60,78017 | €1.484,39 | €2.968,79 | €42,75 | €-3,77 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €2,51 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €901,37 | €1.802,75 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €-4,16 |
| Scanner Top5 Btc Guard Btc Le3 V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €198,99 | €397,98 | €47,76 | €-30,20 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 58,83900 | 58,06542 | 29,75146 | 60,78017 | €1.538,41 | €3.076,82 | €44,31 | €-3,91 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €2,46 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €885,91 | €1.771,82 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01002 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €-4,09 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €195,57 | €391,15 | €46,94 | €-29,68 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 58,83900 | 58,06542 | 29,75146 | 60,78017 | €1.512,01 | €3.024,03 | €43,55 | €-3,84 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,81 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,67 | €0,92 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,19042 | €193,33 | €386,66 | €46,40 | €-29,34 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,83900 | 57,45847 | 29,44047 | 60,81643 | €1.611,37 | €3.222,73 | €46,41 | €29,91 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,81 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,69 | €0,92 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,19042 | €193,45 | €386,89 | €46,43 | €-29,36 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,83900 | 57,45847 | 29,44047 | 60,81643 | €1.612,31 | €3.224,62 | €46,43 | €29,93 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07020 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €-2,76 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07020 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €-0,05 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,71 | €0,00 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1618,90076 | 1618,90076 | 1567,33019 | 817,54488 | 1732,35601 | €12,85 | €25,70 | €0,82 | €0,00 |
| Combo Trend | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02351 | €194,61 | €389,21 | €46,71 | €-0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,27445 | €193,08 | €386,15 | €46,34 | €25,48 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 58,85077 | 58,83900 | 57,90916 | 29,71964 | 60,92231 | €1.350,47 | €2.700,94 | €43,22 | €-0,54 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62826,12271 | 63487,50000 | 63232,34348 | 31727,19197 | 64032,38427 | €1.946,42 | €3.892,84 | €0,00 | €40,98 |
| Combo Mean Reversion | SOL | LONG | Combo Mean Reversion | 60m | 2,0x | 74,39088 | 75,49600 | 75,22660 | 37,56739 | 75,81918 | €1.937,79 | €3.875,57 | €0,00 | €57,57 |
| Combo Mean Reversion | DOGE | LONG | Combo Mean Reversion | 60m | 2,0x | 0,06945 | 0,07020 | 0,06998 | 0,03507 | 0,07079 | €1.937,17 | €3.874,33 | €0,00 | €41,75 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,07020 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €-13,62 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1721,01048 | €20,29 | €40,58 | €1,16 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €1.034,30 | €2.068,59 | €45,78 | €0,00 |
| Combo Scanner | H | LONG | Combo Scanner | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17698 | €190,03 | €380,07 | €45,61 | €-28,84 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 58,29796 | 58,83900 | 57,45847 | 29,44047 | 60,14484 | €1.504,84 | €3.009,69 | €43,34 | €27,93 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €-0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07020 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €-0,06 |
| Combo Adaptive | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,00 | €0,00 |
| Combo Adaptive | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €686,66 | €1.373,32 | €49,73 | €0,00 |
| Combo Adaptive | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €194,92 | €389,84 | €46,78 | €25,72 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 58,29796 | 58,83900 | 58,55727 | 29,44047 | 59,97694 | €69,65 | €139,29 | €0,00 | €1,29 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €-0,00 |
| Combo Adaptive Mfe Trail | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €15,03 | €30,05 | €0,67 | €0,00 |
| Combo Adaptive Mfe Trail | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €619,25 | €1.238,49 | €44,85 | €0,00 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,07020 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,22 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 58,85077 | 58,83900 | 58,00332 | 29,71964 | 60,54567 | €1.531,19 | €3.062,39 | €44,10 | €-0,61 |
| Combo Adaptive Quality7 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1175,20470 | 1147,33658 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €48,59 | €0,00 |
| Combo Adaptive Quality7 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1632,91916 | 1632,91916 | 1587,62241 | 824,62418 | 1723,51265 | €880,79 | €1.761,58 | €48,87 | €0,00 |
| Combo Adaptive Quality7 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02574 | €203,75 | €407,50 | €48,90 | €-0,00 |
| Combo Adaptive Quality7 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €182,81 | €365,62 | €43,87 | €24,13 |
| Combo Adaptive Regime V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €-0,00 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,67910 | 0,82382 | 1,09965 | 0,55902 | €202,91 | €405,83 | €48,70 | €31,15 |
| Combo Adaptive Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 58,29796 | 58,83900 | 58,55727 | 29,44047 | 59,97694 | €1.588,45 | €3.176,91 | €0,00 | €29,48 |
| Combo Adaptive Quality7 Regime V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €919,84 | €1.839,67 | €46,79 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,67910 | 0,82382 | 1,09965 | 0,55902 | €199,19 | €398,38 | €47,81 | €30,57 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,80 | €0,00 |
| Combo Adaptive Long Only V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1652,37083 | 1652,37083 | 1605,97924 | 834,44727 | 1745,15401 | €13,30 | €26,61 | €0,75 | €0,00 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,03881 | 58,83900 | 58,18865 | 29,81460 | 60,73912 | €1.675,98 | €3.351,96 | €48,27 | €-11,34 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €-0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07020 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €-0,05 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,00 | €0,00 |
| Combo Adaptive Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €659,36 | €1.318,73 | €47,75 | €0,00 |
| Combo Adaptive Partial 1R V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €187,17 | €374,34 | €44,92 | €24,70 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 58,29796 | 58,83900 | 58,55727 | 29,44047 | 59,97694 | €66,88 | €133,76 | €0,00 | €1,24 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €931,55 | €1.863,10 | €47,39 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,67910 | 0,82382 | 1,09965 | 0,55902 | €201,73 | €403,45 | €48,41 | €30,96 |
| Combo Adaptive Runner25 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €-0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07020 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €-0,06 |
| Combo Adaptive Runner25 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,00 | €0,00 |
| Combo Adaptive Runner25 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,35 | €34,70 | €1,24 | €0,00 |
| Combo Adaptive Runner25 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €204,60 | €409,21 | €49,10 | €-0,00 |
| Combo Adaptive Runner25 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,41543 | 58,83900 | 58,58664 | 28,99479 | 59,89578 | €14,35 | €28,70 | €0,00 | €0,71 |
| Combo Adaptive Runner25 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,23865 | €183,50 | €367,00 | €44,04 | €24,22 |
| Combo Adaptive Tp3 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €-0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07020 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €-0,06 |
| Combo Adaptive Tp3 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,00 | €0,00 |
| Combo Adaptive Tp3 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,03 | €34,05 | €1,22 | €0,00 |
| Combo Adaptive Tp3 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,41543 | 58,83900 | 58,58664 | 28,99479 | 59,89578 | €14,08 | €28,17 | €0,00 | €0,70 |
| Combo Adaptive Tp3 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,23865 | €180,07 | €360,14 | €43,22 | €23,76 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 62835,53038 | 63487,50000 | 63740,36202 | 83466,52952 | 61025,86711 | €1.146,03 | €3.438,09 | €49,51 | €-35,67 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63487,50000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €8,53 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 62834,55058 | 63487,50000 | 63638,83282 | 83465,22802 | 61225,98608 | €1.305,90 | €3.917,70 | €50,15 | €-40,71 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63487,50000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €2,51 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 74,71805 | 75,49600 | 75,79399 | 99,25048 | 72,56617 | €1.135,84 | €3.407,53 | €49,07 | €-35,48 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 74,57408 | 75,49600 | 75,92873 | 111,48825 | 71,18746 | €1.355,04 | €2.710,08 | €49,23 | €-33,50 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 74,96000 | 75,49600 | 75,91949 | 99,57187 | 73,04103 | €1.293,08 | €3.879,24 | €49,65 | €-27,74 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 74,57408 | 75,49600 | 75,92873 | 111,48825 | 70,78107 | €1.374,20 | €2.748,40 | €49,92 | €-33,98 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 74,39088 | 75,49600 | 75,19974 | 49,96587 | 75,72991 | €1.384,76 | €4.154,29 | €0,00 | €61,71 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 74,57408 | 75,49600 | 76,05188 | 111,48825 | 70,87959 | €1.259,31 | €2.518,63 | €49,91 | €-31,14 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,07020 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €-3,17 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06952 | 0,07020 | 0,07041 | 0,09234 | 0,06774 | €1.295,48 | €3.886,44 | €49,75 | €-38,11 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,93 | €73,85 | €1,65 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €626,90 | €1.253,80 | €44,76 | €0,00 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,83900 | 56,74249 | 29,07362 | 59,22958 | €1.514,30 | €3.028,59 | €43,61 | €66,68 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1901,13000 | 1875,39030 | 960,90919 | 1957,59085 | €47,34 | €94,69 | €1,36 | €-0,08 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63487,50000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.616,79 | €3.233,57 | €46,56 | €-0,65 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €0,00 |
| Master Adaptive No Alt V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68062 | 829,90965 | 1732,79507 | €22,94 | €45,88 | €1,25 | €0,00 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1901,13000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €0,23 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 58,83900 | 58,18865 | 29,81460 | 60,73912 | €1.637,93 | €3.275,87 | €47,17 | €-11,09 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63487,50000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.635,66 | €3.271,33 | €47,11 | €-0,65 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1167,82027 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €0,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1655,75286 | 1655,75286 | 1602,89078 | 836,15519 | 1761,47701 | €734,74 | €1.469,49 | €46,92 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01002 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €-2,02 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 58,83900 | 58,06542 | 29,75146 | 60,61050 | €1.418,93 | €2.837,86 | €40,87 | €-3,60 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €15,69 | €31,37 | €0,90 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.101,72 | €2.203,44 | €48,77 | €0,00 |
| Master Adaptive Expanded V1 | H | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14001 | 0,12939 | 0,12321 | 0,07071 | 0,17362 | €176,03 | €352,07 | €42,25 | €-26,71 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1901,13000 | 1875,39030 | 960,90919 | 1957,59085 | €15,15 | €30,30 | €0,44 | €-0,03 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 58,83900 | 58,18865 | 29,81460 | 60,73912 | €1.636,69 | €3.273,37 | €47,14 | €-11,08 |
| Master Adaptive Expanded V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 494,13881 | 491,71000 | 487,02321 | 249,54010 | 508,37001 | €56,33 | €112,66 | €1,62 | €-0,55 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,43 | €72,87 | €1,62 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €618,57 | €1.237,14 | €44,16 | €0,00 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,83900 | 56,74249 | 29,07362 | 59,22958 | €1.494,18 | €2.988,35 | €43,03 | €65,79 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1901,13000 | 1875,39030 | 960,90919 | 1957,59085 | €46,71 | €93,43 | €1,35 | €-0,08 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63487,50000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.595,31 | €3.190,61 | €45,94 | €-0,64 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1165,32878 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,00 |
| Master Adaptive Runner25 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54904 | 824,18962 | 1768,58749 | €850,90 | €1.701,80 | €47,45 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 58,83900 | 58,06542 | 29,75146 | 61,45886 | €1.476,62 | €2.953,25 | €42,53 | €-3,75 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63487,50000 | 62585,79466 | 32067,59974 | 66243,40603 | €1.599,88 | €3.199,76 | €46,08 | €-0,64 |
| Combo Adaptive Side Regime Guard V1 | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,07020 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €-13,96 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 1,00217 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €7,26 |
| Combo Adaptive Side Regime Guard V1 | ACE | SHORT | Combo Adaptive | 60m | 2,0x | 0,15317 | 0,15317 | 0,15317 | 0,22899 | 0,11641 | €207,74 | €415,49 | €0,00 | €-0,00 |
| Master Adaptive Gb20 Be V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,11 | €74,22 | €1,65 | €0,00 |
| Master Adaptive Gb20 Be V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €630,00 | €1.260,01 | €44,98 | €0,00 |
| Master Adaptive Gb20 Be V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,83900 | 56,74249 | 29,07362 | 59,22958 | €1.521,79 | €3.043,59 | €43,83 | €67,01 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1901,13000 | 1875,39030 | 960,90919 | 1957,59085 | €47,58 | €95,15 | €1,37 | €-0,08 |
| Master Adaptive Gb20 Be V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63487,50000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.624,79 | €3.249,59 | €46,79 | €-0,65 |
| Master Adaptive Gb20 Partial V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,07 | €74,14 | €1,65 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €629,33 | €1.258,67 | €44,93 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,83900 | 56,74249 | 29,07362 | 59,22958 | €1.520,18 | €3.040,35 | €43,78 | €66,94 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1901,13000 | 1875,39030 | 960,90919 | 1957,59085 | €47,53 | €95,05 | €1,37 | €-0,08 |
| Master Adaptive Gb20 Partial V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63487,50000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.623,07 | €3.246,13 | €46,74 | €-0,65 |
| Master Adaptive Gb20 Loss Cap V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,83900 | 56,94975 | 29,07362 | 59,22958 | €1.805,69 | €3.611,39 | €39,00 | €79,51 |
| Master Adaptive Gb20 Loss Cap V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1901,13000 | 1882,24034 | 960,90919 | 1957,59085 | €1.821,95 | €3.643,90 | €39,35 | €-3,18 |
| Master Adaptive Gb20 Loss Cap V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63487,50000 | 62814,39537 | 32067,59974 | 65329,00319 | €1.820,09 | €3.640,18 | €39,31 | €-0,73 |
| 1H Fast V3 Nohigh Range Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 59,03881 | 58,83900 | 58,37757 | 39,65440 | 60,03066 | €1.540,99 | €4.622,96 | €51,78 | €-15,65 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €143,50 | €430,49 | €51,66 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €143,19 | €429,58 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €1.527,56 | €4.582,69 | €51,33 | €-5,82 |
| 1H Fast V3 Nohigh Regime Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1902,79048 | 1901,13000 | 1881,47923 | 1278,04094 | 1934,75736 | €1.508,82 | €4.526,45 | €50,70 | €-3,95 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00217 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €18,40 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63487,50000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €-4,20 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01002 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €-8,45 |
| Main Side Regime Guard V1 | SOL | SHORT | Confluenza trend | 240m | 3,0x | 74,57408 | 75,49600 | 75,80558 | 99,05924 | 72,11109 | €47,14 | €141,41 | €2,34 | €-1,75 |
| Combo Trend Side Regime Guard V1 | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07020 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-24,09 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00217 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €7,13 |
| Combo Trend Side Regime Guard V1 | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ACE | SHORT | Combo Trend | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,09934 | €214,51 | €429,02 | €51,48 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTC | SHORT | Combo Trend | 60m | 2,0x | 62834,55058 | 63487,50000 | 63839,90339 | 93937,65311 | 60622,77440 | €105,21 | €210,42 | €3,37 | €-2,19 |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €19,67 | €59,00 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €136,56 | €409,67 | €49,16 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €135,49 | €406,48 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1901,13000 | 1868,48380 | 1269,21348 | 1921,39394 | €24,52 | €73,57 | €0,82 | €0,45 |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01002 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €-0,68 |
| 1H Fast Nohigh Cap75 Short Only V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,76314 | 0,67910 | 0,75343 | 1,01371 | 0,62578 | €137,15 | €411,45 | €0,00 | €45,31 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,91378 | 58,83900 | 58,25395 | 39,57042 | 59,90353 | €38,49 | €115,47 | €1,29 | €-0,15 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07020 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,33 |
| 1H Balanced V3 Long Only V1 | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €432,90 | €1.298,70 | €46,36 | €0,00 |
| 1H Balanced V3 Long Only V1 | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €120,86 | €362,58 | €43,51 | €-0,00 |
| 1H Balanced V3 Long Only V1 | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 1,00217 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €-0,44 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 62892,88891 | 63487,50000 | 63798,54651 | 83542,72076 | 61081,57371 | €37,97 | €113,91 | €1,64 | €-1,08 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,36815 | 0,34829 | 0,41233 | 0,48902 | 0,27979 | €126,96 | €380,87 | €45,70 | €20,55 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 58,91378 | 58,83900 | 58,06542 | 39,57042 | 60,61050 | €1.077,12 | €3.231,35 | €46,53 | €-4,10 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00217 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €0,16 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,68 | €403,35 | €48,40 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,49600 | 75,79399 | 111,70349 | 72,56617 | €21,81 | €43,62 | €0,63 | €-0,45 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,07020 | 0,07049 | 0,10388 | 0,06749 | €70,07 | €140,14 | €2,02 | €-1,44 |
| Scanner Bottom5 Short Profit Lock V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €205,68 | €411,36 | €49,36 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €205,47 | €410,94 | €49,31 | €27,12 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63487,50000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,40 | €90,81 | €1,31 | €-0,68 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00217 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €0,16 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,98 | €403,97 | €48,48 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,49600 | 75,79399 | 111,70349 | 72,56617 | €21,84 | €43,69 | €0,63 | €-0,45 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,07020 | 0,07049 | 0,10388 | 0,06749 | €70,18 | €140,35 | €2,02 | €-1,44 |
| Scanner Bottom5 Short Mfe Trail V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €205,99 | €411,99 | €49,44 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,34829 | 0,41764 | 0,55748 | 0,28340 | €205,79 | €411,57 | €49,39 | €27,16 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63487,50000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,47 | €90,94 | €1,31 | €-0,68 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive V1 | SPCX | LONG | 2026-08-17T04:06:04+00:00 | 136,67995 | €-3,14 | -0,06 | TIME_EXIT_NO_CANDLES |
| Master Adaptive Runner25 V1 | SPCX | LONG | 2026-08-17T04:06:04+00:00 | 136,67995 | €-3,15 | -0,06 | TIME_EXIT_NO_CANDLES |
| Master Adaptive No Alt V1 | SPCX | LONG | 2026-08-17T04:06:04+00:00 | 136,67995 | €-3,14 | -0,06 | TIME_EXIT_NO_CANDLES |
| Master Adaptive Gb20 V1 | SPCX | LONG | 2026-08-17T04:06:04+00:00 | 136,67995 | €-3,10 | -0,06 | TIME_EXIT_NO_CANDLES |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | 2026-08-17T04:06:04+00:00 | 136,67995 | €-3,15 | -0,06 | TIME_EXIT_NO_CANDLES |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | 2026-08-17T04:06:04+00:00 | 136,67995 | €-3,16 | -0,06 | TIME_EXIT_NO_CANDLES |
| Master Adaptive Expanded V1 | SPCX | LONG | 2026-08-17T04:06:04+00:00 | 136,67995 | €-3,16 | -0,06 | TIME_EXIT_NO_CANDLES |
| Combo Trend | HYPE | LONG | 2026-08-17T04:06:04+00:00 | 59,04760 | €86,42 | 2,10 | TARGET |
| Combo Adaptive Mfe Trail | HYPE | LONG | 2026-08-17T04:06:04+00:00 | 59,05718 | €0,74 | 1,89 | TARGET |
| Sol Adaptive 1H | SOL | SHORT | 2026-08-17T03:05:53+00:00 | 75,55048 | €-53,11 | -1,10 | STOP |
| Scanner Top 5 Long 1H | HYPE | LONG | 2026-08-17T03:05:53+00:00 | 58,85648 | €90,24 | 1,89 | TARGET |
| Scanner Top20 Long | HYPE | LONG | 2026-08-17T03:05:53+00:00 | 58,85648 | €83,15 | 1,89 | TARGET |

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

Generato: 2026-08-17 05:32 UTC


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

Segnali totali salvati: **114**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-17 | BTC | 63.428,86 | +1 | +4 | +3 | +1 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-17 | DOGE | 0.07007 | +2 | +4 | +3 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-17 | SOL | 75,40 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-16 | BTC | 63.005,56 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-16 | DOGE | 0.06966 | +4 | +4 | +3 | +2 | +1 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-16 | SOL | 75,33 | +1 | +3 | +3 | +3 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-15 | BTC | 63.058,07 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-15 | DOGE | 0.07017 | +4 | +4 | +3 | +2 | +1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-15 | SOL | 75,40 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-14 | BTC | 62.749,25 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-14 | DOGE | 0.06940 | +2 | +4 | +3 | +2 | 0 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-14 | SOL | 75,41 | +3 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 38 | 37 | 36 | 35 | 34 | 33 | 30 | 26 | 19 | 10 | 0 | 0 |
| SOL | 38 | 37 | 36 | 35 | 34 | 33 | 30 | 26 | 19 | 10 | 0 | 0 |
| DOGE | 38 | 37 | 36 | 35 | 34 | 33 | 30 | 26 | 19 | 10 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-19 | 30g | 2026-08-18 | domani |
| SOL | 2026-07-19 | 30g | 2026-08-18 | domani |
| DOGE | 2026-07-19 | 30g | 2026-08-18 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 35 | 48,57% | +0,02% | -0,01% | PRIMA CALIBRAZIONE |
| BTC | 2g | 34 | 47,06% | +0,05% | -0,09% | PRIMA CALIBRAZIONE |
| BTC | 3g | 33 | 39,39% | -0,10% | -0,32% | PRIMA CALIBRAZIONE |
| BTC | 5g | 32 | 28,12% | -0,09% | -0,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | 31 | 38,71% | -0,03% | -0,38% | PRIMA CALIBRAZIONE |
| BTC | 10g | 28 | 42,86% | +0,26% | -0,06% | FEEDBACK RAPIDO |
| BTC | 14g | 24 | 41,67% | -0,01% | -0,15% | FEEDBACK RAPIDO |
| BTC | 21g | 17 | 23,53% | -0,71% | -0,96% | FEEDBACK RAPIDO |
| BTC | 30g | 9 | 88,89% | +0,31% | +0,87% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 30 | 50,00% | +0,01% | -0,20% | PRIMA CALIBRAZIONE |
| SOL | 2g | 29 | 41,38% | -0,01% | -0,26% | FEEDBACK RAPIDO |
| SOL | 3g | 28 | 42,86% | +0,09% | -0,23% | FEEDBACK RAPIDO |
| SOL | 5g | 27 | 48,15% | -0,10% | -0,30% | FEEDBACK RAPIDO |
| SOL | 7g | 26 | 57,69% | -0,04% | +0,16% | FEEDBACK RAPIDO |
| SOL | 10g | 23 | 52,17% | -0,13% | +0,21% | FEEDBACK RAPIDO |
| SOL | 14g | 20 | 60,00% | -1,32% | +0,49% | FEEDBACK RAPIDO |
| SOL | 21g | 14 | 57,14% | -2,85% | -0,16% | FEEDBACK RAPIDO |
| SOL | 30g | 9 | 33,33% | -1,02% | -0,95% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 35 | 42,86% | -0,02% | -0,04% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 34 | 44,12% | -0,13% | -0,13% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 33 | 42,42% | -0,31% | +0,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 32 | 50,00% | -0,59% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 31 | 61,29% | -0,86% | +0,57% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 28 | 53,57% | -1,37% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 14g | 25 | 60,00% | -2,12% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 21g | 18 | 83,33% | -3,52% | +2,95% | FEEDBACK RAPIDO |
| DOGE | 30g | 10 | 100,00% | -4,20% | +4,20% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 35 | 48,57% | +0,02% | -0,01% | -0,30% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 37 | 51,35% | +0,01% | +0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 37 | 51,35% | +0,01% | +0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 33 | 51,52% | -0,02% | -0,02% | -0,36% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 32 | 34,38% | +0,16% | -0,40% | -0,18% | +0,66% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 7 | 14,29% | +0,59% | -0,59% | -0,03% | +0,84% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 34 | 47,06% | +0,05% | -0,09% | -0,44% | +0,73% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 36 | 50,00% | +0,03% | +0,03% | -0,45% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 36 | 50,00% | +0,03% | +0,03% | -0,45% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 32 | 50,00% | -0,06% | -0,06% | -0,54% | +0,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 31 | 41,94% | +0,20% | -0,39% | -0,26% | +0,87% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 6 | 16,67% | +0,74% | -0,74% | +0,30% | +1,36% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 33 | 39,39% | -0,10% | -0,32% | -1,36% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | -0,03% | -0,03% | -1,33% | +1,55% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | -0,03% | -0,03% | -1,33% | +1,55% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 31 | 51,61% | -0,05% | -0,05% | -1,35% | +1,46% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 30 | 33,33% | +0,30% | -0,48% | -1,09% | +1,81% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 5 | 20,00% | +1,16% | -1,16% | -0,33% | +2,21% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 32 | 28,12% | -0,09% | -0,49% | -2,11% | +2,04% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 40,00% | -0,01% | -0,01% | -2,06% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 29 | 37,93% | +0,10% | -0,74% | -1,83% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 31 | 38,71% | -0,03% | -0,38% | -2,37% | +2,40% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 33 | 48,48% | -0,06% | -0,06% | -2,36% | +2,41% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,06% | -0,06% | -2,36% | +2,41% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | +0,11% | +0,11% | -2,33% | +2,42% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 28 | 32,14% | +0,33% | -0,90% | -2,10% | +2,65% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 28 | 42,86% | +0,26% | -0,06% | -2,57% | +2,92% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | +0,09% | +0,09% | -2,60% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 30 | 50,00% | +0,09% | +0,09% | -2,60% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | +0,42% | +0,42% | -2,47% | +2,98% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 25 | 32,00% | +0,34% | -0,33% | -2,28% | +3,24% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 24 | 41,67% | -0,01% | -0,15% | -2,83% | +3,41% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 26 | 42,31% | -0,12% | -0,12% | -2,86% | +3,35% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 26 | 42,31% | -0,12% | -0,12% | -2,86% | +3,35% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 22 | 50,00% | +0,31% | +0,31% | -2,58% | +3,53% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 21 | 57,14% | +0,15% | +0,08% | -2,48% | +3,75% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 17 | 23,53% | -0,71% | -0,96% | -3,31% | +3,61% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 19 | 36,84% | -0,75% | -0,75% | -3,35% | +3,50% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 19 | 36,84% | -0,75% | -0,75% | -3,35% | +3,50% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -0,58% | -0,58% | -3,04% | +3,81% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 15 | 26,67% | -0,36% | -0,09% | -2,97% | +3,98% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 9 | 88,89% | +0,31% | +0,87% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 9 | 55,56% | +0,08% | -0,44% | -2,41% | +5,20% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 35 | 42,86% | -0,02% | -0,04% | -0,49% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 37 | 54,05% | -0,13% | +0,20% | -0,61% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 37 | 54,05% | -0,13% | +0,20% | -0,61% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | -0,02% | +0,10% | -0,52% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 32 | 50,00% | -0,12% | +0,11% | -0,60% | +0,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,23% | -0,23% | -0,30% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 34 | 44,12% | -0,13% | -0,13% | -0,77% | +0,92% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 36 | 47,22% | -0,24% | +0,02% | -0,88% | +0,77% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 36 | 47,22% | -0,24% | +0,02% | -0,88% | +0,77% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 47,06% | -0,33% | +0,10% | -0,93% | +0,74% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 31 | 58,06% | -0,30% | +0,29% | -0,91% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 23 | 47,83% | +0,18% | -0,18% | -0,46% | +1,21% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 33 | 42,42% | -0,31% | +0,03% | -1,78% | +2,01% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 35 | 48,57% | -0,42% | -0,06% | -1,88% | +1,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 35 | 48,57% | -0,42% | -0,06% | -1,88% | +1,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 33 | 51,52% | -0,66% | +0,16% | -1,84% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 23 | 39,13% | -0,05% | +0,05% | -1,78% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 32 | 50,00% | -0,59% | +0,19% | -2,65% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,69% | +0,05% | -2,71% | +2,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 31 | 61,29% | -0,86% | +0,57% | -3,09% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 33 | 57,58% | -0,95% | +0,35% | -3,18% | +2,54% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 33 | 57,58% | -0,95% | +0,35% | -3,18% | +2,54% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 31 | 58,06% | -0,94% | +0,30% | -3,21% | +2,41% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,91% | +0,91% | -3,18% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 28 | 53,57% | -1,37% | +0,85% | -3,83% | +2,75% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 30 | 53,33% | -1,40% | +0,71% | -3,88% | +2,64% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 30 | 53,33% | -1,40% | +0,71% | -3,88% | +2,64% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | -1,44% | +0,70% | -3,90% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 29 | 65,52% | -1,43% | +1,43% | -3,95% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 21 | 61,90% | -1,18% | +1,18% | -3,82% | +2,85% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,23% | +0,22% | -1,27% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 25 | 60,00% | -2,12% | +1,60% | -4,78% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 26 | 65,38% | -2,20% | +1,40% | -4,86% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 26 | 65,38% | -2,20% | +1,40% | -4,86% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 24 | 66,67% | -2,25% | +1,39% | -4,95% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 26 | 73,08% | -2,20% | +2,20% | -4,86% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 18 | 83,33% | -3,52% | +2,95% | -6,03% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 19 | 84,21% | -3,54% | +2,69% | -6,07% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 19 | 84,21% | -3,54% | +2,69% | -6,07% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 17 | 88,24% | -3,81% | +2,86% | -6,34% | +2,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 19 | 89,47% | -3,54% | +3,54% | -6,07% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 16 | 87,50% | -3,30% | +3,30% | -5,81% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 9 | 100,00% | -3,98% | +3,98% | -6,65% | +2,73% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 30 | 50,00% | +0,01% | -0,20% | -0,49% | +0,67% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 33 | 57,58% | -0,26% | -0,00% | -0,72% | +0,36% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 36 | 55,56% | -0,15% | -0,09% | -0,63% | +0,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 31 | 51,61% | -0,10% | +0,03% | -0,67% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 35 | 51,43% | -0,09% | -0,01% | -0,59% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 29 | 41,38% | -0,01% | -0,26% | -0,68% | +0,86% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 32 | 46,88% | -0,25% | -0,11% | -0,97% | +0,49% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 35 | 45,71% | -0,20% | -0,13% | -0,89% | +0,68% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 30 | 43,33% | -0,18% | -0,15% | -0,89% | +0,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 34 | 41,18% | -0,15% | -0,19% | -0,81% | +0,74% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 28 | 42,86% | +0,09% | -0,23% | -1,84% | +1,94% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 31 | 41,94% | -0,32% | -0,07% | -2,16% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 41,18% | -0,26% | -0,09% | -2,07% | +1,78% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 29 | 41,38% | -0,21% | -0,28% | -2,00% | +1,80% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 33 | 45,45% | -0,20% | -0,16% | -2,02% | +1,85% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 27 | 48,15% | -0,10% | -0,30% | -2,59% | +2,61% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,33% | -0,09% | -2,88% | +2,31% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,23% | -0,15% | -2,80% | +2,46% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 28 | 46,43% | -0,42% | -0,16% | -2,75% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 32 | 46,88% | -0,28% | -0,24% | -2,88% | +2,55% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 26 | 57,69% | -0,04% | +0,16% | -3,08% | +3,02% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 29 | 62,07% | -0,41% | +0,39% | -3,36% | +2,76% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 32 | 62,50% | -0,38% | +0,36% | -3,30% | +2,87% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | -0,16% | -0,08% | -3,23% | +2,87% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 32 | 37,50% | -0,34% | -0,30% | -3,35% | +2,93% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 23 | 52,17% | -0,13% | +0,21% | -3,69% | +3,64% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 26 | 57,69% | -0,24% | +0,59% | -4,06% | +3,28% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 29 | 55,17% | -0,24% | +0,55% | -3,99% | +3,35% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 24 | 50,00% | +0,17% | -0,06% | -3,90% | +3,45% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,34% | +0,18% | -4,02% | +3,35% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 20 | 60,00% | -1,32% | +0,49% | -4,80% | +3,68% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 22 | 77,27% | -0,69% | +1,01% | -5,06% | +3,44% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 25 | 80,00% | -0,98% | +1,26% | -4,92% | +3,49% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | -0,43% | -0,25% | -4,72% | +3,65% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 26 | 42,31% | -1,10% | +0,32% | -5,00% | +3,50% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 18 | 44,44% | -0,29% | +0,29% | -4,81% | +4,01% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 14 | 57,14% | -2,85% | -0,16% | -7,27% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 15 | 66,67% | -2,46% | +1,27% | -7,21% | +2,50% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 18 | 72,22% | -2,51% | +1,51% | -7,02% | +2,73% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 13 | 30,77% | -2,42% | -1,12% | -6,96% | +2,69% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 19 | 63,16% | -2,34% | +0,17% | -7,02% | +2,78% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 11 | 72,73% | -0,88% | +0,88% | -6,79% | +3,10% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 9 | 33,33% | -1,02% | -0,95% | -7,39% | +3,33% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -1,73% | +0,94% | -7,87% | +2,83% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -1,14% | +0,59% | -7,56% | +3,15% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -1,24% | -0,64% | -7,67% | +3,09% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 10 | 30,00% | -1,14% | -0,73% | -7,56% | +3,15% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,04% | -0,04% | -6,17% | +4,49% | FEEDBACK RAPIDO |
| SOL | 30g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |

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

Generato: 2026-08-17 05:32 UTC

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
| BTC | 38 | PRIMA CALIBRAZIONE | 37 | 9 | 0 | 0 | Famiglia statistica | 1g | 51,35% | +0,01% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 38 | PRIMA CALIBRAZIONE | 35 | 10 | 0 | 0 | Tecnico | 1g | 51,43% | -0,01% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 38 | PRIMA CALIBRAZIONE | 37 | 11 | 0 | 0 | Famiglia statistica | 1g | 54,05% | +0,20% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 7 | 14,29% | -0,59% | +0,59% | -0,03% | +0,84% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 37 | 51,35% | +0,01% | +0,01% | -0,31% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 32 | 34,38% | -0,40% | +0,16% | -0,18% | +0,66% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 6 | 16,67% | -0,74% | +0,74% | +0,30% | +1,36% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 36 | 50,00% | +0,03% | +0,03% | -0,45% | +0,70% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 31 | 41,94% | -0,39% | +0,20% | -0,26% | +0,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 5 | 20,00% | -1,16% | +1,16% | -0,33% | +2,21% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 35 | 51,43% | -0,03% | -0,03% | -1,33% | +1,55% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 30 | 33,33% | -0,48% | +0,30% | -1,09% | +1,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 29 | 37,93% | -0,74% | +0,10% | -1,83% | +2,30% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 33 | 48,48% | -0,06% | -0,06% | -2,36% | +2,41% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 28 | 32,14% | -0,90% | +0,33% | -2,10% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 30 | 50,00% | +0,09% | +0,09% | -2,60% | +2,90% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 25 | 32,00% | -0,33% | +0,34% | -2,28% | +3,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 26 | 42,31% | -0,12% | -0,12% | -2,86% | +3,35% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 21 | 57,14% | +0,08% | +0,15% | -2,48% | +3,75% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 19 | 36,84% | -0,75% | -0,75% | -3,35% | +3,50% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 15 | 26,67% | -0,09% | -0,36% | -2,97% | +3,98% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 9 | 55,56% | -0,44% | +0,08% | -2,41% | +5,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 24 | 37,50% | -0,23% | +0,23% | -0,30% | +0,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 37 | 54,05% | +0,20% | -0,13% | -0,61% | +0,56% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 32 | 50,00% | +0,11% | -0,12% | -0,60% | +0,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 23 | 47,83% | -0,18% | +0,18% | -0,46% | +1,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 36 | 47,22% | +0,02% | -0,24% | -0,88% | +0,77% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 31 | 58,06% | +0,29% | -0,30% | -0,91% | +0,59% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 23 | 39,13% | +0,05% | -0,05% | -1,78% | +2,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 35 | 48,57% | -0,06% | -0,42% | -1,88% | +1,84% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 30 | 50,00% | +0,49% | -0,49% | -2,02% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,40% | -0,40% | -2,68% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 34 | 47,06% | +0,08% | -0,68% | -2,71% | +2,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 30 | 63,33% | +0,75% | -0,75% | -2,89% | +2,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,91% | -0,91% | -3,18% | +2,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 33 | 57,58% | +0,35% | -0,95% | -3,18% | +2,54% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 30 | 63,33% | +1,05% | -1,05% | -3,36% | +2,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 21 | 61,90% | +1,18% | -1,18% | -3,82% | +2,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 30 | 53,33% | +0,71% | -1,40% | -3,88% | +2,64% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,22% | +1,23% | -1,27% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 29 | 65,52% | +1,43% | -1,43% | -3,95% | +2,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 20 | 70,00% | +2,09% | -2,09% | -4,80% | +3,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 26 | 65,38% | +1,40% | -2,20% | -4,86% | +2,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 26 | 73,08% | +2,20% | -2,20% | -4,86% | +2,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 16 | 87,50% | +3,30% | -3,30% | -5,81% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 19 | 84,21% | +2,69% | -3,54% | -6,07% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 19 | 89,47% | +3,54% | -3,54% | -6,07% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 9 | 100,00% | +3,98% | -3,98% | -6,65% | +2,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 10 | 100,00% | +4,20% | -4,20% | -6,79% | +2,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 10 | 100,00% | +4,20% | -4,20% | -6,79% | +2,51% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 33 | 57,58% | -0,00% | -0,26% | -0,72% | +0,36% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 35 | 51,43% | -0,01% | -0,09% | -0,59% | +0,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 32 | 46,88% | -0,11% | -0,25% | -0,97% | +0,49% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 34 | 41,18% | -0,19% | -0,15% | -0,81% | +0,74% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 31 | 41,94% | -0,07% | -0,32% | -2,16% | +1,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 33 | 45,45% | -0,16% | -0,20% | -2,02% | +1,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 30 | 50,00% | -0,09% | -0,33% | -2,88% | +2,31% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,24% | -0,28% | -2,88% | +2,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 29 | 62,07% | +0,39% | -0,41% | -3,36% | +2,76% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 32 | 37,50% | -0,30% | -0,34% | -3,35% | +2,93% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 26 | 57,69% | +0,59% | -0,24% | -4,06% | +3,28% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 30 | 50,00% | +0,18% | -0,34% | -4,02% | +3,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 18 | 44,44% | +0,29% | -0,29% | -4,81% | +4,01% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 22 | 77,27% | +1,01% | -0,69% | -5,06% | +3,44% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 26 | 42,31% | +0,32% | -1,10% | -5,00% | +3,50% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 11 | 72,73% | +0,88% | -0,88% | -6,79% | +3,10% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 15 | 66,67% | +1,27% | -2,46% | -7,21% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 19 | 63,16% | +0,17% | -2,34% | -7,02% | +2,78% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 3 | 33,33% | -0,04% | +0,04% | -6,17% | +4,49% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 7 | 71,43% | +0,94% | -1,73% | -7,87% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 10 | 30,00% | -0,73% | -1,14% | -7,56% | +3,15% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 35 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 35 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 37 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 18 | 16,67% | -0,80% |
| BTC | BREVE | Famiglia statistica | 108 | 50,93% | +0,00% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 93 | 36,56% | -0,42% |
| BTC | SETTIMANALE | Classic technical | 12 | 8,33% | -1,47% |
| BTC | SETTIMANALE | Famiglia statistica | 97 | 45,36% | -0,02% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 82 | 34,15% | -0,67% |
| BTC | SWING | Classic technical | 4 | 50,00% | -0,27% |
| BTC | SWING | Famiglia statistica | 45 | 40,00% | -0,39% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 36 | 44,44% | +0,01% |
| BTC | MEDIO | Famiglia statistica | 10 | 60,00% | +0,21% |
| BTC | MEDIO | Tecnico | 9 | 55,56% | -0,44% |
| DOGE | BREVE | Classic technical | 70 | 41,43% | -0,12% |
| DOGE | BREVE | Famiglia statistica | 108 | 50,00% | +0,06% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 93 | 52,69% | +0,29% |
| DOGE | SETTIMANALE | Classic technical | 65 | 56,92% | +0,83% |
| DOGE | SETTIMANALE | Famiglia statistica | 97 | 52,58% | +0,36% |
| DOGE | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,28% |
| DOGE | SETTIMANALE | Tecnico | 89 | 64,04% | +1,07% |
| DOGE | SWING | Classic technical | 36 | 77,78% | +2,63% |
| DOGE | SWING | Famiglia statistica | 45 | 73,33% | +1,95% |
| DOGE | SWING | Microstruttura exchange | 4 | 100,00% | +0,61% |
| DOGE | SWING | Tecnico | 45 | 80,00% | +2,76% |
| DOGE | MEDIO | Classic technical | 9 | 100,00% | +3,98% |
| DOGE | MEDIO | Famiglia statistica | 10 | 100,00% | +4,20% |
| DOGE | MEDIO | Tecnico | 10 | 100,00% | +4,20% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 96 | 48,96% | -0,06% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 102 | 46,08% | -0,12% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 85 | 56,47% | +0,28% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 5 | 0,00% | -3,42% |
| SOL | SETTIMANALE | Tecnico | 94 | 44,68% | -0,13% |
| SOL | SWING | Classic technical | 29 | 55,17% | +0,51% |
| SOL | SWING | Famiglia statistica | 37 | 72,97% | +1,12% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 45 | 51,11% | +0,25% |
| SOL | MEDIO | Classic technical | 3 | 33,33% | -0,04% |
| SOL | MEDIO | Famiglia statistica | 7 | 71,43% | +0,94% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 10 | 30,00% | -0,73% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 3 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | MEDIO | 11 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 12 | in attesa di controlli maturati |

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

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         38 |              10 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         38 |              10 |          28 | RACCOLTA DATI | 10,00%           | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         38 |              10 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| SOL     | BASSO          | MEDIO          | leva moderata possibile solo con stop e margine                         |
| DOGE    | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-17 05:32 UTC


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
| BTC | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910. | Sotto 62.227 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,19 / 90,54, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 69,65 / 70,69 / 62,19. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.07286 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +1 | +4 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| SOL | +3 | +2 | +3 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| DOGE | +3 | +2 | +4 | 0 | -1 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +1, match regime 20. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 67,50%, return centrale 30g +6,19%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+1** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 20, positivi 30g 55,00%, return p50 +4,99%.
- Scanner path: **0** — Controlli disponibili 36. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -4/12, verdetto debole, trend ribassista, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -7/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo +2, match regime 9. Scanner e regime concordi, ma i match sono meno di 10: nessun bonus. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +4,64%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 9, positivi 30g 77,78%, return p50 +3,53%.
- Scanner path: **0** — Controlli disponibili 36. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -4/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +57,75%, aderenza live +68,93%, errore live +15,54%, gap corrente -19,30%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 34, ma percorso ancorato non aderente: gap -19,30%, errore live +15,54%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,29 $, upside EMA200 +47,60%, gap EMA50/EMA200 -6,29%, hit EMA200 12w +33,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,19 / 90,54, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 69,65 / 70,69 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 12. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 67,50%, return centrale 30g +14,31%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 12, positivi 30g 66,67%, return p50 +11,56%.
- Scanner path: **0** — Controlli disponibili 36. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -2/12, verdetto neutrale / misto, trend ribassista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -5/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Sopra 0.07286 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.


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

Generato: 2026-08-17 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.429 $ | prezzo corrente |
| Power Law centrale | 123.690 $ | deviazione -48,72% |
| Banda p10-p90 | 76.625 $ / 311.681 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 0,48% | posizione storica nel corridoio |
| Esponente β | 5,8183 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3154 cambiando finestra |
| Ultimo halving | 2024-04-19 | 850 giorni fa |
| Fase ciclo | 58,18% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-17 (4352 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1771) × giorni^5.8183
- Prezzo centrale oggi: **123.690 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 0,48%
- Scarto dal centro: **-48,72%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8183 | 91,93% |
| 2015 | 5,9023 | 91,49% |
| 2016 | 5,5882 | 87,73% |
| 2017 | 4,8582 | 82,85% |
| 2018 | 4,5869 | 78,31% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-04 | -13,98% | -3,97% | -2,97% | +63,93% |
| 2016-07-09 → 2020-05-11 | 2018-10-03 | -1,76% | -40,89% | -36,05% | +27,03% |
| 2020-05-11 → 2024-04-19 | 2022-08-26 | -7,20% | -18,04% | +19,39% | +28,37% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | 1.396934310521325 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -3 | 0 | -2.6494195271619336 | 0 |

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

Generato: 2026-08-17 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00119040 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +1,40% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000110 | -3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -2,65% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (+2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +1,31%; 30g +1,40%; 90g +7,44%; 180g -5,75%
- **Daily:** RSI 55.58; MA50 0.00119701; MA200 0.00118165
- **Weekly:** MA30 0.00118255; RSI 47.43
- **Livelli:** supporto 0.00116400; resistenza 0.00119500; breakout 60g 0.00134900; breakdown 60g 0.00104800
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00112700; target 0.00107050
- **Fibonacci:** VICINO — 50.0% a 0.00117900
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-3)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +3,44%; 30g -2,65%; 90g -18,77%; 180g -25,91%
- **Daily:** RSI 48.52; MA50 0.00000113; MA200 0.00000130
- **Weekly:** MA30 0.00000129; RSI 33.11
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000140; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 204 | 51,96% | +1,94% | -1,18% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 197 | 53,30% | +10,17% | +2,42% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 291 | 53,26% | +2,05% | -3,93% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 16 | 62,50% | -0,25% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 16 | 43,75% | -0,60% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 15 | 40,00% | -1,47% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 10 | 10,00% | -2,45% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 34 | 70,59% | +0,29% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 33 | 60,61% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 31 | 67,74% | +0,93% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 24 | 79,17% | +1,67% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 8 | 100,00% | +3,48% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **17 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +57,75%
- **Somiglianza strutturale:** +57,75%
- **Aderenza prezzo live:** +68,93%
- **Errore medio live:** +15,54%
- **Gap prezzo corrente:** -19,30%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 72 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-01
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Pullback e recupero parziale.** Zona bassa **68,83 $** intorno al **26 agosto 2026**; zona alta **77,28 $** intorno al **31 agosto 2026**; fine step circa **77,28 $** entro il **31 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 17 agosto 2026 | 46 | +68,93% | +15,54% | -19,30% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 17 agosto 2026 | 73 | +75,96% | +12,02% | -19,30% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +68,93% | Errore medio live +15,54%. |
| Gap corrente | -19,30% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 79,19 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 90,54 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 69,65 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 396,60 $ |
| Massimo percorso base | 396,60 $ (21 aprile 2029) |

## Grafici

### Grafico frattale sovrapposto

![Frattale BTC 2022 vs SOL 2026](btc_2022_vs_sol_2026_fractal_chart.png)

### Grafico proiezione condizionale

![Proiezione SOL BTC 2022](btc_2022_vs_sol_2026_projection_chart.png)

### Grafico ciclo base

![Ciclo base SOL BTC 2025](btc_2022_vs_sol_2026_cycle_base_chart.png)

### Grafico struttura vs aderenza

![Tracking frattale BTC SOL](btc_2022_vs_sol_2026_tracking_chart.png)

## Livelli chiave

| Livello | Prezzo / soglia | Lettura |
| --- | --- | --- |
| Rientro gap | entro ±12% | Condizione necessaria per tornare operativo. |
| Prima conferma | 79,19 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 90,54 $ | Scenario più credibile. |
| Invalidazione soft | 69,65 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 24 agosto 2026 | -3,31% | 72,93 $ | 72,36 $ | 75,42 $ |
| 14 giorni | 31 agosto 2026 | +2,46% | 77,28 $ | 68,83 $ | 77,28 $ |
| 30 giorni | 16 settembre 2026 | -5,74% | 71,09 $ | 68,83 $ | 78,93 $ |
| 60 giorni | 16 ottobre 2026 | +18,87% | 89,65 $ | 64,18 $ | 90,54 $ |
| 90 giorni | 15 novembre 2026 | +20,89% | 91,18 $ | 64,18 $ | 96,92 $ |
| 120 giorni | 15 dicembre 2026 | +13,05% | 85,26 $ | 64,18 $ | 96,92 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 17 agosto 2026 -> 31 agosto 2026 | +2,46% | 68,83 $ (26 agosto 2026) | 77,28 $ (31 agosto 2026) | 77,28 $ | Pullback e recupero parziale. |
| Step 2 - primo mese | 1 settembre 2026 -> 16 settembre 2026 | -5,74% | 71,09 $ (16 settembre 2026) | 78,93 $ (5 settembre 2026) | 71,09 $ | Prima spike, poi scarico. |
| Step 3 - secondo mese | 17 settembre 2026 -> 16 ottobre 2026 | +18,87% | 64,18 $ (23 settembre 2026) | 90,54 $ (14 ottobre 2026) | 89,65 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 17 ottobre 2026 -> 15 novembre 2026 | +20,89% | 86,72 $ (4 novembre 2026) | 96,92 $ (28 ottobre 2026) | 91,18 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali. La forma simile non compensa un prezzo non aderente.

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
| Prezzo SOL | 75,42 $ |  |
| Weekly RSI | 40,28 / linea grezza 52,95 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,91 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 396,60 $ | Avanzamento +19,02% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 40,9, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | -1 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 75,42 $ |
| TVL Solana | 4,80 mld $ |
| TVL 7g | -1,13% |
| DEX volume 24h | 1,05 mld $ |
| Fees 24h | 6,62 mln $ |
| Stablecoin su Solana | 15,94 mld $ |
| Stake ratio | 68,89% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE**

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

| Voce                      | Valore                                            |
|:--------------------------|:--------------------------------------------------|
| Lifecycle squeeze score | 4 |
| Bias | SQUEEZE SETUP MODERATO |
| Azione coerente | CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO |
| Peso suggerito Global | 0 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-08-10 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 75,42 $ |
| EMA200 weekly target | 111,29 $ |
| Upside verso EMA200 | +47,60% |
| Distanza prezzo da EMA200 | -32,25% |
| Gap EMA50/EMA200 | -6,29% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 40,26 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +33,33% |
| Max gain mediano 12w | +21,66% |
| Drawdown mediano 12w | -20,91% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-17 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-17 05:30:23 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: nessun cambiamento forte rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +67.50% | 0.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +70.00% | -2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +67.50% | 0.00 punti |

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
| BTC | 60.258 $ | 69.772 $ | +43,75% | +15,79% | rimbalzo debole | 69.772 $ | 60.258 $ | +14,29% | -13,64% | spike storicamente più resistente |
| SOL | 71,65 $ | 82,96 $ | +21,43% | +15,79% | rimbalzo poco frequente | 82,96 $ | 71,65 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06660 $ | 0,07711 $ | +57,14% | +15,79% | rimbalzo possibile | 0,07711 $ | 0,06660 $ | +28,12% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +43,75% (7/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 4 poi sono scaricati a -5,00%. Percentuale: +14,29% (4/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +21,43% (3/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +57,14% (16/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 9 poi sono scaricati a -5,00%. Percentuale: +28,12% (9/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-17 05:31:42 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto quando sono disponibili dati successivi

Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g     | P90 30g     |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:------------|:------------|
| BTC | 2026-08-17 | 63.429 $ | SALITA | 67,50% | 55.803,32 $ | 61.056,54 $ | 67.356,60 $ | 74.595,17 $ | 83.228,21 $ |
| SOL | 2026-08-17 | 75,42 $ | SALITA | 70,00% | 68,89 $ | 73,56 $ | 78,92 $ | 90,60 $ | 101,79 $ |
| DOGE | 2026-08-17 | 0.07010 $ | SALITA | 67,50% | 0.05452 $ | 0.06594 $ | 0.08013 $ | 0.09037 $ | 0.09868 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-18**; verificato fino al **2026-08-17**; stato **COMPLETO 30/30g**.
- Reale **63.425,99 $**; p50 previsto **65.807,17 $**; scarto **-3,62%**.
- Errore medio assoluto **3,34%**; massimo **6,04%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-18**; verificato fino al **2026-08-17**; stato **COMPLETO 30/30g**.
- Reale **75,41 $**; p50 previsto **74,26 $**; scarto **1,55%**.
- Errore medio assoluto **2,40%**; massimo **6,51%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-18**; verificato fino al **2026-08-17**; stato **COMPLETO 30/30g**.
- Reale **0.07009 $**; p50 previsto **0.06180 $**; scarto **13,42%**.
- Errore medio assoluto **9,15%**; massimo **20,06%**; DENTRO p10-p90; DENTRO p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 36 | 100,00% | 63,89% | 1,54% | -0,18% |
| BTC | 3g | 34 | 100,00% | 79,41% | 2,11% | -0,68% |
| BTC | 7g | 32 | 100,00% | 84,38% | 2,79% | -0,49% |
| BTC | 14g | 25 | 100,00% | 88,00% | 3,05% | -0,48% |
| BTC | 30g | 9 | 100,00% | 88,89% | 6,86% | -6,86% |
| SOL | 1g | 36 | 80,56% | 66,67% | 1,86% | -0,36% |
| SOL | 3g | 34 | 100,00% | 79,41% | 2,28% | -0,95% |
| SOL | 7g | 32 | 100,00% | 87,50% | 2,06% | -0,25% |
| SOL | 14g | 25 | 100,00% | 92,00% | 1,95% | 0,51% |
| SOL | 30g | 9 | 100,00% | 100,00% | 1,78% | 0,34% |
| DOGE | 1g | 36 | 97,22% | 66,67% | 2,25% | 0,07% |
| DOGE | 3g | 34 | 100,00% | 88,24% | 2,20% | 0,68% |
| DOGE | 7g | 32 | 93,75% | 90,62% | 5,09% | 3,16% |
| DOGE | 14g | 25 | 100,00% | 72,00% | 6,60% | 4,98% |
| DOGE | 30g | 9 | 100,00% | 44,44% | 13,59% | 13,59% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **102**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-17 | BTC | 63.429 $ | SALITA | 67,50% | 67.357 $ | 61.850 $ | 76.357 $ | 2026-09-16 |
| 2026-08-17 | DOGE | 0,07000 $ | SALITA | 67,50% | 0,08000 $ | 0,06000 $ | 0,09000 $ | 2026-09-16 |
| 2026-08-17 | SOL | 75,42 $ | SALITA | 70,00% | 78,92 $ | 73,16 $ | 89,46 $ | 2026-09-16 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-17 05:31 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **63.429,43 $**
- Return normale fra 30 giorni: **67.356,60 $** (6,19%)
- Drawdown normale durante il mese: **61.850,30 $** (-2,49%)
- Drawdown brutto da rispettare: **56.557,76 $** (-10,83%)
- Max gain normale durante il mese: **76.357,17 $** (20,38%)
- Max gain buono / take profit ottimistico: **83.376,36 $** (31,45%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **75,42 $**
- Return normale fra 30 giorni: **78,92 $** (4,64%)
- Drawdown normale durante il mese: **73,16 $** (-3,00%)
- Drawdown brutto da rispettare: **70,05 $** (-7,12%)
- Max gain normale durante il mese: **89,46 $** (18,61%)
- Max gain buono / take profit ottimistico: **97,04 $** (28,67%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,08 $** (14,31%)
- Drawdown normale durante il mese: **0,06 $** (-8,40%)
- Drawdown brutto da rispettare: **0,06 $** (-13,27%)
- Max gain normale durante il mese: **0,09 $** (26,07%)
- Max gain buono / take profit ottimistico: **0,10 $** (39,56%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 63.429,43 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **67,50%**
- Probabilità storica di discesa: **32,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **55.803,32 $** (-12,02%)
- Se va male: **61.056,54 $** (-3,74%)
- Scenario normale: **67.356,60 $** (6,19%)
- Se va bene: **74.595,17 $** (17,60%)
- Se va molto bene: **83.228,21 $** (31,21%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **61.850,30 $** (-2,49%)
- Discesa brutta: **56.557,76 $** (-10,83%)
- Discesa molto brutta: **51.871,23 $** (-18,22%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **76.357,17 $** (20,38%)
- Rialzo buono: **83.376,36 $** (31,45%)
- Rialzo molto forte: **93.869,80 $** (47,99%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **61.850,30 $** e uno spike normale intorno a **76.357,17 $**.

La chiusura a 30 giorni era più spesso positiva: salita 67,50%, discesa 32,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 75,42 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **70,00%**
- Probabilità storica di discesa: **30,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **68,89 $** (-8,65%)
- Se va male: **73,56 $** (-2,46%)
- Scenario normale: **78,92 $** (4,64%)
- Se va bene: **90,60 $** (20,13%)
- Se va molto bene: **101,79 $** (34,97%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **73,16 $** (-3,00%)
- Discesa brutta: **70,05 $** (-7,12%)
- Discesa molto brutta: **65,39 $** (-13,30%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **89,46 $** (18,61%)
- Rialzo buono: **97,04 $** (28,67%)
- Rialzo molto forte: **118,62 $** (57,27%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **73,16 $** e uno spike normale intorno a **89,46 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,07 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **67,50%**
- Probabilità storica di discesa: **32,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-22,22%)
- Se va male: **0,07 $** (-5,94%)
- Scenario normale: **0,08 $** (14,31%)
- Se va bene: **0,09 $** (28,91%)
- Se va molto bene: **0,10 $** (40,78%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-8,40%)
- Discesa brutta: **0,06 $** (-13,27%)
- Discesa molto brutta: **0,05 $** (-30,32%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (26,07%)
- Rialzo buono: **0,10 $** (39,56%)
- Rialzo molto forte: **0,11 $** (51,89%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,09 $**.

La chiusura a 30 giorni era più spesso positiva: salita 67,50%, discesa 32,50%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **16**
- Direzione corretta: **70,00%**
- Errore medio dello scenario centrale: **4,91%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **16**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,22%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **16**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **3,87%**
- Zona rischio toccata: **12,50%**
- Zona rialzo media toccata: **0,00%**
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

Dati ancora insufficienti: previsioni controllate **16** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **16** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **16** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 63.429,43 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **67,50%**
- Casi negativi dopo 30 giorni: **32,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,39%**
- Rendimento medio dopo 30 giorni: **10,30%**
- Rendimento centrale dopo 30 giorni: **6,19%**
- Discesa media durante i 30 giorni: **-7,34%**
- Massimo rialzo medio durante i 30 giorni: **27,60%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **69.965,81 $**
- Scenario centrale a 30 giorni: **67.356,60 $**
- Zona di rischio media: **58.771,68 $**
- Zona di rialzo media: **80.937,27 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,02% → **55.803,32 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,74% → **61.056,54 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,19% → **67.356,60 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 17,60% → **74.595,17 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 31,21% → **83.228,21 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -18,22% → **51.871,23 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -10,83% → **56.557,76 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -2,49% → **61.850,30 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,41% → **63.169,12 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **63.429,43 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 6,41% → **67.495,33 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,74% → **69.605,70 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 20,38% → **76.357,17 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 31,45% → **83.376,36 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 47,99% → **93.869,80 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-08-09   | 2020-11-16 |        88.88 |       133.71 |           0    |         152.04 |
| BTC-USD         | 2018-10-25   | 2019-02-01 |        87.65 |        10.3  |          -2.54 |          18.77 |
| XRP-USD         | 2026-01-10   | 2026-04-19 |        87.64 |        -2.44 |          -2.44 |           6.41 |
| ONE-USD         | 2020-02-16   | 2020-05-25 |        86.81 |       -22.88 |         -22.88 |           8.51 |
| LTC-USD         | 2023-07-21   | 2023-10-28 |        86.66 |         2.15 |          -1.96 |          10.9  |
| 1INCH-USD       | 2024-07-11   | 2024-10-18 |        86.46 |        11.07 |         -15.97 |          17.08 |
| NEO-USD         | 2018-10-24   | 2019-01-31 |        86.38 |        27.24 |          -1.02 |          46.91 |
| MKR-USD         | 2020-02-17   | 2020-05-26 |        86.19 |        36.64 |           0    |         104.38 |
| SOL-USD         | 2026-01-08   | 2026-04-17 |        86.02 |        -4.16 |          -6.58 |           9.54 |
| WAVES-USD       | 2024-05-15   | 2024-08-22 |        85.35 |         6.69 |         -14.17 |           7.19 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 75,42 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **77,87%**
- Rendimento medio dopo 30 giorni: **15,43%**
- Rendimento centrale dopo 30 giorni: **4,64%**
- Discesa media durante i 30 giorni: **-5,22%**
- Massimo rialzo medio durante i 30 giorni: **28,41%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **87,06 $**
- Scenario centrale a 30 giorni: **78,92 $**
- Zona di rischio media: **71,48 $**
- Zona di rialzo media: **96,84 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -8,65% → **68,89 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,46% → **73,56 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 4,64% → **78,92 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 20,13% → **90,60 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 34,97% → **101,79 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -13,30% → **65,39 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -7,12% → **70,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,00% → **73,16 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,15% → **75,31 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **75,42 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,83% → **79,06 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,49% → **81,82 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 18,61% → **89,46 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 28,67% → **97,04 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 57,27% → **118,62 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ONE-USD         | 2020-02-16   | 2020-05-25 |        83.5  |       -22.88 |         -22.88 |           8.51 |
| EOS-USD         | 2018-11-08   | 2019-02-15 |        82.49 |        34.78 |           0    |          52.35 |
| BNB-USD         | 2020-02-16   | 2020-05-25 |        81.44 |        -2.28 |          -3.01 |           9.23 |
| MKR-USD         | 2020-02-17   | 2020-05-26 |        81.07 |        36.64 |           0    |         104.38 |
| EOS-USD         | 2020-02-16   | 2020-05-25 |        80.86 |        -1.75 |          -1.75 |          11.2  |
| ZIL-USD         | 2020-08-11   | 2020-11-18 |        80.86 |       101.63 |          -2.99 |         101.63 |
| ENJ-USD         | 2018-10-24   | 2019-01-31 |        80.23 |       190.3  |         -13.17 |         193.34 |
| VET-USD         | 2020-02-13   | 2020-05-22 |        80.04 |        85.39 |          -2.6  |         109.53 |
| ATOM-USD        | 2020-02-16   | 2020-05-25 |        79.58 |         2.71 |          -1.33 |          20.49 |
| BNB-USD         | 2026-01-15   | 2026-04-24 |        79.47 |         3.09 |          -3.35 |           6.53 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,07 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **67,50%**
- Casi negativi dopo 30 giorni: **32,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,15%**
- Rendimento medio dopo 30 giorni: **14,41%**
- Rendimento centrale dopo 30 giorni: **14,31%**
- Discesa media durante i 30 giorni: **-11,48%**
- Massimo rialzo medio durante i 30 giorni: **29,46%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,09 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -22,22% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -5,94% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 14,31% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 28,91% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 40,78% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,32% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -13,27% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,40% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,83% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,14% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 12,87% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 26,07% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 39,56% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 51,89% → **0,11 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| OP-USD          | 2026-01-06   | 2026-04-15 |        89.63 |        14.03 |          -0.09 |          43.84 |
| VET-USD         | 2022-03-29   | 2022-07-06 |        88.86 |        33.03 |          -9.15 |          33.03 |
| HBAR-USD        | 2020-08-11   | 2020-11-18 |        88.57 |        16.65 |          -0.47 |          30.28 |
| SAND-USD        | 2025-01-09   | 2025-04-18 |        88.27 |        23.74 |           0    |          41.88 |
| XTZ-USD         | 2020-08-09   | 2020-11-16 |        88.14 |        13.45 |          -0.15 |          27.99 |
| ZEC-USD         | 2019-06-21   | 2019-09-28 |        88    |        -6.19 |         -18.51 |           0    |
| WAVES-USD       | 2022-03-27   | 2022-07-04 |        87.9  |         2.44 |         -14.68 |          13.6  |
| ADA-USD         | 2019-06-16   | 2019-09-23 |        87.24 |       -21.3  |         -21.3  |           0    |
| DOGE-USD        | 2025-01-10   | 2025-04-19 |        87.18 |        42.64 |          -1.37 |          58.07 |
| SNX-USD         | 2025-10-07   | 2026-01-14 |        86.97 |       -39.02 |         -43.19 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-17 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.429 $ | False | -17.36% | -10.22% | BEAR | -17.36% | -10.22% |
| DOGE-USD | BEAR | 0.07010 $ | False | -31.90% | -16.72% | BEAR | -17.36% | -10.22% |
| SOL-USD | BEAR | 75,42 $ | False | -10.46% | -16.87% | BEAR | -17.36% | -10.22% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 6.19% | 17.60% | 31.21% | -2.49% | -18.22% | 20.38% | 31.45% | 47.99% | 57.50% | 13.74% | 57.78% | 134.82% |
| BTC-USD | SAME_BTC_REGIME | 22 | 54.55% | 4.00% | 9.91% | 26.25% | -4.45% | -15.46% | 17.54% | 23.00% | 45.49% | 40.91% | -12.36% | 43.23% | 126.23% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 56.52% | 5.70% | 10.69% | 29.94% | -5.64% | -15.65% | 17.99% | 22.83% | 44.97% | 47.83% | -12.16% | 55.48% | 120.35% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 55.00% | 4.99% | 10.49% | 29.25% | -4.45% | -11.39% | 17.54% | 22.67% | 47.99% | 45.00% | -12.36% | 50.21% | 134.82% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 14.31% | 28.91% | 40.78% | -8.40% | -30.32% | 26.07% | 39.56% | 51.89% | 47.50% | -2.05% | 17.10% | 103.11% |
| DOGE-USD | SAME_BTC_REGIME | 18 | 77.78% | 13.66% | 26.87% | 44.13% | -9.86% | -28.41% | 25.42% | 40.19% | 53.31% | 44.44% | -4.55% | 6.98% | 112.48% |
| DOGE-USD | SAME_ASSET_REGIME | 17 | 76.47% | 24.33% | 34.01% | 38.54% | -9.15% | -28.68% | 31.81% | 39.23% | 46.79% | 58.82% | 3.04% | 7.64% | 85.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 66.67% | 11.56% | 25.54% | 33.36% | -10.38% | -30.02% | 20.61% | 34.29% | 42.97% | 41.67% | -6.36% | 3.53% | 7.38% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 4.64% | 20.13% | 34.97% | -3.00% | -13.30% | 18.61% | 28.67% | 57.27% | 65.00% | 21.07% | 56.22% | 157.46% |
| SOL-USD | SAME_BTC_REGIME | 12 | 75.00% | 3.31% | 7.00% | 19.97% | -3.75% | -12.54% | 13.96% | 25.59% | 46.98% | 33.33% | -8.15% | 37.98% | 81.24% |
| SOL-USD | SAME_ASSET_REGIME | 10 | 80.00% | 3.86% | 14.18% | 37.46% | -4.08% | -9.98% | 20.12% | 30.14% | 63.07% | 40.00% | -9.43% | 79.10% | 183.15% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 9 | 77.78% | 3.53% | 15.48% | 54.44% | -3.25% | -8.11% | 22.14% | 32.41% | 77.55% | 33.33% | -11.79% | 68.39% | 149.71% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 54.55% | 4.00% | -4.45% | 23.00% | 40.91% | -12.36% | 45.16% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 100.00% | 16.65% | -0.47% | 41.45% | 100.00% | 42.95% | 102.58% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 13.51% | -16.05% | 34.61% | 50.00% | 24.41% | 115.13% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 71.43% | 2.71% | -0.89% | 23.07% | 57.14% | 38.53% | 81.27% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 18 | 77.78% | 13.66% | -9.86% | 40.19% | 44.44% | -4.55% | 47.66% |
| DOGE-USD | HISTORICAL_BTC_BULL | 19 | 52.63% | 13.45% | -5.75% | 39.90% | 47.37% | -0.89% | 50.61% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 24.33% | -8.70% | 28.68% | 66.67% | 5.82% | 52.26% |
| SOL-USD | HISTORICAL_BTC_BEAR | 12 | 75.00% | 3.31% | -3.75% | 25.59% | 33.33% | -8.15% | 58.19% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 10.20% | -7.94% | 31.45% | 57.14% | 6.51% | 60.16% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 21 | 66.67% | 5.57% | -1.66% | 25.79% | 85.71% | 36.82% | 104.38% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 56.52% | 5.70% | -5.64% | 22.83% | 47.83% | -12.16% | 64.13% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 85.71% | 16.65% | -0.47% | 43.56% | 85.71% | 54.46% | 185.19% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.46% | -17.03% | 27.03% | 0.00% | -24.07% | 28.66% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 85.71% | 5.11% | -0.89% | 23.07% | 71.43% | 38.53% | 67.21% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 17 | 76.47% | 24.33% | -9.15% | 39.23% | 58.82% | 3.04% | 54.20% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 13 | 61.54% | 13.45% | -1.13% | 36.32% | 46.15% | -0.89% | 41.88% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 58.23% | -7.19% | 58.23% | 100.00% | 150.14% | 154.68% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 9 | 55.56% | 2.44% | -9.97% | 27.82% | 22.22% | -18.28% | 41.87% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 10 | 80.00% | 3.86% | -4.08% | 30.14% | 40.00% | -9.43% | 105.92% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 13.69% | -3.24% | 32.03% | 66.67% | 48.19% | 112.82% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 60.00% | 3.09% | -7.94% | 25.79% | 40.00% | -1.64% | 29.69% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 61.01% | -1.30% | 108.24% | 100.00% | 165.76% | 274.22% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 17 | 58.82% | 2.71% | -1.75% | 20.52% | 82.35% | 27.84% | 58.32% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | BTC-USD | 2018-10-25 | 87.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.30% | -2.54% | 18.77% | 39.91% | -2.54% | 39.91% |
| BTC-USD | XRP-USD | 2026-01-10 | 87.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.44% | -2.44% | 6.41% | -17.87% | -21.60% | 6.41% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | NEO-USD | 2018-10-24 | 86.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.24% | -1.02% | 46.91% | 44.33% | -1.02% | 46.91% |
| BTC-USD | SOL-USD | 2026-01-08 | 86.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | ETC-USD | 2018-10-24 | 85.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| BTC-USD | THETA-USD | 2022-04-15 | 84.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -10.88% | 27.86% | -20.52% | -20.52% | 27.86% |
| BTC-USD | ETH-USD | 2026-01-10 | 84.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| BTC-USD | LTC-USD | 2018-10-25 | 84.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.38% | 0.00% | 57.75% | 132.10% | 0.00% | 132.10% |
| BTC-USD | XTZ-USD | 2026-01-10 | 83.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | OP-USD | 2026-01-06 | 89.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.03% | -0.09% | 43.84% | -9.51% | -24.09% | 43.84% |
| DOGE-USD | ADA-USD | 2022-03-27 | 86.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | NEO-USD | 2022-03-27 | 86.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | QTUM-USD | 2022-07-30 | 86.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.20% | -30.29% | 1.37% | -32.40% | -35.81% | 1.37% |
| DOGE-USD | FTM-USD | 2022-03-27 | 85.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.54% | -11.30% | 35.15% | 1.61% | -11.30% | 54.20% |
| DOGE-USD | CHZ-USD | 2022-03-26 | 85.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.08% | -1.30% | 51.20% | 116.30% | -1.30% | 153.33% |
| DOGE-USD | LINK-USD | 2022-03-27 | 85.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| DOGE-USD | DASH-USD | 2022-03-27 | 85.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LTC-USD | 2018-04-28 | 85.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.22% | -27.61% | 0.00% | -21.87% | -30.75% | 0.00% |
| DOGE-USD | THETA-USD | 2022-03-31 | 85.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 34.01% | -12.38% | 34.01% | -13.72% | -13.72% | 34.01% |
| SOL-USD | ENJ-USD | 2018-10-24 | 80.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 190.30% | -13.17% | 193.34% | 417.86% | -13.17% | 644.83% |
| SOL-USD | RUNE-USD | 2026-01-11 | 77.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | SOL-USD | 2026-01-08 | 77.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | NEAR-USD | 2026-01-10 | 76.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 20.47% | -4.92% | 22.14% | 68.39% | -4.92% | 112.24% |
| SOL-USD | QTUM-USD | 2018-10-29 | 76.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.48% | -3.25% | 32.41% | 82.67% | -3.25% | 86.97% |
| SOL-USD | BTC-USD | 2026-01-11 | 75.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.09% | -0.13% | 8.26% | -16.25% | -19.78% | 8.26% |
| SOL-USD | ETH-USD | 2026-01-10 | 75.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| SOL-USD | KAVA-USD | 2026-01-10 | 75.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | 0.00% | 23.31% | -16.11% | -23.42% | 23.31% |
| SOL-USD | BNB-USD | 2026-01-15 | 79.47% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |

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
<!-- MARKET_REGIME_MATCH_END -->

</details>
<!-- COMPACT_SECTION_END:market_regime -->

<!-- COMPACT_SECTION_START:classic_technical -->
<details>
<summary><strong>📐 Conferma tecnica classica</strong></summary>

<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->
# Classic technical confirmation report

Generato: 2026-08-17 05:31 UTC


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
| BTC | 63.429 $ | -7 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 75,42 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07010 $ | -5 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | -2 | -1 | 0 | 0 | -2 | -7 |
| SOL | -4 | 0 | 0 | +1 | 0 | +1 | 0 | -2 |
| DOGE | -4 | +2 | -1 | -1 | 0 | +1 | -2 | -5 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.227 $ | 64.186 $ | 67.248 $ | 57.748 $ | 1,62% | -0,74% | -17,58% |
| SOL | 74,16 $ | 75,94 $ | 83,81 $ | 64,42 $ | 2,19% | 0,52% | -11,60% |
| DOGE | 0.06961 $ | 0.07117 $ | 0.09075 $ | 0.06797 $ | 2,18% | -3,34% | -33,03% |

## Lettura dettagliata

### BTC

- Prezzo: **63.429 $**
- Score classico: **-7 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 1,62%; distanza supporto 1,93%; distanza resistenza 1,20%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-2** — RSI neutrale 46.5; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.00; volume ratio 0.60
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 46.55 |
| MACD histogram | -126.35682 |
| CMF20 | -0.002 |
| Volume ratio 20 | 0.60 |
| MA20 | 63.813 $ |
| MA50 | 63.581 $ |
| MA100 | 66.703 $ |
| MA200 | 69.242 $ |
| Pendenza MA50 20g | +0,48% |
| Pendenza MA200 60g | -10,38% |
| Bollinger width | 4,42% |
| Bollinger position | 0.36 |

### SOL

- Prezzo: **75,42 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,19%; distanza supporto 1,67%; distanza resistenza 0,71%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 51.3; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.05; volume ratio 0.67
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **+1** — Bullish engulfing
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.30 |
| MACD histogram | 0.18098 |
| CMF20 | 0.050 |
| Volume ratio 20 | 0.67 |
| MA20 | 74,46 $ |
| MA50 | 76,07 $ |
| MA100 | 76,86 $ |
| MA200 | 81,78 $ |
| Pendenza MA50 20g | +2,62% |
| Pendenza MA200 60g | -17,14% |
| Bollinger width | 7,18% |
| Bollinger position | 0.67 |

### DOGE

- Prezzo: **0.07010 $**
- Score classico: **-5 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 2,18%; distanza supporto 0,69%; distanza resistenza 1,55%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-1** — RSI neutrale 46.8; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.04; volume ratio 0.57
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **+1** — Bullish engulfing
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 46.77 |
| MACD histogram | 0.00023 |
| CMF20 | 0.044 |
| Volume ratio 20 | 0.57 |
| MA20 | 0.07000 $ |
| MA50 | 0.07191 $ |
| MA100 | 0.08306 $ |
| MA200 | 0.09017 $ |
| Pendenza MA50 20g | -6,71% |
| Pendenza MA200 60g | -16,97% |
| Bollinger width | 3,74% |
| Bollinger position | 0.54 |

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

Generato: 2026-08-17 05:32 UTC


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
| BTC | 63.429 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 9,84% | Fib 23,6% TESTATO (0) @ 63.595 $ | NEL RANGE | 62.553 $ |
| SOL | 75,42 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 17,08% | Fib 23,6% NON ATTIVO (0) @ 73,56 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.07010 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.07931 $ | n/a | 5,28% | Fib 23,6% NON ATTIVO (0) @ 0.08059 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **8 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **9,84%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 63.595 $** — Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 23.6% a 63.595; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.402 $**
- Breakout 60g: **67.248 $**
- Breakdown 60g: **57.748 $**
- RSI14: **46.57**
- ATR14: **1,62%**
- Volume ratio 20g: **0.60**
- Rendimento 30g: **-0,74%**
- Rendimento 90g: **-17,58%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 1,93% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 66.910 $ | n/a | n/a | 71.619 $ | n/a | 5,49% | 65.572 $ | Due minimi simili a 62.201 $ e 62.227 $. Neckline circa 66.910 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 14 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **8 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **17,08%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 73,56 $** — Swing UP 2026-06-06 60,41 -> 2026-08-09 77,62; livello più vicino 23.6% a 73,56; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Bullish engulfing**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **75,94 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **64,42 $**
- RSI14: **51.39**
- ATR14: **2,19%**
- Volume ratio 20g: **0.67**
- Rendimento 30g: **+0,54%**
- Rendimento 90g: **-11,58%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 6,68% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 78,73 $ | n/a | n/a | 86,76 $ | n/a | 4,38% | 77,15 $ | Due minimi simili a 73,40 $ e 70,69 $. Neckline circa 78,73 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 16 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 5,21% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 31 giorni. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-24 -> 2026-08-12**
- Età formazione: **5 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.07380 $**
- Target teorico: **0.07931 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **5,28%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08059 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 23.6% a 0.08059; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07233 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Bullish engulfing**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07117 $**
- Breakout 60g: **0.09075 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **46.81**
- ATR14: **2,18%**
- Volume ratio 20g: **0.57**
- Rendimento 30g: **-3,33%**
- Rendimento 90g: **-33,02%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.08952 $ | n/a | 13,03% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 3,13% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |

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

Generato: 2026-08-17 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-17**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-01**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,42 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,75%**
- Aderenza live principale: **+68,93%**
- Errore medio live principale: **15,54%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **72**
- Osservazioni inclusive dal bottom: **73**
- Osservazioni da inizio programma/scanner: **46**
- Errore assoluto medio dal bottom: **12,02%**
- Errore assoluto medio da inizio programma: **15,54%**
- Gap firmato medio ultimi 7 giorni: **-17,37%**
- Errore assoluto medio ultimi 7 giorni: **17,37%**
- Gap ultimo giorno: **-19,30%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-19,30%**
- Gap firmato medio 7g: **-17,37%**
- Errore assoluto medio 7g: **17,37%**
- Variazione recente gap: **+0,27%**
- Stato gap: **DISALLINEATO SOTTO IL FRATTALE**
- Trend gap: **SOL e vicino al percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 75,27 $ | 91,15 $ | -17,42% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,42 $ | 93,45 $ | -19,30% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-24 | 90,36 $ | 72,93 $ | 72,36 $ / 75,42 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-31 | 95,75 $ | 77,28 $ | 68,83 $ / 77,28 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-07 | 95,29 $ | 76,90 $ | 68,83 $ / 78,93 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-14 | 93,15 $ | 75,17 $ | 68,83 $ / 78,93 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-21 | 85,55 $ | 69,04 $ | 68,83 $ / 78,93 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-28 | 96,02 $ | 77,49 $ | 64,18 $ / 78,93 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-05 | 107,57 $ | 86,81 $ | 64,18 $ / 89,57 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-12 | 111,67 $ | 90,12 $ | 64,18 $ / 90,12 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-19 | 111,00 $ | 89,58 $ | 64,18 $ / 90,54 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-26 | 118,72 $ | 95,81 $ | 64,18 $ / 96,12 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-02 | 113,54 $ | 91,63 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-09 | 111,96 $ | 90,36 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-16 | 114,26 $ | 92,21 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-23 | 108,81 $ | 87,81 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-30 | 107,93 $ | 87,10 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-07 | 103,74 $ | 83,72 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-14 | 107,22 $ | 86,53 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-21 | 103,78 $ | 83,76 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 34 | 41,18% | 7,04% | 13,89% |
| 14g | 27 | 37,04% | 15,72% | 13,36% |
| 21g | 20 | 25,00% | 26,13% | 15,61% |
| 28g | 13 | 30,77% | 28,85% | 16,94% |
| 35g | 6 | 16,67% | 29,29% | 18,16% |
| 42g | 0 | n/a | n/a | n/a |
| 49g | 0 | n/a | n/a | n/a |
| 56g | 0 | n/a | n/a | n/a |
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

Ultima lettura salvata: **2026-08-17** — SOL 75,42 $, gap -19,30%, somiglianza +57,75%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-17 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.444 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0060% | -0,53% | 1,11 | -3,55% | 0 $ | 0 $ |
| SOL | 75,44 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0056% | -4,07% | 1,31 | +1,92% | 0 $ | 0 $ |
| DOGE | 0.07017 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0098% | +2,30% | 2,45 | -4,25% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0030% | 145,67 mln $ | 0,00 | -14,37% |
| BTC | Bitget | OK | +0,0063% | 2,54 mld $ | 0,04 | +33,79% |
| BTC | Kucoin | OK | +0,0054% | 1,50 mld $ | 0,15 | +2,29% |
| SOL | Kraken | OK | +0,0077% | 21,30 mln $ | 0,53 | +14,76% |
| SOL | Bitget | OK | +0,0069% | 361,80 mln $ | 0,00 | +34,59% |
| SOL | Kucoin | OK | -0,0031% | 244,05 mln $ | 0,44 | +3,97% |
| DOGE | Kraken | OK | +0,0087% | 3,75 mln $ | 0,38 | +6,15% |
| DOGE | Bitget | OK | +0,0100% | 92,31 mln $ | 0,40 | +10,87% |
| DOGE | Kucoin | OK | +0,0100% | 119,70 mln $ | 3,71 | -29,49% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 4, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +67,50% | +6,19% | 0 | n/a | RACCOLTA DATI | 0,00 | +67,50% | +6,19% |
| SOL | +70,00% | +4,64% | 0 | n/a | RACCOLTA DATI | 0,00 | +70,00% | +4,64% |
| DOGE | +67,50% | +14,31% | 0 | n/a | RACCOLTA DATI | 0,00 | +67,50% | +14,31% |

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
Storage persistente: **OK** — ultimo asset: exchange_state_B.tar.gz.
<!-- EXCHANGE_MICROSTRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_microstructure -->

<!-- COMPACT_SECTION_START:exchange_signal_tracker -->
<details>
<summary><strong>🧠 Accuratezza segnali exchange</strong></summary>

<!-- EXCHANGE_SIGNAL_TRACKER_START -->
# Accuratezza dati exchange e microstruttura

Generato: 2026-08-17 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-17 | BTC | 63.443,80 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,11 | -0,53% | -3,55% |
| 2026-08-17 | DOGE | 0.07017 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 2,45 | +2,30% | -4,25% |
| 2026-08-17 | SOL | 75,44 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -4,07% | +1,92% |
| 2026-08-16 | BTC | 63.060,70 | V2.1.3 | OK | 0 | 0 | 0,25 | BASSA | 1,64 | +0,59% | -3,23% |
| 2026-08-16 | DOGE | 0.06977 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,19 | -4,27% | -0,62% |
| 2026-08-16 | SOL | 75,43 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,83 | +1,84% | -2,70% |
| 2026-08-15 | BTC | 63.103,10 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,17 | +7,54% | -2,89% |
| 2026-08-15 | DOGE | 0.07029 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,10 | -0,39% | -0,99% |
| 2026-08-15 | SOL | 75,48 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,20 | +2,43% | +1,48% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
| DOGE | 14g | 2 | +50,00% | +0,35% | -1,97% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

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
| BTC | 63.429 $ | +0.0060% | -5.63% | 1.62 | Misto | 1/5 |
| SOL | 75,42 $ | -0.0072% | -1.18% | 2.71 | Misto | 1/5 |
| DOGE | 0.07010 $ | +0.0100% | -15.14% | 4.71 | Rischio sotto | 2/5 |

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

Generato: 2026-08-17 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D       | Weekly                      | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-----------------------------------------------------|:--------------|:----------------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish                                       | IN_FORMAZIONE | Bullish regolare invalidata | INVALIDATA | La precedente bullish regolare non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.                      |      0 |
| SOL     | Misto / nessuna divergenza                           | CONTESTO      | Hidden bearish              | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| DOGE    | Momentum in miglioramento, divergenza non confermata | CONTESTO      | Misto / nessuna divergenza  | CONTESTO   | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                                        |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish                                       | IN_FORMAZIONE | 63.426 $ / 46,55  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71 | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare invalidata                          | INVALIDATA    | 63.426 $ / 39,68  | n/a                                                               | -0,52%              | 1,21             |      0 |
| SOL     | 1D   | Misto / nessuna divergenza                           | CONTESTO      | 75,40 $ / 51,30   | n/a                                                               | +2,66%              | 6,21             |      0 |
| SOL     | 1W   | Hidden bearish                                       | CONFERMATA    | 75,40 $ / 40,26   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Momentum in miglioramento, divergenza non confermata | CONTESTO      | 0.07007 $ / 46,69 | n/a                                                               | -0,86%              | 2,70             |      0 |
| DOGE    | 1W   | Misto / nessuna divergenza                           | CONTESTO      | 0.07007 $ / 33,14 | n/a                                                               | -3,60%              | -0,25            |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Bullish regolare invalidata / INVALIDATA**: La precedente bullish regolare non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.

### SOL

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Momentum in miglioramento, divergenza non confermata / CONTESTO**: Momentum in miglioramento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **7**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           1 | +100,00%      | +4,98%            | RACCOLTA DATI |      0 |
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

Generato: 2026-08-17 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum       | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:---------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:---------------------------|:-----------|:-------------|
| BTC | 63.429 $ | -4 | DEBOLE | Trend ribassista | Momentum misto | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 62.227 | 65.402 |
| SOL | 75,42 $ | -4 | DEBOLE | Trend misto | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 70,69 | 77,62 |
| DOGE | 0.07010 $ | -2 | NEUTRALE / MISTO | Trend ribassista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 0.06895 | 0.07286 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 46.57 | -126.137 | 63.813 | 63.581 | 69.242 | 0,46% | -10,22% | -2,11% | -17,36% |
| SOL | 51.39 | 0.18225 | 74,46 | 76,07 | 81,78 | 2,43% | -16,87% | -0,05% | -10,44% |
| DOGE | 46.81 | 0.00023 | 0.07000 | 0.07191 | 0.09017 | -6,33% | -16,72% | -3,27% | -31,89% |

## Dettaglio asset

### BTC

- Prezzo: **63.429 $**
- Punteggio tecnico: **-4 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 5.775e+04 -> 6.223e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 46.6.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 23.6% a 63.595; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.227**
- Resistenza più vicina: **65.402**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-03. Neckline stimata: 66.910. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 66.910; target 71.619; distanza dalla neckline 5,49%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-03-29 al 2026-08-03. Neckline stimata: 82.792. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 82.792; target 103.383; distanza dalla neckline 30,53%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-03. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 67.248; target 75.387; distanza dalla neckline 6,02%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 9,84%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 9,84%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 9,84%; prezzo sopra neckline.

### SOL

- Prezzo: **75,42 $**
- Punteggio tecnico: **-4 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 73.4 -> 70.69. Ultimi massimi: 78.73 -> 77.62.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-08-09 77,62; livello più vicino 23.6% a 73,56; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **70,69**
- Resistenza più vicina: **77,62**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 67,92 tra 2026-06-19 e 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,12%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 67,92 dal 2026-06-19 al 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,12%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,12%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,08%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 6,68%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,08%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07010 $**
- Punteggio tecnico: **-2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07117 -> 0.07286.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 46.8.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 23.6% a 0.08059; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.07286**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07380; target 0.07931; distanza dalla neckline 5,28%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.09012; distanza dalla neckline 13,03%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 0.07380; target 0.07931; distanza dalla neckline 5,28%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 3,13%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 3,13%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 3,13%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-08-09 | 63.595 | 62.478 | 61.575 | 60.672 | 59.386 | 23.6% / 63.595 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-08-09 | 73,56 | 71,05 | 69,02 | 66,99 | 64,10 | 23.6% / 73,56 | NON ATTIVO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-08-12 | 0.08059 | 0.08779 | 0.09360 | 0.09942 | 0.10770 | 23.6% / 0.08059 | NON ATTIVO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 16/30 previsioni controllate su 44 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 16/30 previsioni controllate su 44 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 16/30 previsioni controllate su 44 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 44 | 16 | 16/30 [█████░░░░░] | 28 | RACCOLTA DATI | 2026-08-18 / tra 1 giorno |
| SOL | 44 | 16 | 16/30 [█████░░░░░] | 28 | RACCOLTA DATI | 2026-08-18 / tra 1 giorno |
| DOGE | 44 | 16 | 16/30 [█████░░░░░] | 28 | RACCOLTA DATI | 2026-08-18 / tra 1 giorno |

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

Generato: 2026-08-17 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 63.429 $          | 63.429 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07010 $         | 0.07010 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 63.429 $          | 63.429 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07010 $         | 0.07010 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 63.429 $          | 63.429 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07010 $         | 0.07010 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 63.429 $          | 63.429 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07010 $         | 0.07010 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 63.429 $          | 63.429 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07010 $         | 0.07010 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 63.429 $          | 63.444 $        | +0,0227%     |
| Exchange Microstructure | SOL     | price             | OK      | 75,42 $           | 75,44 $         | +0,0212%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07010 $         | 0.07017 $       | +0,0999%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 75,42 $           | 75,42 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 75,42 $           | 75,42 $         | +0,0000%     |

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

Il workflow è tecnicamente coerente nei controlli disponibili.
<!-- DATA_QUALITY_COHERENCE_END -->

</details>
<!-- COMPACT_SECTION_END:data_quality -->
