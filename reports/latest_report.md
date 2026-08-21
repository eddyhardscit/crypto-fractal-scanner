<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-21 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +5 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +2 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+5**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+2**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+2**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+5**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910.
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
- Conferme: Adam and Eve Bottom attivo finché mantiene 83,81; nuova conferma tecnica sopra 98,27; milestone analogiche 96,13 / 111,09, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 84,46 / 74,20 / 62,19.

### DOGE

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.09169 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,42 $; upside verso EMA200 +24,26%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-21T05:32:52+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-21T05:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-21T05:05:28+00:00 | 2026-08-21T05:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-21T04:45:00+00:00 | 2026-08-21T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-21T04:00:00+00:00 | 2026-08-21T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-21T00:00:00+00:00 | 2026-08-21T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend Side Regime Guard V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | ENA | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Tp3 V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Runner25 V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BOME | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTW | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 6,56 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 5,07 | 6,00 | 0,93 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,99 | 6,00 | 1,01 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 4,94 | 6,00 | 1,06 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,29 | 6,00 | 1,71 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | BOME | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | BOME | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | BOME | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Quality7 V1 | BOME | 60m | LONG | 7,75 | 7,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Long No Rhv V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.715,38 | -2,85% | €-32,97 | €3.000,00 | -1,10% | 5 | 46 | 34,78% | 0,76 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 46 | 1818 | PRIME INDICAZIONI | 100 (mancano 54) |

