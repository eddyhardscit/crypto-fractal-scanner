<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-15 05:34 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +2 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +4 | NEUTRALE / COSTRUTTIVO | SOLO TRANCHE PICCOLE / NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+1**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+2**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+4**, spot = **SOLO TRANCHE PICCOLE / NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

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

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,16 / 94,00, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 71,47 / 70,69 / 62,19.

### DOGE

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **SOLO TRANCHE PICCOLE / NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07117 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06835 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,65 $; upside verso EMA200 +48,06%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-15T05:34:43+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-15T05:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-15T05:05:31+00:00 | 2026-08-15T05:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-15T04:45:00+00:00 | 2026-08-15T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-15T04:00:00+00:00 | 2026-08-15T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-15T00:00:00+00:00 | 2026-08-15T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Partial 1R V1 | LINK | 60m | LONG | 7,95 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | LINK | 60m | LONG | 7,95 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ACE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | CAP | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | LINK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | CYS | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,12 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -2,46 | 6,00 | 3,54 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,55 | 6,00 | 4,45 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -1,05 | 6,00 | 4,95 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 0,83 | 6,00 | 5,17 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,19 | 6,00 | 5,81 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | CAP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | CAP | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Long Only V1 | CAP | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | CAP | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | CAP | 60m | LONG | 8,25 | 4,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | CAP | 60m | LONG | 8,25 | 5,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | CAP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | CAP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.634,28 | -3,66% | €-114,07 | €3.000,00 | -3,80% | 5 | 41 | 34,15% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 41 | 1346 | PRIME INDICAZIONI | 100 (mancano 59) |

