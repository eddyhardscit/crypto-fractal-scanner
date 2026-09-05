<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-04 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +8 | BULLISH | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +6 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -1 | LEGGERMENTE BEARISH | EVITA LONG / SOLO RIMBALZI VELOCI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+8**, spot = **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+6**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-1**, spot = **EVITA LONG / SOLO RIMBALZI VELOCI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+8**
- Confluenza: **POSITIVA FORTE**
- Bias Global: **Rialzista**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 81.347; conferma del doppio minimo sopra 66.910.
- Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+6**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 108,85 / 129,91, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 86,03 / 74,20 / 62,19.

### DOGE

- Global Confluence: **-1**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **EVITA LONG / SOLO RIMBALZI VELOCI**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,31 $; upside verso EMA200 +7,40%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-04T05:33:13+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-04T05:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-04T05:05:31+00:00 | 2026-09-04T05:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-04T04:45:00+00:00 | 2026-09-04T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-09-04T04:00:00+00:00 | 2026-09-04T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-09-04T00:00:00+00:00 | 2026-09-04T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | USELESS | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | USELESS | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 5,64 | 6,00 | 0,36 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,60 | 6,00 | 0,40 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 5,52 | 6,00 | 0,48 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,84 | 6,00 | 1,16 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 3,35 | 6,00 | 2,65 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 3,10 | 6,00 | 2,90 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | ADA | 60m | LONG | 6,75 | 5,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top10 Long | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 + forza BTC 1H | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Mfe V1 | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Mfe Trail | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Long Only V1 | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Partial 1R V1 | ADA | 60m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.811,54 | -1,88% | €2,98 | €3.000,00 | 0,10% | 6 | 57 | 40,35% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 57 | 2885 | PRIME INDICAZIONI | 100 (mancano 43) |

