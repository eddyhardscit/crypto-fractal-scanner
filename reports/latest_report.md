<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-16 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +2 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -5 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+2**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+2**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-5**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402.
- Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 107,12; milestone analogiche 119,04 / 132,33, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 87,63 / 74,20 / 62,19.

### DOGE

- Global Confluence: **-5**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot dal Global: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.09421 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 3; EMA200 circa 111,08 $; upside verso EMA200 +14,46%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-16T05:33:16+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-16T05:05:33+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-16T05:05:33+00:00 | 2026-09-16T05:05:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-16T04:45:00+00:00 | 2026-09-16T04:45:00+00:00 | 5,9 min | 25,0 min | OK |
| 60m | 12 | 2026-09-16T04:00:00+00:00 | 2026-09-16T04:00:00+00:00 | 5,9 min | 45,0 min | OK |
| 240m | 12 | 2026-09-16T00:00:00+00:00 | 2026-09-16T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top5 Btc Tp3 V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Runner25 V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | AIN | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ARB | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -4,68 | 6,00 | 1,32 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,58 | 6,00 | 1,42 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | POWER | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 3,50 | 6,00 | 2,50 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -3,32 | 6,00 | 2,68 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -3,00 | 6,00 | 3,00 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -2,32 | 6,00 | 3,68 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -2,18 | 6,00 | 3,82 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,16 | 6,00 | 5,84 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.9 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Long No Rhv V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Long Only V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.816,14 | -1,84% | €7,58 | €3.000,00 | 0,25% | 5 | 60 | 41,67% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 60 | 3662 | PRIME INDICAZIONI | 100 (mancano 40) |