- Trade del Principale 4H chiusi: **41**; win rate **34,15%**; profit factor **0,72**.
- Expectancy: **€-9,22** per trade; P&L netto: **€-378,20**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.634,28 | €1.282,24 | €3.846,72 | €192,66 | €12,02 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.583,05 | €5.489,59 | €10.979,18 | €213,00 | €-70,68 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 4 | €10.432,40 | €2.016,51 | €6.049,54 | €208,18 | €-23,56 |
| TEST | Main Side Regime Guard V1 | 5 | €10.395,72 | €2.118,53 | €6.355,60 | €155,48 | €27,72 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.355,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.333,88 | €5.360,34 | €10.720,69 | €207,98 | €-69,01 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.296,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €10.288,28 | €1.830,67 | €5.492,01 | €203,41 | €-13,30 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.278,76 | €1.286,79 | €3.860,36 | €205,26 | €-4,74 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.208,98 | €3.676,96 | €7.353,91 | €204,21 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.137,54 | €630,70 | €1.892,11 | €201,74 | €8,61 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €10.124,69 | €1.983,39 | €5.950,17 | €200,92 | €-39,50 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.077,90 | €2.359,26 | €7.077,78 | €201,57 | €-0,42 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.029,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.027,11 | €3.574,44 | €7.148,87 | €151,50 | €-30,10 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €10.014,74 | €1.782,00 | €5.345,99 | €198,00 | €-12,95 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 8 | €9.988,64 | €2.889,80 | €5.779,60 | €199,06 | €-10,93 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €9.985,79 | €592,29 | €1.776,86 | €198,31 | €17,15 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.977,14 | €1.413,45 | €2.826,90 | €49,75 | €25,79 |
| TEST | Doge Ema 1H | 1 | €9.976,16 | €1.155,63 | €3.466,88 | €49,92 | €-8,11 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.971,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €9.960,90 | €1.302,35 | €3.907,04 | €50,01 | €-39,06 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €9.960,13 | €3.797,91 | €7.595,82 | €199,21 | €-15,84 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.918,77 | €1.406,00 | €2.812,00 | €49,49 | €19,71 |
| TEST | Doge Donchian 1H | 1 | €9.904,04 | €1.295,48 | €3.886,44 | €49,75 | €-43,70 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 5 | €9.903,39 | €3.307,41 | €9.922,22 | €149,72 | €-42,68 |
| TEST | Bilanciata 1H V1 | 6 | €9.898,61 | €1.970,97 | €5.912,90 | €147,90 | €-0,46 |
| TEST | Btc Ema 1H | 1 | €9.885,57 | €1.146,03 | €3.438,09 | €49,51 | €-14,41 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.884,81 | €2.099,14 | €4.198,28 | €197,60 | €4,88 |
| TEST | Ampia 4H | 5 | €9.884,28 | €1.961,33 | €3.922,65 | €148,09 | €9,68 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.872,74 | €1.934,03 | €5.802,10 | €195,92 | €-38,52 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 6 | €9.844,01 | €2.647,66 | €5.295,31 | €197,03 | €-10,60 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €9.835,75 | €2.791,09 | €8.373,26 | €99,34 | €-64,02 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.817,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 7 | €9.809,13 | €1.262,84 | €3.788,53 | €193,37 | €-32,07 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €9.809,03 | €2.673,74 | €5.347,47 | €196,09 | €4,85 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €9.805,12 | €1.246,78 | €3.740,33 | €146,18 | €-12,90 |
| TEST | Combo Mean Reversion | 2 | €9.792,12 | €3.892,85 | €7.785,69 | €46,71 | €65,18 |
| TEST | Rapida 1H V2 | 0 | €9.791,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.788,87 | €3.237,84 | €6.475,68 | €195,92 | €-7,10 |
| TEST | Sol Ema 1H | 1 | €9.777,80 | €1.135,84 | €3.407,53 | €49,07 | €-34,06 |
| TEST | Combo Adaptive Runner25 V1 | 8 | €9.767,69 | €2.359,91 | €4.719,82 | €194,56 | €4,66 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €9.766,74 | €1.869,50 | €5.608,49 | €148,65 | €-12,73 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.764,85 | €2.073,66 | €4.147,33 | €195,21 | €4,83 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.760,08 | €3.330,35 | €6.660,69 | €146,06 | €-0,05 |
| TEST | Scanner Bottom15 Short | 5 | €9.760,08 | €3.330,35 | €6.660,69 | €146,06 | €-0,05 |
| TEST | Scanner Bottom20 Short | 5 | €9.760,08 | €3.330,35 | €6.660,69 | €146,06 | €-0,05 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.751,89 | €3.350,59 | €6.701,19 | €194,62 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €9.745,47 | €1.341,76 | €4.025,27 | €97,56 | €0,05 |
| TEST | Forza relativa 1H V2 | 5 | €9.732,38 | €3.372,39 | €6.744,77 | €146,59 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €9.715,77 | €2.977,52 | €5.955,05 | €48,49 | €47,98 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.715,21 | €2.063,12 | €4.126,24 | €194,21 | €4,80 |
| TEST | Rapida 1H V3 Filtered | 6 | €9.702,91 | €1.857,28 | €5.571,84 | €147,68 | €-12,65 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €9.693,87 | €3.317,86 | €6.635,71 | €145,23 | €-0,48 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.679,13 | €3.312,81 | €6.625,62 | €145,01 | €-0,48 |
| TEST | Sol Adaptive 1H | 0 | €9.674,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.669,99 | €1.512,09 | €3.024,18 | €48,39 | €-7,07 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 5 | €9.659,65 | €1.836,52 | €5.509,57 | €98,24 | €-13,88 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 4 | €9.657,64 | €1.539,16 | €3.078,32 | €193,21 | €6,45 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.656,90 | €2.659,21 | €5.318,42 | €192,78 | €-10,40 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.651,72 | €2.305,85 | €4.611,71 | €193,58 | €-7,06 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.622,79 | €3.130,95 | €9.392,84 | €191,07 | €-67,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.604,64 | €3.287,32 | €6.574,63 | €143,89 | €-0,48 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.594,30 | €2.370,73 | €7.112,20 | €191,79 | €-24,26 |
| TEST | Eth Ema 1H | 1 | €9.593,15 | €1.113,68 | €3.341,04 | €48,11 | €-27,07 |
| TEST | Combo Adaptive Partial 1R V1 | 8 | €9.591,54 | €2.774,92 | €5.549,83 | €191,14 | €-10,49 |
| TEST | Combo Adaptive Tp3 V1 | 8 | €9.585,21 | €2.315,82 | €4.631,64 | €190,93 | €4,57 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.537,75 | €2.025,44 | €4.050,87 | €190,67 | €4,71 |
| TEST | Combo Adaptive Quality7 Regime V1 | 4 | €9.536,16 | €1.519,80 | €3.039,60 | €190,78 | €6,37 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.532,08 | €2.231,48 | €6.694,45 | €190,65 | €-0,39 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.493,31 | €3.109,30 | €6.218,60 | €189,88 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.483,21 | €3.105,99 | €6.211,99 | €189,68 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €9.479,92 | €2.569,79 | €5.139,58 | €189,51 | €4,77 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €9.474,38 | €2.568,29 | €5.136,57 | €189,40 | €4,76 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €9.472,28 | €1.241,72 | €3.725,16 | €187,45 | €-31,05 |
| TEST | Master Adaptive V1 | 5 | €9.446,53 | €3.093,98 | €6.187,96 | €188,95 | €0,00 |
| TEST | Combo Trend | 9 | €9.435,42 | €1.377,00 | €2.753,99 | €188,63 | €4,37 |
| TEST | Scanner Top10 Long | 5 | €9.403,80 | €3.171,75 | €6.343,50 | €188,08 | €0,00 |
| TEST | Scanner Top15 Long | 5 | €9.403,80 | €3.171,75 | €6.343,50 | €188,08 | €0,00 |
| TEST | Scanner Top20 Long | 5 | €9.403,80 | €3.171,75 | €6.343,50 | €188,08 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €9.373,51 | €2.555,02 | €5.110,05 | €187,38 | €4,63 |
| TEST | Benchmark trend following EMA 1H | 9 | €9.349,11 | €2.713,64 | €5.427,28 | €186,89 | €3,88 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.345,94 | €2.243,88 | €4.487,75 | €186,79 | €39,44 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.335,02 | €1.786,12 | €5.358,36 | €187,00 | €4,79 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.321,02 | €3.052,87 | €6.105,74 | €186,44 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €9.307,62 | €2.859,77 | €5.719,53 | €186,16 | €0,00 |
| TEST | Combo Scanner | 5 | €9.293,02 | €3.590,77 | €7.181,54 | €186,69 | €-18,25 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.197,04 | €1.748,57 | €5.245,71 | €93,53 | €-13,21 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.194,55 | €2.506,24 | €5.012,48 | €183,80 | €4,55 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.168,38 | €2.069,67 | €4.139,33 | €183,28 | €4,54 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 0 | €9.028,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.009,09 | €2.598,92 | €5.197,83 | €180,38 | €-9,93 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.634,28 | €-378,20 | 41 | 41 | 34,15% | 0,72 | €-9,22 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.583,05 | €660,35 | 60 | 60 | 48,33% | 1,46 | €11,01 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.432,40 | €459,52 | 61 | 61 | 50,82% | 1,35 | €7,53 | 3,35% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.395,72 | €367,24 | 20 | 20 | 50,00% | 1,85 | €18,36 | 2,40% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.355,43 | €355,43 | 33 | 33 | 48,48% | 1,52 | €10,77 | 3,55% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.333,88 | €409,36 | 28 | 28 | 46,43% | 1,71 | €14,62 | 3,63% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.296,26 | €296,26 | 31 | 31 | 51,61% | 1,36 | €9,56 | 2,31% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.288,28 | €304,86 | 107 | 107 | 42,99% | 1,13 | €2,85 | 4,44% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.278,76 | €284,68 | 102 | 102 | 45,10% | 1,14 | €2,79 | 3,64% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.208,98 | €212,94 | 68 | 68 | 44,12% | 1,13 | €3,13 | 7,66% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.137,54 | €130,01 | 44 | 44 | 47,73% | 1,13 | €2,95 | 5,21% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.124,69 | €164,93 | 97 | 97 | 42,27% | 1,07 | €1,70 | 6,52% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.077,90 | €81,91 | 85 | 85 | 38,82% | 1,04 | €0,96 | 5,68% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.029,32 | €29,32 | 6 | 6 | 66,67% | 1,27 | €4,89 | 1,49% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.027,11 | €57,88 | 42 | 42 | 50,00% | 1,07 | €1,38 | 2,94% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.014,74 | €30,88 | 65 | 65 | 46,15% | 1,02 | €0,48 | 4,78% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
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
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,76 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Combo Adaptive | Combo Adaptive | €9.988,64 | €3,02 | 62 | 62 | 40,32% | 1,00 | €0,05 | 5,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.985,79 | €-30,29 | 99 | 99 | 41,41% | 0,99 | €-0,31 | 6,72% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Ema 4H | Trend following EMA | €9.977,14 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Doge Ema 1H | Trend following EMA | €9.976,16 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.971,04 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.960,90 | €2,03 | 6 | 6 | 50,00% | 1,02 | €0,34 | 1,99% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.960,13 | €-23,21 | 53 | 53 | 45,28% | 0,98 | €-0,44 | 6,59% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,80 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.918,77 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.904,04 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 2,06% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.903,39 | €-49,12 | 3 | 3 | 33,33% | 0,13 | €-16,37 | 1,59% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.898,61 | €-98,17 | 93 | 93 | 41,94% | 0,94 | €-1,06 | 6,96% |
| TEST | Btc Ema 1H | Trend following EMA | €9.885,57 | €-98,30 | 8 | 8 | 37,50% | 0,63 | €-12,29 | 1,72% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.884,81 | €-117,96 | 38 | 38 | 39,47% | 0,90 | €-3,10 | 6,54% |
| TEST | Ampia 4H | Confluenza trend | €9.884,28 | €-125,24 | 34 | 34 | 23,53% | 0,86 | €-3,68 | 4,36% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.872,74 | €-88,02 | 61 | 61 | 39,34% | 0,93 | €-1,44 | 6,52% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.844,01 | €-142,63 | 39 | 39 | 35,90% | 0,84 | €-3,66 | 4,45% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.835,75 | €-95,59 | 33 | 33 | 45,45% | 0,88 | €-2,90 | 3,94% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.817,19 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,06% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.809,13 | €-156,53 | 115 | 115 | 36,52% | 0,94 | €-1,36 | 3,95% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.809,03 | €-193,05 | 59 | 59 | 35,59% | 0,87 | €-3,27 | 8,46% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.805,12 | €-179,72 | 64 | 64 | 42,19% | 0,90 | €-2,81 | 4,70% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.792,12 | €-267,90 | 28 | 28 | 35,71% | 0,72 | €-9,57 | 4,73% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.791,89 | €-208,11 | 29 | 26 | 37,93% | 0,74 | €-7,18 | 3,89% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.788,87 | €-198,74 | 25 | 25 | 40,00% | 0,65 | €-7,95 | 2,73% |
| TEST | Sol Ema 1H | Trend following EMA | €9.777,80 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 3,07% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.767,69 | €-234,18 | 69 | 69 | 34,78% | 0,83 | €-3,39 | 6,25% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.766,74 | €-218,33 | 83 | 83 | 49,40% | 0,87 | €-2,63 | 7,17% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.764,85 | €-237,89 | 43 | 43 | 34,88% | 0,81 | €-5,53 | 6,13% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.760,08 | €-235,30 | 46 | 46 | 34,78% | 0,77 | €-5,12 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.760,08 | €-235,30 | 46 | 46 | 34,78% | 0,77 | €-5,12 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.760,08 | €-235,30 | 46 | 46 | 34,78% | 0,77 | €-5,12 | 5,27% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.751,89 | €-244,06 | 41 | 41 | 31,71% | 0,81 | €-5,95 | 4,45% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.745,47 | €-252,25 | 61 | 56 | 44,26% | 0,82 | €-4,14 | 5,74% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.732,38 | €-262,78 | 69 | 66 | 39,13% | 0,88 | €-3,81 | 8,11% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.715,77 | €-327,61 | 68 | 68 | 42,65% | 0,82 | €-4,82 | 6,53% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.715,21 | €-287,51 | 53 | 53 | 39,62% | 0,80 | €-5,42 | 5,80% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.702,91 | €-282,25 | 127 | 127 | 39,37% | 0,90 | €-2,22 | 7,14% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.693,87 | €-301,10 | 38 | 38 | 34,21% | 0,65 | €-7,92 | 5,27% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.679,13 | €-315,85 | 39 | 39 | 33,33% | 0,60 | €-8,10 | 5,27% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.674,16 | €-325,84 | 9 | 9 | 22,22% | 0,17 | €-36,20 | 3,94% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.669,99 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.659,65 | €-325,27 | 56 | 56 | 37,50% | 0,79 | €-5,81 | 8,59% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.657,64 | €-346,97 | 17 | 17 | 35,29% | 0,46 | €-20,41 | 3,78% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.656,90 | €-329,41 | 40 | 40 | 30,00% | 0,76 | €-8,24 | 6,03% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.651,72 | €-338,45 | 37 | 37 | 29,73% | 0,63 | €-9,15 | 5,31% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.622,79 | €-307,51 | 87 | 87 | 42,53% | 0,86 | €-3,53 | 6,10% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.604,64 | €-390,38 | 66 | 66 | 33,33% | 0,72 | €-5,91 | 6,41% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.594,30 | €-377,15 | 67 | 67 | 44,78% | 0,81 | €-5,63 | 5,63% |
| TEST | Eth Ema 1H | Trend following EMA | €9.593,15 | €-377,82 | 10 | 10 | 20,00% | 0,12 | €-37,78 | 4,10% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.591,54 | €-394,65 | 63 | 63 | 38,10% | 0,69 | €-6,26 | 6,07% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.585,21 | €-416,62 | 50 | 50 | 34,00% | 0,62 | €-8,33 | 6,25% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.537,75 | €-464,92 | 60 | 60 | 38,33% | 0,72 | €-7,75 | 7,59% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.536,16 | €-468,38 | 17 | 17 | 23,53% | 0,29 | €-27,55 | 4,99% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.532,08 | €-464,13 | 41 | 41 | 34,15% | 0,50 | €-11,32 | 5,40% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.493,31 | €-502,86 | 41 | 41 | 21,95% | 0,57 | €-12,26 | 6,68% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.483,21 | €-512,96 | 36 | 36 | 27,78% | 0,55 | €-14,25 | 6,27% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.479,92 | €-522,19 | 44 | 44 | 29,55% | 0,61 | €-11,87 | 9,16% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.474,38 | €-527,73 | 48 | 48 | 31,25% | 0,61 | €-10,99 | 9,46% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.472,28 | €-495,53 | 101 | 101 | 39,60% | 0,79 | €-4,91 | 7,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.446,53 | €-549,65 | 38 | 38 | 26,32% | 0,58 | €-14,46 | 6,08% |
| TEST | Combo Trend | Combo Trend | €9.435,42 | €-567,88 | 92 | 92 | 32,61% | 0,77 | €-6,17 | 9,82% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.403,80 | €-593,61 | 40 | 40 | 35,00% | 0,50 | €-14,84 | 9,13% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.403,80 | €-593,61 | 40 | 40 | 35,00% | 0,50 | €-14,84 | 9,13% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.403,80 | €-593,61 | 40 | 40 | 35,00% | 0,50 | €-14,84 | 9,13% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.373,51 | €-628,48 | 40 | 40 | 30,00% | 0,48 | €-15,71 | 8,92% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.349,11 | €-652,13 | 62 | 62 | 29,03% | 0,59 | €-10,52 | 7,38% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.345,94 | €-691,82 | 37 | 37 | 21,62% | 0,53 | €-18,70 | 7,51% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.335,02 | €-667,17 | 43 | 43 | 30,23% | 0,53 | €-15,52 | 7,54% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.321,02 | €-675,22 | 73 | 73 | 47,95% | 0,55 | €-9,25 | 7,33% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.307,62 | €-689,58 | 80 | 80 | 28,75% | 0,64 | €-8,62 | 8,96% |
| TEST | Combo Scanner | Combo Scanner | €9.293,02 | €-686,81 | 65 | 65 | 33,85% | 0,63 | €-10,57 | 10,13% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.197,04 | €-788,60 | 76 | 76 | 30,26% | 0,64 | €-10,38 | 10,56% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.194,55 | €-807,40 | 52 | 52 | 30,77% | 0,39 | €-15,53 | 9,50% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.168,38 | €-833,46 | 43 | 43 | 25,58% | 0,55 | €-19,38 | 9,06% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.028,46 | €-971,54 | 32 | 32 | 15,62% | 0,30 | €-30,36 | 11,05% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.009,09 | €-977,84 | 77 | 77 | 32,47% | 0,47 | €-12,70 | 11,05% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00494 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €11,68 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63098,87000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €0,34 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,04289 | 1,04289 | 1,03001 | 1,38531 | 0,79260 | €139,17 | €417,52 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,07030 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €-0,42 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 1,00494 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €-0,04 |
| Bilanciata 1H V1 | TUT | SHORT | Confluenza trend | 60m | 3,0x | 0,03281 | 0,03281 | 0,03675 | 0,04359 | 0,02494 | €125,03 | €375,08 | €45,01 | €-0,00 |
| 1H Balanced Long No Rhv V1 | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| 1H Balanced Long No Rhv V1 | APR | LONG | Confluenza trend | 60m | 3,0x | 0,49291 | 0,49291 | 0,43376 | 0,33107 | 0,61121 | €131,87 | €395,61 | €47,47 | €0,00 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1182,39901 | 1155,07338 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | SNDK | LONG | Confluenza trend | 60m | 3,0x | 1632,05865 | 1632,05865 | 1586,54905 | 1096,19939 | 1723,07784 | €570,53 | €1.711,58 | €47,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06625 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €4,79 |
| 1H Balanced Short Trend Down Strict V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,03900 | 1,03900 | 1,03001 | 1,38014 | 0,78964 | €138,10 | €414,31 | €0,00 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,07030 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €-8,11 |
| 1H Balanced Short Trend Down Strict V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1866,05671 | 1883,03000 | 1892,92793 | 2478,74534 | 1812,31428 | €23,32 | €69,97 | €1,01 | €-0,64 |
| 1H Balanced Short Trend Down Strict V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 74,71805 | 75,46500 | 75,79399 | 99,25048 | 72,56617 | €1.131,56 | €3.394,68 | €48,88 | €-33,94 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 1,00494 | 1,01986 | 1,33548 | 0,97642 | €37,09 | €111,28 | €1,60 | €0,05 |
| Bilanciata 1H V2 | BEAT | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,96465 | 0,96465 | 1,08040 | 1,28137 | 0,73313 | €124,99 | €374,96 | €45,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07030 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,42 |
| Bilanciata 1H V3 Filtered | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €457,69 | €1.373,07 | €49,01 | €0,00 |
| Bilanciata 1H V3 Filtered | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €127,78 | €383,34 | €46,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €142,15 | €426,45 | €51,17 | €-0,00 |
| 1H Fast Score 6 75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €32,86 | €98,57 | €0,00 | €0,00 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.363,48 | €4.090,45 | €51,61 | €-30,98 |
| 1H Fast Score 6 75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €155,29 | €465,86 | €51,35 | €5,26 |
| 1H Fast Score 6 75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00989 | 0,01019 | 0,00871 | 0,00664 | 0,01167 | €136,89 | €410,68 | €49,28 | €12,42 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €138,37 | €415,11 | €49,81 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €31,98 | €95,95 | €0,00 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.327,23 | €3.981,70 | €50,24 | €-30,16 |
| 1H Fast Score 6 75 No Trend Up V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €151,16 | €453,47 | €49,98 | €5,12 |
| 1H Fast Score 6 75 No Trend Up V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00989 | 0,01019 | 0,00871 | 0,00664 | 0,01167 | €133,25 | €399,76 | €47,97 | €12,09 |
| 1H Fast Score 6 75 Cost Aware V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95974 | 0,95974 | 1,07491 | 1,27485 | 0,78699 | €145,66 | €436,97 | €52,44 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99774 | 1,00494 | 1,00892 | 1,32533 | 0,98098 | €1.572,34 | €4.717,02 | €52,83 | €-34,04 |
| 1H Fast Score 6 75 Cost Aware V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01007 | 0,01019 | 0,00886 | 0,00676 | 0,01188 | €143,17 | €429,50 | €51,54 | €5,22 |
| 1H Fast Score 6 75 Cost Aware V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €155,35 | €466,05 | €51,37 | €5,27 |
| 1H Fast Nohigh Cap75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,07030 | 0,07069 | 0,09286 | 0,06873 | €1.537,89 | €4.613,67 | €51,67 | €-26,00 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €143,81 | €431,44 | €47,91 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €20,17 | €60,51 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €140,04 | €420,12 | €50,41 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €141,48 | €424,43 | €50,93 | €-13,50 |
| 1H Fast No Pepe V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €771,03 | €2.313,08 | €50,17 | €0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €142,21 | €426,63 | €51,20 | €-0,00 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1191,94474 | 1191,94474 | 1171,66933 | 800,58955 | 1222,35785 | €47,86 | €143,59 | €2,44 | €0,00 |
| 1H Fast No Pepe V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €10,42 | €31,26 | €0,35 | €-0,24 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €140,02 | €420,07 | €50,41 | €-10,85 |
| 1H Fast No Pepe V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06539 | 0,06625 | 0,05878 | 0,04392 | 0,07530 | €166,06 | €498,19 | €50,35 | €6,56 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €9,18 | €27,54 | €0,35 | €-0,21 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,68886 | €146,30 | €438,91 | €48,73 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03778 | 0,03778 | 0,03531 | 0,05019 | 0,02871 | €9,36 | €28,07 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1182,39901 | 1182,39901 | 1161,14575 | 794,17800 | 1224,90555 | €15,88 | €47,65 | €0,86 | €0,00 |
| 1H Fast Tp2 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,91916 | 1632,91916 | 1597,68836 | 1096,77737 | 1703,38077 | €753,45 | €2.260,36 | €48,77 | €0,00 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01297 | €124,29 | €372,86 | €44,74 | €-9,63 |
| 1H Fast Tp2 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 510,22784 | €45,10 | €135,30 | €1,71 | €-1,02 |
| 1H Fast Tp2 V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,08248 | €168,46 | €505,38 | €48,56 | €-21,41 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €776,07 | €2.328,22 | €0,00 | €0,00 |
| Rapida 1H V3 Filtered | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €752,55 | €2.257,65 | €48,96 | €0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €136,31 | €408,92 | €49,07 | €-0,00 |
| Rapida 1H V3 Filtered | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,43 | €169,29 | €1,90 | €-1,31 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €119,44 | €358,31 | €43,00 | €-9,25 |
| Rapida 1H V3 Filtered | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,07915 | €16,48 | €49,45 | €4,75 | €-2,10 |
| 1H Fast V3 Cap75 V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €152,00 | €456,00 | €50,63 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €17,79 | €53,38 | €0,00 | €0,00 |
| 1H Fast V3 Cap75 V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03283 | 0,03283 | 0,03677 | 0,04361 | 0,02692 | €139,04 | €417,11 | €50,05 | €-0,00 |
| 1H Fast V3 Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €150,74 | €452,23 | €49,85 | €5,11 |
| 1H Fast V3 Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00989 | 0,01019 | 0,00871 | 0,00664 | 0,01167 | €132,72 | €398,15 | €47,78 | €12,04 |
| 1H Fast V3 Nohigh V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06991 | 0,07030 | 0,07069 | 0,09286 | 0,06873 | €1.375,16 | €4.125,47 | €46,21 | €-23,25 |
| 1H Fast V3 Nohigh V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €11,94 | €35,81 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,88 | €77,64 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €135,40 | €406,20 | €48,74 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.450,98 | €4.352,95 | €48,75 | €-33,56 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €131,59 | €394,76 | €47,37 | €-10,19 |
| 1H Fast V3 Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €757,07 | €2.271,20 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €683,99 | €2.051,96 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €135,06 | €405,19 | €45,82 | €0,00 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €127,85 | €383,56 | €46,03 | €-12,20 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €44,60 | €133,79 | €1,69 | €-1,01 |
| 1H Fast V3 Long Nohigh Cap75 V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,15 | €405,45 | €48,65 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €806,60 | €2.419,81 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,80 | €77,41 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €144,03 | €432,09 | €48,86 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €135,19 | €405,57 | €48,67 | €-12,90 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €42,36 | €127,08 | €0,00 | €0,00 |
| 1H Fast V3 No Esports V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €736,66 | €2.209,98 | €47,93 | €0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €133,42 | €400,27 | €48,03 | €-0,00 |
| 1H Fast V3 No Esports V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €47,04 | €141,11 | €1,58 | €-1,09 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €119,14 | €357,43 | €42,89 | €-9,23 |
| 1H Fast V3 No Esports V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,07915 | €163,10 | €489,29 | €47,02 | €-20,73 |
| 1H Fast V3 No Esports Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €795,15 | €2.385,44 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €718,39 | €2.155,18 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €141,86 | €425,58 | €48,12 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €134,28 | €402,85 | €48,34 | €-12,81 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €46,84 | €140,52 | €1,77 | €-1,06 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €781,18 | €2.343,53 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €757,50 | €2.272,50 | €49,29 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €137,20 | €411,61 | €49,39 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,80 | €170,41 | €1,91 | €-1,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €120,22 | €360,66 | €43,28 | €-9,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,07915 | €16,59 | €49,77 | €4,78 | €-2,11 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.483,05 | €4.449,14 | €49,83 | €-34,30 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.308,04 | €3.924,12 | €49,51 | €-29,72 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,37 | €406,10 | €48,73 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1142,02581 | 782,71250 | 1200,28321 | €802,37 | €2.407,11 | €48,13 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1582,80136 | 1087,36168 | 1673,04985 | €25,50 | €76,51 | €1,71 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.271,08 | €3.813,23 | €48,11 | €-28,88 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €136,42 | €409,26 | €45,11 | €4,62 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00494 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €9,10 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 63098,87000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €0,58 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €169,57 | €339,13 | €40,70 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €-0,00 |
| Forza relativa 1H V1 | SKHYNIX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €79,48 | €158,95 | €3,52 | €0,00 |
| Forza relativa 1H V1 | TUT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,03281 | 0,03281 | 0,03675 | 0,04906 | 0,02415 | €186,76 | €373,52 | €44,82 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €200,27 | €400,55 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €1,08 | €0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02493 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07030 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-37,54 |
| Benchmark Donchian breakout 1H | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €858,65 | €1.717,31 | €52,93 | €0,00 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,46500 | 75,91354 | 111,70349 | 71,72933 | €1.657,45 | €3.314,90 | €53,04 | €-33,14 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07030 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-36,66 |
| Donchian 1H Gb20 120R V1 | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €838,44 | €1.676,87 | €51,68 | €0,00 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,46500 | 75,91354 | 111,70349 | 71,72933 | €1.618,43 | €3.236,85 | €51,79 | €-32,36 |
| Benchmark Bollinger mean reversion 1H | SNDK | SHORT | Bollinger mean reversion | 60m | 2,0x | 1630,10135 | 1630,10135 | 1667,98054 | 2437,00152 | 1573,28257 | €1.043,30 | €2.086,60 | €48,49 | €-0,00 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 0,99263 | 1,00494 | 1,00079 | 0,50128 | 1,01050 | €1.934,23 | €3.868,45 | €0,00 | €47,98 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07030 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €-0,11 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,71 | €0,00 |
| Benchmark trend following EMA 1H | SNDK | LONG | Trend following EMA | 60m | 2,0x | 1632,05865 | 1632,05865 | 1581,49243 | 824,18962 | 1743,30434 | €724,64 | €1.449,29 | €44,90 | €0,00 |
| Benchmark trend following EMA 1H | ETH | SHORT | Trend following EMA | 60m | 2,0x | 1867,89635 | 1883,03000 | 1897,78269 | 2792,50504 | 1802,14639 | €18,13 | €36,25 | €0,58 | €-0,29 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 62898,88771 | 63098,87000 | 63905,26991 | 94033,83712 | 60684,84686 | €27,47 | €54,94 | €0,88 | €-0,17 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €183,61 | €367,22 | €44,07 | €4,46 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €0,00 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | APR | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €209,11 | €418,21 | €50,19 | €0,00 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €13,45 | €26,90 | €0,77 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.146,19 | €2.292,38 | €50,74 | €0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €199,49 | €398,98 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €-0,00 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €-0,05 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €200,12 | €400,25 | €48,03 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,46500 | 75,79399 | 111,70349 | 72,56617 | €21,64 | €43,28 | €0,62 | €-0,43 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | APR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top10 Long | SNDK | LONG | Scanner Top10 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,05 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | APR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top15 Long | SNDK | LONG | Scanner Top15 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,05 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | APR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top20 Long | SNDK | LONG | Scanner Top20 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,05 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €192,28 | €384,55 | €46,15 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,84 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €22,01 | €44,02 | €1,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €199,69 | €399,39 | €47,93 | €4,85 |
| Scanner Top5 Btc Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €180,23 | €360,46 | €43,26 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,79 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €20,63 | €41,26 | €1,12 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €187,18 | €374,37 | €44,92 | €4,55 |
| Scanner Top5 Btc Guard V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €200,65 | €401,31 | €48,16 | €0,00 |
| Scanner Top5 Btc Guard V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €2,48 | €0,00 |
| Scanner Top5 Btc Guard V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €890,44 | €1.780,87 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €198,69 | €397,39 | €47,69 | €4,83 |
| Scanner Top5 Btc Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €183,74 | €367,48 | €44,10 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,80 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €21,03 | €42,07 | €1,14 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €190,83 | €381,65 | €45,80 | €4,63 |
| Scanner Top5 Btc Guard Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €195,99 | €391,97 | €47,04 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €2,42 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €869,73 | €1.739,45 | €47,32 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €194,07 | €388,15 | €46,58 | €4,71 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €203,12 | €406,24 | €48,75 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €2,51 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €901,37 | €1.802,75 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €201,14 | €402,27 | €48,27 | €4,88 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €199,63 | €399,27 | €47,91 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €2,46 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €885,91 | €1.771,82 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €197,68 | €395,37 | €47,44 | €4,80 |
| Scanner Top5 Btc Runner25 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,01 | €370,01 | €44,40 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,81 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,67 | €0,92 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €196,14 | €392,28 | €47,07 | €4,76 |
| Scanner Top5 Btc Tp3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,11 | €370,23 | €44,43 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,81 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,69 | €0,92 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €196,25 | €392,51 | €47,10 | €4,77 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07030 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €-7,07 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €179,75 | €359,50 | €43,14 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07030 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €-0,14 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,71 | €0,00 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1618,90076 | 1618,90076 | 1567,33019 | 817,54488 | 1732,35601 | €12,85 | €25,70 | €0,82 | €0,00 |
| Combo Trend | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02351 | €194,61 | €389,21 | €46,71 | €-0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €185,72 | €371,43 | €44,57 | €4,51 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62826,12271 | 63098,87000 | 62072,20924 | 31727,19197 | 64032,38427 | €1.946,42 | €3.892,84 | €46,71 | €16,90 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 0,99263 | 1,00494 | 1,00079 | 0,50128 | 1,01169 | €1.946,43 | €3.892,85 | €0,00 | €48,28 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,07030 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €-18,25 |
| Combo Scanner | APR | LONG | Combo Scanner | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €186,01 | €372,01 | €44,64 | €0,00 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1721,01048 | €20,29 | €40,58 | €1,16 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €1.034,30 | €2.068,59 | €45,78 | €0,00 |
| Combo Adaptive | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €-0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €-0,15 |
| Combo Adaptive | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,00 | €0,00 |
| Combo Adaptive | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €686,66 | €1.373,32 | €49,73 | €0,00 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €208,34 | €416,67 | €50,00 | €-10,76 |
| Combo Adaptive | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,52871 | 9,52300 | 9,31805 | 4,81200 | 9,95005 | €21,07 | €42,14 | €0,93 | €-0,03 |
| Combo Adaptive Mfe Trail | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €-0,00 |
| Combo Adaptive Mfe Trail | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €15,03 | €30,05 | €0,67 | €0,00 |
| Combo Adaptive Mfe Trail | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €619,25 | €1.238,49 | €44,85 | €0,00 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,07030 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,26 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €187,35 | €374,71 | €44,96 | €-9,67 |
| Combo Adaptive Quality7 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1175,20470 | 1147,33658 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €48,59 | €0,00 |
| Combo Adaptive Quality7 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1632,91916 | 1632,91916 | 1587,62241 | 824,62418 | 1723,51265 | €880,79 | €1.761,58 | €48,87 | €0,00 |
| Combo Adaptive Quality7 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02574 | €203,75 | €407,50 | €48,90 | €-0,00 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01038 | 0,01019 | 0,00913 | 0,00524 | 0,01287 | €196,76 | €393,51 | €47,22 | €-7,06 |
| Combo Adaptive Regime V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,96465 | 0,96465 | 1,08040 | 1,44215 | 0,73313 | €206,23 | €412,46 | €49,50 | €-0,00 |
| Combo Adaptive Regime V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €-0,00 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01038 | 0,01019 | 0,00913 | 0,00524 | 0,01287 | €197,95 | €395,89 | €47,51 | €-7,10 |
| Combo Adaptive Quality7 Regime V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €200,62 | €401,23 | €48,15 | €-10,36 |
| Combo Adaptive Quality7 Regime V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06625 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €12,24 |
| Combo Adaptive Quality7 Regime V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,41758 | 1,43360 | 1,24747 | 0,71588 | 1,75780 | €198,74 | €397,48 | €47,70 | €4,49 |
| Combo Adaptive Quality7 Regime V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €919,84 | €1.839,67 | €46,79 | €0,00 |
| Combo Adaptive Long Only V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | APR | LONG | Combo Adaptive | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €199,74 | €399,48 | €47,94 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,80 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €205,31 | €410,62 | €49,27 | €-10,60 |
| Combo Adaptive Long Only V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1652,37083 | 1652,37083 | 1605,97924 | 834,44727 | 1745,15401 | €13,30 | €26,61 | €0,75 | €0,00 |
| Combo Adaptive Partial 1R V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €-0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €-0,14 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,00 | €0,00 |
| Combo Adaptive Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €659,36 | €1.318,73 | €47,75 | €0,00 |
| Combo Adaptive Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €200,05 | €400,11 | €48,01 | €-10,33 |
| Combo Adaptive Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,52871 | 9,52300 | 9,31805 | 4,81200 | 9,95005 | €20,23 | €40,46 | €0,89 | €-0,02 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €203,17 | €406,34 | €48,76 | €-10,49 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06625 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €12,40 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,41758 | 1,43360 | 1,24747 | 0,71588 | 1,75780 | €201,27 | €402,54 | €48,31 | €4,55 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €931,55 | €1.863,10 | €47,39 | €0,00 |
| Combo Adaptive Runner25 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive Runner25 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €-0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €-0,14 |
| Combo Adaptive Runner25 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,00 | €0,00 |
| Combo Adaptive Runner25 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,35 | €34,70 | €1,24 | €0,00 |
| Combo Adaptive Runner25 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €204,60 | €409,21 | €49,10 | €-0,00 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €197,77 | €395,55 | €47,47 | €4,80 |
| Combo Adaptive Tp3 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive Tp3 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €-0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €-0,14 |
| Combo Adaptive Tp3 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,00 | €0,00 |
| Combo Adaptive Tp3 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,03 | €34,05 | €1,22 | €0,00 |
| Combo Adaptive Tp3 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €194,08 | €388,16 | €46,58 | €4,71 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 62835,53038 | 63098,87000 | 63740,36202 | 83466,52952 | 61025,86711 | €1.146,03 | €3.438,09 | €49,51 | €-14,41 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63098,87000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €25,79 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63098,87000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €19,71 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 74,71805 | 75,46500 | 75,79399 | 99,25048 | 72,56617 | €1.135,84 | €3.407,53 | €49,07 | €-34,06 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 74,71805 | 75,46500 | 75,67444 | 99,25048 | 72,80527 | €1.302,35 | €3.907,04 | €50,01 | €-39,06 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1867,89635 | 1883,03000 | 1894,79405 | 2481,18898 | 1814,10093 | €1.113,68 | €3.341,04 | €48,11 | €-27,07 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,07030 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €-8,11 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06952 | 0,07030 | 0,07041 | 0,09234 | 0,06774 | €1.295,48 | €3.886,44 | €49,75 | €-43,70 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,13 | €396,27 | €47,55 | €0,00 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,93 | €73,85 | €1,65 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €626,90 | €1.253,80 | €44,76 | €0,00 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,48 | €398,96 | €47,88 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €0,00 |
| Master Adaptive No Alt V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68062 | 829,90965 | 1732,79507 | €22,94 | €45,88 | €1,25 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €201,41 | €402,81 | €48,34 | €-10,40 |
| Master Adaptive Strict3 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €190,97 | €381,94 | €45,83 | €0,00 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1167,82027 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €0,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1655,75286 | 1655,75286 | 1602,89078 | 836,15519 | 1761,47701 | €734,74 | €1.469,49 | €46,92 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €4,54 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €202,38 | €404,77 | €48,57 | €0,00 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €15,69 | €31,37 | €0,90 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.101,72 | €2.203,44 | €48,77 | €0,00 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €195,50 | €391,00 | €46,92 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,43 | €72,87 | €1,62 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €618,57 | €1.237,14 | €44,16 | €0,00 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,43360 | 1,15611 | 0,66345 | 1,78672 | €188,92 | €377,85 | €45,34 | €34,47 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,23400 | 55,05283 | 28,20787 | 58,27020 | €24,55 | €49,10 | €0,71 | €0,33 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1165,32878 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,00 |
| Master Adaptive Runner25 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54904 | 824,18962 | 1768,58749 | €850,90 | €1.701,80 | €47,45 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06625 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €4,64 |
| Combo Adaptive Side Regime Guard V1 | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,07030 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €-18,71 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €-2,19 |
| Combo Adaptive Side Regime Guard V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01249 | €208,05 | €416,11 | €49,93 | €5,05 |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive Gb20 Be V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive Gb20 Be V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,12 | €398,23 | €47,79 | €0,00 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,11 | €74,22 | €1,65 | €0,00 |
| Master Adaptive Gb20 Be V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €630,00 | €1.260,01 | €44,98 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive Gb20 Partial V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,90 | €397,81 | €47,74 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,07 | €74,14 | €1,65 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €629,33 | €1.258,67 | €44,93 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93367 | 0,93367 | 1,04571 | 1,24023 | 0,76561 | €135,90 | €407,70 | €48,92 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €143,50 | €430,49 | €51,66 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €63,81 | €191,43 | €2,14 | €-1,48 |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01007 | 0,01019 | 0,00886 | 0,00676 | 0,01188 | €134,46 | €403,39 | €48,41 | €4,90 |
| 1H Fast V3 Nohigh Regime Guard V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €153,03 | €459,10 | €50,60 | €5,19 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00494 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €12,26 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63098,87000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €15,46 |
| Main Side Regime Guard V1 | BEAT | SHORT | Confluenza trend | 240m | 3,0x | 1,03900 | 1,03900 | 1,03900 | 1,38014 | 0,78964 | €144,10 | €432,31 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend Side Regime Guard V1 | BEAT | SHORT | Combo Trend | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €209,53 | €419,07 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07030 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-28,60 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00494 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €-1,50 |
| Combo Trend Side Regime Guard V1 | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,07030 | 0,07069 | 0,09286 | 0,06873 | €1.499,62 | €4.498,86 | €50,39 | €-25,36 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €140,23 | €420,70 | €46,71 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €19,67 | €59,00 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €136,56 | €409,67 | €49,16 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €137,96 | €413,87 | €49,66 | €-13,16 |
| 1H Balanced V3 Long Only V1 | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07030 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,39 |
| 1H Balanced V3 Long Only V1 | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €432,90 | €1.298,70 | €46,36 | €0,00 |
| 1H Balanced V3 Long Only V1 | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €120,86 | €362,58 | €43,51 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,04 | €402,07 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €-0,05 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,68 | €403,35 | €48,40 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,46500 | 75,79399 | 111,70349 | 72,56617 | €21,81 | €43,62 | €0,63 | €-0,44 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,34 | €402,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €-0,05 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,98 | €403,97 | €48,48 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,46500 | 75,79399 | 111,70349 | 72,56617 | €21,84 | €43,69 | €0,63 | €-0,44 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-54,60 | -1,14 | STOP |
| 1H Fast V3 No Esports Stress Guard V1 | SOL | SHORT | 2026-08-15T03:07:29+00:00 | 75,91019 | €-76,04 | -1,53 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-5,60 | -1,14 | STOP |
| 1H Fast V3 Nohigh Regime Guard V1 | XRP | SHORT | 2026-08-15T03:07:29+00:00 | 1,00892 | €-0,83 | -1,61 | STOP_GAP_STRESS |
| 1H Fast V3 Nohigh Regime Guard V1 | SOL | SHORT | 2026-08-15T03:07:29+00:00 | 75,91019 | €-78,87 | -1,53 | STOP_GAP_STRESS |
| 1H Fast V3 Cap75 V1 | XRP | SHORT | 2026-08-15T03:07:29+00:00 | 1,00892 | €-80,61 | -1,61 | STOP_GAP_STRESS |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-57,05 | -1,14 | STOP |
| Rapida 1H V3 Filtered | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-5,56 | -1,14 | STOP |
| 1H Fast Tp2 V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07055 | €-1,20 | -1,60 | STOP_GAP_STRESS |
| 1H Fast Tp2 V1 | SOL | SHORT | 2026-08-15T03:07:29+00:00 | 75,91019 | €-74,38 | -1,53 | STOP_GAP_STRESS |
| 1H Fast Score 6 75 V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-59,29 | -1,14 | STOP |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-57,71 | -1,14 | STOP |

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