- Trade del Principale 4H chiusi: **57**; win rate **40,35%**; profit factor **0,87**.
- Expectancy: **€-3,28** per trade; P&L netto: **€-187,09**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.811,54 | €699,62 | €2.098,86 | €196,19 | €-0,23 |
| TEST | Benchmark Donchian breakout 1H | 5 | €11.660,32 | €1.220,33 | €2.440,67 | €170,42 | €10,57 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €11.385,79 | €1.191,60 | €2.383,20 | €166,41 | €10,32 |
| TEST | Main Side Regime Guard V1 | 7 | €11.274,68 | €686,67 | €2.060,00 | €223,26 | €225,99 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.011,69 | €1.168,96 | €3.506,87 | €165,93 | €11,32 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.971,19 | €1.176,04 | €2.352,09 | €219,43 | €-0,12 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.720,53 | €1.709,33 | €3.418,65 | €162,82 | €0,13 |
| TEST | Combo Adaptive Long Only V1 | 7 | €10.559,78 | €2.377,49 | €4.754,98 | €211,21 | €-0,47 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 7 | €10.449,06 | €1.342,29 | €4.026,88 | €158,34 | €-10,69 |
| TEST | Rapida 1H V2 | 2 | €10.402,09 | €1.600,89 | €4.802,66 | €104,16 | €-219,34 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 5 | €10.393,78 | €3.331,59 | €9.994,78 | €209,05 | €-206,36 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.379,82 | €1.701,09 | €5.103,26 | €207,64 | €0,00 |
| TEST | Scanner Top15 Long | 10 | €10.375,29 | €1.849,45 | €3.698,91 | €159,39 | €57,37 |
| TEST | Scanner Top20 Long | 10 | €10.375,29 | €1.849,45 | €3.698,91 | €159,39 | €57,37 |
| TEST | Scanner Top5 Btc Tp3 V1 | 8 | €10.368,90 | €1.685,81 | €3.371,62 | €155,55 | €61,02 |
| TEST | Scanner Top5 Btc Runner25 V1 | 8 | €10.362,83 | €1.684,82 | €3.369,64 | €155,46 | €60,99 |
| TEST | Combo Adaptive | 7 | €10.358,36 | €1.317,56 | €2.635,12 | €156,17 | €-0,17 |
| TEST | Sol Donchian 1H | 0 | €10.356,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.343,54 | €1.338,98 | €4.016,93 | €211,55 | €-233,87 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.313,13 | €1.690,16 | €5.070,47 | €206,30 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 8 | €10.276,40 | €1.071,19 | €2.142,37 | €207,40 | €-3,83 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.275,47 | €1.106,74 | €2.213,47 | €205,51 | €-0,15 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.207,96 | €2.293,89 | €4.587,78 | €204,16 | €0,11 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 10 | €10.183,87 | €1.164,74 | €2.329,47 | €153,07 | €58,53 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.157,48 | €140,98 | €422,93 | €50,75 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.138,20 | €574,98 | €1.149,96 | €50,72 | €-5,82 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 8 | €10.133,79 | €775,11 | €2.325,33 | €151,69 | €20,17 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.088,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 5 | €10.070,80 | €1.166,00 | €3.497,99 | €151,13 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.065,19 | €1.980,53 | €3.961,07 | €151,45 | €-0,37 |
| TEST | Btc Bollinger 4H | 1 | €10.062,61 | €985,68 | €1.971,36 | €50,34 | €-4,57 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.039,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.032,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.025,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.019,67 | €817,27 | €1.634,54 | €50,09 | €3,14 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 2 | €10.014,64 | €876,12 | €2.628,37 | €51,20 | €-216,81 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.007,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.002,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.987,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.969,14 | €887,05 | €1.774,10 | €49,83 | €3,40 |
| TEST | Sol Adaptive 1H | 0 | €9.968,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.963,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.937,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.927,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.915,80 | €882,31 | €1.764,61 | €49,57 | €3,39 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €9.900,36 | €1.081,30 | €2.162,60 | €99,08 | €0,15 |
| TEST | Btc Donchian 1H | 0 | €9.897,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.890,39 | €690,19 | €1.380,39 | €49,44 | €4,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €9.889,39 | €2.033,28 | €6.099,85 | €197,98 | €-25,50 |
| TEST | Master Adaptive Gb20 Be V1 | 8 | €9.886,49 | €1.130,79 | €2.261,59 | €197,82 | €-4,36 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €9.878,35 | €1.878,01 | €5.634,04 | €198,00 | €-22,41 |
| TEST | Master Adaptive Gb20 Partial V1 | 8 | €9.875,98 | €1.129,59 | €2.259,18 | €197,61 | €-4,35 |
| TEST | Master Adaptive V1 | 8 | €9.837,78 | €1.125,22 | €2.250,44 | €196,85 | €-4,34 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.834,25 | €847,85 | €1.695,69 | €99,46 | €-3,42 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 3 | €9.829,82 | €1.075,61 | €3.226,84 | €101,77 | €-226,87 |
| TEST | Sol Bollinger 1H | 0 | €9.819,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €9.810,68 | €1.020,33 | €3.060,98 | €147,15 | €13,44 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 7 | €9.784,46 | €1.532,82 | €4.598,46 | €195,01 | €12,21 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €9.756,04 | €205,67 | €617,01 | €48,38 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.750,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.726,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.716,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.709,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 8 | €9.707,92 | €1.110,30 | €2.220,59 | €194,25 | €-4,28 |
| TEST | Scanner Top5 Btc Guard V1 | 8 | €9.700,81 | €1.055,53 | €2.111,06 | €192,98 | €-0,12 |
| TEST | Global Confluence puro 1H | 0 | €9.700,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.693,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.659,09 | €1.148,62 | €3.445,86 | €193,18 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.653,10 | €1.235,88 | €3.707,64 | €197,62 | €-227,70 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.632,75 | €1.037,51 | €2.075,02 | €192,66 | €-0,14 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.603,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.566,83 | €991,45 | €2.974,34 | €143,49 | €13,30 |
| TEST | Master Adaptive Runner25 V1 | 8 | €9.551,34 | €1.501,33 | €3.002,67 | €191,00 | €5,32 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.541,28 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.536,48 | €1.182,06 | €3.546,17 | €190,77 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 9 | €9.527,44 | €1.079,15 | €2.158,29 | €190,65 | €-3,95 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €9.511,51 | €1.849,63 | €5.548,89 | €144,70 | €-39,42 |
| TEST | Btc Ema 1H | 1 | €9.504,89 | €1.101,38 | €3.304,13 | €47,58 | €-9,02 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 8 | €9.475,20 | €1.030,98 | €2.061,97 | €188,49 | €-0,12 |
| TEST | Bilanciata 1H V2 | 5 | €9.373,89 | €1.594,14 | €4.782,43 | €142,11 | €-15,42 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.370,90 | €1.575,97 | €3.151,93 | €187,41 | €0,34 |
| TEST | Bilanciata 1H V1 | 7 | €9.338,54 | €1.683,10 | €5.049,29 | €95,14 | €8,58 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.331,66 | €1.972,71 | €5.918,14 | €190,53 | €-193,40 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.319,48 | €1.027,07 | €2.054,14 | €90,71 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 4 | €9.301,47 | €606,13 | €1.212,26 | €137,05 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €9.258,63 | €1.800,45 | €5.401,36 | €140,85 | €-38,38 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 8 | €9.210,81 | €1.067,36 | €2.134,72 | €93,14 | €54,38 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.180,73 | €931,20 | €1.862,41 | €138,39 | €-0,11 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €9.139,28 | €2.591,47 | €7.774,41 | €138,28 | €-24,48 |
| TEST | Combo Adaptive Mfe Trail | 8 | €9.046,80 | €1.124,48 | €2.248,96 | €146,71 | €-0,88 |
| TEST | Combo Adaptive Tp3 V1 | 8 | €9.038,50 | €1.047,42 | €2.094,84 | €91,40 | €53,36 |
| TEST | Master Adaptive Strict3 V1 | 3 | €8.921,73 | €603,48 | €1.206,96 | €129,97 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 1 | €8.912,04 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €8.870,03 | €185,37 | €370,74 | €44,49 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €8.826,05 | €1.865,82 | €5.597,47 | €180,20 | €-182,92 |
| TEST | Combo Mean Reversion | 1 | €8.798,26 | €942,00 | €1.883,99 | €44,59 | €183,70 |
| TEST | Combo Trend | 5 | €8.790,45 | €1.929,02 | €3.858,05 | €89,68 | €-274,42 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 2 | €8.738,09 | €1.063,55 | €2.127,09 | €86,96 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €8.603,29 | €1.617,25 | €3.234,49 | €86,87 | €34,88 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.446,67 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.811,54 | €-187,09 | 57 | 57 | 40,35% | 0,87 | €-3,28 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.660,32 | €1.650,39 | 130 | 130 | 46,92% | 1,59 | €12,70 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.385,79 | €1.376,10 | 98 | 98 | 45,92% | 1,73 | €14,04 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.274,68 | €1.050,37 | 46 | 46 | 56,52% | 2,37 | €22,83 | 3,82% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.011,69 | €1.002,60 | 183 | 183 | 50,27% | 1,26 | €5,48 | 7,95% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.971,19 | €972,75 | 163 | 163 | 47,85% | 1,32 | €5,97 | 8,85% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.720,53 | €723,08 | 143 | 143 | 51,05% | 1,25 | €5,06 | 10,10% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.559,78 | €563,11 | 146 | 146 | 47,95% | 1,19 | €3,86 | 7,78% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.449,06 | €462,53 | 104 | 104 | 50,00% | 1,24 | €4,45 | 5,24% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.402,09 | €624,37 | 65 | 58 | 50,77% | 1,42 | €9,61 | 3,89% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.393,78 | €605,94 | 98 | 98 | 51,02% | 1,30 | €6,18 | 4,50% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.379,82 | €383,23 | 211 | 211 | 49,29% | 1,11 | €1,82 | 9,50% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.375,29 | €320,19 | 170 | 170 | 48,82% | 1,11 | €1,88 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.375,29 | €320,19 | 170 | 170 | 48,82% | 1,11 | €1,88 | 10,31% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.368,90 | €309,93 | 132 | 132 | 42,42% | 1,11 | €2,35 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.362,83 | €303,89 | 136 | 136 | 42,65% | 1,11 | €2,23 | 12,06% |
| TEST | Combo Adaptive | Combo Adaptive | €10.358,36 | €360,28 | 193 | 193 | 45,60% | 1,11 | €1,87 | 8,17% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.356,28 | €356,28 | 17 | 17 | 64,71% | 2,44 | €20,96 | 2,77% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.343,54 | €579,64 | 263 | 263 | 44,49% | 1,13 | €2,20 | 9,27% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.313,13 | €316,52 | 255 | 255 | 44,31% | 1,07 | €1,24 | 9,48% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Ampia 4H | Confluenza trend | €10.276,40 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.275,47 | €276,97 | 146 | 146 | 45,21% | 1,09 | €1,90 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.207,96 | €210,60 | 160 | 160 | 48,12% | 1,08 | €1,32 | 10,31% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Scanner | Combo Scanner | €10.183,87 | €126,81 | 165 | 165 | 44,85% | 1,04 | €0,77 | 11,38% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.157,48 | €158,05 | 16 | 16 | 37,50% | 1,36 | €9,88 | 3,39% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.138,20 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,35% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.133,79 | €115,01 | 204 | 204 | 43,14% | 1,03 | €0,56 | 10,60% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 1H | Trend following EMA | €10.088,56 | €88,56 | 20 | 20 | 45,00% | 1,16 | €4,43 | 3,33% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.070,80 | €73,11 | 250 | 250 | 39,60% | 1,02 | €0,29 | 6,56% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.065,19 | €67,91 | 170 | 170 | 45,29% | 1,03 | €0,40 | 8,69% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.062,61 | €68,27 | 3 | 3 | 66,67% | 2,25 | €22,76 | 0,91% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.039,42 | €39,42 | 29 | 29 | 44,83% | 1,33 | €1,36 | 0,33% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.032,57 | €32,57 | 13 | 13 | 61,54% | 1,11 | €2,51 | 1,89% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.025,86 | €25,86 | 15 | 15 | 60,00% | 1,07 | €1,72 | 3,08% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.019,67 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.014,64 | €232,84 | 73 | 73 | 45,21% | 1,13 | €3,19 | 6,05% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.007,88 | €7,88 | 29 | 29 | 44,83% | 1,33 | €0,27 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Doge Ema 1H | Trend following EMA | €10.002,70 | €2,70 | 23 | 23 | 60,87% | 1,01 | €0,12 | 2,77% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.987,54 | €-12,46 | 18 | 18 | 33,33% | 0,30 | €-0,69 | 0,15% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Ema 4H | Trend following EMA | €9.969,14 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.968,76 | €-31,24 | 22 | 22 | 45,45% | 0,95 | €-1,42 | 4,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.963,04 | €-36,96 | 18 | 18 | 33,33% | 0,63 | €-2,05 | 0,71% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.937,70 | €-62,30 | 18 | 18 | 33,33% | 0,30 | €-3,46 | 0,76% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.927,41 | €-72,59 | 29 | 29 | 44,83% | 0,56 | €-2,50 | 0,84% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.915,80 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.900,36 | €-98,26 | 145 | 145 | 44,83% | 0,97 | €-0,68 | 11,68% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.897,46 | €-102,54 | 12 | 12 | 41,67% | 0,70 | €-8,55 | 1,91% |
| TEST | Eth Ema 4H | Trend following EMA | €9.890,39 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.889,39 | €-81,46 | 125 | 125 | 44,80% | 0,97 | €-0,65 | 6,64% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.886,49 | €-109,00 | 92 | 92 | 34,78% | 0,96 | €-1,18 | 8,39% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.878,35 | €-95,86 | 205 | 205 | 42,44% | 0,98 | €-0,47 | 12,52% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.875,98 | €-119,52 | 87 | 87 | 37,93% | 0,95 | €-1,37 | 7,98% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.837,78 | €-157,74 | 89 | 89 | 37,08% | 0,94 | €-1,77 | 7,80% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.834,25 | €-161,02 | 134 | 127 | 40,30% | 0,95 | €-1,20 | 10,88% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €9.829,82 | €58,42 | 50 | 50 | 42,00% | 1,04 | €1,17 | 6,49% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.819,99 | €-180,01 | 16 | 16 | 43,75% | 0,68 | €-11,25 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.810,68 | €-200,93 | 195 | 195 | 40,51% | 0,95 | €-1,03 | 10,60% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.784,46 | €-224,99 | 127 | 127 | 46,46% | 0,94 | €-1,77 | 8,44% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.756,04 | €-243,59 | 107 | 107 | 40,19% | 0,91 | €-2,28 | 7,99% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.750,02 | €-249,98 | 18 | 18 | 38,89% | 0,59 | €-13,89 | 3,14% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.726,12 | €-273,88 | 46 | 46 | 43,48% | 0,79 | €-5,95 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.716,18 | €-283,82 | 9 | 9 | 33,33% | 0,35 | €-31,54 | 4,16% |
| TEST | Eth Ema 1H | Trend following EMA | €9.709,75 | €-290,25 | 25 | 25 | 40,00% | 0,66 | €-11,61 | 4,80% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.707,92 | €-287,66 | 123 | 123 | 47,15% | 0,89 | €-2,34 | 9,02% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.700,81 | €-298,29 | 132 | 132 | 39,39% | 0,90 | €-2,26 | 7,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.700,24 | €-299,76 | 20 | 20 | 35,00% | 0,50 | €-14,99 | 3,93% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.693,16 | €-306,84 | 17 | 17 | 29,41% | 0,54 | €-18,05 | 3,74% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.659,09 | €-338,77 | 117 | 117 | 44,44% | 0,85 | €-2,90 | 9,26% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.653,10 | €-117,25 | 159 | 159 | 44,65% | 0,96 | €-0,74 | 7,10% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.632,75 | €-365,84 | 138 | 138 | 44,20% | 0,86 | €-2,65 | 12,28% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.603,78 | €-396,22 | 46 | 46 | 39,13% | 0,69 | €-8,61 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.566,83 | €-444,69 | 158 | 158 | 38,61% | 0,85 | €-2,81 | 10,60% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.551,34 | €-453,31 | 75 | 75 | 33,33% | 0,81 | €-6,04 | 8,44% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.541,28 | €-457,54 | 77 | 77 | 45,45% | 0,76 | €-5,94 | 5,38% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.536,48 | €-461,05 | 223 | 223 | 42,15% | 0,90 | €-2,07 | 10,92% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.527,44 | €-468,88 | 79 | 79 | 26,58% | 0,80 | €-5,94 | 11,41% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.511,51 | €-445,73 | 160 | 160 | 41,88% | 0,89 | €-2,79 | 15,64% |
| TEST | Btc Ema 1H | Trend following EMA | €9.504,89 | €-484,10 | 19 | 19 | 21,05% | 0,35 | €-25,48 | 5,11% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.475,20 | €-523,92 | 149 | 149 | 40,27% | 0,85 | €-3,52 | 8,78% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.373,89 | €-607,01 | 141 | 128 | 42,55% | 0,80 | €-4,31 | 11,82% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.370,90 | €-628,75 | 84 | 84 | 34,52% | 0,73 | €-7,49 | 7,96% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.338,54 | €-666,57 | 146 | 146 | 38,36% | 0,78 | €-4,57 | 15,68% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.331,66 | €-471,60 | 182 | 182 | 40,11% | 0,88 | €-2,59 | 12,67% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.319,48 | €-678,84 | 93 | 93 | 34,41% | 0,77 | €-7,30 | 10,13% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.301,47 | €-698,29 | 93 | 93 | 37,63% | 0,74 | €-7,51 | 11,79% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.258,63 | €-699,76 | 118 | 118 | 43,22% | 0,80 | €-5,93 | 15,94% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.210,81 | €-842,26 | 118 | 118 | 35,59% | 0,66 | €-7,14 | 14,10% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.180,73 | €-818,07 | 148 | 148 | 38,51% | 0,71 | €-5,53 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.139,28 | €-831,58 | 164 | 164 | 38,41% | 0,80 | €-5,07 | 17,41% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.046,80 | €-950,99 | 205 | 205 | 40,98% | 0,76 | €-4,64 | 15,45% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.038,50 | €-1.013,58 | 98 | 98 | 34,69% | 0,54 | €-10,34 | 14,10% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.921,73 | €-1.077,55 | 76 | 76 | 28,95% | 0,64 | €-14,18 | 13,60% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.912,04 | €-1.086,89 | 42 | 42 | 19,05% | 0,27 | €-25,88 | 12,22% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.870,03 | €-1.130,22 | 117 | 117 | 36,75% | 0,65 | €-9,66 | 13,91% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €8.826,05 | €-987,88 | 136 | 136 | 39,71% | 0,65 | €-7,26 | 12,41% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.798,26 | €-1.384,14 | 58 | 58 | 32,76% | 0,42 | €-23,86 | 15,55% |
| TEST | Combo Trend | Combo Trend | €8.790,45 | €-932,55 | 187 | 187 | 38,50% | 0,78 | €-4,99 | 14,08% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.738,09 | €-1.260,63 | 91 | 91 | 34,07% | 0,52 | €-13,85 | 16,19% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.603,29 | €-1.429,23 | 123 | 123 | 30,89% | 0,56 | €-11,62 | 19,11% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.446,67 | €-1.553,33 | 100 | 100 | 39,00% | 0,53 | €-15,53 | 17,47% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,44737 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-0,23 |
| Principale 4H | XMR | LONG | Confluenza trend | 240m | 3,0x | 512,59737 | 512,59737 | 474,66794 | 344,29457 | 588,45625 | €9,14 | €27,43 | €2,03 | €0,00 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €0,00 |
| Bilanciata 1H V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,21967 | 0,22262 | 0,22113 | 0,14755 | 0,23107 | €593,87 | €1.781,62 | €0,00 | €23,89 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,46367 | 1,44737 | 1,43166 | 0,98310 | 1,52769 | €9,95 | €29,86 | €0,65 | €-0,33 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 950,40004 | 947,48000 | 916,50537 | 638,35203 | 1018,18938 | €10,39 | €31,16 | €1,11 | €-0,10 |
| Bilanciata 1H V1 | USELESS | LONG | Confluenza trend | 60m | 3,0x | 0,20717 | 0,21725 | 0,18606 | 0,13915 | 0,24939 | €8,99 | €26,97 | €2,75 | €1,31 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 87,10142 | 86,40800 | 85,21007 | 58,50312 | 90,88410 | €678,01 | €2.034,03 | €44,17 | €-16,19 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | SUI | LONG | Confluenza trend | 60m | 3,0x | 0,78276 | 0,78276 | 0,76213 | 0,52575 | 0,82402 | €40,08 | €120,24 | €3,17 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,13495 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €0,00 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,17053 | 0,17053 | 0,16308 | 0,11454 | 0,18544 | €358,89 | €1.076,67 | €47,05 | €0,00 |
| Bilanciata 1H V2 | XRP | LONG | Confluenza trend V2 | 60m | 3,0x | 1,45862 | 1,44737 | 1,42530 | 0,97971 | 1,52526 | €666,21 | €1.998,63 | €45,65 | €-15,42 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,22262 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-177,16 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €0,00 |
| Bilanciata 1H V3 Filtered | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17350 | 0,17350 | 0,16618 | 0,11654 | 0,18815 | €9,93 | €29,79 | €1,26 | €0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 87,10142 | 86,40800 | 85,21007 | 58,50312 | 90,88410 | €679,88 | €2.039,64 | €44,29 | €-16,24 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €0,00 |
| 1H Fast Score 6 75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 87,56951 | 86,40800 | 86,13990 | 58,81752 | 89,71393 | €974,00 | €2.922,00 | €47,70 | €-38,76 |
| 1H Fast Score 6 75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01517 | 0,01459 | 0,01335 | 0,01019 | 0,01790 | €130,10 | €390,31 | €46,84 | €-14,73 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 940,09798 | 947,48000 | 915,36901 | 631,43248 | 977,19145 | €596,92 | €1.790,77 | €47,11 | €14,06 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 87,56951 | 86,40800 | 86,13990 | 58,81752 | 89,71393 | €948,10 | €2.844,31 | €46,43 | €-37,73 |
| 1H Fast Score 6 75 No Trend Up V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01517 | 0,01459 | 0,01335 | 0,01019 | 0,01790 | €126,64 | €379,93 | €45,59 | €-14,34 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 940,09798 | 947,48000 | 915,36901 | 631,43248 | 977,19145 | €581,05 | €1.743,16 | €45,85 | €13,69 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,22262 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-226,87 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 87,56951 | 86,40800 | 86,13990 | 58,81752 | 89,71393 | €42,17 | €126,51 | €2,07 | €-1,68 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 940,09798 | 947,48000 | 915,36901 | 631,43248 | 977,19145 | €551,75 | €1.655,25 | €43,54 | €13,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 86,53430 | 86,40800 | 85,06318 | 58,12221 | 88,74098 | €28,05 | €84,14 | €1,43 | €-0,12 |
| 1H Fast Nohigh Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 940,09798 | 947,48000 | 915,36901 | 631,43248 | 977,19145 | €575,81 | €1.727,42 | €45,44 | €13,56 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,22262 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-233,87 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,17350 | 0,17350 | 0,16781 | 0,11654 | 0,18205 | €23,60 | €70,79 | €2,32 | €0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,78276 | 0,78276 | 0,76671 | 0,52575 | 0,81485 | €723,42 | €2.170,27 | €44,49 | €0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,22262 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-219,34 |
| Rapida 1H V2 | SUI | LONG | Momentum / breakout V2 | 60m | 3,0x | 0,78276 | 0,78276 | 0,76671 | 0,52575 | 0,80682 | €851,57 | €2.554,72 | €52,37 | €0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,78276 | 0,78276 | 0,76671 | 0,52575 | 0,80682 | €771,18 | €2.313,53 | €47,42 | €0,00 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | XMR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 522,55449 | 522,55449 | 509,89897 | 350,98243 | 541,53777 | €622,76 | €1.868,28 | €45,25 | €0,00 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 87,56951 | 86,40800 | 86,13990 | 58,81752 | 89,71393 | €934,55 | €2.803,66 | €45,77 | €-37,19 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 938,34763 | 947,48000 | 912,98499 | 630,25683 | 976,39159 | €18,68 | €56,04 | €1,51 | €0,55 |
| 1H Fast V3 Cap75 V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,44083 | 1,44737 | 1,41622 | 0,96776 | 1,47774 | €892,98 | €2.678,94 | €45,75 | €12,16 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,22262 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-227,70 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17350 | 0,17350 | 0,16781 | 0,11654 | 0,18205 | €55,75 | €167,24 | €5,49 | €0,00 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 87,10142 | 86,40800 | 85,63037 | 58,50312 | 89,30798 | €977,23 | €2.931,69 | €49,51 | €-23,34 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 940,09798 | 947,48000 | 915,36901 | 631,43248 | 977,19145 | €39,63 | €118,89 | €3,13 | €0,93 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | XMR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 522,55449 | 522,55449 | 509,89897 | 350,98243 | 541,53777 | €33,71 | €101,14 | €2,45 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 87,56951 | 86,40800 | 86,13990 | 58,81752 | 89,71393 | €1.011,12 | €3.033,35 | €49,52 | €-40,23 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 940,09798 | 947,48000 | 915,36901 | 631,43248 | 977,19145 | €625,61 | €1.876,83 | €49,37 | €14,74 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,78276 | 0,78276 | 0,76671 | 0,52575 | 0,80682 | €721,96 | €2.165,88 | €44,40 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 87,56951 | 86,40800 | 86,13990 | 58,81752 | 89,71393 | €35,77 | €107,31 | €1,75 | €-1,42 |
| 1H Fast V3 No Esports Long Only V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21016 | 0,21725 | 0,21016 | 0,14116 | 0,23524 | €211,86 | €635,58 | €0,00 | €21,44 |
| 1H Fast V3 No Esports Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,44083 | 1,44737 | 1,41622 | 0,96776 | 1,47774 | €11,58 | €34,73 | €0,59 | €0,16 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,78276 | 0,78276 | 0,76671 | 0,52575 | 0,80682 | €776,16 | €2.328,49 | €47,73 | €0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,22262 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-216,33 |
| 1H Fast V3 No Esports Stress Guard V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17350 | 0,17350 | 0,16781 | 0,11654 | 0,18205 | €530,26 | €1.590,79 | €52,23 | €0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 86,53430 | 86,40800 | 85,06318 | 58,12221 | 88,74098 | €1.015,41 | €3.046,23 | €51,79 | €-4,45 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 938,34763 | 947,48000 | 912,98499 | 630,25683 | 976,39159 | €10,29 | €30,88 | €0,83 | €0,30 |
| 1H Fast V3 No Esports Stress Guard V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,44083 | 1,44737 | 1,41622 | 0,96776 | 1,47774 | €1.036,59 | €3.109,77 | €53,11 | €14,12 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | XMR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 522,55449 | 522,55449 | 509,89897 | 350,98243 | 541,53777 | €33,05 | €99,14 | €2,40 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 944,01877 | 947,48000 | 917,54529 | 634,06594 | 983,72898 | €12,94 | €38,82 | €1,09 | €0,14 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 87,56951 | 86,40800 | 86,13990 | 58,81752 | 89,71393 | €11,61 | €34,83 | €0,57 | €-0,46 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,44083 | 1,44737 | 1,41622 | 0,96776 | 1,47774 | €928,54 | €2.785,63 | €47,57 | €12,65 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21729 | 0,21725 | 0,19884 | 0,14595 | 0,24497 | €192,06 | €576,19 | €48,92 | €-0,12 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2506,59000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,19 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 86,40800 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €2,47 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08700 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-7,47 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 103,70400 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-0,02 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €0,00 |
| Forza relativa 1H V1 | XRP | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,45362 | 1,44737 | 1,42265 | 0,73408 | 1,52176 | €54,14 | €108,28 | €2,31 | €-0,47 |
| Forza relativa 1H V1 | ADA | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,21967 | 0,22262 | 0,21967 | 0,11094 | 0,23221 | €820,28 | €1.640,56 | €0,00 | €22,00 |
| Forza relativa 1H V1 | ZEC | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1024,96831 | €16,16 | €32,33 | €1,15 | €-0,10 |
| Forza relativa 1H V1 | USELESS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,21016 | 0,21725 | 0,18866 | 0,10613 | 0,25746 | €199,23 | €398,46 | €40,76 | €13,44 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,22262 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-3,42 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SUI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,77315 | 0,77315 | 0,75123 | 0,39044 | 0,82139 | €19,44 | €38,87 | €1,10 | €0,00 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,22262 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-14,22 |
| Benchmark Donchian breakout 1H | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45362 | 1,44737 | 1,41921 | 0,73408 | 1,53965 | €13,02 | €26,04 | €0,62 | €-0,11 |
| Benchmark Donchian breakout 1H | USELESS | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20717 | 0,21725 | 0,18372 | 0,10462 | 0,26581 | €255,96 | €511,91 | €57,96 | €24,90 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,22262 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-13,89 |
| Donchian 1H Gb20 120R V1 | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45362 | 1,44737 | 1,41921 | 0,73408 | 1,53965 | €12,71 | €25,43 | €0,60 | €-0,11 |
| Donchian 1H Gb20 120R V1 | USELESS | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20717 | 0,21725 | 0,18372 | 0,10462 | 0,26581 | €249,93 | €499,86 | €56,60 | €24,32 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 81177,11218 | 80955,40000 | 79878,27838 | 40994,44165 | 84034,54652 | €20,91 | €41,81 | €0,67 | €-0,11 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1018,18938 | €19,29 | €38,57 | €1,38 | €-0,12 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01453 | 0,01459 | 0,01279 | 0,00734 | 0,01802 | €12,62 | €25,24 | €3,03 | €0,11 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top15 Long | USELESS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,18983 | 0,21725 | 0,20146 | 0,09586 | 0,23493 | €201,18 | €402,37 | €0,00 | €58,13 |
| Scanner Top15 Long | ADA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,22330 | 0,22262 | 0,21770 | 0,11277 | 0,23452 | €22,89 | €45,78 | €1,15 | €-0,14 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01453 | 0,01459 | 0,01279 | 0,00734 | 0,01802 | €25,14 | €50,29 | €6,03 | €0,22 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 952,22041 | 947,48000 | 919,28663 | 480,87131 | 1018,08795 | €34,79 | €69,57 | €2,41 | €-0,35 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 87,10142 | 86,40800 | 85,21007 | 43,98622 | 90,88410 | €30,87 | €61,74 | €1,34 | €-0,49 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top20 Long | USELESS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,18983 | 0,21725 | 0,20146 | 0,09586 | 0,23493 | €201,18 | €402,37 | €0,00 | €58,13 |
| Scanner Top20 Long | ADA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,22330 | 0,22262 | 0,21770 | 0,11277 | 0,23452 | €22,89 | €45,78 | €1,15 | €-0,14 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01453 | 0,01459 | 0,01279 | 0,00734 | 0,01802 | €25,14 | €50,29 | €6,03 | €0,22 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 952,22041 | 947,48000 | 919,28663 | 480,87131 | 1018,08795 | €34,79 | €69,57 | €2,41 | €-0,35 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 87,10142 | 86,40800 | 85,21007 | 43,98622 | 90,88410 | €30,87 | €61,74 | €1,34 | €-0,49 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1024,96831 | €23,79 | €47,58 | €1,70 | €-0,15 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1024,96831 | €22,30 | €44,61 | €1,59 | €-0,14 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €0,00 |
| Scanner Top5 Btc Guard V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,45362 | 1,44737 | 1,42265 | 0,73408 | 1,52176 | €18,00 | €36,01 | €0,77 | €-0,15 |
| Scanner Top5 Btc Guard V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21967 | 0,22262 | 0,21976 | 0,11094 | 0,23221 | €20,06 | €40,11 | €0,00 | €0,54 |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 87,56951 | 86,40800 | 85,73144 | 44,22260 | 91,61327 | €19,03 | €38,05 | €0,80 | €-0,50 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,45362 | 1,44737 | 1,42265 | 0,73408 | 1,52176 | €17,59 | €35,17 | €0,75 | €-0,15 |
| Scanner Top5 Btc Guard Mfe V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21967 | 0,22262 | 0,21976 | 0,11094 | 0,23221 | €19,59 | €39,18 | €0,00 | €0,53 |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 87,56951 | 86,40800 | 85,73144 | 44,22260 | 91,61327 | €18,58 | €37,17 | €0,78 | €-0,49 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21967 | 0,22262 | 0,21976 | 0,11094 | 0,23676 | €29,96 | €59,93 | €0,00 | €0,80 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 944,01877 | 947,48000 | 909,98144 | 476,72948 | 1046,13075 | €13,98 | €27,97 | €1,01 | €0,10 |
| Scanner Top5 Btc Runner25 V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18983 | 0,21725 | 0,20146 | 0,09586 | 0,25748 | €209,61 | €419,22 | €0,00 | €60,56 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 87,56951 | 86,40800 | 85,73144 | 44,22260 | 93,08372 | €18,06 | €36,11 | €0,76 | €-0,48 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21967 | 0,22262 | 0,21976 | 0,11094 | 0,23676 | €29,98 | €59,96 | €0,00 | €0,80 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 944,01877 | 947,48000 | 909,98144 | 476,72948 | 1046,13075 | €13,99 | €27,98 | €1,01 | €0,10 |
| Scanner Top5 Btc Tp3 V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18983 | 0,21725 | 0,20146 | 0,09586 | 0,25748 | €209,73 | €419,46 | €0,00 | €60,59 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 87,56951 | 86,40800 | 85,73144 | 44,22260 | 93,08372 | €18,07 | €36,13 | €0,76 | €-0,48 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,22262 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-274,64 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 940,09798 | 947,48000 | 904,77087 | 474,74948 | 1017,81762 | €13,69 | €27,38 | €1,03 | €0,21 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,22262 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €183,70 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | SUI | LONG | Combo Scanner | 60m | 2,0x | 0,77495 | 0,77495 | 0,75348 | 0,39135 | 0,82220 | €26,73 | €53,47 | €1,48 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €0,00 |
| Combo Scanner | ADA | LONG | Combo Scanner | 60m | 2,0x | 0,21967 | 0,22262 | 0,21976 | 0,11094 | 0,23221 | €28,84 | €57,69 | €0,00 | €0,77 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 944,01877 | 947,48000 | 909,98144 | 476,72948 | 1018,90088 | €13,98 | €27,95 | €1,01 | €0,10 |
| Combo Scanner | USELESS | LONG | Combo Scanner | 60m | 2,0x | 0,18983 | 0,21725 | 0,20146 | 0,09586 | 0,23944 | €206,02 | €412,04 | €0,00 | €59,52 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 87,56951 | 86,40800 | 85,73144 | 44,22260 | 91,61327 | €17,39 | €34,78 | €0,73 | €-0,46 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 6,44429 | 6,20200 | 6,15558 | 3,25437 | 7,07944 | €18,75 | €37,49 | €1,68 | €-1,41 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1018,18938 | €27,44 | €54,87 | €1,96 | €-0,17 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €0,00 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 965,47306 | 947,48000 | 931,27074 | 487,56389 | 1033,87770 | €17,08 | €34,16 | €1,21 | €-0,64 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,45862 | 1,44737 | 1,42530 | 0,73660 | 1,52526 | €15,58 | €31,17 | €0,71 | €-0,24 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €0,00 |
| Combo Adaptive Long Only V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,45362 | 1,44737 | 1,42265 | 0,73408 | 1,51556 | €36,99 | €73,99 | €1,58 | €-0,32 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1018,18938 | €25,17 | €50,34 | €1,80 | €-0,15 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1018,18938 | €59,68 | €119,37 | €4,26 | €-0,37 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €0,00 |
| Combo Adaptive Runner25 V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,21967 | 0,22262 | 0,22145 | 0,11094 | 0,23676 | €43,79 | €87,59 | €0,00 | €1,17 |
| Combo Adaptive Runner25 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,18983 | 0,21725 | 0,20293 | 0,09586 | 0,25748 | €188,31 | €376,62 | €0,00 | €54,41 |
| Combo Adaptive Runner25 V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,46367 | 1,44737 | 1,43166 | 0,73915 | 1,55970 | €38,45 | €76,90 | €1,68 | €-0,86 |
| Combo Adaptive Runner25 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1052,08404 | €18,59 | €37,19 | €1,33 | €-0,11 |
| Combo Adaptive Runner25 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 87,07541 | 86,40800 | 85,20205 | 43,97308 | 92,69550 | €14,98 | €29,96 | €0,64 | €-0,23 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €0,00 |
| Combo Adaptive Tp3 V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,21967 | 0,22262 | 0,22145 | 0,11094 | 0,23676 | €43,01 | €86,01 | €0,00 | €1,15 |
| Combo Adaptive Tp3 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,18983 | 0,21725 | 0,20293 | 0,09586 | 0,25748 | €184,79 | €369,57 | €0,00 | €53,39 |
| Combo Adaptive Tp3 V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,46367 | 1,44737 | 1,43166 | 0,73915 | 1,55970 | €37,73 | €75,47 | €1,65 | €-0,84 |
| Combo Adaptive Tp3 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 950,40004 | 947,48000 | 916,50537 | 479,95202 | 1052,08404 | €18,25 | €36,49 | €1,30 | €-0,11 |
| Combo Adaptive Tp3 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 87,07541 | 86,40800 | 85,20205 | 43,97308 | 92,69550 | €14,70 | €29,40 | €0,63 | €-0,23 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 81177,11218 | 80955,40000 | 80008,16176 | 54523,96034 | 83515,01301 | €1.101,38 | €3.304,13 | €47,58 | €-9,02 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80800,35684 | 80955,40000 | 78530,68128 | 40804,18020 | 86474,54655 | €887,05 | €1.774,10 | €49,83 | €3,40 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80800,35684 | 80955,40000 | 78530,68128 | 40804,18020 | 87155,44873 | €882,31 | €1.764,61 | €49,57 | €3,39 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80768,04316 | 80955,40000 | 82830,55933 | 120748,22452 | 77055,51340 | €985,68 | €1.971,36 | €50,34 | €-4,57 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80800,35684 | 80955,40000 | 78324,34707 | 40804,18020 | 86990,38168 | €817,27 | €1.634,54 | €50,09 | €3,14 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,23184 | 103,70400 | 99,63427 | 52,63708 | 117,10505 | €574,98 | €1.149,96 | €50,72 | €-5,82 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2499,33977 | 2506,59000 | 2409,82951 | 1262,16658 | 2723,11538 | €690,19 | €1.380,39 | €49,44 | €4,00 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €0,00 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 937,37744 | 947,48000 | 904,92697 | 473,37561 | 1002,27837 | €23,16 | €46,32 | €1,60 | €0,50 |
| Master Adaptive V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17350 | 0,17350 | 0,16618 | 0,08762 | 0,18815 | €19,41 | €38,83 | €1,64 | €0,00 |
| Master Adaptive V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,20200 | 6,15558 | 3,25437 | 7,02170 | €13,59 | €27,17 | €1,22 | €-1,02 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01473 | 0,01459 | 0,01296 | 0,00744 | 0,01827 | €203,89 | €407,78 | €48,93 | €-3,81 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,77495 | 0,77495 | 0,75348 | 0,39135 | 0,81791 | €824,16 | €1.648,32 | €45,68 | €0,00 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21967 | 0,22262 | 0,21398 | 0,11094 | 0,23107 | €12,67 | €25,34 | €0,66 | €0,34 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €0,00 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 937,37744 | 947,48000 | 904,92697 | 473,37561 | 1002,27837 | €22,86 | €45,71 | €1,58 | €0,49 |
| Master Adaptive Gb20 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17350 | 0,17350 | 0,16618 | 0,08762 | 0,18815 | €19,05 | €38,10 | €1,61 | €0,00 |
| Master Adaptive Gb20 V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,20200 | 6,15558 | 3,25437 | 7,02170 | €13,41 | €26,82 | €1,20 | €-1,01 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01473 | 0,01459 | 0,01296 | 0,00744 | 0,01827 | €201,20 | €402,40 | €48,29 | €-3,76 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,75415 | 0,73459 | 0,38085 | 0,81282 | €26,15 | €52,29 | €1,36 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €0,00 |
| Master Adaptive Runner25 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21967 | 0,22262 | 0,21398 | 0,11094 | 0,23676 | €49,36 | €98,72 | €2,56 | €1,32 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 944,01877 | 947,48000 | 909,98143 | 476,72948 | 1046,13077 | €544,41 | €1.088,83 | €39,26 | €3,99 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,22145 | 0,22262 | 0,21557 | 0,11183 | 0,23323 | €14,03 | €28,06 | €0,75 | €0,15 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €0,00 |
| Master Adaptive Gb20 Be V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 937,37744 | 947,48000 | 904,92697 | 473,37561 | 1002,27837 | €23,28 | €46,55 | €1,61 | €0,50 |
| Master Adaptive Gb20 Be V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17350 | 0,17350 | 0,16618 | 0,08762 | 0,18815 | €19,51 | €39,02 | €1,65 | €0,00 |
| Master Adaptive Gb20 Be V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,20200 | 6,15558 | 3,25437 | 7,02170 | €13,65 | €27,31 | €1,22 | €-1,03 |
| Master Adaptive Gb20 Be V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01473 | 0,01459 | 0,01296 | 0,00744 | 0,01827 | €204,90 | €409,80 | €49,18 | €-3,83 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 937,37744 | 947,48000 | 904,92697 | 473,37561 | 1002,27837 | €23,25 | €46,50 | €1,61 | €0,50 |
| Master Adaptive Gb20 Partial V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17350 | 0,17350 | 0,16618 | 0,08762 | 0,18815 | €19,49 | €38,98 | €1,65 | €0,00 |
| Master Adaptive Gb20 Partial V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,20200 | 6,15558 | 3,25437 | 7,02170 | €13,64 | €27,28 | €1,22 | €-1,03 |
| Master Adaptive Gb20 Partial V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01473 | 0,01459 | 0,01296 | 0,00744 | 0,01827 | €204,68 | €409,37 | €49,12 | €-3,83 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,76865 | 0,76865 | 0,75233 | 0,38817 | 0,81217 | €50,74 | €101,48 | €2,15 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 937,37744 | 947,48000 | 913,03959 | 473,37561 | 1002,27837 | €30,68 | €61,37 | €1,59 | €0,66 |
| Master Adaptive Gb20 Loss Cap V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,29726 | 6,20200 | 6,08916 | 3,18012 | 6,85220 | €29,83 | €59,65 | €1,97 | €-0,90 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01473 | 0,01459 | 0,01296 | 0,00744 | 0,01945 | €198,13 | €396,25 | €47,55 | €-3,71 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,22262 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-216,81 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,22262 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-10,12 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,78276 | 0,78276 | 0,76671 | 0,52575 | 0,80682 | €850,18 | €2.550,53 | €52,28 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17350 | 0,17350 | 0,16781 | 0,11654 | 0,18205 | €10,80 | €32,40 | €1,06 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 87,10142 | 86,40800 | 85,63037 | 58,50312 | 89,30798 | €23,69 | €71,07 | €1,20 | €-0,57 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01459 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €187,89 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2506,59000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,84 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | UNI | LONG | Confluenza trend | 240m | 3,0x | 5,86517 | 6,20200 | 5,34904 | 3,93944 | 6,89744 | €216,26 | €648,78 | €57,09 | €37,26 |
| Main Side Regime Guard V1 | XMR | LONG | Confluenza trend | 240m | 3,0x | 514,15281 | 514,15281 | 470,71063 | 345,33930 | 601,03718 | €9,05 | €27,15 | €2,29 | €0,00 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | SUI | LONG | Combo Trend | 60m | 2,0x | 0,77495 | 0,77495 | 0,75109 | 0,39135 | 0,82745 | €843,75 | €1.687,49 | €51,96 | €0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €0,00 |
| Combo Trend Side Regime Guard V1 | ADA | LONG | Combo Trend | 60m | 2,0x | 0,22156 | 0,22262 | 0,21507 | 0,11189 | 0,23585 | €13,15 | €26,30 | €0,77 | €0,13 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 86,53430 | 86,40800 | 85,06318 | 58,12221 | 88,74098 | €17,54 | €52,63 | €0,89 | €-0,08 |
| 1H Fast Nohigh Cap75 Short Only V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 940,09798 | 947,48000 | 915,36901 | 631,43248 | 977,19145 | €567,79 | €1.703,38 | €44,81 | €13,38 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,22262 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-167,56 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €0,00 |
| 1H Balanced V3 Long Only V1 | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17350 | 0,17350 | 0,16618 | 0,11654 | 0,18815 | €9,39 | €28,17 | €1,19 | €0,00 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 87,10142 | 86,40800 | 85,21007 | 58,50312 | 90,88410 | €643,04 | €1.929,12 | €41,89 | €-15,36 |
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
| Donchian 1H Gb20 120R V1 | UNI | LONG | 2026-09-04T05:00:00+00:00 | 6,21953 | €43,14 | 0,78 | STOP |
| Benchmark Donchian breakout 1H | UNI | LONG | 2026-09-04T05:00:00+00:00 | 6,21953 | €44,18 | 0,78 | STOP |
| Benchmark Bollinger mean reversion 1H | ADA | SHORT | 2026-09-04T04:45:00+00:00 | 0,22639 | €-45,71 | -1,06 | STOP |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ADA | LONG | 2026-09-04T04:45:00+00:00 | 0,22627 | €68,36 | 1,42 | TARGET |
| Master Adaptive V1 | USELESS | LONG | 2026-09-04T03:15:00+00:00 | 0,21743 | €96,68 | 1,98 | TARGET |
| Master Adaptive Gb20 V1 | USELESS | LONG | 2026-09-04T03:15:00+00:00 | 0,21743 | €95,40 | 1,98 | TARGET |
| Master Adaptive Gb20 Partial V1 | USELESS | LONG | 2026-09-04T03:15:00+00:00 | 0,21743 | €97,05 | 1,98 | TARGET |
| Master Adaptive Gb20 Loss Cap V1 | USELESS | LONG | 2026-09-04T03:15:00+00:00 | 0,21743 | €124,47 | 2,65 | TARGET |
| Master Adaptive Gb20 Be V1 | USELESS | LONG | 2026-09-04T03:15:00+00:00 | 0,21743 | €97,16 | 1,98 | TARGET |
| 1H Fast V3 No Esports V1 | BTC | LONG | 2026-09-04T02:30:00+00:00 | 80674,93300 | €-0,32 | -1,12 | STOP |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | LONG | 2026-09-04T02:30:00+00:00 | 80674,93300 | €-0,35 | -1,12 | STOP |
| Rapida 1H V3 Filtered | BTC | LONG | 2026-09-04T02:30:00+00:00 | 80674,93300 | €-0,34 | -1,12 | STOP |

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