- Trade del Principale 4H chiusi: **60**; win rate **41,67%**; profit factor **0,88**.
- Expectancy: **€-3,05** per trade; P&L netto: **€-182,77**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.816,14 | €700,63 | €2.101,90 | €196,32 | €0,00 |
| TEST | Main Side Regime Guard V1 | 6 | €11.807,60 | €829,25 | €2.487,75 | €231,48 | €752,47 |
| TEST | Benchmark Donchian breakout 1H | 7 | €11.492,16 | €1.803,91 | €3.607,83 | €175,28 | €69,44 |
| TEST | Donchian 1H Gb20 120R V1 | 7 | €11.221,59 | €1.761,44 | €3.522,89 | €171,15 | €67,80 |
| TEST | Scanner Top 5 Long 1H | 6 | €11.067,73 | €1.170,53 | €2.341,05 | €221,36 | €138,07 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.014,85 | €712,13 | €2.136,38 | €166,65 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.911,93 | €1.449,24 | €2.898,47 | €167,65 | €121,61 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €10.608,37 | €750,52 | €2.251,55 | €52,50 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 7 | €10.601,69 | €2.345,31 | €4.690,62 | €212,36 | €132,53 |
| TEST | 1H Fast No Pepe V1 | 8 | €10.569,02 | €1.343,40 | €4.030,19 | €211,38 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €10.544,23 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Combo Adaptive | 9 | €10.491,31 | €1.353,46 | €2.706,93 | €158,90 | €127,39 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.481,64 | €1.586,40 | €4.759,20 | €210,71 | €87,71 |
| TEST | Scanner Top15 Long | 7 | €10.452,58 | €1.638,55 | €3.277,10 | €158,63 | €130,25 |
| TEST | Scanner Top20 Long | 7 | €10.452,58 | €1.638,55 | €3.277,10 | €158,63 | €130,25 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.414,29 | €1.576,21 | €4.728,62 | €209,35 | €87,14 |
| TEST | Combo Scanner | 6 | €10.396,55 | €1.541,44 | €3.082,88 | €207,77 | €127,55 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.387,48 | €1.100,94 | €2.201,87 | €205,39 | €129,32 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.366,98 | €457,63 | €1.372,88 | €103,80 | €0,00 |
| TEST | Scanner Top10 Long | 6 | €10.306,25 | €2.312,51 | €4.625,02 | €206,13 | €128,46 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.235,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.203,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.202,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 8 | €10.189,15 | €1.037,28 | €2.074,56 | €203,77 | €1,24 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.189,10 | €140,98 | €422,93 | €50,75 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.172,50 | €753,18 | €2.259,53 | €50,82 | €10,23 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 5 | €10.170,94 | €1.270,00 | €3.810,01 | €155,95 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 2 | €10.129,54 | €876,12 | €2.628,37 | €51,20 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.048,69 | €1.969,94 | €3.939,88 | €151,12 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.042,03 | €604,62 | €1.813,85 | €150,55 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.030,63 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.019,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 7 | €10.008,81 | €1.108,70 | €2.217,39 | €101,32 | €116,72 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.006,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.002,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 3 | €9.993,69 | €500,42 | €1.501,25 | €146,17 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.993,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.990,47 | €740,39 | €2.221,17 | €49,83 | €26,27 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.988,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.985,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.966,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.955,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.942,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.940,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.939,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.936,07 | €738,52 | €2.215,57 | €49,64 | €9,81 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.934,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.927,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €9.884,45 | €650,20 | €1.950,61 | €197,69 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.868,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €9.867,92 | €1.180,13 | €3.540,40 | €192,13 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 3 | €9.840,62 | €490,12 | €1.470,35 | €143,24 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.835,16 | €841,03 | €1.682,06 | €99,39 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.804,97 | €858,16 | €2.574,49 | €49,07 | €-7,25 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €9.795,11 | €1.014,88 | €3.044,64 | €146,37 | €77,16 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €9.789,37 | €1.602,53 | €3.205,07 | €195,79 | €8,22 |
| TEST | Global Confluence puro 1H | 1 | €9.784,51 | €847,30 | €1.694,61 | €0,00 | €82,64 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €9.784,07 | €1.016,22 | €2.032,45 | €195,68 | €122,06 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €9.783,64 | €1.601,60 | €3.203,19 | €195,68 | €8,22 |
| TEST | Eth Ema 4H | 0 | €9.783,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.737,75 | €1.032,07 | €2.064,15 | €192,55 | €121,23 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.701,70 | €853,06 | €2.559,17 | €48,53 | €-3,38 |
| TEST | Eth Donchian 1H | 0 | €9.676,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.632,45 | €1.124,23 | €3.372,70 | €192,65 | €-0,16 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €9.632,20 | €1.075,56 | €3.226,67 | €193,64 | €81,58 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.624,82 | €992,09 | €2.976,26 | €192,50 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.556,53 | €992,59 | €1.985,18 | €191,13 | €119,22 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.551,14 | €989,57 | €2.968,70 | €142,72 | €75,23 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.538,51 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 8 | €9.518,61 | €1.464,38 | €4.393,14 | €190,43 | €119,86 |
| TEST | Eth Adaptive 1H | 1 | €9.516,76 | €748,84 | €2.246,52 | €47,55 | €8,11 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.510,48 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.470,91 | €745,23 | €2.235,70 | €47,32 | €8,07 |
| TEST | Master Adaptive Gb20 Be V1 | 4 | €9.460,99 | €869,45 | €1.738,90 | €144,16 | €109,05 |
| TEST | Master Adaptive Gb20 Partial V1 | 4 | €9.450,93 | €868,53 | €1.737,05 | €144,01 | €108,93 |
| TEST | Master Adaptive V1 | 4 | €9.414,37 | €865,17 | €1.730,33 | €143,45 | €108,51 |
| TEST | Btc Ema 1H | 1 | €9.403,14 | €1.043,20 | €3.129,59 | €47,02 | €0,54 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.396,49 | €881,41 | €1.762,83 | €147,83 | €105,75 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.368,60 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.319,31 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.319,31 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.319,31 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.317,23 | €1.041,98 | €3.125,94 | €140,50 | €7,92 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €9.305,66 | €1.298,71 | €3.896,13 | €141,41 | €15,81 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.291,09 | €981,82 | €1.963,65 | €144,18 | €103,96 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.290,18 | €853,78 | €1.707,57 | €141,57 | €107,08 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 7 | €9.282,83 | €1.026,78 | €2.053,56 | €185,56 | €5,11 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €9.267,65 | €1.263,33 | €3.789,99 | €139,44 | €15,85 |
| TEST | Bilanciata 1H V1 | 8 | €9.259,04 | €1.309,62 | €3.928,85 | €139,97 | €123,19 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.254,74 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.240,66 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 7 | €9.225,39 | €1.421,72 | €2.843,45 | €140,69 | €113,94 |
| TEST | Combo Trend | 5 | €9.175,38 | €1.983,96 | €3.967,91 | €94,84 | €99,76 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.169,55 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 8 | €9.145,92 | €1.143,76 | €2.287,52 | €148,75 | €111,27 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €9.062,49 | €205,67 | €617,01 | €48,38 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 7 | €9.052,81 | €1.395,15 | €2.790,29 | €138,07 | €111,81 |
| TEST | 1H Balanced V3 Long Only V1 | 8 | €9.005,81 | €1.385,34 | €4.156,01 | €180,17 | €113,36 |
| TEST | Master Adaptive No Alt V1 | 4 | €8.970,69 | €1.274,80 | €2.549,60 | €137,85 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €8.970,21 | €909,26 | €1.818,52 | €47,26 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 6 | €8.958,47 | €996,60 | €1.993,20 | €179,28 | €-5,10 |
| TEST | Master Adaptive Strict3 V1 | 6 | €8.948,64 | €1.098,44 | €2.196,88 | €178,97 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €8.733,06 | €714,46 | €2.143,38 | €130,71 | €-6,84 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 4 | €8.684,09 | €1.695,57 | €3.391,13 | €173,79 | €-5,07 |
| TEST | Combo Mean Reversion | 2 | €8.682,93 | €1.595,10 | €3.190,20 | €87,94 | €14,39 |
| TEST | Forza relativa 1H V1 | 7 | €8.613,63 | €1.919,29 | €3.838,59 | €130,24 | €167,75 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 5 | €8.387,25 | €1.864,45 | €3.728,90 | €167,85 | €-4,73 |
| TEST | Benchmark Bollinger mean reversion 1H | 4 | €8.241,48 | €3.268,02 | €6.536,04 | €164,29 | €4,34 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.816,14 | €-182,77 | 60 | 60 | 41,67% | 0,88 | €-3,05 | 6,86% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.807,60 | €1.056,94 | 58 | 58 | 56,90% | 2,18 | €18,22 | 4,35% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.492,16 | €1.424,07 | 162 | 162 | 43,83% | 1,40 | €8,79 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.221,59 | €1.155,10 | 130 | 130 | 42,31% | 1,44 | €8,89 | 6,75% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.067,73 | €931,11 | 190 | 190 | 44,74% | 1,30 | €4,90 | 8,85% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.014,85 | €1.016,26 | 205 | 205 | 48,78% | 1,25 | €4,96 | 7,95% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.911,93 | €792,30 | 155 | 155 | 50,32% | 1,27 | €5,11 | 10,10% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.608,37 | €609,53 | 174 | 174 | 48,28% | 1,17 | €3,50 | 5,29% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.601,69 | €471,98 | 183 | 183 | 44,81% | 1,16 | €2,58 | 7,78% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.569,02 | €570,36 | 290 | 289 | 43,45% | 1,12 | €1,97 | 9,28% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.544,23 | €545,39 | 89 | 80 | 48,31% | 1,26 | €6,13 | 3,89% |
| TEST | Combo Adaptive | Combo Adaptive | €10.491,31 | €365,71 | 217 | 217 | 46,54% | 1,11 | €1,69 | 8,17% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.481,64 | €396,91 | 229 | 229 | 48,91% | 1,11 | €1,73 | 9,50% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.452,58 | €324,34 | 211 | 211 | 47,87% | 1,10 | €1,54 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.452,58 | €324,34 | 211 | 211 | 47,87% | 1,10 | €1,54 | 10,31% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.414,29 | €330,11 | 273 | 273 | 44,32% | 1,07 | €1,21 | 9,48% |
| TEST | Combo Scanner | Combo Scanner | €10.396,55 | €270,98 | 188 | 188 | 43,62% | 1,08 | €1,44 | 11,38% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.387,48 | €259,52 | 156 | 156 | 44,87% | 1,09 | €1,66 | 11,27% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.366,98 | €312,22 | 175 | 174 | 47,43% | 1,11 | €1,78 | 5,24% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.306,25 | €180,57 | 197 | 197 | 45,18% | 1,07 | €0,92 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.235,99 | €235,99 | 23 | 23 | 56,52% | 1,56 | €10,26 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.203,50 | €203,50 | 9 | 9 | 77,78% | 2,77 | €22,61 | 0,85% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.202,44 | €202,44 | 20 | 20 | 60,00% | 1,43 | €10,12 | 3,08% |
| TEST | Ampia 4H | Confluenza trend | €10.189,15 | €189,05 | 61 | 61 | 34,43% | 1,15 | €3,10 | 4,45% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.189,10 | €189,71 | 24 | 24 | 37,50% | 1,26 | €7,90 | 3,39% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.172,50 | €163,68 | 30 | 30 | 60,00% | 1,25 | €5,46 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.170,94 | €173,01 | 71 | 71 | 43,66% | 1,12 | €2,44 | 6,49% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.129,54 | €130,93 | 113 | 113 | 41,59% | 1,05 | €1,16 | 7,07% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.048,69 | €51,04 | 182 | 182 | 44,51% | 1,02 | €0,28 | 8,69% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.042,03 | €43,12 | 283 | 283 | 39,58% | 1,01 | €0,15 | 6,56% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.030,63 | €30,63 | 32 | 32 | 46,88% | 1,21 | €0,96 | 0,33% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.019,53 | €19,53 | 12 | 12 | 50,00% | 1,39 | €1,63 | 0,36% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.008,81 | €-106,34 | 171 | 171 | 42,69% | 0,97 | €-0,62 | 11,68% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.006,13 | €6,13 | 32 | 32 | 46,88% | 1,21 | €0,19 | 0,07% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.002,17 | €2,17 | 15 | 15 | 40,00% | 1,01 | €0,14 | 1,80% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,71 | €-2,29 | 12 | 12 | 33,33% | 0,62 | €-0,19 | 0,04% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.993,69 | €-5,41 | 190 | 190 | 43,16% | 1,00 | €-0,03 | 6,64% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.993,20 | €-6,80 | 5 | 5 | 20,00% | 0,05 | €-1,36 | 0,07% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.990,47 | €-34,33 | 28 | 28 | 46,43% | 0,96 | €-1,23 | 4,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.988,57 | €-11,43 | 12 | 12 | 33,33% | 0,62 | €-0,95 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.985,57 | €-14,43 | 22 | 22 | 36,36% | 0,31 | €-0,66 | 0,17% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.966,02 | €-33,98 | 5 | 5 | 20,00% | 0,05 | €-6,80 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.955,89 | €-44,11 | 5 | 5 | 20,00% | 0,09 | €-8,82 | 0,45% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.942,39 | €-57,61 | 32 | 32 | 46,88% | 0,67 | €-1,80 | 0,84% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.940,92 | €-59,08 | 22 | 22 | 31,82% | 0,53 | €-2,69 | 0,73% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.939,78 | €-60,22 | 16 | 16 | 50,00% | 0,85 | €-3,76 | 1,98% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Sol Ema 1H | Trend following EMA | €9.936,07 | €-72,30 | 30 | 30 | 40,00% | 0,92 | €-2,41 | 4,45% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.934,84 | €-65,16 | 14 | 14 | 50,00% | 0,80 | €-4,65 | 2,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.927,87 | €-72,13 | 22 | 22 | 36,36% | 0,31 | €-3,28 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.884,45 | €-114,38 | 264 | 264 | 41,67% | 0,98 | €-0,43 | 10,60% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.868,16 | €-131,84 | 12 | 12 | 50,00% | 0,70 | €-10,99 | 4,16% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.867,92 | €-134,45 | 200 | 199 | 44,50% | 0,96 | €-0,67 | 7,10% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.840,62 | €-158,16 | 188 | 188 | 45,74% | 0,97 | €-0,84 | 8,44% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.835,16 | €-163,55 | 145 | 138 | 40,00% | 0,95 | €-1,13 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.804,97 | €-186,23 | 18 | 18 | 50,00% | 0,64 | €-10,35 | 2,83% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.795,11 | €-280,22 | 216 | 216 | 41,20% | 0,93 | €-1,30 | 10,86% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.789,37 | €-216,93 | 168 | 168 | 41,67% | 0,94 | €-1,29 | 11,78% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.784,51 | €-298,29 | 22 | 22 | 36,36% | 0,54 | €-13,56 | 3,93% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.784,07 | €-337,27 | 159 | 159 | 36,48% | 0,89 | €-2,12 | 7,34% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.783,64 | €-222,65 | 172 | 172 | 41,86% | 0,94 | €-1,29 | 12,06% |
| TEST | Eth Ema 4H | Trend following EMA | €9.783,14 | €-216,86 | 9 | 9 | 22,22% | 0,41 | €-24,10 | 2,32% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.737,75 | €-382,21 | 148 | 148 | 43,92% | 0,86 | €-2,58 | 12,28% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.701,70 | €-293,39 | 19 | 19 | 36,84% | 0,57 | €-15,44 | 3,47% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.676,47 | €-323,53 | 23 | 23 | 34,78% | 0,61 | €-14,07 | 4,65% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.632,45 | €-365,31 | 138 | 138 | 43,48% | 0,84 | €-2,65 | 9,26% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.632,20 | €-447,32 | 237 | 237 | 42,19% | 0,91 | €-1,89 | 10,92% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.624,82 | €-373,39 | 268 | 268 | 41,04% | 0,93 | €-1,39 | 12,52% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.556,53 | €-561,98 | 176 | 176 | 37,50% | 0,84 | €-3,19 | 8,78% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.551,14 | €-522,31 | 179 | 179 | 39,66% | 0,84 | €-2,92 | 10,86% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.538,51 | €-460,31 | 90 | 90 | 45,56% | 0,79 | €-5,11 | 6,28% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.518,61 | €-598,84 | 216 | 216 | 40,28% | 0,86 | €-2,77 | 14,04% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.516,76 | €-490,01 | 25 | 25 | 36,00% | 0,44 | €-19,60 | 5,20% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.510,48 | €-488,31 | 100 | 100 | 38,00% | 0,80 | €-4,88 | 8,88% |
| TEST | Eth Ema 1H | Trend following EMA | €9.470,91 | €-535,83 | 33 | 33 | 36,36% | 0,52 | €-16,24 | 5,60% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.460,99 | €-648,23 | 116 | 116 | 30,17% | 0,78 | €-5,59 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.450,93 | €-658,17 | 111 | 111 | 32,43% | 0,78 | €-5,93 | 7,98% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.414,37 | €-694,30 | 113 | 113 | 31,86% | 0,78 | €-6,14 | 7,80% |
| TEST | Btc Ema 1H | Trend following EMA | €9.403,14 | €-595,52 | 27 | 27 | 25,93% | 0,38 | €-22,06 | 6,30% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.396,49 | €-709,40 | 102 | 102 | 30,39% | 0,75 | €-6,95 | 8,44% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.368,60 | €-630,73 | 95 | 95 | 33,68% | 0,73 | €-6,64 | 7,96% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.319,31 | €-679,21 | 71 | 71 | 30,99% | 0,65 | €-9,57 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.319,31 | €-679,21 | 71 | 71 | 30,99% | 0,65 | €-9,57 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.319,31 | €-679,21 | 71 | 71 | 30,99% | 0,65 | €-9,57 | 9,06% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.317,23 | €-687,93 | 175 | 161 | 43,43% | 0,81 | €-3,93 | 11,82% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.305,66 | €-707,82 | 202 | 202 | 43,07% | 0,87 | €-3,50 | 15,94% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.291,09 | €-811,71 | 158 | 158 | 39,24% | 0,71 | €-5,14 | 12,31% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.290,18 | €-817,06 | 147 | 147 | 41,50% | 0,75 | €-5,56 | 9,02% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.282,83 | €-722,34 | 106 | 106 | 25,47% | 0,75 | €-6,81 | 11,41% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.267,65 | €-745,93 | 240 | 240 | 41,67% | 0,88 | €-3,11 | 15,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.259,04 | €-861,70 | 201 | 201 | 39,30% | 0,77 | €-4,29 | 15,68% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.254,74 | €-743,80 | 62 | 62 | 30,65% | 0,58 | €-12,00 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.240,66 | €-757,87 | 63 | 63 | 30,16% | 0,56 | €-12,03 | 9,08% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.225,39 | €-886,82 | 155 | 155 | 35,48% | 0,69 | €-5,72 | 14,10% |
| TEST | Combo Trend | Combo Trend | €9.175,38 | €-921,72 | 192 | 192 | 39,58% | 0,78 | €-4,80 | 14,08% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.169,55 | €-829,00 | 90 | 90 | 31,11% | 0,64 | €-9,21 | 10,17% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.145,92 | €-964,00 | 229 | 229 | 41,05% | 0,75 | €-4,21 | 15,45% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.062,49 | €-937,14 | 160 | 160 | 38,75% | 0,77 | €-5,86 | 11,47% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.052,81 | €-1.057,30 | 135 | 135 | 34,81% | 0,59 | €-7,83 | 14,10% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.005,81 | €-1.105,26 | 171 | 171 | 40,35% | 0,65 | €-6,46 | 13,79% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €8.970,69 | €-1.027,78 | 120 | 120 | 31,67% | 0,71 | €-8,56 | 10,55% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.970,21 | €-1.028,69 | 64 | 64 | 28,12% | 0,48 | €-16,07 | 12,43% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.958,47 | €-1.035,72 | 126 | 126 | 37,30% | 0,69 | €-8,22 | 13,14% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.948,64 | €-1.050,04 | 82 | 82 | 28,05% | 0,65 | €-12,81 | 13,60% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.733,06 | €-1.258,81 | 253 | 253 | 39,53% | 0,78 | €-4,98 | 19,03% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.684,09 | €-1.309,29 | 151 | 151 | 37,75% | 0,66 | €-8,67 | 13,91% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.682,93 | €-1.329,39 | 82 | 82 | 37,80% | 0,53 | €-16,21 | 16,01% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.613,63 | €-1.551,70 | 167 | 167 | 33,53% | 0,57 | €-9,29 | 19,11% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.387,25 | €-1.605,79 | 127 | 127 | 34,65% | 0,52 | €-12,64 | 18,33% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.241,48 | €-1.758,74 | 142 | 142 | 42,25% | 0,58 | €-12,39 | 19,96% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,93739 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,00 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,15304 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €116,92 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €2,42 |
| Bilanciata 1H V1 | SOXL | SHORT | Confluenza trend | 60m | 3,0x | 103,87764 | 103,87764 | 107,92422 | 137,98413 | 95,78446 | €357,45 | €1.072,35 | €41,77 | €-0,00 |
| Bilanciata 1H V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 98,21235 | 97,05100 | 100,41559 | 130,45874 | 93,80587 | €33,77 | €101,31 | €2,27 | €1,20 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,08040 | 0,08004 | 0,08221 | 0,10680 | 0,07679 | €12,54 | €37,61 | €0,85 | €0,17 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 75742,76842 | 75715,45000 | 76841,56043 | 100611,64405 | 73545,18440 | €54,24 | €162,71 | €2,36 | €0,06 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,29827 | 1,29595 | 1,34088 | 1,72454 | 1,21306 | €451,28 | €1.353,85 | €44,43 | €2,42 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,15355 | 0,15304 | 0,14495 | 0,10313 | 0,17076 | €15,69 | €47,07 | €2,64 | €-0,16 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,15304 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €7,92 |
| Bilanciata 1H V2 | SOPH | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €129,45 | €388,36 | €46,60 | €-0,00 |
| Bilanciata 1H V2 | ENA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,14148 | 0,14148 | 0,14759 | 0,18793 | 0,12926 | €343,49 | €1.030,46 | €44,49 | €-0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,15304 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €119,89 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,58 | €28,74 | €1,07 | €0,00 |
| Bilanciata 1H V3 Filtered | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €109,03 | €327,10 | €39,25 | €-0,00 |
| Bilanciata 1H V3 Filtered | SUI | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,73075 | 0,73075 | 0,75468 | 0,97068 | 0,68290 | €12,28 | €36,85 | €1,21 | €-0,00 |
| Bilanciata 1H V3 Filtered | SOXL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 102,36854 | 102,36854 | 106,30692 | 135,97955 | 94,49179 | €12,73 | €38,19 | €1,47 | €-0,00 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 97,02159 | 97,05100 | 99,11892 | 128,87701 | 92,82694 | €37,85 | €113,54 | €2,45 | €-0,03 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,15304 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €10,52 |
| 1H Fast Score 6 75 V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,54 | €403,62 | €48,43 | €-0,00 |
| 1H Fast Score 6 75 V1 | BR | SHORT | Momentum / breakout | 60m | 3,0x | 0,25333 | 0,25333 | 0,28373 | 0,33651 | 0,20773 | €124,36 | €373,09 | €44,77 | €-0,00 |
| 1H Fast Score 6 75 V1 | ETH | SHORT | Momentum / breakout | 60m | 3,0x | 2403,12928 | 2398,14000 | 2443,54148 | 3192,15672 | 2342,51097 | €855,82 | €2.567,47 | €43,18 | €5,33 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,15304 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €10,24 |
| 1H Fast Score 6 75 No Trend Up V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,17 | €402,52 | €48,30 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BR | SHORT | Momentum / breakout | 60m | 3,0x | 0,25333 | 0,25333 | 0,28373 | 0,33651 | 0,20773 | €124,96 | €374,89 | €44,99 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ETH | SHORT | Momentum / breakout | 60m | 3,0x | 2403,12928 | 2398,14000 | 2443,54148 | 3192,15672 | 2342,51097 | €894,92 | €2.684,75 | €45,15 | €5,57 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €138,52 | €415,55 | €49,87 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 102,89822 | 102,89822 | 105,54782 | 136,68314 | 98,92383 | €55,88 | €167,63 | €4,32 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €126,49 | €379,47 | €45,54 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,72256 | 0,72256 | 0,74037 | 0,95979 | 0,69583 | €10,60 | €31,79 | €0,78 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €77,16 |
| 1H Fast Nohigh Cap75 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 102,89822 | 102,89822 | 105,54782 | 136,68314 | 98,92383 | €10,17 | €30,51 | €0,79 | €-0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,72256 | 0,72256 | 0,74134 | 0,95979 | 0,69438 | €10,84 | €32,53 | €0,85 | €-0,00 |
| 1H Fast No Pepe V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 103,09810 | 103,09810 | 105,72127 | 136,94865 | 99,16336 | €17,18 | €51,53 | €1,31 | €-0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| 1H Fast Tp2 V1 | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,12852 | €19,37 | €58,12 | €2,22 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €87,14 |
| Rapida 1H V3 Filtered | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,13118 | €23,75 | €71,25 | €2,72 | €-0,00 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SOPH | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €123,86 | €371,59 | €44,59 | €-0,00 |
| 1H Fast V3 Cap75 V1 | LONGXIA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14594 | 0,14594 | 0,12843 | 0,09802 | 0,17221 | €116,19 | €348,57 | €41,83 | €0,00 |
| 1H Fast V3 Cap75 V1 | NEAR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,32054 | 2,32054 | 2,38738 | 3,08245 | 2,22027 | €14,21 | €42,62 | €1,23 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15408 | 0,15304 | 0,14753 | 0,10349 | 0,16391 | €337,70 | €1.013,10 | €43,06 | €-6,84 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | LONGXIA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14685 | 0,14685 | 0,12923 | 0,09863 | 0,17328 | €130,94 | €392,81 | €47,14 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | LONGXIA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14685 | 0,14685 | 0,12923 | 0,09863 | 0,17328 | €137,58 | €412,73 | €49,53 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €81,58 |
| 1H Fast V3 No Esports V1 | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,13118 | €22,41 | €67,23 | €2,57 | €-0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | LONGXIA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14685 | 0,14685 | 0,12923 | 0,09863 | 0,17328 | €134,30 | €402,90 | €48,35 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €87,71 |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,13118 | €23,90 | €71,71 | €2,74 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | PUMP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00383 | 0,00383 | 0,00398 | 0,00508 | 0,00359 | €11,48 | €34,44 | €1,41 | €-0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | LONGXIA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14528 | 0,14528 | 0,12785 | 0,09758 | 0,17143 | €135,50 | €406,49 | €48,78 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,72745 | 0,72745 | 0,78235 | 1,08754 | 0,57376 | €23,11 | €46,21 | €3,49 | €-0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08143 | 0,08004 | 0,08517 | 0,12174 | 0,07096 | €31,75 | €63,49 | €2,92 | €1,08 |
| Ampia 4H | SOL | SHORT | Confluenza trend | 240m | 2,0x | 97,48250 | 97,05100 | 102,49471 | 145,73634 | 83,44831 | €17,85 | €35,69 | €1,84 | €0,16 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €107,35 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €60,42 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €13,42 | €26,84 | €0,90 | €0,00 |
| Forza relativa 1H V1 | ENA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,14025 | 0,14025 | 0,14705 | 0,20968 | 0,12529 | €14,26 | €28,51 | €1,38 | €-0,00 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,72256 | 0,72256 | 0,74546 | 1,08022 | 0,67216 | €672,88 | €1.345,76 | €42,66 | €-0,00 |
| Forza relativa 1H V1 | SOL | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 97,02159 | 97,05100 | 99,11892 | 145,04728 | 92,40747 | €29,78 | €59,56 | €1,29 | €-0,02 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ENA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,14147 | 0,14147 | 0,14728 | 0,21150 | 0,12869 | €12,62 | €25,24 | €1,04 | €-0,00 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €69,44 |
| Benchmark Donchian breakout 1H | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,56868 | 59,42929 | 84,57018 | 49,41718 | €19,03 | €38,06 | €1,92 | €-0,00 |
| Benchmark Donchian breakout 1H | ENA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,13916 | 0,13916 | 0,14676 | 0,20805 | 0,12016 | €18,63 | €37,26 | €2,03 | €-0,00 |
| Benchmark Donchian breakout 1H | UNI | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 6,24425 | 6,24425 | 6,42997 | 9,33516 | 5,77996 | €20,81 | €41,62 | €1,24 | €-0,00 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €67,80 |
| Donchian 1H Gb20 120R V1 | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,56868 | 59,42929 | 84,57018 | 49,41718 | €18,58 | €37,16 | €1,88 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ENA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,13916 | 0,13916 | 0,14676 | 0,20805 | 0,12016 | €18,19 | €36,38 | €1,99 | €-0,00 |
| Donchian 1H Gb20 120R V1 | UNI | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 6,24425 | 6,24425 | 6,42997 | 9,33516 | 5,77996 | €20,32 | €40,64 | €1,21 | €-0,00 |
| Benchmark Bollinger mean reversion 1H | DASH | LONG | Bollinger mean reversion | 60m | 2,0x | 57,17143 | 57,17143 | 54,76797 | 28,87157 | 60,77663 | €497,61 | €995,23 | €41,84 | €0,00 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 97,17943 | 97,05100 | 95,33648 | 49,07561 | 99,94386 | €1.086,31 | €2.172,61 | €41,20 | €-2,87 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,08027 | 0,08004 | 0,07874 | 0,04053 | 0,08256 | €1.080,65 | €2.161,30 | €41,19 | €-6,09 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,28183 | 1,29595 | 1,23929 | 0,64732 | 1,34563 | €603,45 | €1.206,90 | €40,05 | €13,30 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,15304 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €103,96 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €71,53 | €143,05 | €6,46 | €0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €138,07 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,02778 | 0,02777 | 0,02445 | 0,01403 | 0,03445 | €13,77 | €27,53 | €3,30 | €-0,01 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €128,47 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,67309 | €15,10 | €30,20 | €1,12 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,02778 | 0,02777 | 0,02445 | 0,01403 | 0,03445 | €16,14 | €32,28 | €3,87 | €-0,01 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €129,66 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,02727 | 0,02777 | 0,02400 | 0,01377 | 0,03382 | €15,96 | €31,92 | €3,83 | €0,59 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €129,66 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,02727 | 0,02777 | 0,02400 | 0,01377 | 0,03382 | €15,96 | €31,92 | €3,83 | €0,59 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €129,32 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €121,23 |
| Scanner Top5 Btc Mfe V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €122,06 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,02778 | 0,02777 | 0,02445 | 0,01403 | 0,03511 | €17,78 | €35,56 | €4,27 | €-0,01 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €17,38 | €34,75 | €1,16 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €433,72 | €867,43 | €41,49 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15408 | 0,15304 | 0,14566 | 0,07781 | 0,17261 | €349,81 | €699,62 | €38,24 | €-4,73 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €119,23 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,02778 | 0,02777 | 0,02445 | 0,01403 | 0,03511 | €17,37 | €34,73 | €4,17 | €-0,01 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,72626 | €12,97 | €25,94 | €0,97 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15408 | 0,15304 | 0,14566 | 0,07781 | 0,17261 | €377,50 | €755,01 | €41,26 | €-5,10 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,17903 | €673,21 | €1.346,41 | €44,12 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €462,02 | €924,05 | €44,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15408 | 0,15304 | 0,14566 | 0,07781 | 0,17261 | €374,96 | €749,93 | €40,99 | €-5,07 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €8,29 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,02778 | 0,02777 | 0,02445 | 0,01403 | 0,03778 | €167,20 | €334,41 | €40,13 | €-0,07 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €8,29 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,02778 | 0,02777 | 0,02445 | 0,01403 | 0,03778 | €167,30 | €334,60 | €40,15 | €-0,07 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08414 | 0,08004 | 0,08114 | 0,12579 | 0,07812 | €847,30 | €1.694,61 | €0,00 | €82,64 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,15304 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €99,76 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €68,62 | €137,24 | €6,19 | €0,00 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,28183 | 1,29595 | 1,23929 | 0,64732 | 1,34989 | €653,10 | €1.306,20 | €43,35 | €14,39 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €127,55 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €0,00 |
| Combo Scanner | TAO | LONG | Combo Scanner | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 288,22268 | €105,11 | €210,22 | €8,41 | €0,00 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €128,01 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,79 | €25,58 | €0,86 | €0,00 |
| Combo Adaptive | DASH | SHORT | Combo Adaptive | 60m | 2,0x | 55,60888 | 55,60888 | 57,81052 | 83,13527 | 51,20558 | €15,51 | €31,02 | €1,23 | €-0,00 |
| Combo Adaptive | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29595 | 1,33225 | 1,92042 | 1,18918 | €35,04 | €70,07 | €2,60 | €-0,62 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €111,81 |
| Combo Adaptive Mfe Trail | DASH | SHORT | Combo Adaptive | 60m | 2,0x | 55,60888 | 55,60888 | 57,81052 | 83,13527 | 51,20558 | €21,30 | €42,61 | €1,69 | €-0,00 |
| Combo Adaptive Mfe Trail | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29595 | 1,33225 | 1,92042 | 1,18918 | €30,64 | €61,28 | €2,28 | €-0,54 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €132,90 |
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €15,48 | €30,96 | €1,04 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,02813 | 0,02777 | 0,02476 | 0,01421 | 0,03489 | €14,50 | €29,01 | €3,48 | €-0,37 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 286,10361 | €49,09 | €98,18 | €3,93 | €0,00 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €114,50 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €17,00 | €34,01 | €1,14 | €0,00 |
| Combo Adaptive Runner25 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €536,57 | €1.073,13 | €42,92 | €0,00 |
| Combo Adaptive Runner25 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €73,50 | €146,99 | €4,81 | €-0,00 |
| Combo Adaptive Runner25 V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29595 | 1,33225 | 1,92042 | 1,14149 | €31,43 | €62,85 | €2,33 | €-0,56 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €112,36 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €16,69 | €33,37 | €1,12 | €0,00 |
| Combo Adaptive Tp3 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €526,53 | €1.053,06 | €42,12 | €0,00 |
| Combo Adaptive Tp3 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €72,15 | €144,29 | €4,72 | €-0,00 |
| Combo Adaptive Tp3 V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29595 | 1,33225 | 1,92042 | 1,14149 | €30,84 | €61,68 | €2,29 | €-0,55 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 75728,63124 | 75715,45000 | 76866,46226 | 100592,86517 | 73452,96997 | €1.043,20 | €3.129,59 | €47,02 | €0,54 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 97,48250 | 97,05100 | 99,66654 | 129,48925 | 93,11442 | €738,52 | €2.215,57 | €49,64 | €9,81 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 97,17943 | 97,05100 | 95,33648 | 65,27219 | 99,94386 | €853,06 | €2.559,17 | €48,53 | €-3,38 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 98,21235 | 97,05100 | 100,41559 | 130,45874 | 93,80587 | €740,39 | €2.221,17 | €49,83 | €26,27 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 2406,82854 | 2398,14000 | 2457,77157 | 3197,07057 | 2304,94248 | €745,23 | €2.235,70 | €47,32 | €8,07 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 2406,82854 | 2398,14000 | 2457,77157 | 3197,07057 | 2304,94248 | €748,84 | €2.246,52 | €47,55 | €8,11 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08040 | 0,08004 | 0,08221 | 0,10680 | 0,07679 | €753,18 | €2.259,53 | €50,82 | €10,23 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08027 | 0,08004 | 0,07874 | 0,05391 | 0,08256 | €858,16 | €2.574,49 | €49,07 | €-7,25 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,15304 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €108,51 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €481,98 | €963,96 | €46,11 | €0,00 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,09236 | €13,27 | €26,55 | €0,87 | €0,00 |
| Master Adaptive Strict3 V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €465,87 | €931,73 | €44,57 | €0,00 |
| Master Adaptive Strict3 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28110 | 0,28110 | 0,24944 | 0,14195 | 0,34441 | €15,82 | €31,64 | €3,56 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,15304 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €107,08 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,15304 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €105,75 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,15304 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €117,23 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,54 | €25,08 | €0,84 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,29595 | 1,33225 | 1,92042 | 1,18918 | €28,88 | €57,77 | €2,14 | €-0,51 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,15304 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €109,05 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,15304 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €108,93 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,15304 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €5,11 |
| Master Adaptive Gb20 Loss Cap V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,45236 | 0,23694 | 0,51408 | €80,25 | €160,51 | €5,76 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | LONGXIA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14528 | 0,14528 | 0,12785 | 0,07337 | 0,19177 | €176,75 | €353,51 | €42,42 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,02777 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €753,05 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | SUI | SHORT | Confluenza trend | 240m | 3,0x | 0,72995 | 0,72995 | 0,77421 | 0,96962 | 0,64144 | €294,19 | €882,58 | €53,51 | €-0,00 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,29295 | 1,29595 | 1,37261 | 1,71747 | 1,13364 | €83,64 | €250,92 | €15,46 | €-0,58 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,15304 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €121,61 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,09542 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €0,00 |
| Combo Trend Side Regime Guard V1 | TAO | LONG | Combo Trend | 60m | 2,0x | 264,91297 | 264,91297 | 253,14039 | 133,78105 | 290,81264 | €73,76 | €147,52 | €6,56 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €75,23 |
| 1H Fast Nohigh Cap75 Short Only V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 102,89822 | 102,89822 | 105,54782 | 136,68314 | 98,92383 | €9,92 | €29,75 | €0,77 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,15304 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €113,39 |
| 1H Balanced V3 Long Only V1 | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,06 | €27,18 | €1,01 | €0,00 |
| 1H Balanced V3 Long Only V1 | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €103,13 | €309,38 | €37,13 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SUI | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,73075 | 0,73075 | 0,75468 | 0,97068 | 0,68290 | €11,12 | €33,36 | €1,09 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SOXL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 102,46848 | 102,46848 | 106,45133 | 136,11230 | 94,50278 | €12,84 | €38,53 | €1,50 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 97,02159 | 97,05100 | 99,11892 | 128,87701 | 92,82694 | €35,79 | €107,38 | €2,32 | €-0,03 |
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
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | 2026-09-16T04:30:00+00:00 | 0,08063 | €0,63 | 0,56 | STOP |
| Benchmark Donchian breakout 1H | DOGE | SHORT | 2026-09-16T04:30:00+00:00 | 0,08063 | €0,64 | 0,56 | STOP |
| Master Adaptive V1 | POWER | LONG | 2026-09-16T04:15:00+00:00 | 0,13190 | €-62,82 | -1,43 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Runner25 V1 | POWER | LONG | 2026-09-16T04:15:00+00:00 | 0,13190 | €-55,93 | -1,43 | STOP_STRESS_SLIPPAGE |
| Master Adaptive No Alt V1 | POWER | LONG | 2026-09-16T04:15:00+00:00 | 0,13190 | €-61,21 | -1,43 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Gb20 V1 | POWER | LONG | 2026-09-16T04:15:00+00:00 | 0,13190 | €-61,98 | -1,43 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Gb20 Partial V1 | POWER | LONG | 2026-09-16T04:15:00+00:00 | 0,13190 | €-63,07 | -1,43 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Gb20 Be V1 | POWER | LONG | 2026-09-16T04:15:00+00:00 | 0,13190 | €-63,14 | -1,43 | STOP_STRESS_SLIPPAGE |
| Scanner Top 5 Long 1H | AKE | LONG | 2026-09-16T03:30:00+00:00 | 0,02537 | €-3,69 | -1,10 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | 2026-09-16T03:30:00+00:00 | 0,02537 | €-45,30 | -1,10 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | 2026-09-16T03:30:00+00:00 | 0,02537 | €-45,27 | -1,10 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Guard V1 | AKE | LONG | 2026-09-16T03:30:00+00:00 | 0,02537 | €-4,78 | -1,10 | STOP_STRESS_SLIPPAGE |

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