- Trade del Principale 4H chiusi: **46**; win rate **34,78%**; profit factor **0,76**.
- Expectancy: **€-7,25** per trade; P&L netto: **€-333,55**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.715,38 | €979,58 | €2.938,74 | €144,97 | €50,80 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.103,69 | €3.892,32 | €7.784,65 | €167,38 | €133,86 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €10.842,27 | €3.800,68 | €7.601,36 | €163,44 | €130,71 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €10.802,41 | €3.506,79 | €10.520,36 | €162,98 | €54,80 |
| TEST | Combo Trend Side Regime Guard V1 | 8 | €10.744,90 | €2.237,24 | €4.474,49 | €107,49 | €158,90 |
| TEST | Scanner Top 5 Long 1H | 7 | €10.565,59 | €2.073,05 | €4.146,10 | €151,80 | €104,59 |
| TEST | Main Side Regime Guard V1 | 4 | €10.491,38 | €721,94 | €2.165,83 | €208,62 | €15,37 |
| TEST | 1H Fast No Pepe V1 | 9 | €10.400,20 | €2.598,70 | €7.796,10 | €106,62 | €102,50 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 7 | €10.179,84 | €2.219,42 | €4.438,83 | €103,95 | €125,56 |
| TEST | Combo Adaptive | 7 | €10.167,39 | €1.919,17 | €3.838,34 | €102,75 | €166,26 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 7 | €10.131,57 | €2.671,57 | €5.343,15 | €99,47 | €147,96 |
| TEST | Sol Donchian 4H | 1 | €10.130,32 | €727,07 | €1.454,13 | €0,00 | €65,29 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.126,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.107,65 | €665,34 | €1.330,67 | €0,00 | €59,75 |
| TEST | Ampia 4H | 6 | €10.102,33 | €1.636,79 | €3.273,57 | €153,31 | €43,90 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.046,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 9 | €10.035,93 | €877,84 | €2.633,53 | €198,82 | €-9,40 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 1 | €10.029,22 | €155,86 | €467,58 | €51,44 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.022,40 | €50,00 | €750,00 | €8,72 | €-1,65 |
| TEST | Sol Donchian 1H | 1 | €10.022,21 | €937,37 | €2.812,11 | €0,00 | €59,96 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.004,48 | €10,00 | €150,00 | €1,74 | €-0,33 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.983,99 | €1.329,18 | €3.987,53 | €100,07 | €80,28 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.974,31 | €715,87 | €1.431,74 | €0,00 | €64,29 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.951,64 | €333,06 | €999,18 | €49,31 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.949,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.947,73 | €171,19 | €855,93 | €9,95 | €-1,88 |
| TEST | Btc Ema 1H | 0 | €9.942,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.940,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.920,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €9.900,93 | €2.728,82 | €5.457,64 | €147,98 | €115,78 |
| TEST | Sol Ema 1H | 1 | €9.899,48 | €823,54 | €2.470,62 | €0,00 | €52,68 |
| TEST | Sol Bollinger 1H | 0 | €9.892,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.887,99 | €577,20 | €1.154,41 | €0,00 | €47,03 |
| TEST | Eth Adaptive 1H | 0 | €9.878,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 9 | €9.826,58 | €2.441,58 | €4.883,17 | €58,16 | €227,03 |
| TEST | Scanner Top5 Btc Runner25 V1 | 9 | €9.820,83 | €2.440,16 | €4.880,31 | €58,12 | €226,90 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.816,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 9 | €9.813,01 | €1.808,45 | €5.425,34 | €146,75 | €38,43 |
| TEST | Eth Ema 1H | 1 | €9.793,37 | €563,60 | €1.690,79 | €0,00 | €62,97 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 1 | €9.779,65 | €151,98 | €455,94 | €50,16 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €9.767,15 | €1.864,76 | €3.729,52 | €96,61 | €160,28 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.758,68 | €811,83 | €2.435,48 | €0,00 | €51,93 |
| TEST | Rapida 1H V3 Filtered | 9 | €9.749,93 | €1.796,76 | €5.390,27 | €145,80 | €38,19 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 5 | €9.742,29 | €1.771,28 | €3.542,56 | €97,21 | €65,13 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 1 | €9.718,69 | €770,02 | €2.310,06 | €48,65 | €-10,95 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.711,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.702,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 7 | €9.651,39 | €2.301,69 | €4.603,38 | €144,55 | €93,47 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 7 | €9.620,52 | €1.598,12 | €4.794,36 | €142,92 | €22,32 |
| TEST | Combo Adaptive Quality7 Regime V1 | 5 | €9.619,75 | €1.749,00 | €3.498,00 | €95,99 | €64,31 |
| TEST | 1H Fast V3 No Esports V1 | 9 | €9.599,92 | €1.772,63 | €5.317,88 | €143,56 | €37,41 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.595,22 | €199,19 | €398,38 | €47,81 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 6 | €9.591,75 | €2.910,43 | €5.820,86 | €99,24 | €51,90 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 7 | €9.578,52 | €2.000,27 | €4.000,55 | €184,15 | €10,45 |
| TEST | Scanner Top15 Long | 7 | €9.578,52 | €2.000,27 | €4.000,55 | €184,15 | €10,45 |
| TEST | Scanner Top20 Long | 7 | €9.578,52 | €2.000,27 | €4.000,55 | €184,15 | €10,45 |
| TEST | Forza relativa 1H V2 | 5 | €9.574,86 | €1.970,15 | €3.940,29 | €49,78 | €158,81 |
| TEST | 1H Balanced Long No Rhv V1 | 8 | €9.557,05 | €1.387,75 | €4.163,24 | €93,50 | €146,50 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 6 | €9.499,11 | €2.618,07 | €5.236,15 | €141,98 | €111,08 |
| TEST | Combo Adaptive Quality7 V1 | 6 | €9.470,56 | €2.208,05 | €4.416,09 | €97,32 | €82,46 |
| TEST | Bilanciata 1H V2 | 5 | €9.454,94 | €872,37 | €2.617,11 | €142,69 | €17,40 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.447,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.444,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.443,26 | €1.257,19 | €3.771,56 | €94,65 | €75,94 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.435,91 | €146,77 | €440,31 | €48,44 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.430,59 | €195,77 | €391,54 | €46,99 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 7 | €9.426,93 | €2.248,16 | €4.496,32 | €141,18 | €91,30 |
| TEST | Scanner Bottom10 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.320,02 | €1.082,57 | €2.165,15 | €96,67 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.305,85 | €1.080,93 | €2.161,86 | €96,53 | €0,00 |
| TEST | Combo Trend | 6 | €9.296,18 | €1.914,73 | €3.829,45 | €0,48 | €162,78 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.281,63 | €2.558,13 | €5.116,27 | €138,73 | €108,53 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 0 | €9.237,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.234,23 | €1.072,61 | €2.145,22 | €95,79 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 7 | €9.159,78 | €1.521,58 | €4.564,75 | €136,08 | €21,25 |
| TEST | Bilanciata 1H V1 | 1 | €9.151,18 | €135,05 | €405,16 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.114,86 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 8 | €9.022,11 | €1.879,85 | €3.759,69 | €2,63 | €155,98 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 8 | €8.901,85 | €1.858,66 | €3.717,31 | €44,65 | €142,98 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €8.445,51 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.715,38 | €-333,55 | 46 | 46 | 34,78% | 0,76 | €-7,25 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.103,69 | €974,86 | 78 | 78 | 48,72% | 1,56 | €12,50 | 3,63% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.842,27 | €716,47 | 46 | 46 | 47,83% | 1,82 | €15,58 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.802,41 | €754,20 | 95 | 95 | 52,63% | 1,37 | €7,94 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.744,90 | €589,31 | 69 | 69 | 50,72% | 1,43 | €8,54 | 4,33% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.565,59 | €463,96 | 100 | 100 | 46,00% | 1,21 | €4,64 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.491,38 | €477,55 | 29 | 29 | 48,28% | 1,77 | €16,47 | 2,40% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.400,20 | €302,56 | 148 | 148 | 46,62% | 1,11 | €2,04 | 4,46% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.179,84 | €57,08 | 79 | 79 | 43,04% | 1,04 | €0,72 | 8,68% |
| TEST | Combo Adaptive | Combo Adaptive | €10.167,39 | €3,59 | 108 | 108 | 40,74% | 1,00 | €0,03 | 7,91% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.131,57 | €-12,68 | 75 | 75 | 42,67% | 0,99 | €-0,17 | 6,25% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.130,32 | €66,34 | 4 | 4 | 50,00% | 1,63 | €16,58 | 1,05% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.126,53 | €126,53 | 40 | 40 | 45,00% | 1,13 | €3,16 | 3,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.107,65 | €49,10 | 4 | 4 | 50,00% | 1,47 | €12,27 | 1,01% |
| TEST | Ampia 4H | Confluenza trend | €10.102,33 | €60,72 | 45 | 45 | 26,67% | 1,05 | €1,35 | 4,45% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,94 | €46,94 | 7 | 7 | 57,14% | 1,28 | €6,71 | 1,89% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.035,93 | €-9,50 | 168 | 167 | 36,90% | 1,00 | €-0,06 | 6,56% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.029,22 | €29,50 | 121 | 121 | 43,80% | 1,01 | €0,24 | 7,10% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.022,40 | €24,50 | 25 | 25 | 48,00% | 1,27 | €0,98 | 0,33% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.022,21 | €-35,50 | 10 | 10 | 40,00% | 0,86 | €-3,55 | 2,77% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.004,48 | €4,90 | 25 | 25 | 48,00% | 1,27 | €0,20 | 0,07% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,76 | €-5,24 | 14 | 14 | 35,71% | 0,47 | €-0,37 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.983,99 | €-93,54 | 122 | 122 | 40,16% | 0,97 | €-0,77 | 9,12% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Sol Ema 4H | Trend following EMA | €9.974,31 | €-88,69 | 5 | 5 | 20,00% | 0,57 | €-17,74 | 2,27% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,79 | €-26,21 | 14 | 14 | 35,71% | 0,47 | €-1,87 | 0,53% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.951,64 | €-47,76 | 35 | 31 | 42,86% | 0,95 | €-1,36 | 3,89% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.949,57 | €-50,43 | 9 | 9 | 33,33% | 0,85 | €-5,60 | 2,63% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.947,73 | €-49,88 | 25 | 25 | 48,00% | 0,61 | €-2,00 | 0,84% |
| TEST | Btc Ema 1H | Trend following EMA | €9.942,20 | €-57,80 | 10 | 10 | 40,00% | 0,82 | €-5,78 | 1,94% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.940,80 | €-59,20 | 14 | 14 | 35,71% | 0,32 | €-4,23 | 0,89% |
| TEST | Doge Ema 1H | Trend following EMA | €9.920,90 | €-79,10 | 14 | 14 | 57,14% | 0,77 | €-5,65 | 2,61% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.900,93 | €-210,81 | 89 | 89 | 39,33% | 0,90 | €-2,37 | 11,27% |
| TEST | Sol Ema 1H | Trend following EMA | €9.899,48 | €-151,22 | 11 | 11 | 27,27% | 0,61 | €-13,75 | 3,33% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.892,99 | €-107,01 | 8 | 8 | 37,50% | 0,66 | €-13,38 | 1,89% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,99 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,83% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.878,92 | €-121,08 | 10 | 10 | 40,00% | 0,63 | €-12,11 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.826,58 | €-396,77 | 71 | 71 | 35,21% | 0,80 | €-5,59 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.820,83 | €-402,38 | 75 | 75 | 36,00% | 0,80 | €-5,37 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.816,06 | €-183,94 | 11 | 11 | 45,45% | 0,49 | €-16,72 | 2,90% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.813,01 | €-227,71 | 129 | 128 | 47,29% | 0,91 | €-1,77 | 9,50% |
| TEST | Eth Ema 1H | Trend following EMA | €9.793,37 | €-268,16 | 13 | 13 | 30,77% | 0,47 | €-20,63 | 4,80% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,65 | €-220,08 | 85 | 85 | 42,35% | 0,88 | €-2,59 | 7,10% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.767,15 | €-390,71 | 107 | 107 | 39,25% | 0,81 | €-3,65 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.758,68 | €-291,30 | 12 | 12 | 25,00% | 0,35 | €-24,27 | 4,59% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.749,93 | €-290,53 | 173 | 172 | 40,46% | 0,92 | €-1,68 | 9,48% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.742,29 | €-320,36 | 27 | 27 | 40,74% | 0,61 | €-11,87 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.718,69 | €-269,20 | 5 | 5 | 20,00% | 0,05 | €-53,84 | 3,32% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.711,41 | €-288,59 | 13 | 13 | 23,08% | 0,41 | €-22,20 | 4,35% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.702,33 | €-365,26 | 131 | 130 | 41,98% | 0,90 | €-2,79 | 9,66% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.651,39 | €-438,59 | 72 | 72 | 34,72% | 0,77 | €-6,09 | 7,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.620,52 | €-398,92 | 89 | 89 | 38,20% | 0,82 | €-4,48 | 10,60% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.619,75 | €-442,11 | 27 | 27 | 33,33% | 0,47 | €-16,37 | 5,41% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.599,92 | €-488,85 | 145 | 144 | 40,69% | 0,84 | €-3,37 | 9,00% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.595,22 | €-404,43 | 58 | 58 | 39,66% | 0,78 | €-6,97 | 7,74% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.591,75 | €-456,52 | 39 | 39 | 41,03% | 0,63 | €-11,71 | 5,38% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.578,52 | €-429,13 | 77 | 77 | 41,56% | 0,76 | €-5,57 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.578,52 | €-429,13 | 77 | 77 | 41,56% | 0,76 | €-5,57 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.578,52 | €-429,13 | 77 | 77 | 41,56% | 0,76 | €-5,57 | 10,31% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.574,86 | €-581,26 | 88 | 84 | 37,50% | 0,80 | €-6,61 | 10,88% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.557,05 | €-586,71 | 67 | 67 | 38,81% | 0,68 | €-8,76 | 9,26% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Combo Scanner | Combo Scanner | €9.499,11 | €-608,10 | 93 | 93 | 38,71% | 0,76 | €-6,54 | 11,38% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.470,56 | €-609,07 | 54 | 54 | 31,48% | 0,63 | €-11,28 | 8,88% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.454,94 | €-560,73 | 81 | 74 | 39,51% | 0,71 | €-6,92 | 8,84% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.447,55 | €-615,90 | 84 | 83 | 44,05% | 0,76 | €-7,33 | 7,69% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.444,37 | €-621,42 | 89 | 88 | 43,82% | 0,78 | €-6,98 | 9,98% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.443,26 | €-630,07 | 78 | 78 | 38,46% | 0,64 | €-8,08 | 8,85% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,91 | €-563,83 | 111 | 111 | 40,54% | 0,80 | €-5,08 | 6,91% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.430,59 | €-569,07 | 73 | 73 | 39,73% | 0,73 | €-7,80 | 7,02% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.426,93 | €-660,96 | 89 | 89 | 37,08% | 0,71 | €-7,43 | 8,78% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.320,02 | €-678,72 | 58 | 58 | 32,76% | 0,60 | €-11,70 | 8,30% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,85 | €-692,90 | 59 | 59 | 32,20% | 0,58 | €-11,74 | 8,30% |
| TEST | Combo Trend | Combo Trend | €9.296,18 | €-863,69 | 129 | 129 | 34,11% | 0,74 | €-6,70 | 10,85% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.281,63 | €-823,12 | 81 | 81 | 37,04% | 0,58 | €-10,16 | 12,28% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.237,05 | €-762,95 | 59 | 59 | 33,90% | 0,57 | €-12,93 | 11,72% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.234,23 | €-764,52 | 86 | 86 | 32,56% | 0,66 | €-8,89 | 9,40% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.159,78 | €-858,72 | 109 | 109 | 33,03% | 0,70 | €-7,88 | 12,52% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.151,18 | €-848,58 | 120 | 120 | 36,67% | 0,69 | €-7,07 | 13,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,86 | €-884,87 | 37 | 37 | 37,84% | 0,48 | €-23,92 | 10,64% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.022,11 | €-1.131,04 | 94 | 94 | 28,72% | 0,49 | €-12,03 | 12,31% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.901,85 | €-1.238,63 | 112 | 112 | 33,04% | 0,51 | €-11,06 | 15,45% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 2258,11153 | 2350,10000 | 2283,06760 | 1516,69825 | 2433,12687 | €415,70 | €1.247,11 | €0,00 | €50,80 |
| Principale 4H | LINK | LONG | Confluenza trend | 240m | 3,0x | 10,58112 | 10,58112 | 10,13407 | 7,10698 | 11,47522 | €16,96 | €50,87 | €2,15 | €0,00 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1521,81065 | 2396,13352 | €43,23 | €129,69 | €0,00 | €4,83 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,23032 | 1,30921 | 1,27542 | 0,82636 | 1,33685 | €362,43 | €1.087,28 | €0,00 | €69,72 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €372,21 | €1.116,62 | €0,00 | €71,54 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 72,76855 | 72,50200 | 70,17618 | 48,87621 | 77,95329 | €16,05 | €48,15 | €1,72 | €-0,18 |
| 1H Balanced Long No Rhv V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,20285 | 0,20671 | 0,20393 | 0,13625 | 0,21614 | €10,30 | €30,89 | €0,00 | €0,59 |
| 1H Balanced Long No Rhv V1 | SUI | LONG | Confluenza trend | 60m | 3,0x | 0,74725 | 0,74725 | 0,72830 | 0,50190 | 0,78515 | €9,09 | €27,27 | €0,69 | €0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | LINK | LONG | Confluenza trend V2 | 60m | 3,0x | 10,70214 | 10,70214 | 10,45333 | 7,18827 | 11,19976 | €19,07 | €57,20 | €1,33 | €0,00 |
| Bilanciata 1H V2 | BOME | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00115 | 0,00119 | 0,00104 | 0,00077 | 0,00136 | €167,15 | €501,46 | €46,62 | €17,40 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2350,10000 | 2296,55064 | 1510,45050 | 2383,72136 | €531,07 | €1.593,21 | €0,00 | €71,76 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,62 | €43,87 | €0,00 | €1,53 |
| Bilanciata 1H V3 Filtered | BOME | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00117 | 0,00119 | 0,00106 | 0,00079 | 0,00140 | €172,42 | €517,27 | €49,79 | €7,13 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 72,76855 | 72,50200 | 70,17618 | 48,87621 | 77,95329 | €13,01 | €39,02 | €1,39 | €-0,14 |
| 1H Fast Score 6 75 Cost Aware V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €624,93 | €1.874,80 | €51,62 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2339,94790 | 2350,10000 | 2293,95002 | 1571,66500 | 2408,94470 | €907,70 | €2.723,10 | €53,53 | €11,81 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €1.319,73 | €3.959,19 | €0,00 | €45,98 |
| 1H Fast Score 6 75 Cost Aware V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €18,83 | €56,50 | €1,47 | €-0,47 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €-2,16 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,30947 | 1,30921 | 1,27240 | 0,87953 | 1,36509 | €626,69 | €1.880,06 | €53,23 | €-0,38 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| 1H Fast No Pepe V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1213,43264 | 1213,43264 | 1179,70743 | 815,02226 | 1264,02045 | €33,31 | €99,94 | €2,78 | €0,00 |
| 1H Fast No Pepe V1 | LINK | LONG | Momentum / breakout | 60m | 3,0x | 10,64413 | 10,64413 | 10,46121 | 7,14931 | 10,91851 | €17,86 | €53,58 | €0,92 | €0,00 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2319,13373 | 2350,10000 | 2319,13373 | 1557,68482 | 2385,82358 | €863,99 | €2.591,96 | €0,00 | €34,61 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00114 | 0,00119 | 0,00105 | 0,00077 | 0,00128 | €202,87 | €608,61 | €48,19 | €23,44 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €1.285,00 | €3.855,00 | €0,00 | €44,77 |
| 1H Fast No Pepe V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,73835 | 0,73835 | 0,72383 | 0,49592 | 0,76013 | €10,95 | €32,86 | €0,65 | €0,00 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €12,19 | €36,56 | €0,95 | €-0,30 |
| 1H Fast No Pepe V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €17,08 | €51,23 | €1,82 | €-0,01 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| 1H Fast Tp2 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 121,01735 | 121,01735 | 127,15573 | 160,75137 | 108,74057 | €315,49 | €946,48 | €48,01 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1204,83092 | 1204,83092 | 1170,97389 | 809,24477 | 1272,54496 | €18,91 | €56,74 | €1,59 | €0,00 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2319,13373 | 2350,10000 | 2319,13373 | 1557,68482 | 2408,05354 | €10,04 | €30,11 | €0,00 | €0,40 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00114 | 0,00119 | 0,00105 | 0,00077 | 0,00133 | €205,81 | €617,44 | €48,89 | €23,78 |
| 1H Fast Tp2 V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,20285 | 0,20671 | 0,20469 | 0,13625 | 0,21319 | €17,28 | €51,83 | €0,00 | €0,99 |
| 1H Fast Tp2 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 89,26385 | 89,31100 | 88,02436 | 59,95555 | 91,74282 | €10,38 | €31,15 | €0,43 | €0,02 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €-34,58 |
| 1H Fast Tp2 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13544 | €9,83 | €29,49 | €1,05 | €-0,01 |
| Rapida 1H V2 | SOXL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 121,15726 | 121,15726 | 127,13595 | 160,93723 | 112,18923 | €333,06 | €999,18 | €49,31 | €-0,00 |
| Rapida 1H V3 Filtered | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,81 | €65,43 | €1,80 | €0,00 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2324,84488 | 2350,10000 | 2324,84488 | 1561,52081 | 2390,91922 | €9,36 | €28,08 | €0,00 | €0,31 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,02180 | 72,50200 | 72,01459 | 49,71798 | 77,03262 | €14,34 | €43,03 | €1,17 | €-0,88 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €10,13 | €30,39 | €1,98 | €0,65 |
| Rapida 1H V3 Filtered | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €564,49 | €1.693,47 | €0,00 | €51,89 |
| Rapida 1H V3 Filtered | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €12,05 | €36,16 | €0,00 | €0,42 |
| Rapida 1H V3 Filtered | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €561,67 | €1.685,00 | €43,78 | €-13,92 |
| Rapida 1H V3 Filtered | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €456,14 | €1.368,43 | €48,63 | €-0,27 |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2339,94790 | 2350,10000 | 2293,95002 | 1571,66500 | 2408,94470 | €11,60 | €34,80 | €0,68 | €0,15 |
| 1H Fast V3 Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €17,63 | €52,90 | €0,00 | €1,59 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €231,87 | €695,60 | €45,44 | €14,80 |
| 1H Fast V3 Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €535,74 | €1.607,21 | €0,00 | €49,25 |
| 1H Fast V3 Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €15,23 | €45,70 | €0,00 | €0,53 |
| 1H Fast V3 Long Only V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €582,94 | €1.748,82 | €45,43 | €-14,45 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €-30,63 |
| 1H Fast V3 No Esports V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €18,11 | €54,34 | €1,50 | €0,00 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2324,84488 | 2350,10000 | 2324,84488 | 1561,52081 | 2390,91922 | €9,21 | €27,62 | €0,00 | €0,30 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,02180 | 72,50200 | 72,01459 | 49,71798 | 77,03262 | €14,15 | €42,45 | €1,15 | €-0,87 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €10,02 | €30,05 | €1,96 | €0,64 |
| 1H Fast V3 No Esports V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €555,79 | €1.667,38 | €0,00 | €51,09 |
| 1H Fast V3 No Esports V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €11,99 | €35,98 | €0,00 | €0,42 |
| 1H Fast V3 No Esports V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €560,81 | €1.682,44 | €43,71 | €-13,90 |
| 1H Fast V3 No Esports V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €449,06 | €1.347,18 | €47,88 | €-0,27 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2339,94790 | 2350,10000 | 2293,95002 | 1571,66500 | 2408,94470 | €12,18 | €36,55 | €0,72 | €0,16 |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,52 | €55,56 | €0,00 | €1,67 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €243,53 | €730,59 | €47,72 | €15,55 |
| 1H Fast V3 No Esports Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €562,69 | €1.688,06 | €0,00 | €51,73 |
| 1H Fast V3 No Esports Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €16,00 | €48,00 | €0,00 | €0,56 |
| 1H Fast V3 No Esports Long Only V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €612,26 | €1.836,79 | €47,72 | €-15,17 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €-32,18 |
| 1H Fast V3 No Esports Mfe Lock V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,95 | €65,86 | €1,81 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2324,84488 | 2350,10000 | 2324,84488 | 1561,52081 | 2390,91922 | €9,42 | €28,26 | €0,00 | €0,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,02180 | 72,50200 | 72,01459 | 49,71798 | 77,03262 | €14,44 | €43,31 | €1,17 | €-0,89 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €10,12 | €30,35 | €1,98 | €0,65 |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €568,14 | €1.704,43 | €0,00 | €52,23 |
| 1H Fast V3 No Esports Mfe Lock V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €12,13 | €36,40 | €0,00 | €0,42 |
| 1H Fast V3 No Esports Mfe Lock V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €565,43 | €1.696,28 | €44,07 | €-14,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €459,09 | €1.377,28 | €48,95 | €-0,28 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 9,97398 | 9,97398 | 10,38253 | 5,03686 | 11,21104 | €560,46 | €1.120,91 | €0,00 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2258,11153 | 2350,10000 | 2144,35158 | 1140,34632 | 2576,63943 | €502,94 | €1.005,89 | €50,68 | €40,98 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 565,27303 | 589,61000 | 531,45855 | 285,46288 | 659,95358 | €31,20 | €62,41 | €3,73 | €2,69 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 71,99640 | 72,50200 | 66,32059 | 36,35818 | 87,88866 | €16,69 | €33,38 | €2,63 | €0,23 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €581,93 | €1.163,86 | €0,00 | €86,98 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 72,36547 | 72,50200 | 69,70054 | 36,54456 | 78,22831 | €640,11 | €1.280,23 | €47,15 | €2,42 |
| Forza relativa 1H V2 | XRP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,34751 | €533,57 | €1.067,14 | €0,00 | €68,43 |
| Forza relativa 1H V2 | BOME | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00115 | 0,00119 | 0,00104 | 0,00058 | 0,00138 | €14,16 | €28,32 | €2,63 | €0,98 |
| Scalp RSI Short 75 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 89,11517 | 89,31100 | 90,15113 | 94,61061 | 87,56124 | €10,00 | €150,00 | €1,74 | €-0,33 |
| Scalp RSI Short 75 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 89,11517 | 89,31100 | 90,15113 | 94,61061 | 87,56124 | €50,00 | €750,00 | €8,72 | €-1,65 |
| Scalp RSI Short 75 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 89,11517 | 89,31100 | 90,15113 | 106,49263 | 87,04326 | €171,19 | €855,93 | €9,95 | €-1,88 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2350,10000 | 2300,60626 | 1139,69979 | 2409,20720 | €999,19 | €1.998,39 | €0,00 | €82,59 |
| Benchmark Donchian breakout 1H | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,51209 | €910,44 | €1.820,87 | €54,32 | €0,00 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 87,44649 | 89,31100 | 85,50986 | 44,16048 | 92,28805 | €1.243,00 | €2.485,99 | €55,06 | €53,01 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 73,54771 | 72,50200 | 70,54476 | 37,14159 | 81,05509 | €82,39 | €164,78 | €6,73 | €-2,34 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20285 | 0,20671 | 0,19547 | 0,10244 | 0,22131 | €16,05 | €32,11 | €1,17 | €0,61 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2350,10000 | 2300,60626 | 1139,69979 | 2409,20720 | €975,67 | €1.951,34 | €0,00 | €80,64 |
| Donchian 1H Gb20 120R V1 | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,51209 | €889,00 | €1.778,00 | €53,04 | €0,00 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 87,44649 | 89,31100 | 85,50986 | 44,16048 | 92,28805 | €1.213,73 | €2.427,46 | €53,76 | €51,76 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 73,54771 | 72,50200 | 70,54476 | 37,14159 | 81,05509 | €80,45 | €160,90 | €6,57 | €-2,29 |
| Donchian 1H Gb20 120R V1 | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20285 | 0,20671 | 0,19547 | 0,10244 | 0,22131 | €15,68 | €31,35 | €1,14 | €0,60 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 69,29086 | 72,50200 | 72,11451 | 34,99188 | 76,51998 | €468,29 | €936,58 | €0,00 | €43,40 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2264,89289 | 2350,10000 | 2296,53215 | 1143,77091 | 2419,94510 | €713,61 | €1.427,21 | €0,00 | €53,69 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 87,44649 | 89,31100 | 87,65252 | 44,16048 | 91,70706 | €26,87 | €53,74 | €0,00 | €1,15 |
| Benchmark trend following EMA 1H | LINK | LONG | Trend following EMA | 60m | 2,0x | 10,64413 | 10,64413 | 10,38282 | 5,37528 | 11,21901 | €12,99 | €25,97 | €0,64 | €0,00 |
| Benchmark trend following EMA 1H | SUI | LONG | Trend following EMA | 60m | 2,0x | 0,73965 | 0,73965 | 0,71894 | 0,37352 | 0,78521 | €14,44 | €28,87 | €0,81 | €0,00 |
| Benchmark trend following EMA 1H | XRP | LONG | Trend following EMA | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,36053 | €443,18 | €886,36 | €0,00 | €56,84 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,36 | €28,72 | €1,19 | €0,89 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €95,49 | €190,98 | €0,00 | €7,11 |
| Scanner Top 5 Long 1H | LINK | LONG | Scanner Top 5 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €897,38 | €1.794,76 | €50,51 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,21 | €38,43 | €0,00 | €2,26 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €257,00 | €514,01 | €52,33 | €19,79 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,23032 | 1,30921 | 1,27542 | 0,62131 | 1,33685 | €583,16 | €1.166,31 | €0,00 | €74,79 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,20285 | 0,20671 | 0,20393 | 0,10244 | 0,21614 | €16,77 | €33,55 | €0,00 | €0,64 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €0,00 | €5,86 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,09 | €38,18 | €0,00 | €1,34 |
| Scanner Top10 Long | BOME | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €234,16 | €468,32 | €47,68 | €18,03 |
| Scanner Top10 Long | XRP | LONG | Scanner Top10 Long | 60m | 2,0x | 1,27028 | 1,30921 | 1,28230 | 0,64149 | 1,36326 | €18,94 | €37,87 | €0,00 | €1,16 |
| Scanner Top10 Long | ADA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €45,34 | €-15,94 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €0,00 | €5,86 |
| Scanner Top15 Long | LINK | LONG | Scanner Top15 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,09 | €38,18 | €0,00 | €1,34 |
| Scanner Top15 Long | BOME | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €234,16 | €468,32 | €47,68 | €18,03 |
| Scanner Top15 Long | XRP | LONG | Scanner Top15 Long | 60m | 2,0x | 1,27028 | 1,30921 | 1,28230 | 0,64149 | 1,36326 | €18,94 | €37,87 | €0,00 | €1,16 |
| Scanner Top15 Long | ADA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €45,34 | €-15,94 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €0,00 | €5,86 |
| Scanner Top20 Long | LINK | LONG | Scanner Top20 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,09 | €38,18 | €0,00 | €1,34 |
| Scanner Top20 Long | BOME | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €234,16 | €468,32 | €47,68 | €18,03 |
| Scanner Top20 Long | XRP | LONG | Scanner Top20 Long | 60m | 2,0x | 1,27028 | 1,30921 | 1,28230 | 0,64149 | 1,36326 | €18,94 | €37,87 | €0,00 | €1,16 |
| Scanner Top20 Long | ADA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €45,34 | €-15,94 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.131,85 | €2.263,69 | €0,00 | €86,98 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 79,49355 | €663,04 | €1.326,08 | €48,73 | €-18,85 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €239,15 | €478,30 | €48,69 | €18,42 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23713 | 1,30921 | 1,27656 | 0,62475 | 1,35194 | €14,19 | €28,38 | €0,00 | €1,65 |
| Scanner Top 5 + forza BTC 1H | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,21747 | €15,99 | €31,99 | €1,05 | €0,61 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €664,60 | €1.329,20 | €49,51 | €26,97 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.061,05 | €2.122,10 | €0,00 | €81,54 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 79,49355 | €621,57 | €1.243,14 | €45,68 | €-17,67 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €224,19 | €448,38 | €45,65 | €17,27 |
| Scanner Top5 Btc Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23713 | 1,30921 | 1,27656 | 0,62475 | 1,35194 | €13,30 | €26,61 | €0,00 | €1,55 |
| Scanner Top5 Btc Mfe V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,21747 | €14,99 | €29,99 | €0,98 | €0,57 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €623,03 | €1.246,06 | €46,42 | €25,28 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.108,06 | €2.216,13 | €0,00 | €85,15 |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,28 | €28,57 | €0,00 | €1,54 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €228,27 | €456,55 | €46,48 | €17,58 |
| Scanner Top5 Btc Guard V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,27028 | 1,30921 | 1,22380 | 0,64149 | 1,37255 | €18,48 | €36,95 | €1,35 | €1,13 |
| Scanner Top5 Btc Guard V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20843 | 0,20671 | 0,20147 | 0,10526 | 0,22375 | €722,36 | €1.444,72 | €48,26 | €-11,93 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13917 | €13,46 | €26,92 | €1,23 | €-0,01 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.082,29 | €2.164,59 | €0,00 | €83,17 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €13,95 | €27,90 | €0,00 | €1,51 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €222,97 | €445,93 | €45,40 | €17,17 |
| Scanner Top5 Btc Guard Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,27028 | 1,30921 | 1,22380 | 0,64149 | 1,37255 | €18,05 | €36,09 | €1,32 | €1,11 |
| Scanner Top5 Btc Guard Mfe V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20843 | 0,20671 | 0,20147 | 0,10526 | 0,22375 | €705,56 | €1.411,12 | €47,14 | €-11,66 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13917 | €13,15 | €26,29 | €1,20 | €-0,01 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2350,10000 | 2306,95673 | 1139,69979 | 2421,39727 | €964,53 | €1.929,06 | €0,00 | €79,72 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 91,52201 | €12,51 | €25,03 | €0,00 | €0,96 |
| Scanner Top5 Btc Runner25 V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,55211 | 10,55211 | 10,31704 | 5,32882 | 11,25731 | €17,19 | €34,38 | €0,77 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 81,65567 | €64,00 | €127,99 | €4,70 | €-1,82 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €569,98 | €1.139,95 | €0,00 | €67,04 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00116 | 0,00119 | 0,00104 | 0,00059 | 0,00153 | €229,96 | €459,93 | €48,84 | €11,65 |
| Scanner Top5 Btc Runner25 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23032 | 1,30921 | 1,27542 | 0,62131 | 1,39012 | €530,99 | €1.061,99 | €0,00 | €68,10 |
| Scanner Top5 Btc Runner25 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,22278 | €32,84 | €65,68 | €2,15 | €1,25 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,14379 | €18,15 | €36,30 | €1,66 | €-0,01 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2350,10000 | 2306,95673 | 1139,69979 | 2421,39727 | €965,10 | €1.930,19 | €0,00 | €79,77 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 91,52201 | €12,52 | €25,04 | €0,00 | €0,96 |
| Scanner Top5 Btc Tp3 V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,55211 | 10,55211 | 10,31704 | 5,32882 | 11,25731 | €17,20 | €34,40 | €0,77 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 81,65567 | €64,03 | €128,07 | €4,71 | €-1,82 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €570,31 | €1.140,62 | €0,00 | €67,08 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00116 | 0,00119 | 0,00104 | 0,00059 | 0,00153 | €230,10 | €460,19 | €48,87 | €11,66 |
| Scanner Top5 Btc Tp3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23032 | 1,30921 | 1,27542 | 0,62131 | 1,39012 | €531,30 | €1.062,61 | €0,00 | €68,14 |
| Scanner Top5 Btc Tp3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,22278 | €32,86 | €65,72 | €2,15 | €1,25 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,14379 | €18,16 | €36,32 | €1,66 | €-0,01 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 69,29086 | 72,50200 | 72,11451 | 34,99188 | 76,51998 | €482,28 | €964,56 | €0,00 | €44,70 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2264,89289 | 2350,10000 | 2296,53215 | 1143,77091 | 2419,94510 | €734,93 | €1.469,85 | €0,00 | €55,30 |
| Combo Trend | XRP | LONG | Combo Trend | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,36053 | €478,56 | €957,11 | €0,00 | €61,37 |
| Combo Trend | ADA | LONG | Combo Trend | 60m | 2,0x | 0,19795 | 0,20671 | 0,20358 | 0,09996 | 0,21370 | €12,65 | €25,29 | €0,00 | €1,12 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 88,28565 | 89,31100 | 86,59423 | 44,58426 | 92,00679 | €12,61 | €25,21 | €0,48 | €0,29 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.085,91 | €2.171,82 | €0,00 | €83,45 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 79,49355 | €636,13 | €1.272,26 | €46,75 | €-18,09 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €229,44 | €458,89 | €46,72 | €17,67 |
| Combo Scanner | XRP | LONG | Combo Scanner | 60m | 2,0x | 1,23713 | 1,30921 | 1,27656 | 0,62475 | 1,35194 | €13,62 | €27,23 | €0,00 | €1,59 |
| Combo Scanner | ADA | LONG | Combo Scanner | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,21747 | €15,34 | €30,69 | €1,01 | €0,58 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,63 | €1.275,26 | €47,50 | €25,87 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €574,74 | €1.149,48 | €0,00 | €73,71 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €616,14 | €1.232,28 | €0,00 | €78,95 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 74,02180 | 72,50200 | 71,44110 | 37,38101 | 79,18321 | €17,24 | €34,48 | €1,20 | €-0,71 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 88,28565 | 89,31100 | 86,76337 | 44,58426 | 91,33022 | €24,80 | €49,59 | €0,86 | €0,58 |
| Combo Adaptive | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00106 | 0,00059 | 0,00137 | €286,94 | €573,88 | €50,57 | €13,22 |
| Combo Adaptive | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20506 | 0,20671 | 0,19795 | 0,10356 | 0,21928 | €32,01 | €64,01 | €2,22 | €0,51 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 87,44649 | 89,31100 | 88,80519 | 44,16048 | 90,93241 | €53,92 | €107,83 | €0,00 | €2,30 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €564,25 | €1.128,50 | €0,00 | €52,69 |
| Combo Adaptive Mfe Trail | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,73965 | 0,73965 | 0,72101 | 0,37352 | 0,77693 | €17,77 | €35,54 | €0,90 | €0,00 |
| Combo Adaptive Mfe Trail | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00113 | 0,00119 | 0,00113 | 0,00057 | 0,00136 | €198,74 | €397,49 | €0,00 | €21,61 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,28405 | 0,62131 | 1,33685 | €505,43 | €1.010,86 | €0,00 | €64,82 |
| Combo Adaptive Mfe Trail | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2324,84488 | 2350,10000 | 2327,63469 | 1174,04666 | 2438,11520 | €26,46 | €52,93 | €0,00 | €0,57 |
| Combo Adaptive Mfe Trail | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,19795 | 0,20671 | 0,20522 | 0,09996 | 0,21084 | €13,30 | €26,60 | €0,00 | €1,18 |
| Combo Adaptive Mfe Trail | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €478,78 | €957,55 | €43,76 | €-0,19 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €638,10 | €1.276,19 | €46,90 | €-18,14 |
| Combo Adaptive Quality7 V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2339,94790 | 2350,10000 | 2280,80777 | 1181,67369 | 2458,22812 | €39,02 | €78,04 | €1,97 | €0,34 |
| Combo Adaptive Quality7 V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23713 | 1,30921 | 1,27966 | 0,62475 | 1,34151 | €555,60 | €1.111,20 | €0,00 | €64,75 |
| Combo Adaptive Quality7 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €589,54 | €1.179,07 | €0,00 | €35,52 |
| Combo Adaptive Quality7 V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €14,11 | €28,23 | €1,29 | €-0,01 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €680,15 | €1.360,29 | €49,99 | €-19,34 |
| Combo Adaptive Regime V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2278,66564 | 2350,10000 | 2311,06677 | 1150,72615 | 2386,92910 | €48,22 | €96,44 | €0,00 | €3,02 |
| Combo Adaptive Regime V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 88,28565 | 89,31100 | 86,76337 | 44,58426 | 91,33022 | €1.383,29 | €2.766,57 | €47,70 | €32,13 |
| Combo Adaptive Regime V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,27028 | 1,30921 | 1,28499 | 0,64149 | 1,36326 | €575,06 | €1.150,12 | €0,00 | €35,24 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,80 | €41,61 | €1,55 | €0,84 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €653,66 | €1.307,32 | €48,04 | €-18,59 |
| Combo Adaptive Quality7 Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €591,47 | €1.182,95 | €0,00 | €69,57 |
| Combo Adaptive Quality7 Regime V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00107 | 0,00059 | 0,00136 | €285,49 | €570,98 | €47,95 | €12,15 |
| Combo Adaptive Quality7 Regime V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,27028 | 1,30921 | 1,28499 | 0,64149 | 1,36326 | €19,19 | €38,38 | €0,00 | €1,18 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 87,44649 | 89,31100 | 88,13278 | 44,16048 | 90,93241 | €1.247,44 | €2.494,88 | €0,00 | €53,20 |
| Combo Adaptive Long Only V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €29,71 | €59,42 | €0,00 | €3,49 |
| Combo Adaptive Long Only V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €573,33 | €1.146,66 | €0,00 | €73,53 |
| Combo Adaptive Long Only V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €233,67 | €467,34 | €47,58 | €18,00 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,71874 | 72,50200 | 71,23745 | 37,22796 | 78,68131 | €18,24 | €36,48 | €1,23 | €-0,60 |
| Combo Adaptive Long Only V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20285 | 0,20671 | 0,20431 | 0,10244 | 0,21614 | €14,83 | €29,66 | €0,00 | €0,56 |
| Combo Adaptive Long Only V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €554,36 | €1.108,71 | €50,66 | €-0,22 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 87,44649 | 89,31100 | 88,13278 | 44,16048 | 90,93241 | €72,80 | €145,59 | €0,00 | €3,10 |
| Combo Adaptive Partial 1R V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €552,27 | €1.104,54 | €0,00 | €70,83 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €581,64 | €1.163,27 | €0,00 | €74,53 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 74,02180 | 72,50200 | 71,44110 | 37,38101 | 79,18321 | €16,14 | €32,28 | €1,13 | €-0,66 |
| Combo Adaptive Partial 1R V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00106 | 0,00059 | 0,00137 | €275,68 | €551,35 | €48,58 | €12,70 |
| Combo Adaptive Partial 1R V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20843 | 0,20671 | 0,20147 | 0,10526 | 0,22236 | €13,54 | €27,09 | €0,90 | €-0,22 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €661,99 | €1.323,97 | €48,65 | €-18,82 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €599,01 | €1.198,02 | €0,00 | €70,46 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00107 | 0,00059 | 0,00136 | €289,12 | €578,25 | €48,56 | €12,31 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,27028 | 1,30921 | 1,28499 | 0,64149 | 1,36326 | €19,43 | €38,87 | €0,00 | €1,19 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 87,44649 | 89,31100 | 88,23180 | 58,73489 | 90,93241 | €823,54 | €2.470,62 | €0,00 | €52,68 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 85,47309 | 89,31100 | 87,30972 | 43,16391 | 92,86927 | €715,87 | €1.431,74 | €0,00 | €64,29 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 87,44649 | 89,31100 | 88,23180 | 58,73489 | 90,54509 | €937,37 | €2.812,11 | €0,00 | €59,96 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 85,47309 | 89,31100 | 87,30972 | 43,16391 | 93,75681 | €727,07 | €1.454,13 | €0,00 | €65,29 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 87,44649 | 89,31100 | 88,23180 | 58,73489 | 90,93241 | €811,83 | €2.435,48 | €0,00 | €51,93 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 85,47309 | 89,31100 | 87,30972 | 43,16391 | 93,54165 | €665,34 | €1.330,67 | €0,00 | €59,75 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2265,72305 | 2350,10000 | 2306,29586 | 1521,81065 | 2396,13352 | €563,60 | €1.690,79 | €0,00 | €62,97 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2258,11153 | 2350,10000 | 2283,06760 | 1140,34632 | 2498,75762 | €577,20 | €1.154,41 | €0,00 | €47,03 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 2339,01210 | 2350,10000 | 2388,27582 | 3106,98774 | 2265,11654 | €770,02 | €2.310,06 | €48,65 | €-10,95 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €632,92 | €1.265,84 | €0,00 | €44,27 |
| Combo Adaptive Side Regime Guard V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,73965 | 0,73965 | 0,72101 | 0,37352 | 0,77693 | €13,14 | €26,29 | €0,66 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00113 | 0,00119 | 0,00101 | 0,00057 | 0,00136 | €233,88 | €467,76 | €49,14 | €25,42 |
| Combo Adaptive Side Regime Guard V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €576,40 | €1.152,79 | €0,00 | €73,92 |
| Combo Adaptive Side Regime Guard V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 72,76855 | 72,50200 | 70,17618 | 36,74812 | 77,95329 | €23,38 | €46,77 | €1,67 | €-0,17 |
| Combo Adaptive Side Regime Guard V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €721,85 | €1.443,70 | €50,85 | €-17,88 |
| Combo Adaptive Side Regime Guard V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €17,85 | €35,69 | €1,63 | €-0,01 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 71,99640 | 72,50200 | 67,63039 | 48,35758 | 80,72841 | €287,94 | €863,83 | €52,38 | €6,07 |
| Main Side Regime Guard V1 | BOME | LONG | Confluenza trend | 240m | 3,0x | 0,00116 | 0,00119 | 0,00102 | 0,00078 | 0,00144 | €145,79 | €437,37 | €52,48 | €9,31 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 2265,72305 | 2350,10000 | 2295,01732 | 1144,19014 | 2425,11361 | €812,72 | €1.625,45 | €0,00 | €60,53 |
| Combo Trend Side Regime Guard V1 | LINK | LONG | Combo Trend | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,41622 | €12,55 | €25,10 | €0,75 | €0,00 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €584,95 | €1.169,89 | €0,00 | €68,80 |
| Combo Trend Side Regime Guard V1 | SUI | LONG | Combo Trend | 60m | 2,0x | 0,73965 | 0,73965 | 0,71894 | 0,37352 | 0,78521 | €36,53 | €73,06 | €2,05 | €0,00 |
| Combo Trend Side Regime Guard V1 | BOME | LONG | Combo Trend | 60m | 2,0x | 0,00113 | 0,00119 | 0,00100 | 0,00057 | 0,00142 | €223,08 | €446,17 | €52,08 | €24,25 |
| Combo Trend Side Regime Guard V1 | XRP | LONG | Combo Trend | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,36053 | €29,14 | €58,28 | €0,00 | €3,74 |
| Combo Trend Side Regime Guard V1 | ADA | LONG | Combo Trend | 60m | 2,0x | 0,19795 | 0,20671 | 0,20358 | 0,09996 | 0,21370 | €20,16 | €40,31 | €0,00 | €1,78 |
| Combo Trend Side Regime Guard V1 | ENA | LONG | Combo Trend | 60m | 2,0x | 0,12646 | 0,12643 | 0,12003 | 0,06386 | 0,14058 | €518,11 | €1.036,23 | €52,61 | €-0,21 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2350,10000 | 2296,55064 | 1510,45050 | 2383,72136 | €502,31 | €1.506,93 | €0,00 | €67,87 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €13,83 | €41,49 | €0,00 | €1,45 |
| 1H Balanced V3 Long Only V1 | BOME | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00117 | 0,00119 | 0,00106 | 0,00079 | 0,00140 | €163,09 | €489,26 | €47,09 | €6,75 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 72,76855 | 72,50200 | 70,17618 | 48,87621 | 77,95329 | €12,30 | €36,91 | €1,31 | €-0,14 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports V1 | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €68,19 | 1,45 | TARGET |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €69,71 | 1,45 | TARGET |
| Rapida 1H V3 Filtered | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €69,26 | 1,45 | TARGET |
| 1H Fast Score 6 75 Cost Aware V1 | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €76,31 | 1,45 | TARGET |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-0,07 | -0,07 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-0,07 | -0,07 | STOP_GAP_STRESS |
| Scanner Top20 Long | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-53,98 | -1,16 | STOP_GAP_STRESS |
| Scanner Top15 Long | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-53,98 | -1,16 | STOP_GAP_STRESS |
| Scanner Top10 Long | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-53,98 | -1,16 | STOP_GAP_STRESS |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €16,79 | 0,32 | STOP_GAP_STRESS |
| Combo Adaptive Mfe Trail | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-5,55 | -0,13 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-27,42 | -0,58 | STOP_GAP_STRESS |

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