Generato: 2026-09-04 05:32 UTC


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

Segnali totali salvati: **168**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-04 | BTC | 80.963,98 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-04 | DOGE | 0.08695 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-04 | SOL | 103,67 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-03 | BTC | 77.295,19 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-03 | DOGE | 0.08235 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-03 | SOL | 100,15 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-02 | BTC | 77.662,37 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-02 | DOGE | 0.08189 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-02 | SOL | 100,25 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-01 | BTC | 79.026,52 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-01 | DOGE | 0.08350 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-01 | SOL | 104,07 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 56 | 55 | 54 | 53 | 51 | 49 | 46 | 42 | 35 | 28 | 13 | 0 |
| SOL | 56 | 55 | 54 | 53 | 51 | 49 | 46 | 42 | 35 | 28 | 13 | 0 |
| DOGE | 56 | 55 | 54 | 53 | 51 | 49 | 46 | 42 | 35 | 28 | 13 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-22 | 45g | 2026-09-05 | domani |
| SOL | 2026-07-22 | 45g | 2026-09-05 | domani |
| DOGE | 2026-07-22 | 45g | 2026-09-05 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 52 | 51,92% | +0,50% | +0,48% | PRIMA CALIBRAZIONE |
| BTC | 2g | 51 | 52,94% | +0,80% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 3g | 50 | 48,00% | +0,99% | +0,85% | PRIMA CALIBRAZIONE |
| BTC | 5g | 48 | 43,75% | +1,99% | +1,73% | PRIMA CALIBRAZIONE |
| BTC | 7g | 46 | 52,17% | +2,75% | +2,51% | PRIMA CALIBRAZIONE |
| BTC | 10g | 43 | 58,14% | +4,01% | +3,79% | PRIMA CALIBRAZIONE |
| BTC | 14g | 39 | 64,10% | +6,23% | +6,14% | PRIMA CALIBRAZIONE |
| BTC | 21g | 33 | 57,58% | +8,75% | +8,55% | PRIMA CALIBRAZIONE |
| BTC | 30g | 26 | 88,46% | +12,19% | +10,54% | FEEDBACK RAPIDO |
| BTC | 45g | 12 | 83,33% | +22,74% | +15,31% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 48 | 56,25% | +0,71% | +0,58% | PRIMA CALIBRAZIONE |
| SOL | 2g | 47 | 51,06% | +1,35% | +1,20% | PRIMA CALIBRAZIONE |
| SOL | 3g | 46 | 56,52% | +2,12% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 5g | 44 | 61,36% | +3,70% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 7g | 42 | 66,67% | +5,33% | +5,45% | PRIMA CALIBRAZIONE |
| SOL | 10g | 39 | 71,79% | +7,52% | +7,72% | PRIMA CALIBRAZIONE |
| SOL | 14g | 35 | 77,14% | +10,78% | +11,82% | PRIMA CALIBRAZIONE |
| SOL | 21g | 28 | 71,43% | +13,70% | +12,43% | FEEDBACK RAPIDO |
| SOL | 30g | 21 | 52,38% | +15,09% | +5,68% | FEEDBACK RAPIDO |
| SOL | 45g | 12 | 33,33% | +32,98% | -13,41% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 51 | 45,10% | +0,48% | +0,24% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 50 | 50,00% | +0,86% | +0,71% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 49 | 44,90% | +1,19% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 48 | 54,17% | +1,96% | +2,61% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 46 | 60,87% | +2,58% | +3,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 44 | 59,09% | +2,87% | +4,29% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 40 | 72,50% | +5,89% | +8,21% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 33 | 75,76% | +7,22% | +6,02% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 26 | 69,23% | +9,39% | +0,81% | FEEDBACK RAPIDO |
| DOGE | 45g | 13 | 0,00% | +18,68% | -18,68% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 52 | 51,92% | +0,50% | +0,48% | +0,04% | +1,06% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 55 | 54,55% | +0,47% | +0,47% | +0,02% | +1,01% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +0,47% | +0,47% | +0,02% | +1,01% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 50 | 40,00% | +0,61% | +0,20% | +0,14% | +1,16% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 23 | 39,13% | +0,92% | +0,46% | +0,22% | +1,45% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 51 | 52,94% | +0,80% | +0,71% | +0,21% | +1,47% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 54 | 55,56% | +0,90% | +0,90% | +0,32% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +0,90% | +0,90% | +0,32% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 49 | 44,90% | +1,09% | +0,25% | +0,51% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 22 | 40,91% | +1,21% | +0,52% | +0,63% | +1,86% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 50 | 48,00% | +0,99% | +0,85% | -0,98% | +2,64% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 53 | 56,60% | +1,30% | +1,30% | -0,96% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 53 | 56,60% | +1,30% | +1,30% | -0,96% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 48 | 37,50% | +1,65% | -0,11% | -0,77% | +3,18% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,85% | +0,02% | -0,61% | +3,28% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 48 | 43,75% | +1,99% | +1,73% | -1,51% | +4,15% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 51 | 50,98% | +2,25% | +2,25% | -1,48% | +4,48% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 51 | 50,98% | +2,25% | +2,25% | -1,48% | +4,48% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 46 | 41,30% | +2,62% | -1,07% | -1,26% | +4,89% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 19 | 42,11% | +4,39% | -1,73% | -0,88% | +6,44% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 46 | 52,17% | +2,75% | +2,51% | -1,73% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 49 | 59,18% | +3,09% | +3,09% | -1,71% | +5,71% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 49 | 59,18% | +3,09% | +3,09% | -1,71% | +5,71% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 44 | 38,64% | +3,69% | -2,10% | -1,48% | +6,23% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 17 | 35,29% | +6,57% | -4,27% | -0,94% | +9,46% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 43 | 58,14% | +4,01% | +3,79% | -1,87% | +6,72% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 46 | 63,04% | +4,17% | +4,17% | -1,88% | +6,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 46 | 63,04% | +4,17% | +4,17% | -1,88% | +6,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 41 | 41,46% | +4,82% | -1,67% | -1,60% | +7,68% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 14 | 42,86% | +9,05% | -6,02% | -0,58% | +11,93% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 39 | 64,10% | +6,23% | +6,14% | -2,05% | +9,54% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 42 | 64,29% | +6,27% | +6,27% | -2,06% | +9,62% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 42 | 64,29% | +6,27% | +6,27% | -2,06% | +9,62% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 37 | 59,46% | +7,29% | +0,74% | -1,74% | +10,69% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 10 | 40,00% | +11,72% | -7,93% | -0,10% | +15,43% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 33 | 57,58% | +8,75% | +8,55% | -2,87% | +12,32% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 35 | 65,71% | +8,19% | +8,19% | -2,92% | +11,76% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 35 | 65,71% | +8,19% | +8,19% | -2,92% | +11,76% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 31 | 70,97% | +9,42% | +9,42% | -2,71% | +12,97% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 30 | 36,67% | +9,29% | +0,89% | -2,66% | +12,92% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 5 | 0,00% | +15,15% | -15,15% | -1,27% | +17,36% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 26 | 88,46% | +12,19% | +10,54% | -2,89% | +16,05% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 28 | 82,14% | +11,90% | +11,90% | -2,94% | +15,85% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 28 | 82,14% | +11,90% | +11,90% | -2,94% | +15,85% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 24 | 83,33% | +13,09% | +13,09% | -2,68% | +17,31% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 23 | 30,43% | +11,72% | -7,90% | -2,61% | +16,07% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 12 | 83,33% | +22,74% | +15,31% | -2,86% | +26,54% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 13 | 100,00% | +22,82% | +22,82% | -2,84% | +26,60% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 13 | 100,00% | +22,82% | +22,82% | -2,84% | +26,60% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 11 | 36,36% | +22,95% | -6,68% | -2,60% | +27,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 51 | 45,10% | +0,48% | +0,24% | -0,15% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 54 | 57,41% | +0,36% | +0,54% | -0,29% | +1,31% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 54 | 57,41% | +0,36% | +0,54% | -0,29% | +1,31% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 48 | 54,17% | +0,26% | +0,44% | -0,41% | +1,20% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 50 | 50,00% | +0,86% | +0,71% | +0,09% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 53 | 56,60% | +0,63% | +1,00% | -0,12% | +1,83% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 53 | 56,60% | +0,63% | +1,00% | -0,12% | +1,83% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 47 | 55,32% | +0,19% | +0,58% | -0,54% | +1,36% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 49 | 44,90% | +1,19% | +1,30% | -1,66% | +4,05% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +0,96% | +1,54% | -1,83% | +3,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +0,96% | +1,54% | -1,83% | +3,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 46 | 43,48% | +0,00% | +0,37% | -2,15% | +2,55% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 48 | 54,17% | +1,96% | +2,61% | -2,54% | +6,28% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 50 | 54,00% | +1,76% | +2,70% | -2,63% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 50 | 54,00% | +1,76% | +2,70% | -2,63% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 44 | 54,55% | +0,51% | +0,22% | -3,15% | +4,68% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 46 | 60,87% | +2,58% | +3,74% | -2,92% | +8,27% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 48 | 60,42% | +2,48% | +3,59% | -3,01% | +7,90% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 48 | 60,42% | +2,48% | +3,59% | -3,01% | +7,90% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 42 | 54,76% | +0,88% | +0,91% | -3,64% | +6,22% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +0,39% | +0,24% | -1,74% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 44 | 59,09% | +2,87% | +4,29% | -3,37% | +9,83% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +2,67% | +4,05% | -3,42% | +9,45% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +2,67% | +4,05% | -3,42% | +9,45% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 39 | 61,54% | +0,48% | +1,45% | -4,06% | +6,89% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,00% | -0,43% | -2,75% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 40 | 72,50% | +5,89% | +8,21% | -3,00% | +14,57% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 42 | 76,19% | +5,51% | +7,74% | -3,07% | +13,93% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 42 | 76,19% | +5,51% | +7,74% | -3,07% | +13,93% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 35 | 68,57% | +1,94% | +1,44% | -3,72% | +9,28% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 27 | 51,85% | +4,09% | -4,09% | -3,41% | +12,32% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +12,07% | +4,21% | +0,53% | +20,35% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 33 | 75,76% | +7,22% | +6,02% | -4,17% | +16,58% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 35 | 85,71% | +7,39% | +10,77% | -4,19% | +16,86% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 35 | 85,71% | +7,39% | +10,77% | -4,19% | +16,86% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 33 | 87,88% | +7,91% | +11,35% | -4,22% | +17,61% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 23 | 65,22% | +3,23% | -3,23% | -4,58% | +10,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 26 | 69,23% | +9,39% | +0,81% | -5,08% | +20,88% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 28 | 85,71% | +10,27% | +8,63% | -5,04% | +22,25% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 28 | 85,71% | +10,27% | +8,63% | -5,04% | +22,25% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 26 | 92,31% | +8,91% | +11,45% | -5,14% | +21,10% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 28 | 42,86% | +10,27% | -10,27% | -5,04% | +22,25% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 12 | 0,00% | +18,98% | -18,98% | -6,50% | +36,87% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 48 | 56,25% | +0,71% | +0,58% | +0,03% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 50 | 58,00% | +0,39% | +0,37% | -0,22% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 53 | 56,60% | +0,43% | +0,29% | -0,18% | +1,31% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 52 | 51,92% | +0,39% | +0,36% | -0,26% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 36 | 52,78% | +0,61% | +0,57% | -0,16% | +1,57% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 47 | 51,06% | +1,35% | +1,20% | +0,44% | +2,44% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 49 | 46,94% | +0,94% | +0,45% | +0,02% | +1,75% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 52 | 46,15% | +0,90% | +0,40% | +0,01% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 51 | 43,14% | +0,83% | +0,23% | -0,02% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 35 | 51,43% | +0,95% | +0,93% | +0,09% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 46 | 56,52% | +2,12% | +1,93% | -1,34% | +4,37% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 48 | 47,92% | +1,57% | +0,96% | -1,67% | +3,82% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 51 | 47,06% | +1,50% | +0,88% | -1,64% | +3,80% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 50 | 48,00% | +1,34% | +0,03% | -1,73% | +3,51% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 34 | 52,94% | +1,26% | +1,10% | -1,70% | +3,45% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 44 | 61,36% | +3,70% | +3,57% | -1,86% | +7,12% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 46 | 54,35% | +2,93% | +1,75% | -2,21% | +6,35% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 49 | 53,06% | +2,79% | +1,60% | -2,20% | +6,20% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 48 | 47,92% | +2,80% | -0,52% | -2,36% | +6,09% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 32 | 59,38% | +2,05% | +1,87% | -2,26% | +5,26% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 42 | 66,67% | +5,33% | +5,45% | -2,07% | +9,34% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +4,42% | +2,98% | -2,44% | +8,48% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 47 | 61,70% | +4,13% | +2,79% | -2,46% | +8,19% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 46 | 41,30% | +4,09% | -1,36% | -2,64% | +8,13% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 30 | 53,33% | +2,40% | +2,46% | -2,57% | +6,46% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 39 | 71,79% | +7,52% | +7,72% | -2,27% | +11,88% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 41 | 65,85% | +6,49% | +5,38% | -2,74% | +10,62% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 44 | 63,64% | +6,03% | +5,02% | -2,79% | +10,16% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 43 | 48,84% | +5,37% | -2,45% | -3,01% | +9,70% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 27 | 62,96% | +2,36% | +2,49% | -2,97% | +7,06% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +2,90% | +2,90% | -3,71% | +8,09% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 35 | 77,14% | +10,78% | +11,82% | -2,74% | +16,41% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 37 | 83,78% | +10,09% | +10,26% | -3,14% | +14,92% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 40 | 85,00% | +9,10% | +9,72% | -3,19% | +14,09% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,71% | +10,82% | -2,97% | +15,49% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 39 | 33,33% | +7,43% | -6,23% | -3,51% | +12,61% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 23 | 43,48% | +2,55% | +0,38% | -3,66% | +6,91% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 28 | 71,43% | +13,70% | +12,43% | -4,67% | +19,58% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 31 | 83,87% | +13,88% | +15,68% | -4,60% | +19,06% | PRIMA CALIBRAZIONE |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +12,41% | +14,54% | -4,73% | +17,73% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 29 | 68,97% | +15,02% | +15,61% | -4,31% | +20,29% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 33 | 36,36% | +10,52% | -11,76% | -4,96% | +15,64% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |

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