Generato: 2026-09-16 05:32 UTC


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

Segnali totali salvati: **204**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-16 | BTC | 75.786,49 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-16 | DOGE | 0.08011 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-16 | SOL | 97,05 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-15 | BTC | 77.430,91 | +4 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-15 | DOGE | 0.08280 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-15 | SOL | 100,84 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-14 | BTC | 77.497,87 | +3 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-14 | DOGE | 0.08404 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-14 | SOL | 101,01 | +3 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-13 | BTC | 77.274,99 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-13 | DOGE | 0.08485 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-13 | SOL | 101,86 | +4 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 68 | 67 | 66 | 65 | 63 | 61 | 58 | 54 | 47 | 38 | 25 | 10 |
| SOL | 68 | 67 | 66 | 65 | 63 | 61 | 58 | 54 | 47 | 38 | 25 | 10 |
| DOGE | 68 | 67 | 66 | 65 | 63 | 61 | 58 | 54 | 47 | 38 | 25 | 10 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-19 | 60g | 2026-09-17 | domani |
| SOL | 2026-07-19 | 60g | 2026-09-17 | domani |
| DOGE | 2026-07-19 | 60g | 2026-09-17 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 64 | 50,00% | +0,30% | +0,28% | UTILE |
| BTC | 2g | 63 | 50,79% | +0,55% | +0,47% | UTILE |
| BTC | 3g | 62 | 45,16% | +0,69% | +0,58% | UTILE |
| BTC | 5g | 60 | 41,67% | +1,43% | +1,22% | UTILE |
| BTC | 7g | 58 | 50,00% | +2,01% | +1,82% | PRIMA CALIBRAZIONE |
| BTC | 10g | 55 | 56,36% | +2,95% | +2,79% | PRIMA CALIBRAZIONE |
| BTC | 14g | 51 | 54,90% | +4,74% | +4,67% | PRIMA CALIBRAZIONE |
| BTC | 21g | 44 | 63,64% | +9,09% | +8,94% | PRIMA CALIBRAZIONE |
| BTC | 30g | 36 | 91,67% | +15,05% | +13,85% | PRIMA CALIBRAZIONE |
| BTC | 45g | 23 | 86,96% | +22,04% | +16,28% | FEEDBACK RAPIDO |
| BTC | 60g | 9 | 77,78% | +22,72% | +13,23% | FEEDBACK RAPIDO |
| SOL | 1g | 60 | 51,67% | +0,46% | +0,35% | UTILE |
| SOL | 2g | 59 | 47,46% | +0,98% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 3g | 58 | 53,45% | +1,60% | +1,45% | PRIMA CALIBRAZIONE |
| SOL | 5g | 56 | 55,36% | +2,77% | +2,67% | PRIMA CALIBRAZIONE |
| SOL | 7g | 54 | 59,26% | +3,87% | +3,97% | PRIMA CALIBRAZIONE |
| SOL | 10g | 51 | 62,75% | +5,63% | +5,78% | PRIMA CALIBRAZIONE |
| SOL | 14g | 47 | 70,21% | +8,58% | +9,35% | PRIMA CALIBRAZIONE |
| SOL | 21g | 40 | 77,50% | +15,70% | +14,81% | PRIMA CALIBRAZIONE |
| SOL | 30g | 31 | 67,74% | +21,97% | +15,59% | PRIMA CALIBRAZIONE |
| SOL | 45g | 19 | 42,11% | +33,98% | -6,53% | FEEDBACK RAPIDO |
| SOL | 60g | 9 | 33,33% | +32,96% | -10,60% | FEEDBACK RAPIDO |
| DOGE | 1g | 63 | 46,03% | +0,27% | +0,15% | UTILE |
| DOGE | 2g | 62 | 46,77% | +0,58% | +0,28% | UTILE |
| DOGE | 3g | 61 | 40,98% | +0,90% | +0,49% | UTILE |
| DOGE | 5g | 59 | 47,46% | +1,55% | +1,26% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 57 | 56,14% | +1,95% | +2,27% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 54 | 55,56% | +2,41% | +3,37% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 50 | 68,00% | +4,51% | +6,50% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 45 | 71,11% | +7,88% | +7,00% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 36 | 77,78% | +13,42% | +7,22% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 24 | 20,83% | +20,09% | -11,91% | FEEDBACK RAPIDO |
| DOGE | 60g | 10 | 0,00% | +17,41% | -17,41% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 64 | 50,00% | +0,30% | +0,28% | -0,15% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 67 | 52,24% | +0,29% | +0,29% | -0,15% | +0,80% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 67 | 52,24% | +0,29% | +0,29% | -0,15% | +0,80% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 62 | 40,32% | +0,39% | +0,05% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 26 | 42,31% | +0,67% | +0,43% | +0,02% | +1,19% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 63 | 50,79% | +0,55% | +0,47% | -0,02% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 66 | 53,03% | +0,64% | +0,64% | +0,07% | +1,29% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 66 | 53,03% | +0,64% | +0,64% | +0,07% | +1,29% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 61 | 44,26% | +0,78% | +0,10% | +0,21% | +1,42% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 25 | 44,00% | +1,05% | +0,61% | +0,46% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 62 | 45,16% | +0,69% | +0,58% | -1,11% | +2,44% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 65 | 52,31% | +0,96% | +0,96% | -1,09% | +2,65% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 65 | 52,31% | +0,96% | +0,96% | -1,09% | +2,65% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 60 | 36,67% | +1,21% | -0,20% | -0,95% | +2,87% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 60 | 41,67% | +1,43% | +1,22% | -1,72% | +3,81% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 63 | 47,62% | +1,67% | +1,67% | -1,69% | +4,09% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 63 | 47,62% | +1,67% | +1,67% | -1,69% | +4,09% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 58 | 39,66% | +1,91% | -1,01% | -1,53% | +4,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 58 | 50,00% | +2,01% | +1,82% | -2,01% | +4,89% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 61 | 55,74% | +2,32% | +2,32% | -1,98% | +5,17% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 61 | 55,74% | +2,32% | +2,32% | -1,98% | +5,17% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 56 | 39,29% | +2,73% | -1,83% | -1,82% | +5,53% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 55 | 56,36% | +2,95% | +2,79% | -2,19% | +6,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 58 | 60,34% | +3,14% | +3,14% | -2,18% | +6,31% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 58 | 60,34% | +3,14% | +3,14% | -2,18% | +6,31% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 53 | 43,40% | +3,54% | -1,47% | -1,99% | +6,79% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 51 | 54,90% | +4,74% | +4,67% | -2,21% | +8,50% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 54 | 55,56% | +4,85% | +4,85% | -2,21% | +8,63% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +4,85% | +4,85% | -2,21% | +8,63% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 49 | 51,02% | +5,48% | +0,53% | -1,98% | +9,34% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 22 | 31,82% | +5,27% | -3,66% | -1,53% | +9,82% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 44 | 63,64% | +9,09% | +8,94% | -2,18% | +13,19% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 47 | 70,21% | +8,94% | +8,94% | -2,19% | +13,06% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 47 | 70,21% | +8,94% | +8,94% | -2,19% | +13,06% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 42 | 40,48% | +9,82% | -1,02% | -1,92% | +14,03% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 15 | 33,33% | +10,93% | -9,70% | -0,96% | +15,50% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 36 | 91,67% | +15,05% | +13,85% | -2,64% | +19,54% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 38 | 86,84% | +14,68% | +14,68% | -2,69% | +19,20% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 38 | 86,84% | +14,68% | +14,68% | -2,69% | +19,20% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 34 | 88,24% | +15,85% | +15,85% | -2,48% | +20,63% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 33 | 39,39% | +14,98% | -4,06% | -2,43% | +19,87% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 8 | 0,00% | +23,09% | -23,09% | -0,83% | +29,47% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 23 | 86,96% | +22,04% | +16,28% | -3,04% | +27,20% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 25 | 100,00% | +22,11% | +22,11% | -3,09% | +27,16% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 25 | 100,00% | +22,11% | +22,11% | -3,09% | +27,16% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 21 | 100,00% | +22,31% | +22,31% | -2,82% | +27,53% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 20 | 25,00% | +22,39% | -11,19% | -2,74% | +27,61% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 3 | 0,00% | +21,72% | -21,72% | -1,93% | +29,65% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 9 | 77,78% | +22,72% | +13,23% | -2,48% | +29,34% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 9 | 33,33% | +22,20% | -7,65% | -2,41% | +29,34% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 63 | 46,03% | +0,27% | +0,15% | -0,40% | +1,21% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 66 | 59,09% | +0,17% | +0,56% | -0,51% | +1,06% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 66 | 59,09% | +0,17% | +0,56% | -0,51% | +1,06% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 60 | 53,33% | +0,08% | +0,45% | -0,62% | +0,95% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 39 | 43,59% | +0,08% | -0,31% | -0,58% | +0,78% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 62 | 46,77% | +0,58% | +0,28% | -0,21% | +1,79% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 65 | 58,46% | +0,41% | +0,92% | -0,37% | +1,54% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 65 | 58,46% | +0,41% | +0,92% | -0,37% | +1,54% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 59 | 55,93% | +0,04% | +0,63% | -0,73% | +1,14% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 38 | 44,74% | +0,23% | -0,96% | -0,53% | +1,16% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 61 | 40,98% | +0,90% | +0,49% | -1,93% | +3,95% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 64 | 56,25% | +0,72% | +1,31% | -2,06% | +3,61% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 64 | 56,25% | +0,72% | +1,31% | -2,06% | +3,61% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 58 | 46,55% | -0,06% | +0,52% | -2,33% | +2,75% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 37 | 32,43% | +0,56% | -1,92% | -2,31% | +3,73% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 59 | 47,46% | +1,55% | +1,26% | -2,90% | +6,14% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 62 | 53,23% | +1,43% | +2,16% | -2,96% | +5,89% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 62 | 53,23% | +1,43% | +2,16% | -2,96% | +5,89% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 56 | 57,14% | +0,42% | +0,48% | -3,41% | +4,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 35 | 37,14% | +1,49% | -3,98% | -3,27% | +6,12% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 57 | 56,14% | +1,95% | +2,27% | -3,41% | +7,95% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 60 | 58,33% | +2,00% | +2,86% | -3,46% | +7,75% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 60 | 58,33% | +2,00% | +2,86% | -3,46% | +7,75% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 54 | 53,70% | +0,71% | +0,73% | -4,00% | +6,43% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,88% | -5,01% | -3,79% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 54 | 55,56% | +2,41% | +3,37% | -3,70% | +9,69% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 57 | 52,63% | +2,37% | +3,05% | -3,74% | +9,52% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 57 | 52,63% | +2,37% | +3,05% | -3,74% | +9,52% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 51 | 62,75% | +0,57% | +1,32% | -4,34% | +7,46% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 32 | 40,62% | +1,78% | -4,62% | -4,22% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | -0,68% | -1,01% | -4,16% | +8,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 50 | 68,00% | +4,51% | +6,50% | -4,02% | +13,24% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 53 | 73,58% | +4,05% | +6,09% | -4,03% | +12,77% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 53 | 73,58% | +4,05% | +6,09% | -4,03% | +12,77% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 47 | 57,45% | +1,17% | +0,80% | -4,73% | +9,05% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 45 | 71,11% | +7,88% | +7,00% | -4,11% | +18,64% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 46 | 80,43% | +8,32% | +10,89% | -4,04% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 46 | 80,43% | +8,32% | +10,89% | -4,04% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 40 | 57,50% | +5,22% | -3,74% | -4,88% | +14,48% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,18% | -0,50% | -3,01% | +20,33% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 36 | 77,78% | +13,42% | +7,22% | -3,93% | +27,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 38 | 89,47% | +13,85% | +12,65% | -3,96% | +27,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 38 | 89,47% | +13,85% | +12,65% | -3,96% | +27,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 36 | 94,44% | +13,07% | +14,91% | -3,98% | +27,25% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 33 | 42,42% | +12,15% | -9,80% | -4,39% | +25,43% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 25 | 44,00% | +10,47% | -10,47% | -4,32% | +22,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 24 | 20,83% | +20,09% | -11,91% | -5,30% | +38,89% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 25 | 36,00% | +20,00% | -5,31% | -5,36% | +38,82% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 25 | 36,00% | +20,00% | -5,31% | -5,36% | +38,82% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 23 | 39,13% | +19,28% | -3,31% | -5,50% | +38,58% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 25 | 0,00% | +20,00% | -20,00% | -5,36% | +38,82% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 20 | 0,00% | +20,53% | -20,53% | -5,27% | +38,90% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 9 | 0,00% | +17,70% | -17,70% | -6,65% | +37,31% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 60 | 51,67% | +0,46% | +0,35% | -0,25% | +1,33% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 62 | 53,23% | +0,21% | +0,20% | -0,45% | +1,05% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 65 | 52,31% | +0,25% | +0,14% | -0,41% | +1,09% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 60 | 48,33% | +0,26% | +0,23% | -0,46% | +1,06% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 59 | 47,46% | +0,98% | +0,87% | +0,06% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 61 | 44,26% | +0,66% | +0,27% | -0,27% | +1,47% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 64 | 43,75% | +0,65% | +0,24% | -0,26% | +1,53% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 60 | 41,67% | +0,65% | +0,14% | -0,22% | +1,72% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 58 | 53,45% | +1,60% | +1,45% | -1,58% | +3,98% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 60 | 46,67% | +1,18% | +0,69% | -1,84% | +3,56% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 63 | 46,03% | +1,14% | +0,64% | -1,81% | +3,55% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 60 | 46,67% | +1,03% | -0,07% | -1,90% | +3,36% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 56 | 55,36% | +2,77% | +2,67% | -2,27% | +6,30% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 58 | 50,00% | +2,19% | +1,25% | -2,53% | +5,71% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 61 | 49,18% | +2,12% | +1,16% | -2,50% | +5,62% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 59 | 45,76% | +2,19% | -0,51% | -2,63% | +5,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,47% | +1,33% | -2,64% | +4,74% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 54 | 59,26% | +3,87% | +3,97% | -2,70% | +7,97% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 56 | 55,36% | +3,21% | +2,07% | -2,97% | +7,34% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 59 | 55,93% | +3,04% | +1,97% | -2,96% | +7,17% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 58 | 39,66% | +2,99% | -1,34% | -3,11% | +7,10% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 42 | 47,62% | +1,36% | +1,40% | -3,24% | +5,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 51 | 62,75% | +5,63% | +5,78% | -2,85% | +10,23% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 53 | 58,49% | +4,91% | +4,05% | -3,19% | +9,32% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 56 | 57,14% | +4,63% | +3,84% | -3,20% | +9,03% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 55 | 45,45% | +4,09% | -2,02% | -3,38% | +8,64% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 39 | 53,85% | +1,48% | +1,57% | -3,51% | +6,38% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 47 | 70,21% | +8,58% | +9,35% | -3,04% | +14,42% | PRIMA CALIBRAZIONE |

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