Generato: 2026-08-21 05:32 UTC


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

Segnali totali salvati: **126**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-21 | BTC | 75.089,33 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-21 | DOGE | 0.08259 | +2 | +1 | +1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-21 | SOL | 89,61 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-20 | BTC | 69.558,29 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-20 | DOGE | 0.07454 | +4 | +3 | +3 | 0 | +2 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-20 | SOL | 84,90 | +3 | 0 | 0 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-19 | BTC | 64.293,48 | +5 | +3 | +2 | +2 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-19 | DOGE | 0.06997 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-19 | SOL | 76,87 | +2 | +3 | +2 | +2 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-18 | BTC | 64.145,05 | 0 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-18 | DOGE | 0.06969 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-18 | SOL | 75,65 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 42 | 41 | 40 | 39 | 37 | 35 | 34 | 30 | 23 | 14 | 0 | 0 |
| SOL | 42 | 41 | 40 | 39 | 37 | 35 | 34 | 30 | 23 | 14 | 0 | 0 |
| DOGE | 42 | 41 | 40 | 39 | 37 | 35 | 34 | 30 | 23 | 14 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-23 | 30g | 2026-08-22 | domani |
| SOL | 2026-07-23 | 30g | 2026-08-22 | domani |
| DOGE | 2026-07-23 | 30g | 2026-08-22 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 38 | 52,63% | +0,48% | +0,44% | PRIMA CALIBRAZIONE |
| BTC | 2g | 37 | 51,35% | +0,59% | +0,46% | PRIMA CALIBRAZIONE |
| BTC | 3g | 36 | 44,44% | +0,28% | +0,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | 35 | 34,29% | +0,83% | +0,47% | PRIMA CALIBRAZIONE |
| BTC | 7g | 33 | 42,42% | +0,58% | +0,25% | PRIMA CALIBRAZIONE |
| BTC | 10g | 32 | 43,75% | +0,94% | +0,65% | PRIMA CALIBRAZIONE |
| BTC | 14g | 28 | 50,00% | +0,88% | +0,76% | FEEDBACK RAPIDO |
| BTC | 21g | 21 | 33,33% | +0,73% | +0,41% | FEEDBACK RAPIDO |
| BTC | 30g | 13 | 84,62% | +1,66% | +2,05% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 34 | 55,88% | +0,54% | +0,35% | PRIMA CALIBRAZIONE |
| SOL | 2g | 33 | 48,48% | +0,93% | +0,72% | PRIMA CALIBRAZIONE |
| SOL | 3g | 32 | 50,00% | +1,12% | +0,84% | PRIMA CALIBRAZIONE |
| SOL | 5g | 30 | 53,33% | +1,03% | +0,85% | PRIMA CALIBRAZIONE |
| SOL | 7g | 28 | 57,14% | +0,63% | +0,81% | FEEDBACK RAPIDO |
| SOL | 10g | 27 | 59,26% | +1,08% | +1,36% | FEEDBACK RAPIDO |
| SOL | 14g | 23 | 65,22% | +0,67% | +2,25% | FEEDBACK RAPIDO |
| SOL | 21g | 17 | 52,94% | -0,00% | -2,09% | FEEDBACK RAPIDO |
| SOL | 30g | 13 | 38,46% | +1,17% | -1,21% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 39 | 46,15% | +0,42% | +0,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 38 | 47,37% | +0,54% | +0,54% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 37 | 45,95% | +0,39% | +0,69% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 35 | 54,29% | +0,19% | +0,91% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 33 | 60,61% | -0,24% | +1,10% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 32 | 56,25% | -0,43% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 28 | 60,71% | -0,98% | +2,34% | FEEDBACK RAPIDO |
| DOGE | 21g | 22 | 72,73% | -1,80% | +1,86% | FEEDBACK RAPIDO |
| DOGE | 30g | 14 | 85,71% | -2,36% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 38 | 52,63% | +0,48% | +0,44% | +0,07% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 41 | 56,10% | +0,43% | +0,43% | +0,04% | +0,94% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 41 | 56,10% | +0,43% | +0,43% | +0,04% | +0,94% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 36 | 36,11% | +0,63% | +0,06% | +0,21% | +1,13% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 9 | 22,22% | +1,47% | +0,30% | +0,63% | +1,80% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 37 | 51,35% | +0,59% | +0,46% | +0,04% | +1,26% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 40 | 55,00% | +0,73% | +0,73% | +0,20% | +1,40% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 40 | 55,00% | +0,73% | +0,73% | +0,20% | +1,40% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 35 | 40,00% | +0,99% | -0,19% | +0,45% | +1,65% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 8 | 12,50% | +0,95% | -0,95% | +0,58% | +1,56% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 36 | 44,44% | +0,28% | +0,08% | -1,25% | +1,85% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 39 | 56,41% | +0,76% | +0,76% | -1,20% | +2,23% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +0,76% | +0,76% | -1,20% | +2,23% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,35% | +0,35% | -1,24% | +1,77% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 34 | 29,41% | +1,16% | -1,32% | -0,97% | +2,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 8 | 12,50% | +2,41% | -2,41% | -0,24% | +3,25% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 35 | 34,29% | +0,83% | +0,47% | -1,96% | +2,83% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 37 | 43,24% | +0,79% | +0,79% | -1,94% | +2,82% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 37 | 43,24% | +0,79% | +0,79% | -1,94% | +2,82% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 33 | 45,45% | +0,96% | +0,96% | -1,91% | +2,87% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 32 | 34,38% | +1,09% | -1,67% | -1,70% | +3,14% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 7 | 14,29% | +5,22% | -5,22% | -0,85% | +6,49% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 33 | 42,42% | +0,58% | +0,25% | -2,30% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | +0,51% | +0,51% | -2,29% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | +0,51% | +0,51% | -2,29% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 31 | 54,84% | +0,75% | +0,75% | -2,26% | +2,95% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 30 | 33,33% | +0,98% | -1,48% | -2,03% | +3,18% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 5 | 0,00% | +5,48% | -5,48% | -1,02% | +6,59% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 32 | 43,75% | +0,94% | +0,65% | -2,66% | +3,40% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 30 | 56,67% | +1,12% | +1,12% | -2,58% | +3,49% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 29 | 34,48% | +1,07% | +0,49% | -2,43% | +3,73% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 28 | 50,00% | +0,88% | +0,76% | -2,82% | +3,98% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | +0,72% | +0,72% | -2,85% | +3,89% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 30 | 50,00% | +0,72% | +0,72% | -2,85% | +3,89% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | +1,22% | +1,22% | -2,61% | +4,12% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 25 | 60,00% | +1,12% | +1,06% | -2,53% | +4,34% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 21 | 33,33% | +0,73% | +0,41% | -3,17% | +4,45% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 23 | 47,83% | +0,57% | +0,57% | -3,22% | +4,29% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 23 | 47,83% | +0,57% | +0,57% | -3,22% | +4,29% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 19 | 52,63% | +0,98% | +0,98% | -2,95% | +4,70% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 18 | 22,22% | +0,29% | -0,67% | -2,87% | +4,14% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,90% | -0,90% | -2,23% | +2,76% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 13 | 84,62% | +1,66% | +2,05% | -3,10% | +5,77% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 14 | 64,29% | +1,49% | +1,49% | -3,07% | +5,70% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 14 | 64,29% | +1,49% | +1,49% | -3,07% | +5,70% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 11 | 45,45% | -0,01% | -0,46% | -2,60% | +4,94% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 39 | 46,15% | +0,42% | +0,41% | -0,08% | +1,14% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 41 | 56,10% | +0,31% | +0,60% | -0,21% | +1,00% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 41 | 56,10% | +0,31% | +0,60% | -0,21% | +1,00% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 34 | 52,94% | +0,19% | +0,44% | -0,35% | +0,79% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 27 | 37,04% | +0,44% | -0,44% | -0,04% | +1,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,69% | +3,06% | +2,25% | +3,87% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 38 | 47,37% | +0,54% | +0,54% | -0,13% | +1,56% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 40 | 50,00% | +0,40% | +0,64% | -0,26% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 40 | 50,00% | +0,40% | +0,64% | -0,26% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 33 | 60,61% | -0,28% | +0,28% | -0,87% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 27 | 44,44% | +1,08% | -1,08% | +0,40% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 37 | 45,95% | +0,39% | +0,69% | -1,64% | +2,56% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 39 | 51,28% | +0,26% | +0,58% | -1,74% | +2,38% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 39 | 51,28% | +0,26% | +0,58% | -1,74% | +2,38% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 37 | 54,05% | +0,08% | +0,81% | -1,69% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 33 | 48,48% | -0,26% | +0,25% | -1,90% | +1,81% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 26 | 34,62% | +0,93% | -0,93% | -1,60% | +3,14% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 35 | 54,29% | +0,19% | +0,91% | -2,47% | +3,05% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 37 | 51,35% | +0,07% | +0,76% | -2,54% | +2,88% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 37 | 51,35% | +0,07% | +0,76% | -2,54% | +2,88% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 51,43% | +0,10% | +0,78% | -2,53% | +2,79% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 32 | 65,62% | +0,07% | +1,47% | -2,76% | +2,83% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +0,44% | -0,44% | -2,47% | +3,40% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 33 | 60,61% | -0,24% | +1,10% | -2,95% | +3,17% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 35 | 57,14% | -0,36% | +0,86% | -3,04% | +3,04% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 35 | 57,14% | -0,36% | +0,86% | -3,04% | +3,04% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 33 | 57,58% | -0,32% | +0,85% | -3,06% | +2,95% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 23 | 52,17% | -0,04% | +0,04% | -3,05% | +3,58% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 32 | 56,25% | -0,43% | +1,51% | -3,53% | +3,51% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | -0,49% | +1,38% | -3,59% | +3,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 22 | 59,09% | -1,13% | +1,13% | -3,71% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 28 | 60,71% | -0,98% | +2,34% | -4,42% | +3,75% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 30 | 66,67% | -1,06% | +2,07% | -4,43% | +3,57% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 30 | 66,67% | -1,06% | +2,07% | -4,43% | +3,57% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | -1,02% | +2,10% | -4,48% | +3,51% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 29 | 68,97% | -1,32% | +1,32% | -4,53% | +3,41% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 21 | 66,67% | -1,05% | +1,05% | -4,58% | +3,86% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +6,85% | -6,24% | -1,27% | +10,97% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 22 | 72,73% | -1,80% | +1,86% | -5,47% | +3,70% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 23 | 78,26% | -1,89% | +3,25% | -5,53% | +3,53% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 23 | 78,26% | -1,89% | +3,25% | -5,53% | +3,53% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 21 | 80,95% | -1,95% | +3,44% | -5,70% | +3,44% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 23 | 82,61% | -1,89% | +1,89% | -5,53% | +3,53% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 19 | 78,95% | -1,48% | +1,48% | -5,33% | +4,10% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 13 | 84,62% | -2,07% | +2,07% | -6,54% | +3,57% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 34 | 55,88% | +0,54% | +0,35% | -0,03% | +1,18% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 36 | 61,11% | +0,10% | +0,34% | -0,37% | +0,72% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 39 | 58,97% | +0,18% | +0,23% | -0,31% | +0,81% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 38 | 50,00% | +0,12% | +0,08% | -0,43% | +0,69% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,29% | +0,21% | -0,37% | +0,83% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 33 | 48,48% | +0,93% | +0,72% | +0,21% | +1,77% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +0,64% | +0,77% | -0,12% | +1,36% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 39 | 51,28% | +0,62% | +0,69% | -0,11% | +1,47% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 37 | 37,84% | +0,26% | -0,57% | -0,40% | +1,12% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 32 | 50,00% | +1,12% | +0,84% | -1,66% | +2,81% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 35 | 48,57% | +0,67% | +0,89% | -1,96% | +2,46% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 38 | 47,37% | +0,64% | +0,80% | -1,90% | +2,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 33 | 48,48% | +0,83% | +0,77% | -1,81% | +2,66% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 37 | 40,54% | +0,73% | -1,05% | -1,85% | +2,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 30 | 53,33% | +1,03% | +0,85% | -2,48% | +3,52% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 33 | 54,55% | +0,72% | +0,93% | -2,75% | +3,17% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | +0,72% | +0,80% | -2,69% | +3,23% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 31 | 51,61% | +0,70% | +0,94% | -2,63% | +3,32% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 35 | 42,86% | +0,70% | -1,17% | -2,76% | +3,33% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 28 | 57,14% | +0,63% | +0,81% | -2,99% | +3,55% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 31 | 61,29% | +0,22% | +0,97% | -3,26% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 34 | 61,76% | +0,20% | +0,89% | -3,21% | +3,31% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 29 | 55,17% | +0,50% | +0,57% | -3,13% | +3,39% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 33 | 36,36% | +0,24% | -0,86% | -3,30% | +3,43% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 27 | 59,26% | +1,08% | +1,36% | -3,43% | +4,44% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 30 | 63,33% | +0,86% | +1,58% | -3,78% | +4,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 33 | 60,61% | +0,76% | +1,45% | -3,75% | +4,04% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 28 | 57,14% | +1,29% | +1,09% | -3,62% | +4,25% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 32 | 46,88% | +0,07% | -0,22% | -3,88% | +3,64% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 23 | 65,22% | +0,67% | +2,25% | -4,30% | +5,13% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 26 | 80,77% | +1,13% | +2,57% | -4,47% | +4,82% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 29 | 82,76% | +0,69% | +2,63% | -4,41% | +4,73% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 24 | 62,50% | +1,50% | +1,65% | -4,14% | +5,12% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 30 | 36,67% | +0,54% | -1,21% | -4,49% | +4,69% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 17 | 52,94% | -0,00% | -2,09% | -6,68% | +4,89% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 19 | 73,68% | +0,40% | +3,34% | -6,51% | +4,59% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 22 | 77,27% | -0,03% | +3,26% | -6,45% | +4,49% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 17 | 47,06% | +0,76% | +1,76% | -6,24% | +4,98% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 23 | 52,17% | +0,01% | -1,80% | -6,47% | +4,45% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 15 | 53,33% | +2,32% | -2,32% | -6,02% | +5,58% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 13 | 38,46% | +1,17% | -1,21% | -7,64% | +4,78% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | +1,10% | +0,05% | -8,09% | +4,84% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 13 | 61,54% | +0,90% | -0,02% | -7,80% | +4,62% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -0,01% | +0,51% | -7,91% | +3,88% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 14 | 28,57% | +0,92% | -2,26% | -7,74% | +4,55% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 6 | 33,33% | +2,65% | -2,65% | -6,95% | +6,02% | FEEDBACK RAPIDO |
| SOL | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | FEEDBACK RAPIDO |
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