Generato: 2026-09-04 05:33 UTC

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
| BTC | 56 | PRIMA CALIBRAZIONE | 55 | 16 | 0 | 0 | Famiglia statistica | 1g | 54,55% | +0,47% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 56 | PRIMA CALIBRAZIONE | 52 | 21 | 0 | 0 | Tecnico | 1g | 51,92% | +0,36% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 56 | PRIMA CALIBRAZIONE | 54 | 22 | 0 | 0 | Famiglia statistica | 1g | 57,41% | +0,54% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 23 | 39,13% | +0,46% | +0,92% | +0,22% | +1,45% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 55 | 54,55% | +0,47% | +0,47% | +0,02% | +1,01% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 50 | 40,00% | +0,20% | +0,61% | +0,14% | +1,16% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 22 | 40,91% | +0,52% | +1,21% | +0,63% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 54 | 55,56% | +0,90% | +0,90% | +0,32% | +1,56% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 49 | 44,90% | +0,25% | +1,09% | +0,51% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 21 | 38,10% | +0,02% | +1,85% | -0,61% | +3,28% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 53 | 56,60% | +1,30% | +1,30% | -0,96% | +2,88% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 48 | 37,50% | -0,11% | +1,65% | -0,77% | +3,18% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 19 | 42,11% | -1,73% | +4,39% | -0,88% | +6,44% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 51 | 50,98% | +2,25% | +2,25% | -1,48% | +4,48% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 46 | 41,30% | -1,07% | +2,62% | -1,26% | +4,89% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 17 | 35,29% | -4,27% | +6,57% | -0,94% | +9,46% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 49 | 59,18% | +3,09% | +3,09% | -1,71% | +5,71% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 44 | 38,64% | -2,10% | +3,69% | -1,48% | +6,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 14 | 42,86% | -6,02% | +9,05% | -0,58% | +11,93% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 46 | 63,04% | +4,17% | +4,17% | -1,88% | +6,98% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 41 | 41,46% | -1,67% | +4,82% | -1,60% | +7,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 10 | 40,00% | -7,93% | +11,72% | -0,10% | +15,43% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 42 | 64,29% | +6,27% | +6,27% | -2,06% | +9,62% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 37 | 59,46% | +0,74% | +7,29% | -1,74% | +10,69% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 5 | 0,00% | -15,15% | +15,15% | -1,27% | +17,36% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 35 | 65,71% | +8,19% | +8,19% | -2,92% | +11,76% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 30 | 36,67% | +0,89% | +9,29% | -2,66% | +12,92% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 28 | 82,14% | +11,90% | +11,90% | -2,94% | +15,85% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 23 | 30,43% | -7,90% | +11,72% | -2,61% | +16,07% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 13 | 100,00% | +22,82% | +22,82% | -2,84% | +26,60% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 11 | 36,36% | -6,68% | +22,95% | -2,60% | +27,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 54 | 57,41% | +0,54% | +0,36% | -0,29% | +1,31% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 48 | 54,17% | +0,44% | +0,26% | -0,41% | +1,20% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 53 | 56,60% | +1,00% | +0,63% | -0,12% | +1,83% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 47 | 55,32% | +0,58% | +0,19% | -0,54% | +1,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 52 | 55,77% | +1,54% | +0,96% | -1,83% | +3,64% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 46 | 43,48% | +0,37% | +0,00% | -2,15% | +2,55% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 50 | 54,00% | +2,70% | +1,76% | -2,63% | +5,92% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 44 | 54,55% | +0,22% | +0,51% | -3,15% | +4,68% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 48 | 60,42% | +3,59% | +2,48% | -3,01% | +7,90% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +0,24% | +0,39% | -1,74% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 42 | 54,76% | +0,91% | +0,88% | -3,64% | +6,22% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 46 | 58,70% | +4,05% | +2,67% | -3,42% | +9,45% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 7 | 57,14% | -0,43% | +0,00% | -2,75% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 39 | 61,54% | +1,45% | +0,48% | -4,06% | +6,89% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 27 | 51,85% | -4,09% | +4,09% | -3,41% | +12,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 42 | 76,19% | +7,74% | +5,51% | -3,07% | +13,93% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +4,21% | +12,07% | +0,53% | +20,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 35 | 68,57% | +1,44% | +1,94% | -3,72% | +9,28% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 23 | 65,22% | -3,23% | +3,23% | -4,58% | +10,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 35 | 85,71% | +10,77% | +7,39% | -4,19% | +16,86% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 20 | 55,00% | -7,30% | +7,30% | -5,27% | +16,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 28 | 85,71% | +8,63% | +10,27% | -5,04% | +22,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 28 | 42,86% | -10,27% | +10,27% | -5,04% | +22,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 12 | 0,00% | -18,98% | +18,98% | -6,50% | +36,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 13 | 0,00% | -18,68% | +18,68% | -6,62% | +36,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 13 | 0,00% | -18,68% | +18,68% | -6,62% | +36,75% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 36 | 52,78% | +0,57% | +0,61% | -0,16% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 50 | 58,00% | +0,37% | +0,39% | -0,22% | +1,28% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 52 | 51,92% | +0,36% | +0,39% | -0,26% | +1,24% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 35 | 51,43% | +0,93% | +0,95% | +0,09% | +1,92% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 49 | 46,94% | +0,45% | +0,94% | +0,02% | +1,75% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 51 | 43,14% | +0,23% | +0,83% | -0,02% | +1,92% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 34 | 52,94% | +1,10% | +1,26% | -1,70% | +3,45% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 48 | 47,92% | +0,96% | +1,57% | -1,67% | +3,82% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 50 | 48,00% | +0,03% | +1,34% | -1,73% | +3,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 32 | 59,38% | +1,87% | +2,05% | -2,26% | +5,26% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 46 | 54,35% | +1,75% | +2,93% | -2,21% | +6,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 48 | 47,92% | -0,52% | +2,80% | -2,36% | +6,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 30 | 53,33% | +2,46% | +2,40% | -2,57% | +6,46% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 44 | 61,36% | +2,98% | +4,42% | -2,44% | +8,48% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 46 | 41,30% | -1,36% | +4,09% | -2,64% | +8,13% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 27 | 62,96% | +2,49% | +2,36% | -2,97% | +7,06% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 41 | 65,85% | +5,38% | +6,49% | -2,74% | +10,62% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +2,90% | +2,90% | -3,71% | +8,09% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 43 | 48,84% | -2,45% | +5,37% | -3,01% | +9,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 23 | 43,48% | +0,38% | +2,55% | -3,66% | +6,91% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 37 | 83,78% | +10,26% | +10,09% | -3,14% | +14,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 39 | 33,33% | -6,23% | +7,43% | -3,51% | +12,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 31 | 83,87% | +15,68% | +13,88% | -4,60% | +19,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 33 | 36,36% | -11,76% | +10,52% | -4,96% | +15,64% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 20 | 10,00% | -25,57% | +25,57% | -4,94% | +31,98% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 24 | 87,50% | +20,66% | +21,10% | -5,75% | +27,16% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 28 | 14,29% | -18,82% | +18,15% | -5,91% | +23,83% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 5 | 0,00% | -35,45% | +35,45% | -6,51% | +45,53% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 9 | 22,22% | -15,43% | +30,22% | -7,97% | +37,85% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 13 | 30,77% | -16,90% | +32,04% | -7,63% | +39,27% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 52 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 55 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 66 | 39,39% | +0,34% |
| BTC | BREVE | Famiglia statistica | 162 | 55,56% | +0,88% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 147 | 40,82% | +0,11% |
| BTC | SETTIMANALE | Classic technical | 50 | 40,00% | -3,79% |
| BTC | SETTIMANALE | Famiglia statistica | 146 | 57,53% | +3,14% |
| BTC | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | +0,53% |
| BTC | SETTIMANALE | Tecnico | 131 | 40,46% | -1,60% |
| BTC | SWING | Classic technical | 15 | 26,67% | -10,34% |
| BTC | SWING | Famiglia statistica | 77 | 64,94% | +7,14% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 67 | 49,25% | +0,80% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 41 | 87,80% | +15,36% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 34 | 32,35% | -7,51% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 159 | 56,60% | +1,02% |
| DOGE | BREVE | Microstruttura exchange | 24 | 54,17% | +2,59% |
| DOGE | BREVE | Tecnico | 141 | 51,06% | +0,46% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 144 | 57,64% | +3,43% |
| DOGE | SETTIMANALE | Microstruttura exchange | 22 | 45,45% | +0,43% |
| DOGE | SETTIMANALE | Tecnico | 125 | 56,80% | +0,84% |
| DOGE | SWING | Classic technical | 50 | 58,00% | -3,70% |
| DOGE | SWING | Famiglia statistica | 77 | 80,52% | +9,12% |
| DOGE | SWING | Microstruttura exchange | 9 | 77,78% | +1,92% |
| DOGE | SWING | Tecnico | 65 | 66,15% | -1,54% |
| DOGE | MEDIO | Classic technical | 32 | 34,38% | -11,68% |
| DOGE | MEDIO | Famiglia statistica | 41 | 58,54% | -0,03% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 41 | 29,27% | -12,94% |
| SOL | BREVE | Classic technical | 105 | 52,38% | +0,86% |
| SOL | BREVE | Famiglia statistica | 147 | 51,02% | +0,59% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 153 | 47,71% | +0,21% |
| SOL | SETTIMANALE | Classic technical | 89 | 58,43% | +2,26% |
| SOL | SETTIMANALE | Famiglia statistica | 131 | 60,31% | +3,30% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 14 | 64,29% | +2,88% |
| SOL | SETTIMANALE | Tecnico | 137 | 45,99% | -1,41% |
| SOL | SWING | Classic technical | 44 | 40,91% | -5,14% |
| SOL | SWING | Famiglia statistica | 68 | 83,82% | +12,73% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 5 | 60,00% | +13,52% |
| SOL | SWING | Tecnico | 72 | 34,72% | -8,76% |
| SOL | MEDIO | Classic technical | 25 | 8,00% | -27,54% |
| SOL | MEDIO | Famiglia statistica | 33 | 69,70% | +10,82% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 2 | 100,00% | +20,54% |
| SOL | MEDIO | Tecnico | 41 | 19,51% | -18,21% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 8 | in attesa di controlli maturati |
| SOL | MEDIO | 5 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 8 | in attesa di controlli maturati |

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
| BTC     |         56 |              28 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         56 |              28 |          28 | RACCOLTA DATI | 3,57%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         56 |              28 |          28 | RACCOLTA DATI | 7,14%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-09-04 05:32 UTC


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
| BTC | +8 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | Prima resistenza sopra 81.347; conferma del doppio minimo sopra 66.910. | Sotto 62.488 il quadro tecnico peggiora. |
| SOL | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 108,85 / 129,91, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 86,03 / 74,20 / 62,19. |
| DOGE | -1 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | EVITA LONG / SOLO RIMBALZI VELOCI | Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +8 |
| SOL | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +6 |
| DOGE | -2 | 0 | -2 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -1 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+8**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**