Generato: 2026-08-15 05:34 UTC


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

Segnali totali salvati: **108**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-15 | BTC | 63.058,07 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-15 | DOGE | 0.07017 | +4 | +4 | +3 | +2 | +1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-15 | SOL | 75,40 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-14 | BTC | 62.749,25 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-14 | DOGE | 0.06940 | +2 | +4 | +3 | +2 | 0 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-14 | SOL | 75,41 | +3 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-11 | BTC | 63.889,59 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-11 | DOGE | 0.06985 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-11 | SOL | 75,73 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-10 | BTC | 64.966,07 | +6 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-10 | DOGE | 0.06975 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-10 | SOL | 76,57 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 36 | 35 | 34 | 34 | 33 | 31 | 28 | 24 | 17 | 8 | 0 | 0 |
| SOL | 36 | 35 | 34 | 34 | 33 | 31 | 28 | 24 | 17 | 8 | 0 | 0 |
| DOGE | 36 | 35 | 34 | 34 | 33 | 31 | 28 | 24 | 17 | 8 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-17 | 30g | 2026-08-16 | domani |
| SOL | 2026-07-17 | 30g | 2026-08-16 | domani |
| DOGE | 2026-07-17 | 30g | 2026-08-16 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 33 | 48,48% | +0,01% | -0,03% | PRIMA CALIBRAZIONE |
| BTC | 2g | 32 | 43,75% | +0,02% | -0,12% | PRIMA CALIBRAZIONE |
| BTC | 3g | 32 | 37,50% | -0,14% | -0,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | 31 | 29,03% | -0,05% | -0,46% | PRIMA CALIBRAZIONE |
| BTC | 7g | 29 | 41,38% | +0,14% | -0,23% | FEEDBACK RAPIDO |
| BTC | 10g | 26 | 46,15% | +0,44% | +0,09% | FEEDBACK RAPIDO |
| BTC | 14g | 22 | 40,91% | -0,03% | -0,19% | FEEDBACK RAPIDO |
| BTC | 21g | 15 | 26,67% | -0,46% | -0,74% | FEEDBACK RAPIDO |
| BTC | 30g | 8 | 87,50% | +0,47% | +0,85% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 28 | 50,00% | +0,01% | -0,21% | FEEDBACK RAPIDO |
| SOL | 2g | 27 | 44,44% | -0,01% | -0,27% | FEEDBACK RAPIDO |
| SOL | 3g | 27 | 44,44% | +0,09% | -0,24% | FEEDBACK RAPIDO |
| SOL | 5g | 26 | 50,00% | -0,08% | -0,29% | FEEDBACK RAPIDO |
| SOL | 7g | 24 | 62,50% | +0,05% | +0,27% | FEEDBACK RAPIDO |
| SOL | 10g | 21 | 47,62% | -0,40% | -0,03% | FEEDBACK RAPIDO |
| SOL | 14g | 18 | 55,56% | -1,80% | +0,22% | FEEDBACK RAPIDO |
| SOL | 21g | 14 | 57,14% | -2,85% | -0,16% | FEEDBACK RAPIDO |
| SOL | 30g | 7 | 42,86% | -1,44% | -1,09% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 33 | 42,42% | -0,02% | -0,03% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 32 | 43,75% | -0,14% | -0,15% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 32 | 40,62% | -0,35% | -0,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 31 | 51,61% | -0,60% | +0,21% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 29 | 62,07% | -0,92% | +0,60% | FEEDBACK RAPIDO |
| DOGE | 10g | 26 | 53,85% | -1,52% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 14g | 23 | 65,22% | -2,28% | +1,79% | FEEDBACK RAPIDO |
| DOGE | 21g | 17 | 88,24% | -3,42% | +3,42% | FEEDBACK RAPIDO |
| DOGE | 30g | 8 | 100,00% | -4,42% | +4,42% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 33 | 48,48% | +0,01% | -0,03% | -0,30% | +0,55% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | -0,01% | -0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | -0,01% | -0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 31 | 51,61% | -0,04% | -0,04% | -0,36% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 30 | 33,33% | +0,15% | -0,41% | -0,17% | +0,67% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 5 | 0,00% | +0,71% | -0,71% | +0,08% | +1,00% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 32 | 43,75% | +0,02% | -0,12% | -0,46% | +0,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 30 | 46,67% | -0,09% | -0,09% | -0,57% | +0,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 29 | 44,83% | +0,18% | -0,38% | -0,27% | +0,89% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 32 | 37,50% | -0,14% | -0,36% | -1,40% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | -0,09% | -0,09% | -1,39% | +1,46% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,27% | -0,46% | -1,13% | +1,83% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 31 | 29,03% | -0,05% | -0,46% | -2,10% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 33 | 39,39% | -0,04% | -0,04% | -2,06% | +2,11% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 33 | 39,39% | -0,04% | -0,04% | -2,06% | +2,11% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 29 | 41,38% | +0,03% | +0,03% | -2,05% | +2,08% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 28 | 39,29% | +0,15% | -0,72% | -1,82% | +2,36% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 29 | 41,38% | +0,14% | -0,23% | -2,28% | +2,56% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | +0,10% | +0,10% | -2,27% | +2,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | +0,10% | +0,10% | -2,27% | +2,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | +0,31% | +0,31% | -2,23% | +2,59% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 26 | 34,62% | +0,55% | -0,78% | -1,98% | +2,85% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 26 | 46,15% | +0,44% | +0,09% | -2,52% | +3,03% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 28 | 53,57% | +0,24% | +0,24% | -2,56% | +3,01% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 28 | 53,57% | +0,24% | +0,24% | -2,56% | +3,01% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 24 | 62,50% | +0,62% | +0,62% | -2,41% | +3,11% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 23 | 34,78% | +0,54% | -0,19% | -2,21% | +3,40% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 22 | 40,91% | -0,03% | -0,19% | -2,99% | +3,38% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 24 | 41,67% | -0,15% | -0,15% | -3,01% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 24 | 41,67% | -0,15% | -0,15% | -3,01% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 20 | 50,00% | +0,31% | +0,31% | -2,73% | +3,51% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 19 | 57,89% | +0,14% | +0,12% | -2,63% | +3,75% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 3 | 66,67% | +0,00% | -0,00% | -1,93% | +3,08% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 15 | 26,67% | -0,46% | -0,74% | -3,20% | +3,96% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 17 | 41,18% | -0,53% | -0,53% | -3,26% | +3,80% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 17 | 41,18% | -0,53% | -0,53% | -3,26% | +3,80% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 13 | 46,15% | -0,27% | -0,27% | -2,88% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 14 | 28,57% | -0,22% | +0,06% | -2,93% | +4,14% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 8 | 87,50% | +0,47% | +0,85% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 7 | 42,86% | +0,34% | -0,81% | -2,41% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 33 | 42,42% | -0,02% | -0,03% | -0,48% | +0,72% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 35 | 54,29% | -0,13% | +0,22% | -0,61% | +0,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 35 | 54,29% | -0,13% | +0,22% | -0,61% | +0,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 33 | 54,55% | -0,02% | +0,11% | -0,52% | +0,71% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 23 | 39,13% | +0,22% | -0,22% | -0,30% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 32 | 43,75% | -0,14% | -0,15% | -0,79% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,26% | +0,01% | -0,91% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,26% | +0,01% | -0,91% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,36% | +0,09% | -0,96% | +0,77% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 30 | 60,00% | -0,30% | +0,30% | -0,91% | +0,61% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,17% | -0,17% | -0,49% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 32 | 40,62% | -0,35% | -0,00% | -1,84% | +2,02% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 32 | 50,00% | -0,71% | +0,13% | -1,90% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 22 | 40,91% | -0,10% | +0,10% | -1,86% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 31 | 51,61% | -0,60% | +0,21% | -2,69% | +2,41% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 33 | 48,48% | -0,69% | +0,09% | -2,75% | +2,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,69% | +0,09% | -2,75% | +2,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 31 | 48,39% | -0,70% | +0,06% | -2,76% | +2,11% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 29 | 62,07% | -0,92% | +0,60% | -3,22% | +2,52% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 31 | 58,06% | -1,01% | +0,37% | -3,30% | +2,42% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 31 | 58,06% | -1,01% | +0,37% | -3,30% | +2,42% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 29 | 58,62% | -1,01% | +0,32% | -3,34% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,93% | +0,93% | -3,27% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,97% | +0,62% | -0,19% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 26 | 53,85% | -1,52% | +0,88% | -4,06% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 28 | 53,57% | -1,54% | +0,72% | -4,09% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 28 | 53,57% | -1,54% | +0,72% | -4,09% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 26 | 53,85% | -1,59% | +0,71% | -4,14% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 28 | 67,86% | -1,54% | +1,54% | -4,09% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 20 | 65,00% | -1,32% | +1,32% | -4,00% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 23 | 65,22% | -2,28% | +1,79% | -4,99% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 24 | 66,67% | -2,37% | +1,54% | -5,06% | +2,62% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 24 | 66,67% | -2,37% | +1,54% | -5,06% | +2,62% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 22 | 68,18% | -2,44% | +1,53% | -5,18% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 24 | 75,00% | -2,37% | +2,37% | -5,06% | +2,62% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 17 | 88,24% | -3,42% | +3,42% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 17 | 94,12% | -3,42% | +3,54% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 17 | 94,12% | -3,42% | +3,54% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 15 | 100,00% | -3,71% | +3,84% | -6,24% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 17 | 88,24% | -3,42% | +3,42% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 16 | 87,50% | -3,30% | +3,30% | -5,81% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 7 | 100,00% | -4,17% | +4,17% | -6,85% | +2,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 28 | 50,00% | +0,01% | -0,21% | -0,47% | +0,70% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 31 | 58,06% | -0,28% | -0,00% | -0,72% | +0,37% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,16% | -0,10% | -0,63% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -0,11% | +0,03% | -0,67% | +0,52% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 33 | 51,52% | -0,09% | -0,02% | -0,58% | +0,52% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 27 | 44,44% | -0,01% | -0,27% | -0,68% | +0,91% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,27% | -0,11% | -0,98% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,21% | -0,13% | -0,90% | +0,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 28 | 46,43% | -0,19% | -0,16% | -0,91% | +0,74% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 32 | 40,62% | -0,15% | -0,20% | -0,81% | +0,78% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 27 | 44,44% | +0,09% | -0,24% | -1,86% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 30 | 43,33% | -0,33% | -0,07% | -2,19% | +1,67% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 33 | 42,42% | -0,27% | -0,10% | -2,10% | +1,83% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 28 | 42,86% | -0,22% | -0,29% | -2,02% | +1,85% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 32 | 43,75% | -0,20% | -0,17% | -2,04% | +1,90% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 26 | 50,00% | -0,08% | -0,29% | -2,64% | +2,65% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 29 | 51,72% | -0,32% | -0,08% | -2,93% | +2,34% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 32 | 50,00% | -0,22% | -0,14% | -2,84% | +2,48% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 27 | 48,15% | -0,42% | -0,15% | -2,81% | +2,45% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 32 | 46,88% | -0,28% | -0,24% | -2,88% | +2,55% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 24 | 62,50% | +0,05% | +0,27% | -3,15% | +3,18% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 27 | 66,67% | -0,35% | +0,50% | -3,45% | +2,89% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 30 | 66,67% | -0,33% | +0,46% | -3,37% | +2,99% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 25 | 60,00% | -0,08% | +0,01% | -3,31% | +3,02% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 31 | 35,48% | -0,30% | -0,36% | -3,37% | +3,01% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 21 | 47,62% | -0,40% | -0,03% | -3,99% | +3,43% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | -0,49% | +0,41% | -4,36% | +3,07% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 27 | 51,85% | -0,46% | +0,39% | -4,25% | +3,17% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 22 | 45,45% | -0,06% | -0,31% | -4,21% | +3,24% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 28 | 53,57% | -0,56% | +0,39% | -4,27% | +3,18% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,28% | +0,28% | -3,99% | +3,52% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 18 | 55,56% | -1,80% | +0,22% | -5,17% | +3,41% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 20 | 75,00% | -1,06% | +0,82% | -5,42% | +3,17% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 23 | 78,26% | -1,32% | +1,11% | -5,22% | +3,27% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | -0,81% | -0,62% | -5,08% | +3,39% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 24 | 45,83% | -1,44% | +0,59% | -5,29% | +3,28% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 16 | 50,00% | -0,70% | +0,70% | -5,23% | +3,76% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 14 | 57,14% | -2,85% | -0,16% | -7,27% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 13 | 69,23% | -2,76% | +1,54% | -7,29% | +2,50% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 16 | 75,00% | -2,76% | +1,77% | -7,06% | +2,77% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 11 | 27,27% | -2,77% | -1,23% | -7,01% | +2,73% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 17 | 64,71% | -2,55% | +0,13% | -7,06% | +2,81% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 9 | 77,78% | -0,96% | +0,96% | -6,82% | +3,24% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 7 | 42,86% | -1,44% | -1,09% | -7,86% | +2,87% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 6 | 83,33% | -2,07% | +1,15% | -8,21% | +2,50% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 8 | 75,00% | -1,54% | +0,85% | -8,00% | +2,71% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,55% | -0,85% | -8,00% | +2,76% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 8 | 37,50% | -1,54% | -0,79% | -8,00% | +2,71% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 1 | 100,00% | -0,79% | +0,79% | -6,98% | +3,59% | FEEDBACK RAPIDO |
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