Generato: 2026-08-21 05:32 UTC

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
| BTC | 42 | PRIMA CALIBRAZIONE | 41 | 12 | 0 | 0 | Famiglia statistica | 1g | 56,10% | +0,43% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 42 | PRIMA CALIBRAZIONE | 38 | 13 | 0 | 0 | Tecnico | 1g | 50,00% | +0,08% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 42 | PRIMA CALIBRAZIONE | 41 | 13 | 0 | 0 | Famiglia statistica | 1g | 56,10% | +0,60% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 9 | 22,22% | +0,30% | +1,47% | +0,63% | +1,80% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 41 | 56,10% | +0,43% | +0,43% | +0,04% | +0,94% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 36 | 36,11% | +0,06% | +0,63% | +0,21% | +1,13% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 8 | 12,50% | -0,95% | +0,95% | +0,58% | +1,56% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 40 | 55,00% | +0,73% | +0,73% | +0,20% | +1,40% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 35 | 40,00% | -0,19% | +0,99% | +0,45% | +1,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 8 | 12,50% | -2,41% | +2,41% | -0,24% | +3,25% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 39 | 56,41% | +0,76% | +0,76% | -1,20% | +2,23% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 34 | 29,41% | -1,32% | +1,16% | -0,97% | +2,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 7 | 14,29% | -5,22% | +5,22% | -0,85% | +6,49% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 37 | 43,24% | +0,79% | +0,79% | -1,94% | +2,82% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 32 | 34,38% | -1,67% | +1,09% | -1,70% | +3,14% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 5 | 0,00% | -5,48% | +5,48% | -1,02% | +6,59% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 35 | 51,43% | +0,51% | +0,51% | -2,29% | +2,88% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 30 | 33,33% | -1,48% | +0,98% | -2,03% | +3,18% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 29 | 34,48% | +0,49% | +1,07% | -2,43% | +3,73% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 30 | 50,00% | +0,72% | +0,72% | -2,85% | +3,89% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 25 | 60,00% | +1,06% | +1,12% | -2,53% | +4,34% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 2 | 0,00% | -0,90% | +0,90% | -2,23% | +2,76% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 23 | 47,83% | +0,57% | +0,57% | -3,22% | +4,29% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 18 | 22,22% | -0,67% | +0,29% | -2,87% | +4,14% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 14 | 64,29% | +1,49% | +1,49% | -3,07% | +5,70% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 11 | 45,45% | -0,46% | -0,01% | -2,60% | +4,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 27 | 37,04% | -0,44% | +0,44% | -0,04% | +1,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 41 | 56,10% | +0,60% | +0,31% | -0,21% | +1,00% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +3,06% | +3,69% | +2,25% | +3,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 34 | 52,94% | +0,44% | +0,19% | -0,35% | +0,79% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 27 | 44,44% | -1,08% | +1,08% | +0,40% | +2,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 40 | 50,00% | +0,64% | +0,40% | -0,26% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 33 | 60,61% | +0,28% | -0,28% | -0,87% | +0,59% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 26 | 34,62% | -0,93% | +0,93% | -1,60% | +3,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 39 | 51,28% | +0,58% | +0,26% | -1,74% | +2,38% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 33 | 48,48% | +0,25% | -0,26% | -1,90% | +1,81% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -0,44% | +0,44% | -2,47% | +3,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 37 | 51,35% | +0,76% | +0,07% | -2,54% | +2,88% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 32 | 65,62% | +1,47% | +0,07% | -2,76% | +2,83% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 23 | 52,17% | +0,04% | -0,04% | -3,05% | +3,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 35 | 57,14% | +0,86% | -0,36% | -3,04% | +3,04% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 30 | 63,33% | +1,05% | -1,05% | -3,36% | +2,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 22 | 59,09% | +1,13% | -1,13% | -3,71% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +1,35% | -0,51% | -3,58% | +3,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 30 | 66,67% | +1,40% | -1,40% | -3,88% | +2,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 21 | 66,67% | +1,05% | -1,05% | -4,58% | +3,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 30 | 66,67% | +2,07% | -1,06% | -4,43% | +3,57% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 3 | 66,67% | -6,24% | +6,85% | -1,27% | +10,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 29 | 68,97% | +1,32% | -1,32% | -4,53% | +3,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 19 | 78,95% | +1,48% | -1,48% | -5,33% | +4,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 23 | 78,26% | +3,25% | -1,89% | -5,53% | +3,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 23 | 82,61% | +1,89% | -1,89% | -5,53% | +3,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 13 | 84,62% | +2,07% | -2,07% | -6,54% | +3,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 14 | 85,71% | +2,36% | -2,36% | -6,65% | +3,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 14 | 85,71% | +2,36% | -2,36% | -6,65% | +3,35% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 22 | 50,00% | +0,21% | +0,29% | -0,37% | +0,83% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 36 | 61,11% | +0,34% | +0,10% | -0,37% | +0,72% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 38 | 50,00% | +0,08% | +0,12% | -0,43% | +0,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 36 | 52,78% | +0,77% | +0,64% | -0,12% | +1,36% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 37 | 37,84% | -0,57% | +0,26% | -0,40% | +1,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 35 | 48,57% | +0,89% | +0,67% | -1,96% | +2,46% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 37 | 40,54% | -1,05% | +0,73% | -1,85% | +2,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 33 | 54,55% | +0,93% | +0,72% | -2,75% | +3,17% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 35 | 42,86% | -1,17% | +0,70% | -2,76% | +3,33% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 31 | 61,29% | +0,97% | +0,22% | -3,26% | +3,26% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 33 | 36,36% | -0,86% | +0,24% | -3,30% | +3,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 30 | 63,33% | +1,58% | +0,86% | -3,78% | +4,05% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,22% | +0,07% | -3,88% | +3,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 26 | 80,77% | +2,57% | +1,13% | -4,47% | +4,82% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 30 | 36,67% | -1,21% | +0,54% | -4,49% | +4,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 15 | 53,33% | -2,32% | +2,32% | -6,02% | +5,58% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 19 | 73,68% | +3,34% | +0,40% | -6,51% | +4,59% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 23 | 52,17% | -1,80% | +0,01% | -6,47% | +4,45% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 6 | 33,33% | -2,65% | +2,65% | -6,95% | +6,02% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 10 | 70,00% | +0,05% | +1,10% | -8,09% | +4,84% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 14 | 28,57% | -2,26% | +0,92% | -7,74% | +4,55% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 39 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 41 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 25 | 16,00% | -0,97% |
| BTC | BREVE | Famiglia statistica | 120 | 55,83% | +0,64% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 105 | 35,24% | -0,47% |
| BTC | SETTIMANALE | Classic technical | 16 | 6,25% | -4,33% |
| BTC | SETTIMANALE | Famiglia statistica | 106 | 48,11% | +0,69% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 91 | 34,07% | -0,92% |
| BTC | SWING | Classic technical | 6 | 33,33% | -0,48% |
| BTC | SWING | Famiglia statistica | 53 | 49,06% | +0,66% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 43 | 44,19% | +0,34% |
| BTC | MEDIO | Famiglia statistica | 14 | 64,29% | +1,49% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 11 | 45,45% | -0,46% |
| DOGE | BREVE | Classic technical | 80 | 38,75% | -0,81% |
| DOGE | BREVE | Famiglia statistica | 120 | 52,50% | +0,61% |
| DOGE | BREVE | Microstruttura exchange | 13 | 53,85% | +2,30% |
| DOGE | BREVE | Tecnico | 100 | 54,00% | +0,32% |
| DOGE | SETTIMANALE | Classic technical | 69 | 53,62% | +0,22% |
| DOGE | SETTIMANALE | Famiglia statistica | 106 | 54,72% | +0,98% |
| DOGE | SETTIMANALE | Microstruttura exchange | 12 | 58,33% | +0,26% |
| DOGE | SETTIMANALE | Tecnico | 92 | 65,22% | +1,31% |
| DOGE | SWING | Classic technical | 40 | 72,50% | +1,26% |
| DOGE | SWING | Famiglia statistica | 53 | 71,70% | +2,58% |
| DOGE | SWING | Microstruttura exchange | 5 | 80,00% | -3,44% |
| DOGE | SWING | Tecnico | 52 | 75,00% | +1,57% |
| DOGE | MEDIO | Classic technical | 13 | 84,62% | +2,07% |
| DOGE | MEDIO | Famiglia statistica | 14 | 85,71% | +2,36% |
| DOGE | MEDIO | Tecnico | 14 | 85,71% | +2,36% |
| SOL | BREVE | Classic technical | 64 | 46,88% | +0,02% |
| SOL | BREVE | Famiglia statistica | 107 | 54,21% | +0,67% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 112 | 42,86% | -0,51% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 94 | 59,57% | +1,15% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 100 | 42,00% | -0,76% |
| SOL | SWING | Classic technical | 36 | 44,44% | -1,66% |
| SOL | SWING | Famiglia statistica | 45 | 77,78% | +2,90% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 53 | 43,40% | -1,47% |
| SOL | MEDIO | Classic technical | 6 | 33,33% | -2,65% |
| SOL | MEDIO | Famiglia statistica | 10 | 70,00% | +0,05% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 14 | 28,57% | -2,26% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 12 | in attesa di controlli maturati |
| SOL | MEDIO | 10 | in attesa di controlli maturati |
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
| BTC     |         42 |              14 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         42 |              14 |          28 | RACCOLTA DATI | 7,14%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         42 |              14 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| SOL     | MEDIO          | MOLTO ALTO     | leva moderata possibile solo con stop e margine                         |
| DOGE    | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-21 05:32 UTC


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
| BTC | +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910. | Sotto 62.488 il quadro tecnico peggiora. |
| SOL | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Adam and Eve Bottom attivo finché mantiene 83,81; nuova conferma tecnica sopra 98,27; milestone analogiche 96,13 / 111,09, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 84,46 / 74,20 / 62,19. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.09169 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +5 |
| SOL | -1 | 0 | -1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +2 |
| DOGE | +1 | 0 | +1 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 57,50%, return centrale 30g +2,70%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 40. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 11/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 12/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati -0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: cambiamento medio in misto rispetto a ieri.