Generato: 2026-09-16 05:32 UTC

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
| BTC | 68 | UTILE | 67 | 18 | 8 | 0 | Famiglia statistica | 1g | 52,24% | +0,29% | campione utile, valutare con prudenza |
| SOL | 68 | UTILE | 62 | 25 | 6 | 0 | Famiglia statistica | 1g | 53,23% | +0,20% | campione utile, valutare con prudenza |
| DOGE | 68 | UTILE | 66 | 26 | 6 | 0 | Famiglia statistica | 1g | 59,09% | +0,56% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 26 | 42,31% | +0,43% | +0,67% | +0,02% | +1,19% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 67 | 52,24% | +0,29% | +0,29% | -0,15% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 62 | 40,32% | +0,05% | +0,39% | -0,07% | +0,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 25 | 44,00% | +0,61% | +1,05% | +0,46% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 66 | 53,03% | +0,64% | +0,64% | +0,07% | +1,29% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 61 | 44,26% | +0,10% | +0,78% | +0,21% | +1,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 65 | 52,31% | +0,96% | +0,96% | -1,09% | +2,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 60 | 36,67% | -0,20% | +1,21% | -0,95% | +2,87% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 63 | 47,62% | +1,67% | +1,67% | -1,69% | +4,09% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 58 | 39,66% | -1,01% | +1,91% | -1,53% | +4,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 61 | 55,74% | +2,32% | +2,32% | -1,98% | +5,17% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 56 | 39,29% | -1,83% | +2,73% | -1,82% | +5,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 24 | 50,00% | -3,59% | +5,20% | -1,59% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 58 | 60,34% | +3,14% | +3,14% | -2,18% | +6,31% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 53 | 43,40% | -1,47% | +3,54% | -1,99% | +6,79% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 22 | 31,82% | -3,66% | +5,27% | -1,53% | +9,82% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 54 | 55,56% | +4,85% | +4,85% | -2,21% | +8,63% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 49 | 51,02% | +0,53% | +5,48% | -1,98% | +9,34% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 15 | 33,33% | -9,70% | +10,93% | -0,96% | +15,50% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 47 | 70,21% | +8,94% | +8,94% | -2,19% | +13,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 42 | 40,48% | -1,02% | +9,82% | -1,92% | +14,03% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 8 | 0,00% | -23,09% | +23,09% | -0,83% | +29,47% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 38 | 86,84% | +14,68% | +14,68% | -2,69% | +19,20% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 33 | 39,39% | -4,06% | +14,98% | -2,43% | +19,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 3 | 0,00% | -21,72% | +21,72% | -1,93% | +29,65% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 25 | 100,00% | +22,11% | +22,11% | -3,09% | +27,16% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 20 | 25,00% | -11,19% | +22,39% | -2,74% | +27,61% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 9 | 33,33% | -7,65% | +22,20% | -2,41% | +29,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 39 | 43,59% | -0,31% | +0,08% | -0,58% | +0,78% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 66 | 59,09% | +0,56% | +0,17% | -0,51% | +1,06% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 60 | 53,33% | +0,45% | +0,08% | -0,62% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 38 | 44,74% | -0,96% | +0,23% | -0,53% | +1,16% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 65 | 58,46% | +0,92% | +0,41% | -0,37% | +1,54% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 59 | 55,93% | +0,63% | +0,04% | -0,73% | +1,14% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 37 | 32,43% | -1,92% | +0,56% | -2,31% | +3,73% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 64 | 56,25% | +1,31% | +0,72% | -2,06% | +3,61% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 58 | 46,55% | +0,52% | -0,06% | -2,33% | +2,75% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 35 | 37,14% | -3,98% | +1,49% | -3,27% | +6,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 62 | 53,23% | +2,16% | +1,43% | -2,96% | +5,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 56 | 57,14% | +0,48% | +0,42% | -3,41% | +4,91% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 34 | 35,29% | -5,01% | +1,88% | -3,79% | +7,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 60 | 58,33% | +2,86% | +2,00% | -3,46% | +7,75% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 54 | 53,70% | +0,73% | +0,71% | -4,00% | +6,43% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 32 | 40,62% | -4,62% | +1,78% | -4,22% | +8,99% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 57 | 52,63% | +3,05% | +2,37% | -3,74% | +9,52% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | -1,01% | -0,68% | -4,16% | +8,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 51 | 62,75% | +1,32% | +0,57% | -4,34% | +7,46% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 53 | 73,58% | +6,09% | +4,05% | -4,03% | +12,77% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 8 | 50,00% | +1,67% | +6,58% | -3,33% | +14,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 47 | 57,45% | +0,80% | +1,17% | -4,73% | +9,05% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 31 | 48,39% | -7,22% | +5,15% | -4,78% | +14,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 46 | 80,43% | +10,89% | +8,32% | -4,04% | +18,98% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 7 | 57,14% | -0,50% | +7,18% | -3,01% | +20,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 40 | 57,50% | -3,74% | +5,22% | -4,88% | +14,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 25 | 44,00% | -10,47% | +10,47% | -4,32% | +22,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 38 | 89,47% | +12,65% | +13,85% | -3,96% | +27,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 33 | 42,42% | -9,80% | +12,15% | -4,39% | +25,43% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 20 | 0,00% | -20,53% | +20,53% | -5,27% | +38,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 25 | 36,00% | -5,31% | +20,00% | -5,36% | +38,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 25 | 0,00% | -20,00% | +20,00% | -5,36% | +38,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 9 | 0,00% | -17,70% | +17,70% | -6,65% | +37,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 10 | 0,00% | -17,41% | +17,41% | -6,79% | +37,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 10 | 0,00% | -17,41% | +17,41% | -6,79% | +37,10% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 62 | 53,23% | +0,20% | +0,21% | -0,45% | +1,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 60 | 48,33% | +0,23% | +0,26% | -0,46% | +1,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 61 | 44,26% | +0,27% | +0,66% | -0,27% | +1,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 60 | 41,67% | +0,14% | +0,65% | -0,22% | +1,72% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 42 | 52,38% | +0,88% | +1,01% | -1,83% | +3,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 60 | 46,67% | +0,69% | +1,18% | -1,84% | +3,56% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 60 | 46,67% | -0,07% | +1,03% | -1,90% | +3,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 42 | 54,76% | +1,33% | +1,47% | -2,64% | +4,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 58 | 50,00% | +1,25% | +2,19% | -2,53% | +5,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 59 | 45,76% | -0,51% | +2,19% | -2,63% | +5,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 42 | 47,62% | +1,40% | +1,36% | -3,24% | +5,52% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 56 | 55,36% | +2,07% | +3,21% | -2,97% | +7,34% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 58 | 39,66% | -1,34% | +2,99% | -3,11% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 39 | 53,85% | +1,57% | +1,48% | -3,51% | +6,38% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 53 | 58,49% | +4,05% | +4,91% | -3,19% | +9,32% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 55 | 45,45% | -2,02% | +4,09% | -3,38% | +8,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 35 | 45,71% | +0,98% | +2,41% | -3,75% | +7,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 49 | 71,43% | +7,32% | +8,15% | -3,33% | +13,38% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 51 | 37,25% | -4,26% | +6,19% | -3,60% | +11,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 28 | 50,00% | -6,40% | +10,38% | -3,57% | +16,02% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 42 | 78,57% | +15,51% | +15,58% | -3,35% | +21,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 44 | 40,91% | -11,03% | +12,63% | -3,81% | +18,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 34 | 91,18% | +25,29% | +25,60% | -4,46% | +32,86% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 36 | 11,11% | -22,79% | +22,27% | -4,85% | +28,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 17 | 0,00% | -36,25% | +36,25% | -5,53% | +46,74% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 21 | 61,90% | +11,31% | +33,86% | -6,34% | +43,22% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 25 | 16,00% | -26,35% | +34,22% | -6,43% | +43,10% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Classic technical | 3 | 0,00% | -32,23% | +32,23% | -6,17% | +46,05% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 7 | 14,29% | -23,98% | +32,93% | -7,87% | +43,40% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 10 | 40,00% | -5,83% | +32,95% | -7,56% | +43,89% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 64 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 67 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 75 | 42,67% | +0,42% |
| BTC | BREVE | Famiglia statistica | 198 | 52,53% | +0,63% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 183 | 40,44% | -0,01% |
| BTC | SETTIMANALE | Classic technical | 72 | 48,61% | -2,51% |
| BTC | SETTIMANALE | Famiglia statistica | 182 | 54,40% | +2,36% |
| BTC | SETTIMANALE | Microstruttura exchange | 15 | 33,33% | -1,25% |
| BTC | SETTIMANALE | Tecnico | 167 | 40,72% | -1,43% |
| BTC | SWING | Classic technical | 37 | 32,43% | -6,11% |
| BTC | SWING | Famiglia statistica | 101 | 62,38% | +6,76% |
| BTC | SWING | Microstruttura exchange | 6 | 50,00% | -0,28% |
| BTC | SWING | Tecnico | 91 | 46,15% | -0,19% |
| BTC | MEDIO | Classic technical | 11 | 0,00% | -22,71% |
| BTC | MEDIO | Famiglia statistica | 73 | 93,15% | +18,27% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 62 | 33,87% | -6,88% |
| DOGE | BREVE | Classic technical | 114 | 40,35% | -1,05% |
| DOGE | BREVE | Famiglia statistica | 195 | 57,95% | +0,92% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 177 | 51,98% | +0,53% |
| DOGE | SETTIMANALE | Classic technical | 101 | 37,62% | -4,53% |
| DOGE | SETTIMANALE | Famiglia statistica | 179 | 54,75% | +2,68% |
| DOGE | SETTIMANALE | Microstruttura exchange | 27 | 44,44% | -0,39% |
| DOGE | SETTIMANALE | Tecnico | 161 | 57,76% | +0,83% |
| DOGE | SWING | Classic technical | 62 | 48,39% | -5,54% |
| DOGE | SWING | Famiglia statistica | 99 | 76,77% | +8,32% |
| DOGE | SWING | Microstruttura exchange | 15 | 53,33% | +0,66% |
| DOGE | SWING | Tecnico | 87 | 57,47% | -1,29% |
| DOGE | MEDIO | Classic technical | 54 | 20,37% | -15,40% |
| DOGE | MEDIO | Famiglia statistica | 73 | 58,90% | +2,38% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 68 | 20,59% | -14,67% |
| SOL | BREVE | Classic technical | 126 | 50,79% | +0,69% |
| SOL | BREVE | Famiglia statistica | 183 | 48,09% | +0,38% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 180 | 45,56% | +0,10% |
| SOL | SETTIMANALE | Classic technical | 123 | 52,03% | +1,43% |
| SOL | SETTIMANALE | Famiglia statistica | 167 | 54,49% | +2,41% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 172 | 43,60% | -1,27% |
| SOL | SWING | Classic technical | 63 | 47,62% | -2,30% |
| SOL | SWING | Famiglia statistica | 91 | 74,73% | +11,10% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 95 | 38,95% | -7,39% |
| SOL | MEDIO | Classic technical | 41 | 4,88% | -30,98% |
| SOL | MEDIO | Famiglia statistica | 62 | 72,58% | +14,99% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 71 | 16,90% | -21,65% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 5 | in attesa di controlli maturati |
| SOL | MEDIO | 1 | in attesa di controlli maturati |
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