Generato: 2026-08-15 05:34 UTC

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
| BTC | 36 | PRIMA CALIBRAZIONE | 35 | 6 | 0 | 0 | Famiglia statistica | 1g | 51,43% | -0,01% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 36 | PRIMA CALIBRAZIONE | 33 | 8 | 0 | 0 | Tecnico | 1g | 51,52% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 36 | PRIMA CALIBRAZIONE | 35 | 10 | 0 | 0 | Famiglia statistica | 1g | 54,29% | +0,22% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 5 | 0,00% | -0,71% | +0,71% | +0,08% | +1,00% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 35 | 51,43% | -0,01% | -0,01% | -0,31% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 30 | 33,33% | -0,41% | +0,15% | -0,17% | +0,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 29 | 44,83% | -0,38% | +0,18% | -0,27% | +0,89% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 29 | 34,48% | -0,46% | +0,27% | -1,13% | +1,83% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 33 | 39,39% | -0,04% | -0,04% | -2,06% | +2,11% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 28 | 39,29% | -0,72% | +0,15% | -1,82% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 31 | 51,61% | +0,10% | +0,10% | -2,27% | +2,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 26 | 34,62% | -0,78% | +0,55% | -1,98% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 28 | 53,57% | +0,24% | +0,24% | -2,56% | +3,01% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 23 | 34,78% | -0,19% | +0,54% | -2,21% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 3 | 66,67% | -0,00% | +0,00% | -1,93% | +3,08% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 24 | 41,67% | -0,15% | -0,15% | -3,01% | +3,32% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 19 | 57,89% | +0,12% | +0,14% | -2,63% | +3,75% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 17 | 41,18% | -0,53% | -0,53% | -3,26% | +3,80% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 14 | 28,57% | +0,06% | -0,22% | -2,93% | +4,14% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 7 | 42,86% | -0,81% | +0,34% | -2,41% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 23 | 39,13% | -0,22% | +0,22% | -0,30% | +0,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 35 | 54,29% | +0,22% | -0,13% | -0,61% | +0,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 30 | 50,00% | +0,12% | -0,12% | -0,60% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 22 | 50,00% | -0,17% | +0,17% | -0,49% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 34 | 47,06% | +0,01% | -0,26% | -0,91% | +0,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 30 | 60,00% | +0,30% | -0,30% | -0,91% | +0,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 22 | 40,91% | +0,10% | -0,10% | -1,86% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 34 | 47,06% | -0,09% | -0,46% | -1,94% | +1,85% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 30 | 50,00% | +0,49% | -0,49% | -2,02% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,40% | -0,40% | -2,68% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 33 | 48,48% | +0,09% | -0,69% | -2,75% | +2,26% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 30 | 63,33% | +0,75% | -0,75% | -2,89% | +2,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,93% | -0,93% | -3,27% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 31 | 58,06% | +0,37% | -1,01% | -3,30% | +2,42% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,62% | +0,97% | -0,19% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 30 | 63,33% | +1,05% | -1,05% | -3,36% | +2,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 20 | 65,00% | +1,32% | -1,32% | -4,00% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 28 | 53,57% | +0,72% | -1,54% | -4,09% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 28 | 67,86% | +1,54% | -1,54% | -4,09% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 20 | 70,00% | +2,09% | -2,09% | -4,80% | +3,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 24 | 66,67% | +1,54% | -2,37% | -5,06% | +2,62% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 24 | 75,00% | +2,37% | -2,37% | -5,06% | +2,62% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 16 | 87,50% | +3,30% | -3,30% | -5,81% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 17 | 94,12% | +3,54% | -3,42% | -5,95% | +2,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 17 | 88,24% | +3,42% | -3,42% | -5,95% | +2,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 7 | 100,00% | +4,17% | -4,17% | -6,85% | +2,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 8 | 100,00% | +4,42% | -4,42% | -7,00% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 8 | 100,00% | +4,42% | -4,42% | -7,00% | +2,60% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 31 | 58,06% | -0,00% | -0,28% | -0,72% | +0,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 33 | 51,52% | -0,02% | -0,09% | -0,58% | +0,52% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 30 | 50,00% | -0,11% | -0,27% | -0,98% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 32 | 40,62% | -0,20% | -0,15% | -0,81% | +0,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 30 | 43,33% | -0,07% | -0,33% | -2,19% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 32 | 43,75% | -0,17% | -0,20% | -2,04% | +1,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 29 | 51,72% | -0,08% | -0,32% | -2,93% | +2,34% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,24% | -0,28% | -2,88% | +2,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 27 | 66,67% | +0,50% | -0,35% | -3,45% | +2,89% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 31 | 35,48% | -0,36% | -0,30% | -3,37% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,28% | -0,28% | -3,99% | +3,52% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,41% | -0,49% | -4,36% | +3,07% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 28 | 53,57% | +0,39% | -0,56% | -4,27% | +3,18% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 16 | 50,00% | +0,70% | -0,70% | -5,23% | +3,76% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 20 | 75,00% | +0,82% | -1,06% | -5,42% | +3,17% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 24 | 45,83% | +0,59% | -1,44% | -5,29% | +3,28% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 9 | 77,78% | +0,96% | -0,96% | -6,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 13 | 69,23% | +1,54% | -2,76% | -7,29% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 17 | 64,71% | +0,13% | -2,55% | -7,06% | +2,81% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 1 | 100,00% | +0,79% | -0,79% | -6,98% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 6 | 83,33% | +1,15% | -2,07% | -8,21% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 8 | 37,50% | -0,79% | -1,54% | -8,00% | +2,71% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 33 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 33 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 35 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 13 | 15,38% | -0,90% |
| BTC | BREVE | Famiglia statistica | 103 | 49,51% | -0,02% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 88 | 37,50% | -0,41% |
| BTC | SETTIMANALE | Classic technical | 12 | 8,33% | -1,47% |
| BTC | SETTIMANALE | Famiglia statistica | 92 | 47,83% | +0,09% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 77 | 36,36% | -0,58% |
| BTC | SWING | Classic technical | 3 | 66,67% | -0,00% |
| BTC | SWING | Famiglia statistica | 41 | 41,46% | -0,31% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 33 | 45,45% | +0,09% |
| BTC | MEDIO | Famiglia statistica | 8 | 75,00% | +0,47% |
| BTC | MEDIO | Tecnico | 7 | 42,86% | -0,81% |
| DOGE | BREVE | Classic technical | 67 | 43,28% | -0,10% |
| DOGE | BREVE | Famiglia statistica | 103 | 49,51% | +0,05% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 90 | 53,33% | +0,31% |
| DOGE | SETTIMANALE | Classic technical | 63 | 57,14% | +0,87% |
| DOGE | SETTIMANALE | Famiglia statistica | 92 | 53,26% | +0,38% |
| DOGE | SETTIMANALE | Microstruttura exchange | 9 | 66,67% | +0,55% |
| DOGE | SETTIMANALE | Tecnico | 88 | 64,77% | +1,10% |
| DOGE | SWING | Classic technical | 36 | 77,78% | +2,63% |
| DOGE | SWING | Famiglia statistica | 41 | 78,05% | +2,37% |
| DOGE | SWING | Microstruttura exchange | 4 | 100,00% | +0,61% |
| DOGE | SWING | Tecnico | 41 | 80,49% | +2,80% |
| DOGE | MEDIO | Classic technical | 7 | 100,00% | +4,17% |
| DOGE | MEDIO | Famiglia statistica | 8 | 100,00% | +4,42% |
| DOGE | MEDIO | Tecnico | 8 | 100,00% | +4,42% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 91 | 50,55% | -0,06% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 97 | 45,36% | -0,13% |
| SOL | SETTIMANALE | Classic technical | 62 | 50,00% | +0,06% |
| SOL | SETTIMANALE | Famiglia statistica | 80 | 57,50% | +0,27% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 4 | 0,00% | -4,09% |
| SOL | SETTIMANALE | Tecnico | 91 | 45,05% | -0,09% |
| SOL | SWING | Classic technical | 25 | 60,00% | +0,79% |
| SOL | SWING | Famiglia statistica | 33 | 72,73% | +1,10% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 41 | 53,66% | +0,40% |
| SOL | MEDIO | Classic technical | 1 | 100,00% | +0,79% |
| SOL | MEDIO | Famiglia statistica | 6 | 83,33% | +1,15% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 8 | 37,50% | -0,79% |

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
| BTC     |         36 |               8 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         36 |               8 |          28 | RACCOLTA DATI | 12,50%           | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         36 |               8 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | MEDIO          | leva da limitare; 2x/3x solo con invalidazione chiara                   |
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