Conferme: Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 47,50%, return centrale 30g -0,88%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 40. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 11/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +1 (rialzista Adam and Eve Bottom / ATTIVO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 11/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +61,09%, aderenza live +70,11%, errore live +14,95%, gap corrente -0,97%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 36, ma percorso ancorato non aderente: gap -0,97%, errore live +14,95%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,42 $, upside EMA200 +24,26%, gap EMA50/EMA200 -5,93%, hit EMA200 12w +46,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza ALTA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Adam and Eve Bottom attivo finché mantiene 83,81; nuova conferma tecnica sopra 98,27; milestone analogiche 96,13 / 111,09, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 84,46 / 74,20 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 55,00%, return centrale 30g +1,88%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 40. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 5/12, verdetto costruttivo ma non confermato, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score +1 (rialzista Triplo minimo / ATTIVO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 3/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 0, bear 3, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza ALTA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — DOGE: cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.09169 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-08-21 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 75.089 $ | prezzo corrente |
| Power Law centrale | 123.866 $ | deviazione -39,38% |
| Banda p10-p90 | 76.761 $ / 312.451 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 8,03% | posizione storica nel corridoio |
| Esponente β | 5,8153 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3163 cambiando finestra |
| Ultimo halving | 2024-04-19 | 854 giorni fa |
| Fase ciclo | 58,45% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-21 (4356 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1524) × giorni^5.8153
- Prezzo centrale oggi: **123.866 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 8,03%
- Scarto dal centro: **-39,38%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8153 | 91,93% |
| 2015 | 5,8989 | 91,48% |
| 2016 | 5,5843 | 87,72% |
| 2017 | 4,8545 | 82,85% |
| 2018 | 4,5826 | 78,32% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-08 | -19,62% | -13,53% | -6,05% | +59,95% |
| 2016-07-09 → 2020-05-11 | 2018-10-07 | -2,15% | -41,77% | -23,72% | +24,88% |
| 2020-05-11 → 2024-04-19 | 2022-08-30 | -1,13% | -18,08% | +19,02% | +37,89% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | 1.4991497417394362 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -3 | 0 | -0.2792417760480559 | 0 |

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

Generato: 2026-08-21 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00119160 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +1,50% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000110 | -3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -0,28% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

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
- **Rendimenti relativi:** 7g -0,78%; 30g +1,50%; 90g +6,68%; 180g -4,90%
- **Daily:** RSI 52.57; MA50 0.00119293; MA200 0.00117840
- **Weekly:** MA30 0.00118232; RSI 47.57
- **Livelli:** supporto 0.00116400; resistenza 0.00119500; breakout 60g 0.00134900; breakdown 60g 0.00108800
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
- **Rendimenti relativi:** 7g -0,60%; 30g -0,28%; 90g -18,88%; 180g -24,12%
- **Daily:** RSI 48.20; MA50 0.00000112; MA200 0.00000129
- **Weekly:** MA30 0.00000129; RSI 32.83
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000139; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
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
| SOL | 1g | 18 | 55,56% | -0,37% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 16 | 43,75% | -0,67% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 16 | 37,50% | -1,43% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 14 | 7,14% | -3,10% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 35 | 68,57% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 34 | 61,76% | +0,57% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 33 | 69,70% | +0,95% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 28 | 75,00% | +1,39% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 12 | 100,00% | +3,08% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **21 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +61,09%
- **Somiglianza strutturale:** +61,09%
- **Aderenza prezzo live:** +70,11%
- **Errore medio live:** +14,95%
- **Gap prezzo corrente:** -0,97%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 76 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-05
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima retest / debolezza, poi recupero.** Zona bassa **84,46 $** intorno al **26 agosto 2026**; zona alta **96,13 $** intorno al **3 settembre 2026**; fine step circa **94,90 $** entro il **4 settembre 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 21 agosto 2026 | 50 | +70,11% | +14,95% | -0,97% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 21 agosto 2026 | 77 | +76,37% | +11,82% | -0,97% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +70,11% | Errore medio live +14,95%. |
| Gap corrente | -0,97% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 96,13 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 111,09 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 84,46 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 486,66 $ |
| Massimo percorso base | 486,66 $ (21 aprile 2029) |

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
| Prima conferma | 96,13 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 111,09 $ | Scenario più credibile. |
| Invalidazione soft | 84,46 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 28 agosto 2026 | -5,09% | 85,00 $ | 84,46 $ | 90,75 $ |
| 14 giorni | 4 settembre 2026 | +5,98% | 94,90 $ | 84,46 $ | 96,13 $ |
| 30 giorni | 20 settembre 2026 | -3,21% | 86,68 $ | 84,46 $ | 96,86 $ |
| 60 giorni | 20 ottobre 2026 | +22,17% | 109,40 $ | 78,75 $ | 111,09 $ |
| 90 giorni | 19 novembre 2026 | +25,91% | 112,76 $ | 78,75 $ | 118,92 $ |
| 120 giorni | 19 dicembre 2026 | +12,22% | 100,49 $ | 78,75 $ | 118,92 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 21 agosto 2026 -> 4 settembre 2026 | +5,98% | 84,46 $ (26 agosto 2026) | 96,13 $ (3 settembre 2026) | 94,90 $ | Prima retest / debolezza, poi recupero. |
| Step 2 - primo mese | 5 settembre 2026 -> 20 settembre 2026 | -3,21% | 86,68 $ (20 settembre 2026) | 96,86 $ (5 settembre 2026) | 86,68 $ | Prima spike, poi scarico. |
| Step 3 - secondo mese | 21 settembre 2026 -> 20 ottobre 2026 | +22,17% | 78,75 $ (23 settembre 2026) | 111,09 $ (14 ottobre 2026) | 109,40 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 21 ottobre 2026 -> 19 novembre 2026 | +25,91% | 106,41 $ (4 novembre 2026) | 118,92 $ (28 ottobre 2026) | 112,76 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 89,55 $ |  |
| Weekly RSI | 51,15 / linea grezza 52,95 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 44,19 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 486,66 $ | Avanzamento +18,40% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 44,2, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | 4 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Prezzo SOL | 89,55 $ |
| TVL Solana | 5,34 mld $ |
| TVL 7g | +10,44% |
| DEX volume 24h | 2,78 mld $ |
| Fees 24h | 11,03 mln $ |
| Stablecoin su Solana | 16,45 mld $ |
| Stake ratio | 68,81% |
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
| Confronto precedente | 2026-08-17 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 89,55 $ |
| EMA200 weekly target | 111,42 $ |
| Upside verso EMA200 | +24,26% |
| Distanza prezzo da EMA200 | -19,52% |
| Gap EMA50/EMA200 | -5,93% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 51,22 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +46,67% |
| Max gain mediano 12w | +17,93% |
| Drawdown mediano 12w | -31,98% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-21 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-21 05:30:23 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante, ma lettura mista.
- SOL: cambiamento importante in peggioramento rispetto a ieri.
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | misto | NEUTRALE / INCERTO | +57.50% | 0.00 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | NEUTRALE / INCERTO | +47.50% | -2.50 punti |
| DOGE | CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +55.00% | -12.50 punti |

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
| BTC | 71.377 $ | 82.647 $ | +40,91% | +15,79% | rimbalzo debole | 82.647 $ | 71.377 $ | +29,63% | -13,64% | spike storicamente più resistente |
| SOL | 85,07 $ | 98,51 $ | +36,00% | +15,79% | rimbalzo debole | 98,51 $ | 85,07 $ | +25,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07826 $ | 0,09062 $ | +46,67% | +15,79% | rimbalzo debole | 0,09062 $ | 0,07826 $ | +25,00% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 22 prima sono scesi a -5,00%. Tra quei 22, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +40,91% (9/22). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 8 poi sono scaricati a -5,00%. Percentuale: +29,63% (8/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +36,00% (9/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 6 poi sono scaricati a -5,00%. Percentuale: +25,00% (6/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +46,67% (14/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 7 poi sono scaricati a -5,00%. Percentuale: +25,00% (7/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-21 05:31:40 UTC


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

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g     | P90 30g      |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:------------|:-------------|
| BTC | 2026-08-21 | 75.133 $ | INCERTO | 57,50% | 65.415,73 $ | 69.469,30 $ | 77.160,87 $ | 84.903,57 $ | 103.830,27 $ |
| SOL | 2026-08-21 | 89,55 $ | INCERTO | 47,50% | 78,24 $ | 83,56 $ | 88,77 $ | 103,62 $ | 151,10 $ |
| DOGE | 2026-08-21 | 0.08238 $ | INCERTO | 55,00% | 0.05668 $ | 0.07029 $ | 0.08393 $ | 0.09693 $ | 0.12238 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-22**; verificato fino al **2026-08-21**; stato **COMPLETO 30/30g**.
- Reale **75.109,19 $**; p50 previsto **72.439,47 $**; scarto **3,69%**.
- Errore medio assoluto **2,96%**; massimo **8,39%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-22**; verificato fino al **2026-08-21**; stato **COMPLETO 30/30g**.
- Reale **89,61 $**; p50 previsto **77,12 $**; scarto **16,20%**.
- Errore medio assoluto **4,00%**; massimo **17,15%**; DENTRO p10-p90; FUORI p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-22**; verificato fino al **2026-08-21**; stato **COMPLETO 30/30g**.
- Reale **0.08247 $**; p50 previsto **0.06749 $**; scarto **22,20%**.
- Errore medio assoluto **3,59%**; massimo **22,20%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 40 | 92,50% | 57,50% | 2,28% | 0,72% |
| BTC | 3g | 38 | 92,11% | 73,68% | 2,91% | 0,50% |
| BTC | 7g | 34 | 100,00% | 82,35% | 3,21% | 0,04% |
| BTC | 14g | 29 | 100,00% | 82,76% | 3,58% | 0,27% |
| BTC | 30g | 13 | 100,00% | 92,31% | 6,23% | -3,93% |
| SOL | 1g | 40 | 77,50% | 60,00% | 2,70% | 0,67% |
| SOL | 3g | 38 | 92,11% | 73,68% | 3,09% | 0,24% |
| SOL | 7g | 34 | 100,00% | 88,24% | 2,46% | 0,26% |
| SOL | 14g | 29 | 93,10% | 82,76% | 3,78% | 2,50% |
| SOL | 30g | 13 | 100,00% | 76,92% | 4,63% | 3,63% |
| DOGE | 1g | 40 | 90,00% | 62,50% | 2,97% | 1,02% |
| DOGE | 3g | 38 | 94,74% | 81,58% | 2,95% | 1,53% |
| DOGE | 7g | 34 | 91,18% | 88,24% | 5,51% | 3,69% |
| DOGE | 14g | 29 | 93,10% | 65,52% | 7,86% | 6,46% |
| DOGE | 30g | 13 | 100,00% | 46,15% | 15,14% | 15,14% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **114**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-21 | BTC | 75.133 $ | INCERTO | 57,50% | 77.161 $ | 69.707 $ | 88.009 $ | 2026-09-20 |
| 2026-08-21 | DOGE | 0,08000 $ | INCERTO | 55,00% | 0,08000 $ | 0,07000 $ | 0,10000 $ | 2026-09-20 |
| 2026-08-21 | SOL | 89,55 $ | INCERTO | 47,50% | 88,77 $ | 82,16 $ | 100,09 $ | 2026-09-20 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-21 05:31 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +52,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **57,50%**
- Casi negativi / discesa storica: **42,50%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **75.133,45 $**
- Return normale fra 30 giorni: **77.160,87 $** (2,70%)
- Drawdown normale durante il mese: **69.706,56 $** (-7,22%)
- Drawdown brutto da rispettare: **65.044,26 $** (-13,43%)
- Max gain normale durante il mese: **88.008,89 $** (17,14%)
- Max gain buono / take profit ottimistico: **95.944,13 $** (27,70%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **47,50%**
- Casi negativi / discesa storica: **52,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **89,55 $**
- Return normale fra 30 giorni: **88,77 $** (-0,88%)
- Drawdown normale durante il mese: **82,16 $** (-8,26%)
- Drawdown brutto da rispettare: **78,63 $** (-12,19%)
- Max gain normale durante il mese: **100,09 $** (11,77%)
- Max gain buono / take profit ottimistico: **111,74 $** (24,78%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **55,00%**
- Casi negativi / discesa storica: **45,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,08 $** (1,88%)
- Drawdown normale durante il mese: **0,07 $** (-12,04%)
- Drawdown brutto da rispettare: **0,07 $** (-20,96%)
- Max gain normale durante il mese: **0,10 $** (17,97%)
- Max gain buono / take profit ottimistico: **0,11 $** (34,37%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 75.133,45 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **57,50%**
- Probabilità storica di discesa: **42,50%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale debole. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **65.415,73 $** (-12,93%)
- Se va male: **69.469,30 $** (-7,54%)
- Scenario normale: **77.160,87 $** (2,70%)
- Se va bene: **84.903,57 $** (13,00%)
- Se va molto bene: **103.830,27 $** (38,19%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **69.706,56 $** (-7,22%)
- Discesa brutta: **65.044,26 $** (-13,43%)
- Discesa molto brutta: **62.666,39 $** (-16,59%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **88.008,89 $** (17,14%)
- Rialzo buono: **95.944,13 $** (27,70%)
- Rialzo molto forte: **113.960,07 $** (51,68%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **69.706,56 $** e uno spike normale intorno a **88.008,89 $**.

La chiusura a 30 giorni è incerta: salita 57,50%, discesa 42,50%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 89,55 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **47,50%**
- Probabilità storica di discesa: **52,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **78,24 $** (-12,63%)
- Se va male: **83,56 $** (-6,69%)
- Scenario normale: **88,77 $** (-0,88%)
- Se va bene: **103,62 $** (15,71%)
- Se va molto bene: **151,10 $** (68,73%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **82,16 $** (-8,26%)
- Discesa brutta: **78,63 $** (-12,19%)
- Discesa molto brutta: **76,62 $** (-14,44%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **100,09 $** (11,77%)
- Rialzo buono: **111,74 $** (24,78%)
- Rialzo molto forte: **152,60 $** (70,41%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **82,16 $** e uno spike normale intorno a **100,09 $**.

La chiusura a 30 giorni è incerta: salita 47,50%, discesa 52,50%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,08 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **55,00%**
- Probabilità storica di discesa: **45,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,06 $** (-31,20%)
- Se va male: **0,07 $** (-14,68%)
- Scenario normale: **0,08 $** (1,88%)
- Se va bene: **0,10 $** (17,67%)
- Se va molto bene: **0,12 $** (48,56%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-12,04%)
- Discesa brutta: **0,07 $** (-20,96%)
- Discesa molto brutta: **0,06 $** (-33,08%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (17,97%)
- Rialzo buono: **0,11 $** (34,37%)
- Rialzo molto forte: **0,12 $** (51,07%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni è incerta: salita 55,00%, discesa 45,00%. Non c'è un vantaggio netto.

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

- Previsioni già controllate: **20**
- Direzione corretta: **76,92%**
- Errore medio dello scenario centrale: **4,78%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **20**
- Direzione corretta: **90,00%**
- Errore medio dello scenario centrale: **12,60%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **20**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **4,38%**
- Zona rischio toccata: **10,00%**
- Zona rialzo media toccata: **5,00%**
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

Dati ancora insufficienti: previsioni controllate **20** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **20** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **20** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 75.133,45 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **57,50%**
- Casi negativi dopo 30 giorni: **42,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **82,08%**
- Rendimento medio dopo 30 giorni: **9,92%**
- Rendimento centrale dopo 30 giorni: **2,70%**
- Discesa media durante i 30 giorni: **-9,12%**
- Massimo rialzo medio durante i 30 giorni: **25,18%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **82.586,69 $**
- Scenario centrale a 30 giorni: **77.160,87 $**
- Zona di rischio media: **68.284,16 $**
- Zona di rialzo media: **94.055,13 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,93% → **65.415,73 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,54% → **69.469,30 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 2,70% → **77.160,87 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 13,00% → **84.903,57 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 38,19% → **103.830,27 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -16,59% → **62.666,39 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -13,43% → **65.044,26 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,22% → **69.706,56 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,26% → **72.685,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,82% → **74.513,74 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,95% → **78.853,22 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,80% → **81.744,58 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,14% → **88.008,89 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 27,70% → **95.944,13 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 51,68% → **113.960,07 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-08-14   | 2020-11-21 |        88.96 |        53.46 |          -4.5  |          90.41 |
| XRP-USD         | 2023-07-25   | 2023-11-01 |        86.2  |         0.55 |          -4.77 |          17.39 |
| LTC-USD         | 2023-07-25   | 2023-11-01 |        85.77 |         2.3  |          -4.97 |           7.49 |
| THETA-USD       | 2022-04-20   | 2022-07-28 |        85.01 |       -16.53 |         -16.53 |          23.44 |
| ETC-USD         | 2020-08-14   | 2020-11-21 |        84.6  |        -6.61 |         -12.09 |          10.56 |
| LTC-USD         | 2018-10-29   | 2019-02-05 |        83.67 |        66.94 |          -3.86 |          66.94 |
| NEO-USD         | 2018-10-29   | 2019-02-05 |        83.5  |        30.74 |          -2.98 |          44    |
| BNB-USD         | 2018-10-29   | 2019-02-05 |        83.23 |        93.69 |          -1.14 |          93.69 |
| SOL-USD         | 2026-01-13   | 2026-04-22 |        83.2  |        -3    |          -4.48 |          12.01 |
| ETH-USD         | 2026-01-10   | 2026-04-19 |        83.16 |        -6.84 |          -6.84 |           4.91 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 89,55 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **47,50%**
- Casi negativi dopo 30 giorni: **52,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **74,40%**
- Rendimento medio dopo 30 giorni: **26,83%**
- Rendimento centrale dopo 30 giorni: **-0,88%**
- Discesa media durante i 30 giorni: **-8,13%**
- Massimo rialzo medio durante i 30 giorni: **40,65%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **113,58 $**
- Scenario centrale a 30 giorni: **88,77 $**
- Zona di rischio media: **82,27 $**
- Zona di rialzo media: **125,95 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,63% → **78,24 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -6,69% → **83,56 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -0,88% → **88,77 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 15,71% → **103,62 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 68,73% → **151,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -14,44% → **76,62 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,19% → **78,63 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,26% → **82,16 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,01% → **85,96 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,45% → **89,14 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,88% → **91,24 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,51% → **95,38 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,77% → **100,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,78% → **111,74 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 70,41% → **152,60 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| EOS-USD         | 2018-11-13   | 2019-02-20 |        82.18 |        -6.92 |         -16.43 |           8.85 |
| ONE-USD         | 2020-02-21   | 2020-05-30 |        78.94 |       -22.17 |         -28.41 |           0.73 |
| BNB-USD         | 2020-02-21   | 2020-05-30 |        78.52 |       -12.61 |         -14.42 |           0.97 |
| VET-USD         | 2020-02-18   | 2020-05-27 |        78.27 |        82.11 |           0    |          98.84 |
| ATOM-USD        | 2020-02-21   | 2020-05-30 |        77.96 |        -5.94 |         -13.19 |          11.96 |
| ZIL-USD         | 2020-08-11   | 2020-11-18 |        77.78 |       101.63 |          -2.99 |         101.63 |
| EOS-USD         | 2020-02-21   | 2020-05-30 |        77.54 |       -13.99 |         -14.92 |           2.21 |
| MKR-USD         | 2020-02-22   | 2020-05-31 |        77.39 |        -1.14 |          -7.47 |          49.98 |
| QTUM-USD        | 2020-02-21   | 2020-05-30 |        76.81 |        -7.01 |         -11.63 |           4.96 |
| ALGO-USD        | 2020-02-20   | 2020-05-29 |        76.64 |        -9.13 |         -10.1  |           8.93 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,08 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **55,00%**
- Casi negativi dopo 30 giorni: **45,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,31%**
- Rendimento medio dopo 30 giorni: **6,81%**
- Rendimento centrale dopo 30 giorni: **1,88%**
- Discesa media durante i 30 giorni: **-14,21%**
- Massimo rialzo medio durante i 30 giorni: **27,89%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -31,20% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -14,68% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 1,88% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 17,67% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 48,56% → **0,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,08% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -20,96% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,04% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,52% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,44% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,52% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,97% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 34,37% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 51,07% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| OP-USD          | 2026-01-11   | 2026-04-20 |        89.34 |         3.89 |          -3.44 |          39.02 |
| SAND-USD        | 2025-01-14   | 2025-04-23 |        88.18 |         3.56 |          -8.98 |          23.97 |
| SNX-USD         | 2025-10-12   | 2026-01-19 |        87.71 |       -32.4  |         -36.26 |           0    |
| DOGE-USD        | 2025-01-15   | 2025-04-24 |        87.26 |        23.48 |          -6.52 |          36.3  |
| HBAR-USD        | 2020-08-16   | 2020-11-23 |        86.54 |       -12.5  |         -12.5  |          13.17 |
| CHZ-USD         | 2020-08-13   | 2020-11-20 |        86.06 |        44.67 |           0    |          47.97 |
| ALGO-USD        | 2025-01-14   | 2025-04-23 |        85.99 |         4.6  |          -6.82 |          18.34 |
| XTZ-USD         | 2020-08-14   | 2020-11-21 |        85.34 |        -7.78 |         -12.24 |          12.32 |
| KSM-USD         | 2022-04-19   | 2022-07-27 |        85.34 |       -28.63 |         -28.63 |           6.88 |
| BNB-USD         | 2025-10-07   | 2026-01-14 |        84.99 |       -34.77 |         -36.09 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-21 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | DISTRIBUTION | 75.133 $ | True | -2.04% | -9.92% | DISTRIBUTION | -2.04% | -9.92% |
| DOGE-USD | BEAR | 0.08238 $ | False | -19.92% | -16.43% | DISTRIBUTION | -2.04% | -9.92% |
| SOL-USD | MIXED | 89,55 $ | True | 4.65% | -16.34% | DISTRIBUTION | -2.04% | -9.92% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 2.70% | 13.00% | 38.19% | -7.22% | -16.59% | 17.14% | 27.70% | 51.68% | 60.00% | 17.04% | 48.22% | 145.84% |
| BTC-USD | SAME_BTC_REGIME | 1 | 100.00% | 30.61% | 30.61% | 30.61% | -14.39% | -14.39% | 37.23% | 37.23% | 37.23% | 100.00% | 66.62% | 66.62% | 66.62% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 50.00% | -14.77% | -5.84% | -0.48% | -18.59% | -30.78% | 19.63% | 26.18% | 30.11% | 0.00% | -25.57% | -17.40% | -12.51% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 1.88% | 17.67% | 48.56% | -12.04% | -33.08% | 17.97% | 34.37% | 51.07% | 32.50% | -11.43% | 18.09% | 114.31% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -32.40% | -32.40% | -32.40% | -36.26% | -36.26% | 0.00% | 0.00% | 0.00% | 0.00% | -27.09% | -27.09% | -27.09% |
| DOGE-USD | SAME_ASSET_REGIME | 12 | 66.67% | 23.37% | 38.37% | 49.34% | -8.63% | -27.89% | 34.74% | 48.71% | 64.10% | 41.67% | -7.05% | 51.37% | 82.07% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 47.50% | -0.88% | 15.71% | 68.73% | -8.26% | -14.44% | 11.77% | 24.78% | 70.41% | 75.00% | 29.19% | 58.98% | 187.89% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 55.56% | 1.84% | -3.61% | 30.84% | 44.44% | -10.51% | 53.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 15 | 80.00% | 8.41% | -12.16% | 23.74% | 80.00% | 23.22% | 115.39% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 0.00% | -10.93% | -12.48% | 23.59% | 50.00% | 9.44% | 45.87% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 14 | 71.43% | 9.93% | -12.82% | 38.13% | 28.57% | -11.83% | 45.03% |
| DOGE-USD | HISTORICAL_BTC_BULL | 24 | 50.00% | -1.64% | -10.97% | 21.46% | 37.50% | -11.43% | 44.31% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -32.40% | -36.26% | 0.00% | 0.00% | -27.09% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -4.88% | 65.73% | 0.00% | -4.17% | 65.73% |
| SOL-USD | HISTORICAL_BTC_BEAR | 9 | 55.56% | 3.09% | -4.66% | 49.47% | 44.44% | -9.24% | 112.24% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 14.83% | -2.99% | 65.24% | 71.43% | 30.01% | 248.94% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 24 | 37.50% | -2.84% | -9.82% | 17.14% | 87.50% | 30.22% | 58.76% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 60.00% | 4.05% | -4.10% | 28.19% | 55.00% | 13.11% | 64.08% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 77.78% | 9.47% | -12.20% | 26.02% | 66.67% | 29.10% | 191.62% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.77% | -18.59% | 26.18% | 0.00% | -25.57% | 27.75% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 33.33% | -6.61% | -11.63% | 15.31% | 77.78% | 23.44% | 69.53% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 12 | 66.67% | 23.37% | -8.63% | 48.71% | 41.67% | -7.05% | 73.07% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 20 | 55.00% | 1.41% | -8.71% | 23.91% | 35.00% | -10.25% | 29.87% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 6.99% | -17.49% | 31.76% | 0.00% | -3.55% | 31.76% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -10.00% | -20.85% | 9.07% | 14.29% | -27.09% | 11.37% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 13 | 53.85% | 0.30% | -8.51% | 25.50% | 53.85% | 14.57% | 114.84% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 16.59% | -2.96% | 83.43% | 83.33% | 126.54% | 280.55% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.09% | -3.35% | 6.53% | 0.00% | -9.24% | 12.81% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 20 | 30.00% | -5.89% | -9.66% | 12.27% | 90.00% | 26.18% | 51.61% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | DOT-USD | 2024-07-14 | 79.24% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 30.61% | -14.39% | 37.23% | 66.62% | -14.39% | 144.58% |
| BTC-USD | BNB-USD | 2026-01-15 | 82.46% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |
| BTC-USD | MANA-USD | 2018-07-21 | 80.11% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | BEARISH_30D | -32.64% | -33.83% | 32.73% | -41.90% | -44.09% | 32.73% |
| BTC-USD | XLM-USD | 2020-08-14 | 88.96% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | XRP-USD | 2023-07-25 | 86.20% | BULL | BULL | DIFFERENT | MIXED | 0.55% | -4.77% | 17.39% | 0.89% | -4.77% | 17.39% |
| BTC-USD | LTC-USD | 2023-07-25 | 85.77% | BULL | RECOVERY | DIFFERENT | MIXED | 2.30% | -4.97% | 7.49% | 4.09% | -4.97% | 12.10% |
| BTC-USD | THETA-USD | 2022-04-20 | 85.01% | RECOVERY | BEAR | DIFFERENT | BEARISH_30D | -16.53% | -16.53% | 23.44% | -18.80% | -23.27% | 23.44% |
| BTC-USD | ETC-USD | 2020-08-14 | 84.60% | BULL | RECOVERY | DIFFERENT | MIXED | -6.61% | -12.09% | 10.56% | 20.57% | -22.64% | 35.47% |
| BTC-USD | LTC-USD | 2018-10-29 | 83.67% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 66.94% | -3.86% | 66.94% | 170.23% | -3.86% | 170.23% |
| BTC-USD | NEO-USD | 2018-10-29 | 83.50% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 30.74% | -2.98% | 44.00% | 85.04% | -2.98% | 91.46% |
| DOGE-USD | SNX-USD | 2025-10-12 | 87.71% | DISTRIBUTION | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -32.40% | -36.26% | 0.00% | -27.09% | -36.26% | 0.00% |
| DOGE-USD | OP-USD | 2026-01-11 | 89.34% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | KSM-USD | 2022-04-19 | 85.34% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.63% | -28.63% | 6.88% | -34.98% | -36.50% | 6.88% |
| DOGE-USD | OMG-USD | 2025-10-07 | 84.90% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -31.06% | -32.57% | 0.00% | -31.91% | -34.94% | 0.00% |
| DOGE-USD | SOL-USD | 2022-04-19 | 84.40% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.29% | -21.29% | 15.33% | -19.78% | -24.60% | 15.33% |
| DOGE-USD | FTM-USD | 2022-04-01 | 83.69% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 35.00% | -16.51% | 35.47% | -9.93% | -16.51% | 45.15% |
| DOGE-USD | EGLD-USD | 2023-07-10 | 83.67% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 79.03% | -3.32% | 97.30% | 150.60% | -3.32% | 166.35% |
| DOGE-USD | ATOM-USD | 2022-04-01 | 83.66% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 31.00% | -13.26% | 31.00% | 44.09% | -13.26% | 44.68% |
| DOGE-USD | VET-USD | 2022-04-03 | 83.44% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 48.46% | -2.52% | 48.46% | 16.58% | -2.52% | 51.72% |
| DOGE-USD | DOT-USD | 2023-07-25 | 83.35% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 15.73% | -2.44% | 20.65% | 73.20% | -2.44% | 95.07% |
| SOL-USD | EOS-USD | 2018-11-13 | 82.18% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -6.92% | -16.43% | 8.85% | 33.78% | -16.43% | 48.92% |
| SOL-USD | ONE-USD | 2020-02-21 | 78.94% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -22.17% | -28.41% | 0.73% | -4.55% | -28.41% | 0.73% |
| SOL-USD | BNB-USD | 2020-02-21 | 78.52% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -12.61% | -14.42% | 0.97% | 12.13% | -14.42% | 13.70% |
| SOL-USD | VET-USD | 2020-02-18 | 78.27% | RECOVERY | RECOVERY | DIFFERENT | EXPLOSIVE_60D | 82.11% | 0.00% | 98.84% | 258.30% | 0.00% | 308.84% |
| SOL-USD | ATOM-USD | 2020-02-21 | 77.96% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -5.94% | -13.19% | 11.96% | 29.45% | -13.19% | 55.17% |
| SOL-USD | ZIL-USD | 2020-08-11 | 77.78% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 101.63% | -2.99% | 101.63% | 237.58% | -2.99% | 312.16% |
| SOL-USD | EOS-USD | 2020-02-21 | 77.54% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -13.99% | -14.92% | 2.21% | 9.56% | -14.92% | 9.56% |
| SOL-USD | MKR-USD | 2020-02-22 | 77.39% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| SOL-USD | QTUM-USD | 2020-02-21 | 76.81% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -7.01% | -11.63% | 4.96% | 30.99% | -11.63% | 33.54% |
| SOL-USD | ALGO-USD | 2020-02-20 | 76.64% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -9.13% | -10.10% | 8.93% | 36.82% | -10.92% | 69.53% |

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

Generato: 2026-08-21 05:31 UTC


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
| BTC | 75.133 $ | +12 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 89,55 $ | +11 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.08238 $ | +3 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | +2 | +2 | +3 | +3 | 0 | +2 | +12 |
| SOL | -1 | +2 | +2 | +3 | +3 | 0 | +2 | +11 |
| DOGE | -4 | +2 | +2 | +3 | 0 | 0 | 0 | +3 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 74.959 $ | 75.988 $ | 66.910 $ | 57.748 $ | 2,32% | 13,00% | -0,44% |
| SOL | 85,25 $ | 90,67 $ | 83,81 $ | 64,42 $ | 2,82% | 14,76% | 6,33% |
| DOGE | 0.08189 $ | 0.08494 $ | 0.08795 $ | 0.06797 $ | 2,78% | 12,59% | -19,31% |

## Lettura dettagliata

### BTC

- Prezzo: **75.133 $**
- Score classico: **+12 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,32%; distanza supporto 0,26%; distanza resistenza 1,11%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 83.0; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.18; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 82.95 |
| MACD histogram | 943.00520 |
| CMF20 | 0.178 |
| Volume ratio 20 | 2.74 |
| MA20 | 64.697 $ |
| MA50 | 64.276 $ |
| MA100 | 66.183 $ |
| MA200 | 68.986 $ |
| Pendenza MA50 20g | +1,40% |
| Pendenza MA200 60g | -10,09% |
| Bollinger width | 15,07% |
| Bollinger position | 1.42 |

### SOL

- Prezzo: **89,55 $**
- Score classico: **+11 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 2,82%; distanza supporto 5,15%; distanza resistenza 1,15%

Dettaglio:

- Trend: **-1** — prezzo sopra MA200 daily; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 79.7; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.27; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 79.74 |
| MACD histogram | 1.38288 |
| CMF20 | 0.274 |
| Volume ratio 20 | 3.01 |
| MA20 | 76,09 $ |
| MA50 | 76,67 $ |
| MA100 | 76,32 $ |
| MA200 | 81,21 $ |
| Pendenza MA50 20g | +2,52% |
| Pendenza MA200 60g | -16,63% |
| Bollinger width | 18,73% |
| Bollinger position | 1.31 |

### DOGE

- Prezzo: **0.08238 $**
- Score classico: **+3 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,78%; distanza supporto 0,76%; distanza resistenza 2,95%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 76.2; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.22; rialzo con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 76.21 |
| MACD histogram | 0.00119 |
| CMF20 | 0.220 |
| Volume ratio 20 | 3.60 |
| MA20 | 0.07082 $ |
| MA50 | 0.07205 $ |
| MA100 | 0.08161 $ |
| MA200 | 0.08945 $ |
| Pendenza MA50 20g | -5,07% |
| Pendenza MA200 60g | -16,68% |
| Bollinger width | 14,72% |
| Bollinger position | 1.46 |

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

Generato: 2026-08-21 05:32 UTC


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
| BTC | 75.133 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 30,11% | Fib 61,8% TESTATO (0) @ 75.036 $ | BREAKOUT 60G | 74.959 $ |
| SOL | 89,55 $ | Adam and Eve Bottom | ATTIVO | rialzista | 2026-08-19 | 99,70 $ | 36,13% | n/a | Fib 61,8% TESTATO (0) @ 89,07 $ | BREAKOUT 60G | 83,52 $ |
| DOGE | 0.08238 $ | Triplo minimo | ATTIVO | rialzista | 2026-08-21 | 0.09012 $ | 28,90% | n/a | Fib 23,6% TESTATO (0) @ 0.08059 $ | NEL RANGE | 0.08157 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **12 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **30,11%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 61,8% TESTATO (0) @ 75.036 $** — Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 61.8% a 75.036; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **74.959 $**
- Resistenza: **75.988 $**
- Breakout 60g: **66.910 $**
- Breakdown 60g: **57.748 $**
- RSI14: **82.93**
- ATR14: **2,32%**
- Volume ratio 20g: **2.74**
- Rendimento 30g: **+12,97%**
- Rendimento 90g: **-0,47%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | ATTIVO | +1 | rialzista | 67.248 $ | 2026-08-19 | 2g | 76.748 $ | 83,00% | n/a | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: ATTIVO. Target teorico: 76.748 $; progresso: 83,00%; prezzo sopra neckline. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 20,74% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 12 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Adam and Eve Bottom**
- Stato pattern: **ATTIVO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-19 -> 2026-08-01**
- Età formazione: **20 giorni**
- Breakout pattern: **2026-08-19**
- Età breakout: **2 giorni**
- Neckline: **83,81 $**
- Target teorico: **99,70 $**
- Progresso verso target: **36,13%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 61,8% TESTATO (0) @ 89,07 $** — Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 61.8% a 89,07; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **82,13 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: ATTIVO. Target teorico: 99,70; progresso corrente: 36,13%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **83,52 $**
- Resistenza: **90,67 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **64,42 $**
- RSI14: **79.66**
- ATR14: **2,82%**
- Volume ratio 20g: **3.01**
- Rendimento 30g: **+14,65%**
- Rendimento 90g: **+6,22%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adam and Eve Bottom | ATTIVO | +1 | rialzista | 83,81 $ | 2026-08-19 | 2g | 99,70 $ | 36,13% | n/a | 82,13 $ | Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: ATTIVO. Target teorico: 99,70; progresso corrente: 36,13%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Testa e spalle inverso | ATTIVO | +1 | rialzista | 79,35 $ | 2026-08-19 | 2g | 94,28 $ | 68,31% | n/a | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: ATTIVO. Target teorico: 94,28 $; progresso: 68,31%; prezzo sopra neckline. |
| Doppio minimo | ATTIVO | +1 | rialzista | 83,81 $ | 2026-08-19 | 2g | 99,70 $ | 36,13% | n/a | 82,13 $ | Due minimi simili a 67,92 $ e 70,69 $. Neckline circa 83,81 $. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: ATTIVO. Target teorico: 99,70 $; progresso: 36,13%; prezzo sopra neckline. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 26,67% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 12 giorni. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo minimo**
- Stato pattern: **ATTIVO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-30 -> 2026-08-12**
- Età formazione: **9 giorni**
- Breakout pattern: **2026-08-21**
- Età breakout: **0 giorni**
- Neckline: **0.07923 $**
- Target teorico: **0.09012 $**
- Progresso verso target: **28,90%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 0.08059 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 23.6% a 0.08059; stato TESTATO; confluenza: neckline rialzista.
- Invalidazione: **0.07765 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-21 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.09012; progresso corrente: 28,90%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08157 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.08795 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **76.07**
- ATR14: **2,79%**
- Volume ratio 20g: **3.60**
- Rendimento 30g: **+12,42%**
- Rendimento 90g: **-19,44%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo minimo | ATTIVO | +1 | rialzista | 0.07923 $ | 2026-08-21 | 0g | 0.09012 $ | 28,90% | n/a | 0.07765 $ | Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-21 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.09012; progresso corrente: 28,90%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio minimo | ATTIVO | +1 | rialzista | 0.07923 $ | 2026-08-21 | 0g | 0.08952 $ | 30,59% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-21 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.08952 $; progresso: 30,59%; prezzo sopra neckline. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 21,20% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 10 giorni. |

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

Generato: 2026-08-21 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-21**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-05**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **89,55 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+61,09%**
- Aderenza live principale: **+70,11%**
- Errore medio live principale: **14,95%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **76**
- Osservazioni inclusive dal bottom: **77**
- Osservazioni da inizio programma/scanner: **50**
- Errore assoluto medio dal bottom: **11,82%**
- Errore assoluto medio da inizio programma: **14,95%**
- Gap firmato medio ultimi 7 giorni: **-12,23%**
- Errore assoluto medio ultimi 7 giorni: **12,23%**
- Gap ultimo giorno: **-0,97%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-0,97%**
- Gap firmato medio 7g: **-12,23%**
- Errore assoluto medio 7g: **12,23%**
- Variazione recente gap: **+15,72%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL e sotto il percorso ancorato ma sta recuperando**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 85,37 $ | 91,91 $ | -7,11% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 89,55 $ | 90,43 $ | -0,97% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-28 | 85,83 $ | 85,00 $ | 84,46 $ / 90,75 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-04 | 95,83 $ | 94,90 $ | 84,46 $ / 96,13 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-11 | 92,81 $ | 91,91 $ | 84,46 $ / 96,86 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-18 | 88,38 $ | 87,52 $ | 84,46 $ / 96,86 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-25 | 87,31 $ | 86,46 $ | 78,75 $ / 96,86 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-02 | 110,45 $ | 109,38 $ | 78,75 $ / 109,38 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-09 | 110,28 $ | 109,21 $ | 78,75 $ / 110,53 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-16 | 111,08 $ | 110,01 $ | 78,75 $ / 111,09 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-23 | 111,61 $ | 110,53 $ | 78,75 $ / 111,09 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-30 | 119,42 $ | 118,26 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-06 | 108,69 $ | 107,63 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-13 | 115,30 $ | 114,18 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-20 | 112,09 $ | 111,00 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-27 | 106,09 $ | 105,06 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-04 | 105,39 $ | 104,37 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-11 | 110,64 $ | 109,56 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-18 | 106,83 $ | 105,79 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-25 | 102,18 $ | 101,19 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 36 | 44,44% | 7,31% | 13,60% |
| 14g | 31 | 35,48% | 15,39% | 12,64% |
| 21g | 24 | 25,00% | 23,09% | 14,25% |
| 28g | 17 | 47,06% | 26,87% | 14,60% |
| 35g | 10 | 50,00% | 26,09% | 13,15% |
| 42g | 3 | 100,00% | 19,21% | 0,97% |
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

Ultima lettura salvata: **2026-08-21** — SOL 89,55 $, gap -0,97%, somiglianza +61,09%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-21 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 75.097 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0009% | -3,95% | 1,07 | -2,94% | 0 $ | 0 $ |
| SOL | 89,44 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | ALTA | 100% | +0,0118% | +8,30% | 1,57 | -6,87% | 0 $ | 0 $ |
| DOGE | 0.08238 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | ALTA | 100% | +0,0099% | +11,21% | 1,46 | -0,84% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0014% | 158,29 mln $ | 1,08 | -3,30% |
| BTC | Bitget | OK | +0,0084% | 2,40 mld $ | 4,42 | -14,76% |
| BTC | Kucoin | OK | +0,0054% | 1,81 mld $ | 0,51 | +3,74% |
| SOL | Kraken | OK | +0,0256% | 42,32 mln $ | 5,12 | -12,95% |
| SOL | Bitget | OK | +0,0100% | 384,88 mln $ | 25,88 | -34,84% |
| SOL | Kucoin | OK | +0,0100% | 242,34 mln $ | 0,70 | -13,74% |
| DOGE | Kraken | OK | +0,0016% | 4,83 mln $ | 0,72 | +1,25% |
| DOGE | Bitget | OK | +0,0100% | 106,53 mln $ | 0,60 | -9,76% |
| DOGE | Kucoin | OK | +0,0100% | 137,59 mln $ | 1,35 | -30,99% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **-0,50**.
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

- Score grezzo exchange: **+3,25**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** Adam and Eve Bottom attivo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+3,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 4, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 3, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** Triplo minimo attivo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +57,50% | +2,70% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +57,50% | +2,70% |
| SOL | +47,50% | -0,88% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +47,50% | -0,88% |
| DOGE | +55,00% | +1,88% | 0 | n/a | RACCOLTA DATI | 0,00 | +55,00% | +1,88% |

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

Generato: 2026-08-21 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-21 | BTC | 75.096,70 | V2.1.3 | OK | 0 | 0 | 0,25 | BASSA | 1,07 | -3,95% | -2,94% |
| 2026-08-21 | DOGE | 0.08238 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,46 | +11,21% | -0,84% |
| 2026-08-21 | SOL | 89,44 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,57 | +8,30% | -6,87% |
| 2026-08-20 | BTC | 69.515,36 | V2.1.3 | OK | 0 | 0 | 2,25 | ALTA | 1,03 | +8,86% | +1,47% |
| 2026-08-20 | DOGE | 0.07482 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,31 | +2,01% | +4,59% |
| 2026-08-20 | SOL | 84,87 | V2.1.3 | OK | 0 | 0 | 2,00 | MEDIA | 1,16 | -13,35% | +3,32% |
| 2026-08-19 | BTC | 64.333,70 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 9,10 | -1,39% | -1,10% |
| 2026-08-19 | DOGE | 0.06998 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,95 | +3,15% | -0,97% |
| 2026-08-19 | SOL | 76,86 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,89 | +18,37% | +5,45% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 5 | +60,00% | +2,90% | +2,11% | +3,72% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
| DOGE | 14g | 3 | +33,33% | -6,28% | -1,38% | +10,89% | FEEDBACK RAPIDO |
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

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 75.133 $ | +0.0074% | -7.78% | 1.01 | Misto | 1/5 |
| SOL | 89,55 $ | +0.0100% | -16.11% | 2.18 | Rischio sotto | 2/5 |
| DOGE | 0.08238 $ | +0.0100% | -15.16% | 4.81 | Rischio sotto | 2/5 |

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

Generato: 2026-08-21 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily              | Stato D    | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-------------------|:-----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish     | CONFERMATA | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Conferma rialzista | CONTESTO   | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| DOGE    | Conferma rialzista | CONTESTO   | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo               | Stato      | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-------------------|:-----------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish     | CONFERMATA | 75.095 $ / 82,89  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71 | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO   | 75.095 $ / 54,27  | n/a                                                               | +17,78%             | 15,80            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO   | 89,60 $ / 79,70   | n/a                                                               | +23,46%             | 37,12            |      0 |
| SOL     | 1W   | Hidden bearish     | CONFERMATA | 89,60 $ / 51,18   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO   | 0.08247 $ / 76,17 | n/a                                                               | +19,54%             | 37,26            |      0 |
| DOGE    | 1W   | Conferma rialzista | CONTESTO   | 0.08247 $ / 43,11 | n/a                                                               | +13,47%             | 9,71             |      0 |

### BTC

- **1D — Hidden bullish / CONFERMATA**: Hidden bullish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **8**.
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

Generato: 2026-08-21 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend           | Momentum                  | Struttura                                          |   Pattern score | Fibonacci   | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:----------------|:--------------------------|:---------------------------------------------------|----------------:|:------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 75.133 $ | 11 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 77.991 |
| SOL | 89,55 $ | 11 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | +1 | 0 / TESTATO | Adam and Eve Bottom / ATTIVO | Doppio massimo / CANDIDATO | 74,20 | 98,27 |
| DOGE | 0.08238 $ | 5 | COSTRUTTIVO MA NON CONFERMATO | Trend misto | Momentum in miglioramento | Struttura rialzista con massimi e minimi crescenti | +1 | 0 / TESTATO | Triplo minimo / ATTIVO | Doppio massimo / CANDIDATO | 0.06895 | 0.09169 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — ATTIVO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| DOGE | TARGET RAGGIUNTO | ATTIVO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 82.93 | 941.689 | 64.696 | 64.276 | 68.986 | 1,43% | -9,92% | 13,66% | -2,01% |
| SOL | 79.66 | 1.37713 | 76,09 | 76,66 | 81,21 | 2,38% | -16,34% | 14,95% | 4,54% |
| DOGE | 76.07 | 0.00118 | 0.07082 | 0.07205 | 0.08945 | -4,65% | -16,43% | 12,92% | -20,01% |

## Dettaglio asset

### BTC

- Prezzo: **75.133 $**
- Punteggio tecnico: **11 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 6.223e+04 -> 6.249e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Divergenza rialzista nascosta RSI** (1)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 61.8% a 75.036; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.488**
- Resistenza più vicina: **77.991**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 174,63%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (2g); progresso 174,63%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 174,63%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (2g); progresso 174,63%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 96,88%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (2g); progresso 96,88%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 30,11%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 30,11%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 30,11%; prezzo sopra neckline.

### SOL

- Prezzo: **89,55 $**
- Punteggio tecnico: **11 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 70.69 -> 74.2. Ultimi massimi: 78.73 -> 77.62.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 61.8% a 89,07; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **+1**
  - rialzista dominante: Adam and Eve Bottom (ATTIVO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,20**
- Resistenza più vicina: **98,27**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 203,30%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (2g); progresso 203,30%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 134,77%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (2g); progresso 134,77%; prezzo sopra neckline.
- Adam and Eve Bottom: **ATTIVO** (+1)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: ATTIVO. Target teorico: 99,70; progresso corrente: 36,13%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (2g); progresso 36,13%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 39,01%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 26,67%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 39,01%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08238 $**
- Punteggio tecnico: **5 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07117 -> 0.07286.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 23.6% a 0.08059; stato TESTATO; confluenza: neckline rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Triplo minimo (ATTIVO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.09169**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 155,62%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (2g); progresso 155,62%; prezzo sopra neckline.
- Triplo minimo: **ATTIVO** (+1)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-21 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.09012; progresso corrente: 28,90%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-21 (0g); progresso 28,90%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 155,62%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (2g); progresso 155,62%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 21,20%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 21,20%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 21,20%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato   | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:--------|:--------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-08-14 | 67.280 | 70.244 | 72.640 | 75.036 | 78.447 | 61.8% / 75.036 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | DOWN 2026-05-11 -> 2026-08-16 | 79,88 | 83,40 | 86,24 | 89,07 | 93,12 | 61.8% / 89,07 | TESTATO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-08-12 | 0.08059 | 0.08779 | 0.09360 | 0.09942 | 0.10770 | 23.6% / 0.08059 | TESTATO | neckline rialzista | 0 |

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

- **BTC**: 20/30 previsioni controllate su 48 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 20/30 previsioni controllate su 48 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 20/30 previsioni controllate su 48 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 48 | 20 | 20/30 [███████░░░] | 28 | RACCOLTA DATI | 2026-08-22 / tra 1 giorno |
| SOL | 48 | 20 | 20/30 [███████░░░] | 28 | RACCOLTA DATI | 2026-08-22 / tra 1 giorno |
| DOGE | 48 | 20 | 20/30 [███████░░░] | 28 | RACCOLTA DATI | 2026-08-22 / tra 1 giorno |

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

Generato: 2026-08-21 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 75.133 $          | 75.133 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08238 $         | 0.08238 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 75.133 $          | 75.133 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08238 $         | 0.08238 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 75.133 $          | 75.133 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08238 $         | 0.08238 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 75.133 $          | 75.133 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08238 $         | 0.08238 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 75.133 $          | 75.133 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08238 $         | 0.08238 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 75.133 $          | 75.097 $        | -0,0489%     |
| Exchange Microstructure | SOL     | price             | OK      | 89,55 $           | 89,44 $         | -0,1262%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.08238 $         | 0.08238 $       | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 89,55 $           | 89,55 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 89,55 $           | 89,55 $         | +0,0000%     |

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