BTC ha una confluenza positiva forte. Resta comunque necessario evitare leva eccessiva: la conferma deve arrivare da prezzo e resistenze, non solo dallo score.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 82,50%, return centrale 30g +12,86%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 100,00%, return p50 +32,46%.
- Scanner path: **0** — Controlli disponibili 53. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 5/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 81.347; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+6**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 67,50%, return centrale 30g +13,97%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 50,00%, return p50 +9,15%.
- Scanner path: **0** — Controlli disponibili 53. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 9/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 7/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +66,88%, aderenza live +71,40%, errore live +14,30%, gap corrente +8,18%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 50, ma percorso ancorato non aderente: gap +8,18%, errore live +14,30%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,31 $, upside EMA200 +7,40%, gap EMA50/EMA200 -5,78%, hit EMA200 12w +80,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 108,85 / 129,91, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 86,03 / 74,20 / 62,19.

### DOGE

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **EVITA LONG / SOLO RIMBALZI VELOCI**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 30,00%, return centrale 30g -8,81%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 53. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 5/12, verdetto costruttivo ma non confermato, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Triplo minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 1/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — DOGE: cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-09-04 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 80.964 $ | prezzo corrente |
| Power Law centrale | 124.595 $ | deviazione -35,02% |
| Banda p10-p90 | 77.396 $ / 314.719 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 14,74% | posizione storica nel corridoio |
| Esponente β | 5,8067 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3166 cambiando finestra |
| Ultimo halving | 2024-04-19 | 868 giorni fa |
| Fase ciclo | 59,41% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-04 (4370 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0825) × giorni^5.8067
- Prezzo centrale oggi: **124.595 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 14,74%
- Scarto dal centro: **-35,02%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8067 | 91,93% |
| 2015 | 5,8892 | 91,48% |
| 2016 | 5,5735 | 87,73% |
| 2017 | 4,8453 | 82,90% |
| 2018 | 4,5727 | 78,40% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-21 | +7,44% | +3,69% | +22,95% | +80,81% |
| 2016-07-09 → 2020-05-11 | 2018-10-20 | -24,93% | -43,63% | -18,35% | +26,70% |
| 2020-05-11 → 2024-04-19 | 2022-09-13 | -4,50% | -15,23% | +9,20% | +29,22% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 11.311897473605526 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -1.7862194060969339 | 0 |

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