Generato: 2026-08-15 05:34 UTC


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
| SOL | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,16 / 94,00, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 71,47 / 70,69 / 62,19. |
| DOGE | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | SOLO TRANCHE PICCOLE / NO LEVA | Sopra 0.07117 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante. | Sotto 0.06835 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +2 | +4 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| SOL | +3 | +2 | +4 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |
| DOGE | +3 | +2 | +4 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +4 |

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

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 19. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +8,63%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 19, positivi 30g 73,68%, return p50 +8,98%.
- Scanner path: **0** — Controlli disponibili 34. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -8/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 10. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 75,00%, return centrale 30g +5,21%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 10, positivi 30g 80,00%, return p50 +3,86%.
- Scanner path: **0** — Controlli disponibili 34. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +57,75%, aderenza live +69,23%, errore live +15,39%, gap corrente -16,21%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 32, ma percorso ancorato non aderente: gap -16,21%, errore live +15,39%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,65 $, upside EMA200 +48,06%, gap EMA50/EMA200 -5,54%, hit EMA200 12w +33,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in misto rispetto a ieri.

Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,16 / 94,00, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 71,47 / 70,69 / 62,19.

### DOGE

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **SOLO TRANCHE PICCOLE / NO LEVA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 13. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 65,00%, return centrale 30g +12,05%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 13, positivi 30g 76,92%, return p50 +13,28%.
- Scanner path: **0** — Controlli disponibili 34. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+1** — Score tecnico 2/12, verdetto neutrale / misto, trend ribassista, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Adam and Eve Top / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — DOGE: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Sopra 0.07117 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.06835 il rischio ribassista aumenta.


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

Generato: 2026-08-15 05:34 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.058 $ | prezzo corrente |
| Power Law centrale | 123.635 $ | deviazione -49,00% |
| Banda p10-p90 | 76.612 $ / 311.327 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 0,30% | posizione storica nel corridoio |
| Esponente β | 5,8200 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3148 cambiando finestra |
| Ultimo halving | 2024-04-19 | 848 giorni fa |
| Fase ciclo | 58,04% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-15 (4350 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1907) × giorni^5.8200
- Prezzo centrale oggi: **123.635 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 0,30%
- Scarto dal centro: **-49,00%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8200 | 91,94% |
| 2015 | 5,9042 | 91,50% |
| 2016 | 5,5903 | 87,73% |
| 2017 | 4,8604 | 82,85% |
| 2018 | 4,5894 | 78,32% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-03 | -15,25% | -9,52% | -9,13% | +52,98% |
| 2016-07-09 → 2020-05-11 | 2018-10-01 | -4,13% | -41,33% | -37,68% | +26,61% |
| 2020-05-11 → 2024-04-19 | 2022-08-24 | -9,80% | -24,33% | +16,05% | +22,28% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | 0.1423796422559187 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -4 | -1 | -2.745817411130047 | 0 |

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