Il campione comincia a essere utile. Le proposte restano prudenti e vanno verificate tra orizzonti diversi.
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
| BTC     |         68 |              38 |          30 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         68 |              38 |          30 | OSSERVAZIONE 30+ | 2,63%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         68 |              38 |          30 | OSSERVAZIONE 30+ | 5,26%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | MEDIO          | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| SOL     | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-09-16 05:32 UTC


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
| BTC | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402. | Sotto 62.488 il quadro tecnico peggiora. |
| SOL | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 107,12; milestone analogiche 119,04 / 132,33, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 87,63 / 74,20 / 62,19. |
| DOGE | -5 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.09421 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |
| SOL | +3 | 0 | +3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +2 |
| DOGE | -2 | 0 | -2 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -5 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 90,00%, return centrale 30g +25,55%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 65. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **0** — Score tecnico 0/12, verdetto neutrale / misto, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -7/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 65,00%, return centrale 30g +24,41%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 65. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **0** — Score tecnico 0/12, verdetto neutrale / misto, trend misto, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -4/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +70,74%, aderenza live +72,86%, errore live +13,57%, gap corrente +10,19%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 62, ma percorso ancorato non aderente: gap +10,19%, errore live +13,57%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 3, bias SQUEEZE SETUP MODERATO, EMA200 111,08 $, upside EMA200 +14,46%, gap EMA50/EMA200 -5,96%, hit EMA200 12w +56,67%, trend MIGLIORAMENTO. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 107,12; milestone analogiche 119,04 / 132,33, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 87,63 / 74,20 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-5**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 30,00%, return centrale 30g -10,25%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 65. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -5/12, verdetto debole, trend misto, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -9/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +2.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Leva alta, direzione mista, forza 3/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.09421 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-09-16 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 75.786 $ | prezzo corrente |
| Power Law centrale | 125.372 $ | deviazione -39,55% |
| Banda p10-p90 | 77.837 $ / 315.797 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 7,76% | posizione storica nel corridoio |
| Esponente β | 5,7992 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3169 cambiando finestra |
| Ultimo halving | 2024-04-19 | 880 giorni fa |
| Fase ciclo | 60,23% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-16 (4382 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0221) × giorni^5.7992
- Prezzo centrale oggi: **125.372 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 7,76%
- Scarto dal centro: **-39,55%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7992 | 91,93% |
| 2015 | 5,8808 | 91,48% |
| 2016 | 5,5642 | 87,74% |
| 2017 | 4,8372 | 82,94% |
| 2018 | 4,5640 | 78,46% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 81 | 28,40% | 50,97% | 20,89% |
| 180g | 81 | 41,98% | 59,41% | 47,18% |
| 365g | 81 | 58,02% | 72,28% | 81,57% |
| 730g | 81 | 58,02% | 72,72% | 108,81% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-01-31 | +26,77% | +6,72% | +32,31% | +69,58% |
| 2016-07-09 → 2020-05-11 | 2018-10-31 | -36,41% | -45,42% | -16,94% | +45,62% |
| 2020-05-11 → 2024-04-19 | 2022-09-25 | +6,88% | -10,39% | +46,22% | +39,87% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | 7.833053354145436 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -8 | -1 | -4.426712251573772 | 0 |

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