Generato: 2026-09-04 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00128120 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +11,31% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000107 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -1,79% | RIALZISTA | SALE SOLO IN USD: BTC resta più forte |

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
- **Rendimenti relativi:** 7g -5,86%; 30g +11,31%; 90g +23,19%; 180g +3,57%
- **Daily:** RSI 55.82; MA50 0.00120300; MA200 0.00118116
- **Weekly:** MA30 0.00118497; RSI 54.66
- **Livelli:** supporto 0.00122200; resistenza 0.00129400; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** SALE SOLO IN USD: BTC resta più forte
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -3,31%; 30g -1,79%; 90g -19,58%; 180g -19,67%
- **Daily:** RSI 44.22; MA50 0.00000110; MA200 0.00000127
- **Weekly:** MA30 0.00000127; RSI 36.26
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000100
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 206 | 52,43% | +1,98% | -1,06% |
| SOL | 30g | 204 | 47,06% | +4,50% | +0,44% |
| SOL | 90g | 198 | 53,03% | +10,08% | +2,72% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 293 | 53,24% | +1,99% | -3,49% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 31 | 58,06% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 29 | 51,72% | +0,46% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 25 | 52,00% | +1,04% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 18 | 22,22% | -1,43% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 12 | 0,00% | -12,06% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 44 | 68,18% | +0,11% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 42 | 61,90% | +0,46% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 38 | 65,79% | +0,58% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 35 | 68,57% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 26 | 76,92% | +1,16% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **4 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 103,67 $ | 2026-09-04T05:30:23Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 103,61 $ | 2026-09-04T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,06000 $ | -0,06% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=103.66999816894531
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-04T05:30:23Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=103.61000061035156
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-04T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-04T05:32:11Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=109.04585
ANCHOR_AGE_HOURS=0.030290513888888888
CURRENT_VS_ANCHOR_GAP_USD=-0.05999755859375
CURRENT_VS_ANCHOR_GAP_PCT=-0.057873598585367336
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +66,88%
- **Somiglianza strutturale:** +66,88%
- **Aderenza prezzo live:** +71,40%
- **Errore medio live:** +14,30%
- **Gap prezzo corrente:** +8,18%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 90 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-19
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Laterale / movimento non forte.** Zona bassa **95,26 $** intorno al **17 settembre 2026**; zona alta **105,81 $** intorno al **5 settembre 2026**; fine step circa **95,61 $** entro il **18 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=14.30249282534533
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=8.178586451032555
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 4 settembre 2026 | 64 | +71,40% | +14,30% | +8,18% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 4 settembre 2026 | 91 | +76,31% | +11,85% | +8,18% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +71,40% | Errore medio live +14,30%. |
| Gap corrente | +8,18% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 108,85 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 129,91 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 86,03 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 531,62 $ |
| Massimo percorso base | 531,62 $ (21 aprile 2029) |

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
| Prima conferma | 108,85 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 129,91 $ | Scenario più credibile. |
| Invalidazione soft | 86,03 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 11 settembre 2026 | -3,15% | 100,40 $ | 98,76 $ | 105,81 $ |
| 14 giorni | 18 settembre 2026 | -7,78% | 95,61 $ | 95,26 $ | 105,81 $ |
| 30 giorni | 4 ottobre 2026 | +15,82% | 120,07 $ | 86,03 $ | 120,07 $ |
| 60 giorni | 3 novembre 2026 | +16,11% | 120,37 $ | 86,03 $ | 129,91 $ |
| 90 giorni | 3 dicembre 2026 | +11,52% | 115,61 $ | 86,03 $ | 129,91 $ |
| 120 giorni | 2 gennaio 2027 | +10,37% | 114,42 $ | 86,03 $ | 129,91 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 4 settembre 2026 -> 18 settembre 2026 | -7,78% | 95,26 $ (17 settembre 2026) | 105,81 $ (5 settembre 2026) | 95,61 $ | Laterale / movimento non forte. |
| Step 2 - primo mese | 19 settembre 2026 -> 4 ottobre 2026 | +15,82% | 86,03 $ (23 settembre 2026) | 120,07 $ (4 ottobre 2026) | 120,07 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 5 ottobre 2026 -> 3 novembre 2026 | +16,11% | 115,65 $ (10 ottobre 2026) | 129,91 $ (28 ottobre 2026) | 120,37 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 4 novembre 2026 -> 3 dicembre 2026 | +11,52% | 114,14 $ (26 novembre 2026) | 125,86 $ (18 novembre 2026) | 115,61 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 103,67 $ |  |
| Weekly RSI | 58,88 / linea grezza 52,47 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 47,12 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 531,62 $ | Avanzamento +19,50% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 47,1, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | 0 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 103,67 $ |
| TVL Solana | 5,91 mld $ |
| TVL 7g | -1,70% |
| DEX volume 24h | 2,37 mld $ |
| Fees 24h | 10,97 mln $ |
| Stablecoin su Solana | 16,58 mld $ |
| Stake ratio | 68,97% |
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
| Prezzo SOL | 103,67 $ |
| EMA200 weekly target | 111,31 $ |
| Upside verso EMA200 | +7,40% |
| Distanza prezzo da EMA200 | -6,89% |
| Gap EMA50/EMA200 | -5,78% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 58,87 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +80,00% |
| Max gain mediano 12w | +20,12% |
| Drawdown mediano 12w | -38,91% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-04 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-04 05:30:23 UTC**

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
- SOL: cambiamento importante in peggioramento rispetto a ieri.
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +82.50% | +5.00 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +67.50% | -2.50 punti |
| DOGE | CAMBIAMENTO FORTE | peggioramento | RIBASSISTA | +30.00% | +2.50 punti |

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
| BTC | 76.908 $ | 89.051 $ | +75,00% | +15,79% | buona zona storica di rimbalzo | 89.051 $ | 76.908 $ | +6,25% | -13,64% | spike storicamente più resistente |
| SOL | 98,49 $ | 114,04 $ | +58,06% | +15,79% | rimbalzo possibile | 114,04 $ | 98,49 $ | +12,90% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08260 $ | 0,09564 $ | +20,00% | +15,79% | rimbalzo poco frequente | 0,09564 $ | 0,08260 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 27 poi sono rimbalzati fino a +10,00%. Percentuale: +75,00% (27/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **BTC: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 2 poi sono scaricati a -5,00%. Percentuale: +6,25% (2/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 18 poi sono rimbalzati fino a +10,00%. Percentuale: +58,06% (18/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **SOL: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 4 poi sono scaricati a -5,00%. Percentuale: +12,90% (4/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +20,00% (6/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 11 poi sono scaricati a -5,00%. Percentuale: +50,00% (11/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-04 05:31:55 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-04 | 2026-09-04T05:30:23Z | 2026-09-04 05:30:23 |
| SOL | 2026-09-04 | 2026-09-04T05:30:23Z | 2026-09-04 05:30:23 |
| DOGE | 2026-09-04 | 2026-09-04T05:30:23Z | 2026-09-04 05:30:23 |

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
| BTC | 2026-09-04 | 80.956 $ | SALITA | 82,50% | 69.612,13 $ | 82.578,59 $ | 91.365,78 $ | 106.231,53 $ | 136.007,54 $ |
| SOL | 2026-09-04 | 103,67 $ | SALITA | 67,50% | 66,21 $ | 83,79 $ | 118,15 $ | 160,17 $ | 203,03 $ |
| DOGE | 2026-09-04 | 0.08695 $ | DISCESA | 30,00% | 0.06320 $ | 0.07040 $ | 0.07929 $ | 0.08850 $ | 0.10842 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_ASSET_REGIME | 2 | 5 | 5 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 91.365,78 $ | 105.225,41 $ | 136.007,54 $ | 236.620,96 $ |
| SOL | AVAILABLE | SAME_ASSET_REGIME | 2 | 5 | 5 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 118,15 $ | 109,72 $ | 203,03 $ | 303,01 $ |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 0 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.07929 $ | n/a | 0.10842 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-05**; verificato fino al **2026-09-04**; stato **COMPLETO 30/30g**.
- Reale **80.918,20 $**; p50 previsto **70.663,01 $**; scarto **14,51%**.
- Errore medio assoluto **8,25%**; massimo **17,06%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted BTC](scanner_forecast_BTC_regime_adjusted.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-05**; verificato fino al **2026-09-04**; stato **COMPLETO 30/30g**.
- Reale **103,57 $**; p50 previsto **80,36 $**; scarto **28,88%**.
- Errore medio assoluto **14,89%**; massimo **36,50%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-05**; verificato fino al **2026-09-04**; stato **COMPLETO 30/30g**.
- Reale **0.08685 $**; p50 previsto **0.07322 $**; scarto **18,62%**.
- Errore medio assoluto **15,78%**; massimo **43,59%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 53 | 92,45% | 62,26% | 2,20% | 0,68% |
| BTC | 3g | 49 | 89,80% | 71,43% | 3,38% | 1,03% |
| BTC | 7g | 44 | 90,91% | 72,73% | 5,43% | 2,51% |
| BTC | 14g | 37 | 97,30% | 64,86% | 6,56% | 3,96% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 53 | 77,36% | 56,60% | 2,97% | 1,14% |
| SOL | 3g | 49 | 87,76% | 69,39% | 4,17% | 1,91% |
| SOL | 7g | 44 | 86,36% | 68,18% | 5,92% | 4,22% |
| SOL | 14g | 37 | 81,08% | 64,86% | 8,61% | 7,61% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 53 | 84,91% | 56,60% | 3,43% | 0,83% |
| DOGE | 3g | 49 | 87,76% | 67,35% | 4,72% | 2,02% |
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
| BTC | 7g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **156**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-04 | BTC | 80.956 $ | SALITA | 82,50% | 91.366 $ | 70.883 $ | 98.028 $ | 2026-10-04 |
| 2026-09-04 | DOGE | 0,09000 $ | DISCESA | 30,00% | 0,08000 $ | 0,07000 $ | 0,10000 $ | 2026-10-04 |
| 2026-09-04 | SOL | 103,67 $ | SALITA | 67,50% | 118,15 $ | 91,80 $ | 135,57 $ | 2026-10-04 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-09-04 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +82,50%       | Casi positivi 82.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 82.50% >= 80%**
- Casi usati nei grafici: **33**
- Return mediano 7g: **-3,09%**
- Return mediano 14g: **-0,95%**
- Return mediano 30g: **+14,69%**
- Drawdown mediano: **-10,75%**
- Max gain mediano: **+25,52%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+1,67%**
- Spike massimo medio prima del minimo: **+5,55%**
- Spike p75 prima del minimo: **+4,48%**
- Giorno mediano dello spike: **giorno 2**
- Giorno mediano del minimo: **giorno 5**
- Scarico mediano dal picco al minimo: **-12,66%**
- Casi con almeno +5% prima del minimo: **+24,24%**
- Casi con almeno +10% prima del minimo: **+3,03%**
- Casi con almeno +15% prima del minimo: **+3,03%**
- Discesa quasi immediata: **+42,42%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +2,37% | +8,57% | +14,69% | +37,56% | +99,95% |

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
| UNI-USD         | 2023-07-10 | +82,93%      | +100,00%                 |             10 | -2,12%       |              14 | -51,06%          | +297,17%     | ECCEZIONE POSITIVA            |
| VET-USD         | 2020-06-11 | +80,72%      | +9,75%                   |              1 | -6,61%       |               9 | -14,90%          | +109,07%     | ECCEZIONE POSITIVA            |
| XLM-USD         | 2020-12-06 | +89,37%      | +8,98%                   |             10 | -27,99%      |              17 | -33,92%          | +10,93%      | SPIKE PRIMA DEL DUMP          |
| LTC-USD         | 2019-02-19 | +82,64%      | +8,19%                   |              1 | -6,66%       |               5 | -13,72%          | +24,05%      | ECCEZIONE POSITIVA            |
| THETA-USD       | 2019-02-19 | +85,43%      | +7,84%                   |              4 | -3,49%       |               5 | -10,50%          | +29,98%      | ECCEZIONE POSITIVA            |
| EGLD-USD        | 2023-11-16 | +84,61%      | +6,62%                   |              3 | -7,93%       |               5 | -13,65%          | +39,98%      | ECCEZIONE POSITIVA            |
| ADA-USD         | 2020-12-06 | +84,00%      | +5,49%                   |             10 | -14,15%      |              17 | -18,61%          | +62,60%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2023-11-08 | +84,00%      | +5,31%                   |              2 | -15,83%      |              13 | -20,08%          | +13,46%      | RIALZO MODESTO PRIMA DEL DUMP |
| BNB-USD         | 2023-11-16 | +83,08%      | +4,48%                   |              4 | -6,70%       |               5 | -10,70%          | +0,66%       | ECCEZIONE POSITIVA            |
| 1INCH-USD       | 2023-11-18 | +84,71%      | +4,43%                   |              1 | -7,24%       |               3 | -11,18%          | +2,85%       | ECCEZIONE POSITIVA            |
| DOGE-USD        | 2019-04-16 | +80,99%      | +3,92%                   |              2 | -13,02%      |              13 | -16,29%          | +11,75%      | RIALZO MODESTO PRIMA DEL DUMP |
| ADA-USD         | 2023-11-16 | +84,91%      | +3,43%                   |              3 | -3,53%       |               5 | -6,73%           | +63,44%      | ECCEZIONE POSITIVA            |
| AVAX-USD        | 2023-11-22 | +81,11%      | +2,55%                   |              3 | -2,11%       |               5 | -4,54%           | +118,51%     | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-16 | +84,43%      | +2,53%                   |              3 | -7,84%       |               5 | -10,11%          | +14,14%      | DISCESA QUASI IMMEDIATA       |
| XTZ-USD         | 2023-11-16 | +85,70%      | +2,51%                   |              3 | -8,26%       |               5 | -10,51%          | +12,21%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-16 | +88,31%      | +2,50%                   |              3 | -5,18%       |               5 | -7,50%           | +1,25%       | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-16 | +86,05%      | +1,67%                   |              3 | -5,91%       |               5 | -7,46%           | +7,43%       | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-15 | +86,09%      | +1,04%                   |              4 | -10,03%      |               6 | -10,95%          | +8,57%       | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2023-11-18 | +82,71%      | +0,95%                   |              1 | -10,75%      |               3 | -11,60%          | +2,26%       | DISCESA QUASI IMMEDIATA       |
| MATIC-USD       | 2023-11-16 | +83,94%      | +0,79%                   |              3 | -13,46%      |               5 | -14,14%          | +0,40%       | DISCESA QUASI IMMEDIATA       |

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
- Casi positivi / salita storica: **82,50%**
- Casi negativi / discesa storica: **17,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **80.955,88 $**
- Return normale fra 30 giorni: **91.365,78 $** (12,86%)
- Drawdown normale durante il mese: **70.883,01 $** (-12,44%)
- Drawdown brutto da rispettare: **68.708,78 $** (-15,13%)
- Max gain normale durante il mese: **98.028,34 $** (21,09%)
- Max gain buono / take profit ottimistico: **115.989,04 $** (43,27%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **103,67 $**
- Return normale fra 30 giorni: **118,15 $** (13,97%)
- Drawdown normale durante il mese: **91,80 $** (-11,45%)
- Drawdown brutto da rispettare: **77,67 $** (-25,08%)
- Max gain normale durante il mese: **135,57 $** (30,77%)
- Max gain buono / take profit ottimistico: **168,05 $** (62,10%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **30,00%**
- Casi negativi / discesa storica: **70,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,08 $** (-8,81%)
- Drawdown normale durante il mese: **0,07 $** (-15,14%)
- Drawdown brutto da rispettare: **0,06 $** (-26,63%)
- Max gain normale durante il mese: **0,10 $** (11,29%)
- Max gain buono / take profit ottimistico: **0,11 $** (27,60%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 80.955,88 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **82,50%**
- Probabilità storica di discesa: **17,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **69.612,13 $** (-14,01%)
- Se va male: **82.578,59 $** (2,00%)
- Scenario normale: **91.365,78 $** (12,86%)
- Se va bene: **106.231,53 $** (31,22%)
- Se va molto bene: **136.007,54 $** (68,00%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **70.883,01 $** (-12,44%)
- Discesa brutta: **68.708,78 $** (-15,13%)
- Discesa molto brutta: **57.873,96 $** (-28,51%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **98.028,34 $** (21,09%)
- Rialzo buono: **115.989,04 $** (43,27%)
- Rialzo molto forte: **165.450,28 $** (104,37%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **70.883,01 $** e uno spike normale intorno a **98.028,34 $**.

La chiusura a 30 giorni era più spesso positiva: salita 82,50%, discesa 17,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 103,67 $

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

- Se va molto male: **66,21 $** (-36,13%)
- Se va male: **83,79 $** (-19,17%)
- Scenario normale: **118,15 $** (13,97%)
- Se va bene: **160,17 $** (54,50%)
- Se va molto bene: **203,03 $** (95,84%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **91,80 $** (-11,45%)
- Discesa brutta: **77,67 $** (-25,08%)
- Discesa molto brutta: **64,00 $** (-38,27%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **135,57 $** (30,77%)
- Rialzo buono: **168,05 $** (62,10%)
- Rialzo molto forte: **234,80 $** (126,49%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **91,80 $** e uno spike normale intorno a **135,57 $**.

La chiusura a 30 giorni era più spesso positiva: salita 67,50%, discesa 32,50%. Quindi la lettura principale è favorevole.

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

- Se va molto male: **0,06 $** (-27,31%)
- Se va male: **0,07 $** (-19,04%)
- Scenario normale: **0,08 $** (-8,81%)
- Se va bene: **0,09 $** (1,79%)
- Se va molto bene: **0,11 $** (24,69%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-15,14%)
- Discesa brutta: **0,06 $** (-26,63%)
- Discesa molto brutta: **0,06 $** (-31,85%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (11,29%)
- Rialzo buono: **0,11 $** (27,60%)
- Rialzo molto forte: **0,13 $** (45,12%)

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

- Grezzo: **12,86%** → **91.365,78 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **14,87%** → **92.991,31 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-12,44%** → **70.883,01 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **-7,72%** → **74.706,82 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **21,09%** → **98.028,34 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **18,26%** → **95.741,40 $**
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

- Grezzo: **13,97%** → **118,15 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **22,77%** → **127,28 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-11,45%** → **91,80 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-8,46%** → **94,90 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **30,77%** → **135,57 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **34,78%** → **139,73 $**
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

- Grezzo: **-8,81%** → **0,08 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **6,37%** → **0,09 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-15,14%** → **0,07 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **0,20%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **11,29%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **13,81%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 80.955,88 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **82,50%**
- Casi negativi dopo 30 giorni: **17,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,72%**
- Rendimento medio dopo 30 giorni: **27,41%**
- Rendimento centrale dopo 30 giorni: **12,86%**
- Discesa media durante i 30 giorni: **-14,49%**
- Massimo rialzo medio durante i 30 giorni: **41,80%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **103.147,83 $**
- Scenario centrale a 30 giorni: **91.365,78 $**
- Zona di rischio media: **69.223,03 $**
- Zona di rialzo media: **114.793,39 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -14,01% → **69.612,13 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 2,00% → **82.578,59 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 12,86% → **91.365,78 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 31,22% → **106.231,53 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 68,00% → **136.007,54 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,51% → **57.873,96 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,13% → **68.708,78 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,44% → **70.883,01 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,11% → **75.200,91 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -5,01% → **76.896,20 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 6,92% → **86.555,98 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 12,30% → **90.912,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 21,09% → **98.028,34 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 43,27% → **115.989,04 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 104,37% → **165.450,28 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-08-29   | 2020-12-06 |        89.37 |        10.93 |         -27.99 |          10.93 |
| XRP-USD         | 2023-08-09   | 2023-11-16 |        88.31 |         1.25 |          -5.18 |           9.96 |
| BNB-USD         | 2018-11-13   | 2019-02-20 |        88.21 |        39.22 |         -13.17 |          46.99 |
| THETA-USD       | 2023-08-08   | 2023-11-15 |        86.09 |         8.57 |         -10.03 |          20.88 |
| ETC-USD         | 2023-08-09   | 2023-11-16 |        86.05 |         7.43 |          -5.91 |          15.36 |
| LRC-USD         | 2019-11-13   | 2020-02-20 |        85.84 |       -24.87 |         -34.37 |          27.42 |
| XTZ-USD         | 2023-08-09   | 2023-11-16 |        85.7  |        12.21 |          -8.26 |          16.47 |
| THETA-USD       | 2018-11-12   | 2019-02-19 |        85.43 |        29.98 |          -3.49 |         102.52 |
| ADA-USD         | 2023-08-09   | 2023-11-16 |        84.91 |        63.44 |          -3.53 |          78.94 |
| 1INCH-USD       | 2023-08-11   | 2023-11-18 |        84.71 |         2.85 |          -7.24 |          17.19 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 103,67 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **67,50%**
- Casi negativi dopo 30 giorni: **32,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **81,84%**
- Rendimento medio dopo 30 giorni: **27,46%**
- Rendimento centrale dopo 30 giorni: **13,97%**
- Discesa media durante i 30 giorni: **-17,02%**
- Massimo rialzo medio durante i 30 giorni: **51,25%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **132,13 $**
- Scenario centrale a 30 giorni: **118,15 $**
- Zona di rischio media: **86,02 $**
- Zona di rialzo media: **156,80 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -36,13% → **66,21 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -19,17% → **83,79 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 13,97% → **118,15 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 54,50% → **160,17 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 95,84% → **203,03 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -38,27% → **64,00 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -25,08% → **77,67 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,45% → **91,80 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,70% → **97,76 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **103,67 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,25% → **103,93 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,98% → **115,05 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 30,77% → **135,57 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 62,10% → **168,05 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 126,49% → **234,80 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZIL-USD         | 2020-08-26   | 2020-12-03 |        85.73 |       116.9  |         -11.64 |         166.95 |
| NEO-USD         | 2023-08-09   | 2023-11-16 |        85.04 |        14.38 |         -11.27 |          14.38 |
| ADA-USD         | 2020-08-29   | 2020-12-06 |        84.65 |        62.6  |         -14.15 |          62.6  |
| VET-USD         | 2020-03-04   | 2020-06-11 |        84.63 |       109.07 |          -6.61 |         125.67 |
| VET-USD         | 2023-08-11   | 2023-11-18 |        84.28 |        52.02 |          -7.84 |          52.02 |
| 1INCH-USD       | 2023-08-11   | 2023-11-18 |        83.93 |         2.85 |          -7.24 |          17.19 |
| XRP-USD         | 2020-08-29   | 2020-12-06 |        83.88 |       -63.42 |         -65.83 |           0    |
| ENJ-USD         | 2020-10-23   | 2021-01-30 |        83.86 |       111.8  |           0    |         111.8  |
| RUNE-USD        | 2026-01-31   | 2026-05-10 |        83.53 |       -36.07 |         -47.56 |           2.93 |
| MANA-USD        | 2019-11-13   | 2020-02-20 |        83.32 |       -54.5  |         -65.63 |           6.49 |

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

- Somiglianza media dei pattern: **81,13%**
- Rendimento medio dopo 30 giorni: **-2,35%**
- Rendimento centrale dopo 30 giorni: **-8,81%**
- Discesa media durante i 30 giorni: **-16,01%**
- Massimo rialzo medio durante i 30 giorni: **22,61%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -27,31% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -19,04% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -8,81% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 1,79% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 24,69% → **0,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -31,85% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -26,63% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -15,14% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,04% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,73% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,71% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,29% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 27,60% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 45,12% → **0,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| FIL-USD         | 2022-05-05   | 2022-08-12 |        86.64 |       -26.85 |         -35.95 |           0    |
| MANA-USD        | 2025-01-25   | 2025-05-04 |        84.58 |        -2.82 |          -6.91 |          32.03 |
| INJ-USD         | 2021-05-13   | 2021-08-20 |        84.48 |         1.61 |          -0.81 |          44.17 |
| MATIC-USD       | 2022-04-21   | 2022-07-29 |        83.61 |       -16.46 |         -18.64 |           9.17 |
| SOL-USD         | 2021-12-30   | 2022-04-08 |        82.91 |       -31.49 |         -31.49 |           2.89 |
| BTC-USD         | 2025-01-29   | 2025-05-08 |        82.73 |         2.3  |          -1.61 |           8.17 |
| YFI-USD         | 2022-05-05   | 2022-08-12 |        82.58 |       -11.73 |         -26.53 |           0    |
| QTUM-USD        | 2022-05-01   | 2022-08-08 |        82.5  |       -25.68 |         -28.31 |           2.87 |
| BAT-USD         | 2021-05-11   | 2021-08-18 |        82.28 |         4.22 |           0    |          36.57 |
| SAND-USD        | 2021-04-15   | 2021-07-23 |        82.08 |         0.7  |         -10.85 |          15.26 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-04 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-04 | RECOVERY | 80.956 $ | True | 33.00% | -6.75% | RECOVERY | 33.00% | -6.75% |
| DOGE-USD | 2026-09-04 | RECOVERY | 0.08695 $ | False | 6.23% | -13.76% | RECOVERY | 33.00% | -6.75% |
| SOL-USD | 2026-09-04 | RECOVERY | 103,67 $ | True | 66.70% | -11.82% | RECOVERY | 33.00% | -6.75% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 82.50% | 12.86% | 31.22% | 68.00% | -12.44% | -28.51% | 21.09% | 43.27% | 104.37% | 80.00% | 11.34% | 42.45% | 116.01% |
| BTC-USD | SAME_BTC_REGIME | 5 | 100.00% | 34.95% | 39.22% | 81.13% | -6.66% | -17.66% | 46.99% | 102.52% | 116.41% | 100.00% | 71.29% | 120.62% | 133.43% |
| BTC-USD | SAME_ASSET_REGIME | 5 | 80.00% | 29.98% | 34.95% | 192.28% | -14.77% | -18.35% | 34.95% | 102.52% | 229.70% | 80.00% | 8.85% | 34.79% | 56.69% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 32.46% | 33.71% | 34.45% | -12.07% | -18.94% | 68.74% | 85.63% | 95.77% | 100.00% | 53.04% | 62.16% | 67.64% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -8.81% | 1.79% | 24.69% | -15.14% | -31.85% | 11.29% | 27.60% | 45.12% | 32.50% | -10.41% | 9.07% | 44.19% |
| DOGE-USD | SAME_BTC_REGIME | 2 | 0.00% | -25.91% | -21.18% | -18.35% | -27.18% | -34.00% | 4.59% | 6.88% | 8.26% | 0.00% | -37.99% | -29.56% | -24.50% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 13.97% | 54.50% | 95.84% | -11.45% | -38.27% | 30.77% | 62.10% | 126.49% | 70.00% | 29.88% | 80.39% | 186.10% |
| SOL-USD | SAME_BTC_REGIME | 5 | 80.00% | 39.22% | 67.31% | 92.37% | -13.17% | -20.05% | 46.99% | 98.59% | 114.83% | 100.00% | 120.62% | 141.97% | 233.11% |
| SOL-USD | SAME_ASSET_REGIME | 5 | 80.00% | 5.84% | 34.95% | 192.28% | -14.77% | -20.05% | 34.95% | 39.59% | 204.53% | 80.00% | 32.97% | 57.82% | 65.90% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 9.15% | 22.05% | 29.79% | -19.90% | -20.50% | 17.47% | 26.21% | 31.45% | 100.00% | 52.13% | 61.71% | 67.46% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 4 | 50.00% | -6.56% | -29.44% | 26.79% | 50.00% | -5.56% | 31.23% |
| BTC-USD | HISTORICAL_BTC_BULL | 31 | 83.87% | 12.21% | -11.27% | 35.63% | 80.65% | 10.68% | 68.31% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 100.00% | 34.95% | -6.66% | 102.52% | 100.00% | 71.29% | 128.04% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 11 | 9.09% | -11.73% | -22.77% | 10.88% | 18.18% | -32.52% | 16.43% |
| DOGE-USD | HISTORICAL_BTC_BULL | 25 | 44.00% | -1.61% | -8.92% | 36.34% | 44.00% | -3.99% | 47.42% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -21.02% | -29.71% | 11.71% | 0.00% | -7.24% | 11.71% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -25.91% | -27.18% | 6.88% | 0.00% | -37.99% | 6.88% |
| SOL-USD | HISTORICAL_BTC_BEAR | 10 | 50.00% | 10.52% | -16.85% | 51.43% | 60.00% | 26.83% | 68.87% |
| SOL-USD | HISTORICAL_BTC_BULL | 18 | 94.44% | 39.89% | -9.81% | 98.33% | 88.89% | 34.55% | 175.12% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 7 | 14.29% | -22.39% | -24.88% | 28.26% | 14.29% | -22.09% | 28.26% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 5 | 80.00% | 39.22% | -13.17% | 98.59% | 100.00% | 120.62% | 146.42% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 28 | 82.14% | 12.23% | -11.76% | 29.21% | 82.14% | 11.04% | 48.88% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 12.19% | -14.99% | 50.31% | 66.67% | 100.34% | 172.07% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 109.07% | -6.61% | 125.67% | 100.00% | 141.97% | 146.42% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 80.00% | 29.98% | -14.77% | 102.52% | 80.00% | 8.85% | 102.52% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 16 | 12.50% | -13.96% | -20.71% | 11.13% | 18.75% | -32.34% | 17.17% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 23 | 39.13% | -2.82% | -8.92% | 36.46% | 39.13% | -3.99% | 43.41% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 125.28% | 0.00% | 128.29% | 100.00% | 81.09% | 149.46% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 60.71% | 11.06% | -10.65% | 52.14% | 64.29% | 22.32% | 75.76% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 62.60% | -14.15% | 133.93% | 80.00% | 85.18% | 166.95% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 88.19% | -3.30% | 118.90% | 100.00% | 217.92% | 257.00% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 80.00% | 5.84% | -14.77% | 39.59% | 80.00% | 32.97% | 71.29% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_ASSET_REGIME | 2 | 5 | 5 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| DOGE-USD | NONE | 0 | 0 | 2 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_ASSET_REGIME | 2 | 5 | 5 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | THETA-USD | 2018-11-12 | 85.43% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.98% | -3.49% | 102.52% | 34.79% | -3.49% | 102.52% |
| BTC-USD | WAVES-USD | 2023-08-09 | 83.14% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.17% | -14.77% | 11.00% | 8.47% | -14.77% | 32.90% |
| BTC-USD | UNI-USD | 2023-04-02 | 82.93% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 297.17% | -2.12% | 314.49% | -44.88% | -54.06% | 314.49% |
| BTC-USD | LRC-USD | 2020-03-07 | 82.21% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 34.95% | -20.65% | 34.95% | 71.29% | -20.65% | 71.29% |
| BTC-USD | DASH-USD | 2020-08-29 | 82.09% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.81% | -14.89% | 7.15% | 8.85% | -14.89% | 45.20% |
| SOL-USD | WAVES-USD | 2023-08-09 | 82.45% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.17% | -14.77% | 11.00% | 8.47% | -14.77% | 32.90% |
| SOL-USD | LRC-USD | 2020-03-07 | 81.91% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 34.95% | -20.65% | 34.95% | 71.29% | -20.65% | 71.29% |
| SOL-USD | XRP-USD | 2024-08-23 | 79.77% | DISTRIBUTION | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 5.84% | 0.00% | 39.59% | 57.82% | 0.00% | 69.67% |
| SOL-USD | MKR-USD | 2020-03-08 | 79.74% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -16.66% | -19.15% | 0.00% | 32.97% | -19.26% | 45.21% |
| SOL-USD | UNI-USD | 2023-04-02 | 79.60% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 297.17% | -2.12% | 314.49% | -44.88% | -54.06% | 314.49% |

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

Generato: 2026-09-04 05:32 UTC


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
| BTC | 80.956 $ | +5 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 103,67 $ | +7 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.08695 $ | +1 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | +2 | -3 | +3 | 0 | 0 | +2 | +5 |
| SOL | +1 | +2 | 0 | +2 | 0 | 0 | +2 | +7 |
| DOGE | -2 | +2 | -1 | +2 | 0 | 0 | 0 | +1 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 81.347 $ | 81.347 $ | 57.748 $ | 3,49% | 26,35% | 32,85% |
| SOL | 83,52 $ | 110,04 $ | 110,04 $ | 70,69 $ | 5,79% | 40,55% | 63,20% |
| DOGE | 0.08189 $ | 0.09169 $ | 0.09998 $ | 0.06797 $ | 6,35% | 24,00% | 6,75% |

## Lettura dettagliata

### BTC

- Prezzo: **80.956 $**
- Score classico: **+5 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **MEDIO** — ATR14 3,49%; distanza supporto 2,18%; distanza resistenza 0,51%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-3** — RSI alto 72.5; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.25; rialzo con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 72.49 |
| MACD histogram | -6.83407 |
| CMF20 | 0.250 |
| Volume ratio 20 | 1.23 |
| MA20 | 74.762 $ |
| MA50 | 68.452 $ |
| MA100 | 66.282 $ |
| MA200 | 69.567 $ |
| Pendenza MA50 20g | +7,88% |
| Pendenza MA200 60g | -6,89% |
| Bollinger width | 30,51% |
| Bollinger position | 0.75 |

### SOL

- Prezzo: **103,67 $**
- Score classico: **+7 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,79%; distanza supporto 24,06%; distanza resistenza 6,21%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 67.2; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.21; volume ratio 0.97
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 67.18 |
| MACD histogram | 0.03543 |
| CMF20 | 0.208 |
| Volume ratio 20 | 0.97 |
| MA20 | 94,20 $ |
| MA50 | 82,67 $ |
| MA100 | 78,27 $ |
| MA200 | 82,14 $ |
| Pendenza MA50 20g | +8,92% |
| Pendenza MA200 60g | -12,00% |
| Bollinger width | 42,80% |
| Bollinger position | 0.71 |

### DOGE

- Prezzo: **0.08695 $**
- Score classico: **+1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 6,35%; distanza supporto 6,06%; distanza resistenza 5,58%

Dettaglio:

- Trend: **-2** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-1** — RSI sano 60.9; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF neutrale 0.02; rialzo con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 60.89 |
| MACD histogram | -0.00053 |
| CMF20 | 0.017 |
| Volume ratio 20 | 1.24 |
| MA20 | 0.08250 $ |
| MA50 | 0.07545 $ |
| MA100 | 0.07887 $ |
| MA200 | 0.08860 $ |
| Pendenza MA50 20g | +4,61% |
| Pendenza MA200 60g | -13,95% |
| Bollinger width | 36,01% |
| Bollinger position | 0.64 |

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

Generato: 2026-09-04 05:32 UTC


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
| BTC | 80.956 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 40,19% | Fib 23,6% TENUTO (0) @ 75.778 $ | NEL RANGE | 74.959 $ |
| SOL | 103,67 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 46,65% | Fib 23,6% TENUTO (0) @ 98,33 $ | NEL RANGE | 83,52 $ |
| DOGE | 0.08695 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 27,92% | Fib 38,2% TESTATO (0) @ 0.08775 $ | NEL RANGE | 0.08157 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **26 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **40,19%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (0) @ 75.778 $** — Swing UP 2026-07-01 57.748 -> 2026-08-28 81.347; livello più vicino 23.6% a 75.778; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **74.959 $**
- Resistenza: **81.347 $**
- Breakout 60g: **81.347 $**
- Breakdown 60g: **57.748 $**
- RSI14: **72.52**
- ATR14: **3,49%**
- Volume ratio 20g: **1.23**
- Rendimento 30g: **+26,38%**
- Rendimento 90g: **+32,88%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 32.703 $ | n/a | 40,19% | 58.903 $ | Due massimi simili a 82.792 $ e 81.347 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 65.402 $ | 2026-08-19 | 16g | 68.577 $ | 489,88% | n/a | 64.094 $ | Due minimi simili a 62.227 $ e 62.488 $. Neckline circa 65.402 $. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577 $; progresso: 489,88%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **26 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **46,65%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (0) @ 98,33 $** — Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **83,52 $**
- Resistenza: **110,04 $**
- Breakout 60g: **110,04 $**
- Breakdown 60g: **70,69 $**
- RSI14: **67.23**
- ATR14: **5,78%**
- Volume ratio 20g: **0.97**
- Rendimento 30g: **+40,63%**
- Rendimento 90g: **+63,29%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 46,65% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 26 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 16g | 85,65 $ | 341,01% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 341,01%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 16g | 84,05 $ | 468,50% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 468,50%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **24 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **27,92%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TESTATO (0) @ 0.08775 $** — Swing UP 2026-08-01 0.06797 -> 2026-08-22 0.09998; livello più vicino 38.2% a 0.08775; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08157 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **61.02**
- ATR14: **6,34%**
- Volume ratio 20g: **1.24**
- Rendimento 30g: **+24,14%**
- Rendimento 90g: **+6,87%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 27,92% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 24 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 15g | 0.08952 $ | 75,04% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (15 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 75,04%; prezzo sopra neckline. |

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

Generato: 2026-09-04 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-04**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-19**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **103,67 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+66,88%**
- Aderenza live principale: **+71,40%**
- Errore medio live principale: **14,30%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **90**
- Osservazioni inclusive dal bottom: **91**
- Osservazioni da inizio programma/scanner: **64**
- Errore assoluto medio dal bottom: **11,85%**
- Errore assoluto medio da inizio programma: **14,30%**
- Gap firmato medio ultimi 7 giorni: **+9,96%**
- Errore assoluto medio ultimi 7 giorni: **9,96%**
- Gap ultimo giorno: **+8,18%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+8,18%**
- Gap firmato medio 7g: **+9,96%**
- Errore assoluto medio 7g: **9,96%**
- Variazione recente gap: **+0,73%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 100,39 $ | 97,07 $ | +3,42% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 103,67 $ | 95,83 $ | +8,18% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-11 | 92,81 $ | 100,40 $ | 98,76 $ / 105,81 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-18 | 88,38 $ | 95,61 $ | 95,26 $ / 105,81 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-25 | 87,31 $ | 94,45 $ | 86,03 $ / 105,81 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-02 | 110,45 $ | 119,48 $ | 86,03 $ / 119,48 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-09 | 110,28 $ | 119,30 $ | 86,03 $ / 120,74 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-16 | 111,08 $ | 120,17 $ | 86,03 $ / 121,36 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-23 | 111,61 $ | 120,74 $ | 86,03 $ / 121,36 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-30 | 119,42 $ | 129,19 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-06 | 108,69 $ | 117,58 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-13 | 115,30 $ | 124,73 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-20 | 112,09 $ | 121,26 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-27 | 106,09 $ | 114,76 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-04 | 105,39 $ | 114,01 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-11 | 110,64 $ | 119,68 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-18 | 106,83 $ | 115,57 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-25 | 102,18 $ | 110,54 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-01 | 103,74 $ | 112,23 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-08 | 120,07 $ | 129,89 $ | 86,03 $ / 130,81 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 50 | 34,00% | 11,48% | 13,19% |
| 14g | 43 | 25,58% | 19,71% | 11,90% |
| 21g | 36 | 16,67% | 27,01% | 13,96% |
| 28g | 31 | 35,48% | 25,08% | 13,35% |
| 35g | 24 | 54,17% | 15,75% | 12,42% |
| 42g | 17 | 100,00% | 8,48% | 11,43% |
| 49g | 10 | 100,00% | 6,85% | 11,38% |
| 56g | 3 | 100,00% | 10,64% | 8,18% |
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

Ultima lettura salvata: **2026-09-04** — SOL 103,67 $, gap +8,18%, somiglianza +66,88%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-04 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 81.008 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0051% | -0,98% | 7,19 | +1,02% | 0 $ | 0 $ |
| SOL | 103,81 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0057% | -0,92% | 2,53 | -8,75% | 0 $ | 0 $ |
| DOGE | 0.08717 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0099% | -1,57% | 0,99 | +7,73% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | -0,0001% | 160,34 mln $ | 0,14 | +12,93% |
| BTC | Bitget | OK | +0,0100% | 2,65 mld $ | 5,61 | -36,46% |
| BTC | Kucoin | OK | +0,0060% | 1,36 mld $ | 1,07 | -0,60% |
| SOL | Kraken | OK | -0,0056% | 29,32 mln $ | 1,35 | -18,01% |
| SOL | Bitget | OK | +0,0069% | 452,85 mln $ | 7,60 | -66,92% |
| SOL | Kucoin | OK | -0,0009% | 238,13 mln $ | 0,54 | -16,14% |
| DOGE | Kraken | OK | -0,0012% | 4,58 mln $ | 2,11 | -15,46% |
| DOGE | Bitget | OK | +0,0100% | 112,16 mln $ | 13,60 | +0,47% |
| DOGE | Kucoin | OK | +0,0100% | 92,22 mln $ | 2,51 | -7,88% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,50**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +66,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 7, accuratezza +42,86%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+0,75**.
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
| BTC | +82,50% | +12,86% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +82,50% | +12,86% |
| SOL | +67,50% | +13,97% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +67,50% | +13,97% |
| DOGE | +30,00% | -8,81% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +30,00% | -8,81% |

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

Generato: 2026-09-04 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-04 | BTC | 81.007,60 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 7,19 | -0,98% | +1,02% |
| 2026-09-04 | DOGE | 0.08717 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,99 | -1,57% | +7,73% |
| 2026-09-04 | SOL | 103,81 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 2,53 | -0,92% | -8,75% |
| 2026-09-03 | BTC | 77.700,30 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,07 | -3,94% | -0,43% |
| 2026-09-03 | DOGE | 0.08290 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,99 | -0,31% | +1,69% |
| 2026-09-03 | SOL | 100,71 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 2,05 | +1,41% | +10,07% |
| 2026-09-02 | BTC | 77.400,00 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,94 | +2,54% | -1,43% |
| 2026-09-02 | DOGE | 0.08150 | V2.1.3 | OK | 0 | 0 | 1,50 | BASSA | 1,07 | -4,77% | -1,60% |
| 2026-09-02 | SOL | 99,75 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -2,41% | +3,33% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 3 | +66,67% | +0,12% | -0,41% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 3 | +66,67% | +1,27% | -1,97% | +3,06% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | +66,67% | +0,53% | -2,29% | +3,66% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 3 | +66,67% | +10,89% | -4,64% | +16,94% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 8 | +50,00% | +0,90% | -0,21% | +1,91% | FEEDBACK RAPIDO |
| DOGE | 3g | 8 | +37,50% | +1,43% | -3,31% | +6,31% | FEEDBACK RAPIDO |
| DOGE | 7g | 7 | +42,86% | -1,02% | -4,29% | +8,47% | FEEDBACK RAPIDO |
| DOGE | 14g | 5 | +60,00% | +4,09% | -1,22% | +20,18% | FEEDBACK RAPIDO |
| DOGE | 30g | 2 | +100,00% | +31,38% | -1,97% | +40,03% | FEEDBACK RAPIDO |

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
| BTC | 80.956 $ | +0.0053% | -18.66% | 1.30 | Misto | 1/5 |
| SOL | 103,67 $ | -0.0031% | -30.64% | 2.62 | Misto | 1/5 |
| DOGE | 0.08695 $ | +0.0100% | -13.21% | 5.07 | Rischio sotto | 2/5 |

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

Generato: 2026-09-04 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D    | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-----------------------------------------------------|:-----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish                                       | CONFERMATA | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Momentum in indebolimento, divergenza non confermata | CONTESTO   | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| DOGE    | Momentum in indebolimento, divergenza non confermata | CONTESTO   | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish                                       | CONFERMATA | 80.940 $ / 72,49  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista                                   | CONTESTO   | 80.940 $ / 59,53  | n/a                                                                 | +23,87%             | 18,88            |      0 |
| SOL     | 1D   | Momentum in indebolimento, divergenza non confermata | CONTESTO   | 103,62 $ / 67,19  | n/a                                                                 | +18,24%             | -10,61           |      0 |
| SOL     | 1W   | Hidden bearish                                       | CONFERMATA | 103,62 $ / 58,86  | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Momentum in indebolimento, divergenza non confermata | CONTESTO   | 0.08692 $ / 60,98 | n/a                                                                 | +8,08%              | -12,72           |      0 |
| DOGE    | 1W   | Hidden bearish                                       | CONFERMATA | 0.08692 $ / 46,82 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish / CONFERMATA**: Hidden bullish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Momentum in indebolimento, divergenza non confermata / CONTESTO**: Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Momentum in indebolimento, divergenza non confermata / CONTESTO**: Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
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

Generato: 2026-09-04 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend           | Momentum       | Struttura                                          |   Pattern score | Fibonacci   | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:----------------|:---------------|:---------------------------------------------------|----------------:|:------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 80.956 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 81.347 |
| SOL | 103,67 $ | 9 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 110,04 |
| DOGE | 0.08695 $ | 5 | COSTRUTTIVO MA NON CONFERMATO | Trend misto | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TESTATO | Triplo minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.09998 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 72.52 | -5.5652 | 74.763 | 68.452 | 69.567 | 7,78% | -6,75% | 25,32% | 33,00% |
| SOL | 67.23 | 0.03926 | 94,20 | 82,67 | 82,14 | 8,82% | -11,82% | 40,17% | 66,70% |
| DOGE | 61.02 | -0.00052 | 0.08251 | 0.07545 | 0.08860 | 4,79% | -13,76% | 24,25% | 6,23% |

## Dettaglio asset

### BTC

- Prezzo: **80.956 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 6.223e+04 -> 6.249e+04. Ultimi massimi: 6.54e+04 -> 8.135e+04.
- Divergenza: **Divergenza rialzista nascosta RSI** (1)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-08-28 81.347; livello più vicino 23.6% a 75.778; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.488**
- Resistenza più vicina: **81.347**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 298,28%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (16g); progresso 298,28%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 298,28%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (16g); progresso 298,28%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 168,42%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (16g); progresso 168,42%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 40,19%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 40,19%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 45 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 40,19%; prezzo sopra neckline.

### SOL

- Prezzo: **103,67 $**
- Punteggio tecnico: **9 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 70.69 -> 74.2. Ultimi massimi: 77.62 -> 110.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,20**
- Resistenza più vicina: **110,04**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 468,50%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (16g); progresso 468,50%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 310,57%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (16g); progresso 310,57%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 124,99%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (16g); progresso 124,99%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 46,65%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 46,65%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-22 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 60,93%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08695 $**
- Punteggio tecnico: **5 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07286 -> 0.09998.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 37,74%. Fase non abbastanza chiara.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-08-01 0.06797 -> 2026-08-22 0.09998; livello più vicino 38.2% a 0.08775; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Triplo minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.09998**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 238,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (16g); progresso 238,54%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-20 (15 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.09012; progresso corrente: 70,89%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-20 (15g); progresso 70,89%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 238,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (16g); progresso 238,54%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 27,92%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 27,92%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 27,92%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                       | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato   | Confluenza                      |   Score |
|:--------|:----------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:--------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-08-28 | 75.778 | 72.332 | 69.547 | 66.763 | 62.798 | 23.6% / 75.778 | TENUTO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-08-27 | 98,33 | 91,08 | 85,23 | 79,37 | 71,03 | 23.6% / 98,33 | TENUTO | nessuna confluenza indipendente | 0 |
| DOGE | UP 2026-08-01 -> 2026-08-22 | 0.09243 | 0.08775 | 0.08398 | 0.08020 | 0.07482 | 38.2% / 0.08775 | TESTATO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 30/30 previsioni controllate su 62 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 62 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 62 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 62 | 30 | 30/30 [██████████] | 32 | ATTIVA | 2026-09-05 / tra 1 giorno |
| SOL | 62 | 30 | 30/30 [██████████] | 32 | ATTIVA | 2026-09-05 / tra 1 giorno |
| DOGE | 62 | 30 | 30/30 [██████████] | 32 | ATTIVA | 2026-09-05 / tra 1 giorno |

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

Generato: 2026-09-04 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 80.956 $          | 80.956 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08695 $         | 0.08695 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 80.956 $          | 80.956 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08695 $         | 0.08695 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 80.956 $          | 80.956 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08695 $         | 0.08695 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 80.956 $          | 80.956 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08695 $         | 0.08695 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 80.956 $          | 80.956 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08695 $         | 0.08695 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 80.956 $          | 81.008 $        | +0,0639%     |
| Exchange Microstructure | SOL     | price             | OK      | 103,67 $          | 103,81 $        | +0,1370%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.08695 $         | 0.08717 $       | +0,2530%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 103,67 $          | 103,67 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 103,67 $          | 103,67 $        | +0,0000%     |

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

Generato: 2026-09-05T00:30:35+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €44.216,18 | €10.939,69 | 326.707747 | 101.8540 | +10.54% | €3.453,09 | €107,96 | 6.48% | 61 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 95.4969 · L1 98.3506 · media 101.9177 · U1 105.4848 · U2 108.3385.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