Generato: 2026-08-15 05:34 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00119570 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +0,14% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000111 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | -2,75% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

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
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +5,35%; 30g +0,14%; 90g +7,92%; 180g -4,34%
- **Daily:** RSI 57.87; MA50 0.00119675; MA200 0.00118387
- **Weekly:** MA30 0.00118866; RSI 47.90
- **Livelli:** supporto 0.00119400; resistenza 0.00119800; breakout 60g 0.00134900; breakdown 60g 0.00102800
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00113300; target 0.00108600
- **Fibonacci:** VICINO — 50.0% a 0.00117900
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g +3,70%; 30g -2,75%; 90g -20,50%; 180g -25,43%
- **Daily:** RSI 50.58; MA50 0.00000114; MA200 0.00000130
- **Weekly:** MA30 0.00000130; RSI 33.99
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000146; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 204 | 51,96% | +1,94% | -1,18% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 197 | 53,30% | +10,17% | +2,42% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 290 | 53,10% | +2,05% | -3,94% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 16 | 62,50% | -0,24% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 15 | 46,67% | -0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 15 | 40,00% | -1,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 8 | 12,50% | -2,41% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 33 | 66,67% | +0,25% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 32 | 59,38% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 29 | 72,41% | +1,14% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 22 | 72,73% | +1,73% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 6 | 100,00% | +3,63% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **15 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +57,75%
- **Somiglianza strutturale:** +57,75%
- **Aderenza prezzo live:** +69,23%
- **Errore medio live:** +15,39%
- **Gap prezzo corrente:** -16,21%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 70 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-30
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima spike, poi scarico.** Zona bassa **71,47 $** intorno al **26 agosto 2026**; zona alta **78,31 $** intorno al **17 agosto 2026**; fine step circa **71,98 $** entro il **29 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 15 agosto 2026 | 44 | +69,23% | +15,39% | -16,21% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 15 agosto 2026 | 71 | +76,35% | +11,83% | -16,21% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +69,23% | Errore medio live +15,39%. |
| Gap corrente | -16,21% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 79,16 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 94,00 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 71,47 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 411,78 $ |
| Massimo percorso base | 411,78 $ (21 aprile 2029) |

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
| Prima conferma | 79,16 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 94,00 $ | Scenario più credibile. |
| Invalidazione soft | 71,47 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 22 agosto 2026 | -0,35% | 75,13 $ | 75,13 $ | 78,31 $ |
| 14 giorni | 29 agosto 2026 | -4,52% | 71,98 $ | 71,47 $ | 78,31 $ |
| 30 giorni | 14 settembre 2026 | +3,53% | 78,05 $ | 71,47 $ | 81,96 $ |
| 60 giorni | 14 ottobre 2026 | +24,69% | 94,00 $ | 66,63 $ | 94,00 $ |
| 90 giorni | 13 novembre 2026 | +28,15% | 96,61 $ | 66,63 $ | 100,63 $ |
| 120 giorni | 13 dicembre 2026 | +21,29% | 91,44 $ | 66,63 $ | 100,63 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 15 agosto 2026 -> 29 agosto 2026 | -4,52% | 71,47 $ (26 agosto 2026) | 78,31 $ (17 agosto 2026) | 71,98 $ | Prima spike, poi scarico. |
| Step 2 - primo mese | 30 agosto 2026 -> 14 settembre 2026 | +3,53% | 73,35 $ (30 agosto 2026) | 81,96 $ (5 settembre 2026) | 78,05 $ | Laterale / movimento non forte. |
| Step 3 - secondo mese | 15 settembre 2026 -> 14 ottobre 2026 | +24,69% | 66,63 $ (23 settembre 2026) | 94,00 $ (14 ottobre 2026) | 94,00 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 15 ottobre 2026 -> 13 novembre 2026 | +28,15% | 90,03 $ (4 novembre 2026) | 100,63 $ (28 ottobre 2026) | 96,61 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 75,39 $ |  |
| Weekly RSI | 40,21 / linea grezza 53,18 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,91 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 411,78 $ | Avanzamento +18,31% |
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
| Score on-chain | 2 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Prezzo SOL | 75,39 $ |
| TVL Solana | 4,82 mld $ |
| TVL 7g | +1,52% |
| DEX volume 24h | 1,64 mld $ |
| Fees 24h | 8,00 mln $ |
| Stablecoin su Solana | 15,94 mld $ |
| Stake ratio | 68,88% |
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
| Prezzo SOL | 75,39 $ |
| EMA200 weekly target | 111,65 $ |
| Upside verso EMA200 | +48,06% |
| Distanza prezzo da EMA200 | -32,46% |
| Gap EMA50/EMA200 | -5,54% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 40,22 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +33,33% |
| Max gain mediano 12w | +19,45% |
| Drawdown mediano 12w | -22,88% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-15 05:34 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-15 05:30:23 UTC**

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
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +70.00% | -2.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | misto | RIALZISTA | +75.00% | 0.00 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +65.00% | -5.00 punti |

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
| BTC | 59.898 $ | 69.356 $ | +40,00% | +15,79% | rimbalzo debole | 69.356 $ | 59.898 $ | +10,71% | -13,64% | spike storicamente più resistente |
| SOL | 71,62 $ | 82,93 $ | +26,67% | +15,79% | rimbalzo poco frequente | 82,93 $ | 71,62 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06663 $ | 0,07715 $ | +62,50% | +15,79% | rimbalzo possibile | 0,07715 $ | 0,06663 $ | +22,58% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (6/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 3 poi sono scaricati a -5,00%. Percentuale: +10,71% (3/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +26,67% (4/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 20 poi sono rimbalzati fino a +10,00%. Percentuale: +62,50% (20/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 7 poi sono scaricati a -5,00%. Percentuale: +22,58% (7/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-15 05:32:59 UTC


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
| BTC | 2026-08-15 | 63.051 $ | SALITA | 70,00% | 58.354,75 $ | 60.759,35 $ | 68.492,55 $ | 75.304,40 $ | 93.822,61 $ |
| SOL | 2026-08-15 | 75,39 $ | SALITA | 75,00% | 69,72 $ | 75,74 $ | 79,32 $ | 92,06 $ | 135,24 $ |
| DOGE | 2026-08-15 | 0.07014 $ | SALITA | 65,00% | 0.05324 $ | 0.06598 $ | 0.07859 $ | 0.08806 $ | 0.09917 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-16**; verificato fino al **2026-08-15**; stato **COMPLETO 30/30g**.
- Reale **63.058,63 $**; p50 previsto **66.378,43 $**; scarto **-5,00%**.
- Errore medio assoluto **2,80%**; massimo **5,31%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-16**; verificato fino al **2026-08-15**; stato **COMPLETO 30/30g**.
- Reale **75,40 $**; p50 previsto **73,94 $**; scarto **1,97%**.
- Errore medio assoluto **1,82%**; massimo **5,60%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-16**; verificato fino al **2026-08-15**; stato **COMPLETO 30/30g**.
- Reale **0.07012 $**; p50 previsto **0.05994 $**; scarto **16,98%**.
- Errore medio assoluto **12,21%**; massimo **23,44%**; DENTRO p10-p90; DENTRO p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 34 | 100,00% | 61,76% | 1,61% | -0,21% |
| BTC | 3g | 33 | 100,00% | 78,79% | 2,12% | -0,65% |
| BTC | 7g | 30 | 100,00% | 86,67% | 2,54% | -0,09% |
| BTC | 14g | 23 | 100,00% | 86,96% | 2,83% | -0,05% |
| BTC | 30g | 7 | 100,00% | 85,71% | 8,04% | -8,04% |
| SOL | 1g | 34 | 79,41% | 64,71% | 1,94% | -0,40% |
| SOL | 3g | 33 | 100,00% | 78,79% | 2,31% | -0,95% |
| SOL | 7g | 30 | 100,00% | 93,33% | 1,94% | -0,00% |
| SOL | 14g | 23 | 100,00% | 91,30% | 1,88% | 0,80% |
| SOL | 30g | 7 | 100,00% | 100,00% | 1,76% | -0,05% |
| DOGE | 1g | 34 | 97,06% | 64,71% | 2,32% | 0,09% |
| DOGE | 3g | 33 | 100,00% | 87,88% | 2,25% | 0,73% |
| DOGE | 7g | 30 | 93,33% | 90,00% | 5,39% | 3,33% |
| DOGE | 14g | 23 | 100,00% | 69,57% | 6,92% | 5,16% |
| DOGE | 30g | 7 | 100,00% | 28,57% | 14,20% | 14,20% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **96**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-15 | BTC | 63.051 $ | SALITA | 70,00% | 68.493 $ | 61.005 $ | 74.890 $ | 2026-09-14 |
| 2026-08-15 | DOGE | 0,07000 $ | SALITA | 65,00% | 0,08000 $ | 0,06000 $ | 0,09000 $ | 2026-09-14 |
| 2026-08-15 | SOL | 75,39 $ | SALITA | 75,00% | 79,32 $ | 72,94 $ | 87,58 $ | 2026-09-14 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-15 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +75,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **63.050,60 $**
- Return normale fra 30 giorni: **68.492,55 $** (8,63%)
- Drawdown normale durante il mese: **61.004,74 $** (-3,24%)
- Drawdown brutto da rispettare: **58.899,28 $** (-6,58%)
- Max gain normale durante il mese: **74.889,80 $** (18,78%)
- Max gain buono / take profit ottimistico: **86.247,97 $** (36,79%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **75,00%**
- Casi negativi / discesa storica: **25,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **75,39 $**
- Return normale fra 30 giorni: **79,32 $** (5,21%)
- Drawdown normale durante il mese: **72,94 $** (-3,25%)
- Drawdown brutto da rispettare: **70,38 $** (-6,65%)
- Max gain normale durante il mese: **87,58 $** (16,16%)
- Max gain buono / take profit ottimistico: **101,21 $** (34,25%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **65,00%**
- Casi negativi / discesa storica: **35,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,08 $** (12,05%)
- Drawdown normale durante il mese: **0,06 $** (-10,07%)
- Drawdown brutto da rispettare: **0,06 $** (-15,97%)
- Max gain normale durante il mese: **0,09 $** (22,24%)
- Max gain buono / take profit ottimistico: **0,10 $** (37,85%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 63.050,60 $

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

- Se va molto male: **58.354,75 $** (-7,45%)
- Se va male: **60.759,35 $** (-3,63%)
- Scenario normale: **68.492,55 $** (8,63%)
- Se va bene: **75.304,40 $** (19,43%)
- Se va molto bene: **93.822,61 $** (48,81%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **61.004,74 $** (-3,24%)
- Discesa brutta: **58.899,28 $** (-6,58%)
- Discesa molto brutta: **52.585,07 $** (-16,60%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **74.889,80 $** (18,78%)
- Rialzo buono: **86.247,97 $** (36,79%)
- Rialzo molto forte: **109.091,69 $** (73,02%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **61.004,74 $** e uno spike normale intorno a **74.889,80 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 75,39 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **75,00%**
- Probabilità storica di discesa: **25,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **69,72 $** (-7,52%)
- Se va male: **75,74 $** (0,47%)
- Scenario normale: **79,32 $** (5,21%)
- Se va bene: **92,06 $** (22,11%)
- Se va molto bene: **135,24 $** (79,39%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **72,94 $** (-3,25%)
- Discesa brutta: **70,38 $** (-6,65%)
- Discesa molto brutta: **67,39 $** (-10,61%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **87,58 $** (16,16%)
- Rialzo buono: **101,21 $** (34,25%)
- Rialzo molto forte: **154,47 $** (104,89%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **72,94 $** e uno spike normale intorno a **87,58 $**.

La chiusura a 30 giorni era più spesso positiva: salita 75,00%, discesa 25,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,07 $

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

- Se va molto male: **0,05 $** (-24,10%)
- Se va male: **0,07 $** (-5,94%)
- Scenario normale: **0,08 $** (12,05%)
- Se va bene: **0,09 $** (25,54%)
- Se va molto bene: **0,10 $** (41,39%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-10,07%)
- Discesa brutta: **0,06 $** (-15,97%)
- Discesa molto brutta: **0,05 $** (-30,29%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (22,24%)
- Rialzo buono: **0,10 $** (37,85%)
- Rialzo molto forte: **0,11 $** (51,89%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,09 $**.

La chiusura a 30 giorni era più spesso positiva: salita 65,00%, discesa 35,00%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **14**
- Direzione corretta: **70,00%**
- Errore medio dello scenario centrale: **5,19%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **14**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,30%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **14**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **4,17%**
- Zona rischio toccata: **14,29%**
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

Dati ancora insufficienti: previsioni controllate **14** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **14** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **14** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 63.050,60 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,39%**
- Rendimento medio dopo 30 giorni: **16,79%**
- Rendimento centrale dopo 30 giorni: **8,63%**
- Discesa media durante i 30 giorni: **-6,19%**
- Massimo rialzo medio durante i 30 giorni: **31,89%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **73.639,49 $**
- Scenario centrale a 30 giorni: **68.492,55 $**
- Zona di rischio media: **59.147,50 $**
- Zona di rialzo media: **83.156,78 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -7,45% → **58.354,75 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,63% → **60.759,35 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 8,63% → **68.492,55 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,43% → **75.304,40 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 48,81% → **93.822,61 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -16,60% → **52.585,07 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -6,58% → **58.899,28 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,24% → **61.004,74 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,10% → **62.988,60 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **63.050,60 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,86% → **66.743,91 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,45% → **69.007,29 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 18,78% → **74.889,80 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 36,79% → **86.247,97 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 73,02% → **109.091,69 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-08-09   | 2020-11-16 |        89.46 |       133.71 |           0    |         152.04 |
| XRP-USD         | 2023-07-20   | 2023-10-27 |        88.74 |        12.95 |          -0.13 |          31.02 |
| NEO-USD         | 2018-10-24   | 2019-01-31 |        88.23 |        27.24 |          -1.02 |          46.91 |
| BTC-USD         | 2018-10-23   | 2019-01-30 |        88.01 |        10.71 |          -2.49 |          18.83 |
| XRP-USD         | 2026-01-05   | 2026-04-14 |        87.7  |         8.98 |           0    |           8.98 |
| OMG-USD         | 2018-10-24   | 2019-01-31 |        87.15 |        17.35 |          -6.48 |          23.17 |
| LTC-USD         | 2023-07-19   | 2023-10-26 |        87.14 |         4.33 |          -3.48 |           9.18 |
| ETH-USD         | 2026-01-05   | 2026-04-14 |        86.97 |        -1.82 |          -3.01 |           4.21 |
| WAVES-USD       | 2024-05-15   | 2024-08-22 |        86.76 |         6.69 |         -14.17 |           7.19 |
| ETC-USD         | 2018-10-24   | 2019-01-31 |        86.63 |         8.28 |          -4.92 |          22.5  |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 75,39 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **75,00%**
- Casi negativi dopo 30 giorni: **25,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **78,73%**
- Rendimento medio dopo 30 giorni: **31,24%**
- Rendimento centrale dopo 30 giorni: **5,21%**
- Discesa media durante i 30 giorni: **-4,87%**
- Massimo rialzo medio durante i 30 giorni: **45,93%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **98,94 $**
- Scenario centrale a 30 giorni: **79,32 $**
- Zona di rischio media: **71,72 $**
- Zona di rialzo media: **110,02 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -7,52% → **69,72 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 0,47% → **75,74 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 5,21% → **79,32 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,11% → **92,06 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 79,39% → **135,24 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -10,61% → **67,39 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -6,65% → **70,38 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,25% → **72,94 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **75,39 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **75,39 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,15% → **78,52 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,45% → **81,76 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,16% → **87,58 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 34,25% → **101,21 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 104,89% → **154,47 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ENJ-USD         | 2018-10-24   | 2019-01-31 |        85.19 |       190.3  |         -13.17 |         193.34 |
| DASH-USD        | 2020-02-11   | 2020-05-20 |        82.67 |       -10.33 |         -10.33 |           2.52 |
| ZIL-USD         | 2020-08-06   | 2020-11-13 |        82.25 |        61.38 |          -1.51 |          75.54 |
| BCH-USD         | 2020-02-11   | 2020-05-20 |        81.78 |        -3    |          -6.13 |           7.4  |
| EOS-USD         | 2018-11-08   | 2019-02-15 |        81.59 |        34.78 |           0    |          52.35 |
| ONE-USD         | 2020-02-11   | 2020-05-20 |        81.37 |       -21.28 |         -21.28 |           3.36 |
| BNB-USD         | 2026-01-10   | 2026-04-19 |        81.21 |         3.72 |          -0.24 |           9.96 |
| EOS-USD         | 2020-02-11   | 2020-05-20 |        81    |        -3.52 |          -4.81 |           8.72 |
| VET-USD         | 2020-02-13   | 2020-05-22 |        80.9  |        85.39 |          -2.6  |         109.53 |
| BNB-USD         | 2020-02-11   | 2020-05-20 |        80.9  |        -5.81 |          -5.81 |           6.08 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,07 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **65,00%**
- Casi negativi dopo 30 giorni: **35,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,00%**
- Rendimento medio dopo 30 giorni: **11,93%**
- Rendimento centrale dopo 30 giorni: **12,05%**
- Discesa media durante i 30 giorni: **-12,26%**
- Massimo rialzo medio durante i 30 giorni: **26,99%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,09 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -24,10% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -5,94% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 12,05% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 25,54% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 41,39% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,29% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,97% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,07% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,83% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,45% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 11,57% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 22,24% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 37,85% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 51,89% → **0,11 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| OP-USD          | 2026-01-06   | 2026-04-15 |        91.43 |        14.03 |          -0.09 |          43.84 |
| ADA-USD         | 2019-06-16   | 2019-09-23 |        89.49 |       -21.3  |         -21.3  |           0    |
| ZEC-USD         | 2019-06-21   | 2019-09-28 |        88.68 |        -6.19 |         -18.51 |           0    |
| WAVES-USD       | 2022-03-27   | 2022-07-04 |        88.37 |         2.44 |         -14.68 |          13.6  |
| AVAX-USD        | 2025-09-13   | 2025-12-21 |        88.34 |        -0.45 |          -0.48 |          21.42 |
| VET-USD         | 2022-03-29   | 2022-07-06 |        88.18 |        33.03 |          -9.15 |          33.03 |
| HBAR-USD        | 2020-08-06   | 2020-11-13 |        88.17 |         8.3  |          -6.49 |          22.39 |
| ADA-USD         | 2022-03-27   | 2022-07-04 |        87.95 |         6.67 |         -11.01 |          11.91 |
| CHZ-USD         | 2022-03-26   | 2022-07-03 |        87.64 |        38.08 |          -1.3  |          51.2  |
| SNX-USD         | 2025-10-07   | 2026-01-14 |        87.59 |       -39.02 |         -43.19 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-15 05:33 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.051 $ | False | -18.56% | -10.20% | BEAR | -18.56% | -10.20% |
| DOGE-USD | BEAR | 0.07014 $ | False | -35.49% | -16.69% | BEAR | -18.56% | -10.20% |
| SOL-USD | BEAR | 75,39 $ | False | -11.47% | -16.90% | BEAR | -18.56% | -10.20% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 8.63% | 19.43% | 48.81% | -3.24% | -16.60% | 18.78% | 36.79% | 73.02% | 57.50% | 9.56% | 65.84% | 112.25% |
| BTC-USD | SAME_BTC_REGIME | 22 | 72.73% | 8.63% | 17.03% | 49.50% | -2.75% | -10.45% | 18.78% | 37.48% | 70.30% | 45.45% | -8.92% | 66.53% | 105.34% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 73.91% | 8.98% | 18.10% | 45.10% | -3.99% | -15.65% | 18.73% | 28.54% | 59.13% | 52.17% | 5.16% | 67.23% | 103.67% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 73.68% | 8.98% | 16.71% | 56.85% | -3.01% | -7.44% | 18.73% | 25.51% | 67.62% | 47.37% | -11.59% | 70.57% | 117.47% |
| DOGE-USD | ALL_MATCHES | 40 | 65.00% | 12.05% | 25.54% | 41.39% | -10.07% | -30.29% | 22.24% | 37.85% | 51.89% | 45.00% | -3.62% | 14.65% | 86.97% |
| DOGE-USD | SAME_BTC_REGIME | 19 | 84.21% | 15.11% | 26.21% | 46.95% | -10.17% | -19.07% | 24.34% | 42.86% | 52.61% | 47.37% | -2.00% | 11.27% | 111.93% |
| DOGE-USD | SAME_ASSET_REGIME | 14 | 78.57% | 13.66% | 24.05% | 31.38% | -9.96% | -24.84% | 23.28% | 32.73% | 41.23% | 42.86% | -2.61% | 4.50% | 7.10% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 13 | 76.92% | 13.28% | 21.57% | 27.01% | -10.17% | -26.65% | 23.01% | 31.81% | 42.10% | 38.46% | -3.21% | 3.04% | 7.11% |
| SOL-USD | ALL_MATCHES | 40 | 75.00% | 5.21% | 22.11% | 79.39% | -3.25% | -10.61% | 16.16% | 34.25% | 104.89% | 57.50% | 13.74% | 61.82% | 185.86% |
| SOL-USD | SAME_BTC_REGIME | 14 | 85.71% | 4.12% | 19.65% | 69.98% | -1.35% | -7.03% | 20.24% | 43.82% | 90.92% | 50.00% | 10.80% | 62.36% | 137.02% |
| SOL-USD | SAME_ASSET_REGIME | 12 | 75.00% | 3.86% | 13.74% | 20.46% | -3.93% | -12.56% | 18.02% | 24.85% | 46.69% | 41.67% | -9.43% | 57.87% | 138.77% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 80.00% | 3.86% | 14.97% | 37.94% | -3.93% | -7.71% | 20.24% | 27.93% | 63.07% | 40.00% | -9.43% | 60.32% | 174.40% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 72.73% | 8.63% | -2.75% | 37.48% | 45.45% | -8.92% | 89.45% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 90.00% | 14.80% | -0.30% | 35.24% | 90.00% | 21.72% | 93.79% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 28.57% | -3.98% | -6.50% | 21.17% | 42.86% | -0.73% | 78.63% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 19 | 84.21% | 15.11% | -10.17% | 42.86% | 47.37% | -2.00% | 51.35% |
| DOGE-USD | HISTORICAL_BTC_BULL | 18 | 38.89% | -3.70% | -12.12% | 26.59% | 38.89% | -20.58% | 40.32% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 11.10% | 0.00% | 36.94% | 100.00% | 19.41% | 36.94% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 100.00% | 23.81% | -8.62% | 28.42% | 50.00% | -0.95% | 36.12% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 85.71% | 4.12% | -1.35% | 43.82% | 50.00% | 10.80% | 103.55% |
| SOL-USD | HISTORICAL_BTC_BULL | 8 | 87.50% | 8.39% | -2.96% | 92.25% | 50.00% | 4.67% | 237.88% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 18 | 61.11% | 4.59% | -4.35% | 24.53% | 66.67% | 18.49% | 64.82% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 73.91% | 8.98% | -3.99% | 28.54% | 52.17% | 5.16% | 88.16% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 100.00% | 17.51% | -0.07% | 64.82% | 100.00% | 82.44% | 226.50% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.72% | -0.24% | 9.96% | 0.00% | -6.25% | 16.45% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 33.33% | -3.98% | -6.59% | 25.65% | 44.44% | -0.73% | 61.71% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 14 | 78.57% | 13.66% | -9.96% | 32.73% | 42.86% | -2.61% | 43.23% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 13 | 53.85% | 8.30% | -6.49% | 40.57% | 61.54% | 8.45% | 58.07% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 51.18% | -11.72% | 54.71% | 100.00% | 82.52% | 130.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 11 | 54.55% | 2.44% | -10.96% | 24.62% | 18.18% | -21.46% | 31.65% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 12 | 75.00% | 3.86% | -3.93% | 24.85% | 41.67% | -9.43% | 73.00% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 100.00% | 55.48% | -0.75% | 195.28% | 75.00% | 134.76% | 1021.74% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -2.44% | -4.99% | 7.89% | 0.00% | -3.94% | 12.75% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 4 | 75.00% | 57.68% | -1.30% | 105.67% | 75.00% | 84.05% | 167.40% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 18 | 72.22% | 4.59% | -4.29% | 21.01% | 66.67% | 18.49% | 64.82% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | NEO-USD | 2018-10-24 | 88.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.24% | -1.02% | 46.91% | 44.33% | -1.02% | 46.91% |
| BTC-USD | BTC-USD | 2018-10-23 | 88.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.71% | -2.49% | 18.83% | 17.76% | -2.49% | 18.83% |
| BTC-USD | XRP-USD | 2026-01-05 | 87.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.98% | 0.00% | 8.98% | -15.55% | -19.71% | 8.98% |
| BTC-USD | OMG-USD | 2018-10-24 | 87.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.35% | -6.48% | 23.17% | 67.84% | -6.48% | 81.36% |
| BTC-USD | ETH-USD | 2026-01-05 | 86.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.82% | -3.01% | 4.21% | -27.68% | -32.48% | 4.21% |
| BTC-USD | ETC-USD | 2018-10-24 | 86.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | SOL-USD | 2026-01-08 | 85.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | XTZ-USD | 2018-10-24 | 85.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 7.22% | -3.99% | 22.40% | 159.29% | -3.99% | 179.67% |
| BTC-USD | XTZ-USD | 2026-01-10 | 85.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | OP-USD | 2026-01-06 | 91.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.03% | -0.09% | 43.84% | -9.51% | -24.09% | 43.84% |
| DOGE-USD | ADA-USD | 2022-03-27 | 87.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | CHZ-USD | 2022-03-26 | 87.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.08% | -1.30% | 51.20% | 116.30% | -1.30% | 153.33% |
| DOGE-USD | NEO-USD | 2022-03-27 | 87.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | THETA-USD | 2022-03-26 | 87.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.01% | -10.28% | 22.09% | -4.02% | -10.28% | 37.23% |
| DOGE-USD | QTUM-USD | 2022-07-30 | 87.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.20% | -30.29% | 1.37% | -32.40% | -35.81% | 1.37% |
| DOGE-USD | FTM-USD | 2022-03-27 | 86.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.54% | -11.30% | 35.15% | 1.61% | -11.30% | 54.20% |
| DOGE-USD | DASH-USD | 2022-03-27 | 86.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LTC-USD | 2018-04-26 | 86.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -15.33% | -30.36% | 0.00% | -23.00% | -33.38% | 0.00% |
| DOGE-USD | LINK-USD | 2022-03-27 | 86.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| SOL-USD | ENJ-USD | 2018-10-24 | 85.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 190.30% | -13.17% | 193.34% | 417.86% | -13.17% | 644.83% |
| SOL-USD | SOL-USD | 2026-01-08 | 79.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| SOL-USD | RUNE-USD | 2026-01-11 | 79.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | NEAR-USD | 2026-01-05 | 79.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.59% | -7.11% | 17.95% | 56.65% | -7.11% | 107.36% |
| SOL-USD | KAVA-USD | 2026-01-10 | 78.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | 0.00% | 23.31% | -16.11% | -23.42% | 23.31% |
| SOL-USD | XTZ-USD | 2018-11-03 | 78.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 21.01% | 0.00% | 22.38% | 147.35% | 0.00% | 179.64% |
| SOL-USD | QTUM-USD | 2018-10-24 | 77.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 13.12% | -5.39% | 29.47% | 61.55% | -5.39% | 61.55% |
| SOL-USD | BTC-USD | 2026-01-09 | 76.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.62% | -2.47% | 8.47% | -14.93% | -19.62% | 8.47% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | ETH-USD | 2026-01-10 | 75.89% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |

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

Generato: 2026-08-15 05:33 UTC


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
| BTC | 63.051 $ | -8 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 75,39 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07014 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | -3 | -1 | 0 | 0 | -2 | -8 |
| SOL | -3 | 0 | 0 | +1 | 0 | 0 | 0 | -2 |
| DOGE | -4 | +2 | +1 | +1 | 0 | 0 | -2 | -2 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.227 $ | 64.186 $ | 67.248 $ | 57.748 $ | 1,65% | -2,56% | -19,29% |
| SOL | 74,16 $ | 75,94 $ | 83,81 $ | 63,16 $ | 2,40% | -2,41% | -12,87% |
| DOGE | 0.06961 $ | 0.07117 $ | 0.09169 $ | 0.06797 $ | 2,39% | -5,23% | -35,84% |

## Lettura dettagliata

### BTC

- Prezzo: **63.051 $**
- Score classico: **-8 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 1,65%; distanza supporto 1,34%; distanza resistenza 1,79%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-3** — RSI neutrale 43.2; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.03; volume ratio 0.92
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 43.21 |
| MACD histogram | -132.82330 |
| CMF20 | -0.026 |
| Volume ratio 20 | 0.92 |
| MA20 | 63.948 $ |
| MA50 | 63.452 $ |
| MA100 | 67.042 $ |
| MA200 | 69.502 $ |
| Pendenza MA50 20g | +0,44% |
| Pendenza MA200 60g | -10,34% |
| Bollinger width | 4,70% |
| Bollinger position | 0.20 |

### SOL

- Prezzo: **75,39 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,40%; distanza supporto 1,67%; distanza resistenza 0,71%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 51.3; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale -0.00; volume ratio 0.77
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.27 |
| MACD histogram | 0.28152 |
| CMF20 | -0.001 |
| Volume ratio 20 | 0.77 |
| MA20 | 74,47 $ |
| MA50 | 75,90 $ |
| MA100 | 77,16 $ |
| MA200 | 82,29 $ |
| Pendenza MA50 20g | +3,01% |
| Pendenza MA200 60g | -17,16% |
| Bollinger width | 7,51% |
| Bollinger position | 0.66 |

### DOGE

- Prezzo: **0.07014 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 2,39%; distanza supporto 0,80%; distanza resistenza 1,43%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+1** — RSI neutrale 46.6; RSI in miglioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.00; volume ratio 0.56
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 46.61 |
| MACD histogram | 0.00028 |
| CMF20 | 0.001 |
| Volume ratio 20 | 0.56 |
| MA20 | 0.07020 $ |
| MA50 | 0.07212 $ |
| MA100 | 0.08383 $ |
| MA200 | 0.09072 $ |
| Pendenza MA50 20g | -7,02% |
| Pendenza MA200 60g | -16,93% |
| Bollinger width | 5,57% |
| Bollinger position | 0.49 |

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

Generato: 2026-08-15 05:34 UTC


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
| BTC | 63.051 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 9,18% | Fib 23,6% TESTATO (0) @ 63.595 $ | NEL RANGE | 62.553 $ |
| SOL | 75,39 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 17,03% | Fib 23,6% NON ATTIVO (0) @ 73,56 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.07014 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.07931 $ | n/a | 5,22% | Fib 23,6% NON ATTIVO (0) @ 0.08013 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **6 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **9,18%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 63.595 $** — Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 23.6% a 63.595; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.402 $**
- Breakout 60g: **67.248 $**
- Breakdown 60g: **57.748 $**
- RSI14: **43.16**
- ATR14: **1,65%**
- Volume ratio 20g: **0.92**
- Rendimento 30g: **-2,57%**
- Rendimento 90g: **-19,30%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 1,32% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 66.910 $ | n/a | n/a | 71.619 $ | n/a | 6,12% | 65.572 $ | Due minimi simili a 62.201 $ e 62.227 $. Neckline circa 66.910 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 12 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **6 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **17,03%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 73,56 $** — Swing UP 2026-06-06 60,41 -> 2026-08-09 77,62; livello più vicino 23.6% a 73,56; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **75,94 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **63,16 $**
- RSI14: **51.23**
- ATR14: **2,40%**
- Volume ratio 20g: **0.77**
- Rendimento 30g: **-2,43%**
- Rendimento 90g: **-12,88%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 6,64% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 78,73 $ | n/a | n/a | 86,76 $ | n/a | 4,42% | 77,15 $ | Due minimi simili a 73,40 $ e 70,69 $. Neckline circa 78,73 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 14 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 5,25% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 29 giorni. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-24 -> 2026-08-06**
- Età formazione: **9 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.07380 $**
- Target teorico: **0.07931 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **5,22%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08013 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-06 0.06835; livello più vicino 23.6% a 0.08013; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07233 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-06. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07117 $**
- Breakout 60g: **0.09169 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **46.49**
- ATR14: **2,39%**
- Volume ratio 20g: **0.56**
- Rendimento 30g: **-5,27%**
- Rendimento 90g: **-35,86%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 52g | 0.06035 $ | 44,84% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (52 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 44,84%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07380 $ | n/a | n/a | 0.07931 $ | n/a | 5,22% | 0.07233 $ | Due minimi simili a 0.06829 $ e 0.06835 $. Neckline circa 0.07380 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 9 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |

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

Generato: 2026-08-15 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-15**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-30**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,39 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,75%**
- Aderenza live principale: **+69,23%**
- Errore medio live principale: **15,39%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **70**
- Osservazioni inclusive dal bottom: **71**
- Osservazioni da inizio programma/scanner: **44**
- Errore assoluto medio dal bottom: **11,83%**
- Errore assoluto medio da inizio programma: **15,39%**
- Gap firmato medio ultimi 7 giorni: **-16,43%**
- Errore assoluto medio ultimi 7 giorni: **16,43%**
- Gap ultimo giorno: **-16,21%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-16,21%**
- Gap firmato medio 7g: **-16,43%**
- Errore assoluto medio 7g: **16,43%**
- Variazione recente gap: **+0,72%**
- Stato gap: **IN DEVIAZIONE SOTTO IL FRATTALE**
- Trend gap: **SOL e vicino al percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 76,18 $ | 93,65 $ | -18,66% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,39 $ | 89,97 $ | -16,21% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-22 | 89,66 $ | 75,13 $ | 75,13 $ / 78,31 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-29 | 85,91 $ | 71,98 $ | 71,47 $ / 78,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-05 | 97,81 $ | 81,96 $ | 71,47 $ / 81,96 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-12 | 92,66 $ | 77,64 $ | 71,47 $ / 81,96 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-19 | 88,36 $ | 74,04 $ | 71,47 $ / 81,96 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-26 | 95,32 $ | 79,87 $ | 66,63 $ / 81,96 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-03 | 109,38 $ | 91,65 $ | 66,63 $ / 92,55 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-10 | 106,91 $ | 89,58 $ | 66,63 $ / 93,52 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-17 | 109,47 $ | 91,73 $ | 66,63 $ / 94,00 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-24 | 116,81 $ | 97,88 $ | 66,63 $ / 97,88 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-31 | 115,99 $ | 97,19 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-07 | 108,43 $ | 90,85 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-14 | 110,66 $ | 92,72 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-21 | 109,09 $ | 91,41 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-28 | 107,12 $ | 89,76 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-05 | 105,77 $ | 88,63 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-12 | 109,30 $ | 91,58 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-19 | 101,48 $ | 85,03 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 32 | 40,62% | 7,24% | 13,56% |
| 14g | 25 | 32,00% | 16,29% | 12,88% |
| 21g | 18 | 27,78% | 26,22% | 15,20% |
| 28g | 11 | 36,36% | 28,74% | 16,51% |
| 35g | 4 | 0,00% | 29,07% | 17,43% |
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

Ultima lettura salvata: **2026-08-15** — SOL 75,39 $, gap -16,21%, somiglianza +57,75%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-15 05:34 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.103 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0092% | +7,54% | 1,17 | -2,89% | 0 $ | 0 $ |
| SOL | 75,48 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0058% | +2,43% | 1,20 | +1,48% | 0 $ | 0 $ |
| DOGE | 0.07029 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0089% | -0,39% | 1,10 | -0,99% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0018% | 150,80 mln $ | 0,83 | -2,32% |
| BTC | Bitget | OK | +0,0100% | 2,55 mld $ | 8,22 | +20,36% |
| BTC | Kucoin | OK | +0,0100% | 1,49 mld $ | 0,41 | +2,53% |
| SOL | Kraken | OK | +0,0382% | 21,45 mln $ | 0,11 | +15,13% |
| SOL | Bitget | OK | +0,0100% | 353,35 mln $ | 35,86 | -12,88% |
| SOL | Kucoin | OK | +0,0094% | 269,78 mln $ | 0,24 | +7,22% |
| DOGE | Kraken | OK | +0,0041% | 3,90 mln $ | 1,47 | -6,82% |
| DOGE | Bitget | OK | +0,0014% | 92,43 mln $ | 0,14 | +1,96% |
| DOGE | Kucoin | OK | +0,0100% | 124,70 mln $ | 0,48 | -2,29% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
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
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
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

- Score grezzo exchange: **+2,12**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +66,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +70,00% | +8,63% | 0 | n/a | RACCOLTA DATI | 0,00 | +70,00% | +8,63% |
| SOL | +75,00% | +5,21% | 0 | n/a | RACCOLTA DATI | 0,00 | +75,00% | +5,21% |
| DOGE | +65,00% | +12,05% | 0 | n/a | RACCOLTA DATI | 0,00 | +65,00% | +12,05% |

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

Generato: 2026-08-15 05:34 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-15 | BTC | 63.103,10 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,17 | +7,54% | -2,89% |
| 2026-08-15 | DOGE | 0.07029 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,10 | -0,39% | -0,99% |
| 2026-08-15 | SOL | 75,48 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,20 | +2,43% | +1,48% |
| 2026-08-14 | BTC | 62.903,40 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 2,18 | +7,44% | -1,76% |
| 2026-08-14 | DOGE | 0.06947 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,19 | +2,93% | +3,02% |
| 2026-08-14 | SOL | 75,51 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,59 | +1,63% | -3,11% |
| 2026-08-11 | BTC | 64.025,10 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,94 | +4,21% | -7,22% |
| 2026-08-11 | DOGE | 0.07002 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,86 | +1,22% | +10,68% |
| 2026-08-11 | SOL | 76,02 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,13 | +0,02% | +4,16% |

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
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 3 | +66,67% | +0,53% | -0,69% | +6,15% | FEEDBACK RAPIDO |
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

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.051 $ | +0.0100% | -5.12% | 1.31 | Rischio sotto | 2/5 |
| SOL | 75,39 $ | +0.0029% | +0.33% | 2.43 | Misto | 1/5 |
| DOGE | 0.07014 $ | +0.0099% | -13.10% | 4.31 | Misto | 1/5 |

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

Generato: 2026-08-15 05:34 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D       | Weekly                     | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:---------------------------|:--------------|:---------------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish             | IN_FORMAZIONE | Bullish regolare           | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Conferma rialzista         | CONTESTO      | Hidden bearish             | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza | CONTESTO   | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                                          |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish             | IN_FORMAZIONE | 63.058 $ / 43,20  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-13 62.799 $ / RSI 45,39 | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare           | CONFERMATA    | 63.058 $ / 39,04  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20 | n/a                 | n/a              |      0 |
| SOL     | 1D   | Conferma rialzista         | CONTESTO      | 75,40 $ / 51,27   | n/a                                                               | +3,59%              | 9,37             |      0 |
| SOL     | 1W   | Hidden bearish             | CONFERMATA    | 75,40 $ / 40,22   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Misto / nessuna divergenza | CONTESTO      | 0.07017 $ / 46,61 | n/a                                                               | +0,93%              | 7,71             |      0 |
| DOGE    | 1W   | Misto / nessuna divergenza | CONTESTO      | 0.07017 $ / 33,20 | n/a                                                               | -9,73%              | -1,93            |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
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

Generato: 2026-08-15 05:34 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum                  | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista           | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:-----------------------------|:-----------|:-------------|
| BTC | 63.051 $ | -6 | DEBOLE | Trend ribassista | Momentum debole | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 62.227 | 65.402 |
| SOL | 75,39 $ | -3 | DEBOLE | Trend misto | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 70,69 | 77,62 |
| DOGE | 0.07014 $ | 2 | NEUTRALE / MISTO | Trend ribassista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Adam and Eve Top / CANDIDATO | 0.06835 | 0.07117 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ASSENTE | ASSENTE | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 43.16 | -133.336 | 63.948 | 63.452 | 69.502 | 0,30% | -10,20% | -1,16% | -18,57% |
| SOL | 51.23 | 0.28088 | 74,47 | 75,90 | 82,29 | 2,61% | -16,90% | 0,16% | -11,49% |
| DOGE | 46.49 | 0.00028 | 0.07020 | 0.07212 | 0.09072 | -6,82% | -16,69% | -3,04% | -35,52% |

## Dettaglio asset

### BTC

- Prezzo: **63.051 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 5.775e+04 -> 6.223e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 43.2.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 23.6% a 63.595; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.227**
- Resistenza più vicina: **65.402**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-03. Neckline stimata: 66.910. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 66.910; target 71.619; distanza dalla neckline 6,12%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-03-29 al 2026-08-03. Neckline stimata: 82.792. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 82.792; target 103.383; distanza dalla neckline 31,31%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-03. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 67.248; target 75.387; distanza dalla neckline 6,66%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 9,18%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 9,18%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 25 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 9,18%; prezzo sopra neckline.

### SOL

- Prezzo: **75,39 $**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (1)
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
  - Due minimi simili vicino a 67,92 tra 2026-06-19 e 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,17%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 67,92 dal 2026-06-19 al 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,17%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,17%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,03%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 6,64%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,03%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07014 $**
- Punteggio tecnico: **2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 0.06797 -> 0.06835. Ultimi massimi: 0.0738 -> 0.07117.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 46.5.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-06 0.06835; livello più vicino 23.6% a 0.08013; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Adam and Eve Top (CANDIDATO, 0).
- Supporto più vicino: **0.06835**
- Resistenza più vicina: **0.07117**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-06. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 0.07380; target 0.07931; distanza dalla neckline 5,22%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.06829 dal 2026-06-30 al 2026-08-06. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 12,97%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06835 dal 2026-06-30 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 0.07923; target 0.09012; distanza dalla neckline 12,97%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **ASSENTE** (0)
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-07-26. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06829. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 20 giorni.
  - neckline 0.06829; target 0.05735; distanza dalla neckline 2,70%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-08-09 | 63.595 | 62.478 | 61.575 | 60.672 | 59.386 | 23.6% / 63.595 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-08-09 | 73,56 | 71,05 | 69,02 | 66,99 | 64,10 | 23.6% / 73,56 | NON ATTIVO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-08-06 | 0.08013 | 0.08741 | 0.09330 | 0.09919 | 0.10758 | 23.6% / 0.08013 | NON ATTIVO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 14/30 previsioni controllate su 42 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 14/30 previsioni controllate su 42 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 14/30 previsioni controllate su 42 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 42 | 14 | 14/30 [█████░░░░░] | 28 | RACCOLTA DATI | 2026-08-16 / tra 1 giorno |
| SOL | 42 | 14 | 14/30 [█████░░░░░] | 28 | RACCOLTA DATI | 2026-08-16 / tra 1 giorno |
| DOGE | 42 | 14 | 14/30 [█████░░░░░] | 28 | RACCOLTA DATI | 2026-08-16 / tra 1 giorno |

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

Generato: 2026-08-15 05:34 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 63.051 $          | 63.103 $        | +0,0833%     |
| Exchange Microstructure | SOL     | price             | OK      | 75,39 $           | 75,48 $         | +0,1154%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.07014 $         | 0.07029 $       | +0,2139%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |

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

Generato: 2026-08-15T16:30:35+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €41.031,15 | €17.544,74 | 311.135932 | 75.4860 | +2.58% | €568,83 | €49,51 | 6.48% | 8 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 71.0100 · L1 73.1320 · media 75.7845 · U1 78.4369 · U2 80.5589.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