Generato: 2026-09-16 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00127890 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +7,83% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000106 | -8 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -4,43% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g -2,89%; 30g +7,83%; 90g +14,60%; 180g +0,54%
- **Daily:** RSI 49.35; MA50 0.00123460; MA200 0.00118462
- **Weekly:** MA30 0.00118966; RSI 53.86
- **Livelli:** supporto 0.00127500; resistenza 0.00129400; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-8)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -7,86%; 30g -4,43%; 90g -20,63%; 180g -21,00%
- **Daily:** RSI 41.08; MA50 0.00000110; MA200 0.00000125
- **Weekly:** MA30 0.00000125; RSI 37.06
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 208 | 52,40% | +1,95% | -1,06% |
| SOL | 30g | 205 | 47,32% | +4,53% | +0,53% |
| SOL | 90g | 200 | 52,50% | +9,74% | +3,06% |
| DOGE | 7g | 295 | 55,59% | +1,83% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 35 | 54,29% | +0,10% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 35 | 54,29% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 35 | 42,86% | +0,51% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 30 | 33,33% | -0,13% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 16 | 6,25% | -11,34% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 52 | 69,23% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 50 | 60,00% | +0,09% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 46 | 54,35% | -0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 43 | 62,79% | +0,20% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 34 | 67,65% | +0,42% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **16 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 97,07 $ | 2026-09-16T05:30:23Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 97,04 $ | 2026-09-16T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,03000 $ | -0,03% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=97.06999969482422
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-16T05:30:23Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=97.04000091552734
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-16T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-16T05:32:11Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=108.207525
ANCHOR_AGE_HOURS=0.030057645833333334
CURRENT_VS_ANCHOR_GAP_USD=-0.029998779296875
CURRENT_VS_ANCHOR_GAP_PCT=-0.030904274638088314
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +70,74%
- **Somiglianza strutturale:** +70,74%
- **Aderenza prezzo live:** +72,86%
- **Errore medio live:** +13,57%
- **Gap prezzo corrente:** +10,19%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 102 dal bottom usato.
- **Giorno BTC equivalente:** 2023-03-03
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima retest / debolezza, poi recupero.** Zona bassa **87,63 $** intorno al **23 settembre 2026**; zona alta **119,04 $** intorno al **30 settembre 2026**; fine step circa **119,04 $** entro il **30 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=13.569072630130746
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=10.191836947207754
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 16 settembre 2026 | 76 | +72,86% | +13,57% | +10,19% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 16 settembre 2026 | 103 | +76,82% | +11,59% | +10,19% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +72,86% | Errore medio live +13,57%. |
| Gap corrente | +10,19% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 119,04 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 132,33 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 87,63 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 541,52 $ |
| Massimo percorso base | 541,52 $ (21 aprile 2029) |

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
| Prima conferma | 119,04 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 132,33 $ | Scenario più credibile. |
| Invalidazione soft | 87,63 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 23 settembre 2026 | -9,73% | 87,63 $ | 87,63 $ | 97,39 $ |
| 14 giorni | 30 settembre 2026 | +22,63% | 119,04 $ | 87,63 $ | 119,04 $ |
| 30 giorni | 16 ottobre 2026 | +26,10% | 122,41 $ | 87,63 $ | 123,62 $ |
| 60 giorni | 15 novembre 2026 | +28,25% | 124,49 $ | 87,63 $ | 132,33 $ |
| 90 giorni | 15 dicembre 2026 | +19,93% | 116,42 $ | 87,63 $ | 132,33 $ |
| 120 giorni | 14 gennaio 2027 | +36,79% | 132,78 $ | 87,63 $ | 133,24 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 16 settembre 2026 -> 30 settembre 2026 | +22,63% | 87,63 $ (23 settembre 2026) | 119,04 $ (30 settembre 2026) | 119,04 $ | Prima retest / debolezza, poi recupero. |
| Step 2 - primo mese | 1 ottobre 2026 -> 16 ottobre 2026 | +26,10% | 117,05 $ (1 ottobre 2026) | 123,62 $ (14 ottobre 2026) | 122,41 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 17 ottobre 2026 -> 15 novembre 2026 | +28,25% | 118,40 $ (4 novembre 2026) | 132,33 $ (28 ottobre 2026) | 124,49 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 16 novembre 2026 -> 15 dicembre 2026 | +19,93% | 114,31 $ (7 dicembre 2026) | 128,20 $ (18 novembre 2026) | 116,42 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 97,07 $ |  |
| Weekly RSI | 53,67 / linea grezza 52,00 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 45,89 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 541,52 $ | Avanzamento +17,93% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 45,9, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | -2 |
| Bias | NEGATIVA |
| Azione coerente | PRUDENZA / POSSIBILE PRESSIONE |
| Prezzo SOL | 97,07 $ |
| TVL Solana | 5,73 mld $ |
| TVL 7g | -3,72% |
| DEX volume 24h | 2,50 mld $ |
| Fees 24h | 14,22 mln $ |
| Stablecoin su Solana | 15,90 mld $ |
| Stake ratio | 69,27% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**PRUDENZA / POSSIBILE PRESSIONE**

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
| Lifecycle squeeze score | 3 |
| Bias | SQUEEZE SETUP MODERATO |
| Azione coerente | CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO |
| Peso suggerito Global | 0 |
| Trend squeeze | MIGLIORAMENTO |
| Trend squeeze score | 1 |
| Confronto precedente | 2026-09-14 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 97,07 $ |
| EMA200 weekly target | 111,08 $ |
| Upside verso EMA200 | +14,46% |
| Distanza prezzo da EMA200 | -12,64% |
| Gap EMA50/EMA200 | -5,96% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 53,65 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +56,67% |
| Max gain mediano 12w | +27,67% |
| Drawdown mediano 12w | -30,93% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **MIGLIORAMENTO**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-16 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-16 05:30:23 UTC**

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
- SOL: cambiamento importante in peggioramento rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +90.00% | +2.50 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +65.00% | -5.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | RIBASSISTA | +30.00% | -2.50 punti |

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
| BTC | 72.021 $ | 83.393 $ | +71,43% | +15,79% | buona zona storica di rimbalzo | 83.393 $ | 72.021 $ | +2,78% | -13,64% | spike storicamente più resistente |
| SOL | 92,22 $ | 106,78 $ | +36,84% | +15,79% | rimbalzo debole | 106,78 $ | 92,22 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07617 $ | 0,08820 $ | +21,88% | +15,79% | rimbalzo poco frequente | 0,08820 $ | 0,07617 $ | +63,64% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +71,43% (10/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **BTC: su 40 casi simili, 36 prima sono saliti a +10,00%. Tra quei 36, 1 poi sono scaricati a -5,00%. Percentuale: +2,78% (1/36). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +36,84% (7/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 6 poi sono scaricati a -5,00%. Percentuale: +20,00% (6/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +21,88% (7/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 14 poi sono scaricati a -5,00%. Percentuale: +63,64% (14/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-16 05:31:51 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-16 | 2026-09-16T05:30:23Z | 2026-09-16 05:30:23 |
| SOL | 2026-09-16 | 2026-09-16T05:30:23Z | 2026-09-16 05:30:23 |
| DOGE | 2026-09-16 | 2026-09-16T05:30:23Z | 2026-09-16 05:30:23 |

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
| BTC | 2026-09-16 | 75.812 $ | SALITA | 90,00% | 74.916,30 $ | 88.666,20 $ | 95.179,26 $ | 119.021,29 $ | 127.850,07 $ |
| SOL | 2026-09-16 | 97,07 $ | SALITA | 65,00% | 69,31 $ | 88,49 $ | 120,76 $ | 159,35 $ | 191,89 $ |
| DOGE | 2026-09-16 | 0.08018 $ | DISCESA | 30,00% | 0.05790 $ | 0.06306 $ | 0.07197 $ | 0.08251 $ | 0.09655 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 95.179,26 $ | n/a | 127.850,07 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 120,76 $ | n/a | 191,89 $ | n/a |
| DOGE | AVAILABLE | SAME_ASSET_REGIME | 0 | 25 | 0 | 25 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07197 $ | 0.06636 $ | 0.09655 $ | 0.09185 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-17**; verificato fino al **2026-09-16**; stato **COMPLETO 30/30g**.
- Reale **75.784,54 $**; p50 previsto **67.356,60 $**; scarto **12,51%**.
- Errore medio assoluto **14,69%**; massimo **20,70%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-17**; verificato fino al **2026-09-16**; stato **COMPLETO 30/30g**.
- Reale **97,03 $**; p50 previsto **78,92 $**; scarto **22,94%**.
- Errore medio assoluto **23,73%**; massimo **36,38%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-17**; verificato fino al **2026-09-16**; stato **COMPLETO 30/30g**.
- Reale **0.08011 $**; p50 previsto **0.08013 $**; scarto **-0,03%**.
- Errore medio assoluto **13,93%**; massimo **32,58%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 65 | 93,85% | 67,69% | 2,03% | 0,49% |
| BTC | 3g | 61 | 91,80% | 73,77% | 3,20% | 0,73% |
| BTC | 7g | 53 | 90,57% | 71,70% | 5,04% | 2,15% |
| BTC | 14g | 39 | 97,44% | 66,67% | 6,32% | 3,86% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 65 | 81,54% | 61,54% | 2,72% | 0,91% |
| SOL | 3g | 61 | 90,16% | 73,77% | 3,95% | 1,55% |
| SOL | 7g | 53 | 88,68% | 71,70% | 5,47% | 3,41% |
| SOL | 14g | 39 | 82,05% | 66,67% | 8,28% | 7,11% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 65 | 87,69% | 61,54% | 3,14% | 0,68% |
| DOGE | 3g | 61 | 90,16% | 68,85% | 4,68% | 1,63% |
| DOGE | 7g | 53 | 77,36% | 75,47% | 8,41% | 5,55% |
| DOGE | 14g | 39 | 82,05% | 53,85% | 10,84% | 9,21% |
| DOGE | 30g | 23 | 91,30% | 34,78% | 17,34% | 17,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **192**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-16 | BTC | 75.812 $ | SALITA | 90,00% | 95.179 $ | 73.298 $ | 106.851 $ | 2026-10-16 |
| 2026-09-16 | DOGE | 0,08000 $ | DISCESA | 30,00% | 0,07000 $ | 0,06000 $ | 0,09000 $ | 2026-10-16 |
| 2026-09-16 | SOL | 97,07 $ | SALITA | 65,00% | 120,76 $ | 92,90 $ | 129,99 $ | 2026-10-16 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-09-16 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +90,00%       | Casi positivi 90.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 90.00% >= 80%**
- Casi usati nei grafici: **36**
- Return mediano 7g: **+5,23%**
- Return mediano 14g: **+15,85%**
- Return mediano 30g: **+32,78%**
- Drawdown mediano: **-2,96%**
- Max gain mediano: **+43,28%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+0,62%**
- Spike p75 prima del minimo: **+0,00%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-3,10%**
- Casi con almeno +5% prima del minimo: **+2,78%**
- Casi con almeno +10% prima del minimo: **+0,00%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+83,33%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +11,74% | +22,44% | +32,78% | +57,53% | +73,92% |

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
| LRC-USD         | 2020-06-24 | +84,90%      | +7,85%                   |              2 | -6,93%       |               5 | -13,71%          | +47,51%      | ECCEZIONE POSITIVA            |
| INJ-USD         | 2023-11-18 | +89,72%      | +4,94%                   |              1 | -10,45%      |               3 | -14,67%          | +131,17%     | RIALZO MODESTO PRIMA DEL DUMP |
| DASH-USD        | 2020-12-16 | +85,90%      | +4,49%                   |              4 | -17,00%      |              17 | -20,57%          | +18,83%      | RIALZO MODESTO PRIMA DEL DUMP |
| ZIL-USD         | 2023-11-23 | +86,33%      | +2,25%                   |              2 | -1,34%       |               4 | -3,51%           | +21,53%      | DISCESA QUASI IMMEDIATA       |
| ZEC-USD         | 2019-04-26 | +86,72%      | +2,04%                   |              7 | -7,96%       |              13 | -9,80%           | +23,44%      | ECCEZIONE POSITIVA            |
| DOGE-USD        | 2019-04-26 | +85,46%      | +0,48%                   |              2 | -2,10%       |               3 | -2,57%           | +22,75%      | DISCESA QUASI IMMEDIATA       |
| BTC-USD         | 2019-04-27 | +87,04%      | +0,32%                   |              1 | -0,40%       |               2 | -0,71%           | +67,15%      | DISCESA QUASI IMMEDIATA       |
| BCH-USD         | 2019-04-26 | +86,64%      | +0,02%                   |              1 | -10,33%      |               3 | -10,35%          | +64,03%      | DISCESA QUASI IMMEDIATA       |
| QTUM-USD        | 2023-11-21 | +90,03%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,24%      | DISCESA QUASI IMMEDIATA       |
| XLM-USD         | 2020-12-16 | +89,91%      | +0,00%                   |              0 | -33,92%      |               7 | -33,92%          | +48,87%      | ECCEZIONE POSITIVA            |
| THETA-USD       | 2023-11-30 | +88,74%      | +0,00%                   |              0 | -1,35%       |               1 | -1,35%           | +24,03%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-26 | +88,74%      | +0,00%                   |              0 | -2,05%       |               1 | -2,05%           | +0,90%       | DISCESA QUASI IMMEDIATA       |
| 1INCH-USD       | 2023-11-28 | +88,32%      | +0,00%                   |              0 | -0,60%       |               2 | -0,60%           | +24,79%      | DISCESA QUASI IMMEDIATA       |
| MANA-USD        | 2023-11-26 | +87,16%      | +0,00%                   |              0 | -4,09%       |               4 | -4,09%           | +24,12%      | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-30 | +87,15%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +66,00%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-03-02 | +87,13%      | +0,00%                   |              0 | -2,80%       |               1 | -2,80%           | +51,23%      | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-26 | +87,12%      | +0,00%                   |              0 | -3,46%       |               1 | -3,46%           | +24,65%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-26 | +87,10%      | +0,00%                   |              0 | -3,88%       |               4 | -3,88%           | +57,64%      | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-26 | +86,96%      | +0,00%                   |              0 | -2,88%       |               1 | -2,88%           | +8,94%       | DISCESA QUASI IMMEDIATA       |
| AVAX-USD        | 2021-09-13 | +86,57%      | +0,00%                   |              0 | -2,88%       |               1 | -2,88%           | +3,85%       | DISCESA QUASI IMMEDIATA       |

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
- Casi positivi / salita storica: **90,00%**
- Casi negativi / discesa storica: **10,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **75.811,59 $**
- Return normale fra 30 giorni: **95.179,26 $** (25,55%)
- Drawdown normale durante il mese: **73.298,49 $** (-3,31%)
- Drawdown brutto da rispettare: **69.767,11 $** (-7,97%)
- Max gain normale durante il mese: **106.851,36 $** (40,94%)
- Max gain buono / take profit ottimistico: **127.058,20 $** (67,60%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **65,00%**
- Casi negativi / discesa storica: **35,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **97,07 $**
- Return normale fra 30 giorni: **120,76 $** (24,41%)
- Drawdown normale durante il mese: **92,90 $** (-4,30%)
- Drawdown brutto da rispettare: **76,16 $** (-21,55%)
- Max gain normale durante il mese: **129,99 $** (33,91%)
- Max gain buono / take profit ottimistico: **173,25 $** (78,48%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **30,00%**
- Casi negativi / discesa storica: **70,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,07 $** (-10,25%)
- Drawdown normale durante il mese: **0,06 $** (-21,22%)
- Drawdown brutto da rispettare: **0,06 $** (-26,50%)
- Max gain normale durante il mese: **0,09 $** (11,67%)
- Max gain buono / take profit ottimistico: **0,10 $** (21,16%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 75.811,59 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **90,00%**
- Probabilità storica di discesa: **10,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **74.916,30 $** (-1,18%)
- Se va male: **88.666,20 $** (16,96%)
- Scenario normale: **95.179,26 $** (25,55%)
- Se va bene: **119.021,29 $** (57,00%)
- Se va molto bene: **127.850,07 $** (68,64%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **73.298,49 $** (-3,31%)
- Discesa brutta: **69.767,11 $** (-7,97%)
- Discesa molto brutta: **50.901,49 $** (-32,86%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **106.851,36 $** (40,94%)
- Rialzo buono: **127.058,20 $** (67,60%)
- Rialzo molto forte: **141.479,66 $** (86,62%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **73.298,49 $** e uno spike normale intorno a **106.851,36 $**.

La chiusura a 30 giorni era più spesso positiva: salita 90,00%, discesa 10,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 97,07 $

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

- Se va molto male: **69,31 $** (-28,60%)
- Se va male: **88,49 $** (-8,84%)
- Scenario normale: **120,76 $** (24,41%)
- Se va bene: **159,35 $** (64,16%)
- Se va molto bene: **191,89 $** (97,68%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **92,90 $** (-4,30%)
- Discesa brutta: **76,16 $** (-21,55%)
- Discesa molto brutta: **64,51 $** (-33,54%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **129,99 $** (33,91%)
- Rialzo buono: **173,25 $** (78,48%)
- Rialzo molto forte: **218,46 $** (125,06%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **92,90 $** e uno spike normale intorno a **129,99 $**.

La chiusura a 30 giorni era più spesso positiva: salita 65,00%, discesa 35,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,08 $

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

- Se va molto male: **0,06 $** (-27,78%)
- Se va male: **0,06 $** (-21,35%)
- Scenario normale: **0,07 $** (-10,25%)
- Se va bene: **0,08 $** (2,91%)
- Se va molto bene: **0,10 $** (20,41%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-21,22%)
- Discesa brutta: **0,06 $** (-26,50%)
- Discesa molto brutta: **0,05 $** (-33,34%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (11,67%)
- Rialzo buono: **0,10 $** (21,16%)
- Rialzo molto forte: **0,12 $** (44,99%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,09 $**.

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

- Grezzo: **25,55%** → **95.179,26 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **27,56%** → **96.701,49 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-3,31%** → **73.298,49 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **1,41%** → **76.879,31 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **40,94%** → **106.851,36 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **38,12%** → **104.709,74 $**
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

- Grezzo: **24,41%** → **120,76 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **33,21%** → **129,31 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-4,30%** → **92,90 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-1,31%** → **95,80 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **33,91%** → **129,99 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **37,93%** → **133,89 $**
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
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-10,25%** → **0,07 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **4,94%** → **0,08 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-21,22%** → **0,06 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-5,88%** → **0,08 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **11,67%** → **0,09 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **14,20%** → **0,09 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 75.811,59 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **90,00%**
- Casi negativi dopo 30 giorni: **10,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,67%**
- Rendimento medio dopo 30 giorni: **33,07%**
- Rendimento centrale dopo 30 giorni: **25,55%**
- Discesa media durante i 30 giorni: **-8,83%**
- Massimo rialzo medio durante i 30 giorni: **47,91%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **100.883,39 $**
- Scenario centrale a 30 giorni: **95.179,26 $**
- Zona di rischio media: **69.114,82 $**
- Zona di rialzo media: **112.134,83 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -1,18% → **74.916,30 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 16,96% → **88.666,20 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 25,55% → **95.179,26 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 57,00% → **119.021,29 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 68,64% → **127.850,07 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,86% → **50.901,49 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -7,97% → **69.767,11 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,31% → **73.298,49 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,31% → **74.820,03 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **75.811,59 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 15,71% → **87.719,71 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 24,47% → **94.361,33 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 40,94% → **106.851,36 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 67,60% → **127.058,20 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 86,62% → **141.479,66 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| QTUM-USD        | 2023-08-14   | 2023-11-21 |        90.03 |        14.24 |           0    |          19.61 |
| XLM-USD         | 2020-09-08   | 2020-12-16 |        89.91 |        48.87 |         -33.92 |          78.05 |
| INJ-USD         | 2023-08-11   | 2023-11-18 |        89.72 |       131.17 |         -10.45 |         131.17 |
| ETC-USD         | 2022-01-06   | 2022-04-15 |        89.71 |       -40.79 |         -49.28 |           2.33 |
| THETA-USD       | 2023-08-23   | 2023-11-30 |        88.74 |        24.03 |          -1.35 |          40.28 |
| XRP-USD         | 2023-08-19   | 2023-11-26 |        88.74 |         0.9  |          -2.05 |           9.13 |
| 1INCH-USD       | 2023-08-21   | 2023-11-28 |        88.32 |        24.79 |          -0.6  |          33.23 |
| XRP-USD         | 2020-09-08   | 2020-12-16 |        87.2  |       -50.69 |         -62.75 |           2.75 |
| MANA-USD        | 2023-08-19   | 2023-11-26 |        87.16 |        24.12 |          -4.09 |          24.54 |
| ALGO-USD        | 2023-08-23   | 2023-11-30 |        87.15 |        66    |           0    |          79.78 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 97,07 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **65,00%**
- Casi negativi dopo 30 giorni: **35,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,10%**
- Rendimento medio dopo 30 giorni: **35,56%**
- Rendimento centrale dopo 30 giorni: **24,41%**
- Discesa media durante i 30 giorni: **-13,00%**
- Massimo rialzo medio durante i 30 giorni: **58,03%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **131,59 $**
- Scenario centrale a 30 giorni: **120,76 $**
- Zona di rischio media: **84,45 $**
- Zona di rialzo media: **153,40 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -28,60% → **69,31 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -8,84% → **88,49 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 24,41% → **120,76 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 64,16% → **159,35 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 97,68% → **191,89 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,54% → **64,51 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -21,55% → **76,16 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,30% → **92,90 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,41% → **96,67 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **97,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,87% → **98,88 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,02% → **105,83 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 33,91% → **129,99 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 78,48% → **173,25 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 125,06% → **218,46 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| VET-USD         | 2020-03-19   | 2020-06-26 |        87.48 |        96.75 |          -3.23 |         124.5  |
| VET-USD         | 2023-08-21   | 2023-11-28 |        87.35 |        64.56 |          -1.1  |          76.63 |
| NEO-USD         | 2023-08-19   | 2023-11-26 |        87.27 |        26.3  |          -1.52 |          33.63 |
| DOGE-USD        | 2018-06-21   | 2018-09-28 |        87.25 |       -30.32 |         -36.25 |           1.9  |
| ETH-USD         | 2020-05-11   | 2020-08-18 |        87.09 |        -8.18 |         -20.87 |          12.6  |
| ADA-USD         | 2024-09-02   | 2024-12-10 |        87.09 |       -11.19 |         -17.29 |          10.28 |
| BNB-USD         | 2023-10-08   | 2024-01-15 |        86.93 |         5.25 |          -8.08 |           5.25 |
| 1INCH-USD       | 2023-08-21   | 2023-11-28 |        86.79 |        24.79 |          -0.6  |          33.23 |
| ALGO-USD        | 2023-08-23   | 2023-11-30 |        86.69 |        66    |           0    |          79.78 |
| WAVES-USD       | 2023-08-19   | 2023-11-26 |        86.44 |        31.85 |          -3.03 |          34.19 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,08 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **30,00%**
- Casi negativi dopo 30 giorni: **70,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,27%**
- Rendimento medio dopo 30 giorni: **-4,58%**
- Rendimento centrale dopo 30 giorni: **-10,25%**
- Discesa media durante i 30 giorni: **-19,69%**
- Massimo rialzo medio durante i 30 giorni: **19,15%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,07 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -27,78% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -21,35% → **0,06 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -10,25% → **0,07 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 2,91% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 20,41% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,34% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -26,50% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -21,22% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -9,87% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -4,31% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,58% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,57% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,67% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 21,16% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 44,99% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ALGO-USD        | 2026-01-19   | 2026-04-28 |        85.43 |         3.05 |          -4.94 |          19.19 |
| MANA-USD        | 2022-11-02   | 2023-02-09 |        85.39 |       -23.04 |         -23.69 |           9.52 |
| ETH-USD         | 2025-02-24   | 2025-06-03 |        85.12 |        -0.09 |         -14.08 |           8.49 |
| NEO-USD         | 2019-08-15   | 2019-11-22 |        83.91 |        -8.05 |         -18.57 |           4.55 |
| SAND-USD        | 2021-04-25   | 2021-08-02 |        83.86 |        63.91 |          -4.99 |          63.91 |
| XTZ-USD         | 2019-08-25   | 2019-12-02 |        81.93 |        10.63 |           0    |          42.88 |
| QTUM-USD        | 2021-05-26   | 2021-09-02 |        81.92 |         2.9  |         -34.7  |          21.52 |
| XRP-USD         | 2021-05-31   | 2021-09-07 |        81.34 |        -5.07 |         -22.11 |           0    |
| ENJ-USD         | 2022-11-02   | 2023-02-09 |        81.29 |       -20.27 |         -20.27 |          22.87 |
| SOL-USD         | 2022-10-31   | 2023-02-07 |        81.26 |       -27.46 |         -27.46 |           9.72 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-16 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-16 | RECOVERY | 75.812 $ | True | 20.53% | -3.99% | RECOVERY | 20.53% | -3.99% |
| DOGE-USD | 2026-09-16 | BEAR | 0.08018 $ | False | -3.89% | -11.63% | RECOVERY | 20.53% | -3.99% |
| SOL-USD | 2026-09-16 | RECOVERY | 97,07 $ | True | 39.42% | -7.83% | RECOVERY | 20.53% | -3.99% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 90.00% | 25.55% | 57.00% | 68.64% | -3.31% | -32.86% | 40.94% | 67.60% | 86.62% | 77.50% | 21.60% | 74.11% | 138.30% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 47.51% | 47.51% | 47.51% | -6.93% | -6.93% | 68.95% | 68.95% | 68.95% | 100.00% | 137.57% | 137.57% | 137.57% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -10.25% | 2.91% | 20.41% | -21.22% | -33.34% | 11.67% | 21.16% | 44.99% | 55.00% | 1.14% | 15.74% | 32.40% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 25 | 24.00% | -17.24% | -0.09% | 14.56% | -20.27% | -35.59% | 10.63% | 19.20% | 29.02% | 36.00% | -8.74% | 1.32% | 26.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 65.00% | 24.41% | 64.16% | 97.68% | -4.30% | -33.54% | 33.91% | 78.48% | 125.06% | 67.50% | 19.01% | 84.69% | 173.55% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -1.22% | 3.73% | 6.70% | -16.37% | -43.21% | 22.31% | 27.04% | 29.88% | 33.33% | -13.67% | 23.29% | 45.47% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 28 | 92.86% | 25.55% | -3.10% | 58.45% | 71.43% | 18.28% | 80.33% |
| BTC-USD | HISTORICAL_BTC_BULL | 12 | 83.33% | 34.14% | -9.24% | 88.63% | 91.67% | 84.48% | 158.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 27.59% | -11.61% | -20.94% | 21.04% | 44.83% | -1.60% | 27.08% |
| DOGE-USD | HISTORICAL_BTC_BULL | 7 | 42.86% | -1.97% | -18.57% | 33.69% | 100.00% | 15.70% | 53.45% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 25.00% | -5.51% | -24.36% | 7.21% | 50.00% | 7.44% | 56.54% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 65.38% | 18.80% | -3.73% | 59.54% | 65.38% | 12.56% | 78.99% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 81.82% | 60.36% | -0.41% | 118.08% | 90.91% | 166.43% | 282.86% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 0.00% | -21.84% | -23.58% | 7.08% | 0.00% | -23.20% | 7.08% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 93.55% | 24.65% | -3.03% | 55.41% | 74.19% | 20.17% | 80.87% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 66.67% | 23.83% | -14.53% | 95.33% | 83.33% | 37.13% | 149.59% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 48.87% | -33.92% | 78.05% | 100.00% | 170.45% | 192.55% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 81.54% | 0.00% | 131.38% | 100.00% | 137.49% | 137.49% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 47.51% | -6.93% | 68.95% | 100.00% | 137.57% | 144.47% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 25 | 24.00% | -17.24% | -20.27% | 19.20% | 36.00% | -8.74% | 33.12% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 11 | 36.36% | -3.20% | -24.51% | 23.00% | 90.91% | 12.27% | 55.09% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 2.94% | -16.70% | 39.04% | 100.00% | 12.27% | 39.04% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -18.34% | -19.39% | 3.18% | 0.00% | -21.46% | 3.18% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 62.96% | 24.03% | -4.11% | 62.60% | 62.96% | 8.73% | 78.20% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 53.56% | -2.45% | 122.22% | 100.00% | 69.18% | 195.23% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 58.15% | -10.43% | 135.43% | 75.00% | 185.93% | 260.23% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -1.22% | -16.37% | 27.04% | 33.33% | -13.67% | 77.79% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 25 | 0 | 25 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | ALGO-USD | 2026-01-19 | 85.43% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.05% | -4.94% | 19.19% | -23.29% | -25.87% | 19.19% |
| DOGE-USD | MANA-USD | 2022-11-02 | 85.39% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.04% | -23.69% | 9.52% | -9.67% | -23.69% | 9.52% |
| DOGE-USD | ETH-USD | 2025-02-24 | 85.12% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -0.09% | -14.08% | 8.49% | 30.83% | -14.08% | 49.43% |
| DOGE-USD | NEO-USD | 2019-08-15 | 83.91% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -8.05% | -18.57% | 4.55% | 15.70% | -18.57% | 22.70% |
| DOGE-USD | ENJ-USD | 2022-11-02 | 81.29% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -20.27% | -20.27% | 22.87% | -1.58% | -20.27% | 22.87% |
| DOGE-USD | SOL-USD | 2022-10-31 | 81.26% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -27.46% | -27.46% | 9.72% | -16.03% | -27.46% | 9.72% |
| DOGE-USD | NEAR-USD | 2022-11-02 | 81.14% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -20.02% | -20.94% | 19.20% | -8.74% | -20.94% | 19.20% |
| DOGE-USD | YFI-USD | 2022-05-15 | 81.03% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.14% | -10.14% | 17.05% | -14.71% | -16.21% | 17.05% |
| DOGE-USD | AAVE-USD | 2022-10-31 | 80.96% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.69% | -22.69% | 3.44% | -14.07% | -24.14% | 3.44% |
| DOGE-USD | MKR-USD | 2018-07-22 | 80.82% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -39.79% | -49.29% | 10.63% | -23.59% | -49.54% | 10.63% |

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

Generato: 2026-09-16 05:32 UTC


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
| BTC | 75.812 $ | -7 | RIBASSISTA / FRAGILE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | RANGE / FASE NON CHIARA | MEDIO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 97,07 $ | -4 | DEBOLE / NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | COMPRESSIONE / TRIANGOLO POSSIBILE | RANGE / FASE NON CHIARA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.08018 $ | -9 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | -2 | -3 | -2 | 0 | 0 | 0 | -7 |
| SOL | 0 | 0 | -3 | -1 | 0 | 0 | 0 | -4 |
| DOGE | -3 | 0 | -3 | -3 | 0 | 0 | 0 | -9 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 74.959 $ | 77.991 $ | 82.262 $ | 61.769 $ | 2,84% | 20,66% | 17,66% |
| SOL | 83,52 $ | 98,27 $ | 110,04 $ | 70,69 $ | 4,18% | 30,19% | 34,91% |
| DOGE | 0.07809 $ | 0.08494 $ | 0.09998 $ | 0.06797 $ | 5,36% | 15,30% | -6,63% |

## Lettura dettagliata

### BTC

- Prezzo: **75.812 $**
- Score classico: **-7 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,84%; distanza supporto 1,12%; distanza resistenza 2,90%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-3** — RSI neutrale 48.8; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF neutrale -0.05; discesa con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 48.80 |
| MACD histogram | -773.38979 |
| CMF20 | -0.049 |
| Volume ratio 20 | 1.38 |
| MA20 | 78.300 $ |
| MA50 | 71.657 $ |
| MA100 | 67.466 $ |
| MA200 | 70.239 $ |
| Pendenza MA50 20g | +8,46% |
| Pendenza MA200 60g | -4,15% |
| Bollinger width | 7,46% |
| Bollinger position | 0.06 |

### SOL

- Prezzo: **97,07 $**
- Score classico: **-4 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 4,18%; distanza supporto 16,19%; distanza resistenza 1,26%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-3** — RSI neutrale 48.8; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.01; volume ratio 1.14
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 48.84 |
| MACD histogram | -1.41222 |
| CMF20 | 0.012 |
| Volume ratio 20 | 1.14 |
| MA20 | 102,51 $ |
| MA50 | 88,90 $ |
| MA100 | 81,51 $ |
| MA200 | 83,25 $ |
| Pendenza MA50 20g | +13,30% |
| Pendenza MA200 60g | -8,08% |
| Bollinger width | 11,44% |
| Bollinger position | 0.01 |

### DOGE

- Prezzo: **0.08018 $**
- Score classico: **-9 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,36%; distanza supporto 2,58%; distanza resistenza 6,03%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-3** — RSI neutrale 44.1; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-3** — OBV sotto media; CMF negativo -0.10; discesa con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 44.06 |
| MACD histogram | -0.00115 |
| CMF20 | -0.097 |
| Volume ratio 20 | 1.22 |
| MA20 | 0.08530 $ |
| MA50 | 0.07883 $ |
| MA100 | 0.07796 $ |
| MA200 | 0.08792 $ |
| Pendenza MA50 20g | +7,02% |
| Pendenza MA200 60g | -11,86% |
| Bollinger width | 16,61% |
| Bollinger position | 0.11 |

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

Generato: 2026-09-16 05:32 UTC


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
| BTC | 75.812 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 58.946 $ | n/a | 21,83% | Fib 23,6% TESTATO (0) @ 76.477 $ | NEL RANGE | 74.959 $ |
| SOL | 97,07 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 84,86 $ | n/a | -0,39% | Fib 23,6% TENUTO (+1) @ 96,09 $ | NEL RANGE | 83,52 $ |
| DOGE | 0.08018 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 17,96% | Fib 50,0% TESTATO (0) @ 0.08109 $ | NEL RANGE | 0.07809 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **38 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **62.227 $**
- Target teorico: **58.946 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **21,83%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 76.477 $** — Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **63.471 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 38 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **74.959 $**
- Resistenza: **75.988 $**
- Breakout 60g: **82.262 $**
- Breakdown 60g: **61.769 $**
- RSI14: **48.85**
- ATR14: **2,83%**
- Volume ratio 20g: **1.38**
- Rendimento 30g: **+20,68%**
- Rendimento 90g: **+17,69%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 82.792 $ | n/a | n/a | 90.626 $ | n/a | 9,21% | 81.136 $ | Due minimi simili a 74.959 $ e 76.248 $. Neckline circa 82.792 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 14 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 21,83% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 38 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-08-27 -> 2026-09-06**
- Età formazione: **10 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **97,45 $**
- Target teorico: **84,86 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **-0,39%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (+1) @ 96,09 $** — Swing UP 2026-06-06 60,41 -> 2026-09-06 107,12; livello più vicino 23.6% a 96,09; stato TENUTO; confluenza: neckline ribassista.
- Invalidazione: **99,40 $**
- Relazione prezzo/neckline: **vicino alla neckline**
- Dettaglio: Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **83,52 $**
- Resistenza: **97,42 $**
- Breakout 60g: **110,04 $**
- Breakdown 60g: **70,69 $**
- RSI14: **48.88**
- ATR14: **4,17%**
- Volume ratio 20g: **1.14**
- Rendimento 30g: **+30,23%**
- Rendimento 90g: **+34,95%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 97,45 $ | n/a | n/a | 84,86 $ | n/a | -0,39% | 99,40 $ | Due massimi simili a 110,04 $ e 107,12 $. Neckline circa 97,45 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 10 giorni. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 28g | 85,65 $ | 252,75% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 252,75%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 28g | 84,05 $ | 344,54% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 344,54%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **36 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **17,96%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 50,0% TESTATO (0) @ 0.08109 $** — Swing UP 2026-08-01 0.06797 -> 2026-09-05 0.09421; livello più vicino 50.0% a 0.08109; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 36 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07809 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **44.16**
- ATR14: **5,36%**
- Volume ratio 20g: **1.22**
- Rendimento 30g: **+15,40%**
- Rendimento 90g: **-6,55%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.04174 $ | n/a | 17,96% | 0.06933 $ | Due massimi simili a 0.09169 $ e 0.09421 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 11 giorni. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 27g | 0.08952 $ | 9,20% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (27 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 9,20%; prezzo sopra neckline. |

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

Generato: 2026-09-16 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-16**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-03**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **97,07 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+70,74%**
- Aderenza live principale: **+72,86%**
- Errore medio live principale: **13,57%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **102**
- Osservazioni inclusive dal bottom: **103**
- Osservazioni da inizio programma/scanner: **76**
- Errore assoluto medio dal bottom: **11,59%**
- Errore assoluto medio da inizio programma: **13,57%**
- Gap firmato medio ultimi 7 giorni: **+9,74%**
- Errore assoluto medio ultimi 7 giorni: **9,74%**
- Gap ultimo giorno: **+10,19%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+10,19%**
- Gap firmato medio 7g: **+9,74%**
- Errore assoluto medio 7g: **9,74%**
- Variazione recente gap: **+1,35%**
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
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 102,40 $ | 92,81 $ | +10,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 101,79 $ | 92,66 $ | +9,85% | da inizio programma |
| 99 | 2026-09-13 | 2023-02-28 | 99,25 $ | 91,18 $ | +8,84% | da inizio programma |
| 100 | 2026-09-14 | 2023-03-01 | 102,50 $ | 93,15 $ | +10,03% | da inizio programma |
| 101 | 2026-09-15 | 2023-03-02 | 102,50 $ | 92,48 $ | +10,83% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 97,07 $ | 88,09 $ | +10,19% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-23 | 79,52 $ | 87,63 $ | 87,63 $ / 97,39 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-30 | 108,03 $ | 119,04 $ | 87,63 $ / 119,04 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-07 | 108,30 $ | 119,34 $ | 87,63 $ / 122,99 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-14 | 112,18 $ | 123,62 $ | 87,63 $ / 123,62 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-21 | 110,01 $ | 121,22 $ | 87,63 $ / 123,62 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-28 | 120,09 $ | 132,33 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-04 | 107,45 $ | 118,40 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-11 | 115,58 $ | 127,36 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-18 | 116,34 $ | 128,20 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-25 | 105,59 $ | 116,35 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-02 | 105,93 $ | 116,72 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-09 | 105,25 $ | 115,98 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-16 | 107,34 $ | 118,28 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-23 | 104,31 $ | 114,94 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-30 | 103,71 $ | 114,28 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-06 | 120,92 $ | 133,24 $ | 87,63 $ / 133,24 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-13 | 120,06 $ | 132,29 $ | 87,63 $ / 133,24 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-20 | 119,53 $ | 131,71 $ | 87,63 $ / 135,24 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 62 | 40,32% | 10,05% | 12,48% |
| 14g | 55 | 29,09% | 16,75% | 11,39% |
| 21g | 48 | 20,83% | 24,76% | 12,75% |
| 28g | 41 | 26,83% | 26,87% | 12,40% |
| 35g | 35 | 37,14% | 19,90% | 11,48% |
| 42g | 29 | 68,97% | 12,15% | 10,64% |
| 49g | 22 | 90,91% | 6,18% | 10,35% |
| 56g | 15 | 100,00% | 6,36% | 9,26% |
| 63g | 8 | 100,00% | 6,47% | 10,01% |
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

Ultima lettura salvata: **2026-09-16** — SOL 97,07 $, gap +10,19%, somiglianza +70,74%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-16 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 75.680 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0075% | -0,80% | 2,19 | +1,55% | 0 $ | 0 $ |
| SOL | 96,85 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | -0,0023% | +1,06% | 0,98 | +9,75% | 0 $ | 0 $ |
| DOGE | 0.08000 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0048% | -0,06% | 1,87 | +36,63% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0246% | 157,00 mln $ | 0,53 | +5,42% |
| BTC | Bitget | OK | +0,0092% | 2,54 mld $ | 0,20 | -0,56% |
| BTC | Kucoin | OK | +0,0092% | 805,55 mln $ | 1,93 | -0,74% |
| SOL | Kraken | OK | +0,0325% | 24,80 mln $ | 0,16 | -2,55% |
| SOL | Bitget | OK | -0,0032% | 421,95 mln $ | 0,18 | -28,60% |
| SOL | Kucoin | OK | -0,0046% | 143,94 mln $ | 0,80 | -5,01% |
| DOGE | Kraken | OK | +0,0172% | 4,30 mln $ | 0,10 | -13,82% |
| DOGE | Bitget | OK | +0,0085% | 104,96 mln $ | 0,22 | +65,40% |
| DOGE | Kucoin | OK | -0,0021% | 55,69 mln $ | 0,87 | -33,43% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +40,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: neckline ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 9, accuratezza +44,44%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **+2,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
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
| BTC | +90,00% | +25,55% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +90,00% | +25,55% |
| SOL | +65,00% | +24,41% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +65,00% | +24,41% |
| DOGE | +30,00% | -10,25% | 4 | +75,00% | RACCOLTA DATI | 0,00 | +30,00% | -10,25% |

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

Generato: 2026-09-16 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-16 | BTC | 75.680,30 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,19 | -0,80% | +1,55% |
| 2026-09-16 | DOGE | 0.08000 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,87 | -0,06% | +36,63% |
| 2026-09-16 | SOL | 96,85 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 0,98 | +1,06% | +9,75% |
| 2026-09-15 | BTC | 77.614,90 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,91 | -4,50% | -3,26% |
| 2026-09-15 | DOGE | 0.08316 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,69 | -0,98% | +40,84% |
| 2026-09-15 | SOL | 101,20 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,52 | -2,84% | +4,03% |
| 2026-09-14 | BTC | 77.589,72 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 6,91 | -1,62% | +2,07% |
| 2026-09-14 | DOGE | 0.08400 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,59 | -4,08% | +5,67% |
| 2026-09-14 | SOL | 101,13 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 3,34 | -6,34% | -1,87% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | +40,00% | +0,25% | -2,11% | +2,12% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | +40,00% | -1,30% | -3,40% | +2,47% | FEEDBACK RAPIDO |
| BTC | 14g | 3 | +33,33% | -0,17% | -3,31% | +4,48% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 2 | +100,00% | +22,28% | -5,94% | +27,20% | FEEDBACK RAPIDO |
| DOGE | 1g | 9 | +44,44% | +0,77% | -0,33% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | 9 | +33,33% | +1,22% | -3,22% | +5,78% | FEEDBACK RAPIDO |
| DOGE | 7g | 9 | +44,44% | -1,43% | -4,92% | +7,35% | FEEDBACK RAPIDO |
| DOGE | 14g | 8 | +37,50% | +0,57% | -5,38% | +14,44% | FEEDBACK RAPIDO |
| DOGE | 30g | 4 | +75,00% | +14,93% | -1,41% | +41,94% | FEEDBACK RAPIDO |

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

**DOGE** — DOGE: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto. Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 75.812 $ | +0.0053% | -5.23% | 2.02 | Misto | 1/5 |
| SOL | 97,07 $ | -0.0039% | -14.78% | 2.39 | Misto | 1/5 |
| DOGE | 0.08018 $ | +0.0068% | +5.31% | 5.19 | Leva alta, direzione mista | 3/5 |

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

Generato: 2026-09-16 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D    | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:---------------------------|:-----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Misto / nessuna divergenza | CONTESTO   | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Hidden bullish invalidata  | INVALIDATA | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| DOGE    | Hidden bullish invalidata  | INVALIDATA | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Misto / nessuna divergenza | CONTESTO   | 75.782 $ / 48,76  | n/a                                                                 | -2,09%              | -16,91           |      0 |
| BTC     | 1W   | Conferma rialzista         | CONTESTO   | 75.782 $ / 53,34  | n/a                                                                 | +16,87%             | 12,41            |      0 |
| SOL     | 1D   | Hidden bullish invalidata  | INVALIDATA | 97,05 $ / 48,85   | n/a                                                                 | -2,94%              | -14,50           |      0 |
| SOL     | 1W   | Conferma rialzista         | CONTESTO   | 97,05 $ / 53,66   | n/a                                                                 | +27,34%             | 12,95            |      0 |
| DOGE    | 1D   | Hidden bullish invalidata  | INVALIDATA | 0.08011 $ / 44,06 | n/a                                                                 | -1,88%              | -8,48            |      0 |
| DOGE    | 1W   | Hidden bearish             | CONFERMATA | 0.08011 $ / 43,77 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### DOGE

- **1D — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **9**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Bullish regolare |          60 |           1 | +100,00%      | +21,03%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -23,44%           | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          60 |           1 | +100,00%      | +22,85%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          30 |           1 | +100,00%      | +22,35%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           2 | +50,00%       | -8,18%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -16,95%           | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          60 |           1 | 0,00%         | -30,59%           | RACCOLTA DATI |      0 |

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

Generato: 2026-09-16 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend       | Momentum        | Struttura                                          |   Pattern score | Fibonacci   | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:------------|:----------------|:---------------------------------------------------|----------------:|:------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 75.812 $ | 0 | NEUTRALE / MISTO | Trend misto | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 82.262 |
| SOL | 97,07 $ | 0 | NEUTRALE / MISTO | Trend misto | Momentum debole | Compressione / triangolo | 0 | +1 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 107,12 |
| DOGE | 0.08018 $ | -5 | DEBOLE | Trend misto | Momentum debole | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.09421 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | ASSENTE | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 48.85 | -772.347 | 78.301 | 71.658 | 70.239 | 7,87% | -3,99% | 17,53% | 20,53% |
| SOL | 48.88 | -1.41031 | 102,51 | 88,90 | 83,25 | 12,41% | -7,83% | 27,82% | 39,42% |
| DOGE | 44.16 | -0.00115 | 0.08530 | 0.07883 | 0.08792 | 6,53% | -11,63% | 13,98% | -3,89% |

## Dettaglio asset

### BTC

- Prezzo: **75.812 $**
- Punteggio tecnico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 6.249e+04 -> 7.625e+04. Ultimi massimi: 8.135e+04 -> 8.226e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.488**
- Resistenza più vicina: **82.262**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.227 tra 2026-08-03 e 2026-08-14. Neckline stimata: 65.402. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577; progresso corrente: 327,86%. Relazione prezzo/neckline: sopra neckline.
  - neckline 65.402; target 68.577; breakout 2026-08-19 (28g); progresso 327,86%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 189,04%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (28g); progresso 189,04%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 58.076 dal 2026-06-25 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.744; progresso corrente: 100,76%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 75.744; breakout 2026-08-19 (28g); progresso 100,76%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 38 giorni.
  - neckline 62.227; target 58.946; distanza dalla neckline 21,83%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 38 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 31,28%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### SOL

- Prezzo: **97,07 $**
- Punteggio tecnico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 74.2 -> 97.45. Ultimi massimi: 110 -> 107.1.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-06-06 60,41 -> 2026-09-06 107,12; livello più vicino 23.6% a 96,09; stato TENUTO; confluenza: neckline ribassista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,20**
- Resistenza più vicina: **107,12**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 344,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (28g); progresso 344,54%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 228,39%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (28g); progresso 228,39%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 83,45%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (28g); progresso 83,45%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 97,45; target 84,86; distanza dalla neckline -0,39%; prezzo vicino alla neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 38 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 37,31%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 83,81 dal 2026-07-04 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 38 giorni.
  - neckline 70,69; target 57,58; distanza dalla neckline 37,31%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08018 $**
- Punteggio tecnico: **-5 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 0.06895 -> 0.08028. Ultimi massimi: 0.09998 -> 0.09421.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 44.2.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-08-01 0.06797 -> 2026-09-05 0.09421; livello più vicino 50.0% a 0.08109; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.09421**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 115,70%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (28g); progresso 115,70%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06895 dal 2026-07-08 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07866; progresso corrente: 131,38%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07866; breakout 2026-08-19 (28g); progresso 131,38%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (28 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 115,70%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (28g); progresso 115,70%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 36 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 17,96%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 36 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 17,96%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 36 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 17,96%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                       | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato   | Confluenza                      |   Score |
|:--------|:----------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:--------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-09-03 | 76.477 | 72.898 | 70.005 | 67.112 | 62.994 | 23.6% / 76.477 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-09-06 | 96,09 | 89,28 | 83,77 | 78,25 | 70,41 | 23.6% / 96,09 | TENUTO | neckline ribassista | +1 |
| DOGE | UP 2026-08-01 -> 2026-09-05 | 0.08802 | 0.08419 | 0.08109 | 0.07800 | 0.07359 | 50.0% / 0.08109 | TESTATO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 30/30 previsioni controllate su 74 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 74 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 74 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 74 | 30 | 30/30 [██████████] | 44 | ATTIVA | 2026-09-17 / tra 1 giorno |
| SOL | 74 | 30 | 30/30 [██████████] | 44 | ATTIVA | 2026-09-17 / tra 1 giorno |
| DOGE | 74 | 30 | 30/30 [██████████] | 44 | ATTIVA | 2026-09-17 / tra 1 giorno |

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

Generato: 2026-09-16 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 2 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 75.812 $          | 75.812 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08018 $         | 0.08018 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 75.812 $          | 75.812 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08018 $         | 0.08018 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 75.812 $          | 75.812 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08018 $         | 0.08018 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 75.812 $          | 75.812 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08018 $         | 0.08018 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 75.812 $          | 75.812 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08018 $         | 0.08018 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 75.812 $          | 75.680 $        | -0,1732%     |
| Exchange Microstructure | SOL     | price             | WARN    | 97,07 $           | 96,85 $         | -0,2246%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.08018 $         | 0.08000 $       | -0,2245%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 97,07 $           | 97,07 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 97,07 $           | 97,07 $         | +0,0000%     |

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


<!-- SOL_LONG_TERM_CONE_HISTORY_START -->
## SOL Long-Term Cone History

[SOL Long-Term Cone History](sol_long_term_history/README.md)
<!-- SOL_LONG_TERM_CONE_HISTORY_END -->

<!-- SOL_SPOT_ADAPTIVE_START -->
# SOL Spot Adaptive Range — paper trading separato

Generato: 2026-09-17T04:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €44.710,16 | €1.206,27 | 435.448210 | 99.9060 | +11.78% | €4.505,48 | €151,54 | 6.48% | 68 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 93.8496 · L1 96.6541 · media 100.1597 · U1 103.6653 · U2 106.4698.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
